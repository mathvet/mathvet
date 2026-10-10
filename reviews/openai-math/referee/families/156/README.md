# Family 156 — Borsuk's conjecture fails in dimension nine

Subject: Combinatorics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 156 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Constructs a compact subset of $\mathbb R^9$ that cannot be covered by ten sets of strictly smaller diameter, disproving Borsuk's covering assertion already in dimension nine. The example consists of rank-one orthogonal projectors onto lines in $\mathbb R^4$, with the Frobenius metric.

## 2. The repository's own scope note ([`lean/docs/156.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/156.md), verbatim; relative links made absolute)

# Borsuk's conjecture fails in dimension nine

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [A nine-dimensional counterexample to Borsuk's covering assertion](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf)

## Scope

Borsuk's conjecture predicts that every bounded subset of $\mathbb R^d$ can be covered by $d+1$ sets of strictly smaller diameter. The formalized counterexample is the compact set of rank-one orthogonal projectors onto lines in $\mathbb R^4$, with the Frobenius metric. It lies in the nine-dimensional affine space of trace-one symmetric matrices, has diameter $\sqrt2$, and cannot be covered by ten arbitrary sets of smaller diameter.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Nine-dimensional Borsuk counterexample | [BorsukNine.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BorsukNine.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`BorsukNine.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BorsukNine.lean) — the lab's result label: *Nine-dimensional Borsuk counterexample*. Comparator config [`BorsukNine.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BorsukNine.json): theorem(s) `OAI.BorsukNine.main_theorem`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.Borsuk.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**A nine-dimensional counterexample to Borsuk's covering assertion** — [`preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/introduction.tex:18`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/build/sections/introduction.tex#L18):

```latex
\begin{theorem}\label{thm:main}
The compact set
\[
 X=\{uu^{\mathsf T}:u\in\mathbb R^4,\ \|u\|=1\}
 \subset\{A\in\operatorname{Sym}_4(\mathbb R):\operatorname{tr}A=1\},
\]
with the Frobenius metric, has diameter $\sqrt2$ and cannot be covered
by ten subsets of diameter strictly less than $\sqrt2$.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [A nine-dimensional counterexample to Borsuk's covering assertion](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026)

## 5. Your classification

Enter one line for family `156` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
