---
title: "hallucination mitigation"
type: "concept"
slug: "hallucination-mitigation"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 12
---

# hallucination mitigation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **12** speaker(s)

**Definition:** Reducing confident fabrication and sycophancy, and calibrating how much trust an output's confidence deserves.

*Also referred to as: hallucination prevention, hallucination and sycophancy, hallucinated citations, hallucination probes, trust calibration in llm output, llm uncertainty calibration, confidence scoring*

## State of Practice

The center of gravity at this conference moved off the model entirely: hallucination is treated as a property of the system surrounding the model, and the mitigations presented were code, schemas, and escalation paths rather than better prompts. Three ideas recurred independently across tracks — a model's expressed confidence is not evidence (Datadog found LLM uncertainty scores unusable for triage and used cross-run disagreement instead; Programma Labs showed rollout-only confidence intervals hit 17-20% empirical coverage against a nominal 95%); enforcement must live where the model cannot rewrite it (AWS moved rules from prompts into pre-tool-call Python hooks, Isadora & Co made layer four a deterministic regex veto, UC Berkeley used OWL reasoners over agent output, all with the same argument that prompts are suggestions and only code executes); and fluency is an aggravating factor, because a warm, well-formed sentence increases belief in a false claim and silently converts estimates into apparent facts across document revisions. The practical pattern is deterministic-first: rules and graph/SQL queries decide what they can decide, the model handles the residue, corroboration across independent sources raises confidence, and anything under-evidenced or contradictory escalates to a named human. What remains open is the root cause. TypeSafe AI argues overconfidence is by construction in RLHF and needs a new post-training objective optimized for calibrated decision-making; Datadog argues inconsistency is a label-ambiguity and missing-information problem, not a model problem; the guardrail camp argues it is plumbing and a smarter model will not help. All three prescribe different places to spend the reliability budget.

## Consensus

### A model's own expressed confidence is not evidence about correctness; trust signals must come from outside the model — corroborating sources, disagreement across runs or models, or statistically honest uncertainty.

Support: **5** talk(s)

> "At least from what we have tried so far the uncertainty score from LM is not very reliable. It's kind of a LM model doesn't know what it doesn't know."
>
> — [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [14:45](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=885s)

Supporting talks: [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)

### Rules expressed in natural language inside a prompt are suggestions, not constraints; hard guarantees must be enforced in deterministic code outside the model's control — hooks, ontology reasoners, regex vetoes, or a separate validator process.

Support: **4** talk(s)

> "Because prompts probably are suggestions, not constraints. The model process them as a text. Not as a logic it has to execute. It's probabilistic. Only code execute logic."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [35:51](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2151s)

Supporting talks: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)

### Deterministic computation should run first and the model should only handle the residue rules cannot decide — graph or SQL queries for counting, aggregation and relationship traversal; rule engines for eligibility; the LLM for genuinely ambiguous reasoning.

Support: **4** talk(s)

> "the no touch is growing on the share of every order. So, we started with deterministic checks. Agents only for the rules that where what rules can't decide."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s)

Supporting talks: [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)

### Under-evidenced, contradictory, or boundary cases should be routed to a human rather than resolved silently by the system; the engineering problem is selecting which cases those are, not eliminating them.

Support: **4** talk(s)

> "for the cases we do not have this enough information, we move keep that for human escalation."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [13:13](https://www.youtube.com/watch?v=_cVfz88_j7A&t=793s)

Supporting talks: [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md)

### Fluency amplifies the damage of a wrong output, so systems must preserve epistemic status in the artifact — facts separated from estimates, contradictory evidence shown next to supporting evidence — instead of letting the model smooth everything into one confident sentence.

Support: **4** talk(s)

> "A warm, confident voice offering something that isn't real is worse than a cold one because the couple now believes they have a date."
>
> — [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [15:10](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=910s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

## Disagreements

### Is confident fabrication a training-objective defect that must be fixed in post-training, or a system-design problem to be contained around a model you take as given?

| Position A | Position B |
|---|---|
| It is architecture and plumbing: hallucination control is a code change — deterministic hooks, ontology validators, separate critic agents, provenance links — and a smarter model does not solve any of it.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)* | It is by construction in RLHF: the reward model rewards apparent confidence and drops modes, so every RLHF-trained model will overclaim no matter what you wrap around it; the real fix is a new post-training paradigm that optimizes calibrated decision-making rather than human preference.<br>*[What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: If containment is sufficient, reliability budget goes to validators, provenance UI, and escalation queues on top of frontier APIs. If the objective is the defect, all of that is a permanent tax and the leverage is in training or buying differently-post-trained models.*

### Can automated corroboration substitute for human sign-off on a consequential decision, or must a named human always sign?

| Position A | Position B |
|---|---|
| Yes, with enough independent evidence: two independent sources agreeing on the same fact is sufficient grounds to proceed with no human touch, and the no-touch share of decisions should grow over time.<br>*[Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* | No: accountability cannot be transferred to software, a named human must sign every real decision, and businesses should not put AI on decisions with stakes at all — the unsupervised-model failure mode is what produced the half-billion-dollar writeoff.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: This decides whether the target metric is throughput of fully automated cases or quality of the human escalation queue, and it determines whether your system architecture needs a signature and audit trail at the bottom of every output path.*

### What signal should gate escalation — the model's own confidence score, or something computed outside it?

| Position A | Position B |
|---|---|
| A self-reported confidence score attached to each answer works well enough to gate: escalate only the low-confidence answers to a clinician.<br>*[Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* | Self-reported confidence is unreliable and must be replaced by external signals: disagreement across repeated runs or across different models, model internals such as hallucination and linear probes or perplexity over prefill, or confidence intervals corrected for the hierarchical structure of the eval.<br>*[Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md)* |

*Why it matters: Cross-run disagreement and probe-based signals cost 3x inference or model-internals access, while a self-reported score is free — picking wrong either burns budget or ships an escalation queue that misses exactly the cases where the model is confidently wrong.*

## Practical Guidance

**Do:**

- Give every generated claim a one-click path to the exact source paragraph; if a reviewer cannot verify provenance in about 30 seconds, treat the claim as unshippable regardless of whether it is correct.
- Require two independent sources to agree on a fact before allowing a case to proceed without human verification, and reconcile evidence into a normalized store before extraction.
- Run evals at least three times and use verdict flips across runs — not the model's uncertainty score — as the selection signal for human review; in a 93-alert cybersecurity test, 25% flip-flopped across three runs.
- Move rules out of the prompt into a pre-tool-call hook in code: same model, same tools, same prompt, wrong-to-correct outcome change. Use hooks for hard constraints and runtime steering for soft rules, since hooks block unconditionally and force a retry.
- Separate the actor from the checker — an executor/validator/critic chain catches fabricated success responses that a single agent, acting and validating in the same loop, reports as success.
- Replace vector top-k retrieval with a graph or SQL query for any counting, aggregation, or relationship-traversal question, so the model receives a computed verified result instead of estimating over three chunks.
- Validate agent output against a formal ontology after Pydantic type checks, and keep agents side-effect-free so database writes happen only once validation passes — Pydantic at the door, ontology at the ledger.
- Tag estimates distinctly from facts with a marker that survives being copy-pasted into someone else's slides three weeks later, and escalate source contradictions to a human rather than resolving them silently.
- Compute confidence intervals that account for the hierarchical structure of the benchmark; rollout-only intervals achieve ~17-20% empirical coverage against a nominal 95%, and at one million tasks a 4% true performance gap misjudged this way costs hundreds of thousands of dollars a month.
- Tune output guards for false positives over false negatives and prefer deterministic regex checks to a probabilistic classifier — a false positive means someone double-checked a response, a false negative ships a hallucinated number.
- Make the output veto a shared service every surface passes through by default, and make a missing tenant identity field throw rather than silently default.
- Filter the tool registry by semantic search to the top three tools per query and clear it between turns; 29 tool schemas add ~3,000 tokens per call and visible generic tools cause wrong-tool selection.
- Disclose that the agent is AI in its first response, unprompted, rather than letting the user discover it on turn seven.

**Avoid:**

- Asking the model whether its own output is real — self-verification is not a hallucination control, and the lawyer who asked the chatbot 'are these cases real?' got 'yes'.
- Using an LLM's self-reported uncertainty score as the trigger for human review; the model does not know what it does not know.
- Trusting a single LLM extraction over source documents as sufficient to eliminate human review.
- Reporting pass@k on static deterministic environments for computer-use agents — a blind replay agent that replays recorded action sequences matches or beats the frontier model it was extracted from on OSWorld and Mobile World.
- Letting fluent generation merge estimates and facts into one smooth sentence; it converts guesses into apparent facts across successive document revisions.
- Retrieval that ranks by proximity to the query rather than source authority — a system that cannot distinguish an audited filing from an informal note is not ready for consequential use.
- Shipping a single eval run as evidence of behavior, or treating semantic tool filtering alone as bounding context in a multi-turn conversation without clearing the registry.
- Silent defaults for identity in multi-tenant systems — a default caused every white-label venue to ship as sage@hawthornemanner.com.
- Running current models past ~200K tokens of context, and ideally staying under 100K, regardless of advertised context windows.
- Routing purely on task type in agentic workloads; complexity changes mid-session and small models out of distribution can increase total cost through tool-call loops.

## Notable Outliers

- Hallucination is a feature of large language models rather than a defect to eliminate — it is imagination, and the job is guardrails, not removal. ([Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md), [4:04](https://www.youtube.com/watch?v=Sir59K8ZDPU&t=244s))
- Overconfidence is by design, not a bug: because RLHF optimizes human preference, no matter how wrong the models are they will look right, owing to a mode-dropping asymmetry in the reward model analogous to GANs. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [8:07](https://www.youtube.com/watch?v=cJ0EOzey--o&t=487s))
- A benchmark is only adequately de-gamed if a replay agent extracted from it scores near zero on it; by that standard no existing computer-use benchmark qualifies. ([Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [9:16](https://www.youtube.com/watch?v=CTLa_p6iOiY&t=556s))
- Model internals — hallucination probes, linear probes, perplexity over prefill vectors — can serve as a proxy for how lost a model is, and therefore as a live routing trigger. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [38:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2283s))
- One unchecked sentence in a promotional AI demo coincided with roughly an 8% stock drop, about $100 billion of value — there is no such thing as a low-stakes demo anymore. ([Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [8:02](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=482s))
- Agent inconsistency is usually not a model problem at all but label ambiguity and missing information, and semantic plus episodic memory fixes it more cheaply than fine-tuning — 15 of the 25 percentage points of flip-flopping resolved, with 10% still inconsistent. ([Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [22:10](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1330s))

## All Talks

- [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)
- [The State of Model Routing](../talks/the-state-of-model-routing.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)
- [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)

## Speakers

- [Alex Atallah](../speakers/alex-atallah.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Diane Lin](../speakers/diane-lin.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Pierluca D'Oro](../speakers/pierluca-d-oro.md)
- [Shawn Chan](../speakers/shawn-chan.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Walden Yan](../speakers/walden-yan.md)

