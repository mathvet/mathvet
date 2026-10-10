# Family 307 — Failure of rational injectivity for maximal coarse assembly

Subject: Topology. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 307 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Constructs a uniformly discrete bounded-geometry space whose maximal coarse assembly map is not rationally injective. The example is a coarse disjoint union of finite connected graphs of uniformly bounded degree, with an infinite-order kernel class. A companion gives the analogous failure for reduced coarse assembly, disproving the rational coarse Novikov conjecture.

## 2. The repository's own scope note ([`lean/docs/307.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/307.md), verbatim; relative links made absolute)

# Failure of rational injectivity for maximal coarse assembly

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [A counterexample to the coarse Novikov conjecture](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/paper.pdf)

## Scope

The coarse Novikov conjecture predicts rational injectivity of the ordinary coarse assembly map for uniformly discrete spaces of bounded geometry. The formalization constructs a counterexample from a coarse disjoint union of finite connected graphs with uniformly bounded degree. Its degree-one coarse $K$-homology contains an infinite-order class whose image under ordinary coarse assembly into the reduced locally compact Roe algebra vanishes. The class remains nonzero after tensoring with $\mathbb Q$, so rational injectivity fails.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Failure of rational injectivity for ordinary coarse assembly | [CoarseAssembly.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CoarseAssembly.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`CoarseAssembly.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CoarseAssembly.lean) — the lab's result label: *Failure of rational injectivity for ordinary coarse assembly*. Comparator config [`CoarseAssembly.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CoarseAssembly.json): theorem(s) `OAI.CoarseAssembly.bounded_geometry_graph_counterexample_unconditional`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Topology.CoarseAssembly`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Failure of rational injectivity for maximal coarse assembly — *not linked from the scope note*

[`preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026)

`theorem` `thm:main` at [`build/sections/01-introduction.tex:36`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/build/sections/01-introduction.tex#L36):

```latex
\begin{theorem}\label{thm:main}
There exist finite connected graphs $(X_j)_{j\geq1}$ with a common finite
bound on vertex degree, a coarse disjoint union $X=\bigsqcup_{j\geq1}X_j$,
and an infinite-order class $\alpha\in\KX_1(X)$ such that
\[
 \mu_X^{\max}(\alpha)=0.
\]
Consequently, $\mu_X^{\max}\otimes\Q$ is not injective.
\end{theorem}
```

### 4.2 A counterexample to the coarse Novikov conjecture — *linked from the scope note*

[`preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026)

`theorem` `thm:main` at [`build/sections/01-introduction.tex:49`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/build/sections/01-introduction.tex#L49):

```latex
\begin{theorem}\label{thm:main}
There is a uniformly discrete bounded-geometry metric space $X$, which is a
coarse disjoint union of finite connected graphs of uniformly bounded degree,
and an infinite-order element $\alpha\in KX_1(X)$ such that
\[
 \mu_X(\alpha)=0\quad\text{in }K_1(C^*(X)).
\]
Consequently, ordinary coarse assembly for $X$ fails to be injective both
integrally and after tensoring its domain and target with $\Q$.
\end{theorem}
```

## 5. Your classification

Enter one line for family `307` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
