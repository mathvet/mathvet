# Family 347 — Counterexamples to strong forms of Arnold's fixed-point conjecture

Subject: Differential geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 347 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Disproves stable-Morse lower bounds for nondegenerate Hamiltonian fixed points: on simply connected closed K\"ahler manifolds of real dimension $22$, the deficit below the stable Morse number is unbounded. A separate Hamiltonian diffeomorphism of the complex quadric threefold has exactly three fixed points, fewer than the four critical points required of every smooth function.

## 2. The repository's own scope note ([`lean/docs/347.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/347.md), verbatim; relative links made absolute)

# Counterexamples to stable-Morse and strong Arnold fixed-point bounds

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Three fixed points on the symplectic quadric threefold](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf)

## Scope

The critical-number form of Arnold's fixed-point conjecture predicts at least as many fixed points as the minimum number of critical points of a smooth function. The formalized counterexample is a Hamiltonian diffeomorphism of the complex quadric threefold with exactly three fixed points, while every smooth function on that manifold has at least four critical points. At least one fixed point is degenerate. The separate nondegenerate Morse-number construction is not included.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Three-fixed-point Arnold counterexample | [ArnoldCounterexample.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ArnoldCounterexample.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`ArnoldCounterexample.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ArnoldCounterexample.lean) — the lab's result label: *Three-fixed-point Arnold counterexample*. Comparator config [`ArnoldCounterexample.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ArnoldCounterexample.json): theorem(s) `OAI.ArnoldCounterexample.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.Arnold.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Three fixed points on the symplectic quadric threefold** — [`preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf); `theorem` `thm:counterexample` at [`build/sections/00-introduction.tex:56`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/sections/00-introduction.tex#L56):

```latex
\begin{theorem}\label{thm:counterexample}
There is a smooth Hamiltonian diffeomorphism $\phi$ of the closed connected
symplectic six-manifold $Q^3$ such that
\begin{equation}\label{eq:counterexample}
 \#\Fix(\phi)=3<4=\Crit(Q^3)
                  =\operatorname{cuplength}(Q^3;\mathbb Q).
\end{equation}
At least one fixed point of $\phi$ is degenerate.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Hamiltonian Fixed Points Below the Stable Morse Number in Dimension Twenty-Two](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026); [Sharpness of the Cyclic Integral Floer Bound Below the Stable Morse Number](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026); [Hamiltonian Fixed Points Below the Stable Morse Number](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026); [A nondegenerate counterexample to the Morse-number Arnold bound](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026); [Three fixed points on the symplectic quadric threefold](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026)

## 5. Your classification

Enter one line for family `347` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
