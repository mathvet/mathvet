# Which of OpenAI's 372 mathematical results are machine-checked *as stated*?

*A pre-referee fidelity review of [`openai/math`](https://github.com/openai/math) at commit [`fd4aeeb2`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb) (the release of 6 October 2026 as updated upstream on 8 October). First published 8 October 2026 at commit `adc7f124`, moved to `fd4aeeb2` on 10 October after re-reading the twelve families that commit changed; the changelog names every verdict that moved. By MathVet. Every verdict here is pre-referee: the referee round is [pre-registered](https://math.vet/protocol.html) and its result will be published whatever it shows.*

On 6 October 2026 OpenAI released `openai/math`: 722 manuscripts in 372 result families, produced by an internal model, together with a Lean library of 121,734 files and 25.9 million lines; an update on 8 October (commit `fd4aeeb2`) brought the count to 749 manuscripts, 122,458 files and 26.1 million lines. 242 of the families come with Lean formalizations and 416 [Comparator](https://github.com/leanprover/comparator) challenge files; 130 families have no Lean at all.

Lean settles one question completely: *does the proof prove the statement?* For every challenge the repository ships a Comparator configuration under which the Lean kernel checks the solution against the challenge statement using only the three standard axioms. That is the strongest guarantee mathematics has had at this scale, and nothing in this review weakens it.

Lean does not settle a second question: *does the statement say what the manuscript's headline says?* A family's headline (the one-paragraph summary in the repository's `overview.pdf` and `CONTENTS.md`) may claim a theorem for torsion-free groups while the challenge file proves it for a group with torsion; it may claim "at most three" while the file proves "at most five"; it may claim a positive-temperature result while the file proves the zero-temperature case. In each of these three cases the repository's own scope note says so. The headline is what gets quoted; the challenge file is what was checked. This review measures the distance between the two for all 242 families and records it in the vocabulary of the community's [formalization.yaml](https://github.com/mathlib-initiative/formalization.yaml) standard.

## The counts

| | families |
|---|---|
| Lean states the headline claim in full (`full`) | 149 |
| Lean states one of several headline claims, or a special case (`partial`) | 59 |
| Lean states a nontrivially weaker statement (`weaker-statement`) | 18 |
| Lean states a supporting lemma only (`supporting-only`) | 16 |
| No Lean | 130 |

Of 372 families, 149 (40%) have a headline that is machine-checked as stated; 93 (25%) are machine-checked in a narrower form; 130 (35%) rest on the manuscript alone, and the repository's README says of those that "some of the unformalized results could have issues". Nothing in this review says that any theorem is false. It says what was checked.

## How the verdicts were produced

For each of the 242 families we read the overview summary (the headline), the repository's scope note `lean/docs/NNN.md`, every linked `ComparatorChallenges/*.lean` statement, and the definitions those statements depend on. The verdict is about the summary's primary claim. It is `full` if the Lean statement implies that claim after unpacking definitions or one routine step (the step is named in the note); `weaker-statement` if it does not imply it; `partial` if a second co-equal headline claim has no challenge statement, or only a special case is stated; `supporting-only` if the Lean states a lemma or auxiliary result rather than the headline. When the scope note and the Lean disagree, the Lean wins and the disagreement is recorded. Non-standard or hand-built definitions that a reader should check are listed separately for each family.

The reading was done by Claude agents running in Claude Code on 6 and 7 October 2026, one pass per family, with the output validated mechanically against the catalogue (titles, challenge sets, import cones). The maintainer re-read six families by hand and rebuilt eleven challenges locally. There is no second human reader yet. That is why every verdict is labelled pre-referee, and why the [fidelity table](https://math.vet/openai-math/) shows the repository's own scope note next to each verdict: a reader can judge the basis without trusting us.

## What was checked by machine

Beyond reading, we built eleven challenge solutions on an ordinary laptop and ran a [closure comparison](https://github.com/mathvet/mathvet/tree/main/checker): the challenge file is re-elaborated under a fresh namespace inside the solution's environment, and every constant in the transitive closure of the challenge theorems must be matched by a same-named solution constant of the same kind with an alpha-equivalent type (and value, for definitions). A shadowing check requires the challenge text elaborated against Mathlib alone to print identically to its copy elaborated inside the solution. `#print axioms` must return only `propext`, `Classical.choice` and `Quot.sound`. All eleven are clean. The real Comparator, built from source, accepted three of them so far ("Lean default kernel accepts the solution"); it was run with the project's development landrun shim, so without a sandbox. Sandboxing protects the checking machine from an adversarial solution file and does not change what the kernel accepts, but a citable run needs real landrun on Linux and is pending. Further builds and Comparator runs are in progress; the [challenge status page](https://math.vet/openai-math/challenges.html) is regenerated as they finish, and every log is in the repository.

Library-level facts, all reproducible from the clone: the Lean library contains no `sorry` and no custom `axiom` declaration; all 416 challenge configurations permit exactly the three standard axioms; one challenge file (`HarmonicGrowth.lean`) closes its statement with a local `axiom` placeholder instead of `sorry`, which is harmless because the solution module is what gets checked; 23 challenges have external packages in their import cone (PrimeNumberTheoremAnd, StrongPNT, RellichKondrachov, FixedPointTheorems, AbsorptionCutoff and five others), pinned to commits and patched by the lakefile; the repository's own `lean/formalization.yaml` lists its main results as 173 `sources` entries, declares `review.status: unchecked`, and contains no `alignment` table and no `fidelity` block.

## The repository already says much of this

The scope notes in `lean/docs` are candid. Put beside the headlines, they already describe where a challenge statement is narrower than a family's summary. Some of them, verbatim:

> "One statement records the counterexample for a finitely generated group; the more detailed construction gives a finitely presented group with an element of odd prime order. … The further conclusion that the group is nonsofic is outside these statements." — [`lean/docs/197.md`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/197.md), *A torsion-free group algebra that is not directly finite*

> "The paper claims that at most three mutually unbiased orthonormal bases exist in $\mathbb C^6$. The linked formalization proves a weaker family bound: every family in its mutually unbiased bases model has at most five members. … The selected statement does not establish the paper's upper bound of three or its computer-assisted exclusion of four arbitrary bases." — [`lean/docs/266.md`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/266.md), *Exactly three mutually unbiased bases in dimension six*

> "This selected statement identifies the spectral set. It does not assert the pure-point spectral type claimed in the accompanying paper." — [`lean/docs/261.md`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/261.md), *Localization and delocalization in the Anderson model*

> "The selected statement covers these value and approximation results; it does not itself assert convergence of QAOA circuit energies." — [`lean/docs/281.md`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/281.md), *QAOA attains the SK optimum in the thermodynamic-first limit*

> "It is uniform in the gas parameter within this range and concerns ground states, without a positive-temperature assertion." — [`lean/docs/267.md`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/267.md), *Positive-temperature Bose–Einstein condensation and exact quantum depletion*

> "The selected theorem is the reciprocal-sum consequence. The paper's quantitative upper bound for the largest progression-free subset of $\{1,\ldots,N\}$ is outside this statement." — [`lean/docs/159.md`](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/lean/docs/159.md), *Erdős's reciprocal-sum conjecture and quasipolynomial Szemerédi bounds*

What did not exist was one table that puts the two side by side for every family, in a fixed vocabulary, with the evidence linked. That is what the fidelity table is. For the families where our reading and the scope note agree, it adds nothing but convenience; where they disagree, the note says so and the Lean file decides.

## What this review is not

- It is not a claim that any result in the repository is false. We found no false theorem and did not look for one; Lean has already done that work for the formalized statements.
- It is not a review of the mathematics of the 130 unformalized families. Whether those manuscripts are correct is a question for referees, and we hold no opinion on it here.
- It is not a certification that every custom definition matches its textbook counterpart. Where a challenge hand-builds an object (an amenability notion, a complexity model, an entropy), the table lists it under "definitions to check".
- It is not refereed. One model-assisted pass is a map, not a verdict; the error rate of that map is the next thing we publish.

## The error rate

Before any family is re-read, a sample of 40 families was frozen at the first reviewed commit (`adc7f124`, where the counts were 144 `full` and 91 non-`full`): the 12 families whose scope notes already document a divergence, 14 drawn by a seeded random draw from the other 79 non-`full` families, and 14 drawn from the 144 `full` families. The sample and the referee packet stay at that commit. The sample file and its SHA-256 are committed in the repository, and the draw is reproducible from the published seed. Two named mathematicians who read Lean will classify all 40 independently under the same rubric; a third adjudicates disagreements. We publish the stratum-weighted error rate with its 80% Wilson interval whatever it shows, with a target date of 29 October 2026. The decision lines were fixed in advance: at or below 0.10 the table carries the label "referee-verified sample"; at or above 0.20 it is relabelled "first-pass map, unverified"; in between, 20 more families are drawn and the pooled estimate decides. The derivation, the power of the design and the referee instructions are in the [protocol](https://math.vet/protocol.html).

## In the standard's own fields

The Mathlib Initiative's `formalization.yaml` standard (v0.4) already has the slots this review fills: an `alignment` table from source statements to Lean declarations, a `fidelity.divergences` note, and a required `review.status`. Of 58 such files we found in the wild, from OpenAI, Anthropic, Axiom Math, Numina and community projects, none carries a review by a named independent third party, and the file shipped with `openai/math` is `unchecked`. Our review is published as [`formalization-review.yaml`](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/formalization-review.yaml) in exactly that shape, so that registries and tools which already read the standard can read the review, and so that the lab, if it wishes, can diff it against its own notes.

## Using and correcting it

The [table](https://math.vet/openai-math/) is filterable by verdict and subject; each row expands to the headline, our note, the repository's scope note, the challenge files and the machine-check status. The same data is in the repository as CSV, JSON and YAML, together with the audit source files, every build and Comparator log, the checker, and a 405-row paired dataset of challenge statements with their papers' main theorems. The upstream repository is watched; when its HEAD moves, the changed families are rebuilt and re-read and the table is regenerated with a dated changelog entry.

If you find a verdict you disagree with, open an issue with the family number and the challenge line you have in mind. Corrections are made in public and logged. MathVet takes no funding from any lab whose work it reviews; there are no conflicts to disclose at the time of publication.
