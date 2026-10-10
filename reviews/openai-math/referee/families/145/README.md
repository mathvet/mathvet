# Family 145 — Rokhlin's multiple-mixing problem

Subject: Dynamical systems and ergodic theory. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 145 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves that every invertible mixing probability-preserving transformation is mixing of all finite orders, resolving Rokhlin's multiple-mixing problem for a single transformation. Correlations among any finite collection of measurable sets converge to the product of their measures whenever all pairwise time separations diverge.

## 2. The repository's own scope note ([`lean/docs/145.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/145.md), verbatim; relative links made absolute)

# Rokhlin’s multiple-mixing problem

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Rokhlin's multiple-mixing problem for one transformation](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/paper.pdf)

## Scope

Rokhlin's multiple-mixing problem asks whether ordinary mixing of one invertible probability-preserving transformation implies mixing of every finite order. The formalization proves this implication. For each $k\ge3$ and every $k$ measurable sets, the measure of their translated intersection tends to the product of their measures as all successive time gaps tend to infinity.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Mixing of every finite order for one mixing transformation | [Rokhlin.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Rokhlin.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`Rokhlin.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Rokhlin.lean) — the lab's result label: *Mixing of every finite order for one mixing transformation*. Comparator config [`Rokhlin.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Rokhlin.json): theorem(s) `OAI.Rokhlin.mixing_all_finite_orders`; definition(s) `OAI.Rokhlin.timeMap`, `OAI.Rokhlin.IsMixing`, `OAI.Rokhlin.layoutTime`, `OAI.Rokhlin.MixingOfOrder`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Dynamics.MultipleMixing.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Rokhlin's multiple-mixing problem for one transformation** — [`preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/01-introduction.tex:21`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026/build/sections/01-introduction.tex#L21):

```latex
\begin{theorem}
\label{thm:main}
Every invertible mixing probability-preserving transformation is mixing
of every finite order. More explicitly, under the assumptions above, for
every $k\ge3$ and every $A_1,\ldots,A_k\in\mathcal F$,
\[
 \mu\bigl(A_1\cap T^{-n_1}A_2\cap\cdots\cap
             T^{-(n_1+\cdots+n_{k-1})}A_k\bigr)
 \longrightarrow\prod_{i=1}^k\mu(A_i)
\]
as $\min(n_1,\ldots,n_{k-1})\to\infty$ through positive integers.
No standardness or countable-generation assumption is imposed on the
original probability space.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Rokhlin's multiple-mixing problem for one transformation](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Rokhlins-multiple-mixing-problem-for-one-transformation-September-23-2026)

## 5. Your classification

Enter one line for family `145` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
