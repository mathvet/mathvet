#!/bin/bash
# Usage: checker/cloud/run.sh <Challenge> [<Challenge> ...]
# For each challenge: build the solution module (resumable: rerun after an interruption), run the closure comparison
# (checker/lean_cmp.sh), then the real Comparator with landrun. Evidence goes to reviews/openai-math/evidence/lean_checks/
# with a provenance header (machine, landrun status, session URL) and a SHA-256 line printed at the end.
set -uo pipefail
ROOT="${MATHVET_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
export MATHVET_ROOT="$ROOT" OPENAI_MATH_LEAN="$ROOT/upstream/openai-math/lean"
export COMPARATOR_BIN="$ROOT/tmp/comparator/.lake/build/bin/comparator" COMPARATOR_LEAN4EXPORT="$ROOT/tmp/lean4export/.lake/build/bin/lean4export"
export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1
if command -v landrun >/dev/null && landrun --ro /usr --ro /lib --ro /lib64 --ro /bin --ro /etc -- /bin/true 2>/dev/null; then
  export COMPARATOR_LANDRUN="$(command -v landrun)"; SANDBOX="landrun=real $(landrun --version 2>&1 | head -1)"
elif command -v landrun >/dev/null && landrun --best-effort --ro /usr --ro /lib --ro /lib64 --ro /bin --ro /etc -- /bin/true 2>/dev/null; then
  export COMPARATOR_LANDRUN="$ROOT/checker/cloud/landrun-best-effort.sh"; SANDBOX="landrun=real-best-effort $(landrun --version 2>&1 | head -1) on Landlock ABI $(landrun --ro /usr -- /bin/true 2>&1 | grep -o 'Got Landlock ABI v[0-9]*' | head -1)"
else
  export COMPARATOR_LANDRUN="$ROOT/checker/fake-landrun.sh"; SANDBOX="landrun=SHIM (no sandbox: Landlock unavailable on this kernel)"
fi
OUT="$ROOT/reviews/openai-math/evidence/lean_checks"; mkdir -p "$OUT"
SESSION="https://claude.ai/code/${CLAUDE_CODE_REMOTE_SESSION_ID/#cse_/session_}"
for C in "$@"; do
  echo "=== $(date -u +%FT%TZ) $C: build"
  "$ROOT/checker/lean_check.sh" "$C" | tail -3
  if ! grep -q '^== build rc=0' "$OUT/$C.log"; then echo "BUILD FAILED or incomplete for $C; rerun to resume"; continue; fi
  echo "=== $(date -u +%FT%TZ) $C: closure comparison"
  "$ROOT/checker/lean_cmp.sh" "$C" | tail -2
  echo "=== $(date -u +%FT%TZ) $C: Comparator ($SANDBOX)"
  hdr="$OUT/$C.comparator.hdr"
  { echo "== provenance: mathvet cloud run"; echo "machine: $(uname -srm), $(nproc) vCPU, $(free -g | awk '/Mem/{print $2}') GB RAM, Ubuntu $(. /etc/os-release; echo $VERSION_ID)"; echo "kernel lsm: $(cat /sys/kernel/security/lsm 2>/dev/null)"; echo "sandbox: $SANDBOX"; echo "lean: $(lean --version)"; echo "comparator: $(git -C "$ROOT/tmp/comparator" rev-parse --short HEAD)  lean4export: $(git -C "$ROOT/tmp/lean4export" describe --tags --always)"; echo "upstream: openai/math $(git -C "$OPENAI_MATH_LEAN/.." rev-parse HEAD)"; echo "session: $SESSION"; } > "$hdr"
  "$ROOT/checker/comparator_run.sh" "$C" | tail -3
  cat "$hdr" "$OUT/$C.comparator.txt" > "$OUT/$C.comparator.tmp" && mv "$OUT/$C.comparator.tmp" "$OUT/$C.comparator.txt" && rm -f "$hdr"
  echo "=== $(date -u +%FT%TZ) $C: done; sha256 $(sha256sum "$OUT/$C.comparator.txt" | cut -c1-64)"
  grep -E 'okay|accepts|exit=' "$OUT/$C.comparator.txt" | tail -3
done
