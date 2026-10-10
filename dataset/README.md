# dataset/ — 416 Lean challenge statements from `openai/math` paired with their papers' main theorems

One JSON object per Comparator challenge: the Lean challenge file, the natural-language main theorem(s) of the paper(s) it belongs to, the family's overview summary and the lab's own `lean/docs` scope text, structural metadata (import cone, external packages, local checker status) and **MathVet's fidelity label** (does the Lean state the family's headline?). 405 rows, 235 result families, built from the `openai/math` clone at commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a` (2026-10-06, the only upstream commit at review time). The proof library itself (`lean/OAI`, 25.9M lines) stays upstream and is only pointed to (`solution_file`, `cone_*`). Upstream commit `fd4aeeb2` (first version `adc7f124`, 405 rows).

Purpose: evaluate whether a generated Lean statement states the paper's theorem. Labels and additions are Apache-2.0, the same license as the upstream corpus (see Licensing below). The labels are pre-referee (see `../PROTOCOL.md`).

| file | what |
| --- | --- |
| `autoformalization_pairs.jsonl` | the dataset, UTF-8 JSON Lines, 416 rows (6.1 MB), ordered by family number, then by the family's challenge order in `index.json` |
| `stats.json` | every count quoted below, build parameters, cone cross-check |
| `README.md` | this file |

Rebuild (about one minute, deterministic apart from `built_at`; the script was written for the private working repository and expects the clone at `math/`): `python scripts/build_ml_pairs.py` (from a checkout that holds the clone under `math/` or `upstream/openai-math/`) (from a repository that holds the clone). It needs the clone (`math/` in the repo, or in the main checkout when run from a worktree), `index.json` and `verification/` (both tracked); `tmp/import_cones.json` is optional (cross-check only). The builder re-reads its output and asserts: unique challenges, identical keys, `lean_sha256` equals the sha256 of `lean_text` for every untruncated row, every target span lies inside `lean_text`, and every NL block starts at its recorded `tex_file:tex_line`.

```python
import pandas as pd
df = pd.read_json("ml/autoformalization_pairs.jsonl", lines=True)        # 416 rows x 48 columns
gold = df[df.one_to_one & (df.nl_extraction_quality == "good") & (df.fidelity_class == "full")]   # 81 rows
```

## Counts (from `stats.json`)

| | value |
| --- | --- |
| challenges / families / papers in those families | 416 / 242 / 477 (341 are linked from a `lean/docs` page, `lean_linked`) |
| **fidelity, families** (full / partial / weaker-statement / supporting-only) | **144** / 60 / 19 / 12 (none: 0) |
| **fidelity, challenges** (labels are inherited from the family) | **261** / 104 / 25 / 15 |
| **NL extraction quality, challenges** (good / partial / none) | **399** / 6 / 0 |
| NL extraction quality, families (all challenges good / some partial) | 231 / 4 |
| first NL block comes from | `thm:main`-style label 324, first theorem in the introduction 74, `maintheorem` env 1, first theorem anywhere 6 |
| papers with at least one extracted block / with a main block (label, title or env) | 467 of 467 / 388 |
| `one_to_one` (family has 1 challenge and 1 linked paper) | 140 |
| good NL and `full` label | 255 |
| **gold: `one_to_one` and good NL and `full`** | **81** |
| Lean targets resolved | 537 theorems + 65 definitions (all 416 configs resolve) |
| Lean text truncated (> 1000 lines) | 8: EditApproximation, CoarseAssembly, CKSBondiPenrose, ThorpRouting, ThomasonModelStructures, CharacterCriterion, SnakyCertificate, NavierStokesVelocity |
| challenges with a non-Mathlib package in the import cone | 23 (PrimeNumberTheoremAnd 14, StrongPNT 6, RellichKondrachov 6, FixedPointTheorems 3, AbsorptionCutoff 2, Schoenflies, BernoulliRegular, ClassFieldTheory, SphereEversion, Gromov 1 each) |
| local checker status at build time | `check_cmp` pass 11, `check_comparator` pass 3, the rest `none` (solution module not built here) |
| import cone, lines of `lean/OAI` | min 269, median 22,691, p90 130,452, max 2,834,627 (106 challenges <= 10k, 288 <= 50k) |

## Read these before using the labels or the pairs

1. **Fidelity labels are per family, not per pair.** The audit (`verification/lean_scope_audit_part*.{md,json}`) compares a family's *overview summary* (its headline, first-named claim) with *all* of the family's Comparator statements and gives one verdict. Every challenge inherits it (`family_challenges` lists the siblings). A `partial` family can contain a challenge that is a perfectly faithful formalization of the extracted paper theorem (example: `AbhyankarSathaye`, family 049: the Lean states the Sept-24 paper's zero-fibre counterexample for n >= 4; the family headline, the Oct-5 stable-coordinate result, has no statement). For classification use the family as the unit (235 items); the 405-row version is a noisy, inherited relabeling.
2. **The NL side is the paper's main theorem(s), not a per-challenge alignment.** A family with several challenges formalizes several theorems, usually only one of which is the paper's `thm:main`. Papers are ranked per challenge by lexical similarity (`match_score`, a heuristic in [0, 1], not a calibrated probability), but exact pairs are only guaranteed when `one_to_one` is true (140 rows; 81 of them are also good and `full`). `challenge_result_labels` (the "Result" cell of the `lean/docs` table row for that challenge) is a short NL description of what the challenge states.
3. **`nl_extraction_quality` rates the extraction, not the pairing.** `good`: the first block was selected by a main label/title/env or as the first theorem of the introduction, from a paper linked by the docs page. `partial`: only "first theorem anywhere" was available (a technical theorem outside the introduction). `none`: no theorem block (never happens).
4. **The labels came from one model-assisted pass per family**, validated mechanically (schema, titles, challenge sets); there is no second annotator and no agreement statistic. The Lean checks (`check_cmp` pass for 11 rows, real Comparator for 3) only confirm that a challenge statement matches the constant the solution proves, not that it states the NL headline. Verdict policy (verbatim in the audit files): the verdict is about the summary's primary claim; `full` iff the Lean implies it after unpacking definitions or a named routine step; `weaker-statement` iff it does not imply it; a second co-equal headline claim with no statement makes the verdict `partial`; `supporting-only` is a lemma/auxiliary statement only. A `full` label does not say the mathematics is correct (the upstream README states that unformalized results could have issues) and not that every definition is standard (see `fidelity_suspicious_defs`).
5. **Many theorem types are named definitions** (roughly a fifth by a regex count, e.g. `theorem main : MainStatement`). Use `lean_text`, not `lean_targets[*].statement` alone, as the statement of record.
6. **Snapshot fields.** `check_cmp` / `check_comparator` read `verification/lean_checks/` as committed with this build; they change when more solution modules are built. Cone numbers: see "Import cone" below.
7. **Contamination.** The upstream repository is public since 2026-10-06; any model whose training data postdates it may have seen these statements.

## Fields

Identity and provenance

| field | type | meaning |
| --- | --- | --- |
| `challenge` | str | unique key; stem of `lean/ComparatorChallenges/<challenge>.{lean,json}` |
| `upstream_commit`, `source_url` | str | audited `openai/math` commit; GitHub blob URL of the `.lean` at that commit |
| `lean_file`, `config_file` | str | paths inside `openai/math` |
| `challenge_module`, `solution_module` | str | from the Comparator config |
| `solution_file`, `solution_file_lines` | str, int | the solution module's own file (`lean/<module path>.lean`) and its length; most of the proof sits in the import cone below |

Comparator config (verbatim from the `.json`)

| field | type | meaning |
| --- | --- | --- |
| `theorem_names`, `definition_names` | [str] | fully qualified names the solution must provide (`definition_names` is non-empty for 9 challenges, 45 names in all) |
| `permitted_axioms` | [str] | normally `propext`, `Quot.sound`, `Classical.choice` |
| `enable_nanoda` | bool/null | null in 2 configs |
| `solution_imports` | [str]/null | only `SymmetricMahlerEquality` has it |

Lean challenge

| field | type | meaning |
| --- | --- | --- |
| `lean_text` | str | the whole challenge file (imports, definitions, theorem statements ending in `sorry`; `HarmonicGrowth` uses `axiom mainStatement` instead). Files over 1000 lines: first 400 lines, then each target declaration, joined by `-- [... lines a-b of N elided by build_ml_pairs.py ...]` markers |
| `lean_truncated`, `lean_lines_total`, `lean_text_lines`, `lean_bytes_total` | bool, int, int, int | truncation flag; lines and bytes of the original file; lines of `lean_text` |
| `lean_sha256` | str | sha256 of the full original file bytes (verifies untruncated rows; pins truncated ones) |
| `lean_has_sorry`, `lean_has_axiom_decl` | bool | 404 rows have `sorry`; one has an `axiom` placeholder |
| `lean_targets` | [obj] | one per config name: `name`, `role` (`theorem` / `definition`), `kind` (Lean keyword), `line_start`, `line_end` (1-based, **original file** numbering, docstring included), `statement` (declaration without the trailing `:= by sorry`), `text` (as in the file) |
| `lean_targets_status` | str | `ok` when every config name resolved (all 416) |

Import cone and checker status

| field | type | meaning |
| --- | --- | --- |
| `cone_oai_files`, `cone_oai_lines` | int | size of the transitive import cone of `solution_module` inside `lean/OAI` (proxy for proof size and build cost) |
| `cone_external` | [str] | import roots outside `OAI` (Mathlib, Lean core roots, third-party packages) |
| `cone_axiom_files` | [str] | cone files with a custom `axiom` declaration; empty for all rows |
| `check_cmp` | str | `pass` / `fail` / `none`: `scripts/lean_cmp.sh` result in `verification/lean_checks/<challenge>.cmp.txt` (`none` = solution not built or not checked) |
| `check_comparator` | str | same for the real `leanprover/comparator` run (`<challenge>.comparator.txt`) |

Family and fidelity

| field | type | meaning |
| --- | --- | --- |
| `family`, `family_title`, `family_subject` | str | family number (`lean/docs/<family>.md`, cross-checked against `index.json`), title, discipline (17 values) |
| `family_summary` | str | the overview summary of the family (TeX math, some HTML), i.e. the headline the audit judged |
| `family_scope` | str | the `## Scope` text of `lean/docs/<family>.md`, written by the formalizers; **leaks the answer for fidelity classification** |
| `family_challenges` | [str] | all challenges of the family |
| `challenge_result_labels` | [str] | "Result" cell(s) of the docs table row(s) linking this challenge |
| `fidelity_label` | str | audit `headline_formalized`: `full`, `partial`, `weaker-statement`, `supporting-only` (`none` is defined but unused) |
| `fidelity_class` | str | short form: `full`, `partial`, `weaker`, `supporting` |
| `fidelity_gap_note`, `fidelity_suspicious_defs` | str, [str] | the auditor's explanation and list of non-standard definitions; **explanations, not inputs** |
| `fidelity_audit_part` | int | which audit file (1, 2 or 3) |
| `one_to_one` | bool | family has exactly one challenge and one linked paper |

Natural language

| field | type | meaning |
| --- | --- | --- |
| `nl_extraction_quality` | str | `good` / `partial` / `none` (see point 3 above) |
| `nl_primary_paper`, `nl_abstract` | str | directory (under `preprints/`) of the paper the first block came from, and its abstract as given in `CONTENTS.md` (Markdown/HTML-ish) |
| `nl_main_theorems` | [obj] | 1 to 3 raw TeX blocks (see below) |
| `nl_papers` | [obj] | every paper of the family: `dir`, `title`, `abstract`, `lean_linked`, `match_score` (paper-level), `n_theorem_blocks`, `tex_root` |

`nl_main_theorems[*]`: `paper_dir`; `reason` (`main_label`, `main_title`, `main_env`, `intro_first`, `first_theorem`, `fallback_env`); `env`, `label`, `title` (optional argument, e.g. "Main Theorem"); `section`, `subsection`, `in_intro`; `tex_file`, `tex_line` (position in `preprints/<paper_dir>/`); `tex` (the block from `\begin{...}` to `\end{...}`; TeX comments removed, macros and `\ref`s unresolved); `tex_chars`, `tex_truncated` (none truncated; cap 12,000 chars); `n_refs` (count of `\ref`/`\eqref`/`\cite`, a rough self-containedness measure); `match_score` (lexical match of this block with the challenge).

Titles and abstracts are parsed from `CONTENTS.md` and equal `index.json` except for two family-107 manuscripts that `index.json` mis-parses (a "secondary writeup" line gave one of them null fields and the next one a polluted title); they are repaired here and listed in `stats.json` (`index_json_manuscript_repairs`).

How the NL side is built: root TeX file = the file with `\begin{document}` under `preprints/<dir>/build/` (prefers `main.tex` / `paper.tex`; if it has no theorem, the next root, which handles PDF-assembly wrappers), with `\input`/`\include` inlined. Blocks are `theorem`-like environments. A block is *main* when its label matches `main` / `mainthm` / `maintheorem` / `headline` / `principal` as a delimited word (`thm:main`, `intro:main`, `s:main`), when its title reads "Main theorem/result" or "Theorem A", or when the environment is `maintheorem`. The first theorem of the introduction (first `\section`, or one named introduction/overview/main results) is added; if there is neither, the first theorem anywhere (`partial`). Papers of a family are restricted to the docs-linked ones and ranked per challenge by a TF-IDF score: cosine between the challenge's short description (name and docs result label) and each paper's title, plus the same against title and abstract, plus half the cosine between the full Lean-side text (names, docstrings, statement identifiers) and the paper's title, abstract and blocks, divided by 2.5 (`nl_papers[*].match_score`). The best paper's blocks come first, at most 3 in total. There is no ground truth for which paper a challenge belongs to; the score was tuned by eye on the multi-paper families (184 rows), where it mostly follows the result label (e.g. `KaplanskyDirectFiniteness` -> the characteristic-two paper, `MatrixFields` -> the every-field paper) and sometimes does not (`ContinuumCoulombHardness`, whose label says binary charges, goes to the unit-charge paper). Treat blocks after the first, and any block of a multi-paper row, as candidates.

Import cone: `cone_*` are recomputed from the clone with the definition of `scripts/import_cones.py` (transitive `import` closure inside `lean/OAI`) and cross-checked against `tmp/import_cones.json`. They agree for 402 challenges; the original parser mishandled `import all X` and module names with an apostrophe, so `ArtinParabolicIntersections` (781 -> 782 files, 73,065 -> 73,097 lines), `HarmonicArtin` (659 -> 660, 62,869 -> 62,901) and `WeakHessian` (530 -> 542, 64,010 -> 65,542) use the corrected values (the audit files report the same lines). The three `axiom_files` entries in `tmp/import_cones.json` (`OccupiedOverlap`, `OptimalMaxCut`, `PartitionConsistency`) are the word "axiom" at the start of a docstring line, not declarations; here `cone_axiom_files` is empty.

Example (long strings shortened with `...`; real rows are complete):

```json
{"challenge": "BorsukNine", "solution_module": "OAI.Geometry.Borsuk.Main", "theorem_names": ["OAI.BorsukNine.main_theorem"],
 "lean_text": "import Mathlib\n\nnamespace OAI\n\nnamespace BorsukNine\n\nabbrev Vector4 := EuclideanSpace ℝ (Fin 4)\n...", "lean_truncated": false,
 "lean_targets": [{"name": "OAI.BorsukNine.main_theorem", "role": "theorem", "kind": "theorem", "line_start": 25, "line_end": 30,
                   "statement": "theorem main_theorem :\n    IsCompact projectorSet ∧\n    projectorSet ⊆ traceOneSymmetric ∧\n ..."}],
 "cone_oai_files": 269, "cone_oai_lines": 78964, "cone_external": ["Mathlib"], "check_cmp": "none",
 "family": "156", "family_title": "Borsuk's conjecture fails in dimension nine", "family_challenges": ["BorsukNine"],
 "challenge_result_labels": ["Nine-dimensional Borsuk counterexample"],
 "fidelity_label": "full", "fidelity_class": "full", "one_to_one": true, "nl_extraction_quality": "good",
 "nl_main_theorems": [{"paper_dir": "A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026", "reason": "main_label",
                       "label": "thm:main", "section": "Introduction", "in_intro": true, "tex_file": "build/sections/introduction.tex", "tex_line": 18,
                       "n_refs": 0, "tex": "\\begin{theorem}\\label{thm:main}\nThe compact set\n\\[\n X=\\{uu^{\\mathsf T}:u\\in\\mathbb R^4,\\ \\|u\\|=1\\}\n ...", "match_score": 0.0851}],
 "nl_papers": [{"dir": "A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026", "lean_linked": true, "match_score": 0.6914, "n_theorem_blocks": 3}]}
```

## Three evaluation tasks

Split by `family` (never by challenge): siblings share summary, scope text and papers. Example: hold out the families whose `sha256(family)` ends in a fixed hex digit.

### (a) NL theorem -> Lean statement, scored by the Comparator-style checker

- **Input.** `nl_main_theorems[0].tex` (optionally the other blocks, `nl_abstract`, `family_summary`, `challenge_result_labels`) plus a Lean context: `lean_text` with the target spans (`lean_targets[*].line_start..line_end`; only valid when `lean_truncated` is false) removed, so the model sees the definitions but not the statement, and the required names `theorem_names` / `definition_names`. 9 challenge files contain no definitions at all (pure Mathlib), the cleanest cases. The 45 `definition` targets (9 challenges, e.g. `ElementaryPositivity`) are data-producing `def ... := by sorry` witnesses: the thing to reproduce is the `def`'s type.
- **Reference.** `lean_targets[*].statement`.
- **Scoring tiers, strict to lenient.** (1) *elaborates*: candidate file compiles against Mathlib with `sorry` proofs; needs no solution build, works for all 405. (2) *`scripts/lean_cmp.sh` semantics*: the candidate is re-elaborated under a fresh namespace inside the solution module's environment (`scripts/gen_cmp.py`, `scripts/CmpLib.lean`); the closure of constants reachable from the target theorems must be matched, constant by constant, by a same-named `OAI.*` constant of the same kind with alpha-equivalent type (and value, for definitions; constructor counts for inductives); a shadowing check requires the standalone Mathlib-only elaboration to print identically. (3) *`scripts/lean_defeq.sh`*: types and values definitionally equal rather than alpha-equivalent. (4) real `leanprover/comparator` for final confirmation.
- **Cost and coverage.** Tiers 2-4 need the solution module built (`lake build <solution_module>`); `cone_oai_lines` tells how expensive (median 22.7k lines, 106 challenges <= 10k). At build time only 11 rows have `check_cmp = pass` (3 also `check_comparator = pass`). The scripts read `ComparatorChallenges/<C>.lean` directly; scoring a candidate means pointing `gen_cmp.py` at the candidate text (a small change, not done here).
- **Caveat.** Alpha-equivalence is an exact-match criterion against the statement that was actually proved: a faithful but differently phrased formalization fails tier 2. Report tier-1 compile rate and tier-2 pass@k separately; add a rubric or LLM judge using the fidelity definitions for a semantic score.
- **Subsets.** gold = 81 rows (`one_to_one`, good, `full`); silver = 255 rows (good and `full`, pairing not guaranteed).

### (b) Fidelity classification

- **Item.** A family (242 items; the challenge-level 416-row version inherits family labels). **Input:** `family_summary` (optionally the extracted main theorem and abstract) and the Lean text of all the family's challenges (`lean_text`, or the targets plus the definitions they use). **Question:** does the Lean state this headline? **Label:** `fidelity_class` in {`full`, `partial`, `weaker`, `supporting`}.
- **Label distribution (families).** full 144, partial 60, weaker 19, supporting 12; majority-class accuracy 61.3%. Report macro-F1 and a binary full-vs-not score (144 vs 91).
- **Leakage.** Do not feed `family_scope` (the formalizers' scope statement often says what is not covered), `fidelity_gap_note`, `fidelity_suspicious_defs`, `check_*`. `challenge_result_labels` describe the Lean and are borderline; ablate them.
- **Use of the notes.** `fidelity_gap_note` and `fidelity_suspicious_defs` are the rationale; use them to grade explanations or to train a rationale-then-label model, not as inputs.

### (c) Proof-skeleton generation

- **Input.** The Lean statement (`lean_text`) and the NL theorem; optionally the paper's proof, which this file does not store: `preprints/<paper_dir>/<tex_file>` after line `tex_line`.
- **Output.** A Lean file that restates the theorem and proves it from `have` steps or auxiliary `lemma`s whose bodies are `sorry`, with the top-level argument itself complete.
- **Metrics.** (1) skeleton elaborates against Mathlib with only `sorry` warnings; (2) closure: the main theorem's own proof term uses only the skeleton's lemmas, Mathlib and standard axioms (no direct `sorry`), so the decomposition is logically sufficient; (3) fidelity to the real proof: compare the skeleton's lemma statements with the statements of the OAI declarations the solution theorem actually depends on (obtain them from `solution_file` and its cone, with `Expr.getUsedConstants` on the built solution, or by reading the module). The reference decompositions are not stored here.
- **Stratify** by `cone_oai_lines`, `solution_file_lines`, `cone_external` (23 rows depend on third-party packages) and `family_subject`.

## Licensing

- **Upstream content** (`lean_text`, `lean_targets`, `solution_*`, `nl_main_theorems[*].tex`, the abstracts, `family_summary`, `family_scope`, `challenge_result_labels`): extracted from `openai/math`, distributed under the Apache License 2.0 (`LICENSE` at the upstream root and in `lean/`); the manuscripts are credited to "OpenAI". Redistribution keeps the license and must say what was changed: here, 8 Lean files are truncated, TeX comments are removed from the blocks, cone numbers for three challenges are corrected, and all of it is reformatted as JSON. `source_url` and `lean_sha256` point back to the originals.
- **Our additions** (`fidelity_*`, `nl_extraction_quality`, `nl_main_theorems[*].reason|match_score`, `one_to_one`, `check_*`, the family-level audit, `stats.json`, the builder): offered under Apache-2.0 as well, so the file has a single license. This is a default, not a decision recorded elsewhere in this repository: change it here before any public release if you want otherwise.
- No warranty. The fidelity labels are an audit of statements against summaries, not a proof that any theorem is true or that any Lean definition is standard.

## `paper_main_theorems.json` (added 2026-10-10)

One entry per preprint directory at the reviewed commit (722 papers): the paper's main theorem as located by the same
extractor that fills `nl_main_theorems` (the block with a main-theorem label or title, else the first theorem of the
introduction, else the first theorem-like environment; up to three blocks per paper), with `tex_file` and `tex_line`
relative to the paper directory and the TeX excerpt. The per-challenge `nl_main_theorems` field covers only the papers
the lab's scope note links to the Lean; for 13 of the 40 referee-sample families the paper the headline is about is not
among them, so the referee packet (`reviews/openai-math/referee/`) takes its section 4 from this file instead, listing
every paper of the family in catalogue order. Built by the private `scripts/build_paper_theorems.py`.

## `baseline.md` (added 2026-10-10)

Aggregates of a first automated baseline on this dataset: a single-shot Sonnet 5.5 judge (`claude -p`, JSON schema, no tools)
classifying each of the 405 pairs of the first dataset version (upstream commit `adc7f124`) under the PROTOCOL.md rubric, three samples per pair, compared with the MathVet verdicts of that version.
Family-level agreement, confusion matrices, kappa, self-agreement and cost are given; no per-family or per-challenge class is
published while the verdicts are pre-referee (rule T3). The runner is the private `scripts/benchmark_baseline.py`.
