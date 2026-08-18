---
title: "agentic retrieval"
type: "concept"
slug: "agentic-retrieval"
tier: "supporting"
maturity: "contested"
talk_count: 11
speaker_count: 12
---

# agentic retrieval

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **11** talk(s) by **12** speaker(s)

**Definition:** Letting the model plan and iterate its own searches — issuing queries, reading results, and re-querying — instead of a fixed one-shot retrieval step.

*Also referred to as: agentic rag, agentic search, agentic web retrieval, agentic query generation, web search for agents, llm planning vs retrieval, search grounding*

## State of Practice

The field has converged on a diagnosis: with frontier models, the binding constraint on hard knowledge tasks is retrieval, not reasoning — Mixedbread showed Codex scoring 9 points on BrowseComp Plus against a 93% oracle, a gap closed almost entirely by swapping the search tool without touching the reasoning model. Nobody defends one-shot cosine similarity anymore; the shared position is that vector search is one signal among several and structurally cannot answer negative, coverage, or multi-hop questions, so retrieval is now built on hybrid stacks over explicit structure — document outlines, containment hierarchies, citation and dependency graphs, warehouse metadata graphs — with embeddings often demoted to seed-node selection before traversal. What is genuinely contested is how much of the loop the model should own: Microsoft and Mixedbread build and train iterative reflect-and-re-query agents (Mixedbread capping at four rounds with parallel searches inside each), while Phaidra argues LLMs are good at planning searches and bad at performing them and replaces the loop with a two-or-three-step plan-then-deterministic-resolve pipeline that held 100% correctness from 64 to 460,000 GPUs while cutting a validation pass from 116M to 390K tokens. Cost discipline is now first-class: speakers quantify tool-call reductions (40% via subgraph retrieval), token reductions (~300x), and per-query economics (break-even against rented context at ~15,000 entities). The unresolved meta-question, argued openly, is whether rising model capability deletes this engineering — Neo4j speakers already drop graph nodes and prebuilt query shapes that agents no longer need, while Phaidra and the Gates Foundation argue AI-native systems should migrate toward more deterministic scaffolding, not less.

## Consensus

### Pure vector/semantic similarity is insufficient as an agent's retrieval substrate; production systems combine it with lexical, structural, or graph retrieval.

Support: **6** talk(s)

> "I think, you know, for a hot second as an industry, we thought that if we could get really, really good at computing cosine similarity between vectors, we were all set for retrieval. It turns out, you know, things never are are never that easy."
>
> — [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [7:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=444s)

Supporting talks: [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)

### Retrieval quality, not model reasoning, is the current bottleneck on complex knowledge tasks — capable models fail on noisy corpora and recover when handed the right documents.

Support: **4** talk(s)

> "So we see that the models are extremely capable if they would get the right documents but if you put them into the noisy corpus the performance drops sharply. Meaning that actually the bottleneck here is not the reasoning. It's actually the access to the right knowledge it needs to answer this question."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s)

Supporting talks: [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)

### When the corpus already has structure (hierarchy, document outline, citation or dependency graph, schema), the agent should traverse that structure rather than scan or re-embed content — it cuts tokens and tool calls and surfaces nodes similarity search cannot reach.

Support: **6** talk(s)

> "If your data has structure, call it a hierarchy, graph, or a schema, a language model scanning it token by token is definitely the wrong tool."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:04](https://www.youtube.com/watch?v=EUsPvBeIx70&t=844s)

Supporting talks: [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

### Iteration must be explicitly budgeted — round caps, flat-cost pipelines, or an effort knob — because unbounded re-querying is the dominant cost and latency driver, not index size.

Support: **6** talk(s)

> "That's why we decided to um define that it has a maximum four search rounds, but within each search round it can have parallel searches."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [6:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=385s)

Supporting talks: [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)

### Retrieval depth should be matched to query difficulty: single-shot retrieval is adequate for easy questions and iterative reflection should be reserved for hard ones, rather than applying one fixed strategy to everything.

Support: **4** talk(s)

> "for easy cases, like, you know, quick single-shot retrieval is great, but for more sophisticated cases, you do want a system that can reflect on on what's in the data set and decide whether or not we've satisfied the information need as stated in the input before we come back with results"
>
> — [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [8:36](https://www.youtube.com/watch?v=RGSFUqzqErE&t=516s)

Supporting talks: [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)

### MCP is the assumed delivery interface for retrieval: knowledge bases and semantic layers are exposed as MCP servers into tools users already have, rather than wrapped in a bespoke chat app or custom glue code.

Support: **3** talk(s)

> "four different systems one graph uh one semantic layer that's exposed through an MCP then to the to the agents. And so this is the so if you think of the agent's perspective, this is the the structure that it can dynamically discover and reason across at query time."
>
> — [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [14:16](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=856s)

Supporting talks: [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)

## Disagreements

### Should the agent own an open-ended search loop, or should retrieval be a bounded pipeline where the LLM plans once and deterministic code executes?

| Position A | Position B |
|---|---|
| Let the agent iterate: reflect on what it has retrieved, decide whether the information need is satisfied, and re-query — this measurably beats single-shot on hard cases, and multi-turn iteration is what makes outline-based and corpus-wide search work.<br>*[On AI and Knowledge](../talks/on-ai-and-knowledge.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)* | LLMs are good at planning searches and bad at performing them; use a two-or-three-step plan-then-resolve pipeline with deterministic set operations so cost stays flat and recall is exact, and precompute subgraphs so the agent needs fewer tool calls in the first place.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)* |

*Why it matters: It decides whether retrieval cost scales with corpus size and query ambiguity or stays constant — Phaidra measured 116M tokens per validation pass under the loop versus 390K under the bounded pipeline, and 30% correctness versus 100% at 460,000 entities. It also determines whether you can promise reproducibility to mission-critical consumers.*

### Can structural navigation replace vector retrieval, or must it always be paired with it?

| Position A | Position B |
|---|---|
| Graph or hierarchy navigation is a complement, not a replacement — use vector search to pick seed nodes or as a parallel signal, and expect production systems to end up hybrid.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)* | For structured corpora you can drop the embedding stack entirely: the document's markdown section outline is the index, or exact set logic over a hierarchy replaces similarity — no chunker, no embedding model, no vector database.<br>*[Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)* |

*Why it matters: It is the difference between shipping and operating an embedding pipeline (chunking strategy, re-embedding on update, vector store ops) and shipping nothing but a parser plus a traversal tool. It also changes failure modes: hybrid degrades gracefully on unstructured content, structure-only fails hard when the source has no reliable structure.*

### Should the retrieval index be built by LLM extraction, or derived deterministically from existing structure?

| Position A | Position B |
|---|---|
| Prefer deterministic, rule-based loads — regex and document structure, metadata-derived theme labels, layout-model parsing — because they are idempotent, faster, cheaper, and reproducible run to run; LLM assistance is a fallback for poorly labeled sources.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)* | LLM extraction is the right primitive as long as you constrain it: give the extractor a domain schema plus naming and unit ontology instructions, then reconcile entities with embedding-based matching, and have the model write both the extractors and the queries.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* |

*Why it matters: Ingest determinism decides whether you can re-run a pipeline and get the same graph, which in turn decides whether your evals mean anything and whether nightly refresh is affordable at thousands-of-documents scale.*

### Will improving model capability absorb retrieval engineering, or does hand-modeled structure remain the durable asset?

| Position A | Position B |
|---|---|
| Agents are already smart enough to skip modeling work that used to be mandatory — dropping entity nodes from the data model, writing free-form Cypher instead of calling prebuilt query shapes, hill-climbing their own instructions past handwritten ones — and replacing manual processes with learned ones has reliably produced improvements.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)* | AI-native systems should migrate from software 3.0 toward 1.0 as they mature: anything expressible as rules or structure becomes deterministic code, and the modeled tacit knowledge of how your organization actually answers a question stays defensible no matter how good models get.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)* |

*Why it matters: This determines where a team invests a year of effort — in schema, ontology, and eval-driven data modeling, or in thinner scaffolding on the assumption the next model deletes it. Bet wrong and you either ship brittle prompt-glue or over-engineer an index the model would have navigated unaided.*

### Should agents rent context from search and context-as-a-service providers at query time, or own a pre-collected corpus?

| Position A | Position B |
|---|---|
| Own it: query frequency, not record volume, is the cost killer since every repeated query costs the same as the first, and rented providers are capped to fields they already chose to collect — break-even against building your own pipeline arrives at roughly 15,000 entities.<br>*[The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* | Rent the live layer: training alone no longer keeps models useful, freshness decays in under a day for social and ~30 days for news and retail, and sub-second search APIs plus agents that read thousands of long snippets are what make interactive agentic retrieval possible at all.<br>*[How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)* |

*Why it matters: Per-query pricing quietly degrades knowledge work — teams cut refresh frequency and cap result counts to control spend — while owning the pipeline front-loads a week of engineering and a standing freshness obligation. The right answer flips based on whether the questions are ad hoc or persistent and repeated.*

## Practical Guidance

**Do:**

- Cap the agentic search loop at a fixed number of rounds (Mixedbread uses four) and get breadth from parallel searches inside each round rather than more rounds.
- Instruct the model to write 'one concise sentence describing what it wants to find' instead of 'write a search query' — the second phrasing drops it back into keyword-stuffed BM25 patterns.
- Expose several differentiated retrieval tools (a wide semantic search returning ~50 chunks shown as summaries, plus grep, plus structured lookup) so each intent hits the tool that fits it, and make the agent state what evidence it needs before querying.
- Use vector search only to select seed nodes, then traverse relationships and rank neighbors by relatedness to assemble the context window.
- Make retrieval effort a caller-configurable knob and treat it explicitly as a latency-versus-quality trade-off; use single-shot for easy queries.
- Size context by hierarchy depth, not instance count — describe root-to-leaf paths so a 64-unit and a 460,000-unit system produce the same summary.
- For structured documents, use the markdown section outline as the entire retrieval index and let the agent iterate over sections; a 418-section annual report works this way.
- Keep exact set logic, counting, and dedup across near-identical names in deterministic code — every 1.0 function is more reliable ground for the LLM.
- Pull warehouse metadata into a graph as a semantic layer so the agent can see how hundreds of tables interrelate, and leave the actual rows in the warehouse.
- Give any LLM extractor a domain schema plus explicit naming and unit standardization instructions, then run a separate embedding-based entity-matching step because prompts alone are not bulletproof.
- Compute eval ground truth at runtime by re-running a stored graph query against live data, and feed eval failures back into the schema and domain rules rather than treating them as a score.
- Optimize retrieval output for information density per token, not relevance alone.

**Avoid:**

- Speculatively loading whole markdown memory files each turn — it burns 100k+ tokens per round and stops working entirely once the corpus exceeds the 1M-token context.
- Chaining multiple vector hits to answer multi-hop questions; each additional hit is another chance to retrieve the wrong document, and long reasoning chains fail on similarity search even when every needed fact is stored.
- Using semantic search for negative or coverage questions like 'what documentation are we missing' — it can only match similar things.
- Sharding lists of near-identical entity names across parallel LLM calls: it produces phantom equipment that does not exist and silently drops real entities.
- Trusting BEIR/NanoBEIR-style benchmarks as evidence your agent queries well — their entity-based 'caveman style' queries structurally favor BM25 and mis-train agent search behavior.
- ETL-ing terabyte-scale warehouse data into a graph just to give an agent context; justify the move only by recursive-join performance, graph algorithms, embeddings, or clustering.
- Free-form subject-predicate-object triple extraction with no schema — the resulting graph is not usable.
- Letting a production data model sprout hundreds of distinct relationship types; it overflows the model's context and degrades Cypher generation. Use one generic containment relationship name across hierarchy levels.
- Exposing memory through MCP tools that include a forget command the agent can call on itself.
- Using frontier models for document conversion at thousands-of-PDFs scale — cost, non-determinism, and version deprecation between model releases break consistent structured output.

## Notable Outliers

- LLMs are good at planning searches but bad at performing them — so keep the planning step and replace the searching step with deterministic set operations. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [6:29](https://www.youtube.com/watch?v=EUsPvBeIx70&t=389s))
- Agents write keyword-stuffed queries because they were trained on grep-based code exploration and benchmarked against BM25-friendly corpora; the fix is retraining query behavior with a trajectory reward that judges whether the query is a natural sentence and whether exploration volume was appropriate. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s))
- Graph shortest-path traversal surfaced a controlling precedent that is never cited in the target case — found purely through the citation graph, unreachable by vector search or symbol lookup. ([A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [8:56](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=536s))
- Build-versus-rent break-even for agentic web context arrives at just over 15,000 entities or queries, assuming about a week and $5,000 of setup — much lower than most teams assume, because frequency rather than record volume drives cost. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [18:59](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1139s))
- The speaker demoed an entire agentic graph retrieval architecture and then stated plainly that none of the efficiency or accuracy claims in it had been benchmarked. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:54:56](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6896s))
- Once eval scores are strong on an agentic retrieval system over enterprise data, the residual failures are dominated by user-intent ambiguity rather than factually wrong answers — and an answer is only 'correct' if it matches how the question has historically been answered under existing reporting conventions. ([Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [19:08](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1148s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)
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
- [Mike Phipps](../speakers/mike-phipps.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Richard Socher](../speakers/richard-socher.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Tim Ainge](../speakers/tim-ainge.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)
- [Zach Blumenfeld](../speakers/zach-blumenfeld.md)

