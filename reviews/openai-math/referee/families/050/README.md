# Family 050 — A counterexample to Griffiths' positivity conjecture

Subject: Algebraic and complex geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 050 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Constructs ample rank-two bundles on $\mathbb P^1\times\mathbb P^1$ with no smooth Hermitian metric of strictly Griffiths-positive curvature, disproving Griffiths' positivity conjecture already on the quadric surface.

## 2. The repository's own scope note ([`lean/docs/050.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/050.md), verbatim; relative links made absolute)

# A counterexample to Griffiths’ positivity conjecture

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Ample rank-two bundles on the quadric surface without Griffiths-positive metrics](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/paper.pdf)

## Scope

Griffiths' positivity conjecture predicts that every ample holomorphic vector bundle on a smooth complex projective variety admits a smooth Hermitian metric with strictly Griffiths-positive curvature. The formalized counterexample starts with a rank-two algebraic bundle $G$ on $\mathbb P^1\times\mathbb P^1$. Its coordinatewise power pullbacks, tensored with $\mathcal O(1,1)$, are ample for every positive power but admit no such metric for all sufficiently large powers.

The separate very-ampleness result for all admissible even exponents is not included.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Ample bundles without Griffiths-positive metrics | [QuadricBundles.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/QuadricBundles.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`QuadricBundles.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/QuadricBundles.lean) — the lab's result label: *Ample bundles without Griffiths-positive metrics*. Comparator config [`QuadricBundles.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/QuadricBundles.json): theorem(s) `OAI.QuadricCounterexample.main_theorem`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.QuadricBundles.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Ample rank-two bundles on the quadric surface without Griffiths-positive metrics — *linked from the scope note*

[`preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026)

`theorem` `thm:main` at [`build/sections/01-introduction.tex:23`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/ample-rank-two-bundles-on-the-quadric-surface-without-griffiths-positive-metrics-September-24-2026/build/sections/01-introduction.tex#L23):

```latex
\begin{theorem}\label{thm:main}
There is an algebraic vector bundle $G$ of rank two on $S$ such that,
for every positive integer $m$, the bundle
\[
 E_m=f_m^*G\otimes P
\]
is ample. There is an integer $m_0$ such that $E_m$ admits no smooth
Hermitian metric with strictly Griffiths-positive Chern curvature
for every $m\ge m_0$.
\end{theorem}
```

## 5. Your classification

Enter one line for family `050` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
