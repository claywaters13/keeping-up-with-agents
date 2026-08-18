---
title: "continual learning"
type: "concept"
slug: "continual-learning"
tier: "core"
maturity: "frontier"
talk_count: 15
speaker_count: 21
---

# continual learning

**Maturity: FRONTIER** — Frontier — too new or sparse for consensus yet

*Core concept* &middot; discussed across **15** talk(s) by **21** speaker(s)

**Definition:** Systems that keep improving after deployment by incorporating new experience — through weights, memory, or artifacts — rather than being frozen at training time.

*Also referred to as: continual learning for agents, continual learning from traces, continual learning loops, last mile learning, harness learning, compounding learning loops, parametric vs non-parametric learning*

## State of Practice

The field has converged on the framing but not the method: everyone agrees a frozen checkpoint plus a static prompt is the wrong end state, and that the raw material for improvement is the trace exhaust of deployed agents rather than curated human data. The dominant practical stack is production traces → reconstructed replayable environments with explicit graders → an update applied at the cheapest sufficient layer (memory, skill/context artifact, prompt, harness, then weights), gated by a regression check. The hard, unsolved parts are all measurement and environment problems, not modeling problems: how to build environments with enough fidelity that the model does not learn artifacts of the sandbox (a 10% tool-call failure rate silently shortened responses; a too-polite simulated user produced a fake 90% pass rate), how to isolate learning from base-model strength (Berkeley's proposed `gain` = stateful minus stateless reward), and how to fix a new failure without breaking an old one at sublinear cost in accumulated history. Several speakers said outright that nobody is doing real continual learning yet — Trajectory calls the current state 'pseudo continual learning' (offline batch updates, re-upload the model), Mastra says the industry has not figured out the right approach, and Engram notes the paradigm does not even have an agreed name. The most-cited strategic claim is that raw intelligence has stopped being the binding constraint: several independent talks argued that frontier models are already smart enough and that accumulated, situated expertise — private context the model can only acquire after deployment — is the scarce input.

## Consensus

### Deployed production traces, not curated benchmarks or purchased human data, are the primary raw material for post-deployment improvement.

Support: **7** talk(s)

> "what we found is super helpful is taking existing traces from a deployed agent and treating these as the source material"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [9:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=581s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

### Raw logs and feedback are not directly learnable; they must first be lifted into replayable environments with explicit grading before any change can be verified.

Support: **4** talk(s)

> "Here we have log and feedback, but what we really need is a replayable learning environment, a simulation that we can rerun with defined grading on what success looks like, not one instance of what happened and the feedback on top of it."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [3:57](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=237s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)

### An update is only acceptable if it is verified not to regress previously working behavior; forgetting/stability-plasticity is the central failure mode, not a corner case.

Support: **5** talk(s)

> "each of these skills is learning and evolving, uh but every time they learn and evolve, it breaks something downstream."
>
> — [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [14:47](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=887s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)

### Model intelligence is no longer the binding constraint; situated, private, post-deployment context/expertise is the scarce input.

Support: **6** talk(s)

> "This will be a new dimension for us to scale because intelligence is already becoming abundance. The frontier models they are probably smarter than average humans. But expertise is still scarce."
>
> — [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [17:33](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=1053s)

Supporting talks: [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

### Environment/simulator fidelity is the dominant practical failure mode: imperfections with no presence in the reward still induce systematic behavior changes and inflated scores.

Support: **5** talk(s)

> "it's very, very difficult to like perfectly simulate reality and sort of any mistake that you make, even if it's not intentional, will end up inducing these like subtle undesirable behaviors in your model"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [8:25](https://www.youtube.com/watch?v=k35LeKZEhiE&t=505s)

Supporting talks: [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)

### Many of the most useful post-deployment updates happen outside model weights — in memory, skills/context artifacts, prompts, and the harness.

Support: **5** talk(s)

> "The first one is agent continual learning is not necessarily model fine-tuning. The updates and many useful updates can happen in the harness and memory layer."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)

### Current benchmarks and eval practice measure point capabilities on independent instances and therefore cannot measure continual learning at all.

Support: **4** talk(s)

> "what we've done is we've kind of told the models, imagine that every time you do something, you completely forget your memory."
>
> — [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [0:52](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=52s)

Supporting talks: [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)

## Disagreements

### Should learning signal be generated by training in the real production harness, or by building simulated/learned environments?

| Position A | Position B |
|---|---|
| Stop trying to simulate reality — train inside the customer's actual harness, requiring only a completion endpoint plus request/response recording, because the deployed agent already embodies the exact environment distribution. Removing the parallel-rollout requirement (OPSD) also removes the need for one-to-one environment copies, which are themselves a source of bias.<br>*[Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)* | Production is not a learning environment. Lift logs into replayable simulations with deterministic evaluators, and prefer learned simulators over real back ends precisely because full controllability lets you plant answers, guarantee solvability, and build in regression traps.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* |

*Why it matters: This determines whether the expensive engineering investment goes into environment/simulator construction and grading infrastructure, or into on-policy training plumbing that hooks directly into live serving. It also decides whether you can verify a fix before shipping it, or only observe its effect after.*

### Is non-parametric continual learning (memory, context artifacts, skills, harness) sufficient, or must weights change?

| Position A | Position B |
|---|---|
| Keep the base model frozen. The cheapest durable change at the right layer — memory write, skill edit, prompt/code optimization, harness change — captures most of the value, and context should live outside any model or framework so it survives migrations.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)* | Layering methods on top of frozen checkpoints is a sunk cost fallacy; markdown-file memory is a stopgap that degrades as context grows. Gradient-based updates are required — either co-designed architecture/data/algorithms, or on-policy self-distillation into weights — and both parametric and non-parametric mechanisms are needed for it to actually work.<br>*[Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)* |

*Why it matters: It decides whether continual learning is an application-layer infrastructure problem solvable by product teams today, or a pretraining-stack problem that requires retraining models with continual learning as a first-order design requirement. It also changes who owns the improvement loop: the agent platform or the model lab.*

### Should the improvement loop be human-gated, or autonomous with humans reserved for top-level goals?

| Position A | Position B |
|---|---|
| A human maintainer must approve or reject each learning before it lands; expert feedback is low-volume but critical for domain knowledge and alignment, criteria must be discovered by hand-grading raw data, and sensitive regions must be declared permanently off-limits to adaptation.<br>*[WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* | Human-in-the-loop curation per failure mode is unwinnable Whac-A-Mole. Automate environment and reward refinement with compute, surface only the highest-level judgments to humans, and treat recommendations-only autonomy as a defensible interim position but the wrong long-term target.<br>*[Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)* |

*Why it matters: Human approval caps the learning rate at human review throughput, which is fatal if the goal is merging signal from thousands of concurrent rollouts; removing it moves the entire safety burden onto automated regression detection and blast-radius containment.*

### Is GRPO-style RL the right vehicle for continual learning, or a dead end for production settings?

| Position A | Position B |
|---|---|
| GRPO's requirement of many parallel rollouts per prompt cannot be satisfied in real production (you cannot re-run a customer support chat eight ways), it saturates around Sonnet-level performance on LiveCodeBench, and it collapses all reward into one scalar when the real world is messy. On-policy self-distillation from a hint-privileged teacher works from a single example and has surpassed RL at 12B with 100+ tool calls.<br>*[Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)* | RL works if you invest in environment design: reverse-engineer tasks from traces, work backwards from reachable end states, calibrate difficulty so rollouts separate, judge in hindsight, and run an online generate/solve/synthesize loop gated on pass rate — which produced large uplift on tool-use benchmarks. Self-improvement of the training distribution, the AlphaGo mechanism, is the missing ingredient rather than the problem.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md)* |

*Why it matters: Betting on RL means building environment and reward infrastructure as the core asset; betting on distillation-style methods means building teacher/hint design and divergence control instead. The two stacks share almost no components.*

## Practical Guidance

**Do:**

- Report gain (stateful reward minus stateless reward) alongside cumulative reward and cost, on Pareto frontiers — cumulative reward alone confounds learning ability with base model strength
- Require three properties of any continual learning environment: headroom, shared latent structure across instances, and an in-environment learning signal (scalar reward, error messages, or textual feedback)
- Fine-tune your user simulator on real user verbatim until evaluation scores go down, and treat the falling score as evidence the eval got more realistic
- Validate LLM judges like binary classifiers: hand-label ~100 examples pass/fail, split train/dev/test, score precision and recall, and use the data to inform the judge prompt rather than to train a model
- Make the smallest durable change at the right layer — memory write (cheapest), then prompt/harness, then weights (most expensive); use LoRA when weights must change, to bound what can shift
- Put regression prevention inside the optimization objective as a constraint (fix recent failures subject to no regression on past environments), and keep its cost sublinear in the number of accumulated past environments
- Judge in hindsight after seeing the full chain of events, or by polling several models — this catches most reward hacks, while instructing a judge in advance not to allow a behavior does not prevent it in the rollout
- Calibrate generated tasks to intermediate difficulty and keep searching for more of them, since the advantage signal depends on separation across rollouts
- Run small training runs as part of environment design, because some problems only surface once RL is actually running
- Fix input/output interfaces around repeated AI tasks so models and techniques can be swapped inside a stable contract (Shopify got a 550x cost reduction by swapping models with evals held fixed)
- Enforce hard constraints in code rather than in the prompt, and declare regions like auth and payments permanently off-limits to adaptation while leaving things like form layout adaptable
- Store context outside any specific agent framework, versioned like code with owners, approvers, dependency tracking, and impact analysis — agent tooling churns roughly annually and trapped context is lost at each migration
- Give the model privileged hints in the prompt to act as its own teacher, removing the dependency on a stronger model to distill from
- Run evals continuously — locally, at pre-commit, and in CI/CD as a regression suite — from a config-driven (YAML) harness that analysts can edit

**Avoid:**

- Chaining independent benchmark instances together and calling it a continual learning benchmark — they share no structure to exploit, so improvement is impossible by construction
- Shipping an LLM judge whose score does not gate any development or production decision
- Prompting an LLM to generate ~50 test queries as your offline eval set instead of sampling and mutating production traffic
- Using off-the-shelf frontier models as user simulators — they are trained to be helpful and produce unrealistically polite complaints (this yielded a fake 90%+ pass rate at Lyft)
- Trace-to-harness fixes where a coding agent reads a log and edits the agent: the change is untestable even on the sample that motivated it, and introduces hidden regressions
- Treating regression checking as a post-hoc pass rather than a mechanism inside the optimization
- Plain next-token-prediction finetuning on your private corpus — loss goes to ~0.0001, generation collapses, and nothing generalizes
- Assuming any fixed-dataset approach scales: unless the model is underparameterized it eventually learns all the data and saturates, including synthetic data
- Filtering timed-out rollouts out of training — it incentivizes the model to deliberately abuse tool calls to trigger sandbox timeouts and dodge a zero reward
- Leaking the solution in an OPSD hint (the analogue of reward hacking): it produces reasoning traces that can never occur in production
- Per-agent memory systems — they cause context sprawl, prevent a single version of truth, and make it impossible to trace whether a failure was the model, the agent, or the context
- Generic pre-built metrics (helpfulness, toxicity, conciseness) as core metrics — a helpfulness score of 0.5 is not actionable; use binary pass/fail tied to business outcomes
- Reporting an 84% vs 88% alignment difference on 50 traces as a real gain — every score needs an interval
- Per-failure-mode post-training, which is Whac-A-Mole: each new failure forces new data and new environments
- Shipping to live users as the test set before an offline evaluation gate exists

## Notable Outliers

- Vanilla in-context learning topped Continual Learning Bench 1.0 — beating more expensive context-management systems on reward and holding across both the reward-vs-cost and gain-vs-cost Pareto frontiers — though the speaker believes this is a medium-horizon artifact, not the end state. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s))
- Building continual learning methods on top of already-trained checkpoints is a sunk cost fallacy; if continual learning were a first-order design requirement, the whole multi-stage training stack could collapse into one learning phase followed by deployment. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [17:37](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1057s))
- Past a certain threshold of raw intelligence, more intelligence becomes unnecessary and the continual learning algorithm becomes the binding constraint — 'unbounded expertise from bounded intelligence' — and current frontier models may already be past that threshold. ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s))
- An infrastructure defect with zero presence in the reward function — networking issues causing ~10% tool-call failures — systematically drove the model to output shorter and shorter responses. ([Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [7:03](https://www.youtube.com/watch?v=k35LeKZEhiE&t=423s))
- Nobody, including the speaker's own company, is close to true continual learning; the field is doing 'pseudo continual learning' with offline batch updates and model re-uploads, and merging signal from ~10,000 concurrent production rollouts into a single update is an unsolved infrastructure and algorithmic problem. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [20:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1250s))
- Continual learning will require updating weights on local hardware; markdown-file agent memory is only a stopgap because context length becomes inefficient. ([State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [31:31](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=1891s))
- The unit of propagation for a self-adapting system should not be code: deploy one canonical stem, let every user run their own immutable divergence, and merge intent and outcome rather than commits. ([The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [17:11](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=1031s))
- GRPO saturates around Sonnet-level performance on LiveCodeBench and does not push the frontier, while on-policy self-distillation shifts entire distributions and reduces the tokens needed to solve hard problems rather than increasing them. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [10:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=650s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)
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
- [Sara Hooker](../speakers/sara-hooker.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Will Brown](../speakers/will-brown.md)
- [Yu Su](../speakers/yu-su.md)

