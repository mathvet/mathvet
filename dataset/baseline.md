# Faithfulness-benchmark baseline — claude-sonnet-5-5, single-shot judge, 3 samples per pair

Generated 2026-10-10T11:00:55Z. Dataset: `dataset/autoformalization_pairs.jsonl` (405 challenge statements, 235 families, upstream commit `adc7f124`).
Judge: `claude -p --model claude-sonnet-5-5` with a JSON schema, no tools, default effort; one prompt per pair carrying the family
headline, the lab's scope note, the challenge Lean text, the located main-theorem TeX blocks and the PROTOCOL.md rubric; the
prompt names the family's other challenges but shows only the judged one. Nothing from the MathVet review is in the prompt.

**Aggregation rule.** Pair class = majority of the 3 samples; when the samples all differ, the median class in the
faithfulness order full < partial < weaker-statement < supporting-only < none. Family class = the **most faithful** pair
class among the family's challenges. Rationale: the family verdict asks whether the headline is stated by the set of challenge
statements, each judge sees one statement, and a statement that states the headline in full settles the question regardless
of the others. Known limitation: a single-statement judge cannot see that a co-equal second claim has no challenge (the
`partial` case in the rubric), so this rule can only find it when the judged statement itself is a special case; the
one-to-one subset (145 families with exactly one challenge) has no aggregation step and is the clean comparison.

## Coverage

| | count |
|---|---|
| pairs with 3 valid samples | 405 of 405 |
| families with every pair complete | 235 of 235 |
| one-to-one families among them | 145 |

## Family class vs the MathVet verdict (pre-referee, one model-assisted pass)

All complete families (n = 235): agreement 81.7%, binary full/not-full agreement 88.5%,
Cohen's kappa 0.650, linear-weighted kappa 0.739.

| MathVet \ baseline | full | partial | weaker-statement | supporting-only | none | total |
|---|---|---|---|---|---|---|
| **full** | 142 | 2 | 0 | 0 | 0 | 144 |
| **partial** | 25 | 23 | 6 | 3 | 3 | 60 |
| **weaker-statement** | 0 | 3 | 16 | 0 | 0 | 19 |
| **supporting-only** | 0 | 0 | 0 | 11 | 1 | 12 |

One-to-one families (n = 145): agreement 84.1%, binary agreement 91.7%,
Cohen's kappa 0.717, linear-weighted kappa 0.781.

| MathVet \ baseline | full | partial | weaker-statement | supporting-only | none | total |
|---|---|---|---|---|---|---|
| **full** | 85 | 0 | 0 | 0 | 0 | 85 |
| **partial** | 12 | 17 | 4 | 1 | 3 | 37 |
| **weaker-statement** | 0 | 2 | 11 | 0 | 0 | 13 |
| **supporting-only** | 0 | 0 | 0 | 9 | 1 | 10 |

Baseline class distribution (all complete families): {"full": 167, "none": 4, "partial": 28, "weaker-statement": 22, "supporting-only": 14}; MathVet: {"full": 144, "partial": 60, "supporting-only": 12, "weaker-statement": 19}.
Per pair against the family label (n = 405; exact only for one-to-one families): agreement 54.6%, kappa 0.299.

## Self-agreement across the 3 samples

Unanimous pairs 354 of 405 (87.4%); two-of-three 45;
mean pairwise agreement 91.1%; Fleiss' kappa 0.874.

## Cost and time

| | |
|---|---|
| calls (all attempts) | 1215 (1215 ok; errors {}) |
| notional cost (CLI `total_cost_usd`, API list price; the run used a subscription) | $19.69 ($0.0162 per ok call) |
| wall time summed over calls | 8057 s (mean 6.6 s per call) |
| tokens | {"input_tokens": 5158, "cache_creation_input_tokens": 2854985, "cache_read_input_tokens": 9298577, "output_tokens": 639892} |
| first / last call | 2026-10-10T09:21:40Z / 2026-10-10T11:00:55Z |

Both sides of this comparison are model readings: the MathVet verdicts are themselves one model-assisted pass (pre-referee),
so agreement here measures consistency between two automated readings, not correctness. The referee round (PROTOCOL.md)
measures correctness. Per-pair and per-family classes are not published while the verdicts are pre-referee (rule T3); aggregates only.
