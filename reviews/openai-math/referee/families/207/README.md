# Family 207 — The $\ell^1$-Bass and complex Bass trace conjectures

Subject: Algebra. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 207 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves the $\ell^1$-Bass conjecture for every discrete group: Hattori--Stallings traces of idempotent matrices over $\ell^1(G)$ are supported on finitely many finite-order conjugacy classes. The algebraic companion proves the integral Bass trace conjecture and Kaplansky's idempotent conjecture for torsion-free groups over every commutative unital characteristic-zero domain.

## 2. The repository's own scope note ([`lean/docs/207.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/207.md), verbatim; relative links made absolute)

# The ℓ¹-Bass conjecture for all discrete groups

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [The Bass trace conjecture and the characteristic-zero Kaplansky idempotent conjecture](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026.pdf)

## Scope

The formalization proves the complex Bass trace conjecture for every group: the Hattori–Stallings trace of each virtual class of finitely generated projective right $\mathbb C[G]$-modules vanishes on conjugacy classes of infinite-order elements. No finiteness, countability, or geometric hypothesis on $G$ is imposed.

For torsion-free $G$, it identifies the trace on $K_0(\mathbb C[G])$ with the integral augmentation rank and proves the characteristic-zero Kaplansky idempotent conjecture: for every commutative unital domain $R$ of characteristic zero, an idempotent in $R[G]$ is $0$ or $1$.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Complex Bass trace vanishing and support | [BassTrace.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BassTrace.lean) |
| Trace rank and characteristic-zero Kaplansky idempotents for torsion-free groups | [BassTorsionFree.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BassTorsionFree.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`BassTorsionFree.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BassTorsionFree.lean) — the lab's result label: *Trace rank and characteristic-zero Kaplansky idempotents for torsion-free groups*. Comparator config [`BassTorsionFree.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BassTorsionFree.json): theorem(s) `OAI.TorsionFreeBass.torsion_free_corollary`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.RingTheory.BassTrace.TorsionFree`.
- [`BassTrace.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BassTrace.lean) — the lab's result label: *Complex Bass trace vanishing and support*. Comparator config [`BassTrace.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/BassTrace.json): theorem(s) `OAI.BassTrace.RightProjective.bassTraceModules_vanishing_and_support`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.RingTheory.BassTrace.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**The Bass trace conjecture and the characteristic-zero Kaplansky idempotent conjecture** — [`preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/paper.pdf); `theorem` `thm:bass` at [`build/sections/01-introduction.tex:45`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/build/sections/01-introduction.tex#L45):

```latex
\begin{theorem}\label{thm:bass}
Let $G$ be any discrete group. For every $x\in K_0(\C G)$ and every
infinite-order element $g\in G$,
\[
 \HS_G(x)([g]_G)=0.
\]
Equivalently, if $\con_{\mathrm{fin}}(G)$ denotes the conjugacy classes of
finite-order elements, then
\[
 \HS_G\bigl(K_0(\C G)\bigr)
 \subseteq\bigoplus_{C\in\con_{\mathrm{fin}}(G)}\C C.
\]
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [The ℓ¹-Bass Conjecture for Discrete Groups](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026); [The Bass trace conjecture and the characteristic-zero Kaplansky idempotent conjecture](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026)

## 5. Your classification

Enter one line for family `207` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
