---
title: "Gagan Bhat"
type: "speaker"
slug: "gagan-bhat"
role: "Member of Technical Staff"
company: "Anthropic"
talk_count: 1
---

# Gagan Bhat

**Member of Technical Staff &middot; Anthropic**

Gagan is a Product Engineer on Anthropic's Applied AI team. He focuses on prototyping consumer AI features, evaluating model output in vertical domains, and partnering with industry leaders to productize use-cases. Prior to Anthropic, he was an engineer at NVIDIA and Netflix.

[LinkedIn](https://www.linkedin.com/in/gagan-bhat/)

## Talks

- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md) (Workshops Day 1, co-presented)

## Scheduled Sessions

- **Evolution of agentic surfaces** &middot; Day 1 — Workshop Day &middot; 4:30pm-5:30pm &middot; Track 9

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [context compaction](../concepts/context-compaction.md)
- [context engineering](../concepts/context-engineering.md)
- [latency budgets](../concepts/latency-budgets.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [rubric design](../concepts/rubric-design.md)
- [session management](../concepts/session-management.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "that is that harnesses encode assumptions about what Claude cannot do on its own"
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [7:29](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=449s)

> "So, when the model moves and the harness doesn't, it degrades the agent."
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [8:45](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=525s)

> "Opus 4.5 no longer exhibited context anxiety, which means that the fixes that we'd added into the harness itself became dead weight. In fact, it became pure overhead, adding things like latency and causing issues with the cache being discarded incorrectly at times."
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [8:08](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=488s)

> "What you don't want to do is have a stale harness that takes weeks or even months to migrate to a new model, especially with how model release cycles have been coming out shorter and shorter."
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [9:23](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=563s)

> "we saw 60% faster time to first token for P50 use cases or median use cases. And over 90% improvements in latency for time to first token in P95 use cases."
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [23:55](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1435s)

> "harnesses have become the limiting factor to what models can achieve"
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [30:20](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1820s)

> "We took it a step further by introducing the concept of vaults, where you can store security credentials in a secure way, and they're decrypted only when needed at tool execution runtime."
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [22:01](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1321s)

> "if you feed the transcripts and the memory state as a periodic batch process with what we call dreaming, it allows us to extract new insights and new organized structures that essentially feed back and edit the memory as needed to make the next day's agent sessions automatically much more intelligent"
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [27:07](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1627s)

> "If the grader determines that the agent was not able to complete the task, it'll keep trying until it reaches that success criteria that you have defined for your agent."
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [28:58](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1738s)

> "the container was blocking the agent being able to start its model reasoning"
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [11:24](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=684s)

> "The session log essentially contains events of everything that happened during an agent execution."
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [23:55](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1435s)

> "It's a different story to build an agent that runs in your laptop and serves you as a single user compared to when you actually want to deploy it in production and run it at scale for hundreds of thousands or even millions of users."
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [13:55](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=835s)

> "Initially, we used to only give them questions, simple Q&A. We then started delegating tasks to them. And now, we let agents own entire outcomes."
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [1:24](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=84s)

> "with MCP tunnels, they can have their MCP servers run only within their private network and only making outbound calls to the Claude agent loop"
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [25:53](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1553s)

> "with many traditional harness implementations, the context window in the session are one in the same"
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [14:33](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=873s)

> "This is context management and domain expertise. This is what separates a coding agent from a legal agent or go-to-market agent"
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [16:03](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=963s)

