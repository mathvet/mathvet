#!/bin/bash
# One-time VM setup for a MathVet Comparator run on a Claude Code cloud session (Ubuntu 24.04 x86_64, ~4 vCPU, 16 GB RAM,
# 30 GB disk). Idempotent: safe to rerun. Usage: checker/cloud/setup.sh   (from the mathvet checkout; ~10-20 min first time)
# Needs network access to github.com (GitHub proxy) and to the Mathlib cache host cache.mathlib.org (add it to the
# environment's allowed domains, or set MATHLIB_CACHE_GET_URL to a mirror). Writes a machine report to tmp/cloud-machine.txt.
set -uo pipefail
ROOT="${MATHVET_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
UP="$ROOT/upstream/openai-math"; COMMIT=adc7f1241b42e322a6451854ab7e4b4c146bf78a
export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH" ELAN_NO_OVERRIDE_NOTICE=1
mkdir -p "$ROOT/tmp" "$HOME/.local/bin"
log(){ echo "== $(date -u +%FT%TZ) $*"; }

log "tools (apt: jq zstd)"; (apt-get update -qq >/dev/null 2>&1 && apt-get install -y -qq jq zstd >/dev/null 2>&1) || (sudo apt-get update -qq >/dev/null 2>&1 && sudo apt-get install -y -qq jq zstd >/dev/null 2>&1) || true
command -v zstd >/dev/null || (pip install -q zstandard 2>/dev/null && echo "zstd: using python zstandard fallback")
log "elan (binary from GitHub releases; no toolchain yet)"
if ! command -v elan >/dev/null; then curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --no-modify-path --default-toolchain none; fi
# Toolchains: elan normally downloads from releases.lean-lang.org, which cloud environments do not allow by default; the same
# archives are GitHub release assets (allowed), so fetch those and register them with `elan toolchain link`.
link_toolchain() {  # $1 = version tag like v4.34.1
  local v="$1" name="leanprover/lean4:$1" dir="$HOME/.elan/toolchains/leanprover--lean4---$1"
  if elan toolchain list 2>/dev/null | grep -q "lean4---$v"; then echo "toolchain $v present"; return 0; fi
  local arch; arch=$(uname -m); case "$arch" in x86_64) a=linux;; aarch64|arm64) a=linux_aarch64;; esac   # release assets: lean-<v>-linux.tar.zst / -linux_aarch64
  mkdir -p "$dir" && curl -fsSL -o "/tmp/lean-$v.tar.zst" "https://github.com/leanprover/lean4/releases/download/$v/lean-${v#v}-$a.tar.zst" || { echo "download failed for $v"; return 1; }
  if command -v zstd >/dev/null; then tar --zstd -xf "/tmp/lean-$v.tar.zst" -C "$dir" --strip-components=1
  else python3 -c "import zstandard,sys,tarfile; d=zstandard.ZstdDecompressor(); f=open(sys.argv[1],'rb'); tarfile.open(fileobj=d.stream_reader(f), mode='r|').extractall(sys.argv[2])" "/tmp/lean-$v.tar.zst" "/tmp/lean-$v-x" && mv "/tmp/lean-$v-x"/*/* "$dir"/; fi
  rm -f "/tmp/lean-$v.tar.zst"; elan toolchain link "$name" "$dir" && echo "linked $name"
}
link_toolchain v4.34.1 && elan default leanprover/lean4:v4.34.1 2>&1 | tail -1
elan show 2>&1 | grep -E "default|active" | head -3
( cd "$HOME" && lean --version ) || { echo "SETUP_FAILED: lean not runnable from a directory without lean-toolchain"; }

log "openai/math @ $COMMIT (sparse: lean/ only, ~1.7 GB)"
if [ ! -f "$UP/lean/lakefile.lean" ]; then
  rm -rf "$UP"; git clone -q --filter=blob:none --no-checkout https://github.com/openai/math "$UP"
  git -C "$UP" sparse-checkout set lean && git -C "$UP" checkout -q "$COMMIT"
fi
git -C "$UP" rev-parse HEAD

log "landrun (Landlock sandbox used by Comparator)"
if ! command -v landrun >/dev/null; then
  arch=$(uname -m); case "$arch" in x86_64) a=x86_64;; aarch64|arm64) a=arm64;; *) a=$arch;; esac
  case "$a" in x86_64) la=amd64;; *) la=arm64;; esac
  url="https://github.com/Zouuup/landrun/releases/latest/download/landrun-linux-$la"   # no api.github.com: the cloud GitHub proxy only serves attached repos
  curl -fsSL -o /tmp/landrun "$url" && install -m755 /tmp/landrun "$HOME/.local/bin/landrun" && echo "landrun from $url"
  if ! command -v landrun >/dev/null && command -v go >/dev/null; then GOBIN="$HOME/.local/bin" go install github.com/zouuup/landrun/cmd/landrun@latest; fi
fi
LANDRUN_STATUS="unavailable"
if command -v landrun >/dev/null; then
  # the same flag shape Comparator uses: read-only root, exec on the system dirs
  if landrun --ro / --rox /usr --rox /bin --rox /lib --rox /lib64 -- /bin/true 2>/tmp/landrun.err; then LANDRUN_STATUS="real ($(landrun --version 2>&1 | head -1), full ABI)"
  elif landrun --best-effort --ro / --rox /usr --rox /bin --rox /lib --rox /lib64 -- /bin/true 2>/tmp/landrun2.err; then LANDRUN_STATUS="real with --best-effort ($(landrun --version 2>&1 | head -1); $(grep -o 'Got Landlock ABI v[0-9]*' /tmp/landrun.err | head -1))"
  else LANDRUN_STATUS="installed but Landlock unusable: $(head -c 300 /tmp/landrun2.err)"; fi
fi
echo "LANDRUN_STATUS=$LANDRUN_STATUS"

log "lean4export and comparator (pinned to the commits used on the maintainer's machine)"
cd "$ROOT/tmp"
[ -d lean4export ] || git clone -q https://github.com/leanprover/lean4export
[ -d comparator ] || git clone -q https://github.com/leanprover/comparator
( cd lean4export && (git checkout -q 076e8e5 2>/dev/null || { git fetch -q --all --tags; git checkout -q 076e8e5; })
  echo "leanprover/lean4:v4.34.1" > lean-toolchain     # the exporter must be built with the clone's own Lean to read its .olean files
  echo "lean4export at $(git rev-parse --short HEAD), building with $(cat lean-toolchain)"; lake build 2>&1 | tail -2 )
( cd comparator && (git checkout -q ca04cfc 2>/dev/null || { git fetch -q --all; git checkout -q ca04cfc; })
  tc=$(sed 's/.*://' lean-toolchain); echo "comparator at $(git rev-parse --short HEAD), toolchain $tc"; link_toolchain "$tc"; lake build 2>&1 | tail -2 )
SETUP_OK=1
for b in "$ROOT/tmp/lean4export/.lake/build/bin/lean4export" "$ROOT/tmp/comparator/.lake/build/bin/comparator"; do
  if [ -x "$b" ]; then echo "OK $b"; else echo "SETUP_FAILED: missing $b"; SETUP_OK=0; fi
done

log "Mathlib cache"
MIRROR="${MATHVET_CACHE_MIRROR:-https://github.com/mathvet/mathvet/releases/download/mathlib-cache-d13f23b/mathlib-cache-d13f23b.tar}"
if [ -z "${MATHLIB_CACHE_GET_URL:-}" ] && ! curl -fsS -m 15 -o /dev/null https://cache.mathlib.org/ 2>/dev/null && [ ! -d "$HOME/.cache/mathlib" ]; then
  log "cache.mathlib.org unreachable; fetching the mirror tarball (458 MB) from GitHub releases"
  mkdir -p "$HOME/.cache" && curl -fL -o /tmp/mathlib-cache.tar "$MIRROR" && tar -xf /tmp/mathlib-cache.tar -C "$HOME/.cache" && rm -f /tmp/mathlib-cache.tar
  echo "mirror files: $(ls "$HOME/.cache/mathlib" | wc -l)"
fi
cd "$UP/lean" && lake exe cache get 2>&1 | tail -3

log "machine report"
{ echo "date=$(date -u +%FT%TZ)"; uname -a; nproc; free -g | head -2; df -h "$ROOT" | tail -1; cat /sys/kernel/security/lsm 2>/dev/null | sed 's/^/lsm=/'; echo "LANDRUN_STATUS=$LANDRUN_STATUS"; (cd "$UP/lean" && lean --version); echo "SETUP_OK=${SETUP_OK:-0}"; echo "session=https://claude.ai/code/${CLAUDE_CODE_REMOTE_SESSION_ID/#cse_/session_}"; } | tee "$ROOT/tmp/cloud-machine.txt"
[ "${SETUP_OK:-0}" = 1 ] && log "setup done (SETUP_OK=1)" || log "setup finished with failures (SETUP_OK=0)"
