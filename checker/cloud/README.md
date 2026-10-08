# checker/cloud — running the real Comparator on a Claude Code cloud session

A cloud session is a fresh Ubuntu 24.04 x86_64 VM (about 4 vCPU, 16 GB RAM, 30 GB disk) that Claude drives for you; there is no
separate compute charge, only model usage. It gives MathVet what the maintainer's laptop cannot: an isolated Linux machine where
Comparator can run with its real `landrun` (Landlock) sandbox, independent of the machine that produced the first-pass review.

- `setup.sh` installs elan + Lean v4.34.1, makes a sparse clone of `openai/math` at the reviewed commit (`lean/` only), installs
  landrun, builds `lean4export` and `comparator`, and fetches the Mathlib cache. Rerunnable. The Mathlib cache host is
  `cache.mathlib.org`, which is not on the cloud environment's default allowlist: add it under **Custom** network access.
- `run.sh <Challenge>...` builds the solution module (resumable), runs the closure comparison and then Comparator, and writes
  `reviews/openai-math/evidence/lean_checks/<Challenge>.comparator.txt` with a provenance header (machine, kernel LSMs, whether
  landrun was real or the no-sandbox shim, tool versions, the session URL) and prints its SHA-256.
- `.claude/settings.json` at the repository root raises the Bash command timeout to two hours in cloud sessions so a long
  `lake build` can run as one foreground command (a paused session would otherwise lose background work).

Only Mathlib-only import cones fit the VM: the external packages are not patched or built here (see `checker/README.md`).
