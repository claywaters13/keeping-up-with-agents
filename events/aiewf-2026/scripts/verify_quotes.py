#!/usr/bin/env python3
"""Deterministic quote verification for Pass A output. No model involved.

Quotes are checked against the RAW CAPTIONS (raw/caps/<video_id>.en.json3,
events[].segs[].utf8 concatenated), never against data/transcripts/*.md — the
markdown interleaves **[M:SS](url)** timestamp markers between paragraphs, so any
quote spanning a paragraph break fails a naive substring match there.

Matching is on a normalized word sequence (lowercased, punctuation stripped,
whitespace collapsed) because the prompt explicitly permits light repunctuation
but forbids adding, removing, or reordering words.

  python3 scripts/verify_quotes.py                 # summary
  python3 scripts/verify_quotes.py --show-failures
"""
import argparse
import glob
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAPS = os.path.join(ROOT, "raw", "caps")
PASSA = os.path.join(ROOT, "data", "passA")

# curly quotes / dashes / nbsp -> ascii, before punctuation is stripped
TRANS = str.maketrans({
    "‘": "'", "’": "'", "“": '"', "”": '"',
    "–": "-", "—": "-", " ": " ", "​": " ",
})


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").translate(TRANS).lower()
    s = s.replace("'", "").replace("’", "")   # dont == don't
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def caption_words(video_id: str):
    path = os.path.join(CAPS, f"{video_id}.en.json3")
    if not os.path.exists(path):
        return None
    with open(path) as fh:
        data = json.load(fh)
    parts = []
    for ev in data.get("events", []):
        for seg in ev.get("segs", []) or []:
            parts.append(seg.get("utf8", ""))
    return norm("".join(parts))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--show-failures", action="store_true")
    ap.add_argument("--files", nargs="*", help="specific passA json files")
    args = ap.parse_args()

    files = args.files or sorted(
        f for f in glob.glob(os.path.join(PASSA, "*.json"))
        if not os.path.basename(f).startswith(("_", "."))
    )
    if not files:
        print("no Pass A output found", file=sys.stderr)
        return 1

    with open(os.path.join(ROOT, "data", "index.json")) as fh:
        vid_by_slug = {r["slug"]: r["video_id"] for r in json.load(fh)}

    tot = ok = 0
    per_talk, failures, missing_caps = [], [], []

    for path in files:
        with open(path) as fh:
            env = json.load(fh)
        passA = env.get("passA")
        if passA is None:
            # bare envelope (e.g. the pilot runs): model JSON still in `result`
            raw = env.get("result") if isinstance(env.get("result"), str) else None
            if raw:
                raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw.strip())
                try:
                    passA = json.loads(raw)
                except Exception:
                    passA = {}
            else:
                passA = env if "notable_quotes" in env else {}
        meta = env.get("_meta") or {}
        slug = meta.get("slug") or os.path.basename(path)[:-5]
        vid = meta.get("video_id") or vid_by_slug.get(slug)
        caps = caption_words(vid) if vid else None
        if caps is None:
            missing_caps.append(slug)
            continue
        quotes = passA.get("notable_quotes") or []
        t_ok = 0
        for q in quotes:
            text = q.get("text", "")
            tot += 1
            if norm(text) and norm(text) in caps:
                ok += 1
                t_ok += 1
            else:
                failures.append((slug, text))
        per_talk.append((slug, t_ok, len(quotes)))

    print(f"talks checked: {len(per_talk)}")
    print(f"quotes verbatim: {ok}/{tot}" + (f"  ({ok/tot*100:.1f}%)" if tot else ""))
    bad = [p for p in per_talk if p[1] != p[2]]
    print(f"talks with all quotes verbatim: {len(per_talk) - len(bad)}/{len(per_talk)}")
    if missing_caps:
        print(f"missing captions: {len(missing_caps)} -> {missing_caps[:5]}")
    for slug, t_ok, n in bad:
        print(f"  {slug}: {t_ok}/{n}")
    if args.show_failures and failures:
        print("\n--- failed quotes ---")
        for slug, text in failures:
            print(f"[{slug}] {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
