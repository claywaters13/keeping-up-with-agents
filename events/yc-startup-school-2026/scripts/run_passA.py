#!/usr/bin/env python3
"""Pass A batch runner: transcript -> structured JSON, one `claude -p` call per talk.

Resumable (skips talks that already have valid output), bounded concurrency,
optional wall-clock budget. Model access is subscription-only via `claude -p`;
no Anthropic API key is used or required.

  python3 scripts/run_passA.py --minutes 30 --concurrency 2
  python3 scripts/run_passA.py            # run to completion
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
TRANSCRIPTS = os.path.join(ROOT, "data", "transcripts")
PROMPT = os.path.join(ROOT, "scripts", "passA_prompt.md")
OUTDIR = os.path.join(ROOT, "data", "passA")
LOGDIR = os.path.join(OUTDIR, "_logs")
RUNLOG = os.path.join(OUTDIR, "_runlog.jsonl")

# AIEWF had multi-talk keynote block videos that needed splitting before Pass A
# meant anything. Startup School 2026 publishes one talk per video (31-58 min,
# see raw/vetting_20260819.md), so nothing is skipped here.
SKIP_SLUGS = set()

# scripts/passA_prompt.md is copied verbatim from events/aiewf-2026 and is never
# edited (the project's "read it, do not rewrite it" convention for prompt files).
# Its first line names the AI Engineer World's Fair, which is the wrong event for
# this corpus, so the correction is APPENDED after it rather than edited into it
# -- the same pattern run_passC.py uses for its DISAGREEMENT_ADDENDUM.
EVENT_ADDENDUM = """
## Event correction (this corpus, not AIEWF)

Disregard the opening line's reference to the AI Engineer World's Fair. The talk
below is from **Y Combinator's Startup School 2026** (Chase Center, San Francisco,
July 25-26, 2026): a founder-facing event of stage talks and on-stage firesides.
Everything else in the schema and rules above applies unchanged.

Two consequences for extraction:

- Many of these are **firesides**, where a YC host (Garry Tan, Diana Hu, Harj
  Taggar, Luther Lowe) interviews a guest. `>>` marks a likely speaker change.
  Extract the GUEST's positions and quotes, not the interviewer's questions.
- Concepts here are about **company building** as much as AI engineering: hiring,
  fundraising, founder psychology, iteration speed, hardware and deep tech,
  go-to-market, and AI-era startup strategy. Extract those as readily as technical
  concepts. Do not force a talk into AI-engineering vocabulary it does not use.

Transcript follows.

---

"""

CMD = [
    "claude", "-p",
    "--model", "claude-opus-5",
    "--output-format", "json",
    "--allowedTools", "",
    "--strict-mcp-config",
    "--setting-sources", "",
]

stop = threading.Event()          # set by deadline or signal; blocks new launches
_log_lock = threading.Lock()
_print_lock = threading.Lock()
_procs = set()                    # live children, so the grace timer can kill them
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


def extract_json(text):
    """Model output -> dict. Tolerates ```json fences and stray prose."""
    t = text.strip()
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
    """A talk counts as done only if its saved envelope holds parseable Pass A JSON."""
    path = os.path.join(outdir or OUTDIR, f"{slug}.json")
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return False
    try:
        with open(path) as fh:
            env = json.load(fh)
    except Exception:
        return False
    return isinstance(env.get("passA"), dict)


def run_one(rec, timeout, effort=None, outdir=None):
    outdir = outdir or OUTDIR
    logdir = os.path.join(outdir, "_logs")
    os.makedirs(logdir, exist_ok=True)
    slug = rec["slug"]
    tpath = os.path.join(TRANSCRIPTS, f"{slug}.md")
    if not os.path.exists(tpath):
        log(f"MISSING transcript {slug}")
        return {"slug": slug, "ok": False, "error": "missing_transcript"}

    with open(PROMPT) as fh:
        payload = fh.read()
    payload += EVENT_ADDENDUM
    with open(tpath) as fh:
        payload += fh.read()

    env = dict(os.environ)
    env.pop("ANTHROPIC_API_KEY", None)  # subscription auth only

    cmd = CMD + (["--effort", effort] if effort else [])
    t0 = time.time()
    proc = subprocess.Popen(
        cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        cwd=ROOT, env=env,
    )
    with _procs_lock:
        _procs.add(proc)
    try:
        out, err = proc.communicate(payload.encode(), timeout=timeout)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.communicate()
        log(f"TIMEOUT {slug} after {timeout}s")
        return {"slug": slug, "ok": False, "error": "timeout",
                "wall_sec": round(time.time() - t0, 1)}
    finally:
        with _procs_lock:
            _procs.discard(proc)
    wall = time.time() - t0

    if err:
        with open(os.path.join(logdir, f"{slug}.err"), "wb") as fh:
            fh.write(err)

    if proc.returncode != 0:
        log(f"FAIL rc={proc.returncode} {slug} ({wall:.0f}s)")
        return {"slug": slug, "ok": False, "error": f"rc={proc.returncode}",
                "wall_sec": round(wall, 1)}

    try:
        envelope = json.loads(out.decode())
    except Exception as e:
        log(f"FAIL unparseable envelope {slug}: {e}")
        return {"slug": slug, "ok": False, "error": "bad_envelope",
                "wall_sec": round(wall, 1)}

    if envelope.get("is_error"):
        log(f"FAIL is_error {slug}: {str(envelope.get('result'))[:120]}")
        return {"slug": slug, "ok": False, "error": "is_error",
                "wall_sec": round(wall, 1)}

    passA = extract_json(envelope.get("result") or "")
    if passA is None:
        # Keep the raw envelope for inspection but do NOT mark the talk done.
        with open(os.path.join(logdir, f"{slug}.badjson.json"), "w") as fh:
            json.dump(envelope, fh)
        log(f"FAIL bad model JSON {slug}")
        return {"slug": slug, "ok": False, "error": "bad_model_json",
                "wall_sec": round(wall, 1)}

    u = envelope.get("usage") or {}
    tokens_in = (u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
                 + u.get("cache_read_input_tokens", 0))
    tokens_out = u.get("output_tokens", 0)

    envelope["passA"] = passA
    envelope["_meta"] = {
        "slug": slug,
        "video_id": rec.get("video_id"),
        "url": rec.get("url"),
        "word_count": rec.get("word_count"),
        "wall_sec": round(wall, 1),
        "run_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "effort": effort or "default",
    }

    tmp = os.path.join(outdir, f".{slug}.tmp")
    with open(tmp, "w") as fh:
        json.dump(envelope, fh, indent=2)
    os.replace(tmp, os.path.join(outdir, f"{slug}.json"))  # atomic: no half files

    row = {
        "slug": slug, "ok": True, "wall_sec": round(wall, 1),
        "word_count": rec.get("word_count"),
        "tokens_in": tokens_in, "tokens_out": tokens_out,
        "cache_read": u.get("cache_read_input_tokens", 0),
        "cache_creation": u.get("cache_creation_input_tokens", 0),
        "cost_usd": envelope.get("total_cost_usd"),
        "effort": effort or "default",
        "quotes": len(passA.get("notable_quotes") or []),
        "positions": len(passA.get("positions") or []),
        "run_at": envelope["_meta"]["run_at"],
    }
    log(f"OK {slug} {wall:.0f}s in={tokens_in} out={tokens_out} "
        f"${row['cost_usd']:.3f} quotes={row['quotes']}")
    return row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--concurrency", type=int, default=2)
    ap.add_argument("--minutes", type=float, default=0,
                    help="stop launching new talks after this many minutes (0 = no limit)")
    ap.add_argument("--grace", type=float, default=300,
                    help="seconds to let in-flight calls finish after the deadline")
    ap.add_argument("--timeout", type=int, default=900, help="per-call timeout (s)")
    ap.add_argument("--limit", type=int, default=0, help="max talks this run (0 = all)")
    ap.add_argument("--effort", choices=["low", "medium", "high", "xhigh", "max"],
                    help="thinking effort; omit for the model default")
    ap.add_argument("--outdir", help="write elsewhere than data/passA (for A/B samples)")
    ap.add_argument("--slugs", help="comma-separated slugs to run instead of the full queue")
    args = ap.parse_args()

    outdir = args.outdir or OUTDIR
    runlog = os.path.join(outdir, "_runlog.jsonl")
    os.makedirs(outdir, exist_ok=True)
    os.makedirs(os.path.join(outdir, "_logs"), exist_ok=True)

    with open(INDEX) as fh:
        index = json.load(fh)

    if args.slugs:
        want = [s.strip() for s in args.slugs.split(",") if s.strip()]
        index = [r for r in index if r["slug"] in want]
    todo = [r for r in index if r["slug"] not in SKIP_SLUGS and not done(r["slug"], outdir)]
    skipped_done = sum(1 for r in index if r["slug"] not in SKIP_SLUGS and done(r["slug"], outdir))
    if args.limit:
        todo = todo[:args.limit]

    log(f"{len(index)} talks | {len(SKIP_SLUGS)} keynote blocks skipped | "
        f"{skipped_done} already done | {len(todo)} queued | concurrency={args.concurrency} | "
        f"effort={args.effort or 'default'} | outdir={os.path.relpath(outdir, ROOT)}")

    deadline = time.time() + args.minutes * 60 if args.minutes else None
    if deadline:
        log(f"launch deadline in {args.minutes:g} min, then up to {args.grace:g}s grace")

    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, lambda *_: (stop.set(), log("stop requested; draining")))

    t0 = time.time()
    results = []

    def worker(rec):
        if stop.is_set() or (deadline and time.time() >= deadline):
            return None
        row = run_one(rec, args.timeout, args.effort, outdir)
        with _log_lock:
            with open(runlog, "a") as fh:
                fh.write(json.dumps(row) + "\n")
        return row

    pool = ThreadPoolExecutor(max_workers=args.concurrency)
    futs = [pool.submit(worker, r) for r in todo]
    if deadline:
        # Wait out the launch window, then stop new work and drain in flight.
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
            log("grace expired; killing in-flight calls (their talks stay unfinished)")
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
        log(f"per-talk avg: in={sum(r['tokens_in'] for r in ok)/n:,.0f} "
            f"out={sum(r['tokens_out'] for r in ok)/n:,.0f} "
            f"wall={sum(r['wall_sec'] for r in ok)/n:.0f}s "
            f"cost=${sum(r['cost_usd'] for r in ok)/n:.3f}")
    if fail:
        log("failures: " + ", ".join(f"{r['slug']}({r['error']})" for r in fail))
    os._exit(0)  # don't wait on any orphaned child pipes


if __name__ == "__main__":
    main()
