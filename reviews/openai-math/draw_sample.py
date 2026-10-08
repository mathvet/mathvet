#!/usr/bin/env python3
"""Freeze the referee sample for the openai/math review (PROTOCOL.md).

Sample of 40 families, drawn before any family is re-read:
  * the 12 families whose repository scope notes already document a divergence between headline and Lean
    (197, 261, 266, 281, 247, 262, 207, 267, 307, 157, 159, 365), taken with certainty;
  * 14 drawn by a seeded random draw from the other 79 non-`full` families;
  * 14 drawn by a seeded random draw from the 144 `full` families.
Seed: the reviewed upstream commit hash as a string (Python's random.Random(str) is deterministic across platforms).
Output: sample.txt (40 family ids, sorted, one per line) and sample.sha256. Rerun to verify; the files must not change.
"""
import hashlib, json, random
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCUMENTED = ['197', '261', '266', '281', '247', '262', '207', '267', '307', '157', '159', '365']
index = json.load(open(HERE / 'source' / 'index.json', encoding='utf-8'))
seed = index['commit']
verdict = {}
for p in sorted((HERE / 'source').glob('lean_scope_audit_part*.json')):
    for r in json.load(open(p, encoding='utf-8')):
        verdict[r['family']] = r['headline_formalized']
assert len(verdict) == 235 and all(d in verdict and verdict[d] != 'full' for d in DOCUMENTED)
other_nonfull = sorted(f for f, v in verdict.items() if v != 'full' and f not in DOCUMENTED)
full = sorted(f for f, v in verdict.items() if v == 'full')
assert len(other_nonfull) == 79 and len(full) == 144, (len(other_nonfull), len(full))
rng = random.Random(seed)
drawn_nonfull = rng.sample(other_nonfull, 14)
drawn_full = rng.sample(full, 14)
sample = sorted(DOCUMENTED + drawn_nonfull + drawn_full)
assert len(set(sample)) == 40
text = '\n'.join(sample) + '\n'
out = HERE / 'sample.txt'
if out.exists() and out.read_text() != text:
    raise SystemExit('sample.txt already exists and differs: the frozen sample must not change')
out.write_text(text)
digest = hashlib.sha256(text.encode()).hexdigest()
(HERE / 'sample.sha256').write_text(f'{digest}  sample.txt\n')
print('seed', seed)
print('documented', DOCUMENTED)
print('drawn non-full', sorted(drawn_nonfull))
print('drawn full', sorted(drawn_full))
print('sha256', digest)
