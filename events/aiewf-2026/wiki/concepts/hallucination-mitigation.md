---
title: "hallucination mitigation"
type: "concept"
slug: "hallucination-mitigation"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 15
---

# hallucination mitigation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **15** speaker(s)

**Definition:** Reducing confident fabrication and sycophancy, and calibrating how much trust an output's confidence deserves.

*Also referred to as: hallucination prevention, hallucination and sycophancy, hallucinated citations, hallucination probes, trust calibration in llm output, llm uncertainty calibration, confidence scoring*

## State of Practice

The field has largely stopped treating hallucination as a model defect to be prompted away and started treating it as a systems problem to be contained outside the model. The dominant architecture is: deterministic checks first, agents only for what rules cannot decide, a verifier structurally separate from the generator, and provenance attached to every claim so a human can land on the source paragraph in one click. Two specific beliefs hardened at this conference — that a model's self-reported confidence is not evidence (RLHF optimizes apparent confidence, so overconfidence is by construction), and that disagreement across independent runs, models, or sources is the usable trust signal instead. Measurement is under the same suspicion: single-pass evals and static deterministic benchmarks are considered misleading, with one talk demonstrating a blind replay agent matching frontier models on OSWorld and confidence intervals from rollouts alone achieving ~17-20% coverage against a nominal 95%. What remains open is where the last gate lives — a second LLM critic versus regex, OWL reasoners, and SQL/graph queries — and whether corroboration between independent checks ever licenses removing the human signature entirely.

## Consensus

### A model cannot serve as its own verifier; the check must be structurally separate from the generator, because an agent that acts and validates in the same loop rationalizes its own errors into confident success.

Support: **4** talk(s)

> "Before filing, the lawyer got suspicious, so he asked the chatbot, "Are these cases real?" And the chatbot said, "Yes." That is like asking the guy who sold you the watch whether the watch is real."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [17:06](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1026s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)

### Rules written into prompts are probabilistic suggestions; constraints that must hold have to be enforced in code, hooks, schemas, or ontologies that execute outside the model.

Support: **5** talk(s)

> "Because prompts probably are suggestions, not constraints. The model process them as a text. Not as a logic it has to execute. It's probabilistic. Only code execute logic."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [35:51](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2151s)

Supporting talks: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)

### A model's own expressed confidence is not a calibrated trust signal; corroboration across independent sources, runs, or models is what should gate action.

Support: **4** talk(s)

> "At least from what we have tried so far the uncertainty score from LM is not very reliable. It's kind of a LM model doesn't know what it doesn't know."
>
> — [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [14:45](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=885s)

Supporting talks: [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)

### A single passing run is not evidence; LLM systems must be evaluated repeatedly against a sustained pass-rate bar, with uncertainty reported honestly.

Support: **4** talk(s)

> "That means a single evaluation run didn't tell you the whole story. You need to repeat your evaluation multiple times in order to get a holistic picture by the average over the different runs results."
>
> — [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [3:03](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=183s)

Supporting talks: [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)

### Contradictions between sources and cases with insufficient evidence must be surfaced to a human rather than silently reconciled by the model.

Support: **4** talk(s)

> "Your job as a builder isn't resolve the argument. It's to make sure that the argument happens in front of a human instead of quietly along inside box."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [13:43](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=823s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)

### Fluency and warmth amplify the damage of a wrong output rather than softening it, so epistemic status must be carried in the artifact — guesses labeled, sources cited — instead of left to prose.

Support: **4** talk(s)

> "A warm, confident voice offering something that isn't real is worse than a cold one because the couple now believes they have a date."
>
> — [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [15:10](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=910s)

Supporting talks: [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)

### Embedding-proximity retrieval is a fabrication source in its own right: it always returns something, cannot rank by source authority, and cannot count or aggregate — so structured queries over graphs or databases must handle those cases.

Support: **3** talk(s)

> "If your system can can't tell an accountant under oath from a rumor in a group chat, it it is not ready for real money."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [10:16](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=616s)

Supporting talks: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

## Disagreements

### Does agreement between independent checks license removing the human from the loop, or must a named human sign every consequential decision regardless?

| Position A | Position B |
|---|---|
| Corroboration is a sufficient autonomy gate: when two independent sources or two different models return the same answer, proceed with no human verification and reserve people for the disagreements and low-evidence cases.<br>*[Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)* | Accountability cannot be delegated to software no matter how many checks agree; a named human must sign at the bottom of every real decision, and in safety-critical domains even a single failure across tens of thousands of runs is disqualifying.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)* |

*Why it matters: This sets the ceiling on automation economics — whether the human-review budget shrinks toward zero as corroboration improves, or stays fixed as a permanent per-decision cost regardless of model quality.*

### When a constraint cannot be expressed as a deterministic rule, is a second LLM an acceptable verification layer?

| Position A | Position B |
|---|---|
| Yes — a separate critic or executor/validator/critic chain, a second model reviewing the same input, or a frontier model kept watching in the system catches fabricated confirmations that rules cannot express.<br>*[Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)* | No — the final gate must be deterministic (regex vetoes, OWL reasoners, arithmetic reconciliation, rule engines run before agents), explicitly trading coverage for reliability, because any probabilistic checker eventually loses.<br>*[Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)* |

*Why it matters: It decides whether verification cost scales with inference spend and inherits the generator's failure modes, or is capped and auditable but blind to everything the rule language cannot state.*

### Is miscalibration a property of the post-training objective that only a new training paradigm can fix, or a plumbing problem that surrounding system design solves?

| Position A | Position B |
|---|---|
| It is intrinsic to RLHF: optimizing human preference creates a mode-dropping asymmetry so models look right no matter how wrong they are, and the fix is a different post-training target optimized for calibrated decision-making.<br>*[What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* | Model capability is not the bottleneck; the required fixes are provenance, source ranking, reconciliation, escalation, and code-enforced rules, so a smarter model changes nothing about them.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)* |

*Why it matters: It determines whether teams should invest in scaffolding that outlives model upgrades, or expect the next generation of post-training to obsolete much of that scaffolding.*

## Practical Guidance

**Do:**

- Run deterministic rule checks first and invoke agents only for cases the rules cannot decide, growing the no-touch share of traffic incrementally.
- Gate irreversible actions on two independent sources — or two different models reviewing the same artifact — agreeing, and hand off to a human when they disagree.
- Select human-review cases by cross-run or cross-model disagreement rather than by the model's self-reported uncertainty score.
- Make every claim click through to its exact source paragraph in about 30 seconds; treat the click-through as the product.
- Keep facts and estimates in separate boxes with a label that survives being copy-pasted into someone else's slides three weeks later.
- Use graph or SQL queries for counting, aggregation, and relationship traversal instead of letting the model compute over top-k retrieved chunks.
- Enforce hard constraints in a pre-tool-call hook and keep agents side-effect-free until validation passes; use runtime steering, not blocking hooks, for soft rules.
- Run each eval case many times against a sustained pass-rate bar (e.g. 90%), and for safety-critical behavior treat one failure in tens of thousands of runs as unacceptable.
- Compute confidence intervals that account for the hierarchical structure of the benchmark, and vary data, appearance, and initial state across eval runs.
- Route every output surface through one shared deterministic veto service by default so no surface can accidentally opt out.
- Tune output guards toward false positives — a false positive costs a double-check, a false negative ships a hallucinated number.
- Make a missing identity or tenant field throw rather than silently default.
- Return contradictory facts alongside supportive ones so the downstream reviewer sees the conflict.
- Set the acceptable error rate per action class: a 1-in-1000 failure is fine where the user can retry, zero where money or safety moves.
- Feed resolved gray-zone cases into semantic and episodic memory as an alternative to fine-tuning; it also sharpens human labeler consistency.

**Avoid:**

- Asking the model whether its own output is real and treating the answer as a control.
- Writing safety-critical or identity rules as instructions inside a prompt where the voice or task layer can override them.
- Optimizing advice products for engagement and agreeableness — repeated one-sided validation makes users more certain, not more self-aware.
- Reading pass@k on a static deterministic benchmark as capability: a blind replay agent scores the same or better than the frontier model it was extracted from.
- Publishing or deciding on confidence intervals computed from rollouts alone, which cover ~17-20% of the time against a nominal 95%.
- Letting retrieval pick text by proximity to the query when source authority differs — an audited filing and a group-chat rumor rank the same.
- Depending on luck as a control, such as one reviewer happening to have both contradictory documents open at once.
- Rubber-stamp approvals and thousand-line PRs, which produce false confidence rather than review.
- Assuming a smarter model resolves provenance, reconciliation, and supervision gaps.
- Deploying an unsupervised model on consequential decisions — the algorithmic homebuying write-off was a supervision failure, not a modeling failure.

## Notable Outliers

- A blind replay agent that just replays recorded action sequences matches or beats the frontier model it was extracted from on OSWorld and Mobile World, which means pass@k on deterministic environments measures replayability, not capability. ([Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [0:59](https://www.youtube.com/watch?v=CTLa_p6iOiY&t=59s))
- Overconfidence is not a correctable defect but a design consequence: every RLHF model has a structural gap between human preference and results, so models look right no matter how wrong they are. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [6:44](https://www.youtube.com/watch?v=cJ0EOzey--o&t=404s))
- Hallucination is the feature, not the bug — the right response is to fence probabilistic generation with formal ontologies rather than to try to eliminate it. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s))
- Of 93 cybersecurity alerts run three times, about 25% flip-flopped verdicts; episodic memory made 15% consistent and 10% remained inconsistent, because the ambiguity is in the labels, not the model. ([Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [22:10](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1330s))
- Deterministic regex vetoes were chosen over a probabilistic classifier as the last gate — explicitly trading coverage for reliability, and named as a real trade-off rather than an obvious win. ([Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [20:38](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1238s))
- The default assistant traits of helpfulness, agreeableness, and speed are actively harmful in couples therapy: sycophancy is a clinical failure mode, not a polish issue. ([AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md), [7:04](https://www.youtube.com/watch?v=yoONZwV2smc&t=424s))
- Filtering the visible tool set by semantic search to the top three both cuts per-call tool context from ~3,000 tokens to under 300 and improves accuracy, because with all 29 tools visible the model picks the wrong generic tool. ([Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [16:00](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=960s))

## All Talks

- [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)
- [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md)
- [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)
- [The State of Model Routing](../talks/the-state-of-model-routing.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)
- [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

## Speakers

- [Alex Atallah](../speakers/alex-atallah.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Clay Cockrell](../speakers/clay-cockrell.md)
- [Dan Feng](../speakers/dan-feng.md)
- [Diane Lin](../speakers/diane-lin.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Pierluca D'Oro](../speakers/pierluca-d-oro.md)
- [Shawn Chan](../speakers/shawn-chan.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Tony Fabrikant](../speakers/tony-fabrikant.md)
- [Walden Yan](../speakers/walden-yan.md)

