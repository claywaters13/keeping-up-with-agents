---
title: "AI on Your Lakehouse: Context Comes in Shapes, Not Queries"
type: "talk"
slug: "ai-on-your-lakehouse-context-comes-in-shapes-not-queries"
track: "Track 2"
org: "Neo4j"
day: "Day 1 — Workshop Day"
room: "Track 2"
video_id: "kRkcNOsRyYg"
duration_sec: 7150
word_count: 18147
speakers: ["Zach Blumenfeld"]
---

# AI on Your Lakehouse: Context Comes in Shapes, Not Queries

**Speakers:** [Zach Blumenfeld](../speakers/zach-blumenfeld.md)

**Org:** Neo4j

**Track:** Track 2 &nbsp;|&nbsp; **Day/Room:** Day 1 — Workshop Day &middot; Track 2 &nbsp;|&nbsp; **Duration:** 1h 59m

[Watch on YouTube](https://www.youtube.com/watch?v=kRkcNOsRyYg)

## Summary

Zach Blumenfeld of Neo4j runs a nearly two-hour hands-on workshop arguing that lakehouse agents fail not because they can't access data, but because they lack the right *shape* of context. He introduces three graph shapes over a fictional auto-repair chain's BigQuery warehouse and PDF document store: a 'connection' semantic layer (metadata-only graph of tables, columns and join paths, built with Neo4j's Neo Carta labs project) that guides text-to-SQL without ETLing data into the graph; a 'table of contents' outline shape (a deterministic containment tree plus cross-document links with hierarchical URIs) that lets an agent navigate documents rather than only search them; and a 'themes' shape (Leiden community detection over the links-to graph) that surfaces global clusters with no LLM extraction at all. The through-line is that estate-level questions — what documentation is missing, what are we failing to fix repeatedly, how do these tables join — are hard or impossible for vector search because you cannot search for a negative. Worth watching if you're weighing graph RAG against pure vector/text-to-SQL, or want a lightweight deterministic alternative to Microsoft-style entity-extraction GraphRAG; skip it if you want benchmarks, since the speaker admits he ran none.

## Key Points

- The core thesis is that agents on a lakehouse can already retrieve data via text-to-SQL and vector search, but they fail on questions requiring a particular structural shape of context — coverage gaps, global patterns, and multi-hop table joins.
- The connection shape uses Neo Carta to pull only metadata (tables, columns, representative values, join paths) into Neo4j as a semantic layer, deliberately leaving the actual rows in BigQuery so there is no ETL, no sync problem, and no security-posture change.
- The table-of-contents/outline shape is built by a fully deterministic, idempotent load — a containment tree of library/folder/document/section plus next-section ordering and named links — rather than LLM entity extraction, which makes it faster, reproducible, and cheap to rebuild.
- Every node gets a hierarchical URI, which does double duty: it lets the agent drill into subtrees via a parameterized variable-length path query, and it lets a Lucene full-text search be scoped with a simple starts-with post-filter.
- The themes shape runs Leiden community detection (via Neo4j GDS, on an in-memory projection with section-level links collapsed to the document level) and labels clusters purely from existing document and link metadata, trading interpretive richness for stability and cost versus Microsoft GraphRAG's LLM-generated community summaries.
- Blumenfeld explicitly rejects the framing of graph navigation as a replacement for semantic search, saying he always pairs it with at least full-text search, and uses 'semantic expansion' (letting the model add synonyms like misfire/rough idle) to compensate for using Lucene instead of vectors.
- Relationship and label naming is a real tradeoff: he uses a single generic `has` for containment across all levels because per-level names complicate Cypher, and warns that hundreds of relationship types become unmanageable inside a context window.
- He argues agentic Cypher writing has improved dramatically — recommending the Neo4j CLI plus the Cypher and GDS skills so the model gets current syntax instead of years-old Stack Overflow answers — and predicts agents will increasingly prefer free-form Cypher over prefab shapes.
- In the live demo the agent skipped the outline shape on the gap-analysis question and fell back to an exhaustive full-text crawl; it reached the right answer but slower, which he flags as evidence the shapes need better skill guidance rather than as a success.

## Notable Quotes

> "sometimes there are still some challenges around how do you give your agent the right type of context, whether or not they can see all the data in the way that they need, and really take a slice to answer the right type of question."
>
> — [1:43](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=103s) &middot; *States the talk's central problem framing in the speaker's own words.*

> "So this is sort of like proving a negative which can be very hard with something like semantic search, uh, which can only match similar things, right? It can't really find a negative example."
>
> — [5:14](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=314s) &middot; *The sharpest statement of what vector search structurally cannot do.*

> "the thing that we're doing here really is we're not using the graph to copy the data over. There's not like an ETL into graph. What we're doing is we're using the graph as a semantic layer."
>
> — [26:43](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=1603s) &middot; *The key architectural distinction separating this from conventional graph adoption.*

> "the other thing that a graph database is really great at doing is not just making those complicated queries run faster, but actually providing a view or a representation of the data that allows an agent to understand how tables might interrelate."
>
> — [34:48](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=2088s) &middot; *Reframes the value of graph from query performance to agent comprehension.*

> "even though the end join it might only be a three or four hop join, you might have had to understand hundreds of tables or something to be able to arrive at that conclusion."
>
> — [34:48](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=2088s) &middot; *Concrete articulation of why schema scale, not join depth, is the bottleneck.*

> "if you have sensitive data that's in one system, it might not, even though you could physically move it in, you you might not actually be able to for security reasons take that data and just move it into another database."
>
> — [37:30](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=2250s) &middot; *The non-technical reason he gives for metadata-only graphs, often overlooked in graph RAG pitches.*

> "Where you do get an advantage of the ETL over just this metadata and semantic layer graph is if you have graph queries that need that performance"
>
> — [38:06](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=2286s) &middot; *He names the condition under which his own recommended approach is the wrong one.*

> "it's going to go on the internet and get the Stack Overflow questions from like four or five or six years ago and it's going to give you outdated bad cipher basically."
>
> — [41:01](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=2461s) &middot; *Blunt argument for vendor-maintained agent skills over model priors.*

> "the benefits of having a deterministic load like this is number one, it's going to be item potent. Um, so like you're not relying on an LLM in the beginning. Um, it's often going to be a little bit faster."
>
> — [50:27](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3027s) &middot; *Core justification for the lightweight alternative to entity-extraction GraphRAG.*

> "I'd say it's more of a lexical or document structure graph rather than like a full like entity uh you know extraction type of pipeline to create a graph."
>
> — [50:27](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3027s) &middot; *Precisely categorizes what kind of graph he is advocating.*

> "The more granular you get with naming um basically the more sort of detailed uh your agent can be and your end tools can be in putting a query together. But then the more complicated your data model becomes."
>
> — [1:03:22](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3802s) &middot; *A clean statement of the schema-granularity tradeoff.*

> "two years ago, I probably would have said you would need that like additional node. Now, it seems like agents are smart enough where maybe you don't all the time anymore."
>
> — [1:07:53](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=4073s) &middot; *Concedes that improving models shrink how much structure you must pre-build.*

> "I think it would be naive to call it a replacement because most of the people that I see using this will eventually incorporate some sort of hybrid vector retrieval or full text search"
>
> — [1:04:59](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3899s) &middot; *A vendor engineer declining to overclaim against the competing technique.*

> "what we end up with without any sort of um tagging or labeling by AI or a language model um is just simply from the document structure we can tell that this first one um is about you know um BCM um and and bus and all these sorts of things."
>
> — [1:25:55](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=5155s) &middot; *The payoff claim for zero-LLM theme discovery.*

> "the advantage of that is every time I run it, it'll be the same as long as the data stays the same."
>
> — [1:33:48](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=5628s) &middot; *The determinism argument stated as a direct benefit over LLM summarization.*

> "then obviously it costs more money, it's slower, and the you if you run it twice, it might not return the same thing. So there's trade-offs between uh each way of doing it."
>
> — [1:33:48](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=5628s) &middot; *Names all three costs of the Microsoft GraphRAG summarization approach in one line.*

> "if those things aren't already wellleeled, this view might not be super informative right off the bat."
>
> — [1:33:48](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=5628s) &middot; *Honest statement of when the metadata-only theme shape degrades.*

> "So much better than the text to cipher experience that we've had like even as as soon as a year ago or six months ago."
>
> — [1:40:47](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6047s) &middot; *Dates the inflection point he claims for agentic query generation.*

> "it's a shame here that it didn't use the outline it's supposed to do that because basically when it uses the outline it's able to traverse through and find all of the links a little bit more efficiently."
>
> — [1:51:09](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6669s) &middot; *Speaker narrating his own demo not doing what he designed it to do.*

> "for this I haven't run any specific benchmarking on like exactly what I've shown you today."
>
> — [1:54:56](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6896s) &middot; *Important caveat on the evidentiary status of every efficiency claim in the talk.*

## Positions

- Semantic/vector search structurally cannot answer negative or coverage questions ('what documentation are we missing'), because it can only match similar things. ([5:14](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=314s), confidence: stated)
- You should not ETL warehouse data into a graph database for most agent use cases; pull only metadata and keep the data in the warehouse. ([26:43](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=1603s), confidence: stated)
- The main reasons not to move data into a graph are continuous-sync burden on terabyte-scale data, custom ETL complexity, and security posture preventing cross-system data movement. ([37:30](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=2250s), confidence: stated)
- ETL into a graph is justified specifically when you need recursive-join performance, graph algorithms, graph embeddings, or clustering. ([38:06](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=2286s), confidence: stated)
- A deterministic, regex/structure-based document load is preferable to LLM entity extraction when documents already have inherent structure and interlinking, because it is idempotent and faster. ([50:27](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3027s), confidence: stated)
- Graph document navigation is not a replacement for semantic search; production systems should use hybrid retrieval. ([1:04:59](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3899s), confidence: stated)
- Containment relationships should share a single generic name across hierarchy levels, because per-level names make Cypher unnecessarily complicated. ([1:03:22](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3802s), confidence: stated)
- Hundreds of distinct relationship types in a production data model become hard to manage within a model's context window and degrade Cypher generation. ([1:04:10](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3850s), confidence: stated)
- Modern agents are capable enough that entity nodes previously required in a graph data model can often be omitted, with life sciences ontologies as a counterexample. ([1:07:53](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=4073s), confidence: stated)
- Leiden is a more efficient successor to Louvain for community detection. ([1:23:56](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=5036s), confidence: stated)
- LLM-generated community summaries (the Microsoft GraphRAG approach) cost more, run slower, and are non-reproducible across runs compared to deriving theme labels from document metadata. ([1:33:48](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=5628s), confidence: stated)
- Metadata-only theme detection degrades when document titles and link names are poorly labeled, in which case LLM assistance during ingest becomes worthwhile. ([1:33:48](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=5628s), confidence: stated)
- Agent-written Cypher via the Neo4j CLI plus Cypher/GDS skills is substantially better than the text-to-Cypher experience of six to twelve months ago. ([1:40:47](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6047s), confidence: stated)
- As text-to-Cypher capability and skills improve, agents will increasingly prefer writing free-form Cypher over calling prebuilt shape scripts. ([1:47:52](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6472s), confidence: stated)
- Grounding in the document tree reduces hallucination risk relative to chaining multiple vector search hits, since each additional vector hit is another chance to retrieve the wrong document. ([1:44:24](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6264s), confidence: stated)
- None of the efficiency or accuracy claims in this workshop have been benchmarked by the speaker. ([1:54:56](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6896s), confidence: stated)
- Explicitly linking the structured (warehouse metadata) graph to the unstructured (document) graph would enable more deterministic mapping, but is unnecessary because the agent can join them at query time via extracted codes. ([1:57:26](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=7046s), confidence: stated)

## Concepts

- [agentic retrieval](../concepts/agentic-retrieval.md)
- [document parsing](../concepts/document-parsing.md)
- [graph rag](../concepts/graph-rag.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [mcp server design](../concepts/mcp-server-design.md)
- [semantic layer](../concepts/semantic-layer.md)

