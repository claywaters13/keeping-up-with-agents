---
title: "incident response automation"
type: "concept"
slug: "incident-response-automation"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 10
---

# incident response automation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **10** speaker(s)

**Definition:** Agents in the operational loop — triaging alerts, investigating root cause, and remediating production issues.

*Also referred to as: incident triage and root cause investigation, on-call automation, root cause analysis, log monitoring agents, security alert triage, automated remediation, self-healing automation, hypothesis-driven root cause analysis*

## State of Practice

The field has stopped treating production operation as the tail end of shipping an agent and started treating it as the main system: speakers repeatedly framed the post-launch loop — detect, investigate, propose fix, gate, redeploy — as the actual product, with Resolve AI citing ~70% of engineer time spent running code rather than writing it and GitHub putting hands-on-keyboard typing at ~5%. The dominant architecture is layered rather than agentic-all-the-way-down: cheap deterministic or statistical detection first (per-client execution-graph baselines, MMD/KL divergence, rule engines), an agent woken only for the cases rules cannot decide, and a bounded remediation path (5–10% canary rollout, one-PR-max automations, branch-per-hypothesis with rollback on regression). The consensus bottleneck is no longer model capability but environment-specific context — knowledge graphs used as a control plane over which hypotheses an agent may pursue, per-customer learning systems, semantic and episodic memory that beats fine-tuning for consistency. Reliability engineering for these loops is quantitative and unflattering: Datadog found ~25% of 93 cybersecurity alerts flip-flopped verdicts across three runs, and that LLM self-reported uncertainty is a worse triage signal than cross-run or cross-model disagreement. What remains unsettled is how much of the loop closes without a human: some teams auto-open PRs and run ten unattended optimization iterations, while others insist that ambiguous cases escalate by construction and that a fix agent must never review its own diagnosis.

## Consensus

### Pre-production testing cannot enumerate agent failure modes; production traces are the only source of the failure catalog, and the eval suite is built backwards from them.

Support: **3** talk(s)

> "you don't know what your agent will do until it is in the production."
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [2:56](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=176s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Agents Building Agents](../talks/agents-building-agents.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)

### Deterministic and statistical layers should run first and handle everything they can; the agent is invoked only for the residue those layers cannot decide.

Support: **3** talk(s)

> "any complex workflows will have deterministic parts and agentic parts. Don't let agents actually run the deterministic part, right?"
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [13:51](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=831s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)

### The limiting factor for operational agents is captured environment-specific context — knowledge graphs, memory, per-customer learning systems, harness — not model capability, which everyone has equal access to.

Support: **5** talk(s)

> "we need full stack AI. It's not just about the models anymore, it's about the context around the models and what the models can do inside of a specific domain."
>
> — [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [2:51](https://www.youtube.com/watch?v=vSx5IULvBns&t=171s)

Supporting talks: [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Agents Building Agents](../talks/agents-building-agents.md)

### Cases where the agent lacks sufficient evidence must route to a human by construction rather than receive an automated decision, and the automated share is grown incrementally from that baseline.

Support: **3** talk(s)

> "for the cases we do not have this enough information, we move keep that for human escalation."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [13:13](https://www.youtube.com/watch?v=_cVfz88_j7A&t=793s)

Supporting talks: [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Agents Building Agents](../talks/agents-building-agents.md)

### Automated remediation must be bounded and reversible — staged rollout, branch-and-rollback on regression, or a hard cap on how much output one automation may produce.

Support: **3** talk(s)

> "once you know the risk either you can go with uh roll out that system uh um solution for say 5% or 10% of your uh machines monitor it verify everything looks good and then you roll out for your 100% of the nodes"
>
> — [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [12:55](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=775s)

Supporting talks: [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md), [Agents Building Agents](../talks/agents-building-agents.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

### Task completion signals are not a quality metric — an agent run can be technically successful, or recover by luck, while failing the user and raising no alert.

Support: **3** talk(s)

> "So, technically it's successful but still failing the task."
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [4:54](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=294s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Agents Building Agents](../talks/agents-building-agents.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

## Disagreements

### What should gate an agent-authored production fix: automated metric/eval thresholds, or mandatory human or independent-agent review before anything ships?

| Position A | Position B |
|---|---|
| Automated gates are sufficient. Let the agent iterate unattended against evals on its own branch, roll back on regression, and open a PR itself; background automation running while you sleep is the point.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)* | A judgment gate outside the fixing agent is required. Route ambiguous or low-confidence cases to a clinician/SME, have a separate fresh-context agent review the fix because the fixer is biased toward its own diagnosis, and validate failure clusters with humans before implementing anything.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)* |

*Why it matters: This sets the throughput ceiling of the loop and where you spend headcount — a purely eval-gated loop scales with tokens but inherits every blind spot in the eval suite, while a review-gated loop caps at human review bandwidth and makes calibrating that reviewer the critical engineering task.*

### Should investigative reasoning be consolidated into a single agent, or deliberately split across independent agents?

| Position A | Position B |
|---|---|
| Exactly one agent must own end-to-end reasoning. Every handoff loses context and the loss compounds; sub-agents may return investigation results but never reasoning or judgment, and copying a human analyst's step decomposition is the wrong architectural basis.<br>*[Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)* | Independent agents evaluating each other is the mechanism that works. Use an agent-as-a-judge with full trace analysis on top of the operating agent, and keep the fix agent separate from the review agent precisely so their context and incentives differ.<br>*[The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)* |

*Why it matters: It decides whether you invest in context-sharing infrastructure for one long-running agent (50+ turns, high token cost per incident) or in orchestration and handoff protocols between several — and the two designs have opposite failure modes: incoherent conclusions versus self-confirming ones.*

### Should teams build their own production monitoring and diagnosis loop, or adopt a platform that carries the learning system?

| Position A | Position B |
|---|---|
| Build it yourself. Vendor tools offer the same shape of system, but you know what you are looking for, and the internal harness around the model — not the model or the tool — is the competitive advantage.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)* | The hard part is a durable per-environment learning system plus eval infrastructure at scale, which is what a platform supplies; a generic agent without it cannot be effective, and mature teams end up running deterministic evals, LLM-as-a-judge, and agent-as-a-judge together.<br>*[Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)* |

*Why it matters: Both sides agree the environment-specific knowledge layer is the moat, so the question is whether that layer is buildable by a small team as a side effect of operating their own product, or whether it needs dedicated infrastructure a vendor amortizes across customers.*

## Practical Guidance

**Do:**

- Gate deep analysis behind a cheap tier-one check: if end-to-end execution matches the baseline, skip every subsequent tier.
- Scope anomaly baselines per client and per business operation (real-time payments vs. wire), not per HTTP method, and give new endpoints a fresh baseline instead of a generic one to avoid cold-start false positives.
- Canary automated remediation to 5–10% of machines, verify, then go to 100%; make the monitoring system deployment-aware so rollback decisions are correct.
- Emit telemetry asynchronously (OpenTelemetry → Kafka → stream processing) with tail-based sampling, and split detection into a fast hot path for automatable decisions and a slower, more accurate reconciliation path.
- Run each optimization hypothesis on its own git branch and roll back on regression; explicitly forbid the optimizing agent from editing golden datasets or scorers.
- Run evals multiple times and average, and use disagreement across runs or across models — not the model's self-reported uncertainty — to select cases for human review.
- Feed every production failure mode you find back into the golden dataset so the eval suite catches that regression next time.
- Give the monitoring agent access to trajectories, metrics, the database, and the UI; without all four its diagnosis is guesswork.
- Enforce guardrails as deterministic configuration outside the agent, and hold secrets outside the agent's sandbox behind a broker — treat any secret the agent can see as compromised.
- Bound automation output: allow an automation to produce nothing at all, and cap it (e.g. a single PR) so it cannot denial-of-service its owner.
- Require two independent sources to agree before proceeding without human verification, and present contradictory facts alongside supportive ones in the agent's answer.
- Ship anomaly output with supporting explanatory data rather than a single opaque score — 'your health score is 22' is not actionable.
- Pick a sustainable cadence for the expensive analyses: a live-data failure report once per sprint, a token-heavy session analyzer weekly.
- Close the loop until you personally are the bottleneck, then remove yourself — in that order.
- Add a self-healing loop around any RPA/browser automation, and encode your own site's DOM in a purpose-built skill rather than relying on a generic computer-use agent.

**Avoid:**

- Prompting guardrails at the agent — a third party can prompt-inject past them.
- Using LLM-reported confidence scores to decide what needs human review; the model doesn't know what it doesn't know.
- Fixed hard-coded post-release checks and wait intervals — every rollout is unique, and feature flags and infra changes bypass CI/CD with no monitoring at all.
- Using a language model for signal detection (e.g. spotting a sales drop) that statistical methods already handle.
- Letting an agent infer entity and KPI relationships from raw tables — it doesn't scale and it invents relationships not present in the data.
- Distributing judgment across a chain of specialized agents modeled on a human analyst's workflow steps; each handoff drops context.
- Treating a completed run as a success, or letting an agent that recovered by luck pass silently without an alert.
- Letting the agent that produced the fix also review it — it is biased toward its own diagnosis and eager to ship the PR.
- Shipping to production without observability; you are blind to failures you cannot diagnose.
- Blindly trusting single-source LLM extraction as a substitute for review — it improves efficiency but does not eliminate the human.
- Hand-building a custom integration per portal or per system instead of generating configs over a shared action repository.
- Sharing one latency baseline across clients with legitimately different normal behavior — it just generates alert noise.

## Notable Outliers

- A coding agent autonomously took a naive agent from an 18% to an 83% pass rate in about 10 iterations, and found +10% on an internal benchmark for an agent humans had already optimized. ([Agents Building Agents](../talks/agents-building-agents.md), [10:10](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=610s))
- Across 93 cybersecurity alerts run three times, a quarter flip-flopped their verdict; episodic memory made about 15% consistent and 10% stayed inconsistent — the residue is genuine label ambiguity, not model failure. ([Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [22:10](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1330s))
- A single consolidated agent reaches root cause in 20–30 minutes over 50+ turns and a large token spend for analysis that previously took an analyst three to four weeks — the token cost is worth it. ([Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [13:10](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=790s))
- Two engineers' PR agent and review agent open ten times more PRs per day than the three humans on the team. ([The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [10:19](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=619s))
- Slack is the wrong surface for building software because it was designed for the average office worker — directly against the prevailing 'meet engineers in Slack' pattern. ([Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [13:48](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=828s))
- The era of effectively unlimited tokens is ending, so operational agents now have to be designed against a real cost budget rather than assuming cheap inference. ([Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [2:19](https://www.youtube.com/watch?v=vSx5IULvBns&t=139s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [The Future of Evals: From LLM as a Judge to Agent as a Judge](../talks/the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)
- [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

## Speakers

- [Abhilash Asokan](../speakers/abhilash-asokan.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)
- [Diane Lin](../speakers/diane-lin.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [Idan Gazit](../speakers/idan-gazit.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Ritvik Pandya](../speakers/ritvik-pandya.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)

