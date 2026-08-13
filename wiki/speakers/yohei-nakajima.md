---
title: "Yohei Nakajima"
type: "speaker"
slug: "yohei-nakajima"
role: "Managing Partner"
company: "Untapped Capital"
talk_count: 1
---

# Yohei Nakajima

**Managing Partner &middot; Untapped Capital**

Yohei Nakajima is a General Partner and co-founder of Untapped Capital, a pre-seed venture fund backing unexpected founders at the earliest stages. He is best known as the creator of BabyAGI, one of the early open-source autonomous agent experiments that helped popularize task-driven AI agents. Yohei’s work sits at the intersection of venture capital, software prototyping, and frontier AI research: he builds tools and experiments to understand where technology is going, then uses those lessons to support founders and shape investment theses.

Most recently, Yohei has been developing ActiveGraph, an event-log-native architecture for building agents that are replayable, inspectable, forkable, and capable of continuous improvement. Across investing, writing, demos, and open-source projects, his approach is simple: build to learn, share what works, and help more people understand what AI-native systems make possible.

[LinkedIn](https://www.linkedin.com/in/yoheinakajima)

## Talks

- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md) (Graphs)

## Scheduled Sessions

- **Active Graph Agent Runtime (BabyAGI 4)** &middot; Day 4 — Session Day 3 &middot; 11:10am-11:30am &middot; Track 5

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent skills](../concepts/agent-skills.md)
- [audit trails](../concepts/audit-trails.md)
- [durable execution](../concepts/durable-execution.md)
- [graph rag](../concepts/graph-rag.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)

## Quotes

> "agents are awesome, but long-running agents break. And if they're so awesome, why am I still building them? Why they should build themselves."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [0:01](https://www.youtube.com/watch?v=khVX_BUnEwU&t=1s)

> "Let's build the simplest thing that can build itself has basically been kind of my research theme for the last 3 years since I did baby AGI back in March of 2023."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [0:01](https://www.youtube.com/watch?v=khVX_BUnEwU&t=1s)

> "over the course of 3 years I've done nine iterations of baby AGI with less fanfare"
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [0:52](https://www.youtube.com/watch?v=khVX_BUnEwU&t=52s)

> "ActiveGraph is an event-sourced graph runtime for building auditable agents."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [1:22](https://www.youtube.com/watch?v=khVX_BUnEwU&t=82s)

> "today most people build agents around the LLM. You start with the LLM, you add a response API, you give it tools, you add memory, and then you make sure you log everything correctly"
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [2:00](https://www.youtube.com/watch?v=khVX_BUnEwU&t=120s)

> "ActiveGraph asks, what if you build around the log?"
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [2:00](https://www.youtube.com/watch?v=khVX_BUnEwU&t=120s)

> "Nobody here is using the same agent they were using a year ago, and the agent you're going to use a year from now is going to be different."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [2:00](https://www.youtube.com/watch?v=khVX_BUnEwU&t=120s)

> "let's flatten that down into a single immutable event log, and this is the ground truth of the agent"
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [2:35](https://www.youtube.com/watch?v=khVX_BUnEwU&t=155s)

> "LLMs don't talk to each other in ActiveGraph. They all communicate through this shared state, and that's what makes it a little bit different."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [3:04](https://www.youtube.com/watch?v=khVX_BUnEwU&t=184s)

> "in the end you get this beautiful typed event log, which gives you replays. It gives you rollbacks and it gives you forks."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [3:43](https://www.youtube.com/watch?v=khVX_BUnEwU&t=223s)

> "this is not a harness. It's it's a runtime and you can actually rebuild most of the common harnesses on top of it."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [4:19](https://www.youtube.com/watch?v=khVX_BUnEwU&t=259s)

> "It is much more complex about actually pretty unintuitive. I would never write code myself with ActoGraph, but again, AI seems really good at it."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [6:33](https://www.youtube.com/watch?v=khVX_BUnEwU&t=393s)

> "it's inspired by uh blackboard architecture from the '70s or '80s or more recently Kafka, whole bunch of micro workers communicating through a shared state"
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [7:10](https://www.youtube.com/watch?v=khVX_BUnEwU&t=430s)

> "now, AI writes the code, and the workers can be very powerful because they have reasoning capability"
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [7:10](https://www.youtube.com/watch?v=khVX_BUnEwU&t=430s)

> "There was no semantic uh ingestion, no fact extraction, no entity extraction, but I just embedded the query, looked for relevant messages, grabbed a couple messages before and after, made sure it fit into the context, and it actually did pretty well on long mem eval"
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [8:17](https://www.youtube.com/watch?v=khVX_BUnEwU&t=497s)

> "for these loops, it would loop like eight or 13 times, but only accept four or five of those patches. And it actually did have, you know, modest, but like statistically significant improvement on long mem eval scores."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [11:47](https://www.youtube.com/watch?v=khVX_BUnEwU&t=707s)

> "what was most interesting is how much how well the agent understood experiments we've tried before that didn't work."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [13:15](https://www.youtube.com/watch?v=khVX_BUnEwU&t=795s)

> "I've done a lot of YOLO agents where you just like keep trying things and then it works, you're like, "Yeah." But then I don't know the stuff that we tried that didn't work."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [14:19](https://www.youtube.com/watch?v=khVX_BUnEwU&t=859s)

> "my hypothesis is that that's in the training data. And there's just much less training data around how to build LLM based agents."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [14:54](https://www.youtube.com/watch?v=khVX_BUnEwU&t=894s)

> "some some discussions kind of suggests that as models get better, like the harness disappears. But I'm starting to think that's not true. I think we need both"
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [15:28](https://www.youtube.com/watch?v=khVX_BUnEwU&t=928s)

> "we're not our reasoning capability, right? We are we're closer to our our our beliefs, our knowledge, and behaviors that are derived from our actual life experience."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [15:59](https://www.youtube.com/watch?v=khVX_BUnEwU&t=959s)

