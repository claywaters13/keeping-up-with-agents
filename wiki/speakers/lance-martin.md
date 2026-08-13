---
title: "Lance Martin"
type: "speaker"
slug: "lance-martin"
role: "Member of Technical Staff"
company: "Anthropic"
talk_count: 1
---

# Lance Martin

**Member of Technical Staff &middot; Anthropic**

Member of technical staff at Anthropic. Working on the Claude Platform, including Claude Managed Agents and the claude-api skill in Claude Code. Prior to Anthropic, was one of the early team at LangChain. Prior to LangChain, spent several years focused on vision for self-driving cars (Uber ATG, Ike, Nuro) and got a PhD from Stanford.

[LinkedIn](https://www.linkedin.com/in/lance-martin-64a33b5)

## Talks

- [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md) (Claws & Personal Agents)

## Scheduled Sessions

- **Claude for long-horizon tasks** &middot; Day 2 — Session Day 1 &middot; 1:55pm-2:15pm &middot; Track 1

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [background agents](../concepts/background-agents.md)
- [context compaction](../concepts/context-compaction.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [verifier design](../concepts/verifier-design.md)

## Quotes

> "you can think about Claude as a light source and you can think about products as windows that allow the light to pass through"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [0:01](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1s)

> "models could only do, you know, maybe 10 to 20 minutes of autonomous work. This is measured by meter. And in that regime, only certain product surfaces made sense."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [0:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=44s)

> "when models can only do like an hour of work, async as an experience is kind of bad. Um the model goes off and it like hits an error and it comes back to you over a short period of time."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [1:25](https://www.youtube.com/watch?v=9QebvrrY3KY&t=85s)

> "we released a new API called Managed Agents, which basically packages both the harness as well as all the managed deployment infrastructure for you"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [2:33](https://www.youtube.com/watch?v=9QebvrrY3KY&t=153s)

> "giving Claude access to a bunch of your secrets and letting it run for 10 hours and not watching it can be a little bit spooky and have some security concerns, especially as models get extremely capable"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [4:01](https://www.youtube.com/watch?v=9QebvrrY3KY&t=241s)

> "the harness becomes a stateless process that talks to a session. The session is an append-only event log and that can reach out to hands, which are just containers."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [4:01](https://www.youtube.com/watch?v=9QebvrrY3KY&t=241s)

> "If the session, uh sorry, if the harness dies or sandbox dies, it's completely fine because the session is always backed up in this append-only log and credentials are never actually added to the sandbox."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [4:38](https://www.youtube.com/watch?v=9QebvrrY3KY&t=278s)

> "when you're doing something like compaction, you're choosing some logic to retain some amount of context, and naively in a typical in a kind of a typical step, you're discarding all the context that you didn't compact"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [5:17](https://www.youtube.com/watch?v=9QebvrrY3KY&t=317s)

> "when you ask them to do a bunch of work and then say, "Okay, grade your work." If that same context is being used to both do the work and grade, you can get lots of odd artifacts and confabulation"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [5:54](https://www.youtube.com/watch?v=9QebvrrY3KY&t=354s)

> "what we found is it's quite effective to separate verification into a separate context window. This is a very general trend."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [6:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=404s)

> "in Claude code you have goal and manage agents you have outcomes and the principles are really the same. You're setting up a measurable end state in both cases."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [7:24](https://www.youtube.com/watch?v=9QebvrrY3KY&t=444s)

> "instead of encoding steering me and into like me as the human, you're encoding the signal into the environment"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [8:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=524s)

> "this paradigm of loops, which a lot of people been talking about today, paired with very capacity models is a very good general primitive for long-running asynchronous work"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [9:40](https://www.youtube.com/watch?v=9QebvrrY3KY&t=580s)

> "higher capacity models have a better sense of like what abstraction to save to memory that'll be useful later. Like they're not just writing a specific fact."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [13:02](https://www.youtube.com/watch?v=9QebvrrY3KY&t=782s)

> "when I'm writing memory in band over the course of a day over the course of a session, sometimes you can write incorrect memories. And or you're writing things that are locally optimal, but not globally optimal."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [13:02](https://www.youtube.com/watch?v=9QebvrrY3KY&t=782s)

> "Five out of five replicates with raw memory store fell down this trap. With the dreaming, this error is corrected, and it's able to properly localize itself and not fall fall down this trap."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [14:14](https://www.youtube.com/watch?v=9QebvrrY3KY&t=854s)

> "those mistakes get stuck in memory unless you have an offline process to kind of correct them"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [15:40](https://www.youtube.com/watch?v=9QebvrrY3KY&t=940s)

> "we released Claude Tag and a lot of the reaction was like, "Ah, Slack bot.""
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [16:17](https://www.youtube.com/watch?v=9QebvrrY3KY&t=977s)

> "Its identity and credentials are not tied to a given user and has access to organizational level context, not just my local context."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [16:51](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1011s)

> "when you your own personal harness, often new employees takes them weeks or maybe even months to kind of ramp up fully to configure all the right connectors"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [16:51](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1011s)

> "to build real agents that can operate in these long time horizons, a bunch of things need to come together in terms of like architecture, infrastructure, security, memory"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [21:05](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1265s)

> "what I've seen doesn't work is when you specify the structure of memory for the model very explicitly, whether that's in a file system or database or whatever"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [22:41](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1361s)

> "Let the model structure and maintain its own memory. Don't give it a prescribed memory schema."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [23:25](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1405s)

> "Models can reason about their own memory and context structure much better than you can prescribe for them a way to structure their own memories."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [23:25](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1405s)

> "we've actually run a lot of different evals showing that dreaming can indeed improve performance for very intuitive reasons as you see here. But of course, evals are important in like your own context to confirm it's actually worth the offline compute."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [24:13](https://www.youtube.com/watch?v=9QebvrrY3KY&t=1453s)

