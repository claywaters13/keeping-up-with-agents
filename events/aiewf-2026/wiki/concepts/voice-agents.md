---
title: "voice agents"
type: "concept"
slug: "voice-agents"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 11
---

# voice agents

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **11** speaker(s)

**Definition:** Real-time speech-driven agents and the pipeline concerns unique to them — turn taking, barge-in, endpointing, and conversational latency.

*Also referred to as: latency-sensitive voice agents, cascaded voice pipeline, speech-to-speech models, real-time conversational ai, voice interfaces, turn detection, barge-in handling, voice activity detection*

## State of Practice

Voice agent work at this conference was framed almost entirely as a latency-engineering and control-flow problem rather than a model-quality problem. The shared numbers are concrete: humans swap turns in ~200ms, the experience degrades around 800ms, users abandon at 1.5s, and the practical target for first audio is ~950ms — while a standard cloud cascaded pipeline (VAD → STT → LLM → TTS) lands at 1,100–1,300ms with LLM time-to-first-byte (500–650ms) as the dominant term and STT+LLM eating roughly two-thirds of the budget. That budget rules out frontier reasoning models, so teams converged on Haiku-class or fine-tuned tiny models with the state machine, step advancement, and completion judgments lifted out of the model and into application code; scaffolding is treated as a one-time cost in code versus reasoning as a per-turn cost. Turn detection is the least settled layer: pure VAD cannot distinguish a breath from a finished thought, STT-provider endpointing decides better but destroys observability, and the best deployable open model (Smart Turn v3.2) runs at 58.9% recall / 68.4% precision with a VAD timer underneath as a safety net. P95 matters more than P50 because one slow turn kills a conversation, and instruction following visibly decays after 15–20 turns. A separate faction argues the whole turn-based submit-and-wait protocol is the actual defect — that transcribed speech is still batch, and the fix is either routing output to visuals (a ~1s forgiving envelope) or building systems that follow a conversation continuously and choose their own moment to speak.

## Consensus

### Voice agents live inside a sub-second latency budget measured against human turn-taking (~200ms), with perceptible degradation around 800ms and user abandonment by ~1.5s.

Support: **3** talk(s)

> "because 200 milliseconds is how fast humans switch turns with each other in a conversation. And the implications are pretty brutal because at 800 milliseconds, things start to feel off. While at 1.5 seconds, your user just hang up on you"
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [2:18](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=138s)

Supporting talks: [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)

### Frontier reasoning models are the wrong choice for the real-time speaking layer; a small fast model (Haiku-class or a fine-tuned tiny model) is correct because reasoning latency costs more than answer quality gains.

Support: **4** talk(s)

> "A frontier model that think for a full second has already lost the room, no matter how good the answer is."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [0:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=51s)

Supporting talks: [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

### Voice agent quality is determined by the system around the model — audio pipeline, harness, state machine — not by the model itself; a perfect model in a bad pipeline still feels broken.

Support: **3** talk(s)

> "These are all audio engineering problems. They are not LLM problems because you can have the perfect model, perfect track but the experience still might feel broken if the turn taking is off."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [0:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=3s)

Supporting talks: [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

### Speech is the highest-bandwidth human input channel — roughly 3x faster than typing (~200 wpm) — and should be the default way to get thoughts into an AI system.

Support: **3** talk(s)

> "because you may not be aware, but voice dictation, even though it is pretty awkward to talk into your computer with a bunch of co-workers around, it is the fastest way to get your thoughts onto paper."
>
> — [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md), [2:46](https://www.youtube.com/watch?v=I3bpdgFJCUY&t=166s)

Supporting talks: [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)

## Disagreements

### Should the agent wait for the user's turn to end before running inference, or respond continuously while the user is still speaking?

| Position A | Position B |
|---|---|
| Detect end of turn properly and then respond: combine a semantic turn-detection model with a VAD silence timer, tune minimum-silence per domain (~200ms for sales, 1000-1200ms where users need thinking time), and treat endpointing accuracy as the core engineering problem.<br>*[Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)* | Endpointing is the wrong frame — fire inference every 1-2 seconds while the user is still talking, or build a system that continuously follows the conversation and picks its own moment to act, because waiting for silence spends the entire latency budget and the single-slot submit protocol is itself the defect.<br>*[Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [Perception Agents](../talks/perception-agents.md)* |

*Why it matters: It decides whether the engineering effort goes into turn-detection models and VAD tuning or into speculative/streaming inference and prefix-cache architecture, and whether P95 latency is a budget to shave or a constraint you design around entirely.*

### Is voice-in/voice-out the target experience, or should the response come back as visuals?

| Position A | Position B |
|---|---|
| Keep optimizing the voice-to-voice cascaded pipeline; ~755ms is the best measured today, ~500ms is achievable by co-locating models in one GPU cluster, and holding the LLM to sub-700ms TTFT plus a ~950ms first-audio target makes it work.<br>*[Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)* | Fully conversational voice-out needs 200ms or less end-to-end, which is not attainable; switch to voice-in/visuals-out and inherit the roughly one-second forgiving envelope people grant visual responses, no novel architecture needed.<br>*[Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)* |

*Why it matters: It changes the entire stack: a TTS-terminated audio pipeline with tail-latency engineering versus a rendering surface with a slower budget, and it changes which latency number counts as failure.*

### Does using voice as the input channel actually change the interaction model?

| Position A | Position B |
|---|---|
| Yes — dictation is the productivity unlock; speak the messy version of your thinking, capture scrappy unformatted raw material, and let downstream agents structure it.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* | No — speech gets transcribed into the same one-slot text box and submitted, so voice inherits the batch punch-card protocol unchanged; even speech-to-speech models cannot tell whether words were addressed to them.<br>*[The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)* |

*Why it matters: If voice is just faster typing, the win is throughput and you ship dictation; if the protocol is the bottleneck, you have to build floor-holding and addressee modeling, which no dictation improvement will give you.*

## Practical Guidance

**Do:**

- Budget for first audio within ~950ms and hold the LLM to a sub-700ms time-to-first-token target for voice.
- Measure and gate on P95, not P50 — GPT-4.1 looked fine at P50 but spiked to 1.7s at P95, and Claude 3 exceeded 4 seconds.
- Run a semantic turn-detection model (Smart Turn v3.2, BSD-2, 8MB, pip-installable) with a VAD silence timer underneath as a safety net, rather than either alone.
- Tune minimum-silence-milliseconds per domain: ~200ms for a sales agent, 1000-1200ms where users need thinking time.
- Move state tracking, step advancement, completion judgments, and answer selection into an explicit state machine in application code; let the model only propose and speak.
- Pick the fastest model your latency budget allows and spend the remaining engineering effort on scaffolding, since scaffolding is paid once in code and reasoning is paid every turn.
- Keep the first ~90% of the context prefix stable across requests to get prefix caching (up to 90% cheaper and faster inference).
- Prune context or reset the session after 15-20 turns, when instruction following starts to decay and the model gets verbose or drifts off-script.
- Distinguish interruption types — stop for corrections, keep talking through backchannels like 'yeah' and background noise.
- For edge and IoT, fine-tune a tiny (50M-500M) model for voice-to-function-calling on 10k-10M synthetic samples rather than shipping a 2-4B model.

**Avoid:**

- Don't put a frontier reasoning model in the response path — a full second of thinking has already lost the room.
- Don't fix step-skipping and looping with more prompt rules; when reliability approaches a coin flip, take control flow out of the model entirely.
- Don't rely on VAD silence alone for endpointing — a 300-400ms pause looks identical whether the speaker finished, took a breath, or is thinking.
- Don't adopt STT-provider turn detection without accepting that you lose all observability into why it fired or why it cut someone off.
- Don't assume a small parameter count means low latency — GPT-5 mini measured 5,000ms typical, 7,000ms P95, sometimes 10,000ms; the serving platform's latency prioritization matters as much as size.
- Don't burn the latency budget waiting for a full second of silence before starting inference.
- Don't chase unreleased research numbers — Meta's 87.7% recall turn detector has no released code and cannot be deployed.
- Don't trust demos: step-skipping, premature completion, and looping only show up once real users are in the loop.

## Notable Outliers

- 58.9% recall in turn detection is acceptable in production precisely because a VAD timer runs underneath — a miss costs latency, not correctness. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [10:32](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=632s))
- False interruptions have a measurable business cost: cutting users off incorrectly raises the rate at which they escalate to a human agent. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [20:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1203s))
- The three levels of turn-taking sophistication are configuration choices, not architectural ones — the Pipecat pipeline code is essentially identical across all three. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [13:39](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=819s))
- Speech-to-speech models today have no concept of who is speaking or whether words were even meant for them; backchanneling is not the same as knowing who holds the floor. ([The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [11:51](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=711s))
- A tiny model fine-tuned on synthetic data can call 10 different output functions at over 86% reliability from arbitrary text, enough to replace a subscription-gated server-side voice feature with an offline one. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [14:44](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=884s))
- A strong enough harness lets Haiku 4.5 replace Opus 4.7 at expected performance for live voice tutoring, while saving money, time, and latency. ([Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s))
- Sample-based singing synthesis with World pitch shifting is too heavy to run live and must be pre-baked before performance — real-time audio generation has a much harder compute floor than speech. ([While my guitar gently speaks](../talks/while-my-guitar-gently-speaks.md), [16:03](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=963s))

## All Talks

- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md)
- [Perception Agents](../talks/perception-agents.md)
- [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)
- [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)
- [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)
- [While my guitar gently speaks](../talks/while-my-guitar-gently-speaks.md)
- [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Allen Pike](../speakers/allen-pike.md)
- [Antje Barth](../speakers/antje-barth.md)
- [Ben Holmes](../speakers/ben-holmes.md)
- [Cormac Brick](../speakers/cormac-brick.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Ted Johnson](../speakers/ted-johnson.md)
- [Todd Fisher](../speakers/todd-fisher.md)

