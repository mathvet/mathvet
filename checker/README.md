# checker/ — building and comparing Comparator challenges without trusting anyone

Three layers, strict to lenient in what they need and strong to weak in what they establish:

1. **`comparator_run.sh <Challenge>`** — the real [leanprover/comparator](https://github.com/leanprover/comparator): builds the challenge module and the solution module, exports both with `lean4export`, and runs the Lean kernel on the solution against the challenge statement with only the permitted axioms. "Lean default kernel accepts the solution. Your solution is okay!" is the result we quote. Comparator sandboxes the build with `landrun` (Linux Landlock); on other systems `env.sh` falls back to `fake-landrun.sh`, which runs the identical pipeline **without a sandbox** (it protects the checking machine from an adversarial solution file; it does not change what the kernel accepts). Cite a shim run as such.
2. **`lean_check.sh` + `lean_cmp.sh <Challenge>`** — our own closure comparison (`CmpLib.lean`): build the solution module, re-elaborate the challenge file under a fresh namespace inside the solution's environment, and require that every constant in the transitive closure of the challenge theorems is matched by the same-named solution constant of the same kind with an alpha-equivalent type (and value for definitions, parameter/constructor counts for inductives). A shadowing check elaborates the challenge text against Mathlib alone and requires the printout to be identical to the in-solution copy. `#print axioms` must return only `propext`, `Classical.choice`, `Quot.sound`. This is at least as strict as reading the statement by eye and weaker than Comparator only in the sandbox.
3. Reading the statement against the paper — the fidelity review itself, which no script does.

## Setup
- A clone of the reviewed repository at the reviewed commit at `upstream/openai-math` (or set `OPENAI_MATH_LEAN=/path/to/clone/lean`); `elan`; `jq`; `python3`.
- Mathlib cache: from the clone's `lean/` directory, `lake exe cache get`. **Do not run `lake update`**: the clone pins its external packages and applies compatibility patches through a lakefile hook; see the clone's `lean/patches/`. If a package fails to compile (we hit this with RellichKondrachov), apply the clone's patches by hand with `git apply` inside `.lake/packages/<pkg>`.
- `build_comparator.sh` clones and builds `comparator` and a `lean4export` matching the clone's toolchain under `tmp/`.
- Builds are CPU-bound and can take hours for the largest import cones (`cone_oai_lines` in the challenge table tells you which); the eleven challenges reviewed so far built in 29 s to 6.7 h on an M1 laptop.

## Usage
```sh
checker/run_queue.sh CirculantHadamard MahlerConjecture        # build + closure comparison, logs under reviews/openai-math/evidence/lean_checks/
checker/comparator_run.sh CirculantHadamard                    # the real Comparator
python3 scripts/build_review.py                                # regenerate tables, YAML and the site from the logs
```
