#!/usr/bin/env python3
"""One-off repair: strip markdown fences from Pass A envelope `result` strings.

Some Pass A runs had the model wrap its JSON output in ```json ... ``` fences.
envelope['passA'] (extracted by run_passA.py's extract_json, which already
tolerates fences) is fine, but envelope['result'] itself is not directly
json.loads-able, which breaks any consumer that reads `result` raw. This
strips the fence from `result` in place, verifies the stripped string parses
and has the required keys, and rewrites the envelope atomically.

Run only after backing up data/passA/ to data/passA.bak-prefence-fix/.
"""
import json
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASSA = os.path.join(ROOT, "data", "passA")
REQUIRED_KEYS = {"summary", "key_points", "notable_quotes", "concepts", "positions", "speaker_org"}

FENCE_RE = re.compile(r"^```(?:json)?\s*\n?(.*?)\n?```\s*$", re.DOTALL)


def strip_fence(s: str):
    m = FENCE_RE.match(s.strip())
    if m:
        return m.group(1)
    return None


def main():
    fixed = []
    skipped_list_form = []
    still_bad = []

    for path in sorted(glob.glob(os.path.join(PASSA, "*.json"))):
        base = os.path.basename(path)
        if base.startswith("_") or base.startswith("."):
            continue
        with open(path) as fh:
            env = json.load(fh)

        if isinstance(env, list):
            skipped_list_form.append(base)
            continue

        result = env.get("result")
        if not isinstance(result, str):
            continue

        try:
            json.loads(result)
            continue  # already parses fine, nothing to do
        except Exception:
            pass

        stripped = strip_fence(result)
        if stripped is None:
            still_bad.append((base, "no_fence_pattern_matched"))
            continue

        try:
            parsed = json.loads(stripped)
        except Exception as e:
            still_bad.append((base, f"stripped_still_bad_json: {e}"))
            continue

        if not isinstance(parsed, dict) or not REQUIRED_KEYS.issubset(parsed.keys()):
            missing = REQUIRED_KEYS - (parsed.keys() if isinstance(parsed, dict) else set())
            still_bad.append((base, f"missing_keys: {missing}"))
            continue

        env["result"] = stripped
        tmp = path + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(env, fh, indent=2)
        os.replace(tmp, path)
        fixed.append(base)

    print(f"fixed: {len(fixed)}")
    for b in fixed:
        print(f"  {b}")
    if skipped_list_form:
        print(f"skipped (list-form envelope): {skipped_list_form}")
    if still_bad:
        print(f"still bad: {len(still_bad)}")
        for b, reason in still_bad:
            print(f"  {b}: {reason}")


if __name__ == "__main__":
    main()
