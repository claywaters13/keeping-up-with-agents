#!/usr/bin/env python3
"""Portable runner for this repo's eval suite.

Runs each case in evals/<case>/ against the installed aiewf-wiki plugin and scores it
with that case's graders/*.md.

Why this exists: Claude Code ships `claude plugin eval`, which reads exactly this
directory layout and is the more featureful runner (ablation arms, HTML reports, cost
ceilings). Use it if you have it. But it is currently gated behind early access, and an
eval suite in a public repo should be runnable by anyone who clones the repo, so this
script implements the same case/grader spec with nothing but `claude -p`.

Case format   evals/<name>/prompt.md      YAML frontmatter + the prompt body
Grader format evals/<name>/graders/*.md   YAML frontmatter + (for llm graders) a rubric

Grader types:
  regex  pattern / flags / match: contains|not_contains  (deterministic, free)
  llm    a rubric judged by a model with NO tools, which must answer PASS or FAIL

A case passes only if every one of its graders passes.

Prerequisites: the plugin must be installed (see README), since cases invoke it by
asking questions that route through its skill:

    claude plugin marketplace add .
    claude plugin install aiewf-wiki@keeping-up-with-agents

Usage:
    python3 evals/run.py                                  # all cases
    python3 evals/run.py --case refusal-nonexistent-speaker
    python3 evals/run.py --case 'refusal-*'
    python3 evals/run.py --judge-model claude-haiku-4-5-20251001
"""
import argparse
import datetime
import fnmatch
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVALS_DIR = os.path.join(ROOT, "evals")
DEFAULT_JUDGE = "claude-sonnet-5"
CASE_TIMEOUT = 600
JUDGE_TIMEOUT = 180


# ---------------------------------------------------------------------------
# Minimal frontmatter parsing (avoids a PyYAML dependency for a fixed schema)
# ---------------------------------------------------------------------------

def split_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    return parse_frontmatter(raw), body


def parse_scalar(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        inner = v[1:-1]
        if v[0] == '"':
            # YAML double-quoted: \\ and \" are the escapes we actually use
            inner = inner.replace('\\\\', '\\').replace('\\"', '"')
        return inner
    if v.startswith("[") and v.endswith("]"):
        return [p.strip() for p in v[1:-1].split(",") if p.strip()]
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    return v


def parse_frontmatter(raw):
    out = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        out[k.strip()] = parse_scalar(v)
    return out


# ---------------------------------------------------------------------------
# Running
# ---------------------------------------------------------------------------

def child_env():
    env = os.environ.copy()
    # House rule for this project: subscription only, never a metered API key.
    env.pop("ANTHROPIC_API_KEY", None)
    return env


def run_claude(args, stdin_text, timeout):
    proc = subprocess.run(
        args,
        input=stdin_text,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=ROOT,
        env=child_env(),
    )
    return proc


def run_case_agent(case, model=None):
    """Run one case's prompt and return (response_text, meta)."""
    tools = case["meta"].get("allowed_tools") or ["Read", "Glob", "Grep", "Skill"]
    args = [
        "claude", "-p", case["prompt"],
        "--allowedTools", ",".join(tools),
        "--output-format", "json",
        "--strict-mcp-config",
        "--setting-sources", "user",
    ]
    max_turns = case["meta"].get("max_turns")
    if max_turns:
        args += ["--max-turns", str(max_turns)]
    if model:
        args += ["--model", model]

    started = time.time()
    try:
        proc = run_claude(args, None, CASE_TIMEOUT)
    except subprocess.TimeoutExpired:
        return "", {"error": f"timeout after {CASE_TIMEOUT}s", "seconds": CASE_TIMEOUT}
    elapsed = round(time.time() - started, 1)

    if proc.returncode != 0:
        return "", {"error": (proc.stderr or proc.stdout or "").strip()[:400],
                    "seconds": elapsed}
    try:
        env = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return "", {"error": "unparseable envelope: " + proc.stdout[:200],
                    "seconds": elapsed}

    return env.get("result", ""), {
        "seconds": elapsed,
        "num_turns": env.get("num_turns"),
        "cost_usd": env.get("total_cost_usd"),
    }


# ---------------------------------------------------------------------------
# Graders
# ---------------------------------------------------------------------------

def grade_regex(meta, response):
    flags = re.IGNORECASE if "i" in str(meta.get("flags", "")) else 0
    hit = re.search(str(meta["pattern"]), response, flags) is not None
    want = meta.get("match", "contains")
    passed = hit if want == "contains" else not hit
    detail = f"/{meta['pattern']}/ {'matched' if hit else 'did not match'}; expected {want}"
    return passed, detail


JUDGE_TEMPLATE = """You are grading a single response against one rubric. You have NO \
tools, so judge only from the text given to you.

<rubric>
{rubric}
</rubric>

<response_to_grade>
{response}
</response_to_grade>

Apply the rubric strictly, and judge only what the rubric asks about.

First give one or two sentences of reasoning. Then, on the final line and nothing after
it, write your verdict in exactly this form:

VERDICT: PASS
or
VERDICT: FAIL

The reasoning comes first on purpose. Do not state a verdict before you have reasoned,
and make sure the final line agrees with your reasoning.
"""


def grade_llm(meta, rubric, response, judge_model):
    prompt = JUDGE_TEMPLATE.format(rubric=rubric.strip(), response=response.strip())
    args = [
        "claude", "-p",
        "--model", judge_model,
        "--allowedTools", "",
        "--output-format", "json",
        "--strict-mcp-config",
        "--setting-sources", "",
    ]
    try:
        proc = run_claude(args, prompt, JUDGE_TIMEOUT)
    except subprocess.TimeoutExpired:
        return False, f"judge timeout after {JUDGE_TIMEOUT}s"
    if proc.returncode != 0:
        return False, "judge error: " + (proc.stderr or "").strip()[:200]
    try:
        verdict = json.loads(proc.stdout).get("result", "").strip()
    except json.JSONDecodeError:
        return False, "judge returned unparseable envelope"

    # Take the LAST verdict line: the judge reasons first, so an early "fail" inside the
    # rationale must not be mistaken for the decision.
    matches = re.findall(r"VERDICT:\s*(PASS|FAIL)", verdict.upper())
    if matches:
        return matches[-1] == "PASS", verdict[-300:].strip()
    # Ambiguous verdict is a failure: a grader that cannot decide has not passed.
    return False, "no VERDICT line in judge output: " + verdict[:200]


# ---------------------------------------------------------------------------
# Discovery / orchestration
# ---------------------------------------------------------------------------

def load_cases(pattern):
    cases = []
    for name in sorted(os.listdir(EVALS_DIR)):
        case_dir = os.path.join(EVALS_DIR, name)
        prompt_path = os.path.join(case_dir, "prompt.md")
        if not os.path.isfile(prompt_path):
            continue
        if pattern and not fnmatch.fnmatch(name, pattern):
            continue
        with open(prompt_path, encoding="utf-8") as f:
            meta, prompt = split_frontmatter(f.read())

        graders = []
        graders_dir = os.path.join(case_dir, "graders")
        for gname in sorted(os.listdir(graders_dir)) if os.path.isdir(graders_dir) else []:
            if not gname.endswith(".md"):
                continue
            with open(os.path.join(graders_dir, gname), encoding="utf-8") as f:
                gmeta, rubric = split_frontmatter(f.read())
            graders.append({"name": gname[:-3], "meta": gmeta, "rubric": rubric})

        cases.append({"name": name, "meta": meta, "prompt": prompt.strip(),
                      "graders": graders})
    return cases


def run_all(cases, judge_model, model):
    results = []
    for i, case in enumerate(cases, 1):
        print(f"[{i}/{len(cases)}] {case['name']} ... ", end="", flush=True)
        response, meta = run_case_agent(case, model)

        grader_results = []
        if meta.get("error"):
            passed = False
            grader_results.append({"name": "_agent_run", "type": "harness",
                                   "passed": False, "detail": meta["error"], "weight": 0})
        else:
            passed = True
            for g in case["graders"]:
                gtype = g["meta"].get("type", "regex")
                if gtype == "regex":
                    ok, detail = grade_regex(g["meta"], response)
                elif gtype == "llm":
                    ok, detail = grade_llm(g["meta"], g["rubric"], response, judge_model)
                else:
                    ok, detail = False, f"unknown grader type: {gtype}"
                passed = passed and ok
                grader_results.append({"name": g["name"], "type": gtype, "passed": ok,
                                       "detail": detail,
                                       "weight": g["meta"].get("weight", 1)})

        print("PASS" if passed else "FAIL")
        for g in grader_results:
            if not g["passed"]:
                print(f"      ✗ {g['name']}: {g['detail'][:160]}")

        results.append({
            "case": case["name"],
            "description": case["meta"].get("description", ""),
            "tags": case["meta"].get("tags", []),
            "passed": passed,
            "seconds": meta.get("seconds"),
            "cost_usd": meta.get("cost_usd"),
            "graders": grader_results,
            "response": response,
        })
    return results


def write_results_md(results, path, judge_model, model):
    total = len(results)
    n_pass = sum(1 for r in results if r["passed"])
    cost = sum(r["cost_usd"] or 0 for r in results)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d")

    lines = [
        "# Eval results",
        "",
        f"**{n_pass}/{total} cases passing**, last run {stamp}.",
        "",
        f"Runner: `python3 evals/run.py`. Judge model: `{judge_model}`. "
        f"Agent model: `{model or 'default'}`. Agent-run cost this run: ${cost:.2f}.",
        "",
        "Regenerate with `python3 evals/run.py`; this file is written by that script.",
        "",
        "| Case | Result | Graders | Time | What it checks |",
        "|---|---|---|---|---|",
    ]
    for r in results:
        gr = "/".join("✓" if g["passed"] else "✗" for g in r["graders"])
        secs = f"{r['seconds']:.0f}s" if r.get("seconds") else "n/a"
        lines.append(
            f"| `{r['case']}` | {'PASS' if r['passed'] else 'FAIL'} | {gr} | {secs} | "
            f"{r['description']} |"
        )

    failures = [r for r in results if not r["passed"]]
    if failures:
        lines += ["", "## Failures", ""]
        for r in failures:
            lines.append(f"### `{r['case']}`")
            lines.append("")
            for g in r["graders"]:
                if not g["passed"]:
                    lines.append(f"- **{g['name']}** ({g['type']}): {g['detail']}")
            lines.append("")

    lines += [
        "",
        "## Notes",
        "",
        "- A case passes only if *every* grader passes. No partial credit.",
        "- Quote fidelity additionally has a deterministic check that uses no model "
        "judgment at all: `scripts/eval_plugin.sh`. See `evals/README.md` for why.",
        "",
    ]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--case", help="glob filter on case directory name")
    ap.add_argument("--judge-model", default=DEFAULT_JUDGE,
                    help=f"model for llm graders (default: {DEFAULT_JUDGE})")
    ap.add_argument("--model", help="override the model used for the agent runs")
    ap.add_argument("--output-dir", help="where to write the raw run JSON")
    ap.add_argument("--no-results-md", action="store_true",
                    help="do not update evals/RESULTS.md")
    args = ap.parse_args()

    cases = load_cases(args.case)
    if not cases:
        print(f"no cases matched {args.case!r}", file=sys.stderr)
        return 2

    print(f"Running {len(cases)} case(s); judge={args.judge_model}\n")
    results = run_all(cases, args.judge_model, args.model)

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = args.output_dir or os.path.join(EVALS_DIR, "results", stamp)
    os.makedirs(out_dir, exist_ok=True)
    raw_path = os.path.join(out_dir, "aggregate-result.json")
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump({"timestamp": stamp, "judge_model": args.judge_model,
                   "model": args.model, "results": results}, f, indent=2)

    n_pass = sum(1 for r in results if r["passed"])
    print(f"\n{n_pass}/{len(results)} passing. Raw run: {os.path.relpath(raw_path, ROOT)}")

    if not args.no_results_md and not args.case:
        md = os.path.join(EVALS_DIR, "RESULTS.md")
        write_results_md(results, md, args.judge_model, args.model)
        print(f"Wrote {os.path.relpath(md, ROOT)}")

    return 0 if n_pass == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
