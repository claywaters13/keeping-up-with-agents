---
title: "durable execution"
type: "concept"
slug: "durable-execution"
tier: "supporting"
maturity: "consolidating"
talk_count: 20
speaker_count: 23
---

# durable execution

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **20** talk(s) by **23** speaker(s)

**Definition:** Runtimes that survive crashes and restarts by persisting agent state — checkpointing, replay, and idempotent resumption of long-running work.

*Also referred to as: durable runtime, resumability and checkpointing, agent state checkpointing, agent state durability, interrupts and resumable execution, event sourcing, idempotency*

## State of Practice

The field has converged on a single structural answer to agent crashes: the durable artifact is an append-only event log external to both the model and the process executing it, with every other view — model context, UI, audit trail, compaction — treated as a recomputable projection. Practitioners now assume failure rather than design against it: a background run making ~200 tool calls is expected to hit at least one failure, and long-horizon runs are expected to outlive the worker, the sandbox, and sometimes the provider. The second durable-execution primitive that showed up repeatedly is checkpoint-and-replay, used not just for crash recovery but as evaluation infrastructure — replaying real production checkpoints against a changed node beats synthetic eval datasets, and at OpenAI's sandbox scale it requires incremental snapshots (full multi-gigabyte images per turn are financially infeasible) plus lineage-aware scheduling. Reproducibility is explicitly decoupled from model determinism: nobody expects bitwise-identical logits from a hosted API, so the goal is a recorded run and a repeatable state transition, not a frozen model. What is still unsettled is where the durable state physically lives — a snapshotted execution environment versus an external log with a disposable executor — and whether teams should adopt a general durable runtime or build the execution layer themselves. The MCP tasks spec, the field's one attempt at standardizing durable async tool calls, currently has zero client implementations.

## Consensus

### State for a multi-step or long-running agent must live outside the model and outside the process doing the work, not in the LLM's context, in memory, or on local disk.

Support: **5** talk(s)

> "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md)

### An append-only immutable event log should be the system's source of truth, with all other views (context, UI, audit, read models) treated as recomputable projections of it.

Support: **4** talk(s)

> "underneath every serious database is a log. And that log is the durable sequence of changes. Everything else is a view."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [3:18](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=198s)

Supporting talks: [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)

### Checkpointing execution state and replaying from those checkpoints is the working mechanism for both crash recovery and for asking what-if questions about a run.

Support: **5** talk(s)

> "So, checkpoint replay diff decide. And this is really the methodology that that I've seen and I've seen others do, uh which has really scaled."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [3:37](https://www.youtube.com/watch?v=bZISsg7H7DA&t=217s)

Supporting talks: [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

### Failure during a long run is the expected case, not the exceptional one, so durability has to be an architectural property rather than error handling bolted on.

Support: **5** talk(s)

> "It's going to have maybe hundreds of calls to you know, maybe 200 tool calls. You're going to probably guarantee to have at least one failure in that."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [11:35](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=695s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)

### Agents are shifting from request/response to processes that run for hours or days in the cloud, which is what forces the durability requirement.

Support: **4** talk(s)

> "durability just the sheer quality of like being able to run not for minutes but for hours or days"
>
> — [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md), [3:25](https://www.youtube.com/watch?v=8qWIPUia2O8&t=205s)

Supporting talks: [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md)

### Every unit of work and every external boundary needs an enforced terminal condition and system-level idempotency, because a model-driven retry can silently become a new task or an unbounded loop.

Support: **3** talk(s)

> "Every external boundary needs an ending. Success, failure, timeout, cancel, or max attempts."
>
> — [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [10:58](https://www.youtube.com/watch?v=BInpv7lGp1o&t=658s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)

## Disagreements

### Should durable agent state be captured by snapshotting the execution environment, or must it live in an external log with the executor treated as disposable?

| Position A | Position B |
|---|---|
| Snapshot the machine: persist and incrementally checkpoint the sandbox's disk and memory, so the environment itself (filesystem, in-flight variables, Docker image) can be restored and forked; persistence in the sandbox is what makes agents durable knowledge workers rather than ephemeral executors.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)* | Sandboxes are ephemeral and stateless by design, so using one for durability, snapshots, or state is an anti-pattern; the log is the agent and the executor is allowed to be fallible, which is what lets one process advance thousands of agents with no sticky sessions.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md)* |

*Why it matters: It decides whether you invest in snapshot/restore infrastructure (incremental disk images, lineage-aware schedulers, warm pools) or in log storage plus stateless workers, and it determines whether an agent can migrate across machines and providers mid-run.*

### Should teams adopt a general-purpose durable execution runtime or protocol, or build their own execution layer?

| Position A | Position B |
|---|---|
| Adopt a shared layer: a durable workflow engine or standardized async task protocol on both client and server, a new runtime layer beneath agent frameworks, or an existing SDK that already implements ownership, ordering, lifecycle, and receipts.<br>*[MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)* | Existing frameworks were not designed for background, looping, long-running agents, so teams must design the execution layer themselves — and general-purpose implementations will increasingly be replaced by bespoke ones derived from a specification, or by harnesses that need language-level support libraries cannot provide.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)* |

*Why it matters: Betting on a shared runtime buys crash-resumption, pause/resume, and signalling for free but couples you to an experimental spec that currently has no client implementations; building it yourself is the layer that lasts years, so getting it wrong forces a rewrite of everything above it.*

### When a long run crashes, should recovery be delegated to generic infrastructure restart machinery, or must the application own fine-grained resumable state?

| Position A | Position B |
|---|---|
| Let it crash and let the platform recreate the work: custom failure-recovery logic is unnecessary, marking the pod failed and letting Kubernetes and the HPA recreate it is sufficient, and repeatedly swapping nodes in response to crashes is wasted effort since the same machines often then run for 12–24 hours.<br>*[Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md)* | Coarse restart loses real state: a dropped pending permission prompt on resume is unacceptable in production, silent success is worse than a crash because it removes the error boundary, and durability has to be designed in at the level of individual state transitions and receipts.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)* |

*Why it matters: Restart-and-retry is cheap and adequate when the unit of work is a checkpointed training step, but agent work has side effects and human approval gates where a naive restart either duplicates external actions or silently strands the run.*

## Practical Guidance

**Do:**

- Persist a single immutable, typed event log covering user input, model output, tool calls, tool results, permissions, and failures — replays, rollbacks, and forks fall out of it for free
- Build separate optimized read models rather than querying the event store directly for reads
- Treat compaction as a best-effort lossy fork resumed as a new log, and retain the raw log
- Enforce idempotency at the system level rather than trusting the model, since a retry can be reworded just enough to look like a brand new task
- Give agent loops an explicit numeric break condition tied to a metric so they cannot run indefinitely
- Enforce one ordered commit path per mutable state boundary while still allowing parallel reads, sub-agent fan-out, and concurrent sessions
- Make recovery commands runnable without queueing behind the stuck work they are meant to fix
- Snapshot incrementally and return the snapshot immediately while uploading to the cloud in the background
- Score scheduler nodes by how many snapshot lineage layers they already have cached, and combine warm pools with memory-snapshot restore
- Checkpoint training runs every 20–30 minutes when the filesystem can absorb it — a parallel filesystem doing ~1.8 TB/s reads writes a terabyte checkpoint in under 30 seconds
- Persist task IDs on the client — an unpersisted MCP task ID is permanently unrecoverable
- Capture the full session envelope alongside the prompt: LLM version, build ID, and RAG chunks, or the trace is not replayable
- Replay recorded production runs as regression tests by stubbing every node except the one you changed — deterministic and free because it never calls the model
- Run replay analysis at cohort scale with agents doing the diffing, and keep a human at the final ship/no-ship decision
- Take enterprise constraints (audit, isolation, replay) as the architectural foundation and build back up to POC accuracy on those primitives

**Avoid:**

- Using a sandbox for durability, snapshots, or state — sandboxes are ephemeral and stateless by design
- Letting the LLM hold or advance workflow state; it is terrible at remembering whether it is on step three of six
- Relying on fire-and-forget local JSONL writes as your log of record, where a failed write silently loses the data
- Chasing bitwise determinism through a hosted API or pinning temperature to zero as a reproducibility strategy — greedy decoding only fixes the selection rule, not the underlying scores
- Recording at the network layer, since local retrieval, in-process tools, and memory never cross the network
- Saving full multi-gigabyte images on every turn instead of incremental snapshots
- Stateful protocol endpoints like an unfiltered tasks/list that would force scanning a million tasks to find one
- Hand-rolled checkpointing and ad hoc log rehydration whose abstractions leak into the other layers of the harness
- Resuming a session in a way that drops a pending permission prompt and leaves the agent silently paused
- Shipping a change on the evidence of one or two replays — a model that passes 60% of the time is self-consistent only about a quarter of the time
- Repeatedly swapping nodes in response to hourly training crashes
- Bolting auditability, eval, and security onto a working POC as requirements surface — the result is brittle and does not generalize

## Notable Outliers

- The deepest form of vendor lock-in is not model, API, or tool lock-in but log lock-in — if a provider owns your log, the provider owns your agent. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s))
- Once the log is the state, one process can advance thousands of agents instead of one process per agent. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s))
- Fast checkpoint/restore lets a harness run Monte Carlo tree search over sandbox states across many days, backtracking and re-exploring branches. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [32:52](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1972s))
- Long-term memory is incompatible with a sub-500ms transaction SLA, so the agent runs on short-term in-memory context only — durability deliberately traded away for latency. ([Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [11:32](https://www.youtube.com/watch?v=o6U_2vd967Y&t=692s))
- Sometimes you just let it crash: the same machines, code, and data that crashed hourly will then run 12, 16, or 24 hours. ([Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [3:18](https://www.youtube.com/watch?v=byn9PURoBNY&t=198s))
- A deterministic, repeatable, inspectable simulation that deliberately leaks forbidden information (whether a read was stale, and what value was missed) lets an agent design a correct distributed implementation, not just code one. ([The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [13:56](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=836s))
- The MCP tasks spec says clients should persist task IDs, but since an unpersisted ID is unrecoverable it should be a normative MUST. ([MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [19:05](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1145s))
- Event-sourced agents eliminate the need to restart a long run from the beginning after a mundane failure such as an expired API key. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [8:54](https://www.youtube.com/watch?v=khVX_BUnEwU&t=534s))

## All Talks

- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)
- [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md)
- [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)
- [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md)
- [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)
- [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)
- [The Log Is The Agent](../talks/the-log-is-the-agent.md)
- [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)
- [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)
- [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)
- [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)
- [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Abhishek Bhardwaj](../speakers/abhishek-bhardwaj.md)
- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Angie Jones](../speakers/angie-jones.md)
- [Ben Holmes](../speakers/ben-holmes.md)
- [Christopher Lovejoy](../speakers/christopher-lovejoy.md)
- [Cornelia Davis](../speakers/cornelia-davis.md)
- [Dan Farrelly](../speakers/dan-farrelly.md)
- [Divakar Kumar](../speakers/divakar-kumar.md)
- [Dominik Tornow](../speakers/dominik-tornow.md)
- [Gabriel Jorge Menezes](../speakers/gabriel-jorge-menezes.md)
- [Ishaan Sehgal](../speakers/ishaan-sehgal.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Kunal Lanjewar](../speakers/kunal-lanjewar.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Saul Howard](../speakers/saul-howard.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Susheem Koul](../speakers/susheem-koul.md)
- [Tisha Chawla](../speakers/tisha-chawla.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

