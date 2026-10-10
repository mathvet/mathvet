# Family 098 — A negative answer to the Lang--Plaut problem

Subject: Convex and metric geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 098 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Every infinite-dimensional real Banach space contains a compact doubling set that admits no bi-Lipschitz embedding into any finite-dimensional normed space. The doubling constant is universal. This answers the Lang--Plaut problem negatively, even for compact subsets of Hilbert space.

## 2. The repository's own scope note ([`lean/docs/098.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/098.md), verbatim; relative links made absolute)

# Compact counterexamples to bi-Lipschitz dimension reduction

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/main.pdf)

## Scope

The formalized result gives a doubling subset of real $\ell_2$, with doubling constant at most $76800$, that admits no bi-Lipschitz embedding into any finite-dimensional Euclidean space at any finite distortion. A companion gives one universal doubling constant such that every infinite-dimensional real Banach space contains a compact doubling subset with no bi-Lipschitz embedding into any finite-dimensional normed space.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Doubling Hilbert subset without finite-dimensional embedding | [DoublingHilbert.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/DoublingHilbert.lean) |
| Compact counterexamples in infinite-dimensional Banach spaces | [CompactBanach.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CompactBanach.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`CompactBanach.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CompactBanach.lean) — the lab's result label: *Compact counterexamples in infinite-dimensional Banach spaces*. Comparator config [`CompactBanach.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CompactBanach.json): theorem(s) `OAI.CompactBanach.main`; permitted axioms `propext`, `Classical.choice`, `Quot.sound`; solution module `OAI.Geometry.DoublingHilbert.CompactBanach`.
- [`DoublingHilbert.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/DoublingHilbert.lean) — the lab's result label: *Doubling Hilbert subset without finite-dimensional embedding*. Comparator config [`DoublingHilbert.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/DoublingHilbert.json): theorem(s) `OAI.DoublingHilbert.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.DoublingHilbert.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding — *linked from the scope note*

[`preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026)

`theorem` `thm:main` at [`build/main.tex:47`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/build/main.tex#L47):

```latex
\begin{theorem}\label{thm:main}
There is a fixed subset $S$ of real $\ell_2$, equipped with its induced Hilbert distance, whose doubling constant is at most $76800$ and which admits no bi-Lipschitz embedding into $\R^k$ for any positive integer $k$, at any finite distortion.
\end{theorem}
```

## 5. Your classification

Enter one line for family `098` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
