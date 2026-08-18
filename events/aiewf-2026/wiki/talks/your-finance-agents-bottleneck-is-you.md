---
title: "Your Finance Agent's Bottleneck Is You"
type: "talk"
slug: "your-finance-agents-bottleneck-is-you"
track: "AI in Finance"
org: "Auditoria AI"
day: "Day 4 — Session Day 3"
room: "Track 3"
video_id: "z0sh8HyTrDo"
duration_sec: 822
word_count: 1955
speakers: ["Ramana Siddanth Emani"]
---

# Your Finance Agent's Bottleneck Is You

**Speakers:** [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)

**Org:** Auditoria AI

**Track:** AI in Finance &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 13m 42s

[Watch on YouTube](https://www.youtube.com/watch?v=z0sh8HyTrDo)

## Summary

Ramana Siddanth Emani, a data scientist at Auditoria AI, argues that the limiting factor on shipping production AI agents is not model capability, GPUs, or frameworks — all of which improve on their own every few months — but the velocity of the developer's own inner loop. He lays out four harness primitives (parallel sub-agents in git worktrees, skills as organizational 'secret recipes', MCP connections to third-party systems, and a single-pane minimal UX) and walks a nine-step bug-fix pipeline from Jira ticket to staged deploy, claiming a human is genuinely needed only at steps 1 and 9. Part two pushes further: use recursive self-improvement, where you run the loop for a few days, ask the agent to enumerate its own bottlenecks, and remove them daily until a one-sentence prompt ships a fix end to end. He grounds this in finance, where SOX compliance and human sign-off make 'move fast and break things' untenable, and lands on the thesis that the human should remain a verifier but never the throughput ceiling. Worth watching if you're designing internal agent harnesses and want a concrete orchestration pattern; it's a short, opinionated talk with more assertion than measurement.

## Key Points

- Demos are cheap and models, chips, and frameworks all improve on a predictable cadence, so the real differentiator in getting agents to production is how fast your developer loop iterates.
- Sub-agents should run in parallel git worktrees — isolated folders — so that concurrent agents doing independent tasks don't fight over the same files.
- The speaker claims a 48 GB MacBook can sustain roughly 50 active worktrees, i.e. 50 sub-agents working independently, with each QA-reported Jira ticket mapped to its own worktree.
- Skills encode an organization's proprietary workflows and customer-specific recipes, ensuring agents follow the correct internal procedure rather than improvising a fix.
- In a nine-step pipeline (parse ticket → RCA → pull traces/logs → TDD → fix → local e2e → PR → merge → dev/stage deploy), humans are only needed at the first and last steps.
- Orchestration overhead is itself a bottleneck: multi-monitor context switching costs 'neck rotations', so the talk advocates collapsing dashboards, logs, Jira, PRs, and the coding session into one macOS widget.
- Recursive self-improvement of the harness — run the loop for a day or two, have the agent list every bottleneck it hit, then remove them daily — compounds into near-autonomous bug fixing within about a month.
- Combining goals with loops, plus a background 'dreaming' pass that compacts recurring customer session patterns into reusable data points, is how the speaker proposes removing the human from the loop entirely.
- Finance raises the accountability bar: agent-reviewing-agent breaks the auditor/controller sign-off model that SOX compliance assumes, so the human verifier can't simply be deleted.

## Notable Quotes

> "So, how do we in real time fix these production bugs? The answer is your dev loop velocity."
>
> — [2:00](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=120s) &middot; *The thesis of the talk in one line.*

> "Always have the human as a verifier, but not the throughput ceiling because human attention is very limited."
>
> — [12:23](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=743s) &middot; *The closing formulation of the human's proper role, and the sharpest statement of the title's argument.*

> "Is it the model? Do you need a better model? Fable 5, perhaps? Or do you need faster GPUs?"
>
> — [1:06](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=66s) &middot; *Frames the false diagnoses the talk exists to reject.*

> "If you wait 3 and 1/2 months, we are awarded with a new model in the market."
>
> — [2:00](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=120s) &middot; *Puts a number on why model capability isn't the lever worth pulling.*

> "The model capability increases very exponentially. And the developers have to spend a lot of time every day to automate your developer loop."
>
> — [2:00](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=120s) &middot; *States the asymmetry between free model progress and effortful harness progress.*

> "With you as the orchestrator, you can have, let's say, with 48 GB of RAM on your MacBook, you can have 50 active work trees."
>
> — [4:22](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=262s) &middot; *The talk's one concrete capacity number for parallel sub-agents.*

> "You don't want to queue up your tasks because the agent is will do that a lot better than you."
>
> — [5:03](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=303s) &middot; *A direct tradeoff claim: hand scheduling to the agent, not the human.*

> "So, I would say the human is only required at steps 1 and 9 because the in-between steps, the agent can do a lot better work."
>
> — [5:54](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=354s) &middot; *The specific, checkable claim about where human contact belongs in the pipeline.*

> "Second, we have skills. These are your organization secret recipes. So, make sure you have a lot of skills"
>
> — [3:36](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=216s) &middot; *Defines skills as proprietary workflow encoding rather than generic prompting.*

> "So, all of us know production bugs are very high and production guards built by the hour."
>
> — [1:06](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=66s) &middot; *Sets up the demo-to-production gap the harness is meant to close.*

> "Where do you keep the accountability? If something goes wrong in production, you can't say Cloud is doing this. Something is wrong."
>
> — [8:19](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=499s) &middot; *The accountability objection to agent-reviews-agent in regulated domains.*

> "What is the bottleneck? It becomes a human attention because you yourself have to orchestrate all these different tasks."
>
> — [8:19](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=499s) &middot; *Names the bottleneck the title alludes to.*

> "moving fast and breaking things in sector in the finance sector is a lot different"
>
> — [8:19](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=499s) &middot; *Marks where finance diverges from generic startup agent advice.*

> "So, you can see from the graph also, the number of neck rotations to ship one change like reduces a lot drastically."
>
> — [7:27](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=447s) &middot; *Memorable, if informal, metric for the cost of multi-window orchestration.*

> "At the end of one month, let's say, you have a really nice self-automated loop where you just type in one sentence and just say fix this bug for me."
>
> — [10:04](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=604s) &middot; *The concrete payoff claim for recursive harness self-improvement, with a timeline.*

> "you let the agent dream like humans dream in the background so that it collects all the sessions that your customers are using"
>
> — [11:40](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=700s) &middot; *Introduces the 'dreaming' idea — offline compaction of usage patterns into reusable state.*

> "the developers do a lot of variety things in their software development life cycle and sitting behind a desk from 9:00 to 5:00 and just writing code is not valid anymore"
>
> — [11:40](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=700s) &middot; *The implied claim about what the developer role becomes once the loop is automated.*

> "And you just compress all of this into one pane of glass because minimal UX is the key."
>
> — [12:23](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=743s) &middot; *Summarizes the UX primitive as a first-class part of the harness, not a nicety.*

> "So, sorry for the rude title. I don't mean to call the audience here the bottlenecks, but I'm here to talk about the harnesses that you guys are developing"
>
> — [0:01](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=1s) &middot; *Scopes the talk to internal harness engineering rather than agent product design.*

## Positions

- Production agent failures are caused by slow developer loops, not by insufficient model capability, GPU speed, or framework choice. ([2:00](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=120s), confidence: stated)
- A new frontier model arrives roughly every 3.5 months and new chips roughly every year, so waiting on capability is a worse investment than automating your loop. ([2:00](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=120s), confidence: stated)
- A MacBook with 48 GB of RAM can run about 50 active worktrees, i.e. 50 sub-agents in parallel. ([4:22](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=262s), confidence: stated)
- In a nine-step bug-fix-to-stage pipeline, human contact is only necessary at step 1 and step 9; the agent does the intermediate steps better than a human. ([5:54](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=354s), confidence: stated)
- Developers should not manually queue tasks for agents, because the agent schedules its own work better. ([5:03](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=303s), confidence: stated)
- Consolidating dashboards, logs, tickets, PRs, and the coding session into a single widget measurably reduces the context-switching cost of shipping one change. ([7:27](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=447s), confidence: stated)
- Agent-to-agent code review is inadequate in finance because accountability cannot be assigned to the model when something goes wrong in production. ([8:19](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=499s), confidence: stated)
- Iteratively having the agent enumerate and remove bottlenecks in its own harness yields a one-sentence-prompt bug-fixing loop within about a month. ([10:04](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=604s), confidence: stated)
- Background 'dreaming' — compacting recurring customer session patterns into data points the system reuses — is a viable mechanism for agent self-upgrade. ([11:40](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=700s), confidence: stated)
- The human should remain a verifier of agent work but must never be the throughput ceiling of the system. ([12:23](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=743s), confidence: stated)
- Writing code is now cheap enough that shipping impressive demos carries almost no signal about production readiness. ([1:06](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=66s), confidence: implied)
- The traditional 9-to-5 desk-bound code-writing developer role is obsolete once agent loops are automated. ([11:40](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=700s), confidence: implied)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent skills](../concepts/agent-skills.md)
- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [developer productivity metrics](../concepts/developer-productivity-metrics.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [parallel agent execution](../concepts/parallel-agent-execution.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)

