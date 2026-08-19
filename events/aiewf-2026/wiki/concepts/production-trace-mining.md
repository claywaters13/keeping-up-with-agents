---
title: "production trace mining"
type: "concept"
slug: "production-trace-mining"
tier: "core"
maturity: "consolidating"
talk_count: 12
speaker_count: 15
---

# production trace mining

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **12** talk(s) by **15** speaker(s)

**Definition:** Harvesting real production agent transcripts as the raw material for evals, training data, and failure discovery.

*Also referred to as: production trace analysis, production trace evaluation, production trace review, trace mining, agent transcript analysis, production telemetry as eval signal, trace annotation workflow*

## State of Practice

By this conference the field had settled that production transcripts — not benchmarks, not hand-written eval sets — are the highest-value corpus an AI team owns, and that the same trace store feeds three consumers at once: failure discovery, eval/benchmark construction, and training data (SFT, on-policy distillation, RL task synthesis). Meta's framing that benchmarks measure model capability while production measures system behavior, and that the gap widens with autonomy, was echoed across the Evals and Memory tracks. The hard problem has moved from collection to conversion: traces arrive without golden answers, so teams manufacture supervision from them — Oracle solutions to prove task solvability, hindsight judging after the full chain is visible, per-step hint injection chosen by a judge, working backwards from a known-reachable end state. Scale forces a second shift: nobody reads traces anymore, so mining is done by classifiers-as-code run in a sandbox, judge models an order or two of magnitude cheaper than Opus, and agents pointed at other agents' traces — with humans reserved for defining 'correct' and adjudicating disagreement. The live arguments are whether raw production traces or trace-seeded simulation environments are the right substrate, whether mined signal should land in weights or in the harness, and how durable any trace-derived eval set can be when a harness swap invalidates 80% of it.

## Consensus

### Production traces are the highest-value evaluation signal available, and benchmarks or scenario evals alone are insufficient for agentic systems.

Support: **6** talk(s)

> "Production is the largest and the most representative evaluation data any organization will ever have."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)

### Deployed agent traces are usable directly as training/improvement source material, not merely as monitoring output.

Support: **4** talk(s)

> "what we found is super helpful is taking existing traces from a deployed agent and treating these as the source material"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [9:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=581s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)

### Trace mining must assume no golden answer or rubric accompanies the trace; supervision has to be manufactured after the fact.

Support: **4** talk(s)

> "a lot of distillation work is done assuming you have some kind of golden answer that you can distill into the model. And this is often not the case."
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [9:47](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=587s)

Supporting talks: [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)

### Trace volume has outgrown both human reading and naive context-stuffing, so mining must be done by cheap machine-scale readers (classifiers as code, distilled judges, agents reading agents).

Support: **4** talk(s)

> "reading traces at scale is super expensive, uh especially if you have millions of traces and if you have millions of tokens per trace"
>
> — [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [6:29](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=389s)

Supporting talks: [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)

### Evaluation from traces is a continuous post-deployment loop, not a pre-deployment gate.

Support: **4** talk(s)

> "we all know that a simple eval gate does not make a system safe."
>
> — [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [9:12](https://www.youtube.com/watch?v=O72p-rBb2bA&t=552s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)

### Humans, specifically domain experts, must own the definition of 'correct' for trace-derived evals; the mining pipeline surfaces candidates but does not adjudicate them.

Support: **5** talk(s)

> "our system isn't deciding what correct is in a clinical edge case like this one. A licensed professional is."
>
> — [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [11:27](https://www.youtube.com/watch?v=O72p-rBb2bA&t=687s)

Supporting talks: [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

## Disagreements

### Should teams evaluate and iterate on real production traces, or on simulation environments seeded from them?

| Position A | Position B |
|---|---|
| Mine and evaluate the production traces themselves — production is the only representative distribution, and offline trace batches already yield improvement without any replayable environment.<br>*[Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* | Production is not repeatable — database state and tool versions drift, and every test runs on live users — so convert traces into simulated or learned environments and do the iteration there.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* |

*Why it matters: It determines whether you build a trace-mining and classifier stack or a simulation/environment engineering stack, and whether your release gate is a live A/B test or a sim run — Nubank claims the sim path collapses a few weeks of iteration into under a day, while trace-first teams argue sim results are only trustworthy after you have separately measured the sim-to-real gap.*

### Where should improvements discovered in traces be applied — model weights or the harness?

| Position A | Position B |
|---|---|
| Distill or train on the mined traces: hint-guided distillation and RL task synthesis move the model itself, and vertical fine-tunes on trace data can match frontier models.<br>*[Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)* | Fix it in the harness, skills, or structured output first — most teams never need to train, the harness feedback loop is about two minutes, and training on filtered traces measurably degrades out-of-distribution behavior.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)* |

*Why it matters: The weights path requires trace volume, judges, masking, and training infrastructure; the harness path requires none of it. Applied Compute's own numbers show naive SFT on correct traces degrading general coding performance, so choosing the training path without per-step hinting and judge-based token masking can make the agent worse.*

### Can agents be trusted to mine traces autonomously, or must a human read the data?

| Position A | Position B |
|---|---|
| Automate it — send agents to read other agents' traces, let an evaluation agent do full trace analysis and open the fixing PR, and reserve humans for the highest-level judgments about goals and quality.<br>*[The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)* | Humans must review production data directly, because failure modes and usage shift over time, agents are bad at anomaly detection, and self-improvement derived from traces should route to a human maintainer for approve/reject.<br>*[Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* |

*Why it matters: It sets whether trace mining is a staffed function with a domain-expert review budget or a background compute job, and it decides whether agent-authored fixes reach production unreviewed — where a mined 'improvement' can silently break downstream skills or, in clinical settings, ship a miscalibrated guardrail.*

### Is it worth building a durable eval set out of production traces?

| Position A | Position B |
|---|---|
| No — hand-built eval datasets break on every model or harness change (switching to Claude Code CLI invalidated ~80% of tool-call evals), and since nobody would delay a model upgrade two weeks to update them, they were never load-bearing.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* | Yes — every company needs a private benchmark continuously populated from production traces, treated as software with its own CI, pinned dependencies, held-out splits, and release-gate status.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)* |

*Why it matters: One camp invests engineer-months in benchmark infrastructure and gates releases on it; the other spends that time on issue detection over live traces and local code-shaped tests. If Hylak is right, the benchmark investment depreciates with every harness swap.*

## Practical Guidance

**Do:**

- Turn on tracing and point an agent at the trace store as the first, cheapest improvement action.
- Write trace classifiers as code and run them in a sandbox over production volume, rather than clustering traces into issues.
- Use deterministic signals (e.g. keyword frequency) to surface anomaly candidates and give the agent only the investigation step.
- Record, for every mined issue, when it started and what percentage of users it affects — you cannot prioritize without both.
- Judge trace failures in hindsight, after the full chain of events is visible, or by polling several models, rather than instructing a judge against failures in advance.
- Use a judge to choose where in a rollout to inject a hint, and restrict distillation to the next step or a few steps after the injection point, since the KL signal decays with distance.
- Mask which teacher tokens the student learns from with an LLM judge, so the student picks up the target behavior instead of the teacher's connector-word preferences.
- Construct an Oracle solution for every trace-derived benchmark task to prove it is solvable before admitting it to the suite.
- Verify final environment state, the trace, and artifacts — not just the agent's output text.
- Route to subject-matter experts specifically the cases where the agent and the verifiers disagree, instead of asking them to review everything.
- Replace 0–1 or 1–5 quality scores with binary domain-specific checks ('is the answer grounded in the knowledge base, yes/no'), which give usable optimization signal.
- Track cost, latency, and retries alongside pass rate when comparing agent versions.
- Measure and close the sim-to-real gap explicitly before trusting simulation-derived eval results.
- Commit the domain expert's judgment on a flagged trace into CI so every prompt, model, and guardrail change is rescored against it.

**Avoid:**

- Clustering traces as your issue-detection method — cluster boundaries are uncontrollable, hard to track over time, and one cluster can span unrelated root causes.
- Asking an agent to find anomalies in traces; it can only investigate ones you have already surfaced.
- Feeding raw trace data straight into a reading agent's context once you have millions of traces at millions of tokens each.
- Fixing a trace-discovered failure by adding a prohibition to the prompt — locate the root cause in the harness, skills, or structured output instead.
- Running A/B tests as your improvement loop when you have five to ten users, or treating a production A/B as an apples-to-apples comparison at any scale.
- Assuming every mined task comes with a golden answer or rubric.
- Plain SFT on filtered 'correctly formatted' traces or format-targeted reward shaping — both degraded general coding agent performance.
- Letting the agent be able to tell it is running in a simulation, or it will detect and reward-hack the environment.
- Spending months building an eval dataset that a model or harness swap will invalidate.
- Append-only memory files with search on top as the long-term store for what traces teach you.
- Chasing benchmark perfection on trace-derived suites, which drifts focus from the users the benchmark exists to protect.
- Letting optimization loops run against a plateau without traditional-ML validation and an explicit escape hatch.

## Notable Outliers

- Switching harnesses invalidates roughly 80% of hand-built tool-call evals — a concrete depreciation rate for trace-derived eval assets. ([Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [4:14](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=254s))
- A teacher can move a student toward calling a tool purely by reshaping the reasoning path, never touching the tool-call tokens — task-complete rate went from ~22% to ~60% on SWE-bench with test pass rate holding. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s))
- Learned simulators are better RL environments than real production systems, because full back-end control lets you plant the answer and guarantee solvability. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [12:24](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=744s))
- Online hints constructed per-rollout beat a fixed offline hint by a wide margin — ~15% to ~80% correct hyperlink formatting versus a small climb. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [15:21](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=921s))
- An evaluation agent with full trace analysis can go past scoring and open a pull request with the fix. ([The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [5:12](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=312s))
- In a codebase nobody reads, the execution trace is the only remaining way to understand the code — trace mining as a language design requirement, not an ops concern. ([fighting slop with slop](../talks/fighting-slop-with-slop.md), [10:39](https://www.youtube.com/watch?v=AMiyLItEtLA&t=639s))
- Trace-judging quality comparable to Opus is reachable with a cheaper open model at one to two orders of magnitude lower cost, shown on Harvey's legal benchmark. ([Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [8:25](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=505s))
- Most of the gain from a self-improvement loop arrives in the first iteration when the failure signal is clear-cut; the rest is plateau. ([Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s))

## All Talks

- [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)
- [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

## Speakers

- [Akele Reed](../speakers/akele-reed.md)
- [Aman Gupta](../speakers/aman-gupta.md)
- [Annabell Schäfer](../speakers/annabell-schafer.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Ben Hylak](../speakers/ben-hylak.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Rustem Feyzkhanov](../speakers/rustem-feyzkhanov.md)
- [Samuel Denton](../speakers/samuel-denton.md)
- [Shreya Rajpal](../speakers/shreya-rajpal.md)
- [Vaibhav Gupta](../speakers/vaibhav-gupta.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Will Brown](../speakers/will-brown.md)

