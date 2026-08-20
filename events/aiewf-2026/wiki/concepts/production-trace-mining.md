---
title: "production trace mining"
type: "concept"
slug: "production-trace-mining"
tier: "core"
maturity: "consolidating"
talk_count: 13
speaker_count: 16
---

# production trace mining

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **13** talk(s) by **16** speaker(s)

**Definition:** Harvesting real production agent transcripts as the raw material for evals, training data, and failure discovery.

*Also referred to as: production trace analysis, production trace evaluation, production trace review, trace mining, agent transcript analysis, production telemetry as eval signal, trace annotation workflow*

## State of Practice

Across evals, continual-learning, and post-training talks, production traces are treated as the single highest-value dataset an organization owns — Meta Superintelligence Labs calls production "the largest and the most representative evaluation data any organization will ever have," Prime Intellect uses deployed-agent traces as source material for RL tasks when no labels exist, and Snorkel replaces the static benchmark with one continuously repopulated from production. The binding constraint has shifted from collecting traces to reading them: millions of traces at millions of tokens each cannot be fed into a judge's context, so the field is converging on agents and code-mode classifiers that mine traces at scale, with human and domain-expert attention rationed to disputed or high-stakes cases (Snorkel: only where agent and verifiers disagree; SonderMind: only where a licensed clinician must define "correct"). A second consensus is negative: production is where you find failures but not where you test fixes — database state and tool versions differ run to run, and A/B tests are unusable below meaningful user volume. Downstream of that agreement the field splits sharply on what traces become: a curated private benchmark under CI, a stream of on-policy rollouts for distillation and RL, seed material for a simulator, or simply a live signal you classify and never curate. The concrete techniques are unusually specific this year — per-step hint injection chosen by a judge, hindsight judging after the full chain of events, token masking of teacher outputs, Oracle solutions to prove task solvability — and they are mostly reports from teams shipping, not settled practice.

## Consensus

### Production traces, not public or hand-built benchmarks, are the primary source material for evaluating and improving deployed agents.

Support: **6** talk(s)

> "Production is the largest and the most representative evaluation data any organization will ever have."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)

### Human or domain-expert judgment on a deliberately narrow slice of traces remains load-bearing and cannot be fully replaced by automated scoring.

Support: **7** talk(s)

> "you don't need subject matter experts to review everything, but you specifically want to find cases where there's disagreement between agent and different verifiers."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [19:13](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=1153s)

Supporting talks: [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)

### Trace volume has outgrown direct reading — mining must be done by agents or code classifiers over traces, not by dumping traces into a context window or into a human's queue.

Support: **4** talk(s)

> "we need to build agents to efficiently mine data from other agents and it's it's no longer as simple as just like feeding the data into context"
>
> — [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [7:15](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=435s)

Supporting talks: [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)

### Trace collection is the precondition for any continual-learning or post-deployment evaluation loop; without it improvement is guesswork.

Support: **4** talk(s)

> "if you're continual learning company, you need traces, and if you have traces, then you can try to do continual learning over your agents."
>
> — [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [2:26](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=146s)

Supporting talks: [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

### Production is where failures are discovered but a poor place to run comparisons: runs are not reproducible and every experiment lands on real users.

Support: **3** talk(s)

> "production traces in comparison are almost free. You don't have to pay for them. You're going to get them anyway. But the cost is that you're testing on real live users every time you're testing it."
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [4:37](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=277s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)

## Disagreements

### Should mined production traces be curated into a durable private benchmark, or treated as a perishable stream you classify but never invest in curating?

| Position A | Position B |
|---|---|
| Build a private benchmark from production traces and treat it as software: Oracle solutions proving solvability, pinned dependencies, its own CI pipeline, an 80/20 train/held-out split, and use it as a release gate. Clinician-authored scenarios get committed so that judgment lives in CI and every prompt, model, and guardrail change is scored against it.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)* | Do not spend months building eval sets. Switching harnesses (e.g. to the Claude Code CLI) invalidates roughly 80% of tool-call evals, and since almost no team would delay a model upgrade two weeks to update evals, the evals were never load-bearing. Invest instead in classifiers-as-code run over the live trace stream plus issue tracking that reports when an issue started and what percentage of users it hits.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* |

*Why it matters: It decides whether trace mining produces a capital asset that gates releases or an operational monitoring practice with no artifact — and therefore whether an eval-infrastructure spend survives the next model or harness swap.*

### Do mined traces belong in weight updates, or in the harness and context layer?

| Position A | Position B |
|---|---|
| Traces are training data. A batch of offline production traces plus teacher hints yields real behavior change without a replayable environment (SWE-bench task-complete rate 22%→60%), and traces from a deployed agent are the best available basis for constructing RL tasks when no labels exist.<br>*[Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* | Try harness engineering first — its feedback loop is about two minutes and most teams never need to go further. Most teams should not train a frontier-level model at all; the durable artifact is company context managed like code, and prompt-level optimization loops plateau after the first iteration anyway.<br>*[Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)* |

*Why it matters: Training pipelines require GPU budget, trace-retention policy, and a data team; harness and context work needs none of those. Choosing wrong either burns months on infrastructure a prompt change would have covered, or caps behavior change at what the harness can express.*

### Can the trace-to-improvement loop close autonomously, or must a human define the target and approve each learning?

| Position A | Position B |
|---|---|
| The loop can close. A judge can pick hint injection points per rollout online and adapt to whatever the production model does; an online loop of generating, solving, and synthesizing tasks gated on pass rate produces benchmark uplift; an evaluation agent with full trace analysis can open the fixing PR itself.<br>*[Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* | Any target function handed to an agent is incomplete, so an unattended loop optimizes toward the wrong optimum; loops need validation mechanisms and an explicit escape hatch. Learnings reverse-constructed from traces must route to a human maintainer for approve/reject, an eval gate alone does not make a system safe, and a licensed expert — not the system — defines correct behavior in edge cases.<br>*[Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)* |

*Why it matters: It sets whether trace mining is staffed as an autonomous system or as a review pipeline with expert headcount, and it determines who is accountable when a self-derived change degrades behavior.*

### Should traces be replayed into a simulated environment, or mined and acted on as-is against live production?

| Position A | Position B |
|---|---|
| Rebuild a mini-production simulation — database snapshot, sidecar containers, LLM-played users — indistinguishable from production to the agent. Simulation compresses the iteration cycle from weeks to under a day, substitutes for most pre-launch A/B tests, and for tools that cannot be programmed, a learned simulator beats the real system because full back-end control lets you plant the answer and guarantee solvability.<br>*[SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* | Replayability is not required. A single one-time dump of offline production traces plus a one-step on-policy rollout delivers value on day one, evaluation should run continuously as an always-on service against live telemetry, and code-mode classifiers scale directly over the real trace stream.<br>*[Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* |

*Why it matters: Simulation is a large infrastructure build whose value depends entirely on closing an unmeasured sim-to-real gap; if traces alone suffice, that build is wasted, and if they don't, teams ship on signal that never reproduces the conditions their agent actually faces.*

## Practical Guidance

**Do:**

- Turn on tracing and point an agent at the traces — treated as the cheapest first move available for improving an agent
- Write trace classifiers as code and execute them in a sandbox over the trace corpus; this scales to production volume where clustering does not
- For every detected issue, capture two facts before triaging: when it started and what percentage of users it affects
- Surface anomaly candidates with deterministic signals such as keyword frequency, then have the agent investigate only those candidates
- Judge in hindsight, after the full chain of events, or by polling several models — more reliable than instructing a judge against failures in advance, and it catches most reward hacks
- Use a judge to choose where in a rollout to inject a hint, and restrict distillation to the next step or a few steps after the hint, since the KL learning signal decays with distance
- Mask which teacher tokens the student learns from with an LLM judge, to avoid absorbing the teacher's irrelevant connector-word preferences
- Verify final environment state, trace, and artifacts — not just the agent's output text
- Construct an Oracle solution for every benchmark task to prove it is solvable before counting a failure against the agent
- Run each integration test many times against a sustained pass-rate bar (Maven uses 90%) rather than accepting a single pass
- Pair automated rubric scoring of production conversations with a dedicated human review group that also checks whether the rubrics themselves are too strict or too loose
- Replace scalar quality scores with binary domain-specific checks — 'is the answer grounded in the retrieved context, yes/no' — since undefined 0–1 scales are inconsistent across runs
- Start on a frontier model only to establish that the task is possible, then use its traces to port the workload to a cheaper open model
- Route fixes to their actual root cause — harness, skills, or structured output — rather than defaulting to the prompt
- Measure and explicitly close the sim-to-real gap before trusting simulation-derived results
- Keep a held-out set the agent has not seen during experimentation (Snorkel defaults to an 80/20 split)

**Avoid:**

- Do not ask an agent to find anomalies; agents are bad at anomaly detection and should only investigate anomalies you already surfaced
- Do not cluster traces as your issue-detection method — clusters are hard to track over time, their boundaries are uncontrollable, and one cluster can span unrelated root causes
- Do not feed raw trace data into a reading agent's context at scale; treat context as an external object the agent queries
- Do not run A/B tests with five or ten users; experiments only pay off at high volume
- Do not assume a golden answer or rubric accompanies each trace — most distillation work wrongly assumes this and real production data does not have it
- Do not do naive SFT on filtered correctly-formatted traces or reward-shape for output format; both degrade general coding-agent performance on out-of-distribution behavior
- Do not let the agent be able to tell it is in a simulation — it will detect and reward-hack the environment
- Do not push every fix into the prompt; the speakers call prompt-patching a industry-wide anti-pattern
- Do not rely on regexes, verbose prompt instructions, or broad moderation APIs to catch clinically coded or indirect risk language in traces
- Do not treat an eval gate as sufficient for safety — only a continuous learning loop from real traces closes the gap
- Do not build append-only memory files with search over them; entries must be updated and compressed or they will not survive multi-year agent-human timescales
- Do not let optimization loops run indefinitely against a plateau; build in validation and an escape hatch or you burn tokens for nothing

## Notable Outliers

- Adding a single on-policy rollout step to an otherwise fully offline production trace produces a larger SWE-bench pass-rate gain than the fully offline setup — one step of on-policy contact is worth more than the rest of the pipeline. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [13:58](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=838s))
- Online per-rollout hints drove correct hyperlink formatting from ~15% to ~80%, while a fixed offline hint applied uniformly barely moved the behavior at all. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [15:21](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=921s))
- Switching harnesses — for example moving to the Claude Code CLI — invalidates roughly 80% of a team's tool-call evals, and most teams would not delay a model upgrade two weeks to repair them. ([Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [4:14](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=254s))
- There is very little genuine continual learning shipping anywhere, at labs or in real products, despite it being a category multiple companies now sell. ([Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [0:01](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=1s))
- For tools you cannot program against, learn a simulator instead — full back-end control lets you plant the answer, guaranteeing the task is solvable, which the real production system can never do. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [12:24](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=744s))
- Trace-judging quality comparable to Opus is achievable with a cheaper open model at one to two orders of magnitude lower cost, demonstrated on Harvey's legal benchmark; for high-inference workloads, running your own cluster beats per-token API pricing. ([Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [8:25](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=505s))
- 80% of Nubank domain-expert labels confirmed simulated data was usable — for greenfield agents as well as mature ones — and simulation cut roughly ten planned A/B tests per quarter down to about one. ([SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [11:16](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=676s))
- In a self-improvement loop over a clean single-label task, the first iteration captured a 10% accuracy gain and everything after was marginal — you could have stopped after iteration one. ([Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s))

## All Talks

- [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)
- [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)
- [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)
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
- [Dan Feng](../speakers/dan-feng.md)
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

