---
title: "Every Harness Will Become A Claw"
type: "talk"
slug: "every-harness-will-become-a-claw"
track: "Claws & Personal Agents"
org: "Mastra"
day: "Day 2 — Session Day 1"
room: "Track 1"
video_id: "8qWIPUia2O8"
duration_sec: 935
word_count: 2869
speakers: ["Sam Bhagwat"]
---

# Every Harness Will Become A Claw

**Speakers:** [Sam Bhagwat](../speakers/sam-bhagwat.md)

**Org:** Mastra

**Track:** Claws & Personal Agents &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 15m 35s

[Watch on YouTube](https://www.youtube.com/watch?v=8qWIPUia2O8)

## Summary

Sam Bhagwat, co-founder/CEO of Mastra, argues that AI agents are ascending a spectrum — LLM → agent → harness → 'claw' — and that every harness will eventually expand into a claw: an always-on, initiative-taking, self-improving agent. He walks through the capability layers that mark each step: the agent loop, tool calls and memory for agents; durability, planning mode, parallel subagents, autocompaction and resumable threads for harnesses; and heartbeats, multi-channel messaging (Slack, WhatsApp, Telegram), external feed listening, and continual learning for claws. He also covers the in-progress shift from local to cloud harnesses running in sandboxes and opening PRs. The second half is a market prediction: drawing on the 2010s mobile app platform shakeout, he argues that consumer attention only supports one or two winners per category, and that harnesses that are neither economically valuable nor frequently used will be forgotten. Worth watching for a compact taxonomy of agent capability tiers plus a contrarian consolidation forecast.

## Key Points

- The agent-to-harness transition is defined by durability and 'doggedness' — running for hours or days rather than minutes, with persisted streams that can resume after a dropped connection.
- Harness-tier features include planning mode, parallel subagents, TUI affordances and slash commands, skills, dynamically created agents, background bash tasks, autocompaction on context-window exhaustion, thread persistence, and session-long tool approval.
- Queuing, steering, and interrupting mean the user is no longer blocked on turn-taking with the model — Bhagwat contrasts turn-based Civilization with real-time Starcraft.
- The local-to-cloud harness shift has happened largely in the last three months: harnesses that live in Slack with multiple colleagues, run in cloud sandboxes for greater parallelism, and produce GitHub PRs rather than local commits.
- The harness-to-claw step is about imbuing harnesses with initiative and learning: heartbeats that wake the agent on a schedule, listening to external feeds, messaging over multiple channels, a daemon/gateway for incoming and outgoing requests, and continual learning from traces.
- Automatic skill generation is a common form of continual learning, and agents may even modify the code driving them, but the industry has not settled on the right approach.
- 'Steinberger's law': every harness will expand until it becomes a claw, driven by technological, economic, and psychological forces — including users' desire for a 'dopamine casino' where tokens go in and code comes out.
- Bhagwat predicts a shakeout modeled on the 2010s mobile platform: categories consolidate to one or two winners because attention is scarce, and only products that are highly economically valuable or highly frequent survive.
- Practical advice for builders: keep pace with a 3-4x faster rate of change, ensure your agent has the capabilities users need or they will switch to something more powerful, and expect another shakeout wave in the later 2020s.

## Notable Quotes

> "I believe every harness will expand until it becomes a claw. and and and that's a little bit um technological, that's a little bit economic, that's a little bit psychological."
>
> — [9:35](https://www.youtube.com/watch?v=8qWIPUia2O8&t=575s) &middot; *The thesis of the talk, stated as a named law with its three drivers.*

> "there are different levels of self-driving autonomy whether that's like lane assist whether that's Tesla S FSD whether that's I I'm sitting in the back of my Whimo and there's nobody behind the steering wheel"
>
> — [1:32](https://www.youtube.com/watch?v=8qWIPUia2O8&t=92s) &middot; *Frames the whole talk's central analogy: agency as a spectrum, not a binary.*

> "durability just the sheer quality of like being able to run not for minutes but for hours or days"
>
> — [3:25](https://www.youtube.com/watch?v=8qWIPUia2O8&t=205s) &middot; *Gives the concrete operational definition separating a harness from an agent.*

> "You're not just blocked waiting on the LM. Hey, I take a turn and then you take a turn. I'm playing playing Civilization here and I can't take a turn until all the other civilizations are playing."
>
> — [4:03](https://www.youtube.com/watch?v=8qWIPUia2O8&t=243s) &middot; *Memorable framing of steering/interruption as a shift from turn-based to real-time interaction.*

> "yeah you can run all instances of rmrf for slash right that you see in the session even though the first one will probably wipe your machine"
>
> — [4:37](https://www.youtube.com/watch?v=8qWIPUia2O8&t=277s) &middot; *Names the safety tradeoff hiding inside session-long tool approval.*

> "This is always a trade-off and always something you get with distributed systems, right? You can do more in the cloud than you can do locally. You have more resources. It requires a different architecture."
>
> — [5:50](https://www.youtube.com/watch?v=8qWIPUia2O8&t=350s) &middot; *States the cloud-harness tradeoff explicitly rather than treating cloud as strictly better.*

> "I want to talk about what the harness to claw transition is, which is imbuing these agents, imbuing these harnesses with initiative and and learning"
>
> — [6:21](https://www.youtube.com/watch?v=8qWIPUia2O8&t=381s) &middot; *The talk's definition of what makes a claw a claw.*

> "It has a heartbeat which means it wakes up every you know defined amount of time and um and does something"
>
> — [6:54](https://www.youtube.com/watch?v=8qWIPUia2O8&t=414s) &middot; *Concrete mechanism behind the abstract notion of agent initiative.*

> "the agent the harness runs and then you know based on the traces that it generates it it sort of autoimproves itself and there's different ways of doing this."
>
> — [7:37](https://www.youtube.com/watch?v=8qWIPUia2O8&t=457s) &middot; *Defines continual learning operationally as trace-driven self-improvement.*

> "We haven't figured out what the right way of doing it is yet. We're still exploring you know the industry is still exploring options."
>
> — [8:17](https://www.youtube.com/watch?v=8qWIPUia2O8&t=497s) &middot; *Rare admission of open problem status on continual learning.*

> "a lot of folks want these features but they want them with power and control. They don't want to just put a you know a claw on a box right they want to have more."
>
> — [8:17](https://www.youtube.com/watch?v=8qWIPUia2O8&t=497s) &middot; *Articulates the framework vendor's positioning against turnkey claw products.*

> "We want this dopamine casino that we get when we put in tokens and get out code"
>
> — [10:15](https://www.youtube.com/watch?v=8qWIPUia2O8&t=615s) &middot; *The psychological driver of harness expansion, in the talk's most quotable phrase.*

> "the first thing that I've observed um that we've all observed um as a is that harnesses tend to expand. And they expand because we want them to expand."
>
> — [9:35](https://www.youtube.com/watch?v=8qWIPUia2O8&t=575s) &middot; *Locates the expansion force in user demand rather than vendor strategy.*

> "if you look at most of these kinds of categories, and there are quite a few categories, there really only like one or two, you know, logos here that we use"
>
> — [11:18](https://www.youtube.com/watch?v=8qWIPUia2O8&t=678s) &middot; *The historical evidence base for the consolidation prediction.*

> "there's sort of like it either has to be very economically valuable or has to be very frequent. And if it's neither one of the two, um we just forget about it"
>
> — [12:25](https://www.youtube.com/watch?v=8qWIPUia2O8&t=745s) &middot; *A checkable two-factor survival criterion builders can apply to their own product.*

> "I think that in the notsodistant future there will be this very real shakeout and and these categories will kind of emerge and we'll realize that we only have space in our lives for so many of these claws."
>
> — [13:38](https://www.youtube.com/watch?v=8qWIPUia2O8&t=818s) &middot; *The talk's main forward-looking prediction, stated plainly.*

> "if the rate of change increases 3 to 4x that means you know we need to figure out what's going on even more frequently"
>
> — [13:38](https://www.youtube.com/watch?v=8qWIPUia2O8&t=818s) &middot; *One of the few quantitative claims in the talk.*

> "make sure that it has the capabilities that your users need because if it doesn't and if there's newer things that come out, like they may just, you know, pick pick something that's more powerful because that that's happening very quickly"
>
> — [14:21](https://www.youtube.com/watch?v=8qWIPUia2O8&t=861s) &middot; *The actionable takeaway for builders, tying capability gaps to churn risk.*

> "even if you climb up to the top of the hill, keep in mind there's going to be another wave of this sort of these like this this shakeout coming. and you know probably sometime in the later 2020s."
>
> — [14:21](https://www.youtube.com/watch?v=8qWIPUia2O8&t=861s) &middot; *Puts a date range on the prediction, making it falsifiable.*

## Positions

- Every harness will expand until it becomes a claw — an always-on agent with initiative and learning. ([9:35](https://www.youtube.com/watch?v=8qWIPUia2O8&t=575s), confidence: stated)
- Durability — running for hours or days rather than minutes — is the defining property separating a harness from an agent. ([3:25](https://www.youtube.com/watch?v=8qWIPUia2O8&t=205s), confidence: stated)
- The industry has not yet determined the right approach to continual learning for agents. ([8:17](https://www.youtube.com/watch?v=8qWIPUia2O8&t=497s), confidence: stated)
- The shift from local harnesses to always-on cloud harnesses has happened primarily over the last three months and is still in progress. ([5:13](https://www.youtube.com/watch?v=8qWIPUia2O8&t=313s), confidence: stated)
- Cloud harnesses enable more parallelism than local machines but require a different architecture, a distributed-systems tradeoff. ([5:50](https://www.youtube.com/watch?v=8qWIPUia2O8&t=350s), confidence: stated)
- A consolidation shakeout will leave room for only one or two claws per category, mirroring the 2010s mobile app platform. ([13:38](https://www.youtube.com/watch?v=8qWIPUia2O8&t=818s), confidence: stated)
- Products survive consolidation only if they are either highly economically valuable or used very frequently; failing both means being forgotten. ([12:25](https://www.youtube.com/watch?v=8qWIPUia2O8&t=745s), confidence: stated)
- Another shakeout wave will arrive sometime in the later 2020s, even for current category leaders. ([14:21](https://www.youtube.com/watch?v=8qWIPUia2O8&t=861s), confidence: stated)
- Developers want claw-like capabilities delivered with power and control via a framework rather than as a prepackaged product. ([8:17](https://www.youtube.com/watch?v=8qWIPUia2O8&t=497s), confidence: stated)
- Agents are a broader category than coding agents, so the harness-to-claw dynamic is not limited to software development. ([10:15](https://www.youtube.com/watch?v=8qWIPUia2O8&t=615s), confidence: implied)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [context compaction](../concepts/context-compaction.md)
- [continual learning](../concepts/continual-learning.md)
- [durable execution](../concepts/durable-execution.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

