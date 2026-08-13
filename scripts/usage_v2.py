#!/usr/bin/env python3
"""Cost-weighted Claude Code usage, windowed, plus implied caps.

Subscription limits are almost certainly weighted by model rather than raw
token count, so we compute a cost-weighted figure as the proxy for "% of limit".
"""
import json, glob, os, sys, collections
from datetime import datetime, timezone, timedelta

# $/MTok (input, output). Cache read = 0.1x input, cache write = 1.25x input.
RATES = {
    "claude-opus-5": (5.0, 25.0),
    "claude-opus-4-8": (5.0, 25.0),
    "claude-sonnet-5": (3.0, 15.0),
    "claude-sonnet-4-6": (3.0, 15.0),
    "claude-fable-5": (10.0, 50.0),
    "claude-haiku-4-5": (1.0, 5.0),
}

now = datetime.now(timezone.utc)
WINDOWS = {
    "since 2am MDT (08:00 UTC)": now.replace(hour=8, minute=0, second=0, microsecond=0),
    "rolling 5h": now - timedelta(hours=5),
    "rolling 7d": now - timedelta(days=7),
}

files = [f for f in glob.glob(os.path.expanduser("~/.claude/projects/**/*.jsonl"), recursive=True)
         if os.path.getmtime(f) >= (now - timedelta(days=8)).timestamp()]

agg = {k: collections.defaultdict(lambda: collections.Counter()) for k in WINDOWS}
seen = set()

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
                m = d.get("message") or {}
                u = m.get("usage")
                ts = d.get("timestamp")
                if not u or not ts:
                    continue
                uid = d.get("uuid")
                if uid in seen:
                    continue
                seen.add(uid)
                try:
                    t = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                except Exception:
                    continue
                model = (m.get("model") or "unknown").replace("-20251001", "")
                for name, start in WINDOWS.items():
                    if t >= start:
                        c = agg[name][model]
                        c["in"] += u.get("input_tokens", 0)
                        c["cw"] += u.get("cache_creation_input_tokens", 0)
                        c["cr"] += u.get("cache_read_input_tokens", 0)
                        c["out"] += u.get("output_tokens", 0)
                        c["msgs"] += 1
    except Exception:
        continue


def cost(model, c):
    r = RATES.get(model)
    if not r:
        return 0.0
    inr, outr = r
    return ((c["in"] * inr) + (c["cw"] * inr * 1.25) + (c["cr"] * inr * 0.1)
            + (c["out"] * outr)) / 1e6


results = {}
for name in WINDOWS:
    tot_cost = sum(cost(m, c) for m, c in agg[name].items())
    tot_out = sum(c["out"] for c in agg[name].values())
    tot_msgs = sum(c["msgs"] for c in agg[name].values())
    results[name] = (tot_cost, tot_out, tot_msgs)
    print(f"\n=== {name} ===")
    for m, c in sorted(agg[name].items(), key=lambda x: -cost(x[0], x[1])):
        print(f"  {m:22s} out={c['out']/1e6:6.3f}M  weighted=${cost(m,c):8.2f}  msgs={c['msgs']:,}")
    print(f"  {'TOTAL':22s} out={tot_out/1e6:6.3f}M  weighted=${tot_cost:8.2f}  msgs={tot_msgs:,}")

print("\n\n=== IMPLIED CAPS (from Clay: 11% of 5h, 7% of weekly) ===")
c5 = results["since 2am MDT (08:00 UTC)"]
c7 = results["rolling 7d"]
print(f"  5h window used:  ${c5[0]:.2f} weighted  /  {c5[1]/1e6:.3f}M output")
print(f"    -> implied 5h cap:     ${c5[0]/0.11:8.2f}  /  {c5[1]/0.11/1e6:6.2f}M output")
print(f"  7d window used:  ${c7[0]:.2f} weighted  /  {c7[1]/1e6:.3f}M output")
print(f"    -> implied weekly cap: ${c7[0]/0.07:8.2f}  /  {c7[1]/0.07/1e6:6.2f}M output")

PASS_A_COST, PASS_A_OUT = 85.0, 2.17e6
print(f"\n=== PASS A (231 talks: ~$85 weighted, ~2.17M output) ===")
print(f"  as % of implied 5h cap:     {PASS_A_COST/(c5[0]/0.11)*100:5.1f}% (cost)  "
      f"{PASS_A_OUT/(c5[1]/0.11)*100:5.1f}% (output)")
print(f"  as % of implied weekly cap: {PASS_A_COST/(c7[0]/0.07)*100:5.1f}% (cost)  "
      f"{PASS_A_OUT/(c7[1]/0.07)*100:5.1f}% (output)")
