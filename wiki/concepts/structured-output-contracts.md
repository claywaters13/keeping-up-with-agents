---
title: "structured output contracts"
type: "concept"
slug: "structured-output-contracts"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 11
---

# structured output contracts

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **11** speaker(s)

**Definition:** Constraining model output to a schema or type so downstream systems can consume it deterministically.

*Also referred to as: output contracts, schema validation, schema-guided extraction, structured output extraction, pydantic schemas as data contracts, schema constraints, agent-native output formats*

## State of Practice

The field has stopped treating schema-constrained output as a model feature and started treating it as a system boundary: every place one component hands an artifact to another is a contract, and the contract needs a declared shape, an enforcing check, and a record of which check failed. Pydantic and Zod are the de facto declaration languages, but speakers were emphatic that type conformance is the floor, not the ceiling — a well-typed second refund on the same order still passes Pydantic, so several teams add a semantic layer (OWL reasoners, ontology validators, embedding-based entity matching) behind the type check. The sharper move visible across multiple production talks is deciding what the model should be allowed to emit at all: the consensus rule of thumb is that anything with an exact answer — counting, dedup, set logic, document layout parsing, path traversal over a hierarchy — should be deterministic code, and the model's structured output should be a plan or a set of parameters that deterministic code then executes. Phaidra's numbers make the case concretely: a pure-LLM enumeration approach fell from 80% to 30% correctness as entity count grew and burned 116M tokens per validation pass, while a plan-then-resolve pipeline with set operations held 100% at 9,000 tokens per query regardless of scale. The live argument is about the shape of the contract itself — whether constraining a model to a bespoke JSON schema or DSL costs you output quality relative to letting it write a language it already knows, and whether schemas should be co-located in one language across the whole stack or transpiled down to storage.

## Consensus

### Any output another system consumes needs a declared shape; free-form text is acceptable only when a human is the sole reader.

Support: **4** talk(s)

> "defining the shape forces you to get really clear and specific. Because if you can't say what the output should look like, then you probably don't yet fully understand what you're asking the agent to produce."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [11:27](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=687s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)

### A schema without an enforcing check at the boundary is not a contract — validation must be able to halt the artifact, because prompt-level or model-level compliance is not reliable.

Support: **4** talk(s)

> "A gate which logs only warnings is not a gate. It's a suggestion. The gate needs to block the artifact from moving forward."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [10:01](https://www.youtube.com/watch?v=WLXxTaPagA8&t=601s)

Supporting talks: [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)

### Work with an exact answer (counting, dedup, set logic, traversal over known structure) belongs in deterministic code; the model's structured output should feed that code rather than replace it.

Support: **4** talk(s)

> "my rule of thumb here is if a task has an exact answer, reach for code. If it needs interpretation or judgment, that's when you can get the agent to do it, right?"
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [9:56](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=596s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

### Extraction must be handed an explicit domain schema or ontology up front; free-form extraction produces structure that downstream systems cannot query.

Support: **4** talk(s)

> "So, the benefit here is that with consistent node and edge types, relationships become meaningful and something that we can interrogate or query."
>
> — [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [3:46](https://www.youtube.com/watch?v=3ySF0I5iE_0&t=226s)

Supporting talks: [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

### Schema drift between components is a primary failure mode, and it forces teams to reinvent contract testing and version pinning around model and skill outputs.

Support: **3** talk(s)

> "One skill changes its output schema, so three skills downstream break. You decided to add a validation at the boundary because of it. You just reinvented contract testing."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [2:24](https://www.youtube.com/watch?v=WLXxTaPagA8&t=144s)

Supporting talks: [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)

## Disagreements

### Should the model be constrained to a purpose-built schema or DSL, or should it emit a format it already knows natively and be wrapped as thinly as possible?

| Position A | Position B |
|---|---|
| Define a bespoke schema — Pydantic models, OWL ontologies, domain-specific node/edge types, Zod objects — and make the model conform to it; the schema is what makes the output interrogable.<br>*[When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)* | Teaching a model a custom JSON structure or DSL degrades output quality even with many examples; pick a format saturated in its training data (HTML/CSS/JS) and add only a few data attributes as metadata — the thinnest wrapper won over heavier alternatives with larger system prompts and added skills.<br>*[HTML Is All Agents Need](../talks/html-is-all-agents-need.md)* |

*Why it matters: It decides whether your engineering effort goes into schema design and validators, or into rendering/execution infrastructure for a native format — and whether output quality improves automatically as models get better at a widely-trained language.*

### When output must be reliably structured, should an LLM produce the structure under a schema, or should deterministic code produce it while the LLM only plans?

| Position A | Position B |
|---|---|
| The LLM emits schema-conforming output and downstream validators check it; the model is the extractor and the schema plus reasoner keeps it honest.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)* | Do not let the model emit the structure for anything that must be reproducible — use layout models and deterministic parsers for documents, set operations and tree-path resolution for entities, and a pre-built metadata layer for data questions; frontier models as converters are too expensive and too version-unstable to yield consistent structured output at scale.<br>*[Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)* |

*Why it matters: The two camps produce completely different cost curves and failure modes: schema-constrained generation scales with instance count and fails silently by omission, while deterministic extraction scales with structure depth but requires building the parser and metadata layer up front.*

### Is schema conformance sufficient to trust an agent's output, or does a separate semantic layer have to sit behind the type check?

| Position A | Position B |
|---|---|
| A single well-typed schema shared across the stack is the contract — one Zod or Pydantic definition, validated at the boundary, removes the sync problem and gives downstream systems what they need.<br>*[A Song of Types and Agents](../talks/a-song-of-types-and-agents.md), [Build Systems, Not Code](../talks/build-systems-not-code.md)* | Type validity says nothing about semantic validity: constraints like duplicate refunds, payouts to the wrong entity type, or unresolved near-identical entity names pass any type check and need an ontology reasoner, an embedding-based matching pass, or a claim-level verification trail on top.<br>*[Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)* |

*Why it matters: If conformance suffices, boundary validation is nearly free; if it does not, every contract needs a second domain-specific validator and agents must stay side-effect-free until it passes.*

## Practical Guidance

**Do:**

- Declare an explicit output shape (Pydantic, Zod, or an ontology class) for every agent output another component consumes, and reserve free-form prose for outputs where a human is the only reader.
- Layer the checks: types at the entry point, domain rules at the ledger — 'Pydantic at the door, ontology at the ledger' — and keep agents side-effect-free so no database write happens until validation passes.
- Make boundary gates blocking rather than warning-only, and instrument the most expensive handoff first, not the most technically complex one.
- Give the extraction step a domain schema plus ontology instructions covering naming and unit standardization, then run a separate embedding-based matching pass; prompt-level standardization alone is not bulletproof.
- Adopt existing public ontologies (schema.org, FOAF, Dublin Core) instead of authoring one from scratch.
- Route counting, dedup, set logic, and exact traversal to deterministic code and let the model emit only the plan or the search parameters — a two- or three-step plan-then-resolve pipeline keeps cost flat versus an open agentic loop.
- Size context by structure depth rather than instance count: describe root-to-leaf paths rather than enumerating instances.
- Keep one schema definition spanning the stack in one language rather than maintaining parallel type definitions on either side of a service boundary.
- Enforce idempotency at the system level rather than relying on the model, since a retry can be reworded enough to look like a new task.
- Emit an audit record per gate so a failed 2 a.m. run tells you which gate failed, not just that the artifact is wrong.
- Run evals multiple times and average; treat cross-run or cross-model disagreement as the signal for which outputs need human review.
- Mark all externally sourced content in the contract as evidence, not instructions.

**Avoid:**

- Free-form subject-predicate-object triple extraction with no schema — the resulting graph is not something you get very far with.
- Teaching the model a bespoke DSL or custom JSON structure when a format it already knows expresses the same thing.
- Using frontier models as the document-to-structured-output converter at thousands-of-documents scale: cost compounds and version deprecation (5.1 to 5.2) breaks output consistency.
- Naive PDF parsers that truncate text, linearize tables, drop image content, and leak page headers into the extraction.
- Sharding entity enumeration across parallel LLM calls — you get phantom equipment that does not exist plus silent drops of things that do.
- Vector/embedding retrieval as the resolution mechanism for near-identical entity names; recall collapses.
- Gates that only log warnings, and shipping because the artifact looks complete rather than because a check passed.
- Assuming schema conformance equals semantic correctness — a second refund on the same order is well-typed.
- Relying on LLM self-reported uncertainty scores to select cases for human review.
- Dumping extracted metadata as millions of JSON files next to objects in S3, or splitting into a second metadata system with a second programming language researchers will not adopt.
- Letting a coding agent design your agent system — it produces a giant prompt with four jobs in it and no separation of concerns.

## Notable Outliers

- The thinnest possible wrapper — plain HTML with a few data attributes as metadata — beat heavier alternatives with larger system prompts, more context, and added skills; skills should teach taste, not framework syntax. ([HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s))
- Legacy software drifts from 1.0 toward 3.0, but AI-native software should start at 3.0 — everything in the context window — and migrate back toward deterministic 1.0 code for the use cases that earn it. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s))
- RAG with no chunker, no embedding model, and no vector database: the document's markdown section outline is the entire retrieval index, scaling to a 418-section annual report via multi-turn iteration. ([Structuring the Unstructured](../talks/structuring-the-unstructured.md), [14:32](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=872s))
- The single most important piece of context to store about a derived dataset is its source code — a conclusion reached independently by OpenAI's data agent work. ([When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [23:10](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1390s))
- Constraints like duplicate refunds or payouts to the wrong entity type are very tricky to express in English prompting but straightforward as OWL properties. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [18:58](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=1138s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)
- [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)
- [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)
- [Structuring the Unstructured](../talks/structuring-the-unstructured.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)
- [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

## Speakers

- [Angie Jones](../speakers/angie-jones.md)
- [Cedric Clyburn](../speakers/cedric-clyburn.md)
- [Diane Lin](../speakers/diane-lin.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [James Russo](../speakers/james-russo.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Roberto Stagi](../speakers/roberto-stagi.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Tim Ainge](../speakers/tim-ainge.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)

