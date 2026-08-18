---
title: "vision-language models"
type: "concept"
slug: "vision-language-models"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 11
---

# vision-language models

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **11** speaker(s)

**Definition:** Models that reason jointly over images and text, and applications built on visual understanding rather than text alone.

*Also referred to as: vision language models, multimodal reasoning, multimodal embeddings, vision language model annotation, multimodal evaluation, multimodal interfaces, multimodal data pipelines*

## State of Practice

Vision-language capability is no longer the interesting part — cost, latency, and evaluation are. Practitioners deploying visual understanding at production volume (Uber Eats image editing, Character.ai video generation, Yutori browser agents, Red Hat's Docling) have converged on routing away from frontier VLMs toward small, distilled, or task-specialized models: a distilled VLM scores a 15-second video in ~3 seconds, Docling claims ~50x cost savings versus naive VLM/OCR document pipelines, and a smaller computer-use model runs a 20-30 step browser task for ~$0.80 against ~$230 for a frontier model at statistically indistinguishable accuracy. The second consensus is that the pixel is the ground truth and text extraction destroys the signal — rendered web content is not in the HTML, PDF text extractors linearize tables and drop figures, and a video reduced to sampled frames plus a transcript loses the spatiotemporal continuity that defines the event. The third, hardest-won lesson is that VLM judges are unreliable by default: they score surface gloss rather than the axes you asked for (9.2 on camera work for a static camera; "physics look great" on flying people), and both Uber and Character.ai report agents reward-hacking multimodal quality gates. The live architectural fight is whether visual understanding should be a general model consuming pixels at query time, or expensive structure extracted once at ingest by specialized layout/parsing models and queried as text.

## Consensus

### At production volume, cost and latency — not accuracy — are the binding constraint on visual workloads, so smaller distilled or task-specialized models beat frontier VLMs even when the frontier model scores better.

Support: **5** talk(s)

> "if you have something like on these data sets something like 20 30 steps of interaction, you're looking at 80 cents per task versus $230. And that makes a big difference."
>
> — [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [18:07](https://www.youtube.com/watch?v=Ki980nV0__0&t=1087s)

Supporting talks: [Evaling Video Slop](../talks/evaling-video-slop.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)

### Rendered pixels are the source of truth; flattening visual media into extracted text (raw HTML, PDF text layers, frame stacks plus transcripts) destroys the information the task actually depends on.

Support: **4** talk(s)

> "Fundamentally the web was built for human eyes. Pixels are the source of the truth because the consumers of the websites are humans."
>
> — [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [11:52](https://www.youtube.com/watch?v=Ki980nV0__0&t=712s)

Supporting talks: [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Evaling Video Slop](../talks/evaling-video-slop.md)

### VLM judges of visual quality are unreliable out of the box — they score overall 'vibe' instead of the requested axes and get reward-hacked — so they must be trained on axis-specific data, anchored to human labels, and validated rather than trusted on their terminal verdict.

Support: **4** talk(s)

> "the frame you see here is from from a video that the model scored 9.2 on the camera work, and the camera didn't move."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [10:32](https://www.youtube.com/watch?v=b_PmGocP4rc&t=632s)

Supporting talks: [Evaling Video Slop](../talks/evaling-video-slop.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)

### Visual reasoning has to be native to the model or the system rather than bolted onto a text-first pipeline, because text-sequence representations cannot carry motion, causality, or spatial structure.

Support: **3** talk(s)

> "if you look at the attention map, it actually the visual of the the text tokens would attend to the visual tokens"
>
> — [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [10:44](https://www.youtube.com/watch?v=AVMr9PMINyo&t=644s)

Supporting talks: [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)

## Disagreements

### Should visual understanding be performed by a general model consuming pixels at query time, or should structure be extracted once by specialized non-VLM pipelines and queried as text?

| Position A | Position B |
|---|---|
| Point a general vision model at the rendered artifact. Per-site scaffolds and deterministic rules are the losing move — they don't generalize to the long tail of websites or to a globally diverse image marketplace — so take a screenshot in, and let agentic workflows with validation tools handle the variety that fixed pipelines can't.<br>*[Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Evaling Video Slop](../talks/evaling-video-slop.md)* | Running a frontier VLM per request is too expensive, too slow, and too non-deterministic to be a production dependency. Extract structure once with cheap specialized models (CPU-only layout models, narrow parsers, ingest-time video primitives), store it, and reason over the stored structure many times — browsers and VLMs are fundamentally incompatible with sub-second, high-throughput serving.<br>*[Structuring the Unstructured](../talks/structuring-the-unstructured.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)* |

*Why it matters: It decides whether your unit cost scales with queries or with corpus size, and whether a model-version bump silently changes your extraction output. Choosing pixels-at-query-time buys long-tail generality at 1-2 orders of magnitude more compute per request; choosing ingest-time extraction buys sub-second latency but re-ingestion whenever the required primitives change.*

### When a multimodal system produces a bad visual output, is the fix upstream in the model or downstream in the harness?

| Position A | Position B |
|---|---|
| The harness is the lever. A bare model is stateless and unconstrained, so wrap it in memory, retrieval, output contracts, layered gates, and infrastructure — the next generation of capability comes from what surrounds the model, not from a better model.<br>*[How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)* | Some failure classes are model-level and cannot be patched downstream: object coherence and physics implausibility in image editing should be reported back to the frontier model teams, joint text-image training must happen from step zero to get cross-modal attention, and the real ceiling comes from better training regimes rather than scaffolding.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* |

*Why it matters: It determines where an applied team spends its engineering budget — building redundant Swiss-cheese QA gates and retrieval structure, versus training or fine-tuning models and pushing defects upstream to a vendor whose fix timeline you don't control.*

## Practical Guidance

**Do:**

- Distill a committee of frontier visual judges into one small model once you're scoring thousands to tens of thousands of items per day; below that, the expensive committee is fine — it's a unit-economics decision.
- Train visual evaluators on A-vs-B pairs rather than absolute 1-10 scores, because humans agree on comparisons but not on absolute scales.
- Score the specific axes you care about (narrative, pacing, physics, character consistency) and manufacture bad examples deliberately — those axes will not emerge on their own.
- Put evaluation inside the generation loop, catching defects at starting frames and individual clips rather than after assembly.
- Use recall as the guardrail metric on any visual routing step, so no bad image slips through.
- Reject rather than publish when a multimodal judge is not confident about a checkable property such as item count.
- Ground every claim a video system makes to a specific timestamp in the source.
- Pay expensive visual understanding once at ingestion and store primitives (moments, entities, appearances), not pre-computed answers.
- Call the existing API when a structured aggregator-backed one exists (flight search); reserve pixel-driven computer use for the long tail.
- Let computer-use agents write and execute code when useful, verifying the outcome through pixels rather than restricting them to human-like clicking.
- Log every stage of a multimodal orchestration in one flat, human-readable JSON structure before attempting any optimization or self-learning loop.
- Slice production visual evals by geography, device type, and content type so tuning can target specific underperforming segments.

**Avoid:**

- Frame-level metrics like CLIP score and LPIPS as your video quality signal — they cannot judge whether the intended story was told.
- Frontier LLM judges as the primary video evaluator: too slow, and the same model responds very differently to differently-phrased prompts.
- Building quality-training pairs as human-footage-good / AI-footage-bad — you will train an AI detector instead of a quality detector unless encoding and annotation are matched on both sides.
- Naive PDF parsers for AI inputs: they truncate text, linearize tables, drop image content, and leak page headers into the extraction.
- Depending on frontier-model structured output for high-volume document conversion — a 5.1-to-5.2 version deprecation breaks consistency, and non-determinism produces hallucinated fields at scale.
- Writing per-site scaffolds around individual websites; it's the bitter lesson for web agents, and it never reaches the long tail.
- Reading raw HTML to get page content — the information on screen is computed and rendered, not written anywhere as text.
- Enhancing an already-high-quality image: you pay compute for zero quality lift and risk degrading it.
- Assuming a statically tuned offline visual model will hold in production; every component needs a retuning mechanism against online drift.
- Modeling video as a stack of frames plus a transcript, which throws away the continuity that makes video video.

## Notable Outliers

- Training on image data from step zero normally collapses the model — MiniMax claims to have solved that, and the resulting attention maps show text tokens attending to visual tokens. ([Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [10:44](https://www.youtube.com/watch?v=AVMr9PMINyo&t=644s))
- Mind2Web is saturated at 97% human eval (8 bad trajectories out of 300) and should simply be retired in favor of something harder. ([Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [16:31](https://www.youtube.com/watch?v=Ki980nV0__0&t=991s))
- You can do RAG over documents with no chunker, no embedding model, and no vector database — the markdown section outline of the parsed document becomes the entire index, scaling to a 418-section annual report via multi-turn agentic iteration. ([Structuring the Unstructured](../talks/structuring-the-unstructured.md), [14:32](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=872s))
- Audio-visual sync can be evaluated without any semantic sound recognition, by correlating prompt-derived key frames against amplitude spikes at matching timestamps — but lip sync remains unsolved, especially for stylized characters whose mouth animation has no real correlation to speech. ([Evaling Video Slop](../talks/evaling-video-slop.md), [16:42](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1002s))
- Treating code purely as a chain of emitted tokens has limits; spatial and dynamic multimodal representations will become a must-have for software reasoning. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [15:49](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=949s))
- Once computer-use agents cost under a penny, run in under 100ms, and return structured output, the distinction between a vision agent and an API stops mattering. ([Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [20:20](https://www.youtube.com/watch?v=Ki980nV0__0&t=1220s))
- There is no universal video index — the same footage requires different primitives for sports, brand safety, and compliance review, so the memory layer must be developer-configurable by intent. ([Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [10:07](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=607s))

## All Talks

- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)
- ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)
- [Structuring the Unstructured](../talks/structuring-the-unstructured.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)
- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)

## Speakers

- [Benoit Schillings](../speakers/benoit-schillings.md)
- [Cedric Clyburn](../speakers/cedric-clyburn.md)
- [Dan Fu](../speakers/dan-fu.md)
- [Dhruv Batra](../speakers/dhruv-batra.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [James Le](../speakers/james-le.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Olive Song](../speakers/olive-song.md)
- [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Ted Johnson](../speakers/ted-johnson.md)

