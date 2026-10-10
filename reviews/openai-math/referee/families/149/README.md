# Family 149 — Permanence for weakly reversible reaction networks

Subject: Dynamical systems and ergodic theory. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 149 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves the permanence conjecture for every finite weakly reversible mass-action system with fixed positive rate constants. Every positive stoichiometric compatibility class, even an unbounded one, has a common compact convex forward-invariant absorbing set. All positive trajectories in that class therefore eventually share positive lower and finite upper concentration bounds.

## 2. The repository's own scope note ([`lean/docs/149.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/149.md), verbatim; relative links made absolute)

# Classwise permanence for weakly reversible mass-action systems

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Boundedness and persistence of weakly reversible mass-action systems](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/paper.pdf)

## Scope

The boundedness and persistence conjectures for mass-action systems ask whether positive concentrations remain finite and separated from zero. The formalization proves this for every finite weakly reversible reaction network with positive constant reaction rates and every strictly positive initial state. A global forward solution exists, and one $\varepsilon\in(0,1)$ bounds every concentration of every global forward solution between $\varepsilon$ and $\varepsilon^{-1}$ for all nonnegative times. The bound may depend on the network, rates, and initial state.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Global boundedness and persistence for weakly reversible mass-action systems | [MassAction.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/MassAction.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`MassAction.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/MassAction.lean) — the lab's result label: *Global boundedness and persistence for weakly reversible mass-action systems*. Comparator config [`MassAction.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/MassAction.json): theorem(s) `OAI.Problem326.global_bounded_persistent_solution`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.MassAction.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Uniform Permanence in Weakly Reversible Mass-Action Systems — *not linked from the scope note*

[`preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:43`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/build/sections/introduction.tex#L43):

```latex
\begin{theorem}\label{thm:main}
Let $C\subset\Z_{\geq0}^d$ be finite, let $R\subset C\times C$ be
weakly reversible, and fix positive rate constants in
\eqref{eq:mass-action}. For every positive stoichiometric class $P$ there
is a nonempty compact convex set $K_P\subset P$ with the following
properties. Every initial point $x^0\in P$ gives a unique global positive
solution, and there is a finite $T(x^0)\geq0$ such that
\[
  x(t)\in K_P\qquad(t\geq T(x^0)).
\]
Moreover, $K_P$ is forward invariant. In particular, there is
$\eps_P\in(0,1)$, depending only on the network, the fixed rates, and
$P$, such that every such solution satisfies
\begin{equation}\label{eq:uniform-bounds}
  \eps_P\leq x_i(t)\leq\eps_P^{-1}
  \qquad(1\leq i\leq d,\ t\geq T(x^0)).
\end{equation}
\end{theorem}
```

### 4.2 Boundedness and persistence of weakly reversible mass-action systems — *linked from the scope note*

[`preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026)

`theorem` `thm:main` at [`build/sections/01-introduction.tex:40`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/build/sections/01-introduction.tex#L40):

```latex
\begin{theorem}\label{thm:main}
Let $d\ge1$, let $\mathcal C\subset\mathbb Z_{\ge0}^d$ be finite, let $\mathcal R$ be
weakly reversible, and let all reaction rates be positive constants.
For every $x^0\in\R_{>0}^d$, the solution of \eqref{eq:mass-action} with
$x(0)=x^0$ exists for every $t\ge0$. There is a number
$\varepsilon\in(0,1)$, depending on the network, the rates, and $x^0$, such
that
\begin{equation}\label{eq:main-bounds}
 \varepsilon\le x_i(t)\le\varepsilon^{-1}
 \qquad(t\ge0,\ 1\le i\le d).
\end{equation}
\end{theorem}
```

## 5. Your classification

Enter one line for family `149` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
