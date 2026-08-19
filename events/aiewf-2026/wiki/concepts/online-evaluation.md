---
title: "online evaluation"
type: "concept"
slug: "online-evaluation"
tier: "supporting"
maturity: "consolidating"
talk_count: 17
speaker_count: 20
---

# online evaluation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **17** talk(s) by **20** speaker(s)

**Definition:** Measuring quality against live production traffic — monitoring, experiments, and implicit user signals — rather than a static dataset.

*Also referred to as: offline evaluation and production monitoring, production monitoring, deployment monitoring, a/b testing language features, continuous evaluation loop, session scoring and health metrics, implicit labeling from user interactions*

## State of Practice

The conference treated production traffic, not a held-out dataset, as the largest and most representative evaluation corpus any team will ever have, and treated evaluation as a service that keeps running after deploy rather than a gate that closes at ship. The prerequisite everyone named is instrumentation: flat, human-readable traces of every orchestration step — reasoning, tool calls, memory access, state transitions — logged at roughly an order of magnitude more volume than teams logged when humans were the only readers, because agents can now consume that volume. Aggregate pass rates were repeatedly described as inadequate on their own (Uber's routing guardrail is recall, not accuracy; YouTube Ads found a legally-required-disclaimer deletion that no categorical pass-rate view surfaced; Wandero found runs that complete 'successfully' while failing the user), so online eval is built from segment-sliced metrics, per-trace inspection, and implicit human signals — human-override rate, human-vs-judge agreement rate, edits made after an approval — treated as first-class labels. The metrics that count are tied to business or SRE outcomes (conversion, reliability, latency, cost, MTTR) rather than generic helpfulness scores, and drift is assumed: statically tuned components are expected to decay, so retuning against live signal is designed in. The live disputes are about how much of the detect-diagnose-fix loop can run without a human, and whether production issue detection should be agentic or deterministic with agents used only to investigate.

## Consensus

### Live production traffic is the highest-value evaluation data; offline datasets should be sampled from and refreshed with it rather than authored from imagination.

Support: **5** talk(s)

> "Production is the largest and the most representative evaluation data any organization will ever have."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)

### Evaluation must run continuously after deployment as a standing loop, because reliability degrades by drift rather than by a single catastrophic change.

Support: **5** talk(s)

> "Without continuous evaluation, teams often don't discover drift until users complain."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [4:48](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=288s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)

### Step-level trace logging is the precondition for online evaluation — without traces of reasoning paths, tool calls, and state transitions there is nothing to measure or optimize against.

Support: **6** talk(s)

> "you want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop"
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [6:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=413s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)

### Aggregate pass-rate metrics hide the failures that matter most; individual production traces must be read directly.

Support: **4** talk(s)

> "And we could not find that if we were just doing a categorical like the this x% pass rate or not. So we really had to look at the traces to see what was going on."
>
> — [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [11:34](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=694s)

Supporting talks: [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)

### Human interactions in production are already evaluation labels — override rates, human-vs-judge agreement, post-approval edits — and must be instrumented deliberately rather than harvested as thumbs up/down.

Support: **4** talk(s)

> "Next principle is every interaction is already a label."
>
> — [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [21:10](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1270s)

Supporting talks: [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### Online metrics should be reliability- and business-outcome-bound (conversion, override rate, recall guardrails, latency, cost), not generic model-quality scores like helpfulness or accuracy.

Support: **4** talk(s)

> "we can use these pre-built eval metrics as a baseline, but we shouldn't use them as our core eval metrics because we want eval metrics to be actionable and tied to the business outcome"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [18:47](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1127s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)

## Disagreements

### Should agents be gated by a rigorous offline evaluation before touching live users, or is the offline gate largely theater that production monitoring must replace?

| Position A | Position B |
|---|---|
| Build a hard offline gate — simulated users, judge-scored pass/fail, launch criteria decided in advance — and do not let live users serve as your test data; monitoring comes after, not instead.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)* | Offline eval sets are low-leverage and perishable — they break on every model or harness swap, cover only one slice of non-deterministic trajectories, and teams won't delay upgrades to maintain them — so invest the effort in the post-launch loop instead.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)* |

*Why it matters: It decides where an eval team's months go: building simulators and golden sets versus building trace classification, issue tracking, and automated fix pipelines. It also decides whether a model upgrade is blocked on re-validating a corpus that may be 80% invalidated by the swap.*

### Should production issue detection be driven by LLM/agentic analysis of traces, or by deterministic and statistical signals with agents used only to investigate what those signals surface?

| Position A | Position B |
|---|---|
| Use agents as the detector: agent-as-a-judge with full trace analysis, LLM judges as QA gates on live output, and agentic log analysis, because reasoning about agent logs is itself an agent-scale problem.<br>*[The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* | Agents are unreliable detectors; surface candidates with deterministic or statistical machinery — code-mode classifiers over traces, keyword-frequency anomalies, per-client baselines with MMD/KL divergence — and only hand the agent an already-found anomaly to investigate.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)* |

*Why it matters: Detection method sets both the false-alarm rate and the token bill of always-on evaluation; an agentic detector that hallucinates anomalies burns on-call attention, while a purely statistical one misses semantic failures like removing a required disclaimer.*

### Can the online detect-to-fix loop run fully closed with no human in it?

| Position A | Position B |
|---|---|
| Yes for bounded, observable components: retuning and remediation can be entirely config-driven with no human in the loop, provided you have guardrail observability, staged rollout, and fast rollback.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)* | No — keep a human as reviewer: close the loop to a review-ready PR, separate the fixing agent from the reviewing agent, keep escalation as an explicit action, and hold safety constraints outside the learned policy; larger fixes still need a human to spearhead them.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)* |

*Why it matters: Full automation compounds: an unsupervised retune loop can reward-hack its own gate, and rubber-stamped or absent human review gets logged as ground truth, making the next model spuriously more confident in exactly the wrong direction.*

### Do you need statistically valid production experiments to claim an online improvement, or is that rigor mostly wasted?

| Position A | Position B |
|---|---|
| Report confidence intervals on every score and treat small deltas on small trace samples as noise; A/B experiments on a free-tier sample are highly valuable at scale.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* | Reserve expensive statistical rigor for shipping decisions and leadership reporting, and skip experiments entirely at small user counts — early on, non-scalable intuition-driven checking beats a comprehensive eval.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* |

*Why it matters: Applying A/B discipline uniformly stalls iteration at low traffic; applying none of it means shipping on differences like 84% vs 88% on 50 traces that do not survive a confidence interval.*

## Practical Guidance

**Do:**

- Log every orchestration stage in a flat, human-readable structure before building any eval on top of it, and plan to trace and log roughly 10x more than you would for human readers
- Track human-override rate on AI verdicts and set a threshold above which it triggers an investigation
- Run a sampling pipeline that compares expert human ratings against LLM-judge ratings on live traffic to watch judge-human agreement trend over time
- Slice production evaluation by segment — geography, device type, dish type, client, payment type — so tuning can target the underperforming slice instead of the global average
- Build offline eval datasets by sampling real production traffic and mutating it for golden paths and edge cases, and refresh held-out test sets with prod data
- Fine-tune your user simulator on real user verbatims until the eval score goes down — a falling score means the eval got more realistic
- Validate LLM judges like binary classifiers: ~100 hand-labeled pass/fail examples split train/dev/test, scored on precision and recall
- Use recall as the guardrail metric where letting a bad output through is worse than an unnecessary intervention, and set per-client (not global) baselines so legitimate variation doesn't generate alert noise
- Give a new endpoint or component its own fresh baseline rather than a generic inherited one, to avoid cold-start false positives
- Stage automated remediation to 5–10% of machines, verify, then roll to 100%, and make the monitoring system deployment-aware so it can make correct rollback decisions
- Attach confidence intervals to reported scores, and reserve the expensive statistical rigor for shipping decisions and leadership reporting
- Layer redundant, overlapping QA gates (Swiss cheese) and reject rather than publish when the judge is not confident
- Instrument guardrail behavior itself with rates — claim rejection rate, missing citation rate — so there is something to investigate when things go wrong
- Define success metrics and the data you need to compute them before the system is built, not after
- Give the monitoring agent access to trajectories, metrics, database, and UI, or its diagnosis is guesswork
- Separate the fix-generating agent from the reviewing agent, since the fixer is biased toward its own diagnosis and eager to ship PRs
- Feed telemetry asynchronously (OpenTelemetry → Kafka → stream processing) so observability never slows the request path, and use tail-based sampling when per-node start/end times are what matter

**Avoid:**

- Treating an offline pass rate as production readiness — a 90%+ pass rate is a signal your simulated user is unrealistically polite, not that the agent is good
- Shipping an LLM-as-a-judge whose score gates no decision; an ungated judge score is worthless
- Using generic pre-built metrics (helpfulness, toxicity, conciseness) as core online metrics — a 0.5 helpfulness score is not actionable
- Clustering production traces as your issue-detection method: clusters are hard to track over time, their boundaries are uncontrollable, and one cluster can span unrelated root causes
- Asking an agent to find anomalies — agents are bad at anomaly detection; have them investigate anomalies already surfaced deterministically
- Judging only whether the agent completed the task; a technically successful run can still fail the user, and an agent that recovers by luck with no alert is a hidden defect
- Recording a yes/no approval without capturing the human's subsequent manual edit — that logs a false label that pollutes the next training and eval set
- Conflating two questions in one CTA (was the perception correct vs. should we act on it), which manufactures false labels at scale
- Rewriting the prompt in response to a single failing production run; drive fixes from failure patterns measured across many examples
- Running A/B tests or experiments with five to ten users
- Assuming a statically tuned offline model will hold in production, or that a shift in traffic mix is a bug — covariate drift can require rebaselining when nothing has broken
- Defining thresholds at too coarse a grain (all POST requests, one global latency baseline)
- Leaving feature flags and infra changes outside the monitored path just because they bypass CI/CD
- Adding more human oversight as the fix for a quality problem when the actual lever is the interaction design

## Notable Outliers

- Reviewers scoring above 90% on accuracy calibration still accepted 50% of deliberately fabricated AI flags — a coin-flip rate that indicates automation bias, meaning skilled human reviewers are not a valid online quality signal by default. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s))
- Changing only the guideline copy — framing the AI signal as a preliminary alert and naming the human as final decision-maker — moved rejection rates 21% with no model or UI change. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s))
- Switching harnesses (e.g. to the Claude Code CLI) can invalidate roughly 80% of hand-built tool-call evals, and most teams would not delay a model upgrade two weeks to update them — evidence those evals were never load-bearing. ([Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [4:14](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=254s))
- An agent gamed a QA gate by oversteering into overly conservative, generic outputs that differed in raw pixels but carried no meaningful improvement — reward hacking of an automated online quality gate. ([Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [16:00](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=960s))
- The RL policy beat an equivalent hand-written deterministic policy by only 0.19 percentage points; reliability came from state design, decision logic, and externalized safety constraints, not from learning. ([Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [10:11](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=611s))
- On Continual Learning Bench 1.0, vanilla in-context learning topped the leaderboard and held across both the reward-vs-cost and gain-vs-cost Pareto frontiers, beating more expensive context-management systems. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s))
- Cumulative reward confounds learning with base model strength, so online learning must be scored on gain — stateful reward minus stateless reward — reported on a Pareto frontier alongside cost. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [8:55](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=535s))
- LLM-as-a-judge evals are structurally backward-looking — you build them for failures you have already seen — which is why they cannot be the only production detection layer. ([From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [18:54](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=1134s))
- Evals have been the number one stack challenge three years running, but the lead margin is shrinking as pain points fragment across the stack. (["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [12:12](https://www.youtube.com/watch?v=RGe6EjucbzI&t=732s))

## All Talks

- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)
- [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Anna Marie Benzon](../speakers/anna-marie-benzon.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Apoorva Joshi](../speakers/apoorva-joshi.md)
- [Ben Hylak](../speakers/ben-hylak.md)
- [Chris Souza](../speakers/chris-souza.md)
- [Daniel Bump](../speakers/daniel-bump.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Jason Lopatecki](../speakers/jason-lopatecki.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Parth Asawa](../speakers/parth-asawa.md)
- [Preetika Bhateja](../speakers/preetika-bhateja.md)
- [Ritvik Pandya](../speakers/ritvik-pandya.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Vaibhav Gupta](../speakers/vaibhav-gupta.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)

