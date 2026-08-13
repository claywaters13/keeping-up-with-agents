---
title: "Raahul Singh"
type: "speaker"
slug: "raahul-singh"
talk_count: 1
---

# Raahul Singh

## Talks

- [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md) (co-presented)

## Concepts

- [agentic retrieval](../concepts/agentic-retrieval.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [entity resolution](../concepts/entity-resolution.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [long-context processing](../concepts/long-context-processing.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [structured output contracts](../concepts/structured-output-contracts.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "Like we say, a product is something that works for all scenarios and does not fail silently. A demo just has to work for one."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [1:28](https://www.youtube.com/watch?v=EUsPvBeIx70&t=88s)

> "The industry has not really figured out a common naming pattern yet and every single customer can have their own things"
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [0:44](https://www.youtube.com/watch?v=EUsPvBeIx70&t=44s)

> "the problem is often times the names are so similar that semantic search just fails"
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [2:15](https://www.youtube.com/watch?v=EUsPvBeIx70&t=135s)

> "The problem is you get horrible recall and hallucinations. You will see LLMs invent phantom equipment that do not exist, and also silently drop things that do exist."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [3:36](https://www.youtube.com/watch?v=EUsPvBeIx70&t=216s)

> "We have to find something that grows sub-linearly with increasing equipment count. And this is what we figured out. So, we should not grow with instances, we should grow with tree depth."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [4:22](https://www.youtube.com/watch?v=EUsPvBeIx70&t=262s)

> "The depth of the tree grows very slowly, the width grows extremely fast. In other words, you will have a hierarchy that only adds new equipments very rarely, but it adds a lot of them when it does."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [4:57](https://www.youtube.com/watch?v=EUsPvBeIx70&t=297s)

> "because you want to go from the root to the leaf, all you have to do is describe all the paths and that's a very small finite list"
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [5:39](https://www.youtube.com/watch?v=EUsPvBeIx70&t=339s)

> "The second insight that we had was LLMs are good for planning but not good for searching."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [6:29](https://www.youtube.com/watch?v=EUsPvBeIx70&t=389s)

> "Set operations ensure that we have perfect recall and accuracy"
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [8:32](https://www.youtube.com/watch?v=EUsPvBeIx70&t=512s)

> "All of this is a two or three-step process instead of a multi-step agentic loop, which can keep on running over and over again. And this keeps our total cost also relatively flat and constant."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [10:08](https://www.youtube.com/watch?v=EUsPvBeIx70&t=608s)

> "So, we got 80% correctness at 64 GPUs, and that dropped to about 30% when the GPU grew to 400 460,000."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [10:57](https://www.youtube.com/watch?v=EUsPvBeIx70&t=657s)

> "the old approach burned 116 million tokens for just a single validation pass while still having a lot of errors"
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s)

> "the cost of the query was 9,000 tokens a query where the system was 64 GPUs or 460,000"
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s)

> "It's great at parsing ambiguous requests, judging where to look for data and what to look for, handling phrasing we've never seen from a new user that has a different query"
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [13:16](https://www.youtube.com/watch?v=EUsPvBeIx70&t=796s)

> "If your data has structure, call it a hierarchy, graph, or a schema, a language model scanning it token by token is definitely the wrong tool."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:04](https://www.youtube.com/watch?v=EUsPvBeIx70&t=844s)

> "The simple heuristic that usually works, if you can write down the structure or the rules, it's a 1.0 job. And pure LM is weakest exactly when the system is large and well structured, which is precisely where we operate and our customers."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:04](https://www.youtube.com/watch?v=EUsPvBeIx70&t=844s)

> "We started almost pure 3.0. We threw everything in the context window because that is the fastest way to find out what's even worth building."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s)

> "Legacy software drifts from 1.0 towards 3.0 and new AI native software starts at 3.0 and matures towards 1.0 for the use cases that earn it, of course."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s)

> "So every 1.0 function you add is more reliable ground for the LLM to stand on."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [15:33](https://www.youtube.com/watch?v=EUsPvBeIx70&t=933s)

