# Changelog

## 2026-10-08 — sandboxed Comparator run
- Real Comparator (leanprover/comparator ca04cfc) with its Landlock sandbox run on isolated Linux VMs for 354 challenges: **353 accepted, 0 rejected**; 3 could not be built in 15 GB of RAM (NuclearUltrapower, CoarseAssembly, SnakyTwentyOne). ArtinParabolicIntersections, the only challenge whose config also requires the independent nanoda kernel, was accepted by both kernels once `nanoda_bin` was built from ammkrn/nanoda_lib by `.github/workflows/nanoda.yml` and mirrored as release `nanoda-3a24072`. Evidence per challenge in `reviews/openai-math/evidence/cloud/`, status in `STATUS.md` and the challenge table.
- Together with the reviewer's own machine, 362 of 405 challenges now carry a Comparator PASS.
- Checker fixes found by this run (all our own artifacts, none a Comparator finding): definitional-equality fallback and auxiliary-declaration rule in `CmpLib.lean`; declaration scanner (trailing dots, primes, `_root_.`); Lean-error-only counting; the comparison file imports the challenge's imports and scopes the checker's `open`s. See `reviews/openai-math/evidence/cloud/README.md`.

## 2026-10-08 — first publication
- Review of `openai/math` @ `adc7f124` (2026-10-06): 235 families with Lean read against their headlines; verdicts 144 full / 60 partial / 19 weaker-statement / 12 supporting-only; 137 families without Lean.
- Machine checks: 11 challenge solutions built and closure-checked locally with standard axioms; real Comparator (development landrun shim) accepted CirculantHadamard, EntangledGames and CannonGeometricAction; ErdosReciprocal Comparator run and QuasiRiemannHypothesis build in progress.
- Referee protocol pre-registered; 40-family sample frozen (`reviews/openai-math/sample.sha256`).
- Known limits: pre-referee; no sandboxed Comparator run yet; one model-assisted pass per family.
