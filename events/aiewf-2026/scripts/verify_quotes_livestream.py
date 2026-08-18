#!/usr/bin/env python3
"""Same deterministic quote verification as verify_quotes.py, pointed at the
new livestream-gap Pass A outputs in data/passA_segments/. video_id comes
straight from each envelope's _meta (set by run_passA.run_one), so no
index.json lookup is needed -- these segments aren't in the main 231-talk
corpus index.
"""
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from verify_quotes import caption_words, norm  # noqa: E402

PASSA = os.path.join(ROOT, "data", "passA_segments")


def main():
    files = sorted(
        f for f in glob.glob(os.path.join(PASSA, "*.json"))
        if not os.path.basename(f).startswith(("_", "."))
    )
    if not files:
        print("no Pass A output found in data/passA_segments", file=sys.stderr)
        return 1

    tot = ok = 0
    per_talk, failures, missing_caps = [], [], []

    for path in files:
        with open(path) as fh:
            env = json.load(fh)
        passA = env.get("passA") or {}
        meta = env.get("_meta") or {}
        slug = meta.get("slug") or os.path.basename(path)[:-5]
        vid = meta.get("video_id")
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

    print(f"segments checked: {len(per_talk)}")
    print(f"quotes verbatim: {ok}/{tot}" + (f"  ({ok/tot*100:.1f}%)" if tot else ""))
    bad = [p for p in per_talk if p[1] != p[2]]
    print(f"segments with all quotes verbatim: {len(per_talk) - len(bad)}/{len(per_talk)}")
    if missing_caps:
        print(f"missing captions: {len(missing_caps)} -> {missing_caps}")
    for slug, t_ok, n in bad:
        print(f"  {slug}: {t_ok}/{n}")
    for slug, text in failures:
        print(f"  FAILED [{slug}] {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
