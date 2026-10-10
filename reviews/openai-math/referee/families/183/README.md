# Family 183 — Power savings for planar halving lines and $k$-sets

Subject: Combinatorics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 183 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Improves the planar halving-line bound to $O(n^{4/3-\varepsilon})$ for sets with no three collinear and an absolute $\varepsilon>0$. More generally, an $n$-point set with no three collinear has $O(n(k+1)^{1/3-\varepsilon_0})$ strictly separable $k$-subsets for $1\le k\le n/2$, with an absolute $\varepsilon_0>0$. The constants and positive exponents are nonquantitative.

## 2. The repository's own scope note ([`lean/docs/183.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/183.md), verbatim; relative links made absolute)

# Power savings for planar halving lines and <i>k</i>-sets

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [A power saving for planar halving lines](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/main.pdf)

## Scope

A halving pair in an even planar point set is a pair whose line leaves equally many remaining points on each side. The formalization proves that some absolute $\varepsilon>0$ and $C$ bound the number of halving pairs by $Cn^{4/3-\varepsilon}$ for every sufficiently large even $n$ and every $n$-point set with no three collinear. It also proves a bound of the same form for all level-switch counts under the additional generic-position assumptions in the statement. The constants are existential.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Power-saving bounds for halving pairs and level switches | [HalvingLines.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HalvingLines.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`HalvingLines.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HalvingLines.lean) — the lab's result label: *Power-saving bounds for halving pairs and level switches*. Comparator config [`HalvingLines.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HalvingLines.json): theorem(s) `OAI.PlanarHalving.power_bounds`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Combinatorics.HalvingLines.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 A power saving for planar halving lines — *linked from the scope note*

[`preprints/A-power-saving-for-planar-halving-lines-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-power-saving-for-planar-halving-lines-September-25-2026)

`theorem` `thm:halving-power` at [`build/sections/introduction.tex:9`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-power-saving-for-planar-halving-lines-September-25-2026/build/sections/introduction.tex#L9):

```latex
\begin{theorem}\label{thm:halving-power}
There exist absolute constants $\varepsilon>0$, $C<\infty$, and $n_0$
such that, for every even $n\ge n_0$ and every $n$-point set
$P\subset\mathbb R^2$ with no three collinear,
\[
 h(P)\le C n^{4/3-\varepsilon}.
\]
\end{theorem}
```

## 5. Your classification

Enter one line for family `183` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
