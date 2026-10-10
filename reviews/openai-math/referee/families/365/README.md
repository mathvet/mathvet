# Family 365 — Joint metric and connection recovery from one boundary patch

Subject: Partial differential equations. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 365 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Zero-frequency measurements on any nonempty open boundary patch determine a smooth metric and smooth unitary connection on a trivial Hermitian rank-two bundle over a compact connected manifold of dimension at least three, up to diffeomorphism and gauge fixed on that patch. Inputs and observations use the same patch. In contrast, distinct uniformly positive bounded measurable scalar conductivities on a three-dimensional ball can have identical full-boundary data.

## 2. The repository's own scope note ([`lean/docs/365.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/365.md), verbatim; relative links made absolute)

# Joint metric and connection recovery from one boundary patch

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Nonuniqueness for Bounded Measurable Scalar Conductivities in Three Dimensions](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf)

## Scope

The Calderón inverse problem asks whether boundary measurements determine an interior conductivity. The formalized result gives nonuniqueness for bounded measurable scalar conductivities on the ball $B(0,3)\subset\mathbb R^3$: two uniformly positive conductivities differ on a set of positive volume, equal $1$ near the boundary, and have the same full weak Dirichlet-to-Neumann operator. Weak solutions exist uniquely for every boundary trace.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Scalar conductivity nonuniqueness | [Conductivity.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Conductivity.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`Conductivity.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Conductivity.lean) — the lab's result label: *Scalar conductivity nonuniqueness*. Comparator config [`Conductivity.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Conductivity.json): theorem(s) `OAI.ScalarConductivity.main_nonuniqueness`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.Conductivity.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Determination of a metric and a unitary connection from one boundary patch — *not linked from the scope note*

[`preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026)

`theorem` `thm:main` at [`build/sections/01-introduction.tex:39`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Determination-of-a-metric-and-a-unitary-connection-from-one-boundary-patch-October-5-2026/build/sections/01-introduction.tex#L39):

```latex
\begin{theorem}\label{thm:main}
Let $M$ and $\Gamma$ be as above. For $j=1,2$, let $g_j$ be a smooth
Riemannian metric on $M$ and let
$A_j\in C^\infty(M;T^*M\otimes\mathfrak u(2))$. If
\[
 \langle\Lambda_{g_1,A_1,\Gamma}f,h\rangle
 =\langle\Lambda_{g_2,A_2,\Gamma}f,h\rangle
 \quad\text{for all }f,h\in C_c^\infty(\Gamma;\C^2),
\]
then there are a smooth diffeomorphism $\Phi:M\longrightarrow M$ and
a smooth map $U:M\longrightarrow U(2)$ such that
\begin{equation}\label{eq:main-conclusion}
 \Phi|_\Gamma=\Id,\qquad U|_\Gamma=I,\qquad
 g_2=\Phi^*g_1,\qquad
 A_2=U^{-1}(\Phi^*A_1)U+U^{-1}dU.
\end{equation}
Here $I$ denotes the $2\times2$ identity matrix.
\end{theorem}
```

### 4.2 Smooth anisotropic uniqueness in the Calderón problem from one boundary patch — *not linked from the scope note*

[`preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026)

`theorem` `main:patch` (Smooth anisotropic uniqueness from one patch) at [`build/sections/01-introduction.tex:54`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Smooth-Anisotropic-Uniqueness-in-the-Calderon-Problem-from-One-Boundary-Patch-September-24-2026/build/sections/01-introduction.tex#L54):

```latex
\begin{theorem}[Smooth anisotropic uniqueness from one patch]
\label{main:patch}
Let $n\ge3$. Let $M$ be a compact connected smooth $n$-manifold with
nonempty smooth boundary, and let $\Gamma\subset\partial M$ be nonempty,
proper, and relatively open. If two smooth Riemannian metrics $g_1,g_2$
on $M$ satisfy
\[
 \Lambda_{g_1,\Gamma}=\Lambda_{g_2,\Gamma},
\]
then there is a smooth diffeomorphism $\Phi:M\to M$, smooth through
the boundary, such that
\[
 \Phi|_\Gamma=\Id,\qquad g_2=\Phi^*g_1.
\]
\end{theorem}
```

### 4.3 Nonuniqueness for bounded measurable scalar conductivities in three dimensions — *linked from the scope note*

[`preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026)

`theorem` `thm:main` at [`build/paper.tex:79`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nonuniqueness-for-Bounded-Measurable-Scalar-Conductivities-in-Three-Dimensions-September-23-2026/build/paper.tex#L79):

```latex
\begin{theorem}\label{thm:main}
There exist real scalar functions $\gamma_0,\gamma_1\in
L^\infty(B(0,3);\R)$ and constants $0<c<C<\infty$ such that
\begin{enumerate}[label=\textup{(\roman*)},itemsep=2pt]
\item $c\leq\gamma_j\leq C$ almost everywhere, for $j=0,1$;
\item both conductivities equal $1$ in a neighborhood of the boundary;
\item $\abs{\{x:\gamma_0(x)\ne\gamma_1(x)\}}>0$;
\item $\Lambda_{\gamma_0}=\Lambda_{\gamma_1}$ as bounded operators
from $H^{1/2}(\partial B(0,3))$ to $H^{-1/2}(\partial B(0,3))$.
\end{enumerate}
\end{theorem}
```

## 5. Your classification

Enter one line for family `365` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
