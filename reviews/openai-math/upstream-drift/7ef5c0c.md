# Upstream drift: openai/math `fd4aeeb2` (reviewed) → `7ef5c0cc`

New commit: `7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a`, 2026-10-26T14:18:03-07:00, "Merge pull request #3 from openai/codex/update-10-26". Report generated 2026-10-27T11:30:31Z by `scripts/upstream_drift.py`. Files: 40569 added, 0 deleted, 46 modified.

The published review describes the reviewed commit; nothing below changes a verdict. Families listed under "to re-read" have had a verdict input changed (headline, scope note, challenge set or statement) and are queued for a new reading; challenges under "to rebuild" are built and checked on the new commit by the pipeline.

## Summary

- Families: 373 now (372 reviewed); new 1 (378), of which with Lean 1 (378); removed none; families that gained Lean (no formalization in the reviewed release): 1 (079).
- Catalogue title or summary changed for 1 families: 079.
- Scope notes (lean/docs): 027 (M), 032 (A), 066 (M), 079 (A), 195 (M), 237 (M), 301 (M), 378 (A).
- Comparator challenges: 418 now; new 207, modified 11, removed 0.
- Solution files changed under lean/OAI: 39975; challenges whose own solution file changed: ElementaryPositivity (changes deeper in a cone are found only by rebuilding).
- Preprints: 2 directories added, 1 modified.
- Build configuration (lake-manifest, toolchain, lakefile, patches): lean/lakefile.lean — **manual step: the pipeline does not run `lake update`; rebuilds on the new commit are deferred**.
- Referee sample affected: 145.

## To re-read (18 families)

- `027` Integral density on curve character varieties — scope note changed
- `032` The rational Hodge conjecture for CM abelian varieties — new scope note — *not in the reviewed release*
- `066` Bounded klt complements for Fano contractions — scope note changed
- `079` Local smoothing for the Euclidean wave equation — catalogue title/summary changed; challenge LocalSmoothing added; family gained Lean (first formalization of this family; not among the 235 reviewed); new scope note; set of linked challenges changed — *not in the reviewed release*
- `103` Derandomization of logarithmic space: $\mathsf L=\mathsf{RL}=\mathsf{BPL}$ — challenge LogspaceEquality modified
- `110` Optimal-order randomized $k$-server on arbitrary metrics — challenge KServer modified
- `145` Rokhlin's multiple-mixing problem **(in the referee sample)** — challenge Rokhlin modified
- `158` The Euclidean plane cannot be colored with five colors — challenge EuclideanFiveColor modified
- `169` The Shareshian--Wachs $e$-positivity conjecture — challenge ElementaryPositivity modified
- `195` A counterexample to the small Cohen--Macaulay module conjecture — scope note changed
- `237` The three-quarter diameter exponent for honeycomb walks — scope note changed
- `238` Optimal logarithmic mixing of the Thorp shuffle — challenge OccupiedOverlap modified; challenge SpinAngle modified
- `297` A ZFC counterexample to Naimark's problem — challenge Naimark modified
- `301` Classification by trace cones after Razak--Jacelon stabilization — scope note changed
- `361` Counterexamples to Yau's harmonic dimension bound — challenge HarmonicGrowth modified
- `371` Stable blowup for a defocusing Schr\"odinger equation — challenge DefocusingNLS modified
- `374` Sharp one-third stability of optimal transport maps — challenge Brenier modified
- `378` Disproof of the Exponential Time Hypothesis — challenge SubexponentialSAT added; new family with Lean (not in the reviewed release); new scope note — *not in the reviewed release*

## To rebuild and check on the new commit (218 challenges)

`Affine`, `AffineIteration`, `AffineMesh`, `AffinePrism`, `AffineRelativeDimension`, `AffineRelativeMesh`, `AffineScheme`, `AffineSmall`, `AffineSmallPrism`, `AffineSpace`, `AffineSupport`, `AmbientInjectiveResolution`, `AnalyticDifferentialForms`, `AnalyticLeftInverse`, `AnalyticMap`, `AnalyticSheaf`, `Analytification`, `BarycentricAllDegrees`, `BarycentricChains`, `BarycentricHomotopy`, `BarycentricOuterFaces`, `Basic`, `Brenier`, `CM`, `CatenaryDimension`, `CenteredComplexOrientation`, `Chain`, `ChainComplexSplit`, `ChainStalk`, `Challenge`, `ChartFundamentalClass`, `ChartFundamentalClassGenerator`, `ChartFundamentalClassInvariance`, `ChartedSpaceParacompact`, `ClosedFiltration`, `ClosedImmersion`, `ClosedPointDimension`, `ClosedSubset`, `Cochain`, `CochainDescent`, `CochainFlasque`, `CochainOpenCone`, `CochainOpenConeNaturality`, `CochainOpenRestriction`, `CochainOpenSections`, `CochainResolution`, `CochainRestriction`, `CoclassOverlap`, `CoclassSection`, `Cohomology`, `CohomologyFlasqueModel`, `CohomologyInjectiveModel`, `CohomologySection`, `CohomologySheaf`, `CohomologyStalkVanishing`, `ComplexClass`, `ComplexClassDifferentiableInvariance`, `ComplexClassLinearInvariance`, `ComplexOrientation`, `Constant`, `Contractible`, `CoverSmall`, `CoverSmallProjective`, `CoverSmallQuasiIso`, `DefocusingNLS`, `Defs`, `DerivedSections`, `DerivedSectionsLocalization`, `DerivedSectionsNaturality`, `DerivedSectionsShift`, `Dimension`, `DimensionFormula`, `ElementaryPositivity`, `Equidimensional`, `Etale`, `Euclidean`, `EuclideanFiveColor`, `EuclideanVanishing`, `ExactWedge`, `Field`, `FieldToComplex`, `Filtration`, `FiniteFiltrationVanishing`, `FlasqueAcyclic`, `FlasqueBoundedBelow`, `FlasqueCokernel`, `FlasqueComparison`, `FlasqueExtendNat`, `FlasqueLowerVanishing`, `FlasqueLowestCohomology`, `FlasqueQuasiIso`, `FlasqueSections`, `FlattenedSupport`, `FundamentalClass`, `FundamentalClassGenerator`, `GenericPoint`, `GlobalRestriction`, `GlobalSections`, `HarmonicGrowth`, `HodgeStructure`, `HolomorphicCharts`, `HolomorphicDeRham`, `HolomorphicNormalTransition`, `HolomorphicPoincare`, `HomComplexPrecomp`, `HomComplexSingle`, `HomologySection`, `HomologyZeroNaturality`, `InjectiveFlasque`, `IsOpenUnits`, `KInjectiveHom`, `KServer`, `KernelAcyclic`, `KernelCompositionShortExact`, `KrullDimension`, `Lebesgue`, `LiftToInjective`, `LinearDual`, `LinearDualNaturality`, `LocalGenerator`, `LocalHomology`, `LocalHomologyVanishing`, `LocalSmoothing`, `LocalSupportVanishing`, `Localization`, `Locus`, `LogspaceEquality`, `Manifold`, `MapExtend`, `MapExtendNaturality`, `MapOfLocalStalks`, `MappingCoconeShortExact`, `MappingCoconeShortExactNaturality`, `MappingConeMapNaturality`, `MappingConeQuasiIso`, `Naimark`, `NeighborhoodPairImage`, `NestedLocalization`, `NestedOnOpen`, `NormalCoordinates`, `NormalGeometry`, `NormalProjectionCoclass`, `NormalProjectionOverlap`, `NormalSlicePurity`, `Notation`, `OccupiedOverlap`, `Open`, `OpenCover`, `OpenInjectiveResolution`, `OpenRestrictedLowestCohomology`, `OpenRestrictedVanishing`, `OpenRestriction`, `OpenSheafification`, `OpenTransport`, `Pair`, `Poincare`, `PointwiseDimension`, `PolynomialCatenary`, `Projective`, `ProjectiveCompact`, `ProjectiveHausdorff`, `ProjectiveParacompact`, `ProjectiveSpace`, `PuncturedEuclidean`, `Purity`, `RelativeCochainCone`, `RelativeCochainConeNaturality`, `RelativeCohomologyOpenTransport`, `RelativeCohomologySheaf`, `RelativeHomotopyInvariance`, `RelativePairExcision`, `ResidueField`, `RightDerivedFunctorPlusNaturality`, `RightDerivedFunctorPlusShift`, `RightDerivedFunctorPlusShiftNaturality`, `Rokhlin`, `SectionRestrictionCone`, `SectionRestrictionConeNaturality`, `SheafCohomology`, `ShortExactQuasiIso`, `SingularClosedFiltration`, `SingularCohomologySheafComparison`, `SingularComparison`, `SingularFlasqueModel`, `SingularLocusDimension`, `SingularSectionCohomology`, `SingularSectionNaturality`, `SingularSheafComparison`, `SmoothClosedLift`, `SmoothCoordinates`, `SmoothKrullDimension`, `SmoothSupportCoclassSection`, `SmoothSupportPurity`, `Solution`, `SourceOpen`, `SphereAffineBoundary`, `SphereSimplicialHomology`, `SpinAngle`, `SplitDerivativeNormalChart`, `StalkExact`, `StandardEtale`, `StandardSimplexCone`, `Statement`, `StdSimplexMetric`, `StupidTruncation`, `SubdivisionCochain`, `SubexponentialSAT`, `SubsetChains`, `Support`, `SupportExtension`, `SupportSingularGlobal`, `SupportedSingularModel`, `TopPair`, `TranscendenceDegreeKrullDimension`, `Variants`, `WedgeCovectors`, `WithSupport`, `main`

## Catalogue changes (overview summary, old → new)

### `079` Local smoothing for the Euclidean wave equation

**Old title:** Sogge's local smoothing conjecture in dimension three

**New title:** Local smoothing for the Euclidean wave equation

**Old summary:** Resolves Sogge's local smoothing conjecture for the Euclidean wave equation in three spatial dimensions. The estimate holds throughout the full strict range $2<p<\infty$, with Sobolev regularity above $\max\{0,1-3/p\}$. In particular, the critical $L^3$ estimate holds with every positive Sobolev loss.

**New summary:** Proves Sogge's local smoothing conjecture in every spatial dimension $n\ge2$, with arbitrarily small loss above the sharp Sobolev threshold. The wave estimate yields the Bochner--Riesz conjecture and, for $2\le p<\infty$, maximal bounds for these means and sharp bounds for Stein's square function. It also gives Fourier restriction throughout the interior of the conjectured range for the sphere, compact paraboloid, and truncated cone, and local smoothing for the Schrödinger equation. The Kakeya and Nikodym maximal conjectures follow. In particular, every Euclidean Kakeya set has full Hausdorff dimension.

## Changed scope notes (diff)

### `027` Integral density on curve character varieties

```diff
@@ -9,5 +9,5 @@ The following describes the scope of the Lean formalization related to the follo
 The integral-density question asks whether integral points become Zariski dense in every component of a curve character variety after one finite extension of the number field. The linked formalization proves a supporting compatibility result for its marked-surface construction. Given a proper diagram with finitely many vertices, a chosen seam with maximal adjacent facet rank and a positive-genus parent, puncture data, an existing solution over a field, and a chosen boundary occurrence, the produced marked values satisfy every seam equation.
 
-This is conditional compatibility of the produced solution. Potential integral density, including the prescribed-boundary and all-component conclusions, remains outside the selected statement.
+Existence of integral points and Zariski density are not established. The paper's main theorem—potential integral density for $\mathrm{SL}_r$ curve character varieties over one finite extension, including prescribed quasi-unipotent boundary data and every irreducible component—is outside this comparison.
 
 ## Comparator links
```

### `066` Bounded klt complements for Fano contractions

```diff
@@ -9,5 +9,7 @@ The following describes the scope of the Lean formalization related to the follo
 The paper develops uniform Cartier sections for Fano-type contractions as a step toward bounded klt complements. The linked formalization proves a local compactness result: for positive numbers $a_i$, the chart-field retractions indexed by nonnegative weights satisfying $\sum_i a_iw_i=1$ form a compact set in the pointwise topology on the fraction field.
 
-The chart is built over an algebraically closed field from the localization of a polynomial ring at its origin. Its local domain is Noetherian, essentially of finite type and formally unramified over that localization, and formally étale over the polynomial ring. Uniform Cartier sections, bounded klt complements, and the paper's real-boundary and companion conclusions are outside this supporting statement.
+The chart is built over an algebraically closed field from the localization of a polynomial ring at its origin. Its local domain is Noetherian, essentially of finite type and formally unramified over that localization, and formally étale over the polynomial ring.
+
+This compactness result applies to one such chart. It does not construct a Cartier divisor through a prescribed base point whose pullback has a positive log-canonical-threshold bound along the whole fibre depending only on dimension and discrepancy, as required by the paper's uniform Cartier-section theorem. Bounded klt complements and the paper's real-boundary and companion conclusions are also outside this comparison.
 
 ## Comparator links
```

### `195` A counterexample to the small Cohen--Macaulay module conjecture

```diff
@@ -7,7 +7,9 @@ The following describes the scope of the Lean formalization related to the follo
 ## Scope
 
-The small Cohen–Macaulay module conjecture asks whether every complete local domain has a nonzero finitely generated maximal Cohen–Macaulay module. The linked formalization verifies only the ring-theoretic candidate: there exists a three-dimensional complete Noetherian integrally closed local domain over $\mathbb C$ whose residue field is $\mathbb C$.
+The small Cohen–Macaulay module conjecture asks whether every complete Noetherian local domain has a nonzero finitely generated maximal Cohen–Macaulay module. The linked formalization verifies only the ring-theoretic candidate: there exists a three-dimensional complete Noetherian integrally closed local domain over $\mathbb C$ whose residue field is $\mathbb C$.
 
-It does not prove that this ring lacks a nonzero finitely generated maximal Cohen–Macaulay module, or the paper's counterexample essentially of finite type.
+The proof uses a constructed completed surface cone. The resulting existence statement gives only the ring properties above; it does not assert the absence of small Cohen–Macaulay modules.
+
+The paper's main counterexample requires that no nonzero finitely generated module over the ring has depth three. That conclusion, the numerical obstruction used to prove it, and the counterexample essentially of finite type are outside this comparison. The candidate's ring properties alone do not establish the counterexample.
 
 ## Comparator links
```

### `237` The three-quarter diameter exponent for honeycomb walks

```diff
@@ -22,5 +22,7 @@ For critical self-avoiding walks on the honeycomb lattice, the formalization pro
 For the prescribed-boundary-endpoint companion, let $B_h$ be the total critical weight of strict bridges crossing a strip of integral height $h$, from one fixed bottom port to all compatible top ports, with $B_0=1$. The formalization proves
 $c(1+h)^{-1/4}\le B_h\le C(1+h)^{-1/4}$
-for all $h\ge0$ and fixed positive constants $c,C$. This includes finiteness of the path sum. The prescribed-endpoint length law, arch and strip mean laws, and remaining moment and renewal conclusions are outside this supporting statement.
+for all $h\ge0$ and fixed positive constants $c,C$. This includes finiteness of the path sum.
+
+This establishes the bridge-mass estimate in the companion's finite boundary and length inputs, with the terminal port summed over. The companion's main prescribed-endpoint theorem asserts that, for every $\varepsilon>0$, the probability that a chord between two specified ports has length between $R^{4/3-\varepsilon}$ and $R^{4/3+\varepsilon}$ tends to one as $R\to\infty$ in the stated geometries. That length law, its lower bound for the normalizing mass, the arch and strip mean laws, and the remaining moment and renewal conclusions are outside this supporting comparison. The separate strip-mass and displacement-moment results above concern the strip-crossing paper.
 
 ## Comparator links
```

### `301` Classification by trace cones after Razak--Jacelon stabilization

```diff
@@ -7,7 +7,11 @@ The following describes the scope of the Lean formalization related to the follo
 ## Scope
 
-The paper classifies separable nuclear complex $C^*$-algebras after tensoring with the Razak–Jacelon algebra and the compact operators, using their cones of extended lower-semicontinuous traces. The linked formalization proves the ideal-transport part: a trace-cone equivalence induces an order isomorphism of closed two-sided ideals, carrying the ideals determined by finiteness and vanishing of each trace to those of its image.
+The paper classifies separable nuclear complex $C^*$-algebras after tensoring with the Razak–Jacelon algebra and the compact operators, using their cones of extended lower-semicontinuous traces. The linked formalization proves the supporting ideal-transport result from Section 2: a trace-cone equivalence induces an order isomorphism of closed two-sided ideals, carrying the ideals determined by finiteness and vanishing of each trace to those of its image. Here a trace-cone equivalence preserves addition, zero, positive scalar multiplication, and canonical convergence in both directions. The finite ideal is the norm closure of $\{x : \tau(x^*x)<\infty\}$; the zero ideal is characterized on positive elements by $\tau(a)=0$.
 
-For each closed ideal $I$, it also constructs the trace that is zero on positive elements of $I$ and infinite elsewhere. These traces are exactly the additive idempotents, meaning $\tau+\tau=\tau$, and their addition recovers ideal inclusion. Spatial classification, existence of the stabilization models, norm uniqueness, and final intertwining are outside this supporting comparison.
+For each closed ideal $I$, it also constructs the trace that is zero on positive elements of $I$ and infinite elsewhere. These traces are exactly the additive idempotents, meaning $\tau+\tau=\tau$, and their addition recovers ideal inclusion.
+
+The construction includes proofs of the required ideal and closure properties of the finite domain. It also proves lower semicontinuity of the support weight, which is zero where a given trace vanishes and infinite elsewhere.
+
+The paper's main conclusion is an actual isomorphism $A\otimes\mathcal W\otimes\mathcal K\cong B\otimes\mathcal W\otimes\mathcal K$ realizing the trace-cone data. This comparison does not establish that conclusion. Existence of the stabilization models, norm uniqueness, and final intertwining are also outside it.
 
 ## Comparator links
```

## Modified challenge statements (diff)

### `Brenier` (family 374)

```diff


@@ -6,18 +6,5 @@
     "OAI.Problem358.one_third_exponent_is_sharp"
   ],
-  "definition_names": [
-    "OAI.Problem358.E",
-    "OAI.Problem358.uniformMeasure",
-    "OAI.Problem358.IsSupported",
-    "OAI.Problem358.IsCoupling",
-    "OAI.Problem358.quadraticPlanCost",
-    "OAI.Problem358.wasserstein2",
-    "OAI.Problem358.graphPlan",
-    "OAI.Problem358.IsQuadraticOptimalMap",
-    "OAI.Problem358.IsUniqueQuadraticOptimalMap",
-    "OAI.Problem358.mapL2Dist",
-    "OAI.Problem358.cube",
-    "OAI.Problem358.HasExactlyThreeAtoms"
-  ],
+  "definition_names": [],
   "permitted_axioms": [
     "propext",
```

### `DefocusingNLS` (family 371)

```diff
@@ -103,7 +103,10 @@ noncomputable def sobolevProductCoefficient (k : ℝ) (f g : FourierL2)
   ∑' m, sobolevFourierCoefficient k f m * sobolevFourierCoefficient k g (n - m)
 
-noncomputable def sobolevProduct (k : ℝ) (_hk : 6 < k) (f g : FourierL2) : FourierL2 :=
-  ⟨fun n => (sobolevProductWeight k n : ℂ) * sobolevProductCoefficient k f g n,
-    by sorry⟩
+noncomputable def sobolevProduct (k : ℝ) (_hk : 6 < k) (f g : FourierL2) : FourierL2 := by
+  classical
+  exact if h : Memℓp (fun n => (sobolevProductWeight k n : ℂ) *
+      sobolevProductCoefficient k f g n) ((2 : ℕ) : ℝ≥0∞) then
+    ⟨fun n => (sobolevProductWeight k n : ℂ) * sobolevProductCoefficient k f g n, h⟩
+  else 0
 
 run_cmd Lean.modifyEnv fun env => Lean.Meta.auxLemmasExt.setState env {}
@@ -118,5 +121,6 @@ noncomputable def fourierConjugate (f : FourierL2) : FourierL2 :=
 run_cmd Lean.modifyEnv fun env => Lean.Meta.auxLemmasExt.setState env {}
 
-noncomputable def sobolevOddPower (k : ℝ) (hk : 6 < k) : ℕ → FourierL2 → FourierL2
+noncomputable def sobolevOddPower (k : ℝ) (hk : ((6 : ℕ) : ℝ) < k) :
+    ℕ → FourierL2 → FourierL2
   | 0, f => f
   | m + 1, f => sobolevProduct k hk

@@ -7,9 +7,5 @@
     "OAI.DefocusingNLS.gaussian_not_almost_sure_global"
   ],
-  "definition_names": [
-    "OAI.DefocusingNLS.sobolevProduct",
-    "OAI.DefocusingNLS.schrodingerFlow",
-    "OAI.DefocusingNLS.sobolevOddPower"
-  ],
+  "definition_names": [],
   "permitted_axioms": [
     "propext",
```

### `ElementaryPositivity` (family 169)

```diff
@@ -61,3 +61,12 @@ def elementaryPositivityWitness (n : ℕ)
   sorry
 
+theorem elementaryPositivityExpansion (n : ℕ)
+    (G : ElementaryPositivity.NaturalUnitIntervalGraph n) (r : ℕ) :
+    G.chromatic r =
+      ∑ σ : {σ : Equiv.Perm (Fin n) // G.Nondescent σ},
+        MvPolynomial.C (Polynomial.X ^ G.graphInversions σ.val) *
+          MvPolynomial.esymmPart (Fin r) (Polynomial ℕ)
+            ((elementaryPositivityWitness n G).theta σ) := by
+  sorry
+
 end OAI

@@ -2,5 +2,7 @@
   "challenge_module": "ComparatorChallenges.ElementaryPositivity",
   "solution_module": "OAI.Combinatorics.Chromatic.Main",
-  "theorem_names": [],
+  "theorem_names": [
+    "OAI.elementaryPositivityExpansion"
+  ],
   "definition_names": [
     "OAI.elementaryPositivityWitness"
```

### `EuclideanFiveColor` (family 158)

```diff


@@ -5,7 +5,5 @@
     "OAI.EuclideanFiveColor.no_proper_five_coloring"
   ],
-  "definition_names": [
-    "OAI.EuclideanFiveColor.ProperColoring"
-  ],
+  "definition_names": [],
   "permitted_axioms": [
     "propext",
```

### `HarmonicGrowth` (family 361)

```diff
@@ -96,9 +96,5 @@ def MainClaim : Prop :=
       LinearIndependent ℝ u ∧ ∀ i, HarmonicGrowth g k (u i)
 
-
-
-axiom mainStatement : MainClaim
-
-theorem main : MainClaim := mainStatement
+theorem main : MainClaim := by sorry
 
 end HarmonicCounterexample


```

### `KServer` (family 110)

```diff


@@ -5,15 +5,5 @@
     "OAI.KServer.main_theorem"
   ],
-  "definition_names": [
-    "OAI.KServer.Configuration",
-    "OAI.KServer.LabelDistribution",
-    "OAI.KServer.Policy",
-    "OAI.KServer.serve",
-    "OAI.KServer.serviceCost",
-    "OAI.KServer.pathProbability",
-    "OAI.KServer.expectedCost",
-    "OAI.KServer.optimalCost",
-    "OAI.KServer.MainStatement"
-  ],
+  "definition_names": [],
   "permitted_axioms": [
     "propext",
```

### `LogspaceEquality` (family 103)

```diff


@@ -5,26 +5,5 @@
     "OAI.ExactDerandomization.exact_logarithmic_space_derandomization"
   ],
-  "definition_names": [
-    "OAI.ExactDerandomization.Word",
-    "OAI.ExactDerandomization.Language",
-    "OAI.ExactDerandomization.CoinTape",
-    "OAI.ExactDerandomization.Direction.move",
-    "OAI.ExactDerandomization.Direction.moveInput",
-    "OAI.ExactDerandomization.readInput",
-    "OAI.ExactDerandomization.Machine.initial",
-    "OAI.ExactDerandomization.Machine.step",
-    "OAI.ExactDerandomization.Machine.run",
-    "OAI.ExactDerandomization.Machine.spaceThrough",
-    "OAI.ExactDerandomization.Machine.LogSpace",
-    "OAI.ExactDerandomization.Machine.Deterministic",
-    "OAI.ExactDerandomization.Machine.HaltsBy",
-    "OAI.ExactDerandomization.Machine.Decides",
-    "OAI.ExactDerandomization.Machine.extendCoins",
-    "OAI.ExactDerandomization.Machine.acceptanceProbability",
-    "OAI.ExactDerandomization.polynomialClock",
-    "OAI.ExactDerandomization.L",
-    "OAI.ExactDerandomization.RL",
-    "OAI.ExactDerandomization.BPL"
-  ],
+  "definition_names": [],
   "permitted_axioms": [
     "propext",
```

### `Naimark` (family 297)

```diff


@@ -5,13 +5,5 @@
     "OAI.NaimarkZFC.main"
   ],
-  "definition_names": [
-    "OAI.NaimarkZFC.IsSimpleCStar",
-    "OAI.NaimarkZFC.IsState",
-    "OAI.NaimarkZFC.IsFaithfulTracialState",
-    "OAI.NaimarkZFC.IsIrreducible",
-    "OAI.NaimarkZFC.UnitarilyEquivalent",
-    "OAI.NaimarkZFC.HasUniqueIrreducibleRepresentation",
-    "OAI.NaimarkZFC.IsIsomorphicToCompacts"
-  ],
+  "definition_names": [],
   "permitted_axioms": [
     "propext",
```

### `OccupiedOverlap` (family 238)

```diff
@@ -251,5 +251,5 @@ abbrev OccupiedOverlapEndpoint : Prop :=
         (X := hilbertSpace a) I J ≤
         Real.exp (C * (((m + n + 1 : ℕ) : ℝ) * (h : ℝ)^2 *
-          Real.log ((m * n : ℕ) + 2) + (m * n - Ω.card : ℕ))) *
+          Real.log ((m * n : ℕ) + ((2 : ℕ) : ℝ)) + (m * n - Ω.card : ℕ))) *
           min 1 ((r : ℝ) * c / Module.finrank ℂ (space a))
 

@@ -6,11 +6,5 @@
     "OAI.RowColumn.occupied_overlap"
   ],
-  "definition_names": [
-    "OAI.CubeShuffle.UnitaryFinite.IsUnitary",
-    "OAI.CubeShuffle.Specht.hilbertSpace",
-    "OAI.CubeShuffle.Specht.unitaryRepresentation",
-    "OAI.CubeShuffle.Specht.relabelledUnitary",
-    "OAI.RowColumn.OccupiedOverlapEndpoint"
-  ],
+  "definition_names": [],
   "permitted_axioms": [
     "propext",
```

### `Rokhlin` (family 145)

```diff


@@ -5,10 +5,5 @@
     "OAI.Rokhlin.mixing_all_finite_orders"
   ],
-  "definition_names": [
-    "OAI.Rokhlin.timeMap",
-    "OAI.Rokhlin.IsMixing",
-    "OAI.Rokhlin.layoutTime",
-    "OAI.Rokhlin.MixingOfOrder"
-  ],
+  "definition_names": [],
   "permitted_axioms": [
     "propext",
```

### `SpinAngle` (family 238)

```diff
@@ -410,5 +410,8 @@ def missingCellProductFactor {ι : Type*} [Fintype ι] (m : ℕ) (b : ι → ℕ
   ∏ i, missingCellFactor m (b i)
 
-variable {R C : Type*} [Fintype R] [DecidableEq R] [Fintype C] [DecidableEq C]
+universe u_2 u_3
+
+variable {R : Type u_2} {C : Type u_3}
+  [Fintype R] [DecidableEq R] [Fintype C] [DecidableEq C]
 
 def occupiedRow (W : Finset (R × C)) (i : R) : Finset C :=

@@ -5,9 +5,5 @@
     "OAI.SpinAngle.TypeAngle.one_sided_type_angle"
   ],
-  "definition_names": [
-    "OAI.SpinAngle.TypeAngle.row",
-    "OAI.SpinAngle.TypeAngle.column",
-    "OAI.SpinAngle.TypeAngle.phi"
-  ],
+  "definition_names": [],
   "permitted_axioms": [
     "propext",
```

## New challenges

- `Affine` (family ?): module `None`, theorems 
- `AffineIteration` (family ?): module `None`, theorems 
- `AffineMesh` (family ?): module `None`, theorems 
- `AffinePrism` (family ?): module `None`, theorems 
- `AffineRelativeDimension` (family ?): module `None`, theorems 
- `AffineRelativeMesh` (family ?): module `None`, theorems 
- `AffineScheme` (family ?): module `None`, theorems 
- `AffineSmall` (family ?): module `None`, theorems 
- `AffineSmallPrism` (family ?): module `None`, theorems 
- `AffineSpace` (family ?): module `None`, theorems 
- `AffineSupport` (family ?): module `None`, theorems 
- `AmbientInjectiveResolution` (family ?): module `None`, theorems 
- `AnalyticDifferentialForms` (family ?): module `None`, theorems 
- `AnalyticLeftInverse` (family ?): module `None`, theorems 
- `AnalyticMap` (family ?): module `None`, theorems 
- `AnalyticSheaf` (family ?): module `None`, theorems 
- `Analytification` (family ?): module `None`, theorems 
- `BarycentricAllDegrees` (family ?): module `None`, theorems 
- `BarycentricChains` (family ?): module `None`, theorems 
- `BarycentricHomotopy` (family ?): module `None`, theorems 
- `BarycentricOuterFaces` (family ?): module `None`, theorems 
- `Basic` (family ?): module `None`, theorems 
- `CM` (family ?): module `None`, theorems 
- `CatenaryDimension` (family ?): module `None`, theorems 
- `CenteredComplexOrientation` (family ?): module `None`, theorems 
- `Chain` (family ?): module `None`, theorems 
- `ChainComplexSplit` (family ?): module `None`, theorems 
- `ChainStalk` (family ?): module `None`, theorems 
- `Challenge` (family ?): module `None`, theorems 
- `ChartFundamentalClass` (family ?): module `None`, theorems 
- `ChartFundamentalClassGenerator` (family ?): module `None`, theorems 
- `ChartFundamentalClassInvariance` (family ?): module `None`, theorems 
- `ChartedSpaceParacompact` (family ?): module `None`, theorems 
- `ClosedFiltration` (family ?): module `None`, theorems 
- `ClosedImmersion` (family ?): module `None`, theorems 
- `ClosedPointDimension` (family ?): module `None`, theorems 
- `ClosedSubset` (family ?): module `None`, theorems 
- `Cochain` (family ?): module `None`, theorems 
- `CochainDescent` (family ?): module `None`, theorems 
- `CochainFlasque` (family ?): module `None`, theorems 
- `CochainOpenCone` (family ?): module `None`, theorems 
- `CochainOpenConeNaturality` (family ?): module `None`, theorems 
- `CochainOpenRestriction` (family ?): module `None`, theorems 
- `CochainOpenSections` (family ?): module `None`, theorems 
- `CochainResolution` (family ?): module `None`, theorems 
- `CochainRestriction` (family ?): module `None`, theorems 
- `CoclassOverlap` (family ?): module `None`, theorems 
- `CoclassSection` (family ?): module `None`, theorems 
- `Cohomology` (family ?): module `None`, theorems 
- `CohomologyFlasqueModel` (family ?): module `None`, theorems 
- `CohomologyInjectiveModel` (family ?): module `None`, theorems 
- `CohomologySection` (family ?): module `None`, theorems 
- `CohomologySheaf` (family ?): module `None`, theorems 
- `CohomologyStalkVanishing` (family ?): module `None`, theorems 
- `ComplexClass` (family ?): module `None`, theorems 
- `ComplexClassDifferentiableInvariance` (family ?): module `None`, theorems 
- `ComplexClassLinearInvariance` (family ?): module `None`, theorems 
- `ComplexOrientation` (family ?): module `None`, theorems 
- `Constant` (family ?): module `None`, theorems 
- `Contractible` (family ?): module `None`, theorems 
- `CoverSmall` (family ?): module `None`, theorems 
- `CoverSmallProjective` (family ?): module `None`, theorems 
- `CoverSmallQuasiIso` (family ?): module `None`, theorems 
- `Defs` (family ?): module `None`, theorems 
- `DerivedSections` (family ?): module `None`, theorems 
- `DerivedSectionsLocalization` (family ?): module `None`, theorems 
- `DerivedSectionsNaturality` (family ?): module `None`, theorems 
- `DerivedSectionsShift` (family ?): module `None`, theorems 
- `Dimension` (family ?): module `None`, theorems 
- `DimensionFormula` (family ?): module `None`, theorems 
- `Equidimensional` (family ?): module `None`, theorems 
- `Etale` (family ?): module `None`, theorems 
- `Euclidean` (family ?): module `None`, theorems 
- `EuclideanVanishing` (family ?): module `None`, theorems 
- `ExactWedge` (family ?): module `None`, theorems 
- `Field` (family ?): module `None`, theorems 
- `FieldToComplex` (family ?): module `None`, theorems 
- `Filtration` (family ?): module `None`, theorems 
- `FiniteFiltrationVanishing` (family ?): module `None`, theorems 
- `FlasqueAcyclic` (family ?): module `None`, theorems 
- `FlasqueBoundedBelow` (family ?): module `None`, theorems 
- `FlasqueCokernel` (family ?): module `None`, theorems 
- `FlasqueComparison` (family ?): module `None`, theorems 
- `FlasqueExtendNat` (family ?): module `None`, theorems 
- `FlasqueLowerVanishing` (family ?): module `None`, theorems 
- `FlasqueLowestCohomology` (family ?): module `None`, theorems 
- `FlasqueQuasiIso` (family ?): module `None`, theorems 
- `FlasqueSections` (family ?): module `None`, theorems 
- `FlattenedSupport` (family ?): module `None`, theorems 
- `FundamentalClass` (family ?): module `None`, theorems 
- `FundamentalClassGenerator` (family ?): module `None`, theorems 
- `GenericPoint` (family ?): module `None`, theorems 
- `GlobalRestriction` (family ?): module `None`, theorems 
- `GlobalSections` (family ?): module `None`, theorems 
- `HodgeStructure` (family ?): module `None`, theorems 
- `HolomorphicCharts` (family ?): module `None`, theorems 
- `HolomorphicDeRham` (family ?): module `None`, theorems 
- `HolomorphicNormalTransition` (family ?): module `None`, theorems 
- `HolomorphicPoincare` (family ?): module `None`, theorems 
- `HomComplexPrecomp` (family ?): module `None`, theorems 
- `HomComplexSingle` (family ?): module `None`, theorems 
- `HomologySection` (family ?): module `None`, theorems 
- `HomologyZeroNaturality` (family ?): module `None`, theorems 
- `InjectiveFlasque` (family ?): module `None`, theorems 
- `IsOpenUnits` (family ?): module `None`, theorems 
- `KInjectiveHom` (family ?): module `None`, theorems 
- `KernelAcyclic` (family ?): module `None`, theorems 
- `KernelCompositionShortExact` (family ?): module `None`, theorems 
- `KrullDimension` (family ?): module `None`, theorems 
- `Lebesgue` (family ?): module `None`, theorems 
- `LiftToInjective` (family ?): module `None`, theorems 
- `LinearDual` (family ?): module `None`, theorems 
- `LinearDualNaturality` (family ?): module `None`, theorems 
- `LocalGenerator` (family ?): module `None`, theorems 
- `LocalHomology` (family ?): module `None`, theorems 
- `LocalHomologyVanishing` (family ?): module `None`, theorems 
- `LocalSmoothing` (family 079): module `OAI.Analysis.Fourier.LocalSmoothing.Comparator`, theorems `OAI.Analysis.Fourier.LocalSmoothing.Comparator.euclidean_local_smoothing`, `OAI.Analysis.Fourier.LocalSmoothing.Comparator.bochner_riesz`, `OAI.Analysis.Fourier.LocalSmoothing.Comparator.spherical_restriction`, `OAI.Analysis.Fourier.LocalSmoothing.Comparator.kakeya_maximal`, `OAI.Analysis.Fourier.LocalSmoothing.Comparator.kakeya`, `OAI.Analysis.Fourier.LocalSmoothing.Comparator.stein_square`
- `LocalSupportVanishing` (family ?): module `None`, theorems 
- `Localization` (family ?): module `None`, theorems 
- `Locus` (family ?): module `None`, theorems 
- `Manifold` (family ?): module `None`, theorems 
- `MapExtend` (family ?): module `None`, theorems 
- `MapExtendNaturality` (family ?): module `None`, theorems 
- `MapOfLocalStalks` (family ?): module `None`, theorems 
- `MappingCoconeShortExact` (family ?): module `None`, theorems 
- `MappingCoconeShortExactNaturality` (family ?): module `None`, theorems 
- `MappingConeMapNaturality` (family ?): module `None`, theorems 
- `MappingConeQuasiIso` (family ?): module `None`, theorems 
- `NeighborhoodPairImage` (family ?): module `None`, theorems 
- `NestedLocalization` (family ?): module `None`, theorems 
- `NestedOnOpen` (family ?): module `None`, theorems 
- `NormalCoordinates` (family ?): module `None`, theorems 
- `NormalGeometry` (family ?): module `None`, theorems 
- `NormalProjectionCoclass` (family ?): module `None`, theorems 
- `NormalProjectionOverlap` (family ?): module `None`, theorems 
- `NormalSlicePurity` (family ?): module `None`, theorems 
- `Notation` (family ?): module `None`, theorems 
- `Open` (family ?): module `None`, theorems 
- `OpenCover` (family ?): module `None`, theorems 
- `OpenInjectiveResolution` (family ?): module `None`, theorems 
- `OpenRestrictedLowestCohomology` (family ?): module `None`, theorems 
- `OpenRestrictedVanishing` (family ?): module `None`, theorems 
- `OpenRestriction` (family ?): module `None`, theorems 
- `OpenSheafification` (family ?): module `None`, theorems 
- `OpenTransport` (family ?): module `None`, theorems 
- `Pair` (family ?): module `None`, theorems 
- `Poincare` (family ?): module `None`, theorems 
- `PointwiseDimension` (family ?): module `None`, theorems 
- `PolynomialCatenary` (family ?): module `None`, theorems 
- `Projective` (family ?): module `None`, theorems 
- `ProjectiveCompact` (family ?): module `None`, theorems 
- `ProjectiveHausdorff` (family ?): module `None`, theorems 
- `ProjectiveParacompact` (family ?): module `None`, theorems 
- `ProjectiveSpace` (family ?): module `None`, theorems 
- `PuncturedEuclidean` (family ?): module `None`, theorems 
- `Purity` (family ?): module `None`, theorems 
- `RelativeCochainCone` (family ?): module `None`, theorems 
- `RelativeCochainConeNaturality` (family ?): module `None`, theorems 
- `RelativeCohomologyOpenTransport` (family ?): module `None`, theorems 
- `RelativeCohomologySheaf` (family ?): module `None`, theorems 
- `RelativeHomotopyInvariance` (family ?): module `None`, theorems 
- `RelativePairExcision` (family ?): module `None`, theorems 
- `ResidueField` (family ?): module `None`, theorems 
- `RightDerivedFunctorPlusNaturality` (family ?): module `None`, theorems 
- `RightDerivedFunctorPlusShift` (family ?): module `None`, theorems 
- `RightDerivedFunctorPlusShiftNaturality` (family ?): module `None`, theorems 
- `SectionRestrictionCone` (family ?): module `None`, theorems 
- `SectionRestrictionConeNaturality` (family ?): module `None`, theorems 
- `SheafCohomology` (family ?): module `None`, theorems 
- `ShortExactQuasiIso` (family ?): module `None`, theorems 
- `SingularClosedFiltration` (family ?): module `None`, theorems 
- `SingularCohomologySheafComparison` (family ?): module `None`, theorems 
- `SingularComparison` (family ?): module `None`, theorems 
- `SingularFlasqueModel` (family ?): module `None`, theorems 
- `SingularLocusDimension` (family ?): module `None`, theorems 
- `SingularSectionCohomology` (family ?): module `None`, theorems 
- `SingularSectionNaturality` (family ?): module `None`, theorems 
- `SingularSheafComparison` (family ?): module `None`, theorems 
- `SmoothClosedLift` (family ?): module `None`, theorems 
- `SmoothCoordinates` (family ?): module `None`, theorems 
- `SmoothKrullDimension` (family ?): module `None`, theorems 
- `SmoothSupportCoclassSection` (family ?): module `None`, theorems 
- `SmoothSupportPurity` (family ?): module `None`, theorems 
- `Solution` (family ?): module `None`, theorems 
- `SourceOpen` (family ?): module `None`, theorems 
- `SphereAffineBoundary` (family ?): module `None`, theorems 
- `SphereSimplicialHomology` (family ?): module `None`, theorems 
- `SplitDerivativeNormalChart` (family ?): module `None`, theorems 
- `StalkExact` (family ?): module `None`, theorems 
- `StandardEtale` (family ?): module `None`, theorems 
- `StandardSimplexCone` (family ?): module `None`, theorems 
- `Statement` (family ?): module `None`, theorems 
- `StdSimplexMetric` (family ?): module `None`, theorems 
- `StupidTruncation` (family ?): module `None`, theorems 
- `SubdivisionCochain` (family ?): module `None`, theorems 
- `SubexponentialSAT` (family 378): module `OAI.Algorithms.SubexponentialSAT.Main`, theorems `OAI.Algorithms.SubexponentialSAT.SqrtLogSpace.exact_count_and_sat`
- `SubsetChains` (family ?): module `None`, theorems 
- `Support` (family ?): module `None`, theorems 
- `SupportExtension` (family ?): module `None`, theorems 
- `SupportSingularGlobal` (family ?): module `None`, theorems 
- `SupportedSingularModel` (family ?): module `None`, theorems 
- `TopPair` (family ?): module `None`, theorems 
- `TranscendenceDegreeKrullDimension` (family ?): module `None`, theorems 
- `Variants` (family ?): module `None`, theorems 
- `WedgeCovectors` (family ?): module `None`, theorems 
- `WithSupport` (family ?): module `None`, theorems 
- `main` (family ?): module `None`, theorems 

## New preprints

- Local smoothing for the Euclidean wave equation (`Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026`)
- The Exponential Time Hypothesis is False (`The-Exponential-Time-Hypothesis-is-False-October-25-2026`)
