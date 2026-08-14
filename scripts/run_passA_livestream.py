#!/usr/bin/env python3
"""Run Pass A on the newly-identified livestream gap segments in
data/livestream_segments/*.md (output of resegment_order_evidence.py).

Reuses run_passA.run_one() verbatim (same prompt, same subscription-only
claude -p invocation, same atomic-write/fence-stripping/validation logic) by
pointing its TRANSCRIPTS constant at data/livestream_segments instead of
data/transcripts. Writes to data/passA_segments/<slug>.json.

Per-call timeout is 300s (5 min): kill and move on if a call runs long,
rather than let one slow segment hang the whole batch.
"""
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import run_passA  # noqa: E402

SEGDIR = os.path.join(ROOT, "data", "livestream_segments")
OUTDIR = os.path.join(ROOT, "data", "passA_segments")

run_passA.TRANSCRIPTS = SEGDIR  # redirect run_one()'s transcript lookup


def parse_frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" not in line:
                continue
            k, v = line.split(":", 1)
            try:
                fm[k.strip()] = json.loads(v.strip())
            except Exception:
                fm[k.strip()] = v.strip()
    return fm


def main():
    md_files = sorted(f for f in os.listdir(SEGDIR) if f.endswith(".md"))
    records = []
    for f in md_files:
        slug = f[:-3]
        fm = parse_frontmatter(os.path.join(SEGDIR, f))
        records.append({
            "slug": slug, "video_id": fm.get("video_id"),
            "url": fm.get("url"), "word_count": fm.get("word_count"),
        })

    print(f"[{time.strftime('%H:%M:%S')}] {len(records)} livestream segments queued for Pass A")
    os.makedirs(OUTDIR, exist_ok=True)

    results = []
    for rec in records:
        if run_passA.done(rec["slug"], OUTDIR):
            print(f"[{time.strftime('%H:%M:%S')}] SKIP (already done) {rec['slug']}")
            continue
        row = run_passA.run_one(rec, timeout=300, effort=None, outdir=OUTDIR)
        results.append(row)

    ok = [r for r in results if r.get("ok")]
    fail = [r for r in results if not r.get("ok")]
    print(f"\n[{time.strftime('%H:%M:%S')}] Pass A done: {len(ok)} ok, {len(fail)} failed")
    for r in fail:
        print(f"  FAILED {r['slug']}: {r.get('error')}")
    for r in ok:
        print(f"  OK {r['slug']}: {r['wall_sec']}s, ${r['cost_usd']:.3f}, "
              f"{r['quotes']} quotes, {r['positions']} positions")


if __name__ == "__main__":
    main()
