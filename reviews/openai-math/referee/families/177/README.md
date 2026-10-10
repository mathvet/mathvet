# Family 177 — Bounded-degree coboundary expanders in every dimension

Subject: Combinatorics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 177 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Constructs arbitrarily large finite $d$-dimensional simplicial complexes, for every $d\ge3$, with uniformly bounded vertex degrees and uniform $\mathbb F_2$ coboundary expansion in every degree below $d$. Together with the known graph and two-dimensional cases, this establishes the existence of such expanders in every positive dimension.

## 2. The repository's own scope note ([`lean/docs/177.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/177.md), verbatim; relative links made absolute)

# Bounded-degree coboundary expanders

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Bounded-degree coboundary expanders in every dimension](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026/paper.pdf)

## Scope

The formalization constructs bounded-degree $\mathbb F_2$ coboundary expanders in every dimension $d\ge3$. For each such $d$, it gives finite pure connected $d$-dimensional simplicial complexes with vertex counts tending to infinity, one uniform bound on top-dimensional degree at each vertex, and one positive coboundary-expansion constant in every degree below $d$. The constants may depend on $d$. The graph and two-dimensional cases used for the paper's all-positive-dimensions conclusion are separate.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Bounded-degree coboundary expanders in dimensions at least three | [CoboundaryExpanders.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CoboundaryExpanders.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`CoboundaryExpanders.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CoboundaryExpanders.lean) — the lab's result label: *Bounded-degree coboundary expanders in dimensions at least three*. Comparator config [`CoboundaryExpanders.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CoboundaryExpanders.json): theorem(s) `OAI.CoboundaryExpanders.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Combinatorics.Coboundary.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Bounded-degree coboundary expanders in every dimension — *linked from the scope note*

[`preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026)

`theorem` `thm:main` at [`build/source/sections/introduction.tex:40`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-degree-coboundary-expanders-in-every-dimension-September-24-2026/build/source/sections/introduction.tex#L40):

```latex
\begin{theorem}\label{thm:main}
For every integer $d\ge3$, there exist constants $D<\infty$, $\eps>0$,
and finite connected pure $d$-dimensional simplicial complexes $X_m$,
with $|X_m(0)|\longrightarrow\infty$, such that every vertex belongs to
at most $D$ faces of dimension $d$ and, for every
$f\in C^i(X_m;\F)$,
\begin{equation}\label{eq:goal}
 \norm{\delta_i f}_{X_m,i+1}
 \ge \eps\,\dist_{X_m,i}(f,B^i(X_m))
 \qquad(0\le i<d).
\end{equation}
The constants are independent of $m$, $i$, and $f$.
\end{theorem}
```

## 5. Your classification

Enter one line for family `177` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
