---
title: "Structuring the Unstructured"
type: "talk"
slug: "structuring-the-unstructured"
org: "Red Hat"
video_id: "-x5GEVnkuRw"
duration_sec: 1240
word_count: 3937
speakers: ["Cedric Clyburn"]
---

# Structuring the Unstructured

**Speakers:** [Cedric Clyburn](../speakers/cedric-clyburn.md)

**Org:** Red Hat

**Duration:** 20m 40s

[Watch on YouTube](https://www.youtube.com/watch?v=-x5GEVnkuRw)

## Summary

Cedric Clyburn of Red Hat argues that unstructured documents — PDFs, slides, contracts, scanned pages, tables, diagrams — are the real bottleneck for RAG and agentic systems, because none of that data reaches an LLM in a form it can reliably use. He frames the choice as a three-way tradeoff: naive PDF parsers are fast and cheap but produce merged, truncated, unusable text; frontier VLMs give good quality but are expensive, non-deterministic, and version-fragile; Docling (an open-source Linux Foundation project) sits in the middle as a local, CPU-capable CLI/library that emits Markdown, JSON, and a Pydantic document model. Most of the talk is live demo: table and image extraction, layout bounding boxes, VLM image annotation via a local Granite model on Ollama, and a 'chunkless'/agentic RAG pattern where the retrieval index is just the document's Markdown outline — no chunker, embeddings, or vector DB. He closes with scale-out paths: docling-serve as a REST microservice on Kubernetes and a Docling MCP server for agent harnesses. Worth watching if you are building document ingestion and want a concrete, local-first alternative to sending every page to a frontier model.

## Key Points

- Document processing accuracy is upstream of everything else: how you parse the source data is the determining factor in whether the model's final answer is correct.
- He cites a real-world failure mode where a scanned PDF merged two words across columns and produced a nonsensical term that has since propagated into 20 scientific papers and their citations.
- Naive PDF parsers are cheap and CPU-friendly but truncate and merge text, flatten tables linearly, drop image content, and leak page headers — unusable for question answering or agentic validation.
- Frontier models produce decent markdown but cost real money at scale (his example: ~$30 per million output tokens across thousands of PDFs) and their non-determinism plus version deprecation makes consistent structured output hard.
- Docling is positioned as the middle ground — local, open-source, part of the Linux Foundation, installable with pip, exporting to Markdown, JSON, HTML, and a Pydantic document type.
- A Hugging Face case study (Leandro's FinePDFs work on Common Crawl PDFs) showed roughly 50x cost savings using Docling on CPU/GPU versus naive VLM and OCR pipelines.
- Beyond conversion, Docling supports image annotation with vision language models (demoed with a local Granite model over Ollama's OpenAI-compatible endpoint) and targeted structured extraction of fields like invoice number and total.
- The 'chunkless' or agentic RAG demo replaces the vector store with the document's Markdown section outline: the LLM picks the relevant section and pulls its full text, demonstrated on a small paper and on the 418-section IBM 2025 annual report.
- For production scale, docling-serve exposes the pipeline as a REST microservice runnable in containers or Kubernetes, and a Docling MCP server exposes conversion, generation, and manipulation tools to agents like Claude Code, Cursor, or Codex.

## Notable Quotes

> "I think we can all agree that context is the most important aspect to building an AI application or an agent, right? It's the reason that harnesses have become so popular in order to manage the LLM's context."
>
> — [0:00](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=0s) &middot; *Frames the whole talk: document parsing as a context-engineering problem, not a plumbing problem.*

> "there are solutions out there, but they might be proprietary or require you to send your private data to someone else's server"
>
> — [1:12](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=72s) &middot; *States the data-sovereignty motivation for a local-first parser.*

> "that data and the way you process it is the key determining factor in whether your answer is going to be correct or incorrect for the user or customer at the end of the day"
>
> — [2:37](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=157s) &middot; *The talk's central claim, stated plainly.*

> "I have this viral tweet from earlier where 20 scientific papers now feature a new nonsensical term that doesn't exist because AI misinterpreted a very old article that was scanned and taken to a PDF, merging two different words from two different columns in this PDF"
>
> — [2:37](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=157s) &middot; *Concrete, checkable evidence that parse errors propagate into published downstream artifacts.*

> "a lot of this text has been truncated, has been merged, and isn't decipherable even by me as a human"
>
> — [4:10](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=250s) &middot; *Sharp human-readability test for judging naive parser output.*

> "If I'm sending this to a model that's maybe $30 per million output tokens, you can see how this can get quite expensive as I scale this up to dozens or hundreds or, in a lot of cases, thousands of PDFs"
>
> — [4:46](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=286s) &middot; *Names the cost figure behind the argument against frontier-model parsing.*

> "the difference is between maybe a 5.1 of a model that was depreciated in the 5.2 version of a model make it tricky to have structured output that's consistent every single time"
>
> — [4:46](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=286s) &middot; *Identifies model-version churn as an underrated risk in extraction pipelines.*

> "we might be susceptible to hallucinations because models are non-deterministic, and this is really tricky at scale"
>
> — [5:26](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=326s) &middot; *The determinism tradeoff that motivates a model-light pipeline.*

> "It's a fast and cheap, and most importantly, local CLI and library that I can use to take various types of input sources and convert this to markdown, JSON, and a Pydantic data type"
>
> — [5:26](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=326s) &middot; *The tool's positioning and output contract in one sentence.*

> "the two comparisons he did using GPU and using CPU for DocLing allowed him to do this at 50 times of a cost savings compared to VLMs and OCR naively"
>
> — [8:02](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=482s) &middot; *The single hardest number in the talk, from an external case study.*

> "you can see that we've exported eight different tables from that source PDF"
>
> — [11:19](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=679s) &middot; *Grounds the table-extraction claim in a demo result.*

> "what's really important here is that we're doing RAG but without having to use a chunker or embedding model or vector database, etc., etc. So the index ends up being the markdown outline of the document."
>
> — [14:32](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=872s) &middot; *The talk's most contrarian architectural claim.*

> "the final answer in one iteration was pulled from that source material without having to go in the vector database but instead search that docling document structure for the specific text"
>
> — [15:14](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=914s) &middot; *Reports the observed iteration count for the chunkless retrieval demo.*

> "pull the IBM 2025 annual report into the context here, which has 418 sections"
>
> — [15:54](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=954s) &middot; *Sets the scale at which the outline-as-index approach was stress-tested.*

> "this is where we can deploy docling as a REST API service using something that's known as docling serve. This allows us to scale things up and to run this as a microservice as a container or through Kubernetes."
>
> — [16:35](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=995s) &middot; *The production deployment story for high document volume.*

> "we can take a PDF into format like Markdown or JSON with a fully local operation from our own machine without even needing a GPU. It's fast, it's cheap, and most importantly, it's open-source."
>
> — [19:08](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=1148s) &middot; *The closing summary of the value proposition, including the no-GPU claim.*

## Positions

- Unstructured data is becoming the new context layer for AI, and most of the world's data is unstructured and therefore unusable by LLMs without preprocessing. ([0:37](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=37s), confidence: stated)
- How you process source documents, not which model you use, is the key determining factor in answer correctness. ([2:37](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=157s), confidence: stated)
- Simple PDF parsers are unacceptable for AI applications because they truncate text, linearize tables, drop image content, and include page headers. ([4:10](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=250s), confidence: stated)
- Using frontier models for document conversion is prohibitively expensive at thousands-of-PDFs scale and unreliable because model non-determinism and version deprecation break consistent structured output. ([4:46](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=286s), confidence: stated)
- Docling occupies the middle ground between naive parsers and frontier models: fast, cheap, local, and open source, running fully on CPU without a GPU. ([5:26](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=326s), confidence: stated)
- Docling delivers roughly 50x cost savings versus naive VLM and OCR pipelines, per Hugging Face's FinePDFs Common Crawl work. ([8:02](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=482s), confidence: stated)
- RAG can be done without a chunker, embedding model, or vector database by using the document's markdown section outline as the entire retrieval index. ([14:32](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=872s), confidence: stated)
- The outline-as-index retrieval approach scales to large documents, working on a 418-section annual report via multi-turn agentic iteration. ([15:54](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=954s), confidence: implied)
- Layout models can be used to detect and remove personally identifiable information from source documents before extraction. ([12:42](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=762s), confidence: stated)
- Exposing document processing through an MCP server removes the need for agents or developers to know the underlying arguments and commands. ([17:14](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=1034s), confidence: stated)

## Concepts

- [agentic retrieval](../concepts/agentic-retrieval.md)
- [document parsing](../concepts/document-parsing.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [structured output contracts](../concepts/structured-output-contracts.md)
- [vision-language models](../concepts/vision-language-models.md)

