---
title: "Voice Agents That Handle Interrupts"
type: "talk"
slug: "voice-agents-that-handle-interrupts"
track: "Generative Media"
org: "AWS"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "hMlLw1LeIK8"
duration_sec: 1976
word_count: 4761
speakers: ["Lina Colucci"]
---

# Voice Agents That Handle Interrupts

*Program title: Voice agents with Realtime Video*

**Speakers:** [Lina Colucci](../speakers/lina-colucci.md)

**Org:** AWS

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 32m 56s

[Watch on YouTube](https://www.youtube.com/watch?v=hMlLw1LeIK8)

## Summary

Two AWS solutions architects argue that voice agent quality is governed by turn-taking — an audio engineering problem, not an LLM problem — and that identical models with identical prompts produce wildly different user experiences depending on how fast the pipeline detects that a user has started or stopped speaking. They frame the challenge around the 200ms human turn-taking baseline, break down where a cascaded STT→LLM→TTS pipeline spends its 1,100–1,300ms budget, and lay out three escalating approaches: local Silero VAD silence detection, STT-provider-native endpointing (Cartesia, Deepgram), and local VAD plus an open Smart Turn model. They report concrete numbers throughout — Smart Turn v3.2 at 58.9% recall / 68.4% precision, Cartesia ~300ms and Deepgram Nova 3 ~250ms P50 endpointing, LLM time-to-first-token benchmarks with P95 tails as the real risk. The second half is a live Pipecat demo running all three configurations against the same travel-assistant agent, showing that the pipeline code is nearly identical and only the turn-detection configuration changes. Worth watching if you are building production voice agents and need a concrete decision framework plus current latency numbers; skip if you want model-level or prompting advice.

## Key Points

- Turn taking is an audio pipeline problem rather than a model problem — the same LLM and prompt can feel broken or natural depending purely on how fast interruptions are detected and propagated.
- Humans switch turns in about 200ms; at 800ms conversation starts to feel off and at 1.5s users hang up, and the best published measured voice-to-voice time for a cascaded pipeline is still 755ms.
- Silero VAD is a 300K-parameter, 2MB model whose single minimum-silence-milliseconds parameter effectively defines the entire level-one user experience, with the right value depending entirely on domain (≈200ms for sales, 1000–1200ms where users need thinking time).
- VAD fundamentally cannot distinguish a completed sentence, an incomplete thought, a thinking pause, and a backchannel acknowledgement — the silence signal looks identical in all four cases.
- Level two hands turn detection to the STT provider (Cartesia ~300ms P50, Deepgram Nova 3 ~250ms P50), which is smarter because it sees linguistic context, but the decision happens on someone else's server with no explainability when it misfires.
- Level three keeps local VAD as a safety-net timer and layers Smart Turn v3.2 (58.9% recall, 68.4% precision, 8MB, BSD-2, pip-installable) on top, so confident predictions are fast and unconfident ones fall back to the timer.
- In a standard cloud-API setup the total budget is roughly 1,100–1,300ms, with LLM time-to-first-byte at 500–650ms as the dominant bottleneck; STT and LLM together consume about two-thirds of the budget and are the only meaningful levers.
- P95 latency matters more than P50 in voice because a single slow response destroys conversational flow — GPT-4.1 was 536ms P50 but spiked to 1.7s at P95, and Claude 3 exceeded 4 seconds.
- Not all interruptions should stop the agent: corrections warrant an immediate stop, filler and background noise should not, and owning the classification at level three is what makes that distinction possible.
- False interruptions have a measurable production cost — cutting users off incorrectly raises the rate at which they escalate to a human.

## Notable Quotes

> "These are all audio engineering problems. They are not LLM problems because you can have the perfect model, perfect track but the experience still might feel broken if the turn taking is off."
>
> — [0:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=3s) &middot; *states the talk's central thesis in one line*

> "Both the scenarios, the LLM was identical. It was the same model. It was the same prompt, but the difference in the user experience is so different."
>
> — [1:34](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=94s) &middot; *isolates the variable the whole talk is about*

> "because 200 milliseconds is how fast humans switch turns with each other in a conversation. And the implications are pretty brutal because at 800 milliseconds, things start to feel off. While at 1.5 seconds, your user just hang up on you"
>
> — [2:18](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=138s) &middot; *the quantitative constraint that frames every later tradeoff*

> "But even there, best measured response time was 755 milliseconds. So, that's like almost 4x slower than how humans naturally take turns when talking."
>
> — [3:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=187s) &middot; *reports the current state-of-the-art number and the size of the gap*

> "So, coming to Silero VAD, it's a small 300,000 parameter model. It takes in like a short term Fourier transform."
>
> — [5:13](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=313s) &middot; *concrete spec for the baseline component*

> "And the one parameter that minimum silence millisecond is basically the entire user experience of level one. If you keep it very low, the agent is going to be snapping like it will cut people off while they're still, you know, thinking."
>
> — [6:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=361s) &middot; *names the single tuning knob that dominates level-one behavior*

> "If someone is pausing for 300 milliseconds or 400 milliseconds, VAD is seeing the same exact thing. It has no idea like whether the person is catching up their breath or whether they've completely finished their thought."
>
> — [7:24](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=444s) &middot; *the precise failure mode that motivates levels two and three*

> "And their P50 latency for Cartesiant is about 300, and it's about 250 for Deepgram Nova 3."
>
> — [9:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=541s) &middot; *vendor-level endpointing latency numbers*

> "However, the trade-off is with the transparency. Because when it is working, it works great. But when it misfires, or when it cuts someone off at the wrong moment, then you like have no way to figure out"
>
> — [9:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=541s) &middot; *names the explicit tradeoff of outsourcing turn detection*

> "And it has about 58.9% recall and 68.4 percent precision. So, what this means is that about six out of 10 time when someone finishes a sentence, Smart Turn will be able to catch it quickly."
>
> — [9:43](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=583s) &middot; *honest accuracy reporting for the recommended approach*

> "There, they had reported a higher recall at 87.7%, but they haven't released the code, so you really cannot deploy it."
>
> — [10:32](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=632s) &middot; *distinguishes published SOTA from deployable SOTA*

> "Smart Turn is BSD-2 licensed, and it's a 8-MB small model. You can pip install it today as well."
>
> — [11:18](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=678s) &middot; *the practical adoption cost of level three*

> "think about a normal conversation when someone says, "Yeah." Like, if they send an acknowledgement while you're speaking, you don't stop, right?"
>
> — [12:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=721s) &middot; *grounds the backchannel-vs-interruption distinction*

> "So, today most of these systems stop every time, but this is a piece that's improving."
>
> — [12:43](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=763s) &middot; *characterizes the current state of interruption classification*

> "LLM time to first byte, and this is generally the dominant bottleneck because in a typical API setup, you're looking at 500 to 650 ms depending on what model you're calling and from which cloud provider, which region."
>
> — [15:13](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=913s) &middot; *identifies the largest single cost in the latency budget*

> "Now, the Quindos team had demonstrated about 500 ms total voice-to-voice by co-locating all models in the same GPU cluster."
>
> — [16:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=961s) &middot; *the infrastructure-bound floor for total latency*

> "And the key insight to note here is that the STT, LLM, together eat about 2/3 of the is latency budget."
>
> — [16:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=961s) &middot; *tells engineers where optimization effort actually pays*

> "But what matters more in voice than maybe anywhere else is that the P95 tail. Because GPT-4.1 was great at P50, but it spikes to 1.7 at P95."
>
> — [17:58](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1078s) &middot; *argues against benchmarking voice agents on median latency*

> "And it was even worse for Claude 3 that it hit over 4 seconds and because in a conversation you cannot average this out because one slow response and your entire flow is gone."
>
> — [19:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1147s) &middot; *concrete tail-latency data point with the reasoning for why it's fatal*

> "which is the multi-turn trip because after 15 or 20 turn, sometime model starts ignoring parts of the system prompt. They might get to verbose, they go off spirit."
>
> — [19:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1147s) &middot; *raises instruction-following degradation as an underrated voice failure*

> "Because when agents cut people off incorrectly, then users are more likely to request for a human in the loop uh support."
>
> — [20:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1203s) &middot; *ties turn-detection errors to a business metric*

> "And on infrastructure running all of this in production is also hard because five systems that all scale differently and can also fail differently."
>
> — [21:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1263s) &middot; *names the operational cost of the cascaded architecture*

> "So, definitely this is just a a quick demo, but in practice, you would probably combine both the turn detection model and the silence detection."
>
> — [29:12](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1752s) &middot; *the practical recommendation the demo builds toward*

## Positions

- Turn taking is an audio engineering problem, not an LLM problem — a perfect model with a bad audio pipeline still produces a broken experience. ([0:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=3s), confidence: stated)
- Humans switch conversational turns in about 200ms; agent response feels off at 800ms and users abandon at 1.5 seconds. ([2:18](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=138s), confidence: stated)
- 755ms is the best measured voice-to-voice response time for a cascaded pipeline, roughly 4x slower than human turn taking. ([3:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=187s), confidence: stated)
- There is no universally correct minimum-silence threshold; the right value depends on domain, around 200ms for a sales agent and 1000-1200ms where users need thinking time. ([6:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=361s), confidence: stated)
- VAD alone cannot distinguish a completed sentence, an incomplete thought, a thinking pause, and a backchannel acknowledgement because the silence signal is identical. ([8:09](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=489s), confidence: stated)
- STT-provider turn detection makes better decisions than VAD because it uses full audio plus linguistic context, but costs you observability into why it fired. ([9:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=541s), confidence: stated)
- Smart Turn v3.2's 58.9% recall is acceptable in production because a VAD timer runs underneath as a safety net, so misses only cost latency, not correctness. ([10:32](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=632s), confidence: stated)
- Smart Turn v3.2 at 58.9% recall is the best deployable turn detection available today, since higher-recall research results like Meta's 87.7% have no released code. ([20:03](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1203s), confidence: stated)
- A standard cloud-API voice pipeline totals roughly 1,100-1,300ms, with LLM time to first byte at 500-650ms as the dominant component. ([15:13](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=913s), confidence: stated)
- Co-locating all models in one GPU cluster gets total voice-to-voice down to about 500ms, making that the achievable floor for teams willing to invest in infrastructure. ([16:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=961s), confidence: stated)
- STT and LLM together consume about two-thirds of the latency budget and are therefore the only two meaningful levers for improving it. ([16:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=961s), confidence: stated)
- P95 latency matters more than P50 for voice agents because a single slow response destroys the conversation and cannot be averaged away. ([19:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1147s), confidence: stated)
- LLMs should be held to a sub-700ms time-to-first-token target for voice applications. ([16:50](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1010s), confidence: stated)
- Instruction following degrades after roughly 15-20 turns, requiring context pruning or session resets in long voice conversations. ([19:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1147s), confidence: stated)
- False interruptions measurably increase escalation rates to human agents. ([19:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1147s), confidence: stated)
- Agents should not stop for every detected interruption — corrections warrant stopping while backchannels and background noise do not. ([12:01](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=721s), confidence: stated)
- The three levels are configuration choices, not architectural ones — the Pipecat pipeline code is essentially identical across all three. ([13:39](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=819s), confidence: stated)
- Production systems should combine a turn detection model with silence detection rather than relying on either alone. ([29:12](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1752s), confidence: stated)
- Owning the turn detection stack locally is worth it when you need compliance control or want to fine-tune on your own data. ([21:57](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1317s), confidence: stated)

## Concepts

- [context rot](../concepts/context-rot.md)
- [latency budgets](../concepts/latency-budgets.md)
- [voice agents](../concepts/voice-agents.md)

