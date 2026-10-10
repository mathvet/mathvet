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

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**A negatively pinched Kähler threefold without bounded holomorphic coordinates** — [`preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf); `theorem` `main:theorem` at [`build/sections/01-introduction.tex:39`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/build/sections/01-introduction.tex#L39):

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

**A negatively pinched Kähler threefold without bounded holomorphic coordinates** — [`preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/paper.pdf); `theorem` `density:main` (Uniform representing densities) at [`build/sections/04-densities-construction.tex:98`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026/build/sections/04-densities-construction.tex#L98) (further candidate):

```latex
\begin{theorem}[Uniform representing densities]\label{density:main}
There is a constant $K_*>0$, depending only on the fixed profiles
$f,b$ and $R_0$, with the following property.  For every fixed
$D_0>\max\{1,2\sqrt{2R_0}\}$ there is an integer threshold $Q_0$
such that, for every integer $Q\ge Q_0$ and every choice of the
separated sets above, the recursion \eqref{density:recursion}
has the following properties for all $j\ge1$:
\begin{enumerate}
\item $W_j$ is smooth and strictly positive, and $W_j\,d\sigma$
represents holomorphic evaluation at zero.  In particular it is
a probability measure.
\item Under global phase rotation, $W_j$ has frequencies only
between $-\ell_j$ and $\ell_j$, and its mean on every phase orbit
is exactly one.
\item At every point of $S$,
\begin{equation}\label{density:uniform-bounds}
 \begin{gathered}
 c_0W_{j-1}\le W_j\le2W_{j-1},\\
 |ZW_j|\le K_*\sqrt{k_j}\,W_j,
 \qquad |TW_j|\le K_*k_jW_j
 \end{gathered}
\end{equation}
for every unit horizontal vector $Z$.
\end{enumerate}
The threshold $Q_0$ may also be enlarged to impose any fixed lower
threshold on the degrees $k_j$.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [A negatively pinched Kähler threefold without bounded holomorphic coordinates](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-negatively-pinched-Kahler-threefold-without-bounded-holomorphic-coordinates-September-25-2026); [One-sided negative sectional curvature and the holomorphic Liouville property](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/One-sided-negative-sectional-curvature-and-the-holomorphic-Liouville-property-September-25-2026)

## 5. Your classification

Enter one line for family `359` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
