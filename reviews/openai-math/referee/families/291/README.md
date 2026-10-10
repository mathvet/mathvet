# Family 291 — Toms--Winter and equivariant Jiang--Su stability

Subject: Operator algebras. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 291 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves equivariant Jiang--Su stability for every countable discrete amenable group action on a simple separable unital infinite-dimensional nuclear stably finite Jiang--Su-stable $C^*$-algebra, resolving this case of Szab\'o's conjecture without restrictions on trace dynamics. The family also proves the unital Toms--Winter conjecture, equating strict comparison, finite nuclear dimension and Jiang--Su stability in the simple separable unital infinite-dimensional nuclear setting.

## 2. The repository's own scope note ([`lean/docs/291.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/291.md), verbatim; relative links made absolute)

# Cuntz comparison, nuclear dimension, and equivariant Jiang–Su stability

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Tracial projection methods and uniform property $\Gamma$](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf)

## Scope

The formalization proves that real rank zero of the uniform tracial ultrapower of the uniform tracial completion implies uniform property $\Gamma$ for a simple separable unital infinite-dimensional nuclear stably finite $C^*$-algebra with traces. The conclusion holds at every specified free ultrafilter under the corresponding real-rank-zero hypothesis.

The linked comparison results also prove Jiang–Su absorption and uniform property $\Gamma$ for simple separable unital infinite-dimensional nuclear algebras with strict comparison, and for the stated stably projectionless nuclear algebras with bounded densely finite traces, a nonempty compact normalized trace base, and the prescribed finite-target-rank comparison condition.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Uniform property $\Gamma$ from tracial real rank zero | [UniformGamma.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/UniformGamma.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`UniformGamma.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/UniformGamma.lean) — the lab's result label: *Uniform property $\Gamma$ from tracial real rank zero*. Comparator config [`UniformGamma.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/UniformGamma.json): theorem(s) `OAI.ComparatorModel.CurrentMain.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.TracialSplitting.Challenge`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Equivariant Jiang–Su Stability for Amenable Actions in the Unital Stably Finite Case — *not linked from the scope note*

[`preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:10`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/build/sections/introduction.tex#L10):

```latex
\begin{theorem}\label{thm:main}
Let \(A\) be a simple, separable, unital, infinite-dimensional, nuclear,
stably finite complex \(\mathrm C^*\)-algebra satisfying
\(A\cong A\otimes\Zalg\). Let \(G\) be a countable discrete amenable group
and let \(\alpha:G\to\Aut(A)\) be any action. Put
\[
 B=A\otimes\Zalg,\qquad
 \beta_g=\alpha_g\otimes\operatorname{id}_{\Zalg}.
\]
There are a unital \(*\)-isomorphism \(\Phi:A\to B\) and unitaries
\(u_g\in B\), \(g\in G\), such that
\begin{align}
 u_e&=1,& u_{gh}&=u_g\beta_g(u_h),\label{eq:cocycle}\\
 \Phi(\alpha_g(a))&=u_g\beta_g(\Phi(a))u_g^*
 &&(g\in G,\ a\in A).\label{eq:conjugacy}
\end{align}
\end{theorem}
```

### 4.2 Cuntz comparison and Jiang–Su absorption — *not linked from the scope note*

[`preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026)

`theorem` `ext:thm:main` (Simple comparison and absorption) at [`build/sections/introduction.tex:61`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/build/sections/introduction.tex#L61):

```latex
\begin{theorem}[Simple comparison and absorption]
\label{ext:thm:main}
Let $A$ be a separable simple nuclear non-elementary $C^*$-algebra.
If $A$ has strict comparison in the sense of
Equation~\eqref{ext:eq:comparison}, then $A\cong A\otimes_{\min}\Z$.
\end{theorem}
```

### 4.3 Nuclear dimension and Jiang–Su stability without elementary subquotients — *not linked from the scope note*

[`preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026)

`theorem` `thm:main` (Nonsimple nuclear regularity) at [`build/sections/01_introduction.tex:24`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/build/sections/01_introduction.tex#L24):

```latex
\begin{theorem}[Nonsimple nuclear regularity]
\label{thm:main}
\label{intro:regularity}
Let $A$ be a separable nuclear complex $C^*$-algebra with no nonzero
elementary ideal subquotients. The following conditions are equivalent:
\begin{enumerate}
\item $\nucdim(A)<\infty$;
\item $A\cong A\otimes\Z$;
\item $\nucdim(A)\le1$.
\end{enumerate}
\end{theorem}
```

Also located: `theorem` `intro:main` (Sharp bound after Jiang--Su absorption) at [`build/sections/01_introduction.tex:70`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/build/sections/01_introduction.tex#L70).

### 4.4 Tracial projection methods and uniform property Gamma — *linked from the scope note*

[`preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026)

`theorem` `r:thm:main` (Real rank zero and uniform property $\Gamma$) at [`build/sections/01_introduction.tex:57`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/build/sections/01_introduction.tex#L57):

```latex
\begin{theorem}[Real rank zero and uniform property $\Gamma$]
\label{r:thm:main}
Let $A$ be a unital, separable, simple, infinite-dimensional, nuclear,
stably finite $C^*$-algebra with $T(A)\ne\varnothing$, and let
$B=\overline A^{T(A)}$. Fix any free ultrafilter $\omega$ on $\N$.
If $B^\omega$ has real rank zero in its quotient $C^*$-norm, then there is
a projection $p\in B^\omega\cap B'$ such that
\[
 \lambda(px)=\tfrac12\lambda(x)
 \qquad(x\in B,\ \lambda\in\Lambda_\omega).
\]
In particular, $A$ has uniform property $\Gamma$.
\end{theorem}
```

Also located: `theorem` `u:thm:main` (The direct unital comparison route) at [`build/sections/01_introduction.tex:207`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/build/sections/01_introduction.tex#L207).

Also located: `theorem` `n:thm:main` (The direct stably projectionless route) at [`build/sections/01_introduction.tex:237`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/build/sections/01_introduction.tex#L237).

## 5. Your classification

Enter one line for family `291` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
