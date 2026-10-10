#!/usr/bin/env python3
"""Build the referee packet for the frozen 40-family sample (PROTOCOL.md, "The referees").

Per family the referee receives, assembled from the reviewed upstream commit:
  * the overview summary (the headline claim), verbatim;
  * the repository's own scope note lean/docs/NNN.md, verbatim (relative links rewritten to absolute GitHub URLs);
  * every challenge statement linked from that scope note: the .lean file and its Comparator .json, copied alongside;
  * for every paper of the family, in catalogue order, the paper's main theorem at file and line with its TeX excerpt
    (dataset/paper_main_theorems.json, a text heuristic), marked as linked or not linked from the scope note;
and nothing from MathVet: no verdict, no review note, no list of definitions to check. The script refuses to run on a
dirty upstream tree, checks that the challenge set equals the scope note's links, verifies that no review text leaked
into the packet, builds atomically, and writes a SHA-256 manifest of every file but itself.

Usage: python3 reviews/openai-math/referee/make_packet.py [--upstream PATH] [--zip OUT.zip]
  PATH: a checkout of github.com/openai/math at the PACKET commit (referee/COMMIT; default: upstream/openai-math in this
  repository, or $MATHVET_UPSTREAM). The packet is frozen with the sample: its inputs are the copies under frozen/ even after
  the review moves to a newer commit. Outputs: families/NNN/{README.md,*.lean,*.json}, form.csv, manifest.sha256.
"""
import argparse, csv, hashlib, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REV = HERE.parent
ROOT = REV.parents[1]
UPSTREAM_URL = 'https://github.com/openai/math'
MATHVET_URL = 'https://github.com/mathvet/mathvet'
CLASSES = ('full', 'partial', 'weaker-statement', 'supporting-only', 'none')

ap = argparse.ArgumentParser()
ap.add_argument('--upstream', default=os.environ.get('MATHVET_UPSTREAM') or str(ROOT / 'upstream' / 'openai-math'))
ap.add_argument('--zip', default=None, help='also write the packet (plus PROTOCOL.md and sample.txt) as a zip archive at this path')
args = ap.parse_args()
UP = Path(args.upstream)
if not (UP / 'lean' / 'docs').is_dir():
    sys.exit(f'upstream checkout not found at {UP} (clone {UPSTREAM_URL} there, or pass --upstream)')


def git(*a):
    return subprocess.run(['git', '-C', str(UP), *a], capture_output=True, text=True, check=True).stdout


FROZEN = HERE / 'frozen'          # inputs captured at the frozen commit (the review itself may have moved on)
COMMIT = (HERE / 'COMMIT').read_text().strip()
index = json.load(open(FROZEN / 'index.json', encoding='utf-8'))
assert index['commit'] == COMMIT, 'frozen/index.json is not at the packet commit'
if git('rev-parse', 'HEAD').strip() != COMMIT:
    sys.exit(f'{UP} is not at the reviewed commit {COMMIT[:8]}')
dirty = git('status', '--porcelain', '--', 'lean/docs', 'lean/ComparatorChallenges', 'preprints', 'overview.tex', 'CONTENTS.md').strip()
if dirty:
    sys.exit('upstream checkout has local changes in the files this packet copies; refusing:\n' + dirty)
fams = index['families']
manuscripts = {m['dir']: m for m in index['manuscripts']}
paper_thms = json.load(open(FROZEN / 'paper_main_theorems.json', encoding='utf-8'))
assert paper_thms['upstream_commit'] == COMMIT, 'frozen/paper_main_theorems.json is for another commit'
PT = paper_thms['papers']
rows = [json.loads(l) for l in open(FROZEN / 'pairs.jsonl', encoding='utf-8')]
by_ch = {r['challenge']: r for r in rows}
linked_dirs = {r['family']: {p['dir'] for p in r['nl_papers'] if p.get('lean_linked')} for r in rows}
for r in rows:
    linked_dirs[r['family']] |= {p['dir'] for p in r['nl_papers'] if p.get('lean_linked')}
sample = [l.strip() for l in open(REV / 'sample.txt', encoding='utf-8') if l.strip()]
assert len(sample) == 40, len(sample)
digest = hashlib.sha256(''.join(f + '\n' for f in sample).encode()).hexdigest()
assert (REV / 'sample.sha256').read_text().split()[0] == digest, 'sample.txt does not match sample.sha256'

# The review's own text, loaded ONLY to verify afterwards that none of it is in the packet.
review_text = []
for p in sorted((REV / 'source').glob('lean_scope_audit_part*.json')):
    for r in json.load(open(p, encoding='utf-8')):
        if r['family'] in sample:
            review_text.append(r['gap_note'])
            review_text += list(r.get('suspicious_defs') or [])
ft = json.load(open(REV / 'fidelity-table.json', encoding='utf-8'))
for f in ft['families']:
    if f['family'] in sample:
        review_text.append(f['review_note'])
        review_text += list(f.get('definitions_to_check') or [])
review_text += json.load(open(FROZEN / 'review_text.json', encoding='utf-8'))   # the review's text at the frozen commit


def blob(path, line=None):
    return f'{UPSTREAM_URL}/blob/{COMMIT}/{path}' + (f'#L{line}' if line else '')


def tree(path):
    return f'{UPSTREAM_URL}/tree/{COMMIT}/{path}'


def rewrite_links(md):
    """lean/docs/NNN.md links to ../../preprints/… and ../ComparatorChallenges/…; make them absolute at the reviewed commit."""
    md = re.sub(r'\]\(\.\./\.\./preprints/([^)]+)\)', lambda m: f']({UPSTREAM_URL}/blob/{COMMIT}/preprints/{m.group(1)})', md)
    md = re.sub(r'\]\(\.\./ComparatorChallenges/([^)]+)\)', lambda m: f']({UPSTREAM_URL}/blob/{COMMIT}/lean/ComparatorChallenges/{m.group(1)})', md)
    return md


HEURISTIC = ('Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first '
             'theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not '
             'the statement the headline refers to, or the headline refers to a different paper, read that paper\'s own statement '
             'and say so in your justification.')

tmp_out = Path(tempfile.mkdtemp(prefix='families.', dir=HERE))
written = []
for fam in sample:
    fi = fams[fam]
    chs = sorted(fi['lean_challenges'].keys())
    assert chs, f'family {fam} has no challenges in the index'
    scope = (UP / 'lean' / 'docs' / f'{fam}.md').read_text(encoding='utf-8')
    linked_in_note = sorted(set(re.findall(r'ComparatorChallenges/([A-Za-z0-9_]+)\.lean', scope)))
    if linked_in_note != chs:
        sys.exit(f'family {fam}: challenges linked from the scope note {linked_in_note} differ from the index {chs}')
    d = tmp_out / fam
    d.mkdir()
    parts = [f'# Family {fam} — {fi["title"]}', '',
             f'Subject: {fi["subject"]}. Reviewed repository: `{UPSTREAM_URL}` at commit `{COMMIT}`. '
             f'Catalogue entry: family {fam} in `overview.pdf` / `CONTENTS.md`.', '',
             '## 1. Headline claim (the overview summary, verbatim)', '', fi['summary'].strip(), '',
             f'## 2. The repository\'s own scope note ([`lean/docs/{fam}.md`]({blob(f"lean/docs/{fam}.md")}), verbatim; relative links made absolute)', '',
             rewrite_links(scope.strip()), '',
             '## 3. Challenge statements (every file linked from the scope note; copies in this folder)', '']
    for c in chs:
        shutil.copyfile(UP / 'lean' / 'ComparatorChallenges' / f'{c}.lean', d / f'{c}.lean')
        shutil.copyfile(UP / 'lean' / 'ComparatorChallenges' / f'{c}.json', d / f'{c}.json')
        j = json.load(open(d / f'{c}.json', encoding='utf-8'))
        r = by_ch.get(c, {})
        parts += [f'- [`{c}.lean`]({blob(f"lean/ComparatorChallenges/{c}.lean")}) — the lab\'s result label: '
                  f'*{" / ".join(r.get("challenge_result_labels") or []) or "(none)"}*. Comparator config '
                  f'[`{c}.json`]({blob(f"lean/ComparatorChallenges/{c}.json")}): theorem(s) `{"`, `".join(j["theorem_names"])}`'
                  + (f'; definition(s) `{"`, `".join(j["definition_names"])}`' if j.get('definition_names') else '')
                  + f'; permitted axioms {", ".join("`" + a + "`" for a in j["permitted_axioms"])}; '
                  f'solution module `{j["solution_module"]}`.']
    parts += ['', 'The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem '
              'names listed in the config are the ones the Comparator compares.', '',
              '## 4. The papers of this family and their main theorems (file and line, TeX excerpt)', '',
              'Papers in the order of the catalogue entry. The headline\'s first-named claim may be stated in any of them; the '
              'scope note links the Lean to the paper(s) marked *linked from the scope note*. ' + HEURISTIC, '']
    for n, pd in enumerate(fi['papers'], 1):
        info = PT.get(pd) or {}
        title = manuscripts.get(pd, {}).get('title') or info.get('title') or pd
        mark = 'linked from the scope note' if pd in linked_dirs.get(fam, set()) else 'not linked from the scope note'
        parts += [f'### 4.{n} {title} — *{mark}*', '',
                  f'[`preprints/{pd}/paper.pdf`]({blob(f"preprints/{pd}/paper.pdf")}) · [source]({tree(f"preprints/{pd}")})', '']
        blocks = info.get('blocks') or []
        if not blocks:
            parts += ['*No theorem environment was found by the heuristic; read the paper.*', '']
        for i, b in enumerate(blocks):
            label = f'`{b["env"]}`' + (f' `{b["label"]}`' if b.get('label') else '') + (f' ({b["title"]})' if b.get('title') else '')
            tf, tl = b.get('tex_file'), b.get('tex_line')
            where = f'[`{tf}:{tl}`]({blob(f"preprints/{pd}/{tf}", tl)})' if tf else ''
            if i == 0:
                parts += [f'{label} at {where}:', '', '```latex', (b.get('tex') or '').strip(), '```', '']
            else:
                parts += [f'Also located: {label} at {where}.', '']
    parts += ['## 5. Your classification', '',
              f'Enter one line for family `{fam}` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, '
              '`supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, '
              'any non-standard definition you noticed, and the minutes spent.', '']
    (d / 'README.md').write_text('\n'.join(parts), encoding='utf-8')
    written.append(fam)

# Leak check: nothing from the review may appear in the packet (family bundles and the top-level README).
norm = lambda s: re.sub(r'\s+', ' ', s).strip().lower()
fam_text = norm('\n'.join(p.read_text(encoding='utf-8', errors='replace') for p in sorted(tmp_out.rglob('*')) if p.is_file()))
readme_text = norm((HERE / 'README.md').read_text(encoding='utf-8')) if (HERE / 'README.md').exists() else ''
leaks = []
for text in review_text:
    for frag in re.split(r'(?<=[.;])\s+', norm(text)):
        frag = frag.strip(' .;')
        if len(frag) >= 30 and (frag in fam_text or frag in readme_text):
            leaks.append(frag[:70])
for word in ('mathvet', 'verdict', 'pre-referee', 'headline_formalized', 'gap_note', 'suspicious_defs', 'review_note', 'fidelity'):
    if word in fam_text:
        leaks.append(f'keyword {word!r} in a family bundle')
if leaks:
    shutil.rmtree(tmp_out)
    sys.exit('REVIEW TEXT LEAKED INTO THE PACKET: ' + '; '.join(leaks))

out_dir = HERE / 'families'
if out_dir.exists():
    shutil.rmtree(out_dir)
tmp_out.rename(out_dir)

with open(HERE / 'form.csv', 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['family', 'class', 'justification', 'nonstandard_definitions', 'minutes'])
    for fam in sample:
        w.writerow([fam, '', '', '', ''])

with open(HERE / 'manifest.sha256', 'w', encoding='utf-8') as fh:
    for p in sorted(HERE.rglob('*')):
        if p.is_file() and p.name != 'manifest.sha256' and 'families.' not in p.parts[len(HERE.parts)] and '__pycache__' not in p.parts:
            fh.write(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(HERE)}\n')
n_files = sum(1 for p in out_dir.rglob('*') if p.is_file())
print(f'packet: {len(written)} families, {n_files} files, commit {COMMIT[:8]}, no review text found in it')
if args.zip:
    stage = Path(tempfile.mkdtemp(prefix='referee-zip.'))
    shutil.copytree(HERE, stage / 'referee', ignore=shutil.ignore_patterns('__pycache__'))
    proto = (ROOT / 'PROTOCOL.md').read_text(encoding='utf-8')   # the copy in the zip omits "The sample" (it names families by stratum)
    proto = re.sub(r'## The sample \(frozen\)\n.*?(?=\n## The referees)',
                   '## The sample (frozen)\n\n*Omitted from this copy of the protocol because it names families by stratum; the full text is at '
                   f'{MATHVET_URL}/blob/main/PROTOCOL.md. Read it after both forms are in.*\n', proto, flags=re.S)
    (stage / 'referee' / 'PROTOCOL.md').write_text(proto, encoding='utf-8')
    shutil.copyfile(REV / 'sample.txt', stage / 'referee' / 'sample.txt')
    zp = Path(args.zip)
    base = str(zp.with_suffix('')) if zp.suffix == '.zip' else str(zp)
    shutil.make_archive(base, 'zip', root_dir=stage, base_dir='referee')
    shutil.rmtree(stage)
    print('zip:', base + '.zip')
