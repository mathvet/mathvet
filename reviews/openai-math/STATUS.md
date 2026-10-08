# Status — review of openai/math @ `adc7f124`

Generated 2026-10-08T03:38:01Z by `scripts/build_review.py`. Review status: **independent third-party review, pre-referee**.

| | families |
|---|---|
| in the release | 372 |
| with Lean (lean/docs page + Comparator challenges) | 235 |
| `full` — Lean states the headline claim | 144 |
| `partial` — one of several claims, or a special case | 60 |
| `weaker-statement` — a nontrivially weaker statement | 19 |
| `supporting-only` — a lemma or auxiliary statement | 12 |
| without Lean | 137 |

Comparator challenges: 405.

## Machine checks on the reviewer's machine (M1 laptop)
- Solutions built: 11 — `CannonGeometricAction`, `CirculantHadamard`, `EntangledGames`, `ErdosReciprocal`, `EuclideanFiveColor`, `GotsmanLinial`, `InterpolatedFactors`, `MahlerConjecture`, `MassAction`, `PiExponent`, `ThompsonNonamenability`
- Closure comparison + shadowing + axiom check clean: 11 — `CannonGeometricAction`, `CirculantHadamard`, `EntangledGames`, `ErdosReciprocal`, `EuclideanFiveColor`, `GotsmanLinial`, `InterpolatedFactors`, `MahlerConjecture`, `MassAction`, `PiExponent`, `ThompsonNonamenability`
- Real Comparator accepted (development landrun shim, no sandbox): 3 — `CannonGeometricAction`, `CirculantHadamard`, `EntangledGames`
- Comparator running: `ErdosReciprocal`; build in progress: `ContingencyTables`, `QuasiRiemannHypothesis`

Logs: `evidence/lean_checks/<Challenge>.log` (build), `.cmp.txt` (closure comparison), `.comparator.txt` (Comparator).
