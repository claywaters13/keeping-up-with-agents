---
title: "latency budgets"
type: "concept"
slug: "latency-budgets"
tier: "supporting"
maturity: "consolidating"
talk_count: 17
speaker_count: 20
---

# latency budgets

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **17** talk(s) by **20** speaker(s)

**Definition:** Allocating an end-to-end response-time budget across model calls and system hops, including tail latency and time-to-first-token targets.

*Also referred to as: latency budgeting, tail latency, p95 latency, time to first token, latency optimization, time to first token latency, voice agent latency*

## State of Practice

Latency has stopped being a performance metric and become a product constraint: speakers repeatedly derived their budget from a perceptual threshold (200ms human turn-taking, ~950ms before a voice agent feels dead, ~1s for a visual response, 4s as the outer limit of believability in chat) and then worked backwards to an architecture. The unit of budgeting is the tail, not the mean — P95 for voice, P99 for search, P999 for systems layered on S3 where one logical operation fans out into many ~200ms object reads. Concrete decompositions are now public: a cloud-API voice pipeline runs ~1,100–1,300ms with LLM time-to-first-byte at 500–650ms as the dominant term, and co-locating every model in one GPU cluster takes voice-to-voice to ~500ms. The dominant tactics are subtractive rather than additive — strip reasoning out of the model into a state machine, retrieve 3–5 tool schemas instead of shipping 127k tokens of catalog, decouple the agent loop from container startup (60% faster TTFT at P50, >90% at P95), cache a stable prefix, and short-circuit specialists that decide they have nothing to say. What is still argued is whether the budget is spent on intelligence or bought back from it, and whether time-to-first-chunk plus a legible 'thinking' UI can substitute for actually being fast.

## Consensus

### Budget against the tail (P95/P99, sometimes P999), not the median — a single slow response destroys an interaction and cannot be averaged away.

Support: **6** talk(s)

> "With 14 million users, even 1% is a not small number. It is 140,000 of people hitting slow search at scale. P99 is much more important than P50"
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [4:17](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=257s)

Supporting talks: [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### The latency budget is set by a human perceptual threshold, and it determines which products are buildable at all rather than merely how good an existing product feels.

Support: **6** talk(s)

> "in AI era speed is not just performance. speed actually defines what product can exist"
>
> — [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [11:16](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=676s)

Supporting talks: [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)

### For real-time surfaces, select the fastest model that clears your quality bar and move control flow, state, and reasoning into code — model reasoning is a per-turn cost, scaffolding is paid once.

Support: **4** talk(s)

> "Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)

Supporting talks: [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)

### Everything loaded into context is charged to time-to-first-token, so the per-request working set must stay small even as the catalog of tools, skills, and history grows.

Support: **4** talk(s)

> "So, say for example, if you have 500 tools in your agent, the fat agent path can push first token latency past 5 seconds."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [6:38](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=398s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)

### Aggressive budgets are met by architectural change — removing round trips, decoupling blocking setup from first-token reasoning, co-locating or geo-distributing compute — not by incremental tuning or adding hardware.

Support: **5** talk(s)

> "when your baseline is at 4 seconds, we are not talking about optimization. We are talking about redesign."
>
> — [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [8:42](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=522s)

Supporting talks: [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)

### Cache behavior sits on the critical path of the budget: a stable context prefix buys large latency and cost wins, and anything that silently invalidates the cache is a latency regression.

Support: **3** talk(s)

> "if the beginning of the context you send to the model is the same each time, then you can get up to 90% cheaper, faster inference um depending on the conditions."
>
> — [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [11:22](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=682s)

Supporting talks: [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

## Disagreements

### When latency and intelligence conflict, which one is the hard constraint?

| Position A | Position B |
|---|---|
| Latency is the binding constraint and intelligence is what gets cut to fit: take reasoning out of the model, pick the smallest model that is good enough (Haiku-class, Llama 3.2 3B, on-device SLMs), and accept the quality delta because a frontier model that thinks for a second has already lost the user.<br>*[Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* | Quality is the hard constraint and speed is the engineering work: every optimization must be lossless, and latency won back through quantization, speculative decoding, and KV cache compression is immediately reinvested into more intelligence (31 parallel models per conversation) rather than banked.<br>*[200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)* |

*Why it matters: It decides whether your latency budget is a ceiling you design the model choice under, or a resource you spend down on redundancy and supervisor models. In regulated or safety-critical domains the first framing caps achievable accuracy; in consumer real-time products the second framing prices you out of the interaction entirely.*

### Should teams chase total latency, or make the wait legible and stop chasing it?

| Position A | Position B |
|---|---|
| Replace total latency with time to first chunk as the primary UX metric; a 10-second operation is acceptable if the user can see what is happening, and the loading spinner is what actually fails. Equivalently, change the output modality — visuals buy a ~1s envelope where voice demands 200ms.<br>*[Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* | The budget is wall-clock and unmaskable: users perceive the conversation as broken at ~800ms, hang up at 1.5s, and false interruptions measurably raise escalation to human agents — no progressive rendering recovers that.<br>*[Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md)* |

*Why it matters: If perceived latency is the real metric, the investment goes into streaming protocols and rendering layers; if wall-clock is, it goes into co-located GPUs, smaller models, and stripping the model out of the loop. The two roadmaps share almost no work.*

### To hit a sub-second budget, should you own the whole stack or outsource the infrastructure?

| Position A | Position B |
|---|---|
| Vertical integration is required: generic stacks cannot hit the numbers, so build the audio model, the inference optimizations, and the turn-detection stack yourself, and co-locate every model in one GPU cluster.<br>*[200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)* | Hosting, session management, sandboxing, and serving are undifferentiated work; a managed harness or platform delivers better tail latency than in-house builds (60% faster P50 TTFT, >90% at P95) and teams should own only prompts, skills, tools, and domain context.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)* |

*Why it matters: Whether the last few hundred milliseconds are reachable by a small team without building serving infrastructure determines who can compete in real-time AI at all, and whether latency-critical products are startup-addressable or capital-intensive.*

## Practical Guidance

**Do:**

- Set the budget from the interaction's perceptual threshold before choosing components: ~200ms for full voice-to-voice conversation, ~950ms to start speaking, ~1s for a visual response, 4s as the outer limit of believability in chat.
- Hold the LLM to a sub-700ms time-to-first-token target for voice, and measure candidate models at P95, not P50 — a model that is fine at P50 can spike to 1.7s or over 4s at P95.
- Decompose the budget by hop before optimizing: in a cloud-API voice pipeline STT plus LLM eat roughly two-thirds of the total, so they are the only two levers worth pulling.
- Decouple the agent loop from tool-execution container setup so first-token reasoning is not blocked on sandbox startup.
- Retrieve tool schemas just-in-time (K=5 is a strong default; test K=3/5/10 and take the smallest that meets your accuracy target) once you pass ~50 tools; below 20 tools static loading is fine.
- Cap the always-loaded skill/tool description block as a fraction of the context window — Codex caps available skills at 2% and truncates beyond it — and mark the rest as deferred behind tool search.
- Keep the first ~90% of the context identical request-to-request to get prefix caching, and treat cache hit rate as a budget line item (Hippocratic reports 96%+ hit rate and 18x faster prefill).
- Design against P99/P999 when building on object storage: a 256–512KB S3 read is ~200ms at P99 and a tree traversal compounds it, so minimize round trips per logical operation.
- Add a short-circuit to multi-model pipelines — have each specialist first decide whether it needs to speak at all — so parallel breadth does not consume the budget.
- Fire inference every 1–2 seconds while the user is still speaking rather than waiting for a silence window you have already paid for.
- Fix structural and length failures with deterministic post-processing in the harness instead of upgrading to a bigger, slower model.
- Prune context or reset the session after ~15–20 voice turns, where instruction following degrades.
- Re-audit harness workarounds on every model upgrade — fixes written for an older model's limitations become pure latency overhead and can cause incorrect cache discards.

**Avoid:**

- Choosing a model on peer recommendation or benchmark reputation instead of measuring latency on your own workload — the recommended small model came in at ~8 seconds in one evaluation.
- Assuming a small model is a fast model: GPT-5 mini was measured at ~5,000ms typical, 7,000ms P95, sometimes 10,000ms, because the serving platform did not prioritize latency.
- Loading the whole tool catalog on every request: 741 tools costs ~127,000 tokens per call and drops tool-selection accuracy to 13.6%.
- Adding chain-of-thought to a latency-critical small-model call for formatting gains — it added 600ms where few-shot examples added 200ms and worked better.
- Trying to buy your way out of an architectural limit with hardware — an additional 2,000 servers did not close the gap from 10k to 60k requests per second.
- Reusing batch-inference infrastructure for real-time workloads, or serving real-time video from a single region when the requirement is sub-100ms everywhere.
- Tuning a single global minimum-silence threshold: the right value is domain-specific, ~200ms for a sales agent versus 1,000–1,200ms where users need thinking time.
- Relying on turn-detection or VAD alone — combine a turn-detection model with a silence timer so a miss costs latency rather than correctness.
- Running the agent loop and tool execution in the same container, which couples their failure domains as well as their startup cost.
- Making infrastructure decisions from published benchmarks rather than first-principles napkin math — benchmarks routinely hide things like an unnoticed distributed query inflating P99.
- Shipping a traditional loading spinner for a multi-second AI operation; users have left the forgiving phase and expect to see progress.

## Notable Outliers

- Running 31 models in parallel for every patient conversation stays inside a real-time budget because each specialist first decides whether it needs to speak at all, short-circuiting most of them. ([200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [13:00](https://www.youtube.com/watch?v=AN65uc645mE&t=780s))
- An on-device game agent must finish planning inside a 16ms frame at 60Hz or the player sees jank, and time overruns should be penalized harder than space overruns. ([Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [8:44](https://www.youtube.com/watch?v=418t26CVz-w&t=524s))
- A turn-detection model with only 58.9% recall is the right production choice, because a VAD timer running underneath means a miss costs latency rather than correctness. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [10:32](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=632s))
- Sub-100ms interactive video forces geographically distributed GPU capacity — a user in India or Japan must be routed to a GPU there, or the medium breaks. ([The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md), [13:02](https://www.youtube.com/watch?v=5dCAmSDOAjI&t=782s))
- At 1,000 tokens/sec inference, the network — not the model — becomes the dominant bottleneck in the agent loop, which is why the Responses API moved to a persistent WebSocket that ships only changed items. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s))
- Harness workarounds written for an older model's context anxiety became pure overhead on Opus 4.5, adding latency and causing the cache to be discarded incorrectly. ([Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [8:08](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=488s))

## All Talks

- [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)
- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)
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
- [Clay Cockrell](../speakers/clay-cockrell.md)
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
- [Tony Fabrikant](../speakers/tony-fabrikant.md)
- [Vivek Muppalla](../speakers/vivek-muppalla.md)

