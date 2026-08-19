---
title: "agentic retrieval"
type: "concept"
slug: "agentic-retrieval"
tier: "supporting"
maturity: "contested"
talk_count: 12
speaker_count: 15
---

# agentic retrieval

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **12** talk(s) by **15** speaker(s)

**Definition:** Letting the model plan and iterate its own searches — issuing queries, reading results, and re-querying — instead of a fixed one-shot retrieval step.

*Also referred to as: agentic rag, agentic search, agentic web retrieval, agentic query generation, web search for agents, llm planning vs retrieval, search grounding*

## State of Practice

The field has converged on the negative result — pure vector similarity is not a retrieval strategy — and is now arguing about what replaces it. Speakers reported hard numbers on both sides: Mixedbread measured a 84-point gap between oracle context and Codex's default tools on BrowseComp Plus, closing it to three points by swapping the search layer alone without touching the reasoning model; Phaidra measured baseline LLM correctness falling from 80% to 30% as an entity set grew from 64 to 460,000 items. The practical architecture that recurs is layered: a cheap wide sweep (semantic search over chunk summaries, a document outline, or metadata) to pick seeds, then a structured second hop (graph traversal, set operations, hierarchy paths) to assemble the actual answer, with the loop explicitly bounded — four rounds at Mixedbread, two or three steps at Phaidra, a user-facing effort knob at Microsoft. Lexical retrieval refused to die: Towards AI measured BM25 holding 100% recall at 400k tokens where dense retrieval hit 0%, and Mixedbread argued the reverse problem — that BEIR-style benchmarks train agents to emit 'caveman style' keyword queries that make good semantic search unusable. The loudest unresolved question is how much of the search the model should perform itself: several teams reported that giving the agent more freedom (bash browsing, unbounded loops, per-shard LLM enumeration) cost latency, tokens, or accuracy, while Neo4j and Red Hat argued agents are now good enough to write their own Cypher and traverse document structure directly.

## Consensus

### Vector/semantic similarity alone is structurally insufficient for retrieval; production systems must combine it with lexical, structural, or relational methods.

Support: **6** talk(s)

> "And you can see how individual methods don't do as well as combined methods, particularly when you apply them to real-world customer scenarios."
>
> — [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [7:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=444s)

Supporting talks: [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)

### The binding constraint on knowledge tasks is now retrieval and context construction, not model reasoning capability.

Support: **5** talk(s)

> "So we see that the models are extremely capable if they would get the right documents but if you put them into the noisy corpus the performance drops sharply. Meaning that actually the bottleneck here is not the reasoning. It's actually the access to the right knowledge it needs to answer this question."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s)

Supporting talks: [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)

### The search loop must be bounded and tiered by query difficulty — single-shot for easy cases, a small fixed number of iterations for hard ones — rather than left open-ended.

Support: **4** talk(s)

> "for easy cases, like, you know, quick single-shot retrieval is great, but for more sophisticated cases, you do want a system that can reflect on on what's in the data set and decide whether or not we've satisfied the information need as stated in the input before we come back with results"
>
> — [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [8:36](https://www.youtube.com/watch?v=RGSFUqzqErE&t=516s)

Supporting talks: [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)

### Operations that must be exact and reproducible — counting, deduplication, set logic, ground-truth computation — belong in deterministic code, not in the model's scan of the data.

Support: **4** talk(s)

> "If your data has structure, call it a hierarchy, graph, or a schema, a language model scanning it token by token is definitely the wrong tool."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:04](https://www.youtube.com/watch?v=EUsPvBeIx70&t=844s)

Supporting talks: [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

### Retrieval must be engineered as a cost and token-density problem, not only a relevance problem — what you return per token, and how often you re-query, dominates the bill.

Support: **4** talk(s)

> "we carefully evaluate this system to make sure that we give you the most information dense answer that has the fewest tokens uh so that you you know, the the your consumption of tokens has a high value when it comes to all retrieval tasks"
>
> — [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [12:36](https://www.youtube.com/watch?v=RGSFUqzqErE&t=756s)

Supporting talks: [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)

## Disagreements

### Should the agent perform its own searches, or should it only plan and then hand execution to deterministic retrieval code?

| Position A | Position B |
|---|---|
| Let the agent drive: modern models can write free-form Cypher, traverse a document outline, and iterate their way to the answer, so prebuilt query shapes and rigid pipelines are becoming unnecessary scaffolding.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)* | The model plans but does not search: it parses intent and decides where to look, then a deterministic resolver (set operations, hierarchy paths, a trained search tool with capped rounds) executes, because agent-driven search degrades in accuracy, latency, and cost at scale.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: It decides whether you invest in query-generation prompting and skills or in a hardened retrieval service with a narrow LLM interface — and Phaidra's numbers say the wrong choice costs 300x in tokens and 70 points of correctness at large entity counts.*

### Does a graph layer earn its cost for agentic retrieval, or is hybrid vector plus keyword search enough?

| Position A | Position B |
|---|---|
| Graphs are worth it: multi-hop and coverage questions are unreachable by similarity search, and graph seeding plus traversal produced measurable wins (40% fewer tool calls in a .NET codebase; precise answers where the same data in a vector store failed).<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)* | GraphRAG cost more to set up and tied with plain RAG on real-user evaluations, so it is not worth adopting unless your data is genuinely highly interconnected.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: A graph layer is a multi-week ingest, ontology, and schema-maintenance commitment; adopting it on faith and getting a tie is the 'valley of despair' failure the graph advocates themselves warn about.*

### Once context windows reach a million tokens, should you keep loading everything, or is structured retrieval mandatory?

| Position A | Position B |
|---|---|
| Keep the full history untouched: with 97% cache hit rates it was simultaneously cheaper, faster, and higher-recall than every compaction preset, and distinctive facts were still recalled at 800k tokens.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* | Speculative loading is the failure mode: markdown-file memory burns 100k tokens per round and stops working past the 1M window, and a validation pass that cost 116M tokens fell to 390k once retrieval was structured.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)* |

*Why it matters: The two camps are measuring different regimes — a cached conversational context versus a corpus that exceeds any window — and conflating them leads teams either to build retrieval they do not need or to hit a hard wall when their data outgrows the window.*

### Should the retrieval index be built by LLM extraction at ingest, or derived deterministically from structure the documents already have?

| Position A | Position B |
|---|---|
| Use LLM extraction, but constrain it with a domain schema and ontology instructions, then reconcile entities with embedding-based matching; models can also write the extractors themselves.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* | Prefer a deterministic, structure-based load — regex/document-tree parsing, layout models, metadata-derived theme labels — because it is idempotent, faster, cheaper, and reproducible across runs, and LLM community summaries cost more for non-reproducible output.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)* |

*Why it matters: Determines whether your index can be rebuilt identically after a model deprecation — Red Hat flagged that a 5.1-to-5.2 model version change breaks consistent structured output across thousands of PDFs.*

## Practical Guidance

**Do:**

- Cap the search loop at a fixed number of rounds (Mixedbread used four) but allow parallel searches within each round.
- Instruct the model to write 'one concise sentence describing what it wants to find' rather than 'write a search query', to stop it emitting keyword-stuffed BM25-style queries.
- Expose several differentiated retrieval tools (wide semantic sweep over chunk summaries, grep, structural lookup) so each is used only for the intent it fits.
- Make retrieval effort a user-configurable latency-versus-quality knob instead of a fixed platform default.
- Keep BM25/lexical retrieval alongside dense retrieval — dense recall collapsed to 0% at 400k tokens where BM25 held 100%.
- Use vector search only to select seed nodes, then traverse relationships and rank by relatedness to assemble the actual context.
- Scale returned context with hierarchy depth rather than instance count, so a 64-unit and a 460,000-unit system produce comparable summary size.
- Keep warehouse data in the warehouse and pull only metadata into a graph as a semantic layer; ETL into a graph only for recursive-join performance, graph algorithms, embeddings, or clustering.
- Compute eval ground truth by running a stored query against the live data at runtime, since structured data changes under frozen expected answers.
- Log tokens, cache hits, cost, TTFT, and tool calls per turn — cheap to add and most teams skip it.
- Compute the build-versus-rent break-even before standardizing on per-query search APIs; one team's crossover was just over 15,000 entities or queries.

**Avoid:**

- Free-form subject-predicate-object triple extraction with no domain schema — the resulting graph is not usable.
- Assuming semantic search can answer coverage or negative questions ('what documentation are we missing') — it can only match similar things.
- Sharding entity enumeration across parallel LLM calls; it produces phantom entities and silent omissions.
- Layering a bash/filesystem browse tool on top of already-good hybrid search — it added no recall and made responses 50% slower.
- Chaining multiple vector hits to answer a multi-hop question; each additional hop is another chance to retrieve the wrong document.
- Hundreds of distinct relationship types in a production data model — they overflow the model's context and degrade generated queries.
- Aggressively clearing old tool outputs, which just makes the agent re-retrieve information it already had.
- Naive PDF parsers (truncated text, linearized tables, dropped images) and frontier-model document conversion at thousands-of-documents scale.
- Exposing memory through MCP tools that include a 'forget' command the agent can call on itself.
- Storing large-scale agent memory as speculatively-loaded markdown files once the corpus exceeds the context window.

## Notable Outliers

- Agents write 'caveman style' keyword queries because they are trained on grep-based code exploration and evaluated on benchmarks like BEIR that structurally favor BM25 — the benchmarks are actively mis-training agent search behavior. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s))
- You can do RAG with no chunker, no embedding model, and no vector database: the document's markdown section outline becomes the entire retrieval index, demonstrated on a 418-section annual report. ([Structuring the Unstructured](../talks/structuring-the-unstructured.md), [14:32](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=872s))
- Two years ago a graph data model needed dedicated entity nodes; agents are now capable enough that you can often omit them, with life sciences ontologies as the counterexample. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:07:53](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=4073s))
- Query frequency, not record volume, is the dominant cost driver for agentic web context — every repeated query costs the same as the first even when nothing changed, which pushes teams to quietly refresh less often and cap result counts. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [13:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=812s))
- AI-native systems should run Karpathy's drift backwards: start at software 3.0 by throwing everything in the context window to find what is worth building, then migrate toward deterministic 1.0 code as the use case earns it. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s))
- After presenting a full efficiency-and-accuracy argument for graph-based document navigation, the speaker stated none of it had been benchmarked. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:54:56](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6896s))
- Search infrastructure should be rebuilt for agents rather than humans, because agents can read thousands of long snippets instead of ten blue links with short ones. ([First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md), [11:08](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=668s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)
- [On AI and Knowledge](../talks/on-ai-and-knowledge.md)
- [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)
- [Structuring the Unstructured](../talks/structuring-the-unstructured.md)
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Cedric Clyburn](../speakers/cedric-clyburn.md)
- [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Mike Phipps](../speakers/mike-phipps.md)
- [Omar Solano](../speakers/omar-solano.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Richard Socher](../speakers/richard-socher.md)
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Tim Ainge](../speakers/tim-ainge.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)
- [Zach Blumenfeld](../speakers/zach-blumenfeld.md)

