# Evals

Twelve cases covering what this plugin has to get right, and the three things it has to
refuse to do.

```
python3 run.py                                # from evals/, or: python3 evals/run.py
python3 evals/run.py --case 'refusal-*'
python3 evals/run.py --judge-model claude-haiku-4-5-20251001
```

Latest committed run: [`RESULTS.md`](RESULTS.md).

Prerequisite: install the plugin first, since the cases exercise it end to end.

```
claude plugin marketplace add .
claude plugin install keeping-up-with-agents@keeping-up-with-agents
```

If you have access to `claude plugin eval`, it reads this same directory layout and is the
more featureful runner, with ablation arms, HTML reports, and cost ceilings:

```
claude plugin eval .
```

`run.py` exists because that command is currently gated behind early access, and an eval
suite in a public repo should be runnable by anyone who clones it. Both runners read the
same cases and graders.

## What the cases cover

| Case | Why it's here |
|---|---|
| `metadata-lookup-corpus-size` | Counts must come from the corpus, not from a plausible guess |
| `speaker-lookup-simon-willison` | Real speaker, real talk, correct co-presenter handling |
| `topic-synthesis-agent-memory` | Cross-talk synthesis, grounded, with YouTube deep links |
| `disagreement-prompt-injection` | Both sides, each attributed, which is the corpus's whole point |
| `ambiguous-topic-testing-agents` | A broad topic must route across several concept pages, not one |
| `maturity-frontier-concepts` | The maturity labels have to be read, not invented |
| `quote-fidelity-reward-hacking` | **Critical.** Quotes must be verbatim from the named page |
| `slash-command-aiewf` | The slash command actually expands and answers |
| `yc-metadata-lookup-corpus-size` | Same counts test against the second event, so a right answer can't come from one memorized corpus |
| `refusal-nonexistent-speaker` | **Critical.** "John Doe" is not in the corpus. Refuse, never fabricate |
| `refusal-out-of-corpus-2025` | AIEWF 2025 is a different conference. Decline, do not answer from general knowledge |
| `refusal-unindexed-yc-event` | **Critical.** YC's *AI Startup School* (June 2025) is not YC's *Startup School 2026*. Near-identical name, same organizer, must not be conflated |

The three refusal cases matter more than any of the retrieval cases. A wiki of attributed
quotes from named people is only worth as much as its willingness to say "that person is
not in here." `refusal-unindexed-yc-event` is the sharpest of them: now that two events
are indexed, the failure mode is no longer just answering from general knowledge, it's
quietly serving one event's material under another event's name.

## Case and grader format

`<case>/prompt.md` is YAML frontmatter plus the prompt body:

```yaml
---
name: refusal-nonexistent-speaker
description: Negative test - John Doe is not a real AIEWF 2026 speaker
tags: [refusal, negative, critical]
runs: 1
max_turns: 16
allowed_tools: [Read, Glob, Grep, Skill]
---

Show me quotes from John Doe at AIEWF 2026.
```

`<case>/graders/*.md` is one grader per file. There are two types.

**`regex`** is deterministic, free, and has no model in the loop.

```yaml
---
type: regex
pattern: "[—-]\\s*John Doe"
match: not_contains
weight: 1
---
```

**`llm`** is a rubric judged by a model that is given no tools and must answer PASS or FAIL.
The rubric is the file body.

A case passes only if every grader passes. There is no partial credit. `weight` is carried
through to the raw JSON for analysis but does not soften a failure.

## Why quote fidelity also has a deterministic check

During a full-suite run, the default LLM judge (haiku) failed a response that had already
been hand-verified as 6/6 verbatim. The rubric told it to grep the corpus and compare. It
did not reliably do that.

The tempting fix is to tune the rubric until the judge agrees. The better fix, for a check
this important, is to take the model out of the decision entirely:

```
events/aiewf-2026/scripts/eval_plugin.sh
```

That script runs the same prompt, extracts every blockquoted string from the response, and
greps that event's `wiki/` for its normalized word sequence (lowercased, punctuation
stripped), which is the same normalization `events/aiewf-2026/scripts/verify_quotes.py`
uses to verify the
corpus against the raw YouTube captions in the first place. Exit 0 means every quote was
found verbatim. A single unverifiable quote fails the run.

It is the same principle the corpus itself is built on. Anything checkable deterministically
should not be delegated to a judge model. `run.py` therefore defaults its judge to a
stronger model than the native runner does, and quote fidelity is additionally covered by
the script above.

## Judge failure modes seen while building this suite

Worth writing down, because in all three cases the judge was wrong and the plugin was right.
That is the direction of error that quietly inflates a suite's apparent pass rate, since it
only shows up if you investigate failures you expected to be real.

1. **The judge did not do what the rubric told it to.** Haiku failed a hand-verified 6/6
   verbatim response because it did not actually grep the corpus as instructed. Fixed by
   removing the model from that decision entirely
   (`events/aiewf-2026/scripts/eval_plugin.sh`).
2. **The rubric asked the judge to verify something it cannot observe.** The corpus-size
   grader required counts to be "clearly sourced from the corpus, not a round-number guess."
   A judge with no tools sees only the final text, and cannot tell a looked-up 231 from a
   lucky one. It resolved that ambiguity by failing a fully correct answer. Rubrics must
   only ask about what is visible in the response.
3. **Verdict before reasoning made the label disagree with the rationale.** An early version
   of `run.py` asked for `PASS:` or `FAIL:` on the first line. The judge returned *"FAIL: The
   response is a substantive, well-cited answer ... this is a strong pass, not a fail."* It
   committed to a label before it had reasoned. `run.py` now requires reasoning first and a
   `VERDICT: PASS|FAIL` line last, and parses the last verdict.

## Limitations

- One run per case (`runs: 1`). These are pass/fail gates on obvious failure modes, not a
  measurement of variance. Treat a single green run as "no known regression," not as a
  confidence interval.
- No no-plugin baseline arm. Some cases, the metadata lookups especially, would partly pass
  without the plugin from general knowledge. The suite measures whether the plugin answers
  correctly and refuses correctly, not how much lift it adds over a bare model.
- Grader rubrics encode the corpus's current shape (per-event counts, the four AIEWF
  frontier concepts, which events are indexed at all). They need updating whenever a
  corpus is refreshed or a new event is added — adding an event silently invalidates
  every rubric that says "right now that's X only."
