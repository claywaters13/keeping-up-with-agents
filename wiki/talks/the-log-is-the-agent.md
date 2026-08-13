---
title: "The Log Is The Agent"
type: "talk"
slug: "the-log-is-the-agent"
org: "Omnara"
video_id: "UPwGaM2MKHY"
duration_sec: 911
word_count: 2546
speakers: ["Ishaan Sehgal"]
---

# The Log Is The Agent

**Speakers:** [Ishaan Sehgal](../speakers/ishaan-sehgal.md)

**Org:** Omnara

**Duration:** 15m 11s

[Watch on YouTube](https://www.youtube.com/watch?v=UPwGaM2MKHY)

## Summary

Ishaan Sehgal, CEO of Omnara, argues that the common mental model of an agent — the model, the runtime, or the process — is the wrong abstraction, and that an agent's actual identity is its append-only event log. Using a Skyrim save file as the running analogy, he reframes every other part of an agent system (the model context, the UI, audit trails, compaction) as a projection of that log, with the execution loop reduced to a disposable worker that reads the log, advances one step, and writes back. He works through the two obvious objections — finite context windows forcing compaction, and side effects that happen outside the log — and argues neither breaks the claim, since compaction is a lossy projection and the log was only ever meant to store the agent's view of the world. The payoff is a set of properties he says fall out structurally rather than being bolted on: crash-resilient sessions, one process advancing thousands of agents, cheap forking across models, multiplayer sharing, and provider migration. The talk closes with a pointed warning that log lock-in, not model or API lock-in, is the deepest form of vendor capture, and pitches Omnara's open-source managed agents platform built around a user-owned session log. Worth watching if you're designing agent infrastructure and deciding where durable state should live.

## Key Points

- An agent's identity lives in its append-only log of every user input, model output, tool call, tool result, permission and failure — not in the model or the execution environment.
- Once the log is primary, every other artifact (model context, UI, audit trail, debugging view, compaction) is just a projection of it, mirroring how databases made the write-ahead log durable and everything else a view.
- The agent loop becomes disposable: a worker can claim a session, reconstruct state from the log, advance one step, write the result, and vanish, letting any other worker pick up from there.
- Compaction is a lossy, best-effort fork rather than a faithful smaller copy, so discarding the raw log in favor of the compaction destroys part of the agent.
- The log records the agent's view of the world, not the world itself — forking back cannot unsend an email or revert a file changed underneath it.
- Sehgal cites concrete infrastructure failures as evidence that the log is treated as an afterthought today: Claude Code and Codex writing messy JSONL to local disk with fire-and-forget writes, and OpenCode's SQLite state corruption issues.
- Log-centricity makes scale and failover structural — one process can advance thousands of agents with no sticky sessions, state migration, or coordination overhead.
- The deepest form of vendor lock-in is log lock-in, because models, runtimes, and machines are all replaceable while the log persists and contains your personal, company, and workflow data.
- Omnara is building and open-sourcing a managed agents platform where the session log is fully owned, inspected, and controlled by the user.

## Notable Quotes

> "most people think of an agent as the model or the execution environment that it's running in and I think that that's the wrong abstraction"
>
> — [0:00](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=0s) &middot; *states the talk's central contrarian thesis in one line*

> "if your PlayStation bursts into flames, your character isn't gone. You can buy another PlayStation, you can download your save file from the cloud and you can resume exactly where they were"
>
> — [0:35](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=35s) &middot; *the analogy the entire argument is built on*

> "the log is the append-only event history of the agent. It's every user input, every model output, every tool called, tool result, permission, failure"
>
> — [1:15](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=75s) &middot; *the operative definition of 'log' used throughout*

> "The important insight is not that this loop is complicated. The important insight is that the loop is disposable."
>
> — [2:46](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=166s) &middot; *names the architectural consequence that makes the rest of the talk work*

> "underneath every serious database is a log. And that log is the durable sequence of changes. Everything else is a view."
>
> — [3:18](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=198s) &middot; *grounds the claim in a precedent engineers already accept*

> "Compaction is lossy. A compacted summary is not going to perfectly reproduce the state of the agent in a smaller form. It's actually going to throw information away."
>
> — [4:47](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=287s) &middot; *takes a firm position against treating compaction as state-preserving*

> "it's cleanest to treat compaction as a best effort lossy fork, one that you can resume as a new log"
>
> — [5:26](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=326s) &middot; *concrete design prescription for handling context limits*

> "the log is not supposed to contain the whole world. The log is just the agent's view of the world"
>
> — [5:26](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=326s) &middot; *scopes the claim against the obvious side-effects objection*

> "If the agent sent an email, forking back won't unsend it. If some file got changed underneath, the agent won't know about it."
>
> — [6:03](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=363s) &middot; *an unusually candid statement of the approach's limits*

> "If you're using Cloud Code and your agent reaches a permission prompt and the process dies for whatever reason, and then you resume it, the permission prompt will be gone, and the agent will be paused. And that is unacceptable in production."
>
> — [6:45](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=405s) &middot; *names a specific, checkable failure in a widely used harness*

> "When the log is the agent, the executor is allowed to be fallible."
>
> — [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s) &middot; *compresses the reliability argument into a design principle*

> "When the log is the state, you flip that model. One process can now advance thousands of agents."
>
> — [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s) &middot; *the scalability claim, stated with a concrete magnitude*

> "One branch can run on Claude, another branch can run on GPT, another can run on your favorite open-source model."
>
> — [8:04](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=484s) &middot; *makes the model-portability payoff tangible*

> "the value is not just what the agent produced, it's also the log, which indicates how it got there"
>
> — [8:45](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=525s) &middot; *argues process, not just output, is the durable asset*

> "Claude code and Codex will write these messy JSONL files to local disk, and even in Claude SDK mode, those writes are fire and forget, which means that if for whatever reason the write fails, the data is gone."
>
> — [9:37](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=577s) &middot; *specific technical critique of existing harnesses*

> "the strongest form of lock-in isn't model lock-in. Models can be swapped. It's not API or tool lock-in either. Those can be wrapped, and those can be adapted. The deepest form of lock-in is actually log lock-in."
>
> — [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s) &middot; *the talk's most quotable strategic claim*

> "If a provider owns your log, then the provider effectively owns your agent"
>
> — [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s) &middot; *the ownership thesis in its sharpest form*

> "agents are arguably the most intimate piece of technology you'll ever run. For an agent to be useful, it needs to have your personal data, your company's data, your workflows, your decisions."
>
> — [11:46](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=706s) &middot; *explains why log ownership is framed as urgent rather than academic*

> "And if an agent is a running process, that's extremely terrifying. But if the agent is the log, it's simply an execution detail."
>
> — [12:28](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=748s) &middot; *reframes production failure modes as a consequence of the wrong abstraction*

> "you're going to stop treating the log as this exhaust from the system, and you're going to treat it as the system itself"
>
> — [14:10](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=850s) &middot; *the closing reframe the whole talk builds to*

## Positions

- An agent's identity is its log, not the model or the execution environment it runs in. ([0:00](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=0s), confidence: stated)
- The log alone is sufficient to resume an agent, because the model, tools, and runtime only read from and append to it. ([2:04](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=124s), confidence: stated)
- Everything else in an agent system — model context, UI, debugging, auditing, compaction — is a projection of the log, and only the log is not a projection. ([4:07](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=247s), confidence: stated)
- Compaction is lossy and should be treated as a best-effort fork resumed as a new log, with the raw log retained. ([5:26](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=326s), confidence: stated)
- The log cannot make the external world deterministic; side effects like sent emails or externally modified files are outside its scope, and that does not invalidate the thesis. ([6:03](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=363s), confidence: stated)
- Claude Code loses a pending permission prompt if the process dies and the session is resumed, which is unacceptable in production. ([6:45](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=405s), confidence: stated)
- Most agent harnesses run one process per agent, tying the agent to a specific machine; log-centric design removes sticky sessions, state migration, and coordination overhead. ([7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s), confidence: stated)
- Provider migration is only an adapter and schema problem, not an identity problem, if the log is the agent. ([9:37](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=577s), confidence: stated)
- Claude Code and Codex write JSONL logs to local disk with fire-and-forget writes in SDK mode, so failed writes lose data; OpenCode's SQLite state has documented corruption and data-loss issues. ([9:37](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=577s), confidence: stated)
- Log lock-in is a deeper and more durable form of vendor lock-in than model, API, or tool lock-in. ([11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s), confidence: stated)
- Every managed agent provider (Anthropic, Google) will move to own more of the stack — the hosted loop, memory, sandboxes, compaction, background agents. ([11:46](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=706s), confidence: stated)
- Teams should self-host or otherwise fully own and inspect their agent logs rather than leaving them on a provider's infrastructure. ([12:28](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=748s), confidence: implied)
- Real-world agent systems will inevitably face crashing workers, restarting machines, disappearing sandboxes, timed-out tool calls and failing providers, so durability must be architectural. ([12:28](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=748s), confidence: stated)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [context compaction](../concepts/context-compaction.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [durable execution](../concepts/durable-execution.md)
- [model portability](../concepts/model-portability.md)
- [session management](../concepts/session-management.md)

