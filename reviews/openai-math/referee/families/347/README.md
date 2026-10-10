# Family 347 — Counterexamples to strong forms of Arnold's fixed-point conjecture

Subject: Differential geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 347 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Disproves stable-Morse lower bounds for nondegenerate Hamiltonian fixed points: on simply connected closed K\"ahler manifolds of real dimension $22$, the deficit below the stable Morse number is unbounded. A separate Hamiltonian diffeomorphism of the complex quadric threefold has exactly three fixed points, fewer than the four critical points required of every smooth function.

## 2. The repository's own scope note ([`lean/docs/347.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/347.md), verbatim; relative links made absolute)

# Counterexamples to stable-Morse and strong Arnold fixed-point bounds

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Three fixed points on the symplectic quadric threefold](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf)

## Scope

The critical-number form of Arnold's fixed-point conjecture predicts at least as many fixed points as the minimum number of critical points of a smooth function. The formalized counterexample is a Hamiltonian diffeomorphism of the complex quadric threefold with exactly three fixed points, while every smooth function on that manifold has at least four critical points. At least one fixed point is degenerate. The separate nondegenerate Morse-number construction is not included.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Three-fixed-point Arnold counterexample | [ArnoldCounterexample.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ArnoldCounterexample.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`ArnoldCounterexample.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ArnoldCounterexample.lean) — the lab's result label: *Three-fixed-point Arnold counterexample*. Comparator config [`ArnoldCounterexample.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ArnoldCounterexample.json): theorem(s) `OAI.ArnoldCounterexample.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.Arnold.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Hamiltonian Fixed Points Below the Stable Morse Number in Dimension Twenty-Two — *not linked from the scope note*

[`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:37`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026/build/sections/introduction.tex#L37):

```latex
\begin{theorem}\label{thm:main}
For every integer $m\geq1$, there exist a simply connected closed Kähler
manifold $(M_m,\omega_m)$ of real dimension $22$ and a smooth one-periodic
Hamiltonian $H_m$ such that all fixed points of $\phi_{H_m}^1$ are
nondegenerate and
\begin{align*}
 \SM(M_m)&=80+1968m,\\
 \#\Fix(\phi_{H_m}^1)
 &=\#\Fix_0(\phi_{H_m}^1;H_m)=80+1952m.
\end{align*}
Consequently, with $\delta=1/128$, for every $R>0$ some member of this
family satisfies
\[
 \SM(M_m)\geq R,\qquad
 \#\Fix(\phi_{H_m}^1)\leq(1-\delta)\SM(M_m).
\]
\end{theorem}
```

### 4.2 Sharpness of the Cyclic Integral Floer Bound Below the Stable Morse Number — *not linked from the scope note*

[`preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:52`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/build/sections/introduction.tex#L52):

```latex
\begin{theorem}
\label{thm:main}
There exist a simply connected closed K\"ahler manifold $(M,\omega)$
of complex dimension $1666$ and a smooth one-periodic Hamiltonian $H$
such that
\[
 c_1(TM)(\pi_2(M))=\Z,
\]
every fixed point of $\phi_H^1$ is nondegenerate, and
\begin{align*}
 \#\Fix(\phi_H^1)
 &=\#\Fix_0(\phi_H^1;H)
  =\beta_{\Z}^{\mathrm{cyc}}(M)=1\,872\,232,\\
 \SM(M)&=\beta_{\Z}^{\mathrm{cyc}}(M)+32=1\,872\,264.
\end{align*}
\end{theorem}
```

### 4.3 Hamiltonian Fixed Points Below the Stable Morse Number — *not linked from the scope note*

[`preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:26`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/build/sections/introduction.tex#L26):

```latex
\begin{theorem}\label{thm:main}
There exist a simply connected closed Kähler manifold $(M,\omega)$ and a smooth one-periodic Hamiltonian $H$ such that every fixed point of $\phi_H^1$ is nondegenerate and
\[
 \#\Fix_0(\phi_H^1;H)=\#\Fix(\phi_H^1)=\SM(M)-16.
\]
One may take $\dim_{\R}M=1412$, with $\SM(M)=318968$ and $\#\Fix(\phi_H^1)=318952$.
\end{theorem}
```

### 4.4 A nondegenerate counterexample to the Morse-number Arnold bound — *not linked from the scope note*

[`preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026)

`theorem` `thm:main` at [`build/sections/01-introduction.tex:32`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026/build/sections/01-introduction.tex#L32):

```latex
\begin{theorem}\label{thm:main}
There exist a closed connected symplectic manifold $(M,\omega)$ of real
dimension twelve and a smooth one-periodic Hamiltonian $H$ such that every
fixed point of $\phi_H^1$ is nondegenerate and
\[
\#\Fix_0(\phi_H^1;H)=\#\Fix(\phi_H^1)
                   =\chi(M)+128<\Morse(M).
\]
\end{theorem}
```

### 4.5 Three fixed points on the symplectic quadric threefold — *linked from the scope note*

[`preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026)

`theorem` `thm:counterexample` at [`build/sections/00-introduction.tex:56`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/build/sections/00-introduction.tex#L56):

```latex
\begin{theorem}\label{thm:counterexample}
There is a smooth Hamiltonian diffeomorphism $\phi$ of the closed connected
symplectic six-manifold $Q^3$ such that
\begin{equation}\label{eq:counterexample}
 \#\Fix(\phi)=3<4=\Crit(Q^3)
                  =\operatorname{cuplength}(Q^3;\mathbb Q).
\end{equation}
At least one fixed point of $\phi$ is degenerate.
\end{theorem}
```

## 5. Your classification

Enter one line for family `347` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
