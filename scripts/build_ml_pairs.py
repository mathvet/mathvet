#!/usr/bin/env python3
"""Build ml/autoformalization_pairs.jsonl (+ ml/stats.json): one record per Comparator challenge,
pairing the Lean challenge statement with natural-language context (paper main theorems, abstracts,
overview summary, lean/docs scope) and the family-level fidelity label from verification/.

Usage:  python scripts/build_ml_pairs.py [--upstream DIR] [--cones FILE] [--out DIR]
Inputs (all read-only): <upstream>/lean/{ComparatorChallenges,docs}, <upstream>/preprints/*/build/*.tex,
index.json, verification/lean_scope_audit_part{1,2,3}.json, import_cones.json (scripts/import_cones.py output).
"""
import argparse, bisect, datetime, hashlib, json, math, os, re, subprocess, sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# ----------------------------------------------------------------------------- TeX helpers
def read_text(path):
    b = Path(path).read_bytes()
    try:
        return b.decode('utf-8')
    except UnicodeDecodeError:
        return b.decode('latin-1')

def strip_comments(s):
    """Remove unescaped % ... end-of-line comments; keeps line structure. Returns list of lines."""
    out = []
    for line in s.split('\n'):
        i, n, cut = 0, len(line), None
        while i < n:
            c = line[i]
            if c == '\\':
                i += 2
                continue
            if c == '%':
                cut = i
                break
            i += 1
        out.append(line if cut is None else line[:cut])
    return out

INPUT_RE = re.compile(r'\\(?:input|include|subfile)\s*\{([^}]+)\}')

def _resolve(target, cur_dir, base):
    target = target.strip()
    for d in (cur_dir, base):
        for cand in (d / target, d / (target + '.tex')):
            if cand.is_file():
                return cand.resolve()
    return None

def flatten(path, base, depth=0, seen=frozenset()):
    """Inline \\input/\\include recursively. Returns list of (relfile, lineno, text) 'lines'."""
    path = Path(path).resolve()
    rel = os.path.relpath(path, base.parent) if base.parent in path.parents else path.name
    out = []
    for i, line in enumerate(strip_comments(read_text(path)), 1):
        pos = 0
        for m in INPUT_RE.finditer(line):
            pre = line[pos:m.start()]
            if pre.strip():
                out.append((rel, i, pre))
            tgt = _resolve(m.group(1), path.parent, base)
            if tgt is not None and depth < 8 and tgt not in seen:
                out.extend(flatten(tgt, base, depth + 1, seen | {path}))
            pos = m.end()
        out.append((rel, i, line[pos:]))
    return out

def find_roots(pdir):
    """Root TeX files of a paper dir, best first: files containing \\begin{document} (prefer main.tex / paper.tex,
    then shallowest, then largest); falls back to files with \\documentclass."""
    build = Path(pdir) / 'build'
    cands = []
    for t in build.rglob('*.tex'):
        s = '\n'.join(strip_comments(read_text(t)))
        if BEGIN_DOC in s:
            pri = 0 if t.name in ('main.tex', 'paper.tex') else 1
            cands.append((pri, len(t.relative_to(build).parts), -len(s), str(t)))
    if not cands:
        for t in build.rglob('*.tex'):
            if '\\documentclass' in read_text(t):
                cands.append((2, len(t.relative_to(build).parts), 0, str(t)))
    return [Path(c[3]) for c in sorted(cands)]

def read_braced(s, i, open_c='{', close_c='}'):
    """s[i] == open_c: return (content, index after matching close) or (None, i)."""
    depth, j, n = 0, i, len(s)
    while j < n:
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == open_c:
            depth += 1
        elif c == close_c:
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return None, i

SEC_RE = re.compile(r'\\(section|subsection|subsubsection)\*?\s*(?:\[[^\]\n]*\])?\s*\{')
LABEL_RE = re.compile(r'\\label(?:\[[^\]]*\])?\{([^}]*)\}')
BEGIN_DOC = '\\begin{document}'

def norm_ws(s):
    return re.sub(r'\s+', ' ', s).strip()

def parse_sections(txt):
    """List of (pos, level, title) for \\section/\\subsection/\\subsubsection in document order."""
    out = []
    for m in SEC_RE.finditer(txt):
        title, _ = read_braced(txt, m.end() - 1)
        if title is None:
            continue
        out.append((m.start(), {'section': 1, 'subsection': 2, 'subsubsection': 3}[m.group(1)], norm_ws(title)))
    return out

# theorem-like environments we treat as "theorem statements"
THEOREM_ENVS = ['theorem', 'thm', 'maintheorem', 'mainthm', 'main-theorem', 'mainresult', 'Theorem', 'MainTheorem']
FALLBACK_ENVS = ['proposition', 'corollary', 'claim', 'conjecture', 'lemma']   # only if a paper has no theorem env

def discover_theorem_envs(txt):
    """Env names declared via \\newtheorem whose printed name starts with 'Theorem' / 'Main Theorem' (besides the defaults)."""
    extra = set()
    for m in re.finditer(r'\\newtheorem\*?\s*\{([^}]*)\}\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}', txt):
        env, name = m.group(1), m.group(2).strip()
        if re.match(r'(main\s+)?theorem\b', name, re.I) and env not in THEOREM_ENVS:
            extra.add(env)
    return extra

MAIN_LABEL_RE = re.compile(r'(^|[:_.\-])(main|mainthm|maintheorem|mainresult|main-?theorem|headline|principal)([:_.\-0-9]|$)', re.I)
MAIN_TITLE_RE = re.compile(r'^\s*(main\s+(theorem|result)|theorem\s+[A-Z]\b|principal\s+(theorem|result)|headline)', re.I)

def find_blocks(txt, envs, secs):
    """All \\begin{env}...\\end{env} blocks for env in envs, with optional title, label, enclosing sections."""
    blocks = []
    sec_pos = [s[0] for s in secs]
    for env in envs:
        for m in re.finditer(r'\\begin\{%s(\*?)\}' % re.escape(env), txt):
            end_m = re.compile(r'\\end\{%s%s\}' % (re.escape(env), re.escape(m.group(1)))).search(txt, m.end())
            if not end_m:
                continue
            title = None
            j = m.end()
            while j < len(txt) and txt[j] in ' \t\n':
                j += 1
            if j < len(txt) and txt[j] == '[':
                t, k = read_braced(txt, j, '[', ']')
                if t is not None and k <= end_m.start():
                    title = norm_ws(t)
            block = txt[m.start():end_m.end()]
            lm = LABEL_RE.search(block)
            # enclosing \section (level 1) and the last \subsection after it
            k = bisect.bisect_right(sec_pos, m.start()) - 1
            sec_idx, sec, sub = -1, None, None
            kk = k
            while kk >= 0:
                if secs[kk][1] == 2 and sub is None:
                    sub = secs[kk][2]
                if secs[kk][1] == 1:
                    sec_idx, sec = kk, secs[kk][2]
                    break
                kk -= 1
            blocks.append(dict(env=env + m.group(1), pos=m.start(), end=end_m.end(), title=title,
                               label=lm.group(1) if lm else None, section=sec, subsection=sub,
                               section_idx=sec_idx, tex=block))
    blocks.sort(key=lambda b: b['pos'])
    return blocks

INTRO_TITLE_RE = re.compile(r'introduc|overview|main\s+results?|statements?\b|summary\s+of|the\s+(main\s+)?(theorem|result)', re.I)
MAX_BLOCK_CHARS = 12000
REF_RE = re.compile(r'\\(?:eq|auto|c|C|v|V)?ref\*?\s*\{|\\cite[a-z]*\s*(?:\[[^\]]*\])*\s*\{')

def block_kind(b):
    """Why a block counts as a 'main' statement (None if it does not)."""
    if b['env'].rstrip('*') in ('maintheorem', 'mainthm', 'MainTheorem', 'mainresult', 'main-theorem'):
        return 'main_env'
    if b['label'] and MAIN_LABEL_RE.search(b['label']):
        return 'main_label'
    if b['title'] and MAIN_TITLE_RE.search(b['title']):
        return 'main_title'
    return None

def analyze_paper(pdir):
    """Extract candidate main-theorem blocks from one paper dir. Returns dict (never raises on odd TeX)."""
    pdir = Path(pdir)
    res = dict(root=None, n_theorem_blocks=0, n_fallback_blocks=0, picked=[], error=None)
    try:
        roots = find_roots(pdir)
        if not roots:
            res['error'] = 'no root tex'
            return res
        base = pdir / 'build'
        thm_re = re.compile(r'\\begin\{(%s)\*?\}' % '|'.join(re.escape(e) for e in THEOREM_ENVS))
        chosen = None
        for root in roots:           # first root that yields theorem blocks (some papers assemble PDFs in main.tex)
            fl = flatten(root, base)
            txt = '\n'.join(t for _, _, t in fl)
            if thm_re.search(txt):
                chosen = root
                break
        if chosen is None:           # no theorem env anywhere: use the best root (fallback envs may still match)
            root = roots[0]
            fl = flatten(root, base)
            txt = '\n'.join(t for _, _, t in fl)
        # offsets of each flattened line, to map a char position back to (file, line)
        offs, acc = [], 0
        for _, _, t in fl:
            offs.append(acc)
            acc += len(t) + 1
        def origin(pos):
            k = bisect.bisect_right(offs, pos) - 1
            return fl[k][0], fl[k][1]
        di = txt.find(BEGIN_DOC)
        secs = [s for s in parse_sections(txt) if di < 0 or s[0] > di]
        res['root'] = os.path.relpath(root, pdir)
        envs = THEOREM_ENVS + sorted(discover_theorem_envs(txt))
        blocks = [b for b in find_blocks(txt, envs, secs) if di < 0 or b['pos'] > di]
        first_sec = next((i for i, s in enumerate(secs) if s[1] == 1), None)
        def in_intro(b):
            i = b['section_idx']
            return i == -1 or i == first_sec or bool(INTRO_TITLE_RE.search(secs[i][2]))
        for b in blocks:
            b['in_intro'] = in_intro(b)
        res['n_theorem_blocks'] = len(blocks)
        picked = []
        for b in blocks:
            k = block_kind(b)
            if k:
                picked.append((b, k))
        ifirst = next((b for b in blocks if b['in_intro']), None)
        if ifirst is not None and all(ifirst is not p[0] for p in picked):
            picked.append((ifirst, 'intro_first'))
        if not picked and blocks:
            picked.append((blocks[0], 'first_theorem'))
        if not picked:
            fb = [b for b in find_blocks(txt, FALLBACK_ENVS, secs) if di < 0 or b['pos'] > di]
            res['n_fallback_blocks'] = len(fb)
            fb_intro = next((b for b in fb if in_intro(b)), None)
            if fb_intro is None and fb:
                fb_intro = fb[0]
            if fb_intro is not None:
                fb_intro['in_intro'] = in_intro(fb_intro)
                picked.append((fb_intro, 'fallback_env'))
        out = []
        for b, kind in picked[:3]:
            f, ln = origin(b['pos'])
            tex = b['tex']
            out.append(dict(paper_dir=pdir.name, reason=kind, env=b['env'], label=b['label'], title=b['title'],
                            section=b['section'], subsection=b['subsection'], in_intro=b['in_intro'],
                            tex_file=f, tex_line=ln, tex_chars=len(tex), n_refs=len(REF_RE.findall(tex)),
                            tex_truncated=len(tex) > MAX_BLOCK_CHARS,
                            tex=tex if len(tex) <= MAX_BLOCK_CHARS else tex[:MAX_BLOCK_CHARS] + '\n% [... truncated ...]'))
        res['picked'] = out
    except Exception as e:  # keep going on odd TeX
        res['error'] = repr(e)
    return res

# ----------------------------------------------------------------------------- Lean helpers
def lean_mask(text):
    """Blank out comments and string literals (keeping newlines/offsets) so structural regexes ignore them."""
    out, i, n, depth = [], 0, len(text), 0
    while i < n:
        c = text[i]
        if depth == 0 and text.startswith('--', i):
            j = text.find('\n', i)
            j = n if j < 0 else j
            out.append(' ' * (j - i))
            i = j
            continue
        if text.startswith('/-', i):
            depth += 1
            out.append('  ')
            i += 2
            continue
        if depth > 0:
            if text.startswith('-/', i):
                depth -= 1
                out.append('  ')
                i += 2
            else:
                out.append('\n' if c == '\n' else ' ')
                i += 1
            continue
        if c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            if j < n:
                out.append(''.join('\n' if ch == '\n' else ' ' for ch in text[i:j + 1]))
                i = j + 1
                continue
        out.append(c)
        i += 1
    return ''.join(out)

DECL_RE = re.compile(r'^[ \t]*(?:@\[[^\]\n]*\][ \t]*)*(?:(?:private|protected|noncomputable|partial|unsafe|nonrec)[ \t]+)*'
                     r'(theorem|lemma|def|abbrev|instance|structure|inductive|class|axiom|opaque|example)\b[ \t]*([^\s:({\[⦃]*)', re.M)
NS_RE = re.compile(r'^[ \t]*namespace[ \t]+(\S+)', re.M)
SEC_RE_L = re.compile(r'^[ \t]*(?:noncomputable[ \t]+)?section\b[ \t]*(\S*)', re.M)
END_RE = re.compile(r'^[ \t]*end\b[ \t]*(\S*)', re.M)
SORRY_RE = re.compile(r'\bsorry\b')
PROOF_TAIL_RE = re.compile(r'\s*:=\s*(?:by\s*)?sorry\s*$')     # ':= by sorry' / ':= sorry' placeholder proof

def parse_lean_decls(text):
    """Declarations with qualified names and line spans: [{kind, name, full, start, doc_start, end}] (0-based line idx)."""
    masked = lean_mask(text)
    mlines, tlines = masked.split('\n'), text.split('\n')
    events = []   # (line, type, payload)
    for m in NS_RE.finditer(masked):
        events.append((masked.count('\n', 0, m.start()), 'ns', m.group(1)))
    for m in SEC_RE_L.finditer(masked):
        events.append((masked.count('\n', 0, m.start()), 'sec', m.group(1)))
    for m in END_RE.finditer(masked):
        events.append((masked.count('\n', 0, m.start()), 'end', m.group(1)))
    decls = []
    for m in DECL_RE.finditer(masked):
        ln = masked.count('\n', 0, m.start())
        decls.append(dict(kind=m.group(1), name=m.group(2).rstrip('.'), start=ln))   # 'foo.{u}' -> 'foo.'
    events.sort(key=lambda e: e[0])
    # namespace stack walk
    frames, ei = [], 0
    for d in decls:
        while ei < len(events) and events[ei][0] <= d['start']:
            _, typ, arg = events[ei]
            if typ == 'ns':
                frames.append(('ns', arg.split('.')))
            elif typ == 'sec':
                frames.append(('sec', [arg] if arg else []))
            elif typ == 'end' and frames:
                frames.pop()
            ei += 1
        ns = [c for k, comps in frames if k == 'ns' for c in comps]
        nm = d['name']
        d['full'] = nm[len('_root_.'):] if nm.startswith('_root_.') else '.'.join(ns + ([nm] if nm else []))
    # spans
    boundaries = sorted(set([d['start'] for d in decls] + [e[0] for e in events]))
    for d in decls:
        # walk up over attribute-only lines and an adjacent doc comment
        ds = d['start']
        while ds > 0 and re.match(r'^\s*@\[[^\]]*\]\s*$', mlines[ds - 1]):
            ds -= 1
        k = ds - 1
        while k >= 0 and not tlines[k].strip():
            k -= 1
        if k >= 0 and tlines[k].rstrip().endswith('-/') and ds - k <= 2:
            j = k
            while j >= 0 and '/--' not in tlines[j]:
                j -= 1
            if j >= 0 and not any(re.match(r'^\s*(theorem|lemma|def|end|namespace)\b', mlines[x]) for x in range(j, k + 1)):
                ds = j
        d['doc_start'] = ds
        nxt = next((b for b in boundaries if b > d['start']), len(tlines))
        end = None
        for ln in range(d['start'], nxt):
            if SORRY_RE.search(mlines[ln]):
                end = ln
                break
        if end is None:
            end = nxt - 1
        while end > d['start'] and not mlines[end].strip():
            end -= 1
        d['end'] = end
    return decls

def lean_targets(text, theorem_names, definition_names=()):
    """Resolve each theorem/definition name of the Comparator config to its declaration text in the challenge file.
    Returns (list of {name, role, kind, line_start, line_end, statement, text}, status in ok/partial/none)."""
    decls = parse_lean_decls(text)
    tlines = text.split('\n')
    out, missing = [], 0
    wanted = [(n, 'theorem') for n in theorem_names] + [(n, 'definition') for n in definition_names]
    for full, role in wanted:
        cands = [d for d in decls if d['full'] == full]
        if not cands:
            short = full.split('.')[-1]
            cands = [d for d in decls if d['name'].split('.')[-1] == short
                     and d['kind'] in ('theorem', 'lemma', 'def', 'abbrev', 'axiom', 'opaque')]
        if not cands:
            missing += 1
            continue
        d = cands[0]
        body = '\n'.join(tlines[d['doc_start']:d['end'] + 1])
        out.append(dict(name=full, role=role, kind=d['kind'], line_start=d['doc_start'] + 1, line_end=d['end'] + 1,
                        statement=PROOF_TAIL_RE.sub('', body.rstrip()), text=body))
    status = 'ok' if wanted and missing == 0 else ('partial' if out else 'none')
    return out, status

def truncate_lean(text, targets, keep_lines=400):
    """First `keep_lines` lines + the target (theorem/definition) blocks of the full file, with elision markers."""
    lines = text.split('\n')
    n = len(lines)
    out, last = lines[:keep_lines], keep_lines
    for t in sorted(targets, key=lambda t: t['line_start']):
        a, b = t['line_start'], t['line_end']          # 1-based, inclusive
        if b <= last:
            continue
        a = max(a, last + 1)
        if a > last + 1:
            out.append('-- [... lines %d-%d of %d elided by build_ml_pairs.py ...]' % (last + 1, a - 1, n))
        out.extend(lines[a - 1:b])
        last = b
    if last < n:
        out.append('-- [... lines %d-%d of %d elided by build_ml_pairs.py ...]' % (last + 1, n, n))
    return '\n'.join(out)

# ----------------------------------------------------------------------------- lexical matching (heuristic)
STOP = set('''the and for with that this from are was were have has had not but all any each every exists exist such then there
where which when than into also its can may let set map lemma theorem proof def of is in on to by as at or an if be we our
their these those some more most other only over under between using used use given holds hold state states prove proves proved
show shows shown main result results paper here namely follow following sorry nat fun fin lean mathlib namespace open end
begin label mathbb mathcal mathrm mathbf mathfrak mathscr mathit left right frac quad qquad text operatorname emph textbf textit
cite citep citet ref eqref cref autoref item itemize enumerate equation align aligned proposition corollary definition remark
sqrt infty leq geq ldots cdots cdot times boldsymbol widehat widetilde overline underline displaystyle tfrac dfrac limits
proof hspace vspace noindent section subsection paragraph footnote href url'''.split())

def _norm_tokens(ts):
    out = []
    for t in ts:
        t = t.lower()
        if t in STOP:
            continue
        if len(t) > 4 and t.endswith('s') and not t.endswith('ss'):
            t = t[:-1]
        out.append(t)
    return out

def tokens_nl(text):
    text = (text or '').replace('\\', ' ')                 # keep command names (\\zeta -> zeta); formatting ones are in STOP
    text = re.sub(r'<[^>]+>', ' ', text)
    return _norm_tokens(re.findall(r'[A-Za-z]{3,}', text))

def tokens_lean(text):
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text or '')
    text = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', text)
    return _norm_tokens([p for p in re.findall(r'[A-Za-z]+', text) if len(p) >= 3])

def tfidf(tokens, idf, default):
    tf = Counter(tokens)
    return {t: (1 + math.log(c)) * idf.get(t, default) for t, c in tf.items()}

def cosine(a, b):
    if not a or not b:
        return 0.0
    num = sum(w * b.get(t, 0.0) for t, w in a.items())
    den = math.sqrt(sum(w * w for w in a.values())) * math.sqrt(sum(w * w for w in b.values()))
    return num / den if den else 0.0

def lean_docstrings(text, limit=4000):
    return ' '.join(m.group(1) for m in re.finditer(r'/--(.*?)-/', text, re.S))[:limit]

# ----------------------------------------------------------------------------- lean/docs pages
def parse_doc(text):
    """-> dict(title, papers[dirs in order], scope, rows[(result_label, challenge)])"""
    head, _, rest = text.partition('## Scope')
    title = (re.match(r'#\s*(.*)', head) or [None, ''])[1].strip()
    papers = []
    for d in re.findall(r'\]\(\.\./\.\./preprints/(.+?)/[^/\n]*?\.pdf\)', head):
        if d not in papers:
            papers.append(d)
    scope, _, links = rest.partition('## Comparator links')
    rows = []
    for line in links.splitlines():
        if line.lstrip().startswith('|') and 'ComparatorChallenges/' in line:
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            label = ' | '.join(cells[:-1]) if len(cells) > 2 else cells[0]
            for m in re.finditer(r'ComparatorChallenges/([A-Za-z0-9_]+)\.lean', cells[-1]):
                rows.append((label, m.group(1)))
    return dict(title=title, papers=papers, scope=scope.strip(), rows=rows)

# ----------------------------------------------------------------------------- local checker status (verification/lean_checks)
def local_check_status(checks_dir, name):
    cmp_s, comp_s = 'none', 'none'
    p = Path(checks_dir) / f'{name}.cmp.txt'
    if p.is_file():
        m = re.findall(r'comparator-style: ok=(\d+) problems=(\d+) errors=(\d+)([^\n]*)', read_text(p))
        if m:
            ok, prob, err = map(int, m[-1][:3])
            rest = m[-1][3]            # '| no-shadowing | [axioms...]'
            cmp_s = 'pass' if ok > 0 and prob == 0 and err == 0 and 'SHADOW-DIFF' not in rest and 'sorryAx' not in rest else 'fail'
    p = Path(checks_dir) / f'{name}.comparator.txt'
    if p.is_file():
        t = read_text(p)
        if 'Your solution is okay' in t:
            comp_s = 'pass'
        elif re.search(r'comparator exit=[1-9]', t):
            comp_s = 'fail'
    return cmp_s, comp_s

FIDELITY_SHORT = {'full': 'full', 'partial': 'partial', 'weaker-statement': 'weaker', 'supporting-only': 'supporting', 'none': 'none'}
NON_PACKAGES = {'all', 'OAI'}          # import-modifier token / the project itself, artefacts of the cone parser

# ----------------------------------------------------------------------------- import cones (corrected re-computation)
IMPORT_RE = re.compile(r'^import\s+(?:all\s+)?([^\s]+)', re.M)      # handles `import all X` and apostrophes in module names
AXIOM_RE = re.compile(r'^[ \t]*axiom\b', re.M)

class Cones:
    """Transitive import cone of a solution module inside lean/OAI, read lazily from the clone.
    Same definition as scripts/import_cones.py (tmp/import_cones.json) with its two parser bugs fixed:
    `import all X` and module names containing an apostrophe; and `axiom` is only counted outside comments."""
    def __init__(self, lean_dir):
        self.lean_dir, self.cache = Path(lean_dir), {}
    def info(self, mod):
        if mod not in self.cache:
            p = self.lean_dir / (mod.replace('.', '/') + '.lean')
            if not p.is_file():
                self.cache[mod] = None
            else:
                t = p.read_bytes().decode('utf-8', 'ignore')
                ax = bool(AXIOM_RE.search(t)) and bool(AXIOM_RE.search(lean_mask(t)))
                self.cache[mod] = (IMPORT_RE.findall(t), t.count('\n'), ax)
        return self.cache[mod]
    def cone(self, start):
        seen, ext, todo, files, lines, axioms = set(), set(), [start], 0, 0, []
        while todo:
            m = todo.pop()
            if m in seen:
                continue
            seen.add(m)
            i = self.info(m) if m.startswith('OAI.') else None
            if i is None:
                ext.add(m.split('.')[0])
                continue
            files += 1
            lines += i[1]
            if i[2]:
                axioms.append(m)
            todo.extend(i[0])
        return dict(oai_files=files, oai_lines=lines, external=sorted(ext), axiom_files=sorted(axioms))

def main_checkout():
    try:
        gc = subprocess.run(['git', '-C', str(REPO), 'rev-parse', '--git-common-dir'], capture_output=True, text=True, check=True).stdout.strip()
        return (Path(gc) if os.path.isabs(gc) else (REPO / gc)).resolve().parent
    except Exception:
        return REPO

def first_existing(*cands):
    for c in cands:
        if c and Path(c).exists():
            return Path(c)
    raise SystemExit('missing input: tried ' + ', '.join(str(c) for c in cands))

# ----------------------------------------------------------------------------- build
MAX_FULL_LINES = 1000        # challenge files longer than this are truncated: first KEEP_HEAD lines + target blocks
KEEP_HEAD = 400
MAX_JSONL_BYTES = 50 * 1024 * 1024
GOOD_REASONS = {'main_label', 'main_title', 'main_env', 'intro_first'}
MAX_NL_BLOCKS = 3

CONTENTS_HEAD_RE = re.compile(r'^&emsp;\[(.*)\]\(preprints/(.+?)/[^/\n]*?\.pdf\)(.*)$')

def parse_contents(path):
    """CONTENTS.md manuscript entries -> {paper dir: {title, abstract}} (the abstract is the text up to the closing </td>)."""
    lines = read_text(path).split('\n')
    out = {}
    for i, line in enumerate(lines):
        m = CONTENTS_HEAD_RE.match(line)
        if not m:
            continue
        j, buf = i + 1, []
        while j < len(lines) and '</td>' not in lines[j]:
            buf.append(lines[j])
            j += 1
        out[m.group(2)] = dict(title=m.group(1).strip(), abstract='\n'.join(buf).strip() or None)
    return out

def build(upstream, cones_path, out_dir, checks_dir):
    idx = json.load(open(REPO / 'index.json', encoding='utf-8'))
    fams, ms, commit = idx['families'], {m['dir']: m for m in idx['manuscripts']}, idx['commit']
    contents = parse_contents(upstream / 'CONTENTS.md')
    assert set(contents) == set(ms), 'CONTENTS.md manuscripts differ from index.json'
    index_repairs = []                 # index.json mis-parses 2 entries of family 107 ("secondary writeup" line): use CONTENTS.md
    for d, m in ms.items():
        c = contents[d]
        if (m.get('title') or '').strip() != c['title'] or m.get('abstract') != c['abstract']:
            index_repairs.append(d)
        m['title'], m['abstract'] = c['title'], c['abstract']
    lean_dir = upstream / 'lean'
    chal_dir = lean_dir / 'ComparatorChallenges'
    cones_json = json.load(open(cones_path, encoding='utf-8')) if cones_path else {}
    cone_idx = Cones(lean_dir)
    cone_diffs = {}
    audits = {}
    for p in (1, 2, 3):
        for r in json.load(open(REPO / 'verification' / f'lean_scope_audit_part{p}.json', encoding='utf-8')):
            r['_part'] = p
            assert r['family'] not in audits, 'duplicate family in audits'
            audits[r['family']] = r
    lean_fams = sorted(k for k, v in fams.items() if v.get('lean_challenges'))
    assert set(lean_fams) == set(audits), 'audit families != index lean families'
    docs = {k: parse_doc(read_text(lean_dir / 'docs' / f'{k}.md')) for k in lean_fams}
    for k in lean_fams:                       # docs <-> index consistency
        assert docs[k]['scope'] == fams[k]['lean_scope'].strip(), 'scope text differs for %s' % k
        assert {c for _, c in docs[k]['rows']} == set(fams[k]['lean_challenges']), 'challenge links differ for %s' % k
        assert set(docs[k]['papers']) <= set(fams[k]['papers']), 'doc paper not in family %s' % k
        assert set(audits[k]['challenges']) == set(fams[k]['lean_challenges'])

    # ---- NL side: per-paper theorem blocks (all papers of Lean families)
    paper_dirs = [d for k in lean_fams for d in fams[k]['papers']]
    PA = {}
    for d in paper_dirs:
        PA[d] = analyze_paper(upstream / 'preprints' / d)
    sys.stderr.write('analyzed %d papers; errors: %d\n' % (len(PA), sum(1 for r in PA.values() if r['error'])))
    paper_tok = {}
    for d in paper_dirs:
        m = ms[d]
        paper_tok[d] = tokens_nl(m['title'] + ' ' + (m.get('abstract') or '')) + tokens_nl(' '.join(p['tex'] for p in PA[d]['picked']))
    df = Counter()
    for toks in paper_tok.values():
        df.update(set(toks))
    N = len(paper_tok)
    idf = {t: math.log((N + 1) / (c + 1)) + 1 for t, c in df.items()}
    default_idf = math.log(N + 1) + 1
    paper_vec = {d: tfidf(t, idf, default_idf) for d, t in paper_tok.items()}
    title_vec = {d: tfidf(tokens_nl(ms[d]['title']), idf, default_idf) for d in paper_tok}
    def ta_text(d):      # title + abstract; a manuscript listed without abstract gets its first main block instead (avoids a dilution bias)
        return ms[d]['title'] + ' ' + (ms[d].get('abstract') or ' '.join(p['tex'] for p in PA[d]['picked'][:1]))
    ta_vec = {d: tfidf(tokens_nl(ta_text(d)), idf, default_idf) for d in paper_tok}

    rows = []
    for k in lean_fams:
        fam, doc, aud = fams[k], docs[k], audits[k]
        family_challenges = list(fam['lean_challenges'])
        linked = [d for d in doc['papers'] if d in PA]
        cand_dirs = linked or [d for d in fam['papers'] if d in PA]
        for c in family_challenges:
            cfg = json.load(open(chal_dir / f'{c}.json', encoding='utf-8'))
            raw = (chal_dir / f'{c}.lean').read_bytes()
            text = raw.decode('utf-8')
            thm_names, def_names = cfg['theorem_names'], cfg.get('definition_names', [])
            targets, tstatus = lean_targets(text, thm_names, def_names)
            n_lines = len(text.splitlines())
            truncated = n_lines > MAX_FULL_LINES
            lean_text = truncate_lean(text, targets, KEEP_HEAD) if truncated else text
            masked = lean_mask(text)
            cone = cone_idx.cone(cfg['solution_module'])
            if c in cones_json:                       # cross-check against tmp/import_cones.json
                assert cones_json[c]['solution_module'] == cfg['solution_module']
                o = cones_json[c]
                if (o['oai_files'], o['oai_lines']) != (cone['oai_files'], cone['oai_lines']):
                    cone_diffs[c] = dict(import_cones_json=[o['oai_files'], o['oai_lines']], recomputed=[cone['oai_files'], cone['oai_lines']])
                assert set(o['external']) - NON_PACKAGES == set(cone['external']) - NON_PACKAGES, 'external packages differ for %s' % c
            sol_file = 'lean/' + cfg['solution_module'].replace('.', '/') + '.lean'
            sol_path = upstream / sol_file
            labels = [lab for lab, cc in doc['rows'] if cc == c]
            cmp_s, comp_s = local_check_status(checks_dir, c)

            # NL selection: papers ranked by lexical match to the challenge, then each paper's main blocks
            ch_tokens = (tokens_lean(c) * 2 + tokens_nl(' '.join(labels)) * 2 + tokens_lean(' '.join(thm_names + def_names))
                         + tokens_lean(lean_docstrings(text)) + tokens_lean(' '.join(t['text'] for t in targets)))
            chv = tfidf(ch_tokens, idf, default_idf)
            sv = tfidf(tokens_lean(c) + tokens_nl(' '.join(labels)), idf, default_idf)      # short description: name + docs result label
            def paper_score(d):
                return (cosine(sv, title_vec[d]) + cosine(sv, ta_vec[d]) + 0.5 * cosine(chv, paper_vec[d])) / 2.5
            ranked = sorted(((-paper_score(d), i, d) for i, d in enumerate(cand_dirs)))
            blocks = []
            for negsc, _, d in ranked:
                for b in PA[d]['picked']:
                    if len(blocks) >= MAX_NL_BLOCKS:
                        break
                    bt = tfidf(tokens_nl(b['tex'] + ' ' + (b['title'] or '')), idf, default_idf)
                    blocks.append(dict(b, match_score=round(cosine(chv, bt), 4)))
            if not blocks:
                quality = 'none'
            else:
                b0 = blocks[0]
                quality = 'good' if (b0['reason'] in GOOD_REASONS and (b0['paper_dir'] in doc['papers'] or not doc['papers'])) else 'partial'
            primary = blocks[0]['paper_dir'] if blocks else (ranked[0][2] if ranked else None)
            nl_papers = []
            for d in fam['papers']:
                if d not in PA:
                    continue
                nl_papers.append(dict(dir=d, title=ms[d]['title'], abstract=ms[d]['abstract'], lean_linked=d in doc['papers'],
                                      match_score=round(paper_score(d), 4), n_theorem_blocks=PA[d]['n_theorem_blocks'],
                                      tex_root=PA[d]['root']))
            rows.append(dict(
                challenge=c,
                upstream_commit=commit,
                source_url='https://github.com/openai/math/blob/%s/lean/ComparatorChallenges/%s.lean' % (commit, c),
                lean_file='lean/ComparatorChallenges/%s.lean' % c,
                config_file='lean/ComparatorChallenges/%s.json' % c,
                challenge_module=cfg['challenge_module'],
                solution_module=cfg['solution_module'],
                solution_file=sol_file,
                solution_file_lines=sum(1 for _ in open(sol_path, encoding='utf-8')) if sol_path.is_file() else None,
                theorem_names=thm_names,
                definition_names=def_names,
                permitted_axioms=cfg['permitted_axioms'],
                enable_nanoda=cfg.get('enable_nanoda'),
                solution_imports=cfg.get('solution_imports'),
                lean_text=lean_text,
                lean_truncated=truncated,
                lean_lines_total=n_lines,
                lean_text_lines=len(lean_text.splitlines()),
                lean_bytes_total=len(raw),
                lean_sha256=hashlib.sha256(raw).hexdigest(),
                lean_has_sorry=bool(SORRY_RE.search(masked)),
                lean_has_axiom_decl=bool(re.search(r'^[ \t]*axiom\b', masked, re.M)),
                lean_targets=targets,
                lean_targets_status=tstatus,
                cone_oai_files=cone['oai_files'],
                cone_oai_lines=cone['oai_lines'],
                cone_external=sorted(set(cone['external']) - NON_PACKAGES),
                cone_axiom_files=cone['axiom_files'],
                check_cmp=cmp_s,
                check_comparator=comp_s,
                family=k,
                family_title=fam['title'],
                family_subject=fam['subject'],
                family_summary=fam['summary'],
                family_scope=doc['scope'],
                family_challenges=family_challenges,
                challenge_result_labels=labels,
                fidelity_label=aud['headline_formalized'],
                fidelity_class=FIDELITY_SHORT[aud['headline_formalized']],
                fidelity_gap_note=aud['gap_note'],
                fidelity_suspicious_defs=aud['suspicious_defs'],
                fidelity_audit_part=aud['_part'],
                one_to_one=len(family_challenges) == 1 and len(doc['papers']) == 1,
                nl_extraction_quality=quality,
                nl_primary_paper=primary,
                nl_abstract=ms[primary]['abstract'] if primary else None,
                nl_main_theorems=[{kk: vv for kk, vv in b.items()} for b in blocks],
                nl_papers=nl_papers,
            ))
    report = dict(
        index_json_manuscript_repairs=sorted(index_repairs),
        cone_check=dict(compared_with_import_cones_json=len(cones_json), differences=cone_diffs,
                        axiom_files_flagged_in_json={c: v['axiom_files'] for c, v in sorted(cones_json.items()) if v.get('axiom_files')}))
    return rows, PA, report

def compute_stats(rows, PA, extra):
    n = len(rows)
    fam_first = {}
    for r in rows:
        fam_first.setdefault(r['family'], r)
    def cnt(it):
        return dict(sorted(Counter(it).items()))
    s = dict(extra)
    s.update(
        n_challenges=n,
        n_families=len(fam_first),
        n_papers_in_lean_families=len(PA),
        n_lean_linked_papers=len({d for r in rows for p in r['nl_papers'] if p['lean_linked'] for d in [p['dir']]}),
        fidelity_label_challenges=cnt(r['fidelity_label'] for r in rows),
        fidelity_label_families=cnt(r['fidelity_label'] for r in fam_first.values()),
        fidelity_class_challenges=cnt(r['fidelity_class'] for r in rows),
        nl_extraction_quality_challenges=cnt(r['nl_extraction_quality'] for r in rows),
        nl_extraction_quality_families=dict(
            all_challenges_good=sum(1 for f in fam_first if all(x['nl_extraction_quality'] == 'good' for x in rows if x['family'] == f)),
            any_challenge_partial=sum(1 for f in fam_first if any(x['nl_extraction_quality'] == 'partial' for x in rows if x['family'] == f)),
            any_challenge_none=sum(1 for f in fam_first if any(x['nl_extraction_quality'] == 'none' for x in rows if x['family'] == f))),
        nl_first_block_reason=cnt(r['nl_main_theorems'][0]['reason'] for r in rows if r['nl_main_theorems']),
        nl_blocks_per_challenge=cnt(len(r['nl_main_theorems']) for r in rows),
        papers_with_any_block=sum(1 for v in PA.values() if v['picked']),
        papers_with_main_label_block=sum(1 for v in PA.values() if any(p['reason'].startswith('main') for p in v['picked'])),
        challenges_one_to_one=sum(r['one_to_one'] for r in rows),
        challenges_one_to_one_good_full=sum(1 for r in rows if r['one_to_one'] and r['nl_extraction_quality'] == 'good' and r['fidelity_class'] == 'full'),
        challenges_good_and_full=sum(1 for r in rows if r['nl_extraction_quality'] == 'good' and r['fidelity_class'] == 'full'),
        challenges_in_multi_challenge_families=sum(1 for r in rows if len(r['family_challenges']) > 1),
        lean_truncated_challenges=[r['challenge'] for r in rows if r['lean_truncated']],
        lean_targets_status=cnt(r['lean_targets_status'] for r in rows),
        lean_target_counts=dict(theorems=sum(1 for r in rows for t in r['lean_targets'] if t['role'] == 'theorem'),
                                definitions=sum(1 for r in rows for t in r['lean_targets'] if t['role'] == 'definition')),
        lean_without_sorry=[r['challenge'] for r in rows if not r['lean_has_sorry']],
        lean_with_axiom_decl=[r['challenge'] for r in rows if r['lean_has_axiom_decl']],
        lean_total_lines=sum(r['lean_lines_total'] for r in rows),
        lean_total_bytes=sum(r['lean_bytes_total'] for r in rows),
        cone_axiom_files_challenges=[r['challenge'] for r in rows if r['cone_axiom_files']],
        cone_third_party_packages=cnt(p for r in rows for p in r['cone_external'] if p not in ('Mathlib', 'Lean', 'Std', 'Init')),
        challenges_with_third_party_cone_dependency=sum(1 for r in rows if set(r['cone_external']) - {'Mathlib', 'Lean', 'Std', 'Init'}),
        check_cmp=cnt(r['check_cmp'] for r in rows),
        check_comparator=cnt(r['check_comparator'] for r in rows),
        median_cone_oai_lines=sorted(r['cone_oai_lines'] for r in rows)[n // 2],
        fidelity_class_by_nl_quality={fc: cnt(r['nl_extraction_quality'] for r in rows if r['fidelity_class'] == fc)
                                      for fc in sorted({r['fidelity_class'] for r in rows})},
        fidelity_class_by_one_to_one={fc: dict(one_to_one=sum(1 for r in rows if r['fidelity_class'] == fc and r['one_to_one']),
                                               other=sum(1 for r in rows if r['fidelity_class'] == fc and not r['one_to_one']))
                                      for fc in sorted({r['fidelity_class'] for r in rows})},
        lean_lines_total_quantiles=dict(median=sorted(r['lean_lines_total'] for r in rows)[n // 2],
                                        p90=sorted(r['lean_lines_total'] for r in rows)[int(0.9 * n)],
                                        max=max(r['lean_lines_total'] for r in rows)),
        challenges_by_family_size=cnt(len(r['family_challenges']) for r in rows),
        subjects=cnt(r['family_subject'] for r in fam_first.values()),
    )
    return s

def self_check(path, upstream):
    """Re-read the JSONL and assert integrity: hashes, target spans, NL provenance (\\begin{env} at tex_file:tex_line)."""
    back = [json.loads(l) for l in open(path, encoding='utf-8')]
    assert len(back) == len({r['challenge'] for r in back}), 'duplicate challenge rows'
    assert len({tuple(r.keys()) for r in back}) == 1, 'rows have different key sets'
    n_blocks, cache = 0, {}
    for r in back:
        if not r['lean_truncated']:
            assert hashlib.sha256(r['lean_text'].encode('utf-8')).hexdigest() == r['lean_sha256'], r['challenge']
        for t in r['lean_targets']:
            assert t['text'] in r['lean_text'] and t['statement'] in t['text'], (r['challenge'], t['name'])
        for b in r['nl_main_theorems']:
            key = (b['paper_dir'], b['tex_file'])
            if key not in cache:
                cache[key] = read_text(upstream / 'preprints' / b['paper_dir'] / b['tex_file']).split('\n')
            line = cache[key][b['tex_line'] - 1]
            assert '\\begin{' + b['env'].rstrip('*') in line, (r['challenge'], key, b['tex_line'], line[:80])
            if not b['tex_truncated']:
                assert b['tex'].startswith('\\begin{' + b['env'].rstrip('*')) and b['tex'].rstrip().endswith('\\end{' + b['env'] + '}'), (r['challenge'], key)
            n_blocks += 1
    sys.stderr.write('self-check ok: %d rows, %d NL blocks traced to tex_file:tex_line\n' % (len(back), n_blocks))

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mc = main_checkout()
    ap.add_argument('--upstream', default=None, help='openai/math clone (default: <repo>/math or the main checkout)')
    ap.add_argument('--cones', default=None, help='import_cones.json (default: <repo>/tmp or the main checkout)')
    ap.add_argument('--out', default=str(REPO / 'ml'))
    ap.add_argument('--checks', default=str(REPO / 'verification' / 'lean_checks'))
    a = ap.parse_args()
    upstream = first_existing(a.upstream, REPO / 'math', mc / 'math')
    try:
        cones = first_existing(a.cones, REPO / 'tmp' / 'import_cones.json', mc / 'tmp' / 'import_cones.json')
    except SystemExit:
        cones = None                                   # cross-check only; cones are recomputed from the clone
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    rows, PA, report = build(upstream, cones, out, a.checks)
    path = out / 'autoformalization_pairs.jsonl'
    with open(path, 'w', encoding='utf-8') as f:
        for r in rows:
            line = json.dumps(r, ensure_ascii=False)
            line = line.replace('\u2028', '\\u2028').replace('\u2029', '\\u2029').replace('\x85', '\\u0085')   # keep one record per line for any line splitter
            f.write(line + '\n')
    size = path.stat().st_size
    assert size < MAX_JSONL_BYTES, 'JSONL too large: %d bytes' % size
    self_check(path, upstream)
    extra = dict(built_at=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                 upstream_commit=json.load(open(REPO / 'index.json', encoding='utf-8'))['commit'],
                 jsonl_bytes=size,
                 builder='scripts/build_ml_pairs.py',
                 builder_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                 params=dict(max_full_lines=MAX_FULL_LINES, keep_head_lines=KEEP_HEAD, max_nl_blocks=MAX_NL_BLOCKS, max_block_chars=MAX_BLOCK_CHARS))
    extra.update(report)
    stats = compute_stats(rows, PA, extra)
    with open(out / 'stats.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
        f.write('\n')
    sys.stderr.write('wrote %s (%.1f MB, %d rows) and stats.json\n' % (path, size / 1e6, len(rows)))

if __name__ == '__main__':
    main()
