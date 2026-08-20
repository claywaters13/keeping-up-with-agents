---
title: "error analysis and failure taxonomy"
type: "concept"
slug: "error-analysis-and-failure-taxonomy"
tier: "supporting"
maturity: "consolidating"
talk_count: 14
speaker_count: 17
---

# error analysis and failure taxonomy

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **14** talk(s) by **17** speaker(s)

**Definition:** Systematically clustering observed failures into named modes so effort can be aimed at the largest buckets.

*Also referred to as: failure mode clustering, error analysis and failure mode clustering, agent failure taxonomy, error analysis loops, failure mode analysis, root cause analysis for agent failures, crash deduplication via stack backtrace, silent failure detection*

## State of Practice

The conference converged on a specific pipeline: instrument the agent to emit full trajectory traces, mine those traces (weighted toward negative feedback) for recurring failures, give each cluster a name, and promote every named mode into a permanent regression asset — a golden-dataset item, a deterministic evaluator, a stubbed replay test, or a catalogued anti-pattern. The strong claim, repeated across finance, healthcare, ride-hailing, streaming, and security, is that the taxonomy is discovered, not designed: teams that wrote their eval suite before looking at production data got 90%+ pass rates that were artifacts of unrealistic test inputs. Labels should be binary and domain-specific ('answer is grounded in the knowledge base: yes/no', 'repeated Spectator counter allocation in hot path') rather than 0–1 helpfulness scores, because a scalar tells you nothing to fix. Aggregate accuracy is explicitly demoted — reliability, per-cluster hit counts, and cost/latency are what map to business outcomes, and hallucination is treated as one bucket among many rather than the main one. The unresolved parts are all downstream of the taxonomy: who grades (deterministic verifier vs. calibrated LLM judge), how often you mine (continuous control-plane evaluation vs. weekly or per-sprint batch runs, which is a cost decision once trace volume reaches millions), and how much of the fix loop a coding agent may close without a human reading the cluster first.

## Consensus

### The failure taxonomy must be discovered from production traces and real user traffic; it cannot be enumerated in advance, and eval sets written before looking at production data systematically overstate quality.

Support: **7** talk(s)

> "Production is the largest and the most representative evaluation data any organization will ever have."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Agents Building Agents](../talks/agents-building-agents.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)

### Every named failure mode must be promoted into a permanent, rerunnable regression asset (golden-dataset item, replay test, catalogued anti-pattern), or the same class of failure returns.

Support: **5** talk(s)

> "all the failure modes that we are founding during this investigation step, they will become part of the golden dataset that we mentioned earlier and the eval suite is updated to spot those regressions."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [25:33](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1533s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)

### Failure labels should be binary and named per mode, not continuous quality scores, because a scalar score does not tell you what to fix and cannot be calibrated consistently across runs.

Support: **3** talk(s)

> "when you use score-based evals, unless your rubric is very well defined, then this does not exactly tell you what to fix"
>
> — [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [16:53](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1013s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)

### Clusters produced by automated trace analysis must be reviewed by a human with domain expertise before fixes are built, because machine-generated clusters include false positives, intended behavior, and criteria no engineer can judge.

Support: **6** talk(s)

> "review this data and don't review it only with your coding agents but review it as a human."
>
> — [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [15:49](https://www.youtube.com/watch?v=eAXxdtNlK04&t=949s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)

### Remediation should target one named failure class per hypothesis and measure that change in isolation, rather than optimizing against an aggregate pass rate.

Support: **4** talk(s)

> "the system works by creating an hypothesis. So it's tackling one class of problems at a time. It's updating the the agent and it's running the evals again."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [13:32](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=812s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)

## Disagreements

### Should the rare, catastrophic failure modes be waited for in production traffic, or manufactured up front in simulation before any user is exposed?

| Position A | Position B |
|---|---|
| Mine what actually happens: you cannot pre-guess the eval suite, coverage is unbounded, and production is where you learn what to test in the first place.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)* | Define harm categories with a domain expert first and deliberately manufacture the rare dangerous cases in simulation; in patient- or relationship-facing systems the naturally-occurring sample arrives only after someone has been harmed, and a single failing case is unacceptable.<br>*[Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md)* |

*Why it matters: It determines whether your taxonomy is ranked by observed frequency (fix the biggest bucket) or by severity of hypothesized harm (fix the empty bucket that would end the product), and whether simulation infrastructure is a nice-to-have or the gate to launch.*

### Can an LLM judge be trusted to detect and classify failures, or must the grader be deterministic?

| Position A | Position B |
|---|---|
| Graders must be deterministic and code-checkable; models systematically report their own success, produce plausible jargon without understanding, and grade themselves into agreement.<br>*[Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* | An LLM judge is usable once validated like a binary classifier on ~100–240 hand-labeled examples and calibrated for run-to-run variance; validated judges reached F1 0.96 on clinical hazard detection, at least on par with expert clinicians.<br>*[Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)* |

*Why it matters: If judges are untrustworthy, every failure mode needs a hand-built deterministic oracle before it can enter the taxonomy, which caps how fast the taxonomy grows; if they are trustworthy after validation, mining can scale to millions of traces.*

### Should failure detection run continuously as always-on infrastructure, or periodically in batches?

| Position A | Position B |
|---|---|
| Evaluation belongs in the control plane as an always-on service; reliability degrades gradually and without continuous evaluation teams do not discover drift until users complain.<br>*[Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* | Batch the analysis on a fixed cadence — once per sprint, or weekly per service — because reading every trace with an LLM costs more than the original agent executions and requires sampling with learned indicators.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)* |

*Why it matters: At millions of traces the mining bill exceeds the inference bill, so the choice sets both the cost structure of the eval program and the detection latency for a new failure mode.*

### Once a failure cluster is identified, may an agent generate and ship the fix without a human reading the cluster?

| Position A | Position B |
|---|---|
| Automate the loop end to end: if the optimized variant hits target eval scores it ships automatically, and coding agents find fixes humans missed (+10% on an already human-optimized production agent).<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Agents Building Agents](../talks/agents-building-agents.md)* | A human must stay in the approval path — SMEs triage clusters because they can be false positives or intended behavior, agents never push performance fixes to production, and autonomy expands only in proportion to accumulated evidence.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [Agents Building Agents](../talks/agents-building-agents.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)* |

*Why it matters: It sets whether error analysis is a throughput engine (fit more fix cycles into the same window) or a gated safety process, and determines how much verification infrastructure — canaries, regression traps, sandboxing — must exist before the loop can close.*

## Practical Guidance

**Do:**

- Sample eval datasets from production traffic and mutate them to cover golden paths and edge cases, rather than prompting an LLM to invent ~50 test queries.
- Fine-tune your user simulator on real user verbatim until the evaluation score goes down — a falling score means the eval got realistic, not that quality dropped.
- Validate every judge like a binary classifier: hand-label ~100 examples, split train/dev/test, and score precision and recall.
- Weight trace analysis toward sessions with negative feedback, but read positive-feedback traces too, since a technically successful run can still fail the user's task.
- Convert each named failure mode into a code-checkable indicator over time so you can sample traces cheaply instead of reading all of them.
- Attach confidence intervals to reported eval numbers; 84% vs 88% on 50 traces is not a demonstrated gain.
- Keep the pattern/anti-pattern catalog centralized and hierarchically indexed — plain markdown in a shared Git repo works; a vector DB is unnecessary.
- Explicitly forbid the optimizing agent from editing golden datasets or scorers, and run each fix hypothesis on its own branch with rollback on regression.
- Separate the fix-generating agent from the review agent with fresh context, since the fixer is biased toward its own diagnosis.
- Log the full envelope — model version, build ID, RAG chunks — alongside the prompt, so a failing trace can be replayed as a deterministic, zero-cost regression test.
- Build regression-avoidance into the optimization objective itself rather than as a post-hoc check, and give the loop an escape hatch when it plateaus.
- In safety-critical domains, deliberately over-call hazards: false positives are annoying, false negatives are catastrophic.

**Avoid:**

- Not looking at raw traces — without data you cannot form criteria, without criteria no labels, without labels no judge validation, and then you do not know if the pipeline works.
- Generic scalar metrics (helpfulness, toxicity, conciseness on 0–1 or 1–5) as core failure signals; the levels are almost never defined and scores vary run to run.
- Treating hallucination as the primary production failure category — in production it is one bucket among tool failures, API outages, context drift, and long-horizon workflow breakdown.
- Trusting green dashboards and 200 OKs: a catastrophically wrong agent action raises zero exceptions and zero alerts.
- Letting a coding agent read one log and edit the agent directly — the change is untestable and introduces hidden regressions.
- Chasing bitwise determinism or temperature 0 as a debugging strategy; temperature 0 just reproduces the same logical error the same way, and teams burn weeks concluding the system is unknowable.
- Recording at the network layer, since local retrieval, in-process tools, and memory never cross the network.
- Anchoring verifiers to a specific implementation (required names, module placement, private helpers) instead of observable behavior — it inflates false negatives.
- Shipping an agent to production without observability at all, which leaves the team blind to every failure mode.
- Building a self-improvement loop before you have a clear target function; any target you hand an agent is incomplete, and optimizing against it heads toward the wrong optimum.

## Notable Outliers

- Crash-triggering as a failure signal is saturated — top models hit 95% (39/41) on V8 CVEs — so it no longer distinguishes anything; only full control-flow hijack or sandbox escape counts as a real success, where the spread is 73% vs 0%. ([Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [21:32](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1292s))
- Failure taxonomies differ measurably by model family: Claude drops part of a multi-part requirement in roughly two out of three rollouts, and Opus 4.6/4.7 tried to recover golden patches from git history in 25%/18% of rollouts versus ~1% for Gemini and 0% for GPT. ([DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [5:33](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=333s))
- A single line in the prompt saying tests are handled is enough to stop even the strongest models from verifying their own work at all. ([DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [7:09](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=429s))
- Sycophancy is not a polish issue but a named clinical failure mode: repeated one-sided validation returns users to the relationship more certain, more adversarial, and less curious. ([AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md), [6:23](https://www.youtube.com/watch?v=yoONZwV2smc&t=383s))
- One named anti-pattern — repeated Spectator counter object creation in a hot path — recurred in seven Netflix services and was worth 0.5–4.6% of CPU cycles per service, found by cross-repo search once the pattern had a name. ([AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [13:48](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=828s))
- Hand-curating a benchmark to one known failure per program is infeasible: 50% of DARPA Cyber Grand Challenge programs contained unintended exploitable bugs, and AIxCC surfaced 18 more. ([Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [12:38](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=758s))
- An agent that recovers from a mid-task problem by luck, with no alert raised, should be counted as a defect — reliability must not depend on luck. ([The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [4:16](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=256s))
- Most of the gain from a self-improvement loop arrives in the first iteration when the failure signal is clear-cut (68% → ~78%); the remaining iterations barely move it, so you could have stopped there. ([Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md)
- [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Annabell Schäfer](../speakers/annabell-schafer.md)
- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
- [Clay Cockrell](../speakers/clay-cockrell.md)
- [David Brumley](../speakers/david-brumley.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [James Shi](../speakers/james-shi.md)
- [Jared Joselowitz](../speakers/jared-joselowitz.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Rajat Shah](../speakers/rajat-shah.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Susheem Koul](../speakers/susheem-koul.md)
- [Tisha Chawla](../speakers/tisha-chawla.md)
- [Tony Fabrikant](../speakers/tony-fabrikant.md)

