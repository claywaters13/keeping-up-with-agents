---
title: "HTML Is All Agents Need"
type: "talk"
slug: "html-is-all-agents-need"
track: "Generative Media"
org: "HeyGen"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "Cz4v1WHVyZc"
duration_sec: 913
word_count: 2535
speakers: ["James Russo"]
---

# HTML Is All Agents Need

**Speakers:** [James Russo](../speakers/james-russo.md)

**Org:** HeyGen

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 15m 13s

[Watch on YouTube](https://www.youtube.com/watch?v=Cz4v1WHVyZc)

## Summary

James Russo, co-creator and tech lead of Hyperframes at HeyGen, argues that agents should generate video by writing plain HTML, CSS, and JavaScript rather than a custom DSL, JSON schema, or specialized framework, because web languages are the native tongue of LLMs and dominate their training data. He walks through HeyGen's year of experiments — After Effects connectors, Lottie, Rive, Remotion — and explains why the thinnest possible wrapper (HTML plus a few data attributes for timing) beat every heavier abstraction, validated by using a small model (Gemini 3 Flash) as the design partner. The hard engineering problem was determinism: browsers load assets asynchronously, so Hyperframes freezes the browser clock, seeks frame by frame, waits for full load, screenshots, and encodes to MP4, meaning anything renderable in a browser (Three.js, SVG, WebGL, shaders, Lottie) is renderable in a video. He reports scale numbers — 1.3M videos rendered in 90 days, 267K creators, 32K GitHub stars — and is candid that models are still weak at creative work, which is why HeyGen is building a code-to-video benchmark. Worth watching if you care about agent-authored media, format design for LLM output, or deterministic browser rendering.

## Key Points

- HeyGen's core bet is that HTML, CSS, and JavaScript are the native output languages of LLMs, so video generation should use them directly instead of teaching models a new DSL or custom JSON structure.
- After trying After Effects/Premiere connectors, Lottie, Rive, and Remotion, the team found each either produced good output but was not agent-friendly, or required teaching the model a framework, which cost creativity.
- The team deliberately used a small model, Gemini 3 Flash, as the design partner on the theory that if a small model could author workable code in the format, larger coding agents certainly could — and the format would improve automatically as models improve.
- Among many candidate wrappers around HTML, the thinnest one won: essentially plain HTML with a few data attributes carrying timing metadata.
- Deterministic MP4 rendering required fighting the browser's intentional asynchrony — Hyperframes freezes the clock, seeks to each frame, waits for all assets to load, screenshots, and repeats, so preview pixels equal render pixels.
- Because rendering happens in a real browser, anything the web can draw — Three.js, charts, SVGs, shaders, WebGL, WebGPU, Lottie — can appear in a video.
- Hyperframes' bundled skills teach taste and video craft rather than framework syntax, since the model already knows the language; this raises the floor on single-shot output.
- Reported traction: over 1.3 million videos rendered by open-source users in 90 days, 267,000 creators, ~15,000 videos rendered daily, and 32,000 GitHub stars, with the project open source and free forever.
- Russo concedes models are still not good at creative work, and HeyGen is starting a code-to-video benchmark in collaboration with LLM labs and video-agent builders to address it.

## Notable Quotes

> "HTML, CSS, and JavaScript are the native languages of LLMs. Most of their training data, every webpage that gets scraped at the end of day is essentially just HTML, CSS, and JavaScript under the hood."
>
> — [1:52](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=112s) &middot; *the thesis of the talk, stated with its supporting reason*

> "Uh we like to think of this as trying to ask Shakespeare to write a poem in Japanese or Chinese."
>
> — [2:33](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=153s) &middot; *the memorable analogy for why custom DSLs degrade model output*

> "Um then we have HTML, which around November of last year when Gemini 3 and the latest models came out, we saw a step function improvement in what LLMs could do."
>
> — [4:34](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=274s) &middot; *dates the capability shift that made the approach viable*

> "We played around with Remotion quite a bit and honestly thought it was a great example of what LLMs and agents could do with coding. Um however, we noticed that we had to teach them the framework."
>
> — [4:34](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=274s) &middot; *names a specific competing tool and the tradeoff that ruled it out*

> "Um and we decided, let's not fight the model, but find a way where we can let them talk in their native tongue."
>
> — [5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s) &middot; *compact statement of the design philosophy*

> "So, how we did this was starting with a very small model, Gemini 3 Flash, as our design partner. We knew that if the smaller models could author workable code in a framework, then the larger models and these coding agents could 100% do it as well."
>
> — [5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s) &middot; *a transferable methodology for validating an agent-facing format*

> "but to our surprise, the thinnest wrapper ultimately won, which is essentially just HTML at the end of the day with a few data attributes as metadata"
>
> — [5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s) &middot; *reports the counterintuitive empirical result against bigger prompts and skills*

> "The same pixels that the browser sees is ultimately what your video is going to see."
>
> — [6:39](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=399s) &middot; *states the preview/render equivalence guarantee in one line*

> "And this was a lot harder because browsers are async on purpose. Um they have a different set of requirements and concerns to video rendering."
>
> — [6:39](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=399s) &middot; *names the core technical obstacle to deterministic rendering*

> "We freeze the clock in the browser and then we seek deterministically to every single moment in time or every single frame, uh wait for everything to load on the page, ensure that it's loaded and ready to go, and then we take a screenshot and move on to the next frame"
>
> — [7:57](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=477s) &middot; *the actual rendering algorithm, the most reusable engineering detail in the talk*

> "Things like 3.js, charts, SVGs, shaders, WebGL, WebGPU, Lottie, all of these are renderable in the browser, and therefore all of them are renderable in hyperframes."
>
> — [8:43](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=523s) &middot; *quantifies the leverage gained from betting on the browser*

> "Our skill is focused on taste and video aspects because the LLMs and agents already know how to write HTML and CSS and JavaScript, we don't have to teach them the language, we just teach them how to create good videos."
>
> — [9:32](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=572s) &middot; *reframes what skills/system prompts should spend tokens on*

> "However, great output takes craft. Similar to AI coding, you can get decent output by just giving a single prompt and having something that works for your needs, but getting great output from agents requires craft, taste"
>
> — [10:48](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=648s) &middot; *tempers the one-shot demo with a claim about where human effort still lives*

> "Over 1.3 million videos have been rendered by open-source users of Hyperframes in the last 90 days. 267,000 creators have tried it."
>
> — [12:29](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=749s) &middot; *the headline adoption numbers*

> "We have about 15,000 videos every single day being rendered utilizing the open-source framework and 32,000 GitHub stars."
>
> — [12:29](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=749s) &middot; *daily throughput and repo traction*

> "If your agent knows how to write HTML, CSS, and JavaScript, it knows how to create a Hyperframes video."
>
> — [13:12](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=792s) &middot; *the portability claim that follows from the format choice*

> "The one honest thing that we're going to say here is that the models still aren't good at creative work."
>
> — [13:12](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=792s) &middot; *an unusually direct limitation admission from a vendor talk*

> "which is why we started to work on a code to video benchmark where we are trying to work with the LLM labs, any creators who are working on video agents to ensure that we can raise the floor of videos for everyone"
>
> — [13:12](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=792s) &middot; *names the proposed fix and an open call for collaborators*

> "agents are made building incredibly easy. Launching is still quite hard."
>
> — [13:54](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=834s) &middot; *the framing problem statement the whole product is aimed at*

## Positions

- HTML, CSS, and JavaScript are the native languages of LLMs because most training data reduces to them, so agents produce better output in those languages than in a custom DSL or JSON schema. ([1:52](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=112s), confidence: stated)
- Teaching a model a new DSL or custom JSON structure degrades output quality even when given many examples. ([2:33](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=153s), confidence: stated)
- After Effects and Premiere Pro produce gold-standard creative output but are not agent-friendly; their connectors act as copilots rather than sources of creative output. ([3:50](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=230s), confidence: stated)
- Lottie and Rive give decent output but are not agent-friendly and are less editable and controllable than HTML. ([4:34](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=274s), confidence: stated)
- Remotion requires teaching agents the framework and its conventions, which reduces the creativity of the resulting output. ([4:34](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=274s), confidence: stated)
- Around November of the prior year, with Gemini 3 and contemporaneous models, there was a step-function improvement in what LLMs could produce, and unprompted they gravitated toward HTML/CSS/JS. ([4:34](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=274s), confidence: stated)
- The thinnest wrapper around HTML outperformed heavier alternatives with larger system prompts, more context, and added skills. ([5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s), confidence: stated)
- If a small model can author workable code in a format, larger coding agents certainly can, and the format will keep improving as models improve and training data accumulates. ([5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s), confidence: stated)
- Browsers are asynchronous by design, which makes them unsuitable for video rendering without freezing the clock and forcing full asset load per frame. ([6:39](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=399s), confidence: stated)
- Anything renderable in a browser — Three.js, charts, SVGs, shaders, WebGL, WebGPU, Lottie — can be rendered into a Hyperframes video. ([8:43](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=523s), confidence: stated)
- Agent skills should teach taste and domain craft rather than framework syntax, since the model already knows the underlying language. ([9:32](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=572s), confidence: stated)
- Single-shot prompting yields decent video, but great video requires the same craft and iterative decomposition as pre-AI software engineering. ([10:48](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=648s), confidence: stated)
- Hyperframes has rendered over 1.3 million videos for open-source users in 90 days, been tried by 267,000 creators, renders ~15,000 videos per day, and has 32,000 GitHub stars. ([12:29](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=749s), confidence: stated)
- Current models are still not good at creative work, and improving this requires a shared code-to-video benchmark rather than better prompts alone. ([13:12](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=792s), confidence: stated)
- Coding agents have made building easy, but launching a product — the post, the video — remains the harder bottleneck. ([1:14](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=74s), confidence: stated)
- Humans should remain in the loop with a full manual editing surface, so power users can do anything they would do in a conventional video editor. ([11:32](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=692s), confidence: implied)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [build versus buy](../concepts/build-versus-buy.md)
- [generative media pipelines](../concepts/generative-media-pipelines.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [small language models](../concepts/small-language-models.md)
- [structured output contracts](../concepts/structured-output-contracts.md)
- [web data infrastructure](../concepts/web-data-infrastructure.md)

