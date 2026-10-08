#!/bin/bash
# Usage: checker/cloud/finish.sh <batch-name>
# Commits everything under reviews/openai-math/evidence/cloud/ to a branch cloud/<batch-name> and pushes it (the cloud
# session's GitHub proxy authenticates the push when the Claude GitHub App is installed on the repository).
set -uo pipefail
ROOT="${MATHVET_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"; B="cloud/$1"
cd "$ROOT" && git config user.name >/dev/null || git config user.name "MathVet cloud run"
git config user.email >/dev/null || git config user.email "cloud@math.vet"
git checkout -q -B "$B" && git add reviews/openai-math/evidence/cloud tmp/cloud-machine.txt 2>/dev/null; git add reviews/openai-math/evidence/cloud
git commit -q -m "cloud evidence: $1 ($(ls reviews/openai-math/evidence/cloud/*.comparator.txt 2>/dev/null | xargs -n1 basename 2>/dev/null | sed 's/.comparator.txt//' | tr '\n' ' '))
Session: https://claude.ai/code/${CLAUDE_CODE_REMOTE_SESSION_ID/#cse_/session_}" && git push -q -u origin "$B" && echo "pushed $B" || echo "nothing to commit or push failed"
git log --oneline -1; git status -sb | head -1
