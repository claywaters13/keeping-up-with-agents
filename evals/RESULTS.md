# Eval results

**12/12 cases passing**, last run 2026-08-19.

Runner: `python3 evals/run.py`. Judge model: `claude-sonnet-5`. Agent model: `default`. Agent-run cost this run: $4.58.

Regenerate with `python3 evals/run.py`; this file is written by that script.

| Case | Result | Graders | Time | What it checks |
|---|---|---|---|---|
| `ambiguous-topic-testing-agents` | PASS | ✓ | 162s | Ambiguous topic spanning multiple concepts - should route sensibly across eval-harness-design / llm-as-a-judge / verifier-design rather than picking just one narrowly |
| `disagreement-prompt-injection` | PASS | ✓/✓ | 51s | Disagreement reporting - both positions plus who holds each, on prompt injection defense |
| `maturity-frontier-concepts` | PASS | ✓/✓ | 49s | Maturity labeling - correctly lists the 4 frontier-labeled concepts, not other maturities |
| `metadata-lookup-corpus-size` | PASS | ✓/✓ | 22s | Metadata lookup - correct corpus counts from data/index.json or wiki/README.md, not guessed |
| `quote-fidelity-reward-hacking` | PASS | ✓ | 20s | Quote fidelity - speaker quotes must be verbatim from the reward-hacking concept page |
| `refusal-nonexistent-speaker` | PASS | ✓/✓ | 21s | Negative test - John Doe is not a real AIEWF 2026 speaker; must refuse, not invent quotes |
| `refusal-out-of-corpus-2025` | PASS | ✓ | 16s | Negative test - AIEWF 2025 is not in this corpus (2026 only); must decline, not answer from general knowledge |
| `refusal-unindexed-yc-event` | PASS | ✓ | 30s | Negative test - YC's AI Startup School (June 2025) is a different, unindexed event; must decline, not answer from general knowledge or substitute the 2026 corpus |
| `slash-command-aiewf` | PASS | ✓/✓ | 74s | /ask slash command - must expand and answer from the corpus (not "Unknown command"). NOTE - headless sessions require the fully-qualified keeping-up-with-agents:ask form; the bare /ask short name only resolves interactively. |
| `speaker-lookup-simon-willison` | PASS | ✓/✓ | 42s | Speaker lookup - quotes from a real, named speaker in the corpus |
| `topic-synthesis-agent-memory` | PASS | ✓/✓/✓ | 67s | Topic synthesis - agent memory disagreements, cited and grounded in the wiki |
| `yc-metadata-lookup-corpus-size` | PASS | ✓/✓ | 17s | Metadata lookup - correct YC Startup School 2026 corpus counts from data/index.json or wiki/README.md, not guessed |

## Notes

- A case passes only if *every* grader passes. No partial credit.
- Quote fidelity additionally has a deterministic check that uses no model judgment at all: `events/aiewf-2026/scripts/eval_plugin.sh`. See `evals/README.md` for why.
