# Family 356 — Gigli's characterization of Alexandrov curvature

Subject: Differential geometry. Reviewed repository: `https://github.com/openai/math` at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`. Catalogue entry: family 356 in `overview.pdf` / `CONTENTS.md`.

## 1. Headline claim (the overview summary, verbatim)

Proves Gigli's conjecture: in every integer dimension $n\ge2$, Alexandrov curvature at least $\kappa$ is characterized by the full-support $\operatorname{RCD}((n-1)\kappa,n)$ condition with reference measure $\mathcal H^n$ and distributional sectional curvature at least $\kappa$ in the original global test classes. The RCD condition is unreduced.

## 2. The repository's own scope note ([`lean/docs/356.md`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/356.md), verbatim; relative links made absolute)

# Gigli’s characterization of Alexandrov curvature

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Weak Hessian bounds along every geodesic in RCD spaces](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/weak-hessian-geodesics.pdf)

## Scope

The formalization transfers a weak Hessian upper bound to every prescribed minimizing geodesic in an $\mathrm{RCD}(K,N)$ space with finite $N>1$. If a bounded globally Lipschitz function $F$ has weak Hessian bounded above by $G$ times the metric, where $G$ is bounded and continuous, then every constant-speed geodesic $\gamma:[0,1]\to X$ satisfies $(F\circ\gamma)''\le G(\gamma)\,d(\gamma(0),\gamma(1))^2$ in the distributional sense. Constant geodesics are included. The space is complete and separable with full support and measure finite on bounded sets; compactness and metric nonbranching are not assumed.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Weak Hessian bounds along every geodesic | [WeakHessian.lean](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/WeakHessian.lean) |

## 3. Challenge statements (every file linked from the scope note; copies in this folder)

- [`WeakHessian.lean`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/WeakHessian.lean) — the lab's result label: *Weak Hessian bounds along every geodesic*. Comparator config [`WeakHessian.json`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/WeakHessian.json): theorem(s) `OAI.WeakHessian.every_geodesic`; permitted axioms `propext`, `Quot.sound`, `Classical.choice`; solution module `OAI.Geometry.WeakHessian.Main`.

The challenge file is the statement the solution must match; its proofs are `sorry` by design. The theorem names listed in the config are the ones the Comparator compares.

## 4. The papers of this family and their main theorems (file and line, TeX excerpt)

Papers in the order of the catalogue entry. The headline's first-named claim may be stated in any of them; the scope note links the Lean to the paper(s) marked *linked from the scope note*. Each theorem below was located by a text heuristic: the block carrying a main-theorem label or title, else the first theorem of the introduction, else the first theorem-like environment. It is a pointer, not a judgment. If it is not the statement the headline refers to, or the headline refers to a different paper, read that paper's own statement and say so in your justification.

### 4.1 Gigli’s distributional curvature characterization of Alexandrov spaces — *not linked from the scope note*

[`preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026)

`theorem` `main:equivalence` (Gigli's characterization) at [`build/sections/introduction.tex:63`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026/build/sections/introduction.tex#L63):

```latex
\begin{theorem}[Gigli's characterization]
\label{main:equivalence}
Let \(n\ge2\) be an integer, let \(\kappa\in\R\), and let \((M,d)\)
be a complete separable metric space. The following conditions are
equivalent.
\begin{enumerate}[label=\textup{(\Alph*)}]
\item \((M,d)\) is an \(n\)-dimensional Alexandrov space with curvature
bounded below by \(\kappa\).
\item With \(m=\mathcal H^n_d\), the space \((M,d,m)\) has full support,
is \(\RCD((n-1)\kappa,n)\), and satisfies
\begin{equation}
\label{eq:main-curvature}
R(X,Y,Y,X)(f)\ge
\kappa\int_M f\bigl(|X|^2|Y|^2-\langle X,Y\rangle^2\bigr)\dd m
\end{equation}
for every \(X,Y\in\TestV(M)\) and every nonnegative \(f\in\Test(M)\).
\end{enumerate}
The \(\RCD\) condition is unreduced, and the test classes and
curvature sign are exactly those defined above.
\end{theorem}
```

### 4.2 Weak Hessian bounds along every geodesic in RCD spaces — *linked from the scope note*

[`preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/paper.pdf) · [source](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026)

`theorem` `weight:every-geodesic` (Weak Hessian bounds along every geodesic) at [`build/sections/introduction.tex:52`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/build/sections/introduction.tex#L52):

```latex
\begin{theorem}[Weak Hessian bounds along every geodesic]
\label{weight:every-geodesic}
Let \((M,d,m)\) be a full-support \(\RCD(K,N)\) space,
where \(K\in\mathbb R\) and \(1<N<\infty\). Let
\(F\colon M\to\mathbb R\) be bounded and globally Lipschitz,
and let \(G\colon M\to\mathbb R\) be bounded and continuous.
Suppose that for every compactly supported \(g\in\Test(M)\)
and every nonnegative \(h\in\Lip_c(M)\),
\begin{equation}
\label{weight:hessian-assumption}
H_F(\nabla g,\nabla g)(h)
\le\int_M hG\Gamma(g)\dd m.
\end{equation}
Then every constant-speed minimizing geodesic
\(\sigma\colon[0,1]\to M\), of length \(\ell\), satisfies
\begin{equation}
\label{weight:curve-hessian}
(F\circ\sigma)''\le\ell^2G\circ\sigma
\qquad\text{in distributions on }(0,1).
\end{equation}
\end{theorem}
```

## 5. Your classification

Enter one line for family `356` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent.
