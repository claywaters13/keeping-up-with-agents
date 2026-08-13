#!/usr/bin/env python3
"""Aggregate Claude Code token usage from session transcripts.

Reads per-message `usage` blocks out of ~/.claude/projects/**/*.jsonl and
buckets them by rolling window and model.
"""
import json, os, glob, collections
from datetime import datetime, timezone, timedelta

now = datetime.now(timezone.utc)
W5 = now - timedelta(hours=5)
W7D = now - timedelta(days=7)

files = glob.glob(os.path.expanduser("~/.claude/projects/**/*.jsonl"), recursive=True)
cutoff = (now - timedelta(days=8)).timestamp()
files = [f for f in files if os.path.getmtime(f) >= cutoff]

buckets = {"5h": collections.defaultdict(lambda: collections.Counter()),
           "7d": collections.defaultdict(lambda: collections.Counter())}
msgs = {"5h": 0, "7d": 0}

for path in files:
    try:
        with open(path, errors="ignore") as fh:
            for line in fh:
                if '"usage"' not in line:
                    continue
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                if d.get("type") != "assistant":
                    continue
                m = d.get("message")
                if not isinstance(m, dict) or not m.get("usage"):
                    continue
                ts = d.get("timestamp")
                if not ts:
                    continue
                try:
                    t = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                except Exception:
                    continue
                if t < W7D:
                    continue
                u = m["usage"]
                model = (m.get("model") or "unknown").replace("-20251001", "")
                rec = {
                    "in": u.get("input_tokens", 0),
                    "cache_w": u.get("cache_creation_input_tokens", 0),
                    "cache_r": u.get("cache_read_input_tokens", 0),
                    "out": u.get("output_tokens", 0),
                }
                for win, start in (("7d", W7D), ("5h", W5)):
                    if t >= start:
                        for k, v in rec.items():
                            buckets[win][model][k] += v
                        msgs[win] += 1
    except Exception:
        continue


def show(win, label):
    print(f"\n=== {label} ===")
    tot = collections.Counter()
    for model, c in sorted(buckets[win].items(), key=lambda x: -sum(x[1].values())):
        billed_in = c["in"] + c["cache_w"] + c["cache_r"]
        print(f"  {model:28s} in={billed_in/1e6:6.2f}M  out={c['out']/1e6:6.3f}M")
        tot.update(c)
    billed_in = tot["in"] + tot["cache_w"] + tot["cache_r"]
    print(f"  {'TOTAL':28s} in={billed_in/1e6:6.2f}M  out={tot['out']/1e6:6.3f}M  "
          f"({msgs[win]:,} assistant msgs)")
    return billed_in, tot["out"]


print(f"session files scanned: {len(files)}")
show("7d", "LAST 7 DAYS")
show("5h", "LAST 5 HOURS")
