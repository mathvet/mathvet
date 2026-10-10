# Family 291 — Toms--Winter and equivariant Jiang--Su stability

Subject: Operator algebras. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 291 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves equivariant Jiang--Su stability for every countable discrete amenable group action on a simple separable unital infinite-dimensional nuclear stably finite Jiang--Su-stable $C^*$-algebra, resolving this case of Szab\'o's conjecture without restrictions on trace dynamics. The family also proves the unital Toms--Winter conjecture, equating strict comparison, finite nuclear dimension and Jiang--Su stability in the simple separable unital infinite-dimensional nuclear setting.

## 2. The repository's own scope note ([`lean/docs/291.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/291.md), verbatim; relative links made absolute)

# Cuntz comparison, nuclear dimension, and equivariant Jiang–Su stability

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Tracial projection methods and uniform property $\Gamma$](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf)

## Scope

The formalization proves that real rank zero of the uniform tracial ultrapower of the uniform tracial completion implies uniform property $\Gamma$ for a simple separable unital infinite-dimensional nuclear stably finite $C^*$-algebra with traces. The conclusion holds at every specified free ultrafilter under the corresponding real-rank-zero hypothesis.

The linked comparison results also prove Jiang–Su absorption and uniform property $\Gamma$ for simple separable unital infinite-dimensional nuclear algebras with strict comparison, and for the stated stably projectionless nuclear algebras with bounded densely finite traces, a nonempty compact normalized trace base, and the prescribed finite-target-rank comparison condition.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Uniform property $\Gamma$ from tracial real rank zero | [UniformGamma.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/UniformGamma.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`UniformGamma.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/UniformGamma.lean) — the lab's result label: *Uniform property $\Gamma$ from tracial real rank zero*. Comparator config [`UniformGamma.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/UniformGamma.json): theorem(s) `OAI.ComparatorModel.CurrentMain.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.TracialSplitting.Challenge`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Tracial projection methods and uniform property Gamma** — [`preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf); `theorem` `r:thm:main` (Real rank zero and uniform property $\Gamma$) at [`build/sections/01_introduction.tex:57`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/build/sections/01_introduction.tex#L57):

```latex
\begin{theorem}[Real rank zero and uniform property $\Gamma$]
\label{r:thm:main}
Let $A$ be a unital, separable, simple, infinite-dimensional, nuclear,
stably finite $C^*$-algebra with $T(A)\ne\varnothing$, and let
$B=\overline A^{T(A)}$. Fix any free ultrafilter $\omega$ on $\N$.
If $B^\omega$ has real rank zero in its quotient $C^*$-norm, then there is
a projection $p\in B^\omega\cap B'$ such that
\[
 \lambda(px)=\tfrac12\lambda(x)
 \qquad(x\in B,\ \lambda\in\Lambda_\omega).
\]
In particular, $A$ has uniform property $\Gamma$.
\end{theorem}
```

**Tracial projection methods and uniform property Gamma** — [`preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf); `theorem` `u:thm:main` (The direct unital comparison route) at [`build/sections/01_introduction.tex:207`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/build/sections/01_introduction.tex#L207) (further candidate):

```latex
\begin{theorem}[The direct unital comparison route]\label{u:thm:main}
Let $A$ be a simple, separable, unital, infinite-dimensional nuclear
$C^*$-algebra with strict comparison in the preceding sense.
Then $A\cong A\otimes\Z$. When $T(A)\ne\varnothing$, the proof constructs
uniform property $\Gamma$ directly.
\end{theorem}
```

**Tracial projection methods and uniform property Gamma** — [`preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf); `theorem` `n:thm:main` (The direct stably projectionless route) at [`build/sections/01_introduction.tex:237`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/build/sections/01_introduction.tex#L237) (further candidate):

```latex
\begin{theorem}[The direct stably projectionless route]\label{n:thm:main}
Let $A$ be a nonzero simple, separable, nuclear $C^*$-algebra such that
$A\otimes\K$ has no nonzero projections. Suppose that every trace in
$T_{\mathrm{lsc}}(A)$ is bounded on the positive unit ball and that
$T_1(A)$ is nonempty and weak-$*$ compact. Assume that, for
$a,b\in(A\otimes\K)_+$ with $b\ne0$,
\[
 d_\tau(a)<1\quad
 \text{for every }\tau\in T_{\mathrm{lsc}}(A)
 \text{ with }d_\tau(b)=1
 \quad\Longrightarrow\quad a\precsim b.
\]
Then $A$ has uniform property $\Gamma$ and $A\cong A\otimes\Z$.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Equivariant Jiang–Su Stability for Amenable Actions in the Unital Stably Finite Case](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026); [Cuntz comparison and Jiang–Su absorption](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026); [Nuclear dimension and Jiang–Su stability without elementary subquotients](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026); [Tracial projection methods and uniform property Gamma](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026)

## 5. Your classification

Enter one line for family `291` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
