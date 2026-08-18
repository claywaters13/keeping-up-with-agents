---
title: "Your Agent Is Wasting Tokens and You Don't Know It"
type: "talk"
slug: "your-agent-is-wasting-tokens-and-you-dont-know-it"
org: "AWS"
day: "Day 2 — Session Day 1"
room: "Expo Stage 1 NE"
video_id: "uiP88SpCi1Q"
duration_sec: 355
word_count: 1000
speakers: ["Dat Ngo"]
---

# Your Agent Is Wasting Tokens and You Don't Know It

*Program title: Your Agent Is Lying to You About Whether It Worked*

**Speakers:** [Dat Ngo](../speakers/dat-ngo.md)

**Org:** AWS

**Day/Room:** Day 2 — Session Day 1 &middot; Expo Stage 1 NE &nbsp;|&nbsp; **Duration:** 5m 55s

[Watch on YouTube](https://www.youtube.com/watch?v=uiP88SpCi1Q)

## Summary

A ~6-minute lightning talk from an AWS developer advocate laying out five concrete tactics for cutting token spend in agent systems: caching system prompts (and optionally tool prompts and messages), routing requests to cheaper or more expensive models by task difficulty, offloading large tool results to local or cloud storage and passing summaries instead, capping the number of tool-loop iterations, and trimming conversation history with a sliding window. Examples are shown in AWS's Strands Agents framework, though the speaker notes the techniques generalize across providers. The most useful part is the explicit tradeoff discussion around history trimming — a sliding window loses early context, so the speaker recommends summarizing what falls out of the window rather than dropping it. He also recommends running observability tooling before deployment to see how often and how long each tool call runs. Watch it if you want a fast, practical checklist; skip it if you want depth, benchmarks, or measured cost savings, since no numbers are reported.

## Key Points

- Caching the system prompt means the full prompt is sent only on the first agent call, with subsequent calls sending a much reduced payload; tool prompts and messages can be cached the same way.
- Agents should route by task difficulty — a cheap model like Claude Haiku for simple tasks and Claude Sonnet for harder ones — rather than defaulting to the most expensive model for everything.
- The routing decision itself can be delegated to a separate very cheap model instead of hand-written if-statements.
- Large tool results should be stored locally or in the cloud and summarized, so the full result isn't re-injected into context on every iteration of the agent loop.
- Uncapped tool loops can run 10 or 20 times or spiral into an infinite loop, so agents should always set a max-iterations limit.
- Observability tooling should be run before deployment to measure how long each tool call takes and how many times it loops, giving a per-tool efficiency picture.
- In multi-turn conversations the entire history is resent on every call, which can consume hundreds or thousands of tokens; Strands Agents ships a sliding window conversation manager that sends only the last 10 messages by default.
- The stated tradeoff of a sliding window is losing early conversation history, which the speaker suggests mitigating by summarizing the dropped history back into the context window.

## Notable Quotes

> "the idea is that you can add cache prompt equals default. And what that'll do is on the first call of your agent, it will send the full system prompt over and then on every subsequent call, it will have a much reduced system prompt being sent over."
>
> — [0:00](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=0s) &middot; *States the mechanism and payoff of prompt caching concretely.*

> "In this case, maybe we use Claude Haiku for a cheap something cheap and then use Claude Sonnet for something a little bit more difficult."
>
> — [0:51](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=51s) &middot; *Names specific models for the cheap/expensive routing split.*

> "You can even have another model that's very cheap decide which model to use."
>
> — [0:51](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=51s) &middot; *Proposes model-based routing over hardcoded logic.*

> "I highly recommend don't use the most expensive model for everything you're doing. You want to use multiple different models based on the use case."
>
> — [1:36](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=96s) &middot; *The talk's clearest normative stance on model selection.*

> "If you have a large tool result that's coming back, you can store it locally or in the cloud and then use some kind of summarization that saves on tokens."
>
> — [1:36](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=96s) &middot; *Compactly defines the tool-result offloading pattern.*

> "So if you can find any way that where you have this tool result that you don't necessarily send it on every single call back to the large language model, that will save a lot of tokens for you."
>
> — [2:15](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=135s) &middot; *Generalizes offloading beyond the framework-specific API.*

> "I've had this happen often where it calls the tool over and over and over again."
>
> — [2:15](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=135s) &middot; *Grounds the loop-capping advice in reported firsthand experience.*

> "And if you don't cap that tool call, then it might run 10, 20 times. It might get into an infinite loop, which would be very bad for your token usage. So always set a max iterations of how many times it will loop."
>
> — [2:59](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=179s) &middot; *Quantifies the failure mode and gives an unambiguous rule.*

> "A good thing you can do before you deploy your agent is to run some observability tools and take a look at the tool call use for every single tool and then see how long each one of them is running and how many times they're looping."
>
> — [2:59](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=179s) &middot; *The only measurement-oriented recommendation in the talk.*

> "you will find at times that the conversation history will get very large on every single call, that whole conversation history will be sent back to the large language model. And this can eat through hundreds, if not thousands, of tokens."
>
> — [3:40](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=220s) &middot; *Reports the scale of the multi-turn history cost.*

> "In Strand's agents, we have something called sliding window conversation manager, which which this does is it looks back at the last 10 messages and only sends those back."
>
> — [3:40](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=220s) &middot; *Names the concrete mechanism and its default window size.*

> "The downfall of this, or the trade-off of this, I should say, is that you will lose the message history from the beginning."
>
> — [4:23](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=263s) &middot; *The talk's most explicit tradeoff statement.*

> "The way you want to deal with that is you can use uh some sort of summarization of the history and then put that into the context window."
>
> — [4:23](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=263s) &middot; *Gives the mitigation for the sliding-window information loss.*

> "Cache the system prompt. And if you can, maybe the tool prompt and messages. Route by difficulty. Don't use the same expensive model for everything you're doing, for every single task."
>
> — [4:23](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=263s) &middot; *The compressed summary of the talk's checklist.*

## Positions

- Caching the system prompt reduces the payload on every call after the first, since only a much reduced system prompt is sent subsequently. ([0:00](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=0s), confidence: stated)
- Prompt caching is not specific to Strands Agents — it works across model providers. ([0:00](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=0s), confidence: stated)
- You should not use the most expensive model for every task; agents should route across multiple models based on use case. ([1:36](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=96s), confidence: stated)
- A cheap model can be used as the router that decides which model handles a given request. ([0:51](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=51s), confidence: stated)
- Large tool results should be stored outside the context and summarized rather than re-sent to the LLM on every loop iteration. ([1:36](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=96s), confidence: stated)
- Agents should always set a maximum iteration count on tool loops, because uncapped loops can run 10-20 times or become infinite. ([2:59](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=179s), confidence: stated)
- Observability tooling should be run on tool calls before deploying an agent to production. ([2:59](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=179s), confidence: stated)
- Resending full conversation history in multi-turn agents can consume hundreds to thousands of tokens per call. ([3:40](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=220s), confidence: stated)
- Sliding-window history trimming costs you the beginning of the conversation, and summarizing the dropped history into context is the right mitigation. ([4:23](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=263s), confidence: stated)
- Token waste in agents is largely an engineering-hygiene problem solvable with five well-known tactics rather than requiring model or architecture changes. ([5:03](https://www.youtube.com/watch?v=uiP88SpCi1Q&t=303s), confidence: implied)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [context compaction](../concepts/context-compaction.md)
- [context window management](../concepts/context-window-management.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [model routing](../concepts/model-routing.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)

