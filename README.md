# MathVet — independent fidelity reviews of AI-generated formal mathematics

**Does the Lean statement say what the paper claims?** Lean checks proofs. MathVet reviews *statements* against the headlines they are said to establish, in the fields of the community's [formalization.yaml](https://github.com/mathlib-initiative/formalization.yaml) standard, independently of every lab, and publishes the error rate of its own verdicts.

Site: **[math.vet](https://math.vet)** · First review: [`openai/math`](reviews/openai-math/) at commit `adc7f124` (released 2026-10-06, reviewed 2026-10-08) · Status: **pre-referee** (see [PROTOCOL.md](PROTOCOL.md)).

| openai/math | families |
|---|---|
| in the release | 372 |
| with Lean (Comparator challenges) | 235 |
| Lean states the headline in full | 144 |
| Lean states something narrower (60 partial · 19 weaker-statement · 12 supporting-only) | 91 |
| no Lean | 137 |

Read the [explainer](EXPLAINER.md) first. Nothing here claims that any theorem is false; the review says what was machine-checked as stated, what was checked in a narrower form, and what was not checked at all.

## What is in this repository

| path | what |
|---|---|
| [`EXPLAINER.md`](EXPLAINER.md) | the 1,500-word account of the review and its limits |
| [`PROTOCOL.md`](PROTOCOL.md) | the pre-registered referee protocol: frozen 40-family sample, rubric, decision lines, power |
| [`reviews/openai-math/`](reviews/openai-math/) | the review: `fidelity-table.{csv,json}` (235 families), `challenge-status.{csv,json}` (405 challenges), `formalization-review.yaml` (the review in the standard's shape), `STATUS.md`, `sample.txt` + `sample.sha256`, the audit source files under `source/`, every build / closure / Comparator log under `evidence/` |
| [`checker/`](checker/) | the scripts that build a challenge's solution, run the closure comparison and run the real Comparator |
| [`dataset/`](dataset/) | 405 challenge statements paired with their papers' main theorems, scope notes and fidelity labels (Apache-2.0) |
| [`scripts/`](scripts/) | `build_review.py` regenerates every derived file and the site from the sources; `build_index.py`, `import_cones.py`, `build_ml_pairs.py` rebuild the sources from a clone |
| [`docs/`](docs/) | the static site served at math.vet |

## Verdict scale

`full` — the Comparator statement(s) state the family's headline claim · `partial` — only a special case, or only one of several co-equal headline claims · `weaker-statement` — a nontrivially weaker statement · `supporting-only` — a lemma or auxiliary statement · `none` — nothing in the summary is covered. The verdict policy is in [PROTOCOL.md](PROTOCOL.md); the repository's own scope note is quoted next to every verdict.

## Reproduce

```sh
git clone https://github.com/openai/math upstream/openai-math && git -C upstream/openai-math checkout adc7f1241b42e322a6451854ab7e4b4c146bf78a
pip install pyyaml markdown
python3 scripts/build_review.py            # tables, YAML, site from the committed sources and logs
checker/run_queue.sh CirculantHadamard     # rebuild and re-check a challenge yourself (see checker/README.md)
```

## Corrections and contact

Open an [issue](https://github.com/ceshanon/mathvet/issues) with the family number and the challenge line you have in mind. Corrections are made in public and recorded in [CHANGELOG.md](CHANGELOG.md). MathVet takes no funding from any lab whose work it reviews; conflicts, if any arise, are disclosed here.

## License

Apache-2.0 for everything MathVet wrote. The reviewed formalization, manuscripts, scope notes and challenge files are OpenAI's, Apache-2.0, redistributed here only as quoted excerpts, logs and the paired dataset (see [`dataset/README.md`](dataset/README.md) for what was changed).
