---
title: "entity resolution"
type: "concept"
slug: "entity-resolution"
tier: "supporting"
maturity: "consolidating"
talk_count: 8
speaker_count: 9
---

# entity resolution

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **8** talk(s) by **9** speaker(s)

**Definition:** Deciding when records across sources refer to the same real-world thing, and merging them without collapsing distinct entities.

*Also referred to as: entity resolution across source systems, graph-based entity resolution, hierarchical entity resolution, adaptive name resolution, deduplication checks, entity enrichment, cross-document correlation*

## State of Practice

Across this conference, entity resolution showed up less as a standalone discipline than as the step that silently breaks everything downstream — graph construction, cross-system compliance correlation, process mapping, and infrastructure telemetry all failed at the same place: deciding whether two near-identical names refer to the same thing. The consistent finding is that an LLM asked to normalize entities inside a prompt is not a resolver; speakers converged on a pipeline of (a) a domain schema plus explicit ontology instructions on naming and unit standardization at extraction time, (b) a separate, dedicated matching step after extraction, and (c) deterministic code for anything that must be reproducible — exact set logic, counting, dedup across near-identical strings. The mechanism for that matching step is where the field splits: Good Collective argues embedding similarity beats hand-curated mapping precisely because you cannot enumerate entities in advance, while Phaidra reports that on 500,000 data-center sensors the names are so similar that semantic search collapses, and pushes resolution into deterministic set operations. Everyone agreed the failure mode is silent — phantom entities invented, real ones dropped, two Mikes merged — which is why the value case (fraud spanning documents, citation paths, cross-system enterprise queries) is also the risk case. The normalization and join semantics themselves are treated as human-elicited, not inferable: Gates Foundation insists data owners must supply field semantics and join logic, and Phaidra notes the industry has no common naming convention at all.

## Consensus

### The signal that matters lives between records, not within them — resolution and linkage across sources is what surfaces facts no single-document or single-system pipeline can reach.

Support: **3** talk(s)

> "First is many of today's most significant compliance and fraud risk exist between the documents, not within them."
>
> — [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [17:07](https://www.youtube.com/watch?v=Iwe_RY-fYgI&t=1027s)

Supporting talks: [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)

### Resolution quality is set upstream by an explicit domain schema, naming/unit standardization rules, and a normalization layer — not by the matching algorithm alone; without it, the same real-world thing is represented (and scored) inconsistently across sources.

Support: **4** talk(s)

> "Without normalization, the same transaction can be interpreted differently depending on the jurisdiction."
>
> — [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [8:21](https://www.youtube.com/watch?v=Iwe_RY-fYgI&t=501s)

Supporting talks: [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)

### Prompting a frontier LLM to keep entities straight is not a resolution mechanism; a separate, purpose-built matching step (deterministic code or a dedicated tool) is required.

Support: **3** talk(s)

> "These tools are things like make sure person A and person B are actually the same person because a lot of you know, there's a lot of Mikes in every company we work with and Claude gets very confused by this."
>
> — [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [17:14](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1034s)

Supporting talks: [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)

### Entity-resolution failures are silent and arrive wrapped in plausible output — invented entities, dropped entities, wrongly merged people — so they must be caught by explicit checks rather than by inspecting the artifact.

Support: **3** talk(s)

> "The problem is you get horrible recall and hallucinations. You will see LLMs invent phantom equipment that do not exist, and also silently drop things that do exist."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [3:36](https://www.youtube.com/watch?v=EUsPvBeIx70&t=216s)

Supporting talks: [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)

## Disagreements

### Should entity matching be done by embedding similarity, or by deterministic set logic over structure?

| Position A | Position B |
|---|---|
| Embedding-based matching over entity names is the right default, because it does not require knowing all entities in advance and avoids the retrospective, hand-curated mapping trap; graph plus AI techniques in hybrid give the best result.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)* | Semantic/vector similarity is exactly what breaks on near-identical names — recall collapses and the model hallucinates — so dedup, counting, and exact set logic belong in deterministic 1.0 code, with the LLM restricted to planning the search and never performing it.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)* |

*Why it matters: It decides whether you invest in an embedding index and thresholds or in a canonical hierarchy plus set operations, and whether your resolution accuracy degrades with entity count (Phaidra measured 80% → 30% correctness from 64 to 460,000 instances) or stays flat.*

### Does resolved entity data need a graph database, or is the graph just a representation you can hold anywhere?

| Position A | Position B |
|---|---|
| A property graph is the enabling substrate: multi-hop traversal and subgraph matching are things vector search and SQL cannot practically do, and agents should dynamically discover and traverse the schema at query time.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)* | The choice of graph database is unimportant — Postgres is fine; what matters is having a dependency-graph representation of the process, since real enterprise workflows are mostly linear with cycles.<br>*[AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)* |

*Why it matters: It changes whether resolution work is a database migration and a new query language for the team, or a modeling exercise on top of the systems of record enterprises already spent years and millions migrating onto.*

## Practical Guidance

**Do:**

- Give the extractor a domain schema up front, plus separate ontology instructions covering entity naming and unit standardization — treat those instructions as equal in importance to the schema itself.
- Run a dedicated matching step after extraction rather than relying on the extraction prompt to have standardized names consistently.
- Put anything that must be 100% reproducible — exact set logic, counting, dedup across near-identical names — in deterministic code, and use the LLM to plan the search rather than perform it.
- Scale the context you give the model with hierarchy depth (enumerate root-to-leaf paths) instead of with instance count, so a 64-instance and a 460,000-instance system cost roughly the same per query.
- Ship an explicit 'are A and B the same entity?' tool for the agent to call, rather than assuming the model tracks identity across a large context.
- Engage data owners directly to capture field semantics, join logic, data limitations, and security trimming — this cannot be inferred from the data alone.
- Add a normalization layer before cross-jurisdiction or cross-system scoring, so identical records are not scored differently by source.
- For evals over constantly-changing entity data, store the graph query and compute ground truth from the live graph at runtime instead of freezing expected answers.
- Instrument the most expensive handoff first — the one where bad or wrongly merged data costs the most — and make that gate blocking.

**Avoid:**

- Free-form subject-predicate-object triple extraction with no schema — the resulting graph is one you 'wouldn't get very far with'.
- Sharding entity names across parallel LLM calls to work around context limits: it produces hallucinated entities and silent omissions, disqualifying for mission-critical systems.
- Vector/semantic retrieval as the matching mechanism when entity names are near-identical strings; embeddings become indistinguishable and recall degrades.
- Hand-curated mapping tables applied retrospectively, which only work if you already know every entity ahead of time.
- Asking a model to enumerate many similar entity names in one output — frequency penalties cause it to truncate or shut off mid-list.
- Gates that only log warnings on a failed identity or contract check; a gate that does not halt the artifact is a suggestion.
- Validating documents or records independently when the risk you care about is a pattern spanning several of them.
- Open-ended multi-step agentic loops for resolution when a two- or three-step plan-then-resolve pipeline keeps cost flat and bounded.

## Notable Outliers

- Frontier models have no concept of which details a client cares about, and post-trained open-source models beat them at writing normalized process flows from extracted context. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [16:40](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1000s))
- Replacing LLM scanning with deterministic resolution cut a 1GW-scale validation pass from 116 million tokens to 390,000 — roughly 300x — while moving correctness from ~30% to 100%. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s))
- AI-native systems should run Karpathy's drift backwards: start at software 3.0 by throwing everything in the context window, then migrate toward 1.0 for the use cases that earn it. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s))
- Building your own entity extraction pipeline breaks even against renting context at just over 15,000 entities or queries, assuming about a week and $5,000 of setup — a far lower tipping point than most teams assume. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [18:59](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1139s))
- Graph-based subgraph retrieval cut tool calls for code search by 40% on a .NET codebase, surfacing intermediate nodes that neither vector search nor symbol/reference lookup would have found. ([A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [10:28](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=628s))
- Once eval scores are strong, remaining failures are dominated by user-intent ambiguity rather than factually wrong answers — the answer is right, just not what was meant. ([Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [19:08](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1148s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)
- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)
- [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)
- [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Mike Phipps](../speakers/mike-phipps.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Ramesh Raskar](../speakers/ramesh-raskar.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Tim Ainge](../speakers/tim-ainge.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)
- [Varsha Shah](../speakers/varsha-shah.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)

