# Family 088 — Petty's projection-volume conjecture and simplex counterexamples

Subject: Convex and metric geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 088 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves Petty's projection-volume conjecture in the remaining dimensions $n\ge4$: ellipsoids uniquely minimize projection-body volume at fixed body volume. Also establishes the full Lutwak--Petty projection inequalities. In contrast, products of simplices exceed Brannen's proposed simplex maximum for normalized projection-body volume by an exponential factor in every sufficiently large dimension.

## 2. The repository's own scope note ([`lean/docs/088.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/088.md), verbatim; relative links made absolute)

# Sharp projection-body inequalities and a counterexample to simplex maximization

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Petty’s projection-volume conjecture in dimensions at least four](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/paper.pdf)
- [A product counterexample to the simplex maximum for projection-body volume](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/paper.pdf)

## Scope

Petty's projection-volume conjecture predicts

$\displaystyle \frac{|\Pi K|}{|K|^{n-1}}\ge \kappa_{n-1}^{n}\kappa_n^{2-n},$

with equality exactly for ellipsoids; here $\kappa_j$ is the volume of the Euclidean unit ball in dimension $j$. The formalization establishes this for every convex body $K\subset\mathbb R^n$ and every $n\ge4$.

Other inequalities in the projection-body family are not included.

Brannen's simplex-maximization conjecture predicts that a simplex maximizes normalized projection-body volume $|\Pi K|/|K|^{n-1}$ in dimension $n$. The formalized counterexample is the product of two ten-dimensional simplices. Its normalized projection volume, divided by that of a twenty-dimensional simplex, is

$\displaystyle \frac{22{,}355{,}476}{22{,}020{,}096}>1.$

Thus the proposed maximum fails in dimension $20$. The paper's exponential-factor result for every sufficiently large dimension is not included.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Petty's projection-volume inequality | [PettyProjectionVolume.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PettyProjectionVolume.lean) |
| Failure of the simplex upper bound in dimension 20 | [ProjectionCounterexample.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ProjectionCounterexample.lean) |
| Explicit product-of-simplices counterexample | [ProjectionVolume.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ProjectionVolume.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`PettyProjectionVolume.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PettyProjectionVolume.lean) — the lab's result label: *Petty's projection-volume inequality*. Comparator config [`PettyProjectionVolume.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PettyProjectionVolume.json): theorem(s) `OAI.PettyProjection.petty_projection_volume`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.ProjectionBodies.Main`.
- [`ProjectionCounterexample.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ProjectionCounterexample.lean) — the lab's result label: *Failure of the simplex upper bound in dimension 20*. Comparator config [`ProjectionCounterexample.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ProjectionCounterexample.json): theorem(s) `OAI.ProjectionCounterexample.universal_simplex_upper_bound_false`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.ProjectionBody.Counterexample`.
- [`ProjectionVolume.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ProjectionVolume.lean) — the lab's result label: *Explicit product-of-simplices counterexample*. Comparator config [`ProjectionVolume.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ProjectionVolume.json): theorem(s) `OAI.Paper092.product_counterexample`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.ProjectionVolume.ProductCounterexample`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Petty’s projection-volume conjecture in dimensions at least four** — [`preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/paper.pdf); `theorem` `thm:main` at [`build/latex/sections/01_introduction.tex:36`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/build/latex/sections/01_introduction.tex#L36):

```latex
\begin{theorem}\label{thm:main}
For every integer $n\ge4$ and every convex body $K\subset\R^n$,
\begin{equation}\label{eq:main}
 \frac{|\Pi K|}{|K|^{n-1}}
 \ge \kappa_{n-1}^{\,n}\kappa_n^{\,2-n}.
\end{equation}
Equality holds if and only if $K=a+TB_2^n$ for some $a\in\R^n$ and some
invertible linear map $T$.
\end{theorem}
```

**A product counterexample to the simplex maximum for projection-body volume** — [`preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/paper.pdf); `theorem` `thm:counterexample` at [`build/main.tex:90`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/build/main.tex#L90) (further candidate):

```latex
\begin{theorem}\label{thm:counterexample}
Let \(T_{10}=\conv(0,e_1,\ldots,e_{10})\subset\R^{10}\), where the
\(e_i\) are the coordinate unit vectors, and let
\(K=T_{10}\times T_{10}\subset\R^{20}\). Then
\[
 \frac{R_{20}(K)}{c_{20}}
 =\frac{121\binom{20}{10}}{21\cdot2^{20}}
 =\frac{22\,355\,476}{22\,020\,096}>1.
\]
Thus \(K\) violates \eqref{eq:proposed-bound} in dimension twenty.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Petty’s projection-volume conjecture in dimensions at least four](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026); [A product counterexample to the simplex maximum for projection-body volume](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026)

## 5. Your classification

Enter one line for family `088` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
