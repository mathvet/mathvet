# Family 072 — Brennan's conjecture and a counterexample to Kraetzer's prediction

Subject: Real and complex analysis. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 072 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves Brennan's conjecture: for every conformal bijection $\phi$ from a simply connected plane domain onto the disk, $|\phi'|^s$ is area-integrable for $4/3<s<4$. The sharp universal integral-means identity is $B_{\mathcal S}(t)=|t|-1$ for $t\le-2$. A strict bound $B_b(-1)<1/4$ for bounded univalent functions disproves Kraetzer's prediction at that parameter.

## 2. The repository's own scope note ([`lean/docs/072.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/072.md), verbatim; relative links made absolute)

# Brennan's conjecture and the integral-means spectrum

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Brennan's conjecture and sharp inverse-square integral means](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/paper.pdf)
- [A strict inverse-first-power bound for univalent functions](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/paper.pdf)

## Scope

Brennan's conjecture asserts that $|\phi'|^s$ is area-integrable for $4/3<s<4$ when $\phi$ conformally maps a simply connected plane domain with nontrivial spherical boundary onto the disk. The formalization establishes this interval, along with area integrability of $|f'|^t$ for univalent disk maps when $-2<t<2/3$.

It also gives the uniform inverse-square radial-mean bound with exponent $-1-\varepsilon$ for every $\varepsilon>0$ and the spectrum value $B_{\mathcal S}(-2)=1$. The Koebe map and its inverse give divergence at all four boundary exponents.

Kraetzer's proposed integral-means spectrum predicts $B_b(-1)=1/4$ for bounded univalent maps. The formalized result proves $B_b(-1)<1/4$, contradicting that prediction.

The underlying estimate gives constants $0<\varepsilon<1/4$ and $C<\infty$ such that the normalized circular mean of $|f'|^{-1}$ is at most $C(1-r)^{-1/4+\varepsilon}$ for every normalized univalent disk map and $1/2\le r<1$. The bound requires neither bounded image nor boundary regularity, and no numerical value of $\varepsilon$ is specified.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Brennan and inverse-square integral-means bounds | [Brennan.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Brennan.lean) |
| Sharp endpoint divergence | [BrennanSharp.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BrennanSharp.lean) |
| Strict inverse-first-power bound and consequences | [StrictMeans.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/StrictMeans.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`Brennan.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Brennan.lean) — the lab's result label: *Brennan and inverse-square integral-means bounds*. Comparator config [`Brennan.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/Brennan.json): theorem(s) `OAI.Brennan.main_theorem`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.IntegralMeans.Main`.
- [`BrennanSharp.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BrennanSharp.lean) — the lab's result label: *Sharp endpoint divergence*. Comparator config [`BrennanSharp.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BrennanSharp.json): theorem(s) `OAI.Brennan.Sharp.sharp_endpoints`; permitted axioms `propext`, `Classical.choice`, `Quot.sound`; solution module `OAI.Analysis.IntegralMeans.SharpEndpoints`.
- [`StrictMeans.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/StrictMeans.lean) — the lab's result label: *Strict inverse-first-power bound and consequences*. Comparator config [`StrictMeans.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/StrictMeans.json): theorem(s) `OAI.StrictInverseFirstPower.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.StrictMeans.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Brennan's conjecture and sharp inverse-square integral means** — [`preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/paper.pdf); `theorem` `thm:main` (Brennan's conjecture and inverse-square means) at [`build/sections/00-introduction.tex:52`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/build/sections/00-introduction.tex#L52):

```latex
\begin{theorem}[Brennan's conjecture and inverse-square means]
\label{thm:main}
For every $\varepsilon>0$ there is $C_\varepsilon<\infty$ such that
\begin{equation}\label{eq:main-uniform}
 M_{-2}[f'](r)\le C_\varepsilon(1-r)^{-1-\varepsilon}
 \qquad\left(f\in\SSS,\ \frac12\le r<1\right).
\end{equation}
Moreover, $B_{\SSS}(-2)=1$.

Let $W\subset\CC$ be any simply connected domain whose boundary in
the Riemann sphere contains at least two points. Every conformal
bijection $\varphi:W\to\DD$ satisfies
\[
 \int_W|\varphi'(z)|^s\dd A(z)<\infty
 \qquad\left(\frac43<s<4\right).
\]
Equivalently, every univalent map $f:\DD\to\CC$ satisfies
\[
 \int_{\DD}|f'(w)|^t\dd A(w)<\infty
 \qquad\left(-2<t<\frac23\right).
\]
\end{theorem}
```

**A strict inverse-first-power bound for univalent functions** — [`preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/paper.pdf); `theorem` `thm:main` (Uniform inverse-first-power bound) at [`build/sections/00-introduction.tex:44`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/sections/00-introduction.tex#L44) (further candidate):

```latex
\begin{theorem}[Uniform inverse-first-power bound]\label{thm:main}
There exist constants \(0<\varepsilon<1/4\) and \(C<\infty\) such that
\begin{equation}\label{eq:uniform}
 M_{-1}[f'](r)\le C(1-r)^{-1/4+\varepsilon}
 \qquad\text{for every }f\in\SSS\text{ and every }1/2\le r<1.
\end{equation}
Consequently \(B_b(-1)<1/4\), and Kraetzer's conjectured identity
\eqref{eq:kraetzer} is false.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Brennan's conjecture and sharp inverse-square integral means](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026); [A strict inverse-first-power bound for univalent functions](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026)

## 5. Your classification

Enter one line for family `072` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
