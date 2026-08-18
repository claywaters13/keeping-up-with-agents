---
title: "The Golden Age of AI Engineering"
type: "talk"
slug: "the-golden-age-of-ai-engineering"
track: "Software Factories"
org: "OpenAI"
day: "Day 2 — Session Day 1"
room: "Main Stage"
video_id: "pMggiOb18tc"
duration_sec: 1513
word_count: 4638
speakers: ["Alexander Embiricos", "Romain Huet"]
---

# The Golden Age of AI Engineering

**Speakers:** [Alexander Embiricos](../speakers/alexander-embiricos.md), [Romain Huet](../speakers/romain-huet.md)

**Org:** OpenAI

**Track:** Software Factories &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 25m 13s

[Watch on YouTube](https://www.youtube.com/watch?v=pMggiOb18tc)

## Summary

Three OpenAI speakers argue that far from making engineers obsolete, the current moment is a golden age for engineering, because the job was never about writing code but about judgment, taste, and problem selection. Romain Huet and Alexander Embiricos lay out OpenAI's product thesis for Codex — chat as the primary surface plus a collaborative hands-on UI, with the explicit goal of empowering rather than automating engineers — and make an unusually detailed case for building Codex as open layers (responses API, open-source harness, AGENTS.md, app server, plugins) that OpenAI itself dogfoods rather than a simplified developer copy. They then pitch 'value maxing' over token maxing, citing GPT-5.6 Terra at half the cost of 5.5-level intelligence, Luna at $1/$6 per million tokens, and 5.6 Sol on Cerebras at 750 tokens/sec. Peter Steinberger closes with the sharpest content: he no longer runs 10 terminals, he runs a long-lived manager agent that delegates to workers, and his personal bottleneck has migrated from tokens to compute to attention. Worth watching for the manager-of-agents architecture and the openness-as-strategy argument; the first third is largely conference framing.

## Key Points

- Model release cadence at OpenAI has gone from roughly one new model every 15 months to roughly every 6 weeks, and product velocity has followed.
- The speakers explicitly reject the automation framing: the product shape they are targeting maximally empowers engineers and preserves the user's feeling of mastery over the work.
- OpenAI's UI thesis is two modalities — a single chat entity you can ask for anything, plus a collaborative surface for inspecting and steering — and they argue a CLI can't host the collaborative half while an IDE gets the ordering backwards by starting with code instead of conversation.
- Codex is deliberately structured as forkable layers (models via the responses API, open-source harness, AGENTS.md, open-source app server, plugins), with capabilities like context compaction shipped into the public API first so external agents get the same primitives.
- The claim they most want remembered: OpenAI does not build one internal system and a simplified developer system — the VS Code extension and Codex app are built on the same app server they publish.
- 'Value maxing' rather than token maxing is the frame for cost: GPT-5.6 Terra delivers 5.5-level intelligence at half the cost, and Luna runs at $1 per million input and $6 per million output tokens.
- Speed changes the shape of agent use, not just latency: 750 tokens/sec on Cerebras means running five or six parallel approaches and picking the best in the time one answer used to take.
- Steinberger's central argument is that persistent context (server-side compaction), delegation, and automated triggers together close a loop where a long-running manager agent spawns workers, and the human reviews at the outer loop rather than watching code stream by.
- The binding constraint has moved from tokens to compute to attention, and attention is the one input you cannot buy more of — making where you spend it the key skill.
- The open problem the talk hands to the audience: models are advancing faster than the harnesses and organizations around them, and the local-vs-cloud distinction plus laptop-bound agents are artifacts to be designed away.

## Notable Quotes

> "You know, software ate the world. And then AI ate software. But now, what we're here to say is that the AI engineers are eating the world."
>
> — [0:49](https://www.youtube.com/watch?v=pMggiOb18tc&t=49s) &middot; *The talk's thesis statement and its rebuttal to the engineers-are-obsolete argument.*

> "engineering was never about writing code. Engineering has always been about solving problems for yourself and for other people as well."
>
> — [1:29](https://www.youtube.com/watch?v=pMggiOb18tc&t=89s) &middot; *States the definitional move the whole optimistic case rests on.*

> "we used to ship a new model every 15 months or so, and now it's about roughly every 6 weeks"
>
> — [2:10](https://www.youtube.com/watch?v=pMggiOb18tc&t=130s) &middot; *Concrete cadence number anchoring the acceleration claim.*

> "now Codex can do and agents can do any task that you can do on your own computer"
>
> — [3:57](https://www.youtube.com/watch?v=pMggiOb18tc&t=237s) &middot; *Marks the scope expansion from coding assistant to general computer-use agent.*

> "if you pick like a medium length computer task and you give me and the model the same amount of time to get that task done, probably at least in my case, the model will do a better job than me for the average task"
>
> — [5:27](https://www.youtube.com/watch?v=pMggiOb18tc&t=327s) &middot; *An unusually direct capability claim from a product lead, hedged to the average case.*

> "For us, the goal is squarely not to automate engineers."
>
> — [6:03](https://www.youtube.com/watch?v=pMggiOb18tc&t=363s) &middot; *The stated product principle others in the industry openly disagree with.*

> "some people think chat is dead. I think chat is underrated."
>
> — [6:32](https://www.youtube.com/watch?v=pMggiOb18tc&t=392s) &middot; *A contrarian position on interface design that cross-cuts many other talks.*

> "Mostly, you just want to talk and let them cook. And then every now and then, you want to dig in and really dig in all the way to the weeds of things"
>
> — [7:08](https://www.youtube.com/watch?v=pMggiOb18tc&t=428s) &middot; *The team analogy that justifies the two-modality UI.*

> "you can't really build that collaborative interface for any kind of work in a CLI. It's mostly chat."
>
> — [8:36](https://www.youtube.com/watch?v=pMggiOb18tc&t=516s) &middot; *Names the tradeoff behind shipping an app to a CLI-loving audience.*

> "in an IDE, the order is wrong and so you're starting with the code, but now it's time to transition to like working with teammates where you chat first and you dig in when you need it"
>
> — [8:36](https://www.youtube.com/watch?v=pMggiOb18tc&t=516s) &middot; *Specific, arguable critique of the IDE-first agent paradigm.*

> "Codex cannot be a closed product that only OpenAI can improve. So we've intentionally designed Codex as a set of layers that anyone can build on."
>
> — [9:39](https://www.youtube.com/watch?v=pMggiOb18tc&t=579s) &middot; *The openness strategy stated as a design constraint, not a marketing line.*

> "Codex needed a way to compact long contexts for long-running tasks and so we'll build that into the API. So that means your agents can use the same primitives that we built for ourselves."
>
> — [10:15](https://www.youtube.com/watch?v=pMggiOb18tc&t=615s) &middot; *Concrete example of the internal-first-then-API pattern.*

> "We're not building one system for Open AI and a second system that's simplified for developers. At every layer, we actually use the thing that we give to you."
>
> — [13:12](https://www.youtube.com/watch?v=pMggiOb18tc&t=792s) &middot; *The single takeaway the speaker explicitly flags as the section's point.*

> "at only $1 per million input tokens and $6 per million output tokens. I'll leave it up to you to compare those costs, but that is insane value."
>
> — [15:29](https://www.youtube.com/watch?v=pMggiOb18tc&t=929s) &middot; *Hard pricing numbers for the cost-efficiency claim.*

> "this is GPT 5.6 Soul running on Cerebras, the frontier intelligence at now 750 tokens a second"
>
> — [15:29](https://www.youtube.com/watch?v=pMggiOb18tc&t=929s) &middot; *The headline throughput figure of the talk.*

> "the future shouldn't have this awkward distinction between like a local task and a cloud task, and you have to decide where to run everything"
>
> — [17:17](https://www.youtube.com/watch?v=pMggiOb18tc&t=1037s) &middot; *A forward-looking position on agent execution environments.*

> "I thought I was orchestrating. Really, I was polling. I was the scheduler, the router, and the memory."
>
> — [19:19](https://www.youtube.com/watch?v=pMggiOb18tc&t=1159s) &middot; *The sharpest reframing of multi-terminal agent workflows in the talk.*

> "I manage the manager of a small company of agents."
>
> — [19:19](https://www.youtube.com/watch?v=pMggiOb18tc&t=1159s) &middot; *One-line statement of the delegation architecture being advocated.*

> "So, we have persistent context, delegation, and triggers. There's your loop."
>
> — [20:14](https://www.youtube.com/watch?v=pMggiOb18tc&t=1214s) &middot; *Names the three ingredients as a reusable recipe.*

> "last year, I was primarily constrained by tokens. Now, I fixed that by joining OpenAI. I know I know the strategy does not scale."
>
> — [20:14](https://www.youtube.com/watch?v=pMggiOb18tc&t=1214s) &middot; *Self-aware framing of the moving-bottleneck argument.*

> "Now, I'm primarily constrained by attention. And unlike tokens or compute, I can't simply add more of it."
>
> — [21:16](https://www.youtube.com/watch?v=pMggiOb18tc&t=1276s) &middot; *The conclusion of the bottleneck progression and the talk's practical thesis.*

> "the latest generation of models is so good at understanding intent that it's a little bit of a waste of time to watch the agent generate code"
>
> — [21:16](https://www.youtube.com/watch?v=pMggiOb18tc&t=1276s) &middot; *Direct, checkable advice that contradicts common supervise-the-agent practice.*

> "The agent runs the inner execution loop. I set the direction and I make decisions in the outer loop."
>
> — [22:03](https://www.youtube.com/watch?v=pMggiOb18tc&t=1323s) &middot; *Cleanest statement of the human-agent division of labor.*

> "The manager shouldn't be a session trapped inside your app. It should be an agent that I can text, steer from Slack, or hear from wherever I am."
>
> — [23:57](https://www.youtube.com/watch?v=pMggiOb18tc&t=1437s) &middot; *Specifies what current harnesses are missing.*

> "Models are advancing faster than the harnesses and organizations around them. Designing those things is the next engineering problem."
>
> — [23:57](https://www.youtube.com/watch?v=pMggiOb18tc&t=1437s) &middot; *The call to action and the talk's framing of where value now accrues.*

## Positions

- AI will not eliminate engineers; engineering was always about problem-solving and judgment rather than writing code, so this is a return to its roots. ([1:29](https://www.youtube.com/watch?v=pMggiOb18tc&t=89s), confidence: stated)
- OpenAI ships a new model roughly every 6 weeks, down from roughly every 15 months. ([2:10](https://www.youtube.com/watch?v=pMggiOb18tc&t=130s), confidence: stated)
- For an average medium-length computer task given equal time, the model will do a better job than the speaker. ([5:27](https://www.youtube.com/watch?v=pMggiOb18tc&t=327s), confidence: stated)
- The right product goal is to maximally empower engineers, explicitly not to automate them. ([6:03](https://www.youtube.com/watch?v=pMggiOb18tc&t=363s), confidence: stated)
- Chat is underrated rather than dead, and should be the primary agent interface with a hands-on collaborative surface as the secondary one. ([6:32](https://www.youtube.com/watch?v=pMggiOb18tc&t=392s), confidence: stated)
- A CLI cannot host a genuinely collaborative interface for arbitrary work, and an IDE gets the ordering wrong by starting with code instead of conversation. ([8:36](https://www.youtube.com/watch?v=pMggiOb18tc&t=516s), confidence: stated)
- Agent platforms should be built as forkable open layers because a closed product that only its vendor can improve will lose. ([9:39](https://www.youtube.com/watch?v=pMggiOb18tc&t=579s), confidence: stated)
- OpenAI uses the same models, API, harness, and app server internally that it ships to developers, with no simplified second system. ([13:12](https://www.youtube.com/watch?v=pMggiOb18tc&t=792s), confidence: stated)
- GPT-5.6 Terra delivers GPT-5.5-level intelligence at half the cost, and Luna runs at $1 per million input and $6 per million output tokens. ([14:53](https://www.youtube.com/watch?v=pMggiOb18tc&t=893s), confidence: stated)
- GPT-5.6 Sol runs on Cerebras at 750 tokens per second, roughly a substantial PR in 10 seconds. ([15:29](https://www.youtube.com/watch?v=pMggiOb18tc&t=929s), confidence: stated)
- High throughput matters mainly because it enables running five or six parallel approaches and selecting the best, not because a single answer arrives faster. ([16:07](https://www.youtube.com/watch?v=pMggiOb18tc&t=967s), confidence: stated)
- The local-task versus cloud-task distinction should disappear; the agent should choose its own environment. ([17:17](https://www.youtube.com/watch?v=pMggiOb18tc&t=1037s), confidence: stated)
- Server-side compaction, coordination, and automated triggers are the three changes that made a persistent manager-agent workflow viable. ([19:19](https://www.youtube.com/watch?v=pMggiOb18tc&t=1159s), confidence: stated)
- Watching agents generate code is now largely a waste of time because current models understand intent well enough not to need live steering. ([21:16](https://www.youtube.com/watch?v=pMggiOb18tc&t=1276s), confidence: stated)
- Attention, not tokens or compute, is now the binding constraint on agent-assisted engineering. ([21:16](https://www.youtube.com/watch?v=pMggiOb18tc&t=1276s), confidence: stated)
- Neither Codex's cross-host work movement nor Open Claw's gateway-and-nodes model is the final form for untethering agents from a laptop. ([23:01](https://www.youtube.com/watch?v=pMggiOb18tc&t=1381s), confidence: stated)
- Harness and organizational design, not model capability, is the current bottleneck and the next engineering problem. ([23:57](https://www.youtube.com/watch?v=pMggiOb18tc&t=1437s), confidence: stated)
- Connecting an agent to the context before coding and to review and deploy afterward is what lets it begin and land substantially more work. ([4:30](https://www.youtube.com/watch?v=pMggiOb18tc&t=270s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [code review bottlenecks](../concepts/code-review-bottlenecks.md)
- [context compaction](../concepts/context-compaction.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)

