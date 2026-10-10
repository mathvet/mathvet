# Family 124 — Polynomial-time scheduling on three identical machines

Subject: Theoretical computer science. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 124 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Resolves the three-processor unit-job scheduling problem of Garey and Johnson: a deterministic polynomial-time algorithm minimizes makespan for nonpreemptive unit-length jobs with arbitrary precedence constraints on three identical parallel machines. For an explicitly given precedence graph, it decides deadline feasibility exactly and constructs a feasible schedule.

## 2. The repository's own scope note ([`lean/docs/124.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/124.md), verbatim; relative links made absolute)

# Polynomial-time scheduling on three identical machines

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf)

## Scope

The formalization gives a deterministic polynomial-time algorithm for scheduling nonempty collections of unit-length jobs with arbitrary acyclic precedence constraints on three identical parallel machines. It constructs a schedule of minimum makespan and decides exactly whether a valid specified deadline can be met. The algorithm is one fixed finite machine, and its running time is bounded by a polynomial in the binary input length.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Optimal three-machine unit-job scheduling | [ThreeMachine.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ThreeMachine.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`ThreeMachine.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ThreeMachine.lean) — the lab's result label: *Optimal three-machine unit-job scheduling*. Comparator config [`ThreeMachine.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/ThreeMachine.json): theorem(s) `OAI.ThreeMachine.main_theorem`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Computability.Scheduling.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 A Polynomial-Time Algorithm for Three-Machine Unit-Job Scheduling — *linked from the scope note*

[`preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026)

`theorem` `thm:main` at [`build/paper.tex:120`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-polynomial-time-algorithm-for-three-machine-unit-job-scheduling-September-24-2026/build/paper.tex#L120):

```latex
\begin{theorem}\label{thm:main}
Let an explicitly listed finite directed acyclic graph specify the
precedence constraints on \(n\ge1\) nonpreemptive unit-length jobs
on three identical machines. There is a uniform deterministic algorithm
that constructs a feasible schedule of minimum makespan.
Given also an integer deadline \(1\le T\le n\), it decides feasibility
exactly and returns a schedule whenever the answer is affirmative.
Both tasks can be performed in
\(O((L+2)^{150020})\) steps on a deterministic multitape Turing machine,
where \(L\) is the total binary input length.
\end{theorem}
```

## 5. Your classification

Enter one line for family `124` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
