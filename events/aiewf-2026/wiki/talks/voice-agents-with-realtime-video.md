---
title: "Voice agents with Realtime Video"
type: "talk"
slug: "voice-agents-with-realtime-video"
track: "Generative Media"
org: "LemonSlice"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "z1dqv74SpUs"
duration_sec: 1596
word_count: 3977
speakers: ["Lina Colucci"]
---

# Voice agents with Realtime Video

**Speakers:** [Lina Colucci](../speakers/lina-colucci.md)

**Org:** LemonSlice

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 26m 36s

[Watch on YouTube](https://www.youtube.com/watch?v=z1dqv74SpUs)

## Summary

Sidney Primas, CTO and co-founder of LemonSlice, lays out the company's technical bet on "breaking the Avatar Turing test" — making a video avatar indistinguishable from a human on a call. Rather than the rigged/lip-sync approaches most avatar companies use, LemonSlice trains a general video diffusion transformer (a "world model" narrowed to humans) and then converts it into a real-time, causal, single-step generator, which buys emergent capabilities like hands, object interaction, physics, and micro-expressions for free. The talk is unusually concrete about the hard parts: audio encoders trained on audiobooks are too monotone to drive expressive faces, causal attention masking creates error accumulation over hour-long generations, 30 denoising steps must be distilled to one, and the CPU/GPU orchestration ('model harness') that keeps a stream stutter-free is where much of the durable value sits. He claims per-stream cost is now roughly on par with a voice model, and predicts that within two to three years a single end-to-end "EQ model" will ingest user video/audio and emit avatar video/audio, paired with a separate IQ model for reasoning and tool calling. Worth watching if you build voice agents and want to know what adding a real-time visual layer actually costs and breaks.

## Key Points

- LemonSlice's approach is to train a general video DiT/world model and focus it on humans, accepting harder training and deployment in exchange for emergent full-body movement, hand and object interaction, physics, and micro-expressions rather than hand-engineering each one.
- Audio conditioning is the lever for expressiveness: standard audio encoders are trained largely on monotone audiobook data, so LemonSlice invested in its own audio data and embeddings to get emotion and facial expression right.
- Making a video model interactive requires training with a causal attention mask so it can only attend to the past — the future (including future audio) literally does not exist at inference time.
- Real-time generation requires distilling the usual ~30-step denoising process down to a single step from pure noise to output frame.
- Causal generation causes error accumulation, where each generated block's error feeds the next; this is the central hard problem for endless streams, and LemonSlice claims a novel (undisclosed) fix that supports 8- and even 16-hour continuous generations with no noticeable drift.
- Cost per stream has been driven down to roughly the same level as a voice model despite video being far more pixel-heavy, which is what unlocks consumer and entertainment use cases.
- The 'model harness' — orchestrating multiple threads, GPU/CPU work, buffers, queues, and interrupts so the video never stutters — is underrated and, in Primas's view, an increasing share of the value in any real-time AI application.
- The current gap is emotional reactivity: the model can already produce natural emotion and environment interaction, but it isn't controllable or deterministic enough to fire the right emotion at the right time, so LemonSlice is building an 'emotion engine' that predicts actions from the avatar's audio and pending text, targeting launch in one to two months (roughly Sept–Oct 2026).
- Primas predicts a bifurcation: a single end-to-end EQ model handling video/audio in and out plus an internal latent emotional state, driven by a separate IQ model that does the reasoning and tool calling.

## Notable Quotes

> "And Lemon Slice is on a mission to break the Avatar Turing test. What we mean by this is making an Avatar that is indistinguishable from a human on a video call."
>
> — [0:01](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1s) &middot; *States the company's north-star goal in one line.*

> "So, our bet here is in the long term we think most interactions between AI and humans will have a visual visual layer."
>
> — [4:07](https://www.youtube.com/watch?v=z1dqv74SpUs&t=247s) &middot; *The core market thesis others might dispute — that voice-only agents are a waypoint, not the endpoint.*

> "Essentially what we do is we take these world models and we focus them on humans."
>
> — [4:55](https://www.youtube.com/watch?v=z1dqv74SpUs&t=295s) &middot; *Names the architectural bet that separates them from lip-sync-based avatar vendors.*

> "even though it's harder to get the initial model working, it's harder to train the model, it's harder to deploy the model. Once you have a model, you get all of these nice emergent properties"
>
> — [4:55](https://www.youtube.com/watch?v=z1dqv74SpUs&t=295s) &middot; *Explicitly frames the tradeoff being taken: upfront difficulty bought against emergent capability.*

> "most audio encoders today are trained on basically audiobooks, which is very monotone, very simple, don't have a lot of emotions. So, if you want to have a very expressive model, you can't use those audio encoders"
>
> — [9:13](https://www.youtube.com/watch?v=z1dqv74SpUs&t=553s) &middot; *A specific, non-obvious failure mode in off-the-shelf audio encoders for expressive video.*

> "usually video models are bidirectional, so they can look into the past, but they actually also can look into the future"
>
> — [10:01](https://www.youtube.com/watch?v=z1dqv74SpUs&t=601s) &middot; *Sets up why offline video models can't simply be run in real time.*

> "we basically train a model with an attention mask so that the model can only look into the past. So, when you do inference, it never can see the future because the future doesn't exist because like you haven't given it those inputs yet."
>
> — [10:38](https://www.youtube.com/watch?v=z1dqv74SpUs&t=638s) &middot; *The concrete mechanism for interactivity, stated at implementation level.*

> "let's say 30 steps. You spend 30 steps like removing the noise to generate the beautiful beautiful videos. And what we need to do is go from like 30 steps, bring it out to one step."
>
> — [11:22](https://www.youtube.com/watch?v=z1dqv74SpUs&t=682s) &middot; *Quantifies the step-distillation requirement for real-time video.*

> "So now you're looking in the past, you're looking at the error, you're adding more error to it, and then just the error compounds over time."
>
> — [11:58](https://www.youtube.com/watch?v=z1dqv74SpUs&t=718s) &middot; *Cleanest statement of error accumulation, the defining problem in causal video generation.*

> "Like the teddy avatar is generating continuously non-stop frame by frame for 8 hours straight with like no reset throughout the entire process. We have another one that's going to be generating for 16 hours straight."
>
> — [12:36](https://www.youtube.com/watch?v=z1dqv74SpUs&t=756s) &middot; *Hard numbers on generation duration that make the error-accumulation problem concrete.*

> "we've been able to make the models small enough and efficient enough so that the costs are about the same as a voice model."
>
> — [13:20](https://www.youtube.com/watch?v=z1dqv74SpUs&t=800s) &middot; *The single most economically consequential claim in the talk.*

> "I feel like the model hardness is something that is often overlooked but is actually super important and super hard."
>
> — [14:11](https://www.youtube.com/watch?v=z1dqv74SpUs&t=851s) &middot; *Flags serving orchestration, not modeling, as the underrated engineering bottleneck.*

> "you have to orchestrate this perfectly in a way that like the video always remains real time. There is never any stutter that happens inside of the video."
>
> — [14:56](https://www.youtube.com/watch?v=z1dqv74SpUs&t=896s) &middot; *Defines the actual production SLA for a real-time avatar stream.*

> "It has the capabilities to do this. It's just not controllable enough to like make it real time with the conversation and not deterministic enough to to make it useful with the conversation."
>
> — [18:05](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1085s) &middot; *Names controllability, not capability, as the current blocker — a recurring theme across generative systems.*

> "So I strongly believe that in the end uh there'll be a single model um that is the EQ layer for AI."
>
> — [18:46](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1126s) &middot; *The forward-looking architectural prediction the rest of the roadmap hangs on.*

> "What we're not saying is that this EQ model will be very intelligent. Uh it'll be very it'll have very high EQ and it'll be very good at like interacting with people"
>
> — [19:38](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1178s) &middot; *Draws the EQ/IQ split explicitly, which is the debatable part of the prediction.*

> "but I feel strongly that within two or three years you'll be seeing these kinds of end-to-end EQ models coming on the market."
>
> — [20:32](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1232s) &middot; *A dated, falsifiable forecast.*

> "we're uh in the process of figuring out our own version of the Turing test for these avatars, which will just include real people."
>
> — [23:09](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1389s) &middot; *Commits to a public evaluation for a goal that is otherwise unfalsifiable marketing.*

> "Again, like the cost of this is at the same level as an audio model in terms of what we charge for it."
>
> — [25:06](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1506s) &middot; *Restates the cost parity claim in pricing terms, not just compute terms.*

> "I think there'll also be very cool architectural updates to to move to more of like a token approach instead of a diffusion approach that will make video like this type of video generation way cheaper."
>
> — [25:48](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1548s) &middot; *Takes a side on where real-time video architecture is headed: autoregressive tokens over diffusion.*

> "Now the way this is used, just for for kind of everybody's information, is we're mostly the API layer. So, we provide an API. People bring their own LLM. People bring their own usually like voices."
>
> — [7:40](https://www.youtube.com/watch?v=z1dqv74SpUs&t=460s) &middot; *Clarifies the product's position in the stack — a visual layer bolted onto existing voice agents.*

> "the funny thing is he was scheduled to be there for, you know, a quick minute, one interaction, and he actually stayed for 10 minutes."
>
> — [3:28](https://www.youtube.com/watch?v=z1dqv74SpUs&t=208s) &middot; *The one piece of engagement evidence offered for the realism claim.*

## Positions

- Most future AI-human interaction will include a visual layer, not just voice. ([4:07](https://www.youtube.com/watch?v=z1dqv74SpUs&t=247s), confidence: stated)
- Training a general video/world model and focusing it on humans beats the narrower approaches other avatar companies use, because capabilities like hands, object interaction, physics, and micro-expressions emerge rather than needing to be built. ([4:55](https://www.youtube.com/watch?v=z1dqv74SpUs&t=295s), confidence: stated)
- Standard audio encoders, trained mostly on monotone audiobook data, are unsuitable for driving expressive avatar video; custom audio embeddings are required. ([9:13](https://www.youtube.com/watch?v=z1dqv74SpUs&t=553s), confidence: stated)
- Interactive video generation requires a causally masked (past-only) model, which forfeits the bidirectional context standard video models rely on. ([10:38](https://www.youtube.com/watch?v=z1dqv74SpUs&t=638s), confidence: stated)
- Real-time generation requires collapsing ~30 denoising steps into a single step. ([11:22](https://www.youtube.com/watch?v=z1dqv74SpUs&t=682s), confidence: stated)
- LemonSlice has a novel, undisclosed solution to error accumulation that differs from what everyone else does, enabling 8- to 16-hour continuous generation with no noticeable drift. ([12:36](https://www.youtube.com/watch?v=z1dqv74SpUs&t=756s), confidence: stated)
- Real-time avatar video now costs about the same per stream as a voice model, which is what makes consumer use cases viable. ([13:20](https://www.youtube.com/watch?v=z1dqv74SpUs&t=800s), confidence: stated)
- For real-time AI applications, an increasing share of durable value lies in the serving harness — thread, queue, buffer, and interrupt orchestration across CPU and GPU — rather than in the model itself. ([15:28](https://www.youtube.com/watch?v=z1dqv74SpUs&t=928s), confidence: stated)
- The current limiter on lifelike avatars is controllability and determinism of emotion/action, not raw model capability. ([18:05](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1085s), confidence: stated)
- Anything describable in words can currently be generated as an avatar action or emotion; longer term, emotional state will live as a non-human-interpretable latent internal state. ([21:49](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1309s), confidence: stated)
- AI systems will split into a high-EQ end-to-end video/audio model on top and a separate high-IQ model doing reasoning and tool calling underneath. ([19:38](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1178s), confidence: stated)
- End-to-end EQ models taking user video/audio in and emitting avatar video/audio will reach the market within two to three years. ([20:32](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1232s), confidence: stated)
- LemonSlice will not pass its own avatar Turing test in 2026, but will publish the test so progress can be tracked. ([23:09](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1389s), confidence: stated)
- Building the IQ/agent layer — context, harness, tool use — is explicitly not LemonSlice's problem to solve; customers bring their own LLM. ([23:50](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1430s), confidence: stated)
- Token-based architectures will replace diffusion for real-time video and make it substantially cheaper. ([25:48](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1548s), confidence: stated)
- Lower generation cost matters not only for consumer margins but because the savings can be spent on higher resolution. ([25:06](https://www.youtube.com/watch?v=z1dqv74SpUs&t=1506s), confidence: stated)
- Humans absorb information better with a visual channel than through text or voice alone, which is the underlying justification for video avatars. ([4:07](https://www.youtube.com/watch?v=z1dqv74SpUs&t=247s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [generative media pipelines](../concepts/generative-media-pipelines.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)
- [vision-language models](../concepts/vision-language-models.md)
- [world models](../concepts/world-models.md)

