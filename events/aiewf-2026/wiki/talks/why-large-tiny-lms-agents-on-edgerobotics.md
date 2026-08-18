---
title: "Why Large? Tiny LMs & Agents on Edge/Robotics"
type: "talk"
slug: "why-large-tiny-lms-agents-on-edgerobotics"
track: "Robotics & World Models"
org: "Google"
day: "Day 3 — Session Day 2"
room: "Track 2"
video_id: "hacEQHHhu2Q"
duration_sec: 1304
word_count: 3960
speakers: ["Cormac Brick"]
---

# Why Large? Tiny LMs & Agents on Edge/Robotics

**Speakers:** [Cormac Brick](../speakers/cormac-brick.md)

**Org:** Google

**Track:** Robotics & World Models &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 2 &nbsp;|&nbsp; **Duration:** 21m 44s

[Watch on YouTube](https://www.youtube.com/watch?v=hacEQHHhu2Q)

## Summary

Cormac Brick, a tech lead on Google's AI Edge team, argues that getting AI into the vast majority of devices — not just high-end phones and expensive robots — requires dropping below the 1–4B parameter "small model" class into genuinely tiny models of roughly 50M–500M parameters. He first surveys what small models can already do on edge hardware, walking through aggressive quantization (a 2B Gemma model squeezed to ~2.9 bits per weight and 841MB of weights) and measured decode speeds on Raspberry Pi, Jetson Orin Nano, and a Qualcomm NPU board. The core constraint driving everything is DRAM cost, which he says is rising sharply — a Raspberry Pi 3 with 6GB has gone up ~2.5x since launch, and some phone makers are shipping less RAM this year than last. His main claim is that a fine-tuned tiny model plus a synthetic dataset of 10K–10M samples can match or beat a 2–4B model on a single fixed task while running far faster on far cheaper hardware, demonstrated with an 86%+ reliable voice-to-function-calling model and a fully offline voice dictation app built from two fine-tuned tiny Gemma models. Worth watching if you're shipping on-device AI and need concrete numbers on quantization, throughput, and the fine-tuning playbook rather than cloud-scale benchmarks.

## Key Points

- DRAM cost is the dominant and newly acute constraint on edge AI — Raspberry Pi memory pricing has risen ~2.5x since launch and some phone manufacturers are shipping less RAM this year than previously, which casts a shadow over every other design decision.
- "Small" models of 1–4B parameters realistically need 4–8GB of device DRAM once you add the KV cache, runtime, and OS, which limits them to laptops, high-end phones, and higher-end electronics and rules out most IoT, consumer robotics, and low-tier browsers.
- Google's team gets a 2B Gemma model down to roughly 2.9 bits per weight (~841MB of weights) using a mix of 2-bit, 4-bit, and 8-bit quantization plus tricks like per-layer embeddings.
- Concrete throughput numbers: ~7.6 tokens/sec decode for a 2B model on Raspberry Pi (roughly 2x with MTP enabled), ~24 tok/s on a Jetson Orin Nano, and ~4,000 tok/s prefill with 31 tok/s decode on a Qualcomm IoT NPU board — enough for about three high-resolution frames per second.
- Small models are easy because the playbook is just zero-shot prompting (optionally LoRA adapters); tiny models require a harder playbook of either off-the-shelf fixed-task models (ASR, vision, embeddings) or task-specific fine-tuning.
- Dropping from 2B to ~270M parameters raises Raspberry Pi decode from mid-single-digit tokens per second to about 45, because far less has to be read from memory each step.
- Synthetic data in the 10,000 to 10 million sample range is generally sufficient to fine-tune a tiny model to high reliability; the team open-sourced a 'mobile actions' dataset on Hugging Face so others can reproduce their function-calling demo on Function Gemma.
- Real production examples: a text-in/function-call-out mobile actions model covering ~10 functions at over 86% reliability, an ASR front-end giving voice-to-function-calling, and a subscription-free offline dictation app built from two fine-tuned tiny Gemma models that also cleans up filler words and biases toward personal names.
- Tiny models are also what let features like Chrome's built-in summarization and proofreading APIs reach a much wider user base than a larger model could.
- A practical caveat from a demo robot: the same application on Jetson Orin Nano feels real-time while the Raspberry Pi version works but is too slow to meet user interaction requirements.

## Notable Quotes

> "If we want uh for intelligence to get into lots and lots and lots of devices and not just really expensive robots, we are going to need tiny models."
>
> — [0:01](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=1s) &middot; *The thesis of the talk in one sentence.*

> "then even though those tokens are relatively cheap, you're multiplying it by a large number and it'll add up quickly"
>
> — [3:04](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=184s) &middot; *States the cost argument for edge inference at consumer scale.*

> "you'll even see some mobile phone manufacturers are putting less DAM into their devices this year than previously"
>
> — [3:04](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=184s) &middot; *Counterintuitive market signal that motivates the whole memory-budget framing.*

> "You'll also see that since since launch, the cost of a Raspberry Pi 36 gigabytes has gone up by a factor of like 2.5x."
>
> — [3:04](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=184s) &middot; *A hard number on the DRAM cost pressure driving the argument.*

> "in order to be able to get AI applications running on the edge, we need to really think a lot about kind of quantization and we also really need to think about what is the smallest possible um model we can use for a given task"
>
> — [3:50](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=230s) &middot; *Names the two levers the rest of the talk develops.*

> "it's kind of fair to say that a lot of the research uh hours that go into LLMs these days are into the much larger models um and techniques and this types of stuff um and the the lower end of the LLM spectrum is a lot less studied"
>
> — [3:50](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=230s) &middot; *A pointed claim about where research attention is misallocated.*

> "so it uses a mix of like two bit, four bit and 8 bit quantization getting it down to like I know like 2.9 bits per weight if you look at the actual weights we need to hold in memory"
>
> — [6:33](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=393s) &middot; *Specific quantization result behind the sub-1GB footprint claim.*

> "if we take that two billion parameter model and run it on a Raspberry Pi. Um that is will give about 7.6 tokens per second decode. This is without MTP."
>
> — [7:24](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=444s) &middot; *Baseline throughput number for the cheapest tier of hardware.*

> "you can get about like almost 4,000 tokens per second uh preill uh 31 tokens per second decode and that's useful for lots of like almost real-time um uh applications uh on an NPU"
>
> — [8:05](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=485s) &middot; *Shows how much NPU acceleration changes what is feasible.*

> "One medium resolution image is like kind of 500 tokens. A high resolution image is 1120 tokens."
>
> — [8:05](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=485s) &middot; *Concrete token accounting for vision input on edge devices.*

> "we're still at a point where small models are too big because they can't reach like older laptops or kind of more consumer edge devices"
>
> — [11:37](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=697s) &middot; *The pivot from small models to tiny models, stated as a limitation.*

> "the the model you want to run isn't the main feature in the application. It's like one tiny thing in a corner that needs to run while everything else in the system is running"
>
> — [12:16](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=736s) &middot; *System-health framing that most model-size discussions ignore.*

> "So here that kind of jumps up to 45 tokens per second because we need to read less uh from memory each time."
>
> — [14:44](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=884s) &middot; *Quantifies the speedup from shrinking the model and attributes it to memory bandwidth.*

> "this model knows about 10 different output functions and can call them at over 86% uh reliability from a given arbitrary text input"
>
> — [14:44](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=884s) &middot; *The headline reliability number for fine-tuned tiny-model function calling.*

> "voice to function calling is pretty key for lots of IoT and edge devices because um yeah like smaller devices tend to have you know require settings menus and that user interface can be really really challenging for lots of people"
>
> — [15:29](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=929s) &middot; *Explains why this specific capability is the highest-value one on edge hardware.*

> "we we've generally found that in the range of 10,000 to 10 million samples of synthetically generated um data will be sufficient to fine-tune a smaller model to a really really high degree of reliability"
>
> — [16:49](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=1009s) &middot; *The single most actionable number in the talk for anyone attempting the playbook.*

> "if you're willing to put the time and energy into creating a synthetic data set and fine-tuning a model you can achieve a similar like the same or greater quality with a model that is much much smaller will work on a much wider set of devices and will be much much more responsive"
>
> — [16:49](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=1009s) &middot; *States the central tradeoff: engineering effort bought in exchange for model size.*

> "this allows us to take something that would have been a kind of like server only feature of, you know, where you require a subscription to do highly accurate uh voice dictation and have an app that's just able to do that completely offline with very very good quality"
>
> — [18:11](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=1091s) &middot; *Ties the technique to a shipped product and a changed business model.*

> "delivering those features via tiny models allows um the Chrome team to ship them to a much wider set of uh Chrome users than would otherwise be possible"
>
> — [18:48](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=1128s) &middot; *Reach, not capability, is the payoff being optimized for.*

## Positions

- Reaching the majority of devices with AI requires models in the 50M–500M parameter range, not the 1–4B 'small model' class. ([12:16](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=736s), confidence: stated)
- DRAM cost, not compute, is the binding constraint on edge AI deployment, and it is getting worse rather than better. ([3:04](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=184s), confidence: stated)
- The low end of the LLM parameter spectrum is under-researched relative to large models. ([3:50](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=230s), confidence: stated)
- A tiny fine-tuned model can match or exceed the quality of a 2–4B model on a single fixed task such as summarization or proofreading. ([16:49](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=1009s), confidence: stated)
- 10,000 to 10 million synthetic samples is sufficient to fine-tune a tiny model to high reliability for a given task. ([16:49](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=1009s), confidence: stated)
- For small models the right playbook is zero-shot prompting and LoRA adapters, whereas for tiny models you must fine-tune unless an off-the-shelf fixed-task model exists. ([12:48](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=768s), confidence: stated)
- Speedups from shrinking models come primarily from reading fewer bytes from memory per token, not from arithmetic reduction. ([14:44](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=884s), confidence: stated)
- A 2B-class model needs roughly 4GB+ of device DRAM in practice once KV cache, runtime, and the OS are accounted for. ([6:33](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=393s), confidence: stated)
- Raspberry Pi-class hardware running a 2B model is too slow to meet real-time user interaction requirements, while Jetson-class hardware is not. ([10:54](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=654s), confidence: stated)
- Voice-to-function-calling is the key interaction pattern for edge and IoT devices because their settings-menu interfaces are hard for many people to use. ([15:29](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=929s), confidence: stated)
- Generalizing voice-to-function-calling — ideally by having an agent generate the synthetic dataset for you — is the most important next step for tiny models. ([20:01](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=1201s), confidence: stated)
- Developing edge AI for first-party Google products first and then open-sourcing the tooling is the more effective route to broad adoption. ([1:20](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=80s), confidence: implied)

## Concepts

- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [local inference](../concepts/local-inference.md)
- [post-training](../concepts/post-training.md)
- [quantization](../concepts/quantization.md)
- [small language models](../concepts/small-language-models.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)
- [voice agents](../concepts/voice-agents.md)

