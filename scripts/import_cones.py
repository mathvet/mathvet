#!/usr/bin/env python3
"""For each Comparator challenge, compute the transitive import cone of its solution module within lean/OAI
(external packages counted separately) and flag cones containing custom-axiom files."""
import os, re, json, collections
ROOT='/Users/shannon/cc/math/math/lean'
imports={}; lines={}
for dp,_,fs in os.walk(f'{ROOT}/OAI'):
    for fn in fs:
        if fn.endswith('.lean'):
            p=os.path.join(dp,fn); mod=os.path.relpath(p,ROOT)[:-5].replace('/','.')
            t=open(p,encoding='utf-8',errors='ignore').read()
            imports[mod]=re.findall(r'^import\s+([\w.«»]+)',t,re.M)
            lines[mod]=t.count('\n')
axiom_files=set()
for mod in imports:
    p=f'{ROOT}/'+mod.replace('.','/')+'.lean'
    if re.search(r'^\s*axiom\s',open(p,encoding='utf-8',errors='ignore').read(),re.M): axiom_files.add(mod)
def cone(start):
    seen=set(); ext=set(); st=[start]
    while st:
        m=st.pop()
        if m in seen: continue
        if m not in imports:
            ext.add(m.split('.')[0]); continue
        seen.add(m); st.extend(imports[m])
    return seen, ext
out={}
for f in os.listdir(f'{ROOT}/ComparatorChallenges'):
    if f.endswith('.json'):
        j=json.load(open(f'{ROOT}/ComparatorChallenges/{f}'))
        sol=j['solution_module']; c,ext=cone(sol)
        out[f[:-5]]=dict(solution_module=sol, oai_files=len(c), oai_lines=sum(lines.get(m,0) for m in c),
                         external=sorted(ext), axiom_files=sorted(c&axiom_files), missing=sol not in imports)
json.dump(out,open('/Users/shannon/cc/math/tmp/import_cones.json','w'),indent=1)
print('challenges',len(out))
print('missing solution modules:',[k for k,v in out.items() if v['missing']])
print('cones with axiom files:',{k:v['axiom_files'] for k,v in out.items() if v['axiom_files']})
sm=sorted(out.items(), key=lambda kv: kv[1]['oai_lines'])
print('smallest 25:'); [print(f"  {k:40s} files={v['oai_files']:5d} lines={v['oai_lines']:8d} ext={','.join(x for x in v['external'] if x!='Mathlib')}") for k,v in sm[:25]]
print('largest 15:'); [print(f"  {k:40s} files={v['oai_files']:5d} lines={v['oai_lines']:8d} ext={','.join(x for x in v['external'] if x!='Mathlib')}") for k,v in sm[-15:]]
ec=collections.Counter(x for v in out.values() for x in v['external'])
print('external package usage:',ec.most_common())
