# Lean scope audit, part 2 (families 167-377 with a `lean/docs/NNN.md`)

Audited commit: `adc7f1241b42e322a6451854ab7e4b4c146bf78a` (openai/math). Method: for each family, the overview summary (index.json), `lean/docs/NNN.md`, every linked `ComparatorChallenges/<Name>.lean` statement and the definitions it depends on were read; verdicts rest only on the challenge statements, not on `([Lean])` tags. When docs and Lean disagree, Lean wins and the contradiction is noted.

Verdict scale: `full` = Comparator statement(s) state the summary's headline faithfully; `partial` = only a special case / one of several headline claims; `supporting-only` = lemma or auxiliary statement, not the headline; `weaker-statement` = a nontrivially weaker statement; `none` = nothing in the summary is covered.

Verdict policy (applied uniformly): the verdict is about the summary's primary (first-named) claim. `full` iff the Lean statement implies that claim after unpacking definitions or a routine step (the step is named in the note); `weaker-statement` iff the Lean statement does not imply the claim; a second co-equal headline claim of the summary (joined by 'also', 'complementary theorem', 'and') that has no challenge statement makes the verdict `partial`, whereas a mere corollary/application ('together with X this shows') is only noted. The routine step from the Lean form to the summary's form is always named in the note.

Conventions: `external` lists packages in the import cone other than Mathlib, Lean core and Init (those are in every cone). `cone_lines` = lines of `lean/OAI` files in the transitive import cone of each challenge's solution module (tmp/import_cones.json `oai_lines`, recomputed with an import parser that also handles `import all X` and module names containing an apostrophe; the recomputation differs from tmp/import_cones.json only for HarmonicArtin (62,869 -> 62,901), ArtinParabolicIntersections (73,065 -> 73,097) and WeakHessian (64,010 -> 65,542), and removes the spurious external entries `all` (231, Koebe, Ryser) and `OAI` (254); excludes Mathlib and external packages).

## 167 - Pinned distances and a power saving for planar unit distances

- **Verdict:** `full`
- **Challenges:** PinnedDistances, PlanarUnitDistances
- **Cone (OAI lines):** PinnedDistances 15,657, PlanarUnitDistances 28,113 (max 28,113)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `WeakPinned.main : Tendsto (fun n => F n s) atTop (𝓝 0)` with `F n s = sSup {pairFraction P s | P.card = n}` states the rich-pair-fraction form; the summary's 'all but o(n) points determine >= n^{1-eps} distinct distances' follows by a routine pigeonhole step (docs: 'Consequently') that is not itself stated in Lean. The unit-distance theorem IS also stated (`∃ C β, 0 < C ∧ 1 ≤ β ∧ β < 4/3 ∧ ∀ n, (u n:ℝ) ≤ C * n^β`, u = sSup over n-point sets, bounded so a true max); docs paragraph 1 says it 'is not included' but the Lean contradicts that (Lean wins).
- **Suspicious/non-standard definitions:** none found

## 168 - Combinatorial invariance of Kazhdan--Lusztig polynomials

- **Verdict:** `full`
- **Challenges:** KLInvariance
- **Cone (OAI lines):** KLInvariance 42,948
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `combinatorial_invariance` takes arbitrary Coxeter systems `cs`, `cs'` (different W, W' allowed) and `ι : Interval cs u b ≃o Interval cs' u' b'` and concludes `klPolynomial cs u b = klPolynomial cs' u' b'`; `BruhatLE` is the genuine strong Bruhat order (ReflTransGen of length-increasing reflection steps) and the R/P normalization is the standard Kazhdan-Lusztig characterization.
- **Suspicious/non-standard definitions:**
  - `noncomputable def klFamilies (cs) := Classical.epsilon (NormalizedKL cs)` and `klPolynomial cs x y := (klFamilies cs).2 x y`: KL polynomials are defined as an arbitrary solution of the normalization axioms (existence/uniqueness not part of the statement); this is the standard characterization and not trivializing, but it is a non-Mathlib, choice-based definition.

## 169 - The Shareshian--Wachs $e$-positivity conjecture

- **Verdict:** `full`
- **Challenges:** ElementaryPositivity
- **Cone (OAI lines):** ElementaryPositivity 74,575
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `elementaryPositivityWitness n G : G.PermutationWitness` (a `def` closed by `sorry`, not a `theorem`) must supply `theta : {σ // G.Nondescent σ} → Nat.Partition n` with `∀ r, G.chromatic r = Σ_σ C(X^(graphInversions σ)) * esymmPart (theta σ)` in `MvPolynomial (Fin r) ℕ[X]`: an explicit ℕ[q]-positive e-expansion for every natural unit interval graph (stronger than bare positivity). Chromatic quasisymmetric function and Hessenberg-function graphs are the standard definitions.
- **Suspicious/non-standard definitions:** none found

## 170 - Sharp logarithmic exponents for off-diagonal Ramsey numbers

- **Verdict:** `full`
- **Challenges:** RamseyFive, SharpLogRamsey
- **Cone (OAI lines):** RamseyFive 73,678, SharpLogRamsey 63,795 (max 73,678)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `RamseyFive.main : SharpBounds ∧ SharpExponent` covers s=5 (lower `t^4/(log t)^(3+ε)`, upper `C t^4/(log t)^3`, and `(4 log t - log r(5,t))/log log t -> 3`); `SharpLogRamsey.main (s) (hs : 6 ≤ s) : MainBounds s ∧ MainLimit s` covers every s >= 6, so together all s >= 5. r(s,t) = `sInf {n | ∀ G : SimpleGraph (Fin n), K_s ∨ independent t-set}` with Mathlib `IsNClique`/`IsNIndepSet`, standard.
- **Suspicious/non-standard definitions:** none found

## 172 - Classification of finite Euclidean Ramsey configurations

- **Verdict:** `partial`
- **Challenges:** EuclideanRamsey, EuclideanRamseyCircle, EuclideanRamseyNine, EuclideanRamseyQuadratic, EuclideanRamseySpherical, EuclideanRamseyTransitive, GrahamSpherical
- **Cone (OAI lines):** EuclideanRamsey 6,558, EuclideanRamseyCircle 7,309, EuclideanRamseyNine 1,898, EuclideanRamseyQuadratic 6,828, EuclideanRamseySpherical 6,742, EuclideanRamseyTransitive 6,718, GrahamSpherical 969 (max 7,309)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Classification is only for full-affine-span configurations: `classification (hs : 2 ≤ s) (hd : 1 ≤ d) (ha : Injective a) (hspan : affineSpan ℝ (range a) = ⊤) : Ramsey a ↔ FieldCriterion a` (docs: 'for full-affine-span configurations'; the isometric re-embedding reduction to this case is not a challenge statement). The summary's disproof of the Leader-Russell-Walters conjecture has no statement: only the Ramsey half is present (`at_most_five_circle_points_ramsey`, `nine_circle_configuration`, `GrahamSpherical.full_main` = a 12-point non-Ramsey spherical set), nothing says some Ramsey configuration is not contained in a finite transitive set.
- **Suspicious/non-standard definitions:** none found

## 173 - Seymour's second-neighborhood conjecture

- **Verdict:** `full`
- **Challenges:** SeymourSecondNeighborhood
- **Cone (OAI lines):** SeymourSecondNeighborhood 4,861
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `exists_goodVertex (r) (hr : IsOriented r) : ∃ v, GoodVertex r v` over a nonempty `Fintype V`, with `GoodVertex r v := (firstNeighbors r v).card ≤ (secondNeighbors r v).card` and second neighbors `{w | w ≠ v ∧ ¬ r v w ∧ ∃ u, r v u ∧ r u w}` (directed distance exactly two); `IsOriented` = loopless + asymmetric. Exactly Seymour's conjecture.
- **Suspicious/non-standard definitions:** none found

## 174 - Deterministic construction of strong thin spanning trees

- **Verdict:** `full`
- **Challenges:** AlgorithmicThinTrees, StrongThinTree
- **Cone (OAI lines):** AlgorithmicThinTrees 101,101, StrongThinTree 17,363 (max 101,101)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `StrongThinTree.MainStatement` (`∃ C > 0, ∀ k ≥ 1, ∀ n m, 2 ≤ n → ∀ G : MultiGraph n m, G.EdgeConnected k → ∃ T, G.SpanningTree T ∧ ∀ S, |cut T S| ≤ (C/k) * |cut univ S|`) is the existence theorem; `AlgorithmicStrongThinTrees` adds `∃ M : CurrentKS.Machine, ∃ a degree, ... result.state = none ∧ GoodOutput C x ...` for explicit and binary-multiplicity inputs. Both parts of the summary are stated; binary multiplicities are really binary (`encodeNat n = frame (Computability.encodeNat n)` and Mathlib's `encodeNat` is binary).
- **Suspicious/non-standard definitions:**
  - `CurrentKS.Machine` (hand-rolled multi-stack machine with a lookup table, `Machine.run` with a fuel argument) and the notion of polynomial time `M.run x.encode (a * (x.length + 1) ^ degree)` halting with `state = none`: a custom model, not Mathlib's `TM2ComputableInPolyTime`; multi-stack machines are polynomially equivalent to Turing machines so this looks faithful, but 'polynomial time' is a bespoke definition.

## 175 - Talagrand's conjectures and graph decompositions at expectation thresholds

- **Verdict:** `partial`
- **Challenges:** TalagrandDiscreteConvexity, TalagrandExpectationThreshold
- **Cone (OAI lines):** TalagrandDiscreteConvexity 4,259, TalagrandExpectationThreshold 4,834 (max 4,834)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Two of the three claims are stated with explicit constants: `talagrand_expectation_threshold_equivalence : qf F ≤ (25 * 512^4) * q F` (increasing nonempty proper F) and `talagrand_discrete_convexity` with k = 2^75 (`Small p (exceptional (2^75) D)` from `1 - 1/2^75 ≤ familyMeasure p D`). The summary's application, the Ascoli-He-Park-Talagrand graph-decomposition conjecture (also in the family title), has no challenge statement and the docs do not mention it.
- **Suspicious/non-standard definitions:** none found

## 176 - The second Kahn--Kalai conjecture

- **Verdict:** `full`
- **Challenges:** SecondKahnKalai
- **Cone (OAI lines):** SecondKahnKalai 6,753
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `secondKahnKalaiBounds (n) (V) (H) (hn : 2 ≤ n) (hcard : Fintype.card V ≤ n) (hedge : 1 ≤ edgeCount H) : criticalThreshold n H ≤ min 1 (2048 * exp 50 * expectationThreshold n H * (1 + logTwo (edgeCount H))) ∧ criticalThreshold n H ≤ 6144 * exp 50 * expectationThreshold n H * logTwo n`; criticalThreshold = sInf{p | P(G(n,p) contains a copy) ≥ 1/2} using Mathlib `copyCount`, expectationThreshold = sInf{p | ∀ F : H.Subgraph, E[copies of F] ≥ 1/2}. Matches the summary's p_E definition with explicit universal C.
- **Suspicious/non-standard definitions:** none found

## 177 - Bounded-degree coboundary expanders in every dimension

- **Verdict:** `full`
- **Challenges:** CoboundaryExpanders
- **Cone (OAI lines):** CoboundaryExpanders 33,125
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `MainStatement : ∀ d ≥ 3, ∃ D ε, 0 < ε ∧ ∃ X : ℕ → Complex, (∀ m, Pure d ∧ Connected) ∧ #vertices → ∞ ∧ (∀ m v, topDegree d v ≤ D) ∧ ∀ m, ∀ i < d, ∀ f, ε * distance f (coboundaries i) ≤ norm (coboundary f)` over ZMod 2 with top-face-weighted norms (weight = normalized incident top-face count). Standard weighted coboundary expansion; the graph and 2-dim cases are not part of the claim, as the summary says.
- **Suspicious/non-standard definitions:** none found

## 179 - The circulant Hadamard conjecture

- **Verdict:** `full`
- **Challenges:** CirculantHadamard, EvenBarker
- **Cone (OAI lines):** CirculantHadamard 9,496, EvenBarker 9,773 (max 9,773)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `exists_iff_order_one_or_four (n) (hn : 0 < n) : ExistsRealCirculantHadamard n ↔ n = 1 ∨ n = 4` with `IsCirculant H := ∃ h, ∀ i j, H i j = h (j - i)` and `IsSignHadamard H := (∀ i j, IsSign (H i j)) ∧ H * Hᵀ = n • 1`: exact statement of the headline. The Barker corollary is only half stated (`even_length_eq_two_or_four : Even n → IsBarker h → n = 2 ∨ n = 4`); odd lengths and the 'exist exactly at {2,3,4,5,7,11,13}' classification are not in Lean (docs: 'outside this selected additional statement').
- **Suspicious/non-standard definitions:** none found

## 180 - Barnette's Hamiltonian-cycle conjecture

- **Verdict:** `full`
- **Challenges:** BarnetteHamiltonian
- **Cone (OAI lines):** BarnetteHamiltonian 8,936
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `Barnette.main : MainStatement` = `∀ V [Fintype V] G, G.IsRegularOfDegree 3 → G.IsBipartite → Planar G → ThreeVertexConnected G → HasHamiltonianCycle G`, with `Planar` an explicit crossing-free topological embedding (`PlaneEmbedding` with `Path` arcs in ℝ×ℝ), `ThreeVertexConnected` = card >= 4 and connected after deleting any <= 2 vertices, and Mathlib `IsHamiltonianCycle`. The summary's 'equivalently ... Pfaffian graph' reformulation is not stated.
- **Suspicious/non-standard definitions:** none found

## 181 - The Erd\H{o}s--Gallai cycle-decomposition conjecture

- **Verdict:** `full`
- **Challenges:** CycleDecomposition
- **Cone (OAI lines):** CycleDecomposition 21,451
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `MainStatement : ∃ C > 0, ∀ n (G : SimpleGraph (Fin n)), ∃ k, EdgeDecomposition G k ∧ k ≤ C * n` where `EdgeDecomposition` = pairwise-disjoint parts each `CycleOrSingleEdge` (edge set of a Mathlib `IsCycle` walk or `{e}`) covering `G.edgeSet`. Exactly the Erdős–Gallai conjecture with an absolute constant.
- **Suspicious/non-standard definitions:** none found

## 182 - Power savings for polynomial-difference-free sets

- **Verdict:** `partial`
- **Challenges:** SquareDifference
- **Cone (OAI lines):** SquareDifference 24,221
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Only the square case h(x) = x^2 is stated: `IsSquareDifferenceFree A := ∀ a ∈ A, ∀ b ∈ A, ∀ m ≥ 1, a - b ≠ m^2` and `∃ c C, 0 < c ∧ ∀ N ≥ 1, ∀ A ⊆ Icc 1 N, ... → A.card ≤ C * N^(1-c)` (docs: 'a fixed power saving for sets with no nonzero square difference'). The summary's general intersective polynomials of degree k >= 2 (with c_k depending only on degree) and the prime-argument result are not formalized.
- **Suspicious/non-standard definitions:** none found

## 183 - Power savings for planar halving lines and $k$-sets

- **Verdict:** `partial`
- **Challenges:** HalvingLines
- **Cone (OAI lines):** HalvingLines 18,237
- **External packages:** none beyond Mathlib/Lean core
- **Note:** First half is stated: `∃ ε>0, C, n₀, ∀ even n ≥ n₀, ∀ P, GeneralPosition P → halvingCount P ≤ C * n^(4/3-ε)`. The k-set claim O(n(k+1)^{1/3-ε0}) for 1 <= k <= n/2 is NOT stated: the second conjunct only bounds `switchCount P k` (level-switch pairs) by `C * n^(4/3-ε)` uniformly in k, for the stronger hypothesis `Generic P` (distinct x-coordinates/slopes plus a segment-crossing condition), i.e. a weaker, k-independent bound on a different count (docs: 'a bound of the same form for all level-switch counts under the additional generic-position assumptions').
- **Suspicious/non-standard definitions:** none found

## 184 - Coloring and independence in graphs with forbidden subgraphs

- **Verdict:** `partial`
- **Challenges:** CliqueFreeLog
- **Cone (OAI lines):** CliqueFreeLog 5,539
- **External packages:** none beyond Mathlib/Lean core
- **Note:** PRIMARY CLAIM NOT STATED (only a secondary result is formalized). Only the independence half is stated: `logarithmic_independence_bound (r) (hr : 4 ≤ r) : ∃ c > 0, ∀ G, G.CliqueFree r → 2 ≤ averageDegree G → c * n * log d / d ≤ G.indepNum` (averageDegree = 2|E|/|V|). The summary's first and primary claim, the Alon-Krivelevich-Sudakov coloring conjecture in correspondence-coloring form (O_F(Δ/log Δ) colors for any fixed forbidden subgraph F), has no Lean statement, and the docs scope also only mentions the independence bound.
- **Suspicious/non-standard definitions:** none found

## 185 - Counterexamples to infinite matroid intersection and packing/covering

- **Verdict:** `full`
- **Challenges:** InfiniteMatroid, InfiniteMatroidCorollaries
- **Cone (OAI lines):** InfiniteMatroid 4,016, InfiniteMatroidCorollaries 4,477 (max 4,477)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `InfiniteMatroid.main` gives countable infinite `E`, two self-dual matroids with `∀ I₀ I₁ indep, I₀ ∪ I₁ ≠ univ` and `¬ HasPackingCovering M₀ M₁`; `partitional_intersection_counterexample` adds `IsPartitional M₀ ∧ IsPartitional M₁ ∧ ¬ HasIntersection M₀ M₁` (answering Joó's partitional question), and `separate_covering_packing_counterexamples` refutes the covering and packing conjectures separately. Uses Mathlib's infinite `Matroid`; the conjecture predicates (`HasIntersection`, `HasPackingCovering`, `contractOnto M C := (M.dual ↾ C).dual`) are written out by hand and look standard.
- **Suspicious/non-standard definitions:** none found

## 186 - The Friedgut--Kalai graph and hypergraph threshold conjectures

- **Verdict:** `partial`
- **Challenges:** SharpThreshold
- **Cone (OAI lines):** SharpThreshold 7,699
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Only the graph case is stated: `sharp_threshold_width` for vertex-invariant increasing nontrivial `f` on `GraphConfig n`, `graphQuantile (1-ε) f - graphQuantile ε f ≤ (2^19/(log n)^2) * log(1/(2ε))`. The r-uniform hypergraph width O_r((log n)^{-r/(r-1)}) for r >= 3 and the nonmonotone influence bound named in the summary have no statement (docs: graph case only).
- **Suspicious/non-standard definitions:** none found

## 187 - Snaky in 21 Maker moves

- **Verdict:** `full`
- **Challenges:** SnakyCertificate, SnakyConditional, SnakyTwentyOne
- **Cone (OAI lines):** SnakyCertificate 20,237, SnakyConditional 37,837, SnakyTwentyOne 71,326 (max 71,326)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `SnakyPrototype.snaky_winning_strategy_21_with_legal_states : ∃ σ : Policy Cell, (∀ r M B, σ r M B ∉ M ∧ σ r M B ∉ B) ∧ ∀ β, LegalRepliesBeforeFinal σ 21 β ∅ ∅ → HasSnaky (playState σ 21 β ∅ ∅ 21).1 ∧ ...card = 21 ∧ ...` on ℤ×ℤ with all 8 dihedral orientations plus translations, Maker first. The other two challenges are supporting: `SnakyCertificate.certificate_correct` checks a 610-row certificate table (`TableValid ∧ placementCount = 1837 ∧ Output 557 ...`), and `SnakyConditional` is actually the N=35 strategy from the empty board, NOT the 'four conditional winning templates' the docs describe (docs/Lean mismatch).
- **Suspicious/non-standard definitions:**
  - Hand-rolled game model: `Policy α := ℕ → Finset α → Finset α → α`, `playState σ N β M₀ B₀` with Breaker as a fixed sequence `β : ℕ → Cell` (equivalent to an adaptive Breaker against a deterministic σ) and `LegalRepliesBeforeFinal` constraining Breaker only for `k + 1 < N`; looks faithful (final reply unused).

## 188 - The sharp constant in random triangle removal

- **Verdict:** `full`
- **Challenges:** TriangleRemoval
- **Cone (OAI lines):** TriangleRemoval 33,800
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `sharp_terminal_leave` states, for the Mathlib-`PMF` Markov chain `evolve (completeGraph n) (n.choose 2)` that deletes a uniformly chosen remaining triangle (`PMF.uniformOfFinset (triangles G)`), (i) `E[(|G|/n^(3/2) - 1/(2√2))^2] → 0`, (ii) convergence in probability, (iii) `E|G|/n^(3/2) → 1/(2√2)`. This is the summary's mean-square convergence; the process is absorbing at triangle-free graphs so running C(n,2) steps gives the terminal law.
- **Suspicious/non-standard definitions:** none found

## 189 - Exact cycle--clique Ramsey numbers

- **Verdict:** `full`
- **Challenges:** CycleCliqueRamsey
- **Cone (OAI lines):** CycleCliqueRamsey 2,795,707
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `thm_main : (∀ m n : ℤ, n ≤ m → 3 ≤ n → (m, n) ≠ (3, 3) → (cycleCliqueRamsey m.toNat n.toNat : ℤ) = (m - 1) * (n - 1) + 1) ∧ cycleCliqueRamsey 3 3 = 6`, with `RamseyProperty m n N := ∀ G : SimpleGraph (Fin N), cycleGraph m ⊑ G ∨ (⊤ : SimpleGraph (Fin n)) ⊑ Gᶜ` (Mathlib `IsContained`) and `sInf` over ℕ: the exact EFRS statement. Note the import cone is 2.8M lines of `lean/OAI`, the largest in this range.
- **Suspicious/non-standard definitions:** none found

## 190 - Polynomial removal fails for ordered binary matrices

- **Verdict:** `full`
- **Challenges:** MatrixRemoval
- **Cone (OAI lines):** MatrixRemoval 7,609
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `no_polynomial_removal_bound : ∀ c C > 0, ∃ n ≥ 1, ∃ ε ∈ (0,1), ∃ A : BinaryMatrix n, fixedDistance A ≥ ε ∧ copyCount fixedH A < c * ε^C * n^132` for the explicit 66x66 `fixedH`; `copyCount` counts pairs of strictly increasing row/column maps with `A (r i) (c j) = H i j` (ordered, zeros and ones matched) and `fixedMinEdits` is a true min Hamming distance to pattern-free matrices (junk branch n*n+1 exceeds any distance). Matches the summary and docs.
- **Suspicious/non-standard definitions:** none found

## 191 - A power improvement in the Heilbronn triangle problem

- **Verdict:** `weaker-statement`
- **Challenges:** HeilbronnTriangle
- **Cone (OAI lines):** HeilbronnTriangle 24,275
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `heilbronn_power_lower_bound` only yields an unbounded sequence of sizes (`∃ n P, Tendsto n atTop atTop ∧ ∀ j, ... triangleAreasAtLeast (P j) ((n j)^(-2 + heilbronnExponent))`), not 'for every sufficiently large n' (docs: 'The linked construction is for an unbounded sequence of sizes; the paper's statement for every sufficiently large n is broader'). The disproof of the almost-n^-2 upper bound is stated (`almost_n_minus_two_refuted : ¬ eventualAlmostUpperBound (heilbronnExponent/2)`) and follows from the subsequence, so only the all-large-n uniformity is missing; the exponent is an astronomically small explicit constant `1/(100000 * K)`.
- **Suspicious/non-standard definitions:** none found

## 192 - A counterexample to the Gopalan--Servedio conjecture

- **Verdict:** `full`
- **Challenges:** SquareRootDegree
- **Cone (OAI lines):** SquareRootDegree 3,641
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `main : SignedViolations ∧ ¬ BddAbove AbsoluteRatios` with `SignedViolations := ∀ C > 0, ∃ n > 0, ∃ f : Cube (Fin n) → ℝ, IsBoolean f ∧ Nonconstant f ∧ C * √(fourierDegree f) < singletonSum f`; Fourier coefficients are the uniform-average `E[f * χ_s]` over the ±1 cube and `fourierDegree` is the max |s| with nonzero coefficient (real multilinear degree, as the file comment says). Standard definitions, matches the summary exactly.
- **Suspicious/non-standard definitions:** none found

## 194 - Lech's multiplicity conjecture

- **Verdict:** `supporting-only`
- **Challenges:** DuttaDomain
- **Cone (OAI lines):** DuttaDomain 53,953
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `dutta_domain : DuttaDomainClaim` is only a characteristic-p statement over a complete Noetherian local DOMAIN D (`IsShortComplex D F → ... Tendsto (duttaSequence D p F) atTop (𝓝 (duttaMultiplicity D p F)) ∧ multiplicity D ≤ duttaMultiplicity D p F`); docs: 'The paper's full flat-local result in arbitrary characteristic is outside it'. The headline `e(R) ≤ e(S)` for flat local homomorphisms is not stated. `multiplicity` (Hilbert-Samuel via `limUnder` of `d! * colength / N^d`) is standard.
- **Suspicious/non-standard definitions:** none found

## 196 - A counterexample to Kaplansky's zero-divisor conjecture

- **Verdict:** `full`
- **Challenges:** TorsionFreeZeroDivisors
- **Cone (OAI lines):** TorsionFreeZeroDivisors 44,340
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `MainTheorem : ∃ G, Group.IsFinitelyPresented G ∧ TorsionFree G ∧ HasFiniteTwoDimensionalClassifyingSpace G ∧ ∃ α β : MonoidAlgebra (ZMod 2) G, α ≠ 0 ∧ β ≠ 0 ∧ α * β = 0`. `TorsionFree` is the usual `g^n = 1 → g = 1`; the K(G,1) clause asks for a finite 2-dimensional Hausdorff path-connected Mathlib `CWComplex` X with `G ≃* FundamentalGroup X x` and a contractible covering space, which is the standard meaning.
- **Suspicious/non-standard definitions:** none found

## 197 - Nonsofic groups and group-ring counterexamples

- **Verdict:** `partial`
- **Challenges:** GroupRingDeterminant, KaplanskyDirectFiniteness, KaplanskyFinitelyPresented, OddKaplansky
- **Cone (OAI lines):** GroupRingDeterminant 16,337, KaplanskyDirectFiniteness 13,010, KaplanskyFinitelyPresented 13,310, OddKaplansky 18,517 (max 18,517)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Determinant counterexample is stated (`GroupRingDeterminant.main`: f.g. G, n >= 1, integral matrix `A` invertible over ℚ[G], bounded left-regular `T` invertible with `0 < fkDet T < 1`, `fkDet T = exp(Re tr(CFC.log(T*T))/2)`) and a Gottschalk counterexample is stated only for odd characteristic (`OddKaplansky`: K of order p^4, f.g. G with torsion, `ab = 1 ∧ ba ≠ 1`, `cellular b` injective and not surjective). The summary's headline for Kaplansky is a finitely presented TORSION-FREE NONSOFIC group over F_2: the char-2 statements (`KaplanskyDirectFiniteness`, `KaplanskyFinitelyPresented`) give a f.g./f.p. group that has an element of odd prime order, and nonsofic/torsion-free are not stated (docs: 'The further conclusion that the group is nonsofic is outside these statements').
- **Suspicious/non-standard definitions:**
  - `@[irreducible] def sourcePrime : ℕ := Nat.minFac ((Nat.factorial sourceM)^2 + 1)` with `sourceM := Nat.choose 1200 600` in `OddKaplansky`: the characteristic is a specific astronomically large, non-computable prime; existence of a counterexample is claimed only for this prime (not suspicious in logic, but the statement is for one prescribed p).

## 198 - A counterexample to the little finitistic-dimension conjecture

- **Verdict:** `full`
- **Challenges:** FinitisticAsymmetry, LittleFinitistic
- **Cone (OAI lines):** FinitisticAsymmetry 50,191, LittleFinitistic 45,195 (max 50,191)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `exists_counterexample : ∃ A (_ : Ring A) (_ : Algebra ℂ A), FiniteDimensional ℂ A ∧ littleFinitisticDimension A = ⊤ ∧ ∀ m > 0, ∃ N, Module.Finite A N ∧ (2m-2 : WithBot ℕ∞) ≤ projectiveDimension N ∧ projectiveDimension N < ⊤`, where `littleFinitisticDimension A := ⨆ (M) (_ : Module.Finite A M) (_ : projectiveDimension M < ⊤), projectiveDimension M` (Mathlib `projectiveDimension`): unbounded finite projective dimensions over a finite-dimensional complex algebra, as in the summary. `FinitisticAsymmetry` is an extra secondary result.
- **Suspicious/non-standard definitions:** none found

## 199 - Counterexamples to conjectures of Auslander--Reiten, Tachikawa, and Nakayama

- **Verdict:** `partial`
- **Challenges:** AuslanderReiten, Tachikawa
- **Cone (OAI lines):** AuslanderReiten 55,531, Tachikawa 28,942 (max 55,531)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: `ArExplicit.Statement.main` (`FullStatement`: over K = Frac(F₂[X₁,X₂,X₃]) a finite-dimensional algebra and a non-projective Gorenstein-projective module Z (`TotallyAcyclicWitness`) with `Ext^i(Z,Z)` and `Ext^i(Z,A)` subsingleton for i > 0, A/rad ≅ K^8, rad^4 ≠ 0, all conclusions persisting under every field extension E ⊗_K −) and `Tachikawa.main_theorem` (symmetric finite-dimensional algebra over k with a non-projective f.d. module with vanishing self-Ext). Not stated: the 'associated endomorphism algebra' consequences (classical/generalized/strong Nakayama, Auslander-Gorenstein, Wakamatsu tilting) named in the summary's second sentence (docs: 'The later field-extension, endomorphism-algebra, and related homological consequences are not included'; the docs also contradict themselves on field-extension persistence, which the Lean does state).
- **Suspicious/non-standard definitions:** none found

## 205 - Saxl's conjecture and universal tensor squares

- **Verdict:** `full`
- **Challenges:** Saxl, UniversalTensorSquares
- **Cone (OAI lines):** Saxl 7,558, UniversalTensorSquares 217,185 (max 217,185)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `Saxl.saxl_conjecture : ∀ m ≥ 1, ∀ μ with μ.card = (staircase m).card, 0 < kronecker (staircase m) (staircase m) μ` and `universal_tensor_square (n) (hn : 0 < n) (h2 : n ≠ 2) (h4 : n ≠ 4) (h9 : n ≠ 9) : ∃ λ, (∀ ν, 0 < kronecker λ λ ν) ∧ IsIrreducible (spechtRep λ) ∧ ∀ irreducible ρ, ∃ injective intertwiner ρ → S^λ ⊗ S^λ`. Both summary claims are stated.
- **Suspicious/non-standard definitions:**
  - Specht modules are hand-built: `spechtSub t := cyclic (wordRep n d) (polytabloid t)` as the orbit span of the column-antisymmetrized row-word inside `(Fin n → Fin d) → ℂ`, and `kronecker := finrank ℂ (IntertwiningMap (spechtRep t) ((spechtRep a).tprod (spechtRep b)))`. This is the standard polytabloid construction (and `IsIrreducible` of the chosen Specht module is part of the universal statement), but it is not Mathlib's notion, so Saxl's statement is only as faithful as this construction.

## 206 - Finite lattice representation: counterexamples and undecidability

- **Verdict:** `supporting-only`
- **Challenges:** FiniteCongruenceGraph
- **Cone (OAI lines):** FiniteCongruenceGraph 469
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `graph_criterion (Lat) [Fintype Lat] [Lattice Lat] [OrderBot Lat] : Representable Lat ↔ HasGraphWitness Lat` is only the paper's colored-graph characterization (docs: 'This selected theorem is the equivalence with the graph criterion; the paper's undecidability and subgroup-interval conclusions are outside it'). Nothing states that some finite lattice is NOT representable (the headline negative answer to the finite lattice representation problem) or that representability/subgroup-interval membership is undecidable.
- **Suspicious/non-standard definitions:** none found

## 207 - The $\ell^1$-Bass and complex Bass trace conjectures

- **Verdict:** `weaker-statement`
- **Challenges:** BassTorsionFree, BassTrace
- **Cone (OAI lines):** BassTorsionFree 24,157, BassTrace 23,596 (max 24,157)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Headline is the ℓ¹-Bass conjecture over `ℓ¹(G)`, but `bassTraceModules_vanishing_and_support` is only about the group algebra `MonoidAlgebra ℂ G` (Hattori-Stallings trace of every K0 class vanishes off finite-order classes and is supported on them); no ℓ¹(G) appears anywhere (docs: 'proves the complex Bass trace conjecture for every group'; docs title says ℓ¹ but scope does not). The algebraic companion IS stated: `torsion_free_corollary` gives trace = augmentation rank on K0(ℂ[G]) and `∀ R comm. domain with CharZero, e^2 = e → e = 0 ∨ e = 1` for torsion-free G.
- **Suspicious/non-standard definitions:**
  - Hand-rolled K0: `BassTrace.K0.Group R := FreeAbelianGroup (Idempotent R) ⧸ relations R` (relations: e ~ f when `a*b = e ∧ b*a = f`, plus direct sums) and `ModuleK0` of f.g. projective right modules, `HattoriStallings` into `ConjClasses G →₀ ℂ`; standard presentations, not Mathlib objects.

## 210 - Foulkes’ conjecture for sixth powers and quadratic stabilization

- **Verdict:** `partial`
- **Challenges:** FoulkesHowe
- **Cone (OAI lines):** FoulkesHowe 5,029
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Quadratic stabilization is stated: `canonical_foulkes_howe_surjective : ∀ V f.d., ∀ a b, 2 ≤ a → a * (a - 1) ≤ b → ∃ μ, IsFoulkesMap a b V μ ∧ Function.Surjective μ ∧ (unique)`. The headline sixth case of Foulkes' conjecture for all b >= 6 is only reached for b >= 30 = 6*5 (docs: 'The sixth-power specialization is covered for b ≥ 30; the companion's full range b ≥ 6 is not included'); the equivariant embedding is only implicit (dual of surjectivity).
- **Suspicious/non-standard definitions:**
  - `foulkesFormula a b V v := (a!)^(-b) • Σ_{σ : Fin b → Perm (Fin a)} sym_a(fun i => sym_b(fun j => v j (σ j i)))` and `IsFoulkesMap` define the 'canonical' map by hand on `SymPow n V` := span of degree-n products in `SymmetricAlgebra ℂ V`; the theorem also asserts uniqueness, which pins the definition.

## 211 - Geometry, diffusion, and spectra of random planar maps

- **Verdict:** `partial`
- **Challenges:** FKCRT
- **Cone (OAI lines):** FKCRT 40,208
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Only the q > 4 Brownian-CRT limit is stated: `MainStatement : ∀ q > 4, ∃ c > 0, ... Tendsto (fun n => finiteExpectation q (c / √(n+1)) n F) atTop (𝓝 (brownianExpectation P B F))` for every GHP-test F, with the standard excursion realized as the norm of three independent Mathlib `IsBrownianReal` bridges. Not stated: the 0 < q <= 4 convergence to Liouville quantum gravity spheres, the Liouville Brownian motion limits of random walks, and the FK-Ising spectral/heat-trace convergence (docs: 'For every fixed q>4 ...').
- **Suspicious/non-standard definitions:**
  - Entire topology is hand-rolled: `MetricMeasureData`, `ghpEDist := ⨅ amalgamating pseudometrics on X ⊕ Y` (Hausdorff/Lévy-Prokhorov), `IsGHPTest F := (∃ C, ∀ X, |F X| ≤ C) ∧ ∀ X valid, ∀ ε, ∃ δ, ∀ Y valid, ghpEDist X Y < δ → |F Y - F X| < ε` (convergence in distribution defined by bounded tests continuous at valid points); maps are pairs of dart permutations with `fkWeight q M A := q^(k(A) + (|A| - |V|)/2)`; `treeSpace` is a quotient of unitInterval by `excursionDist`. Plausible and documented in the file header, but none of it is Mathlib's notion.

## 212 - No bigeodesics and smooth limit shapes in planar first-passage percolation

- **Verdict:** `partial`
- **Challenges:** GammaPassage, PlanarFirstPassage
- **Cone (OAI lines):** GammaPassage 20,106, PlanarFirstPassage 18,741 (max 20,106)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** PRIMARY CLAIM NOT STATED (only a secondary result is formalized). Stated: exponential case `manuscriptMain` (norm `μ` with `IsTimeConstant`, `DifferentiableAwayFromOrigin`, `UniqueNormalizedSupports`, `C1UnitSphere`, unique supporting line, `HasC1CurveChart` on the frontier) and `GammaFPP.gamma_differentiability` for every shape/rate > 0. Not stated: the first headline claim (no doubly infinite geodesic for iid nonatomic weights with finite second moment of the min of four) and strict convexity of the exponential limit shape (docs: 'Strict convexity is outside these selected differentiability statements'; bigeodesics are not mentioned in the docs scope).
- **Suspicious/non-standard definitions:** none found

## 213 - No infinite critical clusters on quasi-transitive graphs

- **Verdict:** `full`
- **Challenges:** CriticalPercolation, CriticalZ3
- **Cone (OAI lines):** CriticalPercolation 68,224, CriticalZ3 10,358 (max 68,224)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `no_percolation_at_criticality [Infinite V] (hconnected : G.fullGraph.Connected) (hlocal : G.LocallyFinite) (hquasi : G.QuasiTransitive) (hpc : G.criticalProbability < 1) : G.law G.criticalProbability G.percolates = 0` on `BondGraph V E` (multigraphs, `law p = setBernoulli univ p`, `criticalProbability = sInf {p | 0 < P_p(∃ infinite cluster)}`), plus `CriticalZ3.critical_no_infinite`: `∀ᵐ ω ∂bondLaw bondCritical, ∀ x, (bondCluster ω x).Finite` and the same for site percolation, with `bondCritical = sInf {p | 0 < P_p(origin cluster infinite)}`. Both summary claims are stated.
- **Suspicious/non-standard definitions:** none found

## 214 - The Benjamini--Schramm nonuniqueness conjecture

- **Verdict:** `full`
- **Challenges:** BenjaminiSchramm, CayleyPercolation
- **Cone (OAI lines):** BenjaminiSchramm 151,059, CayleyPercolation 55,795 (max 151,059)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `full_main` (infinite, connected, locally finite, quasi-transitive multigraph with `0 < hV G`) concludes `MainConclusion G` including `pc G < ptwo G ∧ ptwo G ≤ pu G` and a coupled interval `[p₁,p₂]` above `pc` with infinitely many infinite clusters a.s.; `critical_laws` gives the finite triangle diagram `triangleDiagram G (pc G) x ≤ operatorNorm^3 ∧ < ⊤` plus mean-field laws; `cayley_main`/`arbitrary_cayley` handle every finite symmetric generating set of a non-Folner-amenable group for every p ∈ (pc, pu). Nonamenability is encoded as positive vertex-isoperimetric constant (graphs) or failure of the Folner condition (groups).
- **Suspicious/non-standard definitions:**
  - Custom 'amenable': `def FolnerAmenable (Λ) : Prop := ∀ K : Finset Λ, ∀ ε > 0, ∃ A : Finset Λ, A.Nonempty ∧ ∀ k ∈ K, ((A.image (· * k)) \ A).card < ε * A.card` (and the identical `AmenableGroup` in CayleyPercolation) is the standard right-Folner criterion, not Mathlib's; for general graphs nonamenability is `0 < hV G` with `hV G := sInf {|∂A| / |A| : A finite nonempty}` (outer vertex boundary). Standard but hand-written.

## 215 - Massive continuum limits and exact mass asymptotics for planar $O(n)$ models

- **Verdict:** `partial`
- **Challenges:** ClassicalON
- **Cone (OAI lines):** ClassicalON 12,907
- **External packages:** none beyond Mathlib/Lean core
- **Note:** PRIMARY CLAIM NOT STATED (only a secondary result is formalized). Only exponential decay of spin correlations is stated: `ExponentialDecay : ∀ n ≥ 3, ∀ β > 0, ∃ A m, 0 < m ∧ ∀ finite lattice graph G, b ∈ [0,β] → 0 ≤ correlation ≤ A * exp(-m * siteDistance x y)` (free boundary, finite volume, uniform in the graph; docs: 'The infinite-volume limit and the separate O(4) spectral-gap claim are not included'). The summary's headline results, the canonical O(3) continuum limit with positive mass gap and the exact O(4) asymptotic m_lat(β) ~ 32 e^{π/4-1/2} √β e^{-πβ}, are not stated.
- **Suspicious/non-standard definitions:** none found

## 218 - Conformal universality for weakly interacting and disordered Ising models

- **Verdict:** `supporting-only`
- **Challenges:** BufferedIsing
- **Cone (OAI lines):** BufferedIsing 3,114
- **External packages:** none beyond Mathlib/Lean core
- **Note:** The only statement is a technical finite-graph inequality: `finite_graph_comparison : exp(-4 * artanh (qZero ..)) ≤ mixtureProb .. mix / mixtureProb .. mix' ∧ ... ≤ exp(4 * artanh (qZero ..))` for Ising with arbitrary fields and boundary mixtures (docs: 'The paper's finite stopping-band approximation theorem is outside this selected statement'). None of the headline results (universality of critical bulk spin/energy limits under weak multispin perturbations, SLE_3 interface limits, weak iid bond disorder) is stated.
- **Suspicious/non-standard definitions:** none found

## 220 - Directional zero--one laws and ballisticity in random environments

- **Verdict:** `partial`
- **Challenges:** DirectionalBallisticity, DirectionalWalk, VelocityHemisphere
- **Cone (OAI lines):** DirectionalBallisticity 98,412, DirectionalWalk 18,194, VelocityHemisphere 116,839 (max 116,839)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: `directional_zero_one (d) (hd : 3 ≤ d) (hell : StrictEllipticity μ) (ℓ ≠ 0) : annealed μ 0 (escape ℓ) = 0 ∨ ... = 1` for IID environments (`environmentLaw μ = infinitePi (fun _ => μ)`), and `directional_transience_implies_ballisticity` (d >= 2, iid uniformly elliptic, `DirectionallyTransient ν ℓ → ∃ v, 0 < dot v ℓ ∧ HasVelocity ν v`), plus the velocity-hemisphere refinement. Not stated: the zero-one law for stationary ergodic finite-range-dependent environments under uniform ellipticity (the docs title says 'beyond iid environments' but the scope and Lean are iid only).
- **Suspicious/non-standard definitions:** none found

## 221 - The M\'ezard--Parisi formula for diluted spin glasses

- **Verdict:** `full`
- **Challenges:** DilutedSpin
- **Cone (OAI lines):** DilutedSpin 56,285
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `mezard_parisi (M : Model p) (hM : Admissible M) : Tendsto (pressure M) atTop (𝓝 (variationalValue M))` for Poisson-diluted even-arity (p >= 2 even) Ising models with the factorization `exp(θ s) = a (1 + b ∏ f_l(s_l))`, independence/identical-distribution of the f_l, b-moment positivity `0 ≤ E[(-b)^n]` and only first-moment integrability of θ and the field; `variationalValue M := ⨅ r, phi M r` with `phi M r := sInf {functional M r ζ m | ζ ∈ Hierarchy (r+1), 0 < m_1 < ... < m_r < 1}`. Matches the summary (Viana-Bray etc. are instances of the class, not separately stated). Caveat: everything is Bochner integrals, so a non-integrable integrand silently evaluates to 0.
- **Suspicious/non-standard definitions:**
  - Custom 'free energy': `pressure M N := (∫ k ∂Poisson(αN), ∫ θ, ∫ h, avg_indices log Σ_σ exp(logWeight) ...) / N` and the hierarchical functional `functional M r ζ m` over `Hierarchy : ℕ → TopCat` (H_0 = ℝ, H_{r+1} = ProbabilityMeasure (H_r)) with `logMean`/`trialLog`; all hand-written, and `phi` is an `sInf` over reals (junk value 0 if unbounded below) with Bochner integrals defaulting to 0 off the integrable class. Not trivializing (convergence to a nontrivial inf is asserted) but the junk-value behaviour is a fidelity risk.

## 222 - Perceptron free energies and microscopic jamming

- **Verdict:** `partial`
- **Challenges:** IsingFiniteness, PerceptronFreeEnergy, SphericalField
- **Cone (OAI lines):** IsingFiniteness 29,170, PerceptronFreeEnergy 71,237, SphericalField 25,018 (max 71,237)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: the spherical Gaussian perceptron formula `SphericalPerceptronFreeEnergy.main : ∀ α β > 0, ∀ φ : ℝ →ᵇ ℝ, ∃ p, variationalValue P α β φ = p ∧ expectedPressure → p ∧ pressure → p in probability`, plus a supporting `spherical_linear_field_formula`. For the Ising perceptron only well-definedness is stated: `variationalValue_real_of_continuous : ∃ p : ℝ, variationalValue α f = (p : EReal)` (docs: 'supporting well-definedness result. It does not assert convergence of the finite-system pressure or ... all bounded Borel log-potentials'). Not stated: Ising free-energy convergence, the bi-orthogonally invariant spherical extension, and the margin -1 jamming gap/force laws.
- **Suspicious/non-standard definitions:**
  - Hand-written variational 'free energies': Ising `variationalValue α f := ⨅ q : OverlapPath, (α * patternFunctional f q : ℝ) + isingEntropy q` with `patternFunctional f q := Filter.limUnder atTop (uniformPattern f q)` (junk value if the limit does not exist) and `isingEntropy q := ⨆ h : FieldStep, ...` in EReal; spherical `variationalValue P α β φ := ⨅ m : Trial, α * controlValue P (β • φ) m + entropy m` via Brownian stochastic control (`Progressive`, `usualBrownianSigma`). Finiteness of a `limUnder`-defined inf is a weak guarantee.

## 227 - The dynamical phase transition in the Sherrington--Kirkpatrick model

- **Verdict:** `partial`
- **Challenges:** CriticalSK, CriticalSKMixing, SKBarriers, SKHighTemperature, SKRatio
- **Cone (OAI lines):** CriticalSK 19,040, CriticalSKMixing 119,320, SKBarriers 56,621, SKHighTemperature 100,110, SKRatio 45,616 (max 119,320)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: stretched-exponential barrier for β > 1 (`SK.main : Tendsto continuousBadMass atTop (𝓝 1) ∧ Tendsto discreteBadMass atTop (𝓝 1)` at time exp(n^(1/10000)), expected bad Gibbs mass over disorder); high-temperature spectral gap `sk_main` (0<β<1: Poincaré constant C and gap ≥ 1/(Cn)) as a supporting result; ratio cutoff `ratio_cutoff` only for 0 ≤ β < 1/2. Critical case is one-sided: `critical_mixing_bounds` gives `n^(2/3-ε) ≤ continuousMixingTime ≤ exp(εn)` (discrete `n^(5/3-ε) ≤ ... ≤ exp(εn)`), so the headline 'mixing time n^{2/3+o(1)} at β=1' has no n^{2/3+ε} upper bound in Lean. Not stated: cutoff for 1/2 <= β < 1 and its log n location, and the critical autocorrelation-process limits (Gaussian/Rademacher, quench relaxing to stationary).
- **Suspicious/non-standard definitions:**
  - Custom 'mixing time': `continuousMixingTime W := sInf {t | 0 ≤ t ∧ ∀ x, continuousDistance W t x ≤ 1/4}` (matrix exponential kernel `NormedSpace.exp (t • generator W)`), `discreteMixingTime W := sInf {k : ℕ | ∀ x, discreteDistance W k x ≤ 1/4}`, `SKRatio.mixingTime g ε := sInf {k | discreteDistance g k ≤ ε}`: standard worst-start total-variation mixing (sets are nonempty so sInf is a true min), but hand-written; `SKBarriers` uses its own `heatBath` kernel and a Poissonized `continuousKernel` (series in k).

## 228 - Continuum phase transitions for radial pair potentials

- **Verdict:** `full`
- **Challenges:** ContinuumTransition, RadialDensityInterval, RadialTransition
- **Cone (OAI lines):** ContinuumTransition 14,988, RadialDensityInterval 14,330, RadialTransition 14,221 (max 14,988)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `ContinuumTemperature.main_theorem : ∃ φ f I βc, Admissible φ ∧ φ = o(r^{-3}) ∧ HasCanonicalFreeEnergy φ f ∧ I open interval ⊆ (0,∞) ∧ βc ∈ (1/2, 3/2) ∧ ∀ ρ ∈ I, dplus < dminus` (Admissible = stable, `φ → +∞` at 0 (divergent core), integrable tail) and `RadialTransition.densityInterval` (bounded continuous φ, `|φ r| ≤ C r^(-3-1/32)`, stable, a nonempty open density interval around 5p/3, common βc ∈ [7/8, 9/8], `StrictTemperatureCorner`); both potentials of the summary and the density-interval statement are covered.
- **Suspicious/non-standard definitions:**
  - Custom 'free energy': `HasCanonicalFreeEnergy φ f := ∀ β ρ > 0, Tendsto (L^{-3} log Z(β, L, ⌊ρL^3⌋)) atTop (𝓝 (-β f β ρ))` / `IsCanonicalFreeEnergy` with explicit `partition φ β L N := (N!)^{-1} ∫_{cube^N} exp(-β energy)` and `energy` in EReal (⊤ at coincident points) for the first potential; standard thermodynamic-limit definitions, free boundary conditions.

## 229 - Sharp three- and four-state reconstruction thresholds

- **Verdict:** `weaker-statement`
- **Challenges:** ThreeStateSupercritical, ThreeStateTreeClauses
- **Cone (OAI lines):** ThreeStateSupercritical 7,691, ThreeStateTreeClauses 7,792 (max 7,792)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Only the supercritical (Kesten-Stigum) direction for the three-state symmetric channel is stated: `regular_supercritical (hcrit : 1 < b * lam^2) : Reconstructs ..` and `poisson_supercritical (hd : 1 < d) (hcrit : 1 < d * lam^2) : Reconstructs ..` (advantage `∑' y, marginal y * (∑ i |posterior y i - 1/3|)/2` converges to L > 0), docs: 'Non-reconstruction at or below the threshold and the stochastic-block-model consequences in the paper are outside them'. The summary's headline is the EXACT threshold dλ²>1 with nonreconstruction at equality, plus the four-state ferromagnetic case and the SBM weak-recovery threshold: none of those is stated (the formalized direction is the classical one, the sharpness is missing).
- **Suspicious/non-standard definitions:** none found

## 230 - Exact Hausdorff measure for SLE

- **Verdict:** `partial`
- **Challenges:** SLELowerPositivity
- **Cone (OAI lines):** SLELowerPositivity 45,103
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Only positivity is stated: `SourceLowerMainTarget : ... ∀ h, IsGauge h → HasSmallRadiusFormula h (hFormula κ) → ∀ᵐ ω ∂P, ∀ s t, 0 < s → s < t → 0 < hausdorffGauge h (segment (γ ω) s t)` with `hFormula κ r = r^d (log log (1/r))^((2-d)/2)`, d = 1 + κ/8, for 0 < κ < 8 (docs: 'almost surely assigns positive measure'). The summary's finiteness half, 'positive finite measure' for every segment and finite expected measure of the trace in every bounded disk, has no Lean statement, so 'exact gauge' is only half-established.
- **Suspicious/non-standard definitions:**
  - SLE is not a Mathlib object: `IsOrdinaryChordalSLE κ γ P := (∀ t, Measurable ..) ∧ ∃ B, IsBrownianReal B P ∧ ∀ᵐ ω, IsCapacityTwoTrace (√κ * B · ω) (γ ω)`, with `IsCapacityTwoTrace` an existential Loewner-chain witness (conformal maps G_t, F_t, ODE `HasDerivWithinAt (G · z) (2 / (G t z - U t))`, hydrodynamic normalization, `F t (U t + iy) → γ t`); `hausdorffGauge h := Measure.mkMetric (ofReal ∘ h ∘ toReal)`. A plausible Loewner-characterization but a hand-written definition of SLE.

## 231 - The free uniform spanning forest is a factor of IID

- **Verdict:** `full`
- **Challenges:** FreeUniformSpanningForest, StronglyRayleighDPP
- **Cone (OAI lines):** FreeUniformSpanningForest 25,262, StronglyRayleighDPP 12,110 (max 25,262)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `fusf_is_factor_iid : ∃ Phi : FactorRule, RuleBorel Phi ∧ RuleEquivariant Phi ∧ ∀ G : GraphCode, WorksOnGraph Phi G` (one rule for all connected locally finite simple graphs on ℕ, equivariant under all relabelings, no root; `HasFUSFLaw` = cylinder probabilities are limits of uniform-spanning-tree cylinder ratios along every connected exhaustion) and `StronglyRayleighDPP` (`strongly_rayleigh_group_factor`, `invariant_positive_contraction_dpp_factor`, `translation_invariant_kernel_dpp_factor`, DPP existence/uniqueness for positive-contraction kernels on countable sets) cover both summary claims. Note: external `all` in tmp/import_cones.json is a parser artifact of `import all Mathlib...` in JointProcessLaw.lean; the cone is Mathlib-only.
- **Suspicious/non-standard definitions:** none found

## 234 - All-temperature pressure for orthogonally invariant Ising spin glasses

- **Verdict:** `full`
- **Challenges:** InvariantIsing
- **Cone (OAI lines):** InvariantIsing 210,755
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `limiting_pressure_of_extreme_limits_unconditional`: for Haar-distributed orthogonal `U N` (`(P.map (U N)).IsMulRightInvariant`), deterministic spectra `eig N` with `empiricalSpectralLaw → ν` (compact support, extreme eigenvalues → a, b), `∫ rotatedPressure .. ∂P → (variationalFunctional (measureR ν b)).toReal` and the same almost surely; `positive_temperature_pressure_unconditional` (all β > 0 via `scaledSpectralLaw`), `ground_state_limit_unconditional` (`Tendsto (thermalVariationalValue ν b) atTop (𝓝 M)` with M the ground-state limit), plus magnetic-field, random-spectrum and Gaussian-pattern variants. All summary claims are stated.
- **Suspicious/non-standard definitions:**
  - Custom 'free energy': `logPartition H := log ((card X)⁻¹ * Σ_x exp(H x))` (normalized by 2^{-N}, i.e. pressure minus log 2), `rotatedPressure`, the Parisi-type `variationalFunctional R := ⨅ p : OverlapPath, entropyFunctional p + spectralFunctional R p` (EReal) and `measureR μ e x` (R-transform via a `h.choose` inverse of the resolvent on (e, ∞)); hand-written variational formulas, with the final value taken via `.toReal` of an EReal (junk if infinite).

## 235 - Random-SAT thresholds, sharp variance and computability

- **Verdict:** `partial`
- **Challenges:** FixedClauseThreshold, SATComputability, SATSharpness, SATVariance
- **Cone (OAI lines):** FixedClauseThreshold 4,818, SATComputability 87,536, SATSharpness 5,273, SATVariance 6,740 (max 87,536)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: `FixedClauseThreshold.main (k) (hk : 3 ≤ k) : HasLimitingThreshold k` (∃ α > 0, P(SAT) → 1 for c < α and → 0 for c > α with m = ⌊c n⌋ i.i.d. uniform proper clauses), `SATComputability.main` (3-SAT threshold α with a `Nat.Partrec.Code` producing rationals q r, |q r - α| ≤ 2^-r) and `variance_main`. But the variance claim is only Θ(n) for k >= 4: for k = 3 the Lean gives `Var(H) ≤ C n ell` with `ell = log(e n)` (an n log n upper bound) and a linear lower bound, so the summary's 'hitting-time variance Θ_k(n) for every fixed k ≥ 3' is not stated for k = 3 (docs: 'They do not show that the logarithmic factor in the k=3 variance bound is necessary').
- **Suspicious/non-standard definitions:** none found

## 236 - The factor-of-IID threshold for free Ising states on trees

- **Verdict:** `full`
- **Challenges:** FreeIsing
- **Cone (OAI lines):** FreeIsing 117,435
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `free_ising_factor_iff_threshold : ∀ d β, 3 ≤ d → 0 ≤ β → (IsFactorOfIID d (tanh β) ↔ tanh β ≤ 1 / √(d-1))`, with `TreeVertex d` the reduced words in Fin d (the d-regular tree), `HasFreeIsingLaw θ` the free zero-field Ising cylinder weights `1/2 ∏_edges (1 ± θ)/2`, and `IsFactorOfIID` = ∃ measurable `Phi` pushing iid Uniform[0,1] labels to that law and a.s. equivariant for each fixed tree automorphism `g`. Exactly the summary's iff, including equality.
- **Suspicious/non-standard definitions:** none found

## 237 - The three-quarter diameter exponent for honeycomb walks

- **Verdict:** `supporting-only`
- **Challenges:** CriticalStripMass, HoneycombBridgeFiniteness, HoneycombFreeEnergy
- **Cone (OAI lines):** CriticalStripMass 62,844, HoneycombBridgeFiniteness 7,790, HoneycombFreeEnergy 985 (max 62,844)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Only technical inputs are stated: `HoneycombBridgeFiniteness.finite_bridge_sums` (summability of bridge weights and first length moments, also in the corridor |x| ≤ h (log h)^2), `CriticalStripMass.critical_strip_mass` (`c * archMass N + bridgeMass N = 1`, `Comparable bridgeMass N^(-1/4)`, `Comparable moment N^(3/4)`, bridge mass monotone) and `HoneycombFreeEnergy.logPartition_tendsto` (existence of the free-energy limit). The summary's headline, that a uniform n-step honeycomb SAW has diameter n^{3/4+o(1)} (and local mass/covering numbers of exponent 4/3, with high polynomial probability), has no Lean statement (docs: 'supporting summability statements ... outside them'; 'does not state ... the 3/4 spatial and moment laws').
- **Suspicious/non-standard definitions:**
  - `freeEnergy o e s := Filter.limUnder atTop (logPartition o e s)` in `HoneycombFreeEnergy` (the theorem `logPartition_tendsto` asserts the limit exists, which makes the junk-value risk moot); SAW partition functions are written with explicit `walkLists`/`saws` and critical activity `rho = 1/√(2+√2)`.

## 238 - Optimal logarithmic mixing of the Thorp shuffle

- **Verdict:** `full`
- **Challenges:** BinarySweep, CoordinateSweeps, CoordinateTrace, FourRowPermanent, OccupiedOverlap, PartialPermutation, SignedSweepMoment, SpinAngle, ThorpFirstReciprocal, ThorpRemaining, ThorpRouting, ThorpWeightedCompatibility, WeightedSweepMoments
- **Cone (OAI lines):** BinarySweep 26,532, CoordinateSweeps 22,897, CoordinateTrace 20,946, FourRowPermanent 622, OccupiedOverlap 24,287, PartialPermutation 5,967, SignedSweepMoment 25,778, SpinAngle 5,259, ThorpFirstReciprocal 8,680, ThorpRemaining 30,574, ThorpRouting 142,145, ThorpWeightedCompatibility 3,341, WeightedSweepMoments 17,383 (max 142,145)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `ThorpResults.remaining_main` (ThorpRemaining) is a conjunction whose last conjunct `OptimalOrderMain := IsTheta atTop (mixingTime d) (log (2^d))` states exactly the Θ(log N) mixing for N = 2^d cards, with `mixingTime d := sInf {t | distance d t ≤ 1/4}`, `distance d t := tv (law d t) (uniform d)` the total-variation distance of the full permutation law (and `InformationMain` records that `lawFrom` from any starting deck has the same distance, plus `distance d (2048 d) → 0`); the 12 other challenge files are supporting Fourier/representation estimates (`regular_trace_smoothing`, `binary_sweep_contraction_and_mixing`, `robust_permanent`, ...). All of them state estimates for the same hand-built Thorp shuffle.
- **Suspicious/non-standard definitions:**
  - Custom Thorp shuffle and 'mixing time': `step (d+1) c := (pairSwitch d c on the head bit, then rotate the coordinate order)` on `State d := Equiv.Perm (Fin d → Bool)` with `Coins (d+1) = (Fin d → Bool) → Bool` iid fair coins, `fairMass`, `tv`, `mixingTime d := sInf {t | distance d t ≤ 1/4}`; this is the standard pair-swap-and-interleave Thorp shuffle and TV-from-uniform with ε = 1/4, but it is a hand-written model and the Θ-statement hides explicit constants (1600d, 2048d, ...). `OccupiedOverlap` shows an `axiom_files` hit (HookModel.lean) that is a doc-comment false positive.

## 240 - Shelah's eventual categoricity conjecture

- **Verdict:** `partial`
- **Challenges:** CHObstruction
- **Cone (OAI lines):** CHObstruction 5,089
- **External packages:** none beyond Mathlib/Lean core
- **Note:** PRIMARY CLAIM NOT STATED (only a secondary result is formalized). `CHObstruction.main (hCH : CH) : ∃ L countable relational, ∃ K, K.IsAEC ∧ K.HasLSNumber ℵ₀ ∧ endpoint = hanf ℵ₀ ∧ K.TwoModels endpoint ∧ ∀ μ, tailThreshold ≤ μ → K.Categorical μ` is the summary's last sentence (under CH a prescribed Hanf threshold need not suffice), formalized with hand-written AEC axioms on `ZFSet` models. The headline, Shelah's eventual categoricity conjecture proved in ZFC, is not stated (docs: 'The later canonical-point obstruction and the separate eventual-categoricity theorem are not included').
- **Suspicious/non-standard definitions:**
  - Hand-rolled abstract elementary classes: `structure ClassData` (`objects`, `strong`), `IsAEC` (iso-closure, partial order, coherence, chain unions over arbitrary `γ.ToType`, LS bound), `LSBound/HasLSNumber`, `Categorical μ := (∃ M, objects M ∧ card = μ) ∧ ∀ M N of size μ, Nonempty (M.Iso N)`, `hanf κ := beth (succ (2^κ)).ord`; standard Shelah axioms but entirely custom, and `antisymm` is literal equality `M = N` of `RelModel`s.

## 241 - Rigidity of the Turing degrees

- **Verdict:** `full`
- **Challenges:** DegreeRigidity
- **Cone (OAI lines):** DegreeRigidity 84,081
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `MainTheorem : ∀ π : Degree ≃o Degree, ∀ a : Degree, π a = a` with `Oracle := ℕ → Bool` (all subsets of ℕ), `Reduces A B := TuringReducible (oracleFunction A) (oracleFunction B)` (Mathlib) and `Degree := Antisymmetrization Oracle Reduces`: every order automorphism of the Turing degrees is the identity. No assumptions; the representation corollaries are not stated.
- **Suspicious/non-standard definitions:** none found

## 242 - Single-fold Diophantine representations

- **Verdict:** `full`
- **Challenges:** SingleFold
- **Cone (OAI lines):** SingleFold 7,598
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `MainStatement : ∀ n ≥ 1, ∀ S : Set (Fin n → ℕ), REPred (· ∈ S) → ∃ m ≥ 1, ∃ P : MvPolynomial (Fin n ⊕ Fin m) ℤ, Represents P S` with `Represents P S := ∀ a, (a ∈ S ↔ ∃ w, P(a,w) = 0) ∧ ∀ w v, P(a,w) = 0 → P(a,v) = 0 → w = v` (witnesses in ℕ): exactly the single-fold representation of every r.e. set. The summary's corollary, undecidability under an at-most-one-solution promise, is not separately stated (docs say so).
- **Suspicious/non-standard definitions:** none found

## 243 - Choiceless counting does not capture polynomial time

- **Verdict:** `full`
- **Challenges:** ChoicelessPolynomialTime, WitnessedChoice
- **Cone (OAI lines):** ChoicelessPolynomialTime 18,461, WitnessedChoice 26,381 (max 26,381)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `CPTSeparation.main : (∀ S T, S.Iso T → (S.query ↔ T.query)) ∧ OrdinaryPolynomialTime ∧ ¬ FullCPT.EvaluationDefinable (fun I => I.query)`, where `query` = consistency of an F₃ linear system coded by 8 relations, `OrdinaryPolynomialTime` uses Mathlib `Turing.TM2ComputableInPolyTime` with finite stack alphabets on ordered encodings, and `EvaluationDefinable` is polynomially bounded choiceless counting over hereditarily finite sets of arbitrary rank; and `WitnessedChoice.main : ∃ φ, φ.formula.wscCount = 1 ∧ φ.BooleanOnAllInputs ∧ ∀ ψ, ψ.isCPT → φ.TrueModels ≠ ψ.TrueModels`. Both separations of the summary are stated.
- **Suspicious/non-standard definitions:**
  - Custom 'choiceless polynomial time with counting', twice and in two different hand-written formalisms: `FullCPT` (ASM-style `Program` with `Rule`/`Term` over `HF A` = `Lists A` quotient, `evaluationAccepts time space := ∃ h ≤ time(|A|), ... (P.occurring rel h).card ≤ space(|A|)`) in ChoicelessPolynomialTime, and the term/formula logic `WitnessedChoice.BGS` (`Term.iterate`, `resource p n := ⌊p(n)⌋₊`, `Formula.wsc`, `isCPT φ := wscCount = 0`) in WitnessedChoice; the nonexpressibility statements are only as good as these encodings of CPTC. 'Polynomial time' for the query itself is Mathlib's standard `TM2ComputableInPolyTime`.

## 244 - The partition principle does not imply choice

- **Verdict:** `partial`
- **Challenges:** PartitionConsistency, PartitionPrinciple
- **Cone (OAI lines):** PartitionConsistency 32,558, PartitionPrinciple 233,891 (max 233,891)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: `PartitionConsistency.main_consistency : Consistent ZF → Consistent (ZF ∪ {PP, ACwo, ¬AC})` (a hand-coded first-order `Derives` calculus, full ZF with arbitrary Separation/Replacement instances, `PP` = every internal surjection X ↠ Y yields an internal injection Y ↪ X, `ACwo` = choice for ordinal-indexed families), which is the summary's first two claims. The third claim, a transitive symmetric extension of any countable transitive model of ZFC with no new countable sequences, appears only as `exists_model_partitionPrinciple_without_choice` and needs an extra hypothesis (an internal strongly inaccessible `K` in the ground model, docs: 'containing an internal strongly inaccessible cardinal') and its conclusion lacks ordinal-indexed choice and the no-new-sequences property (docs: 'stronger transitive-model preservation assertions are outside').
- **Suspicious/non-standard definitions:**
  - Hand-written proof theory and set theory: `Formula`, `Derives` (natural deduction), `Consistent T := ∀ n, ¬ Derives (T.at n) .bot`, `ZF := {p | IsZFAxiom p}` with `separation`/`replacement` coded by variable-index arithmetic, `PP`, `AC`, `ACwo`. The theorem is an implication from `Consistent ZF`, so a coding error that made the encoded ZF inconsistent would make it vacuous; `PartitionPrinciple` uses its own `SetFormula`/`Realize` semantics on `ZFSet`. (`axiom_files` hit for LocalRecords.lean is a doc-comment false positive.)

## 245 - The $\beta$-Barendregt--Geuvers--Klop conjecture

- **Verdict:** `full`
- **Challenges:** TypeSystemNormalization
- **Cone (OAI lines):** TypeSystemNormalization 29,547
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `weak_implies_strong (P : Specification S) (h : SystemWeaklyNormalizing P) : SystemStronglyNormalizing P` for every sort type `S`, arbitrary `axioms`/`rule` relations (nonfunctional allowed), annotated `lam`/`pi` syntax with β-reduction inside annotations (`lam_domain`, `pi_domain`, `pi_body`), typing rules ax/var/weaken/product/abstraction/application/conversion, valid contexts as lists, legal = `∃ A, M : A ∨ A : M`, WN = some β-normal form, SN = `Acc`. Exactly the β-BGK conjecture including open contexts.
- **Suspicious/non-standard definitions:** none found

## 246 - Cannon's conjecture

- **Verdict:** `full`
- **Challenges:** CannonGeometricAction
- **Cone (OAI lines):** CannonGeometricAction 69,536
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `cannon (G) [Group G] [DiscreteTopology G] (D : CayleyData G) (hthin : D.ThinTriangles) (hsphere : Nonempty (Boundary D ≃ₜ SphereTwo)) : ∃ ρ : G →* H3Isom, ProperAction ρ ∧ CocompactAction ρ ∧ (ρ.ker : Set G).Finite`, with hyperbolicity as uniformly thin geodesic triangles in the Cayley graph, `Boundary D` the quotient of based geodesic rays by bounded synchronous distance (quotient of the pointwise topology), H³ the upper half-space with `arcosh(1 + |x-y|²/(2 x₃ y₃))` and its full isometry group. The summary's corollary (torsion-free ⇒ closed hyperbolic 3-manifold group) is not stated.
- **Suspicious/non-standard definitions:**
  - Custom hyperbolic-group boundary: `BasedRay D := {r : ℕ → G // r 0 = 1 ∧ ∀ i j, dist (r i) (r j) = Nat.dist i j}`, `Boundary D := Quotient (raySetoid D)` with `raySetoid r s := ∃ C, ∀ n, dist (r n) (s n) ≤ C`, topology inherited from `ℕ → G` (discrete G): the standard ray model of the Gromov boundary but hand-built rather than a Mathlib notion.

## 247 - An infinite finitely presented residually finite $2$-group

- **Verdict:** `weaker-statement`
- **Challenges:** PeriodicGroup
- **Cone (OAI lines):** PeriodicGroup 38,076
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `thm_main : MainStatement ∧ BurnsideStatement` only gives an infinite finitely presented PERIODIC group (`Periodic G := ∀ g, ∃ m > 0, g^m = 1`, namely `Steinberg 12 R` for some F₂-algebra R, and a general `∃ G` version). The summary's group is a residually finite 2-group (every element of 2-power order) with accompanying nil-algebra consequences; neither 'residually finite' nor '2-power order' nor the algebra statements is stated (docs: 'no common exponent is asserted ... separate nil-algebra and radical-algebra conclusions are outside these selected statements'). The negative answer to the finitely presented Burnside problem itself is covered.
- **Suspicious/non-standard definitions:**
  - `Steinberg n R := PresentedGroup {r | SteinbergRel n R r}` with relations x_{ij}(a+b) = x_{ij}(a) x_{ij}(b), [x_{ij}(a), x_{kl}(b)] = 1 for p.col ≠ q.row ∧ p.row ≠ q.col, and [x_{ij}(a), x_{jk}(b)] = x_{ik}(ab): the standard Steinberg presentation, hand-written (the carrier ring R is existentially chosen).

## 248 - Thompson's group $F$ is nonamenable

- **Verdict:** `full`
- **Challenges:** ThompsonNonamenability
- **Cone (OAI lines):** ThompsonNonamenability 9,457
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `thompson_F_nonamenable_composition : ∃ group : Group F, (∀ h g x, (h * g) x = h (g x)) ∧ ¬ Nonempty (InvariantMean F)` where `F := {f : IntervalHomeomorph // StrictMono f ∧ HasDyadicPLPieces f}` (dyadic breakpoints, slopes 2^k via `DyadicPLWitness`) with group law forced to be composition, and `InvariantMean G` = positive normalized left-invariant linear functional on `lp (fun _ : G => ℝ) ∞`. Exactly the nonamenability of Thompson's F.
- **Suspicious/non-standard definitions:**
  - Custom 'amenable': `InvariantMean G` (positive, `toLinearMap 1 = 1`, `toLinearMap (leftPull h f) = toLinearMap f` on ℓ^∞(G, ℝ)) is the standard invariant-mean definition but is not a Mathlib notion; F itself is hand-defined (Group structure is existentially provided inside the theorem).

## 249 - A finitely generated counterexample to Eilenberg--Ganea

- **Verdict:** `full`
- **Challenges:** EilenbergGanea
- **Cone (OAI lines):** EilenbergGanea 34,123
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `source_main : Group.FG SourceGroup ∧ Group.ResiduallyFinite SourceGroup ∧ cohomologicalDimension SourceGroup = 2 ∧ HasClassifyingSpace.{0} SourceGroup 3 ∧ ¬ HasClassifyingSpace.{u} SourceGroup 2`, with `SourceGroup` the kernel of the height map of an explicit Artin group, `cohomologicalDimension := projectiveDimension (trivial ℤ[G]-module)` and `HasClassifyingSpace Γ d` = aspherical T2 path-connected CW complex with cells only up to dimension d (arbitrary cardinality of cells, any universe). Matches the summary including 'no two-dimensional classifying space, even with infinitely many cells'.
- **Suspicious/non-standard definitions:** none found

## 250 - The Boone--Higman conjecture and higher finiteness

- **Verdict:** `full`
- **Challenges:** BooneHigman, SimpleOvergroups, UniversalFInfinity
- **Cone (OAI lines):** BooneHigman 37,197, SimpleOvergroups 90,766, UniversalFInfinity 19,991 (max 90,766)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `BooneHigman.main (G) [Group.FG G] : HasDecidableWordProblem G ↔ EmbedsInFinitelyPresentedSimpleGroup G` (`ComputablePred` of `evalWord g w = 1` for some finite generating tuple; Mathlib `Group.IsFinitelyPresented`, `IsSimpleGroup`), `SimpleOvergroups.main` (G f.g. with decidable word problem ⇒ ∃ nontrivial simple H of type F∞ and injective `G →* H`) and `UniversalFInfinity.universal_group_of_type_FInfinity` (∃ H of type F∞ into which every `Group.IsFinitelyPresented` group embeds). All three claims are stated; type F∞ = aspherical Hausdorff connected CW complex with `FiniteType` (finitely many cells per dimension).
- **Suspicious/non-standard definitions:** none found

## 251 - Amenability, unitarizability, and Ulam stability

- **Verdict:** `partial`
- **Challenges:** Dixmier, DixmierAllDiscrete
- **Cone (OAI lines):** Dixmier 3,559, DixmierAllDiscrete 4,092 (max 4,092)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: Dixmier's equivalence for all discrete groups (`CurrentMainTheorem : ∀ G discrete, (Amenable G ↔ Unitarizable G) ∧ ∀ ε > 0, ¬ Amenable G → ∃ nonunitarizable π with ‖π g‖ ≤ 1 + ε` on a complete Hilbert space, separable if G is countable) and the countable-group separable witness with bound 101 (`Dixmier.main_theorem_all_universes`). Not stated: the summary's second claim, equivalence of amenability with strong Ulam stability for countable discrete groups (it is not mentioned in the docs scope either, although the family title names Ulam stability).
- **Suspicious/non-standard definitions:**
  - Custom 'amenable': `def Amenable (G) [DiscreteTopology G] : Prop := ∃ m : (G →ᵇ ℂ) →ₗ[ℂ] ℂ, m 1 = 1 ∧ (∀ f, (∀ x, 0 ≤ (f x).re ∧ (f x).im = 0) → 0 ≤ (m f).re ∧ (m f).im = 0) ∧ ∀ g f, m (leftTranslate g f) = m f`, the standard positive left-invariant mean on ℓ^∞(G, ℂ); `SimilarToUnitary π := ∃ S : H ≃L[ℂ] H, ∀ g x, ‖S (π g (S.symm x))‖ = ‖x‖` and `Unitarizable` quantify over Hilbert spaces in one universe (the theorem is universe polymorphic).

## 252 - A non-residually-finite torsion-free hyperbolic group

- **Verdict:** `full`
- **Challenges:** TorsionFreeHyperbolic
- **Cone (OAI lines):** TorsionFreeHyperbolic 10,737
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `main : ∃ (G : Type) (_ : Group G), TorsionFree G ∧ WordHyperbolic G ∧ ¬ Group.ResiduallyFinite G` with `WordHyperbolic` = finite generating set whose Cayley graph has uniformly thin geodesic triangles (all three sides, `SideThin`). The summary's nonlinearity claim (one fixed element killed by every finite-dimensional representation over every commutative field) is not separately stated; it follows from the stated non-residual-finiteness via Mal'cev's theorem (docs: 'Nonlinearity over every field is not a separate conclusion').
- **Suspicious/non-standard definitions:**
  - Custom hyperbolicity: `WordHyperbolic G := ∃ S finite, (mulCayley S).Connected ∧ ∃ δ, ∀ geodesic triangles, SideThin ...` (standard thin-triangles definition on the Cayley graph, hand-written, not a Mathlib notion).

## 253 - An infinite finitely presented simple amenable group

- **Verdict:** `full`
- **Challenges:** SimpleAmenable
- **Cone (OAI lines):** SimpleAmenable 84,848
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `main : ∃ (G : Type) (_ : Group G), Infinite G ∧ Group.IsFinitelyPresented G ∧ IsSimpleGroup G ∧ FolnerAmenable G`, with `FolnerAmenable G := ∀ K : Finset G, ∀ ε > 0, ∃ D, D.Nonempty ∧ ∀ g ∈ K, |(g • D) ∆ D| < ε |D|` (the left Folner criterion). Exactly the summary's existence statement.
- **Suspicious/non-standard definitions:**
  - Custom 'amenable': `FolnerAmenable G := ∀ K : Finset G, ∀ ε : ℝ, 0 < ε → ∃ D : Finset G, D.Nonempty ∧ ∀ g ∈ K, (((D.image (g * ·)) ∆ D).card : ℝ) < ε * D.card`; this is Folner's criterion (equivalent to amenability for discrete groups) but not Mathlib's notion, and the group is existentially chosen.

## 254 - Classifying spaces and geometric obstructions for Artin groups

- **Verdict:** `full`
- **Challenges:** ArtinCAT0, ArtinParabolicIntersections, HarmonicArtin
- **Cone (OAI lines):** ArtinCAT0 9,419, ArtinParabolicIntersections 73,097, HarmonicArtin 62,901 (max 73,097)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** All three claims are stated: `HarmonicArtin.salvetti_cover_contractible [Finite S] (M : CoxeterMatrix S) : ContractibleSpace (SalvettiCover M)` (K(π,1): the cover is the realization of the nerve of the lifted spherical-cell poset), `ArtinCAT0.main` (the explicit 116-generator matrix has entries in {1,2,3,∞} and `¬ GeometricAction (ArtinGroup explicitMatrix) X` for every nonempty proper metric space X with a MulAction, `CAT0` via the CN inequality), and `ArtinParabolicIntersections` (`unconditional_arbitrary_intersections`: `sInf F` of any family of parabolics is parabolic and equals `sInf` of at most `Nat.card S` members; unique parabolic closure; acylindrical hyperbolicity and weak malnormality for irreducible infinite-label groups). Config notes: `ArtinParabolicIntersections.json` has `enable_nanoda: true` (an extra independent-kernel check, not a weakening); tmp/import_cones.json flags external `OAI` for 254 only because it mis-parses the module `MulBlockDiagonal'Entry` (apostrophe), so the true cone is Mathlib-only and ~32 lines larger.
- **Suspicious/non-standard definitions:**
  - `SalvettiCover M := SSet.toTop.obj (nerve (LiftedCell M))` with `LiftedCell M := Artin M × SphericalType M` and the face order generated by `LiftedFace` (minimal-length Coxeter coset representatives lifted to the Artin group): a hand-built model of the universal cover of the Salvetti complex (nerve of its face poset). Nothing in the challenge statement ties this space to a Mathlib notion of Salvetti complex or to the action of the Artin group, so 'asphericity of the Salvetti complex' is only as faithful as this model (the docs call it the equivalent statement that the universal cover is contractible).

## 255 - Quasi-isometric rigidity of virtually polycyclic groups

- **Verdict:** `full`
- **Challenges:** PolycyclicRecognition
- **Cone (OAI lines):** PolycyclicRecognition 232,617
- **External packages:** Gromov
- **Note:** `group_recognition (e : GroupCoarseEquivalence P J) (hP : IsVirtuallyPolycyclic P) [P, J f.g.] : IsVirtuallyPolycyclic J ∧ ∃ Γ finite-index, ∃ S Lie model, Λ, IsUniformLattice Λ ∧ Nonempty (Γ ≃* Λ)` and `lattice_recognition` (a finite-covolume lattice in a simply connected solvable Lie group, quasi-isometric to a f.g. J, makes J virtually a uniform lattice in possibly another such group). 'Quasi-isometric' is encoded as `GroupCoarseEquivalence` (bornologous maps with finite-set errors), which for f.g. groups is equivalent to a quasi-isometry; polycyclic = explicit cyclic subnormal series. Both summary claims are stated.
- **Suspicious/non-standard definitions:**
  - Hand-built coarse geometry: `GroupBornologous f := ∀ S finite, ∃ T finite, ∀ x y, x⁻¹ y ∈ S → (f x)⁻¹ (f y) ∈ T`, `GroupCoarseEquivalence` (maps in both directions plus finite error sets) used instead of word-metric quasi-isometry; `IsUniformLattice Λ := DiscreteTopology Λ ∧ ∃ K compact, ∀ g, ∃ γ k, k ∈ K ∧ γ k = g`; `SimplyConnectedSolvableLieModel` packages Mathlib `LieGroup`/`SimplyConnectedSpace`/`Group.IsSolvable`. Plausible and standard but non-Mathlib. External package `Gromov` is in the import cone.

## 256 - Howie's conjecture on equations over groups

- **Verdict:** `partial`
- **Challenges:** Kervaire
- **Cone (OAI lines):** Kervaire 11,273
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Only the Kervaire special case is stated: `coefficient_injective (A) (w : WordGroup A) (hw : Unimodular w) : Function.Injective (coefficientMap w)` with `WordGroup A := Monoid.Coprod A (Multiplicative ℤ)` and `Unimodular w := exponentSum w = 1 ∨ exponentSum w = -1` (one equation in one unknown with exponent sum ±1; docs: 'the selected unimodular-relator result underlying the conjecture'). The summary's headline, Howie's conjecture for arbitrary finite systems whose exponent-sum matrix has full row rank over ℚ (simultaneous solution in an overgroup), is not stated; the Kervaire companion claim is covered (coefficient injectivity implies nontriviality).
- **Suspicious/non-standard definitions:** none found

## 257 - A hyperbolic group with no geometric CAT(0) action

- **Verdict:** `full`
- **Challenges:** HyperbolicObstruction
- **Cone (OAI lines):** HyperbolicObstruction 56,644
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `MainStatement : ∃ K : FiniteComplex, ∃ x C, ConnectedSpace K.Carrier ∧ K.Aspherical x ∧ 0 ≤ C ∧ K.LinearDiskFilling C ∧ NoGeometricCATZeroAction (FundamentalGroup K.Carrier x) ∧ WordHyperbolic (FundamentalGroup K.Carrier x) ∧ ∀ L, K ≃ₕ L → ¬ CompatibleLocallyCATNegOne L`: a finite aspherical complex (hence a finite classifying space) with word-hyperbolic π₁ (four-point condition) admitting no geometric action on any nonempty proper complete CAT(0) space (`NoGeometricCATZeroAction`, CN-inequality CAT(0)). Matches the summary.
- **Suspicious/non-standard definitions:**
  - Hand-written geometry: `CATZero X := ∀ x y, ∃ γ, IsSegment γ x y ∧ ∀ z, ∀ t ∈ [0,1], dist z (γ t)^2 ≤ (1-t) dist z x^2 + t dist z y^2 - t(1-t) dist x y^2` (CN inequality), `WordHyperbolic` as the four-point condition with `WordDistance` from `sInf`-defined word length, `FiniteComplex` as barycentric realizations of `AbstractSimplicialComplex (Fin n)`; standard formulations but not Mathlib notions.

## 260 - Spacetime Penrose inequalities and rigidity

- **Verdict:** `supporting-only`
- **Challenges:** CKSBondiPenrose
- **Cone (OAI lines):** CKSBondiPenrose 58,903
- **External packages:** none beyond Mathlib/Lean core
- **Note:** The two challenge theorems are `CKSSourceExterior.area_controlled_end_replacement` (a 3-dimensional Cha-Khuri-Sakovich hyperboloidal end can be replaced by asymptotically flat ends keeping the compact interior, completeness and DEC, with `Tendsto (spatialADMEnergy G) ... (√(m² - |p|²) + η)` and `ε R → 0` area loss) and `schwarzschild_equality_examples (m) (hm : 0 < m)` (the Schwarzschild data satisfy `MainHypotheses`, `bondiMass d = m`, `minimumEnclosingArea g = 16π m²`). Neither states the Penrose inequality: the summary's headline (invariant ADM mass ≥ √(min enclosing area/16π) for asymptotically flat data in every dimension n >= 3 under DEC/weak future trapping, with equality rigidity and charged bounds) is absent; docs: 'The paper's general Bondi-Penrose inequality ... remains unformalized' and the conditional inequality 'is not selected'. The challenge deals with the dimension-3 Bondi/CKS class only.
- **Suspicious/non-standard definitions:**
  - Entire geometric-analysis stack is hand-built inside one 3.6k-line challenge file (`MetricJet`, `TensorJet`, `PhysicalDEC`, `CKSData`, `minimumEnclosingArea`, `bondiCharge`, `spatialADMEnergy`, ...) on top of Mathlib manifolds; none is a Mathlib notion and the file has dozens of auxiliary definitions.

## 261 - Localization and delocalization in the Anderson model

- **Verdict:** `weaker-statement`
- **Challenges:** PlanarAndersonSpectrum
- **Cone (OAI lines):** PlanarAndersonSpectrum 767
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `anderson_spectrum_ae (hh : 0 < h) : ∀ᵐ v ∂disorderLaw h, ∃ H, IsAndersonOperator v H ∧ IsSelfAdjoint H ∧ spectrum ℂ H = spectralInterval h` identifies only the spectrum `[-4-h, 4+h]` of the 2D nearest-neighbor Anderson operator (iid Uniform[-h,h] potentials); docs: 'It does not assert the pure-point spectral type claimed in the accompanying paper'. The summary's headline claims (almost-sure pure-point spectrum in d = 2 at every positive disorder, and purely absolutely continuous spectrum on an open interval for weak disorder in every d >= 3) are both unstated.
- **Suspicious/non-standard definitions:** none found

## 262 - Sharp one-dimensional Lieb--Thirring inequalities

- **Verdict:** `weaker-statement`
- **Challenges:** LiebThirring
- **Cone (OAI lines):** LiebThirring 13,717
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Only scalar potentials are treated: `MainClaim : ∀ γ ∈ (1/2, 3/2), (∀ W : ℝ → ℝ, Admissible γ W → negativeMoment γ W ≤ sharpConstant γ * potentialMass γ W) ∧ optimalConstant γ = sharpConstant γ ∧ oneStateConstant γ = sharpConstant γ ∧ equality at (r+1) sech²(r x)` with `negativeMoment` the sup over finite orthonormal families of H¹ weak negative eigenfunctions. The summary's finite-MATRIX-valued potentials with constant independent of matrix size, and the complete classification of equality cases (direct sums of sech² solitons with independent scales/centers and zero channels), are not stated: this is the scalar bound with attainment at one potential but without the equality-case classification.
- **Suspicious/non-standard definitions:**
  - Custom spectral definitions: `H1` as an L² function with an L² weak derivative, `schrodingerForm`, `IsNegativeEigenfunction W k u` (weak eigenfunction at energy -k²) and `negativeMoment γ W := ⨆ N (u k) orthonormal eigenfunctions, Σ (ofReal k_i)^(2γ)` in ℝ≥0∞ instead of Mathlib spectral theory; constants `semiclassicalConstant`, `sharpConstant` are written explicitly (Γ-function formulas).

## 263 - The ionization and generalized ionization conjectures

- **Verdict:** `partial`
- **Challenges:** CoulombIonization, CoulombRadii
- **Cone (OAI lines):** CoulombIonization 95,362, CoulombRadii 77,246 (max 95,362)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** PRIMARY CLAIM NOT STATED (only a secondary result is formalized). Stated: `CoulombIonization.generalized_ionization : ∃ a > 0, TFCharacterization a ∧ JointLimit a ∧ IteratedLimits a` (I_m(Z)/m^{7/3} → a_TF as m → ∞ and Z/m → ∞, and the Z → ∞ first iterated limsup/liminf; energies are infima of the full antisymmetric two-spin form with `FormAdmissible`) and `CoulombRadii.generalized_outer_radii` (`m^{1/3} R_m → (81π²/2)^{1/3}` for both limsup and liminf over any sequence of normalized ground states). Not stated: the summary's first claim, a molecule with M nuclei and total charge Z strictly binds at most Z + CM electrons, and the universal positive upper and lower bounds on first ionization energies/half-electron radii (docs: only 'large-ionization asymptotics').
- **Suspicious/non-standard definitions:**
  - Custom 'energy': `energy Z N := if N = 0 then 0 else sInf {e | ∃ ψ : FormVector N, FormAdmissible ψ ∧ formEnergy Z ψ = e}` (a real `sInf`, junk 0 if unbounded below, which atoms are not) and `IteratedLimits` uses real-valued `limsup`/`liminf` of `ionization m` (junk 0 if unbounded); `CoulombRadii` instead uses EReal-valued limsup/liminf and takes the ground states `Ψ N` as hypotheses (`IsNormalizedGroundState`), so it is vacuous if such minimizers did not exist (they do for neutral atoms). TF functional constant `tfKinetic = (3/10)(3π²)^(2/3)` written by hand.

## 266 - Exactly three mutually unbiased bases in dimension six

- **Verdict:** `weaker-statement`
- **Challenges:** HadamardCubeFiber, MUBSix
- **Cone (OAI lines):** HadamardCubeFiber 980, MUBSix 2,834,627 (max 2,834,627)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `MUB6.fourier_and_family_bound` states `(∀ H, IsHadamard H → ¬ Equivalent H tao → ∀ π, g H (permuteCharge π alpha) = 0) ∧ (∀ n, Attainable n → n ≤ 5)`: the Fourier-vanishing statement (the Matolcsi-Ruzsa-Weiner companion) and only the weak family bound `n ≤ 5` for mutually unbiased orthonormal bases of ℂ⁶ (`IsMUBFamily B := ∀ r ≠ s, ∀ i j, |⟨B r i, B s j⟩|² = 1/6`). Not stated: N(6) = 3, i.e. neither `Attainable 3` nor the exclusion of four bases (docs: 'does not establish the paper's upper bound of three or its computer-assisted exclusion of four'). `n ≤ 5` is the non-existence of 6 MUBs (with Weiner's gap theorem, not in Lean, this would give N(6) <= 4); the binary64 certificate for excluding four is outside the Lean statement. Cone is 2.83M lines of OAI, the largest in this range.
- **Suspicious/non-standard definitions:** none found

## 267 - Positive-temperature Bose--Einstein condensation and quantum depletion

- **Verdict:** `weaker-statement`
- **Challenges:** HardSphere
- **Cone (OAI lines):** HardSphere 71,853
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `condensation_with_mixed : ∃ ε₀ c₀ > 0, ∀ a ρ, ρ a^3 < ε₀ → ∀ thermodynamic sequences (N_k, L_k), (∀ pure ground vectors Ψ_k, c₀ ≤ liminf occupation Ψ_k) ∧ (∀ density operators supported on the ground space, c₀ ≤ liminf mixedOccupation)` is ZERO-temperature ground-state condensation of the hard-sphere gas with a non-sharp lower bound c₀ (docs: 'concerns ground states, without a positive-temperature assertion'). The summary's headline claims are not stated: BEC for the exact canonical Gibbs state at a strictly positive volume-independent temperature, and the sharp Bogoliubov leading quantum-depletion law (thermodynamic limit before dilute limit) for hard spheres and bounded finite-range potentials.
- **Suspicious/non-standard definitions:**
  - Hand-built hard-sphere gas: Dirichlet form domain `dirichletDomain N L a := closure (range SmoothTest.jet)` (smooth compactly supported functions vanishing on `d(x_i,x_j) ≤ a` on the torus `AddCircle L ^3`), `energy u := Σ ‖∇_p u‖²` (no 1/2), `bosonic`, `IsGroundVector`, `occupation ψ := L^{-3} ∫_Y |∫_x ψ(x,Y)|²` and a custom trace-class `Density.Operator`; the zero-mode occupation fraction matches the standard condensate fraction, but all objects are hand-written.

## 269 - The Laughlin gap and stability under scalar disorder

- **Verdict:** `partial`
- **Challenges:** Laughlin, LaughlinFock, LaughlinGap, LaughlinPlanar
- **Cone (OAI lines):** Laughlin 75,092, LaughlinFock 124,088, LaughlinGap 27,741, LaughlinPlanar 77,130 (max 124,088)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: the unperturbed spherical Laughlin gap at flux Q = 3(N-1): `Laughlin.MainTarget` (1/100) and `LaughlinGap.MainTarget` (`(1/25) * distanceToLaughlinSq ψ ≤ energy ψ` for every antisymmetric ψ and N >= N₀), the Fock-space inequality `thm_fock` (H² ≥ γ H for all γ < γ* ≈ 0.4617 and large flux, independent of particle number) and a planar version. Not stated: the summary's second claim, stability of the uniform gap and uniqueness of the ground state under weak bounded real scalar one-body potentials projected to the lowest Landau level (docs: 'Stability under projected one-body potentials and uniqueness of the perturbed ground state are outside it'); nor that `laughlinVector` is a zero-energy state (the inequality is stated against the line through it).
- **Suspicious/non-standard definitions:**
  - Hand-coded spherical V₁ Hamiltonian: `energy ψ := Σ_{i<j} Σ_{p<2Q-1} Σ_{a, a_i = a_j = 0} |pairAmplitude ψ i j p a|²` with explicit Clebsch-Gordan-type `pairCoefficient Q p x y` (descFactorial/factorial formula), `laughlinVector` from the coefficients of ∏(z_i w_j - z_j w_i)^3, and `distanceToLaughlinSq ψ := sInf (range (c ↦ ‖ψ - c • laughlin‖²))`. Its agreement with the physical V₁ projector is not machine-checked against any standard definition.

## 271 - Bloch's law and spontaneous ferromagnetic order

- **Verdict:** `partial`
- **Challenges:** Heisenberg
- **Cone (OAI lines):** Heisenberg 25,400
- **External packages:** none beyond Mathlib/Lean core
- **Note:** PRIMARY CLAIM NOT STATED (only a secondary result is formalized). Only `spontaneous_magnetization (d ℓ) (hd : 3 ≤ d) (hℓ : 1 ≤ ℓ) : DynamicsConverges d ℓ ∧ ∃ β₀ > 0, ∀ β ≥ β₀, ∃ ω, TranslationInvariant ω ∧ IsKMS β ω ∧ (ω.functional (spinZ d ℓ 0)).im = 0 ∧ ℓ/8 ≤ (ω.functional (spinZ d ℓ 0)).re` (nearest-neighbor Heisenberg ferromagnet, every spin S = ℓ/2) is stated, i.e. the summary's third claim. The headline, Bloch's T^{3/2} law with its exact coefficient for general finite-range couplings (and the first lattice correction for 3D nearest-neighbor couplings), has no Lean statement (docs: 'The formalization proves spontaneous magnetization ...').
- **Suspicious/non-standard definitions:**
  - Entire quantum-spin setup is hand-built: `Configuration d ℓ := Site d →₀ Level ℓ` (incomplete tensor product over the all-zero reference configuration), `QuasiLocal d ℓ := closure of the *-algebra of matrix units`, `hamiltonian` with edges counted via `WellOrderingRel`, `dynamics := Filter.limUnder atTop (finiteDynamics .. (box d n) ..)` (with convergence asserted separately by `DynamicsConverges`) and a hand-written `IsKMS` (analytic strip function with F(t) = ω(A α_t B), F(t+iβ) = ω(α_t B A)). Plausible, but none is Mathlib's notion of a KMS state or quantum spin system.

## 272 - Entanglement without secret key and the PPT-square conjecture

- **Verdict:** `partial`
- **Challenges:** DimensionTenChannel, DimensionTenPair
- **Cone (OAI lines):** DimensionTenChannel 44,673, DimensionTenPair 30,164 (max 44,673)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** PRIMARY CLAIM NOT STATED (only a secondary result is formalized). Stated: `DimensionTenChannel.exists_channel_fin21 : ∃ Θ : Map (Fin 21) (Fin 21), PPT Θ ∧ TracePreserving Θ ∧ ¬ EntanglementBreaking (Θ.comp Θ)` (the PPT-square counterexample with `PPT F := CP F ∧ CP (T ∘ F)` and `EntanglementBreaking` via separability of every amplification) and `DimensionTenPair.main_pair` (two explicit PPT maps on 10x10 matrices whose composition is not entanglement breaking and whose Choi matrix has no nonzero product vector in its range). Not stated: the summary's first claim, an entangled state on ℂ¹⁰⊗ℂ¹⁰ with zero distillable secret key under the specified local-instrument/authenticated-communication protocols (docs: 'outside these two selected Comparator statements').
- **Suspicious/non-standard definitions:** none found

## 273 - The entropy photon-number inequality

- **Verdict:** `full`
- **Challenges:** EntropyPhotonNumber
- **Cone (OAI lines):** EntropyPhotonNumber 27,838
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `entropy_photon_number_inequality (n) (hn : 1 ≤ n) (ρA ρB ρC : State n) (hA : FiniteEnergy ρA) (hB : FiniteEnergy ρB) (η ∈ [0,1]) (hC : IsBeamSplitterOutput η ρA ρB ρC) : η * gInv (S ρA / n) + (1 - η) * gInv (S ρB / n) ≤ gInv (S ρC / n)` on the untruncated Fock space ℓ²(ℕⁿ) with arbitrary (entangled) inputs and `gInv` the inverse of the thermal entropy `g t = (t+1) log(t+1) - t log t`. The summary's remark that product thermal inputs attain equality is not separately stated. Caveat: the output state is specified only by the hypothesis `IsBeamSplitterOutput` (explicit matrix-element formula), so the theorem is vacuous if that formula were wrong or unsatisfiable.
- **Suspicious/non-standard definitions:**
  - Hand-written quantum optics: `State n` = positive operator with `HasSum` diagonal 1 on `lp ℂ 2` over `ℕⁿ`, `entropy ρ := ∑' k, (entry (cfc (-t log t) ρ.op) k k).re` (real `tsum`, junk 0 if not summable; finite energy ensures it is), `gInv s := sInf {t ≥ 0 | s ≤ g t}`, and the beam-splitter output defined by explicit coefficients `oneModeBeamCoefficient η k e a b` (binomial/factorial formula) and `IsBeamSplitterOutput`: ∀ k l, HasSum (outputBlock ..) (entry ρC k l).

## 274 - Moore's parity conjecture for $\mathrm{QAC}^0$

- **Verdict:** `full`
- **Challenges:** QACParity, RegularParity
- **Cone (OAI lines):** QACParity 3,613, RegularParity 3,658 (max 3,658)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `QAC.parity_lower_bound : ParityStatement` = `∀ d, c ≥ 1, 0 < ε ≤ 1/2, ∃ n₀, ∀ n ≥ n₀, ∀ N, n ≤ N ≤ n^c, ∀ layers (≤ d layers of disjoint one-qubit unitaries / unbounded-arity Toffolis), ∀ out, ¬ (∀ x : Word n, 1/2 + ε ≤ successProbability (physicalCircuitMatrix layers) out x)` with ancillas initialized to zero (`inputWord`) and `successProbability` the Born probability of the measured output qubit equalling the parity, summing over all garbage. This is exactly Moore's parity conjecture in the measured-output model; `RegularParity` adds the explicit '< 2/3' polynomial-size specialization. Xu-Li's majority reduction is only cited in the summary.
- **Suspicious/non-standard definitions:** none found

## 275 - QMA-hardness of continuum Coulomb energy

- **Verdict:** `full`
- **Challenges:** ContinuumCoulombHardness
- **Cone (OAI lines):** ContinuumCoulombHardness 222,484
- **External packages:** RellichKondrachov
- **Note:** `unit_coulomb_qmaHard : QMAHard unitCoulombCodec.encode unitCoulombPromise` and `binary_coulomb_qmaHard`: every promise problem in QMA (verifier circuits over {H, T, CNOT} generated by a Mathlib `Turing.TM2ComputableInPolyTime`, completeness 2/3, soundness 1/3) has a deterministic polynomial-time many-one reduction (`PolynomialManyOne`, also Mathlib TM2 poly-time) to deciding `groundEnergy ≤ lower` versus `upper ≤ groundEnergy` with `1 ≤ upper - lower`, distinct rational nuclear positions, unary electron count and (for the unit version) unit charges; `groundEnergy` is the `sInf` over normalized antisymmetric H¹ states of the two-spin Coulomb form `kinetic - nuclearEnergy + pairEnergy`. External package `RellichKondrachov` is in the cone.
- **Suspicious/non-standard definitions:**
  - Custom complexity setup: hand-written `QMAGate`/`QMACircuit`/`QuantumVerifier`/`InQMA` (QMA over gate set {H, T, CNOT}, acceptance = Born probability of the last qubit being 1), `PromiseProblem`, `QMAHard`, and a `Codec` library for binary/unary encodings; polynomial time itself is Mathlib's `Turing.TM2ComputableInPolyTime` (not custom). `groundEnergy` is an EReal-valued `sInf` of Bochner-integral forms on H¹ vectors, which is fine because Hardy's inequality makes the Coulomb terms integrable.

## 276 - The classical capacity of generalized amplitude damping

- **Verdict:** `partial`
- **Challenges:** AmplitudeDamping
- **Cone (OAI lines):** AmplitudeDamping 6,206
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: `GAD.main`: for all γ, ν ∈ [0,1], `holevo γ ν n = n * holevo γ ν 1` (additivity across n uses of the same channel), `∃ p, Maximizes γ ν p ∧ holevo n = n / log 2 * objective γ ν p` (explicit one-variable optimization), `capacity γ ν = holevo γ ν 1` (operational capacity as sup of achievable rates with unrestricted collective decoding) and that every maximizing phase-pair product ensemble attains the block value. Not stated: the summary's additivity of Holevo capacity, minimum output entropy and regularized capacity when tensored with ANY finite-dimensional channel (docs: 'Additivity with an arbitrary different partner channel ... not included').
- **Suspicious/non-standard definitions:**
  - Hand-written information theory: `entropy P := (trace (cfc Real.negMulLog P)).re`, `holevo γ ν n := sSup (range ensembleValue)` over arbitrary finite ensembles, GAD Kraus operators `kraus γ ν r`, `Achievable`/`capacity := sSup {R | Achievable γ ν R}` with a `Tendsto` error and liminf-rate condition; standard definitions but not Mathlib's.

## 277 - Threshold repetition for entangled games

- **Verdict:** `full`
- **Challenges:** EntangledGames
- **Cone (OAI lines):** EntangledGames 7,234
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `threshold_parallel_repetition : ∃ κ₀ > 0, ∀ games G with entangledValue G < 1, ∀ 0 < δ < 1 - v, ∀ k ≥ 1, (∀ joint finite-dimensional k-fold strategies S, thresholdProbability G δ S ≤ exp(-κ₀ δ^13 k / (1 + log((a+1)(b+1))))) ∧ thresholdValue G δ ≤ the same bound`, with `Game` an arbitrary correlated question distribution plus predicate, `Strategy` a finite-dimensional bipartite state with POVMs and `entangledValue := sSup` of single-copy success, and `thresholdProbability` = probability of at least ⌈(v+δ)k⌉ wins. Exactly the summary's exponential threshold repetition (explicit δ^13 exponent).
- **Suspicious/non-standard definitions:** none found

## 279 - Exact quantum factoring over a fixed finite gate set

- **Verdict:** `full`
- **Challenges:** ExactQuantumFactoring
- **Cone (OAI lines):** ExactQuantumFactoring 54,007
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `exact_quantum_factoring : MainTheorem := ∃ family : ℕ → Circuit, Uniform family ∧ PolynomialResources family ∧ ∀ ℓ N, 2 ≤ N → N.size = ℓ → ℓ + (paddedLength ℓ)^2 ≤ (family ℓ).qubits ∧ (family ℓ).correctProbability ℓ N = 1` over a fixed 20-gate set (NOT/CNOT/Toffoli/Hadamard/phase with optional inverse and one control), where `correctProbability` is the exact Born probability of outputting the sorted prime factorization with multiplicities (`CorrectEncoding`) and `Uniform` uses a Mathlib `TM2ComputableInPolyTime` generator with finite alphabets. Matches the summary (exact, polynomial gates and qubits, fixed finite gate set).
- **Suspicious/non-standard definitions:**
  - Hand-built circuit model: `Gate := (primitive, inverse, controlled)`, `Primitive.matrix` entries on `List Bool`, `Instruction.matrix`, `Circuit.apply := foldl` over instructions; the polynomial-time notion is Mathlib's `TM2ComputableInPolyTime` applied to unary input `replicate ℓ true` with `Finite (Γ k)`, which is standard; the quantum gate semantics are written by hand.

## 280 - Strong locality for strongly rational unitary vertex operator algebras

- **Verdict:** `partial`
- **Challenges:** VertexAlgebraNet
- **Cone (OAI lines):** VertexAlgebraNet 28,634
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `MinimalVertex.main (hSimple : A.toVertexAlgebra.IsSimple) (hSR : A.IsStronglyRational) : A.PolynomialEnergyBounds ∧ CKLWStrongLocal U _ ∧ Nonempty (IrreducibleConformalNetStructure (intervalAlgebra U _))`: polynomial energy bounds, strong locality (`intervalAlgebra I ≤ (intervalAlgebra I.complement).commutant`) and an irreducible conformal net (isotony, locality, Möbius and Diff(S¹) covariance, unique vacuum, positive energy) for a simple unitary strongly rational VOA, i.e. the strong-locality core of the summary. Not stated: complete rationality of the net (the summary says it generates a COMPLETELY RATIONAL net), unitarizability of all simple modules, and the braided unitary tensor equivalence of Rep(V) with the net's finite-index sectors (docs: 'does not include complete rationality ... unitarizability ... the braided tensor equivalence').
- **Suspicious/non-standard definitions:**
  - Entire VOA/conformal-net stack is hand-built (`VertexAlgebra`, `CFTTypeVOA`, `IsStronglyRational := IsSelfContragredient ∧ IsRational ∧ C2Cofinite`, `smearedMap`, `closedSmoothField`, `localAlgebra`, `IrreducibleConformalNetStructure`), with many definitions using junk defaults: `smearedMap := if h : ∀ v, Summable (..) then tsumMap else 0`, `smoothSmearedField := if h : .. then .. else 0`, `resolvent`/`flow := if h : ∃ L, .. then h.choose else 0`, `projectiveStandardAction := if h : ∃ L, .. then h.choose else 1`. Not Mathlib notions; fidelity rests on these encodings.

## 281 - QAOA optimality for the SK model

- **Verdict:** `supporting-only`
- **Challenges:** SKFullSupport, SKValue
- **Cone (OAI lines):** SKFullSupport 20,357, SKValue 29,844 (max 29,844)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** No QAOA statement exists. The challenges are `SKValue.value_consequences` (conditional on `IsMinimizer W γ` and a diffusion `X`: the finite-size SK ground-state energy per spin `groundStateSequence n` converges to `groundStateValue = parisi W γ`, with martingale/curvature-integral formulas and convergence of finite Gaussian coefficient sums) and `SKFullSupport.full_support` (full support of zero-temperature Parisi minimizers). Docs: 'it does not itself assert convergence of QAOA circuit energies', and 'does not separately assert existence of a minimizer'. The summary's headline (QAOA with finite depth and size/disorder-independent angles reaches the SK ground-state energy per spin, size before depth, plus MaxCut on random regular graphs) is absent.
- **Suspicious/non-standard definitions:**
  - Custom Parisi/stochastic-control objects: `phi W γ t x := sSup {controlPayoff ..}` over `Admissible` progressive controls (real `sSup`), `gradient := deriv (phi W γ t)`, `curvature := deriv (gradient ..)`, `parisi`, `IsMinimizer`, `groundStateValue := limUnder atTop groundStateSequence` (convergence asserted in `ScalarValueConclusion`); derivatives are Mathlib `deriv` (junk 0 where not differentiable).

## 287 - All nonabelian free group factors are isomorphic

- **Verdict:** `full`
- **Challenges:** InterpolatedFactors
- **Cone (OAI lines):** InterpolatedFactors 26,804
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `allInterpolatedIsomorphic (r s : ℝ≥0∞) (hr : 1 < r) (hs : 1 < s) : Nonempty (NormalTracialEquiv (interpolatedTrace r) (interpolatedTrace s) (interpolatedTopology r) (interpolatedTopology s))`: every pair of interpolated free group factors L(F_r), L(F_s) with r,s ∈ (1,∞] (integer ranks via `groupVonNeumann (FreeGroup (Fin n))`, `FreeGroup ℕ` for ∞, and non-integer r as the corner of `L(F_2) ⊗ B(ℓ²)` by a projection of trace `1/√(r-1)`) is related by a *-isomorphism that preserves the canonical trace and is ultraweakly bicontinuous. The summary's statement L(F_2) ≅ L(F_3) and all interpolated factors; the fundamental-group conclusion is a consequence, not stated.
- **Suspicious/non-standard definitions:**
  - Hand-built II_1 factor models: `groupVonNeumann G := centralizer (centralizer (leftTranslations G))` (double commutant of left translations), `canonicalTrace`, `ultraweakOperatorTopology := ⨅ ξ η, induced (T ↦ Σ' k ⟨η k, T (ξ k)⟩)`, corners `Corner p hp` and `selectedProjection a := Classical.epsilon (stabilizedProjectionTrace p = ofReal a)` (junk default projection 0 if none existed, which does not happen in L(F_2)⊗B(ℓ²)); standard but not Mathlib's `VonNeumannAlgebra`-with-trace.

## 288 - Kadison's similarity conjecture

- **Verdict:** `full`
- **Challenges:** KadisonSimilarity, UniformCommutator
- **Cone (OAI lines):** KadisonSimilarity 127,680, UniformCommutator 67,256 (max 127,680)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `similarityTheorem : SimilarityTheorem.{u,v} := ∀ (A : Type u) [CStarAlgebra A] (K : Type v) [Hilbert space K] (π : BoundedUnitalHom A K), SimilarToStar A K π` with `BoundedUnitalHom A H := {π : A →ₐ[ℂ] (H →L[ℂ] H) // Continuous π}` and `SimilarToStar π := ∃ S : (H →L[ℂ] H)ˣ, ∀ a, S π(a⋆) S⁻¹ = (S π(a) S⁻¹)⋆`: Kadison's similarity conjecture for arbitrary Hilbert spaces, plus `universalHyperreflexivity` (one constant for all von Neumann algebras) and the uniform amplified commutator estimate.
- **Suspicious/non-standard definitions:** none found

## 289 - The strong Kadison--Kastler conjecture

- **Verdict:** `partial`
- **Challenges:** StrongKadisonKastler
- **Cone (OAI lines):** StrongKadisonKastler 326,060
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: `universal_strong_stability : ∀ ε > 0, ∃ δ > 0, ∀ H, ∀ von Neumann algebras M N on H (Mathlib `VonNeumannAlgebra`), kkDistance M N < δ → ∃ unitary v, v M v* = N ∧ ‖v - 1‖ < ε` with `kkDistance` the Hausdorff distance of the unit balls. Not stated: the summary's two counterexamples (near-identity conjugacy fails for one-sided near inclusions; arbitrarily close norm-separable C*-algebras need not be ambiently unitarily conjugate); the docs scope also only mentions the stability theorem although the docs title says 'spatial boundaries'.
- **Suspicious/non-standard definitions:** none found

## 290 - Connes' bicentralizer conjecture and relative bicentralizers

- **Verdict:** `supporting-only`
- **Challenges:** BoundedRecovery
- **Cone (OAI lines):** BoundedRecovery 8,104
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Only a technical lemma is stated: `bounded_recovery (S : StandardModularData H) (hscalar : S.ScalarCentralizer) (omega free ultrafilter) (T) (s) (delta) ... (hpositive : 0 < limsup (fixedMean omega (fun t => ‖T (D.unitary t (h n))‖²))) : RecoveryConclusion S T s delta` (a subsequence of uniformly bounded algebra elements v_j with `eta ≤ ‖T (v_j ξ)‖` and spectral support in bands of 4x the width). The summary's headline, Connes' bicentralizer conjecture for every type III₁ factor with separable predual and every faithful normal state (and the relative bicentralizer statement producing an amenable P with P' ∩ c(M) = N' ∩ c(M)), is not stated (docs: 'The absolute bicentralizer conjecture is not included').
- **Suspicious/non-standard definitions:**
  - Hand-built Tomita-Takesaki setting: `StandardModularData` (M, ξ, a hand-written `RealSpectralCalculus` D, J, `tomita_graph` equal to the closure of the graph of S₀ composed with half-exponential cutoffs), `fixedMean omega f := Filter.limUnder omega (symmetricAverage f)` (junk if the ultralimit does not exist, but ultrafilter limits on bounded sequences do exist).

## 291 - Toms--Winter and equivariant Jiang--Su stability

- **Verdict:** `supporting-only`
- **Challenges:** UniformGamma
- **Cone (OAI lines):** UniformGamma 17,302
- **External packages:** none beyond Mathlib/Lean core
- **Note:** The single challenge is `CurrentMain.main : MainClaim`, i.e. `Statement` (for a simple separable nuclear stably finite infinite-dimensional C*-algebra with tracial states and a free ultrafilter U, if the uniform tracial ultrapower of the uniform tracial completion has real rank zero then `UniformPropertyGammaAt A U`), preceded by existential witnesses for the hand-built `NormConstruction`/`NullConstruction`/`CauchyConstruction`/`LimitConstruction`/`TraceConstruction` classes. This is a supporting technical implication (docs: 'real rank zero ... implies uniform property Γ'). The summary's headline results, equivariant Jiang-Su stability for every countable discrete amenable group action and the unital Toms-Winter conjecture (strict comparison ⇔ finite nuclear dimension ⇔ Jiang-Su stability), are not stated.
- **Suspicious/non-standard definitions:**
  - The uniform tracial completion and ultrapowers are hand-built quotients: `UniformTracialCompletion := (familyCauchyNullIdeal τ).Quotient`, `FamilyUltrapower := (familyNullIdeal τ U).Quotient`, with `class NormConstruction : Prop`/`NullConstruction`/`CauchyConstruction`/`LimitConstruction`/`TraceConstruction` and `MainClaim := ∃ h0 : NormConstruction, ... ∃ h4 : TraceConstruction, Statement`, i.e. the C*-algebra structure is posited as existentially provable classes inside the claim; `IsNuclear` and `RealRankZero` are also local definitions.

## 292 - A counterexample to Kirchberg's norm-ultrapower embedding problem

- **Verdict:** `full`
- **Challenges:** NuclearUltrapower
- **Cone (OAI lines):** NuclearUltrapower 18,473
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `main_no_embedding : MainStatementWithCuntzCorollary` states: there is a separable unital C*-algebra `A` with `ι : G →* unitary A` satisfying the universal property of the FULL group C*-algebra of `G = (ℤ[1/2])³ ⋊ (SL₃(ℤ) × ℤ)` (`IsFullGroupAlgebra`), and for every nonzero unital nuclear `B` (nuclear = min and max C*-tensor norms agree on `B ⊗ C` for all C) and every free ultrafilter ω on ℕ there is no injective unital *-homomorphism `A →⋆ₐ[ℂ] NormUltrapower B ω`; the same for the universal Cuntz algebra O₂. Exactly the summary, including the O₂ corollary.
- **Suspicious/non-standard definitions:**
  - Hand-built objects: `NormUltrapower B ω := (ultraCon B ω).Quotient` (bounded sequences modulo ω-null), nuclearity via `minTensorNorm`/`maxTensorNorm` defined as `sSup` over representations on Hilbert spaces of one universe, `IsFullGroupAlgebra` (dense span + universal property), `IsCuntzTwoAlgebra` (two Cuntz isometries). Standard formulations, but none is a Mathlib notion, and the tensor-norm `sSup`s are real-valued.

## 293 - A counterexample to the hyperinvariant-subspace problem

- **Verdict:** `full`
- **Challenges:** BackwardIntertwiners, ContinuousCircleWeight, FiniteFactor, HyperinvariantSubspaces, IrrationalRotation, ProductBrown
- **Cone (OAI lines):** BackwardIntertwiners 5,802, ContinuousCircleWeight 18,350, FiniteFactor 22,601, HyperinvariantSubspaces 22,976, IrrationalRotation 81,127, ProductBrown 24,357 (max 81,127)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Both summary claims are stated: `Hyperinvariant.main_theorem (hInf : ¬FiniteDimensional ℂ H)` (also `BackwardIntertwiners.direct_algebra_corollary`) for every separable infinite-dimensional complex Hilbert space: `∃ T ≠ 0, ‖T^n‖^(1/n) → 0 ∧ TransitiveCommutant T ∧ commutant T ≠ ⊤ ∧ SOT-closed commutant` (no nonzero proper closed hyperinvariant subspace), and for the invariant-projection counterexamples `FiniteFactor.main_theorem` (a II₁ factor with separable predual and a nonzero quasinilpotent T ∈ M with `(1 - p) T p = 0 → p = 0 ∨ p = 1`), `IrrationalRotation.prescribed_irrational_counterexample` (every irrational θ: continuous weight f with `Rotation.IsContinuousCounterexample θ f`, T in the irrational-rotation algebra, nonzero, norm-quasinilpotent, trivial invariant projections) and `ProductBrown` (Brown measure δ₀). 'Hyperfinite' is only implicit (FiniteFactor asserts a II₁ factor with separable predual; the rotation algebra is the hyperfinite one by construction).
- **Suspicious/non-standard definitions:**
  - Hand-written operator-algebra notions: `TransitiveCommutant T := ∀ K closed submodule, (∀ A commuting with T, A K ⊆ K) → K = ⊥ ∨ K = ⊤`, `HasOnlyTrivialInvariantProjections`, `NormQuasinilpotent`, `vectorFugledeKadisonDeterminant`, `IsVectorBrownMeasure`, `strongOperatorTopology`, `HasSeparablePredual M := ∃ separable Banach E, Nonempty (StrongDual ℂ E ≃ₗᵢ⋆[ℂ] M)`; quasinilpotence is via `‖T^n‖^(1/n) → 0` and `ContinuousCircleWeight.MainStatement` does not itself state quasinilpotence (only trivial invariant projections for a weight with log-integral -∞).

## 294 - A counterexample to Kaplansky's quasitrace conjecture

- **Verdict:** `full`
- **Challenges:** KaplanskyQuasitrace, KaplanskyStableFiniteness
- **Cone (OAI lines):** KaplanskyQuasitrace 32,206, KaplanskyStableFiniteness 37,896 (max 37,896)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `kaplansky_quasitrace_counterexample : MainTarget := ∃ separable C*-algebra A, (∃ τ : OneQuasitrace A, τ.Normalized ∧ τ.IsTwo) ∧ ∃ positive contractions a b, ∀ normalized 2-quasitraces τ, 1/144 ≤ Re(τ(a+b) - τ a - τ b)` (all normalized 2-quasitraces are non-additive), and `stable_finiteness_bundle := SimpleStableTensorCounterexample ∧ ReducedQuasitraceLoss ∧ TraceFreeStablyFinite` (C*_r(F₂) and a simple stably finite M whose spatial tensor product `tensorAlgebra ρ` is `ProperlyInfinite`, plus the quasitrace-loss and trace-free examples). Both parts of the summary are stated.
- **Suspicious/non-standard definitions:**
  - Hand-written quasitraces: `OneQuasitrace` (positivity, τ(x*x) = τ(xx*), real/imaginary additivity on self-adjoints, linearity on closed abelian subalgebras) and `IsTwo τ := ∃ σ : OneQuasitrace (M₂(A)), ∀ a, σ (upperLeft a) = τ a` (a 2-quasitrace as one that extends to M₂(A), rather than requiring τ ⊗ Tr₂ to be a quasitrace); `C*_r(F₂)` is built as `closure (adjoin (left translations))` on ℓ²(F₂), `ProperlyInfinite A := ∃ s t, s*s = 1 ∧ t*t = 1 ∧ s*t = 0`.

## 295 - The Kadison--Ringrose cohomology conjecture

- **Verdict:** `full`
- **Challenges:** KadisonRingrose
- **Cone (OAI lines):** KadisonRingrose 62,822
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `main_result {M : Type u} [CStarAlgebra M] [PartialOrder M] [StarOrderedRing M] [WStarAlgebra M] (n) (f : Cochain M (n+2)) (hf : ∀ x, differentialValue f x = 0) : ∃ g : Cochain M (n+1), ∀ x, differentialValue g x = f x` with `Cochain M n := ContinuousMultilinearMap ℂ (fun _ : Fin n => M) M` (bounded multilinear) and the standard Hochschild differential `v₀ f(v₁..vₙ) + Σ_j (-1)^{j+1} f(.., v_j v_{j+1}, ..) + (-1)^{n+1} f(v₀..v_{n-1}) vₙ` with coefficients in M itself: vanishing of bounded Hochschild cohomology in every degree >= 2 for every von Neumann algebra (Mathlib `WStarAlgebra`), no separability or type assumption. Config note: `KadisonRingrose.json` has no `enable_nanoda` key (index.json shows null).
- **Suspicious/non-standard definitions:** none found

## 296 - The generator problem for finite factors

- **Verdict:** `full`
- **Challenges:** FactorGeneration, RelativeGeneration
- **Cone (OAI lines):** FactorGeneration 35,135, RelativeGeneration 36,021 (max 36,021)
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `single_generation_of_II1_separable_predual (S) (hS : IsII1Factor S) (hsep : HasSeparablePredual S) : SinglyGenerated S` (`∃ x ∈ S, wstar {x} = S`, `wstar` the smallest WOT-closed unital *-subalgebra containing x) and `RelativeGeneration.main_theorem : MainTarget`: for every irreducible inclusion `small ≤ large` of concrete II₁ factors with `HasSeparablePredual large`, there is a faithful normal normalized trace on `large` such that `relativeGeneratorLocus small large = {u | wstar (small ∪ {u}) = large}` is a dense Gδ in `unitary large` for the trace 2-norm topology (`traceTopology`). Both summary claims are stated; 'II₁ factor' is encoded as nonzero + WOT-closed + scalar center + finite (isometries unitary) + diffuse.
- **Suspicious/non-standard definitions:**
  - Hand-written von Neumann-algebra notions: `IsII1Factor` (not Mathlib's `VonNeumannAlgebra` with trace), `HasSeparablePredual := ∃ separable Banach X, Nonempty (StrongDual ℂ X ≃ₗᵢ⋆[ℂ] S)`, `wstar := sInf {S | WOTClosed S ∧ s ⊆ S}`, `ultraweakTopology` via summable vector functionals and `traceTopology` generated by `traceDistance` balls on the unitary group; standard formulations.

## 297 - A ZFC counterexample to Naimark's problem

- **Verdict:** `full`
- **Challenges:** Naimark
- **Cone (OAI lines):** Naimark 25,931
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `main : ∃ (A : Type u) (_ : CStarAlgebra A), IsSimpleCStar A ∧ ¬ FiniteDimensional ℂ A ∧ (∃ τ, IsFaithfulTracialState τ) ∧ HasUniqueIrreducibleRepresentation A ∧ ∀ (H : Type v) [Hilbert], ¬ IsIsomorphicToCompacts A H` (universe-polymorphic): a unital infinite-dimensional simple C*-algebra with a faithful tracial state all of whose irreducible representations (nonzero, no nontrivial closed invariant subspace) are unitarily equivalent, yet not isomorphic to the compact operators on any Hilbert space. Matches the summary (nonseparability is a consequence, not stated; the summary's 'alternative to Tanaka' framing is irrelevant to the statement).
- **Suspicious/non-standard definitions:**
  - Hand-written C*-algebra representation theory: `IsSimpleCStar`, `IsFaithfulTracialState`, `IsIrreducible π := π ≠ 0 ∧ no nontrivial closed π-invariant subspace`, `UnitarilyEquivalent`, `IsIsomorphicToCompacts A H := ∃ injective φ : A →⋆ₙₐ[ℂ] (H →L H), range = compact operators`; standard, quantified over Hilbert spaces in explicit universes.

## 298 - A counterexample to Voiculescu’s free-entropy equality conjecture

- **Verdict:** `full`
- **Challenges:** FiniteEntropySeparation
- **Cone (OAI lines):** FiniteEntropySeparation 15,557
- **External packages:** none beyond Mathlib/Lean core
- **Note:** `main : ∃ H M τ n X S, 2 ≤ n ∧ X_i, S_i ∈ M self-adjoint ∧ FreeStandardNoise τ X S ∧ ⊥ < chi τ X ∧ chi τ X ≤ chiStar τ X S - 1/2 ∧ chiStar τ X S - 1/2 < ⊤`: a bounded self-adjoint tuple in a von Neumann algebra with faithful normal trace (`TracialVector`), with S a freely independent semicircular family free from X, and `chi` (microstates with operator-norm cutoff R, limsup over matrix sizes, inf over moment orders m and tolerances ε, sup over R) strictly below the nonmicrostates `chiStar` (free Fisher information integral along X + √s S) by at least 1/2, both finite. Matches the summary (n >= 2 variables, finite and unequal).
- **Suspicious/non-standard definitions:**
  - Custom 'free entropy': `chiCutoff τ X R := ⨅ m ε, limsup_d ((d+1)^{-2} (volume (microstates τ X R m (d+1) ε)).log + (n/2) log(d+1))` in EReal, `chi := ⨆ R, chiCutoff`, `freeFisher := ⨅ conjugate systems ξ, ‖ξ‖²` (∞ if none), `chiStar := (n/2) log(2πe) + 1/2 ∫⁻ (n/(1+s) - Φ*(X + √s S))⁺ - 1/2 ∫⁻ (Φ* - n/(1+s))⁺` via `ConjugateSystem` (polynomial moments) and `FreeSubalgebras`; standard Voiculescu definitions written out by hand (EReal ⊤ - ⊤ conventions are not an issue because the claim bounds chiStar - 1/2 below ⊤).

## 299 - The Kirchberg--R\o rdam character criterion

- **Verdict:** `partial`
- **Challenges:** CharacterCriterion
- **Cone (OAI lines):** CharacterCriterion 25,294
- **External packages:** none beyond Mathlib/Lean core
- **Note:** Stated: `character_criterion (A) [CStarAlgebra A] [Nontrivial A] [SeparableSpace A] (ω) (hω : ω ≤ cofinite) : HasNoCharacters (NormUltrapower.CentralAlgebra A ω) ↔ Nonempty (A ≃⋆ₐ[ℂ] MinTensor.Algebra A JiangSu.Algebra)` (for unital separable A: the relative commutant A_ω ∩ A' has no nonzero *-character iff A ≅ A ⊗_min 𝒵; for unital A the annihilator quotient is trivial). Not stated: the summary's second claim, that the infinite minimal tensor power of every such algebra without characters is Jiang-Su stable (the Dadarlat-Toms question; docs only mention the criterion).
- **Suspicious/non-standard definitions:**
  - The Jiang-Su algebra is not Mathlib's: `JiangSu.Algebra := CStarInductiveLimit.Algebra StandardPrimeModel.presentation.system`, a hand-built inductive limit of prime dimension-drop algebras with explicit multiplicities (`copies p := (p-1)(p^4+p^2+1)`, `size n = 2^(7^n)`), so 'A ≅ A ⊗_min 𝒵' is only as faithful as this model of 𝒵; likewise `NormUltrapower.Algebra`, `MinTensor.Algebra` (spatial/min tensor norm via representation pairs) and the central subalgebra are hand-built (2.1k-line challenge file).

