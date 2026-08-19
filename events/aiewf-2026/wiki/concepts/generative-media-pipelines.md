---
title: "generative media pipelines"
type: "concept"
slug: "generative-media-pipelines"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 9
---

# generative media pipelines

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **9** speaker(s)

**Definition:** Production pipelines that generate video, slides, or other rich media from code or prompts, including how such output is evaluated.

*Also referred to as: programmatic video generation, video frame extraction pipelines, generative video evaluation, code-to-video benchmarking, generative document and slide creation, frame-by-frame video encoding, svg generation benchmarks*

## State of Practice

The field has converged on a substrate answer: generative media should be authored as code the model already knows — HTML/CSS/JS or React/Remotion — and rendered deterministically (freeze the browser clock, seek frame-by-frame, wait for full asset load, screenshot). Custom DSLs, JSON schemas, and canvas-shaped tooling (Figma MCPs, PowerPoint CLIs, screenshot-and-replace loops) are treated as actively harmful because they force the model out of its training distribution. The second shared belief is that generation without an in-loop evaluator is a slot machine: teams now insert verification at starting frames and per-clip, before assembly, and train judges on pairwise A/B comparisons rather than absolute 1–10 scores, because absolute scoring produces judges that rate 'the vibe' (9.2 on camera work for a static camera) rather than the axes you named. Real-time generation is the loudest structural shift — roughly 40 real-time/long-horizon models shipped in the past year at roughly last year's frontier quality, $10 buying about three hours of continuous video — and it does not reuse batch inference infrastructure: it needs causal (past-only) attention, single-step distillation from ~30 denoising steps, and geographically distributed GPUs for sub-100ms latency. On the training side, data curation is the whole game once architecture is locked, with generic aesthetic filters and AI-generated training images both called out as diversity-destroying shortcuts. What nobody has is evaluation: consistency in real-time world models, lip sync on stylized characters, and 'is this good creative work' are all still adjudicated by humans looking at output, including at DeepMind.

## Consensus

### Code — specifically web-stack code the model has already trained on — is the right authoring substrate for agent-generated media, not custom DSLs, JSON schemas, or canvas tools.

Support: **4** talk(s)

> "The fastest way to build an asset today is through code. And it's not just to build software, right? It's really to build anything."
>
> — [Content Is Code](../talks/content-is-code.md), [5:15](https://www.youtube.com/watch?v=yv6xovSsB1U&t=315s)

Supporting talks: [Content Is Code](../talks/content-is-code.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)

### Prompt-and-pray generation is a failure mode; a verification or steering loop must sit inside the generation pipeline rather than after it.

Support: **4** talk(s)

> "you prompt them, you get back a file, you watch and good luck. It's a slot machine. You cannot change it. You cannot do anything about it."
>
> — [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [0:57](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=57s)

Supporting talks: [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Evaling Video Slop](../talks/evaling-video-slop.md)

### The differentiating layer for a media pipeline is the harness — skills, structure, and serving orchestration — not the model, since everyone has access to the same frontier models.

Support: **3** talk(s)

> "And so the models are here and the frontier is really in how we serve them."
>
> — [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [7:07](https://www.youtube.com/watch?v=Xln-On3syJk&t=427s)

Supporting talks: [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

### Skills and context layers should encode domain taste and craft, not framework or tool syntax, because the model already knows the underlying language.

Support: **3** talk(s)

> "Our skill is focused on taste and video aspects because the LLMs and agents already know how to write HTML and CSS and JavaScript, we don't have to teach them the language, we just teach them how to create good videos."
>
> — [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [9:32](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=572s)

Supporting talks: [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Content Is Code](../talks/content-is-code.md)

### Evaluation of generative media quality is unsolved; production teams still fall back on human judgment and are only now building shared benchmarks.

Support: **4** talk(s)

> "evaluation for these real-time models is an unsolved problem. So, today it's literally just look at it and human judgment. That's what it is today. And this is including, by the way, Deep Deep Mind and everything."
>
> — [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [16:20](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=980s)

Supporting talks: [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)

## Disagreements

### Should agent-generated video be authored in raw HTML/CSS/JS or in a purpose-built video framework like React/Remotion?

| Position A | Position B |
|---|---|
| Use the thinnest possible wrapper around raw HTML/CSS/JS plus a few data attributes; any framework must first be taught to the agent, and teaching it measurably reduces the creativity and quality of the output.<br>*[HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)* | Use React/Remotion — video-as-React-code is exactly the artifact agents are strongest at producing, and the framework gives you composition structure and a render path for free.<br>*[Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Content Is Code](../talks/content-is-code.md)* |

*Why it matters: The choice determines whether you invest in framework-teaching context and skills or in a deterministic browser-render harness, and it sets the ceiling on what third-party agents can author against your format without onboarding.*

### Is the binding constraint on generative media products now model capability or serving infrastructure?

| Position A | Position B |
|---|---|
| The models are already good enough; the remaining work is efficiency, global GPU placement, streaming orchestration, and data harnesses — reaching for a stronger model will not fix it.<br>*[Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)* | Model quality is still the limiter: models are not good at creative work, real-time editing platforms are held back by model quality, and frontier image models buy reliability by mode-collapsing away stylistic diversity.<br>*[HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)* |

*Why it matters: It decides whether a team's next hire is an infra engineer building WebRTC/GPU routing or a research team curating data and training its own model, and whether a shared code-to-video benchmark is the field's most urgent missing artifact.*

### Can automated judges evaluate generative video quality today, or is human judgment still the only reliable signal?

| Position A | Position B |
|---|---|
| Yes, if you build them correctly: distill a committee of frontier judges into a small VLM that scores a 15-second video in ~3 seconds, train it on manufactured A/B pairs against explicitly named axes, and run it inside the generation loop.<br>*[Evaling Video Slop](../talks/evaling-video-slop.md)* | No — consistency in real-time models, lip sync on stylized characters, and creative quality are all still eyeballed by humans, including at frontier labs; the honest move is to publish a shared benchmark or Turing test rather than claim an automated judge.<br>*[The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)* |

*Why it matters: If automated judges work, quality scales with compute and eval moves online into the generation loop; if not, every quality improvement is gated on human annotation throughput and shipping velocity is bounded by how many videos your team can watch.*

### Where in the pipeline should the user exert control — approving a plan before generation, or steering during generation?

| Position A | Position B |
|---|---|
| Generate a creative plan, show it to the user for approval or regeneration before any editing starts, then execute the batch and offer a conventional timeline editor for small corrections afterward.<br>*[Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)* | Pre-approval is still the slot machine; real-time models let you steer in under a second while generation is in flight, and instant feedback is the highest attainable form of control.<br>*[The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)* |

*Why it matters: Real-time steering requires sub-100ms globally distributed GPUs and causally masked single-step models, an entirely different infrastructure bill from batch plan-then-render — you cannot hedge and build both.*

## Practical Guidance

**Do:**

- Author media as HTML/CSS/JS or React code and render deterministically: freeze the browser clock, seek to every frame, confirm all assets loaded, screenshot, advance
- Score the axes you actually care about — narrative, pacing, physics, character consistency — explicitly; they will not emerge from a general quality prompt
- Train judges on A/B pairs rather than absolute 1–10 scores, since humans disagree on absolute scales but agree on comparisons
- Catch defects at starting frames and individual clips, before assembly, where correction is far cheaper
- Distill a committee of frontier judges into one small fast VLM (~3s per 15s video) once you are at thousands to tens of thousands of videos per day; below that, the expensive committee is fine
- Write skills that encode editorial craft — cut rules, font pairings, B-roll conventions — not framework syntax
- Keep a conventional timeline/manual editing surface alongside the agentic flow so users can fix a second of runtime or a caption typo
- For real-time video, train with a causal (past-only) attention mask and distill ~30 denoising steps to one
- Place GPUs regionally so every user gets sub-100ms latency; a user in India or Japan must hit a GPU in India or Japan
- Distill expensive VLM curation judgments into a SigLIP-sized classifier before running them over a billion-image corpus
- Train a prompt-expander LLM to rewrite short user prompts into long detailed ones that sit in-distribution with training data
- Train progressively from 256px to 1K — semantics are learned at low resolution, structure and detail only at high
- Maintain the structured source of truth content is generated from: clean PRs, tags, descriptions, feature-vs-bugfix labels, real documentation
- Give consumers directional templates instead of a free-text prompt box, and show a creative plan for approval before executing

**Avoid:**

- Teaching agents a custom DSL or bespoke JSON structure — output quality degrades even with many examples
- Canvas-shaped agent tooling: Figma MCPs, PowerPoint CLIs, screenshot-and-replace loops that make the agent imitate human hands and eyes
- Frame-level metrics like CLIP score and LPIPS as quality proxies — they cannot tell you whether the intended story was told
- Frontier LLM judges as your primary evaluator: too slow, and the same model answers very differently across prompt phrasings
- Building good/bad training pairs as human-footage-vs-AI-footage — you will train an AI detector, not a quality detector, unless encoding and annotation are matched on both sides
- Training image models on AI-generated images: synthetic data is sticky and permanently imprints a recognizable ChatGPT/Nano Banana aesthetic
- Filtering training data with off-the-shelf aesthetic or image-quality scores — it silently deletes stylistic diversity like low-res CRT looks
- Storing extracted media metadata as millions of sidecar JSON files in S3, or splitting into a second system with a second language researchers won't adopt
- Assuming batch inference infrastructure transfers to real-time serving — streaming, live-session memory, and global compute are new requirements
- Reaching for a stronger model to fix harness problems; everyone already uses frontier models
- Publishing skills generated without regard for their contents or structure — most skills in circulation are low quality for exactly this reason
- Expecting single-shot prompting to produce great output; decent yes, great requires the same iterative decomposition as pre-AI engineering

## Notable Outliers

- Editing real user footage is a strictly harder agentic problem than generating video from scratch, because a blank canvas imposes no constraints while editing forces selection and omission from fixed, messy material. ([Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [3:42](https://www.youtube.com/watch?v=pPj_tjlvYjA&t=222s))
- An evaluator model scored 9.2 on camera work for a video where the camera never moved, and praised the physics of ghosts hovering and people flying — because it was trained to score the vibe, not the axes. ([Evaling Video Slop](../talks/evaling-video-slop.md), [10:32](https://www.youtube.com/watch?v=b_PmGocP4rc&t=632s))
- Frontier image models buy their output reliability by significantly mode-collapsing: the most reliable way to render a person is the most boring average person, centered in frame. ([Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [2:11](https://www.youtube.com/watch?v=-tviRdpmHvs&t=131s))
- The world pours roughly 34,000 human years per day into making slide decks, and a 10-hour deck should take 25 minutes once formatting and branding fiddling are removed. ([HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [0:53](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=53s))
- $10 now buys about 3 hours of continuously generated video and $50 buys a full day of visual interaction — comparable to what developers already burn on coding tokens. ([Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [3:20](https://www.youtube.com/watch?v=Xln-On3syJk&t=200s))
- A single avatar has been generated continuously frame-by-frame for 8 hours with no reset and no noticeable drift, at roughly the per-stream cost of a voice model. ([Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [12:36](https://www.youtube.com/watch?v=z1dqv74SpUs&t=756s))
- Structure — clean tagged PRs, accurate diffs, real documentation — not taste, is the scarce and expensive input, and it is the difference between AI purple gradient slop and polished output. ([Content Is Code](../talks/content-is-code.md), [6:42](https://www.youtube.com/watch?v=yv6xovSsB1U&t=402s))
- Agent accuracy on data projects is only 21% until a purpose-built data harness supplies context, and coding agents' trained intuitions actively mislead them on physical media data. ([When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [26:42](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1602s))
- Once real-time generative advertising works, pre-produced ads become unnecessary; what delays it is brand risk aversion, not capability. ([The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [6:21](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=381s))

## All Talks

- [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)
- [Content Is Code](../talks/content-is-code.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)
- [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md)
- [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)
- [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

## Speakers

- [Ahmed Ahres](../speakers/ahmed-ahres.md)
- [Ekaterina Deyneka](../speakers/ekaterina-deyneka.md)
- [James Russo](../speakers/james-russo.md)
- [Keegan McCallum](../speakers/keegan-mccallum.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Nicholas Arcolano](../speakers/nicholas-arcolano.md)
- [Sangwu Lee](../speakers/sangwu-lee.md)
- [Sean Cai](../speakers/sean-cai.md)

