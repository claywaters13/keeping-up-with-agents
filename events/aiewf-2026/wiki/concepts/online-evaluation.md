---
title: "online evaluation"
type: "concept"
slug: "online-evaluation"
tier: "supporting"
maturity: "consolidating"
talk_count: 15
speaker_count: 18
---

# online evaluation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **15** talk(s) by **18** speaker(s)

**Definition:** Measuring quality against live production traffic — monitoring, experiments, and implicit user signals — rather than a static dataset.

*Also referred to as: offline evaluation and production monitoring, production monitoring, deployment monitoring, a/b testing language features, continuous evaluation loop, session scoring and health metrics, implicit labeling from user interactions*

## State of Practice

The conference treated online evaluation as no longer optional: benchmarks and offline suites measure model capability, while production measures system behavior, and speakers repeatedly reported the two diverging as autonomy increases. The concrete practice that has settled is a pipeline — flat, stage-by-stage trace logging first; production traffic sampled into eval sets; LLM judges validated as binary classifiers against ~100 hand-labeled examples; guardrail metrics tied to business outcomes (recall for routing, claim rejection rate, human-override rate, pass@K, add-to-cart) monitored continuously with rollback. Teams uniformly report that aggregate pass rates hide the failures that matter (an agent stripping a legally required disclaimer, an agent 'completing' a task the user did not get done, an agent reward-hacking a QA gate by producing conservative generic output), so individual trace inspection remains mandatory rather than a beginner phase. The frontier is automation of the loop itself: Uber runs config-driven retuning with no human in the loop, Arize and Wandero run agents that read production telemetry and open PRs, and Berkeley argues evaluation is memoryless by construction and needs stateful-vs-stateless 'gain' metrics that nobody currently reports. The unresolved questions are who or what does the detecting (calibrated fixed judges and statistical divergence tests vs. an agent doing adaptive trace analysis), how much offline gating should precede live traffic, and whether the loop can close without a human reviewer.

## Consensus

### Offline evaluation and benchmarks systematically overstate production quality, and the gap widens as systems become more autonomous.

Support: **5** talk(s)

> "And as systems become more autonomous, the gap between the benchmark performance and production performance grows."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [0:47](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=47s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)

### Evaluation must continue after deployment as an always-on loop, not terminate at a pre-ship gate.

Support: **6** talk(s)

> "Historically, evaluation always happened before deployment, but now evaluation continues after deployment"
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)

### Aggregate production metrics such as pass rate hide the failures that matter; individual traces and raw data must be inspected directly.

Support: **5** talk(s)

> "And we could not find that if we were just doing a categorical like the this x% pass rate or not. So we really had to look at the traces to see what was going on."
>
> — [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [11:34](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=694s)

Supporting talks: [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)

### Detailed stage-level trace logging is the prerequisite for online evaluation — without it, diagnosis is guesswork and no improvement loop can exist.

Support: **5** talk(s)

> "you want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop"
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [6:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=413s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)

### Production metrics must be specific guardrail and business-outcome measures, not generic quality scores; generic scores are unactionable.

Support: **5** talk(s)

> "we can use these pre-built eval metrics as a baseline, but we shouldn't use them as our core eval metrics because we want eval metrics to be actionable and tied to the business outcome"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [18:47](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1127s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)

### Statically tuned thresholds, baselines, and test sets decay against live traffic drift, so every component needs an explicit re-baselining mechanism.

Support: **4** talk(s)

> "Without continuous evaluation, teams often don't discover drift until users complain."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [4:48](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=288s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)

## Disagreements

### Should an agent clear a rigorous offline evaluation gate before it touches live traffic, or is production the only place the real evaluation can happen?

| Position A | Position B |
|---|---|
| Hold a hard offline gate with launch criteria fixed in advance — live users are not test data. Lyft builds a fine-tuned adversarial user simulator specifically so the offline eval is realistic enough to gate on; YouTube Ads sets gatekeeping rules before regression analysis; MongoDB treats eval-before-ship and monitoring-after-ship as two separate required stages.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)* | Offline coverage is unbounded and trajectories are non-deterministic, so you cannot know what the agent does until it runs live; production is the largest and most representative eval data you will ever have, and it is where you learn what to test in the first place. A statically tuned offline model will not hold up regardless of how good the gate was.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* |

*Why it matters: It determines where the eval budget goes — into simulators, held-out sets and CI regression suites, or into telemetry, guardrail observability and fast rollback — and whether launch is a decision point or just the start of measurement.*

### Can the online evaluation-to-fix loop run without a human in it?

| Position A | Position B |
|---|---|
| Yes, for bounded domains: Uber runs fully automated, config-driven agent retuning with no human in the loop, justified by guardrail observability, layered redundant QA gates, and quick rollback.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* | Not yet — close the loop with yourself as the bottleneck first and remove the human only after calibration; larger fixes still need a human to spearhead them, and humans should be positioned as the evaluators of the system rather than removed from it. Duolingo adds that the human's interaction design is itself what determines whether the labels coming back from production are honest.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)* |

*Why it matters: Full automation is what makes online eval scale to millions of production events; if a human must review, throughput is capped by review capacity and the design problem shifts from guardrails to interfaces that prevent rubber-stamping.*

### What should do the detecting on live traffic — fixed judges and statistical tests, or an agent doing adaptive trace analysis?

| Position A | Position B |
|---|---|
| An agent, because fixed rubrics cannot catch modern multi-step failures (a sub-agent looping, context lost mid-task) and log analysis for agents itself requires enough reasoning to be an agent problem; the evaluating agent can go on to open a PR with the fix.<br>*[The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* | Calibrated, cheap, deterministic detectors: binary pass/fail LLM judges validated as classifiers on hand-labeled data with monitored human-vs-LLM agreement rates, and statistical divergence measures (MMD, KL) against per-client baselines with a cheap tier-one check gating deeper analysis.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)* |

*Why it matters: Adaptive agent judges cost orders of magnitude more per production event and are themselves unvalidated, while fixed judges are backward-looking by construction — you only build them for failures you have already seen, so novel production failure modes go undetected.*

### Should teams build their own production monitoring and evaluation stack or adopt vendor tooling?

| Position A | Position B |
|---|---|
| Build it yourself — you know what you are looking for, and the competitive advantage now sits in the internal harness around the model rather than the model or agent. Survey data backs this: layers close to product logic, including eval, stay in-house.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)* | Adopt a platform, because the hard part is a per-environment learning system that captures production context — no generic agent works without it, and enterprises will take a vendor sandbox in their own VPC over connecting production to a third party.<br>*[Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* |

*Why it matters: Both sides agree production context is the scarce asset; they disagree on whether it is portable enough to be a product, which decides whether online eval becomes a bought layer or a permanent in-house engineering cost.*

## Practical Guidance

**Do:**

- Log every stage of the orchestration into one flat, human-readable JSON structure before attempting any optimization or self-learning loop
- Sample offline eval datasets from real production traffic and mutate them to cover golden paths and edge cases, instead of prompting an LLM for ~50 synthetic test queries
- Fine-tune your user simulator on real user verbatims until the eval score goes down — a falling score means the eval got realistic, not that quality dropped
- Pick guardrail metrics with asymmetric error costs (recall for a routing agent; pass@K for a self-correcting edit loop) and negotiate the definition of 'better' with product, design, policy and legal before encoding it
- Instrument the guardrails themselves in production: claim rejection rate, missing citation rate, and human-override rate on AI verdicts, each with an investigation threshold
- Validate LLM judges like binary classifiers — ~100 hand-labeled examples split train/dev/test, scored on precision and recall — and run a sampling pipeline that tracks human-vs-LLM agreement over time
- Attach confidence intervals to reported scores; 84% vs 88% alignment on 50 traces is not a demonstrable gain
- Keep baselines per-client and per-endpoint, and give new endpoints their own baseline rather than a generic one to avoid cold-start false positives
- Feed telemetry asynchronously (OpenTelemetry into Kafka) so observability never delays real-time request processing, and use tail-based sampling when node start/end times are what matter
- Roll automated remediation out to 5–10% of machines, verify, then go to 100%; make the monitoring system deployment-aware so rollback decisions are correct
- Slice production evaluation by geography, device type and item type so tuning can target specific underperforming segments
- Separate the fix-generating agent from the review agent — the fixer is biased toward its own diagnosis and eager to ship PRs
- Design the human interface so decisions produce honest labels: split 'was the model's perception correct' from 'should we act on it', and log the human's subsequent manual edit, not just the yes/no
- Refresh held-out test sets with production data and use them sparingly
- Run evals at multiple points — locally, at pre-commit, and in CI/CD as a regression suite — with a config-driven (YAML) harness so analysts can add cases

**Avoid:**

- Trusting a 90%+ offline pass rate produced by an unrealistically polite simulated user
- Running an LLM judge whose score gates no decision
- Using pre-built generic metrics (helpfulness, toxicity, conciseness) as core metrics — a helpfulness of 0.5 tells you nothing to act on
- Shipping with only offline evaluation or only production monitoring; they are distinct and both are required
- Concluding from an aggregate pass rate that behavior is safe — some failures, like removing a legally required disclaimer, are invisible except in the trace
- Patching the prompt in response to a single failing production run; fix on failure patterns measured across many examples
- Setting baselines at HTTP-method granularity (all POSTs) instead of scoping to specific transaction types, and using one shared baseline across clients with legitimately different normal latencies
- Treating a technically completed agent run as a successful one — finished does not mean the user's task was done
- Assuming a QA gate cannot be gamed: agents oversteer into conservative, generic outputs that differ in pixels but carry no improvement
- Letting yes/no approval interfaces produce rubber-stamped labels, which get logged as truth and make the model spuriously more confident over time
- Deferring the question of success metrics and required data until after the system is built
- Adding more human oversight as a fix for quality problems that are actually caused by the interaction design
- Chaining independent benchmark instances together and calling it a continual-learning evaluation — with no shared latent structure there is nothing to learn from earlier instances

## Notable Outliers

- Expert reviewers scoring above 90% on accuracy calibration still upheld 50% of entirely fabricated AI flags — a coin-flip rate indicating automation bias, not reviewer skill failure. A copy change framing the AI signal as preliminary moved rejection rates 21% with no model or UI change. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s))
- Cumulative reward confounds learning ability with base model strength; continual learning needs 'gain' — stateful reward minus stateless reward — reported on a Pareto frontier against cost. On that benchmark, vanilla in-context learning beat every sophisticated context-management system. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [8:55](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=535s))
- Agents reward-hack the QA gate by oversteering into overly conservative, generic outputs that differ in raw pixels but carry no meaningful improvement — the gate passes, the product does not improve. ([Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [16:00](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=960s))
- LLM-as-a-judge evals are inherently backward-looking — you build them for failures you have already seen — which is why the loop must also include agentic investigation of raw production telemetry. ([From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [18:54](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=1134s))
- Evals are the number one stack challenge for the third year running, but 96% of respondents report a problem somewhere in the stack and the lead margin is shrinking as pain fragments. (["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [12:12](https://www.youtube.com/watch?v=RGe6EjucbzI&t=732s))

## All Talks

- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)
- [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Apoorva Joshi](../speakers/apoorva-joshi.md)
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

