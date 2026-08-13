---
title: "vertical domain agents"
type: "concept"
slug: "vertical-domain-agents"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 15
---

# vertical domain agents

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **15** speaker(s)

**Definition:** Agents built for a specific regulated or specialized industry, where domain workflow and expertise dominate the design.

*Also referred to as: domain-specific agents, vertical ai product design, vertical search engines, financial advisory agents, industrial iot agents, high-stakes document workflows, financial compliance automation, prior authorization automation*

## State of Practice

Across finance, healthcare, tax, compliance, GTM, and industrial operations, speakers converged on the view that a vertical agent is mostly a data-and-control-plane problem wearing a model as a hat: the frontier model is assumed adequate, and the differentiator is the semantic layer, the outcome data, and the deterministic scaffolding around it. The dominant architecture is deterministic-first — rules, set operations, normalized payer/jurisdiction views, and materialized cross-context read models handle everything expressible as a rule, with LLM reasoning reserved for the residual gray zone, and confidence established by corroborating two or more independent sources rather than by one extraction. Off-the-shelf frontier models are treated as actively unsafe in regulated verticals for opposite reasons depending on domain: Intuit found them fluently wrong on business economics (40% of advice across ~100k situations reduced to 'acquire new customers'), while SonderMind had to disable built-in provider guardrails on day one because they were over-calibrated to the point of harming users. Once a task is narrowly scoped, several teams reported that a mid-size, SLM, or open-source model grounded in domain data beats a frontier model head-to-head, which matters because token costs reportedly rose in 2026 rather than fell. The unresolved questions are about autonomy and ownership: how much of a high-stakes workflow can run no-touch, whether to own or rent domain context, and whether the runtime should be a bounded 2–3 step pipeline or an open-ended agentic loop.

## Consensus

### Deterministic checks and rule engines should run first and remain in place; agents belong only on the residual cases rules cannot decide, not as a replacement for the existing system.

Support: **3** talk(s)

> "the no touch is growing on the share of every order. So, we started with deterministic checks. Agents only for the rules that where what rules can't decide."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s)

Supporting talks: [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)

### General-purpose frontier models are structurally inadequate for regulated verticals regardless of how much context you give them; the missing ingredient is grounding in the domain's observed outcomes and idiosyncratic structure, not model capability.

Support: **5** talk(s)

> "A frontier model has read about money, but a grounded model in real outcome has actually watched what happens."
>
> — [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s)

Supporting talks: [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)

### Accountability cannot be transferred to the system: low-confidence, ambiguous, or irreversible cases must route to a named human, and a domain expert rather than the engineering team defines what 'correct' means at the edges.

Support: **4** talk(s)

> "You can't outsource accountability to your own software. At the bottom of every real decision, a human signs."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [19:21](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1161s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)

### Vertical agents must be wired to a continuous feedback loop from real completed outcomes (closed deals, audit results, annotated production traces); static rules and one-time eval gates decay against a moving domain.

Support: **5** talk(s)

> "You retrain your agents every quarter with your closed one or closed lost opportunities. And this is critical. Without this, your agents are looking at wrong information, pointing you to the wrong accounts and the wrong people."
>
> — [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [21:34](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1294s)

Supporting talks: [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

### Confidence in a vertical workflow comes from cross-source reconciliation, not from a better single extraction: independent sources agreeing is what licenses automation, and sources disagreeing is a signal to escalate rather than to average away.

Support: **4** talk(s)

> "instead of just having one source, I have two sources that give me the same information and wherever they conquer, I can say with confidence that this drug is already been authorized."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [7:34](https://www.youtube.com/watch?v=_cVfz88_j7A&t=454s)

Supporting talks: [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)

### Once the task is narrowly scoped to a domain, a smaller or cheaper model grounded in domain data is sufficient and often better than a frontier model — model choice is not where the vertical advantage lives.

Support: **3** talk(s)

> "we were able with a midsize cheaper model to outperform the frontier models because of the grounding that I just showed you."
>
> — [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s)

Supporting talks: [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)

### The binding constraint on vertical agents is integration plumbing — a normalized, cross-context semantic layer over the domain's scattered systems — rather than reasoning quality; bolting an agent onto the existing stack fails.

Support: **5** talk(s)

> "it comes down to integration. Businesses want their data properly integrated into AI. They They believe, and are probably right, that if they appropriately leverage AI, they're going to have these dramatic gains in their business"
>
> — [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [4:19](https://www.youtube.com/watch?v=spNAUEgq_A8&t=259s)

Supporting talks: [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)

## Disagreements

### In a high-stakes regulated workflow, can an individual decision ever be completed without a human in the loop on that specific decision?

| Position A | Position B |
|---|---|
| Yes — no-touch is the explicit target and is reached incrementally. Once corroborating independent sources agree and a confidence threshold is met, the order submits itself; the human's role shifts to supervising a queue, and success looks like weekly active users going down while sessions go up.<br>*[Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* | No — a named, fireable human must sign at the bottom of every real decision, and a licensed professional (not the system, not engineering) owns the definition of correct behavior; the unsupervised-model failure mode is the one that writes off half a billion dollars.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* |

*Why it matters: It determines whether you invest engineering in confidence scoring and auto-submit paths or in reviewer-facing provenance and sign-off UI, and it sets where legal liability lands when the agent is wrong.*

### Should the agent runtime be a bounded few-step pipeline or an open-ended agentic loop with sub-agents?

| Position A | Position B |
|---|---|
| Bounded. A two-or-three-step plan-then-resolve pipeline keeps cost flat and constant (9,000 tokens per query at any scale), and where loops exist they need an explicit numeric break condition plus short-term-only memory to hold a sub-500ms SLA.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)* | Open-ended. Full agents should be usable as tools inside other agents, forming recursive sub-agent hierarchies that talk to each other in English, and background agents should run for hours on tasks the user has delegated entirely.<br>*[The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* |

*Why it matters: Bounded pipelines give predictable unit economics and latency SLAs but cap what the agent can attempt; recursive loops raise the capability ceiling while making per-task cost and worst-case latency unbounded.*

### Should a vertical team own its domain context pipeline or rent it from specialized vendors?

| Position A | Position B |
|---|---|
| Own it. Go straight to the known underlying sources, because vendors and data brokers pull from those same sources anyway; frequency — not record volume — is the cost killer, break-even arrives at just over 15,000 entities, and proprietary outcome data is the only durable moat.<br>*[The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)* | Rent it, redundantly. Run multiple identification and enrichment vendors in parallel and dedupe, because no single tool catches every visitor; the vendors churn constantly but your architecture doesn't, so keep the swappable layer thin.<br>*[Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)* |

*Why it matters: The choice sets your marginal cost per query — and therefore whether teams quietly degrade their own product by refreshing weekly instead of daily — and whether the accumulated context becomes a compounding asset or a rental expense.*

### Is exposing citations and evidence to the reviewer the trust mechanism, or is it a failure to finish the job?

| Position A | Position B |
|---|---|
| It is the product. A claim's correctness is irrelevant if provenance can't be checked in one click to the exact source paragraph, contradictions must be surfaced in front of a human rather than resolved silently, and answers should ship with both supportive and contradictory facts attached.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* | Citations shift verification work back onto the customer, which is precisely the cost the vertical product promised to remove — especially in healthcare, legal, and tax. Traces should exist for when trust breaks down, not as the standing interaction model.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* |

*Why it matters: It decides whether the core UI is a reviewable document with source links or a background job queue, and whether you can honestly claim the time savings your pricing is based on.*

## Practical Guidance

**Do:**

- Route every case through deterministic rules first and hand only the rule-undecidable gray zone to an agent; keep the existing rule/ML engine in place as tier one.
- Require two independent sources to agree before letting a case proceed without human verification; anything with insufficient evidence defaults to escalation.
- Implement guardrails as separate LLM-as-judge calls rather than instructions in the main system prompt — more robust, harder to jailbreak, and lets you iterate the core agent without touching safety.
- Have a licensed domain expert define correct behavior on edge cases and commit that judgment into CI, so every prompt, model, and guardrail change is scored against it.
- Make every generated claim click through in one step to the exact source paragraph; if verification takes more than ~30 seconds it doesn't count.
- Keep facts and estimates in separate, labeled boxes with tags that survive being copy-pasted into someone else's slides weeks later.
- Escalate contradictions between sources to a human instead of resolving them silently — treat a contradiction as the highest-value signal in the workflow.
- Grow agent context with hierarchy depth rather than instance count, so a 64-unit and a 460,000-unit system cost roughly the same per query.
- Use deterministic code for anything requiring exact reproducibility — set logic, counting, dedup across near-identical names.
- Build a normalized cross-context semantic layer or materialized view before pointing an agent at the domain's systems; never query the event store directly for reads.
- Normalize across jurisdictions before scoring risk, or identical transactions get scored inconsistently and global comparison breaks.
- Retrain agents quarterly on closed-won and closed-lost outcomes; feed wins, losses, and deferrals back into the knowledge base.
- Keep fit score and intent score separate, and keep the policy engine auditable and adjustable by domain staff without a developer.
- Adjust for selection bias when measuring the impact of a recommended action — the firms that took the action were already different.
- Use frontier models as hypothesis generators and a separately trained, cheaper model as the selector.
- Give each domain agent its own sandboxed filesystem and sandboxed code execution as built-in primitives.
- Set an explicit numeric break condition on any agent loop.
- Capture user-specific conventions automatically from observed product usage rather than shipping a skill-authoring interface.
- Present a plan for approval before any irreversible or dangerous action, and keep self-service controls so users can take the wheel back.

**Avoid:**

- Asking the model to verify its own output as a hallucination control.
- Vector/semantic retrieval over near-identical domain entity names — embeddings become indistinguishable and recall collapses.
- Sharding entity enumeration across parallel LLM calls: it produces phantom equipment that doesn't exist and silently drops things that do.
- Loading many skills, MCP servers, and tools into one agent's context — it measurably degrades performance and is inheritance by another name.
- Retrieval that can't distinguish an audited filing from an informal note and selects text by query proximity rather than source authority.
- Shipping frontier providers' built-in safety guardrails in a mental-health context — they are over-calibrated, and inappropriately triggering is itself a harm that isolates the user.
- Flagging everything as hot, or conflating fit with intent — reps stop acting and stop trusting the system.
- Long-term memory in any path bound by a sub-500ms transaction SLA.
- Using a plain metric or if-condition as the final verdict after agent analysis; it reproduces the rule engine's false positives.
- Validating documents one at a time when the actual fraud pattern only exists between documents.
- Hand-built custom integrations per portal or per payer — they don't scale; generate configs over a shared action repository and add a self-healing loop for runtime breakage.
- Measuring an agentic vertical product by weekly active users.
- Assuming more context substitutes for outcome grounding — a company's entire financial dataset is still one group of data points.
- Chasing perfect benchmark scores, which drifts focus away from the humans the benchmark exists to protect.
- Relying on a single visitor-identification vendor, or trusting individual-level identification at all.
- Generic chat openers like 'How can I help you?' for buyers who have already done their research — they move the user backwards and out.
- Putting a frontier model in front of customers whose lifetime value doesn't justify it.

## Notable Outliers

- The cost of intelligence stopped falling and reversed in 2026 — tokens are up 76% raw and 29% IQ-adjusted before the year is even half over — which inverts the standard assumption that you can wait for models to get cheaper. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [22:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1357s))
- In a Princeton 500-day business simulation, most frontier models drove the company bankrupt in under 500 days, and a simple rules-based system outperformed almost all of them. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s))
- Intelligence and expertise are largely orthogonal; past a threshold of raw intelligence — which current frontier models may already have crossed — the continual-learning algorithm, not the model, is the binding constraint. ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s))
- Visitor identification platforms are ~70% accurate at company level but only 15–20% accurate at individual level, and that is a structural limit rather than something tuning will fix. ([Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [22:23](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1343s))
- Karpathy's drift of software 1.0 into 3.0 runs backwards for AI-native systems: start pure 3.0 by throwing everything in the context window to discover what's worth building, then migrate toward deterministic 1.0 for the use cases that earn it. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s))
- Despite all the talk, domain-specific agents do not meaningfully exist in public today — and 2027, not 2026, will be the year of multi-agent orchestration. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [20:24](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1224s))
- Guardrailing someone inappropriately is a real harm that can block them from care — the objective is more correct triggers, not more triggers. ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [6:24](https://www.youtube.com/watch?v=O72p-rBb2bA&t=384s))

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
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

## Speakers

- [Akele Reed](../speakers/akele-reed.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
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

