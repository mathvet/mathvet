#!/usr/bin/env python3
"""Build index.json: one row per family and per manuscript from the openai/math clone."""
import re, os, json, subprocess, collections
ROOT = '/Users/shannon/cc/math/math'
src = open(f'{ROOT}/overview.tex', encoding='utf-8').read()

def brace(s, i):
    d = 0; j = i
    while True:
        c = s[j]
        if c == '{': d += 1
        elif c == '}':
            d -= 1
            if d == 0: return s[i+1:j], j+1
        j += 1

pat = re.compile(r'\\cataloguesection\{([^}]*)\}\{(\d+)\}|\\resultentry\{(\d+)\}\{')
families = {}
i = 0; sec = None
while True:
    m = pat.search(src, i)
    if not m: break
    if m.group(1):
        sec = m.group(1); i = m.end(); continue
    num = m.group(3); j = m.end()-1
    title, j = brace(src, j); summ, j = brace(src, j); links, j = brace(src, j)
    dirs = re.findall(r'preprints/([^/]+)/', links)
    xrefs = sorted(set(re.findall(r'result[s]? (\d{3})', summ)))
    families[num] = dict(family=num, subject=sec, title=title, summary=summ, papers=dirs, xrefs=xrefs)
    i = j

# CONTENTS.md: Lean tag per family, manuscripts + abstracts
contents = open(f'{ROOT}/CONTENTS.md', encoding='utf-8').read()
lean_tag = {}
for m in re.finditer(r'\*\*(\d{3})\. (.*?)\*\*(.*?)(?=\n</td>)', contents, re.S):
    lean_tag[m.group(1)] = '([Lean](lean/docs/' in m.group(3)
abstracts = {}
for m in re.finditer(r'&emsp;\[(.*?)\]\(preprints/([^/]+)/[^)]*\)\s*\n\n(.*?)\n\n</td>', contents, re.S):
    abstracts[m.group(2)] = dict(title=m.group(1), abstract=m.group(3).strip())

# lean docs scope text + comparator links
lean_docs = {}
for f in os.listdir(f'{ROOT}/lean/docs'):
    num = f[:-3]
    t = open(f'{ROOT}/lean/docs/{f}', encoding='utf-8').read()
    scope = t.split('## Scope',1)[1].split('## Comparator',1)[0].strip() if '## Scope' in t else ''
    chals = re.findall(r'ComparatorChallenges/([A-Za-z0-9_]+)\.lean', t)
    lean_docs[num] = dict(scope=scope, challenges=sorted(set(chals)))

# comparator challenge metadata
chal = {}
for f in os.listdir(f'{ROOT}/lean/ComparatorChallenges'):
    if f.endswith('.json'):
        j = json.load(open(f'{ROOT}/lean/ComparatorChallenges/{f}'))
        name = f[:-5]
        stmt = open(f'{ROOT}/lean/ComparatorChallenges/{name}.lean', encoding='utf-8').read()
        chal[name] = dict(solution_module=j.get('solution_module'), theorem_names=j.get('theorem_names'),
                          definition_names=j.get('definition_names'), enable_nanoda=j.get('enable_nanoda'),
                          permitted_axioms=j.get('permitted_axioms'), statement_lines=stmt.count('\n'))

# citations: OAI:<key> occurrences per paper dir (tex + bib), excluding self
cite_out = collections.defaultdict(set)
for d in os.listdir(f'{ROOT}/preprints'):
    bd = f'{ROOT}/preprints/{d}/build'
    if not os.path.isdir(bd): continue
    keys = set()
    for dp, _, fs in os.walk(bd):
        for fn in fs:
            if fn.endswith(('.tex', '.bib')):
                try: t = open(os.path.join(dp, fn), encoding='utf-8', errors='ignore').read()
                except Exception: continue
                keys |= set(re.findall(r'OAI:([A-Za-z0-9-]+)', t))
    keys.discard(d)
    cite_out[d] = keys
cite_in = collections.Counter()
for d, ks in cite_out.items():
    for k in ks: cite_in[k] += 1

# shipped code / verification dirs
def shipped(d):
    vd = f'{ROOT}/preprints/{d}/verification'
    if not os.path.isdir(vd): return []
    out = []
    for dp, _, fs in os.walk(vd):
        for fn in fs: out.append(os.path.relpath(os.path.join(dp, fn), f'{ROOT}/preprints/{d}'))
    return sorted(out)

def texlines(d):
    n = 0
    bd = f'{ROOT}/preprints/{d}/build'
    for dp, _, fs in os.walk(bd):
        for fn in fs:
            if fn.endswith('.tex'):
                try: n += sum(1 for _ in open(os.path.join(dp, fn), encoding='utf-8', errors='ignore'))
                except Exception: pass
    return n

paper2family = {}
for num, f in families.items():
    for d in f['papers']: paper2family[d] = num

manuscripts = []
for d in sorted(os.listdir(f'{ROOT}/preprints')):
    if not os.path.isdir(f'{ROOT}/preprints/{d}'): continue
    a = abstracts.get(d, {})
    manuscripts.append(dict(dir=d, family=paper2family.get(d), title=a.get('title'), abstract=a.get('abstract'),
                            cites=sorted(cite_out.get(d, [])), cited_by=cite_in.get(d, 0),
                            shipped_files=shipped(d), tex_lines=texlines(d)))

for num, f in families.items():
    f['lean'] = 'none'
    if num in lean_docs:
        f['lean'] = 'comparator' if lean_docs[num]['challenges'] else 'docs-only'
        f['lean_scope'] = lean_docs[num]['scope']
        f['lean_challenges'] = {c: chal.get(c) for c in lean_docs[num]['challenges']}
    f['cited_by_total'] = sum(cite_in.get(d, 0) for d in f['papers'])
    f['shipped_code'] = any(shipped(d) for d in f['papers'])
    f['tex_lines'] = sum(texlines(d) for d in f['papers'])

json.dump(dict(commit='adc7f1241b42e322a6451854ab7e4b4c146bf78a', families=families, manuscripts=manuscripts, challenges=chal),
          open('/Users/shannon/cc/math/index.json', 'w'), indent=1, ensure_ascii=False)
print('families', len(families), 'manuscripts', len(manuscripts), 'challenges', len(chal))
print('lean status:', collections.Counter(f['lean'] for f in families.values()))
print('unmapped papers:', [m['dir'] for m in manuscripts if m['family'] is None][:20])
print('top cited families:', sorted(((f['cited_by_total'], n) for n, f in families.items()), reverse=True)[:15])
