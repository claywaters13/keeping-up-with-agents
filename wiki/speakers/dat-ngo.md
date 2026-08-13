---
title: "Dat Ngo"
type: "speaker"
slug: "dat-ngo"
role: "AI Architect"
company: "Arize AI"
talk_count: 1
---

# Dat Ngo

**AI Architect &middot; Arize AI**

Dat Ngo is an AI Architect at Arize AI focused on agent harnesses, evaluation, observability, and scalable LLM-evaluation pipelines for production AI systems.

## Talks

- [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

## Scheduled Sessions

- **Your Agent Is Lying to You About Whether It Worked** &middot; Day 2 — Session Day 1 &middot; 12:05pm-12:25pm &middot; Expo Stage 1 NE

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [context compaction](../concepts/context-compaction.md)
- [context window management](../concepts/context-window-management.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [model routing](../concepts/model-routing.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)

## Quotes

> "the idea is that you can add cache prompt equals default. And what that'll do is on the first call of your agent, it will send the full system prompt over and then on every subsequent call, it will have a much reduced system prompt being sent over."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [0:00](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=0s)

> "In this case, maybe we use Claude Haiku for a cheap something cheap and then use Claude Sonnet for something a little bit more difficult."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [0:51](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=51s)

> "You can even have another model that's very cheap decide which model to use."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [0:51](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=51s)

> "I highly recommend don't use the most expensive model for everything you're doing. You want to use multiple different models based on the use case."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [1:36](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=96s)

> "If you have a large tool result that's coming back, you can store it locally or in the cloud and then use some kind of summarization that saves on tokens."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [1:36](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=96s)

> "So if you can find any way that where you have this tool result that you don't necessarily send it on every single call back to the large language model, that will save a lot of tokens for you."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [2:15](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=135s)

> "I've had this happen often where it calls the tool over and over and over again."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [2:15](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=135s)

> "And if you don't cap that tool call, then it might run 10, 20 times. It might get into an infinite loop, which would be very bad for your token usage. So always set a max iterations of how many times it will loop."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [2:59](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=179s)

> "A good thing you can do before you deploy your agent is to run some observability tools and take a look at the tool call use for every single tool and then see how long each one of them is running and how many times they're looping."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [2:59](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=179s)

> "you will find at times that the conversation history will get very large on every single call, that whole conversation history will be sent back to the large language model. And this can eat through hundreds, if not thousands, of tokens."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [3:40](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=220s)

> "In Strand's agents, we have something called sliding window conversation manager, which which this does is it looks back at the last 10 messages and only sends those back."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [3:40](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=220s)

> "The downfall of this, or the trade-off of this, I should say, is that you will lose the message history from the beginning."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [4:23](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=263s)

> "The way you want to deal with that is you can use uh some sort of summarization of the history and then put that into the context window."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [4:23](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=263s)

> "Cache the system prompt. And if you can, maybe the tool prompt and messages. Route by difficulty. Don't use the same expensive model for everything you're doing, for every single task."
>
> — [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [4:23](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=263s)

