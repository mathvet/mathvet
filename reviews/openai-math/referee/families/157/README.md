# Family 157 — Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures

Subject: Combinatorics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 157 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Disproves Hadwiger's conjecture even for fractional coloring: arbitrarily large finite simple graphs with independence number at most two satisfy $\chi_f(G)>h(G)$, where $h(G)$ is the largest clique-minor order. Also disproves the fractional Colin de Verdi\`ere chromatic bound $\chi_f(G)\le\mu(G)+1$. In the positive direction, every finite nonempty graph satisfies $\chi_{\mathrm{list}}(G)\le C h(G)$ for a universal constant $C$.

## 2. The repository's own scope note ([`lean/docs/157.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/157.md), verbatim; relative links made absolute)

# Graph coloring, clique minors, and Colin de Verdière invariants

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [A linear list-coloring bound in terms of the Hadwiger number](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf)

## Scope

The Linear List Hadwiger conjecture asks for a universal linear bound on list chromatic number in terms of clique-minor size. The formalization proves that there is one integer $C\ge1$ such that every finite nonempty simple graph $G$ satisfies $\chi_{\mathrm{list}}(G)\le C h(G)$, where $h(G)$ is the largest order of a clique minor. The constant is independent of the graph.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Linear list-coloring bound in the Hadwiger number | [ListHadwiger.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ListHadwiger.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`ListHadwiger.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ListHadwiger.lean) — the lab's result label: *Linear list-coloring bound in the Hadwiger number*. Comparator config [`ListHadwiger.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ListHadwiger.json): theorem(s) `OAI.LinearListHadwiger.main_theorem`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Combinatorics.ListHadwiger.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**A linear list-coloring bound in terms of the Hadwiger number** — [`preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/01-introduction.tex:25`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/build/sections/01-introduction.tex#L25):

```latex
\begin{theorem}\label{thm:main}
There is an absolute integer $C\ge1$ such that every finite nonempty
simple graph $G$ satisfies
\[
 \ell(G)\le C h(G).
\]
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [A counterexample to Hadwiger's conjecture](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026); [A counterexample to the Colin de Verdière chromatic conjecture](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-counterexample-to-the-Colin-de-Verdiere-chromatic-conjecture-September-23-2026); [A linear list-coloring bound in terms of the Hadwiger number](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026)

## 5. Your classification

Enter one line for family `157` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
