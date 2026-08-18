#!/usr/bin/env python3
"""Deterministic quote verification for Pass C output. No model involved.

Every `evidence_quote` in a Pass C consensus item must appear verbatim in the
`evidence_talk` slug's Pass A `notable_quotes` (data/passA/<slug>.json). This
checks against Pass A's own output (the same JSON Pass C was given as input),
not the raw captions — Pass A quotes are separately verified against raw
captions by verify_quotes.py, so this checker's only job is to catch Pass C
inventing or mangling a quote it was handed.

Matching is on a normalized word sequence (lowercased, punctuation stripped)
to tolerate light repunctuation, consistent with verify_quotes.py.

  python3 scripts/verify_passC_quotes.py
  python3 scripts/verify_passC_quotes.py --show-failures
  python3 scripts/verify_passC_quotes.py --files data/passC/reward-hacking.json
"""
import argparse
import glob
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASSA = os.path.join(ROOT, "data", "passA")
PASSC = os.path.join(ROOT, "data", "passC")

TRANS = str.maketrans({
    "‘": "'", "’": "'", "“": '"', "”": '"',
    "–": "-", "—": "-", " ": " ", "​": " ",
})


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").translate(TRANS).lower()
    s = s.replace("'", "").replace("’", "")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def load_passA_quotes():
    """slug -> set of normalized notable_quotes texts."""
    cache = {}
    for fn in os.listdir(PASSA):
        if not fn.endswith(".json") or fn.startswith((".", "_")):
            continue
        slug = fn[:-5]
        try:
            env = json.load(open(os.path.join(PASSA, fn)))
        except Exception:
            continue
        passA = env.get("passA") or {}
        cache[slug] = {norm(q.get("text", "")) for q in (passA.get("notable_quotes") or [])}
    return cache


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--show-failures", action="store_true")
    ap.add_argument("--files", nargs="*", help="specific passC json files")
    args = ap.parse_args()

    files = args.files or sorted(
        f for f in glob.glob(os.path.join(PASSC, "*.json"))
        if not os.path.basename(f).startswith(("_", "."))
    )
    if not files:
        print("no Pass C output found", file=sys.stderr)
        return 1

    quotes_by_slug = load_passA_quotes()

    tot = ok = 0
    per_concept = []
    failures = []          # (concept, evidence_talk, evidence_quote, reason)

    for path in files:
        env = json.load(open(path))
        passC = env.get("passC") or {}
        concept = passC.get("concept") or os.path.basename(path)[:-5]
        c_tot = c_ok = 0
        for item in passC.get("consensus") or []:
            eq = item.get("evidence_quote", "")
            if eq == "":
                continue  # empty string explicitly allowed by the prompt when nothing fits
            et = item.get("evidence_talk", "")
            tot += 1
            c_tot += 1
            slug_quotes = quotes_by_slug.get(et)
            if slug_quotes is None:
                failures.append((concept, et, eq, "unknown_talk_slug"))
                continue
            if norm(eq) in slug_quotes:
                ok += 1
                c_ok += 1
            else:
                failures.append((concept, et, eq, "not_found_in_passA_quotes"))
        per_concept.append((concept, c_ok, c_tot))

    print(f"concepts checked: {len(per_concept)}")
    print(f"evidence_quotes verbatim: {ok}/{tot}" + (f"  ({ok/tot*100:.1f}%)" if tot else "  (no non-empty quotes)"))
    bad = [p for p in per_concept if p[1] != p[2]]
    print(f"concepts with all evidence_quotes verbatim: {len(per_concept) - len(bad)}/{len(per_concept)}")
    for concept, c_ok, c_tot in bad:
        print(f"  {concept}: {c_ok}/{c_tot}")
    if failures:
        print(f"\n*** {len(failures)} FAILED / UNVERIFIABLE QUOTE(S) — POSSIBLE FABRICATION ***")
        for concept, et, eq, reason in failures:
            print(f"  [{concept}] talk={et} reason={reason}\n    {eq!r}")
    elif args.show_failures:
        print("no failures.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
