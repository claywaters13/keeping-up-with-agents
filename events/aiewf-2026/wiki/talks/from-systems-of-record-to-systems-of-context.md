---
title: "From Systems of Record to Systems of Context"
type: "talk"
slug: "from-systems-of-record-to-systems-of-context"
track: "Graphs"
org: "monday.com"
day: "Day 4 — Session Day 3"
room: "Track 5"
video_id: "Btk8wDUVs74"
duration_sec: 957
word_count: 2513
speakers: ["Omri Bruchim"]
---

# From Systems of Record to Systems of Context

**Speakers:** [Omri Bruchim](../speakers/omri-bruchim.md)

**Org:** monday.com

**Track:** Graphs &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 15m 57s

[Watch on YouTube](https://www.youtube.com/watch?v=Btk8wDUVs74)

## Summary

Two engineering managers from monday.com argue that the bottleneck for work assistants is not data access or retrieval but understanding — knowing how a user's entities, people, and commitments connect and which matter right now. They describe the "Monday world model" behind their Sidekick assistant: a precomputed data model built offline from Monday boards, Slack, email, and calendar, split into a slow engine that mines weeks of activity into a durable user profile and a fast engine that recomputes live signals over a short recent window. They ground this two-speed split in prior art from neuroscience (complementary learning systems) and data infrastructure (lambda architecture), and claim it buys graceful degradation, urgency awareness, and compounding value as new sources are added cheaply. Worth watching if you're designing agent memory/context layers and want a concrete architecture for precomputing meaning rather than stuffing more into a prompt at query time. It's a short, architecture-level talk with no benchmarks or evals — the honest caveats (cold start, trailing state, signal bias) are stated but not solved.

## Key Points

- The framing shift is from "system of record" (logging every task, message, and status) to "system of context" (software that understands the connections between those records).
- The speakers insist the hard problem is understanding, not retrieval — agents already have access to boards, Slack, email, and MCP connectors and still can't answer "what should I focus on right now?"
- They name an "agent gap": agents execute well when told what to do (drafting a reply to an escalation) but guess when asked to identify what matters, because they lack a model of the user's priorities.
- Meaning must be computed ahead of time, not at runtime — you cannot build understanding in the moment a user asks the question.
- The Monday world model collects thousands of data points per user and constructs three artifacts: a structural graph of entities and dependencies, a live snapshot of current signals, and a durable learned profile.
- Two engines on different time windows produce this: a slow engine mining weeks of activity into a reinforced persona/routine profile, and a fast engine recomputing urgency signals over a short recent window — "one knows you and the other one knows your day."
- The two-speed design is explicitly borrowed from complementary learning systems in neuroscience (hippocampus vs. neocortex) and lambda architecture in data processing.
- The architecture is designed to degrade rather than fail: sources are isolated so a bad feed can't break the rest, and a thin serve-time layer verifies part of the context against live data while the rest falls back to the last verified context.
- Value compounds because each new data source is cheap to add and only contributes, while stated limits remain: the model trails the live world, new users have no reliable data, and separating signal from noise is the hardest part.

## Notable Quotes

> "The problem was never the missing of data, the retrieval. The problem is like the missing understanding."
>
> — [1:46](https://www.youtube.com/watch?v=Btk8wDUVs74&t=106s) &middot; *The thesis of the talk in one line.*

> "Understanding is the word that we're going to focus the entire the entire talk. Not context, not memory, not retrieval, understanding."
>
> — [1:46](https://www.youtube.com/watch?v=Btk8wDUVs74&t=106s) &middot; *Explicitly rejects the three most common framings in agent-memory discourse.*

> "but asking him what should I focus on first he guess because he doesn't understand what is my priority who am I it doesn't matter if you have a memory or something he still don't know what is the problem"
>
> — [5:20](https://www.youtube.com/watch?v=Btk8wDUVs74&t=320s) &middot; *Defines the 'agent gap' and takes a swipe at memory as a sufficient fix.*

> "you can go to your Monday board and see which PR connected to this item and understand that this line of code came because some customer complain about something."
>
> — [5:59](https://www.youtube.com/watch?v=Btk8wDUVs74&t=359s) &middot; *The git-blame analogy that makes 'records without meaning' concrete.*

> "You need to build it much before someone asks the question."
>
> — [6:37](https://www.youtube.com/watch?v=Btk8wDUVs74&t=397s) &middot; *States the precompute-vs-runtime tradeoff that drives the whole architecture.*

> "he understand who you are and it's simply not a bigger prompt."
>
> — [7:16](https://www.youtube.com/watch?v=Btk8wDUVs74&t=436s) &middot; *Positions the world model against the 'just expand the context window' default.*

> "The problem is really to understand how it works. Understand how each one of these entity connected to each other."
>
> — [7:59](https://www.youtube.com/watch?v=Btk8wDUVs74&t=479s) &middot; *Reframes the goal as relationship modeling rather than data access.*

> "We collect thousands of data points on the user every item status change their activity log messages and meetings and construct three things the agent can resone over."
>
> — [7:59](https://www.youtube.com/watch?v=Btk8wDUVs74&t=479s) &middot; *The only quantitative claim about input scale, plus the three-part output structure.*

> "we use two engines running on different time windows and schedules. A slow engine that runs on a long time window and learns the user and their work and a fast engine that reads what's happening right now and how it affects the user's work."
>
> — [8:53](https://www.youtube.com/watch?v=Btk8wDUVs74&t=533s) &middot; *The core architectural claim of the talk.*

> "One knows you and the other one knows your day."
>
> — [8:53](https://www.youtube.com/watch?v=Btk8wDUVs74&t=533s) &middot; *The most portable summary of the two-engine split.*

> "The fast engine is the opposite. It takes as context a short recent window and recomputes a set of live signals over the user's current state."
>
> — [9:39](https://www.youtube.com/watch?v=Btk8wDUVs74&t=579s) &middot; *Specifies the fast path's contract precisely.*

> "this split isn't something we invented. It's present in two totally different fields. In neuroscience, this split is referred to as complimentary learning systems. And in data processing architecture, it's referred to as a lambda architecture."
>
> — [10:29](https://www.youtube.com/watch?v=Btk8wDUVs74&t=629s) &middot; *Names the prior art the design leans on, useful for cross-talk synthesis.*

> "Two different fields landed on the same idea and that's what we're trying to apply to our data model."
>
> — [10:29](https://www.youtube.com/watch?v=Btk8wDUVs74&t=629s) &middot; *The convergent-evolution argument used to justify the architecture.*

> "Both engines premputee on top of that offline and ahead of time. And when a user engages with Sidekick, a thin slice of logic is recomputed for recent activity, and the entire context is served to the agent."
>
> — [11:18](https://www.youtube.com/watch?v=Btk8wDUVs74&t=678s) &middot; *The concrete offline/online boundary at serve time.*

> "Sources are isolated so a bad feed can't break the rest."
>
> — [11:18](https://www.youtube.com/watch?v=Btk8wDUVs74&t=678s) &middot; *A specific reliability design decision others can adopt or contest.*

> "So it degrades gracefully, but it doesn't fail. Second, it actually understands the urgency of facts."
>
> — [12:11](https://www.youtube.com/watch?v=Btk8wDUVs74&t=731s) &middot; *Names the two behaviors the architecture is claimed to buy.*

> "And the crucial part is that it compounds. Every day the data is captured, the layers fill in and the profile sharpens."
>
> — [12:11](https://www.youtube.com/watch?v=Btk8wDUVs74&t=731s) &middot; *The strategic claim — why they think this is a durable moat rather than a feature.*

> "And adding a new data source is deliberately cheap and only contributes. So the surface only grows. The more it sees, the more it understands."
>
> — [12:11](https://www.youtube.com/watch?v=Btk8wDUVs74&t=731s) &middot; *States the additive-integration design goal explicitly.*

> "the model itself is always trailing the actual live world. New users have no reliable data to reason from yet, and signals have our own biases built in. So the hardest part is actually telling the important parts from the noise."
>
> — [12:57](https://www.youtube.com/watch?v=Btk8wDUVs74&t=777s) &middot; *The talk's honest limitations, including cold start and signal bias.*

> "the most capable agent in the world whether it's like a cloud and Gemini, it doesn't understand you. He need to process it beforehand."
>
> — [14:55](https://www.youtube.com/watch?v=Btk8wDUVs74&t=895s) &middot; *Closing position: model capability doesn't substitute for precomputed user context.*

## Positions

- The bottleneck for work assistants is understanding the connections between records, not retrieving data — retrieval is already solved by existing connectors and MCPs. ([1:46](https://www.youtube.com/watch?v=Btk8wDUVs74&t=106s), confidence: stated)
- Adding memory to an agent does not solve the problem of knowing what a user should prioritize. ([5:20](https://www.youtube.com/watch?v=Btk8wDUVs74&t=320s), confidence: stated)
- Contextual understanding cannot be constructed at query time; it must be computed ahead of time, offline. ([6:37](https://www.youtube.com/watch?v=Btk8wDUVs74&t=397s), confidence: stated)
- A longer context window or a bigger prompt is not a substitute for a structured world model of the user. ([7:16](https://www.youtube.com/watch?v=Btk8wDUVs74&t=436s), confidence: stated)
- User context should be modeled with two engines on different time windows — a slow one that learns durable patterns and a fast one that computes live urgency signals. ([8:53](https://www.youtube.com/watch?v=Btk8wDUVs74&t=533s), confidence: stated)
- The fast/slow split is validated by convergent design in neuroscience (complementary learning systems) and data infrastructure (lambda architecture). ([10:29](https://www.youtube.com/watch?v=Btk8wDUVs74&t=629s), confidence: stated)
- Isolating data sources plus a serve-time verification layer with fallback to last-verified context makes the system degrade gracefully instead of failing. ([11:18](https://www.youtube.com/watch?v=Btk8wDUVs74&t=678s), confidence: stated)
- A context model built this way compounds in value over time and makes each additional data source cheap and purely additive. ([12:11](https://www.youtube.com/watch?v=Btk8wDUVs74&t=731s), confidence: stated)
- The approach cannot serve new users well, since there is no reliable historical data to reason from — a cold-start limitation. ([12:57](https://www.youtube.com/watch?v=Btk8wDUVs74&t=777s), confidence: stated)
- Frontier model capability (Claude, Gemini, GPT) is not the limiting factor for personal work assistants; per-user preprocessing is. ([14:55](https://www.youtube.com/watch?v=Btk8wDUVs74&t=895s), confidence: stated)
- Owning the platform where work actually happens is what makes building this understanding layer feasible. ([2:26](https://www.youtube.com/watch?v=Btk8wDUVs74&t=146s), confidence: implied)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [background agents](../concepts/background-agents.md)
- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [context engineering](../concepts/context-engineering.md)
- [ontology design](../concepts/ontology-design.md)
- [world models](../concepts/world-models.md)

