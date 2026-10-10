#!/usr/bin/env python3
"""Build the referee packet for the frozen 40-family sample (PROTOCOL.md, "The referees").

Per family the referee receives, and this script assembles from the reviewed upstream commit:
  * the overview summary (the headline claim), verbatim;
  * the repository's own scope note lean/docs/NNN.md, verbatim (relative links rewritten to absolute GitHub URLs);
  * every challenge statement linked from that scope note: the .lean file and its Comparator .json, copied alongside;
  * the paper's main theorem at file and line, with the TeX excerpt, as located by the dataset builder (a text heuristic);
and nothing from MathVet: no verdict, no review note, no list of definitions to check. The script checks that nothing from
the review leaked into the packet (the audit's notes must not appear in it) and writes a SHA-256 manifest.

Usage: python3 reviews/openai-math/referee/make_packet.py [--upstream PATH] [--zip OUT.zip]
  PATH: a checkout of github.com/openai/math at the reviewed commit (default: upstream/openai-math in this repository,
  or $MATHVET_UPSTREAM). Outputs: families/NNN/{README.md,*.lean,*.json}, form.csv, manifest.sha256.
"""
import argparse, csv, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REV = HERE.parent
ROOT = REV.parents[1]
UPSTREAM_URL = 'https://github.com/openai/math'

ap = argparse.ArgumentParser()
ap.add_argument('--upstream', default=os.environ.get('MATHVET_UPSTREAM') or str(ROOT / 'upstream' / 'openai-math'))
ap.add_argument('--zip', default=None, help='also write the packet as a zip archive at this path')
args = ap.parse_args()
UP = Path(args.upstream)
if not (UP / 'lean' / 'docs').is_dir():
    sys.exit(f'upstream checkout not found at {UP} (clone {UPSTREAM_URL} there, or pass --upstream)')

index = json.load(open(REV / 'source' / 'index.json', encoding='utf-8'))
COMMIT = index['commit']
head = subprocess.run(['git', '-C', str(UP), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
if head != COMMIT:
    sys.exit(f'{UP} is at {head[:8]}, not at the reviewed commit {COMMIT[:8]}')
fams = index['families']
manuscripts = {m['dir']: m for m in index['manuscripts']}
rows = [json.loads(l) for l in open(ROOT / 'dataset' / 'autoformalization_pairs.jsonl', encoding='utf-8')]
by_ch = {r['challenge']: r for r in rows}
sample = [l.strip() for l in open(REV / 'sample.txt', encoding='utf-8') if l.strip()]
assert len(sample) == 40, len(sample)
digest = hashlib.sha256(''.join(f + '\n' for f in sample).encode()).hexdigest()
assert (REV / 'sample.sha256').read_text().split()[0] == digest, 'sample.txt does not match sample.sha256'

# The review's own text, loaded ONLY to verify afterwards that none of it is in the packet.
review_text = []
for p in sorted((REV / 'source').glob('lean_scope_audit_part*.json')):
    for r in json.load(open(p, encoding='utf-8')):
        if r['family'] in sample:
            review_text.append(('gap_note', r['family'], r['gap_note']))
            for d in r.get('suspicious_defs') or []:
                review_text.append(('suspicious_defs', r['family'], d))


def blob(path, line=None):
    return f'{UPSTREAM_URL}/blob/{COMMIT}/{path}' + (f'#L{line}' if line else '')


def tree(path):
    return f'{UPSTREAM_URL}/tree/{COMMIT}/{path}'


def rewrite_links(md, fam):
    """lean/docs/NNN.md links to ../../preprints/… and ../ComparatorChallenges/…; make them absolute at the reviewed commit."""
    md = re.sub(r'\]\(\.\./\.\./preprints/([^)]+)\)', lambda m: f']({UPSTREAM_URL}/blob/{COMMIT}/preprints/{m.group(1)})', md)
    md = re.sub(r'\]\(\.\./ComparatorChallenges/([^)]+)\)', lambda m: f']({UPSTREAM_URL}/blob/{COMMIT}/lean/ComparatorChallenges/{m.group(1)})', md)
    return md


out_dir = HERE / 'families'
if out_dir.exists():
    shutil.rmtree(out_dir)
out_dir.mkdir()
written = []
for fam in sample:
    fi = fams[fam]
    chs = list(fi['lean_challenges'].keys())
    assert chs, f'family {fam} has no challenges in the index'
    d = out_dir / fam
    d.mkdir()
    scope = (UP / 'lean' / 'docs' / f'{fam}.md').read_text(encoding='utf-8')
    parts = [f'# Family {fam} — {fi["title"]}', '',
             f'Subject: {fi["subject"]}. Reviewed repository: `{UPSTREAM_URL}` at commit `{COMMIT}`. '
             f'Catalogue entry: family {fam} in `overview.pdf` / `CONTENTS.md`.', '',
             '## 1. Headline claim (the overview summary, verbatim)', '', fi['summary'].strip(), '',
             f'## 2. The repository\'s own scope note ([`lean/docs/{fam}.md`]({blob(f"lean/docs/{fam}.md")}), verbatim; relative links made absolute)', '',
             rewrite_links(scope.strip(), fam), '',
             '## 3. Challenge statements (every file linked from the scope note; copies in this folder)', '']
    for c in chs:
        src = UP / 'lean' / 'ComparatorChallenges' / f'{c}.lean'
        cfg = UP / 'lean' / 'ComparatorChallenges' / f'{c}.json'
        shutil.copyfile(src, d / f'{c}.lean')
        shutil.copyfile(cfg, d / f'{c}.json')
        j = json.load(open(cfg, encoding='utf-8'))
        r = by_ch.get(c, {})
        parts += [f'- [`{c}.lean`]({blob(f"lean/ComparatorChallenges/{c}.lean")}) — the lab\'s result label: '
                  f'*{" / ".join(r.get("challenge_result_labels") or []) or "(none)"}*. Comparator config '
                  f'[`{c}.json`]({blob(f"lean/ComparatorChallenges/{c}.json")}): theorem(s) `{"`, `".join(j["theorem_names"])}`'
                  + (f'; definition(s) `{"`, `".join(j["definition_names"])}`' if j.get('definition_names') else '')
                  + f'; permitted axioms {", ".join("`" + a + "`" for a in j["permitted_axioms"])}; '
                  f'solution module `{j["solution_module"]}`.']
    parts += ['', 'The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem '
              'names listed in the config are the ones the Comparator compares.', '',
              '## 4. The paper\'s main theorem (file and line, with the TeX excerpt)', '']
    seen = set()
    for c in chs:
        r = by_ch.get(c, {})
        for i, t in enumerate(r.get('nl_main_theorems') or []):
            key = (t['paper_dir'], t['tex_file'], t['tex_line'])
            if key in seen:
                continue
            seen.add(key)
            title = manuscripts.get(t['paper_dir'], {}).get('title') or t['paper_dir']
            label = f'`{t["env"]}`' + (f' `{t["label"]}`' if t.get('label') else '') + (f' ({t["title"]})' if t.get('title') else '')
            pd, tf, tl = t['paper_dir'], t['tex_file'], t['tex_line']
            pdf_url, tex_url = blob(f'preprints/{pd}/paper.pdf'), blob(f'preprints/{pd}/{tf}', tl)
            parts += [f'**{title}** — [`preprints/{pd}/paper.pdf`]({pdf_url}); {label} at [`{tf}:{tl}`]({tex_url})'
                      + ('' if i == 0 else ' (further candidate)') + ':', '', '```latex', t['tex'].strip(), '```', '']
    parts += ['The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline '
              'refers to, read the paper\'s own statement and say so in your justification.', '']
    papers = [p for p in fi.get('papers', [])]
    if papers:
        parts += ['Papers of this family: ' + '; '.join(f'[{manuscripts.get(p, {}).get("title") or p}]({tree(f"preprints/{p}")})' for p in papers), '']
    parts += ['## 5. Your classification', '',
              f'Enter one line for family `{fam}` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, '
              '`supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, '
              'and the minutes spent.', '']
    (d / 'README.md').write_text('\n'.join(parts), encoding='utf-8')
    written.append(fam)

with open(HERE / 'form.csv', 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    w.writerow(['family', 'class', 'justification', 'minutes'])
    for fam in sample:
        w.writerow([fam, '', '', ''])

# Leak check: nothing from the review may appear in the packet.
packet_text = '\n'.join(p.read_text(encoding='utf-8', errors='replace') for p in sorted(out_dir.rglob('*')) if p.is_file())
norm = lambda s: re.sub(r'\s+', ' ', s).strip().lower()
pt = norm(packet_text)
leaks = []
for kind, fam, text in review_text:
    frag = norm(text)[:80]
    if len(frag) >= 30 and frag in pt:
        leaks.append((kind, fam, frag[:60]))
for word in ('headline_formalized', 'gap_note', 'MathVet verdict', 'fidelity_label', 'pre-referee verdict'):
    if word.lower() in pt:
        leaks.append(('keyword', '-', word))
if leaks:
    sys.exit('REVIEW TEXT LEAKED INTO THE PACKET: ' + '; '.join(map(str, leaks)))

with open(HERE / 'manifest.sha256', 'w', encoding='utf-8') as fh:
    for p in sorted(list(out_dir.rglob('*')) + [HERE / 'form.csv', HERE / 'README.md', HERE / 'score.py']):
        if p.is_file():
            fh.write(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(HERE)}\n')
n_files = sum(1 for p in out_dir.rglob('*') if p.is_file())
print(f'packet: {len(written)} families, {n_files} files, commit {COMMIT[:8]}, no review text found in it')
if args.zip:
    zp = Path(args.zip)
    base = str(zp.with_suffix('')) if zp.suffix == '.zip' else str(zp)
    shutil.make_archive(base, 'zip', root_dir=HERE.parent, base_dir=HERE.name)
    print('zip:', base + '.zip')
