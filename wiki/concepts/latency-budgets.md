---
title: "latency budgets"
type: "concept"
slug: "latency-budgets"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 14
---

# latency budgets

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **14** speaker(s)

**Definition:** Allocating an end-to-end response-time budget across model calls and system hops, including tail latency and time-to-first-token targets.

*Also referred to as: latency budgeting, tail latency, p95 latency, time to first token, latency optimization, time to first token latency, voice agent latency*

## State of Practice

The field has moved from treating latency as a performance metric to treating it as a hard product constraint that decides which experiences can exist at all. Practitioners now budget in explicit numbers rather than vibes: ~200ms is human turn-taking speed, ~950ms is the voice agent's speak-by deadline, ~1s is the forgiving envelope for visual output, ~4s is the outer limit of believability for chat, and 16ms is the frame budget for an on-device game agent. The primary instrumented metric has shifted from total wall-clock latency to time-to-first-token/first-chunk, and from P50 to P95/P99 — a single tail spike destroys a voice conversation or a search session in a way averages hide (GPT-4.1 at 1.7s P95, Claude 3 over 4s, GPT-5 mini at 7s P95). The dominant consumption of the budget is contested but well-measured: LLM TTFB is 500–650ms in a typical cloud voice pipeline (STT+LLM ≈ two-thirds of the total), while at 1,000 tok/s inference the network overtakes inference entirely, and a 741-tool catalog costs 127k tokens of prompt before the model does anything. The consistent conclusion is that budget is bought back architecturally — smaller models with code-based scaffolding, decoupled agent loops and tool containers, just-in-time tool routing, stable-prefix caching, co-location, and ground-up redesign — not by incremental tuning of an existing pipeline.

## Consensus

### Latency budgets must be designed against tail percentiles (P95/P99, sometimes P999), not the median, because a single slow response destroys the interaction and cannot be averaged away.

Support: **5** talk(s)

> "With 14 million users, even 1% is a not small number. It is 140,000 of people hitting slow search at scale. P99 is much more important than P50"
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [4:17](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=257s)

Supporting talks: [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### Time to first token / first chunk, not total response time, is the metric the budget should be allocated and optimized against.

Support: **4** talk(s)

> "you stop chasing the total latency, which we have done for over a decade. You start chasing time to first chunk."
>
> — [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [9:40](https://www.youtube.com/watch?v=maTp79FD9gI&t=580s)

Supporting talks: [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)

### For latency-bound surfaces, pick the smallest/fastest model the budget permits and buy back quality with surrounding engineering, rather than reaching for a frontier reasoning model.

Support: **4** talk(s)

> "Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)

Supporting talks: [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)

### Latency is a product constraint that determines which experiences are buildable at all, not a performance number to tune after the fact.

Support: **4** talk(s)

> "in AI era speed is not just performance. speed actually defines what product can exist"
>
> — [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [11:16](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=676s)

Supporting talks: [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md)

### Context bloat is a latency tax, not just a cost line: unbounded tool/skill schemas and stale harness scaffolding push time to first token up, so context must be explicitly budgeted and loaded just-in-time.

Support: **3** talk(s)

> "So, say for example, if you have 500 tools in your agent, the fat agent path can push first token latency past 5 seconds."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [6:38](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=398s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

## Disagreements

### Where does the latency budget actually get spent — in model inference, or in the system around the model?

| Position A | Position B |
|---|---|
| The model call is the dominant cost; shrink or remove model work (smaller models, scaffolding in code instead of reasoning, on-device inference, fewer thinking tokens). Voice measures LLM TTFB at 500–650ms and STT+LLM at two-thirds of the total budget.<br>*[Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* | Inference is no longer the bottleneck; the surrounding system is. Fix transport, container startup, harness overhead, and data-plane architecture — at 1,000 tok/s the network dominates, decoupling the agent loop from the tool container alone bought 60% P50 / 90%+ P95 TTFT, and a 4s scrape pipeline needed ground-up redesign to reach 550ms.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)* |

*Why it matters: It decides whether a team spends its next quarter on model selection and eval harnesses or on transport, sandboxing, and storage architecture — and the answer flips as inference speeds rise, since a 1,000 tok/s serving tier makes model-side optimization nearly irrelevant.*

### Is the user's latency tolerance a hard perceptual ceiling, or is it elastic if the interface streams and shows progress?

| Position A | Position B |
|---|---|
| Hard ceiling with measured thresholds: 200ms is human turn-taking, 800ms already feels off, users hang up at 1.5s, ~950ms is the speak-by deadline, and 4s is the outer limit of believability. Exceeding it means the experience is broken regardless of output quality.<br>*[Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Frontier results, on device](../talks/frontier-results-on-device.md)* | The ceiling is elastic when the rendering layer streams typed chunks and exposes what the agent is doing — 3–4 seconds is bearable and even 10 seconds is acceptable if the user can see progress and trust the result; stop optimizing total latency and optimize the first chunk instead.<br>*[Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)* |

*Why it matters: If the ceiling is hard, model choice and infrastructure are forced (small models, co-location, on-device); if it is elastic, the same budget buys a much more capable model and the investment moves to the streaming/rendering layer. The split tracks modality — audio has no place to show progress, screens do — so teams should decide which regime their surface is in before setting a number.*

### Should latency be bought by moving inference onto the user's device, or by concentrating and co-locating it in the datacenter?

| Position A | Position B |
|---|---|
| Push inference to the edge: cloud round-trips are the latency, small local models are sufficient for agentic loads at ~25% of the energy, total inference cost drops to zero for the operator, and the future is billions of per-device models.<br>*[Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [Frontier results, on device](../talks/frontier-results-on-device.md)* | The achievable floor comes from centralizing: co-locating STT, LLM, and TTS in one GPU cluster gets voice-to-voice to ~500ms, and serving-side redesign (architecture, not hardware) took a 4s pipeline to 550ms at 6B daily requests.<br>*[Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)* |

*Why it matters: The two paths have opposite failure modes — device inference shifts cost to the user's battery, caps capability at what an NPU can run, and makes capability changes require a 1–2GB app update, while co-location requires owning GPU infrastructure. Picking wrong locks a product into the wrong cost curve for years.*

## Practical Guidance

**Do:**

- Instrument time to first token / first chunk as the primary UX metric and stream typed chunks rather than showing a spinner.
- Set budgets at P95/P99 rather than P50; for object-storage-backed systems assume ~200ms P99 per 256–512KB read and design to minimize round trips.
- Hold the LLM to a sub-700ms time-to-first-byte target in voice pipelines, against a ~950ms total speak-by deadline.
- Cap tool/skill descriptions as an explicit fraction of the context window (Codex uses 2%) and mark tools as deferred so they load via tool search.
- Route tools just-in-time with K≈5 retrieved schemas once you pass ~50 tools; below 20 tools, static loading is fine.
- Decouple the agent loop from tool-execution containers so first-token reasoning doesn't block on sandbox startup.
- Keep the first ~90% of the context prefix identical across requests to get prefix caching (up to 90% cheaper and faster).
- Measure the latency cost of prompt techniques, not just their accuracy: few-shot added 200ms while chain-of-thought added 600ms for the same length-compliance gain.
- Run your own latency evals per candidate model instead of trusting peer recommendations — the socially recommended model came in around 8 seconds.
- Fix structural and length failures with deterministic post-processing in the harness rather than escalating to a larger model.
- Use a persistent WebSocket that transmits only changed items instead of SSE over HTTP once inference is fast enough that the network dominates.
- Pair a turn-detection model with a VAD silence timer as a safety net, and tune minimum-silence to the domain (~200ms for sales, 1000–1200ms where users need thinking time).
- For on-device agents, fit planning inside the 16ms frame at 60Hz and penalize time-budget overruns harder than space overruns.
- Write concrete, verifiable goal prompts rather than essays — the loop only terminates when the model can detect the goal is met.

**Avoid:**

- Incrementally optimizing a pipeline when the target is an order of magnitude away — going from a 4s baseline to sub-second is a redesign, not an optimization.
- Loading the entire tool catalog on every request: 741 tools is ~127k tokens per call and drops tool-selection accuracy to 13.6%.
- Using a frontier reasoning model in the interactive voice path — the reasoning seconds cost more than the answer quality gains.
- Assuming a small model is a fast model; GPT-5 mini showed 5,000ms typical and 7,000ms P95 without a latency-prioritizing serving platform.
- Leaving harness workarounds in place after the model outgrows them — they become pure overhead, adding latency and invalidating cache.
- Judging infrastructure by vendor benchmarks instead of first-principles napkin math; benchmarks routinely hide things like an unnoticed distributed query inflating P99.
- Throwing hardware at an architectural scaling wall — 2,000 extra servers did not close a 10k→60k RPS gap.
- Waiting for a full second of silence before firing inference; that alone blows the budget.
- Traditional loading spinners for AI features — users have left the forgiving phase and expect to see what's happening.
- Letting long conversations run unbounded: instruction following degrades after roughly 15–20 turns, requiring pruning or session resets.

## Notable Outliers

- At ~1,000 tokens/sec inference, the network — not inference — becomes the dominant bottleneck in the agent loop, which is why the Responses API moved to a persistent WebSocket. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s))
- A 10-second wait is acceptable if the user can see what the agent is doing and trust the final output — transparency, not speed, is what buys tolerance. ([Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [11:15](https://www.youtube.com/watch?v=maTp79FD9gI&t=675s))
- An on-device game agent must complete planning within a 16ms frame at 60Hz, and time-budget violations should be penalized harder than space violations because they produce visible jank. ([Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [8:44](https://www.youtube.com/watch?v=418t26CVz-w&t=524s))
- 58.9% recall turn detection is acceptable to ship because a VAD timer runs underneath as a safety net — misses cost latency, not correctness. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [10:32](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=632s))
- Chain-of-thought bought length compliance at 600ms while few-shot examples bought more improvement for only 200ms — prompt technique is a line item in the latency budget. ([Frontier results, on device](../talks/frontier-results-on-device.md), [23:21](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1401s))
- Decoupling the agent loop from the tool-execution container yielded 60% faster TTFT at P50 and over 90% improvement at P95 — a pure architecture win with no model change. ([Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [23:55](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1435s))

## All Talks

- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)
- [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)
- [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md)
- [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)
- [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)
- [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Allen Pike](../speakers/allen-pike.md)
- [Ankush Rastogi](../speakers/ankush-rastogi.md)
- [Arek Borucki](../speakers/arek-borucki.md)
- [Bala Ramdoss](../speakers/bala-ramdoss.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Joanne Song](../speakers/joanne-song.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Shafik Quoraishee](../speakers/shafik-quoraishee.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)

