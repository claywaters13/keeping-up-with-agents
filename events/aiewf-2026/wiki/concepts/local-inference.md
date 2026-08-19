---
title: "local inference"
type: "concept"
slug: "local-inference"
tier: "supporting"
maturity: "consolidating"
talk_count: 16
speaker_count: 31
---

# local inference

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **16** talk(s) by **31** speaker(s)

**Definition:** Running models on the user's own hardware — laptop, phone, edge device, or self-hosted server — instead of a hosted API.

*Also referred to as: on-device inference, local model inference, local llm serving, local-first inference, consumer gpu deployment, edge inference on microcontrollers, self-hosted inference*

## State of Practice

As of this conference, local inference has moved from hobbyist demo to a deployment tier practitioners actually plan around: a 4B model on an iPhone is treated as roughly GPT-4o-class, a 27B dense model beats Llama 405B, and 550B Nemotron 3 Ultra runs at 30 tok/s across four DGX Sparks. The economic argument that carries the room is not falling token prices but rising total spend — agentic sessions consume tokens exponentially faster than per-token prices drop — combined with control, data locality, and avoiding rug-pulls, which enterprises name as often as cost. The technical default is a quantized larger model rather than a natively small one (a 120B at 4-bit beats a 35B at BF16 for the same disk), with selective per-layer precision — first/last layers and QKV projections kept high, linear-attention layers left alone — and KL divergence against the BF16 checkpoint as the honest quality metric rather than accuracy benchmarks. The architecture people converge on is tiered: a frontier model for high-level planning or prototyping, small/local models for execution, with harness quality (tool scoping, post-processing, memory policy) doing much of the work — a controlled experiment holding model and eval fixed showed a 20-point spread from harness alone, and the effect is larger for weaker models. The unresolved parts are where the line sits: DRAM cost, not compute, binds at the edge (a 2B model wants 4GB+ once KV cache and OS are counted), 32K context windows break chat-memory recall from 92-95% down to 33%, and usability — point-and-click setup that auto-configures for your hardware — is repeatedly named as the real blocker, not capability.

## Consensus

### Most workloads do not need frontier-level intelligence; the correct default is the smallest model that clears your acceptance bar, not the most capable one available.

Support: **5** talk(s)

> "You're going to want to select the smallest model that gives acceptable responses for your use case. Or as I like to call it, the SAGE model, the small and good enough model."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [15:26](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=926s)

Supporting talks: [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

### Local open-weight models crossed the threshold for real agentic tool-use work within the last year; this is a recent, datable step change rather than a gradual trend.

Support: **5** talk(s)

> "a year ago this time a year ago we didn't have any local models that were able to successfully run within clo code"
>
> — [The Desktop Frontier](../talks/the-desktop-frontier.md), [2:43](https://www.youtube.com/watch?v=XV2oYi7kojc&t=163s)

Supporting talks: [The Desktop Frontier](../talks/the-desktop-frontier.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### Falling per-token prices are not reducing total inference spend, because agentic and reasoning workloads grow token consumption per session faster than prices drop — this, not unit price, is the economic case for local.

Support: **4** talk(s)

> "Now, token costs have been falling as of late, but total inference spend has been rising because agent can reasoning workloads consume tokens way faster than prices are dropping."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [2:11](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=131s)

Supporting talks: [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### Control, sovereignty, and data locality drive local/open adoption as much as cost — the ability to inspect the stack, keep data inside a perimeter, and not lose access to a model you depend on.

Support: **6** talk(s)

> "they want control, they want sovereignty, they want the ability to switch out models, they don't want to get rugpulled"
>
> — [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [15:08](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=908s)

Supporting talks: [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)

### Quantization is the default path to local deployment, and for a fixed memory or disk budget a larger model at low bit-width beats a smaller model at full precision.

Support: **4** talk(s)

> "they show that the bigger model quantized to 4bit is actually much better um than a 35 billion 16 bit"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [22:50](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1370s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

### The production architecture is tiered: the most capable model does high-level planning (or is used only for prototyping), and smaller/local models execute the subtasks.

Support: **3** talk(s)

> "Your most intelligent should provide you with the overall plan and then subtasks for your smaller executioner like executioner models and that's exactly the future"
>
> — [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [14:30](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=870s)

Supporting talks: [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Frontier results, on device](../talks/frontier-results-on-device.md)

### Public benchmarks, arenas, and peer recommendation are unreliable for selecting or validating a local model; you need your own task-specific eval set and hands-on inspection.

Support: **4** talk(s)

> "there's so many things that I feel can't be captured by a uh model optimizer or after quantizing it or you know certain benchmarks and it's literally me you know running through putting it in cloud code or something and running the model it's like no it doesn't feel just right"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [18:32](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1112s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)

## Disagreements

### For real production agent workloads, should inference actually run on the user's own hardware, or should the model stay on a server even when the stack is otherwise open?

| Position A | Position B |
|---|---|
| Run it locally. Within a year most daily AI tasks will run on a laptop rather than an API; enterprises should buy hardware rather than fund subsidized cloud tokens, and mobile games should push intelligence onto the device to avoid round-trip latency and keep data in the device's security zone.<br>*[Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)* | Keep the model off the endpoint. Current LLMs cannot run on small MCUs so the model must be served from a backend; hosting an agent in the cloud beats local because local hosting makes you responsible for uptime; agents should run autonomously in an encrypted cloud perimeter without requiring the user's device to be online; and swapping in a local model is not drop-in — a 32K window cut chat recall from 92-95% to 33%.<br>*[OpenClaw in Your Hand: Building a Physical AI Terminal](../talks/openclaw-in-your-hand-building-a-physical-ai-terminal.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: This decides whether you invest in hardware and on-device runtimes or in confidential-compute and attestation infrastructure — two completely different engineering programs that both claim the same privacy and control benefits.*

### Can a good harness plus post-training on an open model close the gap to frontier, or must a frontier model remain in the loop?

| Position A | Position B |
|---|---|
| Yes — a sufficiently good harness can make a local open-source model reach cutting-edge proprietary performance (20-point spread from harness alone, with the effect larger for weaker models), and a post-trained open model can beat Opus on a specialized task at a fraction of Haiku's cost in one to two weeks.<br>*[What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)* | No — a frontier model should always remain present in the system, watching if not executing, because out-of-distribution small models increase cost through runaway tool loops (Opus scores 3x better than Haiku on terminal bench at 1/10 the total cost); a capability gap will always exist even as it shrinks; and current base model intelligence is insufficient for the hardest agent decisions.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)* |

*Why it matters: If the harness closes the gap, teams should invest engineering effort in scaffolding and own their stack outright; if not, every local deployment still needs a frontier API dependency and the sovereignty argument is only partially deliverable.*

### To make a small or local model good enough for a task, should you train it (fine-tune, distill, quantization-aware distillation) or leave the weights alone and fix the prompt and harness?

| Position A | Position B |
|---|---|
| Train it. Below ~20B, post-training quantization needs quantization-aware distillation to recover accuracy; tiny models in the 50M-500M range must be fine-tuned on 10k-10M synthetic samples unless an off-the-shelf fixed-task model exists; post-training an open model on your own harness is the fastest path to a differentiated product; distilling frontier models to bootstrap open ones will be the dominant 2026-2027 pattern.<br>*[Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* | Don't train it. Distilled models are a poor fit for shipped apps because every capability change means retraining and pushing a 1-2 GB model over users' data plans; few-shot examples plus deterministic post-processing in the harness closed the gap to Claude on the same task; and fine-tuning-as-a-service has not taken off precisely because model customization is itself a hard problem.<br>*[Frontier results, on device](../talks/frontier-results-on-device.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* |

*Why it matters: Training implies owning a data pipeline, an eval loop, and a model release process; the prompt-and-harness route ships today with off-the-shelf weights but caps out at whatever the base model can do.*

### On local hardware, is minimizing what you send to the model a real lever, or a false economy imported from cloud pricing intuitions?

| Position A | Position B |
|---|---|
| Minimize aggressively. 90% of AI coding cost is input tokens, and a local hybrid index cut context from 83K to 4.9K tokens per question; models should not be used past ~200K tokens and ideally under 100K regardless of advertised windows; when the task exceeds the window a memory harness with a rank-only decisions ledger pays off and good recall policy reduces total token spend.<br>*[We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)* | Do not compact by default. Keeping the full conversation untouched beat every compaction preset simultaneously on recall, cost, and latency, because 97% of tokens were cached; clearing tool outputs makes the agent re-retrieve what it already had; and distinctive facts were recalled reliably up to 800k tokens.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: The keep-everything result depends on a hosted provider's prompt cache, which local deployments do not get — so whether it generalizes determines if local inference needs a retrieval and memory layer as a hard prerequisite or just an optimization.*

## Practical Guidance

**Do:**

- Prototype on a foundation model, then convert individual steps to small or local models for production — 'prototype big, deploy small'
- Build a golden dataset of human-labeled input/output pairs before selecting a local model, and run regression evals continuously like CI tests
- Isolate one variable per prompt variant when tuning a small model; prefer few-shot examples (+200ms latency) over chain-of-thought (+600ms)
- Fix structural and length failures with deterministic post-processing in the harness rather than reaching for a bigger model
- Keep first and last layers and attention/QKV projections at higher precision when quantizing; the middle layers tolerate 1-2 bit
- Evaluate quantized checkpoints by KL divergence over output logits against the BF16 model, and re-test on long-context benchmarks before shipping
- Above ~20-30B use post-training quantization directly; below 20B budget for quantization-aware distillation to recover accuracy
- For tiny (50M-500M) models targeting a single fixed task, generate 10k-10M synthetic samples and fine-tune — voice-to-function-calling hit 86% reliability across 10 functions this way
- Budget ~4GB+ of device DRAM for a 2B-class model once KV cache, runtime, and OS are counted, and treat DRAM cost rather than compute as the binding edge constraint
- For on-device game agents, complete planning inside the 16ms frame at 60Hz and penalize time overruns harder than space overruns
- Combine BM25 keyword with dense semantic retrieval — each alone misses ~1 in 4 results, together ~1 in 10
- Manually inspect LLM-judge scores, since judges favor models from their own family
- Constrain local agents with sandboxing and locked tool arguments (partial function application) rather than per-action human approval, which is safe but slow
- Self-host when your workload shape is known and stable — API pricing amortizes across all customers' usage patterns, so a specialized workload likely costs less on your own compute

**Avoid:**

- Uniformly quantizing all layers — compressing 86% of weights uniformly makes a model useless, not 86% worse; selective per-layer precision is what makes it viable
- Quantizing linear attention layers — short benchmarks look fine while long-context production output turns to gibberish
- Picking a local model on peer recommendation: the socially recommended model came in around 8 seconds latency against a 4-second believability limit
- Explicit negative rules in small-model prompts — strict prohibitions made output worse than few-shot examples
- Shipping per-capability distilled models inside mobile apps, where every change forces a 1-2 GB download over users' data plans
- Assuming a local model is a drop-in swap: a 32K window dropped chat recall from 92-95% to 33%, and raising parameter count does not expand the context window
- Routing on task type alone — complexity changes mid-session, which makes it extremely fragile for agentic work
- Equating cheaper-per-token with cheaper overall — out-of-distribution small models raise total cost through tool-call thrash and runaway loops
- Expecting sparsity to be free: it degrades accuracy more than quantization does, which is why it stayed unadopted despite hardware support
- Fine-tuning SAM 3 directly — you lose the open-vocabulary capability that makes it worth using; distill to a fixed class list instead
- Writing your own crypto or giving an agent direct access to a personal computer — reuse audited software and remove the means to cause harm
- malloc and markdown rendering on an MCU — use pre-allocated fixed buffers
- Cheap components in embedded builds — a low-quality encoder cost extra pull-ups and capacitors, a bad regulator cost weeks in replacement parts

## Notable Outliers

- Compression works only because current models are undertrained — if models were trained on ~300 trillion tokens, the quantization headroom would largely disappear. ([Compression at the Edge](../talks/compression-at-the-edge.md), [12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s))
- Quantizing a single number — one weight in the entire model — can make the model 20% dumber (the 'super weights' result). ([Compression at the Edge](../talks/compression-at-the-edge.md), [14:03](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=843s))
- Reaching the majority of devices needs models in the 50M-500M parameter range, not the 1-4B 'small model' class — small models are still too big for older laptops and consumer edge devices. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [12:16](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=736s))
- Roughly 0.000001% of AI users have ever run an open model themselves — the local ecosystem's entire visible activity is a rounding error on total usage. ([Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [35:59](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=2159s))
- Capability density follows a 'densing law' of ~50% fewer parameters for equivalent capability every 3.5 months, which is why a 2020-architecture RTX 3090 still sells above MSRP — GPUs bought today get more valuable over time. ([The Desktop Frontier](../talks/the-desktop-frontier.md), [16:33](https://www.youtube.com/watch?v=XV2oYi7kojc&t=993s))
- A 10x inference speedup on DGX Spark was achieved in ~3 weeks with no new computer science — just a vLLM backend, quantization, and config tuning of techniques NVIDIA had already published. ([State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [21:43](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=1303s))
- Local models are still a real productivity tax for research: they don't support batch querying, so full evaluation pipelines can only run serially. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [11:48](https://www.youtube.com/watch?v=R3-anFK1YM8&t=708s))

## All Talks

- [Compression at the Edge](../talks/compression-at-the-edge.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)
- [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)
- [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)
- [OpenClaw in Your Hand: Building a Physical AI Terminal](../talks/openclaw-in-your-hand-building-a-physical-ai-terminal.md)
- [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)
- [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)
- [The Desktop Frontier](../talks/the-desktop-frontier.md)
- [The State of Model Routing](../talks/the-state-of-model-routing.md)
- [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [While my guitar gently speaks](../talks/while-my-guitar-gently-speaks.md)
- [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

## Speakers

- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Alex Atallah](../speakers/alex-atallah.md)
- [Alex Cheema](../speakers/alex-cheema.md)
- [Asma Beevi](../speakers/asma-beevi.md)
- [Carter Abdallah](../speakers/carter-abdallah.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Cormac Brick](../speakers/cormac-brick.md)
- [Daniel Han](../speakers/daniel-han.md)
- [George Cameron](../speakers/george-cameron.md)
- [Joanne Song](../speakers/joanne-song.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Lucas Atkins](../speakers/lucas-atkins.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Merve Noyan](../speakers/merve-noyan.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Omar Solano](../speakers/omar-solano.md)
- [Parth Sareen](../speakers/parth-sareen.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Ramesh Raskar](../speakers/ramesh-raskar.md)
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Shafik Quoraishee](../speakers/shafik-quoraishee.md)
- [Stefania Druga](../speakers/stefania-druga.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Todd Fisher](../speakers/todd-fisher.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Walden Yan](../speakers/walden-yan.md)

