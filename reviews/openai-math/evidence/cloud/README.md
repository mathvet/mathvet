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
