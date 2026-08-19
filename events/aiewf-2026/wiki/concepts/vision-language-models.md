---
title: "vision-language models"
type: "concept"
slug: "vision-language-models"
tier: "supporting"
maturity: "contested"
talk_count: 13
speaker_count: 14
---

# vision-language models

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **13** talk(s) by **14** speaker(s)

**Definition:** Models that reason jointly over images and text, and applications built on visual understanding rather than text alone.

*Also referred to as: vision language models, multimodal reasoning, multimodal embeddings, vision language model annotation, multimodal evaluation, multimodal interfaces, multimodal data pipelines*

## State of Practice

Vision has stopped being a demo modality and become load-bearing infrastructure: teams are shipping VLMs as routers, judges, taggers, document parsers, browser operators, and real-time avatar generators. The dominant production pattern is a small, distilled, task-specific visual model inside a verification loop rather than a frontier VLM called per item — Character.ai distills a committee of expert judges into one model that scores a 15-second video in ~3 seconds, Red Hat's Docling runs layout parsing on CPU at ~50x the cost savings of naive VLM/OCR pipelines, and Yutori's Navigator trades accuracy parity with Opus 4.7 and GPT-5.5 for latency and ~80 cents versus ~$230 per multi-step task. Everyone who has run a VLM as a judge has watched it fail confidently — scoring 9.2 on camera work in a video where the camera never moved, or praising the physics of hovering ghosts — so the field has converged on layered gates, pairwise rather than absolute scoring, and grounding every claim to a source timestamp. The unsettled questions are architectural: whether pixels are the durable interface (Yutori's bitter-lesson argument that per-site scaffolds never reach the long tail) or whether expensive visual understanding should be paid once at ingest into a queryable structure (TwelveLabs' context graph, Docling's markdown outline index), and whether visual artifacts should be emitted end-to-end by a generative model or composed through a symbolic intermediate like Remotion code or an asset-tag system. Underneath both, multiple labs argue vision has to be native — MiniMax trained image data from step zero to avoid the collapse other labs hit, LemonSlice takes a general world model and focuses it on humans so hands, physics, and micro-expressions emerge rather than being built.

## Consensus

### For high-volume visual work, a small distilled or specialized model beats a frontier VLM, because latency and cost per item dominate the marginal accuracy the bigger model buys.

Support: **4** talk(s)

> "also tested a bigger model and the results were better, but it was significantly slower."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [8:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=494s)

Supporting talks: [Evaling Video Slop](../talks/evaling-video-slop.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### A visual generation or editing pipeline needs an automated verification layer with re-iteration inside the loop, treated as a required stage rather than an optimization, because the generating model reliably produces defects.

Support: **4** talk(s)

> "Of course agent can make mistakes and that's why we develop this verification layer to make sure that all the the composition is clean, is well defined, everything will be rendered and if there are there are some problems then the agent will reiterate on the composition."
>
> — [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [7:12](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=432s)

Supporting talks: [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)

### Reducing video to sampled frames plus a transcript destroys the property that carries the meaning — continuity across time — so frame-level metrics and text-first pipelines systematically miss what users judge.

Support: **3** talk(s)

> "And that is a useful approximation for some tasks, but it throw away the thing that makes video very unique, which is continuity, right?"
>
> — [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [1:15](https://www.youtube.com/watch?v=mOf-PP4mVjA&t=75s)

Supporting talks: [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)

### VLMs used as scorers or extractors fail confidently — they score surface gloss instead of the requested axis and hallucinate structure — so their output must be gated by external checks rather than trusted at face value.

Support: **3** talk(s)

> "the frame you see here is from from a video that the model scored 9.2 on the camera work, and the camera didn't move."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [10:32](https://www.youtube.com/watch?v=b_PmGocP4rc&t=632s)

Supporting talks: [Evaling Video Slop](../talks/evaling-video-slop.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md)

### Visual capability has to be trained in jointly rather than attached to a text model afterwards; systems that treat vision as a bolt-on cannot reason natively over motion, physics, or spatial relationships.

Support: **3** talk(s)

> "So, from step zero, we trained not only text data, we also trained image data. And it was normal for many other labs that the model would collapse after training a little bit, and we managed to solve that problem."
>
> — [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [10:44](https://www.youtube.com/watch?v=AVMr9PMINyo&t=644s)

Supporting talks: [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)

## Disagreements

### Should visual content be consumed as pixels at query time, or converted once into a structured representation that downstream queries read instead?

| Position A | Position B |
|---|---|
| Pixels are the source of truth and a general screenshot-in model is the only thing that generalizes; parsing, scaffolds, and per-site structure extraction lose to the long tail, since on-screen content is computed and rendered rather than present as text.<br>*[Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)* | Pay the expensive visual understanding once at ingest and query the resulting structure — a context graph of moments/entities/appearances, a markdown-and-JSON document with extracted tables used directly as the retrieval index, or a narrowed page slice that discards ads, widgets, and layout to hit sub-second latency.<br>*[Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)* |

*Why it matters: It decides whether your per-query cost is a VLM forward pass over raw pixels or a cheap lookup, and whether new workflows over the same corpus require re-processing the archive. Yutori's own numbers put a 20-30 step pixel trajectory at 80 cents; TwelveLabs and Docling are arguing that number should be paid once, not per question.*

### Should applied teams build small specialized visual models, or ride frontier general models and push failures upstream?

| Position A | Position B |
|---|---|
| Build or distill your own: a committee of frontier judges distilled into one small fast model, a CPU-only layout model instead of a VLM pipeline, or a smaller-footprint computer-use model whose real edge over trillion-parameter frontier models is latency per step and cost per task rather than accuracy.<br>*[Evaling Video Slop](../talks/evaling-video-slop.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)* | Build on frontier general models and let their improvements carry you: report object-coherence and physics-implausibility failures back to the frontier image-editing teams rather than only patching downstream, and prefer training a general world model you then focus, because capabilities like hands, object interaction, and micro-expressions emerge rather than needing to be built.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)* |

*Why it matters: It sets where a team spends its engineering budget — distillation, serving, and eval-data manufacture versus prompt/harness work and vendor escalation — and Character.ai puts the crossover explicitly at thousands to tens of thousands of items per day.*

### Should a visual artifact be emitted end-to-end by a generative model, or composed through a symbolic intermediate the model writes and a verifier checks?

| Position A | Position B |
|---|---|
| Go through structure: represent video as React/Remotion code because code generation is what agents are strongest at, author games as asset tags and systems queried by shared behaviors rather than one-shot generation, and store primitives — moments, entities, appearances — instead of pre-computed answers.<br>*[Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)* | Go end-to-end: train one model on the joint distribution and accept the harder training and deployment, because the capabilities you would otherwise hand-build emerge, and expect a single high-EQ end-to-end video/audio model to sit on top with reasoning delegated to a separate model underneath.<br>*[Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)* |

*Why it matters: The symbolic path gives you a verifiable, editable artifact — Reelful can re-render a bad composition and users can drop into a timeline editor — while the end-to-end path gives fidelity and emergent behavior but no intermediate to inspect or correct, which is exactly why LemonSlice names controllability, not capability, as its current limiter.*

## Practical Guidance

**Do:**

- Distill a committee of expert judges into one small VLM once volume reaches thousands to tens of thousands of items per day; below that, the expensive committee approach is fine and the unit economics do not justify training and serving your own.
- Train visual judges on A-versus-B pairs rather than absolute 1-10 scores, because humans do not agree on absolute scales but do agree on comparisons.
- Score the explicit axes you care about — narrative, pacing, physics, character consistency — and manufacture badness to create the pairs; do not expect those axes to emerge from naive data.
- Ground every claim a visual system makes to a specific timestamp in the source video.
- Use recall as the guardrail metric for a visual routing agent, and reject rather than publish when the multimodal judge is not confident about a check like item count.
- Log every stage of the multimodal orchestration in a flat, human-readable JSON structure before attempting any optimization or self-learning loop.
- Grade visual context by proximity and editing focus the way level-of-detail grades rendering, instead of feeding the entire scene or archive into the model.
- Convert documents with a local layout model to markdown/JSON on CPU and use the document's section outline as the retrieval index — no chunker, embedding model, or vector database required.
- Use a vision model to bulk-tag asset libraries too large to tag by hand (Nereu tagged 6,000-7,000 assets this way).
- Show the user a creative plan for approval before executing an expensive visual generation, and keep a conventional editing surface for small corrections.
- Slice production evaluation by geography, device type, and item type so tuning can target the specific underperforming segments.
- Verify computer-use outcomes through pixels even when the agent takes a code shortcut — click when you have to, write code when you have to, confirm through what is rendered.
- For real-time avatar video, expect to need custom audio embeddings (standard encoders are trained on monotone audiobook data), a causally masked past-only model, and 30 denoising steps collapsed to one.

**Avoid:**

- Frame-level metrics like CLIP score and LPIPS as the quality bar for video — they cannot tell you whether the intended story was told.
- A frontier LLM as your primary video judge: too slow, and the same model answers very differently depending on how each person prompts it.
- Building good-versus-bad training pairs as human footage versus AI footage — you will train an AI detector, not a quality detector, unless encoding and annotation methodology match on both sides.
- Simple PDF parsers that truncate text, linearize tables, drop image content, and keep page headers — one two-column merge produced a nonsensical term now cited in 20 scientific papers.
- Frontier models for document conversion at thousands-of-PDF scale: the cost compounds, and a 5.1-to-5.2 deprecation breaks the consistency of your structured output.
- Reading raw HTML to extract page content — the information on screen is calculated and rendered, so it is simply not in the markup.
- Writing per-site scaffolds; they do not generalize to the long tail of roughly 200 million active websites.
- Enhancing an already-high-quality image: you pay compute for zero quality lift and risk degrading it, including hallucinating details to match a description.
- Using one identical prompt for every image in a diverse marketplace — the diversity of the output collapses.
- Assuming a single universal video index exists; the same footage yields different required primitives for sports, brand safety, compliance review, and analytics.
- Trusting a self-correcting visual loop's pass rate without checking for reward hacking — agents oversteer into conservative generic outputs that differ in raw pixels but carry no real improvement.

## Notable Outliers

- Mind2Web is saturated — Navigator N1.5 sits at 97% human eval with 8 of 300 trajectories wrong — and the benchmark should simply be retired in favor of something harder. ([Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [16:31](https://www.youtube.com/watch?v=Ki980nV0__0&t=991s))
- A CPU-only layout-model document pipeline delivered roughly 50x cost savings versus naive VLM and OCR pipelines in Hugging Face's FinePDFs Common Crawl work. ([Structuring the Unstructured](../talks/structuring-the-unstructured.md), [8:02](https://www.youtube.com/watch?v=-x5GEVnkuRw&t=482s))
- An avatar model generated continuously frame by frame for 8 hours straight with no reset and no noticeable drift, with a 16-hour run underway — solved by an undisclosed approach to error accumulation that differs from what everyone else does. ([Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [12:36](https://www.youtube.com/watch?v=z1dqv74SpUs&t=756s))
- Real-time avatar video generation now costs about the same per stream as a voice model, which is the specific unlock for consumer use cases. ([Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [13:20](https://www.youtube.com/watch?v=z1dqv74SpUs&t=800s))
- Audio-visual sync can be evaluated without any semantic sound recognition, by correlating prompt-derived key frames against amplitude spikes at matching timestamps — but lip sync remains unsolved, especially for stylized characters whose mouth animation has no real correlation to speech. ([Evaling Video Slop](../talks/evaling-video-slop.md), [16:42](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1002s))
- Treating code purely as a chain of emitted tokens has limits; spatial and dynamic multimodal representations will become a must-have for software reasoning. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [15:49](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=949s))
- Text tokens naturally attend to visual tokens when the model is trained multimodally from step zero — visible directly in the attention map. ([Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [10:44](https://www.youtube.com/watch?v=AVMr9PMINyo&t=644s))
- The share of AI engineers using generative image models and feeling really good about it doubled year over year, from 18% to 36%. (["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [4:47](https://www.youtube.com/watch?v=RGe6EjucbzI&t=287s))
- Editing real user footage is a harder agentic problem than generating video from scratch, because a blank canvas imposes no constraints while editing forces the agent to select and omit from fixed material. ([Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [3:42](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=222s))

## All Talks

- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)
- ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)
- [Structuring the Unstructured](../talks/structuring-the-unstructured.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)
- [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)
- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)
- [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)

## Speakers

- [Arturo Nunez](../speakers/arturo-nunez.md)
- [Benoit Schillings](../speakers/benoit-schillings.md)
- [Cedric Clyburn](../speakers/cedric-clyburn.md)
- [Dan Fu](../speakers/dan-fu.md)
- [Dhruv Batra](../speakers/dhruv-batra.md)
- [Ekaterina Deyneka](../speakers/ekaterina-deyneka.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [James Le](../speakers/james-le.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Olive Song](../speakers/olive-song.md)
- [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Ted Johnson](../speakers/ted-johnson.md)

