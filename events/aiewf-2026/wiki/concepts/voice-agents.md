---
title: "voice agents"
type: "concept"
slug: "voice-agents"
tier: "supporting"
maturity: "consolidating"
talk_count: 8
speaker_count: 9
---

# voice agents

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **8** talk(s) by **9** speaker(s)

**Definition:** Real-time speech-driven agents and the pipeline concerns unique to them — turn taking, barge-in, endpointing, and conversational latency.

*Also referred to as: latency-sensitive voice agents, cascaded voice pipeline, speech-to-speech models, real-time conversational ai, voice interfaces, turn detection, barge-in handling, voice activity detection*

## State of Practice

The field has stopped treating voice as a chat app with a microphone and started treating it as a latency budget with a model inside it. The consensus numbers are now concrete: humans swap turns in ~200ms, agents feel off at ~800ms, users hang up at ~1.5s, and a practical target is first audio at ~950ms — against a cascaded cloud pipeline that totals 1,100–1,300ms, of which LLM time-to-first-byte (500–650ms) plus STT eat roughly two-thirds. That budget makes reasoning frontier models structurally wrong for the turn loop, so the dominant architecture is a Haiku-class or tiny fine-tuned model that only talks, with state tracking, completion judgments, and answer selection lifted into a state machine or harness in application code, and heavy work handed off asynchronously. Turn detection is the other half of the stack and is explicitly an audio-engineering problem: VAD alone cannot distinguish a finished sentence from a breath, so production systems pair a semantic turn model (Smart Turn v3.2, 58.9% recall, 8MB, BSD-2) with a VAD silence timer as a safety net, and tune minimum-silence per domain rather than to a universal value. P95, not P50, is the metric that matters, because one 1.7s spike destroys a conversation. The unresolved frontier is the protocol itself — several speakers argue that even perfect turn detection preserves a one-slot, batch, punch-card exchange, and that the agent should be participating continuously rather than waiting to be handed the floor.

## Consensus

### Voice agents should run the smallest/fastest model the latency budget allows rather than a frontier reasoning model, because reasoning seconds cost more than answer quality gains.

Support: **4** talk(s)

> "Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)

Supporting talks: [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

### Conversational latency is a hard perceptual constraint measured in hundreds of milliseconds, not a nice-to-have: past roughly one second the user treats the agent as broken.

Support: **3** talk(s)

> "because 200 milliseconds is how fast humans switch turns with each other in a conversation. And the implications are pretty brutal because at 800 milliseconds, things start to feel off. While at 1.5 seconds, your user just hang up on you"
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [2:18](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=138s)

Supporting talks: [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)

### The real-time model should be a thin talker: state, control flow, and 'what happens next' belong in surrounding code, with heavy work offloaded to async or larger models outside the turn.

Support: **3** talk(s)

> "the model never really um has to think. It proposes, but ultimately it is the harness that decides."
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [4:04](https://www.youtube.com/watch?v=m24UKZomm7k&t=244s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)

### The strict one-turn-at-a-time exchange — user finishes, agent replies — is a limitation of the current interaction protocol rather than a property of conversation, and voice systems need to participate while the user is still speaking.

Support: **4** talk(s)

> "it's a protocol with exactly one slot. Your message, then it's reply. It has no concept of who's speaking, whether the words were even meant for it."
>
> — [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [11:51](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=711s)

Supporting talks: [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [Perception Agents](../talks/perception-agents.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)

## Disagreements

### Should a voice agent wait to detect the end of the user's turn before running inference, or should it run inference continuously while the user is still speaking?

| Position A | Position B |
|---|---|
| Detect the turn boundary well and then respond: tune minimum-silence per domain (~200ms for sales, 1000–1200ms where users need thinking time), layer a semantic turn-detection model over a VAD timer, and treat accurate endpointing as the core engineering problem.<br>*[Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)* | Don't wait for the turn to end at all — waiting a second for silence has already blown the budget; fire inference every 1–2 seconds mid-utterance, and more broadly build systems that follow the conversation and choose their own moment to speak.<br>*[Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [Perception Agents](../talks/perception-agents.md)* |

*Why it matters: The two designs imply different stacks: endpoint-then-infer optimizes VAD/turn models, prefix caching for a single call, and P95 TTFT, while continuous inference means speculative, repeatedly-discarded generations and a floor set by cost-per-inference rather than by silence thresholds.*

### Does swapping the modality to voice actually fix the interface, or does it just move the same batch protocol to a microphone?

| Position A | Position B |
|---|---|
| Voice is the right human input and visuals the right output; ship voice-in/visuals-out today, since the ~1s visual response envelope is forgiving enough that no novel architecture is needed — and dictation is ~3x faster than typing, so it should be the default input.<br>*[Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* | Speech changes nothing structurally — it is transcribed into the same single-slot submission — and neither chat nor voice is an adequate universal default; the protocol has to start participating, and modality/timing should be the AI's choice, not the user's.<br>*[The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [Perception Agents](../talks/perception-agents.md)* |

*Why it matters: If voice input is the fix, teams invest in STT, latency, and visual rendering on existing architectures; if it isn't, that investment leaves the core problem — the machine not knowing who is speaking, to whom, or when to engage — untouched.*

### To hit the voice latency budget with a small model, is the lever engineering scaffolding around a general model, or task-specific fine-tuning of a tiny one?

| Position A | Position B |
|---|---|
| Keep a general small model (Haiku-class) and pay a one-time cost in code: a state machine that tracks state, validates output, and decides what's next lets the small model perform at the level expected of a frontier model.<br>*[Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* | For the devices that matter you need 50M–500M parameter models, and at that scale prompting and LoRA stop working — you must fine-tune on 10k–10M synthetic samples per task, which yields e.g. 10-function voice-to-function-calling at 86% reliability offline.<br>*[Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)* |

*Why it matters: One path spends engineering time on harness code and keeps a cloud API dependency with its 500–650ms TTFB; the other spends it on synthetic data pipelines and eliminates the network hop entirely, which is the only way to reach hardware with constrained DRAM.*

## Practical Guidance

**Do:**

- Budget first audio at ~950ms; treat 800ms as the point the interaction starts feeling off and 1.5s as the abandonment threshold.
- Measure and gate on P95 TTFT, not P50 — models that look fine at P50 spike to 1.7s (GPT-4.1) or over 4s (Claude 3) at P95.
- Hold the LLM to a sub-700ms time-to-first-token target, and attack STT + LLM first since they consume ~2/3 of the latency budget.
- Pair a semantic turn-detection model with a VAD silence timer underneath, so a missed detection costs latency rather than a wrong interruption.
- Set minimum-silence per domain rather than globally: ~200ms for a sales agent, 1000–1200ms where users need thinking time.
- Move state tracking and 'is this step done / did the user succeed' judgments into an explicit state machine; let the model only propose and speak.
- Keep the first ~90% of the context identical request-to-request to exploit prefix caching (up to 90% cheaper and faster).
- Prune context or reset the session after ~15–20 turns, where instruction following starts to degrade.
- Co-locate STT, LLM, and TTS in one GPU cluster if you need to approach the ~500ms voice-to-voice floor.
- For edge/IoT voice-to-function-calling, fine-tune a tiny model on 10k–10M synthetic samples rather than shipping a 2B model that needs 4GB+ of device DRAM.
- Take control flow out of the model as soon as end-to-end reliability approaches a coin flip.

**Avoid:**

- Don't answer multi-step unreliability with more prompt rules — step-skipping and looping are control problems, not prompting problems.
- Don't put a reasoning frontier model inside the turn loop; a model that thinks for a full second has already lost the room.
- Don't pick the real-time model by parameter count alone — GPT-5 mini showed 5,000ms typical and 7,000ms P95 latencies despite being small and cheap.
- Don't rely on VAD alone: a 300ms pause looks identical whether it's a breath, a thinking pause, a backchannel, or a finished thought.
- Don't stop speaking on every detected interruption — corrections warrant stopping, backchannels and background noise don't, and false interruptions measurably raise escalation to human agents.
- Don't wait for a full second of silence before triggering inference; that alone blows the response budget.
- Don't adopt STT-provider turn detection without accounting for the loss of observability into why it fired.
- Don't validate on demo conditions — demos never surface the mid-lesson step-skipping and looping that real users trigger.
- Don't assume transcribing speech into the same single input slot changes the interaction protocol.

## Notable Outliers

- The best measured voice-to-voice response time for a cascaded pipeline is 755ms — still ~4x slower than natural human turn taking. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [3:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=187s))
- 58.9% recall turn detection is production-acceptable specifically because a VAD timer runs underneath, so misses cost latency rather than correctness; Meta's 87.7%-recall result is unusable because no code was released. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [10:32](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=632s))
- Current speech-to-speech models cannot tell whether the words they heard were addressed to them — a protocol limitation, not a model intelligence limitation. ([The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [11:51](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=711s))
- A strong enough harness let Haiku 4.5 replace Opus 4.7 in a live voice tutor at the expected performance level, saving money, time, and latency. ([Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s))
- A fine-tuned tiny model calls 10 different output functions at over 86% reliability from arbitrary text, running fully offline where dictation was previously a subscription server feature. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [14:44](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=884s))
- You should feel comfortable sending an AI a 15-minute voice memo with random tangents, because dictation is ~3x faster than typing and the messy version is fine. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [8:25](https://www.youtube.com/watch?v=il1c1a2FufU&t=505s))

## All Talks

- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [Perception Agents](../talks/perception-agents.md)
- [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)
- [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)
- [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)
- [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Allen Pike](../speakers/allen-pike.md)
- [Antje Barth](../speakers/antje-barth.md)
- [Cormac Brick](../speakers/cormac-brick.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Ted Johnson](../speakers/ted-johnson.md)

