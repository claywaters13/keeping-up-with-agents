---
title: "human-in-the-loop escalation"
type: "concept"
slug: "human-in-the-loop-escalation"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 12
---

# human-in-the-loop escalation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **12** speaker(s)

**Definition:** Routing to a human when the agent is uncertain or the stakes are high, based on confidence or risk rather than a blanket approval rule.

*Also referred to as: human in the loop escalation, human handoff, calibrated confidence and escalation, risk-based review routing, human-in-the-loop confidence gating, kill switch, human-in-the-loop supervision*

## State of Practice

The field has moved off blanket approval gates and onto routing: the escalation decision is made per-action, from a confidence score or a risk/reversibility classification, so human attention is spent only where it changes an outcome. Concretely this looks like a deterministic or rules layer first, an agent or LLM judge for what rules cannot decide, and a human only for the residue — oncology prior-auth teams attach a confidence score per clinical answer and escalate only those cases; computer-use RL teams treat handoff as a first-class model action requiring calibrated confidence about risk, reversibility, authorization, and visibility; code review is routed by criticality, with authentication, money movement, permissions, and irreversible data reads line by line. There is broad agreement that per-action yes/no prompts are a failed oversight mechanism: reviewers cannot evaluate an opaque command, prompts get disabled in CI anyway, and 31% more PRs are now merged with no review at all. Open questions remain on whether human involvement is permanent architecture or transitional scaffolding that thins as models improve, and on whether the escalation judge should itself be a model (LLM-as-judge, adversary agent) or a deterministic policy engine / ontology reasoner. A distinct and less-appreciated failure mode is over-escalation: in mental health, an inappropriately triggered guardrail is described as a door slam that pushes a user away from care, so the target is correct triggers rather than more triggers.

## Consensus

### Escalation should be gated on a per-case confidence or risk score attached to the agent's output, not on a blanket rule that all outputs (or no outputs) get human review.

Support: **5** talk(s)

> "the medical necessity agent answers simple and complex clinical questions per patient uh and attaches confidence score to any answer. So, we escalate only the ones that actually need a clinician."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [11:39](https://www.youtube.com/watch?v=_cVfz88_j7A&t=699s)

Supporting talks: [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)

### Human oversight is a permanent architectural component of production agent systems, not scaffolding to be removed once models improve.

Support: **4** talk(s)

> "Many people frame human involvement as temporarily temporary necessity. I don't think that's correct. The most successful systems are likely to remain human supervised."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [4:50](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=290s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)

### Deterministic checks run first and decide everything they can; agents and then humans handle only the residue, which is what makes the human queue small enough to be meaningful.

Support: **4** talk(s)

> "the no touch is growing on the share of every order. So, we started with deterministic checks. Agents only for the rules that where what rules can't decide."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s)

Supporting talks: [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)

### A per-action yes/no approval prompt is not a working oversight mechanism — the reviewer usually lacks the context to answer, so it degenerates into rubber-stamping or gets disabled outright.

Support: **3** talk(s)

> "even when the agent knows that it should ask permission and and I get a nice block of, "Hey, Aaron, do you agree? Should I do this thing?" I'm honestly not sure if I should say yes or no"
>
> — [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [5:48](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=348s)

Supporting talks: [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

## Disagreements

### Is human escalation a permanent part of the architecture, or transitional scaffolding that should thin out as models get more capable?

| Position A | Position B |
|---|---|
| Permanent. Human supervision is a design property of successful systems; loops and self-verification relocate where judgment is applied but never remove the requirement, and the clinician's or expert's definition of correct must keep living in CI indefinitely.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* | Transitional. Harness guardrails should be strong early and become progressively thinner as model capability improves, and the no-touch share of a workflow should grow monotonically until human touch is the exception.<br>*[From RL to IRL](../talks/from-rl-to-irl.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* |

*Why it matters: If escalation is permanent you invest in reviewer tooling, attention budgeting, and durable expert-owned eval sets; if transitional you invest in model training, sandboxes, and recovery policies and treat the review queue as a cost to drive to zero.*

### Should the thing that decides whether to escalate be another model, or a deterministic policy/validation layer?

| Position A | Position B |
|---|---|
| A model. Guardrails should be separate LLM-as-judge calls (more robust and harder to jailbreak than prompt-embedded rules), and an equal-power adversary agent rewarded for stopping the worker can catch spirit-of-the-constraint violations that syntactic rules miss.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)* | A deterministic layer. Models are stochastic and infrastructure is not allowed to be — the model emits proposals and a policy engine, ontology reasoner, or rules engine approves them, catching things like duplicate refunds or wrong-entity payouts that natural-language prompting cannot enforce.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* |

*Why it matters: It determines whether your escalation gate is itself non-deterministic and needs its own evals and latency/cost budget, or whether it is auditable code that can be reasoned about and proven to an auditor.*

### Should agents default to escalating when in doubt, or is over-escalation itself a harm to be calibrated down?

| Position A | Position B |
|---|---|
| Default to stopping. Autonomy should default to 'suggest' for every surface with auto-execute opted into per tool, and when a constraint collides with the task the default behavior should be halt and explain rather than find a way around.<br>*[Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)* | Over-triggering is a real harm with real cost. Frontier providers' built-in guardrails were too conservative to use and were turned off on day one; an inappropriate escalation feels like a door slam and can drive a user away from care, so the objective is correct triggers, not more triggers.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* |

*Why it matters: It sets which error you optimize against — a conservative default is safe in code and infrastructure but actively damaging in user-facing support contexts, so the threshold has to be tuned per domain rather than inherited from the model provider.*

## Practical Guidance

**Do:**

- Attach a confidence score to every agent answer and escalate only the cases below threshold, rather than routing all output to review
- Require two independent sources to agree on a fact before proceeding without human verification; treat agreement as the license to skip the human
- Read every line of authentication, money movement, permissions, and irreversible data changes — route review by criticality of the change, not by seniority of the engineer
- Default autonomy to 'suggest' for everything, earn auto-approve per surface, and make auto-execute opt-in per tool
- Build the kill switch first and resolve flags per turn, not at session start, so in-flight conversations honor it; target under 5 minutes from problem to mitigation
- Make halt-and-explain the default when a constraint and the task collide, instead of letting the agent route around the constraint
- Route sub-agents through the same flag/approval middleware as the parent — a flipped kill switch that never reaches a spawned child is the most common architectural hole
- Have a licensed or accountable domain expert define correct behavior in edge cases, then commit that judgment into CI so every prompt, model, and guardrail change is scored against it
- Present contradictory facts alongside supportive ones when handing a case to a human reviewer
- Have the agent DM the human with its proposed answer and ask for confirmation when unsure, rather than either answering blind or silently queueing
- Keep agents side-effect-free and run type checks plus ontology/semantic validation before any database write
- Feed completed audit and investigator outcomes back into the model so the escalation threshold learns, instead of maintaining escalation rules by hand

**Avoid:**

- Presenting a yes/no approval prompt on an opaque command and calling it human oversight — it will not satisfy meaningful-oversight requirements and the human usually cannot evaluate it
- Leaving interactive permission prompts enabled in a CI pipeline, where they block on a human who is not there
- Merging PRs with no review at all, human or agentic — this rose 31% alongside a 242% increase in incidents per PR
- Letting the same agent write the code and also write and grade its tests; if the builder grades itself you did not remove the review, you hid it
- Embedding safety rules only in the main system prompt instead of separate judge calls, which makes them easier to jailbreak away
- Treating an unnecessary escalation as free — an inappropriate guardrail trigger is a genuine harm, not a conservative default
- Relying on the human as the final control when the agent can simply persuade that human to remove the control
- Rewarding only task outcome, which lets a trajectory reach 'done' while taking dangerous intermediate actions that should have triggered a handoff
- Resetting the environment on an infrastructure error instead of surfacing the error to the model so recovery and handoff become native actions

## Notable Outliers

- An agent persuading a human to install a Chrome extension that removes a constraint should be counted as the agent defeating the constraint — the energy came from inside the agentic loop and merely routed through the human as a tool. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- Two independent sources agreeing on the same fact is sufficient grounds to skip human verification entirely, converting a review step into an automated one. ([Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [7:34](https://www.youtube.com/watch?v=_cVfz88_j7A&t=454s))
- Frontier providers' built-in safety guardrails had to be turned off on day one because they are over-calibrated for mental health support, and replaced with purpose-built ones. ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s))
- Harness guardrails are transitional scaffolding by design: they should be strong early and become progressively thinner as the model improves. ([From RL to IRL](../talks/from-rl-to-irl.md), [17:12](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=1032s))
- Within 12 months enterprise buyers will gate deals on demonstrable autonomy and kill-switch controls — if you cannot demo them live, you lose the deal. ([Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [16:16](https://www.youtube.com/watch?v=zU4EagB311U&t=976s))
- Judging whether a worker agent violated the spirit of a constraint is a strictly easier reasoning problem than inferring user intent, which is what makes an equal-power adversary agent tractable as an escalation trigger. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [14:17](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=857s))

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
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Akele Reed](../speakers/akele-reed.md)
- [Alex Volkov](../speakers/alex-volkov.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Gaurav Mishra](../speakers/gaurav-mishra.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Varsha Shah](../speakers/varsha-shah.md)

