# Family 230 — Exact Hausdorff measure for SLE

Subject: Probability and statistical mechanics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 230 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Resolves Schramm’s Hausdorff-measure question for chordal $\mathrm{SLE}_\kappa$, $0<\kappa<8$. The explicit gauge $r^d(\log\log(1/r))^{(2-d)/2}$, $d=1+\kappa/8$, gives almost surely positive finite measure to every trace segment $\gamma([s,t])$ with $0<s<t<\infty$, and finite expected measure to the trace in every bounded disk.

## 2. The repository's own scope note ([`lean/docs/230.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/230.md), verbatim; relative links made absolute)

# Exact Hausdorff gauges for SLE

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [An exact Hausdorff gauge for SLE: A moment-integral and finite-batch construction](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exact-Hausdorff-gauge-for-SLE-September-25-2026/An-exact-Hausdorff-gauge-for-SLE-September-25-2026.pdf)
- [An explicit exact Hausdorff gauge for SLE: A regular formula from quantitative tails and dense visits](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026.pdf)

## Scope

For $0<\kappa<8$, put $d=1+\kappa/8$. The formalization proves that every continuous nondecreasing Hausdorff gauge agreeing with $h(r)=r^d(\log\log(1/r))^{(2-d)/2}$ at sufficiently small positive radii almost surely assigns positive measure to every nontrivial compact positive-time segment of ordinary chordal $\mathrm{SLE}_\kappa$.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Positivity of the explicit gauge on every positive-time segment | [SLELowerPositivity.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SLELowerPositivity.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`SLELowerPositivity.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SLELowerPositivity.lean) — the lab's result label: *Positivity of the explicit gauge on every positive-time segment*. Comparator config [`SLELowerPositivity.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SLELowerPositivity.json): theorem(s) `OAI.SLEExactGauge.sourceLowerMain_proved`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Probability.SLE.LowerPositivity`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 An exact Hausdorff gauge for SLE — *linked from the scope note*

[`preprints/An-exact-Hausdorff-gauge-for-SLE-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exact-Hausdorff-gauge-for-SLE-September-25-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exact-Hausdorff-gauge-for-SLE-September-25-2026)

`theorem` `thm:main` (An exact moment gauge) at [`build/sections/introduction.tex:38`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-exact-Hausdorff-gauge-for-SLE-September-25-2026/build/sections/introduction.tex#L38):

```latex
\begin{theorem}[An exact moment gauge]\label{thm:main}
Fix $0<\kappa<8$, and let $\gamma$ be chordal $\SLE_\kappa$ from
$0$ to $\infty$ in the upper half-plane $\HH$, parametrized by half-plane capacity $2t$.
There is a deterministic Hausdorff gauge $h_\kappa$, depending only on
$\kappa$, such that almost surely, simultaneously for every real
$0<s<t<\infty$,
\[
 0<\Haus^{h_\kappa}(\gamma([s,t]))<\infty.
\]
\end{theorem}
```

### 4.2 An explicit exact Hausdorff gauge for SLE — *linked from the scope note*

[`preprints/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:66`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-explicit-exact-Hausdorff-gauge-for-SLE-September-26-2026/build/sections/introduction.tex#L66):

```latex
\begin{theorem}\label{thm:main}
Let $\gamma$ be ordinary chordal $\mathrm{SLE}_\kappa$ from $0$ to
$\infty$ in $\mathbb H$, parametrized by half-plane capacity $2t$,
and set $\Gamma=\gamma([0,\infty))$. For each fixed $0<\kappa<8$,
on one event of probability one,
\[
 0<\mathcal H^h(\gamma([s,t]))<\infty
 \qquad\text{for every real }0<s<t<\infty.
\]
For every deterministic $0<R<\infty$,
\[
 \mathbb E\mathcal H^h(\Gamma\cap\overline B(0,R))
       \le C_{\kappa,R}<\infty.
\]
In particular, on the same probability-one event,
\[
 \mathcal H^h\bigl(\Gamma\cap([-m,m]+i[0,m])\bigr)<\infty
 \qquad(m=1,2,\ldots).
\]
\end{theorem}
```

## 5. Your classification

Enter one line for family `230` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
