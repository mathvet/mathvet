# Family 266 — Exactly three mutually unbiased bases in dimension six

Subject: Mathematical physics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 266 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves $N(6)=3$, resolving Zauner\textquotesingle s dimension-six mutually unbiased bases conjecture: three such bases exist in $\mathbb C^6$, but four cannot. The exclusion is a complete certified computation under the stated binary64 arithmetic and compiler conditions. An independent companion proves the Matolcsi--Ruzsa--Weiner Fourier-vanishing conjecture for order-six complex Hadamard matrices outside Tao\textquotesingle s cubic equivalence class.

## 2. The repository's own scope note ([`lean/docs/266.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/266.md), verbatim; relative links made absolute)

# Exactly three mutually unbiased bases in dimension six

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [The maximum number of mutually unbiased bases in dimension six](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf)
- [Exact Fourier certificates for complex Hadamard matrices of order six](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026.pdf)

## Scope

The paper claims that at most three mutually unbiased orthonormal bases exist in $\mathbb C^6$. The linked formalization proves a weaker family bound: every family in its mutually unbiased bases model has at most five members. It also proves a Fourier character-sum vanishing statement for order-six complex Hadamard matrices not equivalent to the Tao matrix, uniformly over coordinate permutations.

The selected statement does not establish the paper's upper bound of three or its computer-assisted exclusion of four arbitrary bases.

The linked formalization proves a cancellation lemma used in the order-six complex Hadamard analysis. Let $H$ and its entrywise square both be complex Hadamard matrices, and fix two distinct rows. If the cubes of their six entrywise ratios take only two distinct values, then the sum of the row-ratio terms over either specified cube fiber is zero.

This is a supporting Fourier cancellation statement. The paper's full character-sum vanishing theorem and its mutually unbiased bases bound are outside this selected statement.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Order-six Hadamard Fourier vanishing and a five-basis upper bound | [MUBSix.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/MUBSix.lean) |
| Cube-fiber cancellation for order-six Hadamard row ratios | [HadamardCubeFiber.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HadamardCubeFiber.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`HadamardCubeFiber.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HadamardCubeFiber.lean) — the lab's result label: *Cube-fiber cancellation for order-six Hadamard row ratios*. Comparator config [`HadamardCubeFiber.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HadamardCubeFiber.json): theorem(s) `OAI.HadamardSix.rowRatio_cubeFiber_sum_zero`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.LinearAlgebra.Hadamard.Main`.
- [`MUBSix.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/MUBSix.lean) — the lab's result label: *Order-six Hadamard Fourier vanishing and a five-basis upper bound*. Comparator config [`MUBSix.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/MUBSix.json): theorem(s) `OAI.MUB6.fourier_and_family_bound`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.MutuallyUnbiased.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 The maximum number of mutually unbiased bases in dimension six — *linked from the scope note*

[`preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026)

`theorem` `thm:main` (Computer-assisted) at [`build/sections/introduction.tex:13`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/build/sections/introduction.tex#L13):

```latex
\begin{theorem}[Computer-assisted]\label{thm:main}
Under the arithmetic and compiler conditions in
Appendix~\ref{sec:rounding}, the fresh complete execution documented in
Section~\ref{execute:observed} certifies that there are no four pairwise mutually unbiased orthonormal bases in
$\C^6$. Consequently, $N(6)=3$.
\end{theorem}
```

### 4.2 Exact Fourier certificates for complex Hadamard matrices of order six — *linked from the scope note*

[`preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026)

`theorem` `thm:main` (No complete family) at [`build/paper.tex:142`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/build/paper.tex#L142):

```latex
\begin{theorem}[No complete family]\label{thm:main}
There do not exist seven orthonormal bases
$B_r=(b_{r,0},\ldots,b_{r,5})$ of $\C^6$, $1\le r\le7$, such that
\[
 \bigl|\langle b_{r,i},b_{s,j}\rangle\bigr|^2=\frac16
 \qquad(r\ne s,\ 0\le i,j\le5).
\]
\end{theorem}
```

Also located: `theorem` `thm:fourier` (Fourier vanishing) at [`build/paper.tex:65`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/build/paper.tex#L65).

## 5. Your classification

Enter one line for family `266` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
