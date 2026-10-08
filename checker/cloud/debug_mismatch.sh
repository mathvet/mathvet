#!/bin/bash
# Usage: checker/cloud/debug_mismatch.sh <Challenge> <batch>
# For every constant the closure comparison flagged, print the challenge-copy (Chal.*) and solution (OAI.*) versions with
# universes, implicit arguments and proofs shown, into evidence/cloud/<Challenge>.mismatch-debug.txt, then push via finish.sh.
set -uo pipefail
ROOT="${MATHVET_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"; C="$1"; B="$2"
L="$ROOT/upstream/openai-math/lean"; EV="$ROOT/reviews/openai-math/evidence/cloud"
export PATH="$HOME/.elan/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1
cd "$L" || exit 1
cp "Scratch/Cmp_$C.lean" "Scratch/Dbg_$C.lean"
printf '\nset_option pp.universes true\nset_option pp.explicit true\nset_option pp.proofs true\nset_option pp.fullNames true\n' >> "Scratch/Dbg_$C.lean"
NAMES=$(grep -oE 'CMP OAI\.[A-Za-z0-9_.]+ \[(def|thm|ind|ctor)\] [A-Z_]+MISMATCH' "$EV/$C.cmp.txt" | awk '{print $2}')
for n in $NAMES; do
  printf '#print %s\n#print %s\n' "${n/OAI./Chal.}" "$n" >> "Scratch/Dbg_$C.lean"
done
# second pass without notation: set-builder, filter and similar notations hide instance arguments (e.g. the Decidable
# instance inside Finset.filter), which is exactly where two elaborations of a `classical` tactic block differ
printf '\nset_option pp.notation false\nset_option pp.fieldNotation false\n' >> "Scratch/Dbg_$C.lean"
for n in $NAMES; do
  printf '#print %s\n#print %s\n' "${n/OAI./Chal.}" "$n" >> "Scratch/Dbg_$C.lean"
done
{ echo "== mismatch debug for $C $(date -u +%FT%TZ): the Chal.* constant is the challenge source re-elaborated inside the solution environment; OAI.* is the solution's"; lake env lean "Scratch/Dbg_$C.lean" 2>&1 | grep -v 'has local changes' | grep -v '^CMP '; } > "$EV/$C.mismatch-debug.txt"
wc -c "$EV/$C.mismatch-debug.txt"; cd "$ROOT" && bash checker/cloud/finish.sh "$B" 2>&1 | tail -3
