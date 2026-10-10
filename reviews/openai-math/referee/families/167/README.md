# Family 167 — Pinned distances and a power saving for planar unit distances

Subject: Combinatorics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 167 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves the weak pinned Erd\H{o}s distance conjecture: for every fixed $\varepsilon>0$, all but $o(n)$ points of any $n$-point planar set determine at least $n^{1-\varepsilon}$ distinct nonzero distances. A complementary theorem bounds the number of unit-distance pairs by $O(n^{4/3-\delta})$ for an absolute $\delta>0$.

## 2. The repository's own scope note ([`lean/docs/167.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/167.md), verbatim; relative links made absolute)

# Planar distinct distances and unit-distance bounds

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [The weak pinned planar distance theorem](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/paper.pdf)
- [A power saving for planar unit distances](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf)

## Scope

The formalized result shows that large repeated distance fibers are rare in arbitrary finite planar point sets. For each fixed $s>0$, the largest possible fraction of ordered distinct pairs $(x,y)$ whose distance from the pin $x$ occurs at least $n^s$ times tends to zero as the set size $n$ grows. Consequently, for every $\varepsilon>0$, the fraction of pins determining fewer than $n^{1-\varepsilon}$ distances tends uniformly to zero. The separate unit-distance power-saving theorem is not included.

The planar unit-distance problem asks how many pairs at distance one can occur among $n$ points. The formalization proves that there are absolute constants $C>0$ and $1\le\beta<4/3$ such that every finite planar point set of size $n$ determines at most $Cn^\beta$ unordered unit-distance pairs. The same constants work for every $n$, giving a fixed power improvement over the classical exponent $4/3$.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Weak pinned planar distance theorem | [PinnedDistances.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PinnedDistances.lean) |
| Power saving for planar unit distances | [PlanarUnitDistances.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PlanarUnitDistances.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`PinnedDistances.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PinnedDistances.lean) — the lab's result label: *Weak pinned planar distance theorem*. Comparator config [`PinnedDistances.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PinnedDistances.json): theorem(s) `OAI.WeakPinned.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.PinnedDistances.Main`.
- [`PlanarUnitDistances.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PlanarUnitDistances.lean) — the lab's result label: *Power saving for planar unit distances*. Comparator config [`PlanarUnitDistances.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PlanarUnitDistances.json): theorem(s) `OAI.PlanarUnitDistances.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.UnitDistances.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 The weak pinned planar distance theorem — *linked from the scope note*

[`preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:30`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/build/sections/introduction.tex#L30):

```latex
\begin{theorem}\label{thm:main}
For every fixed $s>0$, one has $F_n(s)\longrightarrow0$ as
$n\longrightarrow\infty$.
\end{theorem}
```

### 4.2 A power saving for planar unit distances — *linked from the scope note*

[`preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-power-saving-for-planar-unit-distances-September-23-2026)

`theorem` `thm:main` at [`build/sections/00-introduction.tex:12`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-power-saving-for-planar-unit-distances-September-23-2026/build/sections/00-introduction.tex#L12):

```latex
\begin{theorem}\label{thm:main}
There are absolute constants \(0<C<\infty\) and \(1\le\beta<4/3\) such that
\(u(n)\le Cn^\beta\) for every nonnegative integer \(n\).
\end{theorem}
```

## 5. Your classification

Enter one line for family `167` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
