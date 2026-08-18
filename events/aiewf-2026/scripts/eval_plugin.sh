#!/usr/bin/env bash
# Deterministic supplement to `claude plugin eval`.
#
# The native eval runner (evals/) covers most of the suite well via LLM graders, but its
# default judge (haiku) does not reliably execute the "grep the corpus to verify this
# quote" instruction we give it in evals/quote-fidelity-reward-hacking/graders/
# quotes_verbatim.md — in a full-suite run it FAILed a response we had already hand-
# verified (via `grep -rl` against wiki/) to be 6/6 verbatim. That's exactly the
# "eval runner's format fights you" case the task anticipated: fall back to a script that
# runs the same prompt and greps for the expected markers itself, with no LLM judgment
# in the loop for the pass/fail call.
#
# What this does:
#   1. Runs the quote-fidelity prompt against the installed aiewf-wiki plugin via `claude -p`
#      (subscription only, no API key).
#   2. Extracts every blockquoted string (`> "..."`) from the response.
#   3. For each quote, greps wiki/ for the normalized word sequence (lowercased,
#      punctuation stripped) — the same normalization approach as
#      scripts/verify_quotes.py, because the model is allowed to repunctuate but not to
#      change words.
#   4. Reports PASS/FAIL per quote and an overall verdict. Any single fabricated quote is
#      a hard FAIL for the whole run — there is no partial credit, matching the task's
#      "any invented quote is a critical failure" bar.
#
# Usage: scripts/eval_plugin.sh [prompt]
# Exit code 0 = every quote verified verbatim, 1 = at least one did not.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROMPT="${1:-Give me exact quotes on reward hacking from the AIEWF 2026 wiki, with attribution.}"
TMP_JSON="$(mktemp)"
trap 'rm -f "$TMP_JSON"' EXIT

echo "== eval_plugin.sh: quote-fidelity deterministic check ==" >&2
echo "Prompt: $PROMPT" >&2
echo >&2

claude -p "$PROMPT" \
  --allowedTools "Skill,Read,Grep,Glob" \
  --strict-mcp-config --setting-sources "user" \
  --output-format json > "$TMP_JSON"

if [ ! -s "$TMP_JSON" ]; then
  echo "FAIL: empty response from claude -p" >&2
  exit 1
fi

python3 "$(dirname "${BASH_SOURCE[0]}")/_verify_quote_fidelity.py" "$REPO_ROOT" "$TMP_JSON"
