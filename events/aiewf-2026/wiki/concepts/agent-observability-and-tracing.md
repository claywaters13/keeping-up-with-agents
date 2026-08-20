---
title: "agent observability and tracing"
type: "concept"
slug: "agent-observability-and-tracing"
tier: "core"
maturity: "consolidating"
talk_count: 34
speaker_count: 39
---

# agent observability and tracing

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **34** talk(s) by **39** speaker(s)

**Definition:** Instrumenting agent runs so every step, tool call, and token is inspectable after the fact — spans, traces, and the tooling that renders them.

*Also referred to as: agent observability, agent trace observability, llm observability, distributed tracing for agents, trace-based observability, agentic observability, session tracing*

## State of Practice

The field has stopped treating tracing as a debugging convenience and now treats it as the load-bearing substrate for everything downstream: evaluation, continual learning, memory, and automated repair. Traditional logs are considered inadequate because what matters for an autonomous run is the chain of decisions — planning steps, tool inputs and outputs, memory access, state transitions — not the final answer, and multiple speakers report that failures invisible in aggregate pass-rate metrics (an agent detecting and then deleting a legally required disclaimer; a wrong trade with zero exceptions and green dashboards) are only findable in traces. Because agents are non-deterministic and their coverage is unbounded, production is now openly treated as the largest and most representative eval set an organization will ever have, which inverts the old order: instrument first, then discover what to test. The volume this creates has outrun human review, so the emerging pattern is agents reading other agents' traces — with code-mode classifiers, learned per-failure-mode indicators, and representative sampling used to keep the mining cost below the cost of the original executions. The live arguments are about representation and economics: whether an emitted OTel span is enough or whether you need checkpointed, replayable execution state; whether to log ten times more or invest in sampling; and how much of the detect→diagnose→fix→ship loop can run without a human at the gate.

## Consensus

### Conventional logs are insufficient for agents; you need step-level traces of reasoning, tool calls, memory access and state transitions, because failures are invisible in final output and aggregate metrics.

Support: **6** talk(s)

> "Agent traces become the equivalent of distributed tracing for autonomous workloads. Without observability, evaluation becomes the guesswork."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)

### Production telemetry is the highest-value evaluation dataset; pre-production tests, offline eval sets and benchmarks cannot cover agent trajectories, so you learn what to test only after shipping.

Support: **7** talk(s)

> "production is the place when you learn what you need to uh what you need to test on the first place."
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [5:36](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=336s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)

### Trace volume has exceeded human reading capacity, so trace analysis itself must be done by agents — with sampling, learned indicators or cheaper models — rather than by people clicking through a dashboard.

Support: **6** talk(s)

> "Before, you wouldn't do that because because humans can't dig through all the logs. It's just noise."
>
> — [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [9:46](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=586s)

Supporting talks: [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)

### Instrumentation must be built before optimization, evals or scaling — observability is a prerequisite foundation, and it is ordinary engineering work rather than an AI problem.

Support: **5** talk(s)

> "you want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop"
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [6:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=413s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

### Traces are not just for debugging — they are the substrate agents learn from: session logs feed memory, skills, retrieval ranking and cross-agent data-source selection.

Support: **5** talk(s)

> "So, densifying feedback is uh really good way to improve agents, and like traces are the substrate that hold that feedback."
>
> — [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [15:23](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=923s)

Supporting talks: [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)

### A useful trace must span the entire trajectory and stack — trigger, context assembly, every tool output, database and permission errors, harness behavior — not just LLM calls and tool calls.

Support: **5** talk(s)

> "So, if you can't see the entirety of a trace from the trigger through the whole stack, it's really hard to debug it, let alone improve your agent and keep evolving it."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [9:08](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=548s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)

## Disagreements

### Is an emitted trace sufficient to debug and improve an agent, or must you record replayable execution state?

| Position A | Position B |
|---|---|
| Traces (OTel spans, logged tool inputs/outputs, session transcripts) are the substrate — turn on tracing, point an agent at it, and deliver the selected data to a coding harness as files.<br>*[Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)* | Traces are structurally insufficient because they are read-only artifacts disconnected from the runtime — they discard in-flight variables, filesystem state, sandbox image and the executing code — so you must checkpoint state at each node boundary and replay it.<br>*[Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)* |

*Why it matters: It decides whether you buy a tracing platform or build a checkpointing runtime underneath your harness, and whether a production incident can become a free, deterministic regression test or only an input to a fresh investigation.*

### Now that agents can consume telemetry, should teams log an order of magnitude more, or is trace volume itself the binding cost constraint?

| Position A | Position B |
|---|---|
| Trace and log roughly 10x more than today, because agents can dig through volumes of telemetry that humans never could and the path the code took is what enables the fix.<br>*[From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* | Reading traces at scale is the expensive part — at millions of traces, LLM review costs more than the original executions — so invest in representative sampling, code-checkable failure indicators, cheaper open models for judging, and tail-based sampling instead of capturing more.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)* |

*Why it matters: Retention and sampling policy set both the observability bill and the ceiling on what automated trace mining can find; at scale, telemetry collection becomes a meaningful share of system load and latency in its own right.*

### Should teams build their own agent observability and monitoring layer, or treat it as undifferentiated infrastructure to outsource?

| Position A | Position B |
|---|---|
| Build it yourself: you know what you're looking for, evals and classifiers belong in your codebase as tests and sandboxed code, and black-box vendor 'SRE agent' products are the wrong shape — the harness, sandbox and skills should be open and user-selectable.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* | Hosting, session management, sandboxing, credentials and observability are undifferentiated work; developers should own only system prompts, skills, tools and domain context, and get the durable session log from the harness.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* |

*Why it matters: This determines where the durable session log lives and who controls it, which in turn governs whether enterprises can keep traces and production connections inside their own VPC.*

### When automated trace analysis produces a fix, can it ship to production without a human reviewing it?

| Position A | Position B |
|---|---|
| Yes, if guardrail observability and fast rollback exist: config-driven retuning and optimized agent variants that hit target eval scores can be shipped automatically with no human in the loop.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)* | No — the agent should stop at an evidence-backed issue or a code review; modifying working production code is risky, a single replay is an anecdote, and human supervision is a permanent feature rather than a temporary stage.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* |

*Why it matters: It sets the throughput ceiling of the improvement loop against blast radius, and determines whether your verification investment goes into canaries and cohort replay or into human review capacity.*

## Practical Guidance

**Do:**

- Log every stage of the orchestration in one flat, human-readable JSON structure before attempting any optimization or self-learning loop
- Record at each node boundary — what enters and what leaves each step — rather than at the network layer, since local retrieval, in-process tools and memory never cross the network
- Capture the full envelope alongside the prompt: LLM version, build ID and RAG chunks, or the trace cannot be replayed
- Trace the whole session from trigger through database errors, permissions issues and performance, not just LLM and tool calls
- Write trace classifiers as code and run them in a sandbox over traces; use deterministic signals such as keyword frequency to surface anomalies and let the agent only investigate ones already found
- Track two things per issue: when it started and what percentage of users it affects
- Feed telemetry asynchronously to OpenTelemetry with Kafka/stream processing downstream, and use tail-based sampling, so instrumentation does not add latency to the request path
- Give new endpoints their own baseline instead of a generic one, to avoid cold-start false positives
- Deliver the selected trace data to a coding harness as files in the repo — 10MB files work — rather than pointing the agent at a raw data source
- Render long time-series metrics as images so input token count is fixed regardless of job duration, and expose logs through tools that return top-K truncated exceptions plus a drill-down
- Separate the fix-generating agent from the review agent, giving the reviewer fresh context, because the fixer is biased toward its own diagnosis
- Ask the agent for a short retrospective at the end of every invocation — what went well, what went wrong, what tools were missing — as a stopgap for missing agent observability tooling
- Store sensitive payloads in schema-driven object storage that the event log only references, so developers can retrace agent behavior while seeing only the schema
- Run observability over tool calls before deploying: check how long each tool runs and how many times loops repeat, and always cap max iterations
- Collect code-checkable indicators per failure mode over time so sampling stays cheap at millions of traces
- Make anomaly output explainable with supporting evidence rather than a single opaque score

**Avoid:**

- Treating aggregate pass-rate metrics as sufficient — failures like an agent detecting and then removing a legally required disclaimer are only visible in the trace
- Trusting green dashboards and 200 OK responses; a catastrophically wrong action produces no exception and no alert
- Clustering traces and treating clusters as issues — clusters are hard to track over time, have uncontrollable boundaries, and one cluster can span unrelated root causes
- Asking an agent to detect anomalies rather than investigate ones you already found deterministically
- Chasing bitwise determinism or pinning temperature to zero as a debugging strategy; it fixes the selection rule, not the underlying scores, and removes the randomness that gives the agent its agency
- Shipping on the basis of one or two replays instead of cohort-level analysis
- Using a sandbox for durability, snapshots or state — sandboxes are ephemeral and stateless by design
- Confusing a developer log with a compliance audit trail, which must record every action, every data access and every authorization
- Hyperfixating on a single failing run when patching prompts; drive fixes from failure patterns measured across multiple examples
- Letting eval results and traces die in a dashboard with no path back into the agent's context, skills or retrieval
- Relying on deterministic telemetry alone to catch violations where the agent never exceeded its authorization and the system looks compliant throughout
- Manual end-to-end testing against live production as your regression strategy, since production data is retained only briefly and regressions become undetectable

## Notable Outliers

- The hardest agent failures are the ones where the agent never exceeds its authorization — the system looks compliant the entire time, so egress filters, sandboxes, auditability and telemetry are necessary but not sufficient. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [10:16](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=616s))
- Determinism was never the goal — debugging was; the right question is how to debug and retest a run you cannot reproduce, and you should capture what the model did rather than freeze the model. ([Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [4:49](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=289s))
- Agents are very bad at anomaly detection — don't ask an agent to find anomalies, ask it to investigate anomalies you have already found deterministically. ([Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [18:30](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=1110s))
- A single replay is just an anecdote; on tau-bench a model that passes 60% of the time is only self-consistent about a quarter of the time, so decisions require cohort analysis. ([Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s))
- Developers can debug and retrace an agent's steps while seeing only the schema of the data and never the protected health information itself, because the event log references immutable object storage rather than carrying the payload. ([Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [11:16](https://www.youtube.com/watch?v=mav15aW9lLM&t=676s))
- At sufficient scale, observability becomes a meaningful part of the system load itself — collecting logs is hard and processing them is harder. ([How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [14:11](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=851s))
- Feeding raw time-series metrics to an LLM fails for long-running jobs; rendering them as images guarantees a fixed input token count regardless of job duration. ([Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s))
- An anomaly reported as a single score is useless — like a doctor telling you your health score is 22; detection output must come with the supporting data that explains it. ([Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [18:13](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=1093s))

## All Talks

- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
- [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)
- [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)
- [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)
- [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
- [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)
- [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)
- [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)
- [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)
- [Your AI Product Will Fail Unless You Can Explain It](../talks/your-ai-product-will-fail-unless-you-can-explain-it.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Abed Matini](../speakers/abed-matini.md)
- [Arjun Singh](../speakers/arjun-singh.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
- [Ben Hylak](../speakers/ben-hylak.md)
- [Chris Souza](../speakers/chris-souza.md)
- [Christopher Lovejoy](../speakers/christopher-lovejoy.md)
- [Dan Farrelly](../speakers/dan-farrelly.md)
- [Daniel Bump](../speakers/daniel-bump.md)
- [Dat Ngo](../speakers/dat-ngo.md)
- [Drasko Profirovic](../speakers/drasko-profirovic.md)
- [Emil Eifrem](../speakers/emil-eifrem.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Jason Lopatecki](../speakers/jason-lopatecki.md)
- [Jia Wu](../speakers/jia-wu.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Kunal Lanjewar](../speakers/kunal-lanjewar.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Moritz Johner](../speakers/moritz-johner.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)
- [Preetika Bhateja](../speakers/preetika-bhateja.md)
- [Rajat Shah](../speakers/rajat-shah.md)
- [Ritvik Pandya](../speakers/ritvik-pandya.md)
- [Saul Howard](../speakers/saul-howard.md)
- [Shashi](../speakers/shashi.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Susheem Koul](../speakers/susheem-koul.md)
- [Tisha Chawla](../speakers/tisha-chawla.md)
- [Vaibhav Gupta](../speakers/vaibhav-gupta.md)
- [Veronica Hylak](../speakers/veronica-hylak.md)
- [Victor Savkin](../speakers/victor-savkin.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)

