---
title: "How we taught agents to use good retrieval"
type: "talk"
slug: "how-we-taught-agents-to-use-good-retrieval"
org: "Mixedbread AI"
video_id: "1IdzkRVmWAA"
duration_sec: 868
word_count: 2057
speakers: ["Hanna Lichtenberg"]
---

# How we taught agents to use good retrieval

**Speakers:** [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)

**Org:** Mixedbread AI

**Duration:** 14m 28s

[Watch on YouTube](https://www.youtube.com/watch?v=1IdzkRVmWAA)

## Summary

Hanna Lichtenberg and co-founder Amir of Mixedbread AI argue that LLM reasoning has improved exponentially while retrieval has crawled, creating what they call a 'knowledge gap' — the bottleneck in agentic knowledge work is access to the right documents, not the model's ability to reason over them. They quantify this with an Oracle baseline on BrowseComp Plus and Office QA Pro: given the right documents, models score 93% and 64%, but Codex with default tools drops to single-digit scores, while swapping in Mixedbread's late-interaction search recovers nearly all of it. They then diagnose why agents write bad queries — coding/grep training, human-mimicking web search habits, and BM25-friendly benchmarks like BEIR — and walk through the harness and training recipe for a small search agent designed to fix it. The harness gives four differentiated tools (overview search, semantic search, metadata filtering, grep), caps exploration at four parallel-capable rounds, and prompts the model to write 'one concise sentence' rather than a 'search query' to break the keyword habit. Training is SFT from a larger teacher plus on-policy RL against a combined retrieval reward (NDCG plus LLM rubric judging) and trajectory reward. Worth watching if you build RAG or agentic search and want a concrete harness-plus-RL recipe with numbers, though the trained agent isn't released yet.

## Key Points

- The gap between LLM reasoning quality and retrieval quality — Mixedbread's 'knowledge gap' — means the bottleneck in complex knowledge tasks is document access, not model reasoning.
- Oracle performance (the model given the correct documents) is 93% on BrowseComp Plus and 64% on Office QA Pro, while Codex with its default tools scores nine and eight points respectively on the same benchmarks.
- Substituting a late-interaction search tool closes most of that gap: three points off Oracle on BrowseComp Plus and near-parity on Office QA Pro.
- Agents write gibberish keyword-stuffed queries for three reasons: they are trained on grep-driven code exploration, they mimic human query patterns for web tools, and retrieval benchmarks like BEIR reward BM25-friendly 'caveman style' entity queries.
- The harness exposes four differentiated tools — overview search (up to 50 summarized chunks), semantic search (full payload, top 10), metadata facet filtering, and grep — so the agent must choose a tool that matches the search intent.
- The agent loop is deliberately short for speed: at most four search rounds, but each round permits parallel searches, and results are deduplicated so the context isn't filled with repeated chunks.
- The agent is seeded with results from an initial semantic search plus available metadata facet hints, so it can plan against a preview of the corpus rather than guessing blind.
- Prompt framing matters: asking for 'one concise sentence describing what it wants to find' rather than a 'search query' prevents the model from reverting to BM25-style keyword output.
- Training combined supervised fine-tuning from a larger teacher with on-policy RL against a retrieval reward (NDCG plus LLM rubric judging of relevance and ranking plausibility) and a trajectory reward judging query naturalness and exploration budget.
- Reported results: NDCG@10 of 0.4 on the Oblique Congress benchmark versus 0.18 for the paper's best GPT multi-hop agent, and a production beta agent ranking top-one on Snowflake's MatchQA at 93.4% accuracy with Gemini 3.5 Flash.

## Notable Quotes

> "So, there's a huge gap between how basically LLMs and the reasoning is evolving and how retrieval is evolving."
>
> — [0:48](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=48s) &middot; *The thesis of the talk stated in one line.*

> "Internally, we call this gap happening right now between reasoning and search the knowledge gap. And it's not just one obscure theory of ours. We see that actually with real benchmarks and real tasks that this gap exists in real world as well."
>
> — [0:48](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=48s) &middot; *Names the central concept and stakes the empirical claim behind it.*

> "Oracle means what is the maximum theoretical performance of the models if you would put in the right documents with the question"
>
> — [1:31](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=91s) &middot; *Defines the measurement device the entire argument rests on.*

> "We see for Office for BrowseComp it's 93% and for Office QA Pro it's 64%."
>
> — [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s) &middot; *The Oracle ceiling numbers.*

> "And you see there's a sharp drop in the quality of the answers Codex produces. For BrowseComp it's nine points and for Office QA Pro it's eight points."
>
> — [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s) &middot; *The headline gap: near-total collapse from Oracle to default agent tooling.*

> "So we see that the models are extremely capable if they would get the right documents but if you put them into the noisy corpus the performance drops sharply. Meaning that actually the bottleneck here is not the reasoning. It's actually the access to the right knowledge it needs to answer this question."
>
> — [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s) &middot; *The load-bearing position — reasoning is not the constraint.*

> "So for BrowseComp the difference between the Oracle and the uh GPT-5 with Mixbread is just three point and for Office QA Pro we even almost completely closed the gap."
>
> — [3:14](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=194s) &middot; *Quantifies how much of the gap is recoverable by retrieval alone.*

> "here's an example query we found uh during some benchmarking, which is senator woman questions billionaires not a company then okay thank you staff will check hearing."
>
> — [3:14](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=194s) &middot; *Concrete artifact of the failure mode, more persuasive than the abstraction.*

> "And the reason why the models write these type of queries is they're mostly trained for coding task, like for coding agents, which are then optimized for code base exploration using tools like grep."
>
> — [4:05](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=245s) &middot; *Causal explanation blaming coding-agent training for bad retrieval behavior.*

> "Most benchmarks we have right now, like Beer, Nano Beer, use Caveman's style queries, which are entity-based queries that structurally favor heavily BM25."
>
> — [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s) &middot; *A direct criticism of standard retrieval benchmarks others rely on.*

> "So, right now, the agent guesses the keywords to actually increase the overlap between the query and documents and can't really use powerful search tools properly."
>
> — [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s) &middot; *Summarizes the behavioral diagnosis the rest of the talk fixes.*

> "Um and to work beyond code search for knowledge work. And most importantly, the agent should be precise, fast, and cheap."
>
> — [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s) &middot; *States the design objectives that justify the small-model choice.*

> "This is used as a very wide semantic search where the agent receives up to 50 retrieve chunks. Um and it sees only summaries of the chunk contents to really have just like an overview of the corpus"
>
> — [5:43](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=343s) &middot; *Specific context-budget tradeoff in tool design.*

> "That's why we decided to um define that it has a maximum four search rounds, but within each search round it can have parallel searches."
>
> — [6:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=385s) &middot; *The concrete latency-versus-exploration tradeoff in the agent loop.*

> "The agent has to articulate articulate what evidence it needs before writing the query."
>
> — [8:15](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=495s) &middot; *Goal framing as a prompt-level mechanism for better queries.*

> "We kind of trick the um model into not thinking it has to write the typical BM25 base query by just instructing it to write one concise sentence describing what it wants to find, instead of directly instructing write a search query, so it cannot fall into this old pattern."
>
> — [9:05](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=545s) &middot; *The single most transferable prompt trick in the talk.*

> "So, the first step in training is um supervised fine-tuning with a larger teacher LLM. And then we uh did on-policy reinforcement learning with an own search reward. Our search reward is a combination of both of a retrieval reward and a trajectory reward."
>
> — [9:59](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=599s) &middot; *The training recipe in compact form.*

> "Of course, like we have rubrics that are where the judge is deciding if the query is really a natural sentence. Also, if the amount of exploration is sufficient, is it too much or too less."
>
> — [11:42](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=702s) &middot; *Shows query style and exploration budget being directly rewarded, not just outcomes.*

> "It's really a sentence describing what it wants to find and not a weird keywordy added behind each other formulation."
>
> — [12:33](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=753s) &middot; *The observable behavior change the whole pipeline was built to produce.*

> "Our trained agent is not released yet, unfortunately. However, we have some intermediate results."
>
> — [12:33](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=753s) &middot; *Important caveat for anyone weighing whether they can use this.*

> "we see that we achieved an NDCG of 10 at 10 of 0.4, which is a huge jump um towards the model that performed best on the paper of this benchmark, which is the GPT multi-hop agent"
>
> — [12:33](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=753s) &middot; *The headline retrieval-quality result versus a named baseline.*

> "And this agent is top one on the snowflakes match QA benchmark, achieving an accuracy of 93.4 when we give the Gemini 3.5 flash model our genetic search as search tool."
>
> — [13:24](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=804s) &middot; *The production result on a public leaderboard, with the model pairing named.*

## Positions

- The bottleneck in complex knowledge tasks is retrieval quality, not model reasoning capability. ([2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s), confidence: stated)
- LLM reasoning has improved exponentially over recent years while search has improved only very slowly over the past 20 years. ([0:00](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=0s), confidence: stated)
- Oracle performance is 93% on BrowseComp Plus and 64% on Office QA Pro, while Codex with default tools scores nine and eight points respectively. ([2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s), confidence: stated)
- Swapping in Mixedbread's late-interaction search closes the Oracle gap to three points on BrowseComp Plus and nearly entirely on Office QA Pro, without changing the reasoning model. ([3:14](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=194s), confidence: stated)
- Agents write keyword-stuffed queries because they are trained on grep-based code exploration, on human-optimized web tools, and against benchmarks that favor BM25. ([4:05](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=245s), confidence: stated)
- Standard retrieval benchmarks such as BEIR and NanoBEIR use entity-based 'caveman style' queries that structurally advantage BM25 and therefore mis-train agent query behavior. ([4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s), confidence: stated)
- Instructing a model to write 'one concise sentence describing what it wants to find' produces better semantic queries than instructing it to write a search query. ([9:05](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=545s), confidence: stated)
- A search agent should expose several differentiated tools rather than one, so semantic search and grep are each used only for the intent they fit. ([8:15](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=495s), confidence: stated)
- Capping the loop at four search rounds with parallel searches inside each round gives enough exploration while keeping the agent fast. ([6:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=385s), confidence: stated)
- A small LLM, distilled from a larger teacher and then RL-trained on search rewards, is sufficient for high-quality agentic retrieval and is faster. ([9:59](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=599s), confidence: stated)
- Rewarding trajectory quality — natural-sentence queries and appropriate exploration volume — in addition to final ranking metrics is necessary to fix agent search behavior. ([10:50](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=650s), confidence: implied)
- Their agent achieves NDCG@10 of 0.4 on the Oblique Congress benchmark versus 0.18 for the best model reported in that benchmark's paper. ([12:33](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=753s), confidence: stated)
- Their production beta agent is ranked first on Snowflake's MatchQA benchmark at 93.4% accuracy with Gemini 3.5 Flash, at lower cost than comparable search-agent setups. ([13:24](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=804s), confidence: stated)
- There remains substantial headroom in how large language models use their search tools. ([13:24](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=804s), confidence: stated)

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

