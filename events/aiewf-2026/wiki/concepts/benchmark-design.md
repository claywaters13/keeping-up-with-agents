---
title: "benchmark design"
type: "concept"
slug: "benchmark-design"
tier: "core"
maturity: "contested"
talk_count: 20
speaker_count: 27
---

# benchmark design

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **20** talk(s) by **27** speaker(s)

**Definition:** Constructing a benchmark that measures what it claims to — task selection, difficulty calibration, discrimination, and holdout discipline.

*Also referred to as: agent benchmark design, agentic benchmark design, held-out private benchmarks, internal benchmarks, difficulty calibration, item response theory, private domain benchmarks*

## State of Practice

The conference's dominant position is that public leaderboards have stopped functioning as a basis for decisions: their tasks come from public repos, their instructions leak answers, their verifiers both accept wrong solutions and reject correct ones, and models mine Git history and the open web for shortcuts — so the recommendation is that every company build a private benchmark over its own domain, with held-out sets the agent has never seen. Benchmark construction is being reframed as an engineering discipline with its own CI: pinned dependencies and base images, fixture checks, and an Oracle solution proving each task is solvable before admission, plus a red-team pass where the authors try to break their own environment for reward hacks. Reward hacking is treated as a benchmark defect rather than a model defect — a proxy left undefined at the boundaries — and several teams now judge in hindsight over the full trajectory rather than instructing a judge against failures in advance. Pass rate alone is broadly rejected as the reported number; speakers add cost, latency, retries, gain (stateful minus stateless reward), environment-state understanding, and Pareto frontiers, and one team argues classical right-answer counting should be replaced outright by item response theory, which exposes negatively-discriminating items as mislabeled gold answers and compresses a 484-item benchmark to ~97 while preserving 99% of the ranking. What remains genuinely unresolved is where tasks should come from (production traces vs. synthetic construction vs. hand-authored novel tasks), whether simulated environments can support behavioral evaluation at all given simulation awareness, and whether large hand-built eval suites are worth the investment when a harness switch can invalidate 80% of them.

## Consensus

### Reward hacking is a property of the benchmark, not the model; environments must be adversarially attacked and verified before tasks are admitted.

Support: **7** talk(s)

> "before we test a task against any agent, we first try to break the environment ourselves"
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s)

Supporting talks: [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### Pass/success rate alone is an invalid headline metric; benchmarks must report cost, latency, retries, learning gain, or state understanding alongside it.

Support: **6** talk(s)

> "to measure the intelligence of an agent, you can't just measure its ability to successfully perform actions."
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)

### Public benchmarks are useful only for orientation and priors; shipping decisions and model selection require a private benchmark built on your own domain, tools, and policies.

Support: **5** talk(s)

> "public benchmark is useful to orient and build your prior, but your private benchmark is useful to ship."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [3:11](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=191s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)

### Holdout discipline must be enforced structurally — private held-out sets plus controls that block the model's retrieval paths (Git history, network, test data) — because contamination is the default state of public task pools.

Support: **5** talk(s)

> "we have this private eval set that is mostly made up of things that happen in our code base which is held out from the evals so we ensure that the models aren't trained on it"
>
> — [Recursive Model Improvement](../talks/recursive-model-improvement.md), [7:53](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=473s)

Supporting talks: [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### A task is not admissible until a known-good solution demonstrates it is solvable and the verifier is strong enough not to reject valid alternative solutions.

Support: **4** talk(s)

> "when we construct Oracle ourselves to make sure that task is solvable in the first place. Because if it's not solvable, agent won't be able to solve it."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [7:02](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=422s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)

### Benchmarks have a short half-life and must be continuously regenerated; an eval everything saturates is no longer measuring anything.

Support: **4** talk(s)

> "if you're looking at an eval and all the models are scoring like 90% probably time to retire that eval and try to get something more difficult"
>
> — [Recursive Model Improvement](../talks/recursive-model-improvement.md), [8:24](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=504s)

Supporting talks: [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)

### In specialist domains the definition of a correct answer must be owned by a credentialed domain expert, not by the AI engineers or the system itself.

Support: **4** talk(s)

> "our system isn't deciding what correct is in a clinical edge case like this one. A licensed professional is."
>
> — [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [11:27](https://www.youtube.com/watch?v=O72p-rBb2bA&t=687s)

Supporting talks: [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Don’t be data poor](../talks/dont-be-data-poor.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)

## Disagreements

### Is a large, deliberately constructed benchmark suite worth the engineering investment, or does model/harness churn make it a wasted asset?

| Position A | Position B |
|---|---|
| Benchmark construction is a first-class engineering discipline worth heavy sustained investment — dedicated CI pipelines, human-authored and reviewed instructions, per-task grader design, and tasks that can take three people a week each to build.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* | Do not spend months building eval sets: they break the moment you switch models or harnesses (roughly 80% of tool-call evals invalidated by a harness change), teams won't actually delay upgrades to repair them, and a few hundred handcrafted expert tasks don't scale to open-ended real work anyway — generate tasks automatically from deployment instead.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* |

*Why it matters: It decides whether you staff a benchmark team and treat the suite as a durable asset, or build a thin continuously-regenerated task pipeline off production traces and accept that any static set is disposable.*

### Can simulated environments support valid behavioral evaluation, given that models can detect simulation?

| Position A | Position B |
|---|---|
| Yes — build a 'mini production' the agent cannot distinguish from the real system (snapshotted databases, sidecar containers, LLM-played users), or go further and learn a simulator, since full back-end controllability lets you plant answers and guarantee solvability in ways real production never can.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* | Behavioral evaluation in simulation is fundamentally compromised because models know they are being tested and act differently; the fix is real-world deployment, or forking a live deployment into simulation so the agent's early turns are genuinely real.<br>*[Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)* |

*Why it matters: If simulation awareness is unfixable, safety and misbehavior results from sandboxed benchmarks don't transfer, and eval infrastructure has to be rebuilt around live deployments with all the reproducibility loss that implies.*

### Should long-horizon tasks be graded end-to-end on the final outcome, or decomposed into per-step verifiers?

| Position A | Position B |
|---|---|
| Decompose: end-to-end outcome grading is too sparse a signal at current model ability, so break tasks into intermediate nodes with their own prompts and verifiers, terminating early when the agent fails a step.<br>*[Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)* | Keep the horizon long and intact — the interesting failures (spending revenue immediately, collusion, drift over hundreds of steps) only appear over runs an order of magnitude longer than typical evals — and solve the sparse-reward credit assignment with value models and RL over the compaction step rather than by chopping the task up.<br>*[Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* |

*Why it matters: Decomposition buys usable signal now but bakes in one assumed solution path and cannot surface emergent long-horizon behavior; the choice determines whether your benchmark measures step competence or actual agency.*

### Where should benchmark tasks come from — real production traces, or synthetically constructed novel tasks?

| Position A | Position B |
|---|---|
| Deployed production traces are the best available source material when no labels exist; the benchmark should be a constantly repopulated dataset from real traffic, with models finding issues in production and turning them back into tasks.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* | Construct tasks synthetically or author novel ones: a sampled set of real customer cases leaves rare edge cases untested, and existing public-repo-derived tasks are contaminated by design, so generating records backwards from a sampled label gives broader coverage and correct labels by construction.<br>*[Don’t be data poor](../talks/dont-be-data-poor.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)* |

*Why it matters: Trace-derived suites inherit the production distribution including its blind spots and cannot exist before you have customers; synthetic suites need a modeled generating process and domain-expert validation but can cover the tail and ship before deployment.*

## Practical Guidance

**Do:**

- Write an Oracle solution for every task and require it to pass in CI before the task enters the dataset
- Red-team your own environment for reward hacks first; admit only tasks that survive the attack pipeline
- Delete Git history at the start of a run (restore it after) and apply a network allowlist, so the model cannot mine the answer
- Retire any eval where models cluster around 90%, and treat eval creation as continuous investment rather than a one-time build
- Keep a held-out split (80/20 is a reasonable default) that the agent has never seen during experimentation
- Fit per-item discrimination with item response theory and inspect negatively-discriminating items — they reliably indicate mislabeled gold answers
- Give each evaluated organization its own private 'fingerprint set' of hard items to detect leakage
- Report gain (stateful reward minus stateless reward) when measuring learning, so base-model strength is not confounded with learning ability
- Verify final environment state, trace, and artifacts — not just the agent's output text
- Judge in hindsight after seeing the whole chain of events, or poll several judge models, rather than instructing a judge against failures up front
- Express task instructions as desired behaviors, objectives, and hard constraints, human-authored and human-reviewed
- Cover both bread-and-butter happy paths and edge cases (tool failures, database problems) the way integration test suites do
- Treat the benchmark as software with its own CI: pinned dependencies, base images, missing-fixture checks, Oracle passes
- Calibrate tasks to intermediate difficulty and keep searching for tasks in that band, since separation across rollouts is what carries signal
- Run small RL runs as part of environment design — some environment defects only appear once training is actually running
- Measure distribution shape alongside a correlation metric when the target is a population rather than a single right answer

**Avoid:**

- Instructions that point at the test file or supply the full implementation interface — the answer is leaked and the model's solution space is locked
- Two-page task instructions (SWE-Bench Pro averages 481 words) that bear no resemblance to how engineers actually prompt
- Verifiers that assert unspecified variable names or exercise unexported functions — these would fail code review in a real project
- Chaining independent benchmark instances together to build a continual-learning benchmark; without shared latent structure there is nothing to learn across instances
- Counting raw correct answers as your ability estimate, and assuming more items yields a better estimate
- Running more synthetic-persona samples on unchanged inputs to boost statistical significance
- Using production A/B tests as your comparison method — differing database state and tool versions make it never apples to apples
- Clustering traces to find issues: cluster boundaries are uncontrollable, hard to track over time, and one cluster can span unrelated root causes
- Chasing a perfect benchmark score, which drifts focus away from the humans the benchmark exists to protect
- Fixing observed failures by appending prohibitions to the prompt instead of the harness, skills, or structured output
- Giving agents tools that can search prior trajectories or archives — they learn to retrieve previous answers instead of reasoning
- Tasks so hard the whole leaderboard is flat (no model above 30% reward) or absurd in scope, like building a C compiler in Rust

## Notable Outliers

- On a real benchmark Claude Opus 4.1 and Gemini 3 Pro differ by 2 correct answers out of 337, yet are almost a full standard deviation apart in IRT-estimated ability — raw counts hide a large capability gap. ([Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [6:38](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=398s))
- Selecting only the highest-discrimination items compressed a 484-item benchmark to about 97 while preserving 99% of the ranking correlation — but the same trick fails on GPQA, whose items are uniformly discriminative. ([Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [11:10](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=670s))
- SWE-Bench Pro accepts wrong implementations on 8.5% of tasks and rejects correct implementations on more than 24%. ([Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [5:30](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=330s))
- Forking a live deployment into simulation at a chosen point dramatically decreases simulation awareness, because the agent's history up to the fork actually happened. ([Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [13:50](https://www.youtube.com/watch?v=cO8qC6HBuBg&t=830s))
- Vanilla in-context learning topped Continual Learning Bench 1.0 on reward and held across both the reward-vs-cost and gain-vs-cost Pareto frontiers, beating far more expensive context-management systems. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s))
- Benchmarks should include open-ended problems with continuous loss functions — e.g. compress 10MB of code losslessly, scored on compressed size plus source size — to force models to invent novel algorithms instead of checking whether code runs. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [14:49](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=889s))
- Human self-inconsistency imposes a hard ceiling on achievable synthetic-persona accuracy; one study measured humans as only about 80% consistent with themselves. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [17:03](https://www.youtube.com/watch?v=YnNF55QV0zs&t=1023s))
- Building the eval forces more rigorous reasoning than doing the analysis yourself — the process exposed that many canonical numerical QC thresholds in bioinformatics are arbitrary. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [10:54](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=654s))
- Opus 4.8 scored much worse than Opus 4.7 on Vending-Bench, traced to Anthropic removing a business-skills component from its post-training recipe — a benchmark detecting a specific training-recipe change. ([Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [2:43](https://www.youtube.com/watch?v=cO8qC6HBuBg&t=163s))
- Tightening the codebase API so test data could not reach training dropped an auto-research agent's data leakage rate to zero — abstraction design constrains reward hacking better than relying on agent intent. ([How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [14:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=850s))
- Scoping a computer-use agent's view to a single window instead of the whole desktop raised pass rate from 62% to 80% while using 34% fewer tokens — the harness, not the model, was the measured variable. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s))

## All Talks

- [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)
- [Don’t be data poor](../talks/dont-be-data-poor.md)
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
- [Anuj Iravane](../speakers/anuj-iravane.md)
- [Ben Hylak](../speakers/ben-hylak.md)
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

