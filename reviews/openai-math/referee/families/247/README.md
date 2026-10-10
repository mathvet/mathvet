# Family 247 — An infinite finitely presented residually finite $2$-group

Subject: Group theory. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 247 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Constructs an infinite finitely presented residually finite group whose elements all have finite $2$-power order, answering the finitely presented Burnside problem negatively even in this class. The construction also yields an infinite-dimensional finitely presented nil associative $\mathbb F_2$-algebra and a finitely presented infinite-dimensional algebraic unitization, giving negative answers to the corresponding nilpotence and Kurosh finiteness questions.

## 2. The repository's own scope note ([`lean/docs/247.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/247.md), verbatim; relative links made absolute)

# An infinite finitely presented residually finite 2-group and a finitely presented nil algebra

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [An infinite finitely presented periodic group](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-infinite-finitely-presented-periodic-group-September-23-2026/paper.pdf)

## Scope

The finitely presented Burnside question asks whether a finitely presented group in which every element has finite order must be finite. The formalization gives a negative answer by constructing an infinite finitely presented periodic group, including a witness realized as a Steinberg group over an algebra of characteristic two. Periodicity means that each element has some finite order; no common exponent is asserted. The paper's separate nil-algebra and radical-algebra conclusions are outside these selected statements.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Infinite finitely presented periodic group | [PeriodicGroup.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PeriodicGroup.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`PeriodicGroup.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PeriodicGroup.lean) — the lab's result label: *Infinite finitely presented periodic group*. Comparator config [`PeriodicGroup.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/PeriodicGroup.json): theorem(s) `OAI.SourceBurnside.thm_main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.GroupTheory.PeriodicGroups.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 An infinite finitely presented residually finite 2-group — *not linked from the scope note*

[`preprints/An-infinite-finitely-presented-residually-finite-2-group-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-infinite-finitely-presented-residually-finite-2-group-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-infinite-finitely-presented-residually-finite-2-group-October-5-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:12`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-infinite-finitely-presented-residually-finite-2-group-October-5-2026/build/sections/introduction.tex#L12):

```latex
\begin{theorem}\label{thm:main}
There exists an infinite residually finite group with an ordinary finite
presentation in which every element has finite 2-power order.
\end{theorem}
```

### 4.2 An infinite finitely presented periodic group — *linked from the scope note*

[`preprints/An-infinite-finitely-presented-periodic-group-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-infinite-finitely-presented-periodic-group-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-infinite-finitely-presented-periodic-group-September-23-2026)

`theorem` `thm:main` at [`build/paper.tex:88`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-infinite-finitely-presented-periodic-group-September-23-2026/build/paper.tex#L88):

```latex
\begin{theorem}\label{thm:main}
There is an infinite periodic group with an ordinary finite
presentation. More precisely, the construction below gives a unital
associative $\F_2$-algebra $R$ for which $\St_{12}(R)$ is infinite,
finitely presented, and periodic.
\end{theorem}
```

## 5. Your classification

Enter one line for family `247` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
