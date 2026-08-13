---
title: "Agents in Production: How OpenGov Built and Scaled OG Assist"
type: "talk"
slug: "agents-in-production-how-opengov-built-and-scaled-og-assist"
org: "OpenGov"
video_id: "4uFVSLgD2Q4"
duration_sec: 1109
word_count: 3047
speakers: ["Gabe De Mesa"]
---

# Agents in Production: How OpenGov Built and Scaled OG Assist

**Speakers:** [Gabe De Mesa](../speakers/gabe-de-mesa.md)

**Org:** OpenGov

**Duration:** 18m 29s

[Watch on YouTube](https://www.youtube.com/watch?v=4uFVSLgD2Q4)

## Summary

An OpenGov engineer walks through the architecture behind OG Assist, a customer-facing agent embedded as a button across the company's government ERP products (budgeting, procurement, asset management, permitting). The talk is mostly a concrete stack tour: why the team abandoned LangGraph for a hand-rolled agent loop built on Effect (a TypeScript library giving them tracing, structured concurrency, and dependency-injected model swapping out of the box), why they adopted Google's A2A protocol as the front-end/back-end contract, and how they handle safety via human-in-the-loop tool approvals and ephemeral sandboxes for code execution. It also covers their two-track feedback system (thumbs up/down signals plus automated evals running against real completions in CI) and rolling summarization for long context. Worth watching if you want a real production example of an agent shipped across a multi-product SaaS suite, or if you're evaluating Effect as an agent framework foundation; less useful if you want depth on any single technique, since each topic gets roughly a minute.

## Key Points

- OG Assist is a single button in the navigation bar of every OpenGov product, and each product team contributes tools and skills to power it, so the agent's capabilities scale with the org rather than with one central team.
- The team started on LangGraph but migrated to their own Effect-native agent loop once the team and use cases scaled, in order to get full control over the loop for complex features.
- Building on Effect propagates tracing, structured concurrency, and logging through the entire agent loop for free, and dependency injection of the language model makes hot-swapping models trivial.
- Google's A2A protocol is used not just for inter-agent communication but as the rigorous schema contract between OpenGov's front end and back end, which the speaker credits with driving team alignment.
- Evals run in CI against real completions and check whether the agent hit the expected tools, working in conjunction with thumbs up/down user feedback to drive iteration.
- The agent loop is deterministically interrupted for tool calls requiring approval, showing an accept/reject UI — used especially for mutating operations to build user trust.
- Code execution and file creation happen in ephemeral, isolated sandboxes that are spun up on demand and torn down afterward, keeping production systems insulated.
- For long conversations, rolling summarization every n messages plus retention of only the most recent messages outperformed simply stuffing in the latest context, and the running summary doubles as a recall/memory layer.
- The agent can render generative UI at runtime — e.g. registering a form primitive and building a form on the fly to collect user choices — and can see and act on what's on the user's screen.
- OpenGov uses Claude and Cursor internally to accelerate reading, writing, and reviewing code, mirroring the customer-facing tools-and-skills approach.

## Notable Quotes

> "all of our product suites and product teams have built tools and skills in order to power this button"
>
> — [2:14](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=134s) &middot; *Names the organizational model that makes a single agent entry point work across a multi-product suite.*

> "originally we were on LangGraph and that was fine until the team really started to scale uh and our use cases started to evolve"
>
> — [5:16](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=316s) &middot; *The explicit framework-migration tradeoff, and the one claim most likely to be contested by other talks.*

> "we decided to move over to our own kind of Effect Native Agent Loop to have full regency over this uh Agent Loop such that if we have complex use cases or features that we need to build, we could kind of get in we we had full control of the of the Agent Loop"
>
> — [6:00](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=360s) &middot; *States the build-vs-adopt rationale for owning the agent loop.*

> "all the cool things you get with Effect is now propagated throughout the entire Agent Loop, like the tracing, structured concurrency, the logging, everything is more fine-grained control"
>
> — [6:00](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=360s) &middot; *Concrete list of what the framework bet actually buys them.*

> "since we're kind of doing dependency injection, we could pass in a different language model if we were to uh hot swap to another one"
>
> — [6:43](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=403s) &middot; *Model portability as an architectural property rather than a migration project.*

> "having this kind of rigorous protocol, this rigorous spec really helped drive our development and drive alignment because, you know, all we had to do was um align with this spec and follow this spec and we knew that this was kind of the contract that our front end and back end would both consume and and produce"
>
> — [8:14](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=494s) &middot; *Reframes A2A as an internal API contract, not just an inter-agent wire format.*

> "Shipping is the start, not the finish."
>
> — [8:56](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=536s) &middot; *The talk's thesis on production agents in one line.*

> "in in the in our CI we we have evals that run against real completions, so we could test the prompt against, "Hey, did it hit some tools? Did it do what it's supposed to do?""
>
> — [9:44](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=584s) &middot; *Specifies what their automated evals actually assert — tool-call correctness in CI.*

> "we deterministically interrupt the agent loop if there is a tool call approval required"
>
> — [10:28](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=628s) &middot; *The human-in-the-loop mechanism stated precisely, including that it is deterministic rather than model-decided.*

> "especially when the agent's trying to do a mutating operation and always always always making sure that, um, humans are in the driver's seat"
>
> — [10:28](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=628s) &middot; *Draws the line for where approval is required: mutating operations.*

> "whenever an agent tries to execute code or tries to create files, it does so in a sandbox"
>
> — [11:10](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=670s) &middot; *A clean, checkable statement of their code-execution safety policy.*

> "we found that having some sort of um rolling summarization was more effective than you know always stuffing in the latest and most recent uh messages"
>
> — [12:12](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=732s) &middot; *A direct empirical position on context management strategy.*

> "when you have this rolling summary of a a really long conversation, then you could do recall over that uh summarization"
>
> — [13:16](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=796s) &middot; *Connects compaction to memory — the summary is the retrieval substrate.*

> "the agent had this primitive registered uh uh this form, and it was able to build out this form for me at runtime and give me some options of what I could choose from"
>
> — [13:56](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=836s) &middot; *Explains generative UI concretely as pre-registered primitives assembled at runtime.*

> "You can't scale what you can't see."
>
> — [14:37](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=877s) &middot; *The observability argument compressed into the talk's most quotable line.*

> "especially working in agentic systems where we're we're integrating with other teams and other APIs and other um other platform capabilities"
>
> — [15:24](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=924s) &middot; *Explains why cross-service tracing matters more for agents than for ordinary services.*

> "we believe that tools and skills are really all you need"
>
> — [16:16](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=976s) &middot; *The strongest stated position in the talk, and a deliberately contrarian one about agent capability design.*

> "we're building tools and skills for customer-facing uh agents and and that has been great, but we're also building them internally as well to help accelerate our development workflows"
>
> — [17:48](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=1068s) &middot; *The symmetry between the external product and internal developer tooling.*

## Positions

- LangGraph was adequate initially but stopped fitting as the team and use cases scaled, justifying a move to a custom agent loop. ([5:16](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=316s), confidence: stated)
- Owning the agent loop end-to-end is worth the build cost because it gives fine-grained control needed for complex features. ([6:00](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=360s), confidence: stated)
- Effect is a good foundation for production TypeScript agents, providing schema, error handling, logging, and tracing out of the box. ([5:16](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=316s), confidence: stated)
- Adopting a rigorous external spec (A2A) as the front-end/back-end contract improves team alignment and development speed. ([8:14](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=494s), confidence: stated)
- Tool-call approval interrupts should be deterministic rather than left to the model's judgment. ([10:28](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=628s), confidence: stated)
- All agent code execution and file creation should be confined to ephemeral isolated sandboxes. ([11:10](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=670s), confidence: stated)
- Rolling summarization plus a truncated recent-message window handles long context better than always including the most recent messages. ([12:12](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=732s), confidence: stated)
- Automated evals asserting tool-call behavior, combined with thumbs up/down feedback, are what enable fast iteration on agent quality. ([9:44](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=584s), confidence: stated)
- Tools and skills are a sufficient abstraction for building agent capability — no additional orchestration primitives are needed. ([16:16](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=976s), confidence: stated)
- Observability is a prerequisite for scaling an agentic system, not an afterthought. ([14:37](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=877s), confidence: implied)
- Distributing tool and skill authorship to individual product teams is how a single agent entry point scales across a product suite. ([2:14](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=134s), confidence: implied)

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agent skills](../concepts/agent-skills.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [context compaction](../concepts/context-compaction.md)
- [data flywheels](../concepts/data-flywheels.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [generative ui](../concepts/generative-ui.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [legacy code migration](../concepts/legacy-code-migration.md)

