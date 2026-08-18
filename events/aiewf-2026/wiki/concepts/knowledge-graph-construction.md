---
title: "knowledge graph construction"
type: "concept"
slug: "knowledge-graph-construction"
tier: "core"
maturity: "consolidating"
talk_count: 16
speaker_count: 17
---

# knowledge graph construction

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **16** talk(s) by **17** speaker(s)

**Definition:** Building and maintaining an explicit graph of entities and relations as a substrate for agent reasoning, retrieval, or enterprise context.

*Also referred to as: knowledge graphs, knowledge graph modeling, knowledge graphs for agents, knowledge graph memory, graph traversal queries, context graph, metadata graph*

## State of Practice

The field has converged on the diagnosis and split on the treatment. Practitioners across tracks now agree that similarity search over embeddings is structurally incapable of multi-hop traversal, aggregation/counting, and negative or coverage questions, and that bigger models and million-token context windows do not fix it — so some explicit structure over entities, relations, and business semantics is required. Where they diverge is construction: one camp builds the graph with schema-guided LLM extraction (agents now write Cypher and entity extractors well enough that graph expertise is no longer a prerequisite), while another argues for deterministic, idempotent loading from existing document structure and metadata, or for keeping data in the warehouse and using the graph only as a metadata/semantic layer over it. The most consistent enterprise finding is that the durable asset is not the graph technology but the modeled tacit knowledge — metric definitions, join logic, reporting conventions, data limitations — which cannot be inferred from the data and must be extracted from data owners. Nearly every production account also insists the graph is a live artifact: runtime execution traces, correction events, eval failures, and closed-won/closed-lost outcomes must flow back into it, because hand-maintained markdown and skills files go stale faster than enterprise definitions change. Notably, several graph advocates volunteered that graphs are often the wrong tool, that their efficiency claims were never benchmarked, and that hybrid vector-plus-graph retrieval — not graph replacement — is what actually ships.

## Consensus

### Vector/similarity retrieval is structurally insufficient for relationship, aggregation, and negative questions — it always returns something, only sees top-k, and cannot traverse or count across the full dataset.

Support: **6** talk(s)

> "Vector search always returns something even when nothing is truly relevant. And the agent only sees the top end chunks of your all data at a time. It cannot aggregate, count, or traverse relationship across all the full data set. So, it estimates."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [18:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1130s)

Supporting talks: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

### A graph is a complement to, not a replacement for, semantic search — production systems seed traversal from vector hits or run hybrid retrieval.

Support: **3** talk(s)

> "I think it would be naive to call it a replacement because most of the people that I see using this will eventually incorporate some sort of hybrid vector retrieval or full text search"
>
> — [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:04:59](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3899s)

Supporting talks: [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)

### Hand-maintained markdown files and skills are not a sufficient context substrate at enterprise scale — they go stale, load speculatively, and burn tokens.

Support: **4** talk(s)

> "we've seen a ton of team that tried to solve this problem using just Markdown files. And the summary is it is part of the solution, but it is not the solution."
>
> — [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [3:31](https://www.youtube.com/watch?v=VGN22pPpb-8&t=211s)

Supporting talks: [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)

### Unconstrained extraction — letting a model infer entities and relationships from raw text or raw tables — produces relationships that do not exist; a domain schema or ontology must bound what gets written.

Support: **4** talk(s)

> "the agent was looking at data, looking at tables, then trying to infer the relationship. That which was not scalable. And it often produce relationship which which is not actually exist in the data."
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [9:11](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=551s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)

### A bigger model or a longer context window does not fix a structure problem; overfilling context degrades answer quality independently of hitting the token limit.

Support: **4** talk(s)

> "The problem here is that the context window is limited, and if you fill the context window too much, the quality of the answer gets degraded, too."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:12](https://www.youtube.com/watch?v=XovaGv4f39A&t=192s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

### The valuable content of the graph is modeled business semantics and tacit process knowledge — metric definitions, reporting conventions, join logic — not the raw data or the graph technology.

Support: **5** talk(s)

> "but our moat here was our understanding of our internal processes the tacet knowledge that you need to to run successful AI and this is true I think no matter how good AI gets how good models get"
>
> — [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [1:09](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=69s)

Supporting talks: [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)

### Graph retrieval's decisive advantage over embedding retrieval is auditability: the returned subgraph or traversal path is inspectable evidence for the answer.

Support: **4** talk(s)

> "graphs are they're accurate. So, they give you very precise information. Explainable because you can look at the graph which got returned. And auditable because now you can actually say these are the this is the context."
>
> — [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [10:52](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=652s)

Supporting talks: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

### The graph must be fed by a runtime feedback loop — execution traces, user corrections, eval failures, and closed outcomes — or it decays into another stale document store.

Support: **5** talk(s)

> "All of these events need to be captured, logged, and used to update your data agent context."
>
> — [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [6:54](https://www.youtube.com/watch?v=B8l81jhvHbI&t=414s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Disagreements

### Should a knowledge graph be built by LLM entity extraction, or by deterministic structural loading (or not built at all)?

| Position A | Position B |
|---|---|
| Use schema-guided LLM extraction as the primary build path — modern agents write Cypher and entity extractors well enough that graph expertise is no longer a prerequisite, and pipelines can construct the graph from raw text files.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)* | Prefer a deterministic, idempotent load derived from existing document structure, links, and metadata — LLM extraction is slower, costlier, and non-reproducible across runs, and re-extraction on every corpus refresh disqualifies graph construction outright for churning data; build the semantic layer and canonical queries first and treat the graph as the last, highest-effort tier.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)* |

*Why it matters: It determines whether your ingest is reproducible and cheap enough to re-run on every data refresh, and whether graph build cost scales with corpus churn or stays fixed. Teams that pick LLM extraction for a fast-changing corpus discover the rebuild cost only after the graph is load-bearing.*

### Should the graph impose one canonical vocabulary across the enterprise, or model the fact that teams legitimately mean different things by the same term?

| Position A | Position B |
|---|---|
| Normalize to a single shared ontology expressed in business language — standardize names and units at extraction, collapse variants with embedding-based entity matching, reuse public ontologies, and treat the historically-conventional answer as the correct one.<br>*[Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)* | Terminology divergence across teams is a feature of how humans work, not a defect to be schema'd away; two teams can compute the same metric differently and both be right, so the system should route to the right definition based on who is asking rather than pick a winner — and what counts as public or private depends on the room, not the data.<br>*[How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)* |

*Why it matters: It decides whether normalization happens once at ingest (one node per concept) or per-request at query time (identity-conditioned views over the same graph), and whether 'correct' is a global property of the answer or relative to the requester. Getting this wrong shows up as an agent that is factually right and organizationally useless.*

### Should source data be materialized into the graph, or should the graph hold only metadata pointing at systems of record?

| Position A | Position B |
|---|---|
| Do not ETL into the graph for most agent use cases — pull metadata only and use the graph as a semantic layer over the warehouse, because continuous sync at terabyte scale, custom ETL, and security policies that forbid cross-system data movement make copying untenable; ETL is justified only for recursive-join performance, graph algorithms, embeddings, or clustering.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)* | Materialize: ingest once and reason many times, consolidating multiple systems of record into a single graph and storing primitives rather than answers, because owned context compounds while rented or federated context decays and re-query costs recur on every access.<br>*[Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* |

*Why it matters: Materializing unlocks graph algorithms, embeddings, and traversal performance but takes on sync and compliance burden; the metadata-only path stays cheap and secure but forecloses anything that needs the data resident in the graph. The break-even is empirical — one speaker put it at roughly 15,000 entities or queries for a scraping pipeline.*

### Should the graph constrain the agent's search space, or serve as an open substrate the agent queries freely?

| Position A | Position B |
|---|---|
| Treat the graph as a control plane: it dictates which paths the agent may take and which hypotheses it may evaluate — every edge is a hypothesis and the agent does not go outside it — with ontology reasoners validating results before any side effect is committed.<br>*[Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)* | Agents are now capable enough to be trusted with free-form querying: entity nodes that used to be required in the data model can often be omitted, and as text-to-Cypher and skills improve, agents will increasingly write their own queries rather than call prebuilt shape scripts.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* |

*Why it matters: It sets how much modeling effort is required up front: a control-plane graph needs every valid investigation path encoded, while an open substrate pushes correctness onto model capability and eval. The constrained design bounds hallucinated reasoning paths; the open design gets cheaper every model generation.*

## Practical Guidance

**Do:**

- Give the extractor a domain schema plus explicit ontology instructions for naming and unit standardization, then run a separate embedding-based entity-matching pass — prompt-level standardization alone is not reliable, and hand-curated mapping requires knowing every entity in advance.
- Seed traversal from vector search, then walk the graph and rank neighbors by relatedness to assemble context, rather than choosing between vector and graph retrieval.
- Use one generic containment relationship name across hierarchy levels instead of per-level names; hundreds of distinct relationship types stop fitting the model's context window and degrade Cypher generation.
- Prefer a deterministic, regex/structure-based loader when documents already carry inherent structure and interlinking — it is idempotent and faster than LLM extraction.
- Build the semantic layer and canonical query tiers first (roughly 80% of enterprise data-agent problems) before attempting the database graph, which is the highest-effort and hardest-to-maintain tier.
- Engage data owners directly to capture field semantics, join logic, data limitations, safeguards, and security trimming — none of it is inferable from the data itself.
- Store a graph query alongside each eval question and compute ground truth against the live graph at eval time, since structured data changes constantly and frozen expected answers rot.
- Route eval failures back into the data model, domain rules, and schema descriptions — treat evals as a data-modeling feedback loop, not a scorecard.
- Ingest once and reason many times: pay for expensive understanding at ingest, store primitives (moments, entities, appearances) rather than pre-computed answers, and ground every claim to a specific source location.
- Pull deterministic work out of the agentic system entirely — detect signals with statistical methods and hand the agent an investigation task, not an identification task.
- Keep end-to-end judgment in exactly one agent; sub-agents may return investigation results but never reasoning or judgment, because context is lost at every handoff.
- Layer validation: Pydantic type checks at the door, ontology/OWL semantic checks at the ledger, and keep agents side-effect-free until validation passes.
- Adopt existing public ontologies (schema.org, FOAF, Dublin Core) rather than inventing a domain vocabulary from scratch.
- Serve the graph into tools users already have via MCP instead of building another chat UI — the interface is not defensible, the model is.

**Avoid:**

- Free-form subject-predicate-object triple extraction with no schema — the resulting graph is one you 'wouldn't get very far with'.
- ETLing warehouse data into a graph by default; continuous sync at terabyte scale, custom ETL, and security policies that forbid cross-system movement usually outweigh the benefit unless you specifically need recursive-join performance, graph algorithms, embeddings, or clustering.
- LLM-generated community summaries when document metadata already implies the themes — they cost more, run slower, and return different results across runs; reserve LLM assistance for corpora with poorly labeled titles and links.
- Bucketing documents by domain when relationships between documents are dense — the supervisor skips domains that look irrelevant at first glance; distribute in no particular order and balance only for bucket size.
- Treating the graph as a lookup layer; if it does not constrain which paths and hypotheses the agent can pursue, you have not bought navigation, only storage.
- Storing agent memory as markdown files once the corpus exceeds the model's context window — everything gets loaded speculatively, at 100k+ tokens per round.
- Exposing memory mutation through MCP tools without guardrails; the agent is one call away from invoking forget and wiping its own memory.
- Recomputing the whole knowledge graph every time the underlying corpus is replaced — for frequently refreshed collections this alone disqualifies the approach.
- Weighting all knowledge bases equally; rank sources of truth and consult cleanest-first, or the agent cannot tell which table, column, or definition is authoritative.
- Conflating fit score and intent score in a GTM context graph — it sends the wrong message to the wrong person, and if everything reads as hot, reps stop trusting the system.
- Deleting nothing: contacts and records failing ICP criteria should be removed, not retained as noise in the graph.
- Adding more knowledge bases and MCP servers as the remedy for bad answers — the failure is structural, not a coverage gap.

## Notable Outliers

- A Neo4j speaker demoing an entire lakehouse graph architecture stated outright that none of the efficiency or accuracy claims in the workshop had been benchmarked. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:54:56](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6896s))
- Graph-based subgraph retrieval cut tool calls for code search by 40% on a .NET codebase, surfacing intermediate nodes that neither vector search nor symbol/reference lookups could reach. ([A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [10:28](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=628s))
- Two years ago the data model would have needed a dedicated entity node; agents are now smart enough that you often don't need it — with life-sciences ontologies as the counterexample. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:07:53](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=4073s))
- Hallucination is a feature of LLMs rather than a defect, which is why the fix is a neuro-symbolic reasoner over a formal ontology rather than better prompting. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s))
- Whoever controls the enterprise's vocabulary through their ontology becomes the linguistic foundation and is locked in — terms like 'skills' and 'MCPs' are being contested in real time right now. ([How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [15:20](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=920s))
- A 100-person factory with no data scientists built a 39-agent company brain for ~$30k against a $230k agency quote, with a values file derived from three generations of a Jain family business running as production guardrails. ([The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [8:28](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=508s))
- Self-built scraping to own context reached break-even against rented context-as-a-service at just over 15,000 entities or queries, assuming roughly a week and $5,000 of setup. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [18:59](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1139s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)
- [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)
- [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)
- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)
- [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Abhilash Asokan](../speakers/abhilash-asokan.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Emil Eifrem](../speakers/emil-eifrem.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Ishita Daga](../speakers/ishita-daga.md)
- [James Le](../speakers/james-le.md)
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Mike Phipps](../speakers/mike-phipps.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Sajjan Kanukolanu](../speakers/sajjan-kanukolanu.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)
- [Tim Ainge](../speakers/tim-ainge.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)
- [Zach Blumenfeld](../speakers/zach-blumenfeld.md)

