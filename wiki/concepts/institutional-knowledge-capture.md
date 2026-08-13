---
title: "institutional knowledge capture"
type: "concept"
slug: "institutional-knowledge-capture"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 13
---

# institutional knowledge capture

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **13** speaker(s)

**Definition:** Turning tacit organizational and team knowledge into durable, retrievable artifacts that agents and people can both use.

*Also referred to as: tacit organizational knowledge, company brain, team memory, second brain systems, organizational knowledge sharing, knowledge base as context repository, file-based knowledge bases*

## State of Practice

The field has stopped treating knowledge capture as a documentation chore and started treating it as the load-bearing layer of agentic systems: speakers repeatedly reported that identical frontier models produce wildly different results depending on what durable context surrounds them, so the bottleneck is memory organization rather than model choice, context length, or number of MCP servers. The dominant architecture is a curated, versioned corpus — markdown skill files, wiki derivative layers, semantic layers, or property graphs — with explicit provenance, contradiction resolution where human corrections win, and a pruning process (human plus agent) that keeps stale facts from being retrieved confidently. Capture is understood as a loop, not a write: correction events, closed-won/closed-lost outcomes, eval failures, and questions asked of the base all feed back into it, and a quarterly-or-faster refresh is treated as mandatory because definitions and processes drift. The hard, unsolved part is tacit knowledge that was never written anywhere — a PM's model of their product, a data owner's join logic and reporting conventions, which of two equally correct metric definitions a given team means — and speakers were candid that existing Notion docs, help centers, and hand-maintained .md files do not contain it. The economic argument is now explicit: the accumulated corpus, not the model or the UI, is the defensible asset, because models are rented and chat interfaces are commodity. Where practitioners still split is on substrate (plain files vs. modeled semantic layer/graph) and on authorship (deliberate human curation vs. automatic harvest from sessions, Slack, and live systems).

## Consensus

### Bad agent output is a knowledge-organization failure, not a model failure — the same frontier model produces radically different results depending on the durable context around it.

Support: **5** talk(s)

> "The 2X people and the 100X people are using the exact same Claude. Same weights, same context window, same API. So, the leverage is not in the weights. It's in how you wire the work."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Content Is Code](../talks/content-is-code.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)

### The accumulated, organization-specific knowledge base is the durable competitive asset; models, agents, and chat UIs are rented or commodity.

Support: **3** talk(s)

> "The organization that captures what it learns like this gets smarter every single day. The one that doesn't wakes up every morning with amnesia, no matter how good the model is. Model quality is rented, but if you build your brain, you you own that brain."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [16:06](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=966s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)

### A knowledge store degrades without active hygiene — provenance, contradiction checking against existing facts, and deliberate pruning of stale entries — because retrieval will surface rotten context with full confidence.

Support: **4** talk(s)

> "a brain nobody curates becomes a garbage dump with great search. Retrieval will surface a stale fact with total confidence."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [13:58](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=838s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### Capture must be a closed loop: corrections, wins/losses, and eval failures are logged and written back into the knowledge base, otherwise the system silently drifts from reality.

Support: **5** talk(s)

> "All of these events need to be captured, logged, and used to update your data agent context."
>
> — [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [6:54](https://www.youtube.com/watch?v=B8l81jhvHbI&t=414s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)

### Captured knowledge should be encoded as executable, reusable artifacts (skill files / written procedures agents run) with named humans responsible for maintaining them, not as prose nobody reads.

Support: **3** talk(s)

> "The AI-native companies that I see inside YC encode all of that as skills, written procedures that their agents execute, and they hire they hire engineers whose job it is to maintain those skills, to do the work the skills can't do yet."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [6:25](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=385s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Content Is Code](../talks/content-is-code.md)

### The knowledge that matters most was never written down — existing docs, help centers, and knowledge bases do not contain the procedural and semantic knowledge held by PMs and data owners, so it must be actively elicited from people.

Support: **3** talk(s)

> "Imagine like all the knowledge that a product manager has in their head about their product. Like, how do you get that into an agent?"
>
> — [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [11:55](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=715s)

Supporting talks: [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Content Is Code](../talks/content-is-code.md)

## Disagreements

### What substrate should institutional knowledge live in — plain files an agent reads directly, or a modeled semantic layer / knowledge graph?

| Position A | Position B |
|---|---|
| Plain markdown on a file system with a reference index is sufficient and superior; skip vector databases, knowledge graphs, and semantic search entirely (one system is 80,000 markdown files; Claude Tag is one markdown file per Slack channel).<br>*[Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)* | Hand-maintained .md files and skills cannot keep pace with changing KPIs, definitions, and processes; knowledge must be modeled into a ranked hierarchy — semantic layer, canonical queries, then a property graph — sourced from live systems and exposed via MCP.<br>*[Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)* |

*Why it matters: It decides whether you staff writers and librarians or data engineers and schema owners, and whether the artifact rots between reviews or updates itself from systems of record. The file camp gets started in a day; the modeled camp is the only one with an answer for metrics that two teams define differently.*

### Who authors the durable artifact — humans writing deliberately, or the system harvesting automatically from work traces?

| Position A | Position B |
|---|---|
| Humans author and curate; the LLM must never write into hand-authored notes, and quality depends on organizational discipline (clean tagged PRs, accurate diffs, conscientiousness) that must exist before agents can help.<br>*[Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Content Is Code](../talks/content-is-code.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* | Hand-authoring does not scale and is the wrong layer; capture belongs in a harness above the agent that materializes sessions, PRs, traces, and Slack channels automatically, and context should be pulled from continuously-updated systems rather than documents.<br>*[A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)* |

*Why it matters: If capture is authored, the prerequisite is a behavior-change program and a librarian headcount; if it is harvested, the prerequisite is infrastructure and defaults (public Slack channels, session recording) and the org gets a corpus it never explicitly wrote — with correspondingly weaker provenance.*

### Can the human judgment layer eventually be captured and automated away, or must a human gate stay permanently in the loop?

| Position A | Position B |
|---|---|
| A human gate is permanent: agents draft, humans send; taste and judgment over final output remain the human's responsibility even in a fully agentic pipeline.<br>*[The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)* | Humans should be removed from the loop for non-core work; with months of eval and infrastructure investment, automated review already catches 100% of issues in those categories and carries lower residual risk than an average human reviewer.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* |

*Why it matters: It determines whether captured knowledge is an input to human decisions or a replacement for them, and therefore whether throughput is capped by review capacity or by eval quality.*

## Practical Guidance

**Do:**

- Rank knowledge sources into an explicit cleanest-first hierarchy (semantic layer → canonical queries → database graph) and build the first two tiers before attempting a graph — they cover roughly 80% of enterprise data-agent questions.
- Attach provenance to every stored fact, run contradiction checks when new information collides with old, and staff a librarian (human plus agent) whose actual job is pruning.
- Make human corrections permanently outrank model-derived facts when two stored facts disagree, and put a salience gate in front of writes so the store doesn't fill with junk.
- Convert every agent task that succeeds into a reusable skill file — if you have to ask for the same thing twice, the capture failed.
- Structure retrieval as index → executive summary → wiki derivative → raw source so the agent can stop at the cheapest layer that answers the question.
- Keep hand-authored notes immutable and write all generated content into a separate derivative layer the LLM owns.
- Update the knowledge base from questions asked of it, not just from ingestion — every query should leave a trace.
- Retrain or refresh agents quarterly against closed-won and closed-lost outcomes so ICP and definition drift don't accumulate silently.
- Engage data owners directly to capture field semantics, join logic, data limitations, and security trimming; this cannot be inferred from the data itself.
- Compute eval ground truth by running a stored query against the live graph at runtime rather than freezing expected answers, when the underlying data changes constantly.
- Feed eval gaps and ambiguities back into the data model, domain rules, and schema descriptions — treat evals as a data-modeling feedback loop, not a score.
- Answer questions the way the organization has historically answered them under existing reporting conventions, not merely correctly.
- Default Slack channels to public, since channel-derived institutional context is only as complete as what the system can see.
- Record exploration chats and ideas into a project folder file system from the start of a project, not after.
- Pool sessions across all developers so the agent has more context than any individual engineer holds, and keep session state portable across agent products.
- Serve the knowledge platform into tools users already have via MCP instead of building another chat UI.

**Avoid:**

- Reaching for a bigger model, a longer context window, or more knowledge bases and MCP servers when answers are bad — none of these fix an unranked, unmaintained source of truth.
- Treating retrieval as the product; an uncurated store is a garbage dump with great search that returns stale facts confidently.
- Relying on hand-maintained .md files and skills as the system of record for definitions, KPIs, and processes that change faster than anyone updates them.
- Assuming Notion docs and help articles carry the tacit knowledge a PM or data owner holds in their head.
- Publishing auto-generated skills without regard for their contents or structure — most skills in circulation are low quality for exactly this reason.
- Holding large combinatorial state (e.g. a seating arrangement for 800 people) in the context window instead of deterministic code.
- Letting agents send outbound communication autonomously; every draft passes a human.
- Standing up vector databases, knowledge graphs, or semantic search for a personal or small-team research system where markdown and a reference index suffice.
- Building your own AI Slackbot over internal knowledge — the prompt-injection attack surface is too large.
- Conflating fit score with intent score, or flagging everything as hot; reps stop acting and stop trusting the system.
- Shipping AI-drafted output that takes a human longer than 30 seconds to edit — past that, people revert to doing it themselves and the initiative is dead.
- Assuming tool access alone drives adoption; without champions, experimentation space, and real agency, the behavior change doesn't happen.

## Notable Outliers

- A 100-person factory with no data scientists built a 39-agent company brain for ~$30k against a $230k agency quote, with zero training cost — the expensive part was teaching the company to remember itself, and the resulting architecture is transferable but the knowledge is not, so the only sellable product is an empty forkable shell. ([The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [8:28](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=508s))
- The memory/company-brain layer should be open source infrastructure like Linux rather than a proprietary profit center — the moat is the accumulated brain, not the software that holds it. ([Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [17:22](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=1042s))
- Structure, not taste, is the scarce and expensive input — clean tagged PRs, accurate diffs, real documentation — and almost no organization actually does it, which is why AI rewards conscientiousness over raw engineering skill. ([Content Is Code](../talks/content-is-code.md), [6:42](https://www.youtube.com/watch?v=yv6xovSsB1U&t=402s))
- Institutional memory should be session-portable across vendors: resume a colleague's session on your machine with exact state and zero setup, and continue a Claude session in Codex mid-stream. ([A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [14:37](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=877s))
- Preference is an unsolved research problem — two teams can compute the same metric differently and both be correct, and neither semantic layers nor memory tools (mem0, memory.md) can route to the right definition based on who is asking. ([Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [11:03](https://www.youtube.com/watch?v=B8l81jhvHbI&t=663s))
- Loading the real open-source repository into a session beats documentation-retrieval tools like Context7, because with the actual code the agent can go deep instead of reading someone's summary of it. ([A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [18:35](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1115s))

## All Talks

- [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)
- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Content Is Code](../talks/content-is-code.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Cat Wu](../speakers/cat-wu.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Ishita Daga](../speakers/ishita-daga.md)
- [Leo Mehr](../speakers/leo-mehr.md)
- [Mike Phipps](../speakers/mike-phipps.md)
- [Nicholas Arcolano](../speakers/nicholas-arcolano.md)
- [Paul Iusztin](../speakers/paul-iusztin.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Sajjan Kanukolanu](../speakers/sajjan-kanukolanu.md)
- [Sanja Grbic](../speakers/sanja-grbic.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Victor Savkin](../speakers/victor-savkin.md)

