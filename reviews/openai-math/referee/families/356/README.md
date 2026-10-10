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

## 4. The paper's main theorem (file and line, with the TeX excerpt)

**Weak Hessian bounds along every geodesic in RCD spaces** — [`preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/paper.pdf`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/paper.pdf); `theorem` `weight:every-geodesic` (Weak Hessian bounds along every geodesic) at [`build/sections/introduction.tex:52`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026/build/sections/introduction.tex#L52):

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

The theorem was located by a text heuristic (see `dataset/README.md`). If it is not the statement the headline refers to, read the paper's own statement and say so in your justification.

Papers of this family: [Gigli’s distributional curvature characterization of Alexandrov spaces](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Giglis-distributional-curvature-characterization-of-Alexandrov-spaces-September-24-2026); [Weak Hessian bounds along every geodesic in RCD spaces](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Weak-Hessian-bounds-along-every-geodesic-in-RCD-spaces-September-24-2026)

## 5. Your classification

Enter one line for family `356` in your copy of `form.csv`: the class (`full`, `partial`, `weaker-statement`, `supporting-only` or `none`, rubric in `README.md`), one sentence of justification naming the step or the gap, and the minutes spent.
