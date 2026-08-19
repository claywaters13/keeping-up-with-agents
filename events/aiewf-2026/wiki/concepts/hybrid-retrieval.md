---
title: "hybrid retrieval"
type: "concept"
slug: "hybrid-retrieval"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 12
---

# hybrid retrieval

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **12** speaker(s)

**Definition:** Combining dense vector search with lexical or structured search and fusing the result sets.

*Also referred to as: hybrid search, vector similarity search, bm25 keyword search, vector search, vector index retrieval, reciprocal rank fusion, late interaction retrieval*

## State of Practice

The field has abandoned the idea that a single retrieval method is sufficient: dense vector search is now treated as one signal among several, always paired with lexical (BM25/grep), metadata filters, or structural traversal, with results fused before they reach the model. The failure mode driving this is specific and repeatable — embeddings blur exact tokens (diagnosis and procedure codes, SKUs, medication names, identifiers buried mid-corpus), so teams report dense recall collapsing to near zero on facts where BM25 holds at 100%, and roughly a 25% miss rate for either method alone versus ~10% fused. Several teams now argue retrieval, not reasoning, is the binding constraint on end-to-end accuracy: models score near-Oracle when handed the right documents and drop by an order of magnitude on the same questions against a noisy corpus. Around the fusion core, the live engineering questions are the shape of the retrieval loop (fixed pipeline versus an agent that issues its own searches), whether a graph or document-tree layer earns its setup cost, and how many candidates to hand back — with speakers converging on tuning top-k per domain against a real eval set rather than shipping a default. Cheap deterministic fusion (weighted score blends, metadata-derived labels, heading-based chunking) is repeatedly reported to beat LLM-in-the-loop reranking and LLM-based extraction on cost, latency, and reproducibility.

## Consensus

### Dense vector similarity alone is not a sufficient retrieval layer; production systems must combine it with lexical/keyword search, metadata filtering, or structural traversal.

Support: **8** talk(s)

> "And you can see how individual methods don't do as well as combined methods, particularly when you apply them to real-world customer scenarios."
>
> — [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [7:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=444s)

Supporting talks: [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)

### The specific failure that forces lexical search into the stack is exact-match retrieval — codes, identifiers, product names, drug names — where semantic similarity returns near-misses that are wrong.

Support: **4** talk(s)

> "if it's a medical chatbot, you need the exact medication. You need don't need something similar or close to it. So, we need to have both both basically uh keyword search and um and the semantic search together."
>
> — [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [30:07](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1807s)

Supporting talks: [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### Retrieval quality, not model choice or reasoning capability, is the binding constraint on answer accuracy and on cost.

Support: **4** talk(s)

> "So we see that the models are extremely capable if they would get the right documents but if you put them into the noisy corpus the performance drops sharply. Meaning that actually the bottleneck here is not the reasoning. It's actually the access to the right knowledge it needs to answer this question."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s)

Supporting talks: [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)

### Vector search is best used to pick entry points, with structure (graph edges, document tree, metadata joins) assembling the rest of the context, rather than chaining more vector hits.

Support: **3** talk(s)

> "it uses the vector search to get the seed nodes where it starts the traversal. And then it uses a graph search pulling the the nearest neighbors and then ranking those by how related they are."
>
> — [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [10:10](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=610s)

Supporting talks: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)

### How many results to return is a domain-specific parameter that must be swept against a test set, not a framework default — more candidates for breadth-style catalogs, fewer where a wrong result carries liability.

Support: **3** talk(s)

> "Run your test set at K equals to three, five, and 10, and then pick the smallest K that meets your accuracy target."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [21:19](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=1279s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)

## Disagreements

### Should retrieval run as a fixed pipeline, or should the agent drive its own multi-round search loop?

| Position A | Position B |
|---|---|
| Fix the pipeline: embed query, run the hybrid retriever, answer. Agent-driven search breaks the citation chain back to source chunks, makes the execution path unpredictable under compliance, and three or four agent loops add 20-30 seconds of latency; one team measured an agentic browse layer adding zero recall over plain hybrid search while being 50% slower, and another found a 0.4ms weighted heuristic beat LLM reranking that cost 2-3 seconds per query.<br>*[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)* | Let the agent search iteratively: agentic retrieval beats single-shot on hard cases across evidence recall and answer completeness, a capped loop (four rounds, parallel searches inside each) with differentiated semantic and lexical tools closes most of the Oracle gap, and as text-to-query capability improves agents should be writing free-form structured queries rather than calling prebuilt shapes.<br>*[How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* |

*Why it matters: It decides whether retrieval effort is a fixed cost you can budget and cite, or a variable latency/quality knob that has to be exposed and monitored. It also determines whether your engineering investment goes into fusion and ranking, or into training and rewarding agent search behavior.*

### Is the right lever on cost sending fewer tokens, or sending more tokens that stay in the prompt cache?

| Position A | Position B |
|---|---|
| Send less. About 90% of spend is input tokens, so the entire game is shrinking what gets shipped: a local hybrid code index cut 83K to 4.9K tokens per question, tool routing cut ~127k of schemas to ~1,000, and speculative markdown memory loading 100k tokens per round is waste that graph traversal removes.<br>*[We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)* | Send more, but keep it stable. Leaving the full history untouched won on cost, latency, and recall simultaneously because 97% of tokens were cache hits — the configuration sending the most tokens was the cheapest to run — while trimming tool outputs made the agent re-retrieve what it already had.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: The two strategies are in direct conflict: aggressive retrieval and pruning invalidate the prefix cache that makes the keep-everything approach cheap. Getting this backwards can move the bill by an order of magnitude either direction, and the answer depends on whether your provider caches and whether the conversation still fits the window.*

### Does a graph layer earn its cost alongside vector search?

| Position A | Position B |
|---|---|
| Yes, for relationship and multi-hop questions. Similarity in vector space is not the same as an actual relationship, so long reasoning chains fail even when every fact is stored; a graph store gives precise, explainable, auditable subgraphs on the same source data, and used as a metadata semantic layer it lets an agent see how hundreds of tables interrelate without any ETL.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)* | Not by default. On real-user evaluations GraphRAG was substantially more expensive to set up and merely tied with plain RAG, so it is not worth adopting unless the data is genuinely highly interconnected.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: Graph adds an ingestion pipeline, a schema, and a second query language to maintain. Adopting it on the wrong corpus buys reproducibility and traversal you never use; skipping it on a highly interconnected corpus leaves multi-hop questions structurally unanswerable.*

### Is heavy reliance on lexical search a permanent architectural component, or a symptom of weak dense retrieval and badly formed agent queries?

| Position A | Position B |
|---|---|
| Permanent. BM25 held 100% recall at 400k tokens where dense retrieval hit 0%, exact-match domains need it outright, and a fixed weighted blend of semantic plus keyword plus recency scores is the cheap, reliable answer.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)* | Symptom. Agents write keyword-stuffed 'caveman style' queries because they were trained on grep-based code exploration and evaluated on benchmarks (BEIR, NanoBEIR) whose entity queries structurally favor BM25; fixing the query formulation and swapping in late-interaction search closes the Oracle gap to three points without changing the reasoning model.<br>*[How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)* |

*Why it matters: One reading says invest in fusion weights and keep BM25 forever; the other says invest in retriever quality and query-formulation training, and expect the lexical crutch to shrink. It also implies current retrieval benchmarks are actively misleading as a basis for picking a retriever.*

## Practical Guidance

**Do:**

- Run dense and keyword search side by side and fuse the results — one team measured each method alone missing ~25% of relevant results and the pair missing ~10%.
- Route exact-token queries (diagnosis and procedure codes, SKUs, medication names) through lexical search or metadata pre-filtering rather than trusting embeddings.
- Chunk on document structure — headings, question/answer units — so each retrieved chunk is citable and a retrieval miss can be traced to a specific chunk.
- Fuse with a cheap deterministic score (e.g. 50% semantic / 30% keyword / 20% recency at 0.4ms) before adding an LLM reranker that costs 2-3 seconds per query.
- Sweep top-k at 3, 5, and 10 on your own test set and ship the smallest K that hits the accuracy target; retrieve more for product catalogs, fewer for medical answers.
- Use vector hits as seed nodes and traverse structure (graph edges, document outline, extracted codes) from there instead of chaining additional vector lookups.
- Instruct the model to write 'one concise sentence describing what it wants to find' rather than 'write a search query', to stop it emitting keyword-stuffed BM25-shaped queries.
- Expose several differentiated retrieval tools (wide semantic search over chunk summaries, lexical/grep) and cap the loop — e.g. four rounds max with parallel searches inside each round.
- Optimize retrieved results for information density per token, not relevance alone, and make retrieval effort a configurable latency-versus-quality knob.
- Instrument per-turn tokens, cache hits, cost, and TTFT for retrieval, and measure savings against a fixed counterfactual baseline instead of estimating them.

**Avoid:**

- Shipping cosine similarity as the entire retrieval layer — the industry's 'get really good at vectors and we're set' phase is over.
- Expecting semantic search to answer negative or coverage questions ('what documentation are we missing') — similarity can only match things that exist.
- Bulk-uploading unstructured documents into a hosted chatbot: you pay tokens before any question is asked, you cannot see how it chunked, and accuracy drops while hallucination rises.
- Resolving multi-hop questions by chaining vector hits — each additional hit is another chance to retrieve the wrong document, and similarity search cannot close a long reasoning chain even when every fact is stored.
- Adopting LLM-generated community summaries (GraphRAG-style) by reflex: costlier, slower, non-reproducible across runs, and one team's real-user eval had it merely tied with plain RAG.
- Setting chunk size, overlap, and top-k by eyeball — 'we didn't actually measure anything, it was just like oh it looks good' was named as the mistake.
- Assuming a hybrid index generalizes across codebases: recall dropped to nearly zero at 396 files once individual files carried many responsibilities.
- Reading BEIR/NanoBEIR-style benchmark results as evidence about your retriever — their entity-based queries structurally advantage BM25.
- Layering an agentic browse step on top of a working hybrid retriever without measuring it — one team found zero added recall and 50% higher latency.
- Reaching for fine-tuning when the failure is retrieval or orchestration; reserve it for behavioral failures or domain-specific performance needs.

## Notable Outliers

- At 400k tokens, dense retrieval gave 0% recall on facts buried in the middle while BM25 still returned them 100% of the time. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [58:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=3538s))
- A weighted 50/30/20 semantic-keyword-recency formula running in 0.4 milliseconds outperformed LLM-based reranking — simple formulas beat complex models most of the time. ([We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s))
- Semantic search structurally cannot prove a negative, so coverage questions ('what documentation are we missing') require structured retrieval, not better embeddings. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [5:14](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=314s))
- Moving vectors from DRAM to object storage with a memory cache makes a million vectors cost about a dollar, versus roughly $100 per million for DRAM-resident vector databases. ([Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [30:32](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1832s))
- A 0.5B-parameter model (Qwen 2.5, ~400MB) running on CPU is sufficient for an FAQ assistant and hallucinates less than larger models, provided the retrieved context is well-vetted. ([Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [42:30](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2550s))
- The same retrieval pattern applied to tool schemas instead of documents holds tool-selection accuracy above 83% from 10 to 1041 tools, where static loading falls to 13.6% at 741 tools. ([The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [4:51](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=291s))

## All Talks

- [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
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
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Omar Solano](../speakers/omar-solano.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Zach Blumenfeld](../speakers/zach-blumenfeld.md)

