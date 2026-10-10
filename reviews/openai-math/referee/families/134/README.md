# Family 134 — Generalized star height at most three

Subject: Theoretical computer science. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 134 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Every regular language over a finite alphabet has a generalized regular expression with at most three nested Kleene stars, allowing union, concatenation and complement over the same alphabet. This establishes an absolute bound independent of automaton size, resolving the uniform-boundedness version of the generalized star-height problem.

## 2. The repository's own scope note ([`lean/docs/134.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/134.md), verbatim; relative links made absolute)

# Generalized star height at most three

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Finite Monoid Computations and a Uniform Generalized Star-Height Bound](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026.pdf)
- [Generalized Star Height at Most Four](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/Generalized-Star-Height-at-Most-Four-September-25-2026.pdf)
- [Generalized Star Height at Most Three](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/article.pdf)

## Scope

Generalized star height measures the nesting of Kleene stars in regular expressions that also allow Boolean operations. The formalization proves that every regular language over a finite alphabet has a generalized expression over the same alphabet of star height at most three. This is stronger than the bound of thirteen in the accompanying finite-monoid paper. The selected statement asserts the uniform expression bound, without separately encoding every construction step of that paper.

The formalization proves that every regular language over a finite alphabet has a generalized regular expression over that same alphabet with star height at most three. Generalized expressions allow Boolean operations as well as concatenation and Kleene star. The bound of three implies the accompanying paper's bound of four; the selected statement concerns the expression bound itself.

Generalized star height measures the nesting of Kleene stars in regular expressions that also allow Boolean operations. The formalization proves that every regular language over a finite alphabet has a generalized regular expression over that same alphabet of star height at most three. Complements are taken in the same free monoid. This is the paper's uniform bound.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Uniform generalized star-height bound of three | [GeneralizedStarHeight.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GeneralizedStarHeight.lean) |
| Generalized star height at most three | [GeneralizedStarHeight.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GeneralizedStarHeight.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`GeneralizedStarHeight.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GeneralizedStarHeight.lean) — the lab's result label: *Uniform generalized star-height bound of three / Generalized star height at most three*. Comparator config [`GeneralizedStarHeight.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GeneralizedStarHeight.json): theorem(s) `OAI.GeneralizedStarHeight.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Computability.StarHeight.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Generalized Star Height at Most Three** — [`preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/introduction.tex:29`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/build/sections/introduction.tex#L29):

```latex
\begin{theorem}\label{thm:main}
For every finite alphabet $\Sigma$ and every regular language
$L\subseteq\Sigma^*$,
\[
                            h_\Sigma(L)\le3.
\]
\end{theorem}
```

**Generalized Star Height at Most Four** — [`preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/01-introduction.tex:24`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/build/sections/01-introduction.tex#L24) (further candidate):

```latex
\begin{theorem}\label{thm:main}
For every finite alphabet $\Sigma$ and every regular language
$L\subseteq\Sigma^*$, one has $h_\Sigma(L)\le4$.
\end{theorem}
```

**Finite Monoid Computations and a Uniform Generalized Star-Height Bound** — [`preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/introduction.tex:33`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/build/sections/introduction.tex#L33) (further candidate):

```latex
\begin{theorem}\label{thm:main}
For every finite alphabet \(\Sigma\) and every regular language
\(L\subseteq\Sigma^*\),
\[
                         h_\Sigma(L)\le 13.
\]
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Finite Monoid Computations and a Uniform Generalized Star-Height Bound](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026); [Generalized Star Height at Most Four](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Generalized-Star-Height-at-Most-Four-September-25-2026); [Generalized Star Height at Most Three](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Generalized-Star-Height-at-Most-Three-September-25-2026)

## 5. Your classification

Enter one line for family `134` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
