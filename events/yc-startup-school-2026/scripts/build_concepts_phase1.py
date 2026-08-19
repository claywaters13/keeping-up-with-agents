#!/usr/bin/env python3
"""Phase 1: author this event's canonical concept vocabulary, seeded from AIEWF 2026.

SHARED-NAMING CONVENTION (decided 2026-08-19): concept *vocabularies* are shared
across events by name; concept *syntheses* (Pass C) stay per-event. So a concept
that AIEWF 2026 already named keeps AIEWF's exact `concept` string and exact
`definition` here, which makes the two events' wikis joinable on concept name.
New concepts are minted only for ideas AIEWF does not cover.

This does two things:

1. Reads every raw concept string out of data/passA/*.json, counts the talks each
   appears in, and writes data/concepts/raw_concepts.tsv (`count<TAB>concept`,
   frequency descending) -- the same file shape run_conceptsB.py expects.
2. Makes ONE `claude -p` call whose prompt carries (a) those raw strings with
   counts and (b) the full AIEWF canonical vocabulary as REUSE CANDIDATES, and
   writes data/concepts/canonical.json plus the raw envelope for cost accounting.

Model access is subscription-only via `claude -p`; no Anthropic API key is used.

  python3 scripts/build_concepts_phase1.py
  python3 scripts/build_concepts_phase1.py --tsv-only
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASSA = os.path.join(ROOT, "data", "passA")
CDIR = os.path.join(ROOT, "data", "concepts")
AIEWF_CANONICAL = os.path.abspath(
    os.path.join(ROOT, "..", "aiewf-2026", "data", "concepts", "canonical.json"))

CMD = ["claude", "-p", "--model", "claude-opus-5", "--output-format", "json",
       "--allowedTools", "", "--strict-mcp-config", "--setting-sources", ""]

TARGET_MIN, TARGET_MAX = 20, 40


def extract_json(text):
    t = (text or "").strip()
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t.strip())
    try:
        return json.loads(t)
    except Exception:
        i, j = t.find("{"), t.rfind("}")
        if i != -1 and j > i:
            try:
                return json.loads(t[i:j + 1])
            except Exception:
                return None
    return None


def raw_concept_counts():
    """concept string -> number of talks that produced it."""
    counts = Counter()
    n_talks = 0
    for path in sorted(glob.glob(os.path.join(PASSA, "*.json"))):
        if os.path.basename(path).startswith(("_", ".")):
            continue
        env = json.load(open(path))
        passA = env.get("passA")
        if not isinstance(passA, dict):
            continue
        n_talks += 1
        for c in set((passA.get("concepts") or [])):
            c = (c or "").strip()
            if c:
                counts[c] += 1
    return counts, n_talks


def build_prompt(counts, n_talks, aiewf):
    lines = [
        f"You are building the canonical concept vocabulary for a linked wiki of "
        f"{n_talks} talks and firesides from Y Combinator's Startup School 2026 "
        f"(Chase Center, San Francisco, July 25-26, 2026).",
        "",
        "This is a founder-facing event, not an engineering conference. Its subject "
        "matter is company building as much as AI: hiring, fundraising, founder "
        "psychology, iteration speed, hardware and deep tech, go-to-market, AI policy, "
        "design, and AI-era startup strategy -- alongside genuinely technical talks on "
        "robotics, autonomous vehicles, coding agents, and model capability.",
        "",
        "Pass A extracted concepts from each talk independently, so the raw list below "
        "has lexical variants and over-specific one-offs. Your job is to propose the "
        "canonical vocabulary every raw string will later be mapped onto. This "
        "vocabulary IS the wiki's graph: each canonical concept becomes a page linking "
        "the talks that engage it.",
        "",
        "## The shared-naming rule (most important instruction here)",
        "",
        "This wiki is one of several event wikis that share ONE concept vocabulary "
        "across events, so that a reader can follow a concept from one event to "
        "another. A sibling corpus -- the AI Engineer World's Fair 2026 -- has already "
        "authored the vocabulary below.",
        "",
        "For every cluster of raw strings you are about to name:",
        "",
        "1. First check the REUSE CANDIDATES list. If an existing concept already "
        "captures the same idea, **reuse its `concept` name and its `definition` "
        "EXACTLY, character for character**. Do not improve the wording, do not "
        "re-scope the definition, do not re-tier it to your own judgement -- copy "
        "`concept`, `definition` and `tier` verbatim and supply your own `aliases` "
        "and `est_talks`. Mark it `\"reused\": true`.",
        "2. Only when no existing concept covers the idea, mint a new one with your own "
        "name and definition. Mark it `\"reused\": false`.",
        "",
        "Reuse when the IDEA matches, even if this event's speakers use different "
        "words for it. Do NOT reuse when the idea is merely adjacent: a founder-"
        "psychology concept is not the same as an engineering-practice concept just "
        "because both mention 'agents'. Forcing a bad reuse is worse than minting.",
        "",
        "Expect a substantial number of NEW concepts. The AIEWF vocabulary is an "
        "AI-engineering vocabulary and covers company building barely at all, so the "
        "founder-facing themes in this event (hiring, fundraising, conviction and "
        "founder psychology, iteration speed, deep tech and hardware startups, "
        "regulation and policy, design) will mostly need new concepts.",
        "",
        "## Output",
        "",
        "Return ONLY a JSON object, no prose before or after:",
        "",
        "{",
        '  "canonical": [',
        "    {",
        '      "concept": "lowercase noun phrase, the page title",',
        '      "definition": "one sentence, precise enough that someone assigning a raw '
        'string to this concept knows whether it belongs",',
        '      "aliases": ["3-8 raw strings from the list below that should map here"],',
        '      "est_talks": 5,',
        '      "tier": "core | supporting",',
        '      "reused": true,',
        '      "reused_from": "aiewf-2026"',
        "    }",
        "  ],",
        '  "drop_guidance": ["3-6 rules describing which raw strings should be dropped '
        'rather than mapped, with examples from the list"],',
        '  "notes": "anything the assignment pass needs to know: ambiguous boundaries, '
        'concepts you deliberately kept separate, concepts you deliberately merged"',
        "}",
        "",
        "Rules:",
        f"- Target **{TARGET_MIN} to {TARGET_MAX} canonical concepts** for {n_talks} "
        "talks. Optimize for a good graph, not for hitting a number exactly.",
        "- A canonical concept must plausibly cover **3 or more talks**. If it cannot, "
        "fold it into a broader parent or leave it to drop_guidance.",
        '- Mark `tier: "core"` for the roughly 8-12 concepts genuinely central to this '
        "event -- what a reader would browse first. Everything else is `\"supporting\"`. "
        "For a reused concept, copy AIEWF's tier instead of judging it yourself.",
        "- Concepts must be **reusable across talks**, not descriptions of one talk's "
        'work. Prefer "founder hiring bar" over "how Science hires engineers".',
        "- Keep concepts that represent a real **distinction** separate even when "
        "related.",
        "- Avoid vendor and product names as concepts unless the product is genuinely "
        "the subject across multiple talks.",
        '- `reused_from` is `"aiewf-2026"` for reused concepts and omitted (or null) '
        "for new ones.",
        "- `aliases` must be strings copied exactly from the raw list.",
        "",
        "## REUSE CANDIDATES -- the AI Engineer World's Fair 2026 canonical vocabulary",
        "",
        "Format: `concept` [tier] -- definition",
        "",
    ]
    for c in aiewf["canonical"]:
        lines.append(f"- **{c['concept']}** [{c['tier']}] -- {c['definition']}")
    lines += [
        "",
        f"## Raw concept strings from this event's {n_talks} talks",
        "",
        "`count<TAB>concept`, sorted by frequency descending. `count` is the number of "
        "talks that produced that exact string.",
        "",
    ]
    for c, n in counts.most_common():
        lines.append(f"{n}\t{c}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tsv-only", action="store_true")
    ap.add_argument("--timeout", type=int, default=1800)
    args = ap.parse_args()

    os.makedirs(CDIR, exist_ok=True)
    counts, n_talks = raw_concept_counts()
    if not counts:
        print("no Pass A concepts found; run Pass A first", file=sys.stderr)
        return 1

    tsv = os.path.join(CDIR, "raw_concepts.tsv")
    with open(tsv, "w") as fh:
        for c, n in counts.most_common():
            fh.write(f"{n}\t{c}\n")
    print(f"{len(counts)} raw concept strings from {n_talks} talks -> "
          f"{os.path.relpath(tsv, ROOT)}")
    if args.tsv_only:
        return 0

    aiewf = json.load(open(AIEWF_CANONICAL))
    print(f"reuse candidates: {len(aiewf['canonical'])} AIEWF 2026 concepts")

    prompt = build_prompt(counts, n_talks, aiewf)
    env = dict(os.environ)
    env.pop("ANTHROPIC_API_KEY", None)  # subscription auth only

    t0 = time.time()
    p = subprocess.Popen(CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, cwd=ROOT, env=env)
    out, err = p.communicate(prompt.encode(), timeout=args.timeout)
    if p.returncode != 0:
        print(f"rc={p.returncode}: {err.decode(errors='ignore')[:400]}", file=sys.stderr)
        return 1
    envelope = json.loads(out.decode())
    if envelope.get("is_error"):
        print(f"is_error: {str(envelope.get('result'))[:400]}", file=sys.stderr)
        return 1

    vocab = extract_json(envelope.get("result") or "")
    if not vocab or "canonical" not in vocab:
        with open(os.path.join(CDIR, "_phase1_badjson.json"), "w") as fh:
            json.dump(envelope, fh)
        print("unparseable vocabulary JSON", file=sys.stderr)
        return 1

    with open(os.path.join(CDIR, "_phase1_envelope.json"), "w") as fh:
        json.dump(envelope, fh, indent=2)
    with open(os.path.join(CDIR, "canonical.json"), "w") as fh:
        json.dump(vocab, fh, indent=2, ensure_ascii=False)

    reused = [c for c in vocab["canonical"] if c.get("reused")]
    new = [c for c in vocab["canonical"] if not c.get("reused")]
    aiewf_names = {c["concept"] for c in aiewf["canonical"]}
    aiewf_defs = {c["concept"]: c["definition"] for c in aiewf["canonical"]}

    # Verify the reuse claim deterministically rather than trusting the flag.
    bad_reuse = [c["concept"] for c in reused
                 if c["concept"] not in aiewf_names
                 or c.get("definition") != aiewf_defs.get(c["concept"])]
    shadow = [c["concept"] for c in new if c["concept"] in aiewf_names]

    print(f"\n{'='*70}\nPHASE 1 VOCABULARY\n{'='*70}")
    print(f"  concepts:          {len(vocab['canonical'])}")
    print(f"  reused from AIEWF: {len(reused)}")
    print(f"  new to this event: {len(new)}")
    print(f"  drop_guidance:     {len(vocab.get('drop_guidance') or [])}")
    print(f"  wall:              {time.time()-t0:.0f}s   "
          f"cost: ${envelope.get('total_cost_usd', 0):.3f}")
    print(f"  reuse claims that do NOT match AIEWF exactly: {len(bad_reuse)}"
          + ("  <-- FIX" if bad_reuse else "  (clean)"))
    for c in bad_reuse:
        print(f"      {c!r}")
    print(f"  'new' concepts shadowing an AIEWF name: {len(shadow)}"
          + ("  <-- FIX" if shadow else "  (clean)"))
    for c in shadow:
        print(f"      {c!r}")
    if not (TARGET_MIN <= len(vocab["canonical"]) <= TARGET_MAX):
        print(f"  NOTE: {len(vocab['canonical'])} concepts is outside the "
              f"{TARGET_MIN}-{TARGET_MAX} target band")
    return 0


if __name__ == "__main__":
    sys.exit(main())
