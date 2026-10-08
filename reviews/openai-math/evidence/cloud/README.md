Sandboxed Linux Comparator runs (checker/cloud/). Each .comparator.txt starts with a provenance header.

Notes on individual logs:
- `ThorpRemaining.cmp.txt` reports `SHADOW-DIFF`: the only difference between the two printouts is `Module` versus `_root_.Module`
  (the pretty-printer adds `_root_.` inside the solution environment because the solution declares another constant named
  `Module` in a nested namespace). The elaborated constant is Mathlib's `Module` in both cases; the closure comparison
  (189 constants, 0 problems) and Comparator agree. The checker now strips the prefix before comparing (2026-10-08).
