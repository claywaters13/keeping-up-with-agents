---
title: "durable execution"
type: "concept"
slug: "durable-execution"
tier: "supporting"
maturity: "consolidating"
talk_count: 17
speaker_count: 19
---

# durable execution

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **17** talk(s) by **19** speaker(s)

**Definition:** Runtimes that survive crashes and restarts by persisting agent state — checkpointing, replay, and idempotent resumption of long-running work.

*Also referred to as: durable runtime, resumability and checkpointing, agent state checkpointing, agent state durability, interrupts and resumable execution, event sourcing, idempotency*

## State of Practice

The field has converged on a single structural claim: for runs measured in hours or days, agent state cannot live in the process, in memory, or on local disk — it must be an external, append-only, durable record that the executor merely reads from and appends to. The corollary appearing in talk after talk is that the model must not hold control flow: the harness owns state transitions, validates tool results, advances the state machine, and commits, while the model only proposes. Failure is treated as certain rather than exceptional — a background run making ~200 tool calls is assumed to hit at least one failure, so resumability, idempotent retry, and explicit terminal states (success/failure/timeout/cancel/max-attempts) are architectural requirements, not hardening. Once the log or checkpoint exists, it is being reused for things beyond crash recovery: forking and rollback, branch-per-model execution, Monte Carlo tree search over sandbox snapshots, and replay-based evaluation against real production state instead of synthetic datasets. What is genuinely unsettled is the substrate — an event log you own, a durable workflow engine beneath the framework, incremental VM/disk snapshots in the sandbox, or language-level serializable execution — and the MCP tasks spec, the one protocol-level attempt to standardize durable async tool calls, still has zero client implementations and is being rewritten.

## Consensus

### State for a long-running agent must live outside the executing process — not in memory, not on local disk, not tied to a specific machine.

Support: **5** talk(s)

> "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)

### The model must not own workflow state or decide what step it is on; the harness tracks position, validates results, and advances the state machine.

Support: **5** talk(s)

> "The harness validates what's comes back, advance the state, and decide what's next. The model never decide where we are. That's the design."
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [0:44](https://www.youtube.com/watch?v=m24UKZomm7k&t=44s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### An append-only event log is the ground truth of an agent; the context window, UI, read models, and compacted summaries are all derived projections of it.

Support: **4** talk(s)

> "underneath every serious database is a log. And that log is the durable sequence of changes. Everything else is a view."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [3:18](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=198s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)

### Failure during a long run is statistically certain, not an edge case, so resumption from the last durable point must be designed in rather than bolted on.

Support: **5** talk(s)

> "It's going to have maybe hundreds of calls to you know, maybe 200 tool calls. You're going to probably guarantee to have at least one failure in that."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [11:35](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=695s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)

### Persisted state pays off beyond crash recovery: the same checkpoints/log enable rollback, forking, branch-per-model execution, and replay-based evaluation.

Support: **6** talk(s)

> "in the end you get this beautiful typed event log, which gives you replays. It gives you rollbacks and it gives you forks."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [3:43](https://www.youtube.com/watch?v=khVX_BUnEwU&t=223s)

Supporting talks: [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

### Idempotency and termination must be enforced by the system, not by the model — every loop needs an explicit break condition and every external boundary needs a terminal state.

Support: **3** talk(s)

> "Every external boundary needs an ending. Success, failure, timeout, cancel, or max attempts."
>
> — [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [10:58](https://www.youtube.com/watch?v=BInpv7lGp1o&t=658s)

Supporting talks: [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)

## Disagreements

### Is a durable event log by itself sufficient to make execution durable, or do you need a dedicated durable workflow/execution engine underneath the harness?

| Position A | Position B |
|---|---|
| The log is the durable primitive and the only non-derived thing in the system. Because the model, tools, and runtime only read from and append to it, the log alone is enough to resume; the executor is allowed to be fallible and one process can advance thousands of agents.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)* | Hand-rolled checkpointing and log-based state rehydration are inadequate abstractions that leak into the context and compute layers; durability belongs in a separate execution layer or durable workflow engine (Temporal-style signals, serializable pause/resume, a checkpointing runtime beneath the framework) that you swap models and sandboxes around.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)* |

*Why it matters: It decides whether durability is something you build into your own data model and own outright, or a dependency you adopt — and log-centric teams argue that whoever owns the log owns the agent, the deepest form of vendor lock-in there is.*

### Should the sandbox be a durable, snapshotted store of agent state, or is durability strictly the execution layer's job?

| Position A | Position B |
|---|---|
| Disk persistence — not compute — is the next unlock: incremental VM and block-device snapshots turn agents from ephemeral executors into durable knowledge workers, with schedulers scoring nodes by cached snapshot lineage and restores backed by warm pools. Snapshot the code, artifacts, and the Docker image or sandbox together between checkpoints.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)* | Sandboxes are ephemeral and stateless by design; using one for durability, snapshots, or state is an anti-pattern. The sandbox is the hands, the execution layer is the brain, and state must be external to both so the sandbox can be swapped without touching execution.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)* |

*Why it matters: If sandbox snapshots are legitimate durable state, your resume path depends on VM lineage, storage cost per turn, and scheduler placement; if not, sandboxes stay disposable and every fact worth surviving must be written to an external store before the box disappears.*

### Should replay eliminate run-to-run variation, or measure it?

| Position A | Position B |
|---|---|
| Freeze it. Bitwise determinism from a hosted API is unobtainable, so record at each node boundary and replay by stubbing every node except the one under change — deterministic, rerunnable, and free because it never calls the model. Deterministic, repeatable, inspectable simulation is precisely what lets an agent be corrected on why it broke.<br>*[Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)* | Replay live and in bulk. A single replay is an anecdote — on τ-bench a model passing 60% of the time is self-consistent only about a quarter of the time — so decisions require hundreds of grounded simulations and cohort-level analysis, and nothing ships on one or two replays.<br>*[Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)* |

*Why it matters: It sets both the cost model and the confidence bar for shipping: stubbed replay is free regression testing that cannot detect a model swap regression, while cohort replay is expensive enough that choosing what to replay becomes its own design problem.*

## Practical Guidance

**Do:**

- Keep the raw append-only log and treat compaction as a lossy, best-effort fork resumed as a new log rather than an in-place rewrite
- Persist run/task IDs durably at launch — an unpersisted handle to a long-running task is permanently unrecoverable
- Give every loop an explicit numeric break condition and every external boundary a terminal state: success, failure, timeout, cancel, or max attempts
- Enforce one ordered commit path per mutable state boundary while still allowing parallel reads, sub-agent fan-out, and concurrent sessions; last-writer-wins is not a consistency model
- Enforce idempotency at the system level, since a retried model call can reword the request enough to look like a brand-new task
- Snapshot incrementally rather than saving multi-gigabyte images every turn, and return the snapshot handle immediately while uploading in the background
- Combine warm pools with memory-snapshot restore, and score scheduler nodes by how many snapshot lineage layers they already have cached
- Prefer block-device access inside a micro VM over shared-folder passthrough — it uses the guest cache and avoids exiting on every filesystem operation
- Capture the full envelope alongside the prompt — model version, build ID, RAG chunks — or the trace is not replayable
- Run replay-based evaluation against real production checkpoints instead of synthetic datasets, and decide on cohorts rather than single runs
- Make recovery commands runnable without queueing behind the stuck work they are meant to fix
- Emit receipts that record what the system allowed, attempted, executed, and what the user-visible edge confirmed — a transcript is not proof
- Make approval a scoped execution state bound to actor, session, run, tool, arguments, and lifetime, with expiration that terminates rather than loops
- Treat incremental updates and checkpoints as mandatory in data-heavy pipelines, not as an optimization

**Avoid:**

- Letting the model remember which step of a multi-step workflow it is on — reliability at coin-flip levels is the signal to pull control flow out of the model entirely
- Relying on fire-and-forget local JSONL writes (Claude Code, Codex SDK mode) or state stores with known corruption issues; a failed write silently loses the run
- Losing pending interaction state on process death — a resumed session that has dropped its permission prompt leaves the agent paused forever
- Restarting a long run from the beginning after a transient failure such as an expired API key
- Stateful protocol endpoints like an unfiltered tasks/list, which force scanning a million tasks to find one and collapse at scale
- Per-client polling as the scale-out story for a million concurrent durable tasks; use notifications instead
- Chasing bitwise determinism by pinning temperature to zero — it fixes the selection rule, not the logits, and removes the variation that gives the agent its agency
- Recording at the network layer, since local retrieval, in-process tools, and memory never cross the network and streaming breaks packet capture
- Treating green dashboards and 200 OKs as correctness signals — silent success is worse than a crash because a crash gives you an error boundary
- Shipping a model or config change on the basis of one or two replays

## Notable Outliers

- Checkpoint/restore of sandbox state lets a harness run Monte Carlo tree search over sandbox states across many days, backtracking and re-exploring. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [32:52](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1972s))
- Persistence counterintuitively improves reliability and scale rather than trading against them. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [31:29](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1889s))
- Log lock-in is a deeper and more durable form of vendor lock-in than model, API, or tool lock-in — if a provider owns your log, it owns your agent. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s))
- Durable agent state should have a hard expiry: seven days is the right forced expiration for in-memory keys, because 24 hours misses work when a user doesn't open their phone. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [6:53](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=413s))
- The MCP tasks spec's 'clients should persist task IDs' ought to be a normative MUST, since an unpersisted task ID is permanently unrecoverable. ([MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [19:05](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1145s))
- The event-sourced runtime is unintuitive enough that writing its code by hand is impractical for humans — it is viable only because AI writes the code, and AI writes shared-state/blackboard architectures better than LLM-agent code because decades of that discussion exist in training data. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [6:33](https://www.youtube.com/watch?v=khVX_BUnEwU&t=393s))

## All Talks

- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)
- [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)
- [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)
- [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)
- [The Log Is The Agent](../talks/the-log-is-the-agent.md)
- [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)
- [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)
- [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)
- [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Abhishek Bhardwaj](../speakers/abhishek-bhardwaj.md)
- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Angie Jones](../speakers/angie-jones.md)
- [Cornelia Davis](../speakers/cornelia-davis.md)
- [Dan Farrelly](../speakers/dan-farrelly.md)
- [Divakar Kumar](../speakers/divakar-kumar.md)
- [Dominik Tornow](../speakers/dominik-tornow.md)
- [Ishaan Sehgal](../speakers/ishaan-sehgal.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Kunal Lanjewar](../speakers/kunal-lanjewar.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Susheem Koul](../speakers/susheem-koul.md)
- [Tisha Chawla](../speakers/tisha-chawla.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

