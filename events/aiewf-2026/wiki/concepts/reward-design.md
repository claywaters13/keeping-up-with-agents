---
title: "reward design"
type: "concept"
slug: "reward-design"
tier: "supporting"
maturity: "contested"
talk_count: 10
speaker_count: 11
---

# reward design

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **10** talk(s) by **11** speaker(s)

**Definition:** Shaping the reward signal itself — density, sparsity, and credit assignment across long rollouts — as distinct from designing the environment or the verifier.

*Also referred to as: reward shaping, reward sparsity, reward signal density, credit assignment in sparse-reward settings, credit assignment in long rollouts, per-token dense reward, dense reward in post-training*

## State of Practice

The field has converged on a diagnosis: a single terminal scalar is a useless training signal for long-horizon agent work, because gradient variance scales with rollout length and credit assignment collapses. The practical response splits along two axes — densifying reward in time (intermediate verification checkpoints, analysis-DAG nodes, per-step teacher hints, value models instead of group-relative baselines) and densifying it in dimension (decomposing a 0-1 quality score into dozens of binary, domain-specific criteria). Everyone accepts that any reward is a proxy that is undefined at its boundaries and that RL-trained models will find those boundaries; the accepted mitigation is hindsight inspection of the full trajectory plus independent verification of environment state, not instructing a judge in advance to disallow a behavior. Difficulty calibration is now treated as part of reward design rather than task curation: tasks that all rollouts pass or all fail carry no advantage signal, so pass-rate gating and eval retirement at ~90% are standard. What remains genuinely open is the mechanism — whether outcome verification should be pushed harder (Factory, Latch, Theta) or replaced by a dense teacher-derived per-token signal that skips reward entirely (Trajectory's OPSD, Cursor's textual feedback), and whether reward authoring is about to be automated or fundamentally requires domain experts.

## Consensus

### Sparse end-of-rollout reward is insufficient for long-horizon tasks; the signal must be densified into intermediate checkpoints derived from verification, traces, or a teacher.

Support: **6** talk(s)

> "Models need dense reward. These verification signals form the basis of that reward that they use to keep them on track over a long-term goal-directed problem."
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [16:01](https://www.youtube.com/watch?v=wpOA-UXynoM&t=961s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)

### Every reward is an incomplete proxy that is undefined at its boundaries, and models optimized against it will exploit those boundaries — reward hacking is the expected outcome, not an edge case.

Support: **6** talk(s)

> "reward hacking is when you have a kind of loose proxy for your objective that is undefined at the boundaries"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [6:20](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=380s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)

### Collapsing task quality into one scalar score (0-1, 1-5, pass/fail) destroys the information the model needs to change its behavior; reward must be decomposed into many concrete, ideally binary criteria.

Support: **4** talk(s)

> "imagine you were trying to write an essay and your teacher just gave you a score of 87 out of 100. You would have to run through so many different examples to get to the idea of what a good essay is"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [6:43](https://www.youtube.com/watch?v=zL1kLftVTlo&t=403s)

Supporting talks: [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)

### Reward is only informative when task difficulty sits in a middle band — tasks that are all-pass or all-fail produce no learning signal, so difficulty and learnability are first-class reward-design parameters.

Support: **3** talk(s)

> "you want tasks that are not too easy, not too hard and you want to be searching for these and iterating on generating more of them"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [14:08](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=848s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)

### Grading should be done in hindsight over the recorded trajectory rather than by instructing a judge in advance about what to disallow, because failures are far easier to identify after the full chain of events is visible.

Support: **3** talk(s)

> "a lot of times we will have a model that does something and it will make mistakes along the way and it's easier to tell what went wrong in hindsight."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [13:31](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=811s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)

## Disagreements

### Should the fix for sparse long-horizon reward be better outcome verification, or a dense per-step/per-token signal that bypasses outcome reward entirely?

| Position A | Position B |
|---|---|
| Keep grading outcomes, but decompose the task so outcomes are checkable at intermediate nodes: deterministic graders and judges that inspect environment state and trajectory at the end of a phase, with agent readiness measured by the density of deterministic validation loops.<br>*[Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)* | Outcome grading is intrinsically too coarse; supervise inside the rollout instead — a teacher model given privileged information hints at a specific step and the student's per-token log-probs are matched against it, or a value model bootstraps credit across the trajectory.<br>*[Recursive Model Improvement](../talks/recursive-model-improvement.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* |

*Why it matters: Outcome-first demands heavy investment in environment instrumentation and judge infrastructure that must be rebuilt per domain; step-level supervision demands a teacher and hint-design discipline instead, and changes whether you need a resettable environment at all.*

### Is group-relative RL (GRPO-style advantage over parallel rollouts) an adequate optimizer for long-horizon reward?

| Position A | Position B |
|---|---|
| Yes — advantage from separation across a group of rollouts is the workhorse; the real engineering problems are async off-policy scheduling, group-reward plumbing, and keeping the harness ignorant of RL, not the estimator itself.<br>*[Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* | No — GRPO saturates around Sonnet-level performance and does not push the frontier; parallel rollouts force environments to be one-to-one copies of the real world, which biases the training distribution. Value models (variance reduction, trajectory-level with compaction, bootstrapping) or parallelism-of-one teacher distillation are the way forward.<br>*[Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)* |

*Why it matters: If parallelism-of-one methods hold up, you can learn directly from single live production rollouts and the environment-cloning bottleneck disappears; if not, every trainable task needs a resettable, forkable environment.*

### Can reward and rubric authoring be automated, or does it require domain experts up front?

| Position A | Position B |
|---|---|
| It automates. Environment and reward design will climb the abstraction ladder the way coding agents did; mine deployed traces to synthesize tasks, gate them on pass rate, and reserve humans for the highest-level judgments about goals and quality.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)* | Domain expertise comes first. Auto-improvement loops only worked in coding because compilation is an unusually clean target function; outside it, experts must supply concrete examples and surface implicit decision criteria, production data must be reviewed by humans and not only by coding agents, and ground truth is best approximated by experts grading each other's work.<br>*[Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)* |

*Why it matters: It sets the cost curve for entering a new vertical: an automated loop is a compute purchase, while expert-authored reward is roughly a week of three specialists per task at Latch and hundreds of labeled examples at Langfuse.*

### How dense should a grading rubric be?

| Position A | Position B |
|---|---|
| Public benchmark signal is too coarse for training; useful rubrics need roughly 20 criteria with about 10 subcriteria each, plus dynamic evaluation-time rubrics that grant partial credit conditional on an agent's earlier mistaken assumption.<br>*[Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)* | A small set of binary, domain-specific checks is the right target; elaborate rubric scores are unreliable — they only loosely correlate with verifiable outcomes and are not yet trustworthy for RL or benchmarking, and most of the gain from an improvement loop lands on the first iteration off a clear-cut signal.<br>*[Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)* |

*Why it matters: Rubric density is a direct cost and reliability tradeoff: too sparse and the reward carries no gradient, too dense and judges apply it inconsistently on exactly the frontier problems you are trying to train.*

## Practical Guidance

**Do:**

- Measure how many deterministic validation loops exist in the codebase before expecting long-horizon autonomy — output quality tracks validatability, not model capability.
- Densify binary pass/fail benchmark output into per-trace feedback the model can act on; treat traces as the substrate holding that feedback.
- Judge in hindsight over the stored trajectory, and have the judge independently verify environment state (GitHub, AWS logs) rather than trusting the agent's reported tool calls.
- Give the judge read-only access to the same harness and environment as the agent, with permissions that prevent it from mutating state after the rollout ends.
- Store, enrich, and phase-segment long trajectories so they are queryable — a single LLM call over a stuffed context window cannot evaluate them.
- Replace generic scalar evaluators with binary domain checks ('the answer is based on the knowledge base: yes/no', brand-name correctness, categorization into known failure modes).
- Manufacture hard verifiable problems by working backward from a known-reachable end state — delete features from a working app until tests fail, then have the model re-implement them.
- Gate synthesized tasks on measured pass rate to keep them in the intermediate-difficulty band; retire any eval where all models score ~90%.
- Run small RL runs as part of reward design, since some pathologies only appear once training is actually running.
- Put explicit counter-pressure on chain-of-thought length into the reward, and expect to juggle it against the task objective.
- Control eval contamination mechanically — delete git history at the start of a run and restore it after, and use network allowlists.
- Add traditional-ML validation splits and an explicit escape hatch to auto-optimization loops so they stop instead of burning tokens against a plateau.

**Avoid:**

- Compressing a messy multi-objective task into a single scalar reward.
- Grading only the final state or the end-to-end outcome when the model is still weak — the signal is too sparse to learn from.
- Scoring open-ended work by comparison against a reference answer or sample trajectory; too many correct solutions exist to enumerate.
- Maximizing rubric density — overly dense rubrics degrade judge consistency exactly on the frontier problems you care about.
- Telling a judge model not to allow a behavior and assuming that prevents it in the rollout; it does not.
- Giving agents tools that can search prior trajectories or archives, which teaches retrieval of past answers instead of reasoning.
- Leaking the solution inside a teacher hint — the resulting reasoning traces cannot occur in production, the OPSD analogue of reward hacking.
- Faking long horizon by chaining unrelated independent subtasks; earlier decisions must influence later ones for the reward to measure anything.
- Treating a target function as complete — optimizing hard against an incomplete target walks toward the wrong optimum.
- Trusting rubric scores for RL when they are only loosely correlated with the verifiable outcomes they are supposed to proxy.

## Notable Outliers

- Given $100K to trade Premier League football matches over a one-year horizon on Kelly Bench, every frontier model lost money — an open-ended, multi-agent, uncertain reward setting the industry's coding-centric benchmarks do not capture. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s))
- On long-horizon tasks a teacher that repeatedly course-corrects a divergent student drives the model into a local optimum dominated by hedging tokens — 'wait', 'but', 'maybe'. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [13:28](https://www.youtube.com/watch?v=zL1kLftVTlo&t=808s))
- Models grow their chains of thought without bound unless reward actively counteracts it, but nobody knows the optimal length for a given problem, so the length penalty is an unresolvable guess. ([Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [18:36](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1116s))
- Group rewards are hard to implement in most RL frameworks because the frameworks assume rollouts live independently and never need to talk to each other. ([Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [17:22](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1042s))
- Building an eval forces more rigorous reasoning than doing the analysis yourself — it exposed that many canonical numerical QC thresholds in bioinformatics are arbitrary. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s))
- On finance tasks averaging 15 human hours across a 50-task sample, frontier models still score around 5 — the reward signal in saturated public benchmarks reflects their short average human task time, not solved capability. ([Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [20:32](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1232s))
- Textual feedback that hints at one specific step of a rollout and reweights probabilities there is more precise than end-of-rollout grading, and generalizes to arbitrary behaviors rather than just tool calling. ([Recursive Model Improvement](../talks/recursive-model-improvement.md), [11:05](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=665s))

## All Talks

- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
- [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md)
- [Recursive Model Improvement](../talks/recursive-model-improvement.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)
- [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)
- [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

## Speakers

- [Annabell Schäfer](../speakers/annabell-schafer.md)
- [Chengxi Taylor](../speakers/chengxi-taylor.md)
- [Eno Reyes](../speakers/eno-reyes.md)
- [George Cameron](../speakers/george-cameron.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Rayan Garg](../speakers/rayan-garg.md)
- [Ronak Malde](../speakers/ronak-malde.md)
- [Ross Taylor](../speakers/ross-taylor.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Will Brown](../speakers/will-brown.md)

