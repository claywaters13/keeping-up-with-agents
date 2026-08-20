---
title: "Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents"
type: "talk"
slug: "healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents"
track: "AI in Healthcare"
org: "Onlay"
day: "Day 4 — Session Day 3"
room: "Track 7"
video_id: "UyyOoJmuATU"
duration_sec: 1225
word_count: 2843
speakers: ["Vasant Kearney"]
---

# Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents

**Speakers:** [Vasant Kearney](../speakers/vasant-kearney.md)

**Org:** Onlay

**Track:** AI in Healthcare &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 20m 25s

[Watch on YouTube](https://www.youtube.com/watch?v=UyyOoJmuATU)

## Summary

Vasant Kearney argues that healthcare claims automation needs a harness, and that X12 — the decades-old EDI transaction standard behind eligibility checks, claim submission, and remittance — is the natural one. The argument: LLM agents perform best when confined to formats with clear, limited, predictable values (like COBOL or TypeScript), and every step in the claim lifecycle already has an X12 correspondence, so even phone calls, portal scraping, and desktop automation can be normalized down to an internal X12 representation. He pairs this with a warning that X12 carries no ground truth — a payer's phone system, web portal, and X12 layer can all agree that a patient is covered and the claim still gets denied — so the internal representation is only 'semi-correct until downstream evidence proves otherwise.' The rest of the talk covers the practical harness pieces: database-backed memory instead of local files for enterprise, the bias risk of persistent user memory, why swapping in a better model breaks systems, and why cost per routine transaction constrains model choice. Worth watching if you're building agents against messy external systems and want a concrete example of grounding agentic output in a public standard schema.

## Key Points

- The goal of agentic workflows in healthcare should be grounded in either driving down the cost of interacting with insurance or improving patient experience, not in technical novelty for its own sake.
- X12 functions as a harness because LLMs thrive under constraint — a strict, public schema gives the model clear limited values to predict and forms a contract with the insurance company.
- Every step of the claim lifecycle (scheduling, treatment, documents, submission, payment) has an X12 correspondence, so agent actions across phone, browser, desktop, and EHR can all be boiled down to structured transactions like the 270 eligibility request, the 275 attachment, the 999 acknowledgement, and the 835 remittance.
- X12 provides structure but not truth: a payer's portal, phone system, and X12 layer may be built by different teams or even different contracted companies, and can all agree on wrong information — coverage can be confirmed three ways and the claim still denied.
- The practical resolution is an internal, self-owned X12 representation treated as semi-correct — correct until downstream evidence proves otherwise.
- Reasoning chains of ~50 multimodal steps are slow, expensive, and compound errors at every step, but fully hardcoding the workflow causes code bloat and requires a large engineering team; the design problem is striking the balance between free agentic execution and hardcoded paths.
- Enterprise healthcare can't use local filesystem memory the way Claude Code or Codex does, so memory lives in a database for logical separation — and persistent user/org memory introduces bias, so users must be able to break out of it.
- Upgrading to a more capable model is not a drop-in improvement: a model that scores better on evals is different, not automatically better for your system, so evals, testing, and validation must be redone before swapping.
- Reducing a multimodal input (like an image) to extracted findings before passing it downstream loses context that a later procedure may depend on, arguing for keeping processing multimodal.
- Cost discipline matters because routine transactions run thousands of times a day; an overpowered, overpriced model defeats the cost-reduction goal.

## Notable Quotes

> "And that goal, at least from my perspective, is to drive the overall cost down."
>
> — [0:55](https://www.youtube.com/watch?v=UyyOoJmuATU&t=55s) &middot; *States the north star that the speaker says all technical choices must ladder up to.*

> "LLMs really thrive, they work well, and when they're confined they have clear limited values that they can predict, and X12 is exactly this."
>
> — [8:22](https://www.youtube.com/watch?v=UyyOoJmuATU&t=502s) &middot; *The core thesis: constraint as an enabler of model reliability.*

> "so it provides this underlying structure this contract between what you're trying to communicate and the insurance company"
>
> — [8:22](https://www.youtube.com/watch?v=UyyOoJmuATU&t=502s) &middot; *Frames X12 as an interface contract rather than a legacy format.*

> "which is like all the different nuts and bolts that that surround this agentic reasoning and that is the concept of memory that we discussed the different tools the checks the permissions the handoffs the evals but also in the context of health care and claims it's x12"
>
> — [8:22](https://www.youtube.com/watch?v=UyyOoJmuATU&t=502s) &middot; *Gives the speaker's explicit definition of 'harness' and slots X12 into it.*

> "when you're introducing new and improved better models more sophisticated more parameters you can't you can't just replace the model and assume it's going to be better it's different"
>
> — [7:35](https://www.youtube.com/watch?v=UyyOoJmuATU&t=455s) &middot; *A concrete engineering position on model upgrades that contradicts common practice.*

> "So, cloud code or codex, they use local memory, they write to your desktop. In enterprise healthcare, we can't really do this, so we do memory in a database, just so we have that logical separation."
>
> — [6:51](https://www.youtube.com/watch?v=UyyOoJmuATU&t=411s) &middot; *Names a specific architectural divergence forced by the enterprise healthcare context.*

> "So, we want to be really careful here because as you introduce memory, you also persistent memory across chats, across days, you also introduce bias."
>
> — [12:03](https://www.youtube.com/watch?v=UyyOoJmuATU&t=723s) &middot; *Identifies the tradeoff of personalization memory rather than treating memory as pure upside.*

> "if you hardcode your whole system, you say we're you're going to throw out this whole agentic process, you limit yourself or your code can explode to be just unmanageable"
>
> — [10:34](https://www.youtube.com/watch?v=UyyOoJmuATU&t=634s) &middot; *The counterweight to agent skepticism — states the cost of the fully deterministic alternative.*

> "and each time it each step is an opportunity to introduce an error and you can have problems"
>
> — [10:34](https://www.youtube.com/watch?v=UyyOoJmuATU&t=634s) &middot; *Compact statement of error compounding across long multi-step agent chains.*

> "So, X12 is a is a system of rules and it doesn't mean that when an insurance company gives you an X12, it's true."
>
> — [15:18](https://www.youtube.com/watch?v=UyyOoJmuATU&t=918s) &middot; *The key qualifier separating schema conformance from correctness.*

> "They also within all of these systems, they can they can all actually agree on the wrong information as well."
>
> — [15:18](https://www.youtube.com/watch?v=UyyOoJmuATU&t=918s) &middot; *Rules out cross-source agreement as a validation strategy.*

> "You call them. You look in the browser and the X12 and they all say, "Yes, this patient is covered." And then you treat the patient, they say claim is denied due to the patient wasn't covered during that time."
>
> — [16:18](https://www.youtube.com/watch?v=UyyOoJmuATU&t=978s) &middot; *The concrete failure scenario behind the no-ground-truth claim.*

> "regardless of if it originates as an X12 or not, you can boil all those transactions down to your own internal semi-correct X12. Correct until downstream evidence proves it otherwise"
>
> — [16:18](https://www.youtube.com/watch?v=UyyOoJmuATU&t=978s) &middot; *The design pattern the talk is ultimately selling: a self-owned, provisionally-true canonical representation.*

> "If you ask agents to make a schema for you you're going to get like all sorts of stuff. But now if we ground it in something standard you can look up all of these and you would know just right off the bat my schema."
>
> — [14:35](https://www.youtube.com/watch?v=UyyOoJmuATU&t=875s) &middot; *Argues public standards beat agent-invented schemas for onboarding and agent research alike.*

> "it might be that you're extracting all this information and missing something that relates to some downstream procedure that you didn't that wasn't the upstream model wasn't aware of it"
>
> — [5:08](https://www.youtube.com/watch?v=UyyOoJmuATU&t=308s) &middot; *Explains the context loss that motivates end-to-end multimodal processing over early extraction.*

> "that claim is like a receipt of what you did. I did this, like here's the invoice."
>
> — [17:45](https://www.youtube.com/watch?v=UyyOoJmuATU&t=1065s) &middot; *Clean mental model for what a claim actually is, useful for non-healthcare engineers.*

> "So, being AI filled is great, but you should also be very AI skeptical. Like these things, they make mistakes and it's not even you can't even say they make mistakes. Like we make mistakes designing them."
>
> — [18:38](https://www.youtube.com/watch?v=UyyOoJmuATU&t=1118s) &middot; *Relocates blame for agent failure from the model to the system designer.*

> "Let's say it's ends up being super super expensive to deliver one of these routine things that need to be done a thousand times a day. You definitely don't want that."
>
> — [19:32](https://www.youtube.com/watch?v=UyyOoJmuATU&t=1172s) &middot; *Ties model selection back to unit economics at production volume.*

## Positions

- LLMs perform better when confined to strict, limited-vocabulary formats, which is why X12 works as a harness for claims agents. ([8:22](https://www.youtube.com/watch?v=UyyOoJmuATU&t=502s), confidence: stated)
- Every step of the claim lifecycle has an X12 correspondence, so any agent action — phone call, portal, desktop, imaging system — can be reduced to a structured transaction. ([13:44](https://www.youtube.com/watch?v=UyyOoJmuATU&t=824s), confidence: stated)
- An X12 response from an insurance company is not ground truth; the payer's portal, phone system, and X12 layer can all report the same wrong answer. ([15:18](https://www.youtube.com/watch?v=UyyOoJmuATU&t=918s), confidence: stated)
- Teams should maintain their own internal X12 representation treated as correct only until downstream evidence disproves it. ([16:18](https://www.youtube.com/watch?v=UyyOoJmuATU&t=978s), confidence: stated)
- Swapping in a newer, higher-scoring model can break a working system, so evals, testing, and validation must be rebuilt from scratch before the upgrade. ([7:35](https://www.youtube.com/watch?v=UyyOoJmuATU&t=455s), confidence: stated)
- Enterprise healthcare agents should store memory in a database rather than on the local filesystem the way Claude Code and Codex do. ([6:51](https://www.youtube.com/watch?v=UyyOoJmuATU&t=411s), confidence: stated)
- Persistent cross-session user memory introduces bias toward repeating yesterday's action, so users must be able to break out of it. ([12:03](https://www.youtube.com/watch?v=UyyOoJmuATU&t=723s), confidence: stated)
- Fully hardcoding the claims workflow is not a viable alternative to agents because the codebase bloats and requires an oversized engineering team. ([10:34](https://www.youtube.com/watch?v=UyyOoJmuATU&t=634s), confidence: stated)
- Collapsing an image into extracted findings before downstream modeling loses context that later procedures depend on, so processing should stay multimodal. ([5:08](https://www.youtube.com/watch?v=UyyOoJmuATU&t=308s), confidence: stated)
- Public standard schemas are preferable to agent-generated schemas because they are lookup-able by both new engineers and coding agents. ([14:35](https://www.youtube.com/watch?v=UyyOoJmuATU&t=875s), confidence: stated)
- Using an overpowered, expensive model for high-frequency routine transactions defeats the cost-reduction purpose of the system. ([19:32](https://www.youtube.com/watch?v=UyyOoJmuATU&t=1172s), confidence: stated)
- Agent failures should be attributed to system design rather than to model error. ([19:32](https://www.youtube.com/watch?v=UyyOoJmuATU&t=1172s), confidence: stated)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [context engineering](../concepts/context-engineering.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [model portability](../concepts/model-portability.md)
- [structured output contracts](../concepts/structured-output-contracts.md)
- [verifier design](../concepts/verifier-design.md)

