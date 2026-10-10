# Referee packet — MathVet review of `openai/math` @ `adc7f124`

This folder is what each referee receives under the pre-registered protocol ([`PROTOCOL.md`](../../../PROTOCOL.md), section
"The referees"): for each of the 40 sampled families ([`sample.txt`](../sample.txt), frozen before any re-reading), the
headline claim, the repository's own scope note, every linked Comparator challenge statement, and the paper's main theorem at
file and line. It contains nothing from MathVet's own reading. Because this repository is public, the blinding is a request:
please do not open MathVet's fidelity table, `STATUS.md` or the review YAML until both referees' forms have been returned.

## What to do

1. **Pilot.** Classify the three families named in your invitation first, timing yourself, and return the form for those
   three before continuing. The pilot checks the packet and the rubric, not you.
2. **Each family.** Open `families/NNN/README.md`. Section 1 is the headline (the overview summary written by the
   repository's authors); section 2 the repository's scope note; section 3 the challenge statements, copied next to the
   README as `.lean` files (their proofs are `sorry` by design: only the statements and the definitions they use matter;
   the theorem names in each `.json` are the ones the Comparator checks); section 4 the paper's main theorem at file and
   line. Decide the class of the summary's **primary (first-named) claim** under the rubric below and add one line to your
   copy of `form.csv` (save it as `form-<yourname>.csv`): the class, one sentence naming the step or the gap, and the
   minutes spent. Quote `.lean` line numbers where that helps.
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
- The paper's main theorem in section 4 was located by a text heuristic (`dataset/README.md`). If you believe the headline
  refers to a different theorem of the paper, read that one and say so in your justification.
- `none` is for a family where nothing in the summary is covered by the Lean statements.
- Links point at the reviewed commit on GitHub; the copies in this folder are byte-identical to it (`manifest.sha256`).

## Files

| file | purpose |
|---|---|
| `families/NNN/README.md` | the four sections above for family NNN |
| `families/NNN/*.lean`, `*.json` | the challenge statements and their Comparator configs, copied from the reviewed commit |
| `form.csv` | the blank classification form (one row per family) |
| `manifest.sha256` | SHA-256 of every file in the packet |
| `score.py` | run after the forms are returned: agreement, adjudicated classes, the error rate and its interval per PROTOCOL.md |
| `make_packet.py` | regenerates this folder from the reviewed commit; it verifies that no review text is in the packet |
