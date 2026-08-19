---
title: "ontology design"
type: "concept"
slug: "ontology-design"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 10
---

# ontology design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **10** speaker(s)

**Definition:** Defining the entity types and relationships of a domain as an explicit schema that agents and graphs are built on.

*Also referred to as: ontology engineering, ontology modeling, domain ontology modeling, entity relationship modeling, firm-specific ontologies, technical ontology, organizational context modeling*

## State of Practice

The conference converged on a hard prerequisite: an LLM will not derive a usable schema on its own, so the entity types, relationships, and constraints of a domain have to be authored up front and then imposed on the model. Free-form subject-predicate-object extraction and agents inferring relationships from raw tables both fail the same way — they produce plausible structure that does not exist in the data — while a supplied schema plus explicit naming/unit instructions produces something queryable. The center of gravity has shifted from ontology-as-data-model to ontology-as-control-plane: Neo4j's semantic layer splits it into a business ontology, a technical ontology of data-source metadata, and runtime execution traces, with agents kept thin above it; ZS Associates uses the graph to dictate which investigation paths and hypotheses an agent may pursue, treating each edge as a hypothesis; Berkeley's neuro-symbolic framing runs OWL validation over agent output before any write. Crucially, the ontology is understood to encode a specific organization's nouns, verbs, and rules rather than universal truth — Kepler's point is that two desks with identical data can be long and short the same stock, so verification means conformance to firm definitions, and Palantir-lineage FDE practice treats each team's divergent terminology as a fact to model, not a defect to normalize away. What remains unsettled is how formal it must be (OWL reasoners versus a flat tag list), whether to reuse public vocabularies or build bespoke ones, and whether canonicalization is a curated closed vocabulary or learned embedding matching.

## Consensus

### Letting the model infer the schema — free-form triple extraction or relationship inference over raw tables — produces relationships that do not exist; the entity/relationship types must be supplied to the extractor in advance.

Support: **4** talk(s)

> "the agent was looking at data, looking at tables, then trying to infer the relationship. That which was not scalable. And it often produce relationship which which is not actually exist in the data."
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [9:11](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=551s)

Supporting talks: [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

### The ontology's job is to encode one organization's own vocabulary and rules, expressed in language its humans use, not database-level naming or a universal ground truth.

Support: **4** talk(s)

> "It is verifying that you got an output that respects the nouns and verbs or the rules of your organization."
>
> — [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [7:26](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=446s)

Supporting talks: [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

### The ontology should function as a runtime control and validation plane that constrains what the agent may do, not merely as a lookup/retrieval schema.

Support: **4** talk(s)

> "the knowledge graph is not just something the agent looks up for data. It is a control plane for the agent."
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [10:32](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=632s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)

### Prompt text, markdown files, and a bigger context window are not substitutes for an explicit schema — constraints that are trivial to state structurally are unreliable to enforce in English.

Support: **4** talk(s)

> "we've seen a ton of team that tried to solve this problem using just Markdown files. And the summary is it is part of the solution, but it is not the solution."
>
> — [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [3:31](https://www.youtube.com/watch?v=VGN22pPpb-8&t=211s)

Supporting talks: [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)

## Disagreements

### How formal does an agent-facing ontology need to be?

| Position A | Position B |
|---|---|
| Use real description logic: OWL classes with domains and ranges, a reasoner that infers facts (Bob teaches Scooter ⇒ Bob is a teacher), and semantic validation of every agent result before it hits the ledger — Pydantic at the door, ontology at the ledger.<br>*[Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)* | Keep it deliberately thin. The core concepts are simple and people add unnecessary complexity; in practice a node/edge type list with naming and unit conventions, or even a flat reference folder of allowed tags, is enough to get the benefit.<br>*[Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md)* |

*Why it matters: Formal logic buys you enforceable invariants (no duplicate refund, no payout to the wrong entity type) but requires an ontology engineer and a reasoner in the write path; a thin schema ships in a week but pushes constraint enforcement back into prompts and code where speakers agree it is unreliable.*

### Should teams adopt existing public ontologies or author a bespoke one per organization?

| Position A | Position B |
|---|---|
| Reuse what already exists — schema.org, FOAF, Dublin Core, DBpedia represent 15–20 years of work and there is no reason to reinvent the wheel.<br>*[Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)* | The value is precisely in the organization's own divergent vocabulary. Sales says customers, ops says clients, finance says billing entities, devs say org IDs — that divergence is how humans work, and verification means conforming to the firm's definitions, not to a shared standard.<br>*[How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)* |

*Why it matters: Standard vocabularies make cross-org data interoperable and cut authoring cost to near zero; bespoke ones are the thing that makes agent output auditable inside a firm and, per the FDE argument, become commercial lock-in once the enterprise adopts your language.*

### Should entity canonicalization run off a curated closed vocabulary or learned embedding matching?

| Position A | Position B |
|---|---|
| Hand-curated mapping is a trap because it is applied retrospectively and requires knowing every entity ahead of time; embedding-based matching after extraction handles the open world and is where graph and AI techniques hybridize best.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)* | Pin the vocabulary. Give the agent a fixed reference list of tags and instruct it to be reluctant to add new ones, or let the graph itself enumerate the only entities and paths the agent is permitted to touch.<br>*[LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)* |

*Why it matters: A closed vocabulary is auditable and prevents drift but silently drops anything the curator did not anticipate; embedding matching absorbs new entities but reintroduces a probabilistic step into the layer whose whole purpose was determinism.*

## Practical Guidance

**Do:**

- Hand the extractor a domain schema plus explicit ontology instructions for naming and unit standardization — the instructions matter as much to extraction quality as the type list does.
- Add a separate post-extraction matching step to canonicalize entities; do not rely on the prompt to standardize them.
- Split the semantic layer into three pillars — a business-facing ontology in end-user language, a technical ontology of data-source metadata, and runtime execution traces — plus an explicit mapping between the first two.
- Name business entities the way people speak: a customer with a first name, not `if_name`.
- Score data-source trustworthiness both top-down by human curation and bottom-up from execution traces of what actually worked, then weight future source selection by context.
- Treat every edge in the graph as a hypothesis the agent is allowed to evaluate, and forbid it from going outside that set.
- Keep agents side-effect-free: validate the result against the ontology before any database write. Pydantic at the door, ontology at the ledger.
- Express invariants like 'no second refund on the same order' as ontology properties rather than natural-language instructions.
- Pull deterministic work out of the agentic system entirely — statistical signal detection before the agent wakes, arithmetic routed to code, so the agent decides what to compute and never computes it.
- Maintain a fixed reference list of tags/types and instruct the agent to be reluctant to add new ones, since models will invent new ones on every pass.
- Write an enrichment timestamp into each record so repeat agent passes only touch what has not been processed.

**Avoid:**

- Free-form subject-predicate-object triple extraction with no schema — the resulting graph will not get you very far.
- Letting an agent infer entity and KPI relationships by staring at raw tables.
- Hand-curated entity mapping applied retrospectively, which only works if you already know every entity in the data.
- Assuming more memory or a longer context window substitutes for a structured model — the most capable frontier model still does not understand your domain or your user.
- Markdown files alone as the enterprise semantic layer; you cannot vibe code your way to data access across a hundred databases.
- Forcing every team onto a single vocabulary — terminology divergence across sales, ops, finance, and engineering is a feature of how humans work, not a bug.
- Building this architecture at a startup with one application on one Postgres database, where the problem does not exist.
- Treating evals or a panel of probabilistic models checking each other as verification; neither turns a non-deterministic system into a deterministic one.
- Wiring business-intent-to-data-source logic into each agent's code and prompts, which violates DRY and means no agent is smarter tomorrow and there is no cross-agent learning.

## Notable Outliers

- Whoever controls the enterprise's vocabulary through their platform's ontology becomes the linguistic foundation and is therefore locked in — ontology design as a commercial moat, not just a modeling exercise. ([How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [15:20](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=920s))
- Hallucination is not a defect to be engineered away — it is the feature of LLMs, and the correct response is a formal ontology acting as guardrails around it rather than trying to make the model deterministic. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s))
- Schema-guided shortest-path subgraph retrieval cut tool calls for code search by 40% on a .NET codebase, surfacing intermediate nodes that neither vector search nor symbol/reference lookup could reach. ([A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [10:28](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=628s))
- Agentic AI is a return to 1980s symbolic AI and expert systems, with loops being the addition that makes the stack Turing complete. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [13:37](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=817s))
- Contextual understanding of a user cannot be assembled at query time at all — it must be precomputed offline by two engines on different time windows, mirroring complementary learning systems in neuroscience and lambda architecture in data infrastructure. ([From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [10:29](https://www.youtube.com/watch?v=Btk8wDUVs74&t=629s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)
- [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)
- [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md)
- [The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md)
- [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)
- [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)

## Speakers

- [Abhilash Asokan](../speakers/abhilash-asokan.md)
- [Ben Holmes](../speakers/ben-holmes.md)
- [Emil Eifrem](../speakers/emil-eifrem.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Joseph Wang](../speakers/joseph-wang.md)
- [Natalie Meurer](../speakers/natalie-meurer.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)
- [Tim Ainge](../speakers/tim-ainge.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)

