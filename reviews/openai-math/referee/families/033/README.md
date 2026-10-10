# Family 033 — Campana's orbifold Iitaka conjecture and logarithmic subadditivity

Subject: Algebraic and complex geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 033 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves Campana's orbifold Iitaka subadditivity conjecture for smooth Fujiki-class-$\mathcal C$ manifolds with rational simple-normal-crossing boundaries. For projective fibrations $f:U\to V$ of smooth complex quasi-projective varieties with connected fibers, general fiber $F$, and $\bar\kappa(V)\ge0$, proves Popa's inequality $\bar\kappa(U)\ge\kappa(F)+\max\{\bar\kappa(V),\operatorname{Var}(f)\}$, where variation measures the whole geometric generic fiber.

## 2. The repository's own scope note ([`lean/docs/033.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/033.md), verbatim; relative links made absolute)

# Iitaka subadditivity, variation, and logarithmic additivity

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [The reverse logarithmic Kodaira inequality and additivity](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/paper.pdf)

## Scope

The paper studies logarithmic Kodaira additivity for connected-fiber morphisms of smooth projective reduced simple-normal-crossing pairs that are smooth on all boundary strata away from the base boundary. The linked formalization proves the negative-fiber branch: for a very general base point, if the logarithmic Kodaira dimension of the fiber is $-\infty$, then the total logarithmic Kodaira dimension equals the sum of the base and fiber dimensions and is $-\infty$. Every positive-degree logarithmic pluriform section on the total space then vanishes.

The finite-dimension and negative-base branches of the paper's additivity theorem are outside this selected statement.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Logarithmic Kodaira additivity in the negative-fiber branch | [LogKodairaFiberNegative.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LogKodairaFiberNegative.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`LogKodairaFiberNegative.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LogKodairaFiberNegative.lean) — the lab's result label: *Logarithmic Kodaira additivity in the negative-fiber branch*. Comparator config [`LogKodairaFiberNegative.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/LogKodairaFiberNegative.json): theorem(s) `OAI.ReverseLogKodaira.SmoothProjectiveVariety.veryGenerally_fiber_negative_branch`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.AlgebraicGeometry.LogKodaira.FiberNegative`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Orbifold and logarithmic Iitaka subadditivity — *not linked from the scope note*

[`preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026)

`theorem` `main:orbifold` (Orbifold subadditivity) at [`build/sections/introduction.tex:135`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026/build/sections/introduction.tex#L135):

```latex
\begin{theorem}[Orbifold subadditivity]\label{main:orbifold}
Let $X$ be a smooth compact connected complex manifold in Fujiki
class $\mathcal C$, let $\Delta$ be a rational SNC boundary, and
let $f:X\to Y$ be a surjective holomorphic map with connected
fibers onto a normal compact irreducible complex space.
For a very general smooth fiber $F$, put $\Delta_F=\Delta|_F$.
Then
\begin{equation}\label{main:inequality}
 \kappa(X,K_X+\Delta)
 \geq\kappa(F,K_F+\Delta_F)+\kappa(f\mid\Delta).
\end{equation}
\end{theorem}
```

### 4.2 Logarithmic Kodaira dimension and whole-fiber variation — *not linked from the scope note*

[`preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026)

`theorem` `thm:main` (Logarithmic variation) at [`build/sections/01-introduction.tex:38`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/build/sections/01-introduction.tex#L38):

```latex
\begin{theorem}[Logarithmic variation]\label{thm:main}
Let $f:U\to V$ be a projective surjective morphism with connected fibers
between smooth connected quasi-projective complex varieties.
Assume $\kbar(V)\geq0$, and let $F$ be its geometric generic fiber.
Then
\begin{equation}\label{eq:main}
 \kbar(U)\geq\kappa(F)+\max\{\kbar(V),\Var(f)\}.
\end{equation}
\end{theorem}
```

Also located: `theorem` `num:main` (The dimension retained by interpolation) at [`build/sections/08-numerical-extension.tex:20`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026/build/sections/08-numerical-extension.tex#L20).

### 4.3 The reverse logarithmic Kodaira inequality and additivity — *linked from the scope note*

[`preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026)

`theorem` `thm:upper-bound` (Reverse logarithmic Kodaira inequality) at [`build/sections/introduction.tex:30`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/build/sections/introduction.tex#L30):

```latex
\begin{theorem}[Reverse logarithmic Kodaira inequality]\label{thm:upper-bound}
Under these hypotheses,
\begin{equation}\label{eq:upper-bound}
 \kappa(X,L_X)\leq\kappa(Y,L_Y)+\kappa(F,L_F).
\end{equation}
If either term on the right is $-\infty$, then
$H^0(X,mL_X)=0$ for every $m>0$.
\end{theorem}
```

### 4.4 Projective Hodge lines and ordinary Iitaka subadditivity — *not linked from the scope note*

[`preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026)

`theorem` `thm:ordinary` (Ordinary Iitaka subadditivity) at [`build/sections/01-introduction.tex:48`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026/build/sections/01-introduction.tex#L48):

```latex
\begin{theorem}[Ordinary Iitaka subadditivity]\label{thm:ordinary}\label{altord:ordinary-subadditivity}
Let $k$ be an algebraically closed field of characteristic zero, and
let $f:X\to Z$ be a surjective projective morphism with connected
fibres between smooth connected projective $k$-varieties. If $F$ is
its geometric generic fibre, then
\[
                     \kappa(X)\geq\kappa(F)+\kappa(Z).
\]
\end{theorem}
```

### 4.5 B-semiampleness for compact log-smooth Kähler fibrations — *not linked from the scope note*

[`preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:83`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026/build/sections/introduction.tex#L83):

```latex
\begin{theorem}\label{thm:main}
Under the assumptions above, \(\mathbf M\) is b-semiample.
More explicitly, there is a smooth compact K\"ahler modification
\(\mu_0:S\to X\) such that:
\begin{enumerate}[label=\textup{(\alph*)}]
\item for every smooth compact K\"ahler modification \(\nu:S_1\to S\),
\[
 M_{S_1}=\nu^*M_S\quad\text{in }\Pic(S_1)_{\Q};
\]
\item for some positive integer \(m\), the actual line bundle
representing \(mM_S\) is generated by its global holomorphic sections.
\end{enumerate}
The theorem includes a point base and relative dimension zero.
No projectivity of \(f\), \(X\), or \(Y\) is assumed.
\end{theorem}
```

## 5. Your classification

Enter one line for family `033` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
