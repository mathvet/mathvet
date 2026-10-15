#!/bin/bash
# Resumable queue for a long-lived Linux VM (no GitHub token: the evidence is pulled back by the operator with rsync).
# Usage: nohup checker/cloud/queue.sh <list-file> > tmp/queue.log 2>&1 &
# Runs checker/cloud/run.sh for each challenge in the list that has no finished Comparator log yet (a comparator.txt with
# an "exit=" line), one at a time; builds resume from .lake if the machine was preempted mid-way. Writes tmp/queue.state.
set -u
ROOT="${MATHVET_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"; cd "$ROOT" || exit 1
LIST="$1"; EV="$ROOT/reviews/openai-math/evidence/cloud"; mkdir -p tmp
echo "$(date -u +%FT%TZ) queue start pid=$$ host=$(hostname) list=$LIST" >> tmp/queue.state
while read -r c; do
  [ -z "$c" ] && continue; case "$c" in \#*) continue;; esac
  if grep -q 'exit=' "$EV/$c.comparator.txt" 2>/dev/null; then echo "$(date -u +%FT%TZ) skip $c (done)" >> tmp/queue.state; continue; fi
  echo "$(date -u +%FT%TZ) start $c" >> tmp/queue.state
  bash checker/cloud/run.sh "$c" 2>&1 | tail -40
  # Lake leaves a <Module>.setup.json (6-8 MB: the module's whole import closure as absolute paths) beside the IR of every
  # module it compiles and never removes it; 28k of them filled the 193 GB disk on 2026-10-13. A built module stays
  # up to date without its setup file (lake build --no-build), so drop them after each challenge.
  find "${OPENAI_MATH_LEAN:-$ROOT/upstream/openai-math/lean}/.lake/build/ir" -name '*.setup.json' -delete 2>/dev/null
  echo "$(date -u +%FT%TZ) disk after $c: $(df -h "$ROOT" | awk 'NR==2{print $4" free of "$2}')"
  echo "$(date -u +%FT%TZ) end $c: $(grep -E 'okay|exit=' "$EV/$c.comparator.txt" 2>/dev/null | tr '\n' ' ' | cut -c1-120)" >> tmp/queue.state
done < "$LIST"
echo "$(date -u +%FT%TZ) queue complete" >> tmp/queue.state
