---
title: "Hanna Lichtenberg"
type: "speaker"
slug: "hanna-lichtenberg"
talk_count: 1
---

# Hanna Lichtenberg

## Talks

- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agentic retrieval](../concepts/agentic-retrieval.md)
- [benchmark design](../concepts/benchmark-design.md)
- [context window management](../concepts/context-window-management.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [retrieval evaluation](../concepts/retrieval-evaluation.md)
- [rubric design](../concepts/rubric-design.md)
- [tool selection](../concepts/tool-selection.md)

## Quotes

> "So, there's a huge gap between how basically LLMs and the reasoning is evolving and how retrieval is evolving."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [0:48](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=48s)

> "Internally, we call this gap happening right now between reasoning and search the knowledge gap. And it's not just one obscure theory of ours. We see that actually with real benchmarks and real tasks that this gap exists in real world as well."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [0:48](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=48s)

> "Oracle means what is the maximum theoretical performance of the models if you would put in the right documents with the question"
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [1:31](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=91s)

> "We see for Office for BrowseComp it's 93% and for Office QA Pro it's 64%."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s)

> "And you see there's a sharp drop in the quality of the answers Codex produces. For BrowseComp it's nine points and for Office QA Pro it's eight points."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s)

> "So we see that the models are extremely capable if they would get the right documents but if you put them into the noisy corpus the performance drops sharply. Meaning that actually the bottleneck here is not the reasoning. It's actually the access to the right knowledge it needs to answer this question."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s)

> "So for BrowseComp the difference between the Oracle and the uh GPT-5 with Mixbread is just three point and for Office QA Pro we even almost completely closed the gap."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [3:14](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=194s)

> "here's an example query we found uh during some benchmarking, which is senator woman questions billionaires not a company then okay thank you staff will check hearing."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [3:14](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=194s)

> "And the reason why the models write these type of queries is they're mostly trained for coding task, like for coding agents, which are then optimized for code base exploration using tools like grep."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [4:05](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=245s)

> "Most benchmarks we have right now, like Beer, Nano Beer, use Caveman's style queries, which are entity-based queries that structurally favor heavily BM25."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s)

> "So, right now, the agent guesses the keywords to actually increase the overlap between the query and documents and can't really use powerful search tools properly."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s)

> "Um and to work beyond code search for knowledge work. And most importantly, the agent should be precise, fast, and cheap."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s)

> "This is used as a very wide semantic search where the agent receives up to 50 retrieve chunks. Um and it sees only summaries of the chunk contents to really have just like an overview of the corpus"
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [5:43](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=343s)

> "That's why we decided to um define that it has a maximum four search rounds, but within each search round it can have parallel searches."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [6:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=385s)

> "The agent has to articulate articulate what evidence it needs before writing the query."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [8:15](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=495s)

> "We kind of trick the um model into not thinking it has to write the typical BM25 base query by just instructing it to write one concise sentence describing what it wants to find, instead of directly instructing write a search query, so it cannot fall into this old pattern."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [9:05](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=545s)

> "So, the first step in training is um supervised fine-tuning with a larger teacher LLM. And then we uh did on-policy reinforcement learning with an own search reward. Our search reward is a combination of both of a retrieval reward and a trajectory reward."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [9:59](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=599s)

> "Of course, like we have rubrics that are where the judge is deciding if the query is really a natural sentence. Also, if the amount of exploration is sufficient, is it too much or too less."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [11:42](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=702s)

> "It's really a sentence describing what it wants to find and not a weird keywordy added behind each other formulation."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [12:33](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=753s)

> "Our trained agent is not released yet, unfortunately. However, we have some intermediate results."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [12:33](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=753s)

> "we see that we achieved an NDCG of 10 at 10 of 0.4, which is a huge jump um towards the model that performed best on the paper of this benchmark, which is the GPT multi-hop agent"
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [12:33](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=753s)

> "And this agent is top one on the snowflakes match QA benchmark, achieving an accuracy of 93.4 when we give the Gemini 3.5 flash model our genetic search as search tool."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [13:24](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=804s)

