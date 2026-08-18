---
title: "generative media pipelines"
type: "concept"
slug: "generative-media-pipelines"
tier: "supporting"
maturity: "consolidating"
talk_count: 5
speaker_count: 4
---

# generative media pipelines

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **5** talk(s) by **4** speaker(s)

**Definition:** Production pipelines that generate video, slides, or other rich media from code or prompts, including how such output is evaluated.

*Also referred to as: programmatic video generation, video frame extraction pipelines, generative video evaluation, code-to-video benchmarking, generative document and slide creation, frame-by-frame video encoding, svg generation benchmarks*

## State of Practice

The field has converged on a single structural bet: rich media — video, decks, product tours, screenshots — is now authored as code and rendered deterministically, rather than sampled end-to-end from a media model. The live argument is which code layer: HeyGen and Nori argue for raw HTML/CSS/JS because it is the native distribution of LLM training data and needs no framework taught (a browser with a frozen clock, seeked frame-by-frame with full asset load per frame, becomes the renderer), while Conductor builds on React + Remotion and argues the scarce input is structure — clean PRs, tags, docs, skills — because content generated from a codebase inherits that codebase's discipline. Evaluation is the weakest link and everyone says so: frame-level metrics (CLIP, LPIPS) don't measure whether a story was told, frontier LLM judges are too slow and too prompt-sensitive to sit in the generation loop, and the working answer at Character.ai is a committee of expert judges distilled into a small VLM (~3s per 15s clip) trained on A/B pairs against named axes — narrative, pacing, physics, character consistency — rather than absolute 1–10 scores. Everyone reports the same failure mode from naive training data: judges that score 'the vibe,' e.g. 9.2 on camera work for a static camera. There is no shared code-to-video benchmark yet; HeyGen is trying to start one, and the honest consensus is that models are still not good at creative work — the wins so far come from the medium and the harness, not from a stronger model.

## Consensus

### Code — not a canvas app, DSL, or end-to-end media model — is now the fastest and highest-fidelity way to produce rich media assets.

Support: **3** talk(s)

> "The fastest way to build an asset today is through code. And it's not just to build software, right? It's really to build anything."
>
> — [Content Is Code](../talks/content-is-code.md), [5:15](https://www.youtube.com/watch?v=yv6xovSsB1U&t=315s)

Supporting talks: [Content Is Code](../talks/content-is-code.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)

### The bottleneck in generative media is the medium and the harness you hand the agent, not model capability — stronger models do not fix it.

Support: **4** talk(s)

> "If you ask me, it's not the model, it's the medium."
>
> — [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [2:20](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=140s)

Supporting talks: [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Content Is Code](../talks/content-is-code.md)

### Single-shot prompting yields adequate media; publishable output requires explicit craft — decomposition, named quality axes, and deliberate structure that will not emerge on its own.

Support: **3** talk(s)

> "However, great output takes craft. Similar to AI coding, you can get decent output by just giving a single prompt and having something that works for your needs, but getting great output from agents requires craft, taste"
>
> — [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [10:48](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=648s)

Supporting talks: [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [Content Is Code](../talks/content-is-code.md), [Evaling Video Slop](../talks/evaling-video-slop.md)

### Current models are not yet good at creative media output; the shipping systems compensate with pipelines, evaluators, and human editing surfaces rather than trusting raw generation.

Support: **3** talk(s)

> "The one honest thing that we're going to say here is that the models still aren't good at creative work."
>
> — [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [13:12](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=792s)

Supporting talks: [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [Content Is Code](../talks/content-is-code.md), [Evaling Video Slop](../talks/evaling-video-slop.md)

## Disagreements

### Should agent-authored media be written against a purpose-built video framework, or against raw HTML/CSS/JS with the thinnest possible wrapper?

| Position A | Position B |
|---|---|
| Use a real framework — React plus Remotion — and invest in the surrounding structure (skills, docs, PR hygiene) that makes its output good; product tours built this way are nearly production-quality already.<br>*[Content Is Code](../talks/content-is-code.md)* | Any framework must be taught to the agent, and teaching it measurably reduces output creativity; the thinnest wrapper — HTML with a few data attributes as metadata — beat heavier alternatives with bigger system prompts, more context, and added skills.<br>*[HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)* |

*Why it matters: It decides whether you spend engineering effort building framework-specific skills and examples, or spend it on taste-level guidance and a deterministic renderer — and whether your output quality improves automatically as base models get better at HTML.*

### Do declarative, deterministic pipelines scale to real users, or do you need an agentic workflow that re-plans per request?

| Position A | Position B |
|---|---|
| Build declarative, robust pipelines with a pre-built metadata layer, incremental updates, and checkpoints; answering each request by running fresh code over raw data is the slowest and most expensive path.<br>*[Content Is Code](../talks/content-is-code.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)* | Fixed pipelines only work for a narrow use case; once real users arrive with their own characters, images, and voices, agentic workflows equipped with quality-validation tools generalize better.<br>*[Evaling Video Slop](../talks/evaling-video-slop.md)* |

*Why it matters: One path invests in reusable schemas, caching, and derived-asset lineage; the other invests in tool-calling agents plus in-loop evaluators, and they have opposite cost curves as request diversity grows.*

## Practical Guidance

**Do:**

- Render video deterministically: freeze the browser clock, seek to every frame, wait for all assets to confirm loaded, screenshot, advance — do not let async browser behavior drive the timeline.
- Score the specific axes you care about (narrative, pacing, physics, character consistency) instead of a single global quality number.
- Train evaluators on A/B pairs rather than absolute 1–10 scores, since humans agree on comparisons but not on scales.
- Put evaluation inside the generation loop and catch defects at the starting-frame and single-clip level, before assembly, where correction is far cheaper.
- Distill a committee of expert judges into one small fast VLM (~3s to score a 15s video) so evaluation can run near-online.
- Write agent skills that teach taste and domain craft — video pacing, deck storytelling — not framework syntax the model already knows.
- Maintain the source structure that generated content inherits: clean, tagged PRs with real descriptions, feature-vs-bugfix labels, revert tracking, and internal docs.
- Store the source code that produced a derived media dataset as its most important context, alongside an LLM-enriched dataset description.
- Use Pydantic schemas that transpile to SQL so there is no separate SQL island or second programming language in a media-metadata pipeline.
- Treat incremental updates and data checkpoints as mandatory for physical/unstructured media pipelines, not as an optimization.
- Run recurring human annotation sessions (10–15 minutes, randomized axes) to continuously recalibrate AI judges rather than labeling once.
- Keep a full manual editing surface so power users can do anything a conventional video editor allows.

**Avoid:**

- Using frame-level metrics like CLIP score or LPIPS as a quality proxy — they cannot tell you whether the intended story was told.
- Making a frontier LLM your primary video judge: too slow, and the same model answers very differently across equivalent prompts.
- Building 'good = human footage, bad = AI footage' training pairs — you get an AI detector, not a quality detector, unless encoding and annotation are matched on both sides.
- Training a judge on naively generated data: it learns surface gloss and scored 9.2 on camera work for a shot where the camera never moved, and praised the physics of hovering ghosts and flying people.
- Teaching agents a custom DSL or bespoke JSON schema — output quality degrades even with many examples.
- Giving agents canvas-shaped tools (Figma MCPs, PowerPoint CLIs, screenshot-and-replace loops) that force them to imitate human hand-and-eye interaction.
- Dumping extracted media metadata as millions of JSON files next to objects in S3, or bolting on a separate centralized metadata DB that forces two systems and two languages.
- Answering media-data questions by running Python scripts over raw assets each time instead of querying a pre-built metadata layer.
- Publishing agent skills generated without regard for their contents or structure — most currently available ones are low quality.
- Paying to train and serve a distilled evaluator at low volume; the committee-of-experts approach is fine until thousands to tens of thousands of videos per day.
- Shipping a beautiful deck that is not wired to company data — formatting is the easy half and a pretty deck alone is worth nothing.
- Defaulting to plain text output for artifacts that are meant to be used.

## Notable Outliers

- Roughly 34,000 human years per day go into making slide decks, and a 10-hour deck should take about 25 minutes once formatting, branding, and layout fiddling are removed. ([HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [0:53](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=53s))
- The editing format of a deck is completely arbitrary — audiences only ever see presentation mode — so you can author in HTML and render to PDF later. ([HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [4:28](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=268s))
- Audio-visual sync can be evaluated without any semantic sound recognition, by correlating prompt-derived key frames against amplitude spikes at matching timestamps — but lip sync remains unsolved, especially for stylized characters whose mouth animation has no real correlation to speech. ([Evaling Video Slop](../talks/evaling-video-slop.md), [16:42](https://www.youtube.com/watch?v=b_PmGocP4rc&t=1002s))
- A larger evaluator model was measurably more accurate, and was still rejected because the added accuracy did not justify the latency. ([Evaling Video Slop](../talks/evaling-video-slop.md), [9:02](https://www.youtube.com/watch?v=b_PmGocP4rc&t=542s))
- Anthropic reported agent accuracy on data projects at only 21% until a purpose-built data harness and explicit context are added. ([When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [0:02](https://www.youtube.com/watch?v=bUJgirn4_yc&t=2s))
- 90 videos of analysis generated on the order of 100,000 metadata records — unstructured media explodes into far more objects than the file count suggests. ([When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [10:53](https://www.youtube.com/watch?v=bUJgirn4_yc&t=653s))
- Decades-old dimensional modeling — star schemas, one big table — should be applied to unstructured media metadata and is currently underused. ([When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [20:19](https://www.youtube.com/watch?v=bUJgirn4_yc&t=1219s))
- 2027 will be the year of the 'content engineer,' following 2026 as the year of the creative technologist. ([Content Is Code](../talks/content-is-code.md), [9:34](https://www.youtube.com/watch?v=yv6xovSsB1U&t=574s))
- Structure, not taste, is the expensive and scarce input — and it is what separates AI purple-gradient slop from something polished. ([Content Is Code](../talks/content-is-code.md), [6:42](https://www.youtube.com/watch?v=yv6xovSsB1U&t=402s))
- Starting with a small model (Gemini 3 Flash) as the design partner: if a small model can author workable code in your format, the large coding agents certainly can. ([HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s))
- 1.3 million videos rendered by open-source users in 90 days, 267,000 creators, ~15,000 renders per day, 32,000 GitHub stars — code-to-video is already at production volume. ([HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [12:29](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=749s))
- Raising output quality requires a shared code-to-video benchmark built with the LLM labs, not better prompting. ([HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [13:12](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=792s))

## All Talks

- [Content Is Code](../talks/content-is-code.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

## Speakers

- [James Russo](../speakers/james-russo.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Nicholas Arcolano](../speakers/nicholas-arcolano.md)
- [Sean Cai](../speakers/sean-cai.md)

