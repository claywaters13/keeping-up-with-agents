---
title: "retrieval evaluation"
type: "concept"
slug: "retrieval-evaluation"
tier: "supporting"
maturity: "contested"
talk_count: 8
speaker_count: 10
---

# retrieval evaluation

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **8** talk(s) by **10** speaker(s)

**Definition:** Measuring the retrieval stage on its own terms — recall, precision, and corpus freshness — separately from end-to-end answer quality.

*Also referred to as: retrieval recall evaluation, corpus freshness and reindexing cost, golden set curation, golden datasets, golden dataset, precision and recall tradeoffs*

## State of Practice

The field arrived at this conference agreeing that retrieval, not reasoning, is now the binding constraint on agentic answer quality — and that you cannot see this unless you score the retrieval stage separately. The sharpest instrument presented was the Oracle ceiling: hand the model the known-correct documents and measure the gap between that score (93% on BrowseComp Plus, 64% on Office QA Pro) and what the same model achieves against the real corpus (nine and eight points with Codex's default tools). Below that, practitioners are measuring recall per retrieval mode (semantic and keyword each miss ~25% alone, ~10% combined), NDCG@10 against public benchmarks, and recall decay as corpus size grows — one team reported recall collapsing to near zero at 396 files when individual files carried many responsibilities. There is no agreed metric suite, however, and the standard benchmarks are under direct attack: BEIR and NanoBEIR were argued to use entity-based 'caveman style' queries that structurally favor BM25 and therefore mis-train agents into writing keyword-stuffed queries. Everyone who touched an LLM judge reported it misbehaving — family favoritism, over-strictness, self-censorship when the generator grades itself — so the operative pattern is a curated golden dataset that absorbs every production failure mode, plus trace inspection, plus a judge held structurally independent of the system under test.

## Consensus

### Retrieval quality, not model capability, is the bottleneck in knowledge-heavy tasks — so retrieval must be measured before swapping in a better model.

Support: **4** talk(s)

> "So we see that the models are extremely capable if they would get the right documents but if you put them into the noisy corpus the performance drops sharply. Meaning that actually the bottleneck here is not the reasoning. It's actually the access to the right knowledge it needs to answer this question."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s)

Supporting talks: [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)

### Aggregate pass-rate metrics hide the failures that matter; you have to read traces and intermediate steps to find them.

Support: **4** talk(s)

> "And we could not find that if we were just doing a categorical like the this x% pass rate or not. So we really had to look at the traces to see what was going on."
>
> — [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [11:34](https://www.youtube.com/watch?v=xyL2Ltkh-SA&t=694s)

Supporting talks: [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Agents Building Agents](../talks/agents-building-agents.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)

### The evaluator must be structurally independent of the system it grades — self-verification and same-family judging both corrupt the score.

Support: **3** talk(s)

> "when the discovery agent is trying to verify its own work in the loop, trying to debate against itself in the loop, it may actually self censor and this may actually hurt recall"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [11:46](https://www.youtube.com/watch?v=imFedndyXYQ&t=706s)

Supporting talks: [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [Agents Building Agents](../talks/agents-building-agents.md), [Frontier results, on device](../talks/frontier-results-on-device.md)

### A curated golden dataset is the ground truth, and it should be continuously fed with failure modes found in production traces rather than frozen at creation.

Support: **3** talk(s)

> "all the failure modes that we are founding during this investigation step, they will become part of the golden dataset that we mentioned earlier and the eval suite is updated to spot those regressions."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [25:33](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1533s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)

### Recall is corpus- and structure-dependent, so it must be re-measured as the corpus scales rather than assumed stable from a small-corpus benchmark.

Support: **3** talk(s)

> "We tested on large projects with 396 files. The recall dropped almost zero. If your files each do one thing, it works well. If your files do many things, it struggles."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [7:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=455s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

## Disagreements

### Should retrieval quality be fixed by improving selective retrieval, or by abandoning selection and putting the whole corpus into cached context?

| Position A | Position B |
|---|---|
| Keep selective retrieval and make it better — late-interaction semantic search, differentiated tools, hybrid semantic+keyword scoring, and dynamic tool access — then score it with recall/NDCG against an Oracle ceiling.<br>*[How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)* | When every document in the collection is relevant, similarity-thresholded retrieval is structurally the wrong tool; load documents into parallel KV caches and have a supervisor interrogate the buckets instead.<br>*[When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* |

*Why it matters: It determines whether recall@k is even a meaningful metric for your system, or whether you should be measuring supervisor bucket-routing coverage and cache lifetime cost instead. It also flips the cost model from token-per-query to KV-cache residency.*

### Should a rigorous eval harness exist before you start iterating, or should you deliberately evaluate by intuition first?

| Position A | Position B |
|---|---|
| Build the golden dataset and scorers up front — they are the harness that makes everything else possible, and choosing without evals ships materially worse products (Gemma was the peer-recommended pick but came in around 8 seconds of latency).<br>*[Agents Building Agents](../talks/agents-building-agents.md), [Frontier results, on device](../talks/frontier-results-on-device.md)* | Vibe first. Early-stage non-scalable intuition evaluation is better than a comprehensive eval, because architecture is still changing and moving to scaled raters too early produces large swings while eval and model are both uncalibrated; start hands-on rather than aiming for automation.<br>*[How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)* |

*Why it matters: It sets where a team spends its first month and whether early prompt/architecture changes are reversible. Premature scaled rating burns budget measuring a moving target; premature vibing means you cannot prove any change helped, and regressions ship silently.*

### Should retrieval results be scored by an LLM judge, or by deterministic metrics and heuristics?

| Position A | Position B |
|---|---|
| LLM judges with explicit rubrics are necessary — they can score trajectory quality (is the query a natural sentence? was exploration sufficient?) and can be kept honest by sampling human-vs-LLM agreement.<br>*[How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Agents Building Agents](../talks/agents-building-agents.md)* | LLM-in-the-loop scoring is too slow and too biased — a weighted heuristic (50% semantic, 30% keyword, 20% recency) runs in 0.4ms versus 2-3 seconds for LLM reranking, and judge scores skew toward the judge's own model family, so numbers must be inspected by hand rather than trusted.<br>*[We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Frontier results, on device](../talks/frontier-results-on-device.md)* |

*Why it matters: This decides whether retrieval eval can run inline in production (heuristics can; LLM judges add seconds and cost) and whether reported score improvements are real or artifacts of judge bias.*

## Practical Guidance

**Do:**

- Measure an Oracle ceiling first — feed the model the known-correct documents and compare against its score on the real corpus — to attribute failure to retrieval versus reasoning before touching the model.
- Report recall separately per retrieval mode; semantic and keyword each miss about one in four results alone, versus about one in ten combined.
- Re-measure recall as corpus size grows, especially where files or documents carry many responsibilities — one system's recall fell to near zero at 396 files.
- Instruct the retrieval agent to write 'one concise sentence describing what it wants to find' rather than 'write a search query', to break the BM25 keyword-stuffing pattern.
- Cap the agentic search loop at a fixed number of rounds (four was reported as sufficient) with parallel searches inside each round.
- Reward trajectory quality (natural-sentence queries, appropriate exploration volume) alongside final ranking metrics when training or scoring a search agent.
- Run regression evals continuously as CI tests so a prompt or model change cannot silently degrade retrieval behavior.
- Keep held-out test sets, use them sparingly, and refresh them with production data.
- Run discovery and verification as separate agents, with the verifier denied access to the discovery agent's reasoning traces and assuming the finding is false by default.
- Explicitly forbid any self-optimizing agent from editing the golden dataset or the scorers.
- Monitor human-versus-LLM-judge agreement through a sampling pipeline, and require raters to give explanations rather than binary pass/fail.
- Treat corpus freshness as an eval dimension with a decay budget: under a day for social media, roughly 30 days for news, finance, and retail.
- Fix ranking, structural, and length failures with deterministic post-processing in the harness before reaching for a bigger model.
- Decide launch gatekeeping criteria before running regression analysis, not after seeing the results.

**Avoid:**

- Don't treat BEIR/NanoBEIR-style entity keyword benchmarks as a proxy for agentic retrieval quality — they structurally favor BM25 and mis-train agents into caveman-style queries.
- Don't judge a retrieval system on end-to-end pass rate alone; it hid an agent actively removing legally required disclaimers.
- Don't trust LLM-judge scores numerically across model families — Claude Opus favored Claude Sonnet's output over Llama 3.2's.
- Don't let a discovery or optimization agent grade its own work; it self-censors and loses recall, or it cheats the evals outright.
- Don't organize documents into domain buckets in a multi-cache setup — with dense inter-document relationships the supervisor skips domains that look irrelevant at first glance.
- Don't change the prompt in response to a single failing run; measure the failure pattern across multiple examples first.
- Don't quote reduction figures against a worst-case full-file-read baseline as if they were real-world savings — modern agentic tools are already smarter than that baseline.
- Don't move to scaled human raters before the eval and the system are calibrated; you get large ups and downs that reflect the rubric, not the model.
- Don't select a retrieval or generation model on peer recommendation instead of your own evals.
- Don't assume a rented context provider can be evaluated on price alone — search-based alternatives carry significant extra token cost to structure raw results, and query frequency, not record volume, drives the bill.

## Notable Outliers

- Standard retrieval benchmarks are not merely imperfect but actively harmful: BEIR and NanoBEIR use entity-based queries that structurally favor BM25, which is part of why agents learn to write keyword-stuffed queries. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s))
- A 0.4ms weighted heuristic (50% semantic, 30% keyword, 20% recency) with an adaptive threshold outperformed LLM-based reranking, which added 2-3 seconds per query. ([We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s))
- Organizing documents into domain buckets hurts recall; distributing them in no particular order, balanced only for minimum bucket size, works better. ([When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:50](https://www.youtube.com/watch?v=XovaGv4f39A&t=230s))
- Context-as-a-Service providers are structurally capped in recall: if the vendor never collected a field, no agent can ever retrieve it from them, whereas a search-based agent can keep exploring. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [11:34](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=694s))
- Giving the model dynamic tools — API queries, logs, live source, sandboxes to detonate proofs-of-concept — rather than code alone raised true positive rate to nearly 100%. ([Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [10:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=631s))
- Prompt-side instructions to retrieve less context are structurally useless: the context is already transmitted and billed before the model reads the prompt. ([We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [1:57](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=117s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)
- [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)
- [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)
- [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

## Speakers

- [Chris Souza](../speakers/chris-souza.md)
- [Daniel Bump](../speakers/daniel-bump.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [Eugene Yan](../speakers/eugene-yan.md)
- [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Preetika Bhateja](../speakers/preetika-bhateja.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)

