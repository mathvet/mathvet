# Family 324 — Lipschitz equivalence without linear isomorphism

Subject: Functional analysis. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 324 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Constructs separable real Banach spaces that are globally bi-Lipschitz equivalent but not linearly isomorphic, resolving the separable Lipschitz-isomorphism problem negatively. Thus even the complete metric structure up to bi-Lipschitz equivalence does not determine a separable Banach space's linear isomorphism class.

## 2. The repository's own scope note ([`lean/docs/324.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/324.md), verbatim; relative links made absolute)

# Lipschitz equivalent Banach spaces need not be linearly isomorphic

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Lipschitz Equivalent Separable Banach Spaces Need Not Be Linearly Isomorphic](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/paper.pdf)
- [Bi-Lipschitz Absorption of $c_0$ Without a Linear Copy of $c_0$](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/paper.pdf)

## Scope

The formalized counterexample gives separable real Banach spaces $X,Y$ that are bi-Lipschitz equivalent but not linearly isomorphic. The bijection has lower Lipschitz bound $4/21$ and upper bound $76/25$. The linear obstruction is explicit: $X$ contains a linear isometric copy of $c_0(\ell_2)$, whereas $Y$ contains no bounded linear copy of that space.

The formalized result constructs one separable real Banach space $X$ that is bi-Lipschitz equivalent to $X\times c_0$ but contains no closed linear subspace isomorphic to $c_0$. The same space contains a bi-Lipschitz copy of $c_0$, is bi-Lipschitz universal for separable metric spaces, and is not linearly isomorphic to $X\times c_0$. Thus nonlinear absorption of $c_0$ does not force a linear copy of it.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Bi-Lipschitz equivalent nonisomorphic Banach spaces | [LipschitzEquivalence.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LipschitzEquivalence.lean) |
| Bi-Lipschitz absorption of $c_0$ | [C0Absorption.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/C0Absorption.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`C0Absorption.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/C0Absorption.lean) — the lab's result label: *Bi-Lipschitz absorption of $c_0$*. Comparator config [`C0Absorption.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/C0Absorption.json): theorem(s) `OAI.C0Absorption.main_result`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.C0Absorption.Main`.
- [`LipschitzEquivalence.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LipschitzEquivalence.lean) — the lab's result label: *Bi-Lipschitz equivalent nonisomorphic Banach spaces*. Comparator config [`LipschitzEquivalence.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LipschitzEquivalence.json): theorem(s) `OAI.LipschitzCounterexample.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.LipschitzEquivalence.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Bi-Lipschitz Absorption of c0 Without a Linear Copy of c0** — [`preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/01-introduction.tex:51`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026/build/sections/01-introduction.tex#L51):

```latex
\begin{theorem}\label{thm:main}
There is a separable real Banach space \(Z\) containing no closed linear
subspace isomorphic to \(c_0\), and an onto bi-Lipschitz map
\[
                 F:Z\oplus_\infty c_0\longrightarrow Z.
\]
\end{theorem}
```

**Lipschitz Equivalent Separable Banach Spaces Need Not Be Linearly Isomorphic** — [`preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/01-introduction.tex:21`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026/build/sections/01-introduction.tex#L21) (further candidate):

```latex
\begin{theorem}
\label{thm:main}
There are separable real Banach spaces \(X,Y\) and a bijection
\(\Psi:X\to Y\) such that, for every \(s,t\in X\),
\begin{equation}
\label{eq:main-bounds}
 \frac4{21}\|s-t\|_X
 \le \|\Psi(s)-\Psi(t)\|_Y
 \le \frac{76}{25}\|s-t\|_X.
\end{equation}
The space \(X\) contains a linearly isometric copy of \(c_0(\ell_2)\), while
\(Y\) contains no closed subspace linearly isomorphic to
\(c_0(\ell_2)\). In particular, \(X\) and \(Y\) are not linearly
isomorphic.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Lipschitz Equivalent Separable Banach Spaces Need Not Be Linearly Isomorphic](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Lipschitz-Equivalent-Separable-Banach-Spaces-Need-Not-Be-Linearly-Isomorphic-September-24-2026); [Bi-Lipschitz Absorption of c0 Without a Linear Copy of c0](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bi-Lipschitz-Absorption-of-c0-Without-a-Linear-Copy-of-c0-September-26-2026)

## 5. Your classification

Enter one line for family `324` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
