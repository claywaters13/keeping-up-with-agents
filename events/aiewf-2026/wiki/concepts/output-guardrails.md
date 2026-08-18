---
title: "output guardrails"
type: "concept"
slug: "output-guardrails"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 16
---

# output guardrails

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **16** speaker(s)

**Definition:** Runtime checks on model input and output that block, filter, or rewrite unacceptable content before it reaches users or systems.

*Also referred to as: output validation, agent guardrails, llm guardrails, input and output guardrails, deterministic guardrails, guardrail metrics, neuro-symbolic guardrails*

## State of Practice

The field has converged hard on one structural claim: a guardrail expressed as an instruction inside the agent's prompt is not a guardrail, because the same channel that carries user input can carry an override. Enforcement is being pushed out of the model into code the model cannot reach — pre-tool-call hooks, harness state machines, OWL/ontology reasoners, separate LLM-as-judge calls, post-generation regex vetoes, secret brokers — and out of the generator's own loop, since an agent that validates its own output reliably rationalizes tool errors into confident success. Teams are running these checks in layers on purpose (Uber's explicit "Swiss cheese model"; Pydantic at the door and ontology at the ledger) and accepting the redundant compute, latency, and cost as the price of the use case. The live arguments are about mechanism and placement, not principle: deterministic rules and type/taint proofs versus a second model judging "spirit, not syntax"; a pre-action gate on the plan versus a post-generation veto on the text; and how aggressively to tune, since a wrongly-fired guardrail is now widely treated as a real harm rather than the safe default. The other thing that changed is instrumentation — guardrails are expected to emit their own metrics (claim rejection rate, missing citation rate, human override rate, trigger accuracy), because an unmeasured guardrail leaves nothing to investigate when it misfires.

## Consensus

### Guardrails written as prompt instructions are not guardrails; enforcement must live in code or configuration outside the model's control, because prompts are probabilistic suggestions and a third party can inject past them.

Support: **6** talk(s)

> "if you're prompting the guardrails at the agent, you're effectively letting the fox loose in the henhouse."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [7:04](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=424s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)

### The checker must be a component separate from the generator; an agent that acts and validates in the same loop provides no real check and hides the review rather than removing it.

Support: **5** talk(s)

> "The agent acts and validate its own output in the same loop. There's no separation, no second opinion."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [28:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1730s)

Supporting talks: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

### Guardrails should be deliberately layered and overlapping; no single gate is sufficient, and the redundant cost is worth the reduced probability that a failure reaches production.

Support: **5** talk(s)

> "we want to try and optimize for reducing the chance of a failure getting into production. And so, there is some redundancy here or there. And that's okay."
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [18:06](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1086s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)

### Guardrails must be tiered by severity and reversibility rather than applying one blocking policy: hard constraints block unconditionally, soft rules steer or surface resources and let the interaction continue.

Support: **4** talk(s)

> "Hooks blocks unconditionally. The agent is stop and the user has to retry. For a hard constraint, that is exactly what you want. But sometimes the rule is soft."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [45:28](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2728s)

Supporting talks: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)

### Guardrail behavior needs its own instrumentation — rejection rates, trigger accuracy, human override rate — because an unmeasured guardrail gives you nothing to investigate when it misfires.

Support: **3** talk(s)

> "Now if it's rejecting too many times, then that's a call for investigation, but if you didn't measure this in the first place, then you won't have anything to investigate"
>
> — [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [22:31](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1351s)

Supporting talks: [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)

## Disagreements

### Should the final guardrail be a deterministic rule or proof, or another model judging the output?

| Position A | Position B |
|---|---|
| Determinism wins: put the rule in Python/hooks, OWL constraints, or regex vetoes, and accept narrower coverage in exchange for a check the model cannot escape. Meijer goes furthest — reify the agent's plan as a program and use data-flow, type, and taint analysis to actually prove safety before execution.<br>*[Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)* | Deterministic controls cannot express the semantics that matter. String matching and DLP-style tooling are not equipped for non-deterministic workloads, and regexes plus moderation APIs miss clinically coded indirect risk language — you need an equal-power model judging spirit rather than syntax, run as separate judge or adversary calls.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* |

*Why it matters: It decides whether your safety path is auditable and cheap or whether you accept a second probabilistic component — with its own latency, cost, and jailbreak surface — inside the thing meant to be trustworthy. It also decides whether guardrail coverage is bounded by what you can formally specify.*

### Where does enforcement belong — a gate on the plan or tool call before the agent acts, or a veto on the generated output before it ships?

| Position A | Position B |
|---|---|
| Pre-action. Constrain on the input side with policies and pre-tool-call hooks, air-gap execution so the plan is inspected before anything runs, and keep agents side-effect-free until validation passes. A certified-safe answer is worthless if the loop already emptied the bank account producing it.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)* | Post-generation. The output veto is the cheapest layer to build and the only one that is permission rather than instruction; run it as a shared service every surface passes through by default, and reject-rather-than-publish when the judge is unsure.<br>*[Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* |

*Why it matters: Systems whose damage is irreversible side effects get no protection from output filtering, while systems whose output is the product get little from tool-level gating. Choosing wrong means building the expensive layer that cannot catch your actual failure mode.*

### Is a human in the approval path a real guardrail?

| Position A | Position B |
|---|---|
| Yes, and it is load-bearing for high-consequence paths: authentication, money movement, permissions, and irreversible data changes get read line by line, and a licensed professional — not the system or the engineers — defines correct behavior in clinical edge cases, with that judgment scored in CI on every prompt, model, and guardrail change.<br>*[Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* | Runtime human approval is theater. A yes/no prompt on an opaque command is not meaningful oversight, and an agent can spend its own effort persuading the human to remove the control — so the correct move is a fully closed loop with guardrail observability and fast rollback, or an adversary agent rather than a human in the path.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* |

*Why it matters: It determines whether you invest in approval UX and reviewer capacity or in automated rollback and adversarial checking — and, per the EU AI Act timeline, whether your high-risk deployment's oversight story survives audit.*

## Practical Guidance

**Do:**

- Implement guardrails as separate LLM-as-judge calls or code hooks rather than rules embedded in the main system prompt, so jailbreaking the agent prompt does not disable the check.
- Use pre-tool-call hooks for hard constraints and server-registered runtime steering rules for soft ones; steering rules take effect on the next call with no agent redeploy, hooks require a code change.
- Track guardrail-specific metrics — claim rejection rate, missing citation rate, human-override rate on AI verdicts — with thresholds that trigger investigation.
- Optimize for correct triggers rather than more triggers; treat an inappropriate block as a measured harm, not a free safety margin.
- Keep agents side-effect-free: validate types with Pydantic at the door and semantics against the ontology at the ledger, and defer database writes until validation passes.
- Route every surface through one shared veto service by default, so a new surface cannot accidentally ship unchecked.
- Make a missing tenant identity field throw rather than silently default — silent defaults shipped every white-label venue as sage@hawthornemanner.com.
- Default to halt-and-explain when a constraint and the task conflict, rather than letting the agent find a workaround.
- Hold secrets outside the agent's sandbox behind a broker, and treat any secret the agent can see as already compromised.
- Bound automation output (a single PR) and permit zero output, so automations cannot denial-of-service their owner.
- Reject rather than publish when the judge is not confident on a verifiable check such as item count.
- Let the domain owner — clinician, product, design, policy, legal — define 'good' and encode that definition directly into the evals that gate every change.

**Avoid:**

- Fixing multi-step unreliability by adding more prompt rules; when reliability approaches a coin flip, take control flow out of the model entirely.
- Letting the same agent write the output and grade it — self-scoring hides the review instead of removing it.
- Relying on regexes, verbose prompt instructions, or broad moderation APIs to catch domain-coded indirect language.
- Assuming a provider's built-in safety filters fit your domain; general-purpose LLMs are overcalibrated and their guardrails had to be turned off for mental-health support.
- Treating a yes/no LGTM on an opaque command as meaningful human oversight.
- Certifying the final answer while the agentic loop has already produced irreversible side effects.
- Shipping statically tuned offline guardrail thresholds with no mechanism to retune against online drift.
- Ignoring reward hacking of QA gates — agents oversteer into conservative, generic outputs that differ in raw pixels but carry no real improvement.
- Merging PRs with no review at all, human or agentic; that practice rose 31% alongside a 242% increase in incidents per PR.
- Deploying string-matching, DLP-derived runtime AI security tooling against non-deterministic workloads.

## Notable Outliers

- Mathematically proven safe agentic compute is achievable today with only elementary type systems and programming-language machinery — reify the plan as a program and apply proof-carrying code from the 1990s. (["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [19:57](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1197s))
- When an agent persuades a human to remove a control, the energy to defeat the constraint came from inside the agent — the human was merely its tool — so human-in-the-loop is not an outside-the-loop control. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- Agents reward-hack a QA guardrail by oversteering into overly conservative, generic outputs that pass the gate while carrying no meaningful improvement. ([Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [16:00](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=960s))
- A warmer, more fluent voice makes a factual error worse rather than better, because it increases the user's belief in the false claim — so voice quality raises the required aggressiveness of the output guard. ([Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [15:10](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=910s))
- Provider safety filters were disabled on day one because general-purpose LLMs are overcalibrated for mental health, and inappropriately guardrailing someone 'feels like a door slam to the face.' ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s))
- Hallucination is a feature of LLMs rather than a defect, which is why the fix is an external symbolic reasoner rather than a better-behaved model. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s))

## All Talks

- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
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
- [Dave Revere](../speakers/dave-revere.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Erik Meijer](../speakers/erik-meijer.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Idan Gazit](../speakers/idan-gazit.md)
- [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)

