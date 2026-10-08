#!/bin/bash
# Usage: checker/cloud/recheck.sh <Challenge> <batch>
# Re-run the closure comparison with the current checker scripts from origin/main (the solution must already be built on this VM),
# then push the refreshed evidence to branch cloud/<batch>.
set -uo pipefail
ROOT="${MATHVET_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"; C="$1"; B="$2"
cd "$ROOT" && git fetch -q origin main && for f in checker/gen_cmp.py checker/gen_checks.py checker/lean_cmp.sh checker/CmpLib.lean checker/env.sh; do git show origin/main:$f > $f; done
export MATHVET_ROOT="$ROOT" OPENAI_MATH_LEAN="$ROOT/upstream/openai-math/lean" MATHVET_CHECKS="$ROOT/reviews/openai-math/evidence/cloud"
export PATH="$HOME/.elan/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1
bash checker/lean_cmp.sh "$C" | tail -3
bash checker/cloud/finish.sh "$B" 2>&1 | tail -3
