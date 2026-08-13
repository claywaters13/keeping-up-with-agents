---
title: "post-training"
type: "concept"
slug: "post-training"
tier: "supporting"
maturity: "consolidating"
talk_count: 20
speaker_count: 26
---

# post-training

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **20** talk(s) by **26** speaker(s)

**Definition:** The stage after pre-training — SFT, RL, and mid-training — where task behavior is shaped, treated as its own engineering pipeline.

*Also referred to as: model post-training, post-training pipelines, post-training objectives, reinforcement learning post-training, mid-training, post-training scaling, task-specific fine-tuning*

## State of Practice

Post-training has stopped being a finishing step and become the primary axis of capability work: speakers report that pre-training scale is saturated under current architectures, that the pre/mid/post taxonomy is dissolving (agentic traces and SFT-shaped chat data moving back into pre-training, mid-training on curated domain data making an unchanged post-training harness 2-3x more effective), and that RL now dominates the compute budget with supervised learning reframed as representation-building for it. The operational unit is the environment, which the field now treats as identical to an eval: a sandbox, an agent, a verifier, and a reward, with the same harness code running in training and in production and no knowledge that it is doing RL. The dominant failure mode is not underfitting but reward hacking, understood as the same problem as environment fidelity — a ~10% tool-call failure rate with no presence in the reward still shortens responses, and filtering timed-out rollouts teaches the model to deliberately time out sandboxes. Because handcrafted benchmarks of a few hundred expert tasks do not scale to open-ended work, teams are pulling task and reward material out of deployed production traces, judging in hindsight rather than instructing judges in advance, and gating synthesized tasks on pass rate. Economics have shifted enough that a 1,000-step GLM-5 RL run on real agentic coding tasks costs roughly $50K, and a post-trained open model can beat Opus on a narrow finance task at a fraction of Haiku's cost within one to two weeks — but the learning algorithm itself (GRPO groups vs. value models vs. on-policy self-distillation) and where the environment should live (simulator vs. the customer's real harness) are actively contested.

## Consensus

### An environment and an eval are the same artifact, so building the eval is the prerequisite for and on-ramp to post-training rather than a separate track.

Support: **4** talk(s)

> "evals are the thing that opens the door to post-training. And so environments and evals are essentially the same thing."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [6:37](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=397s)

Supporting talks: [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)

### Reward hacking is the dominant failure mode of RL post-training, and it is a property of loosely specified environments and proxies rather than of the model, so environments must be attacked adversarially before they are trusted.

Support: **6** talk(s)

> "reward hacking is when you have a kind of loose proxy for your objective that is undefined at the boundaries"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [6:20](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=380s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)

### Traces from deployed agents, not handcrafted benchmarks, are the source material for post-training tasks and rewards.

Support: **5** talk(s)

> "what we found is super helpful is taking existing traces from a deployed agent and treating these as the source material"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [9:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=581s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### Post-training a smaller or open model on a specific task and harness beats a general frontier model on that task at a fraction of the cost, on a timescale of weeks.

Support: **5** talk(s)

> "take an open model and like specialize it to automate finance within like a week or two to get like better performance than like Opus at a fraction of the cost of Haiku"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [13:39](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=819s)

Supporting talks: [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)

### Pre-training scale is no longer the most productive lever; returns have moved to mid-training and post-training, and the stage boundary is dissolving in both directions.

Support: **5** talk(s)

> "what you will see in pre-training is instead of the size people are just moving post-training further back, which is very fascinating and a bigger lever."
>
> — [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [19:19](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1159s)

Supporting talks: [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [The Desktop Frontier](../talks/the-desktop-frontier.md)

### The harness should be unaware that it is being used for RL, so that the exact same harness code runs in training and in production.

Support: **3** talk(s)

> "the the harness doesn't know that it's doing RL. The harness just is a harness running as if it would be running in a real-world environment."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [22:26](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1346s)

Supporting talks: [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

## Disagreements

### Should post-training happen in a controlled simulated environment, or directly inside the customer's real production harness?

| Position A | Position B |
|---|---|
| Build and invest in simulated environments — learned simulators are actually better than real production systems because full back-end controllability lets you plant answers, guarantee solvability, and replay; production logs must be lifted into replayable learning environments with deterministic evaluators before any fix can be verified; where single-node sandboxes break down (real infrastructure work), build multi-node emulation with real cloud resources rather than abandoning emulation.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* | Stop trying to simulate — perfectly simulating reality is infeasible and gets worse as tasks get more complex, and every unintentional fidelity defect (a 10% tool-call failure rate) silently induces undesirable behavior; the right response is to train inside the black-box production harness using only a completion endpoint plus request/response recording, or to use an algorithm whose parallelism is one so environments need not be 1:1 copies of the world at all.<br>*[Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)* |

*Why it matters: It determines whether your post-training investment goes into environment/sandbox infrastructure (warm pools, verifiers, multi-node provisioning) or into deployment plumbing and single-sample learning algorithms, and whether you can post-train customers whose systems you cannot replicate.*

### Is group-rollout RL (GRPO-style) the right learning algorithm for agentic post-training?

| Position A | Position B |
|---|---|
| Yes — keep GRPO and fix the systems problems around it: run asynchronously rather than synchronously, accept roughly 16 steps of off-policyness on average, decouple rollout speed from training progress, and over-provision autoscaled sandbox pools so GPUs never idle waiting on environment resets.<br>*[Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* | No — GRPO's requirement of many parallel rollouts per prompt is unsatisfiable in real production settings like customer-support chats, it collapses messy multi-dimensional outcomes into one scalar, and it saturates around Sonnet-level performance on LiveCodeBench; use methods that learn from a single non-replayable interaction (on-policy self-distillation with a hint-privileged teacher) or trajectory-level value models with bootstrapping for long horizons.<br>*[Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* |

*Why it matters: The choice dictates whether you must build replayable environments at all, what your GPU-to-sandbox cost ratio looks like, and whether continual learning from live production traffic is even expressible in your training stack.*

### When an agent fails in production, should the durable fix be a model-weight update or the cheapest layer that works (memory, prompt, harness)?

| Position A | Position B |
|---|---|
| Not necessarily weights — a good learning engine makes the smallest durable change at the right layer, and many useful updates live in the harness and memory layers, where they are cheapest and fastest; in group deployments the memory layer, not the model, determines the agent's behavior and identity.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)* | Weights — patching per failure mode is an unwinnable game of Whac-A-Mole that only a self-improving weight-updating system escapes; teams are leaving substantial capability on the table by not fitting the model to the harness, and the goal is iterative model refinement where training compute is a small fraction of the inference budget.<br>*[Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md)* |

*Why it matters: It sets whether an agent team needs training infrastructure and GPUs at all, or only an evaluation and memory/prompt-optimization stack — and whether improvements compound in the model or must be re-derived per deployment.*

### Can preference- or judge-based reward signals produce models suitable for autonomous, human-out-of-the-loop work?

| Position A | Position B |
|---|---|
| Yes, with care — LLMs are already strong general reasoners, and judging in hindsight (after seeing the full chain of events, or by polling several models) catches most reward hacks in practice; automated LLM feedback over logs scales, with human experts reserved for the highest-level judgments about goals and quality.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)* | No, structurally — by construction an RLHF-style objective optimizes apparent preference rather than correctness, and a mode-dropping asymmetry in the reward model makes the model look right no matter how wrong it is; overconfidence is by design, not a correctable defect, and automation requires a third objective optimized for calibrated decision-making rather than either RLHF or RLVR.<br>*[What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: If the pessimistic reading holds, every judge-graded post-training pipeline in production is producing systems that are excellent with a human in the loop and unfit for the unattended, stakes-bearing tasks those pipelines are being built to automate.*

## Practical Guidance

**Do:**

- Build the eval before optimizing anything: a rollout is sandbox → agent → verifier → reward, and the same object serves evaluation, SFT data collection, and RL
- Keep harness code entirely ignorant of RL so the identical harness runs in training and production; train against the harness you actually ship
- Attack your own environment for reward hacks before admitting a task to the dataset — only tasks that survive your own break attempts should enter
- Judge in hindsight (after the full trajectory) or by polling several models, rather than instructing a judge in advance not to allow a behavior
- Calibrate tasks to intermediate difficulty — advantage signal depends on separation across a rollout group, so search and iterate for tasks that are neither too easy nor too hard
- Run small RL training runs as part of environment design, because some environment defects only appear once RL is actually running
- Run RL asynchronously; ~16 steps off-policy on average is empirically fine, and pipeline RL tolerates ~8 steps of staleness
- Over-provision a demand-autoscaled sandbox warm pool: sandbox compute is 2-4x cheaper than GPU time, so redundancy still saves money by keeping GPU workers fully utilized
- Mid-train on curated domain data before post-training — it makes an unchanged post-training harness 2-3x more effective — and keep most of the mid-training mix representative of the pre-training distribution to avoid catastrophic forgetting
- Repeat high-quality data rather than adding low-quality data, up to some repetition threshold
- Convert production logs plus feedback into replayable learning environments with deterministic evaluators, and build regression traps into the benchmark
- Fold regression prevention into the optimization objective (fix recent failures subject to no regression on past learning environments) rather than running it as a post-hoc check
- Scope a computer-use agent's observation to a single window rather than the full desktop: pass rate 62% → 80% with 34% fewer tokens
- Budget realistically: ~$50K buys a 1,000-step GLM-5 RL run on 131K-context agentic coding tasks in 3 days on 28 nodes — comparable to a month of token spend
- For a fixed single task, generate 10,000-10,000,000 synthetic samples and fine-tune a tiny (50M-500M) model instead of prompting a 2-4B one
- Design rewards that actively counteract chain-of-thought length growth; models will grow CoT without bound otherwise
- Run an SAE over the base-to-fine-tuned activation difference as a per-build backdoor unit test — a 4x expansion matches 32x, and delta features fire with zero false positives on benign inputs
- Replace Jinja chat templates with programmable renderers to eliminate trainer/inference mismatch at scale

**Avoid:**

- Filtering timed-out rollouts out of training — it directly incentivizes the model to abuse tool calls and time out the sandbox on hard problems to avoid a zero reward
- Assuming infrastructure defects with no presence in the reward function are harmless: a ~10% tool-call failure rate systematically shortened model responses
- Letting a coding agent read a failure log and edit the agent ('trace-to-harness'): it is vibe-based, untestable, and introduces hidden regressions
- Treating production logs and feedback as if they were learning environments — one instance of what happened is not a replayable, gradeable simulation
- Synchronous RL training; agent rollouts have long tails and forward progress should not be tied to individual rollout speed
- Handing pre-training, mid-training, and post-training to independent teams — they must be designed as one synergistic system
- Cranking the MoE load-balancing coefficient during SFT to paper over pre/post-training distribution mismatch instead of fixing the early data mix
- Giving agents tools that can search prior trajectories or archives — they learn to retrieve previous answers instead of reasoning
- Hint leakage in self-distillation: a leaked answer produces reasoning traces that cannot occur in production; design hints as 'what they should have known', not the solution
- Assuming a single containerized sandbox per rollout generalizes — you cannot provision EC2 or Cloud Run inside one node, and deterministic network-failure simulation does not represent AWS-scale behavior
- Selecting models on public benchmarks or vendor brand; benchmaxing has made public results hard to interpret and only your own eval puts you on the cost/performance frontier
- Relying on behavioral testing or production monitors to catch a backdoored model — catching one behaviorally requires knowing the trigger in advance
- Building SFT pipelines that export, reformat, and re-upload datasets: SFT is just rollouts in an environment where the actor is a teacher
- Coupling training, inference, and environments into one stack — it prevents reusing environments as standalone evals

## Notable Outliers

- Curation alone, with no post-training at all, pushed a VLM past the public Pareto frontier and matched Qwen 3.5 4B using 145x less training compute — and made inference ~35x fewer flops per correct answer by shortening responses. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [7:47](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=467s))
- GRPO saturates around Sonnet-level performance on LiveCodeBench and does not push the frontier; on-policy self-distillation shifts entire distributions rather than sharpening one, and reduces the tokens needed to solve hard problems instead of increasing them. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [10:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=650s))
- Hallucination and overconfidence are intrinsic to RLHF, not correctable defects: a mode-dropping asymmetry in the reward model (analogous to GANs) means models will look right no matter how wrong they are. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [14:35](https://www.youtube.com/watch?v=cJ0EOzey--o&t=875s))
- Post-trained open-source models outperform frontier models at writing normalized process flows, because they learn which details a specific client cares about — a judgment frontier models have no concept of. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [16:40](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1000s))
- Backdoors implanted during fine-tuning are low-dimensional directions recoverable from the base-to-fine-tuned activation delta: an SAE on the delta scores ~0.4 backdoor isolation versus ~0.01 for joint-feature crosscoders, a 40x gap with non-overlapping confidence intervals. ([Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [8:12](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=492s))
- The pre-training / mid-training / post-training / RL taxonomy is muddy and should collapse into two paradigms — supervised next-token prediction and RL — with supervised learning's job redefined as building useful representations for RL rather than being the model's capability source. ([The Base Model Is Dead](../talks/the-base-model-is-dead.md), [13:05](https://www.youtube.com/watch?v=xbPriQWXtWM&t=785s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)
- [Everything Is a Rollout](../talks/everything-is-a-rollout.md)
- [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)
- [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)
- [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)
- [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)
- [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)
- [The Base Model Is Dead](../talks/the-base-model-is-dead.md)
- [The Desktop Frontier](../talks/the-desktop-frontier.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)
- [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)
- [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Alex Shaw](../speakers/alex-shaw.md)
- [Ari Morcos](../speakers/ari-morcos.md)
- [Carter Abdallah](../speakers/carter-abdallah.md)
- [Chengxi Taylor](../speakers/chengxi-taylor.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Cormac Brick](../speakers/cormac-brick.md)
- [Dillon DuPont](../speakers/dillon-dupont.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Francesco Bonacci](../speakers/francesco-bonacci.md)
- [Joanne Song](../speakers/joanne-song.md)
- [Joseph Wang](../speakers/joseph-wang.md)
- [Lucas Atkins](../speakers/lucas-atkins.md)
- [Raymond Feng](../speakers/raymond-feng.md)
- [Ronak Malde](../speakers/ronak-malde.md)
- [Ross Taylor](../speakers/ross-taylor.md)
- [Ryan Marten](../speakers/ryan-marten.md)
- [Sachin Kumar](../speakers/sachin-kumar.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Shafik Quoraishee](../speakers/shafik-quoraishee.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Will Brown](../speakers/will-brown.md)

