# Family 299 — The Kirchberg--R\o rdam character criterion

Subject: Operator algebras. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 299 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

A nonzero unital separable complex $C^*$-algebra is Jiang--Su stable exactly when its norm central-sequence algebra has no characters, for every free ultrafilter. This answers the Kirchberg--R\o rdam character question. Also, the infinite minimal tensor power of every such algebra without characters is Jiang--Su stable, answering the Dadarlat--Toms question.

## 2. The repository's own scope note ([`lean/docs/299.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/299.md), verbatim; relative links made absolute)

# The Kirchberg–Rørdam character criterion and infinite tensor-power Jiang–Su stability

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [The Kirchberg–Rørdam character criterion](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/paper.pdf)

## Scope

The Kirchberg–Rørdam criterion relates Jiang–Su absorption to characters of the central-sequence algebra. The formalized result proves that, for every nonzero unital separable complex $C^*$-algebra $A$ and every free ultrafilter on $\mathbb N$, the norm central-sequence algebra has no nonzero character exactly when $A\cong A\otimes_{\min}\mathcal Z$. No nuclearity, simplicity, trace, or comparison hypothesis is imposed.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Kirchberg–Rørdam character criterion | [CharacterCriterion.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CharacterCriterion.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`CharacterCriterion.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CharacterCriterion.lean) — the lab's result label: *Kirchberg–Rørdam character criterion*. Comparator config [`CharacterCriterion.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CharacterCriterion.json): theorem(s) `OAI.KirchbergRordam.character_criterion`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.CharacterCriterion.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 The Kirchberg–Rørdam character criterion — *linked from the scope note*

[`preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:37`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026/build/sections/introduction.tex#L37):

```latex
\begin{theorem}\label{thm:main}
Let $A$ be a nonzero unital separable complex $C^*$-algebra, and let
$\omega$ be any free ultrafilter on $\N$. Then
\[
 F_\omega(A)\text{ has no characters}
 \quad\Longleftrightarrow\quad A\cong A\otmin\Z.
\]
\end{theorem}
```

## 5. Your classification

Enter one line for family `299` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
