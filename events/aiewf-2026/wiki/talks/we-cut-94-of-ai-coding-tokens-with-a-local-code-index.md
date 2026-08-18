---
title: "We Cut 94% of AI Coding Tokens With a Local Code Index"
type: "talk"
slug: "we-cut-94-of-ai-coding-tokens-with-a-local-code-index"
track: "Local AI"
org: "Tesco"
day: "Day 4 — Session Day 3"
room: "Track 4"
video_id: "dRmWYHuIJxM"
duration_sec: 642
word_count: 1320
speakers: ["Rajkumar Sakthivel"]
---

# We Cut 94% of AI Coding Tokens With a Local Code Index

*Program title: Local AI Demos*

**Speakers:** [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)

**Org:** Tesco

**Track:** Local AI &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 4 &nbsp;|&nbsp; **Duration:** 10m 42s

[Watch on YouTube](https://www.youtube.com/watch?v=dRmWYHuIJxM)

## Summary

Rajkumar Sakthivel recounts how he and a collaborator traced a sudden spike in their AI coding bill not to model reasoning but to context bloat — roughly 45,000 tokens sent per query when only about 5,000 mattered. The talk's central argument is that ~90% of AI coding cost is input, so prompt tweaks, model settings, and output compression can't move the needle; the fix has to happen before the request is sent. Their answer is CCE, a free open-source local index that chunks code by function/class, runs semantic and keyword search in parallel, compresses results to signatures, tracks call graphs, and score-gates low-relevance hits — all on-device. On a FastAPI benchmark of 53 files and 20 questions, tokens per question dropped from 83K to 4.9K (94%) while still finding the right code 90% of the time. Worth watching for the cost-structure framing and for the unusually candid limits section: the 94% is measured against a worst-case full-file baseline, and recall collapsed on a 396-file mixed codebase.

## Key Points

- The cost spike came from context volume, not model usage — most tokens sent were files and code the model didn't need for the query.
- Roughly 90% of AI coding spend is input tokens and only 10% is output, so cutting output by 75% saves about 8% total while cutting input by 94% saves about 61%.
- Prompt instructions like 'only show relevant code' cannot work because the 45,000 tokens are already sent and billed before the model reads the prompt; model settings like max tokens and temperature only affect output.
- Their local search layer works in five steps: semantic chunking by function/class/method, parallel semantic plus keyword search, signature-level compression (50-line function down to 5 lines), call-graph linking, and a relevance score threshold that drops weak results.
- Hybrid search exists because each mode fails differently — semantic search misses exact names, keyword search misses synonyms like 'login flow' vs 'sign in' — and each alone misses about 1 in 4 results versus 1 in 10 combined.
- For relevance gating they rejected LLM-as-judge (2-3 seconds of added latency) and fixed thresholds (penalizes short queries) in favor of a weighted formula — 50% semantic, 30% keyword, 20% recency — that runs in 0.4 milliseconds with no extra model calls.
- Benchmarked on FastAPI (53 files, 20 developer questions), context dropped from 83K to 4.9K tokens per question, or 523 tokens with extra compression, while still locating the right code 90% of the time.
- The speaker explicitly discounts his own headline number: 94% is measured against a naive read-every-file baseline, tools like Claude Code are already smarter than that, and recall dropped to near zero on a 396-file codebase with files that each do many things.
- A shared index plus persistent memory lets Claude Code, Cursor, and Copilot reuse the same codebase understanding instead of each tool starting cold every session.
- On a real project of 247 queries, the tool reported 12.4 million tokens saved with 84% of the savings from the search layer and the remainder from compression.

## Notable Quotes

> "Most of the money was not the AI thinking. Most of it was sending too much context."
>
> — [0:01](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=1s) &middot; *The thesis of the entire talk in two sentences.*

> "We measured typical query on our project. It was sending 45,000 tokens of context, but the part of actually mattered is about 5,000 only."
>
> — [0:56](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=56s) &middot; *The core measurement the whole argument rests on.*

> "It's like ordering a pizza and paying for extra nine pizzas you don't eat every time."
>
> — [0:56](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=56s) &middot; *Memorable framing of a 9:1 waste ratio.*

> "The model already got 45,000 tokens before it read the prompt. Cost already happened."
>
> — [1:57](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=117s) &middot; *Explains precisely why prompt-level fixes are structurally incapable of saving money.*

> "This is the most important slide. 90% of your AI cost is input."
>
> — [1:57](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=117s) &middot; *The single number that reorients where optimization effort should go.*

> "if you cut input by 94%, you can save about 61% total. Same math, but different result. Fix the input. That's where your money goes."
>
> — [2:52](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=172s) &middot; *Quantifies the asymmetry between input and output optimization.*

> "By themselves, both searches miss about one in four results. Together, they miss about one in 10."
>
> — [4:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=275s) &middot; *Concrete recall numbers justifying hybrid retrieval over a single search mode.*

> "Sometimes search results returns 10 results, and none of them are right. If they use the bad results, it gives confident wrong answer."
>
> — [5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s) &middot; *Names the failure mode that motivated the score-gating design.*

> "We tried asking AI to judge its own results, too slow. Add 2-3 seconds every time."
>
> — [5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s) &middot; *A measured rejection of LLM-as-judge for inline reranking.*

> "Some simple formula, 50% meaning score, 30% keyword score, 20% how the recent code is."
>
> — [5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s) &middot; *The actual scoring weights, reusable by anyone building similar retrieval.*

> "It runs 0.4 milliseconds, no extra AI calls needed. The lesson we learned, simple formula beats the complex model most of the time."
>
> — [5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s) &middot; *States the talk's secondary thesis about heuristics versus models.*

> "Without using our tool, 83 uh K tokens per questions. With our tools, uh 4.9 K tokens per questions. That is 94% less."
>
> — [6:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=391s) &middot; *The headline benchmark result.*

> "I want to be honest about the limits. The 94% again the worst case, reading full files every time. In a real life, the tools like a cloud code already smarter than that."
>
> — [6:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=391s) &middot; *Rare on-stage caveat that the headline number uses a favorable baseline.*

> "We use full file base because it is the only one we can measure the same way every time."
>
> — [7:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=455s) &middot; *Defends the baseline choice as a reproducibility tradeoff rather than marketing.*

> "We tested on large projects with 396 files. The recall dropped almost zero. If your files each do one thing, it works well. If your files do many things, it struggles."
>
> — [7:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=455s) &middot; *Discloses the scaling failure mode and the codebase property it depends on.*

> "We use a small fast model for search. It's quick. Re-indexing takes under a second. But the bigger model would find more. We chose speed over perfection."
>
> — [7:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=455s) &middot; *Explicit statement of the embedding-model tradeoff they took.*

> "Each tool starts fresh every time. They do not share anything. You explain the same code base to three different days."
>
> — [8:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=511s) &middot; *Frames cross-tool context duplication as a distinct source of waste.*

> "247 queries. 12.4 million tokens saved. Nearly 186 not spent. Most of the savings, 84% came from search layer. The rest of them, compression."
>
> — [9:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=571s) &middot; *Attributes real-world savings between the two mechanisms.*

> "The answer was not a better model. The answer was sending less."
>
> — [9:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=571s) &middot; *The talk's closing argument, stated at its sharpest.*

> "We argue about which model is best, Opus or Sonnet. But the models may be 30% of the cost, but other 70% is what you feed it."
>
> — [9:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=571s) &middot; *A direct challenge to the field's focus on model selection over context engineering.*

## Positions

- About 90% of AI coding tool cost is input tokens and only 10% is output. ([1:57](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=117s), confidence: stated)
- Optimizing output — shorter answers, max token and temperature settings — cannot meaningfully reduce AI coding spend because the cost is on the input side. ([1:57](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=117s), confidence: stated)
- Prompt instructions to send less context are structurally useless, because the context is already transmitted and billed before the model reads the prompt. ([1:57](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=117s), confidence: stated)
- Semantic and keyword search each miss roughly 25% of relevant results alone, but only about 10% when combined. ([4:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=275s), confidence: stated)
- A weighted heuristic score (50% semantic, 30% keyword, 20% recency) with an adaptive threshold outperforms LLM-based reranking for this task, running in 0.4ms instead of adding 2-3 seconds. ([5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s), confidence: stated)
- Simple formulas beat complex models most of the time. ([5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s), confidence: stated)
- Their index cuts context from 83K to 4.9K tokens per question on FastAPI while still finding the right code 90% of the time. ([6:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=391s), confidence: stated)
- The 94% reduction figure is against a worst-case full-file-read baseline; real savings against modern agentic tools like Claude Code are lower. ([6:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=391s), confidence: stated)
- The approach degrades badly on large codebases where individual files have many responsibilities — recall dropped to nearly zero at 396 files. ([7:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=455s), confidence: stated)
- A small, fast embedding model is the right choice over a larger more accurate one, trading retrieval quality for sub-second re-indexing. ([7:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=455s), confidence: stated)
- Running the entire index and search locally, with nothing sent to the cloud, is a design advantage. ([4:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=275s), confidence: stated)
- Because AI coding tools each start from zero context, a single shared index and persistent memory across Claude Code, Cursor, and Copilot eliminates redundant re-explanation of the codebase. ([8:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=511s), confidence: stated)
- Model choice matters far less than context management, since the model is roughly 30% of cost and what you feed it is the other 70%. ([9:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=571s), confidence: stated)
- Self-reported token savings should be measured by instrumenting real queries against a counterfactual baseline, not estimated. ([9:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=571s), confidence: implied)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [code comprehension and indexing](../concepts/code-comprehension-and-indexing.md)
- [context compaction](../concepts/context-compaction.md)
- [context engineering](../concepts/context-engineering.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [local inference](../concepts/local-inference.md)
- [retrieval evaluation](../concepts/retrieval-evaluation.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)

