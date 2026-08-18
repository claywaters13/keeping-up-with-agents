---
title: "Ishaan Sehgal"
type: "speaker"
slug: "ishaan-sehgal"
talk_count: 1
---

# Ishaan Sehgal

## Talks

- [The Log Is The Agent](../talks/the-log-is-the-agent.md)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [context compaction](../concepts/context-compaction.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [durable execution](../concepts/durable-execution.md)
- [model portability](../concepts/model-portability.md)
- [session management](../concepts/session-management.md)

## Quotes

> "most people think of an agent as the model or the execution environment that it's running in and I think that that's the wrong abstraction"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [0:00](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=0s)

> "if your PlayStation bursts into flames, your character isn't gone. You can buy another PlayStation, you can download your save file from the cloud and you can resume exactly where they were"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [0:35](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=35s)

> "the log is the append-only event history of the agent. It's every user input, every model output, every tool called, tool result, permission, failure"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [1:15](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=75s)

> "The important insight is not that this loop is complicated. The important insight is that the loop is disposable."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [2:46](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=166s)

> "underneath every serious database is a log. And that log is the durable sequence of changes. Everything else is a view."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [3:18](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=198s)

> "Compaction is lossy. A compacted summary is not going to perfectly reproduce the state of the agent in a smaller form. It's actually going to throw information away."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [4:47](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=287s)

> "it's cleanest to treat compaction as a best effort lossy fork, one that you can resume as a new log"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [5:26](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=326s)

> "the log is not supposed to contain the whole world. The log is just the agent's view of the world"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [5:26](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=326s)

> "If the agent sent an email, forking back won't unsend it. If some file got changed underneath, the agent won't know about it."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [6:03](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=363s)

> "If you're using Cloud Code and your agent reaches a permission prompt and the process dies for whatever reason, and then you resume it, the permission prompt will be gone, and the agent will be paused. And that is unacceptable in production."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [6:45](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=405s)

> "When the log is the agent, the executor is allowed to be fallible."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s)

> "When the log is the state, you flip that model. One process can now advance thousands of agents."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s)

> "One branch can run on Claude, another branch can run on GPT, another can run on your favorite open-source model."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [8:04](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=484s)

> "the value is not just what the agent produced, it's also the log, which indicates how it got there"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [8:45](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=525s)

> "Claude code and Codex will write these messy JSONL files to local disk, and even in Claude SDK mode, those writes are fire and forget, which means that if for whatever reason the write fails, the data is gone."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [9:37](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=577s)

> "the strongest form of lock-in isn't model lock-in. Models can be swapped. It's not API or tool lock-in either. Those can be wrapped, and those can be adapted. The deepest form of lock-in is actually log lock-in."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s)

> "If a provider owns your log, then the provider effectively owns your agent"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s)

> "agents are arguably the most intimate piece of technology you'll ever run. For an agent to be useful, it needs to have your personal data, your company's data, your workflows, your decisions."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:46](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=706s)

> "And if an agent is a running process, that's extremely terrifying. But if the agent is the log, it's simply an execution detail."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [12:28](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=748s)

> "you're going to stop treating the log as this exhaust from the system, and you're going to treat it as the system itself"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [14:10](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=850s)

