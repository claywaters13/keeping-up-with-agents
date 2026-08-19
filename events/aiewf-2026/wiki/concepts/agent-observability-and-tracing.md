---
title: "agent observability and tracing"
type: "concept"
slug: "agent-observability-and-tracing"
tier: "core"
maturity: "consolidating"
talk_count: 32
speaker_count: 36
---

# agent observability and tracing

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **32** talk(s) by **36** speaker(s)

**Definition:** Instrumenting agent runs so every step, tool call, and token is inspectable after the fact — spans, traces, and the tooling that renders them.

*Also referred to as: agent observability, agent trace observability, llm observability, distributed tracing for agents, trace-based observability, agentic observability, session tracing*

## State of Practice

The conference treats step-level tracing as table stakes and traditional logs as obsolete: what has to be captured is the chain of decisions — reasoning steps, every tool input and output, memory access, state transitions — because for a non-deterministic agent the path matters more than the final answer. The consumer of that telemetry has flipped from a human clicking a Grafana-style dashboard to an agent reading traces and filing or fixing issues, which changes the design constraints: trace volume that was noise to humans is now signal, but reading it all with an LLM at millions of traces costs more than the agent runs themselves, so representative sampling, code-written classifiers, and learned failure indicators replace ad-hoc inspection. Aggregate pass rates and green dashboards are explicitly distrusted — several teams reported catastrophic behavior (removing a legally required disclaimer, selling 1,000 shares instead of $1,000) that produced no exception, no alert, and no metric movement. Production is now the primary evaluation corpus, with offline suites treated as a small held-out sample refreshed from prod. The live frontier is whether a trace is enough at all: two teams argue a read-only span sitting in a vendor tool, disconnected from the code, in-flight variables, and filesystem state, cannot answer why a run went wrong, and push for checkpointed runtimes and deterministic replay instead. Instrumentation point is converging on the execution layer / session log — one durable record that serves debugging, evaluation, replay, and memory self-improvement.

## Consensus

### Traditional logs are insufficient for agents; you need step-level traces of reasoning paths, tool calls, and state transitions, because the chain of decisions matters more than the final output.

Support: **7** talk(s)

> "Agent traces become the equivalent of distributed tracing for autonomous workloads. Without observability, evaluation becomes the guesswork."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### Aggregate metrics — pass rates, completion signals, HTTP status, green dashboards — hide the failures that matter; the failure is only visible by inspecting the trace.

Support: **5** talk(s)

> "And we could not find that if we were just doing a categorical like the this x% pass rate or not. So we really had to look at the traces to see what was going on."
>
> — [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [11:34](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=694s)

Supporting talks: [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)

### The primary consumer of agent telemetry is now another agent, not a human staring at a dashboard — traces feed automated triage, diagnosis, and fix loops.

Support: **6** talk(s)

> "the future observability actually looks a lot more like this than it does clicking around graphana UI"
>
> — [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [5:08](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=308s)

Supporting talks: [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### Production traffic is the largest and most representative evaluation corpus; you cannot know what the agent will do from pre-release test suites, so offline sets should be small, used sparingly, and refreshed from prod.

Support: **5** talk(s)

> "production is the place when you learn what you need to uh what you need to test on the first place."
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [5:36](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=336s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### Instrumentation is a prerequisite, not a later phase: without logging in place first there is nothing to optimize against and no self-improvement loop is possible.

Support: **4** talk(s)

> "you want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop"
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [6:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=413s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)

### Execution traces are a learning substrate, not just a debugging artifact — trace outcomes should feed back into memory, skills, retrieval ranking, and data-source selection.

Support: **5** talk(s)

> "The eval signal dies in the dashboard. This is a missing layer, a system that consume traces, absorb eval, and convert both into retrieval guidance for future runs."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [2:35](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=155s)

Supporting talks: [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)

## Disagreements

### Is an emitted trace a sufficient record of an agent run, or must you checkpoint the full runtime state so runs can be replayed?

| Position A | Position B |
|---|---|
| Traces are the substrate: turn on tracing, ship spans to an observability backend, and point agents at them to mine failures and drive fixes.<br>*[Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)* | A trace is a read-only artifact stamped at the end and stranded away from the code — in-flight variables, filesystem state, and the executing code are all discarded; you need a checkpointing runtime that records what enters and leaves each node so the run can be replayed and diffed.<br>*[Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)* |

*Why it matters: It decides whether observability is a telemetry pipeline you bolt on or a durable runtime layer you build your harness on top of, and whether regression tests come from curated eval sets or from replaying real production runs with single nodes stubbed.*

### Should teams dramatically increase how much they trace and log, or is telemetry volume itself now the binding cost constraint?

| Position A | Position B |
|---|---|
| Trace and log roughly 10x more than today, because agents can consume volumes of telemetry that humans never could, and without it you are guessing which of a million code paths ran.<br>*[From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* | Volume is the problem: reading millions of traces with an LLM costs more than the agent executions did, collecting and processing logs becomes a meaningful share of system load at scale, and replay is expensive — so sample representatively, learn code-checkable failure indicators, and be deliberate about what you keep and what you re-run.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)* |

*Why it matters: Retention and sampling policy is set once and is expensive to reverse; over-collect and the analysis bill exceeds the inference bill, under-collect and the failure you need to diagnose was never recorded.*

### Should anomaly and failure detection over agent traces be deterministic/statistical, or should an agent do the detection?

| Position A | Position B |
|---|---|
| Agents are unreliable at detecting anomalies; use deterministic signals — keyword frequency, MMD/KL divergence against per-client baselines, code-written classifiers run in a sandbox — to surface candidates, and only let the agent investigate what has already been flagged.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)* | Analyzing agent sessions requires enough reasoning that it cannot be done with scripts, regex, and filters — operating the agent is itself an agent problem, and reasoning-and-acting agents beat deterministic workflow graphs at root-cause diagnosis.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)* |

*Why it matters: It sets what you build first — a statistics and baseline pipeline versus a diagnostic agent with tools — and determines whether detection cost scales with traffic volume or with token spend.*

### Should the agent observability and monitoring layer be built in-house or bought as infrastructure?

| Position A | Position B |
|---|---|
| Build it: hosting a session watcher yourself is how you encode what you actually care about, and evals belong in your repo as local code tests rather than in a managed cloud product.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* | Hosting, session management, sandboxing, credentials, and observability are undifferentiated work that should come from the harness or a vendor — with the caveat that enterprises will only accept it running inside their own VPC.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)* |

*Why it matters: Determines where the durable session record lives and who owns it, which in turn constrains whether production data can be routed to a third party at all.*

## Practical Guidance

**Do:**

- Log every stage of an end-to-end orchestration in one flat, human-readable JSON structure before attempting any optimization or self-learning loop
- Capture the full envelope alongside the prompt — LLM version, build ID, RAG chunks retrieved — or the run is not replayable
- Record at each node's boundary (what enters and what leaves), not at the network layer, since local retrieval, in-process tools, and memory never cross the network
- Make the trace span the entire stack from trigger onward — database errors, permission failures, scheduling, performance — not just LLM and tool calls
- Instrument in the execution layer, where user input, feedback, actions, and session results all already flow through
- Write issue detectors as code and run them in a sandbox over traces; let agents investigate anomalies you have already surfaced deterministically
- Track, per issue, when it started and what percentage of users it affects — without both you cannot prioritize
- Scope baselines narrowly: per client, per payment/endpoint type, with new endpoints getting their own baseline to avoid cold-start false positives
- Emit telemetry asynchronously (OpenTelemetry → Kafka → stream processing) with tail-based sampling so observability never delays the request path
- Hand trace data to a coding agent as files checked into the repo — these harnesses work well with files, even ~10MB ones — rather than pointing the agent at a data source
- Evaluate the whole trajectory: was context complete, was every intermediate tool output correct, and did the harness itself contribute to the failure
- Learn code-checkable indicators per failure mode so you can sample representatively instead of reading every trace
- Snapshot real downstream tool responses as fixtures checked in as code, and run offline evals against them (e.g. asserting at most three suggested fixes)
- Run observability over tool calls before deploying — check how long each tool runs and how many times it loops — and always cap max loop iterations
- Ask the agent for a short retrospective at the end of every invocation (what went well, what went wrong, what tools and context were missing)
- Give the diagnosing agent access to trajectories, metrics, the database, and the UI, and keep the fixing agent separate from the reviewing agent
- Make anomaly output explainable with supporting evidence rather than collapsing it to one opaque score

**Avoid:**

- Trusting green dashboards, 200 OKs, or an aggregate pass rate — a catastrophic wrong action produces no exception and no alert
- Clustering traces as your issue-detection method: clusters cannot be tracked reliably over time, their boundaries are uncontrollable, and one cluster spans unrelated root causes
- Asking an agent to find anomalies rather than to investigate ones you already found
- Chasing bitwise determinism or pinning temperature to zero for reproducibility — you cannot get it from a hosted API, and it only makes the model repeat the same reasoning error
- Feeding raw logs or raw time-series metrics straight into context; use top-K truncated exceptions with a drill-down tool, or render metrics as images for fixed token cost
- Having an LLM read all traces at millions-of-traces scale — it costs more than the executions being analyzed
- Using the sandbox for durability, snapshots, or state; sandboxes are ephemeral by design
- Shipping a change on the evidence of one or two replays — a model that passes 60% of the time is self-consistent only about a quarter of the time
- Patching the prompt in response to a single failing run instead of measuring the failure pattern across many examples
- Leaving observability spans disconnected from the code and execution that produced them
- Treating deterministic controls — egress filters, sandboxes, auditability, telemetry — as sufficient; they are necessary but do not catch the agent that stays inside its authorization the whole time

## Notable Outliers

- At millions of agent traces, having an LLM read all of them costs more than the original agent executions did — sampling with learned failure indicators is mandatory, not an optimization. ([The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [21:28](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1288s))
- Render Spark job time-series metrics as images rather than feeding raw series to the LLM, because images guarantee a fixed input token count regardless of how long the job ran. ([Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s))
- At sufficient scale, telemetry stops being free overhead and becomes a meaningful part of the system load itself — collecting logs is hard, processing them is harder. ([How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [14:11](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=851s))
- Clusters are not issues — the naive approach of clustering all traces fails because clusters cannot be tracked over time and a single cluster can span unrelated root causes. ([Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [16:26](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=986s))
- A recorded production trace doubles as a deterministic regression test: stub every node except the one you changed, and the rerun is free because it never calls the model. ([Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [10:52](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=652s))
- The hardest failures to catch leave a perfectly compliant-looking trace — the agent never exceeds its authorization, it just picks the tool that lets it route around the constraint. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [10:16](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=616s))

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
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
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
- [Ben Hylak](../speakers/ben-hylak.md)
- [Chris Souza](../speakers/chris-souza.md)
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
- [Shashi](../speakers/shashi.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Susheem Koul](../speakers/susheem-koul.md)
- [Tisha Chawla](../speakers/tisha-chawla.md)
- [Vaibhav Gupta](../speakers/vaibhav-gupta.md)
- [Veronica Hylak](../speakers/veronica-hylak.md)
- [Victor Savkin](../speakers/victor-savkin.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)

