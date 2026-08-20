---
title: "structured output contracts"
type: "concept"
slug: "structured-output-contracts"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 12
---

# structured output contracts

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **12** speaker(s)

**Definition:** Constraining model output to a schema or type so downstream systems can consume it deterministically.

*Also referred to as: output contracts, schema validation, schema-guided extraction, structured output extraction, pydantic schemas as data contracts, schema constraints, agent-native output formats*

## State of Practice

The conference treats a declared output shape as the default interface between a model and everything downstream of it, not as an optimization: free-form text is acceptable only when a human is the last reader, and any output another skill, service, or database consumes gets a schema. The dominant implementations are Pydantic (Python, transpiled to SQL rather than kept as a separate SQL layer), Zod (TypeScript, one schema shared front to back), and — in regulated domains — pre-existing public standards like X12, schema.org, FOAF, and Dublin Core, on the argument that a standard schema is lookup-able by both a new engineer and a coding agent while an agent-invented one is not. Two things are treated as settled failure modes: prompts do not enforce schemas ("the best prompt in the world isn't bulletproof"), so a separate blocking validation step belongs at each handoff; and schema-valid does not mean correct, so type checking is layered with semantic validation (ontology reasoners, set operations, provenance chains) and agents are kept side-effect-free until validation passes. The live arguments are about what the contract should be made of — a narrow domain vocabulary the model is confined to, versus a format already dense in its training data — and about who produces the structure, since several teams report that LLM-driven extraction degrades badly at scale (80%→30% correctness from 64 to 460,000 entities; hallucinated and silently dropped entities under sharded enumeration) and route it to deterministic code instead. Cost is now part of the argument, not a footnote: 50x for local layout models over naive VLM/OCR conversion, 300x token reduction for a bounded plan-then-resolve pipeline over an agentic loop.

## Consensus

### Any output consumed by another system must conform to a declared shape; free-form text is acceptable only when a human is the sole reader.

Support: **5** talk(s)

> "defining the shape forces you to get really clear and specific. Because if you can't say what the output should look like, then you probably don't yet fully understand what you're asking the agent to produce."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [11:27](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=687s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

### The schema does not enforce itself — prompt-level conformance is unreliable, so a separate validation step must sit at each handoff and must be able to block, not just warn.

Support: **4** talk(s)

> "A gate which logs only warnings is not a gate. It's a suggestion. The gate needs to block the artifact from moving forward."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [10:01](https://www.youtube.com/watch?v=WLXxTaPagA8&t=601s)

Supporting talks: [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)

### Schema-valid output is not the same as correct output; type conformance must be paired with semantic validation, provenance, or downstream disproof.

Support: **4** talk(s)

> "So, X12 is a is a system of rules and it doesn't mean that when an insurance company gives you an X12, it's true."
>
> — [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [15:18](https://www.youtube.com/watch?v=UyyOoJmuATU&t=918s)

Supporting talks: [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

### Ground the contract in a schema or format that already exists publicly or in the model's training data rather than one the agent invents for you.

Support: **4** talk(s)

> "If you ask agents to make a schema for you you're going to get like all sorts of stuff. But now if we ground it in something standard you can look up all of these and you would know just right off the bat my schema."
>
> — [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [14:35](https://www.youtube.com/watch?v=UyyOoJmuATU&t=875s)

Supporting talks: [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

### Work with exactly one correct answer — counting, dedup, set logic, format conversion — should be produced by deterministic code, with the model confined to judgment and planning on either side of the contract.

Support: **4** talk(s)

> "The simple heuristic that usually works, if you can write down the structure or the rules, it's a 1.0 job. And pure LM is weakest exactly when the system is large and well structured, which is precisely where we operate and our customers."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:04](https://www.youtube.com/watch?v=EUsPvBeIx70&t=844s)

Supporting talks: [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)

### One schema definition should serve the whole stack — data, code, and boundary validation — instead of parallel type sets that must be kept in sync.

Support: **3** talk(s)

> "you use the same language for the data, for the schemas, as well as code. Uh there are no SQL island in your code base."
>
> — [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [4:41](https://www.youtube.com/watch?v=bUJgirn4_yc&t=281s)

Supporting talks: [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

## Disagreements

### Should the output contract be a purpose-built domain schema the model is confined to, or a general format already dense in the model's training data?

| Position A | Position B |
|---|---|
| Confine the model to a strict, limited-vocabulary domain schema — X12 transactions, an OWL ontology, a typed node/edge extraction schema with naming and unit standardization instructions. LLMs perform better when the space of valid outputs is small, and the narrower vocabulary is what makes downstream reasoning and constraint checking possible.<br>*[Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)* | Do not teach the model a new format. Custom DSLs and bespoke JSON structures degrade output quality even with many examples; emit HTML/CSS/JS or TypeScript+Zod — what the model already writes natively — and keep the wrapper as thin as possible, adding only a few data attributes as metadata.<br>*[HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)* |

*Why it matters: It decides whether your engineering effort goes into schema and ontology design or into a renderer/runtime for a format the model already speaks, and whether quality improves as you tighten the schema or as base models improve on a widely-trained format.*

### Should structure be extracted by the LLM under a schema, or produced by deterministic non-LLM code with the model kept outside the extraction path?

| Position A | Position B |
|---|---|
| Have the model emit schema-conformant output and correct it in a loop: extract triples against a domain schema then reconcile entities by embedding match; call a tool, check the stop reason, and send unreasonable results back to the LLM until the ontology validator passes.<br>*[A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)* | LLM-produced structure does not survive scale or time. Non-determinism plus model version churn (a 5.1 deprecated by a 5.2) breaks consistent structured output; sharded enumeration invents phantom entities and silently drops real ones; correctness fell from 80% to 30% as entity count grew. Use layout models, set operations, and a pre-built metadata layer, and let the LLM only plan the query.<br>*[Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)* |

*Why it matters: At thousands-of-documents or hundreds-of-thousands-of-entities scale the two paths differ by 50x-300x in cost and by tens of points in accuracy, and only one of them survives a model upgrade without rebuilding evals from scratch.*

### Once data is structured, should it be consumed in a bounded fixed-step pipeline or by an agent looping over the structure?

| Position A | Position B |
|---|---|
| Keep it to a two- or three-step plan-then-resolve pipeline. A multi-step agentic loop can keep running over and over; the bounded version held 9,000 tokens per query whether the system had 64 or 460,000 GPUs, and cost stays flat and constant.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)* | Let the agent iterate over the structure across turns: use the document's markdown section outline as the entire retrieval index and walk it multi-turn (418 sections in an annual report), or loop LLM→tool→validator→LLM until the ontology check passes.<br>*[Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)* |

*Why it matters: Bounded pipelines give predictable cost and reproducibility but require the structure to be complete up front; agentic iteration tolerates incomplete structure at unbounded and unpredictable token cost.*

## Practical Guidance

**Do:**

- Define the output shape before writing the prompt — if you can't state what the output should look like, you don't yet understand what you're asking for
- Give extractors a domain schema plus explicit ontology instructions for naming and unit standardization; these instructions matter as much to extraction quality as the schema itself
- Adopt existing public schemas (X12, schema.org, FOAF, Dublin Core, star schemas) so both new engineers and coding agents can look them up
- Keep one schema definition across the stack — Zod in TypeScript, Pydantic transpiled to SQL — rather than a second set of types at the frontend or a SQL island in the codebase
- Layer the checks: Pydantic types at the door, ontology or semantic reasoner at the ledger; they are complementary, not substitutes
- Keep agents side-effect-free and defer database writes until ontology validation passes
- Add an embedding-based entity matching step after extraction instead of trusting prompt-level normalization to standardize names
- Instrument the most expensive handoff first — the one where bad data costs most — not the most technically complex one
- Treat externally supplied structured messages as correct-until-downstream-evidence-disproves-it and keep your own internal representation
- Enforce idempotency at the system level, since a retried model call can reword the request enough to look like a new task
- Block claim-bearing content from shipping unless the claims are traceable to a source
- Scale context with hierarchy depth rather than instance count, so path descriptions stay a small finite list
- Write skills that teach taste and domain craft when the model already knows the format's syntax
- Run evals multiple times and average, because structured verdicts flip-flop across runs near the decision boundary
- Use disagreement across runs or across models — not the model's self-reported uncertainty — to select cases for human review
- Rebuild evals, tests, and validation from scratch before swapping in a newer, higher-scoring model

**Avoid:**

- Asking an agent to design your schema for you
- Teaching the model a bespoke DSL or custom JSON structure when a format already in its training data would work
- Free-form subject-predicate-object triple extraction with no domain schema
- Gates that only log warnings
- Treating schema validity as correctness — a payer's portal, phone system, and X12 layer can all report the same wrong answer, and a polished artifact is the dangerous failure, not a visibly bad one
- Sharding entity enumeration across parallel LLM calls, which yields phantom equipment and silent omissions
- Pointing frontier models at bulk document conversion at thousands-of-PDFs scale, where non-determinism and version deprecation break consistent structured output
- Cramming four jobs into one giant prompt and then wondering why the agent drifts off the contract
- Splitting the app into two services with a hand-maintained, hand-synchronized contract when one language could carry the schema end to end
- Writing extracted metadata as millions of JSON files next to the objects in S3, or bolting on a separate centralized metadata DB that forces two systems and two languages
- Collapsing an image into extracted findings before downstream modeling, which loses context a later procedure depends on
- Running Python scripts directly over raw data to answer a question instead of building the metadata layer that answers the whole class of questions
- Scanning structured data token by token with a language model when the structure is already written down

## Notable Outliers

- The thinnest possible wrapper won: plain HTML with a few data attributes as metadata beat alternatives with larger system prompts, more context, and added skills — validated by using Gemini 3 Flash, a small model, as the design partner. ([HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s))
- Every step of the claim lifecycle has an X12 correspondence, so any agent action — a phone call, a portal session, a desktop app, an imaging system — can be reduced to the same structured transaction type. ([Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [13:44](https://www.youtube.com/watch?v=UyyOoJmuATU&t=824s))
- Karpathy's drift runs backwards for AI-native systems: legacy software drifts 1.0→3.0, but new AI-native software should start at 3.0 and mature toward 1.0 for the use cases that earn it, because every 1.0 function you add is more reliable ground for the LLM to stand on. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s))
- RAG with no chunker, no embedding model, and no vector database — the document's markdown section outline is the entire retrieval index. ([Structuring the Unstructured](../talks/structuring-the-unstructured.md), [14:32](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=872s))
- Hallucination is a feature of LLMs, not a defect; the fix is not eliminating it but putting a formal ontology reasoner around it as guardrails. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s))
- Data projects demand higher accuracy than software projects because a data question usually has exactly one correct answer, while a software problem has many valid solutions. ([When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [19:22](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1162s))

## All Talks

- [A Practitioner's Guide to Graphs](../talks/a-practitioners-guide-to-graphs.md)
- [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)
- [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)
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
- [Vasant Kearney](../speakers/vasant-kearney.md)

