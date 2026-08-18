---
title: "James Le"
type: "speaker"
slug: "james-le"
role: "Head of Developer Experience"
company: "TwelveLabs"
talk_count: 1
---

# James Le

**Head of Developer Experience &middot; TwelveLabs**

James Le is currently leading Developer Experience at Twelve Labs, a startup building foundation models for video understanding. Previously, he worked at MLOps startups including Superb AI, Snorkel AI, Weights & Biases, and taught production ML content with Full Stack Deep Learning.

[LinkedIn](https://www.linkedin.com/in/khanhnamle94/)

## Talks

- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md) (Graphs)

## Scheduled Sessions

- **Video Has No Memory. Here's How We Built One.** &middot; Day 4 — Session Day 3 &middot; 2:25pm-2:45pm &middot; Track 5

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [citation and grounding](../concepts/citation-and-grounding.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [vision-language models](../concepts/vision-language-models.md)

## Quotes

> "But actually most of the video AI systems these days do not have memory in the system sense."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [0:01](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=1s)

> "So this is the first mental model that I want to highlight, which is that video is not a stack of frames."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [0:43](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=43s)

> "And that is a useful approximation for some tasks, but it throw away the thing that makes video very unique, which is continuity, right?"
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [1:15](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=75s)

> "So meaning in video derives from space, time, modalities, and sequence."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [1:15](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=75s)

> "If we force it into that sequence by sampling frames, by extracting a transcript, uh by dumping everything into a prompt, you lose the spatiotemporal relationships, right, that actually define the event."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [2:37](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=157s)

> "It needs to link today's scene for something that happened in another file, another episode, another camera angle, another season, another year."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [2:37](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=157s)

> "my argument is that video intelligence need a memory layer that decide what to preserve, how to connect it, and how to retrieve later."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [3:17](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=197s)

> "search is obviously super important. It's how you recover relevant moments from large video library. But then it gives candidate. It actually not give you like any continuity."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [5:55](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=355s)

> "with search, you you get like an output like a time-bounded moment, but with memory, you actually return like structured knowledge, timeline, uh explanation, composable output."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [6:30](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=390s)

> "The first is time scaling. So, a real video system should be able to reason over years of footage without reprocessing the whole archive every time, right?"
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [6:30](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=390s)

> "So a context graph is a durable, queryable representation that connects video moment, entities, appearances, relationship, time span, metadata, and corpus level context, right?"
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [7:45](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=465s)

> "Uh so the key idea here is that memory in the context of video understanding is a navigable structure over the entire video volume."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [8:53](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=533s)

> "Number one is to ingest once and reason many times."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [8:53](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=533s)

> "Um second principle is to store primitive, not just answer."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [9:32](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=572s)

> "We work across sports, uh, application, brand safety, compliance review, clear analytics. All of them require different primitives from the same video. So, the memory layer should be configurable, right?"
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [10:07](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=607s)

> "A model could produce a single answer. It is stateless. It start fresh each time, start fresh each time, and doesn't have any constraint."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [10:43](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=643s)

> "did the retrieval find the right evidence? Did the synthesis preserve it, right? Did the worker stay within the budget?"
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [12:34](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=754s)

> "So, what I did is I ingest um 67 videos from the 2022 uh World Cup in Qatar."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [13:07](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=787s)

> "So the thing we want to highlight here is it's not an application layer. It's not an editing platform, not a compliance product."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [18:55](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=1135s)

> "The product is currently in private beta right now."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [19:37](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=1177s)

