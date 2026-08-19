---
title: "vertical domain agents"
type: "concept"
slug: "vertical-domain-agents"
tier: "supporting"
maturity: "consolidating"
talk_count: 13
speaker_count: 16
---

# vertical domain agents

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **13** talk(s) by **16** speaker(s)

**Definition:** Agents built for a specific regulated or specialized industry, where domain workflow and expertise dominate the design.

*Also referred to as: domain-specific agents, vertical ai product design, vertical search engines, financial advisory agents, industrial iot agents, high-stakes document workflows, financial compliance automation, prior authorization automation*

## State of Practice

The field has converged on a hard premise: in a regulated or specialized vertical, the binding constraint is not model capability but domain grounding — proprietary outcome data, normalized cross-source evidence, and encoded workflow rules. Intuit's measurement is representative: across ~100,000 business situations, 54% of frontier-model financial advice collapsed to 'acquire new customers' or 'increase revenue,' and a mid-size grounded model beat frontier models head-to-head. Architecturally, the dominant pattern is deterministic-first: rules and set operations handle everything specifiable, agents handle only the residue (oncology prior-auth, gray-zone fraud, data-center equipment resolution), with confidence scores routing low-evidence cases to a named human or licensed expert. Retrieval is treated as a source-authority and cross-document correlation problem rather than a similarity problem — semantic search fails outright on near-identical entity names, and the highest-value signals (fraud, diligence contradictions) exist between documents, not inside them. Economics have become a first-class design input: narrow agents report 80%+ token efficiency, one team cut 116M tokens per validation pass to 390K, and speakers argue token prices rose in 2026 rather than fell. What remains genuinely unsettled is how much autonomy the vertical earns and whether the final decision should be a deterministic verdict or an arbitrating agent.

## Consensus

### Domain grounding — proprietary outcome data, workflow structure, and encoded expertise — not model scale, is what makes a vertical agent work; a smarter frontier model does not close the gap.

Support: **6** talk(s)

> "you don't close the gap with bigger models. You close the gap with experience, embedding experience into the model by looking at verified outcomes in your data."
>
> — [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [17:51](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=1071s)

Supporting talks: [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)

### A continuous outcome feedback loop is mandatory: static rules, one-time eval gates, and frozen ICP/risk definitions decay against an evolving domain, so completed work (audits, closed-won/lost, clinician annotations, production traces) must be recycled into the system on a schedule.

Support: **6** talk(s)

> "You retrain your agents every quarter with your closed one or closed lost opportunities. And this is critical. Without this, your agents are looking at wrong information, pointing you to the wrong accounts and the wrong people."
>
> — [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [21:34](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1294s)

Supporting talks: [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)

### The domain signal lives across sources, not within any single document or system, so a normalization/semantic layer that reconciles heterogeneous sources into one schema is a prerequisite before any agent reasoning.

Support: **5** talk(s)

> "First is many of today's most significant compliance and fraud risk exist between the documents, not within them."
>
> — [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [17:07](https://www.youtube.com/watch?v=Iwe_RY-fYgI&t=1027s)

Supporting talks: [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)

### Deterministic checks should run first and decide as much of the volume as possible, with LLM agents reserved only for the cases rules cannot resolve.

Support: **4** talk(s)

> "the no touch is growing on the share of every order. So, we started with deterministic checks. Agents only for the rules that where what rules can't decide."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s)

Supporting talks: [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)

### Confidence must be an explicit, computed property of each output, and insufficient-evidence or contradictory cases must escalate to a named human or licensed domain expert rather than being silently resolved by the system.

Support: **4** talk(s)

> "You can't outsource accountability to your own software. At the bottom of every real decision, a human signs."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [19:21](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1161s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)

### Narrow scope with a minimal context window beats a maximally capable agent: fewer tools and tighter, structure-aware context both improve accuracy and collapse cost.

Support: **4** talk(s)

> "You kind of get the idea. You can end up with all kinds of highly efficient, small little agents that are all working together, but maintaining small minimal context windows all the way through."
>
> — [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [29:31](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1771s)

Supporting talks: [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)

## Disagreements

### Can a vertical agent be designed to complete work end-to-end without per-output human review, or is human sign-off structurally irreducible?

| Position A | Position B |
|---|---|
| No-touch autonomy is the target and is achievable incrementally: multi-source agreement can substitute for human verification, work should run as background agents on a conveyor belt with users as supervisors, and success looks like weekly active users falling while sessions rise.<br>*[Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* | A named human must sign every real decision and the domain expert must own the definition of correct; unsupervised models in high-stakes verticals are a supervision failure waiting to happen, and the product must keep the user participating in the decision rather than delegating it away.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)* |

*Why it matters: It determines whether the unit of product value is throughput (orders processed with zero touches) or assurance (a defensible artifact a human can sign), which changes staffing, liability posture, and the metric the roadmap optimizes.*

### For the final decision in an ambiguous case, should the verdict be produced by deterministic code, or by an LLM/agent arbitrating over evidence?

| Position A | Position B |
|---|---|
| Anything that must be reproducible — set logic, counting, dedup, threshold decisions — should be deterministic 1.0 code; AI-native systems should start at 3.0 and migrate toward 1.0 as use cases earn it, because a plan-then-resolve pipeline keeps cost flat and accuracy at 100% across scale.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)* | Reducing the verdict to a metric or if-condition reproduces the false-positive behavior of the rule engines you are replacing; a third arbitration agent reading the other agents' responses, or a learned model that adapts instead of relying on manual rule updates, is the better final step.<br>*[Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* |

*Why it matters: The choice sets whether the system's decisions are auditable and cost-bounded by construction, or adaptive but non-reproducible — which in regulated verticals is the difference between an explainable denial and one nobody in the org can reconstruct.*

### Should the vertical agent own its domain data pipeline, or rent context from vertical data providers and swap them as they change?

| Position A | Position B |
|---|---|
| Own it. Rented context decays while owned context compounds, query frequency (not record volume) is the real cost driver, and per-query pricing pushes teams to refresh less often and cap results — degrading their own knowledge work; proprietary in-situ data is also the only durable moat.<br>*[The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)* | Run several vendor sources in parallel and dedupe, because no single tool has full coverage; the vendors churn constantly but the architecture around them does not, so the integration layer is the asset rather than the pipeline.<br>*[Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)* |

*Why it matters: The break-even was measured at just over 15,000 entities or queries against roughly a week and $5,000 of setup — well below what most teams assume — so getting this wrong locks a vertical product into a cost curve that scales with usage instead of amortizing.*

### Are source citations the right trust mechanism in a vertical product, or do they shift unpaid verification work onto the domain expert?

| Position A | Position B |
|---|---|
| Provenance is the product: any claim must be traceable to its exact source paragraph in about 30 seconds with one click, and a system that cannot distinguish an audited filing from an informal note is not ready for real money.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)* | Citations alone push the verification burden back onto the user and add net work, which is worst precisely in healthcare, legal, and tax; trust should come from execution traces of how the agent worked and from evidence reconciliation that removes the need to check each claim.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* |

*Why it matters: If citations are the deliverable, the UI is a verification surface and the time savings promised to customers shrink accordingly; if reconciliation is the deliverable, the burden of proof moves into the pipeline and the vendor absorbs the error risk.*

## Practical Guidance

**Do:**

- Route every case through deterministic checks first and grow the no-touch share incrementally; invoke an agent only where the rules cannot decide.
- Require two independent sources to agree on a fact before proceeding without human verification, and reconcile evidence into a confidence score per output.
- Build a normalization layer before scoring — without it the same transaction is interpreted differently per jurisdiction and cross-entity risk comparison is meaningless.
- Escalate contradictions between sources to a human instead of letting the model silently pick a winner; a contradiction is the highest-value diligence signal.
- Implement guardrails as separate LLM-as-judge calls rather than rules in the main system prompt — more robust, harder to jailbreak, and lets you iterate the core agent without touching safety.
- Have a licensed domain expert (not engineering) define correct behavior for edge cases, then score every prompt, model, and guardrail change against that definition in CI.
- Grow context with hierarchy depth rather than instance count, and hand exact set logic, counting, and dedup over near-identical names to deterministic code.
- Keep fit score and intent score separate, and make the policy engine auditable and adjustable by domain staff without developer involvement.
- Retrain on closed-won/closed-lost (or completed audits, or clinician annotations) on a fixed cadence — quarterly was the stated interval — and capture user-specific conventions from observed product usage rather than a skill-authoring UI.
- Keep the human's edit cost under ~30 seconds for a drafted artifact and under ~30 seconds/one click to reach a claim's source paragraph, or practitioners will bypass the system.
- Add a self-healing loop that detects and mitigates broken RPA/portal automations during production hours, and generate per-portal configs from a shared action repository instead of hand-building integrations.
- Compute the build-vs-rent break-even explicitly before committing to per-query context pricing; the tipping point measured here was just over 15,000 entities or queries.
- Give each agent a sandboxed filesystem and sandboxed code execution as built-in primitives, and put a numeric break condition on every agent loop.

**Avoid:**

- Validating documents or records one at a time — the fraud and compliance risks that matter are only visible across documents and systems.
- Vector/semantic retrieval over near-identical entity names, and sharding entity lists across parallel LLM calls: you get phantom equipment that does not exist plus silent omission of things that do.
- Retrieval that cannot rank by source authority — if the system can't tell an accountant under oath from a rumor in a group chat, it isn't ready for regulated use.
- Asking the model to verify its own output as a hallucination control.
- Assuming a bigger or newer frontier model will fix the domain gap; in the Princeton 500-day simulation a simple rules-based system outperformed almost all frontier models.
- Comparing outcomes without adjusting for selection bias — the firms that took the action were systematically different from those that didn't, and the naive delta was overstated by roughly 3x in the price-raise example.
- Relying on regexes, verbose prompt instructions, or broad moderation APIs to catch clinically coded indirect risk language.
- Flagging everything as hot: once reps are overwhelmed they stop acting, stop trusting the system, and the initiative is dead.
- Long-term memory in a path with a sub-500ms transaction SLA.
- Bolting AI onto the existing stack and expecting scale — the AI layer, integration layer, and underlying architecture have to be solved together.
- Tracking weekly active users as the success metric for an agentic vertical product; sessions should rise while WAU falls.
- Chasing perfect benchmark scores — it drifts focus away from the people the benchmark exists to protect.
- Feeding the entire scene/dataset into context when proximity- or focus-graded context would do.

## Notable Outliers

- The cost of intelligence reversed direction in 2026: tokens are up 76% raw and 29% IQ-adjusted at the halfway point of the year, so frontier models can't be placed in front of customers unless their lifetime value is very high. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [22:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1357s))
- Visitor identification platforms are ~70% accurate at company level but only 15–20% at individual level, and this is a structural limit rather than a tuning problem. ([Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [22:23](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1343s))
- General-purpose LLM guardrails had to be turned off on day one because they are overcalibrated for mental health; inappropriately triggering a guardrail is itself a harm, so the goal is more correct triggers, not more triggers. ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s))
- Restructuring around hierarchy depth cut a 1GW validation pass from 116 million tokens to 390,000 (~300x) while holding 100% correctness from 64 to 460,000 GPUs, where the baseline LLM approach fell from 80% to about 30%. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s))
- Past a threshold of raw intelligence, further intelligence gains are unnecessary and the continual-learning algorithm becomes the binding constraint — current frontier models may already be good enough. ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s))
- A generic end-to-end background agent gets only 80–90% of the way there; the remaining value is entirely in the user's own quirks and conventions, which must be captured implicitly rather than through a skill-creation interface. ([Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [9:05](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=545s))

## All Talks

- [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)
- [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)
- [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)
- [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)
- [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)
- [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

## Speakers

- [Akele Reed](../speakers/akele-reed.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Arturo Nunez](../speakers/arturo-nunez.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Divakar Kumar](../speakers/divakar-kumar.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Sajjan Kanukolanu](../speakers/sajjan-kanukolanu.md)
- [Shawn Chan](../speakers/shawn-chan.md)
- [Udi Menkes](../speakers/udi-menkes.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)
- [Varsha Shah](../speakers/varsha-shah.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yu Su](../speakers/yu-su.md)

