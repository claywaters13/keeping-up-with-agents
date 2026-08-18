---
title: "Dan Farrelly"
type: "speaker"
slug: "dan-farrelly"
role: "CTO and Co-founder"
company: "Inngest"
talk_count: 1
---

# Dan Farrelly

**CTO and Co-founder &middot; Inngest**

Dan Farrelly is CTO and co-founder of Inngest, a platform for durable serverless functions, workflows and agent orchestration. He was previously CTO at Buffer and created developer tools including Timezone.io and MailDev.

[LinkedIn](https://www.linkedin.com/in/djfarrelly)

## Talks

- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md) (Agent & Harness Engineering)

## Scheduled Sessions

- **Your agent architecture has a half-life of 6 months** &middot; Day 3 — Session Day 2 &middot; 12:05pm-12:25pm &middot; Expo Stage 1 NE

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [background agents](../concepts/background-agents.md)
- [durable execution](../concepts/durable-execution.md)
- [rubric design](../concepts/rubric-design.md)

## Quotes

> "So speaking of building agents if you've been building agents for more than 6 months, you've likely rewritten something, maybe more than once."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [1:04](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=64s)

> "Some parts of your code likely survives. But did they survive by accident?"
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [1:04](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=64s)

> "So, in my opinion, there are three discrete layers. First, the execution layer. I think of this as the brain. It's where flow, state, durability, retries happen."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [2:42](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=162s)

> "This is models, prompts, tools, memory. This is the layer that changes the most."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [2:42](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=162s)

> "So, prompts last weeks, if you're lucky, maybe maybe a single week. Uh the models that you use, months, again, if you're lucky. Uh but I think that execution can last years, if you do it right."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [3:37](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=217s)

> "And what happens then is that one layer's half-life kind of leaks and drags the other components down. You're building it's technical debt by another name."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [3:37](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=217s)

> "So, my thesis is think in layers. Decouple them. So, let's talk about what I mean."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [4:24](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=264s)

> "But I think in a lot of these situations, the abstractions either are not there at all or they're too high-level or the layers merge."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [4:24](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=264s)

> "And I define it as the execution layer as being the system responsible for running your code reliably, managing how, when, or whether each piece of work completes."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [5:49](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=349s)

> "You can swap the model, swap the context, swap the sandbox, the execution layer should be able to remain the same."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s)

> "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s)

> "So, if you can't see the entirety of a trace from the trigger through the whole stack, it's really hard to debug it, let alone improve your agent and keep evolving it."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [9:08](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=548s)

> "So, using it for durability, snapshots, or something in state, I think is an anti-pattern."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [9:57](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=597s)

> "So, I think of the sandbox as the hands and execution as the brain."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [9:57](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=597s)

> "They're all long-running. They're asynchronous. They're delegated. That means that you need to be able to observe them all uh down to the core."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [10:46](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=646s)

> "It's going to have maybe hundreds of calls to you know, maybe 200 tool calls. You're going to probably guarantee to have at least one failure in that."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [11:35](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=695s)

> "So, the frameworks of 3 months ago were not designed to handle this. Right? Like you're going to need to design these systems yourself."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [12:27](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=747s)

> "the middle of the execution layer, when your agent is running, is a key place to instrument and score your agents"
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [16:28](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=988s)

> "Instead of a thumbs up, thumbs down, it's like did we open the PR, right? If it's a research agent, was this research saved? Was it a good report?"
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [18:02](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=1082s)

> "And I think if you can get your execution layer right and think about the right primitives, everything else can quickly evolve around it."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [18:02](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=1082s)

