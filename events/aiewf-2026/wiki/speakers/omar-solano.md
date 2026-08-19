---
title: "Omar Solano"
type: "speaker"
slug: "omar-solano"
role: "AI Engineer"
company: "Towards AI"
talk_count: 1
---

# Omar Solano

**AI Engineer &middot; Towards AI**

Omar Solano is an AI Engineer at Towards AI, where he architects and builds production AI agents and applied LLM systems. His work spans RAG, fine-tuning, agentic workflows, and long-context and reasoning-model systems. He leads client-facing AI consulting projects and delivers hands-on AI engineering workshops for developers, engineering teams, and international conference audiences, including training for Europol and the New York Public Library. Omar has authored 50+ technical lessons and book chapters on RAG, AI agents, fine-tuning, and coding agents, reaching 90,000+ learners through Towards AI's courses and publications.

[LinkedIn](https://www.linkedin.com/in/omar-solano1)

## Talks

- [Context Engineering in 2026](../talks/context-engineering-in-2026.md) (Context Engineering, co-presented)

## Scheduled Sessions

- **Context Engineering in 2026: Compaction, Memory & Cost** &middot; Day 1 — Workshop Day &middot; 2:20pm-4:20pm &middot; Track 6

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agentic retrieval](../concepts/agentic-retrieval.md)
- [context compaction](../concepts/context-compaction.md)
- [context engineering](../concepts/context-engineering.md)
- [context rot](../concepts/context-rot.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [local inference](../concepts/local-inference.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "So ultimately it means that summarization is potentially a trap."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [16:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=1018s)

> "You need to compress by more than 50 times the context. So it can be quite difficult in some cases without losing quality."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [16:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=1018s)

> "all of this together is the is context engineering which basically means to decide what the model sees every time you call it"
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [21:05](https://www.youtube.com/watch?v=WP3hjUXd918&t=1265s)

> "we didn't actually measure anything. It was just like oh it looks good. Okay, we will just set it set it like this."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [32:32](https://www.youtube.com/watch?v=WP3hjUXd918&t=1952s)

> "not touching uh is actually cheaper, it's faster and we have better recall overall. So keeping everything wins on on all of these three fronts."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s)

> "if you remove the tool outputs consistently then the agent needs to rerieve uh afterwards for information it already had. So you're just making the agent uh do more tool calls"
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s)

> "on Deep Seek we saw um the setup that was sending the most tokens is actually the cheapest to run"
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [52:08](https://www.youtube.com/watch?v=WP3hjUXd918&t=3128s)

> "we were still getting the best results out of it because 97% of the tokens that we had were cached"
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [52:08](https://www.youtube.com/watch?v=WP3hjUXd918&t=3128s)

> "whereas if I summarize first or if I compact um the context I had it only gave me the answer back 32% of the time."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [51:05](https://www.youtube.com/watch?v=WP3hjUXd918&t=3065s)

> "So we can see that up until 800k tokens as well the model was not missing out on those facts."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [53:53](https://www.youtube.com/watch?v=WP3hjUXd918&t=3233s)

> "when we increased it to like 400k tokens it was not able to facts that were buried in the middle and it started giving us like 0% recall whereas uh you know something like BM25 it still got 100% every time."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [58:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=3538s)

> "once the conversation doesn't fit in the window um caching was no longer helpful for us and we uh you know we have to make um the context smaller"
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [55:33](https://www.youtube.com/watch?v=WP3hjUXd918&t=3333s)

> "if we have like thousand students uh you know Gemini costs us about like $40,000 40,000 a month whereas Deep Seek Deep Seek was around 1,900 a month"
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [1:00:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=3631s)

> "So the main thing to take away is that um do not compact by default. You have to name the constraint that you have and then you know look for a better alternative."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [1:01:37](https://www.youtube.com/watch?v=WP3hjUXd918&t=3697s)

> "So just using the first tool was enough to get all the relevant information and just having this second tool was just 50% slower."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [30:51](https://www.youtube.com/watch?v=WP3hjUXd918&t=1851s)

> "we compared graph rag with with rag here and it's in our case it just ended up being way costlier to set up and just tie on the results"
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [12:41](https://www.youtube.com/watch?v=WP3hjUXd918&t=761s)

> "the main problem is not is not that it's more costly. It's also that the quality degrades"
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [7:40](https://www.youtube.com/watch?v=WP3hjUXd918&t=460s)

> "right now everyone is is converging towards having more and smaller skills"
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [14:52](https://www.youtube.com/watch?v=WP3hjUXd918&t=892s)

> "right now I think the best way to do it is to just use use your uh code code subscription or your codec subscription because it's cheaper than using the APIs."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [39:09](https://www.youtube.com/watch?v=WP3hjUXd918&t=2349s)

> "I I didn't expect this to to get over $500, but it did."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [43:11](https://www.youtube.com/watch?v=WP3hjUXd918&t=2591s)

