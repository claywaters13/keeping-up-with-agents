#!/usr/bin/env python3
"""Build data/concepts/concept_talks.json: canonical concept -> [talk slug, ...].

Deterministic, no model calls. Maps every raw concept string in data/passA/*.json
through data/concepts/mapping.json (produced by run_conceptsB.py), skipping DROP,
and inverts the result. Same file shape as events/aiewf-2026.

  python3 scripts/build_concept_talks.py
"""
import glob
import json
import os
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASSA = os.path.join(ROOT, "data", "passA")
CDIR = os.path.join(ROOT, "data", "concepts")


def main():
    canonical = json.load(open(os.path.join(CDIR, "canonical.json")))["canonical"]
    canon_names = {c["concept"] for c in canonical}
    mapping = json.load(open(os.path.join(CDIR, "mapping.json")))["mapping"]

    concept_talks = defaultdict(set)
    unmapped, dropped_hits, total_hits = set(), 0, 0

    for path in sorted(glob.glob(os.path.join(PASSA, "*.json"))):
        if os.path.basename(path).startswith(("_", ".")):
            continue
        env = json.load(open(path))
        passA = env.get("passA")
        if not isinstance(passA, dict):
            continue
        slug = env["_meta"]["slug"]
        for raw in set(passA.get("concepts") or []):
            raw = (raw or "").strip()
            if not raw:
                continue
            total_hits += 1
            target = mapping.get(raw)
            if target is None:
                unmapped.add(raw)
                continue
            if target == "DROP":
                dropped_hits += 1
                continue
            if target not in canon_names:
                unmapped.add(raw)
                continue
            concept_talks[target].add(slug)

    out = {c: sorted(slugs) for c, slugs in
           sorted(concept_talks.items(), key=lambda kv: (-len(kv[1]), kv[0]))}
    with open(os.path.join(CDIR, "concept_talks.json"), "w") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)

    empty = sorted(canon_names - set(out))
    sizes = sorted((len(v) for v in out.values()), reverse=True)
    print(f"raw concept mentions:      {total_hits}")
    print(f"  mapped:                  {total_hits - dropped_hits - len(unmapped)}")
    print(f"  dropped by vocabulary:   {dropped_hits}")
    print(f"  UNMAPPED:                {len(unmapped)}"
          + ("  <-- rerun run_conceptsB.py" if unmapped else "  (clean)"))
    for u in sorted(unmapped)[:10]:
        print(f"      {u!r}")
    print(f"concepts with >=1 talk:    {len(out)} / {len(canon_names)} canonical")
    if empty:
        print(f"concepts with 0 talks:     {len(empty)} -> {empty}")
    for n in (3, 5):
        print(f"concepts with >={n} talks:   {sum(1 for s in sizes if s >= n)}")
    return 1 if unmapped else 0


if __name__ == "__main__":
    sys.exit(main())
