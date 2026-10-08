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
- `TalagrandDiscreteConvexity.cmp.txt` (`exceptional`, a `def … := by` tactic block) and `RealL1Renorming.cmp.txt`
  (`instNormedSpaceRealRealL1._aux_1`, an auxiliary definition generated while elaborating an instance) each report one
  closure `VALUE_MISMATCH` of the same re-elaboration kind as HardSphere; Comparator accepted both.
- `SATSharpness.cmp.txt` and `ThreeStateTreeClauses.cmp.txt` report `errors=1` and `SHADOW-DIFF` because the checker's
  declaration scanner produced an invalid `#print` line (a name captured with a trailing dot; a `def _root_.…` declared
  inside a namespace). The closure comparison itself (16 and 25 constants, 0 problems) and Comparator are clean; the
  scanner is fixed (2026-10-08).
- `DixmierAllDiscrete.cmp.txt` and `ForestSpace.cmp.txt` report type mismatches on definitions and their auxiliary
  proofs; Comparator accepted both. `*.mismatch-debug.txt` files (when present) show both elaborations side by side.
