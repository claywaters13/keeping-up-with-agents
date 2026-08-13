---
title: "AI System Design: From Idea to Production"
type: "talk"
slug: "ai-system-design-from-idea-to-production"
org: "MongoDB"
video_id: "T0HhO4YtTfE"
duration_sec: 1732
word_count: 4200
speakers: ["Apoorva Joshi"]
---

# AI System Design: From Idea to Production

**Speakers:** [Apoorva Joshi](../speakers/apoorva-joshi.md)

**Org:** MongoDB

**Duration:** 28m 52s

[Watch on YouTube](https://www.youtube.com/watch?v=T0HhO4YtTfE)

## Summary

Apoorva Joshi (MongoDB) presents a four-phase framework for taking an AI system from idea to production — product requirements, system design, evaluation and monitoring, then optimization for cost, latency, and reliability — and walks it end-to-end through a single worked example: a health insurance claims review system for medical reviewers. Her core argument is that in an era of AI-generated code, the spec is the hard part: a quantified business problem, explicit regulatory and procurement constraints, and a SMART success metric are what let coding agents build the right thing. She is pointedly skeptical of jumping to agents or letting a coding agent pick your architecture, arguing for the simplest design that meets requirements, evaluated and iterated. The talk is concrete about data strategy (sources, update cadence, processing, retrieval technique per source), design patterns (RAG, agents, controlled workflows, LLM-as-router, human-in-the-loop, fine-tuning), and a full metric stack from input/output guardrail compliance to production signals like human override rate. Worth watching if you want a checklist-style, domain-grounded process for AI system design rather than another agent-framework demo.

## Key Points

- Vibe coding is fine for low-stakes projects where you can eyeball correctness, but for systems others depend on, shipping without a spec is dangerous — a point Joshi notes is echoed by people at Anthropic and OpenAI.
- The business problem should be user-specific, measurable, time-relevant, and explicitly solution-agnostic: it must not prescribe whether the answer is an agent, a multi-agent system, or something else.
- Business constraints (data residency, approved cloud models, vendor procurement, mandatory human review) and performance constraints (latency, monthly LLM spend, uptime SLAs) should be gathered before design begins because they shape every downstream architectural decision.
- Joshi frames the role of AI along three dimensions — critical vs. complementary, reactive vs. proactive, and level of autonomy — and shows how mandated human review caps the claims system at semi-autonomous.
- Data strategy means enumerating each source's location, raw format, update frequency, required processing, and best-fit retrieval technique; the claims system uses chunking plus vector or hybrid search for guidelines and PDFs but exact match on patient ID for claims history.
- Rather than jumping to an agent, start with the simplest architecture, evaluate it, find the gaps, and iterate — over-engineering before knowing what is actually failing is the most common mistake she sees.
- Guardrails matter because LLM systems are probabilistic: define what invalid input looks like (e.g. 'write me a poem' to a claims system) and what invalid output looks like (e.g. a verdict with no citations), then measure compliance with rates like claim rejection rate and missing citation rate.
- Evaluation happens before shipping and monitoring after, and you need both; production adds implicit success signals such as how often a human overrides the AI verdict and how long human review takes.
- Accuracy, cost, latency, and reliability need separate optimization passes — reranking and memory for accuracy, semantic caching and batch processing for cost/latency, structured outputs for reliability — and those constraints are non-negotiable at production time.

## Notable Quotes

> "Specs are the new code. The art is in defining the product requirements, the system design, and evaluate criteria so you can be confident that your AI coding buddies are building the right thing."
>
> — [1:27](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=87s) &middot; *The thesis of the talk, stated in one line.*

> "Wipe coding works great when you're building for fun, the stakes are low, and you can easily eyeball whether the output of what you're building is right."
>
> — [0:51](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=51s) &middot; *Names the precise boundary condition where vibe coding stops working.*

> "But the moment you're building something real, something other people depend on, something with real consequences, just ship it is actually kind of dangerous."
>
> — [0:51](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=51s) &middot; *Takes an explicit side against ship-first culture.*

> "It should not prescribe what the system is going to be, whether it's going to be an agent, a multi-agent system, something else."
>
> — [4:01](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=241s) &middot; *A checkable rule for writing problem statements that many teams violate.*

> "Medical reviewers at MDB Health spend an average of 2 days processing claim review requests, which is four times the industry standard for non-urgent cases, and 12 times the industry standard for urgent ones."
>
> — [4:01](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=241s) &middot; *Model of a quantified business problem, with baselines.*

> "reduce the average processing time for urgent claim review requests from 2 days to 1 hour within 90 days of launch"
>
> — [7:20](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=440s) &middot; *Concrete example of a SMART success metric.*

> "It can be tempting to jump straight to building an agent. There's so much hype around them, or let a coding agent decide what the system architecture should look like, but you risk ending up with an over-engineered system by doing this."
>
> — [12:07](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=727s) &middot; *Direct pushback on agent hype and on delegating architecture to coding agents.*

> "So, what you instead want to do is start with the simplest design, evaluate it, find gaps during the evaluation, and iterate from there."
>
> — [12:07](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=727s) &middot; *The prescriptive alternative to agent-first design.*

> "if you're observing that the LLM's failures are behavioral rather than data or orchestration issues, or if you need superior performance on a domain-specific task, then fine-tuning is a good technique to explore."
>
> — [14:48](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=888s) &middot; *Gives a usable decision rule for when fine-tuning is the right lever.*

> "So, evaluation is before, monitoring is after you ship, and you need both of them."
>
> — [20:49](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1249s) &middot; *Crisp distinction between two terms often conflated.*

> "guardrails are an attempt to mitigate these risks and ensure that your system behaves within acceptable boundaries. And what those boundaries are are something you need to define."
>
> — [20:49](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1249s) &middot; *Puts the burden of defining acceptable behavior on the builder, not the tooling.*

> "Now if it's rejecting too many times, then that's a call for investigation, but if you didn't measure this in the first place, then you won't have anything to investigate"
>
> — [22:31](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1351s) &middot; *Argues for instrumenting guardrails rather than just installing them.*

> "For example, for the claims review app, you can track how often a human reviewer overrides the AI verdict."
>
> — [24:28](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1468s) &middot; *A concrete production-only metric that acts as an implicit quality signal.*

> "these constraints become absolutely non-negotiable as you're moving your product to production"
>
> — [25:08](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1508s) &middot; *Marks cost, latency, and reliability as hard gates, not nice-to-haves.*

> "Think deeply about your product's requirements before having AI generate any code. The product spec is the hard part now, it's not the code anymore."
>
> — [26:46](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1606s) &middot; *The talk's closing claim about where engineering difficulty has migrated.*

> "Your latency budget, your cost ceiling, any regulatory requirements, all of these shape every architectural decision downstream."
>
> — [27:32](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1652s) &middot; *Explains why constraint-gathering precedes design rather than following it.*

> "The most common mistake I see is over-engineering the solution before knowing what's actually failing or not even evaluating what's actually failing."
>
> — [27:32](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1652s) &middot; *A first-hand observation about the dominant failure mode in AI system design.*

> "Build evaluation in from the start. You can't improve what you can't measure."
>
> — [27:32](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1652s) &middot; *Compresses the evaluation argument into a takeaway.*

## Positions

- Vibe coding is appropriate only for low-stakes projects where output correctness can be eyeballed; for systems with real consequences it is dangerous. ([0:51](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=51s), confidence: stated)
- Writing the product spec — requirements, system design, and eval criteria — is now the hard part of engineering, not writing the code. ([26:46](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1606s), confidence: stated)
- A business problem statement should be solution-agnostic and must not specify whether the system will be an agent or multi-agent system. ([4:01](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=241s), confidence: stated)
- Letting a coding agent choose your system architecture risks producing an over-engineered system. ([12:07](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=727s), confidence: stated)
- You should start with the simplest architecture that meets requirements, evaluate it, and only then iterate based on observed gaps. ([12:07](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=727s), confidence: stated)
- Over-engineering before knowing what is actually failing is the single most common mistake in AI system building. ([27:32](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1652s), confidence: stated)
- Business, regulatory, and performance constraints must be gathered before design because they determine every downstream architectural decision. ([27:32](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1652s), confidence: stated)
- Vector search alone is insufficient for documents containing diagnosis and procedure codes; metadata pre-filtering or hybrid search is needed. ([11:16](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=676s), confidence: stated)
- Fine-tuning should be reserved for behavioral failures or domain-specific performance needs, not for data or orchestration problems. ([14:48](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=888s), confidence: stated)
- Offline evaluation and production monitoring are distinct and both are required; shipping with only one is insufficient. ([20:49](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1249s), confidence: stated)
- Guardrail behavior must itself be measured with rates like claim rejection rate and missing citation rate, or you have nothing to investigate when things go wrong. ([22:31](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1351s), confidence: stated)
- A rising human-override rate on AI verdicts indicates the system is not doing its job and should trigger investigation above a threshold. ([24:28](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1468s), confidence: stated)
- Accuracy optimization in LLM applications reduces to optimizing what information ends up in the context window. ([25:08](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1508s), confidence: stated)
- A prototype with good accuracy is not production-ready; further iteration on cost, latency, and reliability is required first. ([25:08](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1508s), confidence: stated)
- Data pipelines must run at a cadence matched to each source's update frequency, or the system operates on stale information. ([9:43](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=583s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [online evaluation](../concepts/online-evaluation.md)
- [output guardrails](../concepts/output-guardrails.md)
- [requirements elicitation](../concepts/requirements-elicitation.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [spec-driven development](../concepts/spec-driven-development.md)

