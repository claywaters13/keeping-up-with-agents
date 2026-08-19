---
title: "knowledge graph construction"
type: "concept"
slug: "knowledge-graph-construction"
tier: "core"
maturity: "contested"
talk_count: 17
speaker_count: 18
---

# knowledge graph construction

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **17** talk(s) by **18** speaker(s)

**Definition:** Building and maintaining an explicit graph of entities and relations as a substrate for agent reasoning, retrieval, or enterprise context.

*Also referred to as: knowledge graphs, knowledge graph modeling, knowledge graphs for agents, knowledge graph memory, graph traversal queries, context graph, metadata graph*

## State of Practice

The field has stopped arguing about whether graphs help and moved to arguing about how much of one to build and who builds it. The agreed technical core is narrow and specific: vector similarity returns candidates, not relationships, so it cannot resolve multi-hop chains, cannot aggregate or count over a corpus, and structurally cannot answer negative or coverage questions ('what documentation are we missing') — those need traversal or a query engine that computes rather than samples. The dominant production pattern is hybrid: vector or full-text search picks seed nodes, graph traversal expands and ranks by relatedness, and the returned subgraph doubles as the audit trail. Construction has split into two camps — LLM entity extraction constrained by a hand-authored domain schema and ontology instructions, versus deterministic structure-based ingest (document trees, warehouse metadata) that is idempotent and reproducible — with several speakers explicitly warning that free-form subject-predicate-object extraction and agents inferring relationships off raw tables both produce graphs full of edges that do not exist. A second split runs between materializing data into a graph store and using the graph purely as a metadata semantic layer over data that stays in the warehouse, justified by continuous-sync cost, ETL complexity, and security posture. The consistently reported hard part is neither the database nor the model: it is capturing the tacit organizational knowledge — field semantics, join logic, which source is authoritative, how a metric has historically been computed — and keeping it fed by corrections, execution traces, and eval failures, because that curated model, not the UI or the agent, is what several teams identified as their actual moat.

## Consensus

### Vector similarity retrieval structurally cannot answer multi-hop, aggregation/counting, or coverage/negative questions, no matter how good the embeddings are — it returns similar things, and always returns something.

Support: **6** talk(s)

> "it's sometimes impossible to get to the answer even though you have all the facts because those large multi-hop reasoning chains don't work on similarity searches."
>
> — [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [8:33](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=513s)

Supporting talks: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

### Markdown files, skills, and hand-maintained documents are not a viable knowledge substrate at enterprise scale — they rot, they are loaded speculatively, and they stop working once the corpus exceeds the context window.

Support: **4** talk(s)

> "we've seen a ton of team that tried to solve this problem using just Markdown files. And the summary is it is part of the solution, but it is not the solution."
>
> — [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [3:31](https://www.youtube.com/watch?v=VGN22pPpb-8&t=211s)

Supporting talks: [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)

### An explicit, human-authored schema or ontology must constrain graph construction; letting the model discover the entity and relation structure from raw data or free-form triple extraction produces relationships that do not exist.

Support: **5** talk(s)

> "the agent was looking at data, looking at tables, then trying to infer the relationship. That which was not scalable. And it often produce relationship which which is not actually exist in the data."
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [9:11](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=551s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)

### The graph is not a replacement for semantic search; production retrieval is hybrid, typically vector search to select seed nodes followed by graph traversal and relatedness ranking.

Support: **4** talk(s)

> "I think it would be naive to call it a replacement because most of the people that I see using this will eventually incorporate some sort of hybrid vector retrieval or full text search"
>
> — [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:04:59](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3899s)

Supporting talks: [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)

### A knowledge graph is a live system, not an artifact: corrections, closed-won/closed-lost outcomes, eval failures, and agent execution traces must be logged and written back, or the graph drifts out of date and the agents degrade.

Support: **5** talk(s)

> "All of these events need to be captured, logged, and used to update your data agent context."
>
> — [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [6:54](https://www.youtube.com/watch?v=B8l81jhvHbI&t=414s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

### The durable, defensible asset is the modeled tacit knowledge — process semantics, vocabulary, which source is authoritative — not the model, the agent, or the chat UI.

Support: **4** talk(s)

> "but our moat here was our understanding of our internal processes the tacet knowledge that you need to to run successful AI and this is true I think no matter how good AI gets how good models get"
>
> — [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [1:09](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=69s)

Supporting talks: [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)

### Graph construction is high-effort and often not the right first move; cheaper layers (semantic layer, canonical queries, metadata-only graphs, plain caching) should be exhausted first.

Support: **4** talk(s)

> "Graphs have always been a powerful foundation of computer science and they look beautiful. But sometimes they're genuinely not the right tool for the job."
>
> — [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [0:00](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=0s)

Supporting talks: [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

## Disagreements

### Should the graph hold the data, or only metadata about data that stays where it lives?

| Position A | Position B |
|---|---|
| Materialize into a graph store: ETL or write records, entities, and agent actions into the graph and make it the retrieval and memory substrate the agent traverses.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)* | Do not ETL into the graph for most agent use cases; pull only metadata and use the graph as a semantic layer over data that stays in the warehouse, because continuous sync at terabyte scale, custom ETL, and security posture make movement impractical — ETL is justified only for recursive-join performance, graph algorithms, embeddings, or clustering.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)* |

*Why it matters: This decides whether you own an ingestion pipeline with a continuous-sync and reprocessing burden or a much thinner metadata mapping, and it determines whether the graph can answer questions the source systems cannot.*

### Should an LLM extract the entities and relations, or should the graph be built deterministically from existing structure?

| Position A | Position B |
|---|---|
| Use LLM extraction, constrained by a domain schema and ontology instructions, plus embedding-based entity resolution afterward; modern models can write the Cypher and the extractors for you, so graph expertise is not a prerequisite.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)* | Prefer a deterministic, structure-based load when documents already carry structure and interlinking, and derive themes from document metadata rather than LLM community summaries — LLM construction costs more, runs slower, and is not reproducible across runs.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* |

*Why it matters: Non-idempotent construction means every re-ingest can change what the agent believes, which breaks eval reproducibility and makes graph refresh expensive enough that some teams abandon GraphRAG entirely for frequently replaced corpora.*

### Does agent capability reduce how much explicit structure the graph needs to carry?

| Position A | Position B |
|---|---|
| Yes — agents are now smart enough that entity nodes previously required in the data model can often be omitted, structured and unstructured subgraphs can be joined at query time via extracted codes rather than explicit links, and agents increasingly write free-form Cypher instead of calling prebuilt shape scripts.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)* | No — the formal layer is exactly what keeps a probabilistic model honest: adopt real ontologies, validate agent output against OWL constraints after type checking, and encode business intent, source trust, and mapping in a shared substrate rather than in per-agent code and prompts.<br>*[Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)* |

*Why it matters: If model capability substitutes for schema, graph investment shrinks to metadata and the model absorbs the mapping work; if it does not, every capability jump still leaves you owning an ontology and a validator.*

### Is the knowledge graph a retrieval substrate the agent queries, or a control plane that bounds what the agent may do?

| Position A | Position B |
|---|---|
| Control plane: the graph dictates which paths the agent can take and which hypotheses it may evaluate — every edge is a hypothesis and the agent does not go outside it — and an ontology reasoner validates results before any side effects are committed.<br>*[Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)* | Context substrate: the graph exists to assemble better, cheaper, more auditable context for an otherwise free-running agent — seed-and-traverse memory, subgraph retrieval that cut tool calls, a navigable structure over the corpus.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)* |

*Why it matters: A control-plane graph must be complete and correct enough to exclude valid reasoning paths, a far higher modeling bar than a retrieval graph, and it changes whether graph gaps show up as missed answers or as an agent that silently cannot investigate.*

## Practical Guidance

**Do:**

- Give the extractor an explicit domain schema plus ontology instructions covering naming and unit standardization, then run a separate embedding-based entity-matching step — prompt-level standardization alone is not reliable.
- Retrieve by seeding with vector search and then traversing the graph with relatedness ranking, rather than choosing one or the other.
- Use one generic containment relationship name across hierarchy levels; hundreds of distinct relationship types become unmanageable in the model's context window and degrade Cypher generation.
- Keep warehouse data in the warehouse and pull only metadata into the graph unless you specifically need recursive-join performance, graph algorithms, graph embeddings, or clustering.
- Build the semantic layer and canonical queries first — they cover roughly 80% of enterprise data-agent problems — and treat the database graph as the harder 20%.
- Ground every claim to its source (a timestamp in the video, the returned subgraph) so answers are explainable and auditable.
- Compute eval ground truth by storing a graph query per question and running it against the live graph at eval time, since the underlying structured data keeps changing.
- Feed corrections, closed-won/closed-lost outcomes, and agent execution traces back into the graph, and score data-source trustworthiness both top-down by curation and bottom-up by what traces show actually worked.
- Give the agent a fixed reference list of tags/entities and instruct it to be reluctant to invent new ones; stamp each enriched record with a timestamp so repeat passes only touch unprocessed items.
- Reuse existing public ontologies (schema.org, FOAF, Dublin Core) instead of authoring one from scratch.
- Validate types with Pydantic at the door and semantics with the ontology at the ledger, keeping agents side-effect-free until validation passes.
- Engage data owners directly for field semantics, join logic, data limitations, and security trimming — it cannot be inferred from the data.
- Mask PII, classify sensitivity, and apply per-user entitlements during curation, because AI makes theoretically-accessible data practically accessible.

**Avoid:**

- Free-form subject-predicate-object triple extraction with no schema — the resulting graph is not useful.
- Letting the agent infer entity and KPI relationships from raw tables at query time; it does not scale and invents relationships absent from the data.
- Retrospective hand-curated entity mapping, which only works if you already know every entity in advance.
- Rebuilding the whole knowledge graph every time the corpus is replaced — GraphRAG fits slow-changing collections, not frequently replaced ones.
- LLM-generated community summaries when document metadata already yields theme labels: more cost, more latency, and different output on every run.
- Treating the graph as a replacement for semantic or full-text search.
- Weighting all knowledge bases equally instead of ranking sources of truth cleanest-first.
- Exposing destructive memory operations (a forget command) as MCP tools the agent can call on itself.
- Forcing one enterprise-wide vocabulary on teams that legitimately call the same thing customers, clients, billing entities, and org IDs.
- Presenting graph efficiency or accuracy claims as measured when they have not been benchmarked.

## Notable Outliers

- Agents have gotten capable enough that entity nodes which two years ago were mandatory in the data model can now often be dropped — with life sciences ontologies as the counterexample. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:07:53](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=4073s))
- Delivered a full workshop of graph-vs-alternative efficiency and accuracy claims while stating that none of it had been benchmarked. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:54:56](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6896s))
- Graph expertise is no longer a prerequisite for graph memory, because the model writes better Cypher than the practitioner does. ([CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [11:33](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=693s))
- Parallel KV-cache buckets over the raw documents beat GraphRAG on build speed and simple RAG on accuracy — and documents should be distributed across buckets in no particular order, because domain-organized buckets cause the supervisor to skip domains that look irrelevant. ([When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:50](https://www.youtube.com/watch?v=XovaGv4f39A&t=230s))
- Owning the enterprise's ontology is a lock-in strategy: users adopt your language, and whoever becomes the linguistic foundation becomes the platform everything else builds on. ([How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [15:20](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=920s))
- Neither semantic layers nor agent memory solves the preference problem — two teams can compute the same metric differently and both be correct, so the graph must route to a definition based on who is asking, which is still unsolved. ([Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [11:03](https://www.youtube.com/watch?v=B8l81jhvHbI&t=663s))
- Hallucination is a feature of LLMs, not a defect, which is why the fix is a symbolic ontology reasoner around the model rather than a better model. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s))
- A hundred-person factory with no data scientists built a 39-agent knowledge system for about $30,000 against a $230,000 agency quote, with zero training cost — the expensive part was teaching the company to remember itself. ([The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [8:28](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=508s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)
- [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)
- [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md)
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
- [Ben Holmes](../speakers/ben-holmes.md)
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

