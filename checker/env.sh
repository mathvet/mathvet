# Sourced by the checker scripts. Override any variable in the environment.
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${MATHVET_ROOT:-$(cd "$HERE/.." && pwd)}"
: "${OPENAI_MATH_LEAN:=$ROOT/upstream/openai-math/lean}"                 # the openai/math clone's lean/ directory
: "${MATHVET_CHECKS:=$ROOT/reviews/openai-math/evidence/lean_checks}"     # where logs are written
: "${COMPARATOR_BIN:=$ROOT/tmp/comparator/.lake/build/bin/comparator}"    # leanprover/comparator (checker/build_comparator.sh)
: "${COMPARATOR_LEAN4EXPORT:=$ROOT/tmp/lean4export/.lake/build/bin/lean4export}"
: "${COMPARATOR_LANDRUN:=$(command -v landrun || echo "$HERE/fake-landrun.sh")}"  # real landrun on Linux; the shim sandboxes nothing
export PATH="$HOME/.elan/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1
export OPENAI_MATH_LEAN MATHVET_CHECKS COMPARATOR_BIN COMPARATOR_LEAN4EXPORT COMPARATOR_LANDRUN
mkdir -p "$MATHVET_CHECKS" "$OPENAI_MATH_LEAN/Scratch"
