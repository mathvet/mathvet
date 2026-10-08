#!/bin/bash
# Clone and build leanprover/comparator and lean4export (at a tag whose lean-toolchain matches the clone's toolchain) under tmp/.
source "$(dirname "$0")/env.sh"
TC=$(cat "$OPENAI_MATH_LEAN/lean-toolchain" 2>/dev/null); echo "clone toolchain: $TC"
mkdir -p "$ROOT/tmp" && cd "$ROOT/tmp"
[ -d lean4export ] || git clone -q https://github.com/leanprover/lean4export
[ -d comparator ] || git clone -q https://github.com/leanprover/comparator
cd lean4export && git fetch -q --tags
want=$(echo "$TC" | sed -E 's/.*:(v[0-9]+\.[0-9]+).*/\1/'); best=""
for t in $(git tag | sort -V); do case "$(git show $t:lean-toolchain 2>/dev/null)" in *"$want"*) best=$t;; esac; done
echo "lean4export tag: ${best:-<none matched; using current checkout>}"; [ -n "$best" ] && git checkout -q "$best"
lake build 2>&1 | tail -3; cd ../comparator && lake build 2>&1 | tail -3
ls -la "$ROOT"/tmp/{lean4export,comparator}/.lake/build/bin/ 2>/dev/null
