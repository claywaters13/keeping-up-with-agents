---
title: "graph rag"
type: "concept"
slug: "graph-rag"
tier: "supporting"
maturity: "contested"
talk_count: 7
speaker_count: 7
---

# graph rag

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **7** talk(s) by **7** speaker(s)

**Definition:** Retrieval that traverses a knowledge graph — communities, paths, subgraphs — instead of or alongside flat vector lookup.

*Also referred to as: graphrag, hybrid vector-graph retrieval, personalized pagerank, community detection, global versus local search, shortest path retrieval, subgraph pattern matching*

## State of Practice

The field has stopped arguing about whether graphs help retrieval and started arguing about how much graph you actually need to materialize. The agreed technical core is narrow and structural: top-k vector search can only match similar things, so it cannot answer multi-hop, aggregation/count, or negative-coverage questions ('what documentation are we missing'), and it silently returns a sample the model then presents as fact. The dominant production pattern is hybrid — vector or full-text search to pick seed nodes, then traversal with relatedness ranking to assemble the subgraph — not graph as a replacement for embeddings. What has shifted in the last year is the build cost: speakers report that agent-written Cypher (with CLI access and Cypher/GDS skills) is dramatically better than the text-to-Cypher of six to twelve months ago, so graph expertise is no longer the barrier; the extraction pipeline is. That extraction step is where the disagreement now lives, with credible practitioners variously recommending schema-constrained LLM extraction, fully deterministic structure-based loading, metadata-only graphs over a warehouse, event-log projections with no extraction at all, and parallel cache-augmented generation instead of a graph. Notably, one of the most detailed graph workshops at the conference (from Neo4j) explicitly disclosed that none of its efficiency or accuracy claims had been benchmarked.

## Consensus

### Vector/semantic retrieval structurally cannot answer multi-hop, aggregation/counting, or negative-coverage questions, because it only returns top-k similar chunks and therefore estimates rather than computes.

Support: **5** talk(s)

> "Vector search always returns something even when nothing is truly relevant. And the agent only sees the top end chunks of your all data at a time. It cannot aggregate, count, or traverse relationship across all the full data set. So, it estimates."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [18:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1130s)

Supporting talks: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

### Graph retrieval is a complement to vector search, not a replacement: seed with embeddings or full-text, then traverse and rank by relatedness.

Support: **3** talk(s)

> "I think it would be naive to call it a replacement because most of the people that I see using this will eventually incorporate some sort of hybrid vector retrieval or full text search"
>
> — [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:04:59](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3899s)

Supporting talks: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)

### Graph expertise is no longer a prerequisite for adopting graph retrieval, because current models write Cypher and graph-manipulating code better than most practitioners.

Support: **4** talk(s)

> "If you're not a graph expert, guess what? Claude is. Claude can write Cypher better than I can."
>
> — [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [11:33](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=693s)

Supporting talks: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)

### The operational payoff of graph retrieval is auditability: the returned subgraph or executed query is inspectable evidence for the answer, whereas chained vector hits give you a sample you cannot verify.

Support: **3** talk(s)

> "graphs are they're accurate. So, they give you very precise information. Explainable because you can look at the graph which got returned. And auditable because now you can actually say these are the this is the context."
>
> — [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [10:52](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=652s)

Supporting talks: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)

### The LLM-driven extraction/summarization stage is the expensive and fragile part of a GraphRAG pipeline — slow, costly, and non-reproducible across runs — not the querying.

Support: **4** talk(s)

> "then obviously it costs more money, it's slower, and the you if you run it twice, it might not return the same thing. So there's trade-offs between uh each way of doing it."
>
> — [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:33:48](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=5628s)

Supporting talks: [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)

## Disagreements

### Should you materialize your content into a graph store at all, or keep the graph as a thin layer (or skip it entirely) over data that lives elsewhere?

| Position A | Position B |
|---|---|
| Build and populate a real graph of your content and traverse it — write agent actions into the graph as work happens and retrieve by traversal, because file/markdown memory and vector stores fail past the point where data exceeds the context window.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)* | Don't ETL data into a graph for most agent use cases — use the graph only as a metadata/semantic layer over the warehouse, use whatever store you already have (Postgres is fine), or replace the graph entirely with parallel cache-augmented generation; ETL into a graph is justified only for recursive-join performance, graph algorithms, embeddings, or clustering.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* |

*Why it matters: This decides whether you take on a continuous-sync and ETL burden across terabyte-scale (and often security-siloed) data, or ship with metadata plus query-time joins. It also determines whether 'GraphRAG' is a database procurement decision or just a representation choice inside your existing stack.*

### Should the graph be built by LLM entity/relationship extraction, or derived deterministically from structure that already exists?

| Position A | Position B |
|---|---|
| Use LLM extraction, but only with scaffolding: give the extractor a domain schema plus ontology instructions for naming and unit standardization, then resolve entities with embedding-based matching — or let a managed pipeline build the graph from raw text so you don't hand-construct it.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)* | Skip LLM extraction where you can: a deterministic regex/structure-based load is idempotent and faster when documents are already structured and interlinked, and a structured event log used directly as memory — with no fact or entity extraction — performed well on LongMemEval.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* |

*Why it matters: Extraction determines reproducibility and cost of every rebuild: LLM pipelines give different graphs on reruns and price scales with corpus size, while deterministic loads are idempotent but only work where structure already exists. It also sets whether your graph can be rebuilt on a schedule or must be treated as expensive, semi-permanent state.*

### How should a graph stay current when the underlying corpus changes frequently?

| Position A | Position B |
|---|---|
| Batch-extracted knowledge graphs disqualify themselves for fast-changing corpora — recomputing the graph on every data replacement is computationally expensive and slow, so use a different strategy (parallel KV-cached context buckets) instead.<br>*[When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* | Never recompute: write the graph incrementally as the agent acts, or derive graph state as a projection of an append-only immutable event log, which also gives replays, rollbacks, and forks and survives mid-run failures.<br>*[Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* |

*Why it matters: If graphs must be batch-rebuilt, GraphRAG is limited to slow-moving reference corpora; if graph state can be appended incrementally, it becomes viable as live agent memory. The answer decides whether 'the corpus changes often' is a disqualifier or a non-issue.*

## Practical Guidance

**Do:**

- Give the extractor a domain schema plus explicit ontology instructions for naming and unit standardization — free-form subject-predicate-object triples produce a graph you won't get far with
- Add a separate embedding-based entity-matching step after extraction rather than trusting prompt-level standardization, since it doesn't require knowing all entities in advance
- Use vector search to select seed nodes, then traverse nearest neighbors and rank by relatedness to assemble context
- Route aggregation, counting, and 'what's missing' questions to a graph query so the query engine computes a verified result instead of the model estimating over top-k chunks (this also cuts output tokens)
- Keep warehouse data in the warehouse and pull only metadata into the graph as a semantic layer; reserve ETL-into-graph for recursive-join performance, graph algorithms, graph embeddings, or clustering
- Use a single generic containment relationship name across hierarchy levels instead of per-level names, to keep Cypher simple
- Prefer a deterministic regex/structure-based document load when documents already have inherent structure and interlinking — it's idempotent and faster
- Derive community/theme labels from document metadata and structure where labels are decent, and reach for LLM summarization only when titles and link names are poorly labeled
- Use Leiden rather than Louvain for community detection
- Give the agent CLI access plus Cypher/GDS skills rather than relying on generic text-to-Cypher
- Instrument the win: one .NET codebase evaluation saw a 40% reduction in tool calls for code search using subgraph/shortest-path retrieval

**Avoid:**

- Rushing into GraphRAG or a graph database expecting an instant payoff — many journeys end in the valley of despair
- Treating vector similarity as if it were an actual relationship; long multi-hop chains fail on similarity search even when every needed fact is stored
- Hundreds of distinct relationship types in a production data model — they blow up the context window and degrade Cypher generation
- Speculatively loading markdown-file memory into every round (100k+ tokens) once your data exceeds the 1M-token context window
- Exposing memory over MCP tools that include a forget command — the agent is one call away from wiping its own memory
- Recomputing the whole knowledge graph every time the corpus is replaced
- Bucketing documents by domain when splitting across parallel caches — with dense inter-document relationships the supervisor skips domains that look irrelevant at first glance
- Letting the model pull Cypher patterns from years-old Stack Overflow answers, which yields outdated bad Cypher
- Assuming the entity node your data model needed two years ago is still required — modern agents can often join without it (life sciences ontologies excepted)

## Notable Outliers

- The choice of graph database is unimportant — 'five companies trying to sell you a graph DB, and you can just use Postgres' — what matters is having a dependency-graph representation of the process at all. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [15:17](https://www.youtube.com/watch?v=l0FLhNqBOic&t=917s))
- Extracting the right context out of a large knowledge graph is a distinct and harder problem than generating good output from context, and is best solved with RL-trained custom traversal tools (including entity-resolution tools that disambiguate the many Mikes at every client). ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [17:51](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1071s))
- A structured event log used directly as memory — embed the query, grab neighboring messages, no semantic ingestion, no fact extraction, no entity extraction — did pretty well on LongMemEval. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [8:17](https://www.youtube.com/watch?v=khVX_BUnEwU&t=497s))
- Parallel cache-augmented generation over unordered document buckets builds knowledge significantly faster than GraphRAG while answering more accurately than simple RAG. ([When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [4:37](https://www.youtube.com/watch?v=XovaGv4f39A&t=277s))
- The speaker explicitly disclosed that none of the efficiency or accuracy claims in the entire graph workshop had been benchmarked. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:54:56](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6896s))
- Shortest-path traversal surfaces intermediate nodes that are unreachable by vector search or symbol/reference lookup — Miranda v. Arizona is found for Canvas v. Sheba purely through the citation graph, with no direct citation between them. ([A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [8:56](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=536s))
- AI models write shared-state/blackboard-style agent code better than LLM-agent-style code, because decades of that architectural discussion sit in the training data while LLM agent patterns are only about three years old. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [14:54](https://www.youtube.com/watch?v=khVX_BUnEwU&t=894s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)
- [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)
- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

## Speakers

- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Tim Ainge](../speakers/tim-ainge.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)
- [Zach Blumenfeld](../speakers/zach-blumenfeld.md)

