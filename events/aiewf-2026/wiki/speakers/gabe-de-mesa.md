---
title: "Gabe De Mesa"
type: "speaker"
slug: "gabe-de-mesa"
talk_count: 1
---

# Gabe De Mesa

## Talks

- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agent skills](../concepts/agent-skills.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [context compaction](../concepts/context-compaction.md)
- [data flywheels](../concepts/data-flywheels.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [generative ui](../concepts/generative-ui.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [legacy code migration](../concepts/legacy-code-migration.md)

## Quotes

> "all of our product suites and product teams have built tools and skills in order to power this button"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [2:14](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=134s)

> "originally we were on LangGraph and that was fine until the team really started to scale uh and our use cases started to evolve"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [5:16](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=316s)

> "we decided to move over to our own kind of Effect Native Agent Loop to have full regency over this uh Agent Loop such that if we have complex use cases or features that we need to build, we could kind of get in we we had full control of the of the Agent Loop"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [6:00](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=360s)

> "all the cool things you get with Effect is now propagated throughout the entire Agent Loop, like the tracing, structured concurrency, the logging, everything is more fine-grained control"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [6:00](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=360s)

> "since we're kind of doing dependency injection, we could pass in a different language model if we were to uh hot swap to another one"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [6:43](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=403s)

> "having this kind of rigorous protocol, this rigorous spec really helped drive our development and drive alignment because, you know, all we had to do was um align with this spec and follow this spec and we knew that this was kind of the contract that our front end and back end would both consume and and produce"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [8:14](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=494s)

> "Shipping is the start, not the finish."
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [8:56](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=536s)

> "in in the in our CI we we have evals that run against real completions, so we could test the prompt against, "Hey, did it hit some tools? Did it do what it's supposed to do?""
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [9:44](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=584s)

> "we deterministically interrupt the agent loop if there is a tool call approval required"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [10:28](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=628s)

> "especially when the agent's trying to do a mutating operation and always always always making sure that, um, humans are in the driver's seat"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [10:28](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=628s)

> "whenever an agent tries to execute code or tries to create files, it does so in a sandbox"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [11:10](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=670s)

> "we found that having some sort of um rolling summarization was more effective than you know always stuffing in the latest and most recent uh messages"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [12:12](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=732s)

> "when you have this rolling summary of a a really long conversation, then you could do recall over that uh summarization"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [13:16](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=796s)

> "the agent had this primitive registered uh uh this form, and it was able to build out this form for me at runtime and give me some options of what I could choose from"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [13:56](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=836s)

> "You can't scale what you can't see."
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [14:37](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=877s)

> "especially working in agentic systems where we're we're integrating with other teams and other APIs and other um other platform capabilities"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [15:24](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=924s)

> "we believe that tools and skills are really all you need"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [16:16](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=976s)

> "we're building tools and skills for customer-facing uh agents and and that has been great, but we're also building them internally as well to help accelerate our development workflows"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [17:48](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=1068s)

