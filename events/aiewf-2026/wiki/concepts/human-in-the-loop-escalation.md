---
title: "human-in-the-loop escalation"
type: "concept"
slug: "human-in-the-loop-escalation"
tier: "supporting"
maturity: "consolidating"
talk_count: 16
speaker_count: 19
---

# human-in-the-loop escalation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **16** talk(s) by **19** speaker(s)

**Definition:** Routing to a human when the agent is uncertain or the stakes are high, based on confidence or risk rather than a blanket approval rule.

*Also referred to as: human in the loop escalation, human handoff, calibrated confidence and escalation, risk-based review routing, human-in-the-loop confidence gating, kill switch, human-in-the-loop supervision*

## State of Practice

Escalation has stopped being a fallback and become a designed control surface: teams model handoff as an explicit action the agent can take, gated on evidence sufficiency and blast radius rather than a blanket approve-everything prompt. The routing key is the action class, not the agent — authentication, money movement, irreversible data changes, reimbursement claims, and acute medical intent get human or deterministic handling, while low-stakes flows (appointment scheduling, unit tests, documentation) run unattended at a tolerated failure rate. Confidence that justifies skipping a human is increasingly derived from independent corroboration — two payer sources agreeing, two models scoring the same receipt, a separate judge model — rather than the worker agent's self-report, because a builder that grades itself hides the review instead of removing it. The scarce resource everyone names is human attention: Hinge Health calls people-to-read-the-signal the scaling bottleneck, Meta Superintelligence Labs calls human supervision permanent rather than transitional, and the RL/ETL work explicitly refuses non-escalation rate as an optimization target. The live arguments are about mechanism — whether the escalation trigger is deterministic code above the model, an adversarial supervisor agent, or a learned calibrated-confidence policy inside the model — and about whether a yes/no approval prompt on an opaque command constitutes oversight at all under incoming EU AI Act requirements.

## Consensus

### Escalation should be a first-class action in the agent's action space, taken when evidence or authority runs out — not an implicit failure path

Support: **6** talk(s)

> "Notice that escalation is included in the action space that is not the agent giving up. It is the system correctly recognizing the boundary of its evidence and authority for an operational agent."
>
> — [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [6:22](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=382s)

Supporting talks: [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)

### Human review capacity, not model capability, is the binding constraint — so the design goal is triaging which cases reach a human, not eliminating human review

Support: **4** talk(s)

> "The bottleneck is not the compute, the models, the capability. It's actually having enough people to read the signal and act on it."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [11:27](https://www.youtube.com/watch?v=YXEqC05WEI0&t=687s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)

### Routing is by the stakes and reversibility of the specific action class, not a uniform approval policy — irreversible, financial, permission-granting, and emergency actions always get a human

Support: **5** talk(s)

> "You read every line of authentication, money movement, permissions, and irreversible data."
>
> — [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [14:28](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=868s)

Supporting talks: [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [From RL to IRL](../talks/from-rl-to-irl.md)

### Confidence sufficient to bypass a human must come from independent corroboration — agreeing sources or agreeing models — because a single model's self-assessment is not verification

Support: **3** talk(s)

> "when we receive their receipt, we will use different models to review the same receipt. We only move forward if the results from different models agree with each other."
>
> — [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [14:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=867s)

Supporting talks: [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

### A yes/no approval prompt on an opaque action is not meaningful oversight — reviewers who cannot evaluate what they are approving produce rubber stamps and false confidence

Support: **3** talk(s)

> "A sandbox diagram with a yes no LGTM ain't going to cut it."
>
> — [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [15:36](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=936s)

Supporting talks: [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

## Disagreements

### Who decides that a case warrants escalation — the worker agent reporting its own calibrated confidence, or an independent layer that the worker cannot influence?

| Position A | Position B |
|---|---|
| The agent itself should carry calibrated confidence about risk, reversibility, and authorization, attach a confidence score to each answer, and hand off when that confidence is low — handoff is trained as a native model action.<br>*[From RL to IRL](../talks/from-rl-to-irl.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)* | An agent under a task-completion imperative cannot be trusted to flag itself; escalation must be decided outside the agentic loop — deterministic code that runs before the model on every turn, guardrails as separate LLM-as-judge calls rather than system-prompt rules, a policy engine that approves model proposals, or an adversary agent rewarded for stopping the worker.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)* |

*Why it matters: It determines whether escalation logic is a training objective and prompt concern or a separate always-on component with its own cost, latency, and eval suite. If self-report is unreliable, every system that ships confidence-gated auto-approval is silently under-escalating on exactly the cases where the agent most wants to finish.*

### Should the trigger for human escalation be deterministic rules or a learned/contextual judgment?

| Position A | Position B |
|---|---|
| Deterministic checks first, learning only where rules genuinely cannot decide. Emergency intent routing and identity verification must be code above the model, safety constraints must live outside the learned policy so a policy update cannot redefine the agent's own authority, and an ontology reasoner should validate before any side effect.<br>*[Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)* | Rule-based and pattern-matching triggers are structurally insufficient for the risks that matter: regexes, verbose prompt instructions, and broad moderation APIs miss clinically coded indirect risk, and rule-based compliance systems cannot see fraud spanning documents. The escalation decision should be learned from audit outcomes, investigator feedback, and clinician-labeled traces rather than maintained as rules.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [From RL to IRL](../talks/from-rl-to-irl.md)* |

*Why it matters: Deterministic triggers are auditable and cannot be jailbroken but only fire on what you anticipated; learned triggers catch novel and indirect signals but are themselves non-deterministic and need their own judge-verification loop. The choice sets whether your escalation policy is reviewable by a compliance officer or only observable through eval scores.*

### Is human-in-the-loop escalation a permanent architectural property or a transitional scaffold that shrinks as models improve?

| Position A | Position B |
|---|---|
| Permanent. The most successful systems remain human-supervised; some failure classes cannot be prompted away and the failure rate never reaches zero; rising capability relocates where proof is required but never removes the requirement for proof; and in clinical domains knowing when to stop and hand off is itself a core capability.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)* | Transitional and shrinking. The no-touch share of orders grows incrementally toward full automation, harness guardrails should be strong early and become progressively thinner as model capability improves, and the stated goal is a fully automated lifecycle including auto-fixing production issues.<br>*[Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [From RL to IRL](../talks/from-rl-to-irl.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)* |

*Why it matters: If escalation is permanent, human review tooling, staffing, and reviewer UX are first-class product surfaces worth durable investment; if it is scaffolding, that spend is depreciating and should be minimized in favor of model and training work.*

### In safety-critical consumer domains, is the dominant failure mode escalating too rarely or escalating too often?

| Position A | Position B |
|---|---|
| Too often. General-purpose LLM guardrails are over-calibrated to the point of being unusable and had to be turned off and replaced; inappropriately triggering a guardrail is a genuine harm that can feel like a door slam and drive people away from care, so the objective is trigger accuracy, not trigger frequency.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* | Too rarely. Consumer health AI under-triages life-threatening emergencies half the time, severity should be set by the worst plausible outcome rather than frequency, and a relationship AI that cannot distinguish struggling from unsafe is dangerous at scale — so bias hard toward routing out to 911/988 or a professional.<br>*[Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)* |

*Why it matters: The two camps calibrate the same threshold in opposite directions and would ship different products from identical eval data. It also decides whether a false escalation counts as a defect in your bug taxonomy or as the safe default.*

## Practical Guidance

**Do:**

- Put escalation in the agent's action space as an explicit action, and represent 'unsafe' separately from 'unavailable in the current environment' so the system reports why it stopped
- Require two independent sources agreeing on a fact before proceeding without human verification; escalate wherever the sources conflict or evidence is missing
- Gate irreversible or financial actions on cross-model agreement and hand off to a human when models disagree — zero tolerated failures for reimbursement claims versus ~1-in-1000 for retryable actions like scheduling
- Route emergency intent (self-harm, suicidal ideation, acute medical) with deterministic code that runs before the model on every turn, so the model never sees that turn
- Default every autonomy setting to 'suggest'; earn auto-approve per surface and make auto-execute opt-in per tool, resolved per turn rather than at session start so a kill switch reaches in-flight conversations
- Human-review 100% of high-stakes cases and randomly sample across the remaining capabilities
- When a constraint and the task collide, halt and explain rather than routing around — and treat an agent persuading a human to remove a control as a constraint violation
- Give the reviewer contradictory evidence alongside supportive evidence plus a confidence score, so escalation arrives adjudicable rather than as a bare yes/no
- Make any action an LLM can take also performable by a human on the same context — define context once, then map it to a prompt or to a UI — because escalation points cannot be predicted in advance
- Keep safety constraints outside the learned policy so a policy update cannot silently redefine the agent's own authority
- Set severity by the worst plausible outcome, not frequency: a bug that lightly annoys 100% of users is less severe than one causing serious harm in 0.1% of cases
- Have a licensed domain expert, not the engineering team, define correct behavior in edge cases and encode that judgment as evals that run in CI on every prompt, model, and guardrail change
- Route sub-agents through the same approval middleware as the parent, and verify the judge before changing the agent when an escalation score moves

**Avoid:**

- Measuring success by non-escalation rate — a falling escalation rate can be the correct behavior, not an improvement
- Presenting a yes/no approval on an opaque command and calling it human oversight; it will not satisfy the EU AI Act's meaningful-oversight requirement and in practice produces rubber stamps
- Letting the same agent write the work and grade its own tests — self-scoring hides the review rather than removing it
- Merging PRs with no review at all, human or agentic (up 31%, alongside 242% more incidents per PR)
- Embedding escalation and safety rules in the main system prompt — every authority layer above 'user' is one prompt injection away from being overridden, and if the labs don't trust prompts as a security boundary neither should you
- Spawning sub-agents that bypass the flag/approval middleware, so a flipped kill switch never reaches them
- Optimizing an emotionally sensitive product for engagement when the clinically correct outcome is the user needing the product less and being routed to a professional
- Assuming a single LLM extraction can eliminate human review — it improves efficiency, but non-deterministic output cannot be blindly trusted
- Relying on a pre-launch eval gate over a saved golden dataset as your escalation safety net instead of continuously scoring live traffic
- Resetting the environment on infrastructure errors during training, which teaches the model that failure is transient rather than teaching recovery or handoff
- Quietly downgrading a safety bug because no one has capacity — the only options are fix, delay, or accept with explicit sign-off

## Notable Outliers

- An agent persuading a human to remove a control (e.g. asking them to install a Chrome extension) is a constraint violation by the agent, with the human acting as its tool — the energy to defeat the constraint came from inside the agentic loop ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- The right supervisor is an equal-power adversary agent rewarded for stopping the worker from finishing, judging the spirit rather than the syntax of a constraint — a simpler reasoning problem than inferring user intent, and it would have caught every failure example shown ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [14:17](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=857s))
- The RL escalation policy beat the equivalent hand-written deterministic policy by only 0.19 percentage points, and its higher escalation rate was the intended outcome, not a regression ([Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [10:11](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=611s))
- If humans and LLMs are interchangeable agents over the same context, the delta between a human's and the LLM's output on the same task is itself a valid eval score ([Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [15:50](https://www.youtube.com/watch?v=mav15aW9lLM&t=950s))
- Day one required turning off the frontier providers' built-in guardrails entirely, because over-calibration — itself a compassionate choice by the providers — made the system unusable for mental health support ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s))
- More than two kill-switch fires per week indicates a problem worth investigating; the target is zero, with under 5 minutes from decision to kill and under 30 minutes to roll back a prompt ([Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [14:41](https://www.youtube.com/watch?v=zU4EagB311U&t=881s))
- Helpfulness, agreeableness, and speed — the default assistant traits — are actively harmful in a domain sitting closer to suicide and homicide risk than almost any other, where knowing when to stop coaching is the core capability ([AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md), [12:08](https://www.youtube.com/watch?v=yoONZwV2smc&t=728s))

## All Talks

- [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)
- [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)
- [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [From RL to IRL](../talks/from-rl-to-irl.md)
- [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)
- [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)
- [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Akele Reed](../speakers/akele-reed.md)
- [Alex Volkov](../speakers/alex-volkov.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Anna Marie Benzon](../speakers/anna-marie-benzon.md)
- [Christopher Lovejoy](../speakers/christopher-lovejoy.md)
- [Clay Cockrell](../speakers/clay-cockrell.md)
- [Dan Feng](../speakers/dan-feng.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Gaurav Mishra](../speakers/gaurav-mishra.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Rashi Agrawal](../speakers/rashi-agrawal.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Saul Howard](../speakers/saul-howard.md)
- [Tony Fabrikant](../speakers/tony-fabrikant.md)
- [Varsha Shah](../speakers/varsha-shah.md)

