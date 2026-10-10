# Family 261 — Localization and delocalization in the Anderson model

Subject: Mathematical physics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 261 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Resolves the predicted spectral contrast for the lattice Anderson model with independent uniform site potentials. In dimension two, every positive disorder strength gives almost surely pure-point spectrum. In every fixed dimension $d\ge3$, sufficiently weak positive disorder gives purely absolutely continuous spectrum on a fixed open interval with nonzero spectral weight.

## 2. The repository's own scope note ([`lean/docs/261.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/261.md), verbatim; relative links made absolute)

# Localization and delocalization in the Anderson model

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/paper.pdf)

## Scope

The linked formalization proves a supporting spectral statement for the nearest-neighbor Anderson operator on $\mathbb Z^2$. For every disorder strength $h>0$ with independent site potentials uniform on $[-h,h]$, it constructs the bounded self-adjoint operator almost surely and identifies its spectrum as the real interval $[-4-h,4+h]$.

This selected statement identifies the spectral set. It does not assert the pure-point spectral type claimed in the accompanying paper.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Almost-sure spectrum of the planar Anderson operator | [PlanarAndersonSpectrum.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PlanarAndersonSpectrum.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`PlanarAndersonSpectrum.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PlanarAndersonSpectrum.lean) — the lab's result label: *Almost-sure spectrum of the planar Anderson operator*. Comparator config [`PlanarAndersonSpectrum.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PlanarAndersonSpectrum.json): theorem(s) `OAI.PlanarAnderson.anderson_spectrum_ae`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.MathematicalPhysics.PlanarAnderson.Spectrum`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Absolutely Continuous Spectrum for Weak-Disorder Anderson Models in Dimensions at Least Three — *not linked from the scope note*

[`preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026)

`theorem` `thm:main` at [`build/01-introduction.tex:33`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Absolutely-Continuous-Spectrum-for-Weak-Disorder-Anderson-Models-in-Dimensions-at-Least-Three-September-23-2026/build/01-introduction.tex#L33):

```latex
\begin{theorem}\label{thm:main}
There is a fixed sufficiently small number $e_2\in(0,1/100)$ such that,
for every fixed integer $d\ge3$, there is a number $\lambda_d>0$
with the following property. Set
\begin{equation}\label{eq:energy-windows}
 I_d=
 \begin{cases}
   (-6+e_2/2,-6+e_2),&d=3,\\
   -2d+(1/200,1/100),&d\ge4.
 \end{cases}
\end{equation}
Then
for every fixed $0<\lambda<\lambda_d$, almost surely
\[
 I_d\subset\sigma(H_{\lambda,\omega}),\qquad
 \chi_{I_d}(H_{\lambda,\omega})\ell^2(\ZZ^d)
       \subset\mathcal H_{\mathrm{ac}}(H_{\lambda,\omega}).
\]
In particular, the spectral restriction to $I_d$ is purely absolutely
continuous and $\chi_{I_d}(H_{\lambda,\omega})\ne0$.
For $d\ge4$, one may take $\lambda_d=\sqrt3\,2^{-n_*(d)}$, where the finite-matrix
specification of $n_*(d)$ is given in Definition~\ref{def:threshold}.
For $d=3$, the proof supplies an existential positive threshold.
\end{theorem}
```

### 4.2 Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder — *linked from the scope note*

[`preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026)

`theorem` `main:theorem` at [`build/sections/introduction.tex:19`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/introduction.tex#L19):

```latex
\begin{theorem}\label{main:theorem}
For each fixed $h>0$, almost surely $H_v$ has pure-point spectral type,
admits a complete orthonormal eigenbasis, and has spectrum
\[
 \sigma(H_v)=[-4-h,4+h].
\]
Its eigenvalues are dense in this interval. The probability-one event
in this statement is allowed to depend on $h$.
\end{theorem}
```

## 5. Your classification

Enter one line for family `261` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
