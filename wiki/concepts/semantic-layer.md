---
title: "semantic layer"
type: "concept"
slug: "semantic-layer"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 11
---

# semantic layer

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **11** speaker(s)

**Definition:** A governed modeling layer over business data that gives metrics and entities canonical definitions models can query without inventing joins.

*Also referred to as: semantic layer for business data, metadata layer modeling, dimensional modeling, business ontology, text-to-sql, canonical queries, system of record data*

## State of Practice

Across every talk that touched it, the semantic layer has stopped being a BI artifact and become the load-bearing substrate for enterprise agents: a governed mapping from business-language concepts (metrics, KPIs, entities, join logic, reporting conventions) down to physical data assets, exposed to agents through MCP or tools rather than baked into prompts. The field's shared diagnosis is that model capability is no longer the constraint — bad answers come from an agent that cannot tell which table, which knowledge base, or which of two equally-correct metric definitions to use, and a bigger model, a longer context window, or another MCP server does not fix that. The emerging reference architecture is thin agents over a shared, versioned layer with three parts: a business ontology in human language, a technical ontology of data-source metadata, and runtime execution traces that score which sources actually worked; per-agent memory and hand-maintained .md files are widely treated as anti-patterns because context gets trapped, sprawls, and rots. Practitioners insist the layer sits over systems of record rather than replacing them — Neo4j's lakehouse pattern pulls only warehouse metadata into a graph, forward-deployed teams refuse to make clients migrate off NetSuite, and DataChain rejects both JSON sidecars and a separate metadata database. What is genuinely unsettled is the substrate (property graph/ontology vs. Postgres and star schemas), whether a metric has one canonical definition or requires identity-based routing to per-team definitions, and how much of the layer survives as text-to-query capability improves. Nearly everyone converges on the same economic claim: once competitors share the same models, the modeled understanding of your business — not the model — is the moat.

## Consensus

### Business context, not model intelligence, is the binding constraint on production agent value — capability has outrun the organization's ability to supply canonical semantics.

Support: **6** talk(s)

> "Intelligence has 1,000x'd in the last decade. Just in the last 6 months, we have 2x'd on that axis. On the other hand, context, the situated knowledge of your business, that's barely moved."
>
> — [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [3:17](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=197s)

Supporting talks: [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)

### The semantic layer must live outside any individual agent as a shared substrate; per-agent memory and per-agent hardwiring produce context sprawl, no single version of truth, and no cross-agent learning.

Support: **4** talk(s)

> "the pattern that is emerging is that in order to do things at scale, we need thin agents on a smarter shared substrate."
>
> — [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [4:13](https://www.youtube.com/watch?v=VGN22pPpb-8&t=253s)

Supporting talks: [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

### Without a canonical-definition layer, agents silently apply the wrong business semantics and return confidently wrong answers that are indistinguishable from correct ones.

Support: **4** talk(s)

> "And if you ask Claude to do something like report on revenue, it doesn't say, "I'm not sure." It says, "Here you go." And it gives you a wrong answer that looks exactly like being right."
>
> — [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [7:18](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=438s)

Supporting talks: [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

### Hand-maintained markdown files and skills are not a sufficient semantic layer at enterprise scale — definitions change faster than documents can be updated, and the context rots.

Support: **3** talk(s)

> "we've seen a ton of team that tried to solve this problem using just Markdown files. And the summary is it is part of the solution, but it is not the solution."
>
> — [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [3:31](https://www.youtube.com/watch?v=VGN22pPpb-8&t=211s)

Supporting talks: [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

### Runtime execution traces, correction events, and eval failures should feed back into the semantic layer itself, making source selection and schema descriptions improve over time rather than staying static.

Support: **4** talk(s)

> "And then the third pillar is the run time signals out of your agents. When they walk this graph and they execute, they leave the traces around."
>
> — [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [5:45](https://www.youtube.com/watch?v=VGN22pPpb-8&t=345s)

Supporting talks: [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

### The layer should sit over data where it already lives — model metadata and mappings, do not relocate or re-platform the underlying data.

Support: **3** talk(s)

> "the thing that we're doing here really is we're not using the graph to copy the data over. There's not like an ETL into graph. What we're doing is we're using the graph as a semantic layer."
>
> — [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [26:43](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=1603s)

Supporting talks: [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

### The modeled semantics of the business — not the model, agent framework, or UI — is the durable competitive moat once everyone has the same frontier models.

Support: **3** talk(s)

> "the moat here is that it's not about the model access, it's about the data itself that you have."
>
> — [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s)

Supporting talks: [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

## Disagreements

### Does the semantic layer require a graph/ontology substrate, or is a relational one (Postgres, star schemas, Pydantic-to-SQL) sufficient?

| Position A | Position B |
|---|---|
| A property graph or ontology is the right representation, because business concepts, technical assets, processes, and traces are all linked and must be traversed together, and agents can dynamically discover the schema at query time.<br>*[Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)* | The storage engine is incidental or actively wrong for most teams: the dependency-graph representation matters but 'you can just use Postgres'; the graph is the highest-effort, hardest-to-maintain tier and should be built last if at all; decades-old dimensional modeling (star schema, one big table) applied to metadata is underused.<br>*[AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)* |

*Why it matters: This determines whether a team's first six months go into ontology modeling and a graph database or into curated metric definitions over existing SQL infrastructure. Ishita Daga's claim that the semantic layer plus canonical queries covers ~80% of enterprise data-agent problems directly implies the graph investment is premature for most teams.*

### Should the semantic layer enforce one canonical definition per metric, or resolve to different per-team definitions?

| Position A | Position B |
|---|---|
| A single version of truth is the point of the layer — inconsistent definitions across autonomous agents reproduce the sales-vs-finance revenue discrepancy at machine scale, and an answer is only correct if it matches how the question has historically been answered under existing reporting conventions.<br>*[WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)* | Two teams routinely compute the same metric in different but equally correct ways, so there is no 'right' definition to canonicalize; semantic layers only push the ambiguity back onto the user by requiring them to prompt for a choice, and the real fix is automatic routing to a definition based on who is asking.<br>*[Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)* |

*Why it matters: If definitions are singular, the layer is a governance artifact and the work is getting stakeholders to agree. If they are plural, the layer needs an identity/context routing mechanism that essentially nobody has built — Daga calls it an unsolved research problem.*

### As text-to-query capability improves, should the layer expand into precomputed canonical queries or shrink toward metadata plus free-form generation?

| Position A | Position B |
|---|---|
| Curate and serve canonical queries and pre-built metadata layers: a vetted list of KPI definitions and query shapes is the cleanest tier of the source-of-truth hierarchy, and an agent should first ask whether a prebuilt layer can answer the question in a single SQL-ish query rather than running code over raw data.<br>*[Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)* | Agent-written queries plus CLI/skills are now good enough that agents will increasingly prefer free-form Cypher over calling prebuilt shape scripts, and structures previously required in the data model (dedicated entity nodes) can often be dropped.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)* |

*Why it matters: It sets whether ongoing investment goes into curating and maintaining a growing query library — which is real headcount — or into richer schema description and letting the model compose. Note the position-B speaker explicitly states none of these claims were benchmarked.*

### Once a good semantic layer exists, does model class still matter for the agent on top of it?

| Position A | Position B |
|---|---|
| Grounding beats model size: a mid-size cheaper model grounded in outcome data outperformed frontier models head-to-head, post-trained open-source models beat Claude at writing normalized process flows, and an SLM suffices for a context-fed fraud agent under a sub-500ms SLA.<br>*[Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)* | Model and harness quality are non-negotiable regardless of the layer — 'you can't fix stupid'; an acceptable harness needs a powerful model plus sub-agents, plan mode, full MCP support and file editing, and AI crammed into per-seat subscription products can't fund an intelligent reasoning model.<br>*[Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)* |

*Why it matters: It changes unit economics by an order of magnitude at scale, and determines whether the investment case is 'buy the best model' or 'build the proprietary grounding data and run something cheap on top.'*

### Are plain markdown files adequate infrastructure for dataset and business context?

| Position A | Position B |
|---|---|
| No — markdown is part of the solution but not the solution; hand-maintained .md files and skills cannot keep pace with changing KPIs and processes, and hardcoded context does not scale.<br>*[Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)* | Yes for dataset-level memory — a shared knowledge base of plain markdown files per dataset (description, source code, lineage) is sufficient infrastructure for both agents and humans.<br>*[When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)* |

*Why it matters: Determines whether context is a filesystem convention a team adopts this week or a versioned system with approvers, dependency tracking, and lifecycle management. The disagreement may partly reduce to scale: unstructured-data research teams vs. multi-hundred-source enterprises.*

## Practical Guidance

**Do:**

- Rank knowledge sources into an explicit hierarchy — semantic layer, then canonical queries, then the database graph — and have the agent consult cleanest-first rather than weighting all knowledge bases and MCP servers equally.
- Build the semantic layer and canonical query tiers first; they cover roughly 80% of enterprise data-agent problems and are cheap to set up, while the database graph is the high-effort remaining 20%.
- Model exactly three pillars plus the mapping between the first two: a business ontology in language every human in the org understands ('customer' with a 'first name', not `if_name`), a technical ontology of all data-source metadata, and runtime execution traces.
- Source context from live, continuously-updated systems (GitHub, CRM, Tableau, dbt) rather than static documents that rot.
- Score data sources both top-down by human curation and bottom-up by what execution traces show actually worked, and weight future source selection by context.
- Capture and log every correction event and feed it back into agent context; instrument evals, since teams that skip evaluation cannot tell whether the agent is improving.
- Compute eval ground truth at runtime by re-running a stored graph query against the live graph, rather than freezing expected answers, since structured data changes constantly.
- Feed eval gaps back into the data model, domain rules, and schema descriptions — treat evals as a data-modeling feedback loop, not a scorecard.
- Engage data owners directly to capture field semantics, join logic, data limitations, safeguards, and security trimming; none of this is inferable from the data itself.
- Bake PII masking, sensitivity classification, and per-user entitlements into the curation pipeline, because AI makes theoretically-accessible data practically accessible.
- Pull only warehouse metadata into the layer and keep the data in place; reserve ETL into a graph for cases needing recursive-join performance, graph algorithms, graph embeddings, or clustering.
- Attach citations back to every source system so a human can follow them and verify the important parts weren't hallucinated.
- Manage context like code: versioning, dependency management, named approvers/maintainers/contributors, quality and security posture management.
- Store the source code of a derived dataset as the single most important piece of context about it.
- Use one generic containment relationship name across hierarchy levels instead of per-level names, to keep generated Cypher simple.
- Expose the layer through MCP into tools users already have (Claude, ChatGPT) instead of building another chat UI, and complement open-ended chat with constrained workflow-shaped agent experiences over the same backend.
- Adjust for selection bias when grounding recommendations in outcome data — firms that took an action are systematically different from those that didn't.
- Route self-improving skill changes through a harness that reverse-constructs learnings from traces and sends them to a human maintainer to approve or reject.

**Avoid:**

- Reaching for a bigger model, a longer context window, or more knowledge bases and MCP servers when the agent gives a bad answer — none of these fix source-of-truth ambiguity.
- Giving each agent its own memory system; they learn separately and differently, causing context sprawl and making failures untraceable.
- Hardcoding context into agents or leaving it trapped inside an agent framework, since tooling churns roughly annually (Relevance → Google ADK → Glean → Claude Code → Claude/Codex) and the context is lost at each hop.
- Requiring customers to migrate off systems of record — one client spent $5M and 5 years moving to NetSuite and will not do it again for your tool.
- Letting a production data model accumulate hundreds of distinct relationship types; it stops fitting the context window and degrades Cypher generation.
- Storing extracted metadata as millions of JSON files next to objects in S3, and equally avoid a separate centralized metadata database that forces researchers into two systems and two languages.
- Using LLM-generated community summaries when document metadata suffices — they cost more, run slower, and are non-reproducible across runs.
- Treating graph document navigation as a replacement for semantic search; production systems need hybrid retrieval, and vector search structurally cannot answer coverage or negative questions.
- Querying the event store directly for reads instead of maintaining optimized read models.
- Running an agent loop over the layer without an explicit numeric break condition, and avoid a plain metric or if-condition as the final verdict — it reproduces the false positives of the rule engine you replaced.
- Asking Claude to improve its own prompts or behavior; it was trained on human material and will produce micromanagement.
- Turning an agent loose end-to-end without defining the structure first — plan mode alone does not make YOLO generation work today.
- Treating a transcript as proof of what happened; only a receipt recording what was allowed, attempted, executed, and confirmed at the user-visible edge counts.
- Redesigning a process into so few steps that operators no longer recognize it — an 11-step workflow collapsed to one step tanks adoption even if it is more efficient.

## Notable Outliers

- Semantic and vector search structurally cannot answer coverage or negative questions like 'what documentation are we missing,' because they can only match similar things — a graph-shaped layer is required to prove a negative. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [5:14](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=314s))
- In Princeton's 500-day business simulation, most frontier models drove the company bankrupt in under 500 days and a simple rules-based system outperformed almost all of them. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s))
- Anthropic published that agent accuracy on data projects is only 21% until you add a purpose-built data harness and supply context — and this measured structured data, so it understates the problem for unstructured data. ([When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [0:02](https://www.youtube.com/watch?v=bUJgirn4_yc&t=2s))
- Neither semantic layers nor agent memory solves the preference problem: the former makes the user prompt for a choice, the latter can't tell which of two correct metrics applies when — the answer is routing by requester identity, and the industry has not solved it. ([Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [10:21](https://www.youtube.com/watch?v=B8l81jhvHbI&t=621s))
- The choice of graph database is unimportant — five vendors downstairs are selling you one and you can just use Postgres; what matters is the dependency-graph representation of the process. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [15:17](https://www.youtube.com/watch?v=l0FLhNqBOic&t=917s))
- Modern agents are capable enough that dedicated entity nodes previously required in a graph data model can often be omitted entirely, with life-sciences ontologies as the counterexample. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:07:53](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=4073s))
- Extracting the right context out of a large knowledge graph is a distinct and harder problem than generating good output from context, and is best solved with RL-trained custom traversal tools — including entity resolution like confirming two 'Mikes' are the same person. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [17:51](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1071s))
- Once eval scores are strong, the remaining failures are dominated by user-intent ambiguity rather than factually wrong answers — the answers aren't wrong, they're just not what the user meant. ([Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [19:08](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1148s))
- None of the efficiency or accuracy claims made in this graph-as-semantic-layer workshop were benchmarked by the speaker. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:54:56](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=6896s))

## All Talks

- [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)
- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)
- [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)
- [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)
- [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Alex Bauer](../speakers/alex-bauer.md)
- [Divakar Kumar](../speakers/divakar-kumar.md)
- [Emil Eifrem](../speakers/emil-eifrem.md)
- [Ishita Daga](../speakers/ishita-daga.md)
- [Mike Phipps](../speakers/mike-phipps.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Udi Menkes](../speakers/udi-menkes.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Zach Blumenfeld](../speakers/zach-blumenfeld.md)

