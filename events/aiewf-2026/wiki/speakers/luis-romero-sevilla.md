---
title: "Luis Romero-Sevilla"
type: "speaker"
slug: "luis-romero-sevilla"
talk_count: 1
---

# Luis Romero-Sevilla

## Talks

- [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

## Concepts

- [context rot](../concepts/context-rot.md)
- [context window management](../concepts/context-window-management.md)
- [graph rag](../concepts/graph-rag.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [retrieval evaluation](../concepts/retrieval-evaluation.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)

## Quotes

> "I'm on a mission to solve knowledge representation when all context matters."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [0:03](https://www.youtube.com/watch?v=XovaGv4f39A&t=3s)

> "Inserting to a vector database, it's relatively fast. So, whenever a collection becomes obsolete, we can just replace it with a new one."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [0:51](https://www.youtube.com/watch?v=XovaGv4f39A&t=51s)

> "All the documents in the collection are relevant for us to answer the question. So, we can't just take all the documents in the collection and pass them to LLM."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [1:33](https://www.youtube.com/watch?v=XovaGv4f39A&t=93s)

> "If your collection of documents isn't changed very often, GraphRAG is an excellent approach for finding those relationships within details to answer the user's question."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [2:24](https://www.youtube.com/watch?v=XovaGv4f39A&t=144s)

> "Recomputing a knowledge graph every time the data gets replaced is computationally very expensive, and it takes relatively long time."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [2:24](https://www.youtube.com/watch?v=XovaGv4f39A&t=144s)

> "where we use a model with a large context window, load the documents into the context, and cache the context by storing the model's KB matrix"
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:12](https://www.youtube.com/watch?v=XovaGv4f39A&t=192s)

> "The problem here is that the context window is limited, and if you fill the context window too much, the quality of the answer gets degraded, too."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:12](https://www.youtube.com/watch?v=XovaGv4f39A&t=192s)

> "The solution: what if we use more CAGs in parallel and distribute the documents across different context buckets."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:12](https://www.youtube.com/watch?v=XovaGv4f39A&t=192s)

> "Now, each cache can answer questions regarding its content. And now we just need something to ask the right questions to the right buckets."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:50](https://www.youtube.com/watch?v=XovaGv4f39A&t=230s)

> "But in practice, with very dense relationship between documents, the supervisor tends to ignore domains that at first glance seem irrelevant."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:50](https://www.youtube.com/watch?v=XovaGv4f39A&t=230s)

> "For this reason, all documents are distributed in no particular order. The only requirement is to balance the number of documents in a way that the least amount of documents are needed."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:50](https://www.youtube.com/watch?v=XovaGv4f39A&t=230s)

> "Then the supervisor model start exploring the buckets and progressively builds its internal understanding. And if it finds something interesting, it can ask a specific bucket follow-up questions."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [4:37](https://www.youtube.com/watch?v=XovaGv4f39A&t=277s)

> "Because all caches can be loaded in parallel, the knowledge building process is significantly faster than graph rag while providing more accurate answers than a simple rag."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [4:37](https://www.youtube.com/watch?v=XovaGv4f39A&t=277s)

> "And you're probably thinking, "KV cache can be pretty expensive." And you're absolutely right. But there are ways to reduce that cost by optimizing how long each cache lives."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [4:37](https://www.youtube.com/watch?v=XovaGv4f39A&t=277s)

> "And at the end, there are many retrieval strategies, and all of them have their trade-offs, whether it's compute, cost, speed. Currently, there is no one-solution-fits-all."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [4:37](https://www.youtube.com/watch?v=XovaGv4f39A&t=277s)

