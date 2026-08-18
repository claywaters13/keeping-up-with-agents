---
title: "The 100-Tool Agent Is a Trap"
type: "talk"
slug: "the-100-tool-agent-is-a-trap"
org: "Prosodica"
video_id: "vh2VGuQ3zhY"
duration_sec: 1707
word_count: 3468
speakers: ["Ankush Rastogi", "Sohail Shaikh"]
---

# The 100-Tool Agent Is a Trap

**Speakers:** [Ankush Rastogi](../speakers/ankush-rastogi.md), [Sohail Shaikh](../speakers/sohail-shaikh.md)

**Org:** Prosodica

**Duration:** 28m 27s

[Watch on YouTube](https://www.youtube.com/watch?v=vh2VGuQ3zhY)

## Summary

Sohail Shaikh and Ankush Rastogi of Prosodica argue that the common practice of loading every tool definition into every agent request — the "fat agent" — is an architectural failure that gets worse as the tool catalog grows. They present benchmark numbers showing tool-selection accuracy falling from ~78% at 10 tools to ~13% at 1041 tools for the fat agent, while a semantic router holds above 83% across the same catalog sizes, and they attribute the collapse to lost-in-the-middle attention plus token and latency overhead (741 tools ≈ 127,000 tokens before the user's question is even added). Their fix is "RAG for tools": embed tool descriptions offline into a vector index, retrieve the top-K (default K=5) at runtime, and inject only those schemas — a roughly 99% reduction in tool-context tokens. The talk includes an implementation pattern, a production checklist, an eval methodology (Berkeley Function Calling Leaderboard, synthetic tool pools, K swept at 3/5/10), and honest trade-offs like router misses and weak tool descriptions. Worth watching if you're running an agent past ~50 tools; skippable if you have 10-15 tools, which the speakers explicitly say doesn't need routing.

## Key Points

- Loading the full tool catalog on every request fails not because any individual tool is badly written but because every request is forced to carry the entire catalog.
- In their benchmarks, fat-agent tool-selection accuracy started around 78% at 10 tools and fell to roughly 13.6% at 741-1041 tools, while semantic routing stayed above 83% across the same range.
- A 741-tool catalog consumes about 127,000 tokens of tool descriptions and schemas before the user's actual question is considered; at 100,000 requests/day that is billions of tokens spent just describing tools.
- Just-in-time routing typically injects only three to five schemas, around 1,000 tokens, which is roughly a 99% reduction in tool-context tokens.
- The accuracy collapse is attributed to the lost-in-the-middle problem: models attend more strongly to the beginning and end of long context, so tool schemas packed into the middle are used unreliably.
- Time to first token grows with catalog size for the fat agent — past 5 seconds at around 500 tools — while the router keeps it nearly flat because prompt size stays bounded.
- The implementation is three steps and reuses existing RAG infrastructure: index tool descriptions offline in a vector DB, embed the query and run nearest-neighbor search at runtime, then inject only the retrieved schemas and log every selection.
- The speakers explicitly bound their own advice: under 20 tools a router may be unnecessary, and routing pays off once catalog size makes prompt size, latency, or tool confusion a real production problem.
- Routing's underrated benefit is subtractive — it removes wrong tools from the model's choice set, not just adds the right ones — but it introduces new failure modes (router misses, weak or rare-tool descriptions) that need fallbacks and monitoring.

## Notable Quotes

> "The important point is, basically, the design does not fail because one tool is badly written. It fails because every request is forced to carry the entire catalog."
>
> — [2:52](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=172s) &middot; *The talk's central architectural thesis, stated in one line.*

> "There are, say for example, uh 741 tools in your uh in your entire schema, but and it will look, basically, take up to 127,000 tokens just to have all those tool descriptions in it."
>
> — [2:52](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=172s) &middot; *Anchors the cost argument with the talk's headline token number.*

> "At almost 100 tools, the accuracy drops to around 40%. Less than half of the tools that are called are the correct tools. And if it grows beyond that, like say for example, in over here, at 741 tools, the accuracy will be a mere 13.6%."
>
> — [3:57](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=237s) &middot; *The core benchmark result and the number most likely to be cited from this talk.*

> "So, in short, it's roughly one correct tool out of eight tools."
>
> — [4:51](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=291s) &middot; *Translates 13.6% into an intuition that lands.*

> "It stays above 83% across the same catalog sizes. That is because the model is not choosing from hundreds of tools, it's choosing from a small and relevant set."
>
> — [4:51](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=291s) &middot; *States the router's benchmark result and the mechanism behind it together.*

> "Model pays stronger attention to the beginning and end of the long context. When hundreds of tool schemas are packed into the middle, the model does not reliably use them. So, we end up paying paying for a huge prompt, and that prompts makes the decisions even harder."
>
> — [4:51](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=291s) &middot; *Gives the causal explanation — lost in the middle — rather than just the symptom.*

> "At 100,000 requests a day, if you push this into production, you are sending in billions of tokens and just to describe those tools."
>
> — [5:40](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=340s) &middot; *Scales the per-request cost to a production-sized number.*

> "And with just-in-time routing, the prompt may include only three to five relevant schemas, closer to about 1,000 tokens."
>
> — [5:40](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=340s) &middot; *The concrete size of the routed prompt, the basis for the 99% claim.*

> "That is roughly a 99% reduction in tool context tokens."
>
> — [6:38](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=398s) &middot; *Headline efficiency claim.*

> "So, say for example, if you have 500 tools in your agent, the fat agent path can push first token latency past 5 seconds."
>
> — [6:38](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=398s) &middot; *Puts a specific latency number on the real-time argument.*

> "If you have fewer than 20 tools, a router may be unnecessary. Just load the tools directly. But, once you passed 50 tools in the production system, then justifying router-based schema make more sense."
>
> — [8:26](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=506s) &middot; *The explicit threshold that keeps the talk from being a blanket prescription.*

> "The difference is that we will retrieve tools instead of the documents."
>
> — [9:29](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=569s) &middot; *One-sentence framing of semantic routing for anyone who already knows RAG.*

> "I mean, this is not a new software idea. We have used lazy loading, just-in-time compilation, and on-demand resource loading from years. We are just applying the simple and same principle to the LLM context."
>
> — [11:13](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=673s) &middot; *Situates JIT context injection in familiar systems practice rather than novelty.*

> "Their report token usage went from 150k tokens down to 2,000, which is 98.7% token reduction."
>
> — [12:13](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=733s) &middot; *External corroboration from Anthropic's on-demand MCP tool loading.*

> "In practice, K equals 5 is a strong default starting point."
>
> — [13:27](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=807s) &middot; *The actionable default the talk recommends after sweeping K at 3, 5, and 10.*

> "This is the core lesson from the benchmark. The catalog can grow, but the model's working set should stay small."
>
> — [15:32](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=932s) &middot; *The talk's own summary of what the numbers mean.*

> "This is an underrated benefit. But, the router does not only add the right tool, it also removes the wrong tool from the model's choice set."
>
> — [19:13](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1153s) &middot; *Names the subtractive benefit most discussions of tool retrieval miss.*

> "Run your test set at K equals to three, five, and 10, and then pick the smallest K that meets your accuracy target."
>
> — [21:19](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1279s) &middot; *Concrete tuning procedure rather than a fixed recommendation.*

> "This is not the 6-month platform rewrite. For most team, it is a focused sprint."
>
> — [21:19](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1279s) &middot; *Addresses the adoption-cost objection directly.*

> "So, if you if your agent start failing as tool are added, it doesn't automatically means your prompt are bad. It may means the architecture is asking the model to solve the wrong problem."
>
> — [22:40](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1360s) &middot; *Reframes a debugging instinct — prompt tuning — as an architecture problem.*

> "If your descriptions are weak, embeddings will end up being weak. Write descriptions in the words users actually use and include intent, action, and key entities along with it."
>
> — [24:44](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1484s) &middot; *Names the main new failure mode routing introduces and how to mitigate it.*

> "And the goal is not to make these agents more complicated. It's It is basically to stop forcing the model to reason over irrelevant tools."
>
> — [26:34](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1594s) &middot; *Closing statement of intent, guarding against over-engineering.*

## Positions

- Fat-agent tool-selection accuracy degrades from ~78% at 10 tools to ~40% at 100 tools to 13.6% at 741 tools. ([3:57](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=237s), confidence: stated)
- Semantic routing holds tool-selection accuracy above 83% across catalog sizes from 10 to 1041 tools. ([4:51](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=291s), confidence: stated)
- The fat agent's accuracy collapse is caused by the lost-in-the-middle attention problem, not by badly written individual tools. ([4:51](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=291s), confidence: stated)
- A 741-tool catalog costs about 127,000 tokens per request in tool descriptions and schemas alone. ([2:52](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=172s), confidence: stated)
- Just-in-time routing cuts tool-context tokens by roughly 99%, from ~127k to ~1,000 tokens. ([6:38](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=398s), confidence: stated)
- At around 500 tools, the fat agent path pushes time to first token past 5 seconds, while the router keeps TTFT nearly flat. ([6:38](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=398s), confidence: stated)
- Below 20 tools a router is unnecessary; static loading is fine at 10-15 tools. ([8:26](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=506s), confidence: stated)
- Beyond 50 tools in a production system, router-based schema injection is justified. ([8:26](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=506s), confidence: stated)
- K=5 is the best default number of retrieved tools, with smaller K cheaper and faster and larger K recovering more edge cases. ([13:27](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=807s), confidence: stated)
- Teams should pick the smallest K that meets their accuracy target rather than defaulting to a large K. ([21:19](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1279s), confidence: stated)
- Semantic routing requires no new infrastructure for teams that already run RAG, since it is the same retrieval pattern applied to tools. ([18:24](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1104s), confidence: stated)
- Agent failures that appear as tools are added indicate an architecture problem rather than bad prompts. ([22:40](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1360s), confidence: stated)
- Removing irrelevant tools from the model's choice set is as valuable as surfacing the right ones. ([19:13](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1153s), confidence: stated)
- The runtime overhead of routing — one embedding call and one vector search — is negligible relative to the prompt savings. ([16:30](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=990s), confidence: stated)
- Migrating an existing agent to router-based tool loading is roughly a sprint of work, not a multi-month platform rewrite. ([21:19](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1279s), confidence: stated)
- Tool description quality is the binding constraint on routing quality, so descriptions must be written in the words users actually use. ([24:44](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1484s), confidence: stated)
- The choice of embedding model and vector database is largely immaterial to whether this pattern works. ([18:24](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1104s), confidence: implied)
- Monolithic fat agents are harder to test, riskier to update, and more painful to debug than routed designs. ([7:28](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=448s), confidence: stated)

## Concepts

- [context engineering](../concepts/context-engineering.md)
- [context rot](../concepts/context-rot.md)
- [context window management](../concepts/context-window-management.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [latency budgets](../concepts/latency-budgets.md)
- [model routing](../concepts/model-routing.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [tool selection](../concepts/tool-selection.md)

