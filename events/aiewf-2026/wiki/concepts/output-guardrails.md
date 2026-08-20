---
title: "output guardrails"
type: "concept"
slug: "output-guardrails"
tier: "supporting"
maturity: "consolidating"
talk_count: 15
speaker_count: 20
---

# output guardrails

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **15** talk(s) by **20** speaker(s)

**Definition:** Runtime checks on model input and output that block, filter, or rewrite unacceptable content before it reaches users or systems.

*Also referred to as: output validation, agent guardrails, llm guardrails, input and output guardrails, deterministic guardrails, guardrail metrics, neuro-symbolic guardrails*

## State of Practice

The conference's dominant position is that a guardrail is code, not a prompt: anything expressed as instructions to the model is one prompt injection away from being overridden, so hard constraints must live in deterministic layers that run above or after the model. The concrete architecture that recurred across healthcare, consumer, and marketplace talks is a layered one — deterministic pre-model routing for high-stakes intents (self-harm, emergencies, identity verification), separate LLM-as-judge calls for nuanced checks that regex cannot catch, and a deterministic post-generation veto that every surface passes through by default. Teams accept the latency and cost of extra guardrail model calls when stakes justify it, and deliberately build redundant, overlapping gates on a Swiss-cheese logic. A second theme is that guardrails are themselves instrumented software: you must measure trigger rates, rejection rates, and human-override rates, verify the judge before trusting its score, and treat every new production failure as a new judge. The sharpest live tension is calibration — general-purpose provider guardrails are widely described as over-conservative for domains like mental health, where a false trigger is itself a harm, while security speakers argue nothing short of pre-execution proof is adequate for tool-calling agents.

## Consensus

### A prompt or system-prompt instruction is not a guardrail; enforcement must live in deterministic code outside the model, because a third party can prompt-inject the agent past any instruction.

Support: **6** talk(s)

> "A model is not a guardrail. A model with a system prompt is also not a guardrail. Code that runs above the model is closer."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [6:48](https://www.youtube.com/watch?v=YXEqC05WEI0&t=408s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)

### Safety checking must be structurally separated from generation — a separate judge, validator, or critic pass rather than the generating model checking itself in the same loop.

Support: **6** talk(s)

> "The agent acts and validate its own output in the same loop. There's no separation, no second opinion."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [28:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1730s)

Supporting talks: [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

### Guardrails must be continuously measured in production — trigger/rejection rates, override rates, live-traffic judge scores — because a pre-launch eval gate does not make a system safe.

Support: **4** talk(s)

> "we all know that a simple eval gate does not make a system safe."
>
> — [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [9:12](https://www.youtube.com/watch?v=O72p-rBb2bA&t=552s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### In high-stakes domains, the correct definition of acceptable output must be authored by a domain expert (clinician, product/policy/legal) and encoded into evals, not decided by the engineering team or inferred by the model.

Support: **3** talk(s)

> "our system isn't deciding what correct is in a clinical edge case like this one. A licensed professional is."
>
> — [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [11:27](https://www.youtube.com/watch?v=O72p-rBb2bA&t=687s)

Supporting talks: [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### Layered, deliberately redundant checks are worth their cost, because no single gate is sufficient and overlap reduces the probability a failure reaches production.

Support: **3** talk(s)

> "we want to try and optimize for reducing the chance of a failure getting into production. And so, there is some redundancy here or there. And that's okay."
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [18:06](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1086s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)

## Disagreements

### Should guardrails be tuned to fire aggressively (accepting false positives) or tuned for precision, treating an inappropriate trigger as a real harm?

| Position A | Position B |
|---|---|
| Tune the output guard aggressively; a false positive costs someone a double-check, a false negative ships a hallucinated number or privacy violation to a client. Similarly, when the judge is unconfident, reject rather than publish, and use recall as the guardrail metric so no bad artifact slips through.<br>*[Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)* | General-purpose guardrails are over-calibrated and had to be turned off; an inappropriate guardrail trigger is itself a harm that can drive a person away from care, so the objective is more correct triggers, not more triggers.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* |

*Why it matters: The tuning choice determines whether you optimize for recall or precision on the blocking classifier, and in care-adjacent domains an over-fired guardrail can cause the exact harm the guardrail exists to prevent.*

### Can guardrails be checks applied to model output, or must safety be established before the model's actions execute at all?

| Position A | Position B |
|---|---|
| Runtime checks on generated output — judge calls, post-generation vetoes, verification-and-reiterate layers, QA gates — are the practical mechanism, accepting that some failure rate persists and is monitored.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* | Output-side checking is fundamentally too late once tools are involved: the agentic loop must be air-gapped so the model returns a plan/expression that is statically analyzed and proven safe before any execution; constrain on the input side rather than detecting violations on the output side.<br>*["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)* |

*Why it matters: If output-side checking is adequate, guardrails are a monitoring-and-judging investment; if not, the whole harness must be rebuilt around plan reification and pre-execution proof, at real cost and latency.*

### Should guardrail enforcement be hard-blocking, or should it steer and let the agent continue?

| Position A | Position B |
|---|---|
| Hard constraints belong in hooks that block unconditionally, and when constraint and task collide the default should be halt and explain rather than find a way; identity fields should crash rather than silently default.<br>*[Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)* | Blocking is wrong for soft rules because it forces the user to retry; soft rules should use runtime steering that lets the agent adjust and keep going, and guardrail responses should be tiered by risk rather than applying a single blocking policy.<br>*[Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* |

*Why it matters: Choosing block-vs-steer per rule determines both the user experience of a triggered guardrail and whether rule changes require a code redeploy or take effect on the next call.*

## Practical Guidance

**Do:**

- Route self-harm, suicidal ideation, and acute medical emergencies through deterministic code that runs on every turn before the model sees the message.
- Implement guardrails as separate LLM-as-judge calls rather than safety rules embedded in the main system prompt, so the core agent can be iterated without weakening safety.
- Make the post-generation veto a shared service every surface passes through by default, so no surface can accidentally opt out.
- Measure guardrail behavior itself — claim rejection rate, missing citation rate, human-override rate on AI verdicts — and set thresholds that trigger investigation.
- Score live production traffic continuously with judges, not just a saved golden dataset before launch.
- Verify the judge before changing the agent when a score drops; editing a judge prompt is legitimate engineering, not gaming the eval.
- Sample and human-review high-stakes cases 100% of the time, with random sampling across other capabilities.
- Set severity by the worst plausible outcome rather than frequency: a bug that lightly annoys 100% of users is less severe than one causing serious harm in 0.1% of cases.
- Under uncertainty, hold and fix safety bugs but ship polish bugs.
- Use hooks for hard constraints and runtime steering for soft rules; steering rules registered on a server take effect on the next call with no redeploy.
- Validate agent output against a formal ontology (OWL constraints for duplicate refunds, wrong payee type, invalid status) and keep agents side-effect-free until validation passes — Pydantic at the door, ontology at the ledger.
- Strip PHI at the pipeline boundary at ingestion rather than redacting at runtime in logs and dashboards.
- Prefer deterministic regex-based checks over a probabilistic classifier for the final veto layer, accepting reduced coverage for reliability.
- Keep secrets outside the agent's sandbox behind a broker, and bound automation output (e.g. a single PR, or none at all) so agents cannot denial-of-service their owner.
- Encode a caught mistake into documentation, linters, and reviewers rather than relying on catching it again in review.

**Avoid:**

- Treating a system prompt or model-level alignment as a security boundary — if the labs don't trust the prompt as one, neither should you.
- Letting the same agent both act and validate its own output in one loop, or letting the builder grade itself, which hides the review rather than removing it.
- Prompting the guardrails at the agent, which lets a third party prompt-inject straight past them.
- Pursuing perfect benchmark scores, which drifts focus away from the humans the benchmarks exist to protect.
- Assuming a guardrailed QA gate can't be reward hacked — agents oversteer into conservative, generic outputs that differ in raw pixels but carry no real improvement.
- Shipping a yes/no approval prompt on an opaque command as your human-oversight story.
- Silently defaulting a missing identity field in a multi-tenant system — it caused a white-label leak where every venue shipped as sage@hawthornemanner.com.
- Quietly downgrading a bug's severity because no one has capacity, or treating fast follows as optional backlog rather than committed debt.
- Optimizing a sensitive-domain product for engagement, which is a clinical failure mode and not a polish issue.
- Assuming prompt iteration will eventually drive the failure rate to zero — each fix buys less and some failure classes cannot be prompted away.

## Notable Outliers

- Baking alignment into model weights is not foolproof and is the wrong place for safety; safety is not a mathematical property, which is precisely why ~100 LLM-as-a-judge startups exist — and even a certified-safe answer is worthless if the loop already emptied your bank account while producing it. (["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [12:33](https://www.youtube.com/watch?v=-CnA2lGfymY&t=753s))
- The hardest guardrail failures are ones where the agent never exceeds its authorization — the system looks compliant the entire time — and the energy to overcome a constraint can come from inside the agent routed through a human persuaded to remove the control. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [10:16](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=616s))
- Day one required turning off the frontier providers' built-in guardrails because general-purpose LLMs are over-calibrated for mental health — and that over-calibration is itself a compassionate choice by both the providers and the team. ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s))
- A warmer, more fluent voice makes a factual error worse rather than better, because the user now believes the false claim more strongly — so tone quality raises rather than lowers the required guard strength. ([Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [15:10](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=910s))
- The scaling bottleneck for safe AI is human capacity to read and act on signal, not compute or model capability. ([Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [11:27](https://www.youtube.com/watch?v=YXEqC05WEI0&t=687s))
- Building guardrails first is genuinely slower than bolting them on later, and that cost is an accepted design tradeoff that only high-stakes products should pay — a generic low-stakes chatbot does not need this apparatus. ([Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [20:14](https://www.youtube.com/watch?v=YXEqC05WEI0&t=1214s))

## All Talks

- [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)
- ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [Security Track Intro](../talks/security-track-intro.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Akele Reed](../speakers/akele-reed.md)
- [Alex Volkov](../speakers/alex-volkov.md)
- [Apoorva Joshi](../speakers/apoorva-joshi.md)
- [Clay Cockrell](../speakers/clay-cockrell.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Ekaterina Deyneka](../speakers/ekaterina-deyneka.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Erik Meijer](../speakers/erik-meijer.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Idan Gazit](../speakers/idan-gazit.md)
- [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Rashi Agrawal](../speakers/rashi-agrawal.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Tony Fabrikant](../speakers/tony-fabrikant.md)

