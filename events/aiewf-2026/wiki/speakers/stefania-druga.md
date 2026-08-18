---
title: "Stefania Druga"
type: "speaker"
slug: "stefania-druga"
role: "Research Scientist"
company: "Sakana.ai"
talk_count: 1
---

# Stefania Druga

**Research Scientist &middot; Sakana.ai**

Hi! I am Stef. I am currently a Research Scientist at Sakana AI in Tokyo, Japan working on novel architectures beyond the transformer. Previously I was a research at Google Deep Mind working on novel multimodal AI applications. I graduated with a Ph.D. in Creative AI Literacies at the University of Washington Information School.

[LinkedIn](https://www.linkedin.com/in/drugastefania/)

## Talks

- [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md) (Memory & Continual Learning)

## Scheduled Sessions

- **Memory Harnesses for Long-Running Research Agents** &middot; Day 3 — Session Day 2 &middot; 11:40am-12:00pm &middot; Main Stage

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [audit trails](../concepts/audit-trails.md)
- [benchmark design](../concepts/benchmark-design.md)
- [context rot](../concepts/context-rot.md)
- [local inference](../concepts/local-inference.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [sovereign and air-gapped deployment](../concepts/sovereign-and-air-gapped-deployment.md)

## Quotes

> "if you work with long horizon tasks, you probably run into this issue of context blow. Right? Like when the model starts contradicting itself, or it has to redo the work because it forgot it did that task in the first place, or it starts to drift from your questions because it forgot them."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [0:01](https://www.youtube.com/watch?v=R3-anFK1YM8&t=1s)

> "we see that the trend is to solve longer and longer uh horizon tasks, and also that we're getting fewer and fewer model releases. So, at some point later this year, we're going to have this convergence"
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [1:01](https://www.youtube.com/watch?v=R3-anFK1YM8&t=61s)

> "the CEO of Coinbase actually shared how their company managed to reduce their AI spent while actually increasing uh the AI usage."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [1:01](https://www.youtube.com/watch?v=R3-anFK1YM8&t=61s)

> "the way they did that was by transitioning to use many more local models, but also having better practices, like using better routing, better caching, keeping the context clean"
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [1:56](https://www.youtube.com/watch?v=R3-anFK1YM8&t=116s)

> "these local models are starting to be useful for agentic tasks and for tool use."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [1:56](https://www.youtube.com/watch?v=R3-anFK1YM8&t=116s)

> "on this M3 Ultra with 96 GB and 28 core CPUs, I'm using two models. I'm using the Qwen 27B quantized at 4-bit and the Deep Seek V4 Flash."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [2:42](https://www.youtube.com/watch?v=R3-anFK1YM8&t=162s)

> "you can think of memory as a write-manage-read loop. So, it's not just a database store. It's actually this control loop around the model."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [3:25](https://www.youtube.com/watch?v=R3-anFK1YM8&t=205s)

> "I started with research agents that are the small agents because they have zero durable memory, and I wanted all the memory to come from the harness."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [3:25](https://www.youtube.com/watch?v=R3-anFK1YM8&t=205s)

> "the memory actually didn't add more capability. It was the same performance with memory and without memory, and it only added more cost. So, when your task fits in context, the harness doesn't add much."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [5:43](https://www.youtube.com/watch?v=R3-anFK1YM8&t=343s)

> "if I start to run tasks that are longer term horizon, and the entire task and the relevant context doesn't uh fit, then having a good memory harness really starts to pay off."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [6:36](https://www.youtube.com/watch?v=R3-anFK1YM8&t=396s)

> "the right answer is in a like step 124, but the moment when I ask the question, I'm asking it like at step 500. So, it's completely outside of the context window"
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [6:36](https://www.youtube.com/watch?v=R3-anFK1YM8&t=396s)

> "I ran over 68 questions and for each of these questions there were like multiple cells and lots of different seeds. And what I found was that the rank only ledger performed the best."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [7:31](https://www.youtube.com/watch?v=R3-anFK1YM8&t=451s)

> "it performed better than like just gating the harness by saying do you need to use memory or do you not need to use memory."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [7:31](https://www.youtube.com/watch?v=R3-anFK1YM8&t=451s)

> "The Oracle what it does, it provides the right information, the right memory to the model but it doesn't force it to use it. So the model can get the right memory but still retrieve the wrong information or choose to ignore it or be confused."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s)

> "this actually works on several models, not only on the Qwen 27B but also on the DS4 flash and it also works across different benchmarks. I also tried it on the Spider V2 benchmark."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [9:10](https://www.youtube.com/watch?v=R3-anFK1YM8&t=550s)

> "bad memory is expensive because it spends more token and it can send the agent the wrong way. But having like a good structural policy for recall can save you a lot of tokens and uh budget."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [9:10](https://www.youtube.com/watch?v=R3-anFK1YM8&t=550s)

> "one thing that I want to encourage you from this experiment is to consider the recall policy as a first-class metric"
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [10:01](https://www.youtube.com/watch?v=R3-anFK1YM8&t=601s)

> "going from simple file system retrieval to training memory models um there's there's a wide spectrum of solutions from less structural to completely structured."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [10:54](https://www.youtube.com/watch?v=R3-anFK1YM8&t=654s)

> "these local models I can only what run them in serial, like they don't support batch querying for the deep seed 4 flash. So, that's why I am still running evaluations back on my computer in Tokyo"
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [11:48](https://www.youtube.com/watch?v=R3-anFK1YM8&t=708s)

> "it's a very good test for what memory can do when you can control every single step of the pipeline. And this sovereign capability is part of a bigger ecosystem that is very important for us at Sakana AI in Japan."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [11:48](https://www.youtube.com/watch?v=R3-anFK1YM8&t=708s)

