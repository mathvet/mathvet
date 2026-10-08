#!/usr/bin/env python3
"""Build the MathVet review artifacts for one upstream release from the sources committed in this repository.

Inputs (relative to the repository root):
  reviews/<release>/source/index.json                   catalogue of the upstream repository (scripts/build_index.py)
  reviews/<release>/source/lean_scope_audit_part*.json  the family-level fidelity audit: the review's primary record
  dataset/autoformalization_pairs.jsonl                 per-challenge data, including the lab's own lean/docs scope text
  reviews/<release>/evidence/lean_checks/               build / closure-comparison / Comparator logs written by checker/
  EXPLAINER.md, PROTOCOL.md                             prose rendered into the site
Outputs:
  reviews/<release>/fidelity-table.{csv,json}  one row per family (235)
  reviews/<release>/challenge-status.{csv,json} one row per Comparator challenge (405)
  reviews/<release>/formalization-review.yaml  the review in the shape of formalization.yaml v0.4
  reviews/<release>/STATUS.md                  counts and machine-check status
  docs/                                        the static site (GitHub Pages)
Run: python3 scripts/build_review.py [release]   (needs: pip install pyyaml markdown)
"""
import csv, datetime, hashlib, html, json, re, sys
from collections import Counter, OrderedDict
from pathlib import Path

import yaml, markdown

ROOT = Path(__file__).resolve().parents[1]
RELEASE = sys.argv[1] if len(sys.argv) > 1 else 'openai-math'
REV = ROOT / 'reviews' / RELEASE
SRC = REV / 'source'
CHECKS = REV / 'evidence' / 'lean_checks'
CLOUD = REV / 'evidence' / 'cloud'     # sandboxed Linux runs (checker/cloud/)
DATASET = ROOT / 'dataset' / 'autoformalization_pairs.jsonl'
DOCS = ROOT / 'docs'
UPSTREAM = 'https://github.com/openai/math'
CLASSES = ['full', 'partial', 'weaker-statement', 'supporting-only']
SITE = 'https://math.vet'
REPO_URL = 'https://github.com/mathvet/mathvet'
NOW = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)

sys.path.insert(0, str(ROOT / 'scripts'))
from site_templates import layout, CSS, TABLE_PAGE, CHALLENGES_PAGE, KATEX_HEAD  # noqa: E402


def blob(commit, path):
    return f'{UPSTREAM}/blob/{commit}/{path}'


def tree(commit, path):
    return f'{UPSTREAM}/tree/{commit}/{path}'


# ----------------------------------------------------------------------------- inputs
index = json.load(open(SRC / 'index.json', encoding='utf-8'))
COMMIT = index['commit']
fam_index, ch_index = index['families'], index['challenges']
manuscripts = {m['dir']: m for m in index['manuscripts']}
for m in manuscripts.values():  # upstream CONTENTS.md writes inline math as $`...`$; normalise to $...$
    if m.get('title'):
        m['title'] = re.sub(r'\$`(.*?)`\$', r'$\1$', m['title']).strip()

audit = OrderedDict()
for p in sorted(SRC.glob('lean_scope_audit_part*.json')):
    part = int(re.search(r'part(\d)', p.name).group(1))
    for r in json.load(open(p, encoding='utf-8')):
        r['audit_part'] = part
        audit[r['family']] = r
audit = OrderedDict(sorted(audit.items()))
assert len(audit) == 235, len(audit)

rows = [json.loads(l) for l in open(DATASET, encoding='utf-8')]
by_ch = {r['challenge']: r for r in rows}
assert len(by_ch) == 405, len(by_ch)


# ----------------------------------------------------------------------------- machine-check logs
def scan_checks(name):
    d = dict(build='none', build_seconds=None, closure='none', closure_constants=None, closure_problems=None,
             closure_errors=None, shadowing=None, axioms=None, comparator='none', comparator_finished=None,
             evidence_files=[])
    log = CHECKS / f'{name}.log'
    if log.exists():
        d['evidence_files'].append(log.name)
        t = log.read_text(errors='replace')
        m = re.search(r'^== build rc=(\d+) seconds=(\d+)', t, re.M)
        if m:
            d['build'] = 'built' if m.group(1) == '0' else 'failed'
            d['build_seconds'] = int(m.group(2))
        elif 'Build completed successfully' in t or re.search(r'^AXIOMS:', t, re.M):
            d['build'] = 'built'
        elif 'BUILD FAILED' in t or re.search(r'^error:', t, re.M):
            d['build'] = 'failed'
        else:
            d['build'] = 'incomplete'
    cmp = CHECKS / f'{name}.cmp.txt'
    if cmp.exists():
        d['evidence_files'].append(cmp.name)
        t = cmp.read_text(errors='replace')
        ms = re.findall(r'comparator-style: ok=(\d+) problems=(\d+) errors=(\d+) \| (\S+) \|', t)
        if ms:
            ok, pb, er, sh = ms[-1]
            d.update(closure_constants=int(ok), closure_problems=int(pb), closure_errors=int(er), shadowing=sh)
            d['closure'] = 'ok' if int(pb) == 0 and int(er) == 0 and int(ok) > 0 else 'problems'
            ax = set()
            for m in re.finditer(r'depends on axioms:\s*\[(.*?)\]', t, re.S):
                ax.update(a.strip() for a in m.group(1).replace('\n', ' ').split(',') if a.strip())
            d['axioms'] = sorted(ax)
        elif re.search(r'error', t):
            d['closure'] = 'error'
    comp = CHECKS / f'{name}.comparator.txt'
    if comp.exists():
        d['evidence_files'].append(comp.name)
        t = comp.read_text(errors='replace')
        if 'Your solution is okay!' in t:
            d['comparator'] = 'pass'
        elif re.search(r'== comparator exit=\d+', t) or 'exited with code' in t:
            d['comparator'] = 'fail'
        else:
            d['comparator'] = 'running'
        m = re.search(r'== comparator exit=\d+ end (\S+)', t)
        d['comparator_finished'] = m.group(1) if m else (
            datetime.datetime.fromtimestamp(comp.stat().st_mtime, datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
            if d['comparator'] != 'running' else None)
    for ext in ('challenge.txt', 'solution.txt'):
        if (CHECKS / f'{name}.{ext}').exists():
            d['evidence_files'].append(f'{name}.{ext}')
    d.update(cloud_comparator='none', cloud_sandbox=None, cloud_finished=None, cloud_build=None, cloud_closure=None, cloud_files=[])
    cc = CLOUD / f'{name}.comparator.txt'
    if cc.exists():
        t = cc.read_text(errors='replace')
        d['cloud_files'].append(cc.name)
        if 'Your solution is okay!' in t: d['cloud_comparator'] = 'pass'
        elif 'executable file not found' in t and 'nanoda' in t: d['cloud_comparator'] = 'incomplete'   # the challenge asks for the external nanoda kernel, which the VM lacks; Lean's kernel accepted
        elif re.search(r'== comparator exit=\d+', t): d['cloud_comparator'] = 'fail'
        else: d['cloud_comparator'] = 'running'
        m = re.search(r'^sandbox: (.*)$', t, re.M)
        d['cloud_sandbox'] = m.group(1).strip() if m else None
        m = re.search(r'== comparator exit=\d+ end (\S+)', t)
        d['cloud_finished'] = m.group(1) if m else None
    for ext, key in (('log', 'cloud_build'), ('cmp.txt', 'cloud_closure')):
        f = CLOUD / f'{name}.{ext}'
        if f.exists():
            d['cloud_files'].append(f.name)
            tt = f.read_text(errors='replace')
            if key == 'cloud_build':
                d[key] = 'built' if re.search(r'^== build rc=0', tt, re.M) else 'incomplete'
            else:
                ms = re.findall(r'comparator-style: ok=(\d+) problems=(\d+) errors=(\d+)', tt)
                d[key] = ('ok' if ms and ms[-1][1] == '0' and ms[-1][2] == '0' else 'problems') if ms else 'error'
    return d


def machine_level(ch):
    if ch['cloud_comparator'] == 'pass' and ch['cloud_sandbox'] and 'landrun=real' in ch['cloud_sandbox']:
        return 'comparator-sandboxed-pass'
    if ch['comparator'] == 'pass' or ch['cloud_comparator'] == 'pass':
        return 'comparator-pass'
    if ch['closure'] == 'ok' and ch['build'] == 'built':
        return 'closure-pass'
    if ch['build'] == 'built':
        return 'built'
    if ch['build'] in ('incomplete',):
        return 'build-in-progress'
    if ch['build'] == 'failed':
        return 'build-failed'
    return 'none'


# ----------------------------------------------------------------------------- per-challenge and per-family records
challenges = OrderedDict()
for name in sorted(by_ch):
    r = by_ch[name]
    cfg = ch_index[name]
    chk = scan_checks(name)
    main = (r['nl_main_theorems'] or [None])[0]
    paper = main['paper_dir'] if main else r['nl_primary_paper']
    challenges[name] = OrderedDict([
        ('challenge', name), ('family', r['family']), ('family_verdict', r['fidelity_label']),
        ('result_label', ' / '.join(r['challenge_result_labels'])),
        ('theorem_names', r['theorem_names']), ('definition_names', r['definition_names']),
        ('solution_module', r['solution_module']), ('solution_file', r['solution_file']),
        ('cone_oai_lines', r['cone_oai_lines']), ('cone_external', [e for e in r['cone_external'] if e not in ('Lean', 'Mathlib', 'Std', 'Init', 'all')]),
        ('permitted_axioms', cfg['permitted_axioms']), ('enable_nanoda', cfg.get('enable_nanoda')),
        ('paper_dir', paper), ('paper_title', manuscripts.get(paper, {}).get('title', '')),
        ('paper_theorem', (f"{main['env']} {main['label'] or ''}".strip() + f" ({main['tex_file']}:{main['tex_line']})") if main else ''),
        ('paper_url', tree(COMMIT, f'preprints/{paper}') if paper else ''),
        ('lean_url', blob(COMMIT, r['lean_file'])), ('config_url', blob(COMMIT, r['config_file'])),
        ('lean_sha256', r['lean_sha256']),
        ('machine_check', machine_level(chk)),
    ] + list(chk.items()))

families = OrderedDict()
for fam, a in audit.items():
    fi = fam_index[fam]
    chs = [challenges[c] for c in a['challenges']]
    scope = by_ch[a['challenges'][0]]['family_scope']
    papers = []
    for c in a['challenges']:
        for p in by_ch[c]['nl_papers']:
            if p.get('lean_linked') and p['dir'] not in [q['dir'] for q in papers]:
                papers.append(dict(dir=p['dir'], title=p['title'], url=tree(COMMIT, f"preprints/{p['dir']}")))
    levels = [c['machine_check'] for c in chs]
    best = ('comparator-sandboxed-pass' if 'comparator-sandboxed-pass' in levels else 'comparator-pass' if 'comparator-pass' in levels else 'closure-pass' if 'closure-pass' in levels
            else 'built' if 'built' in levels else 'build-in-progress' if 'build-in-progress' in levels else 'none')
    families[fam] = OrderedDict([
        ('family', fam), ('title', fi['title']), ('subject', fi['subject']), ('headline', fi['summary']),
        ('verdict', a['headline_formalized']), ('challenges', a['challenges']),
        ('review_note', a['gap_note']), ('definitions_to_check', a['suspicious_defs']),
        ('external_packages', sorted({e for c in chs for e in c['cone_external']})),
        ('cone_lines_max', max(c['cone_oai_lines'] for c in chs)),
        ('machine_check', best),
        ('lab_scope_note', scope), ('lab_docs_url', blob(COMMIT, f'lean/docs/{fam}.md')),
        ('overview_entry', f'family {fam} in overview.pdf / CONTENTS.md'),
        ('papers', papers), ('audit_part', a['audit_part']),
        ('second_reader', ''), ('referee_verdict', ''),
    ])

counts = Counter(f['verdict'] for f in families.values())
n_lean = len(families)
n_total = len(fam_index)
n_none = n_total - n_lean
built = [c for c in challenges.values() if c['build'] == 'built']
closure_ok = [c for c in challenges.values() if c['closure'] == 'ok' and c['build'] == 'built']
comp_pass = [c for c in challenges.values() if c['comparator'] == 'pass' or c['cloud_comparator'] == 'pass']
sandboxed = [c for c in challenges.values() if c['machine_check'] == 'comparator-sandboxed-pass']
comp_running = [c for c in challenges.values() if c['comparator'] == 'running']
build_running = [c for c in challenges.values() if c['build'] == 'incomplete']
status = OrderedDict([
    ('release', RELEASE), ('upstream_repo', UPSTREAM), ('upstream_commit', COMMIT),
    ('generated', NOW.isoformat().replace('+00:00', 'Z')),
    ('review_status', 'independent third-party review, pre-referee'),
    ('families_total', n_total), ('families_with_lean', n_lean), ('families_without_lean', n_none),
    ('challenges', len(challenges)),
    ('verdicts', OrderedDict((k, counts[k]) for k in CLASSES)),
    ('non_full', sum(counts[k] for k in CLASSES[1:])),
    ('built_locally', [c['challenge'] for c in built]),
    ('closure_check_pass', [c['challenge'] for c in closure_ok]),
    ('comparator_pass', [c['challenge'] for c in comp_pass]),
    ('comparator_sandboxed_pass', [c['challenge'] for c in sandboxed]),
    ('comparator_running', [c['challenge'] for c in comp_running]),
    ('build_in_progress', [c['challenge'] for c in build_running]),
])

# ----------------------------------------------------------------------------- tables
REV.mkdir(parents=True, exist_ok=True)
json.dump(dict(status=status, families=list(families.values())), open(REV / 'fidelity-table.json', 'w', encoding='utf-8'),
          indent=1, ensure_ascii=False)
with open(REV / 'fidelity-table.csv', 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    cols = ['family', 'title', 'subject', 'verdict', 'challenges', 'machine_check', 'external_packages', 'cone_lines_max',
            'review_note', 'definitions_to_check', 'lab_scope_note', 'lab_docs_url', 'audit_part', 'second_reader', 'referee_verdict']
    w.writerow(cols)
    for f in families.values():
        w.writerow([f[c] if not isinstance(f[c], list) else ' ; '.join(map(str, f[c])) for c in cols])
json.dump(dict(status=status, challenges=list(challenges.values())), open(REV / 'challenge-status.json', 'w', encoding='utf-8'),
          indent=1, ensure_ascii=False)
with open(REV / 'challenge-status.csv', 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh)
    cols = ['challenge', 'family', 'family_verdict', 'result_label', 'theorem_names', 'solution_module', 'cone_oai_lines',
            'cone_external', 'machine_check', 'build', 'build_seconds', 'closure', 'closure_constants', 'closure_problems',
            'shadowing', 'axioms', 'comparator', 'comparator_finished', 'cloud_comparator', 'cloud_sandbox', 'cloud_finished',
            'paper_theorem', 'lean_url', 'evidence_files', 'cloud_files']
    w.writerow(cols)
    for c in challenges.values():
        w.writerow([c[k] if not isinstance(c[k], list) else ' ; '.join(map(str, c[k])) for k in cols])


# ----------------------------------------------------------------------------- formalization-review.yaml (v0.4 shape)
class Lit(str):
    pass


def lit_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')


yaml.add_representer(Lit, lit_representer)


def str_representer(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


yaml.add_representer(str, str_representer)
yaml.add_representer(OrderedDict, lambda d, data: d.represent_dict(data.items()))


def nice(s):
    return re.sub(r'[ \t]+', ' ', s).strip()


sources, seen = [], set()
for c in challenges.values():
    if c['paper_dir'] and c['paper_dir'] not in seen:
        seen.add(c['paper_dir'])
        sources.append(OrderedDict([
            ('title', c['paper_title'] or c['paper_dir']), ('authors', ['OpenAI']),
            ('id', c['paper_url']), ('type', 'article'),
            ('location', c['paper_theorem']), ('relationship', 'formalizes'),
            ('note', f"family {c['family']}; main theorem located by MathVet (see dataset/README.md)"),
            ('license', 'Apache-2.0'),
        ]))

div_lines = []
for f in families.values():
    if f['verdict'] != 'full':
        div_lines.append(f"{f['family']} ({f['verdict']}) {f['title']}: {nice(f['review_note'])}")
divergences = ('MathVet reading, pre-referee, one entry per family whose Lean statements do not state the family headline '
               'in full (class in parentheses: partial | weaker-statement | supporting-only). The lab\'s own scope note '
               'for each family is lean/docs/NNN.md at the reviewed commit and is quoted verbatim in fidelity-table.json '
               '(field lab_scope_note).\n' + '\n'.join(div_lines) + '\n')

alignment = []
for f in families.values():
    for cn in f['challenges']:
        c = challenges[cn]
        check = {'comparator-sandboxed-pass': 'real Comparator with its landrun (Landlock) sandbox accepted the solution on an isolated Linux VM',
                 'comparator-pass': 'real Comparator accepted the solution on the reviewer\'s machine',
                 'closure-pass': 'solution built locally; closure comparison, shadowing check and axiom check clean',
                 'built': 'solution built locally', 'build-in-progress': 'local build in progress',
                 'build-failed': 'local build failed (see evidence)', 'none': 'not built by the reviewer'}[c['machine_check']]
        alignment.append(OrderedDict([
            ('source', f"family {f['family']} — {f['title']}: {c['result_label'] or cn} (the lab's own result label); "
                       f"paper '{c['paper_title']}', {c['paper_theorem']}"),
            ('lean', ', '.join(c['theorem_names'] + c['definition_names'])),
            ('module', c['solution_module']),
            ('status', 'proved'),
            ('note', f"proof status per the lab's Comparator configuration {c['config_url']}; MathVet machine check: {check}. "
                     f"Family verdict (pre-referee): {f['verdict']}."),
        ]))
    if f['verdict'] != 'full':
        alignment.append(OrderedDict([
            ('source', f"family {f['family']} — headline claim as stated in the overview: {nice(f['headline'])}"),
            ('lean', ''), ('module', ''),
            ('status', 'partially-formalized' if f['verdict'] == 'partial' else 'not-formalized'),
            ('note', f"MathVet class {f['verdict']} (pre-referee): {nice(f['review_note'])}"),
        ]))

review_doc = OrderedDict([
    ('version', 'v0.4'),
    ('project', OrderedDict([
        ('name', f'MathVet review of openai/math @ {COMMIT[:8]}'),
        ('description', 'Independent third-party review of whether the 405 Comparator challenge statements in openai/math '
                        'state the headline claims of their 235 result families, in the fields of the formalization.yaml '
                        'standard. The formalization itself is OpenAI\'s; this file records the review and the reviewer\'s '
                        'own machine checks. Every verdict is pre-referee until the referee round described in PROTOCOL.md '
                        'has been published.'),
        ('authors', ['MathVet (math.vet)']),
        ('responsible_maintainers', ['MathVet maintainer, github.com/mathvet']),
        ('license', 'Apache-2.0'),
    ])),
    ('repository', OrderedDict([
        ('role', 'thin-wrapper'),
        ('substantive_formalization', OrderedDict([('id', UPSTREAM), ('revision', COMMIT)])),
    ])),
    ('sources', sources),
    ('related_formalizations', [OrderedDict([('id', UPSTREAM), ('relationship', 'other'), ('note', 'the reviewed formalization')])]),
    ('status', OrderedDict([
        ('scope', f"Review coverage: all {n_lean} families of {UPSTREAM} that have a lean/docs page and all {len(challenges)} "
                  f"Comparator challenges at commit {COMMIT}; {n_none} families have no Lean and are out of scope. "
                  f"Verdicts: full {counts['full']}, partial {counts['partial']}, weaker-statement {counts['weaker-statement']}, "
                  f"supporting-only {counts['supporting-only']}. Reviewer's machine checks: {len(built)} solutions built locally, "
                  f"{len(closure_ok)} with a clean closure comparison and standard axioms, {len(comp_pass)} accepted by the real "
                  f"Comparator, of which {len(sandboxed)} on an isolated Linux VM with the real landrun (Landlock) sandbox. "
                  f"This repository proves nothing itself."),
    ])),
    ('automation', OrderedDict([
        ('methods', [OrderedDict([
            ('method', 'agent'),
            ('models', ['Claude (Anthropic) models run in Claude Code, 2026-10-06 to 2026-10-07']),
            ('framework', 'Claude Code'),
            ('tool_setup', 'One agent pass per family reading the overview summary, lean/docs/NNN.md, every linked '
                           'ComparatorChallenges/*.lean statement and the definitions it depends on; the verdict policy is '
                           'fixed in advance (PROTOCOL.md); output validated mechanically against the catalogue (titles, '
                           'challenge sets, cones). The maintainer re-read six families by hand and rebuilt the listed '
                           'challenges with the checker in checker/.'),
            ('cost', OrderedDict([('wall_time', 'about one day'), ('spend_usd', 'subscription-based usage'),
                                  ('hardware', 'one M1 laptop, 16 GB')])),
        ])]),
        ('notes', 'No second human reader yet; the labels are one model-assisted pass. The referee protocol that measures '
                  'their error rate is pre-registered in PROTOCOL.md.'),
    ])),
    ('fidelity', OrderedDict([('divergences', divergences)])),
    ('review', OrderedDict([
        ('status', 'independent third-party review — pre-referee'),
        ('reviewers', ['MathVet (github.com/mathvet); no author of the reviewed formalization took part']),
        ('notes', 'Statement fidelity only: whether each Comparator challenge statement states its family\'s headline claim. '
                  'Proof correctness is left to Lean/Comparator; the truth of unformalized claims is not assessed. '
                  f'Published {NOW.date().isoformat()}. Error-rate protocol: 40 families (12 documented divergences with '
                  'certainty, 14 drawn from the other non-full families, 14 drawn from the full families; seeded draw, '
                  'sample.txt and its SHA-256 committed before any re-reading), two named referees who read Lean classify '
                  'independently under the same rubric, a third adjudicates; the stratum-weighted error rate with its 80% '
                  'Wilson interval is published whatever it is (target 2026-10-29). Lines fixed in advance: PASS at or below '
                  '0.10, KILL at or above 0.20, RETEST in between (+20 families). See PROTOCOL.md.'),
    ])),
    ('alignment', OrderedDict([('namespace', 'OAI'), ('statements', alignment)])),
    ('mathvet', OrderedDict([
        ('schema', 1), ('site', SITE), ('repository', REPO_URL), ('status', status),
        ('verdict_scale', OrderedDict([
            ('full', 'the Comparator statement(s) state the family headline faithfully'),
            ('partial', 'only a special case, or only one of several co-equal headline claims'),
            ('weaker-statement', 'a nontrivially weaker statement than the headline'),
            ('supporting-only', 'a lemma or auxiliary statement, not the headline'),
            ('none', 'nothing in the summary is covered (defined, unused)'),
        ])),
        ('families', [OrderedDict([(k, f[k]) for k in ('family', 'title', 'subject', 'verdict', 'challenges', 'review_note',
                                                          'definitions_to_check', 'external_packages', 'cone_lines_max',
                                                          'machine_check', 'lab_docs_url', 'audit_part')])
                      for f in families.values()]),
    ])),
    ('acknowledgements', 'The reviewed formalization, manuscripts and scope notes are OpenAI\'s (Apache-2.0). Thanks to the '
                         'authors of Lean, Mathlib, Lake, Comparator and lean4export, and to the Mathlib Initiative for the '
                         'formalization.yaml standard whose fields this file fills.'),
])
header = f"""# yaml-language-server: $schema=https://raw.githubusercontent.com/mathlib-initiative/formalization.yaml/main/schema/formalization.schema.json
# MathVet review of {UPSTREAM} at commit {COMMIT}, generated {status['generated']} by scripts/build_review.py.
# This file uses the formalization.yaml v0.4 standard as a review layer: `repository` points at the reviewed formalization,
# `alignment.statements` lists every Comparator challenge (status `proved`, per the lab's configuration) and, for every
# family whose Lean does not state the headline in full, the headline itself (status `not-formalized` or
# `partially-formalized`); `fidelity.divergences` carries the reviewer's reading; `review` records who reviewed and how.
# Everything is pre-referee. Extra keys under `mathvet` are permitted by the standard (readers tolerate unknown keys).
"""
with open(REV / 'formalization-review.yaml', 'w', encoding='utf-8') as fh:
    fh.write(header)
    yaml.dump(review_doc, fh, allow_unicode=True, sort_keys=False, width=110, default_flow_style=False)


# ----------------------------------------------------------------------------- STATUS.md
def md_list(xs):
    return ', '.join(f'`{x}`' for x in xs) if xs else 'none'


status_md = f"""# Status — review of openai/math @ `{COMMIT[:8]}`

Generated {status['generated']} by `scripts/build_review.py`. Review status: **independent third-party review, pre-referee**.

| | families |
|---|---|
| in the release | {n_total} |
| with Lean (lean/docs page + Comparator challenges) | {n_lean} |
| `full` — Lean states the headline claim | {counts['full']} |
| `partial` — one of several claims, or a special case | {counts['partial']} |
| `weaker-statement` — a nontrivially weaker statement | {counts['weaker-statement']} |
| `supporting-only` — a lemma or auxiliary statement | {counts['supporting-only']} |
| without Lean | {n_none} |

Comparator challenges: {len(challenges)}.

## Machine checks on the reviewer's machine (M1 laptop)
- Solutions built: {len(built)} — {md_list(status['built_locally'])}
- Closure comparison + shadowing + axiom check clean: {len(closure_ok)} — {md_list(status['closure_check_pass'])}
- Real Comparator accepted: {len(comp_pass)} — {md_list(status['comparator_pass'])}
- Of these, accepted **with the real landrun (Landlock) sandbox on an isolated Linux VM** (`evidence/cloud/`): {len(sandboxed)} — {md_list(status['comparator_sandboxed_pass'])}
- Comparator running: {md_list(status['comparator_running'])}; build in progress: {md_list(status['build_in_progress'])}

Logs: `evidence/lean_checks/<Challenge>.log` (build), `.cmp.txt` (closure comparison), `.comparator.txt` (Comparator, laptop, development landrun shim); `evidence/cloud/<Challenge>.*` the same three from the sandboxed cloud runs (each `.comparator.txt` starts with a provenance header naming the machine, the sandbox and the session URL).
"""
(REV / 'STATUS.md').write_text(status_md, encoding='utf-8')


# ----------------------------------------------------------------------------- site
SITE_LIVE = 'https://mathvet.github.io/mathvet/'   # absolute site links in the Markdown become root-relative in the site


def md(text):
    out = markdown.markdown(text, extensions=['tables', 'fenced_code', 'toc', 'sane_lists', 'attr_list'])
    return out.replace('href="' + SITE_LIVE, 'href="')


DOCS.mkdir(exist_ok=True)
(DOCS / RELEASE).mkdir(exist_ok=True)
(DOCS / 'style.css').write_text(CSS, encoding='utf-8')
(DOCS / '.nojekyll').write_text('', encoding='utf-8')

explainer = (ROOT / 'EXPLAINER.md').read_text(encoding='utf-8')
protocol = (ROOT / 'PROTOCOL.md').read_text(encoding='utf-8')
tiles = f"""
<section class="tiles" aria-label="headline numbers">
  <div class="tile"><div class="n">{n_total}</div><div class="l">result families in the release</div></div>
  <div class="tile"><div class="n">{n_lean}</div><div class="l">families with Lean</div></div>
  <div class="tile full"><div class="n">{counts['full']}</div><div class="l">Lean states the headline in full</div></div>
  <div class="tile narrower"><div class="n">{status['non_full']}</div><div class="l">Lean states something narrower<br><small>{counts['partial']} partial · {counts['weaker-statement']} weaker · {counts['supporting-only']} supporting-only</small></div></div>
  <div class="tile none"><div class="n">{n_none}</div><div class="l">no Lean at all</div></div>
  <div class="tile"><div class="n">{len(comp_pass)}<span class="of">/{len(closure_ok)}</span></div><div class="l">Comparator accepted / closure-checked by us<br><small>{len(sandboxed)} sandboxed on an isolated Linux VM</small></div></div>
</section>
<p class="status-line">Review status: <strong>pre-referee</strong>. Upstream commit <code>{COMMIT[:8]}</code>. Generated {status['generated']}. <a href="{RELEASE}/">Open the table →</a></p>
"""
body = tiles + '<article class="prose">' + md(explainer) + '</article>'
(DOCS / 'index.html').write_text(layout('MathVet — which AI-generated Lean statements say what the paper claims?', body, 'home',
                                        extra_head=KATEX_HEAD, generated=status['generated'], commit=COMMIT[:8]), encoding='utf-8')
(DOCS / 'protocol.html').write_text(layout('MathVet — referee protocol', '<article class="prose">' + md(protocol) + '</article>', 'protocol',
                                           extra_head=KATEX_HEAD, generated=status['generated'], commit=COMMIT[:8]), encoding='utf-8')

fam_json = json.dumps([OrderedDict([(k, f[k]) for k in ('family', 'title', 'subject', 'headline', 'verdict', 'challenges', 'review_note',
                                                      'definitions_to_check', 'external_packages', 'cone_lines_max', 'machine_check',
                                                      'lab_scope_note', 'lab_docs_url', 'papers')]) for f in families.values()],
                      ensure_ascii=False).replace('</', '<\\/')
ch_json = json.dumps([OrderedDict([(k, c[k]) for k in ('challenge', 'family', 'family_verdict', 'result_label', 'theorem_names',
                                                     'solution_module', 'cone_oai_lines', 'cone_external', 'machine_check', 'build',
                                                     'build_seconds', 'closure', 'closure_constants', 'closure_problems', 'shadowing',
                                                     'axioms', 'comparator', 'comparator_finished', 'cloud_comparator', 'cloud_sandbox',
                                                     'cloud_finished', 'cloud_files', 'paper_title', 'paper_theorem',
                                                     'lean_url', 'config_url', 'paper_url', 'evidence_files')]) for c in challenges.values()],
                     ensure_ascii=False).replace('</', '<\\/')
(DOCS / RELEASE / 'data.json').write_text(json.dumps(dict(status=status, families=list(families.values()), challenges=list(challenges.values())),
                                                     ensure_ascii=False), encoding='utf-8')
(DOCS / RELEASE / 'index.html').write_text(layout(f'MathVet — fidelity table for openai/math', TABLE_PAGE.replace('__DATA__', fam_json)
                                                  .replace('__COMMIT8__', COMMIT[:8]).replace('__COMMIT__', COMMIT).replace('__GENERATED__', status['generated']), 'table',
                                                  extra_head=KATEX_HEAD, generated=status['generated'], commit=COMMIT[:8]), encoding='utf-8')
(DOCS / RELEASE / 'challenges.html').write_text(layout('MathVet — challenge status for openai/math', CHALLENGES_PAGE.replace('__DATA__', ch_json)
                                                       .replace('__COMMIT8__', COMMIT[:8]).replace('__COMMIT__', COMMIT).replace('__GENERATED__', status['generated']), 'challenges',
                                                       generated=status['generated'], commit=COMMIT[:8]), encoding='utf-8')

print(json.dumps(OrderedDict((k, v) for k, v in status.items() if not isinstance(v, list)), indent=1))
print('built', len(built), 'closure ok', len(closure_ok), 'comparator pass', len(comp_pass), 'running', len(comp_running), 'building', len(build_running))
print('alignment rows', len(alignment), 'sources', len(sources))
