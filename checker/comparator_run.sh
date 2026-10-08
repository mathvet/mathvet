#!/bin/bash
# Usage: checker/comparator_run.sh <Challenge>
# Runs the real leanprover/comparator on the challenge's JSON config. Needs COMPARATOR_BIN, COMPARATOR_LEAN4EXPORT (built
# against the clone's toolchain; see build_comparator.sh) and COMPARATOR_LANDRUN (real landrun on Linux; on other systems
# env.sh falls back to fake-landrun.sh, which runs the same pipeline WITHOUT a sandbox — say so when you cite the result).
source "$(dirname "$0")/env.sh"
C="$1"; L="$OPENAI_MATH_LEAN"; OUT="$MATHVET_CHECKS"
cd "$L" && { echo "== $C comparator start $(date -u +%FT%TZ) landrun=$COMPARATOR_LANDRUN"; lake env "$COMPARATOR_BIN" "ComparatorChallenges/$C.json" 2>&1 | grep -v 'has local changes'; echo "== comparator exit=${PIPESTATUS[0]} end $(date -u +%FT%TZ)"; } > "$OUT/$C.comparator.txt"
grep -E 'okay|accepts|exit=|rror|FAIL|not' "$OUT/$C.comparator.txt" | tail -4
