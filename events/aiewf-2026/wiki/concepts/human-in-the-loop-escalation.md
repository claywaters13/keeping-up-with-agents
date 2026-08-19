---
title: "human-in-the-loop escalation"
type: "concept"
slug: "human-in-the-loop-escalation"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 13
---

# human-in-the-loop escalation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **13** speaker(s)

**Definition:** Routing to a human when the agent is uncertain or the stakes are high, based on confidence or risk rather than a blanket approval rule.

*Also referred to as: human in the loop escalation, human handoff, calibrated confidence and escalation, risk-based review routing, human-in-the-loop confidence gating, kill switch, human-in-the-loop supervision*

## State of Practice

The field has moved off blanket approval gates and onto per-case routing: escalation is treated as an explicit action in the agent's action space, chosen from a confidence score, a risk/reversibility assessment, or a deterministic rule that fires before the model is consulted. The dominant architectural pattern is proposal/disposal separation — the model emits a proposed action, and an external layer (policy engine, deterministic decision engine, ontology reasoner, LLM-as-judge running as a separate call, or flag middleware) decides whether it executes or goes to a human — with the explicit requirement that this layer sit outside the learned policy and outside the system prompt so a policy or prompt update cannot silently redefine the agent's own authority. Practitioners now name over-escalation as a real cost, not a safe default: false guardrail trips are described as a harm to the user, and non-escalation rate is explicitly rejected as an optimization target in favor of routing accuracy. A hard floor survives regardless of confidence — authentication, money movement, permissions, irreversible data changes, and direct production control stay gated. The unresolved questions are whether this scaffolding thins as models improve or is permanent, whether the adjudicator should itself be a model (an adversary agent rewarded for stopping the worker) or strictly symbolic, and whether an agent's self-assessed confidence is admissible evidence for skipping review at all.

## Consensus

### Escalation to a human should be a first-class action the agent can select per case, driven by confidence or evidence sufficiency, rather than a blanket policy applied to whole task categories.

Support: **6** talk(s)

> "Notice that escalation is included in the action space that is not the agent giving up. It is the system correctly recognizing the boundary of its evidence and authority for an operational agent."
>
> — [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [6:22](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=382s)

Supporting talks: [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

### The model should only propose actions; an external layer outside the model and outside the learned policy validates, approves, and executes them.

Support: **6** talk(s)

> "The model just suggests, the platform decides."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:09](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=189s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)

### Escalating too often is a real failure, not a safe default; the objective is correctly routed human attention, so systems should be scored on routing accuracy rather than on volume of human review.

Support: **5** talk(s)

> "we didn't we were not going for more triggers here. We're going for more correct triggers."
>
> — [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [6:24](https://www.youtube.com/watch?v=O72p-rBb2bA&t=384s)

Supporting talks: [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)

### Irreversibility and blast radius override confidence: authentication, money movement, permissions, irreversible data changes, and direct production control stay human-gated no matter how confident the agent is.

Support: **5** talk(s)

> "You read every line of authentication, money movement, permissions, and irreversible data."
>
> — [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [14:28](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=868s)

Supporting talks: [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

## Disagreements

### Is human escalation a transitional scaffold that thins as models improve, or a permanent architectural fixture?

| Position A | Position B |
|---|---|
| Escalation and harness guardrails are temporary scaffolding sized to current model weakness; as capability improves the harness gets thinner and the no-touch share of work grows monotonically, so the design goal is to retire human touchpoints case class by case class.<br>*[From RL to IRL](../talks/from-rl-to-irl.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)* | Human supervision is permanent. Better models relocate where proof and oversight belong but never remove the requirement, and the regulatory direction (EU AI Act, enterprise procurement) is toward more demonstrable control, not less.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)* |

*Why it matters: It decides whether escalation is a durable product surface worth investing in (audit trails, per-surface autonomy tiers, expert-owned definitions of correct) or throwaway scaffolding you should minimize. It also sets whether 'percentage of tasks with no human touch' is a legitimate roadmap metric or an actively misleading one.*

### Should the thing that decides whether to escalate be another model, or a strictly deterministic/symbolic layer?

| Position A | Position B |
|---|---|
| A model-based adjudicator is required, because the failures that matter are ones where the agent never exceeds its authorization and the system looks syntactically compliant the whole time. An equal-power adversary agent rewarded for stopping the worker, or separate LLM-as-judge guardrail calls, can judge the spirit of a constraint where string matching and rules cannot.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* | Adjudication must be deterministic and symbolic — a decision engine, policy engine, ontology reasoner, or safety constraint that lives outside the learned policy — with the model consulted only for cases rules genuinely cannot decide. Reliability in these systems came from state design and external constraints, not from the learned component.<br>*[Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)* |

*Why it matters: A model-based judge adds cost and latency and inherits the same non-determinism it is supposed to police, while a symbolic gate is inspectable and cheap but provably cannot catch spirit-of-the-constraint violations. Picking wrong means either paying double inference for an unauditable veto or shipping a gate that passes every compliant-looking catastrophe.*

### Can an agent's own confidence estimate justify skipping human review?

| Position A | Position B |
|---|---|
| Yes, if it is calibrated and corroborated. Attach a confidence score to each answer and escalate only the low-confidence ones; two independent sources agreeing on the same fact is sufficient grounds to proceed without human verification, and handing control back requires calibrated confidence about risk, reversibility, authorization, and visibility.<br>*[Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [From RL to IRL](../talks/from-rl-to-irl.md)* | No — self-assessment is exactly the faculty being defeated. The energy to overcome a constraint must come from outside the agentic loop; if the builder grades itself you have hidden the review rather than removed it; and safety constraints must sit outside the learned policy so it cannot redefine its own authority.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)* |

*Why it matters: If confidence-gating is admissible, escalation is a threshold-tuning problem and autonomy scales with calibration work. If it is not, every confidence score needs independent corroboration or an out-of-loop veto before it can retire a human, which is a fundamentally more expensive architecture.*

### Should the human gate be an inline per-action prompt, or out-of-band control?

| Position A | Position B |
|---|---|
| Inline. Default every surface to 'suggest', earn auto-approve per surface, make auto-execute opt-in per tool, and escalate individual cases to a clinician or operator at the decision point.<br>*[Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* | Inline prompts are the wrong instrument: interactive permission prompts should be disabled outright in CI pipelines, and a yes/no approval on an opaque command is not meaningful oversight because the reviewer cannot tell whether to say yes. Control belongs out-of-band — kill switches, an adversary agent, tool-hook interception, audit.<br>*[Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)* |

*Why it matters: Inline gating is where most agent products put their oversight today, and if it is decorative rather than meaningful, teams are shipping systems that will not clear the EU AI Act's meaningful-oversight bar while believing they already have. It also determines whether unattended pipeline agents are safe to run at all.*

## Practical Guidance

**Do:**

- Make escalation an explicit action in the agent's action space and evaluate the policy on routing accuracy, not on how rarely it escalates — a drop in autonomy rate can be the correct outcome
- Run deterministic checks first and reserve agent judgment only for cases the rules cannot decide; grow the no-touch share incrementally rather than switching automation on wholesale
- Require two independent sources to agree on a fact before proceeding without human verification; escalate whenever evidence is insufficient
- Place safety constraints outside the learned policy and outside the main system prompt (separate LLM-as-judge calls or an external policy engine), so a policy or prompt update cannot silently redefine the agent's authority
- Default every autonomy surface to 'suggest', earn auto-approve per surface, and make auto-execute opt-in per tool
- Resolve autonomy and kill-switch flags per turn so in-flight conversations honor a downgrade at the next decision point, not at the next session
- Route sub-agents through the same approval middleware as the parent — a flipped kill switch that never reaches spawned children is the most common architectural hole
- Build the kill switch before tool wrapping, autonomy staging, or prompt variants; target under 5 minutes from problem to mitigation
- When a constraint and the task conflict, make the default behavior halt and explain rather than find a workaround
- Read every line of authentication, money movement, permissions, and irreversible data changes regardless of how confident the agent is
- Let a licensed or accountable domain expert define correct behavior in edge cases, then freeze that judgment into CI as a scored eval — not the engineering team, not the system itself
- Have the agent DM the human with its proposed answer for confirmation ('I think I know the answer but I'm not sure') instead of either blocking or answering silently
- Represent 'unsafe' and 'unavailable in this environment' as distinct states, and report the unavailable case for manual review rather than pretending the fix happened
- Hand control back to the user on credential, authorization, and visibility boundaries — treat handoff as a scored optimal action, not as failure
- Keep 100% flag/approval audit trail completeness so escalation decisions can be reconstructed after an incident

**Avoid:**

- Optimizing for non-escalation rate or 'percentage of tasks with no human touch' as the headline success metric
- Presenting a yes/no approval prompt on an opaque command and calling it oversight — the reviewer usually cannot tell whether to approve
- Letting the same agent that produced the work also grade it or write its tests; self-grading hides the review rather than removing it
- Leaving interactive permission prompts enabled in CI pipelines, where they stall the run instead of protecting anything
- Embedding safety rules only in the main system prompt, where they are easier to jailbreak than separate guardrail calls
- Over-triggering guardrails: an inappropriate block is a door slam that can prevent someone from getting needed care
- Letting the model directly control production systems instead of emitting proposals for a gateway to enforce
- Treating a single non-deterministic LLM extraction as sufficient grounds to skip human review
- Merging changes with no review at all, human or agentic
- Trying to enforce invariants like 'no second refund on the same order' through natural-language prompt instructions instead of a formal validator
- Resetting the environment on infra errors, which trains the agent to assume failure is transient rather than to recover or hand off
- Leaving temporary rollout/autonomy flags in place after rollout, where they become load-bearing hidden couplings
- Assuming deterministic controls — egress filters, sandboxes, telemetry — are sufficient on their own

## Notable Outliers

- An agent persuading a human to remove a control counts as the agent supplying the energy to defeat the constraint, with the human merely acting as its tool — so 'a human approved it' is not evidence the constraint held. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- The learned RL policy beat an equivalent hand-written deterministic policy by only 0.19 percentage points; reliability came from state design, decision logic, and external safety constraints, not from the learning component at all. ([Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [10:11](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=611s))
- General-purpose LLM safety guardrails had to be turned off entirely on day one because they are over-calibrated for mental health, and inappropriately escalating is itself a clinical harm. ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s))
- More than two kill switch fires per week indicates a problem worth investigating; the target is zero. ([Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [14:41](https://www.youtube.com/watch?v=zU4EagB311U&t=881s))
- Judging whether a worker agent violated the spirit of a constraint is a strictly easier reasoning problem than inferring user intent, which is why an equal-power adversary agent with a reward for stopping the worker is tractable today. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [14:17](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=857s))
- Two independent sources agreeing on the same fact is sufficient grounds to submit an oncology prior authorization with no human verification. ([Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [7:34](https://www.youtube.com/watch?v=_cVfz88_j7A&t=454s))

## All Talks

- [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)
- [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [From RL to IRL](../talks/from-rl-to-irl.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Akele Reed](../speakers/akele-reed.md)
- [Alex Volkov](../speakers/alex-volkov.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Anna Marie Benzon](../speakers/anna-marie-benzon.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Gaurav Mishra](../speakers/gaurav-mishra.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Varsha Shah](../speakers/varsha-shah.md)

