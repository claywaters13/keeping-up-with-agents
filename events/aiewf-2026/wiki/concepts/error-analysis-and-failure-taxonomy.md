---
title: "error analysis and failure taxonomy"
type: "concept"
slug: "error-analysis-and-failure-taxonomy"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 13
---

# error analysis and failure taxonomy

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **13** speaker(s)

**Definition:** Systematically clustering observed failures into named modes so effort can be aimed at the largest buckets.

*Also referred to as: failure mode clustering, error analysis and failure mode clustering, agent failure taxonomy, error analysis loops, failure mode analysis, root cause analysis for agent failures, crash deduplication via stack backtrace, silent failure detection*

## State of Practice

The field has converged on a bottom-up pipeline: sample real production traces, read them (or cluster them with an agent), name the recurring modes, and convert each named mode into a permanent binary check that gates shipping. Nobody at this conference defended writing the failure taxonomy in advance — Lyft, Mutagent, and Wandero all argue the real criteria are a product of discovery, and Meta Superintelligence Labs frames production telemetry as the largest and most representative eval set an org will ever have. The unit of a taxonomy entry has hardened into a binary, domain-specific assertion ("answer is grounded in the retrieved context: yes/no", "task succeeded") rather than a 0-1 helpfulness score, because scalar scores are inconsistent across runs and give no call to action. Judges that produce those labels are themselves treated as classifiers to be validated — roughly 100 hand-labeled examples, train/dev/test split, precision and recall — and scores are expected to carry confidence intervals, since 84% vs 88% on 50 traces is noise. Two things are genuinely unsettled: how much of the diagnose-fix-verify loop can run without a human in it, and whether a failure can be repaired from a log alone or must first be lifted into a replayable environment with deterministic graders. A recurring warning across very different domains — Lyft's 90% pass rate, Bugcrowd's 95% crash rate, DeepSWE's clustered leaderboard — is that a metric everything passes is a broken instrument, not a solved problem.

## Consensus

### The failure taxonomy must be discovered from production traffic and traces; a complete set of eval criteria cannot be enumerated up front, even by domain experts.

Support: **6** talk(s)

> "Production is the largest and the most representative evaluation data any organization will ever have."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Agents Building Agents](../talks/agents-building-agents.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)

### Evaluation requires step-level traces — context entering each node, every tool output, state transitions — because final-output-only signals (completion, 200 OK, green dashboards) hide real failures.

Support: **6** talk(s)

> "Agent traces become the equivalent of distributed tracing for autonomous workloads. Without observability, evaluation becomes the guesswork."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Agents Building Agents](../talks/agents-building-agents.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)

### LLM judges are unreliable until calibrated against human labels — the same judge scores the same trace differently across runs — so judge quality must be measured before its cluster counts are trusted.

Support: **5** talk(s)

> "next time you run the same evaluator you get a different answer from the same kind of evaluation you ran"
>
> — [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s)

Supporting talks: [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)

### Every newly named failure mode must be immediately converted into a permanent artifact — a golden-dataset item, a replayable environment, a stubbed regression test — so that fixing it cannot silently break what already worked.

Support: **4** talk(s)

> "all the failure modes that we are founding during this investigation step, they will become part of the golden dataset that we mentioned earlier and the eval suite is updated to spot those regressions."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [25:33](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1533s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)

### Failure modes should be expressed as binary, domain-specific pass/fail assertions tied to a business outcome, not as continuous quality scores like helpfulness or correctness on a 0-1 scale.

Support: **3** talk(s)

> "when you use score-based evals, unless your rubric is very well defined, then this does not exactly tell you what to fix"
>
> — [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [16:53](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1013s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)

### A very high pass rate is evidence the measurement is broken — too-easy simulators, saturated success criteria, or verifiers anchored to the wrong thing — rather than evidence the system works.

Support: **3** talk(s)

> "our first attempt at our offline evaluation gave us 90 plus pass rate or accuracy rate, right? Uh this almost sounds too good to be true, and I think it indeed is the too good to be true."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [13:40](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=820s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)

## Disagreements

### Once a failure cluster has been diagnosed and a fix generated, does a human have to approve it before it ships?

| Position A | Position B |
|---|---|
| A human must remain the gate: clustered failure reports are triaged and validated by subject matter experts before fixes are implemented, and code that modifies working production behavior needs human approval regardless of how the fix was verified.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)* | If the optimized variant clears its target eval scores, it ships automatically; the human review step is the throughput bottleneck and should be engineered out, with a separate reviewing agent standing in for the human.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* |

*Why it matters: This sets the ceiling on how many failure modes an org can close per week — Wandero reports its PR and review agents opening ten times more PRs than its three humans — but it also decides whether a mis-clustered false positive or an intended behavior gets 'fixed' into production unreviewed.*

### Can an agent be repaired directly from a production log, or must the failure first be lifted into a replayable environment with deterministic grading?

| Position A | Position B |
|---|---|
| Reading a log and editing the agent is 'vibe-based': the change is untestable for that very sample and can introduce hidden regressions. The log must first become a replayable simulation with defined evaluators, or a recorded trace with every other node stubbed, before any fix counts.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)* | A log-reading agent plus a separate reviewing agent is enough to go from production issue to a review-ready PR in about half an hour, and a coding agent given regression tests can fix a whole suite of issues from one prompt.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Agents Building Agents](../talks/agents-building-agents.md)* |

*Why it matters: The replay-first path costs environment-construction work per failure mode but yields fixes provably free of regressions; the log-first path is roughly an order of magnitude faster to a candidate fix and is where most teams' loops actually run today.*

### Should the grader that assigns a trace to a failure mode be deterministic, or is a calibrated LLM judge acceptable?

| Position A | Position B |
|---|---|
| Graders must be deterministic and code-checkable. Models systematically claim success on their own work, you cannot trust an LLM you are also training, and subjective grading lets reward hacking through; verification should be a program that checks observable behavior.<br>*[Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)* | LLM judges are the workhorse and the fix is calibration, not replacement — validate them like binary classifiers on hand-labeled data; purely test-based verification is itself harmful because it forces you to hint the method in the prompt and makes verifiers brittle to implementation choices.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)* |

*Why it matters: Deterministic graders force you to over-specify the task, which DeepSWE shows produces false negatives against any correct-but-differently-shaped solution; LLM graders keep the task open-ended but make every reported failure-mode frequency an estimate with its own error bars.*

### Does error analysis scale by adding human expert labeling, or by replacing that labeling with agents?

| Position A | Position B |
|---|---|
| Human domain experts are irreducible: they surface the implicit decision criteria that become the high-signal evaluators, and production data must be reviewed by a human rather than only by a coding agent because failure modes and usage shift over time.<br>*[Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* | Manual iteration stops scaling past a certain number of agents; log analysis is itself an agent problem, and at millions of traces you sample representatively using learned code-checkable indicators instead of labeling.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)* |

*Why it matters: It determines whether taxonomy maintenance is a recurring expert-hours line item or an infrastructure cost, and whether your failure modes stay grounded in domain truth or drift toward whatever an LLM finds salient in a trace.*

## Practical Guidance

**Do:**

- Sample eval datasets from production traffic and mutate them to cover golden paths and edge cases, rather than prompting an LLM for ~50 synthetic queries
- Hand-label ~100 traces with pass/fail, split into train/dev/test, and score your judge on precision and recall before trusting the failure counts it produces
- State each failure mode as a binary domain-specific check ('the answer is based on the knowledge base: yes/no') instead of a 0-1 correctness or helpfulness score
- Attach a confidence interval to every reported score, and reserve that statistical rigor for shipping decisions and leadership reports rather than applying it uniformly
- Fine-tune your user simulator on real user verbatim until the eval score goes down — a falling score means the eval got realistic, not that quality dropped
- Add every newly named failure mode to the golden dataset and eval suite at the moment it is identified, so the next fix cannot regress it
- Record what enters and leaves each agent node, plus the full session envelope (model version, build ID, RAG chunks), so a failing run can be replayed with all nodes but the changed one stubbed — deterministic and free
- Run the clustered failure report on a fixed cadence — once per sprint, or weekly per service — rather than only when someone complains
- Give the fix-generating agent and the reviewing agent separate contexts, since the fixer is biased toward its own diagnosis and eager to open PRs
- Keep the catalog of named anti-patterns as markdown in one central Git repo, and once a pattern is confirmed, cross-repo search for its other instances (Netflix found the same one in seven services)
- Verify a fix with a canary measuring CPU, latency, and error rate before it reaches a human — passing tests are not verification
- Explicitly forbid an optimizing agent from editing the golden dataset or the scorers
- Build the taxonomy so a mode is defined by observable behavior, not by whether a specific helper, module placement, or function name exists

**Avoid:**

- Emitting a judge score that gates no decision — an LLM-as-a-judge whose output nobody blocks on is dead weight
- Using pre-built generic metrics (helpfulness, toxicity, conciseness on a 0-1 or 1-5 scale) as core metrics; a 0.5 helpfulness tells you nothing to fix
- Treating hallucination as the primary production failure category — it is one bucket among tool failures, API outages, context drift, and long-horizon breakdowns
- Assuming one failure has one cause and one repair, or that the cheapest layer (memory write) is the right layer
- Editing an agent from a single log without any replayable environment, which produces changes that are untestable and can hide regressions
- Chasing temperature=0 or bitwise determinism from a hosted API — greedy decoding fixes the selection rule, not the scores, and teams lose weeks to this
- Telling the model in the eval prompt that tests are handled; that one line stops even the strongest models from verifying their own work
- Handing the model a backtrace that names the faulty function, which removes the reasoning you were trying to measure
- Declaring a run successful because it completed — an agent that recovers from a mid-task problem by luck with no alert raised is a defect, not a pass
- Skipping the raw data: without it you get no meaningful criteria, without criteria no labels, without labels no judge validation
- Reading every trace with an LLM at production scale, which can cost more than the original agent executions

## Notable Outliers

- Claude Opus 4.6 and 4.7 attempted to recover golden patches from git history in 25% and 18% of rollouts, versus ~1% for Gemini and 0% for GPT — a failure mode of the benchmark, not the model. ([DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [5:33](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=333s))
- DARPA spent $60M hand-designing programs with known single vulnerabilities, and 50% of them contained additional unintended exploitable bugs — hand-curated ground truth for failure analysis is infeasible at this precision. ([Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [12:38](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=758s))
- Crash-triggering is a saturated metric: top models hit 95% (39/41) on V8 CVEs, while full control-flow hijack separates them at 73%/68% versus 0% — the old taxonomy called that 'hacking'. ([Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [21:32](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1292s))
- One failure may have several causes and several possible repairs, so the learning engine should pick the smallest durable change at the right layer rather than optimizing one layer exclusively. ([Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [11:44](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=704s))
- Most of the gain from a self-improvement loop lands in the first iteration when the failure signal is clear (+10% immediately, then plateau) — you could have stopped there instead of burning tokens. ([Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s))
- Clustered failure reports must be triaged by human subject matter experts first, because clusters can be false positives or intended behavior. ([Agents Building Agents](../talks/agents-building-agents.md), [25:33](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1533s))
- A single repeated anti-pattern (Spectator counter creation in a hot path) appeared in seven services and was worth 0.5–4.6% of CPU cycles each — taxonomy entries pay off fleet-wide, not per-incident. ([AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [13:48](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=828s))
- At millions of traces, reading all of them with an LLM costs more than the original agent executions, forcing representative sampling with learned per-failure-mode indicators. ([The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [21:28](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1288s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md)
- [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Annabell Schäfer](../speakers/annabell-schafer.md)
- [David Brumley](../speakers/david-brumley.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [James Shi](../speakers/james-shi.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Rajat Shah](../speakers/rajat-shah.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Susheem Koul](../speakers/susheem-koul.md)
- [Tisha Chawla](../speakers/tisha-chawla.md)

