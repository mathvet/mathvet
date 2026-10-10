# Family 091 — The logarithmic Brunn--Minkowski conjecture

Subject: Convex and metric geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 091 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves the logarithmic Brunn--Minkowski inequality for origin-symmetric convex bodies in every dimension, and the scalar-dilation B-conjecture for all even log-concave Radon measures. For Lebesgue volume it also proves the additive $L_p$ Brunn--Minkowski inequality for full-dimensional origin-symmetric convex bodies throughout $0<p<1$.

## 2. The repository's own scope note ([`lean/docs/091.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/091.md), verbatim; relative links made absolute)

# Logarithmic and <i>L</i><sub><i>p</i></sub> Brunn–Minkowski inequalities and the B-conjecture

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [The logarithmic Brunn–Minkowski conjecture](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf)

## Scope

The logarithmic Brunn–Minkowski conjecture asserts that logarithmic interpolation of origin-symmetric convex bodies preserves the geometric-mean lower bound for volume. The formalized result proves, for every dimension $n\ge1$, such bodies $K,L\subset\mathbb R^n$, and $0\le t\le1$, that their logarithmic Wulff combination has volume at least $|K|^{1-t}|L|^t$. It assumes neither boundary smoothness nor coordinatewise unconditionality.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Logarithmic Brunn–Minkowski inequality | [LogBrunnMinkowski.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LogBrunnMinkowski.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`LogBrunnMinkowski.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LogBrunnMinkowski.lean) — the lab's result label: *Logarithmic Brunn–Minkowski inequality*. Comparator config [`LogBrunnMinkowski.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LogBrunnMinkowski.json): theorem(s) `OAI.LogBrunnMinkowski.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.LogVolume.BrunnMinkowski`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 The logarithmic Brunn–Minkowski conjecture — *linked from the scope note*

[`preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026)

`theorem` `thm:main` (Even logarithmic Brunn--Minkowski inequality) at [`build/introduction.tex:21`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-logarithmic-Brunn-Minkowski-conjecture-September-23-2026/build/introduction.tex#L21):

```latex
\begin{theorem}[Even logarithmic Brunn--Minkowski inequality]
\label{thm:main}
Let $n\ge1$ and let $K,L\subset\R^n$ be convex bodies satisfying
$K=-K$ and $L=-L$. For every $0\le\lambda\le1$,
\begin{equation}\label{eq:main}
 \left|\mathcal W[h_K^{1-\lambda}h_L^\lambda]\right|
 \ge |K|^{1-\lambda}|L|^\lambda.
\end{equation}
\end{theorem}
```

## 5. Your classification

Enter one line for family `091` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
