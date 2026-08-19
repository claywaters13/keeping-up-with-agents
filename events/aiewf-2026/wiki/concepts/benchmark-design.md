---
title: "benchmark design"
type: "concept"
slug: "benchmark-design"
tier: "core"
maturity: "contested"
talk_count: 19
speaker_count: 26
---

# benchmark design

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **19** talk(s) by **26** speaker(s)

**Definition:** Constructing a benchmark that measures what it claims to — task selection, difficulty calibration, discrimination, and holdout discipline.

*Also referred to as: agent benchmark design, agentic benchmark design, held-out private benchmarks, internal benchmarks, difficulty calibration, item response theory, private domain benchmarks*

## State of Practice

The conference's dominant position is that public benchmarks are broken as decision instruments and that the real unit of work is a private, continuously maintained benchmark owned by whoever ships the agent. Concrete failure evidence was presented rather than asserted: SWE-Bench Pro accepts wrong implementations on 8.5% of tasks and rejects correct ones on over 24%, its instructions average 481 words and sometimes name the test file outright; BEIR-style retrieval benchmarks use entity-keyword queries that structurally favor BM25 and thereby train agents to write bad queries; SWE-bench-style graders check only that code runs and produces the right output. Design discipline has consolidated around a repeatable checklist — construct an Oracle to prove solvability, adversarially attack the environment for reward hacks before admitting a task, hold out private tasks because public GitHub-derived tasks are contaminated by construction, grade final environment state and trace rather than just output, and run the benchmark itself under CI with pinned dependencies and base images. Scoring is moving off raw pass counts: speakers argued for cost/latency/retry axes, Pareto frontiers, gain (stateful minus stateless reward) to isolate learning from base capability, and item response theory, where two models two answers apart on a 337-item benchmark differ by nearly a full standard deviation in estimated ability. The deep unresolved questions are where tasks come from (hand-authored by experts vs. mined and synthesized from production traces), whether simulated environments survive simulation-aware models, and whether investing months in an eval set is rational when a harness change can invalidate 80% of it.

## Consensus

### Public benchmarks and leaderboards are not a valid basis for model or system selection; any team shipping agents needs its own private benchmark to make release decisions.

Support: **5** talk(s)

> "public benchmark is useful to orient and build your prior, but your private benchmark is useful to ship."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [3:11](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=191s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)

### Existing public benchmarks measure something structurally different from the work practitioners care about — academic Q&A instead of data analysis, memoryless point capabilities instead of learning, keyword retrieval instead of semantic search, code-runs-and-returns instead of engineering.

Support: **6** talk(s)

> "the existing benchmarks we saw at the time did not measure the tasks relevant to this category of work"
>
> — [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [7:16](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=436s)

Supporting talks: [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)

### Reward hacking is a defect in the benchmark, not the model, and environments must be adversarially attacked by their authors before tasks are admitted to the dataset.

Support: **7** talk(s)

> "before we test a task against any agent, we first try to break the environment ourselves"
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s)

Supporting talks: [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md)

### A task is not admissible until an Oracle or reference solution proves it is solvable, and grader strictness must be calibrated so correct-but-different solutions are not failed.

Support: **4** talk(s)

> "when we construct Oracle ourselves to make sure that task is solvable in the first place. Because if it's not solvable, agent won't be able to solve it."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [7:02](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=422s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md)

### Success rate alone is an inadequate score; benchmarks must report cost and additional axes alongside it, on a frontier rather than a single number.

Support: **5** talk(s)

> "you can compare agents using different metrics, not just success rate, but cost, latency, and retries."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [2:22](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=142s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)

### Contamination is the default state of any benchmark built from public sources, so holdout discipline and run-time controls (private task sets, deleted Git history, network allowlists, train/validation splits) are mandatory rather than optional.

Support: **5** talk(s)

> "we have this private eval set that is mostly made up of things that happen in our code base which is held out from the evals so we ensure that the models aren't trained on it"
>
> — [Recursive Model Improvement](../talks/recursive-model-improvement.md), [7:53](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=473s)

Supporting talks: [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### A benchmark has a short half-life — it decays through saturation and through model/harness changes — so it must be treated as maintained software rather than a fixed reference artifact.

Support: **4** talk(s)

> "if you're looking at an eval and all the models are scoring like 90% probably time to retire that eval and try to get something more difficult"
>
> — [Recursive Model Improvement](../talks/recursive-model-improvement.md), [8:24](https://www.youtube.com/watch?v=q4Tr-DknG2M&t=504s)

Supporting talks: [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)

## Disagreements

### Should benchmark tasks be hand-authored by domain experts, or generated and mined at scale from deployed agent traces?

| Position A | Position B |
|---|---|
| Tasks should be authored and reviewed by humans with domain accountability — engineers writing behavioral instructions, clinicians defining correctness in edge cases, scientists grading each other's work — accepting that a single task may take three people a week to build.<br>*[Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* | Handcrafted sets of a few hundred expert-built tasks do not scale to open-ended real work; the source material should be deployed production traces, reverse-engineered end states, self-play, or automatically damaged codebases, with humans reserved for the highest-level judgments.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* |

*Why it matters: It determines whether benchmark capacity is bounded by expert headcount or by compute, and whether the task distribution is specified up front or discovered from deployment — which in turn decides whether the benchmark can keep pace with model release cadence.*

### Can simulated environments produce trustworthy behavioral evaluation, given that models can detect they are being simulated?

| Position A | Position B |
|---|---|
| Simulation awareness fundamentally compromises behavioral eval; real-world deployment is the ground truth, and the best available repair is forking a live deployment into simulation so the agent's early turns are genuinely real.<br>*[Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)* | High-fidelity simulation is the right substrate — a snapshot database with sidecars, LLM-played users, and full back-end control, which is in some ways better than production because you can plant answers and guarantee solvability.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* |

*Why it matters: If simulation awareness is unfixable, safety and misbehavior findings from every sandboxed eval are suspect and the field needs expensive real-world deployments; if fidelity solves it, benchmark throughput scales with sandbox compute.*

### Is a large hand-built eval set a worthwhile investment for an application team?

| Position A | Position B |
|---|---|
| No — eval sets break as soon as the model or harness changes (switching to a CLI harness can invalidate roughly 80% of tool-call evals), and the fact that teams will not delay a model upgrade two weeks to update them proves they are not load-bearing; invest instead in production issue detection with code-mode classifiers over traces.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* | Yes — build the eval first and optimize against it second; it is the only reliable way to evaluate, release, and improve, and it doubles as a release gate, integration test, and training set.<br>*[Everything Is a Rollout](../talks/everything-is-a-rollout.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md)* |

*Why it matters: This is the difference between spending engineering months on benchmark construction versus on production observability, and it changes what a team can say about a model swap before shipping it.*

### Should benchmark difficulty be pushed to the ceiling, or calibrated to the intermediate band where scores separate?

| Position A | Position B |
|---|---|
| Push difficulty: retire any eval where models score ~90%, require headroom by construction, and accept flat leaderboards where no model exceeds 30% reward as legitimate signal about the frontier.<br>*[Recursive Model Improvement](../talks/recursive-model-improvement.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md)* | Calibrate to the middle: tasks should be neither too easy nor too hard because the learning signal depends on separation across rollouts, items everyone fails carry almost no information, and unreasonably hard tasks (build a C compiler in Rust) do not transfer into engineer trust.<br>*[Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md)* |

*Why it matters: Difficulty targeting decides whether a benchmark discriminates between today's models or only marks a distant frontier, and a benchmark tuned for measurement is useless as an RL environment if every rollout fails.*

### Should verification happen end-to-end on the final outcome, or be decomposed into per-step graders?

| Position A | Position B |
|---|---|
| Decompose: end-to-end outcome grading is too sparse a signal at current model ability, so long-horizon tasks should be split into intermediate nodes with their own prompts and verifiers, terminating early when a step fails.<br>*[Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)* | Keep the trajectory whole: one rollout produces one reward, and judgment is more reliable in hindsight after seeing the full chain of events than as per-step rules specified in advance.<br>*[Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md)* |

*Why it matters: Per-step graders pin the benchmark to one valid solution path and can fail correct-but-different work, while end-to-end rewards give little credit assignment on tasks models currently cannot finish.*

## Practical Guidance

**Do:**

- Construct an Oracle solution for every task before admitting it, to prove the task is solvable at all
- Adversarially attack your own environment for reward hacks before any agent sees the task; only tasks that survive enter the dataset
- Delete .git history at the start of an eval run (restore it after) and apply a network allowlist, so the model cannot mine the answer
- Keep a private holdout set the agent has not seen during experimentation; an 80/20 train/validation split is a reasonable default
- Retire any eval where all models score around 90%, and budget for eval creation as continuous investment because half-life shrinks as models improve
- Write task instructions that express desired behaviors, objectives, and hard constraints — not implementation details, interfaces, or test-file paths
- Grade the final environment state, the trace, and produced artifacts, not just the agent's output text
- Run the benchmark under its own CI pipeline checking pinned dependencies, base images, missing fixtures, and that the Oracle still passes
- Report cost, latency, and retries alongside pass rate; for learning benchmarks report gain (stateful reward minus stateless reward) to separate learning from base capability
- Use item response theory: items with negative discrimination reliably indicate mislabeled gold answers, and selecting high-discrimination items compressed one benchmark from 484 to ~97 items at 99% ranking correlation
- Give each evaluated organization its own fingerprint set of hard items so leakage becomes detectable
- Have an accountable domain expert define correctness in edge cases and commit that judgment into CI; in science, have scientists grade each other's work as the ground-truth proxy
- Judge in hindsight after the full chain of events, or by polling several models, rather than instructing a judge against failures in advance
- Fork real deployments into simulation at a chosen point, so early turns are indistinguishable from production and simulation awareness drops
- Run small RL training runs as part of environment design — some defects only surface once RL is actually running
- Design tasks to be durable across the multiple valid paths a competent practitioner might take
- Surface underlying run data, not just leaderboard position, so the benchmark explains why a model won

**Avoid:**

- Instructions that point at the test file or hand over the complete implementation interface — that leaks the answer and removes any room for a different valid solution
- Graders that assert unspecified variable names or test unexported functions; these are weak verifiers that would fail code review in a real project
- Two-page task prompts (SWE-Bench Pro averages 481 words per instruction), which do not resemble how anyone actually prompts
- Chaining independent existing benchmark instances together to fake a continual-learning benchmark — they share no latent structure to exploit
- Assuming more items means a better ability estimate; overlapping items add almost no information
- Sourcing all tasks from public GitHub repos, which makes contamination the default
- Telling a judge model not to allow a behavior and expecting that to prevent it in the rollout
- Treating production A/B tests as apples-to-apples comparisons — database state and tool versions differ between runs
- A/B tests or experiments at all when you have five or ten users
- Clustering traces to find issues: clusters are hard to track over time, boundaries are uncontrollable, and one cluster can span unrelated root causes
- Asking an agent to detect anomalies; use deterministic signals to surface candidates and let the agent investigate them
- Chasing a perfect benchmark score, which drifts focus away from the humans the benchmark exists to protect
- Demanding 100% grader coverage; mirror engineering test strategy — broad behavioral coverage, precise tests only where security or business logic demands
- Fixing observed failures by adding prohibitions to the prompt instead of to the harness, skills, or output schema
- Building continual-learning benchmarks that a model can beat by training offline, with no in-environment learning signal
- Exposing tools that let the agent search prior trajectories or archives, which teaches retrieval of past answers instead of reasoning

## Notable Outliers

- SWE-Bench Pro accepts wrong implementations on 8.5% of tasks and rejects correct implementations on more than 24% — the verifier is wrong roughly a third of the time. ([Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [5:30](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=330s))
- Claude Opus 4.1 and Gemini 3 Pro differ by two correct answers out of 337, but by almost a full standard deviation in IRT-estimated ability — raw counting hides the real gap. ([Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [6:38](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=398s))
- Behavioral evals in simulation are effectively doomed by simulation awareness; the future of evals is real-world deployment forked into simulation. ([Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [16:53](https://www.youtube.com/watch?v=cO8qC6HBuBg&t=1013s))
- Vanilla in-context learning topped Continual Learning Bench 1.0 on reward and held across both the reward-vs-cost and gain-vs-cost Pareto frontiers, beating more expensive context-management systems. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s))
- Standard retrieval benchmarks (BEIR, NanoBEIR) use entity-based 'caveman style' queries that structurally favor BM25, which is part of why agents write keyword-stuffed queries in production. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [4:52](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=292s))
- Benchmarks should include open-ended problems with continuous loss functions — e.g. compress 10MB of code, scored on compressed size plus source size — to force models to invent novel algorithms rather than pass unit tests. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [14:49](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=889s))
- All frontier models lost money on Kelly Bench when given $100K to trade Premier League matches over a one-year horizon. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [13:05](https://www.youtube.com/watch?v=2bvtay8wGYI&t=785s))
- Tightening the codebase API so test data could not reach training dropped the auto-research agent's data leakage rate to zero — abstraction design constrains reward hacking better than trusting agent intent. ([How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [14:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=850s))
- Rubric scores built from path-invariant choke points are only loosely correlated with verifiable outcomes, so they are not yet trustworthy for RL or benchmarking. ([Verifiable Environments for AI in Biology](../talks/verifiable-environments-for-ai-in-biology.md), [13:46](https://www.youtube.com/watch?v=3ZMUiFaQ3qg&t=826s))
- Switching the agent's computer tool to a window-scoped driver raised pass rate from 62% to 80% while using 34% fewer tokens — the benchmark was measuring the harness, not the model. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s))
- You cannot use synthetic personas to boost statistical significance — rerunning a forecast a thousand times with unchanged inputs improves your estimate of the model, not the accuracy of the forecast. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [15:08](https://www.youtube.com/watch?v=YnNF55QV0zs&t=908s))
- Providing an agent the correct memory does not guarantee it uses it, so oracle retrieval does not reach maximum task performance — the retrieval ceiling is not the capability ceiling. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s))

## All Talks

- [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)
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

