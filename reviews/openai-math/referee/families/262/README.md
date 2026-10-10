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

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Sharp one-dimensional Lieb–Thirring constants** — [`preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/introduction.tex:37`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026/build/sections/introduction.tex#L37):

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

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Equality cases in the sharp one-dimensional matrix Lieb–Thirring inequality](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026); [Sharp one-dimensional Lieb–Thirring inequalities for matrix potentials](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-one-dimensional-Lieb-Thirring-inequalities-for-matrix-potentials-October-5-2026); [Sharp one-dimensional Lieb–Thirring constants](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharp-One-Dimensional-Lieb-Thirring-Constants-September-23-2026)

## 5. Your classification

Enter one line for family `262` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
