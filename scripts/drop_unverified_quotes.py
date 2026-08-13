#!/usr/bin/env python3
"""Drop quotes that are not verbatim against the raw captions.

Idempotent and re-runnable: re-verifies every quote each time, so it can be run
again after new talks are distilled. Dropped quotes are recorded in
data/passA/_dropped_quotes.json rather than discarded silently.

Filler elision is tolerated — the model routinely drops "um"/"uh" and YouTube's
own sound annotations ("[clears throat]") from otherwise-verbatim spans, and
those are not fabrications. Anything beyond that is dropped, because these
quotes get published attributed to named people.

  python3 scripts/drop_unverified_quotes.py --dry-run
  python3 scripts/drop_unverified_quotes.py
"""
import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_quotes import norm, caption_words  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASSA = os.path.join(ROOT, "data", "passA")
DROPPED = os.path.join(PASSA, "_dropped_quotes.json")

FILLER = {"um", "uh", "erm", "mhm"}
SOUND = re.compile(r"\[(?:clears throat|snorts|music|laughter|applause|sighs|coughs)\]")


def strip_filler(s):
    return " ".join(w for w in norm(SOUND.sub(" ", s)).split() if w not in FILLER)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with open(os.path.join(ROOT, "data", "index.json")) as fh:
        vid = {r["slug"]: r["video_id"] for r in json.load(fh)}

    dropped, kept, total = [], 0, 0
    for path in sorted(glob.glob(os.path.join(PASSA, "*.json"))):
        if os.path.basename(path).startswith(("_", ".")):
            continue
        with open(path) as fh:
            env = json.load(fh)
        slug = env["_meta"]["slug"]
        caps = caption_words(vid[slug])
        if caps is None:
            print(f"  SKIP {slug}: no captions")
            continue
        fcaps = strip_filler(caps)

        keep = []
        for q in env["passA"].get("notable_quotes") or []:
            total += 1
            t = q.get("text", "")
            if norm(t) in caps or strip_filler(t) in fcaps:
                keep.append(q)
            else:
                dropped.append({"slug": slug, "timestamp_sec": q.get("timestamp_sec"),
                                "text": t, "why": q.get("why")})
        kept += len(keep)
        n_dropped = len(env["passA"].get("notable_quotes") or []) - len(keep)
        if n_dropped and not args.dry_run:
            env["passA"]["notable_quotes"] = keep
            env.setdefault("_meta", {})["quotes_dropped"] = (
                env["_meta"].get("quotes_dropped", 0) + n_dropped)
            tmp = path + ".tmp"
            with open(tmp, "w") as fh:
                json.dump(env, fh, indent=2)
            os.replace(tmp, path)

    print(f"{total} quotes checked | {kept} kept | {len(dropped)} dropped "
          f"({kept/total*100:.2f}% retained)")
    for d in dropped:
        print(f"  [{d['slug']}] {d['text'][:110]}")
    if not args.dry_run and dropped:
        with open(DROPPED, "w") as fh:
            json.dump(dropped, fh, indent=2)
        print(f"\nrecorded -> {os.path.relpath(DROPPED, ROOT)}")


if __name__ == "__main__":
    main()
