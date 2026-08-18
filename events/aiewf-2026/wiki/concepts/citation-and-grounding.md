---
title: "citation and grounding"
type: "concept"
slug: "citation-and-grounding"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 11
---

# citation and grounding

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **11** speaker(s)

**Definition:** Tying generated claims back to specific sources so a reader can verify provenance, including attribution and evidence traceability.

*Also referred to as: citation traceability, citation grounding, citations and grounding, evidence grounding, source citation and attribution, retrieval explainability, atomic provenance, source provenance*

## State of Practice

The field has moved past "add citations" as a feature and now treats provenance as an architectural property of the pipeline. The shared floor is that every generated sentence must resolve in one click to an exact source unit — a paragraph, a heading-scoped chunk, a video timestamp, a cell in a filing — and that this resolution has to survive the retrieval and generation path intact; teams reported losing it the moment they enabled agent mode, dumped raw PDFs into a chat context, or let a model retype a number instead of referencing it. Above that floor the field splits hard on whether a citation actually discharges the trust obligation: one camp builds the click-through as the product, another argues a citation is an after-the-fact audit that transfers verification labor to the user and must be backed by a deterministic substrate (fixed pipelines, code-executed arithmetic, atomic provenance where the model writes a reference it cannot manipulate). A second live fault line is whether probabilistic corroboration counts as grounding — juries of agents, two agreeing payer sources, and author/verifier model splits are shipping in production even as finance speakers call model-checking-model a category error. Everyone agrees the authoring model cannot be its own verifier, that facts and model guesses must be visually separable and stay separable after copy-paste, and that contradictions between sources should be escalated to a named human rather than smoothed into fluent prose.

## Consensus

### Every generated claim must resolve to a specific source location the user can reach in one click — an exact paragraph, chunk, timestamp, or traced value — and this click-through path, not model quality, is what produces trust.

Support: **7** talk(s)

> "When someone points at a sentence and says, "Show me where this come from." You either click once or land on exact source paragraph, or you open seven browser tabs and start swiping."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [18:10](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1090s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)

### Grounding is decided at ingestion and retrieval, not at generation: chunk and index structure must make each retrieved unit individually referenceable and retrieval failures debuggable, and pure vector similarity is not sufficient to establish that a retrieved fact is actually the relevant one.

Support: **4** talk(s)

> "the challenge here is similar what what vectors give you, which is similarity in vector space, is not the same as actual relationships."
>
> — [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [7:57](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=477s)

Supporting talks: [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### Sourced facts and model-generated estimates must be kept in visibly separate containers, and cases with insufficient or contradictory evidence must be escalated to a human rather than silently reconciled into fluent prose.

Support: **3** talk(s)

> "Model four. Facts and the guesses have to live in separate box. And the fluent AI loves melting them into one smooth sentence."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [14:52](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=892s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)

### The model that produced an output cannot be the thing that certifies it; self-verification and self-reported completion are not hallucination controls.

Support: **4** talk(s)

> "Before filing, the lawyer got suspicious, so he asked the chatbot, "Are these cases real?" And the chatbot said, "Yes." That is like asking the guy who sold you the watch whether the watch is real."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [17:06](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1026s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)

### Numbers and computation must be routed to deterministic code, with the model deciding what to compute and emitting references rather than producing or transcribing values itself.

Support: **4** talk(s)

> "the model decides what to compute. It never does the computation itself."
>
> — [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [12:12](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=732s)

Supporting talks: [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)

## Disagreements

### Is a click-through citation sufficient to make AI output trustworthy, or does it merely relocate the verification burden onto the user?

| Position A | Position B |
|---|---|
| Citations are the core trust artifact and the thing worth building the product around — if a user can land on the exact source paragraph in about 30 seconds, the output is usable; uncitable output simply won't be shared.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)* | A citation is an after-the-fact audit that gets you roughly halfway and pushes checking work back onto the customer; trust must instead come from a deterministic substrate that makes the work product itself the proof, or from readable traces plus asynchronous delegation rather than chat-plus-citation.<br>*[How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* |

*Why it matters: If citations suffice, the investment goes into UI plumbing and source-linking; if they don't, you have to rebuild the numeric layer so the model never touches values and re-architect around background agents, which is a far larger engineering commitment and a different pricing story.*

### Can agreement among multiple probabilistic sources or models establish enough confidence to skip human verification?

| Position A | Position B |
|---|---|
| Yes — two independent sources concurring on an authorization status, or a jury of independent agents with a consensus judge weighing reasoning quality, is grounds to proceed automatically; separating the verifier model from the authoring model (code with Claude, verify with Codex) is a legitimate control.<br>*[Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)* | No — probabilistic systems evaluating each other's work is not verification, and evals cannot convert a non-deterministic model into a deterministic one; a named human must sign at the bottom of every real decision.<br>*[How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)* |

*Why it matters: This sets where the human sits in the loop and therefore the achievable automation rate: corroboration-as-grounding lets the no-touch share grow over time, while the deterministic camp caps autonomy at whatever a rules engine can prove and treats the remainder as permanently human-signed.*

### What substrate should hold the grounded knowledge an agent cites from?

| Position A | Position B |
|---|---|
| A graph — vector seeds plus traversal, or a durable context graph over video moments and entities — because the returned subgraph is itself the auditable explanation and markdown-file memory stops working past the ~1M-token context window.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)* | Plain files and simple retrieval — a markdown corpus with a reference-based index, or heading-chunked documents in Postgres with hybrid BM25 plus embeddings and no framework — because inspectability by hand and a predictable fixed execution path matter more than relational expressiveness.<br>*[Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)* |

*Why it matters: The choice determines whether multi-hop claims can be grounded at all and what an audit trail looks like; it also determines whether provenance survives scale, since one camp says file-based memory collapses past the context window and the other says graph infrastructure is unnecessary overhead you should explicitly forget.*

## Practical Guidance

**Do:**

- Make every sentence resolve in one click to the exact source paragraph; treat the click-through itself as the product surface, not a footnote
- Chunk on headings or question/answer boundaries so each chunk is individually referenceable and you can trace why the right chunk was not retrieved
- Combine BM25 keyword search with semantic search whenever exact identifiers matter (SKUs, brand names, medications) — similarity alone will return something close instead of the right one
- Have the model write a reference to a number rather than the number itself, so it cannot manipulate or restate the value
- Ground every claim in a video system to a specific source timestamp; do the expensive understanding once at ingestion and store primitives (moments, entities, appearances) rather than pre-computed answers
- Tag estimates and guesses with a marker that survives being copy-pasted into someone else's slides three weeks later
- Escalate contradictions between sources to a human instead of silently resolving them; require two independent sources to agree before allowing an unsupervised path
- Attach a confidence score to each extracted answer and route low-confidence or insufficient-evidence cases to human escalation by default
- Separate the verifier from the author — a different model — and give it evidence-producing tools (browser harnesses, screenshots, hooks) instead of asking it whether the work is done
- Block the pipeline from emitting a document whose internal figures don't reconcile, rather than depending on a human catching it at 2am
- Keep hand-authored source notes immutable to the LLM and write all generated content into a separate derivative layer
- Name a human who signs each decision, and mark AI-generated content explicitly as AI-generated

**Avoid:**

- Asking the model whether its own output is real, or treating evals as a substitute for verification
- Letting retrieval rank by proximity to the query when source authority differs — a system that can't distinguish an audited filing from an informal note isn't ready for consequential use
- Bulk-uploading unstructured documents into a cloud chat context and trusting whatever chunking happens invisibly on the other side
- Relying on vector similarity alone for multi-hop chains — you can hold every needed fact and still be unable to reach the answer
- Enabling agent mode and extra tools in a pipeline where referenceability matters; agent-driven search breaks the citation chain back to source chunks
- Shipping 94%-accurate extraction into a decision path and calling it good enough — a wrong number is still wrong in the remaining 6%
- Flattening 'done' into a single green checkmark that conflates mergeable, deployable, and announceable
- Depending on luck — one reviewer happening to have both contradicting documents open — as your contradiction-detection mechanism
- Putting a blank 'ask AI' box in front of users and expecting them to know how to elicit verifiable output

## Notable Outliers

- Institutions buy Bloomberg and FactSet mainly to displace culpability for data errors, not because the data is otherwise unavailable — so grounding is fundamentally a liability-transfer product, not an accuracy product. ([How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [3:37](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=217s))
- Citations are net-negative work: they hand the verification burden back to the customer, which is worst precisely in healthcare, legal, and tax where the citations look most necessary. ([Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [2:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=156s))
- When two independent payer sources report the same authorization fact, that concurrence alone is sufficient to submit the order with no human verification at all. ([Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [7:34](https://www.youtube.com/watch?v=_cVfz88_j7A&t=454s))
- You should deliberately forget vector databases, knowledge graphs, and semantic search for a personal research memory and use plain markdown plus a reference-based index instead. ([Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [19:04](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1144s))
- With a well-vetted retrieved context, a 0.5B-parameter model (~400MB, CPU-only) hallucinates less than larger models and will simply say it doesn't have the information. ([Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [42:30](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2550s))

## All Talks

- [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)
- [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)
- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)
- [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)

## Speakers

- [Abed Matini](../speakers/abed-matini.md)
- [Alex Bauer](../speakers/alex-bauer.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Dotta](../speakers/dotta.md)
- [James Le](../speakers/james-le.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Paul Iusztin](../speakers/paul-iusztin.md)
- [Shawn Chan](../speakers/shawn-chan.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)

