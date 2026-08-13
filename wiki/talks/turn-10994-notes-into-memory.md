---
title: "Turn 10,994 Notes Into Memory"
type: "talk"
slug: "turn-10994-notes-into-memory"
org: "Decoding AI & Louis-François Bouchard, Towards AI"
video_id: "ZRM_TfEZcIo"
duration_sec: 2372
word_count: 6559
speakers: ["Paul Iusztin"]
---

# Turn 10,994 Notes Into Memory

**Speakers:** [Paul Iusztin](../speakers/paul-iusztin.md)

**Org:** Decoding AI & Louis-François Bouchard, Towards AI

**Duration:** 39m 32s

[Watch on YouTube](https://www.youtube.com/watch?v=ZRM_TfEZcIo)

## Summary

Paul Iusztin (Decoding AI) and Louis-François Bouchard (Towards AI) walk through an 18-month effort to turn ~10,000 personal notes across Obsidian, Readwise, Notion and Google Drive into a queryable research memory that coding agents can use. The core argument is that ChatGPT, Codex/Claude Code, NotebookLM and vector-DB RAG each fail a personal research workflow — context evaporates between sessions, you don't own the tool, or the infra is too heavy and not human-inspectable — so you need a thin system sitting between the agent harness and your second brain. They show three versions of that system, ending in an architecture with no database at all: immutable raw files, an `index.yaml` catalog of sources and summaries, and an LLM-generated wiki layer of concepts, entities, comparisons and notes, traversed in a hierarchy so the agent usually stops at an executive summary instead of reading a full source. The wiki is 'alive' — every question the agent can't answer leaves a new file or log entry behind. Worth watching if you want a concrete, files-only memory design and a working Claude Code plugin (the AI Research OS repo) to fork; skip it if you want a polished product or production-scale retrieval.

## Key Points

- The bottleneck in agentic research is not how much context you can feed a model but whether that context survives to the next session, since the agent's context window is simultaneously its database, file system, memory and reasoning space.
- The speakers deliberately reject vector databases, knowledge graphs and semantic search for personal research, arguing the added infrastructure isn't human-inspectable and isn't worth it below production scale.
- The architecture is three layers of plain files: an immutable `raw/` folder the LLM never edits, an `index.yaml` catalog holding per-source links, metadata and summaries, and a `wiki/` folder of LLM-generated derivatives (concepts, entities, comparisons, notes, open questions).
- Retrieval is a token-efficiency hierarchy — the agent reads the index first, then the per-source executive summary, then wiki derivatives, and only reads the full raw source if it still hasn't found the answer.
- V1 was a classic deep-research loop over the public web seeded with hand-picked 'golden links'; V2 pointed the same loop at their own second brain, on the theory that a curated second brain *is* the golden-link set; V3 added the persistent wiki on top because a flat research.md is static and re-running the loop is expensive.
- The deep research loop uses an orchestrator that fans out questions to sub-agents (Gemini grounded in Google), summarizes each returned link, then ranks sources against the original topic and only fully scrapes the top-K — three rounds of six queries yields 40–50 links, most of which are noise.
- The wiki evolves from conversation, not just ingestion: every question can spawn a new concept, note or comparison file and is written to a log, so the store reflects what you didn't understand as much as what you read.
- The wiki is deliberately project-scoped rather than sitting on top of the whole vault — Obsidian (organized with Tiago Forte's PARA method) stays an immutable snapshot, and each project pulls a scoped slice from it via the research skill.
- Known gaps the authors accept by design: missing connectors (Drive, Notion, Slack), no good source provenance or staleness ranking, memory compaction still weak, and no UI — because the project's goal is to teach memory and context management, not to be a product.

## Notable Quotes

> "I spent 18 months turning my second brain into my living research memory."
>
> — [0:00](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=0s) &middot; *The thesis and the scale of investment in one line.*

> "within my second brain, I currently have over 5,000 notes in Obsidian and another 5,000 notes in Readwise and some scattered in Notion and Google Drive"
>
> — [0:00](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=0s) &middot; *Concrete numbers that define the problem size.*

> "you need a system that sits between those harnesses and your second brain"
>
> — [0:34](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=34s) &middot; *States the architectural position against using Codex/NotebookLM directly.*

> "how can we make research better, but more specifically, how can we better leverage what we have?"
>
> — [3:16](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=196s) &middot; *Reframes the goal from acquisition to reuse.*

> "It's not agent native. And it's obviously weak for coding tasks since it's just browser based."
>
> — [5:28](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=328s) &middot; *The specific, checkable objection to NotebookLM.*

> "But, this needs an infrastructure. It's not really human-friendly to be able to digest quickly, to check notes, to make edits. It's hard to inspect by hand."
>
> — [6:21](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=381s) &middot; *The tradeoff case against vector-DB RAG for personal use.*

> "the next session you use Codex, you have to paste it all again or ask it to use skills."
>
> — [7:57](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=477s) &middot; *Names the concrete failure mode motivating the whole system.*

> "The bottleneck is how can you leverage it in the future? Meaning that with an agent, the context window becomes everything, the database, the file system, the memory, the reasoning space."
>
> — [8:36](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=516s) &middot; *The sharpest framing of why context windows aren't memory.*

> "we don't need necessarily to provide more and more and more context for a better research. You need a proper memory and context management"
>
> — [8:36](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=516s) &middot; *Takes a side against the more-context-is-better default.*

> "So basically after three rounds of generating six queries per round, we ended up with like 40-50 links in total."
>
> — [14:32](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=872s) &middot; *Reports the actual fan-out numbers behind the deep research loop.*

> "For the course, it worked great right away. We generated 35 lessons really quick, but we wanted more."
>
> — [15:25](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=925s) &middot; *Quantifies what V1 actually delivered before they scaled ambition.*

> "this research MD file is static. It's a pile of static data. And usually research is not static, right?"
>
> — [17:43](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1063s) &middot; *The motivation for adding the wiki layer.*

> "It consumes a lot of tokens and it takes a lot of time."
>
> — [17:43](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1063s) &middot; *Names the cost that makes persistence necessary.*

> "that's why V3 of this system is actually a deep research algorithm plus an LM knowledge base on top of it, aka the wiki layer."
>
> — [18:20](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1100s) &middot; *One-sentence definition of the final architecture.*

> "you should forget the infra structure you think you need, such as vector databases, knowledge graphs, semantic search, text search."
>
> — [19:04](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1144s) &middot; *The most contrarian claim in the talk.*

> "So, no database, just a simple index based on references."
>
> — [19:45](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1185s) &middot; *The design decision stated at its most compressed.*

> "And sometimes the agent just looks into this, gets what it needs, and goes back. Which is very token efficient, right?"
>
> — [22:51](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1371s) &middot; *Explains why the summary hierarchy pays off.*

> "the beautiful part is that this wiki is actually alive, right? For example, every question leaves a trace into your wiki."
>
> — [23:38](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1418s) &middot; *The idea that distinguishes this from a static research artifact.*

> "Obsidian is just an immutable snapshot that a LLM never touches, right? So, this is my data. I don't really want the LLM to touch my personal notes that I manually write"
>
> — [24:59](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1499s) &middot; *A firm boundary between human-authored source and machine-generated derivative.*

> "The project is the work, and your second brain is the research."
>
> — [26:36](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1596s) &middot; *The organizing metaphor for how scoping works.*

> "usually light or fast is more than enough because remember this process consumes a lot of tokens."
>
> — [28:43](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1723s) &middot; *Practical operating guidance with a stated cost reason.*

> "the other main goal of this project is to teach memory and context management"
>
> — [37:02](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=2222s) &middot; *Explains why missing connectors are not treated as bugs.*

> "our goal is to teach AI engineering. It's not to build the next best product."
>
> — [37:37](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=2257s) &middot; *Sets expectations for anyone considering adopting the repo.*

## Positions

- Personal research memory should be built on plain markdown files and a reference index rather than vector databases, knowledge graphs, or semantic search. ([19:04](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1144s), confidence: stated)
- The limiting factor in agentic research is not how much context you can supply but whether it persists across sessions. ([8:36](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=516s), confidence: stated)
- NotebookLM is unsuitable as a research OS because you don't own it, it isn't agent-native, and it's weak at coding tasks. ([5:28](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=328s), confidence: stated)
- Vector-DB RAG pipelines are the right answer for production products but the wrong answer for a personal, daily-use research system. ([6:21](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=381s), confidence: stated)
- A curated second brain functions as an organically generated set of 'golden links', removing the need to hand-pick seed sources for deep research. ([16:14](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=974s), confidence: stated)
- A hierarchy of index → executive summary → wiki derivative → raw source makes agent retrieval substantially more token-efficient than reading full sources. ([23:38](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1418s), confidence: stated)
- The LLM should never write to your hand-authored notes; generated content belongs in a separate derivative layer. ([24:59](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1499s), confidence: stated)
- A knowledge base should update from questions asked of it, not only from ingestion events. ([24:20](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1460s), confidence: stated)
- Running the deep research loop at its deepest setting is rarely worth the token cost; light or fast settings suffice for most topics. ([29:26](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1766s), confidence: stated)
- For one-off tasks or quick lookups, ChatGPT or a coding agent is the correct tool and building a research OS is overkill. ([3:16](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=196s), confidence: stated)
- Memory compaction remains an unsolved, rapidly moving problem even in their own system. ([37:37](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=2257s), confidence: stated)
- Adding new connectors to such a system is cheap enough that users should extend it themselves rather than wait for maintainers. ([11:38](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=698s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [agent skills](../concepts/agent-skills.md)
- [citation and grounding](../concepts/citation-and-grounding.md)
- [context compaction](../concepts/context-compaction.md)
- [context window management](../concepts/context-window-management.md)
- [institutional knowledge capture](../concepts/institutional-knowledge-capture.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)

