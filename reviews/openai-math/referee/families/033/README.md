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

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**The reverse logarithmic Kodaira inequality and additivity** — [`preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/paper.pdf); `theorem` `thm:upper-bound` (Reverse logarithmic Kodaira inequality) at [`build/sections/introduction.tex:30`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026/build/sections/introduction.tex#L30):

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

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Orbifold and logarithmic Iitaka subadditivity](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Orbifold-and-logarithmic-Iitaka-subadditivity-September-26-2026); [Logarithmic Kodaira dimension and whole-fiber variation](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Logarithmic-Kodaira-dimension-and-whole-fiber-variation-September-26-2026); [The reverse logarithmic Kodaira inequality and additivity](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-reverse-logarithmic-Kodaira-inequality-and-additivity-September-26-2026); [Projective Hodge lines and ordinary Iitaka subadditivity](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Projective-Hodge-lines-and-ordinary-Iitaka-subadditivity-September-27-2026); [B-semiampleness for compact log-smooth Kähler fibrations](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/B-semiampleness-for-compact-log-smooth-Kahler-fibrations-September-10-2026)

## 5. Your classification

Enter one line for family `033` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
