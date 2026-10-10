#!/usr/bin/env python3
"""Score the referee round (PROTOCOL.md). Kept OUTSIDE the referee packet because it needs the MathVet verdicts.

Usage: python3 referee_score.py --a form-A.csv --b form-B.csv [--adjudication adj.csv] [--sample sample.txt] [--out report.md]
       python3 referee_score.py --demo        (synthetic verdicts and forms, to see the output format; prints no real verdict)
Forms: family,class,justification,nonstandard_definitions,minutes (class in full | partial | weaker-statement | supporting-only | none).
Adjudication: family,class,justification — one row for every family on which the two referees differ.
Outputs: inter-referee agreement, the adjudicated class per family, the pre-registered stratum-weighted error rate with its
80% Wilson interval and decision line, the binary (full / not full) rate, and a secondary three-stratum sensitivity figure
(the 12 documented-divergence families were included with certainty, so the pre-registered estimate treats them as part
of a random sample of the 91 non-full families; the sensitivity figure weights them by their own population share).
The decision is withheld (exit code 2) while any sampled family lacks two classes or an adjudication.
"""
import argparse, csv, json, random, sys
from collections import Counter
from math import sqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLASSES = ['full', 'partial', 'weaker-statement', 'supporting-only', 'none']
W_C, W_F = 91 / 235, 144 / 235      # pre-registered stratum weights (PROTOCOL.md)
Z80 = 1.2816
DOCUMENTED = {'197', '261', '266', '281', '247', '262', '207', '267', '307', '157', '159', '365'}   # PROTOCOL.md, "The sample"
N_DOC, N_OTHER_NONFULL, N_FULL = 12, 79, 144


def wilson(k, n, z=Z80):
    if n == 0:
        return (0.0, 0.0)
    p = k / n; den = 1 + z * z / n; c = (p + z * z / (2 * n)) / den
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, c - h), min(1.0, c + h)


def read_form(path, sample):
    out = {}
    with open(path, encoding='utf-8-sig', newline='') as fh:
        for i, r in enumerate(csv.DictReader(fh), 2):
            fam = (r.get('family') or '').strip().zfill(3)
            cls = (r.get('class') or '').strip().lower()
            if not fam or not cls:
                continue
            if fam not in sample:
                sys.exit(f'{path}:{i}: family {fam} is not in the sample')
            if cls not in CLASSES:
                sys.exit(f'{path}:{i}: class {cls!r} is not one of {CLASSES}')
            if fam in out:
                sys.exit(f'{path}:{i}: family {fam} appears twice')
            out[fam] = dict(cls=cls, why=(r.get('justification') or '').strip(), defs=(r.get('nonstandard_definitions') or '').strip(),
                            minutes=(r.get('minutes') or '').strip())
    if not out:
        sys.exit(f'{path}: no rows with a family and a class (expected columns: family,class,justification,...)')
    return out


def kappa(a, b, fams):
    n = len(fams)
    po = sum(a[f] == b[f] for f in fams) / n
    ca, cb = Counter(a[f] for f in fams), Counter(b[f] for f in fams)
    pe = sum(ca[c] * cb[c] for c in CLASSES) / (n * n)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def rate(err, fams, strata):
    """Pre-registered estimate: W_C * (errors among non-full sample) + W_F * (errors among full sample)."""
    nf = [f for f in fams if strata[f] == 'nonfull']; fu = [f for f in fams if strata[f] == 'full']
    e_c = sum(err[f] for f in nf) / len(nf) if nf else 0.0
    e_f = sum(err[f] for f in fu) / len(fu) if fu else 0.0
    return W_C * e_c + W_F * e_f, (len(nf), sum(err[f] for f in nf), e_c), (len(fu), sum(err[f] for f in fu), e_f)


def rate3(err, fams, strata):
    """Sensitivity: three strata (documented 12 / other non-full 79 / full 144), each weighted by its population share."""
    g = {'doc': [f for f in fams if f in DOCUMENTED], 'other': [f for f in fams if strata[f] == 'nonfull' and f not in DOCUMENTED],
         'full': [f for f in fams if strata[f] == 'full']}
    w = {'doc': N_DOC / 235, 'other': N_OTHER_NONFULL / 235, 'full': N_FULL / 235}
    return sum(w[k] * (sum(err[f] for f in g[k]) / len(g[k]) if g[k] else 0.0) for k in g)


def score(form_a, form_b, adjud, mathvet, sample, out, synthetic=False):
    L = []
    fams_both = [f for f in sample if f in form_a and f in form_b]
    missing = [f for f in sample if f not in fams_both]
    a = {f: form_a[f]['cls'] for f in fams_both}; b = {f: form_b[f]['cls'] for f in fams_both}
    final, unresolved = {}, []
    for f in fams_both:
        if a[f] == b[f]:
            final[f] = a[f]
        elif f in adjud:
            final[f] = adjud[f]['cls']
        else:
            unresolved.append(f)
    scored = [f for f in fams_both if f in final]
    strata = {f: ('full' if mathvet[f] == 'full' else 'nonfull') for f in sample}
    complete = not missing and not unresolved
    if fams_both:
        agree = sum(a[f] == b[f] for f in fams_both)
        L.append('## Agreement\n\n' + f'Referees agree on {agree} of {len(fams_both)} families ({agree / len(fams_both):.0%}); '
                 f"Cohen's kappa over the five classes {kappa(a, b, fams_both):.2f}; binary (full / not full) agreement "
                 f'{sum((a[f] == "full") == (b[f] == "full") for f in fams_both)} of {len(fams_both)}.')
    err = {f: final[f] != mathvet[f] for f in scored}
    berr = {f: (final[f] == 'full') != (mathvet[f] == 'full') for f in scored}
    e_hat, (n_c, k_c, e_c), (n_f, k_f, e_f) = rate(err, scored, strata)
    lo, hi = wilson(k_c + k_f, len(scored))
    b_hat = rate(berr, scored, strata)[0]
    sens = rate3(err, scored, strata)
    sec = ['## Error rate of the MathVet verdicts' + (' (SYNTHETIC DATA)' if synthetic else ''), '',
           '| stratum | families scored | adjudicated class differs from MathVet |', '|---|---|---|',
           f'| non-`full` (documented + drawn) | {n_c} (design 26) | {k_c} ({e_c:.1%}) |', f'| `full` | {n_f} (design 14) | {k_f} ({e_f:.1%}) |', '',
           f'Pre-registered stratum-weighted family-level error rate ê = {W_C:.3f}·{e_c:.3f} + {W_F:.3f}·{e_f:.3f} = **{e_hat:.3f}**; '
           f'80% Wilson interval on the pooled {k_c + k_f}/{len(scored)}: [{lo:.3f}, {hi:.3f}]. '
           f'Binary (`full` vs not-`full`) disagreement rate, same weighting: {b_hat:.3f}. '
           f'Sensitivity (three strata, secondary): {sens:.3f}.', '']
    if complete:
        decision = 'PASS' if e_hat <= 0.10 else 'KILL' if e_hat >= 0.20 else 'RETEST'
        sec.append(f'Pre-registered decision line: **{decision}** (PASS ≤ 0.10, KILL ≥ 0.20, RETEST otherwise).')
    else:
        pend = missing + unresolved
        # range: every pending family counted as agreeing with MathVet, or every one as an error
        lo_e = rate({**err, **{f: False for f in pend}}, scored + pend, strata)[0]
        hi_e = rate({**err, **{f: True for f in pend}}, scored + pend, strata)[0]
        sec.append(f'**NO DECISION (incomplete):** {len(missing)} families without two classes ({", ".join(missing) or "none"}), '
                   f'{len(unresolved)} disagreements without an adjudication ({", ".join(unresolved) or "none"}). PROTOCOL.md requires '
                   f'every disagreement to be adjudicated before the rate is published. If the pending families all agree with MathVet '
                   f'ê = {lo_e:.3f}; if they are all errors ê = {hi_e:.3f}.')
    L.append('\n'.join(sec))
    tbl = ['## Per family', '', '| family | MathVet (pre-referee) | referee A | referee B | adjudicated | final | differs |', '|---|---|---|---|---|---|---|']
    for f in sample:
        if f in scored:
            tbl.append(f'| {f} | {mathvet[f]} | {a[f]} | {b[f]} | {adjud[f]["cls"] if f in adjud else ""} | {final[f]} | {"**yes**" if err[f] else ""} |')
        else:
            tbl.append(f'| {f} | {mathvet[f]} | {form_a.get(f, {}).get("cls", "")} | {form_b.get(f, {}).get("cls", "")} | | *pending* | |')
    L.append('\n'.join(tbl))
    just = ['## Justifications', '']
    for f in sample:
        if f in form_a or f in form_b:
            just.append(f'- **{f}** — A ({form_a.get(f, {}).get("cls", "")}): {form_a.get(f, {}).get("why", "")} '
                        f'— B ({form_b.get(f, {}).get("cls", "")}): {form_b.get(f, {}).get("why", "")}'
                        + (f' — adjudication ({adjud[f]["cls"]}): {adjud[f]["why"]}' if f in adjud else '')
                        + (f' — non-standard definitions noted: {form_a.get(f, {}).get("defs", "")} / {form_b.get(f, {}).get("defs", "")}'
                           if form_a.get(f, {}).get('defs') or form_b.get(f, {}).get('defs') else ''))
    L.append('\n'.join(just))
    text = '# Referee round — scoring per PROTOCOL.md' + (' — SYNTHETIC DEMO, NOT A RESULT' if synthetic else '') + '\n\n' + '\n\n'.join(L) + '\n'
    if out:
        Path(out).write_text(text, encoding='utf-8')
    print(text)
    return complete


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a'); ap.add_argument('--b'); ap.add_argument('--adjudication'); ap.add_argument('--out')
    ap.add_argument('--sample', default=str(HERE / 'sample.txt'), help='the family list to score (default: the frozen 40; a RETEST pool may be passed)')
    ap.add_argument('--demo', action='store_true')
    args = ap.parse_args()
    sample = [l.strip() for l in open(args.sample, encoding='utf-8') if l.strip()]
    if args.demo:
        rng = random.Random(0)
        fake = {f: ('full' if i < 14 else rng.choice(CLASSES[1:4])) for i, f in enumerate(sample)}   # synthetic "verdicts", same 26/14 shape
        fa, fb, adj = {}, {}, {}
        for f in sample:
            ca = cb = fake[f]
            if rng.random() < 0.15: ca = rng.choice([c for c in CLASSES if c != ca])
            if rng.random() < 0.15: cb = rng.choice([c for c in CLASSES if c != cb])
            fa[f] = dict(cls=ca, why='demo', defs='', minutes='20'); fb[f] = dict(cls=cb, why='demo', defs='', minutes='25')
            if ca != cb: adj[f] = dict(cls=rng.choice([ca, cb]), why='demo adjudication')
        print('(SYNTHETIC: the "MathVet" column below is random, not the real verdicts)\n')
        score(fa, fb, adj, fake, sample, None, synthetic=True)
        return
    if not (args.a and args.b):
        ap.error('--a and --b are required (or --demo)')
    frozen = HERE / 'referee' / 'frozen' / 'verdicts.json'   # the verdicts at the frozen commit; the live review may have moved on
    if frozen.exists():
        mathvet = json.load(open(frozen, encoding='utf-8'))['verdicts']
    else:
        mathvet = {}
        for p in sorted((HERE / 'source').glob('lean_scope_audit_part*.json')):
            for r in json.load(open(p, encoding='utf-8')):
                mathvet[r['family']] = r['headline_formalized']
    unknown = [f for f in sample if f not in mathvet]
    if unknown:
        sys.exit(f'families without a MathVet verdict (not in the audit): {unknown}')
    if Path(args.sample).resolve() == (HERE / 'sample.txt').resolve():
        n_nonfull = sum(1 for f in sample if mathvet[f] != 'full')
        assert (n_nonfull, len(sample) - n_nonfull) == (26, 14), (n_nonfull, len(sample) - n_nonfull)
    adjud = read_form(args.adjudication, sample) if args.adjudication else {}
    complete = score(read_form(args.a, sample), read_form(args.b, sample), adjud, mathvet, sample, args.out)
    sys.exit(0 if complete else 2)


if __name__ == '__main__':
    main()
