# Family 197 — Nonsofic groups and group-ring counterexamples

Subject: Algebra. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 197 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Constructs a finitely presented torsion-free nonsofic group whose group algebra over $\mathbb F_2$ is not directly finite, disproving Kaplansky's conjecture even without torsion. Companion examples give injective nonsurjective cellular automata on all configurations, refuting Gottschalk's surjunctivity conjecture. Another counterexample is an integral group-ring matrix, invertible over the rational group ring, with Fuglede--Kadison determinant strictly between zero and one, disproving the unrestricted Determinant Conjecture.

## 2. The repository's own scope note ([`lean/docs/197.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/197.md), verbatim; relative links made absolute)

# A torsion-free group algebra that is not directly finite

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/paper.pdf)
- [A Counterexample to the Group-Ring Determinant Conjecture](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/paper.pdf)
- [A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Odd Characteristic](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/paper.pdf)

## Scope

Kaplansky's direct-finiteness conjecture asserts that $ab=1$ implies $ba=1$ for $a,b\in K[G]$, for every field $K$ and group $G$. The formalized results construct a finite field of characteristic two and a group algebra violating this implication. One statement records the counterexample for a finitely generated group; the more detailed construction gives a finitely presented group with an element of odd prime order.

The detailed construction also gives a precise recipe for choosing the data and proves that the required search terminates. The further conclusion that the group is nonsofic is outside these statements.

A nonsingular integer matrix has absolute determinant at least $1$. The group-ring Determinant Conjecture extends this bound to matrices over $\mathbb Z[G]$ for every discrete group $G$. If $T_A$ is the operator induced by such a matrix $A$ on finite direct sums of $\ell^2(G)$, and $\mu_A$ is the spectral measure of $T_A^*T_A$ with respect to the group trace, the conjecture asserts

$\displaystyle \int_{(0,\infty)}\log t\,d\mu_A(t)\ge0,$

with the zero spectral atom omitted. For an invertible square matrix, this is equivalent to its Fuglede–Kadison determinant being at least $1$.

The formalized result contradicts that bound. It gives a finitely generated group $G$ and an $n\times n$ matrix over $\mathbb Z[G]$, with $n\ge1$, that is invertible over $\mathbb Q[G]$. Its bounded left-regular operator is invertible and has determinant strictly between $0$ and $1$.

The formalization uses the trace of $\log(T^*T)$ to define the determinant for the invertible operator $T$. The paper's additional spectral-measure integral conclusion is not included.

Kaplansky's direct-finiteness conjecture asserts that $ab=1$ implies $ba=1$ in every group algebra over a field. Let $p$ be the smallest prime divisor of $\bigl(\binom{1200}{600}!\bigr)^2+1$; this prime is odd. The formalized result constructs a field $K$ of order $p^4$, a finitely generated group $G$ with torsion, and elements $a,b$ violating this implication. The associated cellular automaton on all configurations $K^G$ is injective but not surjective.

The formalization also contains fixed-field transfer results, separate from the statement linked below.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Finitely presented characteristic-two counterexample | [KaplanskyFinitelyPresented.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KaplanskyFinitelyPresented.lean) |
| Characteristic-two direct-finiteness counterexample | [KaplanskyDirectFiniteness.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KaplanskyDirectFiniteness.lean) |
| Group-ring determinant counterexample | [GroupRingDeterminant.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GroupRingDeterminant.lean) |
| Prescribed odd-characteristic counterexample | [OddKaplansky.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/OddKaplansky.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`GroupRingDeterminant.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GroupRingDeterminant.lean) — the lab's result label: *Group-ring determinant counterexample*. Comparator config [`GroupRingDeterminant.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/GroupRingDeterminant.json): theorem(s) `OAI.GroupRingDeterminant.main`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.GroupDeterminants.Main`.
- [`KaplanskyDirectFiniteness.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KaplanskyDirectFiniteness.lean) — the lab's result label: *Characteristic-two direct-finiteness counterexample*. Comparator config [`KaplanskyDirectFiniteness.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KaplanskyDirectFiniteness.json): theorem(s) `OAI.KaplanskyCounterexample.main_theorem`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.RingTheory.DirectFiniteness.Main`.
- [`KaplanskyFinitelyPresented.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KaplanskyFinitelyPresented.lean) — the lab's result label: *Finitely presented characteristic-two counterexample*. Comparator config [`KaplanskyFinitelyPresented.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/KaplanskyFinitelyPresented.json): theorem(s) `OAI.KaplanskyCounterexample.finitelyPresented_counterexample`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.RingTheory.DirectFiniteness.FinitelyPresented`.
- [`OddKaplansky.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/OddKaplansky.lean) — the lab's result label: *Prescribed odd-characteristic counterexample*. Comparator config [`OddKaplansky.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/OddKaplansky.json): theorem(s) `OAI.OddKaplansky.main_theorem`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Algebra.OddKaplansky.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**A Counterexample to the Group-Ring Determinant Conjecture** — [`preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/paper.pdf); `theorem` `thm:main` at [`build/main.tex:90`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/build/main.tex#L90):

```latex
\begin{theorem}\label{thm:main}
There are a finitely generated discrete group $G_D$, an integer
$n\ge1$, and $A\in\Mat_n(\Z[G_D])$ invertible over $\Q[G_D]$ such
that
\[
 0<\det_{\N(G_D)}(T_A)<1.
\]
The integral in Equation~\eqref{eq:conjecture} is finite and strictly
negative. Thus the unrestricted group-ring Determinant Conjecture
has a negative resolution.
\end{theorem}
```

**A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two** — [`preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/paper.pdf); `theorem` `thm:main` at [`build/sections/01-introduction.tex:8`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/build/sections/01-introduction.tex#L8) (further candidate):

```latex
\begin{theorem}
\label{thm:main}
There exist a finite field $K$ of characteristic two, a finitely presented group $G$ containing an element of odd prime order, and elements $a_{\mathrm{out}},b_{\mathrm{out}}\in K[G]$ such that
\[
a_{\mathrm{out}}b_{\mathrm{out}}=1,
\qquad b_{\mathrm{out}}a_{\mathrm{out}}\ne1.
\]
The field, group, and finite sums are specified by a terminating prescription involving finite sets and finite-field arithmetic.
\end{theorem}
```

**A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Odd Characteristic** — [`preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/paper.pdf); `theorem` `op:main` at [`build/sections/01-introduction.tex:13`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/build/sections/01-introduction.tex#L13) (further candidate):

```latex
\begin{theorem}\label{op:main}
Put
\[
 m=\binom{1200}{600},\qquad
 p=\min\{h\in\mathbb Z:h>1,\ h\mid(m!)^2+1\}.
\]
Then $p$ is an odd prime. There are a specified field $K$ of order $p^4$,
a specified finitely generated group $G$ containing torsion, and specified
finite sums $a,b\in K[G]$ satisfying $ab=1$ and $ba\ne1$.
\end{theorem}
```

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [A Torsion-Free Group Algebra That Is Not Directly Finite](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026); [A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026); [A Counterexample to the Group-Ring Determinant Conjecture](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026); [A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Odd Characteristic](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026)

## 5. Your classification

Enter one line for family `197` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
