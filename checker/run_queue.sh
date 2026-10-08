#!/bin/bash
# Usage: nohup checker/run_queue.sh Challenge1 Challenge2 ... > tmp/queue.log 2>&1 &
# For each challenge: build + print checks (lean_check.sh), then the closure comparison (lean_cmp.sh) if the build succeeded.
source "$(dirname "$0")/env.sh"
for c in "$@"; do
  echo "=== $(date -u +%FT%TZ) start $c"
  "$HERE/lean_check.sh" "$c"
  if grep -q '^== build rc=0' "$MATHVET_CHECKS/$c.log"; then "$HERE/lean_cmp.sh" "$c"; else echo "skip cmp: build failed for $c"; fi
  echo "=== $(date -u +%FT%TZ) done $c"
done
echo "=== $(date -u +%FT%TZ) QUEUE COMPLETE"
