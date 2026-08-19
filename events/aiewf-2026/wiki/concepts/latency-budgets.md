---
title: "latency budgets"
type: "concept"
slug: "latency-budgets"
tier: "supporting"
maturity: "consolidating"
talk_count: 15
speaker_count: 17
---

# latency budgets

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **15** talk(s) by **17** speaker(s)

**Definition:** Allocating an end-to-end response-time budget across model calls and system hops, including tail latency and time-to-first-token targets.

*Also referred to as: latency budgeting, tail latency, p95 latency, time to first token, latency optimization, time to first token latency, voice agent latency*

## State of Practice

Latency has been promoted from a performance metric to a product constraint: speakers repeatedly framed it as determining which products can exist at all, and they now quote hard human thresholds rather than vague targets — ~200ms for human conversational turn-taking, ~950ms before a voice agent feels dead, ~1s for a visual response, ~4s as the outer limit of believability in chat, and 16ms per frame for an on-device game agent. The budget is decomposed and attributed: a cloud-API voice pipeline totals ~1,100–1,300ms with LLM time-to-first-byte at 500–650ms as the dominant term, STT+LLM eating two-thirds of the budget, and co-locating every model in one GPU cluster is the demonstrated floor at ~500ms voice-to-voice. Everyone who measured argues from the tail rather than the median — P95 for voice, P99 for user-facing search, P99/P999 for anything issuing many S3 round trips — because a single spike is not averageable in an interactive session. Time to first token/first chunk has largely displaced total latency as the headline metric, and the levers people actually pulled were architectural: decoupling the agent loop from the tool-execution container (60% faster TTFT at P50, >90% at P95), retrieving tool schemas just-in-time instead of shipping a 127k-token catalog, prefix caching, and picking the smallest model the budget allows while moving control flow into code. The open arguments are about where the budget is really spent — several teams report inference is no longer the bottleneck at all, with the network, container startup, or the rendering layer dominating — and whether you should engineer latency down or redesign the interaction so users tolerate more of it.

## Consensus

### Latency is a product constraint that decides what can be built, not a performance metric to optimize later; teams argue from concrete human-perception thresholds (200ms turn-taking, ~1s visual response, ~4s believability, 16ms frame).

Support: **6** talk(s)

> "in AI era speed is not just performance. speed actually defines what product can exist"
>
> — [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [11:16](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=676s)

Supporting talks: [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md)

### Design and report against the tail (P95/P99/P999), not the median, because one slow response in an interactive session cannot be averaged away.

Support: **4** talk(s)

> "With 14 million users, even 1% is a not small number. It is 140,000 of people hitting slow search at scale. P99 is much more important than P50"
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [4:17](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=257s)

Supporting talks: [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)

### Time to first token / first chunk, not total response time, is the metric to budget against for AI features.

Support: **4** talk(s)

> "you stop chasing the total latency, which we have done for over a decade. You start chasing time to first chunk."
>
> — [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [9:40](https://www.youtube.com/watch?v=maTp79FD9gI&t=580s)

Supporting talks: [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)

### Select the fastest/smallest model the latency budget permits and buy back quality with scaffolding, evals, and post-processing — frontier reasoning models are the wrong default on an interactive path.

Support: **4** talk(s)

> "Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)

Supporting talks: [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)

### Prompt payload size is a latency line item, not only a cost line item: loading everything up front (tool schemas, skill descriptions, oversized context) directly inflates time to first token.

Support: **3** talk(s)

> "So, say for example, if you have 500 tools in your agent, the fat agent path can push first token latency past 5 seconds."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [6:38](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=398s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### Order-of-magnitude latency wins come from architectural redesign — decoupling, co-location, ground-up rebuilds — not from incremental tuning or adding hardware to the existing design.

Support: **4** talk(s)

> "when your baseline is at 4 seconds, we are not talking about optimization. We are talking about redesign."
>
> — [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [8:42](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=522s)

Supporting talks: [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)

## Disagreements

### When the model cannot meet the interaction's latency budget, should you engineer the pipeline down to the budget or change the interaction so users tolerate a longer wait?

| Position A | Position B |
|---|---|
| Drive the number down: co-locate STT/LLM/TTS in one GPU cluster for ~500ms voice-to-voice, hold the LLM to sub-700ms TTFT, distribute GPUs regionally for sub-100ms interactive video, rebuild the pipeline from scratch to go from 4s to 550ms.<br>*[Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)* | Move to a more forgiving envelope instead: swap voice-out for visuals-out to trade a 200ms budget for a ~1s one, and use streaming first chunks plus a visible 'thinking' state so a 10-second total wait is acceptable.<br>*[Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)* |

*Why it matters: One path spends the engineering budget on inference infrastructure and model serving; the other spends it on the rendering and UX layer and accepts today's model latencies. Choosing wrong means either building a GPU footprint you did not need or shipping an interaction whose budget you can never meet.*

### Is model inference still the dominant term in the end-to-end latency budget?

| Position A | Position B |
|---|---|
| Yes — LLM time-to-first-byte at 500–650ms is the dominant component of a voice pipeline, STT+LLM eat two-thirds of the budget, and model choice alone is the difference between an 8-second and a usable response.<br>*[Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* | No — at ~1,000 tokens/sec the network, not inference, is the bottleneck; container startup blocks first-token reasoning; and the delivery/rendering layer between model output and screen is where the product actually stalls.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)* |

*Why it matters: It determines whether you profile and optimize the model call (smaller model, faster provider, fewer tokens) or the transport and orchestration around it (WebSockets over SSE, pre-warmed sandboxes, streaming render). Optimizing the wrong term yields nothing at P95.*

### Should the first tokens of the prompt be shrunk per request, or held identical across requests?

| Position A | Position B |
|---|---|
| Shrink it: retrieve only the ~3–5 relevant tool schemas just-in-time (127k tokens down to ~1,000, ~99% reduction) and mark tools as deferred so they load through tool search rather than into the context window.<br>*[The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* | Stabilize it: keep the first ~90% of the context window byte-identical from request to request so prefix caching yields up to 90% cheaper and faster inference, and treat that as the architecture most LLM apps are converging on.<br>*[Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* |

*Why it matters: Per-request tool retrieval mutates the prompt prefix, which is exactly what prefix caching requires to stay stable — so the two techniques compete for the same region of the context window, and a team that adopts both without care pays the cache miss on every turn.*

### Should latency-critical inference be moved onto the user's device or onto latency-optimized remote infrastructure?

| Position A | Position B |
|---|---|
| On-device: cloud round trips make mobile gameplay AI expensive and slow, an SLM uses ~25% of the energy, inference cost shifts to the consumer, and the future is billions of small per-device models.<br>*[Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [Frontier results, on device](../talks/frontier-results-on-device.md)* | Remote but engineered: real-time experiences need co-located model clusters and globally distributed GPUs that route a user in India or Japan to nearby capacity, and the choice of a latency-prioritizing inference platform matters more than model size.<br>*[The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* |

*Why it matters: Local execution eliminates the round trip but caps model capability, drains battery, and — for distilled models — forces a 1–2 GB redownload on every capability change; remote execution keeps capability and shipping velocity but makes geography and provider queueing part of your budget.*

## Practical Guidance

**Do:**

- Instrument and report time to first token / first chunk as the primary latency metric, and stream partial output rather than showing a spinner
- Set SLOs at P95 (voice) or P99/P999 (search, S3-backed systems), not P50 — GPT-4.1 looked fine at P50 and spiked to 1.7s at P95
- Hold the LLM to a sub-700ms time-to-first-token target for voice, and budget the whole cascaded pipeline against ~1,100–1,300ms of typical cloud-API cost
- Extract control flow, state tracking, and answer selection into a state machine so a Haiku-class model can answer in ~900ms instead of a reasoning model taking several seconds
- Decouple the agent loop from tool execution so container setup does not block first-token reasoning (measured: 60% faster TTFT at P50, >90% at P95)
- Above ~50 tools, retrieve schemas just-in-time via embedding search; start at K=5 and test K=3/5/10, picking the smallest K that hits your accuracy target
- Cap always-resident context blocks as a fraction of the window (Codex caps the skills list at 2%) and mark the rest as deferred/lazily discoverable
- Tune minimum-silence per domain — ~200ms for a sales agent, 1000–1200ms where users need thinking time — and run a VAD timer under a turn-detection model so misses cost latency rather than correctness
- Fire inference every 1–2 seconds while the user is still speaking instead of waiting for a full second of silence
- Keep the leading ~90% of the context prefix identical across requests to exploit prefix caching
- Benchmark candidate models on your own golden set rather than peer recommendation — the socially recommended model came in around 8 seconds
- Fix structural and length failures with deterministic post-processing in the harness; chain-of-thought bought compliance at +600ms while few-shot cost only +200ms
- Route interactive video users to GPUs in their own region; sub-100ms everywhere is a capacity-placement problem, not a model problem
- Budget object-storage designs against ~200ms P99 per 256–512KB read and minimize round trips, since tree traversal compounds them
- Keep on-device agent planning inside the 16ms frame at 60Hz, or accept visible jank

**Avoid:**

- Loading the full tool catalog on every request — 741 tools is ~127k tokens per call and pushes TTFT past 5 seconds at ~500 tools
- Putting a reasoning frontier model on the interactive path; a model that thinks for a full second has already lost a voice conversation
- Chasing average or total latency as the headline number, or using a traditional loading spinner as the wait affordance
- Assuming batch inference infrastructure transfers to real-time serving — streaming, live-session memory, and global compute are new requirements
- Trying to buy your way out of a scaling wall with hardware; 2,000 extra servers did not close a 10k→60k RPS gap without an architecture change
- Leaving harness workarounds for old model limitations in place after a model upgrade — they become pure overhead, adding latency and discarding the cache incorrectly
- Trusting third-party benchmarks over first-principles napkin math, since a benchmark can hide something like a distributed query inflating P99
- Relying on VAD silence thresholds alone: a 300–400ms pause looks identical whether the speaker finished, is thinking, or is taking a breath — and false interruptions measurably raise escalation to human agents
- Shipping distilled on-device models for mobile when every capability change means retraining and pushing a 1–2 GB download over users' data plans
- Sizing a real-time budget by parameter count alone — GPT-5 mini is small and cheap yet showed 5,000ms typical and 7,000ms P95 in practice

## Notable Outliers

- The best measured voice-to-voice response time for a cascaded pipeline is 755ms — still roughly 4x slower than the ~200ms at which humans switch conversational turns. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [3:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=187s))
- At 1,000 tokens/sec inference (GPT-5.3 Codex Spark on Cerebras), inference stopped being the bottleneck and the network became it — motivating a persistent WebSocket that transmits only changed items instead of SSE over HTTP. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s))
- Four seconds is the upper limit of believability for users in LLM chat, and many frontier-model calls exceed it. ([Frontier results, on device](../talks/frontier-results-on-device.md), [1:28](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=88s))
- An on-device game agent must produce a plan inside a 16ms frame at 60Hz, and time overruns should be penalized harder than space overruns because they break the user experience directly. ([Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [8:44](https://www.youtube.com/watch?v=418t26CVz-w&t=524s))
- Real-time generative video is not a quality compromise — the real-time sample had better motion than the batch one at about 1/100th the cost, ending the $10-per-minute 'slot machine' workflow. ([Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [1:46](https://www.youtube.com/watch?v=Xln-On3syJk&t=106s))
- A search pipeline was taken from a 4-second average to 550ms while scaling from 400 million to nearly 6 billion daily requests — and hitting 60k RPS immediately produced a 150k RPS target. ([How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [11:16](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=676s))
- Users will accept a 10-second wait if the agent shows what it is doing — the tolerable-wait question is about legibility, not duration. ([Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [11:15](https://www.youtube.com/watch?v=maTp79FD9gI&t=675s))

## All Talks

- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)
- [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)
- [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)
- [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md)
- [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)
- [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md)
- [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)
- [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)
- [While my guitar gently speaks](../talks/while-my-guitar-gently-speaks.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Ahmed Ahres](../speakers/ahmed-ahres.md)
- [Allen Pike](../speakers/allen-pike.md)
- [Ankush Rastogi](../speakers/ankush-rastogi.md)
- [Arek Borucki](../speakers/arek-borucki.md)
- [Bala Ramdoss](../speakers/bala-ramdoss.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Joanne Song](../speakers/joanne-song.md)
- [Keegan McCallum](../speakers/keegan-mccallum.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Shafik Quoraishee](../speakers/shafik-quoraishee.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Todd Fisher](../speakers/todd-fisher.md)

