---
title: "catastrophic forgetting"
type: "concept"
slug: "catastrophic-forgetting"
tier: "supporting"
maturity: "contested"
talk_count: 12
speaker_count: 12
---

# catastrophic forgetting

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **12** talk(s) by **12** speaker(s)

**Definition:** Loss of prior capability when a model is updated on new data, and the stability–plasticity tradeoff that governs it.

*Also referred to as: stability-plasticity tradeoff, capability decay, model collapse, capability drift, capability regression across model versions, complementary learning systems, mode collapse*

## State of Practice

Nobody at this conference treats forgetting as a solved or exotic problem: it showed up as the default outcome of every narrow update, from SFT on correctly-formatted traces degrading general coding-agent performance, to biomedically fine-tuned models underperforming their own general-purpose base models, to a frontier checkpoint (Opus 4.8) regressing sharply on Vending-Bench after a business-skills component was dropped from its post-training recipe. The organizing frame is the stability–plasticity tradeoff, with Asawa arguing most continual-learning failures land on one side of it and Su framing the reconciliation of stable-and-resistant vs. plastic-and-eager systems as the open problem. Practitioners have converged on three concrete mitigations rather than one: keep the mid-training mix mostly representative of the pre-training distribution when domain-adapting; narrow what the update is allowed to touch (LoRA, judge-masked teacher tokens, distilling only the step or few steps after an injected hint, since KL signal decays with distance); and make no-regression a constraint inside the optimization objective rather than a post-hoc check. The loudest structural move is to sidestep weights entirely — memory layers, harness edits, precomputed per-user context, and context-window anchoring all avoid forgetting by construction, and on Continual Learning Bench 1.0 vanilla in-context learning topped the leaderboard over more expensive context-management systems. What is unresolved is whether that sidestep is the answer or an evasion: Asawa calls building continual learning on frozen checkpoints a sunk cost fallacy, and Su argues both parametric and non-parametric learning are required.

## Consensus

### Training a model on a narrow new behavior degrades unrelated prior capabilities unless the update is deliberately constrained (data mix, masked tokens, or bounded parameters).

Support: **4** talk(s)

> "even doing SFT on traces where we knew the hyperlink was correctly formatted, we saw that there was this sort of degradation in overall coding agent performance"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [14:35](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=875s)

Supporting talks: [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)

### Adaptation increasingly happens outside model weights — in memory, harness, prompt, or precomputed context layers — where forgetting is avoided by construction and changes stay inspectable and reversible.

Support: **4** talk(s)

> "The first one is agent continual learning is not necessarily model fine-tuning. The updates and many useful updates can happen in the harness and memory layer."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)

### Preventing regression has to be designed into the update mechanism itself — the data mix, the token mask, the optimization constraint — not run as a check after the update lands.

Support: **3** talk(s)

> "A better approach is a regression aware learning where the regression is not be treated as a post-hoc approach, but as a mechanism within the optimization itself."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [13:19](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=799s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)

### The stability–plasticity tradeoff is the right taxonomy for continual-learning failures: models are not natively equipped to hold both, so systems must supply the balance externally.

Support: **3** talk(s)

> "I'm going to argue that most failure modes in continual learning fall on one side of the stability plasticity trade-off."
>
> — [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:50](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=890s)

Supporting talks: [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)

### A newer or specialized checkpoint cannot be assumed to retain the capabilities of the model it replaces; capability loss between versions is real and must be measured, not inferred.

Support: **3** talk(s)

> "One thing that really surprised us when we ran Opus 4.8 was that it was much much worse."
>
> — [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [2:07](https://www.youtube.com/watch?v=cO8qC6HBuBg&t=127s)

Supporting talks: [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)

## Disagreements

### Should continual learning be pushed into model weights, or kept in non-parametric layers precisely because weights forget?

| Position A | Position B |
|---|---|
| Keep updates out of the weights. Fine-tuning layers a thin new signal over vast prior sediment in ways that are no longer auditable and that measurably degrade the base model; memory, harness, prompt, and precomputed-context layers are cheaper, reversible, and cannot catastrophically forget.<br>*[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)* | Non-parametric methods are a ceiling, not a solution. Weight-level learning is required — either co-designed from scratch (architecture, data, and algorithm together) or delivered today via targeted distillation and mid-training — and building only on frozen checkpoints is a sunk cost fallacy.<br>*[Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)* |

*Why it matters: It decides whether teams invest in memory/context infrastructure on top of an API model or in a training stack with replay data and regression suites. It also decides who owns the fix when an agent forgets: the application team or the model team.*

### Is catastrophic forgetting a tractable engineering problem on today's models, or an artifact of models that were never designed to learn continually?

| Position A | Position B |
|---|---|
| Tractable now. Keeping most of the mid-training mix representative of the pre-training distribution prevents forgetting entirely; judge-masked distillation acquires out-of-distribution behavior while cutting degradation; regression-constrained optimization raised a support agent from 78% to 97% without breaking what worked.<br>*[Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* | Structural. These checkpoints were never built to be continual learners, no monolithic model can compress millions of heterogeneous microworlds into one static representation, and mitigations bolted onto a frozen checkpoint buy margin rather than capability.<br>*[Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)* |

*Why it matters: If it is tractable, forgetting is a data-and-objective hygiene problem you staff today. If it is structural, current mitigation work is a local optimum and the binding constraint is a new training regime — which changes what a continual-learning roadmap is even aiming at.*

### Do you need a replayable, evaluator-backed environment before you can safely update an agent?

| Position A | Position B |
|---|---|
| Yes. Production logs are not learning environments; a log plus feedback is one instance with no way to verify a fix, so trace-to-harness edits are vibe-based and can plant hidden regressions. Lift logs into simulations with deterministic evaluators and deliberate regression traps first, and measure gain against a stateless baseline so you know learning actually happened.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)* | No. Replayability of the production environment is not required — a one-time batch of offline production traces plus offline hints already delivers targeted behavior change (SWE-bench task-complete rate 22% to 60%) with base task performance holding steady.<br>*[Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)* |

*Why it matters: Environment construction is the expensive prerequisite in the whole pipeline. If offline traces suffice, enterprises can start improving agents on day one; if they do not, every unverified memory write or harness edit is an untracked regression risk accumulating in production.*

## Practical Guidance

**Do:**

- When domain-adapting, keep the majority of the mid-training mix representative of the original pre-training distribution — this reportedly prevents catastrophic forgetting outright while still capturing the domain gain
- Restrict distillation to the step immediately after an injected hint, or a few steps out, because the KL learning signal decays with distance from the hint and distilling the whole rollout imports teacher idiosyncrasies
- Use an LLM judge to mask which teacher tokens the student actually learns from, filtering the teacher's irrelevant connector-word preferences out of the update
- Encode no-regression on accumulated past learning environments as a constraint inside the optimization objective, and keep its cost sub-linear in the number of environments so it stays feasible as they pile up
- Make the smallest durable change at the cheapest sufficient layer — memory, then prompt/harness, then weights — rather than defaulting to the layer you own
- Use LoRA when weights must change, to bound the number of parameters the update can move
- Report gain (stateful reward minus stateless reward) alongside cumulative reward, so base-model strength is not mistaken for retained learning
- Build regression traps into your eval suite deliberately, and re-run the whole gate on every base-model version bump rather than trusting a newer checkpoint of the same family
- Prefer online, per-rollout hints chosen by a judge over a fixed hint applied uniformly — ~15% to ~80% correct formatting versus a small climb, at similar risk

**Avoid:**

- Reward-shaping for an output format, or SFT on correctly-formatted traces, as a way to teach an out-of-distribution behavior — both degraded general coding-agent performance in practice
- Treating regression checks as a post-hoc step after the update has already been chosen
- Shipping unverified memory-layer writes: it is the cheapest and fastest layer to change, which is exactly why its efficacy and regression risk usually go unmeasured
- Trace-to-harness edits where a coding agent reads a log and rewrites the agent — the change is untestable, so hidden regressions land silently
- Fine-tuning a persona or specialty into base weights when a context window would do; specialized fine-tunes underperformed their general-purpose base models on physician-reviewed tasks
- Training on AI-generated images — synthetic data is sticky enough to permanently imprint a recognizable ChatGPT/Nano Banana aesthetic on the model
- Filtering a corpus with off-the-shelf aesthetic or image-quality scores, which silently deletes stylistic coverage you will not get back
- Chaining independent benchmark instances together and calling it a continual-learning eval — with no shared latent structure there is nothing for the model to carry forward

## Notable Outliers

- Opus 4.8 scored much worse than Opus 4.7 on Vending-Bench because Anthropic removed a business-skills component from the post-training recipe — capability loss between adjacent frontier checkpoints, confirmed by the lab. ([Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [2:43](https://www.youtube.com/watch?v=cO8qC6HBuBg&t=163s))
- In a 2026 Nature Medicine study across 12 clinics, biomedically fine-tuned models underperformed their own general-purpose base models on physician-reviewed tasks, attributed to catastrophic forgetting. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [29:05](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1745s))
- Domain adaptation need not cost general capability at all: keeping most of the mid-training mix representative of the pre-training distribution prevents catastrophic forgetting entirely, and the better domain data makes an unchanged post-training harness 2–3x more effective. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [14:57](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=897s))
- Building continual-learning methods on top of already-trained frozen checkpoints is a sunk cost fallacy — the models were never designed to be continual learners, and if continual learning were a first-order requirement the multi-stage training stack could collapse into one learning phase followed by deployment. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [17:37](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1057s))
- On Continual Learning Bench 1.0 vanilla in-context learning beat more sophisticated context-management systems on reward and held across the reward-vs-cost and gain-vs-cost Pareto frontiers — though the speaker calls it an artifact of medium-horizon tasks, not the end state. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s))
- A teacher can shift a student toward calling a tool purely by reshaping the reasoning path, never touching the tool-call tokens — targeted behavior change with the blast radius kept off the behavior itself. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s))
- Synthetic data is 'so sticky' that once you train on AI-generated images the aesthetic is permanently imprinted — a trained observer can identify a model distilled on ChatGPT or Nano Banana Pro outputs. ([Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [7:27](https://www.youtube.com/watch?v=-tviRdpmHvs&t=447s))

## All Talks

- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Ending AI Slop](../talks/ending-ai-slop.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)
- [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)

## Speakers

- [Alex Volkov](../speakers/alex-volkov.md)
- [Ari Morcos](../speakers/ari-morcos.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Lukas Petersson](../speakers/lukas-petersson.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Parth Asawa](../speakers/parth-asawa.md)
- [Samuel Denton](../speakers/samuel-denton.md)
- [Sangwu Lee](../speakers/sangwu-lee.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yu Su](../speakers/yu-su.md)

