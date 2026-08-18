---
title: "ontology design"
type: "concept"
slug: "ontology-design"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 9
---

# ontology design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **9** speaker(s)

**Definition:** Defining the entity types and relationships of a domain as an explicit schema that agents and graphs are built on.

*Also referred to as: ontology engineering, ontology modeling, domain ontology modeling, entity relationship modeling, firm-specific ontologies, technical ontology, organizational context modeling*

## State of Practice

The field has converged on a blunt claim: agents cannot infer a domain's entity types and relationships at runtime, and every serious deployment presented here front-loads that schema as an explicit artifact. Free-form triple extraction and "let the agent read the tables" both fail the same way — ZS reported agents fabricating relationships that don't exist in the data, and Good Collective reported unschematized subject-predicate-object graphs you "wouldn't get very far with." The ontology is increasingly treated not as a data model but as a runtime control surface: Neo4j pushes discovery, mapping, and source-trust logic down into a shared semantic layer (business ontology + technical ontology of data-source metadata + a mapping + execution traces) so agents can stay thin; ZS uses the knowledge graph to bound which investigation hypotheses an agent may pursue at all, one hypothesis per edge; UC Berkeley runs OWL domain/range and cardinality constraints as a post-LLM validator before any write. A parallel thread from finance and forward-deployed engineering reframes the ontology as organizational rather than universal — Kepler's position is that verification means conforming to one firm's "nouns and verbs," since two desks can read identical data in opposite directions. The live arguments are about authorship (hand-written OWL versus embedding-learned matching and trace-derived source scores), reuse (schema.org versus bespoke), and whether an enterprise should be forced onto one canonical vocabulary at all.

## Consensus

### Agents and extractors must be given an explicit domain schema; letting an LLM infer entities and relationships from raw data or free text produces unusable or fabricated structure.

Support: **4** talk(s)

> "the agent was looking at data, looking at tables, then trying to infer the relationship. That which was not scalable. And it often produce relationship which which is not actually exist in the data."
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [9:11](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=551s)

Supporting talks: [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

### The ontology should be expressed in the organization's own business vocabulary and rules rather than in database-level naming — it encodes a firm's definitions, not universal truth.

Support: **4** talk(s)

> "you don't say if underscore name. No, you have a customer and they have a first name."
>
> — [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [4:56](https://www.youtube.com/watch?v=VGN22pPpb-8&t=296s)

Supporting talks: [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

### The ontology/graph is a control and guardrail layer that constrains what an agent may do or conclude, not merely a lookup or retrieval layer.

Support: **4** talk(s)

> "the knowledge graph is not just something the agent looks up for data. It is a control plane for the agent."
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [10:32](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=632s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)

### Prompt text, markdown files, and larger context windows are not substitutes for a structured schema; constraints that are trivial to state formally are unreliable to enforce in natural language.

Support: **4** talk(s)

> "A second refund on the same order is a is is a problem. But ontologies could catch it, whereas it's it's very tricky to do that in in English."
>
> — [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [18:58](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1138s)

Supporting talks: [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)

### Deterministic work — computation, signal detection, validation, precomputed context — belongs outside the probabilistic model, with the schema layer serving as that deterministic substrate.

Support: **4** talk(s)

> "any complex workflows will have deterministic parts and agentic parts. Don't let agents actually run the deterministic part, right?"
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [13:51](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=831s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)

## Disagreements

### Should an enterprise converge on one canonical ontology, or should the layer accommodate each team's divergent vocabulary?

| Position A | Position B |
|---|---|
| Build a single business-facing ontology expressed in language every human in the organization understands, and make it the shared substrate all agents resolve against — a formal specification of one shared conceptualization.<br>*[Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)* | Terminology divergence across sales, ops, finance, and engineering ("customers" / "clients" / "billing entities" / "org IDs") is how humans actually work and should not be eliminated by forcing one schema; the platform's leverage comes from becoming the linguistic foundation others map into, not from flattening vocabulary.<br>*[How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)* |

*Why it matters: It decides whether the ontology project is a one-time normalization effort or an ongoing mapping-and-aliasing problem, and whether disagreement about names is a defect to fix or a permanent input to model.*

### Should teams adopt existing public ontologies or author a bespoke domain schema?

| Position A | Position B |
|---|---|
| Reuse the taxonomies people have refined for 15–20 years — schema.org, FOAF, Dublin Core, DBpedia — instead of reinventing the wheel, and get OWL inference for free.<br>*[Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)* | The value is in the domain-specific schema: a custom extraction ontology with naming and unit standardization instructions, a business ontology mapped to your own data-source metadata, or a KG of your own metrics and entities that defines the agent's hypothesis space.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)* |

*Why it matters: Starting from a public vocabulary buys standard reasoners and interoperability but rarely covers the firm-specific rules that verification actually depends on; starting bespoke means writing and maintaining every constraint yourself.*

### Should the mapping between vocabulary and data be hand-curated or learned from signals?

| Position A | Position B |
|---|---|
| Learn it: embedding-based entity matching beats hand-curated mapping because you cannot know all entities in advance, source trustworthiness should be scored bottom-up from execution traces, and per-user structure should be computed offline from thousands of behavioral data points.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)* | Author it formally: OWL classes, domain/range, and cardinality constraints checked by a deterministic reasoner, or explicit graph edges enumerating the hypotheses an agent is permitted to evaluate — anything probabilistic in the validation path defeats the purpose.<br>*[Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)* |

*Why it matters: Learned mappings scale to open-world data but reintroduce probability into the layer that was supposed to constrain the model; hand-authored ones are auditable and repeatable but cap the domain at what someone wrote down.*

## Practical Guidance

**Do:**

- Give the extraction model a domain schema plus explicit naming and unit standardization instructions — the instructions matter as much to output quality as the schema itself.
- Follow extraction with a separate entity-matching step (embedding-based) rather than trusting prompt-level standardization to deduplicate entities.
- Structure the semantic layer as three pillars: a business-facing ontology, a technical ontology of all data-source metadata, and runtime execution traces — plus an explicit mapping between the first two.
- Score data sources both top-down by human curation and bottom-up by what execution traces show actually worked, so source selection improves across agents over time.
- Validate LLM output against ontology constraints before any database write: Pydantic at the door for types, ontology at the ledger for semantics, and keep agents side-effect-free until validation passes.
- Encode constraints that natural language can't reliably enforce — duplicate refunds, payouts to the wrong entity type, invalid status values — as OWL properties.
- Treat each graph edge as one hypothesis the agent is allowed to evaluate, and forbid investigation outside that boundary.
- Precompute contextual structure offline on a schedule rather than assembling it at query time; split it into a slow engine that learns durable patterns and a fast engine that recomputes live signals over recent activity.
- Let the model decide what to compute and route the arithmetic to code — it is both more correct and cheaper than running 1+1 through a multi-billion-parameter model.
- Isolate data sources behind a serve-time verification layer that falls back to last-verified context, so a bad feed degrades the system instead of breaking it.

**Avoid:**

- Free-form subject-predicate-object triple extraction with no schema — the resulting graph is not usable.
- Letting the agent infer entity and KPI relationships by reading raw tables at runtime; it does not scale and invents relationships absent from the data.
- Treating markdown files, skills, or a bigger prompt as the schema — they are part of the solution, not the solution, and cross-agent learning is lost when the wiring lives in code and prompts.
- Reaching for GraphRAG or a graph database expecting an instant payoff; a startup with one application on one Postgres does not need this architecture.
- Using multiple probabilistic models to check each other's work as a stand-in for deterministic validation.
- Treating evals or citations as verification — a citation is an after-the-fact audit, and 94% extraction accuracy still means a wrong number 6% of the time.
- Copying a human analyst's workflow steps into your agent topology; splitting the work that way loses context at every handoff and leaves no agent owning the end-to-end picture.
- Distributing judgment across sub-agents — delegate investigation and return results, never reasoning or conclusions.
- Assuming the schema you build retrospectively will hold; naive retrospective mapping requires knowing all entities ahead of time.

## Notable Outliers

- Hallucination is a feature of LLMs rather than a defect, and the fix is neuro-symbolic guardrails — agentic AI is a return to 1980s expert systems, which failed only because they could not scale. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s))
- Controlling the enterprise's vocabulary through your platform's ontology is the lock-in mechanism: users don't just adopt your product, they adopt your language, and if you become the linguistic foundation you are locked in. ([How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [15:20](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=920s))
- Verification is not ground truth — in finance two desks can be long and short off identical data, so the ontology's job is verifying output respects one organization's nouns, verbs, and rules. ([How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [6:44](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=404s))
- Schema-driven subgraph retrieval cut tool calls for code search by 40% on a .NET codebase, surfacing intermediate nodes that neither vector search nor symbol/reference lookup could reach. ([A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [10:28](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=628s))
- Atomic provenance: the model writes a reference to a number and can never write or manipulate the number itself — it doesn't even understand what the number is. ([How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [10:11](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=611s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)
- [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)
- [The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md)
- [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)
- [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)

## Speakers

- [Abhilash Asokan](../speakers/abhilash-asokan.md)
- [Emil Eifrem](../speakers/emil-eifrem.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Joseph Wang](../speakers/joseph-wang.md)
- [Natalie Meurer](../speakers/natalie-meurer.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)
- [Tim Ainge](../speakers/tim-ainge.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)

