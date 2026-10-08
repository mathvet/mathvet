#!/usr/bin/env python3
"""Generate Scratch/Cmp_<C>.lean: re-elaborate the challenge under namespace `Chal` inside the solution environment,
then compare, Comparator-style, every Chal.* constant in the transitive closure of the challenge theorems against the
same-named OAI.* constant: alpha-equivalence of types (and of values for definitions, constructor types for inductives)
after renaming the Chal prefix. Also prints axioms of each theorem."""
import re, sys, json
import os; L=os.environ.get('OPENAI_MATH_LEAN') or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'upstream','openai-math','lean')
C=sys.argv[1]
j=json.load(open(f'{L}/ComparatorChallenges/{C}.json'))
src=open(f'{L}/ComparatorChallenges/{C}.lean',encoding='utf-8').read()
body=re.sub(r'^import .*$','',src,flags=re.M).replace('namespace OAI','namespace Chal').replace('end OAI','end Chal')
body=re.sub(r'\bOAI\.','Chal.',body)
thms=' '.join(t.replace('OAI.','Chal.',1) for t in j['theorem_names'])
meta=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'CmpLib.lean'),encoding='utf-8').read().replace('import Lean','')+'\nopen CmpLib\n'
# SHADOWCHECK: fully qualified Chal decl names (namespace tracking), printed in the solution env for diffing against the Mathlib-only print
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
        decls.append((kind, full.replace('OAI.','Chal.',1) if full.startswith('OAI.') else 'Chal.'+full))
out=[f"import {j['solution_module']}", "import Lean", meta, body, "", f"#cmp_closure {thms}"]
out.append("-- SHADOWCHECK prints")
for t in j['theorem_names']: out.append(f"#check @{t.replace('OAI.','Chal.',1)}")
for k,d in decls:
    if k!='thm': out.append(f"#print {d}")
for t in j['theorem_names']: out.append(f"#print axioms {t}")
open(f'{L}/Scratch/Cmp_{C}.lean','w').write('\n'.join(out)+'\n')
print('ok')
