---
title: "continual learning"
type: "concept"
slug: "continual-learning"
tier: "core"
maturity: "frontier"
talk_count: 18
speaker_count: 24
---

# continual learning

**Maturity: FRONTIER** — Frontier — too new or sparse for consensus yet

*Core concept* &middot; discussed across **18** talk(s) by **24** speaker(s)

**Definition:** Systems that keep improving after deployment by incorporating new experience — through weights, memory, or artifacts — rather than being frozen at training time.

*Also referred to as: continual learning for agents, continual learning from traces, continual learning loops, last mile learning, harness learning, compounding learning loops, parametric vs non-parametric learning*

## State of Practice

Continual learning was the conference's most-attended open problem and its least-settled one — Jack Morris noted it does not yet have an agreed name (sleep-time compute, neural memory, write-time compute, machine studying), which is itself evidence of how early the paradigm is. Practitioners converged on one substrate: production traces, not curated benchmarks, are the raw material, because real tasks lack golden answers, verifiable rewards, and replayable environments. Where they split is what to do with those traces — RELAI and Prime Intellect argue you must first lift logs into replayable learning environments with explicit evaluators, while Applied Compute and Trajectory built methods (offline/online hinting, on-policy self-distillation) specifically to avoid that requirement, since GRPO's demand for many parallel rollouts per prompt is unsatisfiable in a live customer-support chat. The layer question is equally open: Shlok Khemani argues continual learning already ships today as ChatGPT's ~4,000-token profile and Claude's ~1,000-token profile updated on a loop, while Parth Asawa calls building on frozen checkpoints a sunk-cost fallacy and Ronak Malde calls the current state 'pseudo continual learning' — offline batch updates and model re-uploads. Nearly everyone agreed the binding constraint has moved off raw model intelligence: Yu Su's framing (intelligence and expertise are largely orthogonal; past a threshold, the continual-learning algorithm sets the slope) was echoed in different vocabulary by the context-layer, DSPy, and post-training talks. The consistently reported failure mode is regression — every team that shipped a working loop reported that acquiring a new behavior degraded old ones unless regression was built into the objective rather than checked afterward.

## Consensus

### Deployed production traces, not handcrafted benchmarks, are the source material for continual learning — which makes tracing/observability a prerequisite rather than an adjunct.

Support: **7** talk(s)

> "what we found is super helpful is taking existing traces from a deployed agent and treating these as the source material"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [9:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=581s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)

### Methods that assume a golden answer, an explicit rubric, or a verifiable reward do not survive contact with production; the hard and valuable cases are the non-verifiable ones.

Support: **4** talk(s)

> "a lot of distillation work is done assuming you have some kind of golden answer that you can distill into the model. And this is often not the case."
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [9:47](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=587s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)

### Continual learning is not synonymous with weight updates — memory, prompt, and harness layers carry most of today's useful updates, and the cheapest sufficient layer should be tried first.

Support: **5** talk(s)

> "The first one is agent continual learning is not necessarily model fine-tuning. The updates and many useful updates can happen in the harness and memory layer."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)

### Raw model intelligence is no longer the binding constraint on real-world usefulness; situated, accumulated context/expertise is, and it cannot be obtained by scaling pre-training.

Support: **5** talk(s)

> "Once the raw intelligence has across a certain threshold, we don't need a stronger intelligence anymore"
>
> — [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s)

Supporting talks: [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)

### Regression — new learning silently breaking previously working behavior — is the defining failure mode, and it must be handled inside the update mechanism rather than as a post-hoc check.

Support: **5** talk(s)

> "the goal is to improve an agent from its his own experience where every fix is proven to help and proven to break nothing that already worked"
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [11:01](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=661s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)

### A log plus a thumbs-down is not a training signal — some graded, rerunnable structure with an explicit success definition has to be constructed before any change can be shown to help.

Support: **5** talk(s)

> "So, the second takeaway is production logs are not learning environments."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)

## Disagreements

### Does continual learning require a replayable environment, or can you learn durably from single, non-replayable production traces?

| Position A | Position B |
|---|---|
| You must lift logs into replayable learning environments with simulators and deterministic evaluators before any update; without replay you cannot verify the fix or detect regressions, and learned simulators are actually preferable to the real production system because full back-end control lets you plant answers and guarantee solvability.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* | Replayability is the wrong requirement — it forces environments to be one-to-one copies of reality and injects bias. Train inside the customer's actual black-box harness with only a completion endpoint, accept off-policy non-replayable data, and use teacher hints or on-policy self-distillation to extract signal from a parallelism of one.<br>*[Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)* |

*Why it matters: This decides whether enterprises must fund environment/simulator construction before seeing any improvement, or can hand over a trace dump on day one — and it determines whether GRPO-family RL is usable at all in production settings like support chat.*

### Can continual learning be built on top of today's frozen checkpoints, or does it require co-designing architecture, data, and training?

| Position A | Position B |
|---|---|
| It already works on top of existing models: a running-profile loop outside the weights is continual learning that is deployed today, harness engineering has a ~two-minute feedback loop and satisfies most teams, and a single learning-environment generation plus one optimization loop moved a support agent from 78% to 97%.<br>*[Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)* | Bolting methods onto checkpoints never designed to be continual learners is a sunk-cost fallacy. Real continual learning needs parametric change — markdown memory is a stopgap that becomes context-inefficient, non-parametric approaches alone provably plateau, and the multi-stage training stack should collapse into one learning phase followed by deployment.<br>*[Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)* |

*Why it matters: It sets where a team should spend the next year — context/memory infrastructure and eval loops, or training infrastructure and weight-update pipelines — and whether the current generation of agent memory products is a foundation or a bridge.*

### Is continual learning already shipping in production, or is nothing deployed today actually continual learning?

| Position A | Position B |
|---|---|
| It is here now: ChatGPT and Claude both run profile-update loops on a fixed cadence, enterprises get measurable improvement from offline trace batches today, and verified per-fix optimization loops are running against real support agents.<br>*[Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* | Nobody is close. What exists is pseudo continual learning — offline batch updates and model re-uploads — merging ~10,000 concurrent production rollouts into one update is unsolved, current evaluation is memoryless and does not measure learning at all, and the industry has not determined the right approach.<br>*[Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md)* |

*Why it matters: Whether you treat this as a buildable feature or an open research bet determines roadmap timing, and it changes how much credence to give vendor claims of 'continual learning' shipping today.*

### Do engineered memory and context-management systems beat plain accumulation of experience in context?

| Position A | Position B |
|---|---|
| Vanilla in-context learning topped Continual Learning Bench 1.0 on reward and held across the reward-vs-cost and gain-vs-cost Pareto frontiers, beating more expensive context-management systems on tasks requiring real learning.<br>*[Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)* | Naive accumulation does not scale: append-only memory files with search will fail over multi-year human-agent relationships, per-agent memory produces context sprawl and no single version of truth, and serious teams build bespoke profile architectures in-house rather than dumping traces into context.<br>*[Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)* |

*Why it matters: If sophisticated memory machinery does not beat naive in-context accumulation at medium horizons, most memory infrastructure spend is premature — but the result may be a horizon artifact that flips at production timescales, and knowing which determines whether to build now.*

## Practical Guidance

**Do:**

- Report gain (stateful reward minus stateless reward) alongside cumulative reward and cost on Pareto frontiers — cumulative reward alone confounds learning ability with base model strength.
- Use a judge to pick where in the rollout to inject a hint rather than hinting at the start, and distill only the next step or a few steps after it, since the KL learning signal decays with distance from the hint.
- Mask teacher tokens with an LLM judge so the student learns the target behavior and not the teacher's preferred connector words — this reduces catastrophic degradation.
- Filter solutions out of hints (hint leakage is the OPSD analogue of reward hacking): translate logs into what the model reasonably should have known, never the answer.
- Build regression avoidance into the optimization objective — fix recent failures subject to no regression on past learning environments — and keep the cost sub-linear in accumulated environments.
- Make the smallest durable change at the right layer: memory is cheapest and fastest, prompt/harness medium, model weights most expensive; LoRA makes weight updates cheaper and safer by bounding what can change.
- Try harness engineering before fine-tuning — the feedback loop is roughly two minutes and most teams never need to go further.
- Validate LLM judges like binary classifiers: ~100 hand-labeled pass/fail examples split train/dev/test, scored on precision and recall.
- Fine-tune your user simulator on real user verbatim until evaluation scores go down — a falling score means the eval got realistic, not that quality dropped.
- Judge in hindsight, after seeing the full chain of events or by polling several models; simple hindsight review catches most reward hacks.
- Work backwards from a known-reachable end state, throw away the solution, and learn to find it again — this manufactures supervision for free well beyond code.
- Start with a frontier model only to establish that the task is possible, then use its traces to port the task to a cheaper open model.
- Fix the task's input/output interface and evals so the model underneath can be swapped as a one-line change (Shopify: 550x cost reduction, same evals).
- Run small training runs as part of environment design — some problems only appear once RL is actually running.
- Attach a confidence interval to every reported score; 84% vs 88% on 50 traces is not a demonstrated gain.

**Avoid:**

- Chaining independent benchmark instances together and calling it a continual learning benchmark — they share no latent structure for the agent to exploit across instances.
- Treating production logs plus a feedback label as a learning environment; a single instance of what happened is not rerunnable and not gradable.
- Trace-to-harness 'vibe' edits where a coding agent reads a log and rewrites the agent — the change is untestable and introduces hidden regressions.
- Filtering timed-out rollouts out of training: it teaches the model to deliberately abuse tool calls and time out the sandbox to dodge a zero reward.
- Reward shaping for output format, or SFT on correctly formatted traces — both degraded general coding-agent performance on out-of-distribution behaviors.
- Applying one fixed offline hint uniformly when per-rollout online hints are available (~15%→80% correct formatting versus a small climb).
- Plain next-token-prediction finetuning on your own corpus: loss goes to ~0.0001, generation collapses, and no useful generalization appears.
- Per-failure-mode post-training — it is unwinnable Whac-A-Mole, and any fixed dataset saturates unless the model is underparameterized.
- Append-only memory logs with search over them; entries must be updated and compressed, because humans are not append-only logs either.
- Outsourcing memory to a third-party provider, or giving each agent its own memory system — the first cannot evolve with the product, the second produces context sprawl and no single version of truth.
- Using off-the-shelf frontier models as user simulators for support evals — they are trained to be helpful and produce unrealistically polite complaints (Lyft's first pass reported a bogus 90%+ pass rate).
- Shipping an LLM judge whose score gates no decision, or generic pre-built metrics (helpfulness 0.5) that no one can act on.
- Defining evaluation criteria before looking at data — criteria have to be discovered by grading real outputs.
- Letting self-improving skills evolve without explicit dependency and impact tracking; every skill that learns breaks something downstream.

## Notable Outliers

- Intelligence and expertise are largely orthogonal, so scaling model intelligence alone yields 'the world's smartest novice' — expertise compresses the search space while intelligence brute-forces it. ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [12:30](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=750s))
- On long-horizon tasks the OPSD teacher repeatedly course-corrects a divergent student and drives the model into a local optimum dominated by hedging tokens — 'wait', 'but', 'maybe'. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [13:28](https://www.youtube.com/watch?v=zL1kLftVTlo&t=808s))
- A ~10% tool-call failure rate from networking issues, with no presence whatsoever in the reward function, systematically made the model output shorter and shorter responses — environment fidelity and reward hacking are the same problem. ([Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [7:03](https://www.youtube.com/watch?v=k35LeKZEhiE&t=423s))
- Vanilla in-context learning topped Continual Learning Bench 1.0 over more sophisticated context-management systems, on reward and on both cost Pareto frontiers. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s))
- ChatGPT and Claude sit at opposite ends of the same compute tradeoff: a ~4,000-token profile updated every few days versus a ~1,000-token profile updated every 24 hours — higher serving cost for lower update cost, and vice versa. ([Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [13:18](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=798s))
- No frontier lab will supersize a model for pre-training again under the current architecture; instead they are pushing post-training further back, because architecture determines the ceiling and size is already at it. ([Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [18:39](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1119s))
- Rather than one artifact plus feature flags, deploy one canonical stem and let every user run their own bounded divergence of it — blast radius becomes one context and rollback needs no deploy. ([The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [7:56](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=476s))
- A teacher can move a student toward calling a tool purely by reshaping the reasoning path, never touching the tool-call tokens — SWE-bench task-complete rate went from ~22% to ~60% with test pass rate holding steady. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)
- [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Scaling Compute on Context](../talks/scaling-compute-on-context.md)
- [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)
- [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)
- [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Alex Cheema](../speakers/alex-cheema.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Isaac Miller](../speakers/isaac-miller.md)
- [Jack Morris](../speakers/jack-morris.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Maxime Rivest](../speakers/maxime-rivest.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Parth Asawa](../speakers/parth-asawa.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Raymond Feng](../speakers/raymond-feng.md)
- [Ronak Malde](../speakers/ronak-malde.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Samuel Denton](../speakers/samuel-denton.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Shlok Khemani](../speakers/shlok-khemani.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Will Brown](../speakers/will-brown.md)
- [Yu Su](../speakers/yu-su.md)

