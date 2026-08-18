---
title: "hybrid retrieval"
type: "concept"
slug: "hybrid-retrieval"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 9
---

# hybrid retrieval

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **9** speaker(s)

**Definition:** Combining dense vector search with lexical or structured search and fusing the result sets.

*Also referred to as: hybrid search, vector similarity search, bm25 keyword search, vector search, vector index retrieval, reciprocal rank fusion, late interaction retrieval*

## State of Practice

The field has closed the book on pure dense retrieval: every talk that touched retrieval quality reported that cosine similarity over embeddings alone loses a material fraction of relevant results, and that adding a second, differently-biased retrieval leg recovers most of it (Tesco measured ~25% miss for each of semantic and keyword alone versus ~10% fused; Microsoft reported combined methods beating individual methods specifically on real customer scenarios rather than academic sets). The failure modes are now named and specific rather than vague: exact identifiers (SKUs, medication names, diagnosis and procedure codes) that embeddings blur, negation and coverage questions ('what documentation are we missing') that similarity structurally cannot express, and multi-hop chains where every fact is indexed but no single chunk is similar to the question. What is unsettled is what the second leg should be — BM25/lexical, metadata pre-filters, or graph traversal seeded by vector hits — and whether fusion should be a fixed, deterministic scoring pipeline or an agent that reflects and re-queries. Fusion itself is trending cheap and deterministic: a weighted score (50% semantic / 30% keyword / 20% recency) at 0.4ms and SQL-side reciprocal rank fusion were both preferred over LLM rerankers that add 2-3 seconds. The same retrieval-plus-fusion pattern is now being pointed at non-document corpora — tool schemas, agent memory, warehouse metadata — on the argument that teams already running RAG need no new infrastructure to do it.

## Consensus

### Vector/semantic similarity alone is insufficient for production retrieval; it must be combined with a lexical, metadata, or structural retrieval method.

Support: **6** talk(s)

> "I think, you know, for a hot second as an industry, we thought that if we could get really, really good at computing cosine similarity between vectors, we were all set for retrieval. It turns out, you know, things never are are never that easy."
>
> — [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [7:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=444s)

Supporting talks: [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)

### Fusing two retrieval modalities measurably lifts recall over either one alone, and the gain shows up on real workloads rather than only in theory.

Support: **3** talk(s)

> "By themselves, both searches miss about one in four results. Together, they miss about one in 10."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [4:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=275s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)

### The specific trigger for adding a lexical/keyword leg is corpora containing exact identifiers — medications, SKUs, brand names, diagnosis and procedure codes — where 'similar' is a wrong answer.

Support: **3** talk(s)

> "if it's a medical chatbot, you need the exact medication. You need don't need something similar or close to it. So, we need to have both both basically uh keyword search and um and the semantic search together."
>
> — [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [30:07](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1807s)

Supporting talks: [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### Retrieval quality, not model capability, is the binding constraint on answer accuracy and on cost — so effort belongs in the retrieval layer rather than in model selection.

Support: **4** talk(s)

> "So we see that the models are extremely capable if they would get the right documents but if you put them into the noisy corpus the performance drops sharply. Meaning that actually the bottleneck here is not the reasoning. It's actually the access to the right knowledge it needs to answer this question."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s)

Supporting talks: [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)

### Fusion and ranking should be done with deterministic code (weighted scores, RRF, structural rules) rather than an LLM call in the retrieval path, because deterministic paths are faster, reproducible, and testable.

Support: **3** talk(s)

> "It runs 0.4 milliseconds, no extra AI calls needed. The lesson we learned, simple formula beats the complex model most of the time."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)

## Disagreements

### Should the retrieval path be a fixed pipeline, or should an agent drive search with multiple reflective rounds?

| Position A | Position B |
|---|---|
| Use a fixed direct-RAG pipeline: embed query, run the hybrid retriever, answer. Agent loops add 20-30 seconds of latency, break the citation chain back to source chunks, and make the execution path unpredictable — disqualifying when compliance matters.<br>*[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)* | Let an agent run the search: cap it at ~4 rounds with parallel searches inside each round, or expose retrieval effort as a user-facing latency-versus-quality knob where single-shot handles easy cases and a reflective loop handles hard ones. Agentic retrieval beats single-shot on evidence recall and answer completeness for difficult queries.<br>*[How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md)* |

*Why it matters: This determines whether hybrid retrieval is a library call you can unit-test and cite from, or a runtime policy you have to evaluate, budget, and monitor. It also decides whether latency is bounded by construction or only in expectation.*

### What should the second retrieval leg be — lexical keyword search, or structural graph traversal?

| Position A | Position B |
|---|---|
| Pair dense search with BM25/keyword and metadata filters, fused by a scoring formula or SQL-side RRF. Two text-space modalities cut the miss rate to roughly one in ten, and the infrastructure is a Postgres/vector table you already run.<br>*[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)* | Pair dense search with graph traversal: use vector search only to pick seed nodes, then traverse relationships and rank by relatedness. Similarity in vector space is not relationship, so multi-hop questions stay unanswerable no matter how good the lexical leg is — and chaining vector hits adds a fresh chance of retrieving the wrong document at every hop.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)* |

*Why it matters: It sets the ingest burden: heading-based chunking and a keyword index versus entity extraction, a graph schema, and a Cypher-capable query layer. Note both position-B talks are from Neo4j, so the graph side is less independently corroborated than its two-talk count suggests; the lakehouse talk also explicitly says graph navigation is not a replacement and expects hybrid vector/full-text anyway.*

### Should agents be steered toward keyword-style queries, or away from them?

| Position A | Position B |
|---|---|
| Keyword queries are load-bearing — BM25 is a first-class leg of the retriever and exact-token matching is exactly what dense search cannot do, so keep the keyword score in the fusion formula (30% in Tesco's weighting) and expose keyword search as a tool.<br>*[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)* | Agents write keyword-stuffed 'caveman' queries because they were trained on grep-based code exploration and benchmarked on BEIR/NanoBEIR, which structurally favor BM25 — this is a training artifact to be corrected. Instruct the model to write one concise natural sentence describing what it wants to find, and RL-reward it for doing so.<br>*[How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)* |

*Why it matters: One camp tunes the fusion weights; the other changes the query the agent emits and treats the retrieval benchmark suite itself as the bug. If position B is right, teams optimizing hybrid weights against BEIR-style evals are hill-climbing a metric that rewards the wrong query distribution.*

### Should the retriever return a wide candidate set or the smallest set that meets the accuracy target?

| Position A | Position B |
|---|---|
| Go wide first: a broad semantic pass returning up to 50 chunks, shown to the agent as summaries, gives it an overview of the corpus before it narrows.<br>*[How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)* | Keep the working set small and domain-tuned: test K at 3, 5, and 10 and pick the smallest that meets the target (K=5 as default), retrieve more for product catalogs and fewer for medical answers because of accuracy and liability, and remember that removing irrelevant candidates is as valuable as surfacing the right ones.<br>*[The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)* |

*Why it matters: Candidate-set width drives both token spend and the lost-in-the-middle degradation that the 100-tool benchmark measured directly; a wide set is only safe if something downstream (summarization, a second narrowing round) shrinks it before the answer model sees it.*

## Practical Guidance

**Do:**

- Run dense and BM25/keyword retrieval in parallel and fuse the result sets; budget on the observed drop from ~1-in-4 misses per method to ~1-in-10 fused.
- Fuse with a cheap deterministic score — e.g. 50% semantic + 30% keyword + 20% recency with an adaptive threshold — and keep it in the sub-millisecond range rather than calling an LLM reranker that adds 2-3 seconds.
- Add a metadata pre-filter leg whenever documents carry codified identifiers (diagnosis and procedure codes, SKUs, medication names); vector search alone will not resolve them.
- Chunk on document headings (question/answer pairs) so a retrieval failure names a specific chunk you can trace, rather than an anonymous 512-character window.
- Sweep top-k at 3, 5, and 10 and ship the smallest K that hits your accuracy target; bias k up for product catalogs and down for medical or liability-sensitive answers.
- Expose several differentiated retrieval tools (wide semantic search, grep/lexical, structured query) instead of one generic search tool, so each intent hits the modality that fits it.
- Instruct the model to write 'one concise sentence describing what it wants to find' rather than 'write a search query', to keep it out of the keyword-stuffing pattern.
- For multi-hop questions, use vector search only to select seed nodes and then traverse relationships, ranking neighbors by relatedness, instead of chaining more vector hits.
- Make retrieval effort a configurable latency-versus-quality knob: single-shot for easy queries, a reflective/agentic loop for hard ones, capped at roughly four rounds with parallel searches inside each round.
- Optimize the retriever for information density per token, not relevance alone — the answer model pays for every retrieved token.
- Instrument real queries against a counterfactual baseline before claiming token or cost savings, and state which baseline the number is against.

**Avoid:**

- Treating cosine similarity as the whole retrieval system — it was a hot-second industry assumption that did not survive real customer scenarios.
- Asking semantic search to answer negative or coverage questions ('what documentation are we missing'); similarity can only match, it cannot prove absence.
- Putting an LLM judge or reranker in the hot retrieval path when a weighted formula gets there in 0.4ms.
- Chaining multiple vector hits to reach a multi-hop answer — each additional hop is another chance to retrieve the wrong document.
- Bulk-uploading unstructured documents into a chatbot and paying for the tokens before a question is even asked; preprocess into structured chunks instead.
- Enabling full agent mode over the retriever when citations or compliance matter — agent-driven search breaks the chain back to source chunks.
- Letting the agent emit entity-stuffed 'caveman' queries; that behavior is inherited from grep-style code search and BM25-favoring benchmarks, not from what your corpus needs.
- Assuming a code-index-style hybrid retriever generalizes to large repos where files carry many responsibilities — recall collapsed to near zero at 396 files.
- Making infrastructure decisions off published benchmarks that may be measuring the wrong thing rather than first-principles napkin math.

## Notable Outliers

- Standard retrieval benchmarks (BEIR, NanoBEIR) use entity-based 'caveman style' queries that structurally favor BM25, and this is why agents have learned to write bad semantic queries — the eval suite is the root cause, not the retriever. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s))
- Late-interaction search alone closed the Oracle gap to three points on BrowseComp Plus and nearly entirely on Office QA Pro without changing the reasoning model — evidence that a sufficiently good single retriever may matter more than the fusion strategy. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [3:14](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=194s))
- Moving vectors to object storage with a memory cache for the working set is roughly 100x cheaper than DRAM-resident vector databases — a million vectors for a dollar versus ~$100 per million — which changes the cost calculus of keeping a dense leg at all. ([Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [30:32](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1832s))
- The same retrieve-then-fuse pattern applied to tool schemas instead of documents cut tool-context from ~127k tokens to ~1,000 and held selection accuracy above 83% from 10 to 1041 tools, versus 13.6% for loading the full catalog. ([The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [6:38](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=398s))
- A 0.5-billion-parameter model (Qwen 2.5, ~400MB) running on CPU is sufficient for an FAQ assistant and hallucinates less than larger models, provided the retrieved context is well-vetted. ([Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [42:30](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2550s))
- A deterministic regex/structure-based document load beats LLM entity extraction when documents are already structured and interlinked, because it is idempotent and faster — and metadata-derived theme labels beat LLM community summaries on cost, speed, and reproducibility. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [50:27](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3027s))
- The speaker states outright that none of the efficiency or accuracy claims in the workshop were benchmarked. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:54:56](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6896s))

## All Talks

- [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [On AI and Knowledge](../talks/on-ai-and-knowledge.md)
- [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)
- [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

## Speakers

- [Abed Matini](../speakers/abed-matini.md)
- [Ankush Rastogi](../speakers/ankush-rastogi.md)
- [Apoorva Joshi](../speakers/apoorva-joshi.md)
- [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Zach Blumenfeld](../speakers/zach-blumenfeld.md)

