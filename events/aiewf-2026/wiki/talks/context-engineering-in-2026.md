---
title: "Context Engineering in 2026"
type: "talk"
slug: "context-engineering-in-2026"
track: "Context Engineering"
org: "Omar Solano & Samridhi Vaid, Towards AI"
day: "Day 1 — Workshop Day"
room: "Track 6"
video_id: "WP3hjUXd918"
duration_sec: 3806
word_count: 10435
speakers: ["Louis-François Bouchard", "Omar Solano", "Samridhi Vaid"]
---

# Context Engineering in 2026

*Program title: Context Engineering in 2026: Compaction, Memory & Cost*

**Speakers:** [Louis-François Bouchard](../speakers/louis-francois-bouchard.md), [Omar Solano](../speakers/omar-solano.md), [Samridhi Vaid](../speakers/samridhi-vaid.md)

**Org:** Omar Solano & Samridhi Vaid, Towards AI

**Track:** Context Engineering &nbsp;|&nbsp; **Day/Room:** Day 1 — Workshop Day &middot; Track 6 &nbsp;|&nbsp; **Duration:** 1h 3m

[Watch on YouTube](https://www.youtube.com/watch?v=WP3hjUXd918)

## Summary

Three speakers from Towards AI report on a large battery of experiments run against their production AI tutor to answer one question: does context compaction actually help? Louis-François Bouchard first surveys the 2026 toolkit — truncation, sliding windows, selective retention, summarization, offloading to files/wikis, RAG — then argues that prompt caching has changed the economics so much that summarization is often a trap, since any transformation of the context invalidates the cache and you must compress ~50x to break even. Omar Solano shows the eval harness and the headline result: across 11 presets, doing nothing to the context beat their own hand-tuned production defaults on recall, cost, and latency simultaneously, because clearing tool outputs just forces the agent to re-retrieve. Samridhi Vaid extends this to cheaper models, longer contexts, and local deployment, finding keeping-everything holds up to 800k tokens and 95% detail recall on DeepSeek, but collapses locally where a 32K window kills caching and retrieval becomes mandatory. Worth watching if you are building an agent harness and want empirical numbers rather than folklore about when to compact.

## Key Points

- Prompt caching inverts the usual cost intuition: because cached tokens can be up to 50x cheaper, the run that sent the most tokens (full history, 97% cached) was the cheapest to operate, while summarization forces fresh reads and writes every turn.
- For compaction to be economically worthwhile against a cached context, you need to compress by more than 50x, which is very hard to do without losing quality — so summarization is often a net loss.
- Their hand-tuned production defaults (clear tool outputs after 5,000 tokens keeping the last five, summarize after 30,000 tokens keeping the last 20 messages) were never measured before deployment and lost to simply keeping the full history on recall, cost, and latency.
- Clearing old tool outputs backfires because the agent then re-retrieves information it already had, adding tool calls that raise both cost and time to first token.
- Multi-turn quality is where techniques separate: in single-turn tasks nearly every preset scored well because there weren't enough tokens to trigger the strategies at all, while production quality dropped to 38% on multi-turn.
- Adding a second tool that let the agent browse the knowledge base with sandboxed bash commands produced identical recall to the existing hybrid-search retriever while running 50% slower, so it was cut.
- Long-context recall held up far better than 'context rot' folklore suggests — distinctive facts were still found at 800k tokens, though recall on ambiguous facts halved.
- Local deployment flips the conclusion entirely: with a 32K MacBook context window, caching stops helping, chat recall falls from 92–95% to 33%, and retrieval becomes the only viable strategy.
- Dense semantic search alone degrades badly at scale — 0% recall on facts buried in the middle at 400k tokens — while BM25 held 100%, which is why they run hybrid search.
- Graph RAG was tested and rejected: costlier to set up and statistically tied with plain RAG on their real-user evaluations.

## Notable Quotes

> "So ultimately it means that summarization is potentially a trap."
>
> — [16:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=1018s) &middot; *the talk's central contrarian thesis, stated in one line*

> "You need to compress by more than 50 times the context. So it can be quite difficult in some cases without losing quality."
>
> — [16:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=1018s) &middot; *quantifies the break-even point that makes compaction uneconomic under caching*

> "all of this together is the is context engineering which basically means to decide what the model sees every time you call it"
>
> — [21:05](https://www.youtube.com/watch?v=WP3hjUXd918&t=1265s) &middot; *the working definition of context engineering the whole talk operates under*

> "we didn't actually measure anything. It was just like oh it looks good. Okay, we will just set it set it like this."
>
> — [32:32](https://www.youtube.com/watch?v=WP3hjUXd918&t=1952s) &middot; *candid admission that their shipped production defaults were unvalidated folklore*

> "not touching uh is actually cheaper, it's faster and we have better recall overall. So keeping everything wins on on all of these three fronts."
>
> — [45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s) &middot; *the headline experimental result, sweeping all three metrics*

> "if you remove the tool outputs consistently then the agent needs to rerieve uh afterwards for information it already had. So you're just making the agent uh do more tool calls"
>
> — [45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s) &middot; *the causal mechanism explaining why aggressive clearing costs more, not less*

> "on Deep Seek we saw um the setup that was sending the most tokens is actually the cheapest to run"
>
> — [52:08](https://www.youtube.com/watch?v=WP3hjUXd918&t=3128s) &middot; *the counterintuitive cost inversion that caching creates*

> "we were still getting the best results out of it because 97% of the tokens that we had were cached"
>
> — [52:08](https://www.youtube.com/watch?v=WP3hjUXd918&t=3128s) &middot; *the cache-hit number that makes the full-history strategy affordable*

> "whereas if I summarize first or if I compact um the context I had it only gave me the answer back 32% of the time."
>
> — [51:05](https://www.youtube.com/watch?v=WP3hjUXd918&t=3065s) &middot; *direct quality cost of compaction against the 95% full-history baseline*

> "So we can see that up until 800k tokens as well the model was not missing out on those facts."
>
> — [53:53](https://www.youtube.com/watch?v=WP3hjUXd918&t=3233s) &middot; *empirical pushback on the assumption that long contexts inevitably rot*

> "when we increased it to like 400k tokens it was not able to facts that were buried in the middle and it started giving us like 0% recall whereas uh you know something like BM25 it still got 100% every time."
>
> — [58:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=3538s) &middot; *concrete failure mode of dense-only retrieval at scale, with the lexical baseline beating it outright*

> "once the conversation doesn't fit in the window um caching was no longer helpful for us and we uh you know we have to make um the context smaller"
>
> — [55:33](https://www.youtube.com/watch?v=WP3hjUXd918&t=3333s) &middot; *names the exact constraint under which compaction becomes necessary again*

> "if we have like thousand students uh you know Gemini costs us about like $40,000 40,000 a month whereas Deep Seek Deep Seek was around 1,900 a month"
>
> — [1:00:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=3631s) &middot; *a ~20x model-choice cost delta at their projected scale*

> "So the main thing to take away is that um do not compact by default. You have to name the constraint that you have and then you know look for a better alternative."
>
> — [1:01:37](https://www.youtube.com/watch?v=WP3hjUXd918&t=3697s) &middot; *the talk's closing prescription, framed as constraint-first rather than technique-first*

> "So just using the first tool was enough to get all the relevant information and just having this second tool was just 50% slower."
>
> — [30:51](https://www.youtube.com/watch?v=WP3hjUXd918&t=1851s) &middot; *measured rejection of agentic filesystem browsing for their workload*

> "we compared graph rag with with rag here and it's in our case it just ended up being way costlier to set up and just tie on the results"
>
> — [12:41](https://www.youtube.com/watch?v=WP3hjUXd918&t=761s) &middot; *rare public negative result on graph RAG from a real deployment*

> "the main problem is not is not that it's more costly. It's also that the quality degrades"
>
> — [7:40](https://www.youtube.com/watch?v=WP3hjUXd918&t=460s) &middot; *frames context bloat as a quality problem before a billing problem*

> "right now everyone is is converging towards having more and smaller skills"
>
> — [14:52](https://www.youtube.com/watch?v=WP3hjUXd918&t=892s) &middot; *a field-level trend claim on skill granularity and progressive disclosure*

> "right now I think the best way to do it is to just use use your uh code code subscription or your codec subscription because it's cheaper than using the APIs."
>
> — [39:09](https://www.youtube.com/watch?v=WP3hjUXd918&t=2349s) &middot; *practical, slightly subversive advice on cutting LLM-as-judge eval costs*

> "I I didn't expect this to to get over $500, but it did."
>
> — [43:11](https://www.youtube.com/watch?v=WP3hjUXd918&t=2591s) &middot; *grounds the real price of running a serious context-strategy eval sweep*

## Positions

- Summarization is usually a trap because it invalidates the provider's prompt cache, so you must compress by more than 50x for it to pay off. ([16:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=1018s), confidence: stated)
- Keeping the full conversation history untouched beat every compaction preset simultaneously on memory recall, cost, and latency in their experiments. ([45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s), confidence: stated)
- Aggressively clearing old tool outputs increases total cost because the agent re-retrieves information it already had. ([45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s), confidence: stated)
- Agents should not compact by default; compaction is only justified once a named constraint (such as a context window too small for caching to apply) forces it. ([1:01:37](https://www.youtube.com/watch?v=WP3hjUXd918&t=3697s), confidence: stated)
- Graph RAG was more expensive to set up and tied with plain RAG on their real-user evaluations, so it is not worth adopting unless your data is highly interconnected. ([12:41](https://www.youtube.com/watch?v=WP3hjUXd918&t=761s), confidence: stated)
- Letting the agent browse the knowledge base with bash commands added no recall over hybrid search and made responses 50% slower. ([30:51](https://www.youtube.com/watch?v=WP3hjUXd918&t=1851s), confidence: stated)
- Long context does not necessarily rot: distinctive facts were recalled reliably up to 800k tokens without any compaction. ([53:53](https://www.youtube.com/watch?v=WP3hjUXd918&t=3233s), confidence: stated)
- Dense semantic search alone is insufficient at large context sizes; BM25 keyword search retained 100% recall where dense retrieval dropped to 0%. ([58:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=3538s), confidence: stated)
- Single-turn benchmarks cannot distinguish context management strategies because they never accumulate enough tokens to trigger compaction at all. ([44:47](https://www.youtube.com/watch?v=WP3hjUXd918&t=2687s), confidence: stated)
- Running local models is not a drop-in substitute for cloud for chat memory: a 32K window cut chat recall from 92–95% to 33%, and increasing model parameter count does not expand the context window. ([59:45](https://www.youtube.com/watch?v=WP3hjUXd918&t=3585s), confidence: stated)
- Using a coding-agent subscription for LLM-as-judge grading is cheaper than paying per-token API prices. ([39:09](https://www.youtube.com/watch?v=WP3hjUXd918&t=2349s), confidence: stated)
- Many small, cross-referencing skills loaded on demand are better than large monolithic ones, because progressive disclosure conserves context. ([14:52](https://www.youtube.com/watch?v=WP3hjUXd918&t=892s), confidence: stated)
- Sub-agents add complexity without benefit for a single-purpose tutor agent, so they were deliberately not used. ([11:50](https://www.youtube.com/watch?v=WP3hjUXd918&t=710s), confidence: stated)
- Comprehensive per-turn logging (tokens, cache hits, cost, TTFT, tool calls, user frustration) is cheap to implement and most teams skip it. ([20:15](https://www.youtube.com/watch?v=WP3hjUXd918&t=1215s), confidence: stated)

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

