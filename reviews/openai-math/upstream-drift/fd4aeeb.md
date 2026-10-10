# Upstream drift: openai/math `adc7f124` (reviewed) → `fd4aeeb2`

New commit: `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, 2026-10-07T22:20:00-07:00, "Merge pull request #1 from openai/codex/update-10-7". Report generated 2026-10-10T08:56:24Z by `scripts/upstream_drift.py`. Files: 1135 added, 31 deleted, 19 modified.

The published review describes the reviewed commit; nothing below changes a verdict. Families listed under "to re-read" have had a verdict input changed (headline, scope note, challenge set or statement) and are queued for a new reading; challenges under "to rebuild" are built and checked on the new commit by the pipeline.

## Summary

- Families: 372 now (372 reviewed); new 0 (none), of which with Lean 0 (none); removed none; families that gained Lean (no formalization in the reviewed release): 7 (027, 066, 075, 103, 137, 195, 301).
- Catalogue title or summary changed for 1 families: 032.
- Scope notes (lean/docs): 027 (A), 049 (M), 066 (A), 075 (A), 103 (A), 130 (M), 137 (A), 157 (M), 195 (A), 237 (M), 301 (A).
- Comparator challenges: 416 now; new 11, modified 0, removed 0.
- Solution files changed under lean/OAI: 726; challenges whose own solution file changed: none (changes deeper in a cone are found only by rebuilding).
- Preprints: 27 directories added, 3 modified.
- Build configuration (lake-manifest, toolchain, lakefile, patches): unchanged.
- Referee sample affected: 157.

## To re-read (12 families)

- `027` Integral density on curve character varieties — challenge CharacterVarietiesAllSeamsSupport added; family gained Lean (first formalization of this family; not among the 235 reviewed); new scope note; set of linked challenges changed — *not in the reviewed release*
- `032` The rational Hodge conjecture for CM abelian varieties — catalogue title/summary changed — *not in the reviewed release*
- `049` A stable-coordinate counterexample in four variables — challenge StableCoordinateFour added; scope note changed; set of linked challenges changed
- `066` Bounded klt complements for Fano contractions — challenge CartierChartCompactnessSupport added; family gained Lean (first formalization of this family; not among the 235 reviewed); new scope note; set of linked challenges changed — *not in the reviewed release*
- `075` The $L\log L$ Fourier-convergence conjecture — challenge FourierLLogL added; family gained Lean (first formalization of this family; not among the 235 reviewed); new scope note; set of linked challenges changed — *not in the reviewed release*
- `103` Derandomization of logarithmic space: $\mathsf L=\mathsf{RL}=\mathsf{BPL}$ — challenge LogspaceEquality added; family gained Lean (first formalization of this family; not among the 235 reviewed); new scope note; set of linked challenges changed — *not in the reviewed release*
- `130` Fourier transforms below $n\log n$ — challenge UniformFourier added; scope note changed; set of linked challenges changed
- `137` One-tape time simulation in two-fifths-power space — challenge OneTapeSpace added; family gained Lean (first formalization of this family; not among the 235 reviewed); new scope note; set of linked challenges changed — *not in the reviewed release*
- `157` Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures **(in the referee sample)** — challenge HadwigerCounterexample added; scope note changed; set of linked challenges changed
- `195` A counterexample to the small Cohen--Macaulay module conjecture — challenge SurfaceConeCandidateSupport added; family gained Lean (first formalization of this family; not among the 235 reviewed); new scope note; set of linked challenges changed — *not in the reviewed release*
- `237` The three-quarter diameter exponent for honeycomb walks — challenge HoneycombBridgeMassSupport added; scope note changed; set of linked challenges changed
- `301` Classification by trace cones after Razak--Jacelon stabilization — challenge TraceIdealTransportSupport added; family gained Lean (first formalization of this family; not among the 235 reviewed); new scope note; set of linked challenges changed — *not in the reviewed release*

## To rebuild and check on the new commit (11 challenges)

`CartierChartCompactnessSupport`, `CharacterVarietiesAllSeamsSupport`, `FourierLLogL`, `HadwigerCounterexample`, `HoneycombBridgeMassSupport`, `LogspaceEquality`, `OneTapeSpace`, `StableCoordinateFour`, `SurfaceConeCandidateSupport`, `TraceIdealTransportSupport`, `UniformFourier`

## Catalogue changes (overview summary, old → new)

### `032` The rational Hodge conjecture for CM abelian varieties

**Old title:** The rational Hodge conjecture for CM abelian varieties and products of K3 surfaces

**New title:** The rational Hodge conjecture for CM abelian varieties

**Old summary:** Proves the rational Hodge conjecture for every complex CM abelian variety, in every dimension and codimension. Through Milne's theorems, this also gives the Tate conjecture for all abelian varieties over finite fields and the Hodge standard conjecture for abelian varieties in every characteristic. Companion results prove rational Hodge for arbitrary products of projective complex K3 surfaces and algebraicity of the Kuga--Satake correspondence for every such surface.

**New summary:** Proves the rational Hodge conjecture for every complex CM abelian variety, in every dimension and codimension. Through Milne's theorems, this also gives the Tate conjecture for all abelian varieties over finite fields and the Hodge standard conjecture for abelian varieties in every characteristic.

## Changed scope notes (diff)

### `049` A stable-coordinate counterexample in four variables

```diff
@@ -4,7 +4,10 @@ The following describes the scope of the Lean formalization related to the follo
 
 - [An explicit noncoordinate polynomial with affine three-space zero fibre](../../preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/paper.pdf)
+- [A stable coordinate that is not a coordinate in four variables](../../preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/stable-coordinate-four-variables.pdf)
 
 ## Scope
 
+The stable coordinate conjecture predicts that a polynomial that becomes a coordinate after adjoining variables was already a coordinate. The formalization gives an explicit degree-five polynomial in four complex variables that becomes a coordinate after adjoining one variable but is not a coordinate in four variables. Every fiber is isomorphic to affine three-space, yet no fiber can be carried to a coordinate hyperplane by an ambient polynomial automorphism.
+
 The Abhyankar–Sathaye conjecture predicts that a polynomial defining an affine-space quotient must be an ambient coordinate. For every $n\ge4$, the formalized counterexample gives $F\in\mathbb C[x_1,\ldots,x_n]$ with quotient $\mathbb C[x_1,\ldots,x_n]/(F)\cong\mathbb C[y_1,\ldots,y_{n-1}]$, although $F$ is not a coordinate.
 
@@ -17,2 +20,3 @@ A companion gives $n-1$ commuting, locally nilpotent derivations, linearly indep
 | Noncoordinate polynomial in every dimension at least four | [AbhyankarSathaye.lean](../ComparatorChallenges/AbhyankarSathaye.lean) |
 | Commuting locally nilpotent derivations | [CommutingDerivations.lean](../ComparatorChallenges/CommutingDerivations.lean) |
+| Degree-five stable noncoordinate with nonrectifiable affine-space fibers | [StableCoordinateFour.lean](../ComparatorChallenges/StableCoordinateFour.lean) |
```

### `130` Fourier transforms below $n\log n$

```diff
@@ -4,4 +4,5 @@ The following describes the scope of the Lean formalization related to the follo
 
 - [Finite tensor savings and exact Fourier circuits](../../preprints/Finite-tensor-savings-and-exact-Fourier-circuits-September-25-2026/main.pdf)
+- [An explicit power saving for the exact discrete Fourier transform](../../preprints/An-explicit-power-saving-for-the-exact-discrete-Fourier-transform-September-25-2026/main.pdf)
 
 ## Scope
@@ -9,4 +10,6 @@ The following describes the scope of the Lean formalization related to the follo
 The formalized result gives exact discrete Fourier transforms with arbitrarily small normalized circuit cost along an unbounded sequence of lengths. For every $c>0$ and every cutoff $N_0\ge2$, some $n\ge N_0$ has a circuit computing the unnormalized DFT with fewer than $cn\log_2 n$ gates. Addition, subtraction, and multiplication by a predetermined complex scalar each cost one gate; diagonal scalings are charged. The result is subsequential, with no all-length, bounded-coefficient, conditioning, or bit-complexity claim.
 
+A separate uniform formalization gives fixed deterministic programs for every positive length $n$, computing the canonical discrete Fourier transform and the full convolution of two length-$n$ complex vectors exactly. Their work is $O(n(\log n)^{1-10^{-13}})=o(n\log n)$, including root-order selection and scalar preparation. The chosen root of unity is supplied; the model permits exact complex arithmetic and unrestricted coefficients, while integer values and indices remain polynomially bounded in $n$. The synthesis appendix's extraction, search, and printer uniformization is outside these selected statements.
+
 ## Comparator links
 
@@ -14,2 +17,3 @@ The formalized result gives exact discrete Fourier transforms with arbitrarily s
 | --- | --- |
 | Subsequential savings for exact Fourier circuits | [ExactFourier.lean](../ComparatorChallenges/ExactFourier.lean) |
+| Uniform exact DFT and convolution with a power saving | [UniformFourier.lean](../ComparatorChallenges/UniformFourier.lean) |
```

### `157` Counterexamples to the Hadwiger and Colin de Verdi\`ere conjectures **(in the referee sample)**

```diff
@@ -4,7 +4,12 @@ The following describes the scope of the Lean formalization related to the follo
 
 - [A linear list-coloring bound in terms of the Hadwiger number](../../preprints/A-linear-list-coloring-bound-in-terms-of-the-Hadwiger-number-September-23-2026/paper.pdf)
+- [A counterexample to Hadwiger's conjecture](../../preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/paper.pdf)
 
 ## Scope
 
+Hadwiger's conjecture predicts $\chi(G)\le h(G)$ for every finite graph, where $h(G)$ is the largest clique-minor order. The formalization constructs arbitrarily large finite simple counterexamples with independence number at most two. For a graph on $m$ vertices it proves
+$h(G)<26m/75+2/3<m/2\le\chi(G)$.
+This disproves the ordinary chromatic form. The paper's fractional-chromatic strengthening and the Colin de Verdière consequence are outside this selected statement.
+
 The Linear List Hadwiger conjecture asks for a universal linear bound on list chromatic number in terms of clique-minor size. The formalization proves that there is one integer $C\ge1$ such that every finite nonempty simple graph $G$ satisfies $\chi_{\mathrm{list}}(G)\le C h(G)$, where $h(G)$ is the largest order of a clique minor. The constant is independent of the graph.
 
@@ -14,2 +19,3 @@ The Linear List Hadwiger conjecture asks for a universal linear bound on list ch
 | --- | --- |
 | Linear list-coloring bound in the Hadwiger number | [ListHadwiger.lean](../ComparatorChallenges/ListHadwiger.lean) |
+| Arbitrarily large counterexamples to Hadwiger's conjecture | [HadwigerCounterexample.lean](../ComparatorChallenges/HadwigerCounterexample.lean) |
```

### `237` The three-quarter diameter exponent for honeycomb walks

```diff
@@ -6,4 +6,5 @@ The following describes the scope of the Lean formalization related to the follo
 - [Renewal and changes of law for critical honeycomb walks](../../preprints/Renewal-and-changes-of-law-for-critical-honeycomb-walks-September-26-2026/main.pdf)
 - [Critical strip-crossing mass on the honeycomb lattice](../../preprints/Critical-strip-crossing-mass-on-the-honeycomb-lattice-September-26-2026/main.pdf)
+- [Critical honeycomb chords with prescribed boundary endpoints](../../preprints/Critical-honeycomb-chords-with-prescribed-boundary-endpoints-September-26-2026/main.pdf)
 
 ## Scope
@@ -19,4 +20,8 @@ This selected result supplies the limiting free energy. It does not state the pa
 For critical self-avoiding walks on the honeycomb lattice, the formalization proves that the total weight of paths crossing a strip of height $N$ is comparable to $N^{-1/4}$, while the first horizontal-displacement moment of return paths is comparable to $N^{3/4}$. It also proves finiteness of the strip sums, the exact arch–bridge balance identity, comparison of successive moment increments with bridge mass, and monotonicity of bridge mass. The comparison constants are uniform in the strip height.
 
+For the prescribed-boundary-endpoint companion, let $B_h$ be the total critical weight of strict bridges crossing a strip of integral height $h$, from one fixed bottom port to all compatible top ports, with $B_0=1$. The formalization proves
+$c(1+h)^{-1/4}\le B_h\le C(1+h)^{-1/4}$
+for all $h\ge0$ and fixed positive constants $c,C$. This includes finiteness of the path sum. The prescribed-endpoint length law, arch and strip mean laws, and remaining moment and renewal conclusions are outside this supporting statement.
+
 ## Comparator links
 
@@ -26,2 +31,3 @@ For critical self-avoiding walks on the honeycomb lattice, the formalization pro
 | Existence of the honeycomb free-energy limit | [HoneycombFreeEnergy.lean](../ComparatorChallenges/HoneycombFreeEnergy.lean) |
 | Critical honeycomb strip mass and displacement moment | [CriticalStripMass.lean](../ComparatorChallenges/CriticalStripMass.lean) |
+| Strict honeycomb bridge mass of order $(1+h)^{-1/4}$ | [HoneycombBridgeMassSupport.lean](../ComparatorChallenges/HoneycombBridgeMassSupport.lean) |
```

## New challenges

- `CartierChartCompactnessSupport` (family 066): module `OAI.AlgebraicGeometry.CartierSections.ChartCompactness`, theorems `OAI.CartierSections.isCompact_closedChartFieldRetraction_cone`
- `CharacterVarietiesAllSeamsSupport` (family 027): module `OAI.AlgebraicGeometry.CharacterVarieties.Seams.ProducedSolution`, theorems `OAI.IntegralCharacterVarieties.SurfacePresentation.Diagram.producedMarkedValues_allSeams`
- `FourierLLogL` (family 075): module `OAI.Analysis.FourierLLogL.PaperMain`, theorems `OAI.FourierLLogL.paperMain`
- `HadwigerCounterexample` (family 157): module `OAI.Combinatorics.HadwigerCounterexample.Main`, theorems `OAI.HadwigerCounterexample.exists_counterexamples`, `OAI.HadwigerCounterexample.not_hadwiger_conjecture`
- `HoneycombBridgeMassSupport` (family 237): module `OAI.Combinatorics.HoneycombChords.BridgeMass`, theorems `OAI.CriticalHoneycomb.finiteBridgeMassEstimate`
- `LogspaceEquality` (family 103): module `OAI.Computability.Logspace.Equality`, theorems `OAI.ExactDerandomization.exact_logarithmic_space_derandomization`
- `OneTapeSpace` (family 137): module `OAI.Computability.SpaceSimulation.Main`, theorems `OAI.Fifths.Single.capped`, `OAI.Fifths.Single.unknown`
- `StableCoordinateFour` (family 049): module `OAI.AlgebraicGeometry.StableCoordinate.Principal`, theorems `OAI.StableCoordinate.principal_package`
- `SurfaceConeCandidateSupport` (family 195): module `OAI.AlgebraicGeometry.SurfaceCones.CandidateRing`, theorems `OAI.SmallCM.candidate_ring_properties`
- `TraceIdealTransportSupport` (family 301): module `OAI.Analysis.TraceCone.IdealTransport`, theorems `OAI.TraceConeClassification.TraceConeEquiv.idealOrderIso_finIdeal`, `OAI.TraceConeClassification.TraceConeEquiv.idealOrderIso_zeroIdeal`, `OAI.TraceConeClassification.closed_ideal_weight_exists`, `OAI.TraceConeClassification.ExtendedTrace.zero_mem_finiteSquareSet`, `OAI.TraceConeClassification.ExtendedTrace.star_mem_finiteSquareSet`, `OAI.TraceConeClassification.ExtendedTrace.smul_mem_finiteSquareSet`, `OAI.TraceConeClassification.ExtendedTrace.add_mem_finiteSquareSet`, `OAI.TraceConeClassification.ExtendedTrace.mul_mem_finiteSquareSet_left`, `OAI.TraceConeClassification.ExtendedTrace.isClosed_finiteIdeal`, `OAI.TraceConeClassification.ExtendedTrace.mul_mem_finiteIdeal_left`, `OAI.TraceConeClassification.ExtendedTrace.mul_mem_finiteIdeal_right`, `OAI.TraceConeClassification.ExtendedTrace.lowerSemicontinuous_supportWeight`, `OAI.TraceConeClassification.ClosedIdeal.weight_idempotent`, `OAI.TraceConeClassification.ClosedIdeal.finiteIdeal_weight`, `OAI.TraceConeClassification.ClosedIdeal.le_iff_add_weight`, `OAI.TraceConeClassification.ExtendedTrace.idempotent_eq_weight`, `OAI.TraceConeClassification.closedIdealEquivOfAdditive_weight`
- `UniformFourier` (family 130): module `OAI.Computability.FourierTransform.Main`, theorems `OAI.PowerSaving.transform_main`, `OAI.PowerSaving.convolution_main`

## New preprints

- A pointwise 2-converse for elliptic curves with rational two-torsion (`A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026`)
- Abelian covers, Gale correspondences, and the Hodge conjecture for powers (`Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026`)
- Conditional good minimal models for compact Kähler fourfolds (`Conditional-good-minimal-models-for-compact-Kahler-fourfolds-October-6-2026`)
- Deforming hypersymplectic four-manifolds to hyperkähler triples (`Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples-October-7-2026`)
- Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank (`Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026`)
- Finite ordinary minimal model programs on compact Kähler fourfolds (`Finite-ordinary-minimal-model-programs-on-compact-Kahler-fourfolds-October-6-2026`)
- Fontaine–Mazur modularity at the prime 2 (`Fontaine-Mazur-modularity-at-the-prime-2-October-6-2026`)
- Gaussian free-field limits of weighted integer Lipschitz heights (`Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-October-6-2026`)
- Goldfeld's analytic density conjecture and the 2-converse for elliptic curves (`Goldfelds-analytic-density-conjecture-and-the-2-converse-for-elliptic-curves-October-7-2026`)
- Hilbert’s tenth problem over the rational numbers (`Hilberts-tenth-problem-over-the-rational-numbers-October-6-2026`)
- Incompressible Box Transport and Finite Computation (`Incompressible-Box-Transport-and-Finite-Computation-October-6-2026`)
- Log abundance for compact Kähler spaces under logarithmic Iitaka subadditivity (`Log-abundance-for-compact-Kahler-spaces-under-logarithmic-Iitaka-subadditivity-October-6-2026`)
- Milne's rationality conjecture for abelian varieties (`Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026`)
- Numerical semiampleness of nef adjoint classes on compact Kähler manifolds (`Numerical-semiampleness-of-nef-adjoint-classes-on-compact-Kahler-manifolds-October-6-2026`)
- Taming implies compatibility on four-manifolds (`Taming-implies-compatibility-on-four-manifolds-October-6-2026`)
- Termination of generalized-canonical flips on compact Kähler fourfolds (`Termination-of-generalized-canonical-flips-on-compact-Kahler-fourfolds-October-6-2026`)
- Termination of generalized log canonical flips on compact Kähler fourfolds (`Termination-of-generalized-log-canonical-flips-on-compact-Kahler-fourfolds-October-7-2026`)
- The Gaussian free field limit of integer Lipschitz heights with two-arc boundary data (`The-Gaussian-free-field-limit-of-integer-Lipschitz-heights-with-two-arc-boundary-data-October-6-2026`)
- The Selmer converse for elliptic curves at every prime (`The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026`)
- The joint scaling limit of critical Ashkin-Teller currents (`The-joint-scaling-limit-of-critical-Ashkin-Teller-currents-October-6-2026`)
- The mean analytic rank of quadratic twists of elliptic curves (`The-mean-analytic-rank-of-quadratic-twists-of-elliptic-curves-October-6-2026`)
- The p-adic section conjecture (`The-p-adic-section-conjecture-October-6-2026`)
- The rational Hodge conjecture for CM abelian varieties (`The-rational-Hodge-conjecture-for-CM-abelian-varieties-October-6-2026`)
- The two-primary Birch–Swinnerton-Dyer formula in Selmer corank at most one (`The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026`)
- Uniform real Lipschitz surfaces on the triangular lattice (`Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-October-6-2026`)
- Unrestricted pro-modularity at the prime two (`Unrestricted-pro-modularity-at-the-prime-two-October-6-2026`)
- Weil classes and Hodge classes on abelian powers (`Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026`)
