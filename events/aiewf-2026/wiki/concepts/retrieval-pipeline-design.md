---
title: "retrieval pipeline design"
type: "concept"
slug: "retrieval-pipeline-design"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 14
---

# retrieval pipeline design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **14** speaker(s)

**Definition:** The mechanics between corpus and context — chunking, indexing, reranking, and top-k thresholds — as engineering choices with measurable effects.

*Also referred to as: semantic chunking, chunking strategies, reranking, retrieval re-ranking, top-k retrieval tuning, semantic code chunking, chunkless retrieval, relevance scoring and thresholding*

## State of Practice

The field has stopped treating retrieval as a solved commodity layer ("chunk it, embed it, top-k it") and now treats every stage between corpus and context as a measurable engineering decision. The dominant diagnosis is that pure embedding similarity is not a retrieval strategy: it misses about one in four relevant items on its own (we-cut-94), collapses entirely on near-identical entity names (semantic-blindness), and cannot express "return everything" or multi-hop traversal at all (when-all-context-matters, a-practitioners-guide-to-graphs). Practitioners are responding by pushing work in two directions — upstream into ingestion (layout-aware parsing, heading-based chunking, insert-time tokenization, precomputed hierarchies and graphs) and sideways into deterministic code (BM25 + reciprocal-rank fusion, weighted heuristic rerankers, set operations) — while shrinking what actually reaches the model. The economics are now explicit and quantified: ~90% of AI coding spend is input tokens, 73% of agent pipeline failures trace to retrieval and context stuffing, a 741-tool catalog costs 127k tokens per request, and a naive full-context validation pass burned 116M tokens where a structured one used 390k. What is genuinely unsettled is the substrate — several credible teams now ship retrieval systems with no vector database at all (markdown outlines, reference indexes, parallel KV caches), while others treat the embedding index as the boring, adequate default and put their effort into what gets ranked and why.

## Consensus

### Pure vector/semantic similarity is insufficient as a retrieval strategy on its own and must be combined with keyword matching, structural traversal, or deterministic set logic.

Support: **6** talk(s)

> "By themselves, both searches miss about one in four results. Together, they miss about one in 10."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [4:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=275s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)

### The size of the model's working set, not the size of the corpus, is the thing to optimize — retrieval pipelines should aim for order-of-magnitude token reductions rather than better recall at any cost.

Support: **6** talk(s)

> "This is the core lesson from the benchmark. The catalog can grow, but the model's working set should stay small."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [15:32](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=932s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### Answer correctness is determined upstream by how source data is parsed, chunked, and modeled — far more than by model choice or retriever tuning.

Support: **6** talk(s)

> "that data and the way you process it is the key determining factor in whether your answer is going to be correct or incorrect for the user or customer at the end of the day"
>
> — [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [2:37](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=157s)

Supporting talks: [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)

### Anything in the retrieval path that can be expressed as deterministic code — reranking formulas, set operations, dedup, counting, filters, guardrails — should be code rather than an LLM call, for cost, latency, testability, and hallucination reasons.

Support: **4** talk(s)

> "It runs 0.4 milliseconds, no extra AI calls needed. The lesson we learned, simple formula beats the complex model most of the time."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)

### Expensive understanding work belongs at ingestion/index time, paid once, rather than at query time per request.

Support: **5** talk(s)

> "Number one is to ingest once and reason many times."
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [8:53](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=533s)

Supporting talks: [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### Retrieval must stay traceable back to a specific source unit (chunk, section, timestamp) so failures are debuggable and answers are citable; designs that break that chain are a regression.

Support: **3** talk(s)

> "Then you can go track it why this right chunk hasn't been retrieved. So, in this way you have more uh more uh clear path towards how you can debug it."
>
> — [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [16:28](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=988s)

Supporting talks: [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)

## Disagreements

### Does a serious retrieval pipeline need a vector database and embedding index at all?

| Position A | Position B |
|---|---|
| No — drop the vector DB. Use plain files with a reference index, the document's own markdown section outline, or parallel KV-cached context buckets as the retrieval substrate; embeddings add infrastructure that is opaque, hard to inspect by hand, and unnecessary for the actual access patterns.<br>*[Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* | Yes — the embedding index is the boring, adequate default. Postgres + pgvector with BM25 fusion, or an embedding call plus one vector search, is cheap enough that the choice of embedding model and vector DB is nearly immaterial; the leverage is in what you index and how you rank it.<br>*[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)* |

*Why it matters: This decides whether a team stands up and operates embedding infrastructure at all, and whether retrieval quality work happens in ranking code or in document structuring. The no-vector-DB camp is mostly describing corpora that are small, hierarchical, or personally curated; the pro camp is describing heterogeneous corpora where users query in words that never appear in the source.*

### Should retrieval run as a fixed, bounded pipeline or as an agentic loop that iterates until satisfied?

| Position A | Position B |
|---|---|
| Fixed and bounded. A direct-RAG path (embed query → hybrid retrieve → answer) or a two-to-three-step plan-then-resolve pipeline keeps the execution path predictable, cost flat, latency under control, and the citation chain intact; three or four agent loops add 20-30 seconds and lose the user.<br>*[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)* | Agentic iteration is the mechanism. Let the model search the document outline over multiple turns (418-section annual report), or let a supervisor progressively explore context buckets and ask follow-up questions, or run a multi-round deep-research loop — iteration is what makes a structure-only index work without embeddings.<br>*[Structuring the Unstructured](../talks/structuring-the-unstructured.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)* |

*Why it matters: It sets the cost and latency profile of every query and determines whether the system is auditable for compliance. Notably the two camps split on corpus dynamics: the bounded camp serves high-volume user-facing queries, the iterative camp serves low-volume, high-value research and analysis queries.*

### Is building an explicit graph or hierarchy over the corpus worth its construction and maintenance cost?

| Position A | Position B |
|---|---|
| Yes — structure is the enabling capability, not an optimization. Shortest-path traversal surfaces intermediate nodes vector search and symbol lookup cannot find (40% fewer tool calls on a .NET codebase); a property graph lets an agent discover and traverse schema at query time; growing context with tree depth instead of instance count held 100% correctness from 64 to 460,000 GPUs.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)* | Usually not. Recomputing a knowledge graph every time the corpus is replaced is prohibitively slow, and for personal or document-shaped corpora the graph is infrastructure you should explicitly forget you need — a reference index or the document's existing outline gets you there.<br>*[When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)* |

*Why it matters: Graph construction is the single largest upfront investment in a retrieval pipeline and the one hardest to reverse. The dividing variable that emerged is corpus churn and intrinsic structure: graphs pay off on stable, densely-linked, hierarchical data and lose badly on frequently-replaced document collections — even the graph advocate opens by warning that graphs are often not the right tool.*

## Practical Guidance

**Do:**

- Combine BM25 keyword search with semantic search and fuse the rankings — exact-match domains (SKUs, brand names, medications, near-identical equipment names) fail catastrophically on embeddings alone.
- Chunk on document structure (headings, question-answer pairs, sections) rather than fixed 512-character windows with overlap, so every chunk is clean, referenceable, and debuggable.
- Rerank with a cheap weighted heuristic — one team used 50% semantic, 30% keyword, 20% recency with an adaptive threshold, running in 0.4ms — instead of an LLM judge that adds 2-3 seconds per query.
- Tune top-k per domain rather than globally: retrieve more for product catalogs (unretrieved products are unsellable), fewer for medical answers where accuracy and liability dominate.
- Run your test set at K=3, 5, and 10 and pick the smallest K that hits your accuracy target; K=5 is a reasonable starting default for tool/schema retrieval.
- Route tools through the same retrieval pattern as documents once you pass ~50 tools — just-in-time schema injection cut tool context from ~127k to ~1,000 tokens while holding selection accuracy above 83%.
- Tokenize at insert time, not query time, and serve reads and listings from a denormalized collection separate from the source-of-truth store.
- Scale context with hierarchy depth rather than instance count, and use deterministic set operations for counting, dedup, and exact set logic over near-identical names.
- Use a layout-aware local document converter (CPU-only, open source) rather than a frontier VLM for bulk PDF conversion — roughly 50x cost savings and deterministic output that survives model deprecation.
- Measure savings by instrumenting real queries against a stated baseline, and be explicit about what the baseline is (94% was against worst-case full-file reads, not against a modern agentic tool).
- Give an extraction model a domain schema plus ontology instructions (naming and unit standardization), then add a separate embedding-based matching step — prompt-level standardization alone is not reliable.
- Block prompt injection and out-of-scope requests in code before the LLM call, rather than via system-prompt instructions.

**Avoid:**

- Bulk-uploading unstructured documents into a hosted chatbot — you pay tokens before any question is asked, you cannot see how it chunked, and accuracy drops while hallucination rises.
- Assuming semantic similarity suffices for entity resolution: near-identical names produce indistinguishable embeddings, and sharding those names across parallel LLM calls yields phantom equipment and silent omissions.
- Sending hundreds of tool schemas or documents in a single prompt — accuracy fell from ~78% at 10 tools to 13.6% at 741 tools, driven by lost-in-the-middle attention, not by badly written tools.
- Filling the context window as full as it will go; answer quality degrades well before the hard token limit.
- Bucketing documents by domain and letting a supervisor pick buckets — with dense inter-document relationships it skips domains that look irrelevant at first glance; distribute documents in no particular order instead.
- Optimizing output length, max tokens, or temperature to control spend when ~90% of the cost is input, or instructing the model to 'send less context' after the context has already been transmitted and billed.
- Adding agent mode or extra tools to a RAG chatbot without checking what it costs you — agent-driven search breaks the citation chain back to source chunks.
- Free-form subject-predicate-object triple extraction with no schema; the resulting graph is not something you get very far with.
- Assuming a single-file-per-concept code index generalizes — recall dropped to nearly zero at 396 files when individual files carried many responsibilities.
- Treating eval results and observability traces as a dashboard artifact — with no path back into retrieval, the pipeline cannot learn from yesterday's failures.

## Notable Outliers

- You can do RAG with no chunker, no embedding model, and no vector database — the index is just the markdown outline of the document, searched by the agent over multiple turns, and it worked on a 418-section annual report. ([Structuring the Unstructured](../talks/structuring-the-unstructured.md), [14:32](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=872s))
- Retrieval context should grow with tree depth, not instance count: describing all root-to-leaf paths is a small finite list, so a 64-GPU and a 460,000-GPU system cost about the same 9,000 tokens per query. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [5:39](https://www.youtube.com/watch?v=EUsPvBeIx70&t=339s))
- Organizing documents into domain buckets actively hurts recall; distribute them in no particular order, balanced only so the fewest documents per bucket are needed. ([When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:50](https://www.youtube.com/watch?v=XovaGv4f39A&t=230s))
- A 0.5B-parameter model (~400MB, CPU-only) is sufficient for an FAQ assistant and hallucinates less than larger models, provided the retrieved context is well-vetted first. ([Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [42:30](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2550s))
- Retrieval ranking should be weighted by whether a memory historically helped or hurt task outcomes, not by similarity alone — 66% to 76% on tau-bench policy following, 80% once memories are consolidated into skills. ([User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s))
- AI-native systems should start as pure software 3.0 (throw everything in the context window to find out what is worth building) and migrate toward deterministic 1.0 as they mature — the reverse of legacy software's drift. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s))
- Enterprise retrieval correctness is defined socially, not factually: an answer is only correct if it matches how the question has historically been answered under existing reporting conventions. ([Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [6:32](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=392s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)
- [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)
- [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md)
- [Structuring the Unstructured](../talks/structuring-the-unstructured.md)
- [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)
- [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)
- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)
- [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)
- [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Abed Matini](../speakers/abed-matini.md)
- [Ankush Rastogi](../speakers/ankush-rastogi.md)
- [Arek Borucki](../speakers/arek-borucki.md)
- [Cedric Clyburn](../speakers/cedric-clyburn.md)
- [James Le](../speakers/james-le.md)
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Mike Phipps](../speakers/mike-phipps.md)
- [Paul Iusztin](../speakers/paul-iusztin.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Tim Ainge](../speakers/tim-ainge.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)

