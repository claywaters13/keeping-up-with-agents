#!/usr/bin/env python3
"""Pass C batch runner: per-concept synthesis from Pass A JSON (not raw transcripts).

For each canonical concept, gathers every tagged talk's full position list and
verified quotes from data/passA/*.json, builds a JSON payload, and asks
claude -p to synthesize state-of-practice / consensus / disagreements /
practical guidance / outliers / maturity. Resumable, bounded concurrency,
atomic writes. Model access is subscription-only via `claude -p`; no
Anthropic API key is used or required.

  python3 scripts/run_passC.py --concepts "agent harness design,reward hacking,llm-as-a-judge"
  python3 scripts/run_passC.py --min-talks 5   # skip thin concepts
  python3 scripts/run_passC.py                 # run everything, largest first
"""
import argparse
import json
import os
import re
import signal
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "data", "index.json")
PASSA = os.path.join(ROOT, "data", "passA")
CONCEPTS_DIR = os.path.join(ROOT, "data", "concepts")
CONCEPT_TALKS = os.path.join(CONCEPTS_DIR, "concept_talks.json")
CANONICAL = os.path.join(CONCEPTS_DIR, "canonical.json")
PROMPT = os.path.join(ROOT, "scripts", "passC_prompt.md")
OUTDIR = os.path.join(ROOT, "data", "passC")

# Added 2026-08-13 after Clay's pilot review: two of the pilot's disagreements
# rested on a single talk per side (a juxtaposition, not a field-level
# disagreement). Appended after the prompt file (which stays unmodified per
# the project's "read it, do not rewrite it" convention) rather than edited
# into scripts/passC_prompt.md.
DISAGREEMENT_ADDENDUM = """
## Additional guidance (added 2026-08-13, post-pilot)

A disagreement backed by only one talk on each side is a juxtaposition, not a
field-level disagreement -- two people can differ without the field being
divided. Prefer disagreements where at least one side has 2+ distinct talks.
If a concept only yields 1-vs-1 tensions, it is fine to return fewer
disagreements (or none) rather than padding with single-talk juxtapositions.
This does not relax rule 2 for `consensus` (still 3+ distinct talks required).
"""

REQUIRED_KEYS = {
    "concept", "state_of_practice", "consensus", "disagreements",
    "practical_guidance", "notable_outliers", "maturity", "maturity_rationale",
}

CMD = [
    "claude", "-p",
    "--model", "claude-opus-5",
    "--output-format", "json",
    "--allowedTools", "",
    "--strict-mcp-config",
    "--setting-sources", "",
]

stop = threading.Event()
_log_lock = threading.Lock()
_print_lock = threading.Lock()
_procs = set()
_procs_lock = threading.Lock()


def kill_inflight():
    with _procs_lock:
        live = list(_procs)
    for p in live:
        try:
            p.kill()
        except Exception:
            pass


def log(msg):
    with _print_lock:
        print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return re.sub(r"-+", "-", s)


def extract_json(text):
    """Model output -> dict. Tolerates ```json fences and stray prose."""
    t = (text or "").strip()
    if t.startswith("```"):
        t = re.sub(r"^```(?:json)?\s*", "", t)
        t = re.sub(r"\s*```$", "", t.strip())
    try:
        return json.loads(t)
    except Exception:
        pass
    i, j = t.find("{"), t.rfind("}")
    if i != -1 and j > i:
        try:
            return json.loads(t[i:j + 1])
        except Exception:
            return None
    return None


def done(slug, outdir=None):
    """A concept counts as done only if its saved envelope holds parseable,
    schema-complete Pass C JSON."""
    path = os.path.join(outdir or OUTDIR, f"{slug}.json")
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return False
    try:
        with open(path) as fh:
            env = json.load(fh)
    except Exception:
        return False
    passC = env.get("passC")
    return isinstance(passC, dict) and REQUIRED_KEYS.issubset(passC.keys())


def build_payload(concept_rec, talk_slugs, by_slug, passa_cache):
    """concept_rec: {"concept":..,"definition":..}. Returns (payload_dict, missing_slugs)."""
    talks = []
    missing = []
    for s in talk_slugs:
        d = passa_cache.get(s)
        if d is None:
            missing.append(s)
            continue
        rec = by_slug.get(s, {})
        quotes = [
            {"quote": q.get("text", ""), "timestamp_sec": q.get("timestamp_sec")}
            for q in (d.get("notable_quotes") or [])
        ]
        talks.append({
            "slug": s,
            "title": rec.get("title", ""),
            "speakers": rec.get("speakers", []),
            "org": rec.get("org", ""),
            "track": rec.get("track", ""),
            "url": rec.get("url", ""),
            "positions": d.get("positions") or [],
            "quotes": quotes,
        })
    payload = {
        "concept": {"name": concept_rec["concept"], "definition": concept_rec.get("definition", "")},
        "talks": talks,
    }
    return payload, missing


def run_one(concept_rec, talk_slugs, by_slug, passa_cache, timeout, outdir=None):
    outdir = outdir or OUTDIR
    logdir = os.path.join(outdir, "_logs")
    os.makedirs(logdir, exist_ok=True)
    name = concept_rec["concept"]
    slug = slugify(name)

    payload, missing = build_payload(concept_rec, talk_slugs, by_slug, passa_cache)
    if missing:
        log(f"WARN {slug}: {len(missing)} talks missing Pass A output, skipping them: {missing[:5]}")
    if not payload["talks"]:
        log(f"SKIP {slug}: no talks with Pass A output")
        return {"slug": slug, "concept": name, "ok": False, "error": "no_talks"}

    with open(PROMPT) as fh:
        prompt_text = fh.read()
    stdin_payload = prompt_text + DISAGREEMENT_ADDENDUM + "\n" + json.dumps(payload)

    env = dict(os.environ)
    env.pop("ANTHROPIC_API_KEY", None)  # subscription auth only

    t0 = time.time()
    proc = subprocess.Popen(
        CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        cwd=ROOT, env=env,
    )
    with _procs_lock:
        _procs.add(proc)
    try:
        out, err = proc.communicate(stdin_payload.encode(), timeout=timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.communicate()
        log(f"TIMEOUT {slug} after {timeout}s")
        return {"slug": slug, "concept": name, "ok": False, "error": "timeout",
                "wall_sec": round(time.time() - t0, 1), "talk_count": len(payload["talks"])}
    finally:
        with _procs_lock:
            _procs.discard(proc)
    wall = time.time() - t0

    if err:
        with open(os.path.join(logdir, f"{slug}.err"), "wb") as fh:
            fh.write(err)

    if proc.returncode != 0:
        log(f"FAIL rc={proc.returncode} {slug} ({wall:.0f}s)")
        return {"slug": slug, "concept": name, "ok": False, "error": f"rc={proc.returncode}",
                "wall_sec": round(wall, 1), "talk_count": len(payload["talks"])}

    try:
        envelope = json.loads(out.decode())
    except Exception as e:
        log(f"FAIL unparseable envelope {slug}: {e}")
        return {"slug": slug, "concept": name, "ok": False, "error": "bad_envelope",
                "wall_sec": round(wall, 1), "talk_count": len(payload["talks"])}

    if envelope.get("is_error"):
        log(f"FAIL is_error {slug}: {str(envelope.get('result'))[:120]}")
        return {"slug": slug, "concept": name, "ok": False, "error": "is_error",
                "wall_sec": round(wall, 1), "talk_count": len(payload["talks"])}

    passC = extract_json(envelope.get("result") or "")
    if passC is None or not REQUIRED_KEYS.issubset(passC.keys() if isinstance(passC, dict) else {}):
        with open(os.path.join(logdir, f"{slug}.badjson.json"), "w") as fh:
            json.dump(envelope, fh)
        log(f"FAIL bad/incomplete model JSON {slug}")
        return {"slug": slug, "concept": name, "ok": False, "error": "bad_model_json",
                "wall_sec": round(wall, 1), "talk_count": len(payload["talks"])}

    u = envelope.get("usage") or {}
    tokens_in = (u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
                 + u.get("cache_read_input_tokens", 0))
    tokens_out = u.get("output_tokens", 0)

    envelope["passC"] = passC
    envelope["_meta"] = {
        "concept": name,
        "slug": slug,
        "talk_count": len(payload["talks"]),
        "missing_talks": missing,
        "wall_sec": round(wall, 1),
        "run_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }

    tmp = os.path.join(outdir, f".{slug}.tmp")
    with open(tmp, "w") as fh:
        json.dump(envelope, fh, indent=2)
    os.replace(tmp, os.path.join(outdir, f"{slug}.json"))  # atomic: no half files

    row = {
        "slug": slug, "concept": name, "ok": True, "wall_sec": round(wall, 1),
        "talk_count": len(payload["talks"]),
        "tokens_in": tokens_in, "tokens_out": tokens_out,
        "cache_read": u.get("cache_read_input_tokens", 0),
        "cache_creation": u.get("cache_creation_input_tokens", 0),
        "cost_usd": envelope.get("total_cost_usd"),
        "consensus": len(passC.get("consensus") or []),
        "disagreements": len(passC.get("disagreements") or []),
        "maturity": passC.get("maturity"),
        "run_at": envelope["_meta"]["run_at"],
    }
    log(f"OK {slug} ({row['talk_count']} talks) {wall:.0f}s in={tokens_in} out={tokens_out} "
        f"${row['cost_usd']:.3f} consensus={row['consensus']} disagreements={row['disagreements']} "
        f"maturity={row['maturity']}")
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--concurrency", type=int, default=2)
    ap.add_argument("--minutes", type=float, default=0,
                    help="stop launching new concepts after this many minutes (0 = no limit)")
    ap.add_argument("--grace", type=float, default=300)
    ap.add_argument("--timeout", type=int, default=900, help="per-call timeout (s)")
    ap.add_argument("--limit", type=int, default=0, help="max concepts this run (0 = all)")
    ap.add_argument("--min-talks", type=int, default=0,
                    help="skip concepts with fewer than this many tagged talks")
    ap.add_argument("--outdir", help="write elsewhere than data/passC")
    ap.add_argument("--concepts", help="comma-separated concept names to run instead of the full queue")
    args = ap.parse_args()

    outdir = args.outdir or OUTDIR
    runlog = os.path.join(outdir, "_runlog.jsonl")
    os.makedirs(outdir, exist_ok=True)
    os.makedirs(os.path.join(outdir, "_logs"), exist_ok=True)

    with open(INDEX) as fh:
        by_slug = {r["slug"]: r for r in json.load(fh)}
    with open(CONCEPT_TALKS) as fh:
        concept_talks = json.load(fh)
    with open(CANONICAL) as fh:
        canonical = {c["concept"]: c for c in json.load(fh)["canonical"]}

    # preload all Pass A output once (shared across concepts, talks repeat across concepts)
    passa_cache = {}
    for fn in os.listdir(PASSA):
        if not fn.endswith(".json") or fn.startswith((".", "_")):
            continue
        slug = fn[:-5]
        try:
            with open(os.path.join(PASSA, fn)) as fh:
                env = json.load(fh)
            if isinstance(env.get("passA"), dict):
                passa_cache[slug] = env["passA"]
        except Exception:
            continue
    log(f"loaded {len(passa_cache)} Pass A outputs")

    concept_names = list(concept_talks.keys())
    if args.concepts:
        want = [c.strip() for c in args.concepts.split(",") if c.strip()]
        missing_c = [c for c in want if c not in concept_talks]
        if missing_c:
            log(f"unknown concepts requested: {missing_c}")
        concept_names = [c for c in want if c in concept_talks]

    # sort by talk count descending (prioritize highest-leverage concepts)
    concept_names.sort(key=lambda c: len(concept_talks[c]), reverse=True)

    if args.min_talks:
        concept_names = [c for c in concept_names if len(concept_talks[c]) >= args.min_talks]

    queue = []
    for name in concept_names:
        slug = slugify(name)
        if done(slug, outdir):
            continue
        crec = canonical.get(name, {"concept": name, "definition": ""})
        queue.append((crec, concept_talks[name]))

    skipped_done = sum(1 for name in concept_names if done(slugify(name), outdir))
    if args.limit:
        queue = queue[:args.limit]

    log(f"{len(concept_names)} concepts in scope | {skipped_done} already done | "
        f"{len(queue)} queued | concurrency={args.concurrency} | "
        f"outdir={os.path.relpath(outdir, ROOT)}")

    deadline = time.time() + args.minutes * 60 if args.minutes else None
    if deadline:
        log(f"launch deadline in {args.minutes:g} min, then up to {args.grace:g}s grace")

    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, lambda *_: (stop.set(), log("stop requested; draining")))

    t0 = time.time()
    results = []

    def worker(crec, talk_slugs):
        if stop.is_set() or (deadline and time.time() >= deadline):
            return None
        row = run_one(crec, talk_slugs, by_slug, passa_cache, args.timeout, outdir)
        with _log_lock:
            with open(runlog, "a") as fh:
                fh.write(json.dumps(row) + "\n")
        return row

    pool = ThreadPoolExecutor(max_workers=args.concurrency)
    futs = [pool.submit(worker, crec, talk_slugs) for crec, talk_slugs in queue]
    if deadline:
        while time.time() < deadline and not stop.is_set():
            if all(f.done() for f in futs):
                break
            time.sleep(1)
        stop.set()
        log("deadline reached; no new launches, draining in-flight")
        drain_until = time.time() + args.grace
        while time.time() < drain_until and not all(f.done() for f in futs):
            time.sleep(1)
        if not all(f.done() for f in futs):
            log("grace expired; killing in-flight calls (their concepts stay unfinished)")
            kill_inflight()
            time.sleep(5)
    else:
        while not all(f.done() for f in futs):
            if stop.is_set():
                break
            time.sleep(1)
    pool.shutdown(wait=False, cancel_futures=True)
    for f in futs:
        if f.done() and not f.cancelled():
            try:
                r = f.result()
            except Exception as e:
                log(f"worker exception: {e}")
                continue
            if r:
                results.append(r)

    ok = [r for r in results if r.get("ok")]
    fail = [r for r in results if not r.get("ok")]
    elapsed = time.time() - t0
    log(f"done: {len(ok)} ok, {len(fail)} failed, {elapsed/60:.1f} min elapsed")
    if ok:
        n = len(ok)
        log(f"per-concept avg: in={sum(r['tokens_in'] for r in ok)/n:,.0f} "
            f"out={sum(r['tokens_out'] for r in ok)/n:,.0f} "
            f"wall={sum(r['wall_sec'] for r in ok)/n:.0f}s "
            f"cost=${sum(r['cost_usd'] for r in ok)/n:.3f}")
    if fail:
        log("failures: " + ", ".join(f"{r['slug']}({r['error']})" for r in fail))
    os._exit(0)


if __name__ == "__main__":
    main()
