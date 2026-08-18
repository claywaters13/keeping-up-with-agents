---
title: "HTML is All You Need (for Agents to Make Graphics)"
type: "talk"
slug: "html-is-all-you-need-for-agents-to-make-graphics"
track: "Generative Media"
org: "Nori"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "JRTAtZ5iBkU"
duration_sec: 420
word_count: 1152
speakers: ["James Russo"]
---

# HTML is All You Need (for Agents to Make Graphics)

*Program title: HTML Is All Agents Need*

**Speakers:** [James Russo](../speakers/james-russo.md)

**Org:** Nori

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 7m 00s

[Watch on YouTube](https://www.youtube.com/watch?v=JRTAtZ5iBkU)

## Summary

Amol Kapoor, CEO of Nori, argues that agents aren't bad at graphics — the tools we hand them are wrong. Canvas-based tools (PowerPoint, Figma, Slides) and raw SVG force models to reason in pixels and coordinates, which is a human's native medium, not a model's. His fix is to make HTML the editing format: models have seen billions of examples, HTML tags carry semantic layout meaning, and the browser handles pixel placement so the model never sets a coordinate. He shows Nori using this for board decks, sales decks, docs, and even the video itself ("literally just divs all the way down"), and notes the editing format is arbitrary since audiences only see the presentation mode. The closing pitch is a general design principle for agent tooling: stop thinking like a user, think like the model.

## Key Points

- Agents' poor visual output is a medium problem rather than a model-capability problem — the same model that fails at hand-written SVG succeeds when asked for HTML.
- Canvas tools like PowerPoint, Figma, and Canva encode their data in application-private formats designed around human click-drag-resize motions, which agents cannot manipulate coherently.
- The Simon Willison 'pelican riding a bicycle' SVG test is a poor proxy for spatial reasoning because no human could hand-write that SVG either.
- HTML works as an agent-native graphics medium because tags carry built-in layout semantics, models have massive training exposure to it, and the browser converts structure to pixels.
- The editing format for a deck is arbitrary — the audience only ever sees presentation mode — so you should pick whatever format agents are already good at and render to PDF or another target later.
- HTML output stays fully readable, themeable, and line-editable, unlike opaque binary or canvas formats.
- A well-formatted deck is worthless without content, so the bigger unlock is giving the model access to company data (call transcripts, emails, Slack, docs) so it can build decks end to end.
- The generalizable principle is to build agent tools around how the model thinks — in words, tokens, and structure — instead of porting human interaction patterns.

## Notable Quotes

> "Most people think coding agents only write code. But if you ask me, that's just bad marketing."
>
> — [0:07](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=7s) &middot; *Frames the talk's central reframing of what coding agents are for.*

> "You have to be able to think like an agent to get it to do what you want it to do."
>
> — [0:07](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=7s) &middot; *States the thesis in one line, before any of the HTML specifics.*

> "Every day, the world pours something like 34,000 human years into making slide decks. Most of that time isn't the thinking, it's the fiddling."
>
> — [0:53](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=53s) &middot; *The only hard number in the talk, and it sizes the problem.*

> "A deck that takes 10 hours should really take about 25 minutes once you remove all the formatting and the branding and the moving things around."
>
> — [0:53](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=53s) &middot; *Quantifies the claimed upside of removing manual formatting work.*

> "Every one of these tools is built for human hands and human eyes."
>
> — [0:53](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=53s) &middot; *Compact statement of why canvas tools fail agents.*

> "There is a data structure underneath, but it's in a format that only the application can read."
>
> — [1:39](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=99s) &middot; *Names the specific technical reason agents can't drive design tools.*

> "AI skeptics say that it's not just the tools. Agents fundamentally can't reason about space."
>
> — [1:39](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=99s) &middot; *States the opposing position the talk is arguing against.*

> "If you ask me, it's not the model, it's the medium."
>
> — [2:20](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=140s) &middot; *The talk's core claim, stated as a direct rebuttal to the skeptic position.*

> "If I asked you, someone who is presumably human, to handwrite an SVG of a pelican, you wouldn't be able to do that either."
>
> — [2:20](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=140s) &middot; *The argument that invalidates the pelican benchmark as a capability test.*

> "Asking an AI to use a canvas is like asking a human to write SVG by hand. It doesn't really make sense."
>
> — [2:57](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=177s) &middot; *The talk's key analogy, inverted to indict the whole class of agent design tools.*

> "You need to give the AI tools based on how it thinks, not in pixels, in language. Words, tokens, structure, that is its native medium."
>
> — [2:57](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=177s) &middot; *Generalizes the argument from graphics to agent tool design broadly.*

> "HTML lets the model think in structure. HTML tags have meanings built into the language."
>
> — [3:39](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=219s) &middot; *The mechanism behind why HTML beats SVG for models.*

> "So, the model never actually places a coordinate, and you can get all sorts of visual effects, charts and layouts, fonts and motion, all of it for free."
>
> — [3:39](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=219s) &middot; *Explains what the browser absorbs on the model's behalf.*

> "PowerPoint is a tool that you use to make slide decks. The deck itself, that's just the presentation mode."
>
> — [4:28](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=268s) &middot; *Separates editing format from output format, which licenses the whole approach.*

> "The editing format is totally arbitrary."
>
> — [4:28](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=268s) &middot; *The pivotal permission-granting claim of the talk.*

> "What you're watching is just HTML and CSS. It's literally just divs all the way down."
>
> — [5:07](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=307s) &middot; *Self-demonstrating evidence — the talk video itself is the artifact.*

> "Plain text is a choice, generally a choice of convenience, but it's usually the wrong one if you're actually trying to create something of use."
>
> — [5:07](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=307s) &middot; *A contrarian take on agent output defaults that extends beyond slides.*

> "I do want to take a quick beat here and point out that a beautiful deck on its own is generally not worth anything."
>
> — [5:50](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=350s) &middot; *Honest caveat that formatting is the smaller half of the problem.*

> "Let your agents do all the grunt work while you focus on vision and story."
>
> — [5:50](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=350s) &middot; *States the intended division of labor between human and agent.*

> "Stop thinking like a user. Think like the model. Give it the right language, and for graphics, all you need is HTML."
>
> — [6:26](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=386s) &middot; *The explicit single takeaway the speaker asks the audience to keep.*

## Positions

- Agents' failure at graphics is caused by the medium they are given, not by a model limitation in spatial reasoning. ([2:20](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=140s), confidence: stated)
- Coding agents are general-purpose agents; calling them 'coding' agents is a marketing artifact that understates what they can do. ([0:07](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=7s), confidence: stated)
- The pelican-in-SVG test measures the difficulty of the medium more than the model's spatial ability, since humans also cannot hand-write such an SVG. ([2:20](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=140s), confidence: stated)
- Canvas-based agent tooling — Figma MCPs, PowerPoint CLIs, screenshot-and-replace loops — is the wrong approach because it makes agents imitate human interaction patterns. ([2:57](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=177s), confidence: stated)
- HTML is the right authoring medium for agent-generated graphics because models have trained on billions of examples of it and its tags carry layout semantics. ([3:39](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=219s), confidence: stated)
- The editing format of a deck does not matter because audiences only ever see the presentation mode, so you can choose HTML and render to PDF later. ([4:28](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=268s), confidence: stated)
- Roughly 34,000 human years per day go into making slide decks, most of it formatting rather than thinking. ([0:53](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=53s), confidence: stated)
- A 10-hour deck should take about 25 minutes if formatting, branding, and layout fiddling were removed. ([0:53](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=53s), confidence: stated)
- Plain text is usually the wrong output default for agents producing artifacts meant to be used. ([5:07](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=307s), confidence: stated)
- Formatting is the easy half of the problem; the real value comes from connecting the model to company data so it can source deck content itself. ([5:50](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=350s), confidence: stated)
- Arc AGI-style benchmarks are built on the premise that agents cannot reason about space, a premise the speaker rejects. ([1:39](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=99s), confidence: implied)

## Concepts

- [agent tool design](../concepts/agent-tool-design.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [generative media pipelines](../concepts/generative-media-pipelines.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [web data infrastructure](../concepts/web-data-infrastructure.md)
- [world models](../concepts/world-models.md)

