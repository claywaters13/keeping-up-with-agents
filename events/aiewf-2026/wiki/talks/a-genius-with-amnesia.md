---
title: "A Genius With Amnesia"
type: "talk"
slug: "a-genius-with-amnesia"
org: "Nx"
video_id: "jVjt-2g8NMY"
duration_sec: 1199
word_count: 3363
speakers: ["Victor Savkin"]
---

# A Genius With Amnesia

**Speakers:** [Victor Savkin](../speakers/victor-savkin.md)

**Org:** Nx

**Duration:** 19m 59s

[Watch on YouTube](https://www.youtube.com/watch?v=jVjt-2g8NMY)

## Summary

Victor Savkin of Nx argues that coding agents are 'a genius with amnesia': brilliant within a session but constrained along two axes — space (an agent sees and writes one repo at a time, never the whole system of hundreds or thousands of repos) and time (every session starts from a blank slate, so the human becomes the memory). He walks through a concrete multi-repo change that required seven separate re-explanations of what was conceptually one change, then argues both limits can be lifted at the harness layer rather than by better models. The proposed solution is Polygraph, an agent-agnostic 'meta harness' that builds a unified dependency graph across every repo a GitHub user can reach, boots coordinated agents across selected repos, treats multi-repo CI as one vector, and captures agent traces so a session's full state can be materialized on another developer's machine — even under a different agent. The demo covers multi-repo sessions, session resumption across machines and agents, semantic search over past sessions for prior art, and pulling open-source repos in for real-code (rather than docs) grounding. Worth watching if you care about multi-repo agentic workflows, organizational memory across sessions, or harness design above the model.

## Key Points

- Agent limitations fall into two categories: a spatial one (repo-bound context, seeing perhaps 1/1000 of the system) and a temporal one (no episodic memory, so every session starts fresh).
- Because agents can't see or write across repos, humans re-explain the same change to each consumer; Savkin's worked example turns one logical change into seven explanations across four repos.
- The cost of re-explanation is both developer time and tokens — changing something across 20 repos means re-explaining it 20 times.
- Savkin's framing is that the true graph of organizational work has two layers: a repository graph at the bottom (owned plus open-source dependencies) and a graph of agentic sessions on top that created and modified it.
- Polygraph is a meta harness, not an agent: it extracts metadata from repos a user can access to build a unified dependency graph, then creates the illusion of one large code base the agent can read and write anywhere.
- Multi-repo CI is treated as a single vector, so a failure in one repo triggers reasoning about whether the consumer needs a patch or the producing library is broken.
- Capturing intent, repos, PRs, and full agent traces makes sessions portable — a coworker can reconstruct the same repos, SHAs, and agent history on a different machine with a different agent, enabling cross-agent memory sharing.
- The session graph enables retrieval of prior art: asking which past sessions are relevant lets teams replicate an approach taken by a respected engineer, improving cross-repo consistency.
- Savkin prefers pulling the actual open-source repo into a session over documentation-retrieval tools like Context7, because real code lets the agent investigate deep problems.

## Notable Quotes

> "You would have a genius on one side and something deeply deficient on the other. And that's what agents are."
>
> — [0:41](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=41s) &middot; *The thesis of the talk in one line, and the source of the title.*

> "So we have seven explanations for what essentially is one change."
>
> — [1:57](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=117s) &middot; *Quantifies the redundancy cost with the talk's central worked example.*

> "an agent essentially is repo bound. Agent sees and changes generally one repo at a time. It never sees the whole system, which can be hundreds or thousands of repos."
>
> — [2:41](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=161s) &middot; *States the spatial half of the diagnosis precisely.*

> "Second is amnesia. Agent forget the work. Every session start with a blank slate. The human becomes the memory in this case."
>
> — [2:41](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=161s) &middot; *States the temporal half, plus the pointed claim that humans are currently the memory layer.*

> "the agent writes to one repo at a time, it means it can't validate changes downstream."
>
> — [3:27](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=207s) &middot; *Names the specific failure mode — no downstream validation — rather than a vague context complaint.*

> "Changing something across 20 repos means re-explaining things 20 times. A lot of developer time spent, but also a lot of tokens burned."
>
> — [4:11](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=251s) &middot; *Frames the problem as both a human-time and a token-cost problem.*

> "Imagine an agent that could see one file at a time maximum and can only look five messages back."
>
> — [5:45](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=345s) &middot; *The reductio that makes the current constraints feel absurd.*

> "We built an agent agnostic meta harness called Polygraph. Okay, let me show you what it does and how it fixes the issues we just discussed."
>
> — [6:28](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=388s) &middot; *Introduces the artifact and its positioning as agent-agnostic infrastructure.*

> "if a GitHub user, any user, has access to thousands of repos, some of them they own, many of them are open source, we can analyze them and extract a lot of metadata out of them to build unified dependency graph"
>
> — [6:28](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=388s) &middot; *Explains the core mechanism: graph built from access scope, without touching the repos themselves.*

> "I want to have about 300 repos I own, right? And thousands of open source repos my projects depend on."
>
> — [7:22](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=442s) &middot; *A concrete scale figure for what the graph spans.*

> "What if one of them fails, right? Polygraph treats all the CI as one vector."
>
> — [8:24](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=504s) &middot; *Names the design decision that makes multi-repo CI tractable.*

> "Polygraph lets you treat complex multi-repo change as if it was a single repo change."
>
> — [9:19](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=559s) &middot; *The product claim in its cleanest form.*

> "What you get is an agent with eidetic or photographic memory of your entire organization."
>
> — [9:59](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=599s) &middot; *The aspirational end state the memory machinery is aimed at.*

> "Polygraph isn't an agent. It's a meta harness around an agent that makes them uh more capable."
>
> — [10:49](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=649s) &middot; *Clarifies the layer of the stack being argued about — harness, not model.*

> "I can work, they can work, and we can share our memories as though we used to different agents in different machine."
>
> — [14:01](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=841s) &middot; *Stakes out cross-agent, cross-machine memory portability as the key capability.*

> "I resume their session on my machine, I get the exact state, fully functional, zero setup, and then I just talk to my agent about the decisions we made"
>
> — [14:37](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=877s) &middot; *Concrete workflow change: code review by resuming the author's session instead of asking the author.*

> "Instead of doing stuff from scratch, where, you know, every single implementation is bespoke, I can make it replicate the approach used in the session by an engineer I respect."
>
> — [16:49](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1009s) &middot; *Reframes session memory as a consistency and best-practices mechanism, not just recall.*

> "I much prefer this to say context seven, because if I have the real code, the agent can go really deep."
>
> — [18:35](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1115s) &middot; *A direct, contestable preference for real source over documentation retrieval.*

> "So, agents are constrained in space and time. They only see a small fraction of the code base, as they don't know the past"
>
> — [18:35](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1115s) &middot; *The closing restatement of the two-axis framing.*

> "Because it crosses developer boundaries, not per developer, the agent can have more context than any single developer."
>
> — [19:13](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1153s) &middot; *The strongest claim in the talk: pooled session memory can exceed any individual's knowledge.*

## Positions

- Today's coding agents are fundamentally constrained along two axes — space (one repo at a time) and time (no memory across sessions) — and these, not model capability, are the binding limits. ([2:41](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=161s), confidence: stated)
- Because agents lack a model of how repos fit together, the human is forced to act as both the research layer and the memory layer of the system. ([3:27](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=207s), confidence: stated)
- Re-explaining a change to N repos costs N times the developer effort and tokens, so multi-repo re-explanation is a measurable efficiency loss. ([4:11](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=251s), confidence: stated)
- The right fix lives in a harness layer above the agent rather than in the agent itself; the solution should be agent-agnostic. ([6:28](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=388s), confidence: stated)
- A unified dependency graph can be built purely from metadata extraction, without changing any line of code in the analyzed repos. ([6:28](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=388s), confidence: stated)
- Multi-repo CI should be evaluated as a single unit so the system can attribute a failure to either the consumer or the producing library. ([8:24](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=504s), confidence: stated)
- The same infrastructure that solves cross-repo context also solves episodic memory, because capturing intent, repos, PRs, and traces makes sessions relatable and restorable. ([9:19](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=559s), confidence: stated)
- Session state, not just conversational memory, is what enables another person to continue someone else's work — the full state of the world must be materialized. ([14:01](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=841s), confidence: stated)
- Memory should be portable across different agent products, so a session started in Claude can be continued in Codex mid-stream. ([14:37](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=877s), confidence: stated)
- Loading the real open-source repository into a session is superior to documentation-retrieval tools like Context7 for diagnosing deep problems. ([18:35](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1115s), confidence: stated)
- Pooling sessions across all developers in an organization gives an agent more context than any individual developer possesses. ([19:13](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1153s), confidence: stated)
- Other organizations have converged on similar solutions, so this is a general architectural pattern rather than a single vendor's idiosyncrasy. ([5:45](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=345s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [code comprehension and indexing](../concepts/code-comprehension-and-indexing.md)
- [institutional knowledge capture](../concepts/institutional-knowledge-capture.md)
- [model portability](../concepts/model-portability.md)
- [session management](../concepts/session-management.md)

