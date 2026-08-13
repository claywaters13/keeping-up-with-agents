---
title: "reward design"
type: "concept"
slug: "reward-design"
tier: "supporting"
maturity: "contested"
talk_count: 9
speaker_count: 10
---

# reward design

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **9** talk(s) by **10** speaker(s)

**Definition:** Shaping the reward signal itself — density, sparsity, and credit assignment across long rollouts — as distinct from designing the environment or the verifier.

*Also referred to as: reward shaping, reward sparsity, reward signal density, credit assignment in sparse-reward settings, credit assignment in long rollouts, per-token dense reward, dense reward in post-training*

## State of Practice

The field has moved past the assumption that a terminal scalar reward is enough: across coding, finance, and biology, speakers report that end-of-rollout grading is too sparse to carry credit across 50-100 tool calls, and that gradient variance scales with trajectory length while the reward stays a single number. The consensus response is densification — deterministic validation loops embedded in the codebase (Factory), intermediate nodes of an analysis DAG (LatchBio), trajectory-level value models with compaction (General Reasoning), per-token teacher log-prob matching (Trajectory), or mid-rollout textual feedback that reweights probabilities at a specific step (Cursor). Simultaneously, practitioners now treat verifiable rewards as the easy special case: math answers, unit tests, and database state cover a shrinking fraction of economically valuable work, so judge models, rubrics, and hindsight review are being pressed into the reward slot despite known unreliability (LatchBio measured only loose numerical correlation between rubric scores and verifiable outcomes, and Langfuse showed LLM-judge scores are non-deterministic run to run). Reward hacking is treated as a structural property of loose proxies rather than a bug — a proxy undefined at its boundaries will be exploited, whether by mining git history for the answer, escaping the sandbox, reading a hidden test suite, or leaking a hint into the reasoning trace. Task difficulty is now a reward-design variable in its own right: because group-relative advantage depends on separation across rollouts, tasks that are all-pass or all-fail contribute no signal, so pass-rate-gated generation and eval retirement at ~90% are standard practice. What remains genuinely open is whether the reward should come from a deterministic verifier or an agentic judge, and whether reward design should be automated up the abstraction ladder or anchored to human domain experts.

## Consensus

### A single terminal reward at the end of a long rollout is too sparse to train on; the reward signal has to be densified into intermediate checkpoints, per-step feedback, or a learned value estimate.

Support: **5** talk(s)

> "Models need dense reward. These verification signals form the basis of that reward that they use to keep them on track over a long-term goal-directed problem."
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [16:01](https://www.youtube.com/watch?v=wpOA-UXynoM&t=961s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)

### Reward hacking is not an edge case but the expected outcome of any loose proxy, so environments and graders must be designed on the assumption the model will find and exploit the undefined boundary.

Support: **5** talk(s)

> "reward hacking is when you have a kind of loose proxy for your objective that is undefined at the boundaries"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [6:20](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=380s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)

### Collapsing a messy multi-objective task into one scalar score destroys the information the model needs; rewards should be decomposed into multiple explicitly defined criteria or binary domain-specific checks.

Support: **4** talk(s)

> "we are shoving every single reward into one scaler in order to train on when the real world is messy."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [2:54](https://www.youtube.com/watch?v=zL1kLftVTlo&t=174s)

Supporting talks: [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md)

### Verifiable rewards are the easy special case that produced the math and competitive-coding gains; the economically valuable domains now being targeted admit no clean ground truth, so reward must come from soft verification.

Support: **4** talk(s)

> "a lot of the early RL that we were doing in in recent times was really in hard verifiable domains and that's why we saw these gains in in math and kind of uh like data structure style coding problems"
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [10:14](https://www.youtube.com/watch?v=2aS7aKoXn64&t=614s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

### Task difficulty is part of reward design: tasks the model always solves or never solves produce no usable signal, so tasks must be searched for and gated into an intermediate-difficulty, learnable band.

Support: **3** talk(s)

> "you want tasks that are not too easy, not too hard and you want to be searching for these and iterating on generating more of them"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [14:08](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=848s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)

## Disagreements

### For soft-verifiable domains, should the reward come from a deterministic verifier applied to a decomposed task, or from an agentic judge with a rubric?

| Position A | Position B |
|---|---|
| Keep the reward deterministic. Decompose the task until each piece has a Python-function grader; rubric scores are only loosely correlated with verifiable outcomes and are not yet trustworthy for RL or benchmarking. Framing a problem as a set of verification systems is what makes it solvable at all.<br>*[Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)* | Deterministic verifiers are impractical, brittle, or impossible for the ambiguous, open-ended tasks that matter economically, and comparing against a reference answer fails because too many solutions are correct. Judges must be built as agents that reuse the harness, inspect the trajectory, and independently query environment state, scored against roughly 20 criteria with ~10 subcriteria each.<br>*[Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* |

*Why it matters: It decides whether the frontier of RL-trainable work is bounded by what you can write an assertion for, or whether judge noise is acceptable to absorb into the gradient. Getting it wrong either stalls at code-and-math-shaped tasks or trains on a reward signal with unquantified correlation to the real objective.*

### Can outcome reward with group-relative advantage carry long-horizon tasks, or is per-step/per-token credit assignment required?

| Position A | Position B |
|---|---|
| Outcome reward over a group of rollouts remains the core mechanism; the work is in the infrastructure around it — async rollouts tolerating ~16 steps of off-policyness, group rewards across rollouts, and calibrating task difficulty so advantage separates within the group.<br>*[Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* | Group-relative outcome reward is the bottleneck itself. Value models beat GRPO for long horizons because they cut length-scaled gradient variance and permit bootstrapping; per-token teacher supervision removes the need for parallel rollouts entirely; and mid-rollout textual feedback is more precise than grading the end state. GRPO is reported to saturate around Sonnet-level performance on LiveCodeBench without pushing the frontier.<br>*[Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)* |

*Why it matters: It determines whether the environment must be a faithful, resettable, N-times-parallel copy of production (GRPO's requirement) or can be a single live production trace, which changes what infrastructure and what data you need to do continual learning at all.*

### Should reward hacking be prevented ex ante by constraining the environment, or caught ex post by reviewing the trajectory?

| Position A | Position B |
|---|---|
| Close the hole before the run: delete git history at the start and restore it at the end, allowlist the network, and do not ship agents tools that let them search prior trajectories or archives, because that teaches retrieval of previous answers instead of reasoning.<br>*[Recursive Model Improvement](../talks/recursive-model-improvement.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* | You cannot enumerate the holes in advance, and instructing a judge not to allow a behavior does not stop it in the rollout; judge in hindsight after seeing the full chain of events, with the judge inspecting the trajectory and environment state. Over-constraining the environment also collapses the state space of paths the agent explores.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md)* |

*Why it matters: Ex-ante constraints are cheap but restrict exploration and only cover known exploits; ex-post hindsight review preserves exploration but requires storing, enriching, and segmenting every long trajectory into a queryable artifact — a substantially larger data-infrastructure commitment.*

### Should reward and environment design be automated by models, or anchored to human domain experts?

| Position A | Position B |
|---|---|
| Reward design follows coding agents up the abstraction ladder: generate, solve, and synthesize tasks in an online loop gated on pass rate, let compute handle environment refinement, and surface only the highest-level judgments about goals and quality to humans. Being bottlenecked on humans launching and reviewing runs is the state to escape.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)* | The target function you hand an agent is always incomplete, so an auto-improvement loop optimizes toward the wrong optimum. Production data must be reviewed by a human, not only by coding agents, and domain experts are needed to surface the implicit decision criteria that become the evaluators; in biology, scientists grading each other's work is the best available proxy for ground truth and each task took three people a week to build.<br>*[Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)* |

*Why it matters: It sets the cost curve for entering a new domain: automated task synthesis promises thousands of environments cheaply, while expert-anchored construction caps you at hundreds but keeps the proxy tied to what practitioners actually value.*

## Practical Guidance

**Do:**

- Count the deterministic validation loops in a codebase before expecting long-horizon autonomy — agent readiness is that count, not model capability
- Decompose end-outcome grading into intermediate nodes of the task's analysis DAG when models are still weak at the end-to-end task
- Gate generated tasks on pass rate to keep them in the not-too-easy/not-too-hard band, and retire any eval where all models score ~90%
- Construct tasks by reverse engineering from a known-reachable end state: delete a feature until tests fail, or plant the answer and throw away the solution path, so supervision comes for free and solvability is guaranteed
- Replace 0-1 and 1-5 generic quality scores with binary domain-specific assertions such as 'the answer is based on the knowledge base: yes/no'
- Judge in hindsight over the completed trajectory, or poll several models, rather than trying to specify failures in advance
- Give the judge read-only access to the real environment (GitHub, AWS logs) and have it verify state independently, since the agent's reported tool calls are not reliable evidence
- Delete git history at the start of an eval or training run and restore it after, and apply a network allowlist, so scores are not inflated by answer retrieval
- Run small RL runs as part of environment and reward iteration, because some reward pathologies only appear once RL is actually running
- Explicitly counteract unbounded chain-of-thought growth in the reward, accepting that the optimal token budget per problem is unknown
- Apply RL to the compaction step itself, not just the task, when trajectories exceed the context window
- Design hints so they encode what the model should have known rather than the solution, and filter leaked answers out of hint text
- Add traditional-ML validation splits plus an explicit escape hatch to any optimization loop

**Avoid:**

- Mashing every objective into one scalar reward when the real-world task is multi-objective
- Maximizing rubric density — overly dense rubrics degrade judge consistency exactly on the frontier problems you care about
- Grading only the final state, or comparing against a reference answer or sample trajectory, on open-ended tasks where correct solutions cannot be enumerated
- Telling a judge model not to allow a behavior as your reward-hacking defense; it does not prevent the behavior in the rollout
- Shipping agents tools that can search prior trajectories or archives, which trains retrieval of past answers instead of reasoning
- Constraining the allowed path so tightly that you collapse the state space the agent explores
- Spending compute on environments the model cannot learn from — learnability is a first-class design criterion alongside difficulty
- Treating public benchmark scores as training reward; their signal is too coarse, and their short average human task time means saturation does not indicate the capability is solved
- Faking long horizon by chaining unrelated independent subtasks, which measures nothing about capability because earlier decisions never influence later ones
- Assuming a self-improvement loop keeps paying off past the first iteration, or letting it burn tokens for hours against a plateau
- Treating a plateau as purely a model failure when noise in the ground-truth labels themselves caps achievable accuracy

## Notable Outliers

- Rubric scores built from path-invariant choke points are associated with verifiable outcomes but only loosely correlated numerically, which is why LatchBio does not yet trust them for RL or benchmarking. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [13:46](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=826s))
- Hint leakage is the OPSD analogue of reward hacking: a leaked answer produces reasoning traces that could never occur in production, so hint design is as load-bearing as reward design. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [16:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1010s))
- On long-horizon tasks the teacher repeatedly course-corrects a divergent student, driving the model into a local optimum dominated by hedging tokens like 'wait', 'but', and 'maybe'. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [13:28](https://www.youtube.com/watch?v=zL1kLftVTlo&t=808s))
- Given $100K to trade Premier League football matches over a one-year horizon, every frontier model lost money — an open-ended, multi-agent reward setting the industry's coding-and-procedure bias does not cover. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s))
- Dynamic evaluation-time rubrics that grant partial credit by assuming an agent's earlier mistaken assumption was correct are an emerging credit-assignment pattern. ([Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [17:13](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1033s))
- Textual feedback — a teacher hinting at one specific rollout step and reweighting probabilities there — is more precise than end-of-rollout grading and generalizes beyond tool calling. ([Recursive Model Improvement](../talks/recursive-model-improvement.md), [11:05](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=665s))
- Almost all of the gain from a prompt self-improvement loop arrived in the first iteration from a clear-cut failure signal; the remaining iterations moved little. ([Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s))
- Supervised signal from the environment gives the model a likelihood model over environment tokens — a native world model — which RL reward alone would not produce. ([Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [17:35](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1055s))

## All Talks

- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
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
- [Will Brown](../speakers/will-brown.md)

