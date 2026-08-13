---
title: "small language models"
type: "concept"
slug: "small-language-models"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 18
---

# small language models

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **18** speaker(s)

**Definition:** Deliberately small or narrowly specialized models chosen for cost, latency, or deployability over frontier generality.

*Also referred to as: tiny language models, small model substitution, task-specific models, specialized domain models, domain-specific llms, model specialization, domain specialization*

## State of Practice

The field has stopped treating model size as a proxy for quality and started treating it as a budget line with latency, DRAM, and energy denominations. The dominant claim across tracks is that the frontier model is the wrong default for production: roughly 90% of tasks don't need frontier intelligence, a voice agent must start speaking inside ~950ms (and 4s is the outer limit of believability in chat), and a 2B model needs ~4GB of device DRAM at a moment when Raspberry Pi memory prices have gone up 2.5x. The consensus workflow is prototype big, deploy small — build against a frontier model, then push components down to a 3-4B open model, a fine-tuned task model, or a 50M-500M tiny model, validated against a golden dataset rather than peer recommendation. Where speakers split is on how you close the residual gap: one camp keeps weights frozen and pays once in code (state machines that hold workflow state, deterministic post-processing for structural/length failures, few-shot examples at +200ms instead of chain-of-thought at +600ms), the other changes the weights (10k-10M synthetic samples for a tiny model, post-training an open model on your harness, RL over verified outcome data). Both camps report the same headline result — small model beats or matches frontier on the narrow task — which is why the argument is about method, not possibility. The economic argument is sharper than a year ago: total inference spend is rising even where per-token prices fall, because agentic and reasoning workloads consume tokens faster than prices drop, and at least one speaker claims the per-token trend itself reversed in 2026.

## Consensus

### Most production workloads do not need frontier-level intelligence; the correct selection rule is the smallest model that produces acceptable output for the specific use case, not the most capable one available.

Support: **7** talk(s)

> "most people probably do not need frontier level intelligence for like 90% of their tasks"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [26:45](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1605s)

Supporting talks: [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)

### A small model inside a strong harness performs at the level expected of a frontier model; the surrounding scaffolding, not the parameter count, is what determines delivered reliability.

Support: **5** talk(s)

> "instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn't have as much reasoning capabilities, but because of the harnessing around it, it's still able to perform at the level in which we expect"
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

### Falling per-token prices do not produce falling bills, because agentic and reasoning workloads multiply token consumption faster than unit prices move — so cost control has to come from architecture, not from waiting.

Support: **4** talk(s)

> "Now, token costs have been falling as of late, but total inference spend has been rising because agent can reasoning workloads consume tokens way faster than prices are dropping."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [2:11](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=131s)

Supporting talks: [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

### Latency, not answer quality, is the binding constraint in interactive systems, and frontier reasoning time costs more than the quality it buys.

Support: **4** talk(s)

> "A frontier model that think for a full second has already lost the room, no matter how good the answer is."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [0:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=51s)

Supporting talks: [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### Frontier models belong at the top of the stack — prototyping, planning, hypothesis generation, synthetic data generation — while smaller models execute the subtasks in production.

Support: **4** talk(s)

> "Now, first off, I like to think of this as prototype big, deploy small. Just repeat this to yourself."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [8:56](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=536s)

Supporting talks: [Frontier results, on device](../talks/frontier-results-on-device.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

### On a narrowly scoped task, a specialized smaller model matches or beats a frontier model head-to-head — via fine-tuning, post-training, or grounding in proprietary outcome data.

Support: **5** talk(s)

> "we were able with a midsize cheaper model to outperform the frontier models because of the grounding that I just showed you."
>
> — [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s)

Supporting talks: [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Frontier results, on device](../talks/frontier-results-on-device.md)

### The trajectory is toward many specialized models coordinating, not one general model absorbing every workload — no single static model can cover the heterogeneity of real deployment environments.

Support: **4** talk(s)

> "It's just like too heterogeneous and dynamic for any monolithic model to try to compress it into one static representation"
>
> — [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [5:27](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=327s)

Supporting talks: [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)

## Disagreements

### When a small model falls short on your task, do you fix the harness around it or change the model's weights?

| Position A | Position B |
|---|---|
| Leave the weights alone. Extract control flow and state into application code, add deterministic post-processing for structural and length failures, tune prompts with few-shot examples, and use the thinnest possible wrapper — the scaffolding cost is paid once in code rather than on every turn, and shipping a retrained 1-2GB model to mobile users for every capability change is untenable.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)* | Change the model. Generate 10k-10M synthetic samples and fine-tune a tiny model per fixed task, post-train an open model on the harness you care about, or train an RL selector on verified outcome data — because prompting and context cannot supply experience the model never had.<br>*[Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* |

*Why it matters: This decides whether a team needs a data-labeling and training pipeline plus a weight-distribution story, or only software engineers writing state machines and post-processors. It also determines the update cadence: a harness change ships instantly, a weights change ships as a multi-gigabyte binary over users' data plans.*

### Is a frozen small model plus good scaffolding sufficient, or is the real ceiling the inability to accumulate expertise over time?

| Position A | Position B |
|---|---|
| Sufficient. The model proposes and the harness decides; judgments about task completion and next step are engineered outside the model, so a static Haiku-class model plus a state machine delivers reliable multi-step behavior indefinitely.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)* | Insufficient. Intelligence and expertise are orthogonal, and past a threshold of raw intelligence the continual-learning algorithm becomes the binding constraint; markdown-file agent memory is a stopgap and real progress requires updating weights, locally, from in-situ experience.<br>*[Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* |

*Why it matters: If scaffolding is sufficient, the small-model roadmap is an engineering problem solved today. If expertise accumulation is the ceiling, every harness-based system is capped at 'world's smartest novice' and the investment belongs in local training infrastructure instead.*

### Is the per-token cost of intelligence still falling?

| Position A | Position B |
|---|---|
| Yes — unit prices continue to drop and the rising bill is purely a volume effect from exponentially growing tokens per session; some operators report token counts exploding while total costs stay flat.<br>*[Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* | No — the trend reversed in 2026. Tokens are up 76% raw and 29% IQ-adjusted at the halfway point of the year, which means you cannot put a frontier model in front of a customer unless that customer has very high lifetime value.<br>*[The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* |

*Why it matters: If unit prices keep falling, cost-driven downsizing is an optimization you can defer and recover through volume growth. If the trend has genuinely reversed, per-unit-economics pressure compounds and downsizing becomes a survival requirement for any consumer-facing product this year.*

### How small does 'small' actually need to be to reach the majority of devices?

| Position A | Position B |
|---|---|
| 3-4B is the target. A 4B Qwen 3.5 on an iPhone is roughly GPT-4o-equivalent, a 4B model on a phone today beats GPT-4 at launch, and within a year most daily AI work runs on a laptop-hosted model.<br>*[State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Frontier results, on device](../talks/frontier-results-on-device.md)* | 1-4B is still too big — it cannot reach older laptops or consumer edge devices, where the model is one small feature in a corner of an app competing for DRAM with everything else. Reaching the majority of devices requires 50M-500M parameters, which means fine-tuning is mandatory rather than optional.<br>*[Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)* |

*Why it matters: At 3-4B the playbook is zero-shot prompting and LoRA adapters on off-the-shelf weights; at 50M-500M you must build a synthetic-data pipeline and fine-tune per task. The two answers imply completely different team compositions and time-to-first-deploy.*

## Practical Guidance

**Do:**

- Prototype on a foundation model, then convert components to small and specialized models for production ('prototype big, deploy small').
- Build a curated, preferably human-labeled golden dataset of input-output pairs before choosing a model, and select on eval results rather than peer recommendation — one recommended model came in at ~8 seconds latency.
- Pick the fastest model your latency budget allows, then spend the remaining engineering effort on scaffolding; budget ~950ms to first speech for voice and treat 4 seconds as the outer limit of believability in chat.
- Move workflow state, completion judgments, and next-step selection into an explicit state machine — the model proposes, the harness decides.
- Prefer few-shot examples for small models (+200ms) over chain-of-thought (+600ms); isolate one variable per prompt variant when testing.
- Fix structural and length failures with deterministic post-processing in the harness instead of escalating to a larger model — post-processing closed the gap and beat the frontier baseline.
- Manually inspect LLM-judge scores rather than trusting the numbers: judges favor models from their own family (Opus favoring Sonnet over Llama 3.2).
- Run regression evals continuously, like CI tests, so a prompt or model change cannot silently degrade behavior overnight.
- For tiny (50M-500M) models, generate 10,000-10,000,000 synthetic samples and fine-tune; expect ~86% reliability on ~10 output functions for voice-to-function-calling.
- Size device memory realistically: a 2B-class model needs ~4GB+ of DRAM once KV cache, runtime and OS are counted, and mixed 2/4/8-bit quantization to ~2.9 bits per weight is what makes it fit.
- Route frontier models to top-level planning and hypothesis generation, with smaller models executing subtasks and a separately trained selector deciding which hypothesis to act on.
- Have agents emit HTML/CSS/JavaScript rather than a custom format; a small model (Gemini 3 Flash) authoring workable code in a format is the signal that larger agents will handle it too.
- When agent reliability approaches a coin flip, take the control flow out of the model rather than adding prompt rules.

**Avoid:**

- Reaching for more prompt rules when a multi-step agent skips steps or loops — that is a control problem, not a prompting problem.
- Asking the model to remember which step of a workflow it is on.
- Explicit negative constraints in small-model prompts — they made results measurably worse than few-shot examples or reformatted input.
- Trusting LLM-judge scores numerically without inspection.
- Shipping distilled models to mobile apps, where every capability change forces a retrain and a 1-2 GB download over users' data plans.
- Teaching a model a new DSL or custom JSON structure — quality degrades even with many examples.
- Loading many skills, MCP servers and tools into one agent's context; research shows it makes the agent substantially worse, and it is inheritance by another name.
- Assuming more context substitutes for outcome grounding — a company's complete financial data is still just one group of data points.
- Fine-tuning SAM 3 directly; distill to a fixed class list and drop the expensive autoencoder instead, or you lose the open-vocabulary capability that made it worth using.
- Targeting Raspberry Pi-class hardware for real-time interaction with a 2B model — 7.6 tokens/sec decode is too slow; Jetson-class NPU reaches ~31 tokens/sec decode.
- Validating agent reliability under demo conditions, which systematically fail to surface the step-skipping and looping that real users trigger.
- Expecting to close a domain gap by scaling to a bigger model.

## Notable Outliers

- Past a threshold of raw intelligence, further intelligence is unnecessary and the continual-learning algorithm becomes the binding constraint — current frontier models may already be smart enough, producing 'the world's smartest novice.' ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s))
- In a Princeton 500-day business simulation, most frontier models drove the company bankrupt in under 500 days, and a simple rules-based system outperformed almost all of them. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s))
- DeepSeek V4 Flash is 137 times cheaper per task than Fable 5, and narrow task scoping is what makes the cheap model reliable enough to actually use. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [17:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1057s))
- An SLM consumes about 25% of the energy an LLM uses for the same task, and a task-specific model about half of that again. ([Frontier results, on device](../talks/frontier-results-on-device.md), [6:32](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=392s))
- Reaching the majority of devices requires 50M-500M parameter models, because the model is usually one small feature in the corner of an app rather than the app itself — and DRAM cost is getting worse, with some phone makers shipping less memory than last year. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [12:16](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=736s))
- On the order of 0.000001% of AI users have ever run an open model themselves, making distribution rather than capability the decisive variable this year. ([Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [35:59](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=2159s))
- EXO Labs and NVIDIA got a 10x inference improvement on DGX Spark in about three weeks using only existing techniques — vLLM backend, quantization, config tuning — with no new computer science. ([State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [21:43](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=1303s))
- Deliberately starting with a very small model (Gemini 3 Flash) as the design partner is a format-validation strategy: if the small model can author workable code in your format, the coding agents certainly can. ([HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s))

## All Talks

- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)
- [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)
- [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Alex Cheema](../speakers/alex-cheema.md)
- [Carter Abdallah](../speakers/carter-abdallah.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Cormac Brick](../speakers/cormac-brick.md)
- [James Russo](../speakers/james-russo.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Lucas Atkins](../speakers/lucas-atkins.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Udi Menkes](../speakers/udi-menkes.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yu Su](../speakers/yu-su.md)

