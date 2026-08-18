---
title: "Evolution of agentic surfaces"
type: "talk"
slug: "evolution-of-agentic-surfaces"
track: "Workshops Day 1"
org: "Anthropic"
day: "Day 1 — Workshop Day"
room: "Track 9"
video_id: "K0X9QDRkIdg"
duration_sec: 1883
word_count: 5657
speakers: ["Gagan Bhat", "Isabella Kai He"]
---

# Evolution of agentic surfaces

**Speakers:** [Gagan Bhat](../speakers/gagan-bhat.md), [Isabella Kai He](../speakers/isabella-kai-he.md)

**Org:** Anthropic

**Track:** Workshops Day 1 &nbsp;|&nbsp; **Day/Room:** Day 1 — Workshop Day &middot; Track 9 &nbsp;|&nbsp; **Duration:** 31m 23s

[Watch on YouTube](https://www.youtube.com/watch?v=K0X9QDRkIdg)

## Summary

Two members of Anthropic's Applied AI team trace how the surface for building agents has moved from the raw Messages API, to the Claude Agent SDK (which packaged the Claude Code harness and agentic loop), to Claude managed agents, where Anthropic runs the loop, sandbox, credentials, session state, and observability so teams only own their task, context, and domain knowledge. The core argument is that harnesses encode assumptions about what the model can't do yet, those assumptions go stale as models improve, and a stale harness actively degrades a newer model — their example is the context-anxiety workarounds built for Sonnet 4.5 becoming pure overhead under Opus 4.5. They walk through the architecture: decoupling the 'brain' (agent loop) from the 'hands' (tool execution), three primitives (agent, environment, session), durable session logs that enable resumption and context re-reading, and four session states for reliability. A live demo builds an SRE incident-investigation agent from scratch, and four field lessons cover credential vaults, latency wins from decoupling (60% faster TTFT at P50, >90% at P95), session logs as the basis for both observability and memory, and self-hosted sandboxes/MCP tunnels for security-conscious enterprises. Worth watching if you maintain your own agent harness and want a concrete case for why that maintenance burden is now the bottleneck, plus previews of 'dreaming' (batch memory self-improvement) and 'outcomes' (a grader agent that retries against a rubric).

## Key Points

- Agentic surfaces have gone through three generations — Messages API (tokens in, tokens out), Claude Agent SDK (packaged agentic loop, file system, tools, sandboxing), and Claude managed agents (Anthropic-run production infrastructure) — each absorbing more of what teams previously hand-rolled.
- Harnesses encode assumptions about model limitations, and those assumptions must be re-questioned every release: context-reset fixes added for Sonnet 4.5's 'context anxiety' became dead weight and added latency and cache-discard bugs once Opus 4.5 no longer exhibited the behavior.
- Managed agents decouples the agent loop ('brain') from the tool execution environment ('hands'), which improves reliability (a dead sandbox can be respawned and retried), allows on-demand container spin-up, and lets the sandbox run anywhere including a customer VPC.
- The architecture rests on three primitives — agent (model, prompts, tools, skills), environment (the container, with network allowlists), and session (a durable cloud-persisted record of every interaction) — with four session states: idle, running, rescheduling, terminated.
- Because every event is written to a durable session log, the harness can read slices of context back into the window after Claude discards them, decoupling the context window from the session in a way traditional harnesses cannot.
- Decoupling produced a measured latency win: the model starts reasoning immediately while container setup runs in parallel (or is skipped), yielding 60% faster time to first token at P50 and over 90% improvement at P95.
- Credential vaults keep security tokens out of the model's view entirely, decrypting only at tool execution runtime in the separated hands environment.
- Frontier features extend the same fundamentals: 'dreaming' batch-processes session transcripts plus current memory state to rewrite memory for self-improving agents, and 'outcomes' runs a separate grader agent against a user-defined rubric that makes the agent retry until success criteria are met.

## Notable Quotes

> "that is that harnesses encode assumptions about what Claude cannot do on its own"
>
> — [7:29](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=449s) &middot; *The thesis of the whole talk in one line.*

> "So, when the model moves and the harness doesn't, it degrades the agent."
>
> — [8:45](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=525s) &middot; *The sharpest statement of the failure mode they are arguing against.*

> "Opus 4.5 no longer exhibited context anxiety, which means that the fixes that we'd added into the harness itself became dead weight. In fact, it became pure overhead, adding things like latency and causing issues with the cache being discarded incorrectly at times."
>
> — [8:08](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=488s) &middot; *The concrete, named example that grounds the stale-assumptions claim.*

> "What you don't want to do is have a stale harness that takes weeks or even months to migrate to a new model, especially with how model release cycles have been coming out shorter and shorter."
>
> — [9:23](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=563s) &middot; *Names the operational cost and ties it to release cadence.*

> "we saw 60% faster time to first token for P50 use cases or median use cases. And over 90% improvements in latency for time to first token in P95 use cases."
>
> — [23:55](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1435s) &middot; *The talk's only hard performance numbers.*

> "harnesses have become the limiting factor to what models can achieve"
>
> — [30:20](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1820s) &middot; *The closing claim that reframes harness design as the bottleneck, not model capability.*

> "We took it a step further by introducing the concept of vaults, where you can store security credentials in a secure way, and they're decrypted only when needed at tool execution runtime."
>
> — [22:01](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1321s) &middot; *Specific mechanism for the most-asked enterprise security question.*

> "if you feed the transcripts and the memory state as a periodic batch process with what we call dreaming, it allows us to extract new insights and new organized structures that essentially feed back and edit the memory as needed to make the next day's agent sessions automatically much more intelligent"
>
> — [27:07](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1627s) &middot; *Defines 'dreaming', the talk's most novel and least-documented idea.*

> "If the grader determines that the agent was not able to complete the task, it'll keep trying until it reaches that success criteria that you have defined for your agent."
>
> — [28:58](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1738s) &middot; *Explains the retry-until-graded-success loop behind 'outcomes'.*

> "the container was blocking the agent being able to start its model reasoning"
>
> — [11:24](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=684s) &middot; *The design flaw in their first architecture that motivated brain/hands separation.*

> "The session log essentially contains events of everything that happened during an agent execution."
>
> — [23:55](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1435s) &middot; *Defines the primitive that observability, memory, and context recovery all depend on.*

> "It's a different story to build an agent that runs in your laptop and serves you as a single user compared to when you actually want to deploy it in production and run it at scale for hundreds of thousands or even millions of users."
>
> — [13:55](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=835s) &middot; *Frames the prototype-to-production reliability gap the product targets.*

> "Initially, we used to only give them questions, simple Q&A. We then started delegating tasks to them. And now, we let agents own entire outcomes."
>
> — [1:24](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=84s) &middot; *Compact three-stage framing of how task delegation has escalated.*

> "with MCP tunnels, they can have their MCP servers run only within their private network and only making outbound calls to the Claude agent loop"
>
> — [25:53](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1553s) &middot; *Names a specific deployment pattern for teams that won't expose MCP servers publicly.*

> "with many traditional harness implementations, the context window in the session are one in the same"
>
> — [14:33](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=873s) &middot; *States the architectural distinction that makes context recovery possible.*

> "This is context management and domain expertise. This is what separates a coding agent from a legal agent or go-to-market agent"
>
> — [16:03](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=963s) &middot; *Draws the line between what Anthropic manages and what the developer must still own.*

## Positions

- Harness fixes written for a model's limitations become pure overhead — adding latency and cache invalidation bugs — once a newer model no longer has that limitation. ([8:08](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=488s), confidence: stated)
- Harnesses, not model capability, are now the limiting factor on what agent products can achieve. ([30:20](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1820s), confidence: stated)
- Harnesses should be designed for the model capabilities of tomorrow rather than tuned to today's model, and built from small independent swappable primitives. ([9:23](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=563s), confidence: stated)
- Putting the agent loop and tool execution in the same container is the wrong architecture: it blocks first-token reasoning on container setup and couples the failure domains. ([11:24](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=684s), confidence: stated)
- Decoupling the agent loop from tool execution delivered 60% faster time to first token at P50 and over 90% improvement at P95. ([23:55](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1435s), confidence: stated)
- The model should never see security tokens; credentials belong in a vault decrypted only at tool execution time. ([22:01](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1321s), confidence: stated)
- Production agent infrastructure (hosting, session management, sandboxing, credentials, observability) is undifferentiated work that teams should outsource rather than build. ([5:11](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=311s), confidence: stated)
- A durable session log is the single substrate for observability, context recovery, and memory self-improvement — the answer to both 'what is my agent doing' and 'how does it get better'. ([23:55](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1435s), confidence: stated)
- Feeding session transcripts plus current memory state through a periodic batch 'dreaming' process makes subsequent agent sessions measurably more intelligent without retraining. ([27:07](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1627s), confidence: stated)
- Developers should own only the system prompts, skills, tools, and domain context; the agent loop, memory, and observability should come from the harness. ([16:03](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=963s), confidence: stated)
- Rubric-based grader agents running alongside the agent loop unlock tasks that were not possible a couple of months ago. ([29:37](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1777s), confidence: stated)
- Enterprise adoption depends on letting tool execution run inside the customer's own VPC under their own policies, not just in the vendor's cloud. ([25:22](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1522s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [context compaction](../concepts/context-compaction.md)
- [context engineering](../concepts/context-engineering.md)
- [latency budgets](../concepts/latency-budgets.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [rubric design](../concepts/rubric-design.md)
- [session management](../concepts/session-management.md)

