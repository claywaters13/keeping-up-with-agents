---
title: "incident response automation"
type: "concept"
slug: "incident-response-automation"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 12
---

# incident response automation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **12** speaker(s)

**Definition:** Agents in the operational loop — triaging alerts, investigating root cause, and remediating production issues.

*Also referred to as: incident triage and root cause investigation, on-call automation, root cause analysis, log monitoring agents, security alert triage, automated remediation, self-healing automation, hypothesis-driven root cause analysis*

## State of Practice

The conference converged on a common shape for operational agents: cheap deterministic or statistical detection first, an agent that investigates only what the rules could not decide, and an explicit escalation path for insufficient evidence. Speakers repeatedly reported that model capability is no longer the binding constraint — the constraint is capturing environment-specific context (service topology, per-client baselines, payer rules, business KPI relationships) so the agent can tell a real incident from normal variance. Detection infrastructure is getting concrete: per-client and per-transaction-type baselines rather than per-HTTP-method, tail-based sampling with async OTel→Kafka so telemetry does not slow the request path, hot-path plus reconciliation-path decisioning, and staged remediation rollout at 5–10% of nodes before 100%. On the fix side, the loop now routinely terminates in an agent-authored PR — detection to review-ready diff in roughly half an hour — with the fixing agent deliberately separated from the reviewing agent and forbidden from editing the golden dataset or scorers. What is still openly argued is how much execution authority the agent gets (propose-only versus act-and-verify), whether agents or deterministic signals should do the finding, and whether curated eval suites are load-bearing when models and harnesses churn every few months. A recurring sober note: one RL-based ETL remediation agent beat its hand-written deterministic policy by only 0.19 percentage points, and the speaker attributed the system's reliability to state design and external safety constraints, not the learning.

## Consensus

### Detection over measurable signals should be deterministic or statistical; the agent's job is to investigate what has already been surfaced, and to handle only the cases rules cannot decide.

Support: **5** talk(s)

> "Last lesson here is that agents are very, very bad at anomaly detection. So don't ask your agent to find anomalies. Uh ask it to investigate anomalies you've already found."
>
> — [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [18:30](https://www.youtube.com/watch?v=jHMiYtjoJfA&t=1110s)

Supporting talks: [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)

### Escalation to a human must be a first-class, explicitly modeled outcome triggered by insufficient evidence or low confidence — not a failure state the system optimizes away.

Support: **5** talk(s)

> "Notice that escalation is included in the action space that is not the agent giving up. It is the system correctly recognizing the boundary of its evidence and authority for an operational agent."
>
> — [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [6:22](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=382s)

Supporting talks: [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Agents Building Agents](../talks/agents-building-agents.md)

### Pre-production testing cannot characterize an operational agent's behavior; production traces are the primary source of truth and shipping without trace-level observability leaves the team blind.

Support: **4** talk(s)

> "you don't know what your agent will do until it is in the production."
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [2:56](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=176s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Agents Building Agents](../talks/agents-building-agents.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)

### The bottleneck for operational agents is captured environment- and domain-specific context, not model capability or execution ability.

Support: **4** talk(s)

> "You need the execution engine, that's great, but you really need that production context that tells you is this important or not important."
>
> — [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [10:48](https://www.youtube.com/watch?v=vSx5IULvBns&t=648s)

Supporting talks: [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

### The remediation loop now terminates in an agent-authored pull request produced directly from trace analysis, with human review as the gate rather than human diagnosis.

Support: **3** talk(s)

> "the the the the PR agent and the review agent send 10 times more PR than the three of us every day."
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [10:19](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=619s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Agents Building Agents](../talks/agents-building-agents.md)

## Disagreements

### Should an operational agent be granted authority to execute remediation in production, or should it only ever propose an action for a human to approve?

| Position A | Position B |
|---|---|
| Agents should act. Remediation is rolled out progressively (5–10% of machines, verify, then 100%), orders proceed to submission with no human touch once multi-source evidence corroborates, and background automations close issues outright when deterministic guardrails bound the blast radius.<br>*[Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)* | The agent proposes and never holds final authority: safety constraints sit outside the policy, benchmark results are a feasibility demo that must precede shadow-mode deployment on real incidents, AI augments rather than replaces CI/CD, and clustered failure findings are validated by human SMEs before any fix is implemented.<br>*[Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Agents Building Agents](../talks/agents-building-agents.md)* |

*Why it matters: It determines whether you build an approval queue and shadow-mode harness or a staged-rollout-and-rollback controller, and it sets who is accountable when the agent's remediation is itself the incident.*

### Should agents mine traces to discover issues, or should deterministic signals surface candidates that agents then investigate?

| Position A | Position B |
|---|---|
| Point an agent at the trace corpus: cluster negative-feedback traces into failure reports, run an evaluation agent that searches across enormous volumes of traces, and run an LLM-driven session analyzer because log analysis for agents requires too much reasoning for scripts and filters.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)* | Clusters are not issues — they cannot be tracked over time, their boundaries are uncontrollable, and one cluster spans unrelated root causes. Use deterministic signals (keyword frequency, MMD/KL divergence against per-client baselines, statistical drops) or code-mode classifiers run in a sandbox, then hand the agent the candidate.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)* |

*Why it matters: It decides where your token budget goes and whether your issue tracker has stable identities — you cannot answer 'when did this start and how many users does it affect' from clusters that redraw their own boundaries every run.*

### Should judgment in an incident-response system be consolidated in one agent or split across specialized agents?

| Position A | Position B |
|---|---|
| Exactly one agent owns end-to-end reasoning. Sub-agents may return investigation results but never reasoning or judgment, because every handoff loses context and the loss compounds; the incoherence came from how the work was split, not from the LLM.<br>*[Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)* | Split judgment deliberately: a separate review agent with fresh context judges the fixer's PR because fixers are biased toward their own diagnosis, and a separate judge agent evaluates the operational agent's trajectory because the actor cannot see its own loops.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* |

*Why it matters: Consolidation buys coherent root-cause narratives at 50+ turns and high token cost; separation buys independent adversarial checks on the fix. Choosing wrong yields either fragmented diagnoses or a self-approving remediation loop.*

### Is a curated offline eval suite worth building for an operational agent?

| Position A | Position B |
|---|---|
| Yes — a golden dataset plus scorers is the test suite for non-deterministic systems, every discovered failure mode is added back to it, mature teams run deterministic evals plus LLM-as-a-judge plus agent-as-a-judge, and every eval must be run multiple times and averaged because one run does not tell the story.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)* | No — large hand-built eval sets break the moment you change model or harness (switching to a CLI harness invalidated ~80% of tool-call evals), and since almost no team would delay a model upgrade two weeks to update them, the evals are not load-bearing. Pre-launch unit tests, regex and scripted simulations cover only one slice; production is where you learn what to test.<br>*[Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)* |

*Why it matters: It sets whether months of engineering go into dataset curation or into production trace instrumentation and classifiers — and whether a model upgrade is a two-week revalidation or a same-day swap.*

### Should incident-response monitoring be bought as a platform or built in-house?

| Position A | Position B |
|---|---|
| Buy/adopt a platform: teams need a per-customer knowledge system that learns the environment, an always-on cloud agent embedded in Slack and Teams, and eval infrastructure at production scale (over 100 million evals a month, top teams running 3,800+ evaluators).<br>*[Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* | Build it yourself in your own repo: build the monitoring system in-house because you know what you are looking for, and write evals as local tests in code — managed cloud prompt and eval products are largely obsolete now that the prompt is the whole harness and codebase.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)* |

*Why it matters: The competitive claim on both sides is that the harness, not the model, is the moat — so this is really a bet on whether environment knowledge is a portable product or something only your own team can encode.*

## Practical Guidance

**Do:**

- Gate deeper analysis behind a cheap tier-one check: model the request as a short-lived DAG and if end-to-end execution matches the baseline, skip every further tier.
- Scope baselines per client and per transaction type (real-time payments, wire payments) rather than per HTTP method, and give a new endpoint its own baseline to avoid cold-start false positives.
- Roll automated remediation out to 5–10% of machines, verify, then go to 100% of nodes; make the monitoring system deployment-aware so it can make correct rollback decisions.
- Feed telemetry asynchronously to OpenTelemetry with Kafka and stream processing downstream so observability never delays real-time request processing, and use tail-based sampling when you need start/end times per node.
- Run detection on two paths: a hot path for fast automatable decisions and a slower, more accurate reconciliation path.
- Require two independent sources to agree before skipping human verification, and attach a confidence score to every agent answer so only low-confidence cases reach a clinician or operator.
- Keep safety constraints outside the learned policy so a policy update cannot silently redefine the agent's own authority, and represent 'unsafe' and 'unavailable in this environment' as distinct states.
- Run each optimization or fix hypothesis on its own git branch and roll back on regression; explicitly forbid the fixing agent from editing golden datasets or scorers.
- Use a separate review agent with fresh context to judge the fixing agent's PR, since fixers are biased toward their own diagnosis and eager to ship.
- Select cases for human review using disagreement across repeated runs or across different models, and feed the resolved rulings back into semantic and episodic memory.
- Give every monitoring agent access to trajectories, metrics, the database, and the UI — without all four its output is guesswork.
- Bound automation output (at most a single PR) and allow automations to produce nothing at all; keep secrets outside the agent's sandbox behind a broker and express guardrails as deterministic configuration, not prompt text.
- Make anomaly output explainable with the supporting data rather than a single opaque score, and embed the agent in Slack or Teams instead of a separate product UI.
- Close the loop with yourself as the bottleneck first, then remove the human — and re-derive baselines when traffic mix shifts, since covariate drift means nothing is broken.

**Avoid:**

- Treating trace clusters as issues — they cannot be tracked reliably over time, their boundaries are uncontrollable, and one cluster can span unrelated root causes.
- Asking an agent to find anomalies; agents cannot reliably do anomaly detection, only investigation of ones already surfaced.
- Using LLM self-reported uncertainty scores to decide what needs human review — the model does not know what it does not know.
- Distributing judgment across a chain of specialized agents that mimics a human analyst's workflow steps; each handoff loses context and the loss compounds.
- Letting an agent infer entity and KPI relationships from raw tables — it does not scale and produces relationships that do not exist in the data.
- Prompting guardrails at the agent, which lets a third party prompt-inject past them.
- Trusting a single LLM extraction from a single source as grounds to skip human review.
- Measuring an operational agent by its non-escalation rate; a deliberate increase in escalation can be the correct behavior.
- Treating benchmark MTTR reductions as production validation — run shadow mode against real incident traces before granting execution authority, and evaluate across repeated runs since one favorable run is a demo.
- Relying on task-completion signals as a quality metric: a technically successful run can still fail the user, and an agent that recovers by luck with no alert is a hidden defect.
- Leaning on fixed hard-coded post-release checks and wait intervals, and assuming CI/CD covers everything — feature flags and infra changes often bypass it with no monitoring at all.
- Running an agent inside the deterministic part of a workflow that should have executed before the agent was ever invoked.

## Notable Outliers

- An RL policy for ETL failure remediation beat an equivalent hand-defined deterministic policy by only 0.19 percentage points on a compact state space — the reliability came from state design, decision logic, and external safety constraints, not from the learning. ([Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [10:11](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=611s))
- Across 93 cybersecurity alerts run three times, a quarter flip-flopped their verdict; episodic memory made about 15% consistent and left 10% still inconsistent — the residual ambiguity is in the labels, not the model. ([Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [22:10](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1330s))
- A knowledge graph should be the agent's control plane, not a lookup layer: every edge is a hypothesis the agent may evaluate, and it cannot investigate outside that graph. ([Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [10:32](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=632s))
- Any secret an agent can see must be treated as already compromised, so secrets belong outside the sandbox behind a broker. ([Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [11:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=719s))
- A coding agent autonomously took a naive agent from 18% to 83% pass rate in about 10 iterations, and found +10% of improvements on a production agent humans had already optimized. ([Agents Building Agents](../talks/agents-building-agents.md), [10:10](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=610s))
- Roughly 70% of an engineer's time goes to running code already shipped to production rather than writing it — so coding was never the bottleneck, and AI-generated code is raising the production issue volume. ([Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [1:32](https://www.youtube.com/watch?v=vSx5IULvBns&t=92s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Designing Agents (The Floor Is the Frontier)](../talks/designing-agents-the-floor-is-the-frontier.md)
- [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)
- [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)
- [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

## Speakers

- [Abhilash Asokan](../speakers/abhilash-asokan.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Anna Marie Benzon](../speakers/anna-marie-benzon.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Ben Hylak](../speakers/ben-hylak.md)
- [Diane Lin](../speakers/diane-lin.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [Idan Gazit](../speakers/idan-gazit.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Ritvik Pandya](../speakers/ritvik-pandya.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)

