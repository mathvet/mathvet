# Family 262 — Sharp one-dimensional Lieb--Thirring inequalities

Subject: Mathematical physics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 262 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves the sharp one-dimensional Lieb--Thirring inequality for $1/2<\gamma<3/2$ and arbitrary finite-matrix potentials $W\ge0$ with $\int\operatorname{tr}(W^{\gamma+1/2})<\infty$: the optimal constant is the scalar one-bound-state value, independent of matrix size. All equality cases are direct sums, in one constant unitary basis, of scalar $\operatorname{sech}^2$ solitons with independent scales and centers, and zero channels.

## 2. The repository's own scope note ([`lean/docs/262.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/262.md), verbatim; relative links made absolute)

# Sharp finite-matrix Lieb–Thirring inequalities and all equality cases

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Sharp one-dimensional Lieb–Thirring constants](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/paper.pdf)

## Scope

The formalized result determines the sharp one-dimensional Lieb–Thirring constant for $1/2<\gamma<3/2$. For every nonnegative $W\in L^{\gamma+1/2}(\mathbb R)$, it bounds the full negative-eigenvalue moment of $-d^2/dx^2-W$ by the one-bound-state constant times the potential integral. This constant is optimal and is attained by $(r+1)\mathrm{sech}^2(rx)$, where $r=(\gamma-1/2)^{-1}$. No finite spectral cutoff is imposed.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Sharp one-dimensional Lieb–Thirring inequality | [LiebThirring.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LiebThirring.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`LiebThirring.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LiebThirring.lean) — the lab's result label: *Sharp one-dimensional Lieb–Thirring inequality*. Comparator config [`LiebThirring.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LiebThirring.json): theorem(s) `OAI.SharpLiebThirring.sharp_lieb_thirring`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.LiebThirring.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Equality cases in the sharp one-dimensional matrix Lieb–Thirring inequality — *not linked from the scope note*

[`preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026)

`theorem` `thm:main` (Equality classification) at [`build/sections/introduction.tex:34`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/build/sections/introduction.tex#L34):

```latex
\begin{theorem}[Equality classification]\label{thm:main}
For every $W$ satisfying~\eqref{intro:class},
\begin{equation}\label{intro:sharp}
 \Tr(H_W)_-^\gamma\le C_\gamma\int_\R\tr(W^p),
 \qquad
 C_\gamma=\left(\frac{\gamma-1/2}{\gamma+1/2}\right)^{\gamma-1/2}
       \frac{\Gamma(\gamma+1)}{\sqrt\pi\,\Gamma(\gamma+3/2)}.
\end{equation}
Put $r=(\gamma-1/2)^{-1}$. Equality holds if and only if there are
$k\in\{0,\ldots,m\}$, a constant unitary matrix $U$, positive numbers
$a_1,\ldots,a_k$, and real numbers $x_1,\ldots,x_k$ such that almost
everywhere
\begin{equation}\label{intro:classification}
 W(x)=U\diag\bigl(w_1(x),\ldots,w_k(x),0,\ldots,0\bigr)U^*,
 \quad
 w_j(x)=(r+1)a_j^2\sech^2\!\bigl(ra_j(x-x_j)\bigr).
\end{equation}
The case $k=0$ means $W=0$. Each nonzero channel has exactly one negative
eigenvalue, $-a_j^2$, and therefore every extremal potential has at most
$m$ negative eigenvalues, counted with multiplicity.
\end{theorem}
```

### 4.2 Sharp one-dimensional Lieb–Thirring inequalities for matrix potentials — *not linked from the scope note*

[`preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026)

`theorem` `thm:main` (Sharp matrix inequality) at [`build/sections/introduction.tex:28`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026/build/sections/introduction.tex#L28):

```latex
\begin{theorem}[Sharp matrix inequality]\label{thm:main}
For every $1/2<\gamma<3/2$, every finite $m\ge1$, and every $W$ satisfying
\eqref{eq:potential-class},
\begin{equation}\label{eq:main-bound}
 \Tr(H_W)_-^\gamma\le C_\gamma\int_\R\tr(W(x)^{\gamma+1/2})\,dx,
 \qquad
 C_\gamma=
 \left(\frac{\gamma-1/2}{\gamma+1/2}\right)^{\gamma-1/2}
 \frac{\Gamma(\gamma+1)}{\sqrt\pi\,\Gamma(\gamma+3/2)}.
\end{equation}
The constant is optimal in every matrix dimension. With
$r=(\gamma-1/2)^{-1}$, it is attained by
\begin{equation}\label{eq:extremal-potential}
 W(x)=\diag\big((r+1)\sech^2(rx),0,\ldots,0\big).
\end{equation}
\end{theorem}
```

### 4.3 Sharp one-dimensional Lieb–Thirring constants — *linked from the scope note*

[`preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:37`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/build/sections/introduction.tex#L37):

```latex
\begin{theorem}\label{thm:main}
For every $1/2<\gamma<3/2$ and every nonnegative
$W\in L^{\gamma+1/2}(\R)$,
\begin{equation}\label{eq:main}
 \Tr(H_{-W})_-^\gamma
 \le 2\left(\frac{\gamma-1/2}{\gamma+1/2}\right)^{\gamma-1/2}
       L_{\gamma,1}^{\cl}\int_\R W^{\gamma+1/2}.
\end{equation}
The constant is optimal and equals $L_{\gamma,1}^{(1)}$.
More precisely, if $r=(\gamma-1/2)^{-1}$, equality is attained by
$W(x)=(r+1)\sech^2(rx)$.
\end{theorem}
```

## 5. Your classification

Enter one line for family `262` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
