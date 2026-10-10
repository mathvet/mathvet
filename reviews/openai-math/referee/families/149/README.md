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

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Boundedness and persistence of weakly reversible mass-action systems** — [`preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/01-introduction.tex:40`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026/build/sections/01-introduction.tex#L40):

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

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Uniform Permanence in Weakly Reversible Mass-Action Systems](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026); [Boundedness and persistence of weakly reversible mass-action systems](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Boundedness-and-persistence-of-weakly-reversible-mass-action-systems-September-25-2026)

## 5. Your classification

Enter one line for family `149` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
