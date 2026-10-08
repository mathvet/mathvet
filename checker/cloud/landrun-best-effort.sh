#!/usr/bin/env bash
# Optional wrapper (Comparator already passes --best-effort itself; keep for other callers): adds --best-effort so that a kernel with an older
# Landlock ABI (the cloud VM has ABI v7; landrun 0.1.17 asks for v9) still sandboxes with everything that ABI supports,
# instead of refusing. The real landrun must be on PATH or in LANDRUN_BIN. Everything else is passed through unchanged.
set -euo pipefail
REAL="${LANDRUN_BIN:-$(command -v landrun)}"
exec "$REAL" --best-effort "$@"
