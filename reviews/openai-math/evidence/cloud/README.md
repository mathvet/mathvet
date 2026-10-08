Sandboxed Linux Comparator runs (checker/cloud/). Each .comparator.txt starts with a provenance header.

Notes on individual logs:
- `ThorpRemaining.cmp.txt` reports `SHADOW-DIFF`: the only difference between the two printouts is `Module` versus `_root_.Module`
  (the pretty-printer adds `_root_.` inside the solution environment because the solution declares another constant named
  `Module` in a nested namespace). The elaborated constant is Mathlib's `Module` in both cases; the closure comparison
  (189 constants, 0 problems) and Comparator agree. The checker now strips the prefix before comparing (2026-10-08).
- `HardSphere.cmp.txt` reports 3 closure problems (`Orbital.map`, `Orbital.continuous`, an auxiliary `_proof_3`): both definitions
  are tactic blocks, which re-elaborate differently inside the solution's environment. Comparator, which compares the compiled
  challenge module with the solution for structural identity of every reachable constant, accepted the solution; see
  `checker/README.md` for why Comparator's verdict is the authority here.
- `BassTrace.cmp.txt` reports `SHADOW-DIFF` for the same reason as ThorpRemaining (printer `_root_.` prefixes; the session ran
  the checker version from before the fix). Closure comparison 90 constants, 0 problems; Comparator accepted.
- `TalagrandDiscreteConvexity.cmp.txt` (`exceptional`, a `def … := by classical; exact Finset.univ.filter …` tactic block)
  and `RealL1Renorming.cmp.txt` (`instNormedSpaceRealRealL1._aux_1`, an auxiliary definition generated while elaborating
  an instance) each report one closure `VALUE_MISMATCH` of the same re-elaboration kind as HardSphere; Comparator accepted
  both. `TalagrandDiscreteConvexity.mismatch-debug.txt` (printed without notation) shows the only difference: the
  `Decidable` instance that `Finset.filter` carries. The solution's compiled copy uses `Classical.propDecidable`; the copy
  re-elaborated inside the solution environment finds a constructive instance (`Fintype.decidableForallFintype`,
  `Nat.decidableForallFin`, `Finset.decidableMem`, …). Both define the same finset; `Decidable` is a subsingleton.
- `SATSharpness.cmp.txt` and `ThreeStateTreeClauses.cmp.txt` report `errors=1` and `SHADOW-DIFF` because the checker's
  declaration scanner produced an invalid `#print` line (a name captured with a trailing dot; a `def _root_.…` declared
  inside a namespace). The closure comparison itself (16 and 25 constants, 0 problems) and Comparator are clean; the
  scanner is fixed (2026-10-08).
- `MatroidProphet.cmp.txt` reports `errors=2` and `SHADOW-DIFF` for the same scanner reason (two `#print` lines with a
  trailing dot); the closure comparison (22 constants, 0 problems) and Comparator are clean. `BalancedThreeStack.cmp.txt`
  reports `errors=5` because the session ran the checker version that counted every line containing the word `error`,
  and the challenge defines a constant named `BalancedTransport.error`; there is no Lean error in the file (82 constants,
  0 problems; Comparator accepted). Both files are being refreshed with the current checker.
- `NavierStokesVelocity.cmp.txt` reports `errors=1` and `SHADOW-DIFF`: the declaration scanner cut the name `table'` at
  its prime, so one `#print` line named a non-existent constant; the same error appears in both elaborations and the
  shadow difference is only the file name inside that error message. Closure comparison 260 constants, 0 problems;
  Comparator accepted. Scanner fixed (2026-10-08, primes in names).
- `RyserCovering.cmp.txt` and `RyserOddExtensions.cmp.txt` report `errors=1` and `SHADOW-DIFF`: the challenge files say
  `attribute [-instance] instDecidablePairwiseCoeFinsetOfDecidableEqOfDecidableRel in` before a definition, naming a
  Mathlib instance that the solution module does not import, so the copy re-elaborated inside the solution environment
  could not resolve the name (the standalone copy, with the challenge's own `import Mathlib`, could). Closure comparison
  11 and 12 constants, 0 problems; Comparator accepted. The checker now adds the challenge's imports to the comparison
  file (2026-10-08).
- `UniformGamma.cmp.txt` reports six closure problems on `CurrentMain.boundedFamilyProductCStar`, an instance declared
  with an empty `where` (every field is filled by instance inference and auto-generated proofs `_proof_4` … `_proof_8`):
  the same re-elaboration kind as HardSphere (instance paths chosen in the richer solution environment; auxiliary proofs
  numbered per elaboration). The other 158 constants match; Comparator accepted. Being refreshed with the current checker.
- `DixmierAllDiscrete.cmp.txt` and `ForestSpace.cmp.txt` report type mismatches on definitions and their auxiliary
  proofs; Comparator accepted both. `*.mismatch-debug.txt` files (when present) show both elaborations side by side.
- Diagnostics (`*.mismatch-debug.txt`, 2026-10-08): for DixmierAllDiscrete the only difference between the two elaborations is
  the instance path typeclass resolution chose for the metric on ℂ (`CommCStarAlgebra.toNormedCommRing` inside the solution's
  richer environment versus `NormedField.toNormedCommRing` in the solution itself), two definitionally equal terms; for
  ForestSpace the printed terms are identical and the difference is invisible to the pretty-printer. The checker now reports,
  for every structural mismatch, whether the two sides are definitionally equal (`DEFEQ`), and the summary line carries
  `defeq_only=N`; such cases no longer count as problems.
- Rechecks with the definitional-equality fallback (2026-10-08): DixmierAllDiscrete and ForestSpace have 0 problems (5 and 9
  structural differences, all definitionally equal); HardSphere's `Orbital.map` is definitionally equal and the one remaining
  entry is an auto-generated auxiliary proof (`map._proof_3`), which the checker now reports as `AUX` (numbered per elaboration;
  compared through the parent's value) rather than as a problem.
