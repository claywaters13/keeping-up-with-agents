---
title: "institutional knowledge capture"
type: "concept"
slug: "institutional-knowledge-capture"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 14
---

# institutional knowledge capture

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **14** speaker(s)

**Definition:** Turning tacit organizational and team knowledge into durable, retrievable artifacts that agents and people can both use.

*Also referred to as: tacit organizational knowledge, company brain, team memory, second brain systems, organizational knowledge sharing, knowledge base as context repository, file-based knowledge bases*

## State of Practice

The consensus position across this conference is that the differentiator in agentic systems has moved from the model to the knowledge layer around it: identical frontier models produce wildly different results depending on what organizational context they can retrieve, and 'bad answer → bigger model / longer context / more MCP servers' is explicitly named as the wrong reflex. Practitioners are converging on an architecture with four parts: an explicit hierarchy of sources of truth (semantic layer and canonical queries first, graph or raw stores last), a derivative layer of agent-generated artifacts (wikis, skills, procedures) kept separate from hand-authored source notes, hygiene machinery (provenance, salience gating, contradiction resolution where human corrections win, active pruning), and a feedback loop that writes corrections, wins/losses, eval failures, and answered questions back into context. Two failure modes dominate the reports: hand-maintained .md files and skills rot faster than enterprise definitions change, and an uncurated store becomes 'a garbage dump with great search' that returns stale facts confidently. The hardest unsolved problems named are preference routing (two teams computing the same metric differently, both correct, with no way to route by requester identity), memory compaction, and getting genuinely tacit knowledge — what a PM or data owner holds in their head — into a durable artifact at all. Economically, several speakers argue the accumulated brain is the only durable moat, since model quality is rented; costs cited are low ($30K to build a 39-agent factory brain, a couple thousand a month to run, zero training spend).

## Consensus

### Agent quality is bounded by the organization and retrievability of captured knowledge, not by model capability — swapping in a bigger model or longer context does not fix bad answers.

Support: **6** talk(s)

> "The brain isn't a smarter model. It's actually a really, really well-organized memory."
>
> — [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [2:37](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=157s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Content Is Code](../talks/content-is-code.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### Without an explicit external memory layer, every session restarts from zero and the human is forced to act as the organization's memory; the durable artifact, not the model, is what compounds.

Support: **4** talk(s)

> "The organization that captures what it learns like this gets smarter every single day. The one that doesn't wakes up every morning with amnesia, no matter how good the model is. Model quality is rented, but if you build your brain, you you own that brain."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [16:06](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=966s)

Supporting talks: [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### A knowledge store requires active hygiene — salience gating on write, provenance, contradiction detection with a deterministic precedence rule, and pruning — or retrieval surfaces stale facts with full confidence.

Support: **5** talk(s)

> "A salience gate that decides what's even worth remembering, so the brain doesn't fill up with junk. When two facts disagree, corrections win."
>
> — [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [6:49](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=409s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### Capture must be a closed loop: corrections, answered questions, closed-won/closed-lost outcomes, and eval failures have to be written back into the knowledge layer, not just ingested once.

Support: **5** talk(s)

> "every send, every reply, and every closed deal should make the model smarter, should make your system smarter"
>
> — [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [25:54](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1554s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)

### Existing documentation and knowledge bases are insufficient because the knowledge that matters is tacit — held by data owners and PMs — and must be actively elicited from them rather than inferred from artifacts.

Support: **3** talk(s)

> "Imagine like all the knowledge that a product manager has in their head about their product. Like, how do you get that into an agent?"
>
> — [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [11:55](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=715s)

Supporting talks: [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Content Is Code](../talks/content-is-code.md)

### Captured knowledge should be materialized as reusable executable artifacts (skill files, written procedures) rather than prose, and every successful one-off task should be promoted into one.

Support: **4** talk(s)

> "The AI-native companies that I see inside YC encode all of that as skills, written procedures that their agents execute, and they hire they hire engineers whose job it is to maintain those skills, to do the work the skills can't do yet."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [6:25](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=385s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Content Is Code](../talks/content-is-code.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)

## Disagreements

### Does an agent-facing institutional knowledge layer need modeled structure (semantic layer, property graph, dependency graph), or are plain markdown files and a reference index sufficient?

| Position A | Position B |
|---|---|
| Build modeled structure: a ranked semantic layer over canonical queries, a property graph the agent can discover and traverse at query time, or an extracted cross-repo dependency graph. Files cannot express which source is authoritative, how fields join, or how entities relate.<br>*[Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)* | Skip the infrastructure: plain markdown plus a reference-based index, wiki derivative layers, and per-channel or per-skill markdown files. Vector DBs, knowledge graphs, and semantic search are explicitly named as things to forget for this use case.<br>*[Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* |

*Why it matters: The graph camp is committing months of data modeling, data-owner interviews, and eval-driven schema iteration before the agent works at all; the file camp ships in a weekend and treats retrieval as trivially solved. The split partly tracks scope — the file advocates work over personal or team-scale corpora while the graph advocates span thousands of employees and systems of record — but both camps are shipping to production, so the crossover point is undefined.*

### Should the durable knowledge layer be deliberately authored by humans as an organizational discipline, or extracted automatically from live systems because humans will not maintain it?

| Position A | Position B |
|---|---|
| Derive it. Hand-maintained .md files and skills go stale faster than enterprise definitions, KPIs, and processes change, so context should be sourced from continuously-updated systems (GitHub, dbt, CRM, Tableau), extracted repo metadata, and pooled agent sessions.<br>*[Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)* | Author it. Clean tagged PRs, real descriptions, documented async practices, curated skills, and recorded exploration sessions are the scarce input; AI rewards conscientiousness and organizational excellence, and the fix is instilling that discipline rather than routing around it.<br>*[Content Is Code](../talks/content-is-code.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)* |

*Why it matters: This decides whether you staff librarians and skill maintainers and change human process, or build extraction pipelines and treat human-written docs as untrustworthy. It also determines whether an org with poor documentation hygiene is blocked from agentic work or can bootstrap around it.*

### Once institutional knowledge is captured well enough, can the human be removed from the output loop?

| Position A | Position B |
|---|---|
| No — the human gate is permanent by design. Agents draft, humans send; taste and judgment over the final output remain a human responsibility even in a fully agentic pipeline.<br>*[The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)* | Yes — removing humans from the loop is the explicit goal, achievable with months of eval and infrastructure investment; automated review already catches 100% of issues on non-core changes and lands 65% of product PRs.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* |

*Why it matters: If the human gate is permanent, the knowledge layer only needs to be good enough to draft, and review capacity caps throughput; if it can be removed, the captured knowledge plus eval suite becomes the entire quality bar and the investment shifts from reviewers to evals.*

## Practical Guidance

**Do:**

- Rank knowledge sources into an explicit hierarchy — semantic layer, then canonical queries, then database graph — and consult cleanest-first; build the first two tiers before attempting the graph, since they cover roughly 80% of enterprise data-agent questions.
- Log every user correction event and feed it back into agent context, and retrain agents quarterly on closed-won and closed-lost data to counter ICP/definition drift.
- Keep hand-authored notes immutable and write all agent-generated content into a separate derivative layer (index → executive summary → wiki → raw source), which is also more token-efficient to retrieve from.
- Give enrichment agents a fixed reference list of tags and instruct them to be reluctant to add new ones; stamp each processed note with an enrichment timestamp so repeat passes only touch unprocessed notes.
- Attach provenance to every fact, run contradiction checks when new information collides with old, and assign a named librarian (human plus agent) whose actual job is pruning.
- Promote every agent task that succeeds into a reusable skill file — if you have to ask for the same thing twice, the capture failed.
- Interview data owners directly for field semantics, join logic, data limitations, safeguards, and security trimming; validate baseline assumptions with the customer before building on them.
- Compute eval ground truth at runtime by running a stored query against the live graph rather than freezing expected answers, and route eval failures back into the data model and schema descriptions.
- Expose the knowledge layer through MCP into tools people already use rather than building another chat UI, and expect off-the-shelf MCP servers to need forking and state-passing for production use.
- Mask PII, classify sensitivity, and enforce per-user entitlements inside the curation pipeline, because AI makes theoretically-accessible data practically accessible.

**Avoid:**

- Responding to bad agent answers by reaching for a bigger model, a longer context window, or more knowledge bases and MCP servers.
- Weighting all knowledge bases equally so the agent has no signal about which source holds the truth.
- Relying on hand-maintained .md files and skills as the mechanism for definitions, KPIs, and processes that change frequently — the context rots.
- Publishing agent-generated skills without curating their contents or structure; most skills in circulation were generated with no regard for either.
- Letting the LLM write into your hand-authored personal notes instead of a separate generated layer.
- Treating retrieval as the product — an uncurated brain becomes a garbage dump with great search that returns stale facts confidently.
- Letting agents send outbound communication autonomously; drafts should pass a human.
- Holding large combinatorial state (e.g. a seating chart for 800 people) in the context window instead of deterministic compute.
- Automating an intake or request pipeline without scoping discipline, which produces high-volume low-quality output.
- Conflating fit score with intent score, or flagging everything as hot — reps stop acting and stop trusting the system.
- Assuming tool access alone drives adoption in a large org; without champions, experimentation space, and agency the behavior does not change.

## Notable Outliers

- The architecture of a company brain is transferable but the knowledge is not, so the correct product to ship other companies is an empty forkable shell — no vendor can build your brain for you. ([The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [9:13](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=553s))
- Structure — clean tagged PRs, real descriptions, knowing what was reverted — is the expensive scarce input in AI-assisted production, not taste; and essentially no organization actually does it. ([Content Is Code](../talks/content-is-code.md), [6:42](https://www.youtube.com/watch?v=yv6xovSsB1U&t=402s))
- The knowledge/memory layer should be open-source infrastructure like Linux rather than a proprietary profit center. ([Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [17:22](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=1042s))
- Preference — two teams computing the same metric correctly but differently — is unsolved by both semantic layers and agent memory; the answer is routing to the right definition by requester identity, and neither frontier labs nor industry have it. ([Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [11:03](https://www.youtube.com/watch?v=B8l81jhvHbI&t=663s))
- Pooling agent sessions across all developers in an organization gives the agent more context than any single developer possesses, and that session state should be portable enough to resume someone else's work in a different agent product. ([A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [19:13](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1153s))
- Once eval scores are strong, remaining failures are dominated by user-intent ambiguity rather than factually wrong answers — the answer is right, just not what the user meant. ([Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [19:08](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1148s))
- Claude Tag's accuracy depends on Slack channels being public, so knowledge-capture accuracy becomes an argument for defaulting the whole organization to public channels. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [45:17](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=2717s))
- Loading the real open-source repository into a session beats documentation-retrieval tools like Context7 for deep diagnosis — source code is a better knowledge artifact than docs about it. ([A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [18:35](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1115s))

## All Talks

- [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)
- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Content Is Code](../talks/content-is-code.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Ben Holmes](../speakers/ben-holmes.md)
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

