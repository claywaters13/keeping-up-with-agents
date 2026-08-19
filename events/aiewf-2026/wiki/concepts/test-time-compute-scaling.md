---
title: "test-time compute scaling"
type: "concept"
slug: "test-time-compute-scaling"
tier: "supporting"
maturity: "contested"
talk_count: 10
speaker_count: 12
---

# test-time compute scaling

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **10** talk(s) by **12** speaker(s)

**Definition:** Spending more compute at inference — longer reasoning, sampling, or search — to buy accuracy without changing weights.

*Also referred to as: test-time compute, inference-time scaling, pass@k, reasoning offloading, test-time compute training, deep research loops*

## State of Practice

The conference's working definition of test-time compute has shifted from "let the model think longer" to "spend inference budget through a structure the model itself controls." Speakers repeatedly reported that unstructured scaling — a Karpathy-style "here's the codebase, here's the objective, optimize" loop — saturates at a fixed performance ceiling on open-ended long-horizon work, while the same underlying model keeps improving when decomposition, compaction, or recursion is made an explicit action (Radicait's linked component-document hierarchy, OpenProse's RLMs, General Reasoning's generate-summarize-continue loop). The practical corollary is that harness quality substitutes for parameter count: Qwen 3.5 9B run as an RLM was reported to beat Opus and GPT-5.4 run as plain LLMs on long-CoT tasks, LangChain matches Opus-level trace judging at one to two orders of magnitude lower cost on open models, and Microsoft's voice team hit 900ms first-token by moving all control flow into a state machine and leaving the model only the talking. Cost discipline is now explicit rather than assumed: latency budgets (950ms for voice), token budgets (light/fast deep-research settings), and zero-lift passes (re-enhancing an already-good image) are treated as reasons to spend less, not more. Every team scaling iteration count also reported reward hacking — agents oversteering into generic outputs to clear a QA gate, or retrieving prior answers instead of reasoning — so verification gates and hindsight judging are treated as a mandatory part of the loop rather than an add-on. The measurement layer is under active attack: on deterministic environments, pass@k was shown to be formally equivalent to the success rate of a blind replay agent, and confidence intervals from rollouts alone achieve 17-20% empirical coverage against a nominal 95%.

## Consensus

### Unstructured test-time scaling saturates; the gains come from imposing an explicit structure — decomposition, compaction, recursion — on how the inference budget is spent.

Support: **4** talk(s)

> "before if I just say say here's our code base and here's my objective Google optimized this process similar to what originally Carpathy's readme file in this program MD it would not it would not generate it would saturate after a while"
>
> — [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [9:55](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=595s)

Supporting talks: [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### A small or open model inside a strong harness matches or beats a frontier model run bare, at one to two orders of magnitude lower cost.

Support: **3** talk(s)

> "Qwen 3.59B as an RLM can beat Opus and um and GPT-5.4, all the top frontier models as LLMs on these long reasoning tasks"
>
> — [Recursive Coding Agents](../talks/recursive-coding-agents.md), [6:35](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=395s)

Supporting talks: [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

### Iterating at inference against a score or gate produces reward hacking, so extra passes must be paired with verification — ideally judged in hindsight rather than by instructing a judge in advance.

Support: **4** talk(s)

> "reward hacking is when you have a kind of loose proxy for your objective that is undefined at the boundaries"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [6:20](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=380s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)

### The binding constraint on long-horizon inference is not context window size but context management — treating context as an external object the agent queries lets a system process orders of magnitude more tokens than its window.

Support: **4** talk(s)

> "we don't need necessarily to provide more and more and more context for a better research. You need a proper memory and context management"
>
> — [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [8:36](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=516s)

Supporting talks: [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)

### Expensive reasoning should be routed to the specific step that pays for it rather than applied uniformly across the pipeline.

Support: **4** talk(s)

> "And like practically speaking, honestly, yes, we start with Opus, we start with 55 because we just want to know if the task is even possible."
>
> — [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [7:50](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=470s)

Supporting talks: [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Disagreements

### When an agent saturates on a task, should the marginal dollar go into inference-time scaffolding or into training the weights?

| Position A | Position B |
|---|---|
| Spend it on the harness: orchestration and behavior are the bottleneck, not intelligence. Harness engineering has a roughly two-minute feedback loop, most teams never need to go further, and an explicit decomposition scaffold widens the improvement space with no weight changes.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)* | Spend it on RL: a state-of-the-art base model is not enough to make a useful product, RL post-training is the decisive ingredient, and supervised pre-training's job is now merely to build representations that RL composes over a sufficiently difficult environment.<br>*[Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* |

*Why it matters: It decides whether a team builds an environment/RL stack with GPU clusters and value models, or a prompt-and-orchestration layer they can iterate on in minutes. The two paths have wildly different capital requirements and different failure modes when the underlying model is upgraded.*

### Should more reasoning at inference be the default, with cost accepted as the price of accuracy?

| Position A | Position B |
|---|---|
| Yes — scale it deliberately. Route hypothesis generation and critique to a stronger reasoning model, generate tokens until the window ends and then compact and continue, and treat structured token generation as the mechanism that keeps the loop improving on open-ended problems.<br>*[Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* | No — budget it, and remove it where it does not pay. A frontier model that thinks for a full second has already lost a voice conversation; control flow belongs in a state machine paid for once in code; the deepest deep-research setting is rarely worth its token cost; and an extra enhancement pass on an already-good input costs compute for zero lift while risking degradation.<br>*[Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* |

*Why it matters: The answer sets the default architecture for real-time and high-volume products: either a reasoning model in the hot path, or a small fast model wrapped in deterministic code with reasoning reserved for offline or escalated steps.*

### Is inference-time scaffolding a durable engineering layer or a temporary crutch that post-training will absorb?

| Position A | Position B |
|---|---|
| Temporary. Hierarchical decomposition prompting is analogous to chain-of-thought on GPT-4-era models and will be needed less as models are post-trained to decompose problems themselves; base models are already being redesigned as priors for reasoning and agentic behavior.<br>*[Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md)* | Durable. Orchestration is the next step rather than raw intelligence, harnesses must evolve over time alongside models and tasks, and scaffolding is the better investment precisely because it is paid once in code rather than on every turn.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)* |

*Why it matters: If scaffolding is temporary, elaborate harness code is technical debt that each model release erases; if durable, the harness is the product and deserves the same versioning, evals, and reuse discipline as any other system component.*

## Practical Guidance

**Do:**

- Make decomposition a separate explicit action — have the coding agent generate a linked hierarchy of component documents over the codebase before asking it to propose improvements.
- Require that the model, not a hardcoded map-reduce pipeline, chooses how to decompose the problem; keep the intermediate state symbolic (files) so it can exceed the context window.
- Start on a frontier model only to establish that the task is possible, then use its traces to port the workload to a cheaper open model.
- Extract control flow, state tracking, and answer selection into application code (a state machine) and pick the fastest model your latency budget allows — roughly 950ms to first speech for voice.
- Compact at the context boundary — generate to the end of the window, summarize, continue — and apply RL to the compaction step itself, not just the task.
- Judge in hindsight, after seeing the full chain of events, or by polling several models; telling a judge in advance not to allow a behavior does not prevent it in the rollout.
- Track pass@K across iterations of a self-correcting edit loop, with an explicit K after which you take a coverage hit instead of publishing.
- Vary data, appearance, and initial state across runs, and compute confidence intervals that account for the benchmark's hierarchical structure — rollout-only intervals give 17-20% coverage against a nominal 95%.
- Route the hypothesis-generation and post-implementation critique steps to a stronger reasoning model (e.g. packaging code and data out to a Pro-tier API) while leaving routine implementation on the cheap model.
- Calibrate generated tasks to intermediate difficulty and gate on pass rate — too-easy and too-hard tasks give no separation across rollouts.

**Avoid:**

- "Here's the codebase, here's the objective, optimize" prompts on open-ended work — they plateau, and the agent proposes hyperparameter tweaks rather than architectural changes like 2.5D to 3D convolutions.
- Reporting pass@k on a static deterministic environment: it is formally equivalent to measuring a blind replay agent, which already matches or beats the frontier model it was extracted from.
- Spending reasoning tokens on turns where latency is the binding constraint — a one-second pause reads to a user as a dead conversation.
- Running extra enhancement passes on inputs that are already good enough: you pay compute for zero quality lift and risk the model hallucinating detail to match the prompt.
- Accepting outputs that clear a QA gate by oversteering into conservative generic results that differ in raw pixels but carry no meaningful improvement.
- Giving agents tools that search prior trajectories or archives — it teaches retrieval of previous answers instead of reasoning.
- Append-only memory files with search over them as the long-term substrate; entries must be updated and compressed to survive multi-year horizons.
- Letting the LLM write into your hand-authored source notes; keep generated content in a separate derivative layer.
- Assuming more inference compute compensates for weak perception — no current LLM reliably identifies a small scientific feature such as a lung nodule, because it was never trained on that data.
- Publishing when the judge is not confident on a multimodal check; reject instead, and keep redundant overlapping gates even though they cost extra passes.

## Notable Outliers

- Pass@k evaluated on a deterministic environment is formally equivalent to measuring the success rate of a blind replay agent — so a benchmark is only adequately de-gamed if a replay agent extracted from it scores near zero. ([Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [1:48](https://www.youtube.com/watch?v=CTLa_p6iOiY&t=108s))
- An unmodified default RLM harness performs like a top-10 purpose-built memory system, against which billions of dollars of custom memory engineering are being spent. ([Recursive Coding Agents](../talks/recursive-coding-agents.md), [5:01](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=301s))
- Given $100K to trade Premier League matches over a one-year horizon, every frontier model lost money — evidence that inference scaling does not transfer to open-ended multi-agent environments. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s))
- A 1M-token context window is orders of magnitude short of genuinely long-horizon intellectual work, which needs tens to hundreds of billions of tokens. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [9:49](https://www.youtube.com/watch?v=2bvtay8wGYI&t=589s))
- Overconfident confidence intervals from rollout-only statistics can cause a deployment decision that costs hundreds of thousands of dollars per month at one million tasks with a 4% true performance gap. ([Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [13:49](https://www.youtube.com/watch?v=CTLa_p6iOiY&t=829s))
- Hierarchical decomposition prompting is a temporary scaffold analogous to chain-of-thought on GPT-4-era models, and will be needed less as models are post-trained to decompose problems themselves. ([Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [18:24](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=1104s))
- For voice agents the budget was never IQ, it was milliseconds — a frontier model that thinks for a full second has lost the room regardless of answer quality. ([Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [0:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=51s))

## All Talks

- [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)
- [The Base Model Is Dead](../talks/the-base-model-is-dead.md)
- [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Chengxi Taylor](../speakers/chengxi-taylor.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Paul Iusztin](../speakers/paul-iusztin.md)
- [Pierluca D'Oro](../speakers/pierluca-d-oro.md)
- [Ross Taylor](../speakers/ross-taylor.md)
- [Sina Shahandeh](../speakers/sina-shahandeh.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Will Brown](../speakers/will-brown.md)

