#!/bin/bash
# Apply openai/math's own compatibility patches (lean/patches/<pkg>-lean4341.patch) to the external packages that lake has
# materialised under lean/.lake/packages/<pkg>. Upstream applies them from a lakefile post_update hook, which only runs on
# `lake update`; this project never runs `lake update` (it would move the pinned manifest), so the patches are applied here.
# Idempotent: a patch that is already applied (reverse-applies cleanly) is skipped. Usage: checker/apply_patches.sh [lean dir]
set -u
source "$(dirname "$0")/env.sh"
L="${1:-$OPENAI_MATH_LEAN}"; cd "$L" || exit 1
n_ok=0; n_skip=0; n_fail=0
for p in patches/*-lean4341.patch; do
  pkg=$(basename "$p" -lean4341.patch); d=".lake/packages/$pkg"
  if [ ! -d "$d" ]; then echo "SKIP $pkg: package not materialised"; n_skip=$((n_skip+1)); continue; fi
  if git -C "$d" apply --check --reverse "$PWD/$p" >/dev/null 2>&1; then echo "ok   $pkg: already applied"; n_ok=$((n_ok+1)); continue; fi
  if git -C "$d" apply "$PWD/$p" >/dev/null 2>&1; then echo "ok   $pkg: applied"; n_ok=$((n_ok+1)); else echo "FAIL $pkg: patch does not apply"; n_fail=$((n_fail+1)); fi
done
echo "patches: applied/present $n_ok, skipped $n_skip, failed $n_fail"
[ $n_fail -eq 0 ]
