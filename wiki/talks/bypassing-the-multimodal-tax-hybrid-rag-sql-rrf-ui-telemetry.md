---
title: "Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry"
type: "talk"
slug: "bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry"
org: "Ogilvy"
video_id: "Akm1sqvWG4A"
duration_sec: 2747
word_count: 6285
speakers: ["Abed Matini"]
---

# Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry

**Speakers:** [Abed Matini](../speakers/abed-matini.md)

**Org:** Ogilvy

**Duration:** 45m 47s

[Watch on YouTube](https://www.youtube.com/watch?v=Akm1sqvWG4A)

## Summary

A hands-on, demo-heavy walkthrough of a framework-free RAG stack built by Ogilvy's Abed Matini for an HR FAQ assistant: Docling converts uploaded PDFs/Word/PowerPoint/images to markdown locally, chunks land in PostgreSQL as vectors, and retrieval combines cosine-similarity vector search with BM25 keyword search plus reranking. The core argument is that pre-structuring documents on local CPU avoids the 'multimodal tax' of dragging a raw 28-page PDF into a cloud chatbot — you burn tokens before asking anything and have no visibility into how it was chunked. Matini spends most of the talk demoing four chunking strategies (heading-based, paragraph, fixed 512-char with 64-char overlap, sentence-group) and showing how clean chunks give traceable citations while a bulk-uploaded handbook returns vague, unattributable answers. He also argues against agentic loops for this use case: deterministic Python functions handle date lookup, guardrails, and prompt-injection blocking before anything reaches the LLM, which keeps latency low and makes behavior testable. Worth watching if you want a concrete, low-cost local RAG blueprint (Qwen 2.5 0.5B, Ollama, Docker, Langfuse) and are weighing structured ingestion against just uploading documents to a big model.

## Key Points

- Uploading raw documents directly to a cloud LLM spends tokens before any question is asked and hides how the document was chunked, so tables and structure can be misread with no way to inspect it.
- Running Docling locally on CPU to convert documents to markdown before chunking gives visibility into chunk boundaries and costs nothing beyond local compute, which matters when documents run to 200 pages.
- The demo compares four chunking strategies — heading-based, paragraph-based, fixed 512 characters with 64-character overlap, and sentence-group for OCR'd screenshots — each suited to different document shapes.
- Bulk-uploading a 28-page handbook produces meaningless chunks like bare signature/date lines, which slows retrieval, reduces accuracy, and increases hallucination compared to a question-answer structured FAQ file.
- Clean heading-based chunks make citations traceable: the demo shows the answer alongside the exact source chunk, so a wrong answer can be debugged back to which chunk failed to retrieve.
- Hybrid retrieval is necessary because semantic search alone returns 'close' matches, but product SKUs, brand names, and medications require exact keyword hits from BM25, fused and reranked before hitting the LLM.
- Top-k should be tuned to the use case: medical answers should retrieve fewer for accuracy and liability reasons, while product catalogs need a wider window or entire product lines never surface.
- The system deliberately uses plain Python functions instead of LLM agents for date lookup, guardrails, and injection detection — faster locally, fully controllable, and coverable by a test suite.
- Guardrails and prompt-injection checks (intent regexes, term dictionaries, an LLM classifier) run in code before the LLM call, keeping the system prompt tiny while the real rules live in testable code.
- Matini started with a 7-billion-parameter model, found it too slow and wordy, and settled on Qwen 2.5 0.5B (~400MB), arguing that well-vetted retrieved context makes the smallest model sufficient and less prone to fabrication.

## Notable Quotes

> "as soon as we upload these documents, we going to basically lose some of our tokens that we supposed to have only for uh processing these documents without even asking a question"
>
> — [0:57](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=57s) &middot; *states the core 'multimodal tax' problem the whole talk is built around*

> "Another issue is you don't know how that document looks li- looks like there and that chunking uh how it's being chunked and how uh basically that LLM is seeing it. So, that would be a risk quality."
>
> — [8:37](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=517s) &middot; *names the observability cost of drag-and-drop ingestion, not just the token cost*

> "imagine if if one or two pages the cost is next to nothing, but if you have 200 pages uh, then the cost going to be too much"
>
> — [10:14](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=614s) &middot; *quantifies when the local-preprocessing tradeoff starts to pay off*

> "So, this going to slow down and reduce the accuracy of our chat. It's going to increase hallucination."
>
> — [12:46](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=766s) &middot; *direct causal claim linking bad chunking to hallucination*

> "So, each heading and answer is going to heading as a question and answer is going to become a chunk. So, we know our chunking is clean, and it's easy to uh reference."
>
> — [14:29](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=869s) &middot; *explains the heading-based strategy and why it aids citation*

> "Then you can go track it why this right chunk hasn't been retrieved. So, in this way you have more uh more uh clear path towards how you can debug it."
>
> — [16:28](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=988s) &middot; *frames traceable chunks as a debugging capability, the payoff of structured ingest*

> "one of the best practices for rag is you just divide based on 512 character, and you have 64% overlap between the chunks, so you won't lose the track"
>
> — [19:17](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1157s) &middot; *the concrete fixed-size chunking recipe he demos (stated as 64% though demoed as 64 characters)*

> "But you see the issue with that is it's coming here to assist the next system. So, it's breaking. It's not the best but in some cases it works for you."
>
> — [21:14](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1274s) &middot; *acknowledges the tradeoff of fixed-length chunking rather than selling it*

> "The real one reason for that is the speed cuz I'm running this locally. I'm having running this on Ollama. I don't have I don't need to three four agents to loop three times four times because then I'll have to wait I have to wait 20 30 seconds for it and user would lose the interest."
>
> — [26:34](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1594s) &middot; *the latency argument against multi-agent loops, with a concrete number*

> "If something can be done by a Python function, let's a Python function then run it for you. Then you have also the full control over the function. Won't be any hallucination because you need to you're going to write your test suite so to just cover most of the situations."
>
> — [26:34](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1594s) &middot; *the deterministic-code-over-agents position, tied to testability*

> "You don't need the LLM to bring you back the current date. You don't need the LLM to calculate for you something"
>
> — [27:13](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1633s) &middot; *crisp heuristic for what should never be an LLM call*

> "if it's a medical chatbot, you need the exact medication. You need don't need something similar or close to it. So, we need to have both both basically uh keyword search and um and the semantic search together."
>
> — [30:07](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1807s) &middot; *the clearest justification for hybrid over pure vector search*

> "If you don't let the window your window to pull those information, those products are never going to be sold and never going to be shown in the chatbot. So, it's important how many you can fetch."
>
> — [31:01](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1861s) &middot; *ties top-k tuning to a business outcome, not just retrieval metrics*

> "So, if you're having products, you would bring more. You retrieve more. If it's something medical, you retrieve less."
>
> — [33:05](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1985s) &middot; *compact rule of thumb for domain-dependent top-k*

> "The direct rag is is just uh following the it's a fixed pipeline. It's not going to go calling anything. You know, the the path is quite clear. You have embed embedded query, you have a hybrid retriever. And you just bring up the answer. It's good if compliance is quite important for you."
>
> — [34:02](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2042s) &middot; *states when to prefer fixed pipelines over agent mode*

> "the point of lots of these guardrails is that the issue should stop before we um the prompt injection or anything that we have uh or a question that is we're not supposed to respond. We shouldn't even send it to the LLM to generate anything."
>
> — [37:35](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2255s) &middot; *the pre-LLM guardrail principle stated plainly*

> "although the system prompt looks quite small and just few sentences, uh, I'm actually prompting way more in the uh, code"
>
> — [37:35](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2255s) &middot; *reveals the design choice of moving policy out of prompts into code*

> "it's not like uh uh LM that sometimes likes to listen to you as you're uh as the instruction and sometimes just escape and does its own thing"
>
> — [40:11](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2411s) &middot; *the reliability argument for code-based rather than prompt-based guardrails*

> "Interesting finding from my side was you don't need the biggest model. You if you can vet your data before sending it to your LLM, a smaller smallest model can sort you out and get a good uh uh answer for you."
>
> — [42:30](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2550s) &middot; *the talk's headline empirical claim about retrieval quality substituting for model size*

> "If it doesn't have information, it's simply it's going to say no, I don't have that information."
>
> — [43:16](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2596s) &middot; *claims small models abstain more readily, framed as a safety property*

> "we use Docling for uh to do the heavy job. And then we use the Postgres vector database to just store everything. Uh didn't use any specific framework."
>
> — [44:14](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2654s) &middot; *the framework-free stack summary in one line*

## Positions

- Uploading raw documents into a cloud chatbot consumes tokens before any question is asked, making local preprocessing cheaper at scale. ([0:57](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=57s), confidence: stated)
- Bulk-uploading an unstructured 28-page handbook produces meaningless chunks that reduce accuracy and increase hallucination relative to structured question-answer chunks. ([12:46](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=766s), confidence: stated)
- Heading-based chunking yields clean, referenceable chunks that make retrieval failures debuggable. ([16:28](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=988s), confidence: stated)
- Semantic search alone is insufficient for domains requiring exact matches (SKUs, brand names, medications); BM25 keyword search must be combined with it. ([30:07](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1807s), confidence: stated)
- Multi-agent loops are the wrong tradeoff for a locally-hosted chatbot because three or four agent loops add 20-30 seconds of latency and lose the user. ([26:34](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1594s), confidence: stated)
- Anything that can be done by a deterministic Python function should be, rather than delegated to an LLM, because it eliminates hallucination and can be covered by tests. ([26:34](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1594s), confidence: stated)
- Fixed direct-RAG pipelines are preferable to agent mode when compliance matters, because the execution path is predictable. ([34:02](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2042s), confidence: stated)
- Guardrails and prompt-injection filters should block requests in code before the LLM is called, not via system-prompt instructions. ([37:35](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2255s), confidence: stated)
- Optimal top-k depends on domain: retrieve more for product catalogs, fewer for medical answers because of accuracy and liability. ([33:05](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1985s), confidence: stated)
- A 0.5-billion-parameter model (Qwen 2.5, ~400MB) is sufficient for an FAQ assistant if the retrieved context is well-vetted, and hallucinates less than larger models. ([42:30](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=2550s), confidence: stated)
- The entire stack runs on CPU without a GPU, so it can be deployed on any staging server or GitHub Codespace. ([5:46](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=346s), confidence: stated)
- Enabling agent mode with extra tools costs referencing ability, since agent-driven search breaks the citation chain back to source chunks. ([27:57](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=1677s), confidence: stated)
- A production chatbot that accumulates too many tools becomes unmanageable, which is an argument for a framework-free fixed pipeline. ([1:53](https://www.youtube.com/watch?v=Akm1sqvWG4A&t=113s), confidence: implied)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [citation and grounding](../concepts/citation-and-grounding.md)
- [document parsing](../concepts/document-parsing.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)

