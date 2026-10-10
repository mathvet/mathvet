# Referee protocol — error rate of the MathVet verdicts on openai/math

*Pre-registered 8 October 2026, before any family in the sample was re-read by a referee. The thresholds below are not revised after data.*

*Note added 10 October 2026: the published review has moved to upstream commit `fd4aeeb2`; the sample, the referee packet and the population counts below remain at `adc7f124` as frozen. The thresholds are unchanged.*

## What is measured

Each of the 235 families with Lean in `openai/math` (commit `adc7f124`) carries one MathVet verdict in {`full`, `partial`, `weaker-statement`, `supporting-only`} about whether its Comparator challenge statements state the family's headline claim (the overview summary). The verdicts came from one model-assisted pass per family. The quantity measured here is the **family-level error rate** of those verdicts: the fraction of families on which the adjudicated referee verdict differs from the MathVet verdict, estimated on a stratified sample and weighted to the population. A secondary number, the binary `full` versus not-`full` disagreement rate, is reported alongside.

## The sample (frozen)

40 families, listed in [`reviews/openai-math/sample.txt`](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/sample.txt) (SHA-256 in `sample.sha256`), composed of:

- **12 with certainty**: the families whose repository scope notes already document a divergence between headline and Lean (197, 261, 266, 281, 247, 262, 207, 267, 307, 157, 159, 365). They are the cases most likely to be argued about, so they are all in.
- **14 drawn at random** from the other 79 non-`full` families.
- **14 drawn at random** from the 144 `full` families.

The draw is seeded with the reviewed commit hash and reproduced by `reviews/openai-math/draw_sample.py`; the script refuses to overwrite a differing `sample.txt`.

## The referees

Two named research mathematicians who read Lean, neither an author of the reviewed formalization nor affiliated with a lab whose work MathVet reviews, classify all 40 families independently. A named third referee adjudicates every disagreement between the two. Each referee receives, per family: the overview summary (the headline), the repository's scope note `lean/docs/NNN.md`, every linked challenge `.lean` file, the paper's main theorem at file and line, and nothing from MathVet (no verdict, no note). They apply the rubric below and record a class and one sentence of justification. A timed three-family pilot precedes the full run. Referees are paid at their stated rate; their names, rates and hours are published with the result. Consent in writing is obtained before the pilot.

## The rubric (identical to the one used for the original pass)

The verdict is about the summary's primary (first-named) claim.

- `full`: the Lean statement(s) imply that claim after unpacking definitions or one routine step; name the step.
- `partial`: only a special case is stated, or a second co-equal headline claim (joined by "also", "and", "complementary theorem") has no challenge statement. A mere corollary or application ("together with X this shows") does not make a verdict `partial`.
- `weaker-statement`: the Lean statement does not imply the primary claim (a nontrivially weaker statement).
- `supporting-only`: the Lean states a lemma or auxiliary result, not the headline.
- `none`: nothing in the summary is covered.

When the scope note and the Lean disagree, the Lean wins. Non-standard definitions are noted but do not by themselves change the class.

## The estimate and the decision lines

Let $e_c$ be the error fraction among the 26 non-`full` sample families and $e_f$ among the 14 `full` ones. The published estimate is $\hat e = \tfrac{91}{235}\,e_c + \tfrac{144}{235}\,e_f$, with an 80% Wilson interval computed on the pooled 40 as an approximation. Lines fixed in advance:

- **PASS**, $\hat e \le 0.10$: the table carries "referee-verified sample; family-level error rate $\hat e$ [interval]".
- **KILL**, $\hat e \ge 0.20$: the table is publicly relabelled "first-pass map, unverified"; the referee-verified subset is published as such.
- **RETEST**, otherwise: 20 more families are drawn with the same method and strata; the pooled 60 decide with the same lines; if still in between, the rate is published with its interval and no label is claimed.

Power of the design, computed before data (derivation code below): if the true error rates are 5% (non-full) and 3% (full), P(PASS) = 0.94; at 30% / 15%, P(KILL) = 0.53 and P(RETEST) = 0.44; at 40% / 20%, P(KILL) = 0.85. A sample of 40 cannot certify a rate below about 5%; the number is published with its interval for that reason.

## Publication

The rate, its interval, the per-family referee classes, the adjudications and the referees' names are published in this repository whatever the result shows, with a target date of **29 October 2026**. Verdicts that the referees overturn are corrected in the table with a changelog entry naming the change. Until then every verdict is labelled pre-referee and no MathVet prose assigns a verdict class to a named family.

## Derivation code

```python
from math import comb, sqrt
W_C, W_F = 91/235, 144/235          # stratum weights
N_C, N_F = 26, 14                   # sample sizes per stratum
def binom(n, k, p): return comb(n, k) * p**k * (1-p)**(n-k)
def dist(true_c, true_f):
    pr = {"pass": 0.0, "kill": 0.0, "retest": 0.0}
    for kc in range(N_C + 1):
        for kf in range(N_F + 1):
            p = binom(N_C, kc, true_c) * binom(N_F, kf, true_f)
            e = W_C * kc / N_C + W_F * kf / N_F
            pr["pass" if e <= 0.10 else "kill" if e >= 0.20 else "retest"] += p
    return pr
def wilson(k, n, z=1.2816):         # 80% interval
    p = k/n; den = 1 + z*z/n; c = (p + z*z/(2*n))/den
    h = z*sqrt(p*(1-p)/n + z*z/(4*n*n))/den
    return max(0, c-h), min(1, c+h)
for tc, tf in [(0.05, 0.03), (0.10, 0.05), (0.20, 0.10), (0.30, 0.15), (0.40, 0.20)]:
    print(tc, tf, dist(tc, tf))
for k in (2, 4, 6, 8, 10):
    print(k, '/40 ->', wilson(k, 40))
```
