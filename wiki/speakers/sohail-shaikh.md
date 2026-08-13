---
title: "Sohail Shaikh"
type: "speaker"
slug: "sohail-shaikh"
talk_count: 1
---

# Sohail Shaikh

## Talks

- [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md) (co-presented)

## Concepts

- [context engineering](../concepts/context-engineering.md)
- [context rot](../concepts/context-rot.md)
- [context window management](../concepts/context-window-management.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [latency budgets](../concepts/latency-budgets.md)
- [model routing](../concepts/model-routing.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [tool selection](../concepts/tool-selection.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "The important point is, basically, the design does not fail because one tool is badly written. It fails because every request is forced to carry the entire catalog."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [2:52](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=172s)

> "There are, say for example, uh 741 tools in your uh in your entire schema, but and it will look, basically, take up to 127,000 tokens just to have all those tool descriptions in it."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [2:52](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=172s)

> "At almost 100 tools, the accuracy drops to around 40%. Less than half of the tools that are called are the correct tools. And if it grows beyond that, like say for example, in over here, at 741 tools, the accuracy will be a mere 13.6%."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [3:57](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=237s)

> "So, in short, it's roughly one correct tool out of eight tools."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [4:51](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=291s)

> "It stays above 83% across the same catalog sizes. That is because the model is not choosing from hundreds of tools, it's choosing from a small and relevant set."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [4:51](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=291s)

> "Model pays stronger attention to the beginning and end of the long context. When hundreds of tool schemas are packed into the middle, the model does not reliably use them. So, we end up paying paying for a huge prompt, and that prompts makes the decisions even harder."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [4:51](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=291s)

> "At 100,000 requests a day, if you push this into production, you are sending in billions of tokens and just to describe those tools."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [5:40](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=340s)

> "And with just-in-time routing, the prompt may include only three to five relevant schemas, closer to about 1,000 tokens."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [5:40](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=340s)

> "That is roughly a 99% reduction in tool context tokens."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [6:38](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=398s)

> "So, say for example, if you have 500 tools in your agent, the fat agent path can push first token latency past 5 seconds."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [6:38](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=398s)

> "If you have fewer than 20 tools, a router may be unnecessary. Just load the tools directly. But, once you passed 50 tools in the production system, then justifying router-based schema make more sense."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [8:26](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=506s)

> "The difference is that we will retrieve tools instead of the documents."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [9:29](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=569s)

> "I mean, this is not a new software idea. We have used lazy loading, just-in-time compilation, and on-demand resource loading from years. We are just applying the simple and same principle to the LLM context."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [11:13](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=673s)

> "Their report token usage went from 150k tokens down to 2,000, which is 98.7% token reduction."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [12:13](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=733s)

> "In practice, K equals 5 is a strong default starting point."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [13:27](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=807s)

> "This is the core lesson from the benchmark. The catalog can grow, but the model's working set should stay small."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [15:32](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=932s)

> "This is an underrated benefit. But, the router does not only add the right tool, it also removes the wrong tool from the model's choice set."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [19:13](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1153s)

> "Run your test set at K equals to three, five, and 10, and then pick the smallest K that meets your accuracy target."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [21:19](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1279s)

> "This is not the 6-month platform rewrite. For most team, it is a focused sprint."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [21:19](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1279s)

> "So, if you if your agent start failing as tool are added, it doesn't automatically means your prompt are bad. It may means the architecture is asking the model to solve the wrong problem."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [22:40](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1360s)

> "If your descriptions are weak, embeddings will end up being weak. Write descriptions in the words users actually use and include intent, action, and key entities along with it."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [24:44](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1484s)

> "And the goal is not to make these agents more complicated. It's It is basically to stop forcing the model to reason over irrelevant tools."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [26:34](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1594s)

