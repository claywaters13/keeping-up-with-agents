---
title: "Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster"
type: "talk"
slug: "velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster"
track: "Agentic Engineering"
org: "Ref."
day: "Day 4 — Session Day 3"
room: "Track 8"
video_id: "Kz4QJmNrVXU"
duration_sec: 1237
word_count: 3867
speakers: ["Matt Dailey"]
---

# Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster

**Speakers:** [Matt Dailey](../speakers/matt-dailey.md)

**Org:** Ref.

**Track:** Agentic Engineering &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 20m 37s

[Watch on YouTube](https://www.youtube.com/watch?v=Kz4QJmNrVXU)

## Summary

Matt Dailey, CEO of Ref., argues that AI-accelerated individual engineers create a team-level pathology he calls 'velocity sickness' — the stress of sudden output increases that produces output without impact. He diagnoses four symptoms (too many PRs, moving in many directions at once, 'declaring agent bankruptcy' each morning, and critical decisions being made by agents rather than humans) and traces them to a tooling mismatch: IDEs and chat interfaces were built for the implementation phase, which agents have now largely absorbed. His proposed fix is a 'decision layer' built around durable, shared docs rather than isolated ephemeral chats — separating the agent as action from the doc as state, so agents become stateless and start from the same shared context. The payoff he claims is easier code review (alignment moved earlier), no agent bankruptcy, a durable decision log, and a shift from code velocity to idea velocity. Watch this if you manage or work on a team where individual AI adoption is outpacing collective throughput; it's a short, concrete, opinionated framing with three immediately actionable practices, though it's also a pitch adjacent to the speaker's product.

## Key Points

- Velocity sickness is defined as the stress caused by sudden output increases thanks to AI, affecting individuals or teams, with the result being output without impact.
- The four symptoms Dailey names are too many PRs to merge, moving in many directions at once, declaring agent bankruptcy, and critical decisions being made by agents.
- He treats agents making critical decisions as the most important problem, because ceding decisions means ceding ownership of the code and ultimately of the product.
- The shape of engineering work has changed from plan-implement-polish done by a human to planning and polish by humans with implementation absorbed by agents, but tools like the IDE were built for the implementation phase.
- Chats are the wrong primitive for the decision layer because they are isolated, ephemeral, and 'brain off'; docs surface key decisions and make them durable and shareable.
- The core conceptual flip is separating agent-as-action from doc-as-state, so agents are effectively stateless and every new agent starts from the same engineered context.
- A healthy sign of adoption is people writing plans they then choose not to implement — evidence they are exploring the idea maze and prioritizing rather than falling into prototype gravity.
- Moving alignment earlier makes code review simpler because the hardest part of review — deciding what actually matters — has already been settled up front.
- The three concrete takeaways are: think of your work as two gears (planning and polish) and notice which one you're in, treat your plan as a portal to the software system, and share your plan with a human teammate rather than only with an agent.

## Notable Quotes

> "The problem we work on at Ref is one you might be familiar with where individual engineers are going really fast with AI, but the team as a whole is not."
>
> — [0:12](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=12s) &middot; *States the talk's core premise: the bottleneck has moved from the individual to the team.*

> "This is uh the stress caused by sudden output increases thanks to AI."
>
> — [3:22](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=202s) &middot; *The definition of the talk's titular term.*

> "Um it affects individuals or teams. Um and the result is output without impact."
>
> — [4:00](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=240s) &middot; *The one-line diagnosis the rest of the talk works from.*

> "if if you as an engineer are letting an agent make a critical decision, you are seeding control of your code. You are no longer the owner of that code. The agent is."
>
> — [3:22](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=202s) &middot; *The strongest normative claim in the talk, and the one most likely to be contested.*

> "it feels like you're doing a lot of work but you're doing the same work and you're spending tokens twice."
>
> — [2:41](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=161s) &middot; *Names the concrete cost of agent bankruptcy in both time and tokens.*

> "This is a person who's writing a lot, but those pages that they're writing are going unread."
>
> — [5:20](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=320s) &middot; *The anecdote that makes 'output without impact' visceral outside of engineering.*

> "our IDE, our workhorse, um it was built for implementation and polish to be done by an individual, to be heads down building as a software engineer writing code."
>
> — [7:06](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=426s) &middot; *The tooling-mismatch argument in one sentence.*

> "This is like arguably should not even be on this slide cuz it's not our human work anymore. It's done by the agent."
>
> — [7:42](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=462s) &middot; *Stakes out a strong position that implementation has left the human workflow entirely.*

> "The skill now is what gear am I in? Am I using the appropriate tools for the gear that I'm what I'm trying to accomplish right now."
>
> — [9:25](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=565s) &middot; *Reframes the core engineering skill under AI as tool-context selection.*

> "It'd be a tool built for docs and not chat."
>
> — [9:25](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=565s) &middot; *The talk's central prescription, stated as a slogan.*

> "The problem with chats is that they are the relic of building for implementation. So they're they're default isolated and ephemeral and and brain off."
>
> — [10:03](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=603s) &middot; *The critique of chat as a primitive, which underpins the doc-centric proposal.*

> "Our work now is figure out what decisions matter and then make those decisions and then get out of the way while the agents fill in the rest."
>
> — [10:53](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=653s) &middot; *A compact statement of the new division of labor between humans and agents.*

> "If you were If you think back to being a manager or a lead on a team before AI, if your team was having struggling with alignment, you would not tell them like, "Let's go all work in Slack DMs.""
>
> — [11:32](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=692s) &middot; *The analogy that makes the case against chat-as-alignment-medium intuitive.*

> "Plan mode is great, but it's largely a a rich chat message where the agent is saying, "Hey, here's a like better visualization of what I'm trying to express to you.""
>
> — [12:09](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=729s) &middot; *Explicitly differentiates his proposal from plan mode and spec-driven development.*

> "What you want is to separate the the agent as the action and the doc as the state."
>
> — [13:21](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=801s) &middot; *The architectural insight the whole approach rests on.*

> "You're ultimately doing context engineering in this doc, so that every agent is largely stateless and starts from this place um the same place."
>
> — [13:21](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=801s) &middot; *Connects the doc-centric workflow to context engineering as a practice.*

> "the first thing we see happen actually is that people start to plan and then not implement their plan. Uh and this is actually like a really good sign."
>
> — [14:08](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=848s) &middot; *A counterintuitive adoption metric — abandoned plans as evidence of health.*

> "One way I like to frame this is that you're you're shifting from code velocity to idea velocity."
>
> — [14:44](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=884s) &middot; *The talk's summary reframe of what velocity should mean post-AI.*

> "the code review is easier because the hardest part of any code review is, you know, what actually matters here."
>
> — [15:58](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=958s) &middot; *Names the specific mechanism by which earlier alignment reduces review load.*

> "declaring agent bankruptcy is just not a thing because you've made your agent stateless."
>
> — [16:38](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=998s) &middot; *Direct claim linking the doc-as-state design to elimination of a named failure mode.*

> "I think the future of engineering is multiplayer. It's going to be multi multiplayer by default sooner than we think."
>
> — [17:59](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=1079s) &middot; *A forward-looking prediction that others in the field might dispute.*

> "Give it to someone on your team. This is like, I feel like very unnatural for a lot of people."
>
> — [19:18](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=1158s) &middot; *The most actionable and least tool-dependent takeaway.*

## Positions

- AI adoption increases individual engineer output without a corresponding increase in team output, producing output without impact. ([4:00](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=240s), confidence: stated)
- An engineer who lets an agent make a critical decision has ceded ownership of that code to the agent. ([3:22](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=202s), confidence: stated)
- Implementation is no longer human work; it belongs to the agent. ([7:42](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=462s), confidence: stated)
- The IDE is a tool built for a style of work (heads-down individual implementation and polish) that no longer matches how engineers work. ([7:06](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=426s), confidence: stated)
- Chat is the wrong medium for the decision layer because it is isolated, ephemeral, and encourages accepting the agent's recommended option without thinking. ([10:03](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=603s), confidence: stated)
- Plan mode is insufficient because it is still a rich chat message inside an isolated ephemeral environment rather than a durable shared artifact. ([12:09](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=729s), confidence: stated)
- Spec-driven development operates at the product/behavior level and is too far removed from engineering reality to serve as the decision layer. ([12:09](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=729s), confidence: stated)
- Separating agent-as-action from doc-as-state makes agents effectively stateless and eliminates the need to declare agent bankruptcy. ([16:38](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=998s), confidence: stated)
- Moving alignment earlier in the process makes code review simpler because the hardest part of review is determining what matters. ([15:58](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=958s), confidence: stated)
- Writing plans that never get implemented is a positive signal, because it means ideas are being explored and prioritized rather than built by default. ([14:08](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=848s), confidence: stated)
- Extracting decisions into durable docs up front is superior to having an LLM summarize sessions after the fact, which risks picking the wrong things. ([17:12](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=1032s), confidence: stated)
- Engineering will become multiplayer by default sooner than most people expect. ([17:59](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=1079s), confidence: stated)
- Because agent-era work is more creative, engineers should collaborate more with each other, not less. ([17:59](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=1079s), confidence: stated)
- Sharing a plan with a human teammate before implementation yields feedback valuable enough to justify the discomfort of doing so. ([19:18](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=1158s), confidence: stated)

## Concepts

- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [code review bottlenecks](../concepts/code-review-bottlenecks.md)
- [cognitive debt](../concepts/cognitive-debt.md)
- [context engineering](../concepts/context-engineering.md)
- [parallel agent execution](../concepts/parallel-agent-execution.md)
- [session management](../concepts/session-management.md)
- [spec-driven development](../concepts/spec-driven-development.md)

