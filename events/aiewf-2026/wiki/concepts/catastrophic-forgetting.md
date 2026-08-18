---
title: "catastrophic forgetting"
type: "concept"
slug: "catastrophic-forgetting"
tier: "supporting"
maturity: "contested"
talk_count: 10
speaker_count: 10
---

# catastrophic forgetting

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **10** talk(s) by **10** speaker(s)

**Definition:** Loss of prior capability when a model is updated on new data, and the stability–plasticity tradeoff that governs it.

*Also referred to as: stability-plasticity tradeoff, capability decay, model collapse, capability drift, capability regression across model versions, complementary learning systems, mode collapse*

## State of Practice

Catastrophic forgetting has moved from a training-time curiosity to a production operations problem, and it is now argued at four distinct layers: weights, harness/prompt, memory, and data mixture. The empirical anchors cited most often are concrete regressions in shipped systems — Opus 4.8 scoring far worse than 4.7 on Vending-Bench after Anthropic removed a business-skills component from its post-training recipe, and a 2026 Nature Medicine result in which biomedically fine-tuned models underperformed their own general-purpose base models. Practitioners consistently frame failures on the stability–plasticity axis, and the sharpest methodological claim of the conference is that regression prevention belongs inside the optimization objective as a constraint (fix recent failures subject to no regression on accumulated past environments) rather than as a post-hoc check, with the added constraint that the check cannot scale linearly in the number of past environments. Mitigation splits cleanly: data-side prevention (keep most of a mid-training mix representative of the pre-training distribution, which Datology claims eliminates domain-adaptation forgetting entirely) versus architecture-side avoidance (never touch weights — put durable changes in memory, harness, and precomputed context, where they stay auditable, versionable, and reversible). What is uncontested is that forgetting is undetectable without a replayable environment plus deterministic evaluators that outlive any single update; production logs, anecdotes, and self-grading loops are all explicitly ruled out as evidence.

## Consensus

### Updating a model or agent to fix new failures routinely destroys previously working capability, so silent regression is the expected outcome of an update rather than an edge case.

Support: **4** talk(s)

> "What uh might have been working previously, but with these changes might not work properly, and create some hidden regressions."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [8:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=536s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)

### You cannot detect forgetting without a standing, replayable evaluation artifact that outlives any individual update — production logs, real-world anecdotes, and the updating process itself cannot prove that nothing broke.

Support: **5** talk(s)

> "This is verifiable continual learning in practice, where each update is tested, every gain is measured, and nothing that already works breaks during this optimization."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [20:46](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1246s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)

### A large share of durable improvement can and should be made outside the weights — in memory, harness, and precomputed context — precisely because those layers are inspectable and reversible when an update goes wrong.

Support: **3** talk(s)

> "The first one is agent continual learning is not necessarily model fine-tuning. The updates and many useful updates can happen in the harness and memory layer."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)

### Stability versus plasticity is the correct organizing frame: nearly every continual-learning failure is a system either refusing to absorb new experience or absorbing it at the cost of what it already knew.

Support: **3** talk(s)

> "I'm going to argue that most failure modes in continual learning fall on one side of the stability plasticity trade-off."
>
> — [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:50](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=890s)

Supporting talks: [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)

## Disagreements

### Should continual learning — and therefore the fight against forgetting — happen in the model weights, or in the scaffolding around a frozen model?

| Position A | Position B |
|---|---|
| In the weights. Bolting continual-learning methods onto an already-trained frozen checkpoint is a sunk cost fallacy; the fix is parametric, co-designing architecture, data, and algorithm, and curating the training/mid-training mix so specialization does not cost general capability. Non-parametric context tricks are at best a stopgap and at worst only marginal gains.<br>*[Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)* | Around the weights. Weight updates are the most expensive and least auditable layer and demonstrably degrade base capability; make the smallest durable change at the cheapest layer (memory, then prompt/harness), anchor knowledge in the context window where provenance survives, and precompute structured context per user offline.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)* |

*Why it matters: It determines whether a team's forgetting budget is spent on data-mixture engineering and training runs or on eval harnesses, memory schemas, and retrieval infrastructure — and whether a specialized model is a fine-tune or a general model plus a curated corpus.*

### Is catastrophic forgetting already a solved engineering problem, or the open research frontier?

| Position A | Position B |
|---|---|
| Solved, at least for domain adaptation: keeping most of the mid-training mix representative of the pre-training distribution prevents catastrophic forgetting entirely, and better domain data makes an unchanged post-training harness 2–3x more effective. The remaining work is curation, not new algorithms.<br>*[Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)* | Unsolved and frontier: models were never designed to be continual learners, regression-aware continual improvement is explicitly named as the research frontier, fine-tuned specialist models still lose to their own base models, and a frontier lab itself shipped a version that lost a whole skill class.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)* |

*Why it matters: If forgetting is a data-mixture problem, a team buys its way out with curation and can safely fine-tune; if it is unsolved, every weight update needs a regression harness and an escape hatch, and specialization should be avoided until one exists.*

### Can automated evaluators certify that an update forgot nothing, or does that certification require a human expert in the loop?

| Position A | Position B |
|---|---|
| Automated: deterministic evaluators plus regression traps built into generated learning environments are sufficient to prove each fix helps and breaks nothing, and the whole point of a benchmark is to remove humans from the verification loop so the optimization can run.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)* | Human required: automated metrics structurally cannot adjudicate fidelity, LLM-as-judge is reward-hackable and worse than human judgment, a builder that grades itself hides the review rather than removing it, and code should not ship unless a human can defend it.<br>*[The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)* |

*Why it matters: It sets whether continual improvement can run unattended at production cadence or is throttled to the rate at which an expert can gate releases, and it decides where the headcount and cost of a learning loop actually land.*

## Practical Guidance

**Do:**

- When domain-adapting, keep most of the mid-training mix representative of the pre-training distribution rather than saturating it with domain data — this is claimed to prevent catastrophic forgetting entirely while still making post-training 2–3x more effective.
- Express the update as a constrained optimization: fix the recent failures subject to no regression on the accumulated past learning environments, with the regression term inside the objective rather than as a post-hoc gate.
- Convert production logs plus feedback into replayable learning environments with deterministic evaluators before applying any fix, and deliberately seed regression traps into the benchmark.
- Make the smallest durable change at the cheapest layer — memory first, then prompt/harness, then weights — and if weights must change, use LoRA to bound the number of parameters that can move.
- Report gain (stateful reward minus stateless reward) alongside cumulative reward, so retained learning is separated from base model capability.
- Keep a long-horizon behavioral eval running across vendor model versions so a silently dropped skill (e.g. business skills removed from a post-training recipe) surfaces as a score drop instead of a production incident.
- Prefer context-window anchoring over fine-tuning when the goal is fidelity to a specific corpus, so provenance is preserved and the configuration stays versionable and revertible.
- Repeat high-quality data rather than adding low-quality data, up to some threshold.
- Encode a caught mistake into documentation, linters, and reviewers rather than trusting review to catch the same class of mistake again.

**Avoid:**

- Trace-to-harness edits where a coding agent reads a log and rewrites the agent — the change is untestable even on the sample that motivated it, and introduces hidden regressions.
- Regression checks whose cost scales linearly (or worse) with the number of accumulated past learning environments; they become infeasible as the environment set grows.
- Fine-tuning a specialist and assuming it beats its general-purpose base — in the 2026 Nature Medicine study the biomedically fine-tuned models underperformed their own base models.
- Unverified memory-layer writes: they are the cheapest and fastest update path and therefore the one most often shipped with no efficacy or regression evidence at all.
- Chaining independent benchmark instances together and calling it a continual-learning benchmark — without shared latent structure there is nothing to retain or forget.
- Letting the same agent write the code and write/grade its own tests; self-scoring hides the review rather than eliminating it.
- Treating a longer context window or a bigger prompt as a substitute for a structured, precomputed model of the user.
- Assuming time-locked or period-anchored training removes contamination — it relocates the contamination to an earlier textual moment rather than removing it.

## Notable Outliers

- Opus 4.8 performed much worse than Opus 4.7 on Vending-Bench because Anthropic removed a business-skills component from its post-training recipe — a frontier lab shipping a documented capability regression across a point release. ([Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [2:43](https://www.youtube.com/watch?v=cO8qC6HBuBg&t=163s))
- In a 2026 Nature Medicine study across 12 clinics, general-purpose frontier models beat dedicated clinical tools, and biomedically fine-tuned models underperformed their own general-purpose base models due to catastrophic forgetting. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [29:05](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1745s))
- Building continual-learning methods on top of already-trained frozen checkpoints is a sunk cost fallacy; if continual learning were a first-order design requirement, the whole multi-stage training stack could collapse into a single learning phase followed by deployment. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [17:37](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1057s))
- Vanilla in-context learning topped the Continual Learning Bench 1.0 leaderboard on reward and held across both the reward-vs-cost and gain-vs-cost Pareto frontiers, beating far more expensive context-management systems. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s))
- Past a threshold of raw intelligence, further intelligence gains stop mattering and the continual-learning algorithm becomes the binding constraint — current frontier models may already be smart enough. ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s))
- Fine-tuning suppresses random distortion at the surface while amplifying it underneath, layering a thin personal signal over cultural sediment in the base weights in a way that is no longer open to audit. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [28:10](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1690s))
- Curating only the English portion of a corpus measurably improves non-English performance, with transfer magnitude correlated to language similarity — capability moves across the distribution rather than being partitioned by it. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [11:34](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=694s))

## All Talks

- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Ending AI Slop](../talks/ending-ai-slop.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)

## Speakers

- [Alex Volkov](../speakers/alex-volkov.md)
- [Ari Morcos](../speakers/ari-morcos.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Lukas Petersson](../speakers/lukas-petersson.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Parth Asawa](../speakers/parth-asawa.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yu Su](../speakers/yu-su.md)

