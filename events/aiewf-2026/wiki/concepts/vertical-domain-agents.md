---
title: "vertical domain agents"
type: "concept"
slug: "vertical-domain-agents"
tier: "supporting"
maturity: "consolidating"
talk_count: 16
speaker_count: 19
---

# vertical domain agents

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **16** talk(s) by **19** speaker(s)

**Definition:** Agents built for a specific regulated or specialized industry, where domain workflow and expertise dominate the design.

*Also referred to as: domain-specific agents, vertical ai product design, vertical search engines, financial advisory agents, industrial iot agents, high-stakes document workflows, financial compliance automation, prior authorization automation*

## State of Practice

Across finance, healthcare, tax, compliance, GTM, infrastructure and even game tooling, speakers converged on the same architecture: a deterministic core that decides everything rules can decide, narrow agents invoked only for the residual ambiguous cases, evals whose definition of "correct" is owned by a licensed or credentialed domain expert, and a proprietary outcome dataset that the frontier labs do not have. The model itself is treated as a commodity input — multiple teams reported that post-trained smaller models, SLMs, or a mid-size model grounded in outcome data beat frontier models on cost and latency at equal or better quality, and Intuit reported frontier advice collapsing to 'acquire new customers' in 40% of ~100,000 business situations. The unsolved surface is autonomy: Risa Labs is pushing oncology prior-auth toward zero human touch using two-source evidence agreement, while Allos AI argues finance and pharma are still 'AI-in-the-loop' where the expert decides and AI only compresses their time. Evaluation methodology is likewise split — SonderMind and Ufonia run LLM judges as the safety backbone (F1 0.96 versus clinicians), while Allos AI says LLM-as-judge simply fails in finance and pharma because there are no answer keys and the model emits plausible jargon. Almost nobody claimed a model-capability bottleneck: the reported blockers are plumbing, provenance, integration, and the absence of expert judgment in the loop. Phaidra's framing captured the trajectory — AI-native vertical systems start as pure prompt-and-context and mature *toward* deterministic code for the cases that earn it.

## Consensus

### The moat in a vertical is proprietary outcome data plus domain expertise, not model access, infrastructure, or agent scaffolding — all of which are commodities.

Support: **5** talk(s)

> "the moat here is that it's not about the model access, it's about the data itself that you have."
>
> — [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s)

Supporting talks: [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)

### Deterministic rules and code should handle every case they can decide, with LLM agents invoked only for the residual ambiguous set — not as a replacement for the existing rule engine.

Support: **4** talk(s)

> "the no touch is growing on the share of every order. So, we started with deterministic checks. Agents only for the rules that where what rules can't decide."
>
> — [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [16:01](https://www.youtube.com/watch?v=_cVfz88_j7A&t=961s)

Supporting talks: [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)

### Frontier-level intelligence is unnecessary for most vertical workflows; post-trained smaller models, SLMs, or narrowly scoped cheaper models hit the quality bar at far lower cost and latency.

Support: **4** talk(s)

> "Health care is actually many specific workflows. You don't need, you know, Fable 5 to actually solve all of your clinical notes. We we don't need frontier level intelligence for every problem."
>
> — [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [18:11](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1091s)

Supporting talks: [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

### Vertical systems should be decomposed into many narrowly scoped agents rather than one agent asked to cover the whole workflow.

Support: **4** talk(s)

> "Last I checked, there was no tax on building more AI agents. So, why do you want your single agent to do everything?"
>
> — [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [4:21](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=261s)

Supporting talks: [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)

### A credentialed domain expert — not the engineering team, not the model — must define what a correct output is, and their judgment must be encoded into the eval suite before iteration begins.

Support: **4** talk(s)

> "our system isn't deciding what correct is in a clinical edge case like this one. A licensed professional is."
>
> — [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [11:27](https://www.youtube.com/watch?v=O72p-rBb2bA&t=687s)

Supporting talks: [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)

### Low-confidence, contradictory, or irreversible cases must route to a named human rather than being resolved silently by the system, and accountability stays with that human.

Support: **5** talk(s)

> "You can't outsource accountability to your own software. At the bottom of every real decision, a human signs."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [19:21](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1161s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)

### Verified outcomes from completed work — closed-won/closed-lost deals, finished audits, clinician annotations, real business results — must be fed back on a schedule or the system decays against domain drift.

Support: **4** talk(s)

> "You retrain your agents every quarter with your closed one or closed lost opportunities. And this is critical. Without this, your agents are looking at wrong information, pointing you to the wrong accounts and the wrong people."
>
> — [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [21:34](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1294s)

Supporting talks: [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

## Disagreements

### Should a vertical agent's target end state be full no-touch automation, or permanent expert decision-making with AI only compressing the expert's time?

| Position A | Position B |
|---|---|
| No-touch is the goal and is reachable incrementally: build a confidence mechanism (e.g. two independent sources agreeing on a fact), grow the automated share of orders over time, and design the product so the user supervises a conveyor belt rather than operating it — weekly active users should actually decline.<br>*[Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)* | In high-stakes verticals the correct model today is AI-in-the-loop, not human-in-the-loop: the expert makes every decision, a named human signs at the bottom of every output, and autonomy is only widened stage by stage in proportion to accumulated safety evidence.<br>*[Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)* |

*Why it matters: It determines whether the product is priced and sold as labor replacement or as a time multiplier, and whether engineering invests in confidence/arbitration machinery or in provenance and review UX.*

### Can an LLM be trusted to grade a vertical system's output?

| Position A | Position B |
|---|---|
| Yes, if the judge is calibrated by embedded domain experts and validated against them: separate LLM-as-judge guardrail calls are more robust than prompt-embedded safety rules, and a judge validated on 240 examples matched or slightly beat expert clinicians at hazard detection (F1 0.96).<br>*[Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)* | No — in finance and pharma there are no answer keys, so the model produces plausible jargon without understanding concepts like alpha; rubrics-as-rewards creates an echo chamber where the AI grades itself into agreement, and a verifier good enough to grade contextual clinical decisions would already be the best generator. Asking a model to check its own output is not a hallucination control at all.<br>*[Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)* |

*Why it matters: If LLM judges are valid, eval throughput scales with compute and CI can gate every prompt change; if not, iteration speed is capped by expensive expert review time and by rubric-authoring rather than by engineering.*

### Where should accumulated domain expertise live — in model weights, or outside the model in code, context, and structure?

| Position A | Position B |
|---|---|
| In the weights: post-train smaller models per sub-workflow, train an RL selector on verified business outcomes, and treat continual learning (both parametric and non-parametric) as the algorithm that converts intelligence into expertise — a specialized team with unique data can outpace the frontier's rate of improvement on a narrow problem.<br>*[From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)* | Outside the model: the required fixes are plumbing and honesty problems that a smarter model does not solve, structured data should be traversed by deterministic set operations rather than scanned token-by-token, and error analysis over observability logs is the highest-ROI improvement and should precede any weight-touching technique — fine-tuning also incurs recurring cost every time a new base model ships.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* |

*Why it matters: It decides whether a vertical team needs a training stack and data-labeling pipeline at all, or whether the same headcount is better spent on retrieval, semantic layers, and deterministic tooling.*

### Is the hard part of a vertical agent the domain, or the engineering method that is the same in every domain?

| Position A | Position B |
|---|---|
| The method is portable — moving from a hedge fund to pharma changed the domain but not the engineering, and lessons from building tax agents transfer directly to other verticals; what changes is which expert you hire and which proprietary data you hold.<br>*[Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* | The vertical rewrites the architecture: healthcare is on hard mode for quality, latency and cost simultaneously; patient-facing products cannot A/B test or roll back at all and must be developed against simulation; and mental health required disabling the frontier providers' built-in guardrails on day one because general-purpose models are over-calibrated for the use case.<br>*[From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)* |

*Why it matters: It sets whether a team can reuse a generic agent platform and swap the knowledge base, or must rebuild the release process, safety case, and guardrail stack per vertical.*

### Do citations and source links build user trust, or do they offload the vendor's verification work onto the customer?

| Position A | Position B |
|---|---|
| Citations shift the verification burden back to the user and add net work, which is especially damaging in healthcare, legal, and tax; trust should come from traces of how the agent produced each value, and from background execution the user does not have to babysit.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* | One-click provenance to the exact source paragraph, in about 30 seconds, is the product itself — correctness is irrelevant without it — and the review artifact should surface both supportive and contradictory evidence rather than a resolved answer.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* |

*Why it matters: It changes the core UI investment: an audit-trail surface built for a skeptical reviewer, versus a delegation surface built to keep the user out of the loop entirely.*

## Practical Guidance

**Do:**

- Start with deterministic checks and let the automated ('no-touch') share of cases grow over time, reserving agents strictly for what rules cannot decide.
- Require two independent sources to agree on a fact before proceeding without human verification; escalate anything below the confidence threshold.
- Hire the domain expert (trader, clinician, tax preparer) before you start iterating — engineers cannot tell whether vertical output is good.
- For open-ended outputs, replace the single golden response with expert-authored rubrics of required elements, adjudicated by a second expert and QA'd by a third.
- Implement guardrails as separate LLM-as-judge calls rather than instructions in the main system prompt; the latency and cost hit is worth the jailbreak resistance.
- Optimize for correct guardrail triggers, not more triggers — an inappropriate block is itself a harm that keeps people from care.
- Grow context with hierarchy depth rather than instance count, so a 64-GPU and a 460,000-GPU system cost roughly the same per query.
- Use LLMs to plan searches and deterministic set operations to execute them; anything that must be 100% reproducible (counting, dedup, exact set logic) belongs in code.
- Escalate contradictions between sources to a human instead of letting the model silently reconcile them; keep facts and estimates in visually separate, copy-paste-durable labels.
- Manufacture rare-but-dangerous scenarios in simulation with diverse synthetic personas before any real user exposure, and deliberately over-call hazards rather than under-call them.
- Ship the evidence, not the model: pinned prompts, datasets, call transcripts and judge verdicts mapped to named hazards are the regulatory deliverable.
- Pause the agent whenever it is about to make an assumption, and require plan approval before irreversible actions.
- Keep an explicit numeric break condition on every agent loop.
- Keep fit score and intent score separate, and make the policy engine auditable and adjustable by domain staff without a developer.
- Hold AI-drafted output to a sub-30-second edit budget — beyond that, users write their own and the initiative dies.
- Retrain or refresh on closed-won/closed-lost and completed-audit outcomes on a fixed cadence (quarterly was the cited interval).

**Avoid:**

- Asking the model to verify its own output, or treating rubrics-as-rewards as ground truth — it produces an echo chamber, not a check.
- Bolting AI onto an existing stack (GTM system, game engine) without also solving integration and the underlying architecture.
- Sharding near-identical entity names across parallel LLM calls, or relying on vector similarity over them — you get phantom entities and silent omissions.
- Loading many skills, MCP servers, and tools into one agent's context; measured performance degrades, and it is inheritance by another name.
- A/B tests, canary rollouts, and 'ship to 5% and watch the dashboard' on patient-facing systems — you cannot un-say a call or roll back harm.
- Citing a vendor's model-card benchmark score as a defense in a post-incident review.
- Flagging everything as hot: once reps are overwhelmed they stop acting and the system is dead.
- Chasing perfect benchmark scores, which drifts focus away from the humans the benchmark exists to protect.
- Relying on long-term memory inside a sub-500ms transaction SLA, or collapsing the final verdict to a single metric threshold — that reproduces the false-positive behavior of the rule engine you replaced.
- Building a separate skill-authoring interface and expecting users to fill it in; capture conventions from observed usage instead.
- Treating web/context acquisition as a one-time snapshot — social data decays in under a day, news/finance/retail in about 30.

## Notable Outliers

- The cost of intelligence reversed direction in 2026: tokens are up 76% raw and 29% IQ-adjusted at the halfway point of the year, which is why frontier models cannot be put in front of customers without very high lifetime value. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [22:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1357s))
- In Princeton's 500-day business simulation, most frontier models drove the company bankrupt and a simple rules-based system outperformed almost all of them. ([Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md), [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s))
- Baseline LLM correctness fell from 80% at 64 GPUs to about 30% at 460,000 GPUs, and a single validation pass at 1GW scale burned 116 million tokens versus 390,000 after redesign — roughly a 300x reduction with zero failures across 66 production cases. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s))
- Frontier providers' built-in guardrails had to be turned off on day one because general-purpose LLMs are over-calibrated for mental health, and an inappropriate guardrail 'feels like a door slam to the face'. ([Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [19:44](https://www.youtube.com/watch?v=O72p-rBb2bA&t=1184s))
- Owning the scraping pipeline broke even against renting context at just over 15,000 entities or queries, assuming ~a week and $5,000 of setup — a tipping point most teams assume is far higher. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [18:59](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1139s))
- Past a threshold of raw intelligence, further intelligence gains stop mattering and the continual-learning algorithm becomes the binding constraint — otherwise you get 'the world's smartest novice'. ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [14:22](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=862s))

## All Talks

- [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)
- [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)
- [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)
- [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)
- [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)
- [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)
- [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [Why Off-the-Shelf AI Doesn't Understand Money](../talks/why-off-the-shelf-ai-doesnt-understand-money.md)

## Speakers

- [Akele Reed](../speakers/akele-reed.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Arturo Nunez](../speakers/arturo-nunez.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
- [Chaitanya Asawa](../speakers/chaitanya-asawa.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Divakar Kumar](../speakers/divakar-kumar.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Jared Joselowitz](../speakers/jared-joselowitz.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Sajjan Kanukolanu](../speakers/sajjan-kanukolanu.md)
- [Shawn Chan](../speakers/shawn-chan.md)
- [Udi Menkes](../speakers/udi-menkes.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)
- [Varsha Shah](../speakers/varsha-shah.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yu Su](../speakers/yu-su.md)

