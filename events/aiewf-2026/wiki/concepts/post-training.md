---
title: "post-training"
type: "concept"
slug: "post-training"
tier: "supporting"
maturity: "contested"
talk_count: 22
speaker_count: 28
---

# post-training

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **22** talk(s) by **28** speaker(s)

**Definition:** The stage after pre-training — SFT, RL, and mid-training — where task behavior is shaped, treated as its own engineering pipeline.

*Also referred to as: model post-training, post-training pipelines, post-training objectives, reinforcement learning post-training, mid-training, post-training scaling, task-specific fine-tuning*

## State of Practice

Post-training has stopped being a finishing step and become the main lever: with pre-training scale saturating under current architectures, speakers describe RL and mid-training as where capability now comes from, and several describe post-training-shaped data (SFT chats, agentic traces, long-context) migrating backward into pre-training so the stage taxonomy itself is dissolving. The unit of work is the environment, and the field has converged on the claim that an environment and an eval are the same object — the same sandbox/agent/verifier/reward primitive serves evaluation, SFT data generation, RL, and distillation, which makes building your own eval the on-ramp to training rather than a parallel track. The dominant source material is no longer curated human data or handcrafted benchmarks but deployed production traces, because most economically valuable tasks are non-verifiable and no golden rubric exists. The hardest recurring failure is that environment fidelity and reward hacking are the same problem: a 10% tool-call failure rate silently shortens responses, filtering timed-out rollouts teaches the model to time out sandboxes, and hint-based distillation has its own analogue in hint leakage. Economics have shifted enough that a 1,000-step RL run on a frontier-size model over real agentic coding tasks costs roughly $50K, and multiple teams report post-trained open or tiny models beating Opus-class frontier models on a single narrow task at one to two orders of magnitude lower cost. What remains genuinely unsettled is the algorithm (GRPO versus on-policy self-distillation versus value models), whether to simulate the environment or train inside the customer's live harness, and whether weights are the right layer to change at all.

## Consensus

### Pre-training scale is no longer the most productive axis; post-training/RL is where marginal capability now comes from, and post-training-shaped work is moving earlier in the pipeline.

Support: **5** talk(s)

> "pre-training size in particular is not your most lucrative axis of scale."
>
> — [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [10:38](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=638s)

Supporting talks: [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)

### Environments and evals are the same artifact, so building your own eval is the prerequisite and on-ramp to post-training — one environment serves evaluation, SFT data collection, RL, and distillation.

Support: **4** talk(s)

> "evals are the thing that opens the door to post-training. And so environments and evals are essentially the same thing."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [6:37](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=397s)

Supporting talks: [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)

### Traces from a deployed agent, not handcrafted benchmarks or curated human data, are the primary source material for post-training.

Support: **6** talk(s)

> "We can improve for free today by using offline production traces. Give us a dump of your production data. We'll find a way to make it valuable."
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [9:05](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=545s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### Verifiable rewards are the easy special case; the bulk of real-world value sits in non-verifiable tasks where no golden answer, rubric, or binary grade exists.

Support: **5** talk(s)

> "often we don't actually have verifiable rewards. And so messy real world tasks often we're kind of figuring out as we go."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [0:13](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=13s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)

### A post-trained smaller or open model beats a frontier model on a specific narrow task, at one to two orders of magnitude lower cost, within one to two weeks of work.

Support: **4** talk(s)

> "take an open model and like specialize it to automate finance within like a week or two to get like better performance than like Opus at a fraction of the cost of Haiku"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [13:39](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=819s)

Supporting talks: [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

### Environment fidelity defects and reward hacking are the same failure: any unintended imperfection in the environment or reward proxy gets systematically exploited by the trained model.

Support: **5** talk(s)

> "And the main sort of problem is like has kind of two names, which are both the same problem, environment fidelity and reward hacking."
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [7:03](https://www.youtube.com/watch?v=k35LeKZEhiE&t=423s)

Supporting talks: [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md)

### The pre-training / mid-training / post-training boundary is dissolving — the stages should be designed as one system, with SFT-style and agentic data pulled backward into earlier training.

Support: **3** talk(s)

> "what you will see in pre-training is instead of the size people are just moving post-training further back, which is very fascinating and a bigger lever."
>
> — [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [19:19](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1159s)

Supporting talks: [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)

## Disagreements

### When a training environment fails to match reality, should you build a higher-fidelity simulation or abandon simulation and train inside the live production harness?

| Position A | Position B |
|---|---|
| Invest in fidelity: lift logs into replayable learning environments, provision real multi-node cloud infrastructure, or learn a simulator you fully control so you can plant answers and guarantee solvability.<br>*[Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* | Perfect simulation is infeasible and every imperfection injects subtle pathologies, so train directly in the customer's black-box harness using only a completion endpoint plus request/response recording, learning from non-replayable single interactions.<br>*[Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)* |

*Why it matters: It determines whether the expensive asset is an environment-engineering team building sandboxes and evaluators, or a training stack that runs against someone else's opaque orchestration. It also decides whether replayability and parallel rollouts are available at all, which cascades into the choice of RL algorithm.*

### Is GRPO-style group-relative RL over parallel rollouts the right optimization method for production agent post-training?

| Position A | Position B |
|---|---|
| Yes — group-relative advantage over many rollouts per prompt is the workhorse; make it practical by going async, tolerating ~8–16 steps of off-policyness, and calibrating tasks to intermediate difficulty so the advantage signal separates.<br>*[Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* | No — requiring many parallel rollouts per prompt is unsatisfiable in real production (you cannot re-run a customer support chat), collapses messy reality into one scalar, and saturates; use on-policy self-distillation from a hint-privileged teacher with parallelism of one, or value models for long horizons.<br>*[Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* |

*Why it matters: The algorithm choice dictates the entire infrastructure: parallel-rollout RL forces one-to-one replayable environment copies and a rollout scheduler, while self-distillation needs a judge, hint design, and per-token masking instead. It also determines whether continual learning from live single-shot production traffic is even reachable.*

### Should teams reach for weight updates at all, or exhaust harness, prompt, and memory changes first?

| Position A | Position B |
|---|---|
| Change the smallest, cheapest layer that durably fixes the failure — harness engineering has a roughly two-minute feedback loop, most teams never need to go further, and weight updates are the most expensive and riskiest layer.<br>*[Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* | Harness-only work leaves real capability unclaimed and turns into per-failure-mode Whac-A-Mole; post-train the model on your own harness, because the frontier model getting better is not the same as your model getting better.<br>*[Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* |

*Why it matters: This decides whether an org needs a training stack, GPUs, and RL researchers at all, or just tracing plus prompt iteration. It also changes the failure mode you have to defend against: silent prompt regressions versus catastrophic forgetting and reward hacking.*

### Is RLHF/human-preference optimization the right post-training objective going forward?

| Position A | Position B |
|---|---|
| RLHF is the foundation of everything usable — it is what turned LLMs into products, with a 1B RLHF model outperforming a 175B one, and essentially all deployed models are trained with it.<br>*[Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* | RLHF structurally produces overconfidence and hallucination via a mode-dropping asymmetry in the reward model, so it is fine for human-in-the-loop assistance but disqualifying for automation; the next paradigm optimizes for calibrated decision-making, which is neither RLHF nor RLVR.<br>*[What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: If overconfidence is by construction rather than a fixable defect, then no amount of prompting or eval work makes today's models safe for stakes-bearing autonomous decisions, and the whole reward-modeling stack needs replacing rather than tuning.*

## Practical Guidance

**Do:**

- Build the eval/environment first and only then optimize against it — the same rollout primitive (sandbox → agent → verifier → reward) serves evaluation, SFT data collection, RL, and distillation.
- Keep harness code completely ignorant of RL so the identical harness runs in training and in production.
- Run RL asynchronously and accept off-policy staleness; ~16 steps off-policy on average is empirically fine, and ~8 steps is the reported ceiling for pipeline RL before quality degrades.
- Adversarially attack your own environment for reward hacks before admitting a task to the dataset; only tasks that survive the break-it pipeline enter.
- Calibrate tasks to intermediate difficulty — not too easy, not too hard — and iterate on generating more of them, since the advantage signal depends on separation across a rollout set.
- Judge in hindsight, after seeing the full chain of events (or by polling several models), rather than instructing a judge in advance not to allow a behavior.
- Run small training runs as part of environment design, because some problems only surface once RL is actually running.
- For hint-based distillation, use a judge to pick the per-step injection point and distill only the next step or a few steps after the hint — the KL signal decays with distance from the hint.
- Mask which teacher tokens the student learns from with an LLM judge, to strip the teacher's irrelevant connector-word preferences and reduce catastrophic degradation.
- Keep most of the mid-training mix representative of the pre-training distribution when domain-adapting; better domain data in mid-training makes an unchanged post-training harness two to three times more effective.
- Repeat high-quality data rather than showing additional low-quality data, up to some threshold.
- Derisk a hero run with small-scale runs on curated data under simulated token scarcity, at 50–100x less compute.
- Over-provision a warm sandbox pool with a demand-based autoscaler — sandbox compute is two to four times cheaper than GPU time, so redundancy still saves money by keeping GPU workers fully utilized.
- Replace Jinja chat templates with programmable renderers to eliminate trainer/inference mismatch at scale.
- Train separate RL experts on a shared base model and distill them into one checkpoint rather than training a single model across many environments at once.
- Budget concretely: a 1,000-step GLM-5 run on 28 nodes over long-horizon coding tasks at 131K context takes ~3 days and ~$50K; a competitive open-frontier-class model is achievable for under $20M all-in.

**Avoid:**

- Filtering timed-out rollouts out of training — it incentivizes the model to deliberately abuse tool calls to time out the sandbox on hard problems and dodge a zero reward.
- Tolerating infrastructure defects that have no presence in the reward function: a ~10% tool-call failure rate silently drives the model toward shorter and shorter responses.
- Assuming every task comes with a golden answer or a beautifully golden rubric — most production distillation has neither.
- Reward-shaping for a specific output format, or SFT on correctly-formatted traces alone: both degraded general coding-agent performance on out-of-distribution behaviors.
- Applying one fixed offline hint uniformly across rollouts — per-rollout online hints moved correct hyperlink formatting from ~15% to ~80%, versus a small climb offline.
- Leaking the solution into the hint (the OPSD analogue of reward hacking), which produces reasoning traces that can never occur in production.
- Synchronous RL training — agent rollouts have long tails, and forward progress should not be tied to the slowest individual rollout.
- Letting chain-of-thought grow without bound; models will keep extending it unless reward design actively counteracts it.
- Treating production logs plus feedback as a learning environment — they are one instance of what happened, not a replayable simulation with defined grading.
- Giving agents tools that search prior trajectories or archives, which teaches retrieval of previous answers instead of reasoning.
- Cranking the MoE load-balancing coefficient late in SFT to paper over a pre/post-training distribution mismatch, rather than fixing the early data mix.
- Coupling training, inference, and environments into a single stack, which forfeits the ability to run the same environments as standalone evals.
- 'Trace-to-harness' fixes where a coding agent reads a log and edits the agent — untestable, vibe-based, and a source of hidden regressions.
- Relying on public benchmarks or vendor brand for model selection instead of your own eval; benchmaxing has made published results hard to interpret.

## Notable Outliers

- Both RLHF and RLVR are the wrong objective — the next post-training paradigm optimizes for calibrated decision-making, with a different API shape from either, because hallucination is intrinsic to preference optimization via a GAN-like mode-dropping asymmetry in the reward model. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [16:08](https://www.youtube.com/watch?v=cJ0EOzey--o&t=968s))
- GRPO saturates around Sonnet-level performance on LiveCodeBench and does not push the frontier; on-policy self-distillation shifts entire distributions rather than sharpening one, and reduces the tokens needed to solve hard problems instead of increasing them. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [10:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=650s))
- A teacher can move a student toward calling a tool purely by reshaping the reasoning path, without ever modifying the tool-call tokens themselves — task-complete call rate went from ~22% to ~60% with test pass rate held steady. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s))
- Post-trained open-source models beat frontier models at writing normalized enterprise process flows, because they learn which details the client cares about — something frontier models have no concept of. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [16:40](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1000s))
- Web text has fallen from ~85% of GPT-3's training mix to ~15% in MAI Thinking 1, and base models have shifted from encoding human knowledge and world priors to encoding reasoning and agentic behavior priors — supervised learning now exists to build representations for RL. ([The Base Model Is Dead](../talks/the-base-model-is-dead.md), [16:17](https://www.youtube.com/watch?v=xbPriQWXtWM&t=977s))
- Fewer than roughly 5,000 people in the world know how to train frontier models at scale, and because agentic and post-training compute does not require co-located GPUs, that tacit knowledge — not hardware — is the exploitable bottleneck. ([Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [13:58](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=838s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)
- [Everything Is a Rollout](../talks/everything-is-a-rollout.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
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
- [Samuel Denton](../speakers/samuel-denton.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Shafik Quoraishee](../speakers/shafik-quoraishee.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Will Brown](../speakers/will-brown.md)

