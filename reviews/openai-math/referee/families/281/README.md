# Family 281 — QAOA optimality for the SK model

Subject: Mathematical physics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 281 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves that QAOA approaches the ground-state energy of the Gaussian zero-field Sherrington--Kirkpatrick model when system size tends to infinity before circuit depth. For every accuracy, finite depth and deterministic angles independent of size and disorder achieve the required limiting expected energy per spin. This also yields leading-order optimal expected MaxCut values on large-degree random regular graphs, with size tending to infinity before degree.

## 2. The repository's own scope note ([`lean/docs/281.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/281.md), verbatim; relative links made absolute)

# QAOA attains the SK optimum in the thermodynamic-first limit

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [QAOA attains the SK ground-state energy in the thermodynamic-first limit](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026.pdf)
- [Full support of the zero-temperature Sherrington–Kirkpatrick order parameter](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/main.pdf)

## Scope

The linked formalization supplies variational identities for the Gaussian zero-field Sherrington–Kirkpatrick ground-state energy used in the paper's QAOA argument. Conditional on an admissible Parisi minimizer and its associated diffusion, it proves convergence of the finite-system ground-state energy, identifies its limit with the Parisi value, and gives equivalent terminal-martingale and integrated-curvature formulas.

It also proves convergence of finite Gaussian coefficient sums to the curvature integral, which approaches the ground-state value as the terminal time tends to one. The selected statement covers these value and approximation results; it does not itself assert convergence of QAOA circuit energies.

The formalization proves that every admissible integrable minimizer of the zero-temperature Parisi functional for the pure zero-field Sherrington–Kirkpatrick model has full relative Stieltjes support on $[0,1)$. Equivalently, the order parameter increases strictly between every two overlap values below one, so its support has no gap. The covariance normalization is $\xi(t)=t^2/2$.

The statement also constructs the associated diffusion and proves its selected self-consistency moment identities. It is conditional on the order parameter being a minimizer and does not separately assert existence of a minimizer.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Parisi ground-state value identities and finite Gaussian approximation | [SKValue.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SKValue.lean) |
| Full support of zero-temperature SK minimizers | [SKFullSupport.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SKFullSupport.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`SKFullSupport.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SKFullSupport.lean) — the lab's result label: *Full support of zero-temperature SK minimizers*. Comparator config [`SKFullSupport.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SKFullSupport.json): theorem(s) `OAI.ZeroTemperatureSK.full_support`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Probability.SKSupport.Main`.
- [`SKValue.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SKValue.lean) — the lab's result label: *Parisi ground-state value identities and finite Gaussian approximation*. Comparator config [`SKValue.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/SKValue.json): theorem(s) `OAI.SKValue.value_consequences`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Probability.SKValue.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 QAOA attains the SK ground-state energy in the thermodynamic-first limit — *linked from the scope note*

[`preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026)

`theorem` `thm:main` at [`build/sections/01-introduction.tex:111`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/build/sections/01-introduction.tex#L111):

```latex
\begin{theorem}\label{thm:main}
For the zero-field SK model~\eqref{eq:sk-model},
\begin{equation}\label{eq:main-result}
 \lim_{p\to\infty}Q_p=\Pstar.
\end{equation}
Equivalently, for every $\varepsilon>0$ there exist a finite integer $p$ and
deterministic real vectors $\gamma,\beta\in\R^p$, independent of $n$ and $J$,
such that $v_p(\gamma,\beta)\ge\Pstar-\varepsilon$.
\end{theorem}
```

### 4.2 Full support of the zero-temperature Sherrington-Kirkpatrick order parameter — *linked from the scope note*

[`preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026)

`theorem` `thm:full-support` (Full support at zero temperature) at [`build/main.tex:119`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/build/main.tex#L119):

```latex
\begin{theorem}[Full support at zero temperature]\label{thm:full-support}
If $\gamma\in\mathcal U$ minimizes $\mathcal P$, then
\[
 \supp\mu_\gamma=[0,1).
\]
In particular $\gamma(b)>\gamma(a)$ whenever $0\leq a<b<1$.
For the solution of~\eqref{eq:model-diffusion},
\begin{equation}\label{eq:main-consistency}
 \E[u_\gamma(t,X_t)^2]=t,\qquad
 \E[\Phi_{\gamma,xx}(t,X_t)^2]=1,
 \qquad 0\leq t<1.
\end{equation}
\end{theorem}
```

## 5. Your classification

Enter one line for family `281` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
