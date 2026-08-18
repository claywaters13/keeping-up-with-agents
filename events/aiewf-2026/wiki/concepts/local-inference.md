---
title: "local inference"
type: "concept"
slug: "local-inference"
tier: "supporting"
maturity: "consolidating"
talk_count: 14
speaker_count: 27
---

# local inference

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **14** talk(s) by **27** speaker(s)

**Definition:** Running models on the user's own hardware — laptop, phone, edge device, or self-hosted server — instead of a hosted API.

*Also referred to as: on-device inference, local model inference, local llm serving, local-first inference, consumer gpu deployment, edge inference on microcontrollers, self-hosted inference*

## State of Practice

The debate at this conference was no longer whether local models are usable but where the remaining bottlenecks sit. A 4B model on a phone is treated as roughly GPT-4o-class, 4-bit quantization is the assumed default deployment format, and multiple speakers independently put the share of real workloads that need frontier intelligence at around 10%. The economic argument has shifted from per-token price to total spend: prices fall while agentic sessions consume tokens exponentially faster, so shifting execution to owned hardware is framed as a cost-predictability and control decision rather than a penny-pinching one. The live engineering problems are the harness (a 20-point spread on identical model and eval from harness changes alone), context management (90% of coding-agent cost is input tokens), evaluation (accuracy benchmarks miss quantization damage; LLM judges favor their own family), and usability (auto-configuring a model to arbitrary consumer hardware is still not point-and-click). The unresolved questions are how you actually get a good task model — quantize a big general one, post-train an open one, or fine-tune a tiny one on synthetic data — and whether a hosted frontier model remains permanently in the loop as planner.

## Consensus

### The overwhelming majority of real workloads do not require frontier-level intelligence, so the right default is the smallest model that produces acceptable output.

Support: **5** talk(s)

> "most people probably do not need frontier level intelligence for like 90% of their tasks"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [26:45](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1605s)

Supporting talks: [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

### Total inference spend is rising even as per-token prices fall, because agentic and reasoning sessions consume tokens faster than prices drop — which is the economic case for moving execution local.

Support: **4** talk(s)

> "Now, token costs have been falling as of late, but total inference spend has been rising because agent can reasoning workloads consume tokens way faster than prices are dropping."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [2:11](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=131s)

Supporting talks: [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)

### Control, sovereignty, and data custody — not token cost — are the primary enterprise drivers for local and open models, including guaranteed continued access to a specific checkpoint.

Support: **6** talk(s)

> "they want control, they want sovereignty, they want the ability to switch out models, they don't want to get rugpulled"
>
> — [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [15:08](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=908s)

Supporting talks: [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### The harness — tool access, memory, context hygiene, retry structure — is what closes the gap between local models and hosted frontier models, and it matters more the weaker the model is.

Support: **5** talk(s)

> "So, scores range from 52.4% to 76.2%. So, more than a 20-point difference, and only the harness changed."
>
> — [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s)

Supporting talks: [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)

### What you feed the model dominates which model you pick as a cost lever; input tokens and recall policy are where spend actually goes.

Support: **3** talk(s)

> "We argue about which model is best, Opus or Sonnet. But the models may be 30% of the cost, but other 70% is what you feed it."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [9:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=571s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)

### Standard accuracy benchmarks and LLM judges are unreliable for evaluating small, quantized, or local models; you need task-specific evals and manual inspection.

Support: **4** talk(s)

> "Claude Opus was comparing Claude Sonnet's response to uh Llama 3.2's response, and of course Claude was favoring its little sister"
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [25:57](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1557s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)

### The emerging architecture splits planning from execution: a large model produces the plan and subtasks, smaller or local models execute them.

Support: **4** talk(s)

> "Your most intelligent should provide you with the overall plan and then subtasks for your smaller executioner like executioner models and that's exactly the future"
>
> — [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [14:30](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=870s)

Supporting talks: [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### For a fixed memory or disk budget, running a larger model at 4-bit beats running a smaller model at full precision, which is why 4-bit is the de facto local deployment format.

Support: **4** talk(s)

> "they show that the bigger model quantized to 4bit is actually much better um than a 35 billion 16 bit"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [22:50](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1370s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

## Disagreements

### Should agents actually run on the user's own hardware, or should they be hosted in the cloud with local control enforced cryptographically?

| Position A | Position B |
|---|---|
| Run it locally: own the hardware end to end, keep data inside the device or the developer's own machine, and treat serial or slower execution as an acceptable price for sovereignty.<br>*[The Desktop Frontier](../talks/the-desktop-frontier.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)* | Host the agent in the cloud for most use cases — local hosting makes you responsible for uptime, and long-running agents must operate while the user's device is offline; privacy is better achieved with attestation, enclaves, and client-held keys than with local execution.<br>*[The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)* |

*Why it matters: This determines whether the privacy and control benefits of 'local' require local silicon at all, or can be delivered by verifiable remote execution — which changes hardware purchasing, uptime engineering, and the entire threat model.*

### How do you get a model good enough to run locally on your task — post-train or fine-tune it, or take a general open model and fix the surrounding system?

| Position A | Position B |
|---|---|
| Specialize the weights: post-train an open model on your harness (one to two weeks to beat Opus on a finance task), or fine-tune a tiny model on 10k–10M synthetic samples to match a 2–4B model on one fixed task.<br>*[Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* | Leave the weights alone: take a general open checkpoint, quantize it, and invest in prompting, few-shot examples, deterministic post-processing, and harness design — distilled or custom-trained models are an operational liability, since every capability change means retraining and shipping a new 1–2 GB artifact to users.<br>*[Frontier results, on device](../talks/frontier-results-on-device.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Compression at the Edge](../talks/compression-at-the-edge.md)* |

*Why it matters: It decides whether a local AI team needs a training pipeline and synthetic data infrastructure at all, or just evals and engineering — and whether shipping updates means a model download or a config change.*

### Does a hosted frontier model need to stay permanently in the loop, or can the whole system run locally?

| Position A | Position B |
|---|---|
| Keep frontier intelligence always present — watching if not executing — because routing on task type is fragile, task complexity shifts mid-session, and out-of-distribution small models can increase total cost through runaway tool loops.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* | The frontier model is eliminable: a good enough harness lets a local open model reach cutting-edge performance, most daily tasks will run on a laptop within a year, and a 3B local model plus post-processing already beat a frontier baseline on a real product task.<br>*[What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)* |

*Why it matters: If a frontier model must always be reachable, offline and air-gapped deployments stay out of reach and the API dependency never goes away; if not, the hosted call becomes a prototyping tool you delete before shipping.*

### Is the local capability constraint about to dissolve, or is hardware the hard wall?

| Position A | Position B |
|---|---|
| It dissolves fast: capability density is halving parameter counts every ~3.5 months, GLM 5.2-class intelligence lands on a single 32GB RTX 5090 within 18 months, and open models exceed today's frontier within 12.<br>*[The Desktop Frontier](../talks/the-desktop-frontier.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* | Memory and physics push back: DRAM cost is the binding edge constraint and is getting worse (phone makers are shipping less RAM, Raspberry Pi 6GB cost up 2.5x), weight quantization is near Pareto optimality, and current model base intelligence is still insufficient for the harder on-device agent tasks.<br>*[Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)* |

*Why it matters: It sets whether you design today's product around a model that will comfortably fit next year's consumer device, or engineer hard against a 50M–500M parameter, 4GB-DRAM ceiling that is not moving.*

## Practical Guidance

**Do:**

- Prototype on a frontier model, then convert production paths to the smallest model that gives acceptable responses for the specific use case.
- Build a golden human-labeled input/output dataset first, and run regression evals continuously like CI tests so a prompt or model change cannot silently degrade behavior.
- Evaluate quantized checkpoints with KL divergence of output logits against the BF16 model rather than with accuracy benchmarks.
- Keep the first layer, last layer, and attention/QKV projections at higher precision while pushing middle layers to 1–2 bit.
- Run long-context benchmarks specifically before shipping a quantized model — short benchmarks will not surface linear-attention damage.
- Prefer few-shot examples over chain-of-thought for small models: CoT added 600ms of latency versus 200ms for few-shot, with worse gains.
- Fix structural and length failures with deterministic post-processing in the harness instead of reaching for a bigger model.
- Attack input tokens, not output settings — combine semantic and keyword search (missing ~1 in 10 versus ~1 in 4 alone) and use a cheap weighted score (50% semantic / 30% keyword / 20% recency, 0.4ms) instead of LLM reranking.
- Keep agent sessions under ~200K tokens of context, ideally under 100K, regardless of the advertised window.
- Use one long-lived sidekick agent with a running context instead of spawning fresh sub-agents, since cached tokens are ~10x cheaper.
- Constrain agent capabilities structurally — sandbox, deny arbitrary file read/write by default, and lock tool arguments via partial application so the model cannot see or change them.
- For on-device game agents, budget planning inside a 16ms frame at 60Hz and penalize time overruns harder than space overruns.
- For tiny (50M–500M) models, generate 10,000–10,000,000 synthetic samples and fine-tune per fixed task; voice-to-function-calling hit 86%+ reliability across 10 functions this way.
- Instrument real queries against a counterfactual baseline to measure token savings rather than estimating them.

**Avoid:**

- Do not quantize linear attention layers — short benchmarks look fine and the model turns to gibberish in real long-context production use.
- Do not apply post-training quantization out of the box below ~20B parameters; sub-20B needs quantization-aware distillation to recover accuracy, and QAT on wrong data breaks the model rather than helping.
- Do not pick a local model from peer recommendation — the socially recommended choice came in at ~8 seconds latency, past the 4-second limit of user believability.
- Do not trust LLM-judge scores numerically; judges favor models from their own family, so inspect results manually.
- Do not route on task type alone — it is extremely fragile for agentic work because complexity changes mid-session.
- Do not assume a smaller model is cheaper: out-of-distribution small models call tools excessively and can raise total cost, and Opus scored 3x better than Haiku on terminal bench at 1/10 the total cost.
- Do not use prompt instructions to ask for less context — the context was already transmitted and billed before the model read the prompt.
- Do not treat compaction as a cost or throughput fix; it forces a cache miss and raises input token cost. Compact for intelligence, not economics.
- Do not add a memory harness when the task and its relevant context fit in the window — it adds cost with no capability gain.
- Do not ship distilled models into mobile apps if capabilities change often; each change means retraining and pushing a 1–2 GB download over users' data plans.
- Do not use explicit negative constraints in small-model prompts — they made results worse than few-shot examples.
- Do not rely on behavioral instructions to tame agents, and do not give agents direct access to personal computers; only sandboxing and removing the means to cause harm work.
- Do not write your own crypto for privacy-preserving inference; reuse trustworthy existing software and keep the security-critical surface small (~20k lines in a memory-safe language).
- Do not fine-tune SAM 3 directly — you lose the open-vocabulary capability that makes it valuable; distill to a fixed class list instead.
- Do not economize on components in embedded AI builds — a cheap encoder cost extra pull-ups and capacitors and a bad regulator cost weeks in replacement parts.

## Notable Outliers

- Roughly 0.000001% of AI users have ever run an open model themselves — the local AI community is a rounding error relative to API users. ([Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [35:59](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=2159s))
- Reaching the majority of devices requires 50M–500M parameter models, not the 1–4B 'small model' class — small models are still too big for older laptops and consumer edge devices. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [12:16](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=736s))
- DRAM cost, not compute, is the binding edge constraint, and it is getting worse: some phone makers shipped less RAM this year and Raspberry Pi 6GB cost rose ~2.5x since launch. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [3:04](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=184s))
- Compression works only because current models are undertrained; if models were trained on ~300 trillion tokens the compression headroom would largely disappear. ([Compression at the Edge](../talks/compression-at-the-edge.md), [12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s))
- Quantizing a single number in a model — one weight — can make it 20% dumber (the super weights result). ([Compression at the Edge](../talks/compression-at-the-edge.md), [14:03](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=843s))
- Weight quantization is close to Pareto optimality with maybe 1–3 bits left; future gains must come from KV cache compression and sparsity, and sparsity remains unadopted despite NVIDIA hardware support because it degrades accuracy more than quantization. ([Compression at the Edge](../talks/compression-at-the-edge.md), [39:54](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2394s))
- A 10x local inference speedup on DGX Spark was achieved in ~3 weeks using only existing techniques (vLLM backend, quantization, config tuning) with no new research — and a 550B Nemotron 3 Ultra runs at 30 tok/s across four Sparks. ([State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [21:43](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=1303s))
- The local code index degrades to near-zero recall at 396 files when individual files carry many responsibilities, and the headline 94% saving is against a worst-case full-file-read baseline, not against modern agentic tools. ([We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [7:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=455s))
- GPUs bought today appreciate as models get more efficient — the 2020-architecture RTX 3090 still sells above MSRP — so buying hardware beats renting subsidized cloud tokens that will get repriced. ([The Desktop Frontier](../talks/the-desktop-frontier.md), [16:33](https://www.youtube.com/watch?v=XV2oYi7kojc&t=993s))
- The 5-minute KV cache lifetime is an operational and pricing decision by providers, not a physical constraint — which is part of why self-hosting for your specific workload shape costs less. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [34:46](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2086s))
- Open claw's 10-minute heartbeat to the user's default model was the specific trigger that made auto-routing explode in January 2026, after two years of near-zero adoption. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [27:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1623s))
- Continual learning will require updating model weights locally; markdown-file agent memory is only a stopgap because context length becomes inefficient. ([State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [31:31](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=1891s))
- No comprehensive public resource exists for comparing the quality of community-produced quantized checkpoints — the ecosystem ships quants nobody has systematically evaluated. ([Compression at the Edge](../talks/compression-at-the-edge.md), [44:21](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2661s))
- Restricting a general-purpose agent for safety destroys its usefulness; a narrowly sandboxed special-purpose agent is the better tradeoff today. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [14:59](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=899s))

## All Talks

- [Compression at the Edge](../talks/compression-at-the-edge.md)
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
- [Lucas Atkins](../speakers/lucas-atkins.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Merve Noyan](../speakers/merve-noyan.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Parth Sareen](../speakers/parth-sareen.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Ramesh Raskar](../speakers/ramesh-raskar.md)
- [Shafik Quoraishee](../speakers/shafik-quoraishee.md)
- [Stefania Druga](../speakers/stefania-druga.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Walden Yan](../speakers/walden-yan.md)

