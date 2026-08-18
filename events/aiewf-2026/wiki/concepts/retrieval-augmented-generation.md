---
title: "retrieval-augmented generation"
type: "concept"
slug: "retrieval-augmented-generation"
tier: "core"
maturity: "consolidating"
talk_count: 11
speaker_count: 11
---

# retrieval-augmented generation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **11** talk(s) by **11** speaker(s)

**Definition:** Grounding generation in an external corpus retrieved at inference time; the overall architecture, not any single retrieval component.

*Also referred to as: retrieval augmented generation, retrieval pipelines, vector rag, enterprise data grounding, retrieval over private corpora, cache augmented generation, corpus-level retrieval*

## State of Practice

The field has stopped treating RAG as "embed, cosine-similarity, stuff the top-k into a prompt" and now treats it as a full architecture: ingest, curate, ground, budget tokens, and evaluate. Nearly every speaker who touched retrieval reported that pure vector similarity underperforms — Microsoft's measured result is that combined methods (lexical + vector + metadata filtering) beat any single method on real customer scenarios, MongoDB's healthcare example needs metadata pre-filtering for diagnosis/procedure codes, and Sakana's benchmark had a rank-only decisions ledger beat vector RAG outright on long-horizon recall. The second shift is that the corpus, not the retriever, is where the work is: provenance on every fact, contradiction checks, active pruning, and grounding every claim to a specific source location (a citation, a video timestamp) are now table stakes, with missing-citation rate and human-override rate tracked as production metrics. The third is that retrieved context is a token budget to be optimized, not a bucket to be filled — speakers reported rendering time-series as images for fixed token cost, exposing top-K-truncated-plus-drill-down tools instead of raw log dumps, summarizing subagent findings back to a parent, and explicitly optimizing for information density per token. Where the field is still arguing: whether to retrieve a subset at all versus load the whole corpus into parallel KV caches, whether the retrieval loop should be model-driven or held inside a deterministic harness, and whether semantically organizing the corpus helps or actively hurts recall.

## Consensus

### Vector similarity search alone is insufficient for production retrieval; it must be combined with lexical search, metadata pre-filtering, or a different structure entirely.

Support: **5** talk(s)

> "I think, you know, for a hot second as an industry, we thought that if we could get really, really good at computing cosine similarity between vectors, we were all set for retrieval. It turns out, you know, things never are are never that easy."
>
> — [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [7:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=444s)

Supporting talks: [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)

### Retrieved context is a token budget to be optimized, not a window to be filled; what ends up in context determines answer quality more than retriever sophistication.

Support: **6** talk(s)

> "The problem here is that the context window is limited, and if you fill the context window too much, the quality of the answer gets degraded, too."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:12](https://www.youtube.com/watch?v=XovaGv4f39A&t=192s)

Supporting talks: [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)

### Retrieval quality is bounded by corpus hygiene: without provenance on every fact, contradiction checking, and active pruning, retrieval confidently surfaces stale or wrong information.

Support: **5** talk(s)

> "the primitive is not memory. It's memory plus hygiene, provenance on every fact, contradiction contradiction checks when new information collides with the old, and a librarian, human plus agent, whose actual job is pruning."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [14:39](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=879s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)

### The retriever is the commodity; the differentiated asset is the curated, organization-specific corpus being retrieved from.

Support: **4** talk(s)

> "Retrieval is easy. Being worth retrieving from is the product."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [12:37](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=757s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md)

### Retrieval architecture should be matched to task difficulty — start with the simplest thing, and add a retrieval or memory layer only when evaluation shows the task does not fit in context.

Support: **4** talk(s)

> "the memory actually didn't add more capability. It was the same performance with memory and without memory, and it only added more cost. So, when your task fits in context, the harness doesn't add much."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [5:43](https://www.youtube.com/watch?v=R3-anFK1YM8&t=343s)

Supporting talks: [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

### Fine-tuning is the wrong instrument for a grounding or data problem; put the source material in the context window instead and reserve fine-tuning for behavioral failures.

Support: **3** talk(s)

> "Fine-tuning tries to make the model be the persona. The context window lets the model speak through the persona's record."
>
> — [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [27:12](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1632s)

Supporting talks: [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)

## Disagreements

### When the corpus is small enough to fit, should the system retrieve a relevant subset at all, or load the entire corpus into context (sharded across parallel caches)?

| Position A | Position B |
|---|---|
| Skip selective retrieval: split the whole document set across parallel KV-cached context buckets and have a supervisor interrogate all of them, because thresholded similarity retrieval structurally cannot return 'all documents' when every document is relevant.<br>*[When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* | Always retrieve selectively into a curated, structured layer — pay understanding cost once at ingest, store primitives, and optimize for the most information-dense answer in the fewest tokens, because dumping everything destroys relationships and wastes budget.<br>*[Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* |

*Why it matters: It decides whether your cost curve is dominated by per-query KV cache lifetime or by one-time ingestion plus index maintenance, and whether corpus churn (documents replaced frequently) is cheap or catastrophic.*

### Should the retrieval loop be driven by the model's own reasoning, or constrained inside a deterministic harness?

| Position A | Position B |
|---|---|
| Let the model drive: agentic retrieval that reflects on whether the information need is satisfied beats single-shot on hard cases, and hand-built deterministic graphs proved more brittle than a reasoning-and-acting agent for diagnosis.<br>*[On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* | Constrain it: a bare model is stateless and unconstrained, so retrieval needs an explicit deterministic harness with task planning, an operating envelope, and output contracts — and computation that belongs in deterministic space must never be pushed into latent space.<br>*[Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* |

*Why it matters: It determines whether cost and latency are bounded per query or open-ended, and whether failures are debuggable by reading a fixed pipeline or require replaying a nondeterministic trace.*

### Does semantically organizing the corpus (domain buckets, knowledge graphs, entity structure) improve or degrade recall?

| Position A | Position B |
|---|---|
| Structure it: build a durable context graph linking moments, entities, appearances, and time spans, or a hygiene-managed brain with hot/cold promotion — capability comes from memory organization, not a smarter model.<br>*[Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* | Don't over-structure: organizing documents into domain buckets hurt recall because the supervisor skipped domains that looked irrelevant at first glance, so distribute in no particular order; and a rank-only decisions ledger outperformed both vector RAG and gated memory.<br>*[When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)* |

*Why it matters: Semantic partitioning is expensive to build and re-derive on every corpus update; if it also biases the router away from non-obvious sources, teams are paying twice for negative value.*

### Where does the next marginal gain in grounded generation come from — better models, or better retrieval infrastructure around them?

| Position A | Position B |
|---|---|
| Intrinsic model knowledge, not retrieval or tooling, is what produced the current exponential in AI-assisted work.<br>*[On AI and Knowledge](../talks/on-ai-and-knowledge.md)* | The models are effectively fixed inputs — everyone uses the same weights — so the gains come from infrastructure: fresh live data pipelines, workflow wiring, memory organization, and context management as model release cadence slows.<br>*[How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)* |

*Why it matters: It sets whether a team's roadmap is 'wait for the next model and keep the stack thin' or 'invest in ingestion, curation, and recall policy as the durable asset.'*

## Practical Guidance

**Do:**

- Combine retrieval methods — lexical, vector, and metadata pre-filtering — and evaluate them against each other on real customer scenarios rather than shipping cosine similarity alone.
- Expose retrieval effort as a configurable knob: single-shot retrieval for easy queries, agentic reflect-and-re-retrieve only for hard ones, treating it explicitly as a latency-vs-quality trade.
- Pay expensive understanding once at ingestion and store primitives (moments, entities, appearances) rather than pre-computed answers, so queries never reprocess the archive.
- Ground every generated claim to a specific source location (citation, timestamp) and track missing-citation rate and claim-rejection rate as production guardrail metrics.
- Attach provenance to every stored fact, run contradiction checks when new information collides with old, and make human corrections permanently outrank model-derived facts.
- Replace raw dumps with summarizing tools: give the agent 'top-K truncated exceptions' plus a drill-down tool instead of the log itself, and render time-series metrics as images so input token count is fixed regardless of job duration.
- Have subagents summarize findings back to the parent so the parent's context window stays healthy.
- Treat recall policy as a first-class metric and measure it on token spend, not just accuracy — bad recall costs tokens and sends the agent the wrong way.
- Snapshot real downstream tool responses as checked-in fixtures and run offline evals against them, instead of testing manually against production data that gets retention-deleted.
- Run each ingestion pipeline at a cadence matched to that source's update frequency, or the system answers confidently from stale data.
- Ship with both offline evaluation and production monitoring — evaluation before, monitoring after, and neither substitutes for the other.
- Put a domain expert in the evaluation loop at build time and gate time for fidelity-critical corpora; automated metrics cannot adjudicate whether output matches an archive they cannot see.

**Avoid:**

- Assuming that retrieving the right document means the model will use it — oracle retrieval did not reach maximum task performance; the model can still ignore or misread correct memory.
- Filling the context window as full as it will go; answer quality degrades well before the hard token limit.
- Partitioning documents into domain buckets when inter-document relationships are dense — the supervisor skips domains that look irrelevant at first glance.
- Choosing GraphRAG for a corpus that is replaced frequently; recomputing the knowledge graph on every replacement is too slow and expensive to be viable.
- Feeding raw time-series or raw logs to the model — token-inefficient, and it breaks on long-running jobs even when it works in the small.
- Fine-tuning to fix what is actually a data or orchestration problem; it layers thin signal over unauditable base weights and can trigger catastrophic forgetting.
- Treating retrieval as done once search works — an uncurated corpus becomes a garbage dump with great search that surfaces stale facts with total confidence.
- Holding large combinatorial state (e.g. an 800-person seating arrangement) in the context window when it belongs in deterministic compute.
- Jumping to an agentic or multi-agent retrieval architecture before evaluation has shown what is actually failing.
- Relying on the last exception in a log as the root cause, or on regex filters to clean retrieval inputs — neither scales; learn which signals appear in successful runs and filter those as red herrings.

## Notable Outliers

- Documents should be distributed across parallel context caches in no particular order, balanced only so the fewest documents per bucket are needed — deliberately random assignment beat semantic bucketing. ([When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:50](https://www.youtube.com/watch?v=XovaGv4f39A&t=230s))
- A rank-only decisions ledger outperformed both vector RAG and binary memory gating across 68 questions, multiple seeds, two local models, and a second benchmark (Spider V2). ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [7:31](https://www.youtube.com/watch?v=R3-anFK1YM8&t=451s))
- Rendering time-series metrics as images beats feeding raw series to the LLM, because it guarantees a fixed input token count for any Spark job regardless of duration. ([Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s))
- Every knowledge base should be exposed as an MCP server so agents connect with no glue code. ([On AI and Knowledge](../talks/on-ai-and-knowledge.md), [10:55](https://www.youtube.com/watch?v=RGSFUqzqErE&t=655s))
- For historical personas, fine-tuning is strictly worse than context-window anchoring: it suppresses random distortion at the surface while amplifying cultural contamination underneath, where it can no longer be audited. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [28:10](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1690s))
- Latency is not a performance metric but a product constraint — a 4-second retrieval pipeline cannot support interactive AI workflows, and getting to 550ms required a ground-up redesign, not optimization. ([How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [11:16](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=676s))
- A company-wide grounded agent system was built for ~$30,000 against a $230,000 agency quote, with zero training cost, running at a couple thousand dollars a month. ([The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [8:28](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=508s))

## All Talks

- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)
- [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)
- [On AI and Knowledge](../talks/on-ai-and-knowledge.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)
- [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

## Speakers

- [Apoorva Joshi](../speakers/apoorva-joshi.md)
- [Drasko Profirovic](../speakers/drasko-profirovic.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [James Le](../speakers/james-le.md)
- [James Russo](../speakers/james-russo.md)
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Stefania Druga](../speakers/stefania-druga.md)

