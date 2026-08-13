---
title: "agent observability and tracing"
type: "concept"
slug: "agent-observability-and-tracing"
tier: "core"
maturity: "consolidating"
talk_count: 30
speaker_count: 34
---

# agent observability and tracing

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **30** talk(s) by **34** speaker(s)

**Definition:** Instrumenting agent runs so every step, tool call, and token is inspectable after the fact — spans, traces, and the tooling that renders them.

*Also referred to as: agent observability, agent trace observability, llm observability, distributed tracing for agents, trace-based observability, agentic observability, session tracing*

## State of Practice

The field has settled on the premise that agent traces are the primary debugging and evaluation artifact, and that aggregate metrics — pass rates, 200 OKs, green dashboards — systematically hide the failures that matter, because an agent can complete successfully while doing exactly the wrong thing. What is required is not request logging but the full decision chain: reasoning steps, every tool input and output, memory access, state transitions, retries, and the infrastructure errors underneath, spanning the whole session from trigger to result. The consumer of that trace has shifted from a human clicking a Grafana-style UI to an agent that reads telemetry, files an evidence-backed issue, and opens a PR — which in turn justifies logging an order of magnitude more than before, but also creates a new cost problem, since reading millions of traces with an LLM can exceed the cost of the original executions. Production telemetry, not benchmarks or synthetic scenario sets, is now treated as the largest and most representative evaluation dataset an organization has, so evaluation is drifting from a pre-deploy gate into an always-on service riding the same trace substrate. The unresolved argument is about what the substrate actually is: a durable session log and OTel spans, or a checkpointed runtime that snapshots in-flight variables, filesystem state, and the executing code so a production run can be deterministically replayed with one node swapped.

## Consensus

### Aggregate pass-rate metrics and final outputs are insufficient for agent quality; specific classes of failure are only findable by inspecting the trace of reasoning and tool calls.

Support: **6** talk(s)

> "And we could not find that if we were just doing a categorical like the this x% pass rate or not. So we really had to look at the traces to see what was going on."
>
> — [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [11:34](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=694s)

Supporting talks: [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)

### Instrumentation is a precondition, not an afterthought: log and trace the full orchestration before attempting to optimize, evaluate, or scale the agent.

Support: **5** talk(s)

> "you want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop"
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [6:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=413s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

### The consumer of agent telemetry is now another agent, not a human browsing dashboards; the output of the observability loop should be a proposed fix or PR rather than a chart.

Support: **5** talk(s)

> "the future observability actually looks a lot more like this than it does clicking around graphana UI"
>
> — [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [5:08](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=308s)

Supporting talks: [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)

### Because agent trajectories are non-deterministic and coverage is unbounded, production traces — not pre-launch test suites — are what tell you which failure modes exist and therefore what to test.

Support: **6** talk(s)

> "production is the place when you learn what you need to uh what you need to test on the first place."
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [5:36](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=336s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)

### A usable agent trace must span more than LLM and tool calls — state transitions, memory access, retries, permissions and database errors, and the session envelope all have to be in the same trace.

Support: **5** talk(s)

> "So, if you can't see the entirety of a trace from the trigger through the whole stack, it's really hard to debug it, let alone improve your agent and keep evolving it."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [9:08](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=548s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)

### Trace-derived signals must ship with their supporting evidence rather than as a single opaque score, because the trace is the surface on which humans (users, reviewers, on-call) grant or withhold trust.

Support: **4** talk(s)

> "If you go to the doctor and doctor says your health score is 22, it doesn't make much sense to you."
>
> — [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [18:13](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=1093s)

Supporting talks: [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)

## Disagreements

### Is an emitted trace or session log a sufficient observability substrate, or must the runtime itself be checkpointed so runs can be replayed from code?

| Position A | Position B |
|---|---|
| A durable session log / trace of everything that happened during execution is the single substrate — it answers 'what is my agent doing', feeds context recovery, memory, and evaluation, and is the equivalent of distributed tracing for autonomous workloads.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)* | Traces are structurally inadequate because they are read-only artifacts disconnected from the runtime that discard in-flight variables, filesystem state, and the executing code; you need checkpointed state, recorded node boundaries, and fixtures so a production run can be replayed deterministically with one node swapped.<br>*[Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)* |

*Why it matters: It decides whether observability is a side-channel you bolt on with OTel spans or a property of the execution layer you must architect for up front — and whether a captured production failure can be turned into a free, rerunnable regression test or only into a document an agent reads.*

### Is agent observability an adaptation of existing distributed-systems tooling, or does it require a genuinely new layer of the stack?

| Position A | Position B |
|---|---|
| Reuse what exists: OpenTelemetry with async export, Kafka and stream processing, tail-based sampling, canaries, and standard SRE reliability patterns. Observability, canary, and verify logic are ordinary engineering foundations, not AI problems.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)* | Non-deterministic workloads break the assumptions of the existing stack — spans are disconnected from execution, string-matching runtime security tooling does not apply, and evaluation has to move into a control plane — so a new durable-runtime layer beneath the harness is required.<br>*[Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md)* |

*Why it matters: It determines whether teams staff this as an SRE/platform extension of their existing telemetry pipeline or bet on an emerging category of runtime tooling that mostly does not exist in production-ready form yet.*

### Should teams build their own agent observability and monitoring layer, or treat it as undifferentiated infrastructure to outsource?

| Position A | Position B |
|---|---|
| Build it yourself — you know what you are looking for, black-box vendor 'SRE agent' products are the wrong shape, and the harness watching your agent is where competitive advantage now lives since everyone has the same models.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* | Hosting, session management, sandboxing, credentials, and observability are undifferentiated work; developers should own only system prompts, skills, tools, and domain context, and let a shared substrate supply the loop, memory, and observability.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)* |

*Why it matters: Enterprises will not route production connections to a third party regardless, so the practical resolution — vendor sandbox or MCP tunnel inside the customer's own VPC — changes the deployment model for every observability vendor in the space.*

### Should teams dramatically increase trace and log volume now that agents can read it, or is trace volume itself the cost problem to design around?

| Position A | Position B |
|---|---|
| Trace and log roughly 10x more than today, because agents can dig through volumes of telemetry that humans never could — the noise that made verbose logging pointless for humans is no longer a constraint.<br>*[From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* | Volume is the binding constraint: reading millions of traces with an LLM costs more than the original executions, collecting and processing logs becomes a meaningful part of system load at scale, and replay is expensive enough that selecting what to replay is itself a design problem — so sample representatively, use tail-based sampling, and learn code-checkable indicators per failure mode.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)* |

*Why it matters: The two prescriptions produce opposite retention and sampling policies, and with token prices rising the cost of an always-on trace-reading agent can quietly exceed the cost of the agent fleet it is watching.*

## Practical Guidance

**Do:**

- Log every stage of the orchestration in a flat, human-readable JSON structure before building any eval or self-learning loop
- Capture the full envelope alongside the prompt — LLM version, build ID, RAG chunks — or the trace will not be replayable
- Record at each node boundary (what enters and what leaves), not at the network layer, since local retrieval, in-process tools, and memory never cross the network
- Export telemetry asynchronously with Kafka/stream processing downstream so tracing never sits in the latency path of a real-time request
- Use tail-based sampling when what matters is when each node's request started and ended
- Give new endpoints their own baseline and scope thresholds per client and per operation type, rather than one global baseline per HTTP method
- Snapshot real tool responses as fixtures checked into the repo so offline evals can quantify agent quality instead of relying on intuition
- Deliver selected trace data to a coding agent as files in the repo — harnesses handle even ~10MB files well
- Instrument at the execution layer, where triggers, user input, tool calls, feedback, and session results all converge
- Run observability over tool calls before deploying: check how long each tool runs and how many times the loop repeats, and cap max iterations
- Separate the agent that diagnoses and writes the fix from the agent that reviews it, giving the reviewer fresh context
- Score trace cohorts at thousands-scale with LLMs and make the runtime queryable by MCP servers and skills so agents can fetch artifacts
- Render long time-series metrics as images so input token count stays fixed regardless of job duration
- Use outcome signals from the trace — was the PR opened, was the report saved — as evaluation data instead of thumbs up/down
- Log a short per-invocation agent retrospective (what went well, what tools were missing, what context would help next time) as a stopgap where agent observability tooling does not yet exist

**Avoid:**

- Treating green dashboards, 200 OKs, and aggregate pass rates as evidence of correctness — a catastrophic wrong action raises no exception
- Chasing bitwise reproducibility by pinning temperature to zero; it fixes the selection rule, not the scores, and hosted APIs cannot deliver it
- Blaming GPU concurrency for run-to-run variation instead of batch invariance, non-associative float math, and MoE expert overflow
- Using the sandbox for durability, snapshots, or state — sandboxes are ephemeral by design
- Rewriting a prompt in response to a single failing run; drive fixes from failure patterns measured across many examples
- Shipping a change on the basis of one or two replays instead of cohort-level analysis
- Letting eval results and traces terminate in a dashboard with no path back into the agent's context, skills, or retrieval
- Assuming telemetry is free — at scale, collecting and processing logs becomes a meaningful part of system load and complexity
- Reducing an anomaly to a single opaque score with no supporting data
- Trusting a diagnostics agent's trace reading without surfacing its assumptions, since an agent reading traces without code access will infer things that are wrong

## Notable Outliers

- GPU concurrency is not the source of LLM non-determinism — an isolated matrix multiplication run a thousand times is bit-identical; the real culprit is that your request gets batched with whatever other traffic hit the server that millisecond. ([Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [3:53](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=233s))
- At millions of traces, having an LLM read all of them costs more than the agent executions that produced them. ([The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [21:28](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1288s))
- At sufficient scale, observability stops being a side concern and becomes part of the system load itself — collecting logs is hard, processing them is harder. ([How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [14:11](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=851s))
- In a world where nobody reads all the code, the execution trace is the only way to understand the code — and full-program tracing can be made effectively zero-cost if designed in from first principles. ([fighting slop with slop](../talks/fighting-slop-with-slop.md), [10:39](https://www.youtube.com/watch?v=AMiyLItEtLA&t=639s))
- Execution traces should feed back as a bottom-up trust ranking of data sources: what actually worked in practice weights which source an agent picks next time, giving cross-agent learning. ([Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [8:19](https://www.youtube.com/watch?v=VGN22pPpb-8&t=499s))
- Replaying from production checkpoints cut a multi-hour process to 5 minutes across hundreds of simulations, with 90% fewer hallucinations and results within two points of production. ([Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [4:27](https://www.youtube.com/watch?v=bZISsg7H7DA&t=267s))
- Rendering Spark metrics as images rather than raw series guarantees a fixed input token count for analyzing any job regardless of its duration. ([Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s))

## All Talks

- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)
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

