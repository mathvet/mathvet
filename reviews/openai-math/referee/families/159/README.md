# Family 159 — Erd\H{o}s's reciprocal-sum conjecture and quasipolynomial Szemer\'edi bounds

Subject: Combinatorics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 159 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves Erd\H{o}s's conjecture that every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. Quantitatively, for each fixed $k\ge3$, every subset of $\{1,\ldots,N\}$ with no nonconstant $k$-term progression has size at most $C_kN\exp[-c_k(\log N)^{\varepsilon_k}]$, with positive constants depending only on $k$.

## 2. The repository's own scope note ([`lean/docs/159.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/159.md), verbatim; relative links made absolute)

# Erdős’s reciprocal-sum conjecture and quasipolynomial Szemerédi bounds

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Quasipolynomial Bounds for Arithmetic Progressions](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf)

## Scope

Erdős's reciprocal-sum conjecture asks whether every set of positive integers with divergent reciprocal sum contains arithmetic progressions of every finite length. The formalization proves this statement: for every requested length, such a set contains a progression with positive common difference.

The selected theorem is the reciprocal-sum consequence. The paper's quantitative upper bound for the largest progression-free subset of $\{1,\ldots,N\}$ is outside this statement.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Erdős's reciprocal-sum arithmetic-progression conjecture | [ErdosReciprocal.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ErdosReciprocal.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`ErdosReciprocal.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ErdosReciprocal.lean) — the lab's result label: *Erdős's reciprocal-sum arithmetic-progression conjecture*. Comparator config [`ErdosReciprocal.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ErdosReciprocal.json): theorem(s) `OAI.Erdos3.manuscriptReciprocalProgressionTheorem`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Combinatorics.Progressions.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Quasipolynomial Bounds for Arithmetic Progressions** — [`preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/paper.pdf); `theorem` `ap:main` at [`build/sections/00-introduction.tex:13`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026/build/sections/00-introduction.tex#L13):

```latex
\begin{theorem}\label{ap:main}
For each fixed integer $k\ge3$ there are constants
$C_k,c_k,\varepsilon_k>0$ such that, for every $N\ge2$,
\begin{equation}\label{ap:density-bound}
 r_k(N)\le C_kN\exp\bigl(-c_k(\log N)^{\varepsilon_k}\bigr).
\end{equation}
Equivalently, there is $A_k\ge1$ such that an $\alpha$-dense subset
of $[N]$ contains a nonconstant $k$-term progression whenever
\begin{equation}\label{ap:threshold}
 \log N\ge A_k\bigl(2+\log(1/\alpha)\bigr)^{A_k},
 \qquad 0<\alpha\le1.
\end{equation}
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Quasipolynomial Bounds for Arithmetic Progressions](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026)

## 5. Your classification

Enter one line for family `159` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
