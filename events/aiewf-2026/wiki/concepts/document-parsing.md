---
title: "document parsing"
type: "concept"
slug: "document-parsing"
tier: "supporting"
maturity: "consolidating"
talk_count: 5
speaker_count: 5
---

# document parsing

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **5** talk(s) by **5** speaker(s)

**Definition:** Turning PDFs, scans, and other unstructured documents into structured text a model can consume, including layout and table extraction.

*Also referred to as: document parsing to markdown, document layout analysis, table extraction, optical character recognition, unstructured data ingestion, document structure graph, unstructured multimodal data*

## State of Practice

The field has stopped treating PDF-to-text as a solved plumbing step and now treats it as the dominant determinant of downstream answer quality — Red Hat's position that "how you process source documents, not which model you use" drives correctness went essentially unchallenged. The stack that emerged is a middle path between two rejected extremes: naive text extractors (which truncate, linearize tables, merge columns, and leak page headers) and running every page through a frontier VLM (rejected on cost at thousands-of-documents scale, and on non-determinism plus model-version churn breaking structured-output consistency). Docling was the concrete tool named in two independent talks, both emphasizing fully local CPU-only operation, markdown/JSON/Pydantic output, and one citing Hugging Face's FinePDFs work at ~50x cost savings versus naive VLM/OCR. The most interesting shift is what the parse output is used for: preserved heading/section structure is increasingly the retrieval index itself, with speakers demonstrating RAG over a 418-section annual report with no chunker, embedding model, or vector DB. Where the field is still divided is trust — whether well-parsed extraction output can be consumed as data, or whether the parser may only emit provenance-carrying references that a deterministic substrate resolves, which is what a 94%-accurate fine-tuned extractor is deemed insufficient for in finance.

## Consensus

### Deterministic, code-based document processing should be preferred over LLM/VLM extraction wherever document structure makes it possible, because it is idempotent, faster, cheaper, and testable.

Support: **4** talk(s)

> "the benefits of having a deterministic load like this is number one, it's going to be item potent. Um, so like you're not relying on an LLM in the beginning. Um, it's often going to be a little bit faster."
>
> — [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [50:27](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=3027s)

Supporting talks: [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)

### Parsing quality, not model selection, is the binding constraint on answer correctness; bad parses manifest directly as hallucination and are not recoverable by using a stronger model.

Support: **4** talk(s)

> "that data and the way you process it is the key determining factor in whether your answer is going to be correct or incorrect for the user or customer at the end of the day"
>
> — [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [2:37](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=157s)

Supporting talks: [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)

### Preserve the document's native structure (headings, sections, outline, links) through the parse and use it as the retrieval unit, instead of blind fixed-size character chunking.

Support: **3** talk(s)

> "what's really important here is that we're doing RAG but without having to use a chunker or embedding model or vector database, etc., etc. So the index ends up being the markdown outline of the document."
>
> — [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [14:32](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=872s)

Supporting talks: [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)

### Documents must be parsed into a structured layer ahead of query time rather than dumped raw into a model's context or scanned per-question, because per-query token cost and inconsistency scale badly with corpus size.

Support: **3** talk(s)

> "imagine if if one or two pages the cost is next to nothing, but if you have 200 pages uh, then the cost going to be too much"
>
> — [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [10:14](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=614s)

Supporting talks: [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

## Disagreements

### Can values extracted by a document parser be consumed directly as data, or may the pipeline only emit references that a deterministic system resolves back to the source?

| Position A | Position B |
|---|---|
| Parser output (markdown, JSON tables, LLM-enriched metadata) is trustworthy enough to feed straight into retrieval, answers, and downstream tables; the eight tables Docling exports from a PDF are the working artifact.<br>*[Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)* | No extraction accuracy short of 100% is usable for consequential decisions — a fine-tuned extractor at 94% beating foundation models is still unacceptable — so the model must write only an atomic-provenance reference to a number and never the number itself; citations are an after-the-fact audit, not verification.<br>*[How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)* |

*Why it matters: It decides whether your parsing layer outputs values or pointers, and therefore whether you need a deterministic substrate that recomputes from source cells. Getting this wrong is invisible in evals and shows up as a wrong number in a work product nobody can trace.*

### Once documents are parsed with structure preserved, does structural navigation replace vector retrieval or merely supplement it?

| Position A | Position B |
|---|---|
| Structure is enough on its own — the markdown outline is the entire index, with the agent iterating multi-turn over sections, no chunker, embedding model, or vector DB required even on a 418-section annual report.<br>*[Structuring the Unstructured](../talks/structuring-the-unstructured.md)* | Structural navigation is not a replacement; production systems need hybrid retrieval, with BM25 keyword search mandatory for exact-match domains (SKUs, brand names, medications) where semantic similarity is actively wrong.<br>*[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)* |

*Why it matters: It determines whether a document pipeline ships with an embedding store and reranker at all, and how much per-query latency and multi-turn agent iteration you accept in exchange for dropping that infrastructure.*

## Practical Guidance

**Do:**

- Convert PDFs locally with a CPU-only layout model (Docling was named in two talks) to markdown/JSON/Pydantic rather than paying frontier-model output tokens per page.
- Chunk on headings so each chunk is a referenceable question-answer unit, which makes a retrieval miss debuggable back to a specific chunk.
- Keep the document outline/section tree as a first-class retrieval index and let the agent traverse it before falling back to similarity search.
- Pair semantic search with BM25 keyword search whenever exact tokens matter — SKUs, brand names, medications.
- Route any arithmetic over extracted numbers to code; have the model decide what to compute, never compute it.
- Use a deterministic regex/structure-based load when documents already carry inherent structure and interlinking, reserving LLM assistance for ingest where titles and link names are poorly labeled.
- Use layout models to detect and strip PII from source documents before extraction.
- Store extracted metadata in a queryable typed layer (Pydantic schemas transpiled to SQL) with incremental updates and checkpoints, not millions of sidecar JSON files on S3.
- Store the source code that produced a derived dataset as its most important context, alongside an LLM-written description.
- Tune top-k by domain: retrieve more for product catalogs, fewer for medical answers where a wrong retrieval carries liability.

**Avoid:**

- Bulk-uploading raw multi-page documents into a hosted chatbot — it burns tokens before any question is asked and you cannot see how it chunked them.
- Simple PDF text extractors that truncate text, linearize tables, drop images, and pull in page headers; column-merging errors have already injected nonsensical terms into 20 scientific papers.
- Running every page through a frontier VLM at scale — cost compounds at thousands of PDFs and a 5.1→5.2 deprecation breaks your structured-output consistency.
- Default 512-character chunking with overlap as a reflex 'best practice'; it produces chunks that cut mid-answer and reference the wrong section.
- Treating evals or a high extraction-accuracy score as verification for consequential numbers.
- Stacking probabilistic checkers — having one model check another's extraction is not a verification strategy.
- Three-to-four agent loops over a parsed corpus in an interactive assistant; 20-30 seconds of latency loses the user, and agent-driven search breaks the citation chain back to source chunks.
- Enforcing guardrails and prompt-injection defenses through system-prompt instructions instead of blocking in code before the LLM is called.
- Assuming a stronger frontier model will fix agent performance on unstructured data — everyone already uses frontier models; the harness is the differentiator.
- Humans manually transcribing numbers out of filings into spreadsheet models.

## Notable Outliers

- AI misparsing of a scanned two-column PDF merged words from adjacent columns into a nonsensical term that now appears in 20 published scientific papers — a parsing bug propagating into the literature. ([Structuring the Unstructured](../talks/structuring-the-unstructured.md), [2:37](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=157s))
- A 0.5B-parameter model (Qwen 2.5, ~400MB) is sufficient for an FAQ assistant and hallucinates less than larger models, provided the retrieved context is well-vetted — quality of parse substitutes for model size. ([Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [42:30](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2550s))
- With atomic provenance the model writes a reference to a number and cannot write or manipulate the number in any way — it doesn't even understand what that number is. ([How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [10:11](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=611s))
- CPU-based Docling delivered roughly 50x cost savings versus naive VLM and OCR pipelines in Hugging Face's FinePDFs Common Crawl work. ([Structuring the Unstructured](../talks/structuring-the-unstructured.md), [8:02](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=482s))
- Institutions buy Bloomberg and FactSet primarily to displace culpability for data errors — 'at least if it's wrong, everyone on Wall Street has the same incorrect information' — which sets the real bar for automated extraction. ([How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [3:37](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=217s))
- 2,000 video files can generate millions of extracted objects, so unstructured extraction output outgrows the source corpus by orders of magnitude and needs its own execution engine. ([When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [2:55](https://www.youtube.com/watch?v=bUJgirn4_yc&t=175s))
- Modern agents are capable enough that entity nodes formerly required in a document graph data model can often be omitted entirely, with life-sciences ontologies as the counterexample. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [1:07:53](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=4073s))

## All Talks

- [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)
- [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)
- [Structuring the Unstructured](../talks/structuring-the-unstructured.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

## Speakers

- [Abed Matini](../speakers/abed-matini.md)
- [Cedric Clyburn](../speakers/cedric-clyburn.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)
- [Zach Blumenfeld](../speakers/zach-blumenfeld.md)

