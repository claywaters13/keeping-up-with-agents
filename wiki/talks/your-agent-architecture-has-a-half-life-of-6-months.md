---
title: "Your agent architecture has a half-life of 6 months"
type: "talk"
slug: "your-agent-architecture-has-a-half-life-of-6-months"
track: "Agent & Harness Engineering"
org: "CTO, Inngest"
day: "Day 3 — Session Day 2"
room: "Expo Stage 1 NE"
video_id: "X1kp-ABIIxQ"
duration_sec: 1160
word_count: 2919
speakers: ["Dan Farrelly"]
---

# Your agent architecture has a half-life of 6 months

**Speakers:** [Dan Farrelly](../speakers/dan-farrelly.md)

**Org:** CTO, Inngest

**Track:** Agent & Harness Engineering &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Expo Stage 1 NE &nbsp;|&nbsp; **Duration:** 19m 20s

[Watch on YouTube](https://www.youtube.com/watch?v=X1kp-ABIIxQ)

## Summary

Dan Farrelly (CTO of Inngest) argues that agent architectures decay fast because teams couple layers that change at wildly different rates, and offers a three-layer mental model as the fix: an execution layer (the brain: flow, state, durability, retries), a context layer (models, prompts, tools, memory — the fastest-changing), and a compute layer (sandboxes, browsers, runtimes). His thesis is that prompts have a half-life of weeks and models of months, but a well-designed execution layer can last years — so that's the layer worth investing in and the one to keep decoupled from everything else. He specifies what an execution layer must provide: resumability with durable state stored outside the work, flexible invocation primitives (crons, events, APIs, human-in-the-loop, sub-agents, sync/async/delayed), and full-session observability from trigger through the whole stack. He walks through a concrete three-function self-improving loop (cron health check → triage agent → weekly reviewer) to show why emerging patterns like background agents and autonomous loops break frameworks designed even three months ago. Worth watching if you're deciding how much orchestration to build yourself versus inherit from a framework, or wondering where to instrument outcome-based agent scoring — though the last few minutes are an Inngest pitch.

## Key Points

- Agent architectures should be reasoned about as three conceptual layers — execution (brain), context (knowledge), and compute (hands) — rather than as component diagrams.
- Each layer has a different half-life: prompts decay in weeks, models in months, but execution can last years if designed correctly, and coupling them lets the fastest-decaying layer drag the rest down.
- The execution layer is defined as the system responsible for running code reliably and managing how, when, and whether each piece of work completes, independent of underlying infrastructure.
- Resumability requires that state be durable and external — a three-hour agent run cannot hold state in memory or on disk, or a failure at step 38 forces a restart that burns tokens, cost, and completed work.
- An execution layer must support mixed invocation patterns (crons, events, APIs, human-in-the-loop, sub-agents, synchronous, asynchronous, delayed), otherwise harness logic starts absorbing queues, workers, polling, backoff, and scheduling.
- Using sandboxes for durability, snapshots, or state is an anti-pattern because sandboxes are ephemeral and stateless by design; the execution layer should supply the sandbox's context, sequence, and durability.
- Observability must cover the entire session trace — database errors, permission issues, triggers, performance — not just LLM and tool calls, and traces must be inspectable by both humans and agents.
- Because user input, feedback, actions, and session results all flow through the execution layer, it is the natural hub for instrumenting outcome-based scores (did a PR get opened, was the research report saved) rather than thumbs up/thumbs down.
- Emerging patterns — background agents, dynamic workflows, autonomous loops, agent factories — are all long-running, asynchronous, and delegated, and frameworks from three months ago were not designed for them.

## Notable Quotes

> "So speaking of building agents if you've been building agents for more than 6 months, you've likely rewritten something, maybe more than once."
>
> — [1:04](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=64s) &middot; *States the talk's premise in one line.*

> "Some parts of your code likely survives. But did they survive by accident?"
>
> — [1:04](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=64s) &middot; *The framing question that sets up intentional architecture versus drift.*

> "So, in my opinion, there are three discrete layers. First, the execution layer. I think of this as the brain. It's where flow, state, durability, retries happen."
>
> — [2:42](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=162s) &middot; *The core mental model of the talk.*

> "This is models, prompts, tools, memory. This is the layer that changes the most."
>
> — [2:42](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=162s) &middot; *Identifies the context layer as the volatile one.*

> "So, prompts last weeks, if you're lucky, maybe maybe a single week. Uh the models that you use, months, again, if you're lucky. Uh but I think that execution can last years, if you do it right."
>
> — [3:37](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=217s) &middot; *The half-life numbers the entire argument rests on.*

> "And what happens then is that one layer's half-life kind of leaks and drags the other components down. You're building it's technical debt by another name."
>
> — [3:37](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=217s) &middot; *Names the failure mode of coupling layers.*

> "So, my thesis is think in layers. Decouple them. So, let's talk about what I mean."
>
> — [4:24](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=264s) &middot; *The thesis stated explicitly.*

> "But I think in a lot of these situations, the abstractions either are not there at all or they're too high-level or the layers merge."
>
> — [4:24](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=264s) &middot; *A direct critique of frameworks, pre-built harnesses, and custom rolls alike.*

> "And I define it as the execution layer as being the system responsible for running your code reliably, managing how, when, or whether each piece of work completes."
>
> — [5:49](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=349s) &middot; *The talk's working definition of its central term.*

> "You can swap the model, swap the context, swap the sandbox, the execution layer should be able to remain the same."
>
> — [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s) &middot; *The decoupling test in one sentence.*

> "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
>
> — [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s) &middot; *A concrete, checkable engineering constraint.*

> "So, if you can't see the entirety of a trace from the trigger through the whole stack, it's really hard to debug it, let alone improve your agent and keep evolving it."
>
> — [9:08](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=548s) &middot; *Ties observability scope to iteration speed, not just debugging.*

> "So, using it for durability, snapshots, or something in state, I think is an anti-pattern."
>
> — [9:57](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=597s) &middot; *A clear, contestable stance on sandbox usage.*

> "So, I think of the sandbox as the hands and execution as the brain."
>
> — [9:57](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=597s) &middot; *Compact statement of the compute/execution division of labor.*

> "They're all long-running. They're asynchronous. They're delegated. That means that you need to be able to observe them all uh down to the core."
>
> — [10:46](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=646s) &middot; *Characterizes what the emerging architectures have in common.*

> "It's going to have maybe hundreds of calls to you know, maybe 200 tool calls. You're going to probably guarantee to have at least one failure in that."
>
> — [11:35](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=695s) &middot; *Puts a number on why resumability is not optional for background agents.*

> "So, the frameworks of 3 months ago were not designed to handle this. Right? Like you're going to need to design these systems yourself."
>
> — [12:27](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=747s) &middot; *The talk's sharpest claim against existing frameworks.*

> "the middle of the execution layer, when your agent is running, is a key place to instrument and score your agents"
>
> — [16:28](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=988s) &middot; *Locates evaluation instrumentation at a specific architectural layer.*

> "Instead of a thumbs up, thumbs down, it's like did we open the PR, right? If it's a research agent, was this research saved? Was it a good report?"
>
> — [18:02](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=1082s) &middot; *Concrete alternative to explicit-feedback scoring.*

> "And I think if you can get your execution layer right and think about the right primitives, everything else can quickly evolve around it."
>
> — [18:02](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=1082s) &middot; *The closing summary of the investment argument.*

## Positions

- Prompts have a useful lifetime of weeks, models of months, but a well-designed execution layer can last years. ([3:37](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=217s), confidence: stated)
- Most teams couple their execution, context, and compute layers together, which causes the shortest-lived layer to force rewrites of the others. ([3:37](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=217s), confidence: stated)
- The execution layer is the stable layer worth investing engineering effort in, and getting it right prevents rewriting large components every six months. ([5:10](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=310s), confidence: stated)
- A correctly architected system lets you swap the model, context, or sandbox without changing the execution layer. ([6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s), confidence: stated)
- A three-hour agent run cannot keep its state in memory or on disk; state must be durable and external to the work. ([6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s), confidence: stated)
- Manual checkpointing and log-based state rehydration are inadequate because those abstractions leak into other layers of the harness. ([7:32](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=452s), confidence: stated)
- Without flexible orchestration primitives, harness logic ends up absorbing queues, workers, polling, backoff, and scheduling, producing bad abstractions. ([8:13](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=493s), confidence: stated)
- Observability must span the full session trace including database errors, permissions issues, triggers, and performance — not just LLM and tool calls. ([9:08](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=548s), confidence: stated)
- Using a sandbox for durability, snapshots, or state is an anti-pattern because sandboxes are ephemeral and stateless by design. ([9:57](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=597s), confidence: stated)
- A background agent making on the order of 200 tool calls will almost certainly experience at least one failure. ([11:35](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=695s), confidence: stated)
- Agent execution traces need to be inspectable by agents, not only by humans, so that reviewer functions can evaluate what was executed. ([10:46](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=646s), confidence: stated)
- Frameworks from three months ago were not designed for loop and background-agent architectures, so teams must design these systems themselves. ([12:27](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=747s), confidence: stated)
- The execution layer is the ideal hub for observability and agent scoring because user input, feedback, actions, and session results all flow through it. ([15:43](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=943s), confidence: stated)
- Outcome-based signals such as whether a PR was opened or a report was saved are better evaluation data than thumbs up/thumbs down feedback. ([18:02](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=1082s), confidence: implied)
- A useful self-improving agent loop can be built from as few as three functions: a scheduled health check, a triage agent, and a periodic reviewer. ([14:59](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=899s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [background agents](../concepts/background-agents.md)
- [durable execution](../concepts/durable-execution.md)
- [rubric design](../concepts/rubric-design.md)

