---
title: "offline evaluation"
type: "concept"
slug: "offline-evaluation"
tier: "supporting"
maturity: "consolidating"
talk_count: 13
speaker_count: 17
---

# offline evaluation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **13** talk(s) by **17** speaker(s)

**Definition:** Pre-deployment evaluation against fixed datasets and splits, run before shipping rather than against live traffic.

*Also referred to as: pre-registration in eval design, train/test splits for agent evals, train/validation/test splits, counterfactual evaluation, scenario-based evaluation, behavioral evals, oracle ground-truth evaluation*

## State of Practice

Offline evaluation is no longer treated as a static test set run once before launch; the field now builds it as a continuously repopulated private benchmark derived from production traces, executed as a release gate on every change to the agent stack. The dominant design pattern is a simulated or replayed mini-production environment — snapshotted databases, recorded tool fixtures, sidecar containers, LLM-driven user simulators — because A/B testing variants in live traffic can never be repeatable across differing database state and tool versions. Grading has moved away from scalar quality scores toward binary, domain-specific, business-tied pass/fail rubrics, with the judge itself validated like a classifier against roughly a hundred hand-labeled examples and reported with confidence intervals. Verification targets the whole trajectory — final environment state, tool calls, artifacts, cost, latency, retries — not just the final answer, and benchmarks are versioned software with their own CI, Oracle solvability checks, and held-out splits. The recurring humbling lesson is that an easy eval is worse than no eval: Lyft's 90%+ first-pass rate was an artifact of an unrealistically polite simulated user, and cybersecurity benchmarks that scored 'crash the program' as success rated a model at 50% hacking success when its real exploitation rate was 0%. What remains unsettled is how much authority offline results should carry relative to production telemetry, and whether an LLM can be trusted to grade at all.

## Consensus

### Offline eval datasets should be built from real production traffic, traces, and recorded tool responses rather than from synthetic or LLM-generated test cases.

Support: **5** talk(s)

> "It's not a static benchmark. It's a constantly populated data set from your production traces."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [0:52](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=52s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)

### Every organization shipping agents needs its own private benchmark; public benchmarks and leaderboard scores are orientation only and cannot be the basis for a ship decision.

Support: **5** talk(s)

> "public benchmark is useful to orient and build your prior, but your private benchmark is useful to ship."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [3:11](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=191s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### The offline eval suite should function as a hard release gate: no model swap, prompt change, or agent-stack change ships until the full suite shows no regression.

Support: **5** talk(s)

> "we run the whole eval set and we make sure that for example Fable is strictly better than Opus 48 and that gives us the confidence to drop it in"
>
> — [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [16:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1014s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)

### Evaluation criteria should be binary and domain-specific rather than continuous generic quality scores; off-the-shelf helpfulness/correctness/toxicity metrics on a 0-1 or 1-5 scale are low-signal and unactionable.

Support: **3** talk(s)

> "eval should be framed around a task success or failure. And a binary outcome is very easy to calibrate and train um LLM judge that can consistently score your agent trajectory."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [19:32](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1172s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md)

### Evaluation criteria cannot be fully specified in advance; they must be discovered by a human domain expert reading raw outputs and labeling them, and that expert is a build-time requirement for any credible offline eval.

Support: **5** talk(s)

> "The key idea is that we actually discover what our evaluation criteria is by looking at the data and grading our outputs."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [23:02](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1382s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)

### Scoring the agent's final output is insufficient; offline evaluation must verify the trajectory — tool calls, reasoning path, final environment state, and produced artifacts — alongside cost, latency, and retries.

Support: **4** talk(s)

> "Agent traces become the equivalent of distributed tracing for autonomous workloads. Without observability, evaluation becomes the guesswork."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)

### A single run or a small trace sample is not evidence; offline results need repeated seeds, cohort-level aggregation, and confidence intervals before they justify a decision.

Support: **3** talk(s)

> "So which basically means that one replay is just an anecdote and having a cohort analysis is way way way better."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s)

Supporting talks: [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)

### Classical ML validation discipline transfers directly: label a few hundred examples, split into train/dev/held-out sets, and report on data the system has not seen during experimentation.

Support: **3** talk(s)

> "we can hand label around 100 examples with pass fail labels and then split the data into train, dev, and validation sets like how we used to do with machine learning models"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [21:17](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1277s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)

## Disagreements

### Should the authoritative evaluation signal come from a pre-deployment offline suite, or from continuous evaluation of live production traffic?

| Position A | Position B |
|---|---|
| Offline is where you decide. Live users must never be the test set; production A/B comparisons are not repeatable because database state and tool versions drift, and production data ages out before regressions can be detected, so the offline benchmark is the gate you ship against.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)* | Production is where you decide. The highest-value evaluation signal comes from real users on real systems; evaluation belongs in the control plane as an always-on service after deployment, and evals over live traces — not offline evals — are what produce the data for continual-learning loops.<br>*[Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* |

*Why it matters: It determines whether engineering budget goes into building a repeatable simulation/replay environment or into production telemetry and online scoring infrastructure, and whether a failing offline score can block a release at all.*

### Can an LLM be trusted to grade offline eval results, or must the grader be deterministic or human?

| Position A | Position B |
|---|---|
| Yes, with discipline — an LLM judge validated like a binary classifier against hand-labeled data is workable, and the next step is an evaluation agent with full trace access that can score dynamic trajectories and even open a fixing PR.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* | No — in domains with ground truth the grader must be deterministic, because models systematically claim success they did not achieve; and where fidelity is a relation between output and an external archive, an automated metric structurally cannot adjudicate it and a domain expert must.<br>*[Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)* |

*Why it matters: Deterministic oracles and expert review cap how many eval cases you can run, while LLM judges scale to millions per month but can inherit the failure mode they are supposed to detect — the choice sets both the cost curve and the credibility of every reported score.*

### Should the offline environment be a purpose-built simulation the agent runs live against, or a replay of checkpointed real executions?

| Position A | Position B |
|---|---|
| Build a mini-production simulation: snapshotted databases, sidecar containers, an LLM standing in for the user, Oracle-verified tasks, and steps with per-step verifiers — indistinguishable from production so the agent cannot detect and exploit it.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)* | Don't simulate — checkpoint and replay. Grounding every counterfactual in a previously recorded execution (code, artifacts, container state) makes simulations trustworthy in a way ungrounded ones are not; record real tool responses as checked-in fixtures rather than authoring an environment.<br>*[Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)* |

*Why it matters: Simulation covers edge cases and tool failures that never occurred in production but costs an environment-authoring team; replay is cheap and faithful but can only re-examine paths the system already took, so it cannot test genuinely new scenarios.*

## Practical Guidance

**Do:**

- Sample eval cases from production traffic and mutate them to cover both golden paths and edge cases like tool failures and database problems, mirroring integration test design
- Construct an Oracle solution for every benchmark task first, to prove the task is solvable before admitting it to the suite
- Hand-label ~100 examples pass/fail, split train/dev/test, and score the judge on precision and recall like a binary classifier
- Replace scalar quality scores with binary domain-specific checks — 'is the answer grounded in retrieved context, yes/no' rather than 'correctness: 0.7'
- Fine-tune the user simulator on real customer verbatims until the evaluation score goes down, and treat the drop as evidence of realism
- Attach a confidence interval to every reported score; treat 84% vs 88% on 50 traces as indistinguishable
- Hold out a test set (roughly 80/20) that the agent never saw during experimentation, and re-run the whole gate whenever the base model changes
- Treat the benchmark as software with its own CI pipeline: pinned dependencies, pinned base images, fixture-presence checks, and an Oracle-passes check
- Record real downstream tool responses as fixtures checked into the repo so evals replay deterministically after production data is retained away
- Verify final environment state, trace, and artifacts alongside the output, and report cost, latency, and retries next to pass rate
- Make the eval harness config-driven (YAML) so analysts and data scientists can add cases without engineering work, and run it locally, at pre-commit, and in CI
- Reserve expensive statistical rigor for high-stakes moments — ship decisions and leadership reporting — rather than applying it uniformly
- Route failures to their root cause: fix them in the harness, skills, or structured output rather than in the prompt
- Use replay cohorts of hundreds of runs, not one or two, before accepting a cheaper-model swap, and keep a human at the final ship/hold decision

**Avoid:**

- Prompting an LLM for ~50 test queries and calling that an eval dataset
- Believing a 90%+ first-pass rate — check whether your simulated user is unrealistically polite and articulate before celebrating
- Shipping an LLM judge whose score gates nothing; a floating score no one acts on is worthless
- Using pre-built generic metrics (helpfulness, toxicity, conciseness) as core metrics — a 0.5 helpfulness score tells you nothing to act on
- Writing evaluation criteria before you have read raw outputs; not looking at the data breaks labels, criteria, and judge validation downstream
- Letting the agent detect that it is in a simulation — it will reward-hack the environment instead of solving the task
- Scoring a proxy for success (a crash, a single-bug find) instead of the real outcome; crash-triggering is saturated at 95% across frontier models and no longer distinguishes anything
- Handing the model a hint that removes the reasoning step, such as a backtrace naming the vulnerable function
- Assuming a benchmark task has exactly one correct answer or one planted defect — DARPA's hand-curated challenges accumulated unintended bugs in 50% of cases
- Treating production A/B runs as apples-to-apples comparisons across differing database state and tool versions
- Relying on manual end-to-end tests against live production when production data is retained only briefly, making regressions undetectable
- Swapping in a cheaper model on cost and latency alone — the outcome quality loss shows up only in cohort-level replay
- Running an auto-improvement loop against an eval with no plateau detection or escape hatch

## Notable Outliers

- Fine-tune your user simulator until the evaluation score goes down — a falling offline score is the signal that the eval got more realistic, not that quality dropped. ([Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [16:55](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1015s))
- A model that passes τ-bench 60% of the time is self-consistent only about a quarter of the time, so a single replay is an anecdote rather than evidence. ([Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s))
- Oracle retrieval — handing the agent exactly the right memory — still does not reach maximum task performance, because the model can ignore or misuse correct context. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s))
- Rhetorical authenticity must be explicitly excluded as a scoring axis, because rewarding voice validates the exact failure the instrument exists to catch. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [47:19](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=2839s))
- Eval tooling is not the constraint for customers; the skill of writing high-quality evals is what takes a long time. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [49:35](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2975s))
- Most of the gain from a self-improvement loop arrives in the first iteration off a clear failure signal — 68% to 78% — after which it plateaus, partly because the ground-truth labels themselves are noisy. ([Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s))
- Under a broken benchmark definition Kimi appeared to succeed at hacking 50% of the time; under a real exploitation criterion it scored 0%. ([Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [21:32](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1292s))

## All Talks

- [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)
- [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)
- [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Annabell Schäfer](../speakers/annabell-schafer.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Cat Wu](../speakers/cat-wu.md)
- [David Brumley](../speakers/david-brumley.md)
- [Drasko Profirovic](../speakers/drasko-profirovic.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Kunal Lanjewar](../speakers/kunal-lanjewar.md)
- [Marah Abdin](../speakers/marah-abdin.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Robert McHardy](../speakers/robert-mchardy.md)
- [Rustem Feyzkhanov](../speakers/rustem-feyzkhanov.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Stefania Druga](../speakers/stefania-druga.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Varsha Shah](../speakers/varsha-shah.md)

