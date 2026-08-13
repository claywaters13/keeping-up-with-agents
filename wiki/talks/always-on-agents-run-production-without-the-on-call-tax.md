---
title: "Always-on agents run production without the on-call tax"
type: "talk"
slug: "always-on-agents-run-production-without-the-on-call-tax"
track: "Agentic Engineering"
org: "Resolve AI"
day: "Day 4 — Session Day 3"
room: "Track 8"
video_id: "vSx5IULvBns"
duration_sec: 1496
word_count: 5207
speakers: ["Justin Smith"]
---

# Always-on agents run production without the on-call tax

**Speakers:** [Justin Smith](../speakers/justin-smith.md)

**Org:** Resolve AI

**Track:** Agentic Engineering &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 24m 56s

[Watch on YouTube](https://www.youtube.com/watch?v=vSx5IULvBns)

## Summary

Justin Smith, a founding product engineer at Resolve AI, argues that the first wave of AI coding has shifted the bottleneck from writing code to running it: PRs are bigger and more frequent, sometimes authored by people who don't understand the system, and production complexity is growing faster than the operational structures around it. His answer is to use AI inside production — specifically always-on background agents that handle the long tail of operational work that never shows up in a job description: deployment monitoring, scheduled health checks, on-call handoff reports, and first-responder answers to Slack questions. The central technical claim is that execution (calling tools, loading dashboards) is the easy half; the hard and differentiating half is production context — knowing that a metric 'smells off' — which requires a persistent learning/knowledge system that keeps up as the environment evolves. He demos an agent that reads a GitHub release tag, reasons about what changed, and builds a release-specific monitoring plan (including downstream causal chains like a Kafka pipeline) rather than running fixed CI/CD checks, then re-checks on its own schedule over hours or days. Worth watching if you're thinking about agents that live in Slack and operate systems continuously, rather than agents you prompt.

## Key Points

- A cited survey found roughly 70% of an engineer's time goes not to writing code but to running it in production — maintaining platforms, scaling infra, debugging incidents, on-call, hot fixes, run books, and escalations.
- AI coding assistance increases change velocity and therefore production issues, so the response has to be AI operating inside production, not just AI writing code.
- A task decomposes into execution plus production context, and Resolve's position is that production context is the more important and harder half — execution can load a dashboard, but context tells you the metric looks wrong.
- Models are already capable enough; the binding constraint is a learning system that captures how your specific environment, services, and causal chains work and keeps growing as the system evolves.
- Background agents cover the long tail of operational work that has no ceremony attached — deploy watching, morning digests, unpaged P99 drift, capacity reports, recurring health checks.
- Agents can be triggered four ways — schedules, recurring events, event streams (CI/CD, Slack), and direct messages — and run always-on in a cloud sandbox with a file system, so closing your laptop doesn't matter.
- For deployments, the agent inspects what actually changed and builds a customized, per-release check plan with a self-chosen re-check cadence (another hour, or back in three days), explicitly not replacing existing CI/CD but patching its gaps — including unmonitored feature flags and infra changes.
- The intended surface area is where engineers already work: Slack or MS Teams as a first-party experience, with agents that passively watch channels, decide whether they have enough confidence to answer, and can DM a human to confirm before replying publicly.
- Agent tasks are set up conversationally and are editable in-thread — telling the agent 'this is too verbose, make it shorter' updates the underlying recurring task for future runs.

## Notable Quotes

> "70% of the time from an engineer is actually not just like is not focused just on writing code. It's actually spent on actually running the code that is actually shipped into production."
>
> — [1:32](https://www.youtube.com/watch?v=vSx5IULvBns&t=92s) &middot; *The load-bearing statistic the whole talk is built on.*

> "So, really coding was never the the the big bottleneck"
>
> — [2:19](https://www.youtube.com/watch?v=vSx5IULvBns&t=139s) &middot; *One-line thesis reframing the first wave of AI coding tools.*

> "AI is creating a lot more issues in production as, you know, AI code sort of goes through. Um it's not clear we have the right sort of um structures in place to deal with the amount of kind of changes that are coming through."
>
> — [2:19](https://www.youtube.com/watch?v=vSx5IULvBns&t=139s) &middot; *States the causal link between coding velocity and operational risk.*

> "unlimited tokens is is sort of coming to an end, the the token max, right?"
>
> — [2:19](https://www.youtube.com/watch?v=vSx5IULvBns&t=139s) &middot; *A concrete market prediction about AI cost discipline.*

> "we need full stack AI. It's not just about the models anymore, it's about the context around the models and what the models can do inside of a specific domain."
>
> — [2:51](https://www.youtube.com/watch?v=vSx5IULvBns&t=171s) &middot; *Names the shift from model capability to context and domain scope.*

> "the answer is, well, you got to use AI inside of production to deal with um sort of the the amount of increase of complexity that AI is kind of putting into your product or into your system."
>
> — [3:27](https://www.youtube.com/watch?v=vSx5IULvBns&t=207s) &middot; *The talk's central prescription, stated plainly.*

> "models have gotten incredi- incredibly capable over the last um year, let's say, right? But especially over the last like 6 months or so."
>
> — [6:19](https://www.youtube.com/watch?v=vSx5IULvBns&t=379s) &middot; *Sets up the argument that models aren't the constraint.*

> "the idea of understanding, like truly understanding your environment um and the way that your services interact and where the hotspots are, keeping track of all of that sort of understanding is incredibly difficult."
>
> — [6:19](https://www.youtube.com/watch?v=vSx5IULvBns&t=379s) &middot; *Identifies environment understanding, not reasoning, as the hard problem.*

> "It has to have an underlying sort of learning system to be able to capture that knowledge um and that sort of understanding of how your system operates."
>
> — [6:59](https://www.youtube.com/watch?v=vSx5IULvBns&t=419s) &middot; *States the architectural requirement behind the product.*

> "A task is just execution and the context to understand how to actually execute the task."
>
> — [10:07](https://www.youtube.com/watch?v=vSx5IULvBns&t=607s) &middot; *The definitional frame for the rest of the talk.*

> "it's one thing to go check a dashboard. It's another thing to say that metric smells off."
>
> — [10:07](https://www.youtube.com/watch?v=vSx5IULvBns&t=607s) &middot; *The clearest articulation of the execution-vs-context tradeoff.*

> "You need the execution engine, that's great, but you really need that production context that tells you is this important or not important."
>
> — [10:48](https://www.youtube.com/watch?v=vSx5IULvBns&t=648s) &middot; *Explicitly ranks context above execution for background agents.*

> "Always runs. It's in the cloud. Um, so if you close your laptop, it's okay. Um, runs inside of a sandbox, so it has kind of a file system underneath it."
>
> — [12:16](https://www.youtube.com/watch?v=vSx5IULvBns&t=736s) &middot; *Concrete runtime design choice distinguishing background from interactive agents.*

> "any change inside of your environment is an opportunity for something to go wrong."
>
> — [13:25](https://www.youtube.com/watch?v=vSx5IULvBns&t=805s) &middot; *The operating principle behind deployment monitoring as the flagship use case.*

> "Often times you have change systems that you're not piping through a CICD system like a feature flag or maybe some infra changes that might happen which maybe don't get any monitoring at all."
>
> — [14:05](https://www.youtube.com/watch?v=vSx5IULvBns&t=845s) &middot; *Names a specific, checkable gap in standard CI/CD coverage.*

> "our goal is not to sit here and say, "We're going to replace an entire CI/CD pipeline."
>
> — [17:57](https://www.youtube.com/watch?v=vSx5IULvBns&t=1077s) &middot; *Deliberate scoping against a bigger claim competitors might make.*

> "it would be great if you had a single engineer just focused on like watching all the things on every release, but that's really expensive. There's a lot of cognitive load."
>
> — [18:31](https://www.youtube.com/watch?v=vSx5IULvBns&t=1111s) &middot; *The economic argument for automating deploy watching.*

> "it could decide, I want to wait for another hour cuz this type of issue might only hit every you know, every so often"
>
> — [19:01](https://www.youtube.com/watch?v=vSx5IULvBns&t=1141s) &middot; *Shows agent autonomy over timing rather than hard-coded intervals.*

> "It's not hard for me to go answer questions, but it's disrupting me and if I don't go answer it, um, they won't get an answer for a while."
>
> — [16:25](https://www.youtube.com/watch?v=vSx5IULvBns&t=985s) &middot; *Frames the real cost of Slack support as interruption, not difficulty.*

> "you can have an agent that basically will DM you to say, "I think I know the answer to this, but I'm not sure. Can you confirm this for me before I, you know, respond back?""
>
> — [16:56](https://www.youtube.com/watch?v=vSx5IULvBns&t=1016s) &middot; *A practical human-in-the-loop confidence pattern for public-facing agent replies.*

> "cost of operational work, it's not navigating uh, you know, it's it's it's not just in the task execution, it's in the environment complexity"
>
> — [23:51](https://www.youtube.com/watch?v=vSx5IULvBns&t=1431s) &middot; *The closing restatement of the talk's core claim.*

## Positions

- Engineers spend about 70% of their time running code in production rather than writing it, per a survey study. ([1:32](https://www.youtube.com/watch?v=vSx5IULvBns&t=92s), confidence: stated)
- Writing code was never the real engineering bottleneck; operating systems in production is. ([2:19](https://www.youtube.com/watch?v=vSx5IULvBns&t=139s), confidence: stated)
- AI-generated code is increasing the volume of production issues, and existing organizational structures are not equipped for the resulting change rate. ([2:19](https://www.youtube.com/watch?v=vSx5IULvBns&t=139s), confidence: stated)
- The era of effectively unlimited tokens is ending — prices are rising and companies are becoming more stringent about AI spend. ([2:19](https://www.youtube.com/watch?v=vSx5IULvBns&t=139s), confidence: stated)
- Model capability is no longer the limiting factor for production agents; capturing and maintaining an understanding of the specific environment is. ([6:19](https://www.youtube.com/watch?v=vSx5IULvBns&t=379s), confidence: stated)
- Production context matters more than execution capability for background agents. ([10:07](https://www.youtube.com/watch?v=vSx5IULvBns&t=607s), confidence: stated)
- Standard CI/CD checks are good baselines but are not exhaustive, because every rollout is unique and needs different signals watched. ([14:05](https://www.youtube.com/watch?v=vSx5IULvBns&t=845s), confidence: stated)
- Feature flags and infrastructure changes frequently bypass CI/CD and receive no monitoring at all. ([14:05](https://www.youtube.com/watch?v=vSx5IULvBns&t=845s), confidence: stated)
- AI agents should augment rather than replace existing CI/CD pipelines. ([17:57](https://www.youtube.com/watch?v=vSx5IULvBns&t=1077s), confidence: stated)
- An agent that dynamically reasons about what changed and builds a per-release check plan catches problems that fixed hard-coded checks and wait intervals miss. ([19:01](https://www.youtube.com/watch?v=vSx5IULvBns&t=1141s), confidence: implied)
- Agents should be embedded in the tools engineers already use, like Slack and MS Teams, rather than requiring people to visit a separate product UI. ([21:57](https://www.youtube.com/watch?v=vSx5IULvBns&t=1317s), confidence: stated)
- Every company's environment is unique enough that a generic agent cannot be effective without a per-customer knowledge system. ([23:11](https://www.youtube.com/watch?v=vSx5IULvBns&t=1391s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [background agents](../concepts/background-agents.md)
- [context engineering](../concepts/context-engineering.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [online evaluation](../concepts/online-evaluation.md)

