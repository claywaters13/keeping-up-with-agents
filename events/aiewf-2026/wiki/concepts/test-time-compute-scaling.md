---
title: "test-time compute scaling"
type: "concept"
slug: "test-time-compute-scaling"
tier: "supporting"
maturity: "contested"
talk_count: 9
speaker_count: 11
---

# test-time compute scaling

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **9** talk(s) by **11** speaker(s)

**Definition:** Spending more compute at inference — longer reasoning, sampling, or search — to buy accuracy without changing weights.

*Also referred to as: test-time compute, inference-time scaling, pass@k, reasoning offloading, test-time compute training, deep research loops*

## State of Practice

The field has stopped treating test-time compute as a dial you turn and started treating it as a structure you build. Speakers converged on the finding that unstructured spend — a long 'here's the codebase, optimize it' prompt, a deeper research setting, more reasoning tokens — saturates, while the same token budget spent through explicit decomposition (linked component documents, recursive sub-agent calls, symbolic state on a file system, compaction loops) keeps buying accuracy; Lee Robinson's RLM framing and Sina Shahandeh's hierarchical hypothesis scaffold are two versions of the same claim, and Ross Taylor's compaction-plus-RL work is the training-side version. Everyone building production loops now assumes the loop will be reward-hacked: Uber's editing agent oversteers into generic outputs that differ in pixels but not quality, Will Brown locates hacking precisely at proxies undefined at the boundaries, and Pierluca D'Oro shows a blind replay agent matching frontier models on OSWorld — which makes pass@k on deterministic environments formally meaningless. The economics are now explicitly tiered rather than uniform: route hypothesis generation and critique to the strongest reasoning model, route routine work to the smallest model the latency budget allows, and treat scaffolding as a one-time cost in code versus reasoning as a cost paid every turn. The unresolved question is durability — whether harnesses are permanent architecture or, as Shahandeh argues by analogy to chain-of-thought on GPT-4, a transitional crutch that post-training will absorb.

## Consensus

### Unstructured test-time compute saturates; extending the scaling curve requires making decomposition an explicit, externalized step rather than asking the model to think longer.

Support: **4** talk(s)

> "that allows a very uh structured way to scale the test time compute to to generate more and more tokens on this problem"
>
> — [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [18:24](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=1104s)

Supporting talks: [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### Any loop that spends more inference compute against a proxy objective will be gamed by the system being scaled, so the verification layer — not the compute budget — is the real design problem.

Support: **4** talk(s)

> "reward hacking is when you have a kind of loose proxy for your objective that is undefined at the boundaries"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [6:20](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=380s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md)

### Inference compute should be tiered per sub-task rather than spent uniformly: strong reasoning models on the small number of steps that need judgment, the fastest/cheapest model everywhere else.

Support: **4** talk(s)

> "Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)

Supporting talks: [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### The context window is not the ceiling on test-time compute — externalizing state to files, indexes, and compaction lets a run process orders of magnitude more tokens than the model can hold.

Support: **4** talk(s)

> "the RLMs can process information that is many orders of magnitude larger than their context window, tens of millions of tokens"
>
> — [Recursive Coding Agents](../talks/recursive-coding-agents.md), [5:01](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=301s)

Supporting talks: [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)

## Disagreements

### Should the next increment of capability be bought by post-training the weights or by building the inference-time harness around them?

| Position A | Position B |
|---|---|
| Post-training is decisive: a state-of-the-art base model alone does not make a product, RL now dominates the compute budget, and supervised learning's job is reduced to laying down the atomic skills RL will later compose. Capability belongs in the weights, learned from environments built out of production traces.<br>*[Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* | The models are already intelligent enough; the bottleneck is orchestration and behavior. A 9B model run as an RLM beats frontier models run as plain LLMs, and a state machine plus a small model beats an unscaffolded reasoning model — so spend on the harness, not on training.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)* |

*Why it matters: It determines whether a team's differentiated IP is an RL environment and a training pipeline or an orchestration layer and skill library — and whether frontier model upgrades erase your moat or extend it.*

### Is prompt-level decomposition scaffolding permanent architecture, or a transitional crutch that post-training will absorb?

| Position A | Position B |
|---|---|
| Transitional. Hierarchical decomposition prompting is analogous to chain-of-thought on GPT-4-era models; as models are post-trained to compartmentalize and break down problems themselves, these tricks will be needed less. RL on sufficiently difficult environments lets the model learn the composition itself.<br>*[Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md)* | Permanent. Scaffolding is a cost paid once in code rather than on every turn, and the missing layer is how to specify, manage, reuse, and verify work — a layer that gets more valuable, not less, as models improve.<br>*[Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md)* |

*Why it matters: If scaffolding is transitional, elaborate harnesses are depreciating assets to be kept thin and swappable; if permanent, they deserve to be built as durable products with their own languages, dependency wiring, and golden-session capture.*

### Is pass@K a valid measure of what repeated test-time sampling buys you?

| Position A | Position B |
|---|---|
| Yes — pass@K is the right metric for a self-correcting loop, because the pass rate should rise with each QA feedback iteration, and gating task generation on measured pass rate is what makes iterative loops trainable and tunable.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* | No — on a static deterministic environment, pass@k is formally equivalent to measuring the success rate of a blind replay agent, so it rewards memorized action sequences rather than capability. Benchmarks must vary data, appearance, and initial state before repeated sampling means anything.<br>*[Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md)* |

*Why it matters: Every claim that 'more attempts buys accuracy' rests on this metric; if the environment is deterministic, the reported lift may be exploitable structure rather than reasoning, and deployment decisions get made on numbers with ~17-20% confidence-interval coverage.*

### When the task allows it, should you spend more inference time on deeper reasoning, or is depth usually not worth its cost?

| Position A | Position B |
|---|---|
| Spend it. Routing hypothesis generation and post-implementation critique to a stronger reasoning model produces much better improvements, and the emergence of reflective backtracking behavior came precisely from more RL compute and bigger context windows rather than a different objective.<br>*[Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* | Usually not worth it. Reasoning latency costs more than the answer quality it buys, the deepest research setting is rarely worth its token cost when light or fast suffices, and enhancing an already-good output is doubly bad — compute spent for zero lift plus degradation risk.<br>*[Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* |

*Why it matters: It sets the default for new systems: either start deep and trim, or start at the cheapest tier and escalate only on measured need — which drives both unit economics and whether a real-time product is feasible at all.*

## Practical Guidance

**Do:**

- Make decomposition a separate explicit action that emits a linked hierarchy of component documents over the codebase, then have the reasoning model propose improvements per component — this measurably widens the space of proposals beyond hyperparameter tweaks
- Route hypothesis generation and post-implementation critique to the strongest available reasoning model (e.g. via a CLI that packages code and data to a Pro-tier API) while keeping implementation on the cheaper agent
- Cap self-correcting edit loops at K iterations with an explicit 'take the coverage hit and never publish' branch, and track pass@K rather than pass@1
- Vary initial state, app theme, and underlying data across runs — varying initial state is rare in existing benchmarks and is the single most important missing property
- Extract a replay agent from your benchmark and check that it scores near zero; if a blind script matches the frontier model, the benchmark measures exploitable structure
- Compute confidence intervals that account for the benchmark's hierarchical structure (task/config/rollout), not from rollouts alone, and accept 'not confident enough to decide' as an output
- Judge in hindsight after seeing the full chain of events, or poll several models, rather than instructing a judge in advance to disallow a behavior
- Apply RL to the compaction step itself, not only to the task, and prefer value models over GRPO for long-horizon runs to cut gradient variance and enable bootstrapping
- Move control flow, state tracking, and answer selection into a state machine in application code so the model's only job is generating the response — target ~900ms first-token for voice
- Log every stage of the orchestration in a flat, human-readable JSON before attempting any optimization or self-learning loop
- Build tasks by working backwards from a known-reachable end state, or by planting answers in a learned simulator, so solvability is guaranteed and supervision is free
- Layer redundant QA gates (Swiss cheese) and reject rather than publish when the judge is not confident on a multimodal check
- Default to light or fast deep-research depth, with an index → executive summary → wiki derivative → raw source hierarchy so the agent reads the cheapest sufficient layer

**Avoid:**

- Don't rely on 'here's the codebase, here's the objective, optimize' — it saturates after a while regardless of how much compute you give it
- Don't use pass@k as a headline metric on a static deterministic environment; it is formally the same as scoring a blind replay agent
- Don't compute error bars from rollouts alone — empirical coverage lands around 17-20% against a nominal 95%, and overconfident intervals can cost hundreds of thousands of dollars a month at a million tasks
- Don't give agents tools to search prior trajectories or archives; they learn to retrieve previous answers instead of reasoning
- Don't assume more iterations means better output — agents oversteer into overly conservative generic results that differ in raw pixels while carrying no meaningful improvement
- Don't spend reasoning latency inside a real-time loop; a frontier model that thinks for a full second has already lost the conversation
- Don't run additional enhancement passes on already-high-quality outputs: you pay compute for zero lift and risk hallucinated artifacts
- Don't expect RL to install dense new knowledge — it refines existing skills, and the knowledge has to be there from supervised training
- Don't ship a statically tuned offline configuration; every component needs a mechanism to retune itself against online drift
- Don't stand up a vector DB, knowledge graph, or semantic search layer for a personal research memory when a markdown corpus with a reference index is more inspectable and more token-efficient

## Notable Outliers

- A blind replay agent that just replays recorded action sequences matches or beats the frontier model it was extracted from on OSWorld and MobileWorld. ([Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [0:59](https://www.youtube.com/watch?v=CTLa_p6iOiY&t=59s))
- Qwen 3.5 9B run as an RLM beats Opus and GPT-5.4 run as plain LLMs on the Long CoT benchmark — harness, not scale, decided the result. ([Recursive Coding Agents](../talks/recursive-coding-agents.md), [6:35](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=395s))
- Given $100K to trade Premier League football matches over a one-year horizon on Kelly Bench, every frontier model lost money. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s))
- A 1M-token context window is orders of magnitude short of genuinely long-horizon intellectual work, which needs tens to hundreds of billions of tokens. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [9:49](https://www.youtube.com/watch?v=2bvtay8wGYI&t=589s))
- No LLM today can reliably identify a lung nodule, because none are trained on scientific images — weak observation, not weak reasoning, is the barrier to autonomous science. ([Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [15:52](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=952s))
- Off-policy staleness of up to about eight steps is acceptable in pipeline RL before quality degrades — the explicit trade against GPU utilization. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [15:17](https://www.youtube.com/watch?v=2bvtay8wGYI&t=917s))

## All Talks

- [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md)
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
- [Will Brown](../speakers/will-brown.md)

