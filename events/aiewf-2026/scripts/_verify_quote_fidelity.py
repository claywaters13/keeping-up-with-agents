#!/usr/bin/env python3
"""Helper for scripts/eval_plugin.sh: deterministic quote-fidelity check.

Reads a `claude -p --output-format json` envelope from a file, extracts every
blockquoted string in the response, and greps wiki/ for the normalized word sequence
(lowercased, punctuation stripped) of each — matching scripts/verify_quotes.py's
philosophy that the model may repunctuate but must not change words.

Usage: _verify_quote_fidelity.py <repo_root> <result_json_path>
Exit code 0 = every quote verified verbatim, 1 = at least one did not / no quotes found.
"""
import json
import os
import re
import sys


def normalize(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def normalized_grep(quote: str, wiki_dir: str):
    target = normalize(quote)
    if not target:
        return None
    for root, _, files in os.walk(wiki_dir):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(root, fn)
            try:
                with open(path, encoding="utf-8") as f:
                    content = f.read()
            except OSError:
                continue
            if target in normalize(content):
                return path
    return None


def main():
    repo_root, result_path = sys.argv[1], sys.argv[2]
    with open(result_path, encoding="utf-8") as f:
        d = json.load(f)
    text = d.get("result", "")

    quote_re = re.compile(r'^>\s*[“"](.+?)[”"]\s*$', re.MULTILINE)
    quotes = quote_re.findall(text)

    if not quotes:
        print("FAIL: no blockquoted quotes found in response (expected at least one)")
        sys.exit(1)

    wiki_dir = os.path.join(repo_root, "wiki")
    all_ok = True
    print(f"Found {len(quotes)} quote(s) in response.\n")
    for i, q in enumerate(quotes, 1):
        hit = normalized_grep(q, wiki_dir)
        status = "PASS" if hit else "FAIL"
        if not hit:
            all_ok = False
        short = q if len(q) < 90 else q[:87] + "..."
        print(f'[{status}] quote {i}: "{short}"')
        if hit:
            print(f"       verified in {hit.replace(repo_root + os.sep, '')}")
        else:
            print("       *** NOT FOUND VERBATIM IN wiki/ - possible fabrication ***")
    print()
    if all_ok:
        print(f"OVERALL: PASS - {len(quotes)}/{len(quotes)} quotes verified verbatim")
        sys.exit(0)
    else:
        print("OVERALL: FAIL - at least one quote could not be verified verbatim (CRITICAL)")
        sys.exit(1)


if __name__ == "__main__":
    main()
