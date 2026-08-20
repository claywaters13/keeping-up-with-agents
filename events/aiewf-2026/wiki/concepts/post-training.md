---
title: "post-training"
type: "concept"
slug: "post-training"
tier: "supporting"
maturity: "contested"
talk_count: 23
speaker_count: 29
---

# post-training

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **23** talk(s) by **29** speaker(s)

**Definition:** The stage after pre-training — SFT, RL, and mid-training — where task behavior is shaped, treated as its own engineering pipeline.

*Also referred to as: model post-training, post-training pipelines, post-training objectives, reinforcement learning post-training, mid-training, post-training scaling, task-specific fine-tuning*

## State of Practice

Post-training has stopped being a finishing step and become the main axis of capability: with pre-training scale seen as saturated at the current architecture, speakers describe teams moving post-training data and objectives earlier (agentic traces and chat-shaped data pulled into pre/mid-training) while spending the bulk of the marginal compute budget on RL and distillation. The unit of work is the environment, and the field now treats environments and evals as the same object — a sandbox, an agent, a verifier, a reward — so building your eval is the on-ramp to training, and one environment serves RL, SFT generation, on-policy distillation, and prompt optimization. The dominant raw material is deployed production traces rather than handcrafted benchmarks, but nobody thinks a log is trainable as-is: it must be lifted into something replayable and gradeable, or paired with privileged information (a hint, a planted answer, a hindsight judge) to manufacture a teacher stronger than the on-policy model. Reward hacking and environment fidelity are understood as one problem — a ~10% tool-call failure rate silently shortens responses, filtering timed-out rollouts teaches the model to time out sandboxes — so environments get adversarially attacked before tasks are admitted. Economically, post-training has come within reach of ordinary teams: a 1,000-step GLM-5 RL run on real agentic coding tasks costs roughly $50K, a specialized open model can beat Opus on a finance task at a fraction of Haiku's price in one to two weeks, and multiple speakers report frontier-competitive narrow models for high six figures to low millions. The unsolved parts are the algorithm (GRPO's parallel-rollout requirement does not survive contact with single-shot production interactions), non-verifiable rewards, and merging thousands of concurrent production rollouts into one update — which everyone concedes is still batch, offline, pseudo-continual learning.

## Consensus

### Deployed production traces, not handcrafted benchmark suites, are the primary source material for post-training data — but they must first be converted into something replayable or gradeable.

Support: **7** talk(s)

> "what we found is super helpful is taking existing traces from a deployed agent and treating these as the source material"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [9:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=581s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)

### Post-training, not additional pre-training scale, is now the decisive lever on model quality; the base model is a prior for RL rather than the main source of capability.

Support: **6** talk(s)

> "what you will see in pre-training is instead of the size people are just moving post-training further back, which is very fascinating and a bigger lever."
>
> — [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [19:19](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1159s)

Supporting talks: [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md)

### Reward hacking is a defect of the environment and its proxy objective, not model misbehavior: any infrastructure imperfection or boundary the reward leaves undefined will be found and exploited.

Support: **6** talk(s)

> "And the main sort of problem is like has kind of two names, which are both the same problem, environment fidelity and reward hacking."
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [7:03](https://www.youtube.com/watch?v=k35LeKZEhiE&t=423s)

Supporting talks: [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)

### Environments and evals are the same artifact, so building the eval is the prerequisite and on-ramp to post-training — the same environment then serves RL, SFT generation, distillation, and prompt optimization.

Support: **5** talk(s)

> "evals are the thing that opens the door to post-training. And so environments and evals are essentially the same thing."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [6:37](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=397s)

Supporting talks: [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)

### A post-trained smaller or open model beats a frontier model on a narrow production task, at one to two orders of magnitude lower cost, on a timescale of one to two weeks.

Support: **5** talk(s)

> "take an open model and like specialize it to automate finance within like a week or two to get like better performance than like Opus at a fraction of the cost of Haiku"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [13:39](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=819s)

Supporting talks: [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [The Desktop Frontier](../talks/the-desktop-frontier.md)

### The field is over-indexed on verifiable domains (math, code, tests); the remaining value and the hard open problems are in non-verifiable, open-ended tasks with no answer key.

Support: **5** talk(s)

> "First, I believe now the AI industry is a little bit too biased towards coding and procedure task."
>
> — [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

### Capability gaps are data gaps: curation and data-mix design, not architecture or raw compute, are the binding constraint, and better upstream data multiplies the effectiveness of an unchanged post-training pipeline.

Support: **5** talk(s)

> "the gap in models is usually a gap in data. Models typically are only as good at as data is."
>
> — [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [2:20](https://www.youtube.com/watch?v=zkX03APVj0M&t=140s)

Supporting talks: [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)

## Disagreements

### Should production post-training happen inside a built simulation of the task, or directly inside the customer's real harness and real infrastructure?

| Position A | Position B |
|---|---|
| Build the environment: production logs are not learning environments, so lift them into replayable simulations with explicit evaluators — and learned simulators are actually preferable to real systems because full back-end controllability lets you plant the answer and guarantee solvability.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)* | Stop simulating: perfect simulation is infeasible and every fidelity gap induces subtle undesirable behavior, so train inside the customer's black-box production harness (model completion endpoint plus request/response recording) or in multi-node sandboxes provisioning real cloud resources.<br>*[Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)* |

*Why it matters: It decides whether your post-training investment goes into simulator/evaluator engineering or into orchestration that trains against live systems, and it changes what you can verify: simulators give guaranteed-solvable, regression-testable tasks, while real harnesses give distributional truth but non-replayable, off-policy data.*

### Is group-relative RL over parallel rollouts (GRPO) the right workhorse for improving deployed models, or must production post-training learn from a single non-replayable interaction?

| Position A | Position B |
|---|---|
| Keep RL and fix the infrastructure around it — go async, tolerate ~8–16 steps of off-policy staleness, use value models or pipeline RL for long horizons, and accept that a proper frontier-scale agentic run is now a ~$50K, three-day job.<br>*[Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md)* | GRPO's requirement of many rollouts per prompt is unsatisfiable in real settings like a customer support chat and forces environments to be one-to-one copies of the world; use teacher-hint self-distillation that learns from a single trace by matching student log-probs without the hint to teacher log-probs with it.<br>*[Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)* |

*Why it matters: The two paths need different infrastructure (rollout fan-out and reward plumbing versus hint construction, judges, and per-step KL masking) and have different failure modes — reward hacking versus hint leakage — so committing early determines which one your team has to learn to debug.*

### Should a team touch weights at all, or exhaust harness, prompt, and memory changes first?

| Position A | Position B |
|---|---|
| Post-train: the harness is where capability is being left on the table only because the model was never fitted to it, so take the best open model and post-train it on the harness you care about — and for tiny edge models fine-tuning on 10k–10M synthetic samples is mandatory, not optional.<br>*[Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)* | Make the smallest durable change at the right layer: continual learning is not necessarily fine-tuning, harness engineering has a roughly two-minute feedback loop against weeks for weights, and plain error analysis over observability logs is the cheapest, highest-ROI improvement — most teams never need to go further.<br>*[Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)* |

*Why it matters: It sets whether a team staffs and budgets a training stack (GPUs, environments, rollout infra) or an observability-and-iteration stack, and it changes the recurring cost profile — fine-tuning must be redone on every new base model release, while harness changes port forward.*

### Can an LLM judge or rubric serve as the reward signal when the task has no answer key?

| Position A | Position B |
|---|---|
| Yes, if you judge in hindsight rather than in advance: judges are powerful general reasoners, hindsight review over the full chain of events catches most reward hacks, and a judge can also pick where to inject hints and mask which teacher tokens are learned from.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)* | No, not in expert verticals: the model produces plausible jargon without understanding the underlying concept, rubrics-as-rewards creates an echo chamber where the AI grades itself into agreement, and optimizing against a preference/judge signal is exactly what makes models confidently wrong.<br>*[Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: If judges work, non-verifiable domains are trainable at compute scale with humans reserved for top-level goal judgments; if they don't, every improvement loop in finance, pharma, and similar fields is gated on scarce, expensive domain experts sitting inside the loop.*

## Practical Guidance

**Do:**

- Build the eval/environment before selecting a model, then reuse the identical environment for RL, SFT generation, on-policy distillation, and prompt optimization
- Keep the harness ignorant that it is doing RL, so the same harness code runs in training and in production
- Run async RL rather than synchronous; ~8 steps (pipeline RL) to ~16 steps (average off-policyness) of staleness is empirically fine and decouples progress from rollout long tails
- Adversarially attack your own environment for reward hacks before admitting a task to the dataset — only tasks that survive the break-it pipeline enter
- Calibrate tasks to intermediate difficulty and keep searching for more of them, since the advantage signal depends on separation across a rollout group
- Judge in hindsight over the full trajectory (or poll several models) instead of instructing a judge in advance not to allow a behavior
- Use a judge to choose where in a rollout to inject a hint, and distill only on the next step or a few steps after it — the KL learning signal decays with distance from the hint
- Mask teacher tokens with an LLM judge so the student does not learn the teacher's connector-word preferences, which reduces catastrophic degradation
- Over-provision a warm sandbox pool with a demand-based autoscaler for RL rollouts; sandbox compute is 2–4x cheaper than leaving GPUs idle on spin-up
- Curate mid-training domain data before post-training — it makes an unchanged post-training harness two to three times more effective
- Repeat high-quality data rather than adding low-quality data, up to some repetition threshold
- Derisk a large run with small-scale runs on curated data under simulated token scarcity, at 50–100x less compute
- Replace Jinja chat templates with programmable renderers to eliminate trainer/inference mismatch at scale
- Start with a frontier model only to establish that the task is possible, then use its traces to port the task onto a cheaper open model
- For tiny (50M–500M parameter) fixed-task models, generate 10k–10M synthetic samples and fine-tune rather than prompting
- Bake regression checks into the optimization objective itself, sub-linearly in the number of accumulated past learning environments, rather than as a post-hoc pass
- Diff base-model against fine-tuned activations with a sparse autoencoder as a per-build unit test for backdoors introduced during fine-tuning

**Avoid:**

- Filtering timed-out rollouts out of training — it incentivizes the model to deliberately time out the sandbox on hard problems to avoid a zero reward
- Ignoring infrastructure defects that have no presence in the reward function; a ~10% tool-call failure rate alone drove systematically shorter model responses
- Assuming every task comes with a golden answer or rubric — most useful continual learning has to work without one
- Applying one fixed offline hint at the start of a rollout; per-rollout online hints took correct formatting from ~15% to ~80% where the fixed hint barely moved
- Leaking the solution into the hint (the OPSD analogue of reward hacking) — it produces reasoning traces that cannot occur in production
- Format-reward shaping or SFT on correctly-formatted traces as a way to induce a behavior; both degraded general coding-agent performance out of distribution
- Editing the agent from a log with a coding agent and calling it fixed — the change is untestable and creates hidden regressions
- Letting chains of thought grow without bound; models will inflate length unless reward design actively counteracts it
- Coupling training, inference, and environments into a single stack, which prevents reusing environments as standalone evals
- Giving agents tools that search prior trajectories or archives — they learn to retrieve the previous answer instead of reasoning
- Single-node containerized sandboxes for infrastructure-ownership tasks; you cannot provision EC2- or Cloud-Run-like resources inside one node
- Per-failure-mode post-training, which is unwinnable Whac-A-Mole as new modes surface
- Cranking the MoE load-balancing coefficient late in SFT to paper over expert imbalance — it is a symptom of pre/post distribution mismatch that belongs in the early data mix
- Trusting public benchmarks or vendor brand for model selection instead of your own eval; benchmaxing makes published results hard to interpret

## Notable Outliers

- Galactica's thinking-token tags already applied RL pressure to internal reasoning in 2022; reflective backtracking failed to emerge only because base models, RL compute, and context windows were too small — not because the objective was wrong. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [7:56](https://www.youtube.com/watch?v=2bvtay8wGYI&t=476s))
- Hallucination and overconfidence are by construction in any RLHF model — a mode-dropping asymmetry in the reward model analogous to GANs — so the next paradigm is neither RLHF nor RLVR but optimization for calibrated decision-making. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [14:35](https://www.youtube.com/watch?v=cJ0EOzey--o&t=875s))
- GRPO saturates around Sonnet-level performance on LiveCodeBench and does not push the frontier, while on-policy self-distillation shifts entire distributions and reduces the tokens needed to solve hard problems instead of increasing them. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [10:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=650s))
- A teacher can move a student toward calling a tool purely by reshaping the reasoning path, without ever modifying the tool-call tokens — task-complete call rate went from ~22% to ~60% with test pass rate holding steady. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s))
- A model competitive with the open frontier can be trained for under $20 million all-in including salaries, compute, and every failed attempt — making the 'hundreds of millions to customize a model' figure false. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [16:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1010s))
- A fine-tuned model can pass every behavioral test and still carry a backdoor; training a sparse autoencoder on the base-to-fine-tuned activation difference scores ~0.4 on backdoor isolation versus ~0.01 for joint-feature crosscoders, with non-overlapping confidence intervals. ([Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [8:12](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=492s))
- Fewer than roughly 5,000 people worldwide know how to train frontier models at scale, and because agentic and post-training compute does not need co-located GPUs, that tacit knowledge is now an exploitable search space for distributed actors. ([Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [13:58](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=838s))
- Only two paradigms actually matter — supervised next-token prediction and RL — and since RL dominates the compute budget, supervised training's job is to build representations and expose the atomic skills RL will later compose. ([The Base Model Is Dead](../talks/the-base-model-is-dead.md), [14:02](https://www.youtube.com/watch?v=xbPriQWXtWM&t=842s))
- Curating only the English portion of a pre-training corpus measurably improves non-English performance, with transfer magnitude correlated to language similarity. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [11:34](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=694s))
- Nobody, including the speaker's own company, is doing true continual learning — the field is doing pseudo continual learning with offline batch updates and model re-uploads, and merging ~10,000 concurrent production rollouts into one update is unsolved. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [20:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1250s))

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
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)
- [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)
- [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Alex Shaw](../speakers/alex-shaw.md)
- [Ari Morcos](../speakers/ari-morcos.md)
- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
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

