# Family 323 — Relative independence of the separable quotient problem

Subject: Functional analysis. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 323 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Establishes, relative to the consistency of a measurable cardinal, that the separable quotient problem is independent of ZFC. The assertion that every infinite-dimensional Banach space has a separable infinite-dimensional quotient can hold for all real and complex Banach spaces, whereas the continuum hypothesis yields counterexamples over both fields.

## 2. The repository's own scope note ([`lean/docs/323.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/323.md), verbatim; relative links made absolute)

# Independence of the separable quotient problem

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Relative independence of the separable quotient problem](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/paper.pdf)

## Scope

The separable quotient problem asks whether every infinite-dimensional Banach space has an infinite-dimensional separable quotient. The linked formalization proves the negative direction under the continuum hypothesis: over both the real and complex fields, there is an infinite-dimensional Banach space admitting no bounded linear surjection onto an infinite-dimensional separable Banach space.

This is the conditional counterexample direction. The positive consistency direction and the paper's full relative-independence conclusions are outside the selected statement.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Failure of the separable quotient assertion under the continuum hypothesis | [SeparableQuotientNegative.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SeparableQuotientNegative.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`SeparableQuotientNegative.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SeparableQuotientNegative.lean) — the lab's result label: *Failure of the separable quotient assertion under the continuum hypothesis*. Comparator config [`SeparableQuotientNegative.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SeparableQuotientNegative.json): theorem(s) `OAI.SeparableQuotient.negative_main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.SeparableQuotients.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Relative independence of the separable quotient problem** — [`preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/paper.pdf); `theorem` `intro:main` at [`build/sections/introduction.tex:34`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/build/sections/introduction.tex#L34):

```latex
\begin{theorem}\label{intro:main}
For each $\mathbb F\in\{\R,\C\}$, ZFC proves the following implications.
\begin{enumerate}[label=\textup{(\roman*)}]
 \item If $\mathfrak c$ is real-valued measurable, then $\SQ_{\mathbb F}$
 holds.
 \item If the continuum hypothesis holds, then $\SQ_{\mathbb F}$ fails.
\end{enumerate}
Consequently, if ZFC with a measurable cardinal is consistent, then
$\SQ_{\mathbb F}$ is independent of ZFC. Consistency of its failure
requires only consistency of ZFC.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Relative independence of the separable quotient problem](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026)

## 5. Your classification

Enter one line for family `323` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
