---
title: "voice agents"
type: "concept"
slug: "voice-agents"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 13
---

# voice agents

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **13** speaker(s)

**Definition:** Real-time speech-driven agents and the pipeline concerns unique to them — turn taking, barge-in, endpointing, and conversational latency.

*Also referred to as: latency-sensitive voice agents, cascaded voice pipeline, speech-to-speech models, real-time conversational ai, voice interfaces, turn detection, barge-in handling, voice activity detection*

## State of Practice

Voice is the one agent domain where the budget is measured in milliseconds rather than IQ, and the field has converged on hard numbers: humans switch turns in ~200ms, an agent feels off at 800ms, and users hang up at 1.5s, while the best measured cascaded voice-to-voice pipeline sits at 755ms and a typical cloud-API stack runs 1,100-1,300ms with LLM time-to-first-byte (500-650ms) as the dominant term. The dominant architectural answer is to shrink the model in the hot path and move control flow, state tracking, and answer selection into a state machine or harness — Haiku-class models with scaffolding are reported to hit ~900ms on questions that take an unscaffolded reasoning model several seconds — with heavier work handed off asynchronously. Turn taking is treated as an audio-engineering problem rather than an LLM problem: VAD alone cannot distinguish a finished thought from a breath, the best deployable turn-detection model (Smart Turn v3.2) gets only 58.9% recall, and production practice is to stack a turn model over a VAD silence timer so misses cost latency instead of correctness. Failure attribution has shifted off the model generally: Hippocratic reports that most apparent reasoning failures are transcription errors, and feeding conversation context and a constrained domain vocabulary into a decoder-only audio LLM cut medical WER by over 50%. Tail latency, not median, is the operative metric — one 4-second P95 response destroys a conversation and false interruptions measurably raise human-escalation rates — and long sessions degrade separately, with instruction following slipping after 15-20 turns. In high-stakes deployments (healthcare voice at 200M interactions and 200K clinical calls), the release process is simulation-plus-evidence rather than A/B tests or canaries, because a spoken utterance cannot be rolled back.

## Consensus

### Voice agents must hit a sub-second response budget anchored on human turn-taking (~200ms), with ~800ms as the point the experience degrades and ~1-1.5s as the point users disengage.

Support: **4** talk(s)

> "because 200 milliseconds is how fast humans switch turns with each other in a conversation. And the implications are pretty brutal because at 800 milliseconds, things start to feel off. While at 1.5 seconds, your user just hang up on you"
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [2:18](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=138s)

Supporting talks: [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)

### The model in the real-time speaking path should be the smallest and fastest one the latency budget allows; the thinking, control flow, and state belong in surrounding code, not in a frontier reasoning model.

Support: **4** talk(s)

> "Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)

Supporting talks: [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

### What breaks a voice agent usually is not the LLM — it is the audio pipeline, the transcription, or the interaction protocol around the model.

Support: **3** talk(s)

> "These are all audio engineering problems. They are not LLM problems because you can have the perfect model, perfect track but the experience still might feel broken if the turn taking is off."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [0:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=3s)

Supporting talks: [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)

### Silence is not a reliable end-of-turn signal, and barge-in handling is a separate engineering problem: VAD sees an identical signal for a breath, a thinking pause, a backchannel, and a completed sentence.

Support: **4** talk(s)

> "If someone is pausing for 300 milliseconds or 400 milliseconds, VAD is seeing the same exact thing. It has no idea like whether the person is catching up their breath or whether they've completely finished their thought."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [7:24](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=444s)

Supporting talks: [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)

### Tail latency (P95/P99) is the governing metric for voice, because a single slow turn destroys the conversation and cannot be averaged away by a good median.

Support: **3** talk(s)

> "But what matters more in voice than maybe anywhere else is that the P95 tail. Because GPT-4.1 was great at P50, but it spikes to 1.7 at P95."
>
> — [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [17:58](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1078s)

Supporting talks: [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)

## Disagreements

### When latency engineering buys you headroom, should you spend it on more intelligence or on doing less model work?

| Position A | Position B |
|---|---|
| Reinvest recovered latency into more intelligence: never bank the savings, run many specialist models in parallel (31 per conversation) with short-circuiting, treat output quality as a hard constraint and require every speed optimization to be lossless.<br>*[200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)* | Spend the headroom on removing model work: strip reasoning, state, and control flow out of the model entirely, then downgrade to a small model (Haiku 4.5 replacing Opus 4.7) because reasoning is a per-turn cost while scaffolding is paid once in code.<br>*[Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* |

*Why it matters: It determines whether your engineering budget goes into inference optimization and model redundancy or into harness code and state machines — and whether a small model is a compromise or the correct default.*

### Is fully conversational voice-in/voice-out achievable with today's stacks, or should the output modality change?

| Position A | Position B |
|---|---|
| Yes, with engineering: co-locating all models in one GPU cluster reaches ~500ms voice-to-voice, scaffolded small models start speaking in ~900ms, and clinical deployments already run two-way phone conversations at scale.<br>*[Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)* | No: true conversational voice-out needs 200ms or less, which nobody hits, so route the response to visuals and exploit the far more forgiving ~1-second visual envelope instead of waiting for novel architectures.<br>*[Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* |

*Why it matters: It decides whether you invest in TTS/turn-taking infrastructure and co-located serving, or design a fundamentally different product surface where speech is input-only.*

### Does voice input actually change how humans interact with AI, or is it just a faster keyboard?

| Position A | Position B |
|---|---|
| Dictation is the correct default input: ~200 words per minute, roughly 3x faster than typing, good enough that you should send the AI a rambling 15-minute voice memo and let it sort out the mess.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md)* | Speaking changes nothing structurally: the voice is transcribed into the same single-slot batch submission, the machine still only engages after the human packages a complete turn, and today's speech-to-speech models cannot even tell whether words were addressed to them.<br>*[The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)* |

*Why it matters: If dictation is sufficient, the work is throughput and transcription quality; if the protocol is the bottleneck, the work is building systems that model who is in the room, who holds the floor, and when to speak.*

## Practical Guidance

**Do:**

- Budget voice-to-voice end-to-end and measure P95, not P50; hold the LLM to sub-700ms time-to-first-token and expect STT+LLM to consume about two-thirds of the total budget
- Tune minimum-silence per domain rather than using a default: ~200ms for a sales agent, 1000-1200ms where users need thinking time
- Run a turn-detection model (Smart Turn v3.2, 8MB, BSD-2, pip-installable) with a VAD silence timer underneath as a safety net, so a missed endpoint costs latency instead of correctness
- Discriminate interruption types: stop for corrections, keep speaking through backchannels and background noise, since false interruptions raise human-escalation rates
- Fire inference every 1-2 seconds while the user is still speaking instead of blowing the budget waiting for a full second of silence
- Keep the first ~90% of the context identical request-to-request to exploit prefix caching (up to 90% cheaper and faster; 96%+ KV cache hit rate and 18x faster prefill in one production stack)
- Move step tracking and 'are we done' judgments into a harness or state machine — the model proposes, the harness validates, advances state, and decides what comes next
- Feed conversation context and a constrained domain vocabulary into the ASR (a finite medication list rather than an open one) — this cut medical word error rate by over 50%
- Prune context or reset the session after 15-20 turns, when instruction following starts to drift
- Validate the serving platform's latency, not just the model size — a small model on a non-latency-prioritized platform measured 5,000ms typical and 7,000ms P95
- For high-stakes voice, manufacture rare hazard cases in simulation with diverse personas (verbose vs. terse), grade with a validated LLM judge, and deliberately over-call hazards
- Size your test set to your error target: ~450 tests to be 99% sure of catching a 1% error rate, ~1,900 to see it ten times

**Avoid:**

- Fixing multi-step unreliability by prompting harder or adding more rules — when reliability approaches a coin flip, take the control flow out of the model instead
- Putting a reasoning frontier model in the real-time path: a model that thinks for a full second has already lost the room regardless of answer quality
- Relying on VAD alone for endpointing, or on an STT provider's built-in turn detection without accepting that you lose observability into why it fired
- Trusting public audio benchmarks recorded in quiet rooms, or a vendor's model-card score, as evidence your deployment will work
- A/B testing or canary-rolling voice agents on patients — a spoken utterance cannot be rolled back, and randomizing people into a worse variant is unethical and often illegal
- Assuming a single model is enough in a safety-critical conversation, and assuming synthetic data alone will get you to the required accuracy
- Validating only in demo conditions, which never surface the step-skipping and looping that real users trigger
- Treating 80-90% agentic accuracy as adequate for high-stakes voice: at 10,000 calls a day, even 1% error means 100 people get the wrong outcome

## Notable Outliers

- 58.9% recall is a perfectly deployable turn-detection number in production, because the VAD timer underneath means a miss costs only latency; the higher-recall 87.7% research result is useless since no code was released. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [10:32](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=632s))
- On the same harm rubric, the Polaris voice system scores 99.89% no-harm versus about 81% for human clinicians — not because humans are bad, but because AI systems don't get tired and it runs 30+ supervisor models. ([200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [17:50](https://www.youtube.com/watch?v=AN65uc645mE&t=1070s))
- Speech-to-speech models have no concept of who is speaking or whether the words were even meant for them — that is a protocol limitation, not a dumb model, and backchanneling noises are not the same as knowing who is in the room. ([The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [11:51](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=711s))
- The best measured voice-to-voice response for a cascaded pipeline is 755ms, roughly 4x slower than human turn taking, and the three levels of turn-taking sophistication are configuration choices — the Pipecat pipeline code is essentially identical across all of them. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [3:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=187s))
- Voice-to-function-calling is the key interaction pattern for IoT and edge devices because settings menus are unusable for many people, and a fine-tuned tiny model calls 10 functions at over 86% reliability from arbitrary text. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [15:29](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=929s))
- Energy-gap segmentation cannot slice speech into words because real speech often has no silence between words; even adding sonority-peak syllabification still required manual segment editing. ([While my guitar gently speaks](../talks/while-my-guitar-gently-speaks.md), [8:03](https://www.youtube.com/watch?v=E_Txocq-Lrw&t=483s))

## All Talks

- [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md)
- [Perception Agents](../talks/perception-agents.md)
- [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)
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
- [Jared Joselowitz](../speakers/jared-joselowitz.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Ted Johnson](../speakers/ted-johnson.md)
- [Todd Fisher](../speakers/todd-fisher.md)
- [Vivek Muppalla](../speakers/vivek-muppalla.md)

