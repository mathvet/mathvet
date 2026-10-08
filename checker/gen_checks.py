#!/usr/bin/env python3
"""Generate challenge-side and solution-side Lean check files for a Comparator challenge.
Prints: `#check @thm` (type only) for theorems, `#print` for every def/abbrev/structure/inductive declared in the
challenge file (fully qualified via namespace tracking), and `#print axioms` on the solution side."""
import re, sys, json
import os; L=os.environ.get('OPENAI_MATH_LEAN') or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'upstream','openai-math','lean')
C=sys.argv[1]
j=json.load(open(f'{L}/ComparatorChallenges/{C}.json'))
src=open(f'{L}/ComparatorChallenges/{C}.lean',encoding='utf-8').read()
ns=[]; decls=[]
for line in src.splitlines():
    m=re.match(r'^\s*namespace\s+([\w.«»]+)',line)
    if m: ns.append(m.group(1)); continue
    m=re.match(r'^\s*end\s+([\w.«»]+)',line)
    if m and ns and ns[-1]==m.group(1): ns.pop(); continue
    m=re.match(r'^\s*(?:private\s+|protected\s+|noncomputable\s+|@\[[^\]]*\]\s*)*(?:def|abbrev|structure|inductive|class|theorem|lemma)\s+([\w.«»]+)',line)
    if m:
        name=m.group(1).rstrip('.')
        full=name[len('_root_.'):] if name.startswith('_root_.') else ('.'.join(ns+[name]) if ns else name)
        kind='thm' if re.search(r'\b(theorem|lemma)\b',line) else 'def'
        decls.append((kind,full))
thms=[d for k,d in decls if k=='thm']; defs=[d for k,d in decls if k=='def']
# sanity: json theorem names should be among thms
missing=[t for t in j['theorem_names'] if t not in thms]
ch=[src,'']
so=[f"import {j['solution_module']}",'']
for t in j['theorem_names']:
    ch.append(f'#check @{t}'); so.append(f'#check @{t}'); so.append(f'#print axioms {t}')
for d in defs:
    ch.append(f'#print {d}'); so.append(f'#print {d}')
open(f'{L}/Scratch/Challenge_{C}.lean','w').write('\n'.join(ch)+'\n')
open(f'{L}/Scratch/Solution_{C}.lean','w').write('\n'.join(so)+'\n')
print(json.dumps(dict(theorems=thms, defs=defs, json_theorems=j['theorem_names'], missing_from_parse=missing)))
