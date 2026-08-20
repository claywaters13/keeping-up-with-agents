---
title: "online evaluation"
type: "concept"
slug: "online-evaluation"
tier: "supporting"
maturity: "consolidating"
talk_count: 18
speaker_count: 21
---

# online evaluation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **18** talk(s) by **21** speaker(s)

**Definition:** Measuring quality against live production traffic — monitoring, experiments, and implicit user signals — rather than a static dataset.

*Also referred to as: offline evaluation and production monitoring, production monitoring, deployment monitoring, a/b testing language features, continuous evaluation loop, session scoring and health metrics, implicit labeling from user interactions*

## State of Practice

The field now treats pre-launch evaluation as a gate, not as evidence: a passing offline suite tells you the system did not fail on cases you already imagined, and essentially nothing about live behavior. What practitioners actually run in production is continuous LLM-judge scoring of real conversations, guardrail-rate telemetry (claim rejection rate, missing-citation rate, human-override rate), stratified human review weighted 100% toward high-stakes cases, and per-segment slicing by geography, device, and content type. The prerequisite everyone converges on is trace-level logging — flat, human-readable, one record per orchestration stage — because aggregate pass rates demonstrably hide categorical failures (YouTube Ads found the agent detecting a legally required disclaimer and then deleting it, invisible in the pass-rate metric). Production traffic is also the dataset: teams sample and mutate real traffic rather than prompting a model for fifty synthetic test cases, and refresh held-out sets from prod. Judges are treated as software under test — validated like binary classifiers on ~100 hand-labeled examples with precision/recall, and re-verified before the agent is blamed for a score drop. The live argument is about autonomy: whether the detect-diagnose-retune loop closes without a human, and whether an agent or a deterministic statistical signal is what should notice the problem in the first place.

## Consensus

### Offline/pre-launch evaluation is necessary but insufficient; a statically tuned system does not hold up, so judges must continuously score live production traffic after launch.

Support: **6** talk(s)

> "What actually holds up in production is judges that continuously keep scoring real conversations as they happen. Not a saved golden data set. Live traffic."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [9:41](https://www.youtube.com/watch?v=YXEqC05WEI0&t=581s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)

### Trace-level logging of every reasoning step, tool call, and state transition is the precondition for online evaluation — conventional logs and aggregate pass rates are not enough.

Support: **6** talk(s)

> "you want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop"
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [6:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=413s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)

### Production traffic, not synthetic or hand-authored prompts, is the highest-value evaluation dataset; offline test sets should be sampled from and refreshed with prod data.

Support: **4** talk(s)

> "Production is the largest and the most representative evaluation data any organization will ever have."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

Supporting talks: [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)

### The online judge must itself be validated against human labels before its scores are trusted or acted on, with ongoing human-vs-LLM agreement monitoring.

Support: **4** talk(s)

> "In a non-deterministic system, the judge is also non-deterministic. Before you trust the score, verify the scorer."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [17:32](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1052s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### The production signal should terminate in an automated fix loop — an agent investigates the trace evidence and produces a diagnosis or PR before a human is paged.

Support: **4** talk(s)

> "shipping is the easiest part today. If you want to if you want to build a production agent, you need to close the loop first"
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [18:30](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=1110s)

Supporting talks: [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)

### Online evaluation belongs in your own repo and infrastructure — as code, tests, and self-built monitors — rather than in a separate managed eval or black-box SRE product.

Support: **3** talk(s)

> "we built it ourselves, so there are a lot of other companies and tools that provide the same kind of system, but I prefer to build it myself because I know what I'm interested in for, what I'm looking for."
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [13:59](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=839s)

Supporting talks: [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)

## Disagreements

### How much should a team invest in a curated offline eval suite before relying on production monitoring?

| Position A | Position B |
|---|---|
| Build a rigorous offline evaluation gate first — a fine-tuned user simulator, calibrated binary rubrics, launch gatekeeping criteria decided in advance — and do not expose live users to an unvalidated agent.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)* | Do not spend months on hand-built eval sets; they break on every model or harness swap and are not load-bearing. Ship, then learn what to test from production, where trajectories are non-deterministic and coverage is unbounded anyway.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)* |

*Why it matters: It determines whether an eval team's budget goes into simulators and golden datasets or into trace infrastructure and live judges, and whether a model upgrade is blocked for two weeks of eval maintenance or shipped behind production monitoring.*

### Should the loop from online signal to system change run without a human in it?

| Position A | Position B |
|---|---|
| Fully closed and config-driven: retune prompts and thresholds automatically against online drift, with guardrail observability and fast rollback as the safety net, and stage automated remediation to 5-10% of nodes before 100%.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)* | Keep a human as reviewer and authority holder: agents produce evidence-backed issues and PRs, but humans approve; high-stakes cases get 100% review, escalation is an explicit action, and shadow-mode should precede any execution authority.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)* |

*Why it matters: Full closure removes the human-capacity ceiling that several speakers call the real scaling bottleneck, but it also means a reward-hacked judge or a miscalibrated guardrail propagates to production with only rollback as recourse.*

### What should detect anomalies in production data — an agent, or a deterministic/statistical signal?

| Position A | Position B |
|---|---|
| Agents are bad at anomaly detection. Use deterministic signals (keyword frequency, statistical divergence like MMD or KL against per-client baselines) to surface candidates, and only let the agent investigate what has already been found.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)* | Log and trace analysis requires enough reasoning that it must be done by an agent; agent-as-a-judge searching across enormous trace volume finds subtle failures (e.g. silent loops) that scripts, filters, and fixed rubrics never surface.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* |

*Why it matters: It decides whether the expensive token spend goes into scanning all traffic or only into investigating flagged candidates, and whether novel failure classes you never anticipated can be discovered at all.*

### Are human decisions captured in production trustworthy enough to serve as ground-truth labels for online evaluation?

| Position A | Position B |
|---|---|
| Human labels are the golden source of truth that models and judges should be aligned to, and per-message member feedback is the truth signal that catches what automated judges miss.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)* | Automation bias contaminates them: reviewers scoring above 90% on calibration still upheld 50% of fabricated AI flags, and rubber-stamped approvals get logged as truth, making the model spuriously more confident over time.<br>*[Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)* |

*Why it matters: If production approvals are contaminated, every downstream online metric and retraining set inherits the bias, and the fix is interaction design rather than more oversight or a better judge.*

## Practical Guidance

**Do:**

- Log every stage of the orchestration into one flat, human-readable JSON record before attempting any optimization or self-learning loop.
- Run judges continuously over live conversations; sample high-stakes cases for human review 100% of the time and sample randomly across the rest.
- Instrument guardrail behavior itself as production rates — claim rejection rate, missing-citation rate — and track human-override rate on AI verdicts with a threshold that triggers investigation.
- Validate each judge like a binary classifier: ~100 hand-labeled pass/fail examples split into train/dev/test, scored on precision and recall.
- Attach a confidence interval to every reported score — 84% vs 88% on 50 traces is not a demonstrated gain.
- Build offline datasets by sampling and mutating production traffic; refresh held-out test sets with prod data and use them sparingly.
- Fine-tune the user simulator on real user verbatims until the eval score goes down, and treat the drop as evidence of realism, not regression.
- Slice production metrics by geography, device type, and content type so tuning can target the specific underperforming segment.
- Use per-client baselines and give every new endpoint its own baseline to avoid cold-start false positives.
- When a judge score drops, verify the judge before changing the agent's prompt; editing a judge prompt is legitimate engineering.
- Track, for each production issue, when it started and what percent of users it affects — both are needed to prioritize.
- Write trace classifiers as code and run them in a sandbox over production traces.
- Separate the fix-generating agent from the review agent, since the fixer is biased toward its own diagnosis and eager to open PRs.
- Stage automated remediation to 5-10% of machines, verify, then roll to 100%; make the monitor deployment-aware so it can decide on rollback.
- Strip PHI at the ingestion boundary rather than redacting at runtime, so production traces and dashboards are safe to evaluate against.

**Avoid:**

- Using live users as the test data for an unvalidated agent.
- Trusting a 90%+ production-simulation pass rate — it usually means the simulated user is unrealistically polite and articulate.
- Shipping generic prebuilt metrics (helpfulness, toxicity, conciseness scores) as core online metrics; a helpfulness of 0.5 is not actionable.
- Running an LLM-as-a-judge whose score gates no decision.
- Relying on aggregate pass rates alone — categorical failures like stripping a legally required disclaimer only show up in the traces.
- Clustering traces as your issue-detection method: clusters are hard to track over time, boundaries are uncontrollable, and one cluster spans unrelated root causes.
- Asking an agent to find anomalies rather than to investigate ones you already surfaced deterministically.
- Running A/B tests or experiments on a base of five to ten users.
- Assuming an offline-tuned component will stay tuned — every component needs a mechanism to retune against online drift.
- Logging a rubber-stamped human approval as a true label, or recording a yes/no decision while discarding the human's subsequent manual edit.
- Waiting for user complaints as your drift detector.
- Rewriting the prompt in response to a single failing production run instead of a failure pattern measured across examples.
- Setting baselines at HTTP-method granularity (all POSTs) rather than at the specific transaction type.

## Notable Outliers

- The QA gate itself gets reward hacked: the editing agent oversteers into overly conservative, generic outputs that differ in raw pixels but carry no meaningful quality improvement. ([Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [16:00](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=960s))
- Reviewers consistently scoring above 90% on accuracy calibration still accepted 50% of deliberately fabricated AI flags — a coin-flip rate indicating automation bias, and reviewer skill is no defense against it. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s))
- Changing only the guideline copy — framing the AI signal as a preliminary alert and requiring independent evidence — shifted rejection rates 21% with no model or UI change. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s))
- Switching harnesses (e.g. to the Claude Code CLI) can invalidate roughly 80% of hand-built tool-call evals, and most teams would not delay a model upgrade two weeks to repair them — which proves those evals were never load-bearing. ([Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [4:14](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=254s))
- Teams should trace and log roughly 10x more than they do today, because agents can consume volumes of telemetry that humans never could. ([From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [9:12](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=552s))
- Reliability is now a threshold requirement rather than a differentiator — only one in five survey respondents named it a top-three model consideration. (["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [6:53](https://www.youtube.com/watch?v=RGe6EjucbzI&t=413s))

## All Talks

- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)
- [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Anna Marie Benzon](../speakers/anna-marie-benzon.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Apoorva Joshi](../speakers/apoorva-joshi.md)
- [Ben Hylak](../speakers/ben-hylak.md)
- [Chris Souza](../speakers/chris-souza.md)
- [Daniel Bump](../speakers/daniel-bump.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Jason Lopatecki](../speakers/jason-lopatecki.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Parth Asawa](../speakers/parth-asawa.md)
- [Preetika Bhateja](../speakers/preetika-bhateja.md)
- [Rashi Agrawal](../speakers/rashi-agrawal.md)
- [Ritvik Pandya](../speakers/ritvik-pandya.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Vaibhav Gupta](../speakers/vaibhav-gupta.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)

