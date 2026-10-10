# Referee packet — MathVet review of `openai/math` @ `adc7f124`

This folder is what each referee receives under the pre-registered protocol ([`PROTOCOL.md`](https://github.com/mathvet/mathvet/blob/main/PROTOCOL.md), section
"The referees"): for each of the 40 sampled families ([`sample.txt`](https://github.com/mathvet/mathvet/blob/main/reviews/openai-math/sample.txt), frozen before
any re-reading), the headline claim, the repository's own scope note, every linked Comparator challenge statement, and the
main theorem of every paper of the family at file and line. It contains nothing from MathVet's own reading.

**Blinding is a request, because this repository is public.** Until both referees' forms have been returned, please do not
open anything of MathVet's except this folder: not the fidelity table, `STATUS.md`, the review YAML, the `dataset/`,
`source/` or `docs/` folders, the site math.vet, nor the section "The sample" of `PROTOCOL.md` (it names families by
stratum). Read the protocol's "The referees" and "The rubric" sections only; the rubric is repeated below.

## What to do

1. **Consent and pilot.** Written consent precedes the pilot (the protocol requires it). Then classify the three families
   named in your invitation first, timing yourself, and return the form for those three before continuing. The pilot
   checks the packet and the rubric, not you.
2. **Each family.** Open `families/NNN/README.md`. Section 1 is the headline (the overview summary written by the
   repository's authors); section 2 the repository's scope note; section 3 the challenge statements, copied next to the
   README as `.lean` files (their proofs are `sorry` by design: only the statements and the definitions they use matter;
   the theorem names in each `.json` are the ones the Comparator checks); section 4 every paper of the family with its
   main theorem at file and line. Decide the class of the summary's **primary (first-named) claim** under the rubric
   below and add one line to your copy of `form.csv` (save it as `form-<yourname>.csv`): the class, one sentence of
   justification naming the step or the gap, any non-standard definition you noticed, and the minutes spent. Quote
   `.lean` line numbers where that helps.
3. **Independence.** Do not discuss a family with the other referee until both forms are in. Where the two of you
   disagree, the adjudicator sees both justifications and decides; the adjudication is published with the result.
4. **Return** `form-<yourname>.csv` and any general remarks by email. As the protocol states, your name, rate and hours are
   published with the result.

## The rubric (verbatim from PROTOCOL.md)

The verdict is about the summary's primary (first-named) claim.

- `full`: the Lean statement(s) imply that claim after unpacking definitions or one routine step; name the step.
- `partial`: only a special case is stated, or a second co-equal headline claim (joined by "also", "and", "complementary theorem") has no challenge statement. A mere corollary or application ("together with X this shows") does not make a verdict `partial`.
- `weaker-statement`: the Lean statement does not imply the primary claim (a nontrivially weaker statement).
- `supporting-only`: the Lean states a lemma or auxiliary result, not the headline.
- `none`: nothing in the summary is covered.

When the scope note and the Lean disagree, the Lean wins. Non-standard definitions are noted but do not by themselves change the class.

## Conventions

- The Lean statement(s) of a family are the `theorem_names` (and `definition_names`) listed in each challenge's `.json`,
  as they appear in the copied `.lean` file; the definitions in that file are part of the statement.
- Section 4 lists the family's papers in catalogue order and marks which of them the scope note links the Lean to. The
  headline's first-named claim may be stated in a paper the Lean is not linked to; that is part of what you are judging.
- The theorem shown for each paper was located by a text heuristic (the block with a main-theorem label or title, else
  the first theorem of the introduction). It is a pointer, not a judgment. If it is not the statement the headline refers
  to, read the paper's own statement and say so in your justification.
- `none` is for a family where nothing in the summary is covered by the Lean statements.
- Links point at the reviewed commit on GitHub; the copies in this folder are byte-identical to it (`manifest.sha256`).

## Files

| file | purpose |
|---|---|
| `families/NNN/README.md` | the four sections above for family NNN |
| `families/NNN/*.lean`, `*.json` | the challenge statements and their Comparator configs, copied from the reviewed commit |
| `form.csv` | the blank classification form (one row per family) |
| `manifest.sha256` | SHA-256 of every file in this folder except itself |
| `make_packet.py` | regenerates this folder from the reviewed commit; it verifies that no review text is in the packet |

Scoring happens outside this folder, after the forms are returned (`reviews/openai-math/referee_score.py`, which needs the
verdicts and therefore is not part of the packet).
