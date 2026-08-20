---
title: "small language models"
type: "concept"
slug: "small-language-models"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 19
---

# small language models

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **19** speaker(s)

**Definition:** Deliberately small or narrowly specialized models chosen for cost, latency, or deployability over frontier generality.

*Also referred to as: tiny language models, small model substitution, task-specific models, specialized domain models, domain-specific llms, model specialization, domain specialization*

## State of Practice

The field has moved past "use the best model available" as a default. Across voice, clinical documentation, finance, edge/IoT, and local-first deployments, speakers converged on the claim that frontier-level intelligence is unnecessary for the large majority of production tasks, and that the binding constraints are latency (950ms to first audio for voice, ~4s ceiling for chat), unit cost, and deployability (DRAM on device, sovereignty, guaranteed access). Two distinct routes to making a small model work were demonstrated: engineered scaffolding — pulling state tracking, control flow, and completion judgments out of the model into a deterministic harness or state machine — and post-training, where a small open model is fine-tuned on proprietary or synthetic task data. Both routes produced the same reported outcome: a Haiku-class or open small model matching or beating an Opus/frontier model on the narrow task, at a fraction of cost and latency. Notably, the economic argument is not that tokens are cheap: multiple speakers reported that total inference spend is rising because agentic sessions consume tokens faster than prices fall, and one tracked per-token prices actually reversing upward in 2026. What remains unsettled is the size class that matters (1–4B "small" versus 50M–500M "tiny"), whether a frontier model stays in the production loop as planner or hypothesis generator, and whether harness engineering or fine-tuning is the higher-leverage investment.

## Consensus

### Most production tasks do not require frontier-level intelligence; the correct default is the smallest model that clears the quality bar for that specific task.

Support: **8** talk(s)

> "Health care is actually many specific workflows. You don't need, you know, Fable 5 to actually solve all of your clinical notes. We we don't need frontier level intelligence for every problem."
>
> — [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [18:11](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1091s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

### A small model reaches frontier-level task performance only when surrounded by engineered scaffolding that removes state tracking and control flow from the model; the model proposes, the harness decides.

Support: **6** talk(s)

> "instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn't have as much reasoning capabilities, but because of the harnessing around it, it's still able to perform at the level in which we expect"
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)

### The motivation for going small is latency and total cost rather than quality, and total inference spend is rising even as per-token prices fall because agentic sessions consume tokens faster than prices drop.

Support: **5** talk(s)

> "Now, token costs have been falling as of late, but total inference spend has been rising because agent can reasoning workloads consume tokens way faster than prices are dropping."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [2:11](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=131s)

Supporting talks: [Frontier results, on device](../talks/frontier-results-on-device.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

### Post-training or fine-tuning a small model on proprietary or synthetic task data beats an off-the-shelf frontier model on that narrow task, at dramatically lower cost, and is achievable in weeks.

Support: **5** talk(s)

> "take an open model and like specialize it to automate finance within like a week or two to get like better performance than like Opus at a fraction of the cost of Haiku"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [13:39](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=819s)

Supporting talks: [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

### The architecture is trending from one general model toward many narrow specialized models, because no single model can absorb the idiosyncrasies of every domain or workflow.

Support: **5** talk(s)

> "It's just like too heterogeneous and dynamic for any monolithic model to try to compress it into one static representation"
>
> — [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [5:27](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=327s)

Supporting talks: [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)

## Disagreements

### To make a small model production-viable on a task, should you invest in harness/scaffolding engineering around an off-the-shelf model, or in post-training a specialized model?

| Position A | Position B |
|---|---|
| Invest in scaffolding and deterministic code. The model is off-the-shelf and swappable; you pay the cost once in code rather than on every turn, and structural failures are fixed with post-processing, not a bigger or retrained model. Frontier-results-on-device explicitly rejects distillation for mobile because every capability change forces a retrain and a 1–2 GB redownload.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* | Invest in training. Prompting and context are not substitutes for grounding in outcome or in-domain data; you post-train per-section or per-task models on proprietary data (100M clinical conversations, verified business outcomes) or on 10k–10M synthetic samples, which is what actually closes the quality gap and produces the durable moat.<br>*[From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)* |

*Why it matters: The two routes demand completely different teams and cost structures — control-flow engineers and eval harnesses versus a data pipeline, labeling budget, and training infrastructure. Choosing wrong means either a scaffolding stack that plateaus below the quality bar, or a training investment on a problem that a state machine would have solved for free.*

### Does a frontier model remain in the production path as a planner, hypothesis generator, or escalation target, or should it be removed entirely?

| Position A | Position B |
|---|---|
| Keep it at the top of the stack. The frontier model produces the high-level plan or candidate hypotheses and smaller/local models execute the subtasks; cheap event gates decide when to escalate to a heavier model rather than running one continuously.<br>*[State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)* | Remove it. Planning, state, and answer selection belong in application code, not in any model, so there is nothing left for a frontier model to do at runtime; frontier models are also simply too expensive to place in front of a customer without very high lifetime value.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* |

*Why it matters: If a frontier model stays in the loop, latency and cost floors are set by its slowest call and you retain a hard API dependency; if it is removed, the entire system can run locally or on cheap inference, but every planning decision must be encoded and maintained as deterministic logic.*

### What parameter range actually counts as the useful 'small model' target?

| Position A | Position B |
|---|---|
| The 1–4B class. A 4B Qwen 3.5 on an iPhone is roughly GPT-4o-quality, Llama 3.2 3B hits ~90% accuracy on thread summarization, and a 4B model on a phone today beats GPT-4 at launch — this is the size that makes local-first practical.<br>*[State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Frontier results, on device](../talks/frontier-results-on-device.md)* | 1–4B is still too big. Reaching the majority of devices requires 50M–500M parameters, because a 2B-class model needs 4GB+ of device DRAM once KV cache, runtime, and OS are counted, DRAM cost is rising, and the model is usually a minor feature running alongside everything else — a fine-tuned tiny model matches a 2–4B model on a single fixed task anyway.<br>*[Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)* |

*Why it matters: The size class determines whether zero-shot prompting plus LoRA is viable or whether task-specific fine-tuning is mandatory, and it determines the addressable device population — Jetson/phone-class flagship hardware versus the long tail of older laptops and IoT devices.*

## Practical Guidance

**Do:**

- Prototype on a frontier model, then convert production paths to the smallest model that passes your golden dataset — 'prototype big, deploy small'.
- Move state tracking, completion judgments ('is the lesson done?', 'did the user succeed?'), and next-step selection into a deterministic state machine in application code; let the model only propose or speak.
- Pick the fastest model your latency budget allows — ~950ms to first speech for voice, a 4s ceiling for chat believability — and spend remaining engineering effort on scaffolding rather than model upgrades.
- Fix structural and length compliance failures with deterministic post-processing in the harness instead of escalating to a larger model; one talk closed the gap to Claude this way while saving ~$1/day of inference.
- Prefer few-shot examples over reformatted input or chain-of-thought when prompting small models: few-shot added 200ms while CoT added 600ms for a weaker gain.
- Build a curated human-labeled golden dataset and run regression evals continuously like CI tests, so a prompt or model change cannot silently degrade behavior.
- Manually inspect LLM-judge scores rather than trusting the numbers — judges systematically favor models from their own family.
- For fixed-task tiny models, generate 10,000–10,000,000 synthetic samples and fine-tune; a ~86% function-call reliability across ~10 output functions is achievable at that scale.
- Use cheap always-on event gates to decide when to escalate to a heavy model, rather than running the heavy model continuously over a stream.
- Budget 4GB+ of device DRAM for a 2B-class model once KV cache, runtime, and OS are counted, and use mixed 2/4/8-bit quantization (~2.9 bits per weight) to fit.
- Decompose the problem into per-section or per-subtask workflows and post-train a distinct small model for each — e.g. one per section of a clinical note.
- When training on proprietary outcome data, adjust for selection bias — firms that took an action are systematically different from those that didn't ($4,200/day vs $2,800/day naive becomes ~$1,150 corrected).
- Keep small models in their native formats — HTML/CSS/JS rather than a custom DSL — since that is what dominates their training data.

**Avoid:**

- Don't answer multi-step unreliability by adding more prompt rules; when reliability approaches a coin flip, take the control flow out of the model entirely.
- Don't pick a model on peer recommendation — the socially recommended model (Gemma) came in around 8 seconds latency and would have shipped a materially worse experience.
- Don't use explicit negative constraints in small-model prompts; strict negative rules measurably worsened output versus few-shot.
- Don't ship distilled per-capability models inside mobile apps, where every capability change forces retraining and a 1–2 GB download over users' data plans.
- Don't treat more context as a substitute for outcome grounding — a company's complete financial data is still just one group of data points.
- Don't load many skills, MCP servers, and tools into a single agent's context; it is functionally inheritance and it degrades performance.
- Don't teach a model a custom DSL or bespoke JSON schema when a language it already knows will do — quality drops even with many examples.
- Don't fine-tune SAM 3 directly; distill to a fixed class list and drop the expensive autoencoder for a lighter detector, or you lose the open-vocabulary capability you wanted.
- Don't target Raspberry Pi-class hardware for real-time 2B-model interaction — ~7.6 tokens/sec decode is too slow; Jetson-class NPUs reach ~31 tokens/sec.
- Don't trust a single LLM verifier as ground truth on open-ended domains: a verifier good enough to grade would already be your best generator.
- Don't rely on demo conditions to surface failures — step-skipping, premature completion, and looping only appear with real users.

## Notable Outliers

- The 1–4B 'small model' class is still too big: reaching the majority of devices requires 50M–500M parameter models, because the model is usually one small feature running alongside everything else in the system. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [12:16](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=736s))
- The cost of intelligence stopped falling and reversed in 2026 — tokens are up 76% raw and 29% IQ-adjusted at the halfway point of the year. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [22:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1357s))
- In a Princeton 500-day business simulation, most frontier models drove the company bankrupt and a simple rules-based system outperformed almost all of them. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s))
- Past a certain threshold of raw intelligence, further intelligence gains are unnecessary and the continual-learning algorithm becomes the binding constraint — current frontier models may already be smart enough. ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s))
- A small model (Gemini 3 Flash) was deliberately used as the design partner for a new output format, on the logic that if the small model can author workable code in it, larger coding agents certainly can. ([HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s))
- DRAM cost, not compute, is the binding constraint on edge AI, and it is getting worse — some phone makers shipped less DRAM this year, and Raspberry Pi 6GB cost has risen ~2.5x since launch. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [3:04](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=184s))
- Roughly 0.000001% of AI users have ever run an open model themselves, despite a 4B model on a phone now being more useful than GPT-4 at launch. ([Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [35:59](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=2159s))
- On a problem where quality is already maxed out, the reason to train your own model is purely to cut cost and latency — not to improve quality. ([From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [19:23](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1163s))

## All Talks

- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)
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
- [Chaitanya Asawa](../speakers/chaitanya-asawa.md)
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

