---
title: "CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens"
type: "talk"
slug: "crabrag-why-automated-assistants-need-graph-memory-not-more-tokens"
track: "Graphs"
org: "Neo4j"
day: "Day 4 — Session Day 3"
room: "Track 5"
video_id: "Q0VkgCyNVUg"
duration_sec: 1242
word_count: 3263
speakers: ["Stephen Chin"]
---

# CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens

**Speakers:** [Stephen Chin](../speakers/stephen-chin.md)

**Org:** Neo4j

**Track:** Graphs &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 20m 42s

[Watch on YouTube](https://www.youtube.com/watch?v=Q0VkgCyNVUg)

## Summary

Stephen Chin of Neo4j argues that the markdown-file memory used by today's coding and personal agents (Open Claw, Hermes agent, Goose) breaks down at scale, burning 100k+ tokens per round by loading everything in hopes something is relevant. He walks through the progression from markdown files to vector stores to graphs, arguing that vector similarity is not the same as actual relationships and fails on multi-hop reasoning. The core of the talk is a live A/B demo: the same home-lab digital twin, built from the same source markdown, loaded into a vector store versus a Cognee/Neo4j graph, queried for security exposures. The graph side returns precise, actionable answers (a specific Debian 8 Minecraft server, specific WAN-exposed ports) where the vector side punts or tells the user to go check the config themselves. Worth watching if you want a concrete side-by-side of vector vs. graph memory rather than an abstract GraphRAG pitch, plus a practical architecture: vector search for seed nodes, then graph traversal and ranking.

## Key Points

- Agent memory in most current tools is just markdown files (agent memory files, tool files, daily memory files), which are human-readable but token-wasteful because everything gets loaded speculatively.
- Chin reports his average agents load at least 100k tokens per round, largely repetitively, which is tolerable at small scale with a high-quality model but fails at large scale.
- Skill-based systems fail when the wrong skill or no skill loads, and chains of skills are needed to complete a task; Neo4j has an arXiv paper on representing skills as a graph.
- Goose treats memory as just another MCP server with pluggable remember/retrieve/forget commands, but the underlying storage is still plain files on disk — and exposing a forget command means the agent is one tool call from wiping its own memory.
- Vector databases improve retrieval but similarity in vector space is not the same as real relationships, producing hallucinations and failing on long multi-hop reasoning chains even when all the facts are present.
- The demo architecture combines both: vector search finds the seed nodes, then graph traversal pulls nearest neighbors and ranks them by relatedness, giving multi-hop answers.
- Graphs give accuracy, explainability, and auditability — you can inspect exactly which subgraph produced the answer and then fix extraction or deduplicate nodes to converge on better results.
- You don't need graph expertise to start: Chin claims Claude writes Cypher better than he does and can build entity extractors, so long as you know the model you're trying to build.
- The A/B test on identical source data showed the vector store returning 'couldn't find specific details' and deflecting work back to the user, while the graph store named the exact out-of-date host and the exact WAN-exposed services.

## Notable Quotes

> "But, if your whole memory is a bunch of markdown files, you're wasting a lot of tokens."
>
> — [2:57](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=177s) &middot; *The talk's thesis in one line.*

> "my my average agents are loading up at least 100k in tokens for each round."
>
> — [3:32](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=212s) &middot; *Concrete number quantifying the cost of file-based memory.*

> "they they basically load up everything in the hopes that something will be useful in the context. At small scale that works where you get the results you want with a high quality model. It doesn't work at large scale"
>
> — [3:32](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=212s) &middot; *States the scale-dependent tradeoff explicitly.*

> "He wakes up every day, and his memory file flips, and now it's a new day, and he forgets everything from yesterday."
>
> — [0:59](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=59s) &middot; *Frames the problem the whole talk addresses.*

> "It kind of at the end of each task it goes and it reflects and it adds back in new skills or new things which it needs."
>
> — [4:53](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=293s) &middot; *Names a specific competing memory mechanism (Hermes agent reflection) and credits it.*

> "It relies heavily on MCP as the layer. Over 70 MCP extensions. And what it does is it treats memory just like another MCP server."
>
> — [5:41](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=341s) &middot; *Reports a number and characterizes Goose's memory architecture.*

> "same great idea, same fundamental problem. We're We're storing the memory. We're storing the memory of agents as markdown files on disks."
>
> — [6:23](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=383s) &middot; *The critique that unifies Open Claw, Hermes, and Goose.*

> "most dangerously, now you have MCP tools, you're one step away from calling the forget command and just wiping out your own memory."
>
> — [6:23](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=383s) &middot; *Names a specific failure mode of tool-exposed memory.*

> "the challenge here is similar what what vectors give you, which is similarity in vector space, is not the same as actual relationships."
>
> — [7:57](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=477s) &middot; *The core argument against vector-only memory.*

> "it's sometimes impossible to get to the answer even though you have all the facts because those large multi-hop reasoning chains don't work on similarity searches."
>
> — [8:33](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=513s) &middot; *Sharpest statement of the vector-store limitation.*

> "you suffer from getting facts which are related in some way and they're not your shell."
>
> — [9:16](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=556s) &middot; *Memorable framing of near-miss retrieval.*

> "it uses the vector search to get the seed nodes where it starts the traversal. And then it uses a graph search pulling the the nearest neighbors and then ranking those by how related they are."
>
> — [10:10](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=610s) &middot; *The actual hybrid architecture behind the demo.*

> "graphs are they're accurate. So, they give you very precise information. Explainable because you can look at the graph which got returned. And auditable because now you can actually say these are the this is the context."
>
> — [10:52](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=652s) &middot; *States the three claimed advantages of graph memory.*

> "If you're not a graph expert, guess what? Claude is. Claude can write Cypher better than I can."
>
> — [11:33](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=693s) &middot; *Directly addresses the adoption objection to graphs.*

> "We're going to do have Claude write each action into the graph as he works. We're going to follow up by traversing, not re-reading it."
>
> — [11:33](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=693s) &middot; *Compresses the write-then-traverse memory pattern into one sentence.*

> "One is a vector database store, that's our our A test. And the second is a graph store, that's our B test."
>
> — [12:04](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=724s) &middot; *Establishes the demo is a controlled comparison on identical source data.*

> "so it gives us very precise actionable information. And so that's the difference between same same exact data. One is a vector store, one is a graph store"
>
> — [14:15](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=855s) &middot; *The demo's punchline claim.*

> "the memory search returned some information and it's telling me check services configuration expects pfSense rule. So, it told me to go do the job for it."
>
> — [15:42](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=942s) &middot; *Names a specific observed failure mode of the vector-backed agent.*

> "if you're doing anything at at large scale where it doesn't fit into the 1 million context window of the modern models, you really need a better memory system than just throwing things in markdown files."
>
> — [17:15](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=1035s) &middot; *The talk's closing recommendation, with the scale threshold made explicit.*

## Positions

- Storing agent memory as markdown files wastes a large number of tokens because everything is loaded speculatively. ([2:57](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=177s), confidence: stated)
- His agents load at least 100k tokens per round. ([3:32](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=212s), confidence: stated)
- File-based memory works at small scale with a high-quality model but does not work at large scale. ([3:32](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=212s), confidence: stated)
- Hermes agent has a better memory system than Open Claw because it reflects at the end of each task and writes back new skills. ([4:53](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=293s), confidence: stated)
- Goose has over 70 MCP extensions and treats memory as just another MCP server backed by plain files. ([5:41](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=341s), confidence: stated)
- Exposing memory through MCP tools creates a risk that the agent calls the forget command and wipes its own memory. ([6:23](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=383s), confidence: stated)
- Similarity in vector space is not the same as actual relationships, and relying solely on vector lookup causes hallucinations. ([7:57](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=477s), confidence: stated)
- Long multi-hop reasoning chains cannot be resolved by similarity search even when all the needed facts are stored. ([8:33](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=513s), confidence: stated)
- Multi-hop queries are also very expensive on traditional relational databases. ([9:16](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=556s), confidence: stated)
- The best architecture uses vector search to select seed nodes and then graph traversal with relatedness ranking to assemble context. ([10:10](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=610s), confidence: stated)
- Graph-based retrieval is accurate, explainable, and auditable because you can inspect the returned subgraph that produced the answer. ([10:52](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=652s), confidence: stated)
- Claude can write Cypher better than the speaker can and can build entity extractors, so graph expertise is not a prerequisite for adopting graph memory. ([11:33](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=693s), confidence: stated)
- On identical source data, a graph store produces precise actionable answers where a vector store fails to surface the relevant information. ([14:15](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=855s), confidence: stated)
- Once your data exceeds the 1 million token context window of modern models, markdown-file memory is no longer viable. ([17:15](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=1035s), confidence: stated)
- Representing skills as a graph is a promising way to solve the wrong-skill-loaded problem. ([4:53](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=293s), confidence: implied)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent skills](../concepts/agent-skills.md)
- [agentic retrieval](../concepts/agentic-retrieval.md)
- [citation and grounding](../concepts/citation-and-grounding.md)
- [context window management](../concepts/context-window-management.md)
- [graph rag](../concepts/graph-rag.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [model context protocol](../concepts/model-context-protocol.md)

