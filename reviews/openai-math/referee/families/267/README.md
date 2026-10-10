# Family 267 — Positive-temperature Bose--Einstein condensation and quantum depletion

Subject: Mathematical physics. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 267 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves Bose--Einstein condensation for the exact canonical Gibbs state of the three-dimensional hard-sphere gas: each fixed exclusion distance and sufficiently small fixed density admit a strictly positive temperature, independent of volume, with positive condensate fraction in the thermodynamic limit. At zero temperature, proves the Bogoliubov leading quantum-depletion law for hard spheres and fixed bounded nonnegative radial finite-range potentials of positive scattering length, taking the thermodynamic limit before the dilute limit.

## 2. The repository's own scope note ([`lean/docs/267.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/267.md), verbatim; relative links made absolute)

# Positive-temperature Bose–Einstein condensation and exact quantum depletion

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Ground-state condensation in the dilute hard-sphere gas](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/paper.pdf)

## Scope

The formalization proves ground-state Bose–Einstein condensation in the dilute hard-sphere gas. There are absolute constants $\varepsilon_0,c_0>0$ such that, whenever the density $\rho$ and hard-sphere radius $a$ satisfy $\rho a^3<\varepsilon_0$, the condensate occupation fraction has limit inferior at least $c_0$ along every thermodynamic sequence with $N/L^3\to\rho$.

The bound covers every pure ground state, every mixed state supported on the ground space, and the normalized ground-space projection. It is uniform in the gas parameter within this range and concerns ground states, without a positive-temperature assertion.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Uniform ground-state condensation in the dilute hard-sphere gas | [HardSphere.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HardSphere.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`HardSphere.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HardSphere.lean) — the lab's result label: *Uniform ground-state condensation in the dilute hard-sphere gas*. Comparator config [`HardSphere.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/HardSphere.json): theorem(s) `OAI.HardSphere.condensation_with_mixed`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Analysis.HardSphere.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Bose–Einstein condensation at positive temperature in the dilute hard-sphere gas — *not linked from the scope note*

[`preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:41`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bose-Einstein-condensation-at-positive-temperature-in-the-dilute-hard-sphere-gas-October-5-2026/build/sections/introduction.tex#L41):

```latex
\begin{theorem}\label{thm:main}
For every $a>0$, there is $\rho_*(a)>0$ such that for each fixed
$0<\rho<\rho_*(a)$ there is a fixed temperature $T=T(a,\rho)>0$ for which
\[
 \liminf_{\substack{L\to\infty\\N/L^3\to\rho}}
 \frac{\langle u_{0,L},\gamma^{(1)}_{N,L,T}u_{0,L}\rangle}{N}>0.
\]
The exclusion distance, density, and temperature are held fixed in this
limit.
\end{theorem}
```

### 4.2 Quantum Depletion and Momentum Distribution in the Dilute Hard-Sphere Bose Gas — *not linked from the scope note*

[`preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:66`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/build/sections/introduction.tex#L66):

```latex
\begin{theorem}\label{thm:main}
For every $a>0$, every bounded continuous real function $f$ on $\R^3$,
and every $\eps>0$, there is $\rho_0(a,f,\eps)>0$ with the following
property. Fix $0<\rho<\rho_0$ and put $\eta=\rho a^3$. For every
sequence $N_j,L_j\longrightarrow\infty$ with
$N_j/L_j^3\longrightarrow\rho$,
\begin{equation}\label{intro:main-limit}
 \limsup_{j\to\infty}\ \sup_{\Gamma\in\mathcal G_{N_j,L_j,a}}
 \left|
 \frac{1}{N_j\sqrt\eta}
 \sum_{\substack{k\in(2\pi/L_j)\Z^3\\k\ne0}}
 f\!\left(\frac{k}{\sqrt{8\pi\rho a}}\right)n_{\Gamma,L_j}(k)
       -\int_{\R^3}f\,\dd\nu_{\mathrm{Bog}}
 \right|\le\eps.
\end{equation}
\end{theorem}
```

### 4.3 Quantum Depletion for Fixed Bounded Repulsive Potentials — *not linked from the scope note*

[`preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026)

`theorem` `thm:main` at [`build/source/sections/introduction.tex:41`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026/build/source/sections/introduction.tex#L41):

```latex
\begin{theorem}\label{thm:main}
For every potential $v$ satisfying the assumptions above and every
$\epsilon>0$, there is $\rho_0(v,\epsilon)>0$ such that, for every fixed
$0<\rho<\rho_0(v,\epsilon)$ and every sequence
$N_k,L_k\to\infty$ with $N_k/L_k^3\to\rho$,
\[
 \limsup_{k\to\infty}\ \sup_{\Gamma\in\mathcal G^v_{N_k,L_k}}
 \left|\frac{1-B_\Gamma}{\sqrt{\rho a_v^3}}
                       -\frac8{3\sqrt\pi}\right|\le\epsilon.
\]
\end{theorem}
```

### 4.4 A density-uniform condensate bound for dilute Bose gases — *not linked from the scope note*

[`preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026)

`theorem` `thm:main` at [`build/sections/introduction.tex:25`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-density-uniform-condensate-bound-for-dilute-Bose-gases-September-27-2026/build/sections/introduction.tex#L25):

```latex
\begin{theorem}\label{thm:main}
For every potential $v$ as above there are constants
$\rho_*(v)>0$ and $c_*(v)>0$ with the following property.
For every $0<\rho<\rho_*(v)$ there is $L_0(\rho,v)<\infty$ such that,
for every $L\ge L_0(\rho,v)$, every integer $N\ge1$ satisfying
$\rho/2\le N/L^3\le2\rho$, and every $0\le T\le\rho^2$,
\[
 \frac{\langle u_0,\gamma^{(1)}_{N,L,T}u_0\rangle}{N}
 \ge c_*(v).
\]
Consequently, for each such fixed density $\rho$ and fixed
$0\le T\le\rho^2$, every sequence with $L\to\infty$ and
$N/L^3\to\rho$ has lower limiting condensate fraction at least $c_*(v)$.
\end{theorem}
```

### 4.5 Ground-state condensation in the dilute hard-sphere gas — *linked from the scope note*

[`preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026)

`theorem` `main:theorem` (Condensation in every ground state) at [`build/sections/introduction.tex:48`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Ground-state-condensation-in-the-dilute-hard-sphere-gas-September-24-2026/build/sections/introduction.tex#L48):

```latex
\begin{theorem}[Condensation in every ground state]\label{main:theorem}
There are absolute constants $\varepsilon_0,c_0>0$ with the following
property. Fix $a,\rho>0$ satisfying $\rho a^3<\varepsilon_0$.
For every sequence of particle numbers $N_k$ and lengths $L_k$ such that
\[
 N_k\longrightarrow\infty,\qquad L_k\longrightarrow\infty,
 \qquad \frac{N_k}{L_k^3}\longrightarrow\rho,
\]
and every choice of normalized, possibly complex, bosonic ground
eigenvectors $\Psi_k$ of the hard-sphere Hamiltonians,
\begin{equation}\label{main:limit}
 \liminf_{k\to\infty} B(\Psi_k)\ge c_0.
\end{equation}
\end{theorem}
```

## 5. Your classification

Enter one line for family `267` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
