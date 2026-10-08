#!/usr/bin/env python3
"""First-pass audit of lean/docs scope notes: does the Lean cover the family's headline claim?
Flags hedging phrases; a subagent/human confirms the flagged ones."""
import os, re, json
ROOT='/Users/shannon/cc/math/math'
idx=json.load(open('/Users/shannon/cc/math/index.json'))
PH=[r'does not assert', r'not asserted', r'is not asserted', r'outside (?:this|the) selected statement', r'outside the result',
    r'not included', r'are not included', r'is not included', r'supporting', r'selected statement', r'special case',
    r'not formalized', r'does not include', r'not part of', r'only', r'excluded', r'without', r'weaker', r'partial',
    r'no explicit', r'not explicit', r'ineffective', r'not computable', r'noncomputable', r'oracle', r'assum']
rows={}
for f in sorted(os.listdir(f'{ROOT}/lean/docs')):
    num=f[:-3]; t=open(f'{ROOT}/lean/docs/{f}',encoding='utf-8').read()
    scope=t.split('## Scope',1)[1].split('## Comparator',1)[0] if '## Scope' in t else t
    hits={p:len(re.findall(p,scope,re.I)) for p in PH}
    hits={k:v for k,v in hits.items() if v}
    strong=[p for p in hits if p in (r'does not assert',r'not asserted',r'is not asserted',r'outside (?:this|the) selected statement',r'not included',r'are not included',r'is not included',r'supporting',r'not formalized',r'does not include')]
    sents=[s.strip() for s in re.split(r'(?<=[.])\s+',scope) if re.search('|'.join(PH[:12]),s,re.I)]
    fam=idx['families'].get(num,{})
    rows[num]=dict(title=fam.get('title'), n_challenges=len(fam.get('lean_challenges',{})), strong_flags=strong, hits=hits, flagged_sentences=sents[:6])
json.dump(rows,open('/Users/shannon/cc/math/verification/lean_scope_audit_firstpass.json','w'),indent=1,ensure_ascii=False)
strongs=[n for n,r in rows.items() if r['strong_flags']]
print(len(rows),'families with docs;',len(strongs),'with strong hedge phrases:')
for n in strongs: print(n, rows[n]['title'][:60], '|', rows[n]['strong_flags'], '|', (rows[n]['flagged_sentences'][0][:160] if rows[n]['flagged_sentences'] else ''))
