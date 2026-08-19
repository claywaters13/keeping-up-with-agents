---
title: "offline evaluation"
type: "concept"
slug: "offline-evaluation"
tier: "supporting"
maturity: "contested"
talk_count: 15
speaker_count: 19
---

# offline evaluation

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **15** talk(s) by **19** speaker(s)

**Definition:** Pre-deployment evaluation against fixed datasets and splits, run before shipping rather than against live traffic.

*Also referred to as: pre-registration in eval design, train/test splits for agent evals, train/validation/test splits, counterfactual evaluation, scenario-based evaluation, behavioral evals, oracle ground-truth evaluation*

## State of Practice

Offline evaluation at this conference is no longer "run the model against a fixed test set" — it is the construction and maintenance of a private, domain-specific simulation environment that gates releases. The dominant recipe: seed datasets from real production traces rather than LLM-generated test queries, snapshot tool responses and environment state as checked-in fixtures so runs are reproducible, prove each task solvable with an Oracle before it enters the suite, and verify final environment state, trace, and artifacts rather than just the model's text output. Grading has converged hard on binary, domain-specific pass/fail criteria tied to business outcomes; generic scalar metrics (helpfulness 0-1, correctness 1-5) are widely dismissed as low-signal and inconsistent across runs, and criteria are discovered by grading real outputs rather than specified up front. Judges themselves are now treated as classifiers to be validated — roughly 100 hand-labeled examples split train/dev/test, scored on precision and recall — and scores without confidence intervals are called out as not decision-grade. The unresolved fault lines are whether the offline suite is worth its maintenance cost given model and harness churn (one harness swap was reported to invalidate ~80% of tool-call evals), whether the primary quality signal should be the pre-ship gate or continuous production telemetry, and whether an LLM can be trusted to grade at all in domains where it can self-report success.

## Consensus

### Offline eval datasets should be seeded from real production traffic, traces, or recorded executions rather than synthetically generated test cases.

Support: **5** talk(s)

> "It's not a static benchmark. It's a constantly populated data set from your production traces."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [0:52](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=52s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)

### An offline eval is only worth building if it gates a decision — a release, a model swap, a merge — rather than producing a score someone reads.

Support: **5** talk(s)

> "You can put it as a release gate for your agent and verify that any change to agent stack in didn't reduce regression suddenly."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [5:30](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=330s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)

### Public and static benchmarks are necessary for orientation but structurally cannot support shipping decisions; each team needs its own private, domain-specific eval.

Support: **5** talk(s)

> "public benchmark is useful to orient and build your prior, but your private benchmark is useful to ship."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [3:11](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=191s)

Supporting talks: [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)

### Binary, domain-specific pass/fail criteria are the correct grading unit; generic scalar quality scores (helpfulness, correctness, conciseness on 0-1 or 1-5 scales) are low-signal and not actionable.

Support: **4** talk(s)

> "eval should be framed around a task success or failure. And a binary outcome is very easy to calibrate and train um LLM judge that can consistently score your agent trajectory."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [19:32](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1172s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)

### Humans with domain expertise must label and read raw outputs; evaluation criteria are discovered by grading real data, not specified in advance.

Support: **5** talk(s)

> "If you don't look at the data, you won't be able to create meaningful criteria uh or labels. And if you don't have labels, you won't be able to evaluate your judges. And if you're not evaluating your judges, you don't know if your uh agentic pipeline is working as as expected."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [26:58](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1618s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)

## Disagreements

### Should the primary quality signal for an agent be a pre-deployment offline gate, or continuous evaluation of live production traffic?

| Position A | Position B |
|---|---|
| Offline simulation is the primary signal: live users must not be used as test data, and production A/B comparison is not repeatable because database state and tool versions differ between runs, so the controlled offline environment is the only apples-to-apples surface. The domain expert builds the instrument once and it functions as a pre-ship gate, re-run when the base model changes.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)* | Production is the primary signal: it is the largest and most representative evaluation dataset an organization will ever have, evaluation should be an always-on service in the control plane rather than a pre-deployment phase, and it is live-trace evals — explicitly not offline evals — that generate the data needed for continual learning loops.<br>*[Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* |

*Why it matters: It determines where the engineering budget goes — into simulation environments, fixtures, and Oracle construction, or into tracing, classifiers over production traces, and drift detection. Teams that pick wrong either ship blind or spend months maintaining a suite that never catches the failures users actually hit.*

### Is a large hand-built offline eval suite a durable asset, or does model and harness churn make it a liability?

| Position A | Position B |
|---|---|
| Every company shipping agents needs its own benchmark, treated as engineering: pinned dependencies, its own CI pipeline, 80/20 train/validation splits, held-out sets, Oracle solutions per task. Model rollouts are gated on the full suite showing the new model is strictly better than the incumbent, and the bottleneck is the skill of writing high-quality evals, not tooling.<br>*[From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)* | Teams should not spend months building eval sets, because a new model or a harness switch breaks them — moving to the Claude Code CLI invalidated roughly 80% of tool-call evals. The proof that these suites are not load-bearing is that almost no team would delay a model upgrade by two weeks to update them; evals should instead be lightweight local tests living in code alongside the harness.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* |

*Why it matters: A team that treats the benchmark as long-lived infrastructure will pay continuous maintenance and may still be blocked by every model release; a team that treats evals as disposable tests loses the regression coverage that makes 'strictly better than the incumbent' a checkable claim.*

### Can an LLM be trusted to grade offline eval runs, or must the grader be deterministic?

| Position A | Position B |
|---|---|
| Graders must be deterministic and programmatic — Oracle solutions, environment-state verifiers, exploit checks, measurable conditions. LLM judges self-report success in domains where success is exactly what is in question, and they return different answers across runs on the same input, which makes them unusable as an optimization target.<br>*[Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)* | LLM and agent judges are the correct grading mechanism for agent trajectories, provided they are validated like binary classifiers against hand labels and scored on precision and recall; the frontier is agent-as-a-judge doing adaptive trace analysis, because fixed rubrics cannot catch multi-step agent failures.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* |

*Why it matters: Deterministic verification bounds what you can put in the suite to tasks with checkable end states, while LLM judging covers open-ended trajectories at the cost of a grader that itself drifts. Choosing wrong means either a suite that cannot express your real task or a gate that quietly moves under you.*

## Practical Guidance

**Do:**

- Seed the eval dataset by sampling production traffic and mutating it to cover golden paths and edge cases, rather than prompting an LLM for ~50 test queries
- Run every candidate task against a hand-built Oracle solution first to prove the task is solvable before it enters the benchmark
- Capture real downstream tool responses in a record mode and check the fixtures into the repo as code, so eval runs are reproducible without live production
- Verify final environment state, the trace, and produced artifacts — not only the agent's final output
- Hand-label ~100 examples pass/fail, split into train/dev/test, and score the judge on precision and recall before trusting it
- Attach a confidence interval to every reported score; treat 84% vs 88% on 50 traces as no evidence of a gain
- Hold out a set the agent has not seen during experimentation; an 80/20 train/validation split is a reasonable default
- Gate model rollouts on the full eval suite showing the new model is strictly better than the incumbent
- Treat the benchmark as software with its own CI pipeline checking pinned dependencies, base images, missing fixtures, and Oracle passes
- Measure cost, latency, and retries alongside pass rate
- Fine-tune the user simulator on real user verbatim until the eval score goes down — a falling score means the eval got more realistic
- Make the eval harness config-driven (YAML) so analysts and data scientists can add test cases without engineers
- Run evals at multiple points: locally, at pre-commit, and in CI/CD as a regression suite
- Decide on cohorts of replays, never on one or two runs, and keep a human at the final ship/no-ship decision
- Decompose long-horizon tasks into steps with a separate prompt and verifier per step so runs can terminate early on failure

**Avoid:**

- Shipping an LLM-as-a-judge whose score gates no decision — it is dead weight
- Using pre-built generic metrics (helpfulness, toxicity, conciseness) as core eval metrics; a helpfulness of 0.5 is not actionable
- Trusting a 90%+ offline pass rate — it usually means the simulated user is unrealistically polite and articulate, not that the agent is good
- Defining evaluation criteria fully before grading any real outputs
- Manual end-to-end testing against live production, where data is retained only briefly and regressions become undetectable
- Expecting A/B tests of agent variants in production to be apples-to-apples; database state and tool versions differ between runs
- Letting the agent detect that it is running in a simulation — it will reward-hack the environment
- Fixing eval failures by adding prohibitions to the prompt; route the fix to the harness, skills, or structured output based on root cause
- Benchmarks that assume one vulnerability or one defect per program, or that score a crash as success
- Feeding the model a backtrace pointing at the vulnerable function — it removes the reasoning the eval is meant to measure
- Clustering traces as your issue-detection method: clusters are hard to track over time and one cluster can span unrelated root causes
- Running A/B tests or experiments when you have five to ten users
- Asking an agent to find anomalies; use deterministic signals to surface candidates and let the agent investigate them

## Notable Outliers

- Switching harnesses — for instance moving to the Claude Code CLI — invalidates roughly 80% of a hand-built tool-call eval set. ([Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [4:14](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=254s))
- Fine-tune the LLM user simulator until the evaluation score goes down; a falling score is the signal the eval finally got realistic. ([Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [16:55](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1015s))
- Crash-triggering has saturated as a metric — top models hit 95% (39/41) on V8 CVEs — while full control-flow hijack still separates models cleanly at 73% and 68% versus 0%. ([Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [22:12](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=1332s))
- Rhetorical authenticity must be explicitly excluded as a scoring axis, because rewarding a persona for sounding right validates the exact failure the eval exists to catch. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [47:19](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=2839s))
- Oracle retrieval does not reach maximum task performance: handing the agent the correct memory does not guarantee it uses it, so retrieval-quality evals overstate achievable ceilings. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s))
- Hand-curating benchmark programs with exactly one known bug is infeasible — 50% of DARPA's $60M Cyber Grand Challenge problems contained unintended exploitable bugs. ([Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [12:38](https://www.youtube.com/watch?v=ZFxh7sqbUZo&t=758s))

## All Talks

- [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)
- [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md)
- [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)
- [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)
- [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Anna Marie Benzon](../speakers/anna-marie-benzon.md)
- [Annabell Schäfer](../speakers/annabell-schafer.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Ben Hylak](../speakers/ben-hylak.md)
- [Cat Wu](../speakers/cat-wu.md)
- [David Brumley](../speakers/david-brumley.md)
- [Drasko Profirovic](../speakers/drasko-profirovic.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Kunal Lanjewar](../speakers/kunal-lanjewar.md)
- [Marah Abdin](../speakers/marah-abdin.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Robert McHardy](../speakers/robert-mchardy.md)
- [Rustem Feyzkhanov](../speakers/rustem-feyzkhanov.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Stefania Druga](../speakers/stefania-druga.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Varsha Shah](../speakers/varsha-shah.md)

