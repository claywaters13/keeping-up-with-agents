---
title: "Generative Video at the Speed of Light"
type: "talk"
slug: "generative-video-at-the-speed-of-light"
track: "Generative Media"
org: "uRun"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "Xln-On3syJk"
duration_sec: 522
word_count: 1226
speakers: ["Keegan McCallum"]
---

# Generative Video at the Speed of Light

**Speakers:** [Keegan McCallum](../speakers/keegan-mccallum.md)

**Org:** uRun

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 8m 42s

[Watch on YouTube](https://www.youtube.com/watch?v=Xln-On3syJk)

## Summary

Keegan McCallum, founder of the interactive-media inference provider uRun, argues that the interesting frontier in generative video is no longer quality but efficiency and long-horizon, real-time generation. He walks the quality timeline (Will Smith spaghetti → Sora → Sora 2 → SeeDance) only to set it aside, then demos Helios — a real-time distill of Wan 2.1 14B (auto-captioned as 'Juan 2.1') — which produces last-year's-frontier quality continuously and for roughly a hundredth of the cost of minutes-long batch generation. That cost collapse ($10 ≈ 3 hours of continuous video, $50 ≈ 15 hours) unlocks interaction patterns rather than clips: magic-mirror webcam transforms, visual companions for people who don't think in text, and content creation where you steer a generation in under a second instead of pulling a $10-per-minute slot machine. The second half is a pitch: serving this is the hard part (global GPUs, WebRTC/ICE/TURN, multi-model streaming pipelines), so uRun offers a drop-in React component over a programmable Python runtime, plus a CLI and MCP server so agents can build these apps. Worth watching if you care about real-time video infrastructure or interactive AI interfaces; it's eight minutes and mostly a landscape-plus-product talk, not a technical deep dive.

## Key Points

- The quality axis in generative video is largely solved at the frontier, and the underexplored axis is efficiency plus long-horizon continuous generation.
- Helios, a real-time distill of Wan 2.1 14B served by uRun, generates clips faster than a viewer can consume them at roughly the quality bar frontier models hit a year earlier.
- In a side-by-side, the real-time generation had better motion than the minutes-long batch generation and cost about 1/100th as much.
- At least 40 models with real-time and/or long-horizon generation capabilities shipped in the past year, spanning world models, avatar models, and video-to-video transformation.
- Economics have crossed a threshold: $10 buys about 3 hours of continuous generated video and $50 buys about 15 hours — a full day of interacting with AI in a visual medium.
- Real-time steering replaces the current 'slot machine' content-creation loop of prompts, keyframes, and ~$10 per minute of output, letting creators redirect a generation in under a second and later render a full-fidelity clip with a model like Google Gemini Omni.
- Video-native interaction is an accessibility story: it opens the benefits that text-oriented users already get from coding models to people who learn and think visually.
- The hard part of building these apps is serving infrastructure — globally distributed GPUs, WebRTC/ICE/TURN, and frame-synchronized multi-model streaming pipelines — which uRun abstracts behind a React component, a Python runtime, a CLI, and an MCP server.

## Notable Quotes

> "We have the classic Will Smith eating spaghetti from 2023. It is nightmare fuel and not something you would ever mistake for reality."
>
> — [0:01](https://www.youtube.com/watch?v=Xln-On3syJk&t=1s) &middot; *Sets the quality-timeline baseline the whole talk pivots away from.*

> "I'm here to talk about another axis which models are improving along, which is efficiency and, uh, the long horizon generations."
>
> — [0:57](https://www.youtube.com/watch?v=Xln-On3syJk&t=57s) &middot; *The talk's thesis in one line.*

> "And the other video, um, is a bunch of clips, um, that have been generated faster than you can consume them."
>
> — [0:57](https://www.youtube.com/watch?v=Xln-On3syJk&t=57s) &middot; *Defines what 'real-time' concretely means for video generation.*

> "they're about at the same quality as the frontier models were last year"
>
> — [0:57](https://www.youtube.com/watch?v=Xln-On3syJk&t=57s) &middot; *Names the explicit quality tradeoff accepted in exchange for speed.*

> "It's got better motion and it was generated for about a 100th of the cost."
>
> — [1:46](https://www.youtube.com/watch?v=Xln-On3syJk&t=106s) &middot; *The talk's headline number, and a claim that speed doesn't always cost quality.*

> "There's been at least 40 models with real-time capabilities and long horizon generation capabilities released this year."
>
> — [2:33](https://www.youtube.com/watch?v=Xln-On3syJk&t=153s) &middot; *Quantifies the pace of the field rather than asserting it vaguely.*

> "And so we're at a place right now where $10 can get you 3 hours worth of generated video continuously with most of these models and $50 would give you an entire day interacting with an AI in a visual medium."
>
> — [3:20](https://www.youtube.com/watch?v=Xln-On3syJk&t=200s) &middot; *Reframes video cost in terms developers already understand from token spend.*

> "You could ask to see yourself in a car you like or with a haircut you're considering."
>
> — [4:05](https://www.youtube.com/watch?v=Xln-On3syJk&t=245s) &middot; *Concrete consumer use case for real-time video-to-video.*

> "because these are open-ended models that can transform what they're seeing on a webcam in real time"
>
> — [4:05](https://www.youtube.com/watch?v=Xln-On3syJk&t=245s) &middot; *States the capability that separates these models from fixed-purpose filters.*

> "you know, working with AI involves a lot of reading and a lot of text. For some people that's more difficult."
>
> — [4:05](https://www.youtube.com/watch?v=Xln-On3syJk&t=245s) &middot; *Frames generative video as an accessibility argument, not just entertainment.*

> "Uh so, there's more opportunities to have companions or visual mediums that are going to allow more people to experience the things a lot of us have with coding models"
>
> — [4:48](https://www.youtube.com/watch?v=Xln-On3syJk&t=288s) &middot; *Ties the visual medium directly to the productivity gains developers already enjoy.*

> "so far we've very much had a slot machine type approach where you're setting up a prompt and maybe some key frames and spending about $10 a minute to try and get the shot that you want"
>
> — [4:48](https://www.youtube.com/watch?v=Xln-On3syJk&t=288s) &middot; *Names the current workflow's failure mode with a price attached.*

> "But with these models you can actually steer them in real time in under a second while they're generating and get the actual shots that you want."
>
> — [4:48](https://www.youtube.com/watch?v=Xln-On3syJk&t=288s) &middot; *States the proposed replacement for prompt-and-pray generation, with a latency figure.*

> "and with modern models like Google Gemini Omni, you can actually render these out as a more full fidelity clip"
>
> — [5:31](https://www.youtube.com/watch?v=Xln-On3syJk&t=331s) &middot; *Describes the draft-then-render pipeline that reconciles speed with final quality.*

> "You're going to need to set up probably WebRTC and ICE and TURN."
>
> — [6:13](https://www.youtube.com/watch?v=Xln-On3syJk&t=373s) &middot; *Concretely names the unglamorous infrastructure most teams underestimate.*

> "And for the most interesting use cases, you're going to want a model wire multiple models together in continuous streaming workflows"
>
> — [6:13](https://www.youtube.com/watch?v=Xln-On3syJk&t=373s) &middot; *Argues the interesting applications are multi-model pipelines, not single-model calls.*

> "And so, our idea is what if there was just a React component that you could drop into your application to make it easy to provide video interactively inside your applications with any model."
>
> — [6:13](https://www.youtube.com/watch?v=Xln-On3syJk&t=373s) &middot; *The product thesis stated plainly.*

> "And I argue that in 2026, don't just need platforms, we need software factories and ways for agents interact with these."
>
> — [7:07](https://www.youtube.com/watch?v=Xln-On3syJk&t=427s) &middot; *An explicit, contestable claim about how AI infrastructure should be packaged.*

> "And so the models are here and the frontier is really in how we serve them."
>
> — [7:07](https://www.youtube.com/watch?v=Xln-On3syJk&t=427s) &middot; *The closing argument: the bottleneck has moved from model capability to serving.*

## Positions

- The important axis of improvement in generative video is now efficiency and long-horizon generation, not frontier quality. ([0:57](https://www.youtube.com/watch?v=Xln-On3syJk&t=57s), confidence: stated)
- Real-time generation is not necessarily worse than slow batch generation — the real-time sample had better motion at about 1/100th the cost. ([1:46](https://www.youtube.com/watch?v=Xln-On3syJk&t=106s), confidence: stated)
- Today's real-time models sit at roughly the quality bar that frontier video models hit one year ago. ([0:57](https://www.youtube.com/watch?v=Xln-On3syJk&t=57s), confidence: stated)
- At least 40 models with real-time and long-horizon capabilities were released in the past year. ([2:33](https://www.youtube.com/watch?v=Xln-On3syJk&t=153s), confidence: stated)
- $10 buys about 3 hours of continuous generated video and $50 buys about 15 hours, comparable to what developers already burn on coding tokens. ([3:20](https://www.youtube.com/watch?v=Xln-On3syJk&t=200s), confidence: stated)
- Current generative video content creation is a slot machine costing about $10 per minute of output, and sub-second real-time steering is the better workflow. ([4:48](https://www.youtube.com/watch?v=Xln-On3syJk&t=288s), confidence: stated)
- Generative video is an accessibility technology that extends AI's benefits to people who don't think or learn in text. ([4:05](https://www.youtube.com/watch?v=Xln-On3syJk&t=245s), confidence: stated)
- The discussion of real-time video should not be confined to world models; the more interesting applications are broader. ([5:31](https://www.youtube.com/watch?v=Xln-On3syJk&t=331s), confidence: implied)
- Building interactive video apps requires globally distributed GPUs, WebRTC/ICE/TURN, and frame-synchronized multi-model pipelines, which is hard enough to justify a hosted abstraction. ([6:13](https://www.youtube.com/watch?v=Xln-On3syJk&t=373s), confidence: stated)
- In 2026 developers need software factories with CLI and MCP access for agents, not just platforms. ([7:07](https://www.youtube.com/watch?v=Xln-On3syJk&t=427s), confidence: stated)
- The models are good enough already; the remaining frontier is serving infrastructure. ([7:07](https://www.youtube.com/watch?v=Xln-On3syJk&t=427s), confidence: stated)

## Concepts

- [agent tool design](../concepts/agent-tool-design.md)
- [generative media pipelines](../concepts/generative-media-pipelines.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [latency budgets](../concepts/latency-budgets.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [world models](../concepts/world-models.md)

