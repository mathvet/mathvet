# Family 081 — The David--Semmes Riesz-transform problem in higher codimension

Subject: Real and complex analysis. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 081 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Resolves the remaining higher-codimension Riesz-transform rectifiability problem: for $d\ge4$ and $2\le n\le d-2$, an $n$-Ahlfors--David regular Radon measure on $\mathbb R^d$ is uniformly $n$-rectifiable whenever its $n$-dimensional Riesz transform is uniformly $L^2$-bounded over all positive hard truncations. The rectifiability bounds depend only on dimension, regularity and operator bounds.

## 2. The repository's own scope note ([`lean/docs/081.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/081.md), verbatim; relative links made absolute)

# Riesz transforms and rectifiability in higher codimension

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Riesz transforms and uniform rectifiability in higher codimension](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/paper.pdf)

## Scope

The formalized result proves that bounded Riesz transforms force quantitative uniform rectifiability in higher codimension. For $d\ge4$ and $2\le n\le d-2$, an $n$-Ahlfors–David regular measure whose positive hard truncations have one uniform $L^2$ operator bound has big pieces of Lipschitz images. The mass fraction and Lipschitz constant depend only on the dimensions and the stated regularity and operator bounds, and work at every support point and admissible radius, including unbounded support. The variation and principal-value corollary is not included.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Quantitative higher-codimension Riesz rectifiability | [RieszQuantitative.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/RieszQuantitative.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`RieszQuantitative.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/RieszQuantitative.lean) — the lab's result label: *Quantitative higher-codimension Riesz rectifiability*. Comparator config [`RieszQuantitative.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/RieszQuantitative.json): theorem(s) `OAI.RieszRectifiability.quantitative_higher_codimension_riesz_rectifiability`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.RieszRectifiability.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Riesz transforms and uniform rectifiability in higher codimension — *linked from the scope note*

[`preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026)

`theorem` `thm:main` at [`build/sections/00-introduction.tex:61`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/build/sections/00-introduction.tex#L61):

```latex
\begin{theorem}\label{thm:main}
Let $d\ge4$ and $2\le n\le d-2$ be integers. Let $\mu$ be an
$n$-Ahlfors--David regular Radon measure on $\R^d$ satisfying
\eqref{eq:riesz-bound}. Then $\mu$ is uniformly $n$-rectifiable in the
sense of Definition~\ref{def:ur}. Its constants $\theta$ and $M$ can
be chosen in terms of $d,n,C_{\rm AD}$ and $C_{\rm R}$ alone.
\end{theorem}
```

## 5. Your classification

Enter one line for family `081` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
