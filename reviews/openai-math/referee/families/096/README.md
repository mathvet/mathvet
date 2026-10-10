# Family 096 — The Gaussian propeller conjecture

Subject: Convex and metric geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 096 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves that the sum of squared Gaussian first moments of any finite measurable partition is at most $9/(8\pi)$. In dimension at least two, three planar sectors of angle $2\pi/3$, extended orthogonally, attain the bound. Combined with the separate Unique Games theorem, this proves NP-hardness of improving the loss factor $(8\pi/9)(1-1/k)$ for identity-target kernel clustering with fixed $k\ge3$ on rational centered positive semidefinite inputs.

## 2. The repository's own scope note ([`lean/docs/096.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/096.md), verbatim; relative links made absolute)

# The Gaussian propeller conjecture in every dimension

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [The Gaussian propeller bound in every dimension](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/main.pdf)

## Scope

The Gaussian propeller problem asks how large the sum of squared Gaussian first moments can be over a partition. The formalized result proves the sharp bound $9/(8\pi)$ for every positive dimension and every positive number of labelled cells, allowing empty cells and arbitrary masses. In dimension at least two with at least three cells, three planar sectors of angle $120^\circ$, extended in orthogonal directions, attain equality. The separate Gaussian-maxima and kernel-clustering consequences are not included.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Gaussian propeller bound and attainment | [GaussianPropeller.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GaussianPropeller.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`GaussianPropeller.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GaussianPropeller.lean) — the lab's result label: *Gaussian propeller bound and attainment*. Comparator config [`GaussianPropeller.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GaussianPropeller.json): theorem(s) `OAI.GaussianPropeller.all_partitions`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Probability.GaussianPropeller.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 The Gaussian propeller bound in every dimension — *linked from the scope note*

[`preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026)

`theorem` `thm:main` at [`build/main.tex:81`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/build/main.tex#L81):

```latex
\begin{theorem}\label{thm:main}
For all positive integers $d$ and $k$, every measurable partition
$(A_1,\ldots,A_k)$ of $\mathbb R^d$ satisfies
\[
 \sum_{i=1}^k\left\|\int_{A_i}x\,d\gamma_d(x)\right\|^2
 \le\frac9{8\pi}.
\]
Empty cells are allowed. The constant is sharp whenever $d\ge2$ and
$k\ge3$: three planar sectors of angle $2\pi/3$, multiplied by the
orthogonal complement of their plane, attain equality, with any further
cells empty.
\end{theorem}
```

Also located: `theorem` `kc:main` (Kernel-clustering hardness) at [`build/sections/kernel-application.tex:53`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/build/sections/kernel-application.tex#L53).

## 5. Your classification

Enter one line for family `096` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
