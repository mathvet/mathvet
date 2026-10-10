# Family 312 — The Grothendieck homotopy hypothesis

Subject: Topology. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 312 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves the Grothendieck homotopy hypothesis for $\infty$-groupoids associated with every Grothendieck coherator in the Ara--Henry convention: these algebraic objects recover the homotopy theory of spaces.

## 2. The repository's own scope note ([`lean/docs/312.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/312.md), verbatim; relative links made absolute)

# The Grothendieck homotopy hypothesis

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [The Grothendieck homotopy hypothesis via elementary expansions](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/paper.pdf)

## Scope

The Grothendieck homotopy hypothesis asks whether algebraic $\infty$-groupoids recover the homotopy theory of spaces. The formalized result is the elementary-expansion theorem used in this approach: for every Grothendieck coherator in the Ara–Henry convention and every boundary-cellular model, attaching an $(n+1)$-disk along its source $n$-face induces a weak equivalence.

The later semi-model structure and full comparison with the homotopy theory of spaces are not included.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Elementary-expansion weak equivalence | [GrothendieckElementaryExpansion.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GrothendieckElementaryExpansion.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`GrothendieckElementaryExpansion.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GrothendieckElementaryExpansion.lean) — the lab's result label: *Elementary-expansion weak equivalence*. Comparator config [`GrothendieckElementaryExpansion.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GrothendieckElementaryExpansion.json): theorem(s) `OAI.Grothendieck.elementary_expansion`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.CategoryTheory.Globular.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**The Grothendieck homotopy hypothesis via elementary expansions** — [`preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/00-introduction.tex:50`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026/build/sections/00-introduction.tex#L50):

```latex
\begin{theorem}\label{thm:main}
Fix any Grothendieck coherator \(\mathcal C\).
Let \(X\) be a cellular \(\mathcal C\)-infinity-groupoid, let \(n\ge0\),
and let \(a:D_n\to X\) be any cell.  In the pushout square
\[
\begin{tikzpicture}[baseline=(current bounding box.center),
                   node distance=1.25cm and 2.2cm,>=Stealth]
\node (a) {\(D_n\)};
\node (b) [right=of a] {\(D_{n+1}\)};
\node (c) [below=of a] {\(X\)};
\node (d) at (b |- c) {\(X^+\)};
\draw[->] (a) -- node[above] {\(s_n\)} (b);
\draw[->] (a) -- node[left] {\(a\)} (c);
\draw[->] (b) -- (d);
\draw[->] (c) -- node[below] {\(i\)} (d);
\end{tikzpicture}
\]
where \(s_n\) is the source inclusion, the map \(i:X\to X^+\)
is a weak equivalence.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [The Grothendieck homotopy hypothesis via elementary expansions](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Grothendieck-homotopy-hypothesis-via-elementary-expansions-September-24-2026)

## 5. Your classification

Enter one line for family `312` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
