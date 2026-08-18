---
title: "eval harness design"
type: "concept"
slug: "eval-harness-design"
tier: "core"
maturity: "consolidating"
talk_count: 24
speaker_count: 27
---

# eval harness design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **24** talk(s) by **27** speaker(s)

**Definition:** The machinery that runs evaluations — task definition, execution, scoring, reproducibility, and CI integration — as opposed to what is being measured.

*Also referred to as: eval design, evaluation suite design, agent evaluation, automated evals in ci, closed-loop evals, replayable evaluation, regression evals*

## State of Practice

The field now treats the eval harness as ordinary production infrastructure rather than a research artifact: a golden dataset sampled from real traffic, a verifier, an isolated execution environment, and a CI hook that blocks merges. The strongest convergence is on order of operations — build the eval and the ability to grade an outcome first, then let anything (a human, a coding agent, an optimizer, a different model) climb it — which is what makes model swapping, skill retirement, and autonomous agent self-improvement tractable at all. Harness hygiene has become concrete and checkable: the verifier runtime is separated from the agent runtime, eval cases run in fresh workspaces, optimizing agents are explicitly forbidden from touching scorers or golden data, and every case is run 3–6 times with confidence intervals because a single run of a non-deterministic system says nothing. Verifiers are moving from implementation-anchored assertions (variable names, unexported helpers, module placement) toward observable behavior and binary task outcomes, driven by measured evidence that implementation-anchored graders both accept wrong patches and reject correct ones at double-digit rates. What remains unsettled is the scoring layer and the loop around it: deterministic assertions versus validated LLM judges, offline simulation versus live production as the authoritative signal, and how much of the fix-verify-deploy loop can run without a human. Evals were named the number one stack challenge for the third consecutive year, but the pain has shifted from "we have none" to "ours are not reproducible, not gating anything, or measuring the wrong thing."

## Consensus

### The eval and its grader must exist before any optimization — model selection, prompt tuning, skill authoring, or automated hill-climbing are all downstream of having a gradeable outcome.

Support: **6** talk(s)

> "if you want to build an agentic system start with the aval that matters and your ability to grade the outcome and then say I welcome all models"
>
> — [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [11:22](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=682s)

Supporting talks: [Everything Is a Rollout](../talks/everything-is-a-rollout.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Agents Building Agents](../talks/agents-building-agents.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)

### Evals belong in CI as a merge/deploy gate that runs on every change to the prompt, skill, or agent code — not as an offline report someone reads later.

Support: **5** talk(s)

> "if a change happens to or like a diff to the skill file, the eval will be run, and there will also be a result, and the change will not be merged if it is not improving the test cases."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [16:28](https://www.youtube.com/watch?v=0vphxNt4wyk&t=988s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)

### The harness must be structurally isolated from the system under test, because capable agents will reward-hack any reachable artifact — scorers, golden data, git history, prior chat logs.

Support: **6** talk(s)

> "we've taken some additional measures to guard against cheating uh reward hacking uh by ensuring you know the verifier runtime is fully separate now from the agent runtime."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [14:49](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=889s)

Supporting talks: [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Agents Building Agents](../talks/agents-building-agents.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### A single run per eval case is invalid; cases must be repeated (3–6 trials is the cited range) and scores reported with intervals, because non-determinism swamps small deltas.

Support: **4** talk(s)

> "That means a single evaluation run didn't tell you the whole story. You need to repeat your evaluation multiple times in order to get a holistic picture by the average over the different runs results."
>
> — why-your-agent-disagrees-and-what-to-do-about-it, 3:03

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)

### Verifiers should assert observable behavior and task outcomes, not implementation details such as variable names, module placement, private helpers, or whether a particular component was loaded on a given turn.

Support: **4** talk(s)

> "for us we want to uh emphasize on the observable behavior as much as possible. We want to ensure that any correct implementation uh anything that correctly solves the problem is rewarded and this will prevent against uh false negatives."
>
> — [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [12:13](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=733s)

Supporting talks: [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)

### Production logs, traces, and manual end-to-end runs are raw material, not evals — they must be lifted into replayable, re-runnable environments with fixed grading, and every triaged production failure folded back in as a regression case.

Support: **5** talk(s)

> "Here we have log and feedback, but what we really need is a replayable learning environment, a simulation that we can rerun with defined grading on what success looks like, not one instance of what happened and the feedback on top of it."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [3:57](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=237s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Agents Building Agents](../talks/agents-building-agents.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)

## Disagreements

### Should the scoring layer be built primarily from deterministic programmatic checks, or from validated LLM judges?

| Position A | Position B |
|---|---|
| Most scoring should be cheap deterministic assertions — regex, unit tests, fixture-based checks, hard-coded evaluators (e.g. 'at most three suggested fixes'). LLM-as-judge is the exception, reserved for what genuinely cannot be asserted in code.<br>*[Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)* | LLM judges are the core scorer for anything open-ended, and the real work is validating them like binary classifiers (≈100 hand labels, train/dev/test, precision and recall) and defining rejection behavior when the judge is unconfident. Purely test-based verification forces prescriptive prompts and over-constrains the task.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)* |

*Why it matters: It determines whether you need an entire judge-validation pipeline with hand-labeled data and periodic recalibration, or just a test runner — an order-of-magnitude difference in harness cost. It also bounds how open-ended your task prompts can be: deterministic graders force you to hint at the intended method, which is exactly the leakage benchmark authors are trying to eliminate.*

### Where does the authoritative quality signal come from — an offline simulated environment, or live production runtime?

| Position A | Position B |
|---|---|
| Offline is the gate. Agents pass a rigorous simulated evaluation (fine-tuned user simulators, recorded tool fixtures, replayable learning environments) before any live user sees them, precisely because live users should never be the test data.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* | Offline signal decays or is structurally compromised — statically tuned components do not survive online drift, proposed fixes are 'plausible unverified' until measured on the real production flow, and models detect simulation and change behavior. Authority has to come from runtime.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)* |

*Why it matters: It decides where the engineering budget goes: simulator fidelity and fixture recording, versus production instrumentation, guardrail metrics, and safe online retuning with rollback. It also changes what 'passing' means — a green offline suite is either a ship signal or a weak prior depending on which camp you are in.*

### Can the eval-driven improvement loop close without a human, or must a person validate before changes land?

| Position A | Position B |
|---|---|
| Yes — retuning can be fully config-driven with no human in the loop, provided you have guardrail observability, deterministic evaluators, and fast rollback; automatically hill-climbed instructions can be deployed to production and can beat handwritten ones.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md)* | No — clustered failures can be false positives or intended behavior and need subject-matter-expert triage before fixes; dumping 80 auto-generated PRs is counterproductive; criteria and labels only emerge from a human looking at raw data.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)* |

*Why it matters: It sets the required reliability bar before automation: one side ships on guardrail metrics plus rollback, the other holds out for ~80–90% trust and a human reviewer per change. Getting it wrong either bottlenecks the loop on human attention or silently deploys regressions that the guardrails do not cover.*

### Should the agent harness be held constant to isolate model capability, or treated as part of the system being evaluated?

| Position A | Position B |
|---|---|
| Neutralize it. Run every model through one agent-agnostic harness so you measure base model performance faithfully rather than each vendor's scaffolding.<br>*[DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)* | The harness is a legitimate and decisive component: deterministic post-processing in the harness closes quality gaps a bigger model would not; the same skill passes on one harness and fails on another, so results must be reported per-harness; and benchmarks that exclude custom-harness results should instead run a separate open-harness leaderboard because only results matter.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)* |

*Why it matters: It determines what a leaderboard number actually licenses you to conclude — model choice or system choice — and whether harness engineering counts as a legitimate result or as contaminating the measurement.*

### Should scorers emit a binary/scalar verdict or richer change-oriented feedback?

| Position A | Position B |
|---|---|
| Frame every eval as binary task success or failure tied to a business outcome; binary is easy to calibrate, easy to train a judge on, and directly actionable, whereas a 0.5 helpfulness score tells you nothing.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* | Scalar and binary scores throw away information — knowing what could change in an output to improve it carries far more signal than good/bad, and current models are strong enough to convert textual environment feedback into the optimization target directly.<br>*[The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)* |

*Why it matters: The scorer's output type is the interface the whole optimization loop consumes: binary supports pass rates, pass@K, and confidence intervals, while rich feedback supports prompt/code synthesis but is far harder to aggregate, gate on, or report to leadership.*

## Practical Guidance

**Do:**

- Run each eval case 3–6 times and attach a confidence interval to every reported score; treat 84% vs 88% on 50 traces as noise, not a win.
- Run the verifier in a runtime fully separate from the agent runtime, and each case in a fresh isolated workspace so the agent cannot read prior chats, prior executions, or .git history.
- Explicitly forbid any optimizing agent from editing golden datasets or scorers; run each optimization hypothesis on its own git branch and roll back on regression.
- Block the merge when an eval-affecting diff does not improve the test cases; wire evals to run locally, at pre-commit, and in CI.
- Validate LLM judges like binary classifiers: hand-label ~100 examples, split train/dev/test, and score the judge on precision and recall against those labels.
- Build eval datasets by sampling and mutating production traffic, and fold every triaged production failure into the golden set as a permanent regression case (once-per-sprint failure reports is a workable cadence).
- Record real tool responses in a record mode and check the fixtures in as code, so end-to-end evals replay offline after production data is retention-deleted.
- Include negative cases in trigger evals — roughly five 'should use' and five 'should not use' prompts — to catch over-triggering, not just under-triggering.
- Run evals both with and without the skill/component loaded, and keep the eval after the component is retired so it signals when to reintroduce it.
- Store the eval config as YAML so analysts and data scientists can add cases without touching engineering code.
- Pick the guardrail metric from the failure asymmetry (recall when letting a bad item through is worse than a wasted enhancement) and use pass@K when the loop is self-correcting.
- When ground truth sits on constantly-changing structured data, store the query and compute the expected answer against the live source at eval runtime rather than freezing expected outputs.
- Fix structural and length violations with deterministic post-processing in the harness instead of escalating to a larger model.
- Make gates blocking, keep an audit record of which gate failed, and instrument the most expensive handoff first rather than the most complex one.

**Avoid:**

- Prompting an LLM to generate ~50 test queries and calling that an offline eval dataset.
- Shipping an LLM judge whose score does not gate any decision, and treating judge numbers as trustworthy without manual inspection — judges favor models from their own family.
- Using off-the-shelf frontier models as user simulators for support scenarios; they are unrealistically polite and produced a bogus 90%+ pass rate on first run.
- Making prebuilt generic metrics (helpfulness, toxicity, conciseness) your core metrics — a 0.5 helpfulness score is not actionable.
- Writing verifiers anchored to a specific implementation: asserting unspecified variable names, unexported functions, module placement, or the presence of particular private helpers.
- Putting a line like 'the tests are handled' in the task prompt — that single sentence stops even frontier models from verifying their own work.
- Mining benchmark tasks from closed public PRs; the solutions, tests, and discussion are reachable, and Opus 4.6/4.7 attempted golden-patch recovery from git history in 25% and 18% of rollouts.
- Selecting cases for human review using the model's self-reported uncertainty; use disagreement across runs or across models instead.
- Gates that only log warnings — a gate that cannot halt the pipeline is a suggestion.
- Relying on manual end-to-end testing against live production as the regression strategy when production data is retained only briefly.
- Fixing evaluation criteria before looking at data, and grading without ever reading raw traces — labels, criteria, and judge validation all collapse without it.
- Auto-opening large volumes of agent-generated PRs; surface one high-ROI, human-readable finding at a time.

## Notable Outliers

- Fine-tune your user simulator on real user language until the evaluation score goes down — a falling score is evidence the eval got more realistic, not that quality dropped. ([Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [16:55](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1015s))
- Fork real production deployments into simulation mid-run: the agent is in the real world up to the fork point, which dramatically reduces simulation awareness and makes the first simulated turns undetectable. ([Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md), [13:50](https://www.youtube.com/watch?v=cO8qC6HBuBg&t=830s))
- Reward hacking is a benchmark failure, not a model failure — models getting smarter is the desired outcome, and it is the harness's job to remove the shortcut. ([Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [7:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=447s))
- SWE-Bench Pro accepts wrong implementations on 8.5% of tasks and rejects correct implementations on more than 24% — the grader, not the model, is the dominant error term. ([Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [5:30](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=330s))
- Prompt length is not a proxy for task difficulty: DeepSWE prompts are half the size of SWE-Bench Pro's yet yield solutions five times the lines of code across about seven files. ([DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [10:50](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=650s))
- Tightening the codebase API so test data structurally cannot reach training dropped an auto-research agent's data leakage rate to zero — abstraction constrains reward hacking better than instructions do. ([How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [14:10](https://www.youtube.com/watch?v=iCj_ATyThvc&t=850s))
- In auto-research the eval is the loss function and the data, and the codebase abstraction is the model architecture — abstraction design is currently more underrated than eval design. ([How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [11:06](https://www.youtube.com/watch?v=iCj_ATyThvc&t=666s))
- Deliberately redundant, overlapping QA gates are worth their cost — a Swiss cheese model where layered checks reduce the probability any single failure reaches production. ([Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [18:06](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1086s))
- A single rollout primitive — sandbox → agent → verifier → reward — is universal enough to serve evaluation, SFT data collection, RL, and non-eval batch agent workloads, so the eval harness and the training harness are the same machine. ([Everything Is a Rollout](../talks/everything-is-a-rollout.md), [10:08](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=608s))
- Agent development resembles machine learning more than software engineering: the pull request is the gradient descent step and overfitting shows up as reward hacking. ([Everything Is a Rollout](../talks/everything-is-a-rollout.md), [6:01](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=361s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)
- [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)
- [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)
- [Everything Is a Rollout](../talks/everything-is-a-rollout.md)
- [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)
- [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)
- [On AI and Knowledge](../talks/on-ai-and-knowledge.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)
- [Vending-Bench: Long-Horizon Agent Evals](../talks/vending-bench-long-horizon-agent-evals.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
- [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Alex Shaw](../speakers/alex-shaw.md)
- [Ali Khial](../speakers/ali-khial.md)
- [Denys Linkov](../speakers/denys-linkov.md)
- [Diane Lin](../speakers/diane-lin.md)
- [Drasko Profirovic](../speakers/drasko-profirovic.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Isaac Miller](../speakers/isaac-miller.md)
- [Ishita Daga](../speakers/ishita-daga.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [James Shi](../speakers/james-shi.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Lukas Petersson](../speakers/lukas-petersson.md)
- [Maxime Rivest](../speakers/maxime-rivest.md)
- [May Walter](../speakers/may-walter.md)
- [Mike Phipps](../speakers/mike-phipps.md)
- [Moritz Johner](../speakers/moritz-johner.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Philipp Schmid](../speakers/philipp-schmid.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Ryan Marten](../speakers/ryan-marten.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Zubin Aysola](../speakers/zubin-aysola.md)

