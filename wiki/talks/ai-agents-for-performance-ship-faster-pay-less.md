---
title: "AI Agents for Performance: Ship Faster, Pay Less"
type: "talk"
slug: "ai-agents-for-performance-ship-faster-pay-less"
track: "Agent & Harness Engineering"
org: "Netflix"
video_id: "CgsWxRUY5Eo"
duration_sec: 2018
word_count: 5357
speakers: ["Rajat Shah"]
---

# AI Agents for Performance: Ship Faster, Pay Less

**Speakers:** [Rajat Shah](../speakers/rajat-shah.md)

**Org:** Netflix

**Track:** Agent & Harness Engineering &nbsp;|&nbsp; **Duration:** 33m 38s

[Watch on YouTube](https://www.youtube.com/watch?v=CgsWxRUY5Eo)

## Summary

Rajat Shah, a staff software engineer on Netflix's AI platform team, argues that AI coding agents have made code authoring ~10x faster while quietly inflating compute cost, because agents optimize for shipping, not for performance, and don't know your internal frameworks. His fix is to put agents on the other side of the ledger: feed production profiler output (call stacks, self/inclusive CPU) directly to a coding agent, which recognizes common anti-patterns like O(n²) loops and per-iteration object allocation, checks out the exact production commit, traces the call path, and opens a code review — in under five minutes for a large codebase. The talk's central artifact is a central, ever-growing pattern/anti-pattern catalog stored as plain markdown in a Git repo (not a vector DB), which acts as fleet-wide long-term memory so later agents don't redo earlier discovery work, and which can be shifted left from post-hoc profiling into code review and even code authoring. Shah is emphatic that the non-AI foundations — test coverage, canary automation, observability — matter more than the agent, and that a human must still approve every merge. Worth watching if you run production services at scale and want a concrete, deliberately unglamorous playbook for level-2 agentic automation with real Netflix numbers attached.

## Key Points

- Faster AI-authored code is driving up infrastructure compute cost, because coding agents are tuned to ship working code fast and don't know your platform, framework, or internal codebase patterns.
- Profiler output is effectively a universal, well-structured format across Java, Python, and Go runtimes, which makes it unusually good input for an LLM without any language-specific tooling.
- The agent can identify a quadratic algorithm purely from the call stack in the profiling data, before ever looking at the source code.
- Given the right instructions, the agent completes the full loop — code search, checkout at the exact production commit, call-path trace, code review — in under 5 minutes on a large codebase.
- The biggest leverage is fan-out: one confirmed anti-pattern (a per-iteration Spectator counter allocation) was found in seven services via cross-repo search, worth 0.5–4.6% of CPU cycles each.
- Long-term memory is implemented as a centralized Git repo of markdown pattern/anti-pattern entries with symbols, confirmed services, and a confidence level — a stateful catalog plus a stateless LLM equals fleet-wide memory.
- Noise control before requesting human attention is layered: existing unit/integration tests must pass, then an automated canary compares CPU, latency, and error rate between old and new code on identical traffic.
- The maturity path runs reactive-to-proactive: start by profiling production, then shift left into reviewer-agent inline comments, then into the authoring agent consulting the catalog before it emits inefficient code.
- Shah deliberately stops at level-2 automation (fixed workflow, tools and hooks) and caps agent authority at opening a code review, since level-3 autonomy demands heavy investment in evaluation, sandboxing, and prompt-injection defenses.

## Notable Quotes

> "the compute cost also uh is increasing at a similar pace uh because uh it doesn't always uh write the fastest code"
>
> — [0:48](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=48s) &middot; *States the talk's core premise — the hidden cost side of 10x code authoring.*

> "Your um agent doesn't know specific details about your platforms and your frameworks uh and your internal code base patterns."
>
> — [1:32](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=92s) &middot; *Rebuts the 'newer models will just write performant code' objection head-on.*

> "People typically end up looking at profiling data only when something is going wrong at 2:00 a.m. and somebody needs to fix a problem because your CPU is unbearable."
>
> — [4:09](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=249s) &middot; *Names the status quo the whole system is designed to replace.*

> "irrespective of which language, which runtime you're using in production, the output of a profiling data is actually very similar and very well-structured for an LLM agent to use"
>
> — [5:50](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=350s) &middot; *The key enabling assumption that makes the approach language-agnostic.*

> "it knows that this is consuming 8.8% of the CPU time during that uh uh period of profiling"
>
> — [10:20](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=620s) &middot; *Concrete number from the first production finding.*

> "This is purely by looking at the call stack that the profiling uh uh data produced."
>
> — [8:53](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=533s) &middot; *Marks the 'aha' — pattern detection happens before any source inspection.*

> "All of it could be done uh in a very large code base with powerful enough code agents in less than 5 minutes."
>
> — [11:20](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=680s) &middot; *The headline throughput claim against a 20-minute-plus manual baseline.*

> "we found that same bad pattern were actually implemented in seven different services uh through cross repo code searches"
>
> — [12:59](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=779s) &middot; *Quantifies the fan-out effect that makes the catalog worth building.*

> "if fixed across all of those different code repos, it could have savings between 0.5 to 4.6% of CPU cycles"
>
> — [13:48](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=828s) &middot; *Reports the actual production savings range.*

> "And together a stateful catalog and a state stateless LLM can become a full fleet-wide memory um for for a coding agent to use."
>
> — [15:26](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=926s) &middot; *Compact statement of the memory architecture.*

> "The solution that I mentioned so far of a memory is not very fancy vector search or or a vector database that needs to store all the catalog of patterns and anti-patterns. Rather, you can start with just a markdown files in a in a centralized Git repo."
>
> — [17:04](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1024s) &middot; *Takes a contrarian side against vector-DB-first agent memory designs.*

> "I'm still keeping the confidence uh bar to just send a code review and not directly uh push it to production. That's by intent."
>
> — [19:51](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1191s) &middot; *Explicit autonomy ceiling, stated as a deliberate design choice.*

> "there is still need for a human approval because you're modifying an existing code that is running just fine in in production in order to optimize it, which is which is very risky"
>
> — [19:51](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1191s) &middot; *Gives the reasoning behind the human-in-the-loop guardrail.*

> "And what I mentioned here is that this is not an AI problem. The observability, canary, verify logic, these are all standard checks that you need need to have in your system."
>
> — [22:47](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1367s) &middot; *The talk's main dissent from AI-first framing of this workflow.*

> "Here's a mental model. Profiler gives the estimate, canary gives ground truth."
>
> — [23:30](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1410s) &middot; *The most quotable compression of the verification design.*

> "You want that reactive path to be your initial guide to build that initial catalog."
>
> — [24:26](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1466s) &middot; *Names the sequencing — reactive first, proactive later.*

> "This could sometimes slow down the uh speed of uh newer code uh being written and might end up consuming more tokens."
>
> — [26:05](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1565s) &middot; *Acknowledges the cost tradeoff of shifting the catalog into authoring.*

> "You still want these foundations very, very right. Your test coverage needs to be rock solid."
>
> — [26:55](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1615s) &middot; *Sets the prerequisite bar before any of this is safe.*

> "You can't simply run AI agents without the right level of security guardrails so that prompt injection and other security attacks that a typical agent infrastructure currently cannot always solve for."
>
> — [32:18](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1938s) &middot; *Why he stops short of full autonomy.*

> "start with level one. Try to move to level two and you get maximum benefits"
>
> — [32:18](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1938s) &middot; *The closing prescriptive recommendation on automation level.*

## Positions

- AI coding agents increase infrastructure compute cost at roughly the same pace they increase code authoring speed, because they do not write the fastest code. ([0:48](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=48s), confidence: stated)
- Newer, better models will not solve performance by themselves, because they lack knowledge of your internal platforms, frameworks, and codebase patterns. ([1:32](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=92s), confidence: stated)
- A human performance engineer spends roughly 20 minutes just identifying hot paths from profiling data. ([4:09](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=249s), confidence: stated)
- Profiler output is structurally similar enough across languages and runtimes that a single LLM workflow works regardless of whether the service is Java, Python, or Go. ([5:50](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=350s), confidence: stated)
- An agent can identify an O(n²) pattern from the call stack alone, without reading the source code first. ([8:53](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=533s), confidence: stated)
- The full pipeline from profile to opened code review completes in under 5 minutes on a large codebase. ([11:20](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=680s), confidence: stated)
- One anti-pattern (repeated Spectator counter object creation in a hot path) appeared in seven Netflix services and was worth 0.5–4.6% of CPU cycles per service. ([13:48](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=828s), confidence: stated)
- Agent memory for this use case should be plain markdown in a central Git repo, not a vector database or vector search. ([17:04](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1024s), confidence: stated)
- The pattern catalog must be centralized rather than team- or product-specific to be useful across the fleet. ([16:13](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=973s), confidence: stated)
- Agents should never push performance fixes directly to production; a human must approve the code review because modifying working production code is risky. ([19:51](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1191s), confidence: stated)
- Passing tests are insufficient verification; an automated canary comparing CPU, latency, and error rate should be a prerequisite before a code review reaches a human. ([21:57](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1317s), confidence: stated)
- The hard prerequisites — observability, canary, verification logic — are ordinary engineering foundations, not AI problems, and matter more than the agent itself. ([22:47](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1367s), confidence: stated)
- Teams should begin with the reactive post-production path to bootstrap the catalog, then shift left toward review-time and authoring-time prevention. ([24:26](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1466s), confidence: stated)
- Consulting the pattern catalog during code authoring slows generation and consumes more tokens, so the catalog must be hierarchically structured and indexed to avoid filling agent context. ([26:05](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1565s), confidence: stated)
- A fixed, predefined workflow with no LLM planning or reasoning is sufficient for this use case and can be run on a weekly schedule per service. ([31:32](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1892s), confidence: stated)
- Level-3 autonomy (agent plans and acts freely) requires heavy investment in evaluation, sandboxing, and prompt-injection defenses that current agent infrastructure cannot always provide, so level 2 is where most teams should stop. ([32:18](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1938s), confidence: stated)
- Without solid integration points and foundations, introducing agents into the performance workflow will cause more friction and more production bugs than it removes. ([29:04](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1744s), confidence: stated)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [code comprehension and indexing](../concepts/code-comprehension-and-indexing.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)

