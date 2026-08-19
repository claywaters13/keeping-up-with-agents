---
title: "durable execution"
type: "concept"
slug: "durable-execution"
tier: "supporting"
maturity: "consolidating"
talk_count: 19
speaker_count: 21
---

# durable execution

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **19** talk(s) by **21** speaker(s)

**Definition:** Runtimes that survive crashes and restarts by persisting agent state — checkpointing, replay, and idempotent resumption of long-running work.

*Also referred to as: durable runtime, resumability and checkpointing, agent state checkpointing, agent state durability, interrupts and resumable execution, event sourcing, idempotency*

## State of Practice

The field has converged on a single structural claim: for runs measured in hours or days, agent state cannot live in the model's context, in process memory, or on local disk — it must be externalized into something append-only and replayable. The dominant formulation is event sourcing: an append-only log of every input, model output, tool call, result, permission and failure, with model context, UI, debugging views and compaction all treated as projections of it, which yields replay, rollback and forking for free. Failure is now treated as the expected case rather than an exception — a background run making ~200 tool calls is assumed to hit at least one failure, and large training runs were observed crashing hourly before running clean for 12–24 hours on identical hardware — so the mitigation is frequent checkpointing and idempotent resumption, not failure prevention. What is genuinely unsettled is the substrate: a typed event log, a full environment snapshot (code + artifacts + filesystem + VM memory), or a durable workflow engine, and whether the sandbox itself may hold durable state. The protocol layer is behind the practice: MCP tasks mandates durability across client, server and network failure, but as of this conference no MCP client implements it, and the V2 spec still only says clients "should" persist task IDs even though an unpersisted ID is permanently unrecoverable. Durability has also stopped being purely crash insurance — checkpoint lineage is being used for branching across models, Monte Carlo tree search over sandbox states, and replay-based evaluation on real production runs.

## Consensus

### State for long-running agents must be externalized from the executing process — not held in model context, process memory, or local disk — so that the executor is allowed to be fallible.

Support: **6** talk(s)

> "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)

### Failure during long runs is statistically certain, so checkpoint-and-resume must be architectural rather than an error path bolted on later.

Support: **7** talk(s)

> "It's going to have maybe hundreds of calls to you know, maybe 200 tool calls. You're going to probably guarantee to have at least one failure in that."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [11:35](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=695s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)

### Persisted execution history is not only crash insurance — it is what enables replay, rollback, forking onto different models, and replay-based evaluation.

Support: **5** talk(s)

> "in the end you get this beautiful typed event log, which gives you replays. It gives you rollbacks and it gives you forks."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [3:43](https://www.youtube.com/watch?v=khVX_BUnEwU&t=223s)

Supporting talks: [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md)

### The model proposes and the harness commits: state transitions, ordering, and completion judgments are engineered outside the model, never delegated to it.

Support: **5** talk(s)

> "A model proposes the harness commits and the receipts proves it."
>
> — [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [2:40](https://www.youtube.com/watch?v=BInpv7lGp1o&t=160s)

Supporting talks: [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### The execution/durability layer is the longest-lived layer of the stack and should be decoupled so models, prompts, context, and sandboxes can be swapped without rewriting it.

Support: **4** talk(s)

> "You can swap the model, swap the context, swap the sandbox, the execution layer should be able to remain the same."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)

### Resumption must be idempotent and enforced by the system, because a model-driven retry can silently reword a request into what looks like a new task.

Support: **3** talk(s)

> "you have to design for idempotency, which is where you can run the same thing twice and the second run doesn't cause a mess."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [13:17](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=797s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)

## Disagreements

### Is an append-only event log sufficient durable state, or must you snapshot the full execution environment (code, artifacts, filesystem, memory)?

| Position A | Position B |
|---|---|
| The log is the agent and is sufficient to resume: the model, tools and runtime only read from and append to it, so everything else — model context, UI, compaction, debugging views — is a disposable projection.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)* | Logs and traces are insufficient because they discard in-flight variables, filesystem state, and the executing code; durability requires checkpointing the code plus artifacts plus the environment (Docker image or sandbox), and log-based state rehydration leaks its abstractions into other layers of the harness.<br>*[Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)* |

*Why it matters: It determines whether resumption is a cheap schema/adapter problem solvable by any process on any machine, or requires incremental multi-gigabyte snapshot infrastructure with lineage-aware scheduling. It also decides whether replay-based evaluation can faithfully re-run a production incident or only re-narrate it.*

### Should the sandbox be a durable substrate that persists agent state, or is sandbox persistence an anti-pattern?

| Position A | Position B |
|---|---|
| Disk persistence and fast incremental snapshot/restore inside the sandbox are the next major unlock, turning agents from ephemeral executors into durable knowledge workers; persistence counterintuitively improves reliability and scale.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)* | Sandboxes are ephemeral and stateless by design, so using one for durability, snapshots, or state is an anti-pattern — the sandbox is the hands, the execution layer is the brain and owns state.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)* |

*Why it matters: If the sandbox is durable, snapshot lineage becomes the checkpoint mechanism and schedulers must be layer-cache-aware; if it is not, every durable fact has to be written through to an external execution layer before the sandbox can be reclaimed.*

### How much correctness engineering does resumption need — is crash-and-restart-from-checkpoint enough, or must you build idempotency, ordered commits, and terminal states?

| Position A | Position B |
|---|---|
| Resumption requires explicit invariants: system-level idempotency, one ordered commit path per mutable state boundary, receipts proving what executed, and a terminal state for every external boundary — because last-writer-wins is not a consistency model and naive implementations break on concurrency, process failure, and network failure.<br>*[Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)* | Custom failure-recovery logic is wasted effort: checkpoint often, let it crash, mark the unit failed and let the platform (Kubernetes, the HPA) recreate it — reactively chasing each crash costs more than it saves.<br>*[Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md)* |

*Why it matters: The restart-and-checkpoint model is safe only when the work has no externally visible side effects; agents that send emails, open PRs, or move money need the ordered-commit machinery, so the choice sets how much of the durable-execution layer you own versus delegate to an orchestrator.*

## Practical Guidance

**Do:**

- Persist an append-only event history of every user input, model output, tool call, tool result, permission, and failure — and treat model context, UI, debugging and compaction as projections of it
- Keep long-run state outside the process so one process can advance many agents and any worker can pick up any run (no sticky sessions or state migration)
- Checkpoint on a fixed cadence rather than on failure; with a fast enough parallel filesystem, 20–30 minute checkpoints on large training runs cost effectively nothing (a terabyte written in under 30 seconds)
- Make snapshots incremental with layered lineage instead of saving full multi-gigabyte images every turn, and score scheduler nodes by how many lineage layers they already have cached
- Return the snapshot to the caller immediately while the upload to cloud storage continues in the background
- Treat compaction as a lossy best-effort fork resumed as a new log, and retain the raw log
- Enforce idempotency at the system level, with one ordered commit path per mutable state boundary — allow parallel reads, sub-agent fan-out, and concurrent sessions everywhere else
- Give every external boundary an ending: success, failure, timeout, cancel, or max attempts — and make recovery commands runnable without queueing behind the stuck work they are fixing
- Persist task IDs client-side for any async/long-running tool protocol; an unpersisted ID is permanently unrecoverable
- Put an explicit numeric break condition on every agent loop
- Record the full envelope — LLM version, build ID, RAG chunks — alongside the prompt, so a production run can be replayed with every node stubbed except the one under change
- Run a lint pass over the agentic system to detect half-completed runs
- Decide from replay cohorts, not single replays: a model that passes 60% of the time is self-consistent only about a quarter of the time
- Use block-device access inside micro VMs rather than shared-folder filesystem passthrough, which exits on every filesystem operation and bypasses the guest cache

**Avoid:**

- Letting the model hold or advance workflow state — it is terrible at remembering whether it is on step three of six, and when reliability approaches a coin flip that is the signal to pull control flow out of the model entirely
- Restarting a long run from the beginning after a transient failure such as an expired API key
- Relying on the model to make retries safe; a retry risks it rewording the request just enough to look like a brand new task
- Fire-and-forget writes of session state to local disk (as Claude Code and Codex do with JSONL, even in SDK mode) — if the write fails the data is gone
- Leaving a pending permission prompt as unpersisted state: if the process dies and the session resumes, the prompt is gone and the agent is stuck paused
- Swapping out nodes reactively after every crash — the same machines, code, and data often run 12–24 hours after a series of hourly crashes
- Stateful protocol endpoints like an unfiltered tasks/list, which forces you to page through a million tasks to find one, and per-client polling models that do not scale to millions of concurrent tasks
- Querying the event store directly for reads instead of maintaining optimized read models
- Chasing bitwise determinism from a hosted API — it is unobtainable, and the randomness is what gives the agent its agency; record the run instead
- Recording at the network layer, since local retrieval, in-process tools, and memory never cross the network and streaming/async breaks packet capture
- Long-term memory in latency-bound paths — a sub-500ms transaction SLA rules it out; use short-term in-memory context
- Leaving your logs on a provider's infrastructure: log lock-in is deeper than model, API, or tool lock-in, and if a provider owns your log it effectively owns your agent

## Notable Outliers

- The deepest form of vendor lock-in is not model, API, or tool lock-in but log lock-in — models can be swapped and APIs wrapped, but whoever owns your log owns your agent. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s))
- Checkpoint/restore of sandbox state lets a harness run Monte Carlo tree search over environment states across many days, backtracking and re-exploring branches. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [32:52](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1972s))
- Persistence counterintuitively improves reliability and scale rather than trading against them — the two look orthogonal but are tightly related. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [31:29](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1889s))
- Zero MCP clients implement MCP tasks, and that is the correct engineering call: the spec was marked experimental and V2 changes it substantially, including dropping tasks/list and going stateless. ([MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [0:01](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1s))
- Ordering bugs in durable state are experienced by users as agent personality defects — forgetful, dead, confused — which makes commit ordering a product feature, not an internal concern. ([Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [9:15](https://www.youtube.com/watch?v=BInpv7lGp1o&t=555s))
- AI writes shared-state/blackboard-style event-sourced agent code better than LLM-agent-style code, because decades of that architectural discussion sit in the training data while LLM agent patterns are only three years old. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [14:54](https://www.youtube.com/watch?v=khVX_BUnEwU&t=894s))

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
- [Sean Cai](../speakers/sean-cai.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Susheem Koul](../speakers/susheem-koul.md)
- [Tisha Chawla](../speakers/tisha-chawla.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

