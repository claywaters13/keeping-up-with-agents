---
title: "benchmark design"
type: "concept"
slug: "benchmark-design"
tier: "core"
maturity: "consolidating"
talk_count: 18
speaker_count: 25
---

# benchmark design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **18** talk(s) by **25** speaker(s)

**Definition:** Constructing a benchmark that measures what it claims to — task selection, difficulty calibration, discrimination, and holdout discipline.

*Also referred to as: agent benchmark design, agentic benchmark design, held-out private benchmarks, internal benchmarks, difficulty calibration, item response theory, private domain benchmarks*

## State of Practice

This conference treated benchmark design as an engineering discipline with catalogued failure modes, not an academic exercise. The dominant position is that public leaderboards are contaminated, saturated, and weakly verified — an audit of SWE-Bench Pro found it accepts wrong implementations on 8.5% of tasks and rejects correct ones on over 24% — so any team shipping agents is expected to build a private benchmark over its own domain, from novel or production-trace-derived tasks, with a real holdout. Task admission now has explicit gates: an oracle run proving the task is solvable and establishing the performance ceiling, an adversarial pass where the authors try to reward-hack their own environment before any agent sees it, difficulty calibrated to intermediate pass rates, and verification of final environment state, trace, and artifacts rather than just the model's output string. Reporting has moved past pass rate to cost, latency, retries, gain over a stateless baseline, and item-level psychometrics — item response theory was shown to separate two models differing by 2 correct answers out of 337 by nearly a full standard deviation of estimated ability, and to surface negatively-discriminating items that turn out to have mislabeled gold answers. Environments and evals are converging on one artifact (sandbox → agent → verifier → reward) reused for evaluation, SFT collection, RL, and release gating, which makes the benchmark repo software that needs pinned dependencies and its own CI. What remains genuinely open is where evaluation should happen — simulation is controllable but agents detect it — and how much credentialed human labor per task is unavoidable.

## Consensus

### Public benchmarks are for orientation only; any team shipping agents must build its own private benchmark over its own tools, data, and policies, because that is the only basis for model selection.

Support: **5** talk(s)

> "public benchmark is useful to orient and build your prior, but your private benchmark is useful to ship."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [3:11](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=191s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### Contamination is assumed by default and must be actively engineered against — novel or private tasks, held-out splits, deleted Git history, network allowlists, and API boundaries that make test data unreachable from training.

Support: **6** talk(s)

> "we have this private eval set that is mostly made up of things that happen in our code base which is held out from the evals so we ensure that the models aren't trained on it"
>
> — [Recursive Model Improvement](../talks/recursive-model-improvement.md), [7:53](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=473s)

Supporting talks: [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)

### Reward hacking is a defect in the benchmark, not the model, and tasks should be attacked adversarially by their own authors before admission to the dataset.

Support: **6** talk(s)

> "before we test a task against any agent, we first try to break the environment ourselves"
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s)

Supporting talks: [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### A task is only valid if its difficulty is calibrated and its ceiling is demonstrated — construct an oracle or upper-bound run to prove solvability, target intermediate pass rates, and retire tasks that are saturated or unreachable.

Support: **6** talk(s)

> "you want tasks that are not too easy, not too hard and you want to be searching for these and iterating on generating more of them"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [14:08](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=848s)

Supporting talks: [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

### A single success-rate number is an inadequate benchmark output; cost, latency, retries, gain over a stateless baseline, state understanding, and distribution shape must be reported alongside it.

Support: **6** talk(s)

> "you can compare agents using different metrics, not just success rate, but cost, latency, and retries."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [2:22](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=142s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md)

### The grader is itself a major error source and must be audited — weak verifiers that assert unspecified internals, mislabeled gold answers, and path-dependent rubrics silently corrupt results.

Support: **4** talk(s)

> "the test is basically checking functions that are unexported. So, if that was a PR in any of our projects, and exposed these type of tests, we would not accept it. So, this is what a weak verifier looks like."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [6:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=387s)

Supporting talks: [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)

### Benchmarks measure the full agent system — harness, tools, retrieval, and memory policy — not the model; swapping a scaffold component moves scores by margins comparable to changing models.

Support: **5** talk(s)

> "So we see that the models are extremely capable if they would get the right documents but if you put them into the noisy corpus the performance drops sharply. Meaning that actually the bottleneck here is not the reasoning. It's actually the access to the right knowledge it needs to answer this question."
>
> — [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [2:25](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=145s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md)

## Disagreements

### Can a simulated environment validly measure agent behavior, or does simulation awareness impose a ceiling that forces evaluation into real deployments?

| Position A | Position B |
|---|---|
| Build simulations faithful and controllable enough that the agent cannot tell — a snapshot database, sidecar containers, an LLM standing in for the user. Learned simulators are actually preferable to production systems, because full back-end control lets you plant the answer and guarantee solvability.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* | Models already detect simulation and behave differently, so behavioral and safety evals in sandboxes are structurally compromised. The fix is to run agents in real deployments and fork them into simulation mid-trajectory, and to expect real-life evals to dominate simulated ones.<br>*[Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)* |

*Why it matters: It decides whether safety and misbehavior results from sandboxed benchmarks can be trusted at all, and whether eval budget goes into simulation fidelity or into instrumented, non-reproducible real-world deployments.*

### Should benchmark tasks be harvested and synthesized from deployed production traces, or hand-authored as novel tasks by domain experts?

| Position A | Position B |
|---|---|
| Mine deployed agent traces as source material and generate tasks online, gating on pass rate. A handcrafted set of a few hundred expert-built tasks is not a scalable basis for open-ended real-world work, and the benchmark should be a continuously repopulated dataset rather than a static artifact.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)* | Tasks must be novel and authored and reviewed by humans, expressing objectives and hard constraints rather than implementation details. This is expensive — biology tasks took a group of three people about a week each — but it is what makes tasks contamination-free and trustworthy.<br>*[Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)* |

*Why it matters: It sets cost per task by two orders of magnitude and determines whether the benchmark can grow with model capability; trace-derived sets inherit the real production distribution but also its blind spots, while hand-authored sets are novel by construction but stay small enough to saturate.*

### Who defines what 'correct' means on a benchmark task — a credentialed domain expert on every case, or automated judges with humans reserved for the top of the stack?

| Position A | Position B |
|---|---|
| A licensed or credentialed expert owns the definition of good, and that judgment is committed into CI so every prompt, model, and guardrail change is scored against it. In science, having scientists grade each other's work is the best available proxy for ground truth and is what exposes badly specified tasks.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)* | Reserve humans for the highest-level judgments about goals and quality and let compute handle the rest of environment refinement; route subject-matter experts only to cases where the agent and the verifiers disagree, rather than reviewing everything.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)* |

*Why it matters: Expert-per-task review caps benchmark throughput and therefore coverage of the long tail, while selective review risks locking in whatever the judge models already get wrong — a tradeoff that is acceptable in tool-use benchmarks and unacceptable in clinical or biosafety ones.*

### Is a published ranked leaderboard the right primary output of a benchmark?

| Position A | Position B |
|---|---|
| Publish the leaderboard and get frontier labs to compete on it; lab competition on your benchmark directly improves the models your product depends on, and a flat leaderboard is itself an informative signal about a capability frontier.<br>*[Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)* | Leaderboards report who won without saying why; the benchmark should surface underlying run data and diagnostics, be judged by whether a community merges and builds on the work, and explicitly not be optimized to perfection.<br>*[Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)* |

*Why it matters: If the leaderboard is the artifact, benchmark authors optimize for a clean scalar and labs optimize against it; if diagnostics are the artifact, the benchmark must ship trajectories, Pareto frontiers, and failure taxonomies, which is a different engineering investment.*

## Practical Guidance

**Do:**

- Write an oracle solution for every task before admitting it, to prove the task is solvable and to establish the performance ceiling the benchmark is measuring against.
- Try to reward-hack your own environment before any agent touches it, and admit only tasks that survive that pipeline.
- Delete Git history at the start of a run (restoring it after) and enforce a network allowlist, or public-eval scores will overstate capability.
- Retire any eval where all models score around 90%, and treat eval creation as a continuous investment because eval half-life shrinks as models improve.
- Report gain — stateful reward minus stateless reward — not just cumulative reward, so learning ability is isolated from base model strength, and plot reward, gain, and cost as Pareto frontiers.
- Verify final environment state, execution trace, and produced artifacts, not just the agent's output text.
- Decompose long-horizon tasks into steps with a separate prompt and verifier per step, with early termination on failure, since end-to-end outcome grading is too sparse a signal at current model ability.
- Run the benchmark repo through its own CI pipeline: pinned dependencies, base images, missing fixtures, and an oracle pass on every task.
- Use item discrimination to prune the benchmark — one 484-item set compressed to ~97 items while preserving 99% ranking correlation — and treat negatively-discriminating items as evidence of a mislabeled gold answer.
- Keep a held-out split (80/20 was offered as a default) that the agent has not seen during experimentation, plus per-organization fingerprint item sets to detect leakage.
- Make graders path-invariant: check that every valid solution path a competent practitioner could take still passes.
- Catch reward hacks by reviewing rollouts in hindsight, after seeing the full chain of events, rather than instructing a judge in advance not to allow the behavior.
- Phrase task instructions as desired behaviors, objectives, and hard constraints, and have a human author and review them.
- Route subject-matter expert time to cases where the agent and the verifiers disagree instead of reviewing every trace.

**Avoid:**

- Instructions that name the test file or hand the agent the full implementation interface — both leak the answer and invalidate the task.
- Tests that assert unspecified variable names or exercise unexported functions; these would fail code review in a real project and produce false negatives at scale.
- Two-page task prompts — SWE-Bench Pro instructions average 481 words, which is not how engineers actually prompt.
- Chaining independent benchmark instances together and calling it a continual-learning benchmark; independent instances share no latent structure for the agent to exploit.
- Assuming more items means a better ability estimate — overlapping items add almost no information.
- Counting raw correct answers as a capability measure, which is classical test theory and treats every item as equally important.
- Using production A/B tests as a substitute for a benchmark: database state and tool versions differ between runs, so it is never apples-to-apples.
- Fixing observed failures by adding prohibitions to the prompt instead of the harness, skills, or structured output.
- Building tasks out of public GitHub repositories, which are already in the training distribution.
- Entity-based 'caveman style' queries in retrieval benchmarks (BEIR, NanoBEIR), which structurally favor BM25 and train agents into keyword-stuffing behavior.
- Trusting rubric scores that are only loosely correlated with verifiable outcomes as an RL or benchmarking signal.
- Pursuing perfect benchmark scores, which shifts focus away from the humans the benchmark exists to protect.
- Running more synthetic-persona samples on unchanged inputs to boost statistical significance — it improves your estimate of the model, not the accuracy of the forecast.

## Notable Outliers

- Two models separated by 2 correct answers out of 337 (Claude Opus 4.1 at 245, Gemini 3 Pro at 247) differ by almost a full standard deviation in item-response-theory-estimated ability — the raw count hides the gap entirely. ([Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [6:38](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=398s))
- SWE-Bench Pro accepts wrong implementations on 8.5% of tasks and rejects correct implementations on over 24% — the grader error rate is larger than most reported model differences. ([Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [5:30](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=330s))
- A long-horizon business eval detected a training-recipe regression: Opus 4.8 scored much worse than Opus 4.7 because a business-skills component had been removed from post-training. ([Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [2:43](https://www.youtube.com/watch?v=cO8qC6HBuBg&t=163s))
- There is a hard ceiling on synthetic-persona accuracy set by human self-inconsistency — one study measured humans as only about 80% consistent with themselves — so ground truth itself must be split in half and correlated against itself to calibrate the benchmark. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [17:03](https://www.youtube.com/watch?v=YnNF55QV0zs&t=1023s))
- Benchmarks should include open-ended tasks with continuous loss functions — e.g. write a lossless compressor for 10MB of data, scored on compressed size plus source size — rather than binary pass/fail on whether code runs. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [14:49](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=889s))
- Standard retrieval benchmarks are not just mismeasuring but actively mis-training: entity-based queries that favor BM25 teach agents to write keyword-stuffed queries they then carry into real knowledge work. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s))

## All Talks

- [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [Everything Is a Rollout](../talks/everything-is-a-rollout.md)
- [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)
- [From Tokens to Cells: Foundation Models for Single-Cell Biology](../talks/from-tokens-to-cells-foundation-models-for-single-cell-biology.md)
- [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)
- [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)
- [Recursive Model Improvement](../talks/recursive-model-improvement.md)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)
- [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)
- ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)
- [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md)
- [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)
- [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

## Speakers

- [Akele Reed](../speakers/akele-reed.md)
- [Akram Baharlouei](../speakers/akram-baharlouei.md)
- [Alex Shaw](../speakers/alex-shaw.md)
- [Ali Khial](../speakers/ali-khial.md)
- [Benoit Schillings](../speakers/benoit-schillings.md)
- [Chengxi Taylor](../speakers/chengxi-taylor.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Dillon DuPont](../speakers/dillon-dupont.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Francesco Bonacci](../speakers/francesco-bonacci.md)
- [George Cameron](../speakers/george-cameron.md)
- [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)
- [Ishan Anand](../speakers/ishan-anand.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Lukas Petersson](../speakers/lukas-petersson.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Niv Granot](../speakers/niv-granot.md)
- [Parth Asawa](../speakers/parth-asawa.md)
- [Ross Taylor](../speakers/ross-taylor.md)
- [Rustem Feyzkhanov](../speakers/rustem-feyzkhanov.md)
- [Ryan Marten](../speakers/ryan-marten.md)
- [Stefania Druga](../speakers/stefania-druga.md)
- [Will Brown](../speakers/will-brown.md)
- [Yuval Belfer](../speakers/yuval-belfer.md)
- [Zubin Aysola](../speakers/zubin-aysola.md)

