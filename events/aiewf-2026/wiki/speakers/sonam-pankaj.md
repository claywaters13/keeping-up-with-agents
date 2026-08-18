---
title: "Sonam Pankaj"
type: "speaker"
slug: "sonam-pankaj"
talk_count: 1
---

# Sonam Pankaj

## Talks

- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent skills](../concepts/agent-skills.md)
- [context rot](../concepts/context-rot.md)
- [data flywheels](../concepts/data-flywheels.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [rubric design](../concepts/rubric-design.md)

## Quotes

> "An agent is an LLM that has agency to reason, invoke tools, uh, interact with the real world, retrieve uh the memory to complete the task. One major loop here is missing is uh learning."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [0:01](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=1s)

> "Gartner reported 85% of AI just failing traction. So, it's in McKinsey's 2025 report. The problem came out to be most of the time is that retrieval is static."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [0:48](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=48s)

> "73% of our uh pipelines fails because of retrieval, not generation, and context stuffing."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [1:39](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=99s)

> "We made wrong answers appear faster and cheaper, but we forgot to make retrieval learn."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [1:39](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=99s)

> "The eval signal dies in the dashboard. This is a missing layer, a system that consume traces, absorb eval, and convert both into retrieval guidance for future runs."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [2:35](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=155s)

> "current memory is that they basically store user preferences, profile, conversation history, or long-lived personalization. So, chat experience is not self-improving learning systems for production."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [3:32](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=212s)

> "we have come up with something called utility score, which is a similarity weighted by how useful it is for the agent to execute the task."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [3:32](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=212s)

> "It's a runtime layer that let the large language agent improve from experiences without retraining, fine-tuning, or manual prompt engineering."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [4:37](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=277s)

> "How it's a little different from compile time like DS5 because of you bake in all the lessons in the prompt, here is actually improving while it is executing the task."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [4:37](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=277s)

> "you do not retrieve by keyword, you do retrieve by semantic similarity to the current task weighted by whether those memories have historically helped or hurt the execution or the outcome."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [4:37](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=277s)

> "The event outcome becomes a first-class signal in the retrieval re-ranking and not just for retrieval."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [5:29](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=329s)

> "One of the key things is it treat memory as reasoning, not as facts, statistics, fact with no context and no history, but reasoning."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [5:29](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=329s)

> "So, we have seen the performance improve from 66 to 76% without baking in uh skills and with skills reflect performance at 80."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s)

> "once there are enough memory like 10 memories, uh what we do is we bake in the reasoning and the understanding into skills so that your agent always remains updated."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s)

> "Even though that column is no useful anymore, it remains in the system prompt. So, there's no system right now that can update that"
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [7:22](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=442s)

> "with the other memory system, it gets to 58.2. But with the refined memory system, uh, it gets to 61.3%."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [8:14](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=494s)

> "First of all, there's a cold start. So, in the beginning, it's pure semantic search until, uh, enough reviews have been accumulated."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [8:14](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=494s)

> "So, we have built reflect in such a way that most of these problems and most of these elements are now reduced except for cold start which we cannot do much about it."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [9:07](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=547s)

> "it's forming memories which is retrieved based on the utility score that is the score which basically keeps improving keeps re-ranking itself on the basis of how useful that memory was."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [13:39](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=819s)

