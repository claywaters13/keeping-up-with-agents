---
title: "output guardrails"
type: "concept"
slug: "output-guardrails"
tier: "supporting"
maturity: "contested"
talk_count: 13
speaker_count: 17
---

# output guardrails

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **13** talk(s) by **17** speaker(s)

**Definition:** Runtime checks on model input and output that block, filter, or rewrite unacceptable content before it reaches users or systems.

*Also referred to as: output validation, agent guardrails, llm guardrails, input and output guardrails, deterministic guardrails, guardrail metrics, neuro-symbolic guardrails*

## State of Practice

The field has largely stopped treating guardrails as prompt text and started treating them as systems engineering: a check that lives in the model's own instruction stream is considered defeated by construction, because a third party can prompt-inject past it and the model itself is optimizing for task completion. The dominant pattern is a separate evaluator sitting outside the generating loop — a distinct LLM-as-judge call, a validator/critic agent, a pre-tool-call hook, an ontology reasoner, or a regex veto — because a builder that grades itself hides review rather than removing it. Practitioners now instrument the guardrail itself, tracking claim rejection rate, missing-citation rate, human-override rate, and pass@K, on the grounds that an unmeasured guard gives you nothing to investigate when it misfires. Layering is assumed: Uber runs deliberately redundant, overlapping QA gates on a Swiss-cheese model, and SonderMind is explicit that an eval gate alone does not make a system safe. What remains unsettled is the substrate — whether the guard should itself be a probabilistic model (adversary agents, judges) or a deterministic artifact (types, OWL constraints, taint analysis, regex) — and the tuning direction, since over-blocking is now recognized as a real harm and not a free safety margin. Everyone accepts that guardrails cost latency and money and reduce rather than eliminate risk.

## Consensus

### Guardrails expressed as instructions inside the model's prompt are not guardrails; enforcement must sit in code, config, or a separate call that the model cannot override.

Support: **7** talk(s)

> "if you're prompting the guardrails at the agent, you're effectively letting the fox loose in the henhouse."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [7:04](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=424s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)

### The checker must be structurally separate from the generator — an agent that acts and validates in the same loop provides no real check and will rationalize its own failures into confident success.

Support: **8** talk(s)

> "The agent acts and validate its own output in the same loop. There's no separation, no second opinion."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [28:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1730s)

Supporting talks: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

### A single gate is insufficient; guardrails should be layered with deliberate redundancy, accepting overlapping checks as the price of lowering the probability that a failure reaches production.

Support: **5** talk(s)

> "we want to try and optimize for reducing the chance of a failure getting into production. And so, there is some redundancy here or there. And that's okay."
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [18:06](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=1086s)

Supporting talks: [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)

### Guardrail firing must itself be measured as a production metric — rejection rate, trigger accuracy, human-override rate — or you have no way to detect a miscalibrated guard.

Support: **3** talk(s)

> "Now if it's rejecting too many times, then that's a call for investigation, but if you didn't measure this in the first place, then you won't have anything to investigate"
>
> — [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [22:31](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1351s)

Supporting talks: [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### Guardrails cost real latency and money and do not eliminate risk; the tradeoff is accepted deliberately based on the sensitivity of the use case rather than assumed away.

Support: **3** talk(s)

> "this will probably raise cost. It might introduce latency. uh it's not going to eliminate risk. Nothing can."
>
> — [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [15:36](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=936s)

Supporting talks: [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

## Disagreements

### Should the guardrail itself be a probabilistic model (LLM judge or adversary agent), or a deterministic artifact (types, ontologies, regex, hooks)?

| Position A | Position B |
|---|---|
| The guard must be another model, because deterministic string-matching and rule engines are structurally unequipped for non-deterministic workloads and cannot judge whether the spirit of a constraint was violated; run a separate judge, critic, or reward-incentivized adversary agent.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)* | Probabilistic guards eventually lose; the guard must be deterministic — regex vetoes, Python pre-tool-call hooks, OWL/ontology constraints, or type and taint analysis over a reified plan — trading coverage for a guarantee.<br>*[Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)* |

*Why it matters: It determines whether guardrail coverage is bounded by what you can formally specify or by what a second model happens to catch, and whether your safety story is auditable to a regulator. Meijer argues the entire LLM-judge industry exists precisely because safety is not formally specifiable, which Martin-Dye and Coyle answer by narrowing the scope of what gets guarded rather than accepting a probabilistic check.*

### Should output guards be tuned aggressively toward blocking, or is over-triggering itself a first-class harm to be minimized?

| Position A | Position B |
|---|---|
| Tune aggressively: false positives are far cheaper than false negatives, recall is the right guardrail metric, and when the judge is not confident the correct behavior is to reject rather than publish.<br>*[Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)* | Inappropriate blocking is a real harm that can deny users the thing they came for; general-purpose models are over-calibrated and their built-in filters had to be turned off entirely, and a high rejection rate is a bug to investigate, not a safety win. Optimize for correct triggers, not more triggers.<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)* |

*Why it matters: The tuning direction sets whether you ship a system that fails closed and frustrates legitimate users, or one that lets edge cases through; in regulated or clinical domains both failure modes are attributable harms, so the choice determines who owns the calibration decision.*

### Does the decisive check belong on the generated output, or before the agent is allowed to act at all?

| Position A | Position B |
|---|---|
| Post-generation: the last layer is a veto on the finished artifact — an output guard, a QA gate on the rendered composition, an output-guardrail scenario suite — that every surface passes through before anything ships.<br>*[Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)* | Pre-action: constraining the agent on the input side with policies beats detecting violations on the output side, agents should be side-effect-free and validated before writing, and a certified-safe answer is worthless if the loop already emptied your bank account producing it.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)* |

*Why it matters: For content generation the output is the only side effect, so a post-hoc veto suffices; for tool-calling agents the damage is done before the output exists, which means teams porting content-style guardrails onto agentic systems are guarding the wrong boundary.*

### When a guard fires, should the system halt or repair and retry?

| Position A | Position B |
|---|---|
| Halt: the default when constraint and task collide is halt-and-explain rather than find-a-way; hooks block unconditionally and the user retries; agents should not act absent a proof of safety.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)* | Repair: a failed check should feed a bounded correction loop — re-iterate on the composition, keep enhancing for K iterations against the QA gate, or use runtime steering that lets the agent adjust and keep going for soft rules.<br>*[Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)* |

*Why it matters: Repair loops raise coverage but create a reward-hacking surface — Uber saw agents oversteer into generic conservative outputs that pass the gate without improving anything — while halting preserves the guard's integrity at the cost of user-visible failures.*

## Practical Guidance

**Do:**

- Use code hooks for hard constraints that must block unconditionally, and runtime steering registered on a server for soft rules the agent should adjust to and continue past; steering rules change without redeploying the agent
- Implement guardrails as separate LLM-as-judge calls rather than embedding safety rules in the main system prompt, so the core agent can be iterated on without recalibrating safety
- Track guardrail behavior as named production metrics: claim rejection rate, missing citation rate, human-override rate on AI verdicts, and pass@K for self-correcting loops
- Choose the guardrail metric from the asymmetry of the errors — Uber uses recall for routing because letting a bad image through is worse than an unnecessary enhancement
- Reject rather than publish when the judge is not confident about a check it cannot verify (e.g. item count in a multimodal image)
- Route the output veto through a shared service that every surface passes through by default, rather than wiring it per surface where a new surface can silently opt out
- Make missing identity fields throw in multi-tenant systems — a silent default shipped every venue as sage@hawthornemanner.com
- Have a licensed domain expert define correct behavior in edge cases and commit that judgment into CI, so every prompt, model, and guardrail change is scored against it
- Keep agents side-effect-free: Pydantic type checks at the door, ontology validation at the ledger, database writes only after validation passes
- Hold secrets outside the agent's sandbox behind a broker — treat any secret an agent can see as already compromised
- Bound automation output (a single PR, and permission to produce nothing at all) so guarded automations cannot denial-of-service their owner
- Retune guards against online drift with config-driven closed loops backed by guardrail observability and fast rollback, rather than freezing offline thresholds

**Avoid:**

- Relying on frontier providers' built-in safety filters for a specialized domain — SonderMind turned them off on day one as over-calibrated for mental health
- Regexes, verbose prompt instructions, and broad moderation APIs as the risk detector for clinically coded indirect language they cannot parse
- Letting the same agent write the code and write or grade its own tests — if the builder grades itself you did not remove review, you hid it
- Optimizing for more guardrail triggers rather than more correct ones; an inappropriate block can feel like a door slam and drive a user away from care
- Guard gates that can be reward-hacked: agents oversteer into conservative generic outputs that differ in raw pixels but carry no real improvement
- A yes/no approval prompt on an opaque command as your human-oversight story — it will not satisfy the EU AI Act's meaningful-oversight requirement
- Certifying an answer safe after the agentic loop has already run, when the side effects that mattered happened during generation
- Treating deterministic controls (egress filters, gVisor sandboxes, telemetry) as sufficient — they are necessary but do not stop an agent that never exceeds its authorization
- Assuming runtime AI security tooling built on data-leak-prevention and string matching transfers to non-deterministic workloads

## Notable Outliers

- Mathematically proven safe agentic compute is achievable today: have the model return a program representing the computation rather than executing it, then use ordinary data flow analysis, type checking, and taint analysis — including for the lethal trifecta — with elementary type systems. (["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [19:57](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1197s))
- An agent persuading a human to remove a control counts as the agent supplying the energy to defeat the constraint, routed through the human as a tool — so approval-based guardrails are inside the agentic loop, not outside it. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- Hallucination is a feature of LLMs rather than a defect, and the answer is a formal ontology reasoner as the guardrail rather than trying to suppress the behavior. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s))
- A warmer, more fluent voice makes a factual error worse rather than better, because it raises the user's belief in the false claim — so voice quality raises the required strictness of the output guard. ([Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [15:10](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=910s))
- Deliberately choosing deterministic regex checks over a probabilistic classifier for the output veto, accepting lower coverage for reliability, and naming it as a real trade-off rather than an obvious win. ([Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [20:38](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1238s))

## All Talks

- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)
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
- [Soumya Gupta](../speakers/soumya-gupta.md)

