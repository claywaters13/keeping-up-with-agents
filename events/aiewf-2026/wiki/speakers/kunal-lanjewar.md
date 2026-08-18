---
title: "Kunal Lanjewar"
type: "speaker"
slug: "kunal-lanjewar"
role: "Staff Engineer"
company: "Riot Games"
talk_count: 1
---

# Kunal Lanjewar

**Staff Engineer &middot; Riot Games**

Kunal Lanjewar runs tier-zero infrastructure at Riot Games, where he builds and operates production AI agents and backend services that power games like VALORANT and League of Legends. He's the author of Guild, an open-source tool that gives AI agents persistent memory and task coordination across sessions. Previously, he helped scale Sky: Children of the Light to 300M+ downloads and millions of daily active players, and built the backend for its Guinness World Record-holding Aurora concert. His work has been featured at GDC, DataCon LA, and on the MongoDB Podcast. Earlier in his career he also built systems for NASA missions.

[LinkedIn](https://www.linkedin.com/in/kunallanjewar/)

## Talks

- [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md) (AI-Native Enterprises)

## Scheduled Sessions

- **Your Hero Agent Needs a Party** &middot; Day 4 — Session Day 3 &middot; 2:25pm-2:45pm &middot; Leadership 1

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [durable execution](../concepts/durable-execution.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [model portability](../concepts/model-portability.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [simulation environments](../concepts/simulation-environments.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

## Quotes

> "We've had the save button for documents for decades now. Since the 1980s, people have been used to pressing control S, command S uh or auto saving while you're working to have a persistent state. But agents, they don't have that today."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [0:00](https://www.youtube.com/watch?v=bZISsg7H7DA&t=0s)

> "The only thing we have which is closest is a trace. A trace gives you the emitted telemetry data of how an agent calls tools in the input and output of that state."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [0:00](https://www.youtube.com/watch?v=bZISsg7H7DA&t=0s)

> "all of that is lost and it is only stamped as a read-only trace by the end, which is sitting in another tool far away from where the actual code is"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [0:47](https://www.youtube.com/watch?v=bZISsg7H7DA&t=47s)

> "I think this is what's missing today in the industry is that we don't have a clear connection between the observability spans that are emitted with Odel and the execution."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [0:47](https://www.youtube.com/watch?v=bZISsg7H7DA&t=47s)

> "Well, save allows you to replay. You can go back in history and ask the what if question."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [1:25](https://www.youtube.com/watch?v=bZISsg7H7DA&t=85s)

> "So, checkpoint replay diff decide. And this is really the methodology that that I've seen and I've seen others do, uh which has really scaled."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [3:37](https://www.youtube.com/watch?v=bZISsg7H7DA&t=217s)

> "It's It's It's basically evaluating using your production traces. So, it's basically evaluating using your production checkpoints."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [3:37](https://www.youtube.com/watch?v=bZISsg7H7DA&t=217s)

> "now they've reduced it to 5 minutes uh with hundreds of simulations, have 90% less hallucinations, and they're still two points within what they've seen in production"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [4:27](https://www.youtube.com/watch?v=bZISsg7H7DA&t=267s)

> "So, the simulations are pretty good because they're grounded in what's already happened."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [4:27](https://www.youtube.com/watch?v=bZISsg7H7DA&t=267s)

> "and this combination of code and the artifacts that it created and the environment in which it ran in, whether it was a Docker image or a sandbox, those are all snapshotted in state here between the checkpoints"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [5:49](https://www.youtube.com/watch?v=bZISsg7H7DA&t=349s)

> "because I have the code, it's very easy for me to do tool calls and to change these particular things and do more experiments than I would have had if I was completely disconnected from the code base"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [8:01](https://www.youtube.com/watch?v=bZISsg7H7DA&t=481s)

> "is to be using agents and LLMs to analyze these cohorts across a plethora of data because at some point uh, I mean, 10 is probably easy to do, but what if you have thousands?"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [11:44](https://www.youtube.com/watch?v=bZISsg7H7DA&t=704s)

> "this is where skills and MCP servers get really relevant and having the runtime be queryable and go into your execution and fetch the artifacts is very important"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [12:41](https://www.youtube.com/watch?v=bZISsg7H7DA&t=761s)

> "what I've personally seen is that having a naive model swap usually or often times doesn't work"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [13:24](https://www.youtube.com/watch?v=bZISsg7H7DA&t=804s)

> "they saw that there could be a false economy if you do a naive model swap because it might look on paper that you're faster and you're cheaper, but at the end of the day you have to look at the value created"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s)

> "a model that passes 60% of the time is only self-consistent about a quarter of the time"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s)

> "So which basically means that one replay is just an anecdote and having a cohort analysis is way way way better."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s)

> "This can get very expensive of course and this is where you have to be really smart about what you replay and have tooling that really helps you."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [14:44](https://www.youtube.com/watch?v=bZISsg7H7DA&t=884s)

> "you can start from real runs, not synthetic, but real runs, real production uh state"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [14:44](https://www.youtube.com/watch?v=bZISsg7H7DA&t=884s)

> "Um never ship anything by just replaying one or two things. Um and just do this at scale and uh ship, route, and hold, and try to automate that loop as much as possible."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [15:28](https://www.youtube.com/watch?v=bZISsg7H7DA&t=928s)

> "So, the verdict is don't ship. So, even though it looked like from a single replay that it was cheaper to do and we reached the same result, across a bunch of those support cases, you actually saw that our agent concludes that you shouldn't be using a cheaper model in this particular case for your data."
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [15:28](https://www.youtube.com/watch?v=bZISsg7H7DA&t=928s)

> "you can do this if you model your agent with your harness in a runtime that can checkpoint state and is able to replay that state from code with different scenarios"
>
> — [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [16:11](https://www.youtube.com/watch?v=bZISsg7H7DA&t=971s)

