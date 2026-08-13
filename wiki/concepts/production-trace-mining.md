---
title: "production trace mining"
type: "concept"
slug: "production-trace-mining"
tier: "core"
maturity: "consolidating"
talk_count: 9
speaker_count: 12
---

# production trace mining

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **9** talk(s) by **12** speaker(s)

**Definition:** Harvesting real production agent transcripts as the raw material for evals, training data, and failure discovery.

*Also referred to as: production trace analysis, production trace evaluation, production trace review, trace mining, agent transcript analysis, production telemetry as eval signal, trace annotation workflow*

## State of Practice

The field has converged on real production transcripts as the highest-value raw material for evaluation — Meta's position that "production is the largest and the most representative evaluation data any organization will ever have" went essentially unchallenged, and Snorkel, Prime Intellect, Arize, and SonderMind all described pipelines whose input is a continuously repopulated stream of deployed-agent traces rather than a static hand-authored set. The unit of harvest is the full trajectory, not the final answer: reasoning path, tool calls, memory access, state transitions, and terminal environment state, because multi-step agents fail in ways (loops, silent tool degradation, drift) that output-only scoring cannot see. What splits the room is what happens next. One camp replays and scores mined traces in place, treating production telemetry as the eval set and pushing evaluation into the control plane as an always-on service; the other treats traces only as seed material for simulated environments — snapshot databases, sidecar containers, LLM-played users — because you cannot run repeatable A/B comparisons against live users and shifting database state. A second live split is how much human gating the loop needs: SonderMind, Langfuse, and Atlan insist a named domain expert owns the definition of "correct" and approves every learned change, while Prime Intellect, Snorkel, and Arize argue humans should be reserved for top-level goal judgments with compute — hindsight judges, verifier disagreement triage, auto-generated PRs — doing the rest. Nobody at the conference argued that a pre-deployment eval gate is sufficient.

## Consensus

### Real deployed-agent traces, not hand-authored test sets or public benchmarks, are the primary source material for evals and training data.

Support: **5** talk(s)

> "Production is the largest and the most representative evaluation data any organization will ever have."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)

### A pre-deployment eval gate is insufficient; evaluation must run continuously on live traffic after release, because reliability degrades gradually rather than in visible single-change failures.

Support: **4** talk(s)

> "we all know that a simple eval gate does not make a system safe."
>
> — [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [9:12](https://www.youtube.com/watch?v=O72p-rBb2bA&t=552s)

Supporting talks: [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)

### Public benchmarks are useful only for orientation; every team shipping agents needs a private benchmark built from its own domain's traces, tools, and policies.

Support: **3** talk(s)

> "public benchmark is useful to orient and build your prior, but your private benchmark is useful to ship."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [3:11](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=191s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)

### Mined traces are unlabeled until a named domain expert defines what correct looks like; the loop cannot discover the target function on its own.

Support: **4** talk(s)

> "the clinical theme owns the definition of good. So vibes don't count here. An accountable judgment from a licensed expert does."
>
> — [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [13:50](https://www.youtube.com/watch?v=O72p-rBb2bA&t=830s)

Supporting talks: [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)

### The unit of evaluation is the whole trajectory — tool calls, state transitions, intermediate artifacts — not the final output, so ordinary application logs are inadequate and full traces are mandatory infrastructure.

Support: **4** talk(s)

> "Agent traces become the equivalent of distributed tracing for autonomous workloads. Without observability, evaluation becomes the guesswork."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md)

## Disagreements

### Should the eval dataset be harvested from live production traffic, or synthesized in simulation with traces used only as seed material?

| Position A | Position B |
|---|---|
| Mine and score real production traces directly — production telemetry is higher-value signal than any scenario-based eval, so evaluation should be moved into the production control plane and run continuously on live traffic.<br>*[Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* | Don't wait on or experiment against production data — traces seed task construction, but evaluation should run in a snapshot 'mini production' (sidecar containers, mocked tools, LLM-played users), because live A/B tests are never apples-to-apples and every production experiment is run on real users.<br>*[SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* |

*Why it matters: It decides whether your investment goes into production observability and control-plane evals or into environment engineering (DB snapshots, tool mocks, Oracle solutions, sim-to-real gap measurement), and whether pre-launch A/B tests stay on the critical path — Nubank claims cutting ten planned A/B tests per quarter to about one.*

### How much human gating does the trace-to-improvement loop need?

| Position A | Position B |
|---|---|
| A licensed or named domain expert must define correctness and approve each learned change; production data must be reviewed by a human, not only by coding agents, because failure modes and usage shift over time.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)* | Reserve humans for the highest-level judgments about goals and quality and let compute do the rest — hindsight judges and polled models catch most reward hacks, SMEs are routed only to verifier-disagreement cases, and an eval agent can go as far as opening the fix PR itself.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* |

*Why it matters: This sets the throughput ceiling of the loop and where the accountability sits: expert-gated loops scale with expert hours (SonderMind ships a clinician's judgment into CI), while compute-gated loops scale with tokens but inherit whatever the judge model gets wrong.*

### When generic LLM-as-a-judge fails on mined agent traces, should judges get more agentic or more constrained?

| Position A | Position B |
|---|---|
| Make the judge an agent — fixed rubrics with fixed scores cannot catch multi-step failures like a subagent looping, so evaluation needs adaptive analysis over the full trace, alongside (not replacing) deterministic and LLM-judge evals.<br>*[The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)* | Make the judge smaller and binary — scalar 0-1/1-5 quality scores are low-signal and inconsistent across runs, so decompose the task into per-step verifiers and yes/no domain-specific checks with a clinician- or expert-authored definition behind each.<br>*[Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* |

*Why it matters: Judge determinism is what makes a mined-trace benchmark usable as a release gate; if the judge itself returns different answers across runs, regression detection and RL reward both become unreliable.*

## Practical Guidance

**Do:**

- Construct an Oracle solution for every task mined from traces to prove it is solvable before admitting it to the benchmark
- Verify final environment state, the trace, and produced artifacts — not just the agent's output text
- Treat the benchmark as software with its own CI pipeline checking pinned dependencies, base images, missing fixtures, and Oracle passes
- Hold out a split (roughly 80/20) the agent has not seen during experimentation, and cover both bread-and-butter paths and edge cases like tool failures and database problems
- Route subject-matter-expert review specifically to cases where the agent and the verifiers disagree, rather than reviewing everything
- Judge in hindsight after seeing the full chain of events, or by polling several models, instead of instructing a judge against failures in advance
- Replace scalar correctness/helpfulness/hallucination scores with binary domain-specific checks (e.g. 'the answer is based on the knowledge base — yes/no')
- Report cost, latency, and retries alongside pass rate when comparing agent configurations
- Score every prompt, model, and guardrail change against the expert-labeled trace set in CI so the expert's judgment lives in the pipeline
- Explicitly measure and close the sim-to-real gap before trusting simulated eval results
- Give optimization loops traditional-ML validation plus an escape hatch so they stop at a plateau instead of burning tokens
- Decompose long-horizon mined tasks into steps with separate prompts and verifiers per step, terminating early when the agent fails
- Calibrate mined tasks to intermediate difficulty — not too easy, not too hard — so the advantage signal separates across rollouts

**Avoid:**

- Fixing a failure discovered in traces by adding a prohibition to the prompt — locate the root cause in the harness, skills, or structured output instead
- Using production A/B tests as the comparison mechanism, since database state and tool versions differ between runs and it is never apples-to-apples
- Letting the agent detect it is running in simulation — it will reward-hack the environment once it knows
- Generic 0-1 or 1-5 evaluators whose levels are never defined, which are low-signal and inconsistent across runs
- Chasing a perfect benchmark score, which drifts focus from the humans the benchmark exists to protect
- Assuming hallucination is the primary production failure mode — it is one category among many for agents
- Per-agent memory systems that each learn separately from their own traces, producing context sprawl and no single version of truth
- Reviewing production data only with coding agents instead of also as a human
- Positioning humans as fallback handlers instead of as the evaluators of the system

## Notable Outliers

- Work backwards from a known-reachable end state, throw away the solution, then have the model learn to find it again — this yields supervision for free without any labels and generalizes well beyond code. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [11:17](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=677s))
- For tools and websites that cannot be programmatically reproduced, learn a simulator of them — full back-end controllability lets you plant the answer and guarantee solvability, making learned simulators better RL environments than real production systems. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [12:24](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=744s))
- An evaluation agent with full trace analysis can go past scoring and automatically open a pull request with the fix. ([The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [5:12](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=312s))
- Fixing one flagged trace through the annotation-to-eval loop lifted the entire self-harm risk category, not just that scenario. ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [12:54](https://www.youtube.com/watch?v=O72p-rBb2bA&t=774s))
- 80% of Nubank domain-expert labels confirmed simulated conversations produce usable eval data — for greenfield agents as well as mature ones — and eval results on sim correlate highly with real production data. ([SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [11:16](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=676s))
- In a codebase nobody fully reads, the execution trace is the only way to understand the code — and full-program tracing can be made effectively zero-cost if designed in from first principles, which is untenable in Python or TypeScript. ([fighting slop with slop](../talks/fighting-slop-with-slop.md), [10:39](https://www.youtube.com/watch?v=AMiyLItEtLA&t=639s))
- General-purpose model guardrails had to be turned off on day one because they are over-calibrated, and an inappropriate guardrail trigger is itself a harm — the objective is trigger accuracy, not trigger frequency. ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [6:24](https://www.youtube.com/watch?v=O72p-rBb2bA&t=384s))
- Most of the gain from a self-improvement loop arrived in the first iteration (68% to ~78%, plateauing near 83%) where the failure signal was clear-cut — you could have stopped there. ([Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s))

## All Talks

- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)
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
- [Dave Revere](../speakers/dave-revere.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Rustem Feyzkhanov](../speakers/rustem-feyzkhanov.md)
- [Shreya Rajpal](../speakers/shreya-rajpal.md)
- [Vaibhav Gupta](../speakers/vaibhav-gupta.md)
- [Will Brown](../speakers/will-brown.md)

