#!/usr/bin/env python3
"""Phase 2: assign every raw concept string to a canonical concept, or DROP.

Phase 1 (data/concepts/canonical.json) already aliased 1,067 raw strings; those
assignments are authoritative and free. This pass only handles the remainder,
batched and run in parallel, resumable per batch.

  python3 scripts/run_conceptsB.py --batch-size 100 --concurrency 3
  python3 scripts/run_conceptsB.py --merge-only
"""
import argparse
import json
import os
import re
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CDIR = os.path.join(ROOT, "data", "concepts")
BATCHDIR = os.path.join(CDIR, "assign")

CMD = ["claude", "-p", "--model", "claude-opus-5", "--output-format", "json",
       "--allowedTools", "", "--strict-mcp-config", "--setting-sources", ""]

_print_lock = threading.Lock()


def log(m):
    with _print_lock:
        print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


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


def build_prompt(vocab, batch):
    lines = [
        "You are assigning raw concept strings to a fixed canonical vocabulary for a wiki "
        "of 228 AI Engineer World's Fair 2026 talks.",
        "",
        "The canonical vocabulary is FIXED. Do not invent, rename, or split concepts. Every "
        "raw string maps to exactly one canonical concept, or to DROP.",
        "",
        "## Canonical vocabulary", "",
    ]
    for c in vocab["canonical"]:
        lines.append(f"- **{c['concept']}** [{c['tier']}] — {c['definition']}")
    lines += ["", "## When to DROP", ""]
    lines += [f"- {g}" for g in vocab.get("drop_guidance", [])]
    if vocab.get("notes"):
        lines += ["", "## Disambiguation rules from the vocabulary author", "",
                  vocab["notes"]]
    lines += [
        "", "## Task", "",
        "For each raw string below, return the canonical concept it belongs to, or \"DROP\".",
        "",
        "Return ONLY a JSON object, no prose:",
        "",
        '{ "assignments": [ {"raw": "<string exactly as given>", '
        '"concept": "<canonical concept, or DROP>"} ] }',
        "",
        "Rules:",
        "- `raw` must be copied EXACTLY as given, including hyphens and spacing.",
        "- `concept` must be a canonical concept spelled exactly as listed above, or DROP.",
        "- Return one entry for every raw string. Do not skip any. Do not add extras.",
        "- Prefer the most specific canonical concept that genuinely covers the string.",
        "- DROP is correct for one-off implementation trivia, talk-craft, narrow domain "
        "minutiae, and strings that only make sense with one talk's context restored. "
        "Do not force a bad fit just to avoid DROP.",
        "",
        "## Raw strings", "",
    ]
    lines += [f"- {s}" for s in batch]
    return "\n".join(lines) + "\n"


def run_batch(i, vocab, batch, timeout):
    out_path = os.path.join(BATCHDIR, f"batch_{i:03d}.json")
    if os.path.exists(out_path):
        try:
            d = json.load(open(out_path))
            if len(d.get("assignments") or []) == len(batch):
                return ("cached", i, len(batch))
        except Exception:
            pass
    env = dict(os.environ)
    env.pop("ANTHROPIC_API_KEY", None)
    t0 = time.time()
    p = subprocess.Popen(CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, cwd=ROOT, env=env)
    try:
        out, err = p.communicate(build_prompt(vocab, batch).encode(), timeout=timeout)
    except subprocess.TimeoutExpired:
        p.kill(); p.communicate()
        log(f"batch {i}: TIMEOUT")
        return ("timeout", i, 0)
    if p.returncode != 0:
        log(f"batch {i}: rc={p.returncode} {err[:200].decode(errors='ignore')}")
        return ("fail", i, 0)
    env_json = json.loads(out.decode())
    if env_json.get("is_error"):
        log(f"batch {i}: is_error")
        return ("fail", i, 0)
    res = extract_json(env_json.get("result"))
    if not res or "assignments" not in res:
        log(f"batch {i}: unparseable")
        return ("fail", i, 0)
    res["_cost_usd"] = env_json.get("total_cost_usd")
    tmp = out_path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(res, fh, indent=2)
    os.replace(tmp, out_path)
    got = len(res["assignments"])
    log(f"batch {i}: {got}/{len(batch)} assigned in {time.time()-t0:.0f}s "
        f"(${env_json.get('total_cost_usd', 0):.3f})")
    return ("ok", i, got)


def merge(vocab, raw_counts):
    """Combine phase-1 aliases with phase-2 batches; validate; write mapping.json."""
    canon = {c["concept"] for c in vocab["canonical"]}
    mapping, source = {}, {}
    for c in vocab["canonical"]:
        for a in c.get("aliases", []):
            mapping[a] = c["concept"]
            source[a] = "phase1_alias"
        # the canonical label itself, when it appears verbatim in the raw list
        if c["concept"] in raw_counts:
            mapping[c["concept"]] = c["concept"]
            source[c["concept"]] = "phase1_alias"

    invented, missing = [], []
    for path in sorted(os.listdir(BATCHDIR)) if os.path.isdir(BATCHDIR) else []:
        if not path.startswith("batch_"):
            continue
        d = json.load(open(os.path.join(BATCHDIR, path)))
        for a in d.get("assignments", []):
            raw, con = a.get("raw", "").strip(), (a.get("concept") or "").strip()
            if raw not in raw_counts:
                continue  # model altered the string; the unassigned check will catch it
            if con != "DROP" and con not in canon:
                invented.append((raw, con)); continue
            if raw not in mapping:
                mapping[raw] = con
                source[raw] = "phase2"

    unassigned = [r for r in raw_counts if r not in mapping]
    kept = {k: v for k, v in mapping.items() if v != "DROP"}
    dropped = [k for k, v in mapping.items() if v == "DROP"]

    out = {"mapping": mapping, "source": source,
           "stats": {"raw_strings": len(raw_counts), "mapped": len(kept),
                     "dropped": len(dropped), "unassigned": len(unassigned),
                     "invented_concepts": len(invented)}}
    with open(os.path.join(CDIR, "mapping.json"), "w") as fh:
        json.dump(out, fh, indent=2)

    print(f"\n{'='*70}\nMERGE + VALIDATION\n{'='*70}")
    print(f"  raw strings:        {len(raw_counts):,}")
    print(f"  mapped to concept:  {len(kept):,}")
    print(f"  dropped:            {len(dropped):,}")
    print(f"  UNASSIGNED:         {len(unassigned):,}" +
          ("  <-- rerun to fix" if unassigned else "  (clean)"))
    print(f"  invented concepts:  {len(invented):,}" +
          ("  <-- rejected" if invented else "  (clean)"))
    if invented[:5]:
        for r, c in invented[:5]:
            print(f"      {r!r} -> {c!r}")
    if unassigned[:8]:
        print("  e.g. unassigned:", unassigned[:8])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-size", type=int, default=100)
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--merge-only", action="store_true")
    args = ap.parse_args()

    os.makedirs(BATCHDIR, exist_ok=True)
    vocab = json.load(open(os.path.join(CDIR, "canonical.json")))
    raw_counts = {}
    for line in open(os.path.join(CDIR, "raw_concepts.tsv")):
        n, s = line.rstrip("\n").split("\t", 1)
        raw_counts[s] = int(n)

    aliased = {a for c in vocab["canonical"] for a in c.get("aliases", [])}
    aliased |= {c["concept"] for c in vocab["canonical"] if c["concept"] in raw_counts}
    todo = [s for s in raw_counts if s not in aliased]
    log(f"{len(raw_counts)} raw | {len(aliased)} already aliased by phase 1 | "
        f"{len(todo)} to assign")

    if not args.merge_only:
        batches = [todo[i:i + args.batch_size]
                   for i in range(0, len(todo), args.batch_size)]
        log(f"{len(batches)} batches of <={args.batch_size}, concurrency={args.concurrency}")
        with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
            results = list(pool.map(
                lambda t: run_batch(t[0], vocab, t[1], args.timeout), enumerate(batches)))
        bad = [r for r in results if r[0] in ("fail", "timeout")]
        log(f"batches: {sum(1 for r in results if r[0]=='ok')} ok, "
            f"{sum(1 for r in results if r[0]=='cached')} cached, {len(bad)} failed")

    merge(vocab, raw_counts)


if __name__ == "__main__":
    main()
