#!/bin/bash
# Usage: checker/lean_check.sh <Challenge> [--nobuild]
# Builds the solution module named in ComparatorChallenges/<Challenge>.json, then prints `#check @theorem` for every
# theorem and `#print` for every definition declared in the challenge file, once against Mathlib alone and once inside
# the solution's environment, and `#print axioms` for the solution. Output: $MATHVET_CHECKS/<Challenge>.{log,challenge.txt,solution.txt}
set -u
source "$(dirname "$0")/env.sh"
C="$1"; NOBUILD="${2:-}"; L="$OPENAI_MATH_LEAN"; OUT="$MATHVET_CHECKS"
J="$L/ComparatorChallenges/$C.json"; MOD=$(jq -r .solution_module "$J")
LOG="$OUT/$C.log"
cd "$L"
if [ "$NOBUILD" != "--nobuild" ]; then
  : > "$LOG"; echo "== $C  module=$MOD  start=$(date -u +%FT%TZ)" | tee -a "$LOG"
  T0=$(date +%s); lake build "$MOD" >> "$LOG" 2>&1; RC=$?; T1=$(date +%s)
  echo "== build rc=$RC seconds=$((T1-T0))" | tee -a "$LOG"
  [ $RC -ne 0 ] && { echo "BUILD FAILED $C"; exit 1; }
else
  echo "== $C recheck (no build) $(date -u +%FT%TZ)" | tee -a "$LOG"
fi
python3 "$HERE/gen_checks.py" "$C" >> "$LOG"
lake env lean "$L/Scratch/Challenge_$C.lean" 2>&1 | grep -v "declaration uses 'sorry'" | grep -v '^warning: .*has local changes' > "$OUT/$C.challenge.txt"
lake env lean "$L/Scratch/Solution_$C.lean" 2>&1 | grep -v '^warning: .*has local changes' > "$OUT/$C.solution.txt"
echo "AXIOMS: $(grep 'depends on axioms' "$OUT/$C.solution.txt" | tr '\n' ' ')" | tee -a "$LOG"
echo "== end=$(date -u +%FT%TZ)" >> "$LOG"
