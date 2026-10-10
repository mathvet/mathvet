# Family 362 — Global smoothness for relativistic Vlasov--Maxwell

Subject: Partial differential equations. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 362 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves large-data global existence and uniqueness for the three-dimensional, one-species relativistic Vlasov--Maxwell system. Smooth admissible initial data may be arbitrary provided the particle density is compactly supported and the electromagnetic fields have finite energy and bounded derivatives of every order; the solution remains smooth on every finite time interval.

## 2. The repository's own scope note ([`lean/docs/362.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/362.md), verbatim; relative links made absolute)

# Global smoothness for relativistic Vlasov–Maxwell

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Global classical solutions of the three-dimensional relativistic Vlasov–Maxwell system](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf)

## Scope

The formalized result gives global existence and uniqueness for the three-dimensional one-species relativistic Vlasov–Maxwell system. The initial particle density is nonnegative, smooth, and compactly supported; the initial fields have bounded derivatives of all orders, finite energy, and satisfy both Gauss constraints. The solution is smooth on every finite time interval, has compact particle phase support there, and is unique among classical solutions. No smallness, symmetry, or neutrality assumption is imposed.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Global classical Vlasov–Maxwell solutions | [VlasovMaxwell.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/VlasovMaxwell.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`VlasovMaxwell.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/VlasovMaxwell.lean) — the lab's result label: *Global classical Vlasov–Maxwell solutions*. Comparator config [`VlasovMaxwell.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/VlasovMaxwell.json): theorem(s) `OAI.RVM.global_classical_solution`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.VlasovMaxwell.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Global classical solutions of the three-dimensional relativistic Vlasov–Maxwell system** — [`preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf); `theorem` `thm:global` at [`build/sections/introduction.tex:42`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/build/sections/introduction.tex#L42):

```latex
\begin{theorem}\label{thm:global}
Every smooth admissible datum \eqref{eq:data} generates a unique global
classical solution of \eqref{eq:rvm}. For every finite $T$, this solution
satisfies
\[
 f\in C^\infty([0,T]\times\R^3_x\times\R^3_v),\qquad
 E,B\in C^\infty([0,T]\times\R^3_x;\R^3),
\]
and $f$ has compact phase-space support on $[0,T]$.
The two divergence constraints hold for all time.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Global classical solutions of the three-dimensional relativistic Vlasov–Maxwell system](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026)

## 5. Your classification

Enter one line for family `362` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
