#!/usr/bin/env python3
"""Score the referee round (PROTOCOL.md): agreement between the two referees, adjudicated classes, and the stratum-weighted
family-level error rate of the MathVet verdicts with its 80% Wilson interval and the pre-registered decision line.

Usage: python3 score.py --a form-A.csv --b form-B.csv [--adjudication adjudication.csv] [--out report.md]
       python3 score.py --demo                      (synthetic forms, to see the output format; no real data)
Forms: family,class,justification,minutes  (class in full | partial | weaker-statement | supporting-only | none).
Adjudication: family,class,justification — one row for every family on which the referees differ.
The MathVet verdicts come from ../source/lean_scope_audit_part*.json, the sample from ../sample.txt (both frozen).
"""
import argparse, csv, json, random, sys
from collections import Counter
from math import sqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
REV = HERE.parent
CLASSES = ['full', 'partial', 'weaker-statement', 'supporting-only', 'none']
W_C, W_F = 91 / 235, 144 / 235      # stratum weights (PROTOCOL.md)
N_C, N_F = 26, 14                   # sample sizes per stratum
Z80 = 1.2816


def wilson(k, n, z=Z80):
    if n == 0:
        return (0.0, 0.0)
    p = k / n; den = 1 + z * z / n; c = (p + z * z / (2 * n)) / den
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, c - h), min(1.0, c + h)


def read_form(path):
    out = {}
    with open(path, encoding='utf-8', newline='') as fh:
        for r in csv.DictReader(fh):
            fam = (r.get('family') or '').strip().zfill(3)
            cls = (r.get('class') or '').strip().lower()
            if not fam or not cls:
                continue
            if cls not in CLASSES:
                sys.exit(f'{path}: family {fam}: class {cls!r} is not one of {CLASSES}')
            out[fam] = dict(cls=cls, why=(r.get('justification') or '').strip(), minutes=(r.get('minutes') or '').strip())
    return out


def kappa(a, b, fams):
    n = len(fams)
    po = sum(a[f] == b[f] for f in fams) / n
    ca, cb = Counter(a[f] for f in fams), Counter(b[f] for f in fams)
    pe = sum(ca[c] * cb[c] for c in CLASSES) / (n * n)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def score(form_a, form_b, adjud, mathvet, sample, out):
    lines = []
    missing = [f for f in sample if f not in form_a or f not in form_b]
    if missing:
        lines.append(f'**Incomplete:** no class from both referees for {", ".join(missing)}; these families are excluded below.')
    fams = [f for f in sample if f not in missing]
    a = {f: form_a[f]['cls'] for f in fams}
    b = {f: form_b[f]['cls'] for f in fams}
    final, unresolved = {}, []
    for f in fams:
        if a[f] == b[f]:
            final[f] = a[f]
        elif f in adjud:
            final[f] = adjud[f]['cls']
        else:
            unresolved.append(f)
    if unresolved:
        lines.append(f'**Unresolved disagreements (no adjudication row):** {", ".join(unresolved)}; excluded below. '
                     'PROTOCOL.md requires an adjudication for every disagreement before the rate is published.')
    scored = [f for f in fams if f in final]
    agree = sum(a[f] == b[f] for f in fams)
    lines.append(f'## Agreement\n\nReferees agree on {agree} of {len(fams)} families ({agree / len(fams):.0%}); '
                 f"Cohen's kappa over the five classes {kappa(a, b, fams):.2f}. "
                 f'Binary (full / not full) agreement {sum((a[f] == "full") == (b[f] == "full") for f in fams)} of {len(fams)}.')
    strata = {f: ('full' if mathvet[f] == 'full' else 'nonfull') for f in scored}
    n_c = sum(1 for f in scored if strata[f] == 'nonfull'); n_f = len(scored) - n_c
    err = {f: final[f] != mathvet[f] for f in scored}
    k_c = sum(err[f] for f in scored if strata[f] == 'nonfull'); k_f = sum(err[f] for f in scored if strata[f] == 'full')
    e_c = k_c / n_c if n_c else 0.0; e_f = k_f / n_f if n_f else 0.0
    e_hat = W_C * e_c + W_F * e_f
    lo, hi = wilson(k_c + k_f, len(scored))
    decision = 'PASS' if e_hat <= 0.10 else 'KILL' if e_hat >= 0.20 else 'RETEST'
    berr = {f: (final[f] == 'full') != (mathvet[f] == 'full') for f in scored}
    bk_c = sum(berr[f] for f in scored if strata[f] == 'nonfull'); bk_f = sum(berr[f] for f in scored if strata[f] == 'full')
    b_hat = W_C * (bk_c / n_c if n_c else 0) + W_F * (bk_f / n_f if n_f else 0)
    lines.append(f'## Error rate of the MathVet verdicts\n\n'
                 f'| stratum | families scored | adjudicated class differs from MathVet |\n|---|---|---|\n'
                 f'| non-`full` (documented + drawn) | {n_c} (design {N_C}) | {k_c} ({e_c:.1%}) |\n'
                 f'| `full` | {n_f} (design {N_F}) | {k_f} ({e_f:.1%}) |\n\n'
                 f'Stratum-weighted family-level error rate ê = {W_C:.3f}·{e_c:.3f} + {W_F:.3f}·{e_f:.3f} = **{e_hat:.3f}**; '
                 f'80% Wilson interval on the pooled {k_c + k_f}/{len(scored)}: [{lo:.3f}, {hi:.3f}].\n\n'
                 f'Binary (`full` vs not-`full`) disagreement rate, same weighting: {b_hat:.3f}.\n\n'
                 f'Pre-registered decision line: **{decision}** (PASS ≤ 0.10, KILL ≥ 0.20, RETEST otherwise).'
                 + (' Excluded families make this provisional.' if missing or unresolved else ''))
    lines.append('## Per family\n\n| family | MathVet (pre-referee) | referee A | referee B | adjudicated | final | differs |\n|---|---|---|---|---|---|---|')
    for f in sample:
        if f in scored:
            adj = adjud[f]['cls'] if f in adjud else ''
            lines.append(f'| {f} | {mathvet[f]} | {a[f]} | {b[f]} | {adj} | {final[f]} | {"**yes**" if err[f] else ""} |')
        else:
            lines.append(f'| {f} | {mathvet[f]} | {a.get(f, "")} | {b.get(f, "")} | | *excluded* | |')
    lines.append('\n## Justifications\n')
    for f in sample:
        if f in form_a or f in form_b:
            lines.append(f'- **{f}** — A ({form_a.get(f, {}).get("cls", "")}): {form_a.get(f, {}).get("why", "")} '
                         f'— B ({form_b.get(f, {}).get("cls", "")}): {form_b.get(f, {}).get("why", "")}'
                         + (f' — adjudication ({adjud[f]["cls"]}): {adjud[f]["why"]}' if f in adjud else ''))
    text = '# Referee round — scoring per PROTOCOL.md\n\n' + '\n\n'.join(lines) + '\n'
    if out:
        Path(out).write_text(text, encoding='utf-8')
    print(text)
    return e_hat, decision


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a'); ap.add_argument('--b'); ap.add_argument('--adjudication'); ap.add_argument('--out')
    ap.add_argument('--demo', action='store_true')
    args = ap.parse_args()
    sample = [l.strip() for l in open(REV / 'sample.txt', encoding='utf-8') if l.strip()]
    mathvet = {}
    for p in sorted((REV / 'source').glob('lean_scope_audit_part*.json')):
        for r in json.load(open(p, encoding='utf-8')):
            mathvet[r['family']] = r['headline_formalized']
    assert all(f in mathvet for f in sample)
    n_nonfull = sum(1 for f in sample if mathvet[f] != 'full')
    assert (n_nonfull, len(sample) - n_nonfull) == (N_C, N_F), (n_nonfull, len(sample) - n_nonfull)
    if args.demo:
        rng = random.Random(0)
        fa, fb, adj = {}, {}, {}
        for f in sample:
            ca = cb = mathvet[f]
            if rng.random() < 0.15:
                ca = rng.choice([c for c in CLASSES if c != ca])
            if rng.random() < 0.15:
                cb = rng.choice([c for c in CLASSES if c != cb])
            fa[f] = dict(cls=ca, why='demo', minutes='20'); fb[f] = dict(cls=cb, why='demo', minutes='25')
            if ca != cb:
                adj[f] = dict(cls=rng.choice([ca, cb]), why='demo adjudication')
        print('(synthetic data: forms drawn at random around the MathVet verdicts; not a result)\n')
        score(fa, fb, adj, mathvet, sample, None)
        return
    if not (args.a and args.b):
        ap.error('--a and --b are required (or --demo)')
    adjud = read_form(args.adjudication) if args.adjudication else {}
    score(read_form(args.a), read_form(args.b), adjud, mathvet, sample, args.out)


if __name__ == '__main__':
    main()
