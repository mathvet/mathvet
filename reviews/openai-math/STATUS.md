# Status — review of openai/math @ `adc7f124`

Generated 2026-10-08T10:46:24Z by `scripts/build_review.py`. Review status: **independent third-party review, pre-referee**.

| | families |
|---|---|
| in the release | 372 |
| with Lean (lean/docs page + Comparator challenges) | 235 |
| `full` — Lean states the headline claim | 144 |
| `partial` — one of several claims, or a special case | 60 |
| `weaker-statement` — a nontrivially weaker statement | 19 |
| `supporting-only` — a lemma or auxiliary statement | 12 |
| without Lean | 137 |

Comparator challenges: 405.

## Machine checks on the reviewer's machine (M1 laptop)
- Solutions built: 11 — `CannonGeometricAction`, `CirculantHadamard`, `EntangledGames`, `ErdosReciprocal`, `EuclideanFiveColor`, `GotsmanLinial`, `InterpolatedFactors`, `MahlerConjecture`, `MassAction`, `PiExponent`, `ThompsonNonamenability`
- Closure comparison + shadowing + axiom check clean: 11 — `CannonGeometricAction`, `CirculantHadamard`, `EntangledGames`, `ErdosReciprocal`, `EuclideanFiveColor`, `GotsmanLinial`, `InterpolatedFactors`, `MahlerConjecture`, `MassAction`, `PiExponent`, `ThompsonNonamenability`
- Real Comparator accepted: 66 — `AlgorithmicThinTrees`, `AsymptoticallyMinimalLittlewood`, `BassTorsionFree`, `BassTrace`, `BorsukNine`, `CannonGeometricAction`, `CirculantHadamard`, `CoboundaryExpanders`, `CommonBasesFPRAS`, `Conductivity`, `CoulombIonization`, `CoulombRadii`, `CriticalPercolation`, `CriticalZ3`, `DimensionTenChannel`, `DimensionTenPair`, `ElasticityUniqueness`, `EntangledGames`, `EntropyPhotonNumber`, `EuclideanFiveColor`, `EvenBarker`, `ExactFourier`, `ExactQuantumFactoring`, `GeneralizedStarHeight`, `GotsmanLinial`, `GroupRingDeterminant`, `HardSphere`, `HarmonicGrowth`, `IndependentSets`, `InterpolatedFactors`, `KServer`, `KaplanskyDirectFiniteness`, `KaplanskyFinitelyPresented`, `Laughlin`, `LiebThirring`, `ListHadwiger`, `LittlewoodFiniteFlatness`, `LogConcaveQuery`, `MahlerConjecture`, `MassAction`, `MatchingAffineLift`, `MatchingPSD`, `NoiselessRegression`, `OddKaplansky`, `PeriodicGroup`, `PiExponent`, `PlaneColoring`, `QACParity`, `RandomizedMeanPayoff`, `SKFullSupport`, `SKValue`, `SidorenkoCounterexample`, `StrongThinTree`, `Superstring`, `SwitchChain`, `SymmetricPolar`, `ThompsonNonamenability`, `ThorpRemaining`, `ThreeMachine`, `TorsionFreeZeroDivisors`, `TraceReconstruction`, `TypeSystemNormalization`, `UniformKServer`, `UniformSparsestCut`, `VlasovMaxwell`, `WeisfeilerLeman`
- Of these, accepted **with the real landrun (Landlock) sandbox on an isolated Linux VM** (`evidence/cloud/`): 66 — `AlgorithmicThinTrees`, `AsymptoticallyMinimalLittlewood`, `BassTorsionFree`, `BassTrace`, `BorsukNine`, `CannonGeometricAction`, `CirculantHadamard`, `CoboundaryExpanders`, `CommonBasesFPRAS`, `Conductivity`, `CoulombIonization`, `CoulombRadii`, `CriticalPercolation`, `CriticalZ3`, `DimensionTenChannel`, `DimensionTenPair`, `ElasticityUniqueness`, `EntangledGames`, `EntropyPhotonNumber`, `EuclideanFiveColor`, `EvenBarker`, `ExactFourier`, `ExactQuantumFactoring`, `GeneralizedStarHeight`, `GotsmanLinial`, `GroupRingDeterminant`, `HardSphere`, `HarmonicGrowth`, `IndependentSets`, `InterpolatedFactors`, `KServer`, `KaplanskyDirectFiniteness`, `KaplanskyFinitelyPresented`, `Laughlin`, `LiebThirring`, `ListHadwiger`, `LittlewoodFiniteFlatness`, `LogConcaveQuery`, `MahlerConjecture`, `MassAction`, `MatchingAffineLift`, `MatchingPSD`, `NoiselessRegression`, `OddKaplansky`, `PeriodicGroup`, `PiExponent`, `PlaneColoring`, `QACParity`, `RandomizedMeanPayoff`, `SKFullSupport`, `SKValue`, `SidorenkoCounterexample`, `StrongThinTree`, `Superstring`, `SwitchChain`, `SymmetricPolar`, `ThompsonNonamenability`, `ThorpRemaining`, `ThreeMachine`, `TorsionFreeZeroDivisors`, `TraceReconstruction`, `TypeSystemNormalization`, `UniformKServer`, `UniformSparsestCut`, `VlasovMaxwell`, `WeisfeilerLeman`
- Comparator running: `ErdosReciprocal`; build in progress: `ContingencyTables`, `QuasiRiemannHypothesis`

Logs: `evidence/lean_checks/<Challenge>.log` (build), `.cmp.txt` (closure comparison), `.comparator.txt` (Comparator, laptop, development landrun shim); `evidence/cloud/<Challenge>.*` the same three from the sandboxed cloud runs (each `.comparator.txt` starts with a provenance header naming the machine, the sandbox and the session URL).
