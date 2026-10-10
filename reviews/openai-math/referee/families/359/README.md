# Family 359 — Negative K\"ahler curvature without bounded holomorphic coordinates

Subject: Differential geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 359 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Constructs a contractible domain in $\mathbb C^3$ with a complete negatively pinched K\"ahler metric but no bounded holomorphic coordinates, disproving bounded-domain uniformization in this setting. A higher-dimensional example has sectional curvature at most $-1$ and only constant bounded holomorphic functions; its curvature is not bounded below.

## 2. The repository's own scope note ([`lean/docs/359.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/359.md), verbatim; relative links made absolute)

# Negative Kähler curvature without bounded holomorphic coordinates

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [A negatively pinched Kähler threefold without bounded holomorphic coordinates](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf)

## Scope

The formalized result constructs a nonempty contractible complex threefold with a complete Kähler metric whose real sectional curvatures lie between two fixed negative constants. Nevertheless, it has no system of bounded holomorphic coordinates and is not biholomorphic to a bounded domain. The metric is obtained from an explicitly controlled potential. This is the negatively pinched construction; the different companion with only one-sided curvature control is separate.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Negatively pinched Kähler threefold without bounded coordinates | [PinchedKahler.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PinchedKahler.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`PinchedKahler.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PinchedKahler.lean) — the lab's result label: *Negatively pinched Kähler threefold without bounded coordinates*. Comparator config [`PinchedKahler.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PinchedKahler.json): theorem(s) `OAI.PinchedHartogs.main_theorem`, `OAI.PinchedHartogs.controlled_potential`, `OAI.PinchedHartogs.metric_transfer`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.Kahler.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 A negatively pinched Kähler threefold without bounded holomorphic coordinates — *linked from the scope note*

[`preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026)

`theorem` `main:theorem` at [`build/sections/01-introduction.tex:39`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/build/sections/01-introduction.tex#L39):

```latex
\begin{theorem}\label{main:theorem}
There exist a contractible domain $M\subset\C^3$, a smooth complete
K\"ahler metric $g$ on $M$, and finite constants $0<A\le B$ such that
\[
 -B\le K_g(\sigma)\le -A<0
\]
for every real two-plane $\sigma\subset T_pM$ and every $p\in M$.
No bounded holomorphic map $F:M\to\C^3$ has a nowhere-vanishing Jacobian
determinant. In particular, $M$ is not biholomorphic to a bounded domain
in $\C^3$.
\end{theorem}
```

Also located: `theorem` `density:main` (Uniform representing densities) at [`build/sections/04-densities-construction.tex:98`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/build/sections/04-densities-construction.tex#L98).

### 4.2 One-sided negative sectional curvature and the holomorphic Liouville property — *not linked from the scope note*

[`preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026)

`theorem` `thm:main` at [`build/01-introduction.tex:21`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026/build/01-introduction.tex#L21):

```latex
\begin{theorem}\label{thm:main}
For some finite integer $m\ge2$ there is a domain
$\mathcal T\subset\mathbb C^m$, diffeomorphic to $\mathbb R^{2m}$,
with a complete K\"ahler metric $g$ such that
\[
 \operatorname{Sec}_g\le-1,
 \qquad H^\infty(\mathcal T)=\mathbb C.
\]
The sectional curvatures of $g$ are unbounded below.
\end{theorem}
```

## 5. Your classification

Enter one line for family `359` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
