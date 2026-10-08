#!/bin/bash
# Usage: checker/lean_cmp.sh <Challenge>   (the solution module must be built: run lean_check.sh first)
# Comparator-style closure comparison (CmpLib.lean): the challenge file is re-elaborated under namespace `Chal` inside the
# solution's environment; every Chal.* constant in the transitive closure of the challenge theorems must be matched by the
# same-named OAI.* constant of the same kind with an alpha-equivalent type (and value for definitions, constructor counts
# for inductives). Then a shadowing check: the challenge text elaborated against Mathlib alone must print identically to
# its copy elaborated inside the solution. Then `#print axioms`. Output: $MATHVET_CHECKS/<Challenge>.cmp.txt
source "$(dirname "$0")/env.sh"
C="$1"; L="$OPENAI_MATH_LEAN"; OUT="$MATHVET_CHECKS"
python3 "$HERE/gen_cmp.py" "$C" >/dev/null || exit 1
cd "$L" && lake env lean "$L/Scratch/Cmp_$C.lean" 2>&1 | grep -v 'has local changes' | grep -vE "declaration uses .sorry." > "$OUT/$C.cmp.txt"
n_ok=$(grep -c 'CMP .* ok$' "$OUT/$C.cmp.txt"); n_bad=$(grep -cE 'MISMATCH|MISSING|NOT_FOUND' "$OUT/$C.cmp.txt"); n_err=$(grep -c 'error' "$OUT/$C.cmp.txt")
python3 "$HERE/gen_checks.py" "$C" >/dev/null
lake env lean "$L/Scratch/Challenge_$C.lean" 2>&1 | grep -v 'has local changes' | grep -vE "declaration uses .sorry.|warning:" | tr -s '[:space:]' ' ' > "$OUT/$C.standalone.norm"
lake env lean "$L/Scratch/Cmp_$C.lean" 2>&1 | grep -v 'has local changes' | grep -vE "declaration uses .sorry.|warning:|^CMP " | sed "/depends on axioms/,/\]/d" | sed 's/Chal\./OAI./g' | tr -s '[:space:]' ' ' > "$OUT/$C.insolution.norm"
if cmp -s "$OUT/$C.standalone.norm" "$OUT/$C.insolution.norm"; then SHADOW="no-shadowing"; else SHADOW="SHADOW-DIFF(see $C.standalone.norm vs $C.insolution.norm)"; fi
echo "== $C comparator-style: ok=$n_ok problems=$n_bad errors=$n_err | $SHADOW | $(grep 'depends on axioms' "$OUT/$C.cmp.txt" | sed 's/.*depends on axioms: //' | sort -u | tr '\n' ' ')" | tee -a "$OUT/$C.cmp.txt"
grep -E 'MISMATCH|MISSING|NOT_FOUND|error' "$OUT/$C.cmp.txt" | head -12
