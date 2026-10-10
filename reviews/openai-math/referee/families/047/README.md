# Family 047 — Complex counterexamples to cancellation and affine fibrations

Subject: Algebraic and complex geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 047 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Constructs an integral complex affine fourfold $X\not\cong\mathbb A^4$ with $X\times\mathbb A^1\cong\mathbb A^5$, disproving affine-space cancellation over $\mathbb C$ in dimension four. It also disproves the Dolgachev--Weisfeiler affine-fibration conjecture: smooth surjections $X\to\mathbb A^1$ and $\mathbb A^5\to\mathbb A^2$ have every residue-field fiber isomorphic to affine three-space but are not Zariski-locally trivial.

## 2. The repository's own scope note ([`lean/docs/047.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/047.md), verbatim; relative links made absolute)

# Zariski cancellation and affine fibrations over the complex numbers

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [An explicit failure of complex affine-space cancellation](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf)

## Scope

Affine-space cancellation asks whether $X\times\mathbb A^1\cong\mathbb A^{n+1}$ forces $X\cong\mathbb A^n$. The formalized result gives an explicit finite-type complex domain $A$ of Krull dimension four with $A[w]\cong\mathbb C[x_1,\ldots,x_5]$ but $A\not\cong\mathbb C[x_1,\ldots,x_4]$. Thus adjoining one variable erases a genuine algebraic distinction.

The separate stable-coordinate and general line-bundle lifting consequences are not included.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Complex affine-space cancellation counterexample | [ComplexCancellation.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ComplexCancellation.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`ComplexCancellation.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ComplexCancellation.lean) — the lab's result label: *Complex affine-space cancellation counterexample*. Comparator config [`ComplexCancellation.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ComplexCancellation.json): theorem(s) `OAI.ComplexCancellation.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Algebra.AffineCancellation.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 An explicit failure of complex affine-space cancellation — *linked from the scope note*

[`preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026)

`theorem` `thm:main` at [`build/sections/01-introduction.tex:59`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/build/sections/01-introduction.tex#L59):

```latex
\begin{theorem}
\label{thm:main}
The algebra $A$ in \eqref{eq:example} is an integral complex algebra of
dimension four. For an independent variable $w$,
\[
 A[w]\simeq\kk\poly5,
 \qquad
 A\not\simeq\kk\poly4.
\]
Consequently the Zariski cancellation problem over the complex numbers has
a negative answer in dimension four.
\end{theorem}
```

## 5. Your classification

Enter one line for family `047` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
