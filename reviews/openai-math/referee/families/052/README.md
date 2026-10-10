# Family 052 — Tangent-bundle splittings and universal covers

Subject: Algebraic and complex geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 052 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

A splitting of the tangent bundle of a compact K\"ahler manifold into two integrable holomorphic subbundles induces a compatible product decomposition of its universal cover, proving the two-summand form of Beauville's splitting conjecture. On smooth rationally connected projective manifolds, both summands are automatically integrable, establishing H\"oring's conjecture and the corresponding product decomposition.

## 2. The repository's own scope note ([`lean/docs/052.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/052.md), verbatim; relative links made absolute)

# Tangent splittings and product decompositions

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Universal-cover splitting for compact Kähler manifolds](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/paper.pdf)
- [Integrability of split tangent bundles on rationally connected manifolds](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/main.pdf)

## Scope

The splitting question asks whether a holomorphic decomposition of the tangent bundle comes from a product decomposition of the universal cover. The formalized result gives an affirmative answer for a compact connected Kähler manifold whose tangent bundle splits into two positive-rank, integrable holomorphic subbundles. The universal cover is a product of connected simply connected complex manifolds of the prescribed dimensions, and the differential identifies the two tangent factors with the original summands.

Both integrability assumptions are required. Automatic integrability and the paper's additional corollaries are not included.

The formalization proves integrability of both summands in a holomorphic splitting of the tangent bundle of a rationally connected projective manifold. More precisely, for a compact connected complex manifold of dimension at least two with a projective embedding witnessing rational connectedness, each positive-rank summand of a holomorphic tangent-bundle splitting is integrable. The paper's compatible product decomposition is a separate consequence, outside this selected statement.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Universal-cover product splitting | [KahlerSplitting.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KahlerSplitting.lean) |
| Integrability of both holomorphic tangent summands | [SplitTangentIntegrability.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SplitTangentIntegrability.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`KahlerSplitting.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KahlerSplitting.lean) — the lab's result label: *Universal-cover product splitting*. Comparator config [`KahlerSplitting.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KahlerSplitting.json): theorem(s) `OAI.UniversalCoverSplitting.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.KahlerSplitting.Main`.
- [`SplitTangentIntegrability.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SplitTangentIntegrability.lean) — the lab's result label: *Integrability of both holomorphic tangent summands*. Comparator config [`SplitTangentIntegrability.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SplitTangentIntegrability.json): theorem(s) `OAI.SplitTangent.integrability_main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.SplitTangent.RationalVariation`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Universal-cover splitting for compact Kähler manifolds — *linked from the scope note*

[`preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026)

`theorem` `thm:main` at [`build/intro.tex:100`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Universal-cover-splitting-for-compact-Kahler-manifolds-September-23-2026/build/intro.tex#L100):

```latex
\begin{theorem}\label{thm:main}
Let $X$ be a compact connected K\"ahler manifold of complex dimension
$n\geq2$, and let
\[
T_X=E_1\oplus E_2
\]
be a specified decomposition into integrable holomorphic subbundles of
positive ranks $r_1,r_2$. If $\pi:\widetilde X\to X$ is the ordinary
universal covering map, there are connected simply connected complex
manifolds $Y_1,Y_2$ and a biholomorphism
$\Phi:\widetilde X\to Y_1\times Y_2$ such that
\[
\dd\Phi(\pi^*E_i)=\pr_i^*T_{Y_i}\qquad(i=1,2),
\]
where $\dd\pi$ identifies $T_{\widetilde X}$ with $\pi^*T_X$.
In particular, $\dim_\C Y_i=r_i$.
\end{theorem}
```

### 4.2 Integrability of split tangent bundles on rationally connected manifolds — *linked from the scope note*

[`preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026)

`theorem` `thm:main` (Automatic integrability) at [`build/sections/introduction.tex:21`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Integrability-of-split-tangent-bundles-on-rationally-connected-manifolds-September-23-2026/build/sections/introduction.tex#L21):

```latex
\begin{theorem}[Automatic integrability]\label[theorem]{thm:main}
Let \(X\) be a smooth connected projective complex manifold of dimension
at least two. Suppose that two general points of \(X\) lie on the image
of a morphism \(\PP^1\to X\). For every specified holomorphic decomposition
\[
T_X=E_1\oplus E_2
\]
into subbundles of positive rank, both \(E_1\) and \(E_2\) are integrable.
\end{theorem}
```

## 5. Your classification

Enter one line for family `052` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
