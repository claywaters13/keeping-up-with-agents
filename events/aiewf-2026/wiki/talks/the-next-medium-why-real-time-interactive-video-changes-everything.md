---
title: "The Next Medium: Why Real-Time Interactive Video Changes Everything"
type: "talk"
slug: "the-next-medium-why-real-time-interactive-video-changes-everything"
track: "Generative Media"
org: "Reactor"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "5dCAmSDOAjI"
duration_sec: 1050
word_count: 3093
speakers: ["Ahmed Ahres"]
---

# The Next Medium: Why Real-Time Interactive Video Changes Everything

*Program title: The Next Medium: Why Real-Time Interactive Video Changes Everything for Developers*

**Speakers:** [Ahmed Ahres](../speakers/ahmed-ahres.md)

**Org:** Reactor

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 17m 30s

[Watch on YouTube](https://www.youtube.com/watch?v=5dCAmSDOAjI)

## Summary

Ahmed Ahres, head of go-to-market at Reactor, argues that 'world models' are best understood as real-time interactive video, and that making video real-time changes the medium rather than merely speeding it up. He draws two historical analogies — GPS enabling Uber, and digital viewfinders enabling Instagram and TikTok — to claim that instant feedback unlocks entire application categories that were impossible with batch, prompt-and-wait generation. He surveys three model families (infinite interactive video like a real-time Veo/Sora, controllable world models like Genie 3, and live interactive avatars), the use cases Reactor's users are building on them (interactive livestreams, medical and cooking simulation, real-time video editing), and the infrastructure differences between batch and real-time inference: pixel streaming, persistent session memory, and sub-100ms global GPU routing. It's a short, opinionated market-and-infra overview rather than a technical deep dive — worth watching if you want a framing for why real-time generation is a distinct product category, plus a candid admission that evaluation for these models is unsolved.

## Key Points

- Ahres defines world models narrowly as real-time interactive video, rejecting the looser marketing usage that spans Gaussian splatting and ordinary video generation.
- Today's batch video models (Veo 3, Seedance 2) return a file you cannot alter, which he calls a slot machine; the core problem is not quality but the absence of control.
- Real-time capability changes what a medium is rather than just making it faster — GPS made Uber possible, and digital viewfinders that let creators see what they are shooting made Instagram and TikTok possible.
- He identifies three real-time model categories: infinite interactive video models, controllable world models in the Genie 3 mold, and live interactive avatars, which he says have not yet been cracked and remain 'kind of weird' in customer support settings.
- Beyond games, controllable world models feed robotics with unlimited simulated training data and could displace LLM- or textbook-based education with situated experiences.
- Real-time advertising — inserting a brand's logo into generated content based on what a viewer just searched for — would eliminate pre-produced ads, though brand caution will delay it.
- Reactor exposes four third-party models behind one API (ByteDance's Helios, Alibaba's Lingbo, and NVIDIA's LongLive-2 and a video-to-video editing model), positioning itself as the developer platform layer rather than a model trainer.
- Real-time inference infrastructure diverges from batch on three axes: streaming pixels to clients, maintaining memory across a persistent live session, and routing users to nearby GPUs to hold sub-100ms latency worldwide.
- Memory is the acknowledged weak point of current real-time world models — as in Genie 3 demos, a character that looks away and back will not remember the scene.
- Evaluating real-time world models for consistency is an open research problem that no lab including DeepMind has solved; the current practice is human judgment by eyeballing output.

## Notable Quotes

> "in today's world I think world models is a little bit of a marketing term that people think about it from a Gaussian splatting standpoint others from video but the way we define world models is really real time interactive video"
>
> — [0:01](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=1s) &middot; *Sets the talk's definitional stake against the industry's looser use of the term.*

> "you prompt them, you get back a file, you watch and good luck. It's a slot machine. You cannot change it. You cannot do anything about it."
>
> — [0:57](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=57s) &middot; *The talk's central framing of what's wrong with batch video generation.*

> "what happens when video becomes programmable like software. And what happens when pixels can be generated in real time?"
>
> — [0:57](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=57s) &middot; *States the animating question of the company and the talk.*

> "And real time changes what the medium is. It doesn't just make it faster."
>
> — [2:53](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=173s) &middot; *The thesis in one line — a claim about media, not latency.*

> "Now, you'd think GPS has just made it a bit faster to know where I am, but actually Uber would not exist if we did not have the GPS."
>
> — [2:53](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=173s) &middot; *The load-bearing historical analogy for why real-time unlocks new categories.*

> "Instagram and TikTok would not exist if we could not produce high-quality content and the only reason why we're able to produce high-quality content among many reasons is because we can see in real time what's happening."
>
> — [4:01](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=241s) &middot; *Second analogy, tying instant visual feedback directly to platform-scale outcomes.*

> "real-time actually ends the slot machine type of mentality and actually gives you the the control that you need. And a big thing I like to say is instant feedback is the ultimate level of control"
>
> — [5:46](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=346s) &middot; *Names control, not fidelity, as the binding constraint for creators.*

> "If I can know what you looked for a minute ago, why can't I insert the logo of whatever you've been looking for? Why can't I produce an ad in real-time in front of you?"
>
> — [6:21](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=381s) &middot; *Concrete and contested application, which the speaker admits he is not fond of.*

> "But, because you can control whatever you want to control in any environment, this creates a new opportunity to generate infinite amount of data for robotics."
>
> — [8:16](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=496s) &middot; *Links world models to the robotics data bottleneck he says is a huge market today.*

> "I don't actually believe that in the future of education is LLM based or textbook based."
>
> — [8:16](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=496s) &middot; *A sharp minority position on education against the prevailing LLM-tutor consensus.*

> "The thing with avatars, though, is it hasn't actually been cracked. They're still all kind of weird."
>
> — [9:05](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=545s) &middot; *Rare candor about a category many vendors claim is production-ready.*

> "Why? Because pixels can be generated in real time. So, there's no reason why I cannot put a live stream on X, YouTube, or Twitch and enable users to pick what happens next."
>
> — [9:43](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=583s) &middot; *The clearest example of a product shape only real-time generation permits.*

> "the thing that I think I like to drive home is building infrastructure for regular video generation models is very different from real time."
>
> — [11:43](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=703s) &middot; *The infrastructure argument that justifies a separate platform layer.*

> "you cannot just take what works for batch inference and apply to real time inference."
>
> — [11:43](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=703s) &middot; *Compact statement of the batch-vs-real-time infra tradeoff.*

> "one of the things that live live real-time models struggle with is memory. If you've seen demos from Genie 3, for example, we've all seen that the character can look back and then will not remember what what's going on."
>
> — [12:20](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=740s) &middot; *Names the specific unsolved failure mode with a public reference point.*

> "it needs to be sub-100 millisecond latency anywhere you are. And if you're deploying applications in the world, then someone based in India or someone based in Japan should be routed to a GPU that is based in India or Japan"
>
> — [13:02](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=782s) &middot; *Puts a hard number on the latency budget and its geographic implication.*

> "If not, if you don't have the compute worldwide, then the experiences are not real time anymore and it breaks completely the medium."
>
> — [13:02](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=782s) &middot; *Frames global GPU distribution as a correctness requirement, not an optimization.*

> "we use multiple GPUs um up to optimizing the model weights, applying quantization techniques. So, there are ways, it's just a matter of priorities"
>
> — [13:54](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=834s) &middot; *Answers how 16 FPS reaches 30 FPS and frames it as a prioritization choice.*

> "evaluation for these real-time models is an unsolved problem. So, today it's literally just look at it and human judgment. That's what it is today. And this is including, by the way, Deep Deep Mind and everything."
>
> — [16:20](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=980s) &middot; *The most consequential admission in the talk — no eval methodology exists for this class of model.*

## Positions

- World models should be defined as real-time interactive video, not as Gaussian splatting or offline video generation. ([0:01](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=1s), confidence: stated)
- Real-time generation changes the nature of the medium rather than only making existing workflows faster. ([2:53](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=173s), confidence: stated)
- Uber could not have existed without GPS, and Instagram and TikTok could not have existed without real-time visual feedback while shooting. ([3:28](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=208s), confidence: stated)
- The main unmet need of content creators using generative video is control, not output quality. ([5:46](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=346s), confidence: stated)
- Instant feedback is the highest attainable form of control, and it is unreachable without real-time generation. ([5:46](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=346s), confidence: stated)
- Once real-time generative advertising works, pre-produced ads will no longer be needed; brand risk aversion is what delays this, not capability. ([6:21](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=381s), confidence: stated)
- The future of education is neither LLM-based nor textbook-based but situated, steppable simulated experiences. ([8:16](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=496s), confidence: stated)
- Robotics world models are already a very large market, with many labs training such models. ([7:41](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=461s), confidence: stated)
- Interactive avatars remain unsolved and still feel off in customer support deployments. ([9:05](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=545s), confidence: stated)
- Current real-time video editing platforms built on these models are not yet good, limited by model quality. ([10:19](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=619s), confidence: stated)
- Batch inference infrastructure cannot be reused for real-time inference; streaming, live-session memory, and global compute are new requirements. ([11:43](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=703s), confidence: stated)
- Real-time interactive video requires sub-100ms latency everywhere, which forces geographically distributed GPU capacity. ([13:02](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=782s), confidence: stated)
- Memory is a current failure mode of live world models — Genie 3 demos show characters forgetting scenes when they look away and back. ([12:20](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=740s), confidence: stated)
- Raising real-time frame rates from 16 FPS to 30 FPS is achievable today via multi-GPU serving, weight optimization, and quantization; it is a prioritization question. ([13:54](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=834s), confidence: stated)
- No one, including DeepMind, has solved evaluation of consistency in real-time world models; the field relies on human eyeballing. ([16:20](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=980s), confidence: stated)
- The right layer for a startup here is the developer platform and infrastructure, letting the community build deterministic rule-checking and higher-level tooling on top. ([15:41](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=941s), confidence: implied)

## Concepts

- [generative media pipelines](../concepts/generative-media-pipelines.md)
- [latency budgets](../concepts/latency-budgets.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)
- [world models](../concepts/world-models.md)

