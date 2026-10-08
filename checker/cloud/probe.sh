#!/bin/bash
# Quick (<5 min) measurement of a cloud session VM for a Comparator run: kernel + Landlock, resources, reachability of the
# hosts the setup needs, toolchain install time. Prints a report and writes it to tmp/cloud-probe.txt.
ROOT="${MATHVET_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"; mkdir -p "$ROOT/tmp" "$HOME/.local/bin"
export PATH="$HOME/.elan/bin:$HOME/.local/bin:$PATH"
{
echo "== probe $(date -u +%FT%TZ) session=https://claude.ai/code/${CLAUDE_CODE_REMOTE_SESSION_ID/#cse_/session_}"
echo "-- machine"; uname -a; (. /etc/os-release && echo "$PRETTY_NAME"); echo "nproc=$(nproc) mem=$(free -g | awk '/Mem/{print $2}')G disk_free=$(df -h "$ROOT" | awk 'NR==2{print $4}')"; id -un
echo "-- kernel security"; echo "lsm=$(cat /sys/kernel/security/lsm 2>&1)"; echo "virt=$(systemd-detect-virt 2>&1)"; cat /sys/fs/cgroup/cpu.max /sys/fs/cgroup/memory.max 2>&1 | tr '\n' ' '; echo
echo "-- landrun"; a=$(uname -m); case "$a" in x86_64) la=amd64;; *) la=arm64;; esac
curl -fsSL -o "$HOME/.local/bin/landrun" "https://github.com/Zouuup/landrun/releases/latest/download/landrun-linux-$la" && chmod +x "$HOME/.local/bin/landrun" && echo "downloaded landrun ($(landrun --version 2>&1 | head -1))"
if landrun --best-effort --ro / --rox /usr --rox /bin --rox /lib --rox /lib64 -- /bin/true 2>/tmp/landrun.err; then echo "LANDLOCK=works (best-effort)"; else echo "LANDLOCK=fails: $(head -c 300 /tmp/landrun.err)"; fi
echo "-- reachability"
for u in https://github.com https://api.github.com https://raw.githubusercontent.com https://objects.githubusercontent.com https://release-assets.githubusercontent.com https://releases.lean-lang.org https://cache.mathlib.org https://lakecache.blob.core.windows.net https://reservoir.lean-lang.org https://pypi.org; do printf "%s -> %s\n" "$u" "$(curl -s -o /dev/null -m 15 -w '%{http_code}' "$u" || echo FAIL)"; done
echo "-- toolchain v4.34.1 via GitHub release asset"
T0=$(date +%s); command -v zstd >/dev/null || (apt-get install -y -qq zstd >/dev/null 2>&1 || true)
curl -fL -o /tmp/lean.tar.zst "https://github.com/leanprover/lean4/releases/download/v4.34.1/lean-4.34.1-linux.tar.zst" && mkdir -p /tmp/lean && tar --zstd -xf /tmp/lean.tar.zst -C /tmp/lean --strip-components=1 && /tmp/lean/bin/lean --version; echo "toolchain seconds=$(( $(date +%s) - T0 )) size=$(du -sh /tmp/lean | cut -f1)"
echo "-- mathlib mirror asset reachable"; curl -sI -L -m 20 -o /dev/null -w "mirror HEAD -> %{http_code} %{size_download}\n" https://github.com/mathvet/mathvet/releases/download/mathlib-cache-d13f23b/mathlib-cache-d13f23b.tar.sha256
echo "-- env"; env | grep -i -E 'CLAUDE_CODE_REMOTE|BASH_|TIMEOUT' | sed 's/=.*/=(set)/' | tr '\n' ' '; echo "BASH_DEFAULT_TIMEOUT_MS=$BASH_DEFAULT_TIMEOUT_MS"
echo "-- python benchmark"; python3 -c "
import time; t=time.time(); s=0
for i in range(20_000_000): s+=i*i
print('python 20M loop seconds', round(time.time()-t,2))"
echo "== probe done $(date -u +%FT%TZ)"
} 2>&1 | tee "$ROOT/tmp/cloud-probe.txt"
