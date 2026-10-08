#!/bin/bash
# Usage: nohup checker/comparator_queue.sh > tmp/comparator_queue.log 2>&1 &
# For up to 12 hours, runs the real Comparator on every challenge that has a clean closure check but no Comparator result yet.
source "$(dirname "$0")/env.sh"
for i in $(seq 1 72); do
  for f in "$MATHVET_CHECKS"/*.cmp.txt; do
    c=$(basename "$f" .cmp.txt)
    [ -f "$MATHVET_CHECKS/$c.comparator.txt" ] && continue
    grep -q '^== build rc=0' "$MATHVET_CHECKS/$c.log" 2>/dev/null || grep -q 'Build completed successfully' "$MATHVET_CHECKS/$c.log" 2>/dev/null || continue
    grep -q 'comparator-style: ok=' "$f" 2>/dev/null || continue
    echo "=== $(date -u +%FT%TZ) comparator $c"
    "$HERE/comparator_run.sh" "$c"
  done
  sleep 600
done
