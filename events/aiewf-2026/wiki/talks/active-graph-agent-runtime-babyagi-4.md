---
title: "Active Graph Agent Runtime (BabyAGI 4)"
type: "talk"
slug: "active-graph-agent-runtime-babyagi-4"
track: "Graphs"
org: "Untapped Capital"
day: "Day 4 — Session Day 3"
room: "Track 5"
video_id: "khVX_BUnEwU"
duration_sec: 1054
word_count: 3684
speakers: ["Yohei Nakajima"]
---

# Active Graph Agent Runtime (BabyAGI 4)

**Speakers:** [Yohei Nakajima](../speakers/yohei-nakajima.md)

**Org:** Untapped Capital

**Track:** Graphs &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 17m 34s

[Watch on YouTube](https://www.youtube.com/watch?v=khVX_BUnEwU)

## Summary

Yohei Nakajima presents ActiveGraph (BabyAGI 4), an experimental open-source 'event-sourced graph runtime for building auditable agents.' Instead of building around the LLM and bolting on logging, ActiveGraph makes an immutable typed event log the ground truth; the log projects a graph state, and 'behaviors' react to graph changes and emit new events rather than calling each other directly. Policies gate which graph changes an agent can make unilaterally versus which need a proposed patch, a test, or a human in the loop, and the log design gives replay, rollback, and forking natively. He reports experiments using the log itself as memory on LongMemEval, self-modification loops that only accept patches that measurably improve accuracy, an 'ActiveGraph Lab' that researches itself, and a Pokémon TCG Kaggle deck agent tuned over ~80 passes. Worth watching if you care about auditable long-running agents, self-improvement loops, or blackboard-style architectures applied to LLM agents — and if you can tolerate an admittedly experimental, unintuitive programming model.

## Key Points

- ActiveGraph inverts the usual stack: rather than an LLM with tools, memory, and logging attached, the immutable typed event log is the source of truth and the graph state is a projection of that log.
- Both what the agent does and how the agent itself changes are flattened into one event log, on the argument that agent definitions change constantly and are usually tracked separately from agent activity.
- Behaviors — which may be deterministic or LLM-backed, and can live on nodes or edges — subscribe to graph changes and emit events; LLMs never talk to each other directly, only through shared state.
- Policies define which graph modifications are allowed outright versus which require a proposed patch, contradiction checks, or human approval, e.g. adding a research source is cheap but editing a prompt is gated.
- Context management is expressed as a graph query ('views') that exposes a subset of the graph to a given behavior.
- The design is explicitly a runtime, not a harness: ReAct and other common harnesses can be rebuilt on top of it, and capabilities are bundled as composable 'packs' (memory, tools, identity, chat) with object types, behaviors, and policies.
- Using the structured log directly as memory — embedding the query, retrieving nearby messages, no fact or entity extraction — scored well on LongMemEval, suggesting log and memory data largely overlap.
- Self-modification experiments used fork, static gate, sandbox gate, and measured accuracy before accepting a patch; loops ran 8–13 iterations and accepted only 4–5 patches, yielding modest but statistically significant LongMemEval gains.
- Nakajima hypothesizes AI writes ActiveGraph-style code well because decades of blackboard/Kafka shared-state literature is in training data, whereas LLM-agent patterns are only ~3 years old.
- He argues the harness will not disappear as models improve: long-running agents need an 'experiential world model' from their own log alongside a predictive world model.

## Notable Quotes

> "agents are awesome, but long-running agents break. And if they're so awesome, why am I still building them? Why they should build themselves."
>
> — [0:01](https://www.youtube.com/watch?v=khVX_BUnEwU&t=1s) &middot; *States the motivating problem and the self-improvement thesis in one breath.*

> "Let's build the simplest thing that can build itself has basically been kind of my research theme for the last 3 years since I did baby AGI back in March of 2023."
>
> — [0:01](https://www.youtube.com/watch?v=khVX_BUnEwU&t=1s) &middot; *Frames the whole three-year research program behind the talk.*

> "over the course of 3 years I've done nine iterations of baby AGI with less fanfare"
>
> — [0:52](https://www.youtube.com/watch?v=khVX_BUnEwU&t=52s) &middot; *Concrete number on the iteration history behind BabyAGI 4.*

> "ActiveGraph is an event-sourced graph runtime for building auditable agents."
>
> — [1:22](https://www.youtube.com/watch?v=khVX_BUnEwU&t=82s) &middot; *The one-line definition of the system.*

> "today most people build agents around the LLM. You start with the LLM, you add a response API, you give it tools, you add memory, and then you make sure you log everything correctly"
>
> — [2:00](https://www.youtube.com/watch?v=khVX_BUnEwU&t=120s) &middot; *Names the incumbent architecture the talk is arguing against.*

> "ActiveGraph asks, what if you build around the log?"
>
> — [2:00](https://www.youtube.com/watch?v=khVX_BUnEwU&t=120s) &middot; *The core inversion the entire talk rests on.*

> "Nobody here is using the same agent they were using a year ago, and the agent you're going to use a year from now is going to be different."
>
> — [2:00](https://www.youtube.com/watch?v=khVX_BUnEwU&t=120s) &middot; *Justifies logging agent changes, not just agent actions.*

> "let's flatten that down into a single immutable event log, and this is the ground truth of the agent"
>
> — [2:35](https://www.youtube.com/watch?v=khVX_BUnEwU&t=155s) &middot; *The central design commitment.*

> "LLMs don't talk to each other in ActiveGraph. They all communicate through this shared state, and that's what makes it a little bit different."
>
> — [3:04](https://www.youtube.com/watch?v=khVX_BUnEwU&t=184s) &middot; *The sharpest architectural differentiator versus multi-agent messaging.*

> "in the end you get this beautiful typed event log, which gives you replays. It gives you rollbacks and it gives you forks."
>
> — [3:43](https://www.youtube.com/watch?v=khVX_BUnEwU&t=223s) &middot; *States the concrete payoff of event sourcing for agents.*

> "this is not a harness. It's it's a runtime and you can actually rebuild most of the common harnesses on top of it."
>
> — [4:19](https://www.youtube.com/watch?v=khVX_BUnEwU&t=259s) &middot; *Positions ActiveGraph against the agent-framework category.*

> "It is much more complex about actually pretty unintuitive. I would never write code myself with ActoGraph, but again, AI seems really good at it."
>
> — [6:33](https://www.youtube.com/watch?v=khVX_BUnEwU&t=393s) &middot; *Rare admission of a real ergonomic tradeoff, and a bet on AI-authored code.*

> "it's inspired by uh blackboard architecture from the '70s or '80s or more recently Kafka, whole bunch of micro workers communicating through a shared state"
>
> — [7:10](https://www.youtube.com/watch?v=khVX_BUnEwU&t=430s) &middot; *Names the intellectual lineage of the design.*

> "now, AI writes the code, and the workers can be very powerful because they have reasoning capability"
>
> — [7:10](https://www.youtube.com/watch?v=khVX_BUnEwU&t=430s) &middot; *Explains why an architecture that failed in the '80s might work now.*

> "There was no semantic uh ingestion, no fact extraction, no entity extraction, but I just embedded the query, looked for relevant messages, grabbed a couple messages before and after, made sure it fit into the context, and it actually did pretty well on long mem eval"
>
> — [8:17](https://www.youtube.com/watch?v=khVX_BUnEwU&t=497s) &middot; *Reports a surprisingly strong baseline result against elaborate memory pipelines.*

> "for these loops, it would loop like eight or 13 times, but only accept four or five of those patches. And it actually did have, you know, modest, but like statistically significant improvement on long mem eval scores."
>
> — [11:47](https://www.youtube.com/watch?v=khVX_BUnEwU&t=707s) &middot; *The only quantified self-improvement result in the talk, honestly hedged.*

> "what was most interesting is how much how well the agent understood experiments we've tried before that didn't work."
>
> — [13:15](https://www.youtube.com/watch?v=khVX_BUnEwU&t=795s) &middot; *Identifies negative-result retention as the underrated benefit of log-centric agents.*

> "I've done a lot of YOLO agents where you just like keep trying things and then it works, you're like, "Yeah." But then I don't know the stuff that we tried that didn't work."
>
> — [14:19](https://www.youtube.com/watch?v=khVX_BUnEwU&t=859s) &middot; *Names the failure mode that policy-gated experimentation fixes.*

> "my hypothesis is that that's in the training data. And there's just much less training data around how to build LLM based agents."
>
> — [14:54](https://www.youtube.com/watch?v=khVX_BUnEwU&t=894s) &middot; *A testable explanation for why models code better in an old architectural idiom.*

> "some some discussions kind of suggests that as models get better, like the harness disappears. But I'm starting to think that's not true. I think we need both"
>
> — [15:28](https://www.youtube.com/watch?v=khVX_BUnEwU&t=928s) &middot; *Direct disagreement with a widely held position about harnesses.*

> "we're not our reasoning capability, right? We are we're closer to our our our beliefs, our knowledge, and behaviors that are derived from our actual life experience."
>
> — [15:59](https://www.youtube.com/watch?v=khVX_BUnEwU&t=959s) &middot; *The philosophical case for identity-as-log.*

## Positions

- Agents should be built around an immutable event log as ground truth rather than around the LLM, with graph state derived as a projection of that log. ([2:00](https://www.youtube.com/watch?v=khVX_BUnEwU&t=120s), confidence: stated)
- Changes to the agent itself and the agent's actions should live in one log rather than being tracked in two different places. ([2:35](https://www.youtube.com/watch?v=khVX_BUnEwU&t=155s), confidence: stated)
- LLM components should never message each other directly; all coordination should go through shared state. ([3:04](https://www.youtube.com/watch?v=khVX_BUnEwU&t=184s), confidence: stated)
- ActiveGraph is a runtime, not a harness, and common agent harnesses such as ReAct can be rebuilt on top of it. ([4:19](https://www.youtube.com/watch?v=khVX_BUnEwU&t=259s), confidence: stated)
- A structured log used directly as memory — with no fact or entity extraction — performs well on LongMemEval. ([8:17](https://www.youtube.com/watch?v=khVX_BUnEwU&t=497s), confidence: stated)
- Gated self-modification loops produced modest but statistically significant accuracy improvements on LongMemEval, accepting only about 4-5 of 8-13 proposed patches. ([11:47](https://www.youtube.com/watch?v=khVX_BUnEwU&t=707s), confidence: stated)
- Roughly 20-30 of about 80 Pokémon TCG deck-agent passes were accepted, with the score slowly improving to around 27%. ([13:45](https://www.youtube.com/watch?v=khVX_BUnEwU&t=825s), confidence: stated)
- AI models write shared-state/blackboard-style agent code better than LLM-agent-style code because decades of that architectural discussion exist in the training data while LLM agent patterns are only about three years old. ([14:54](https://www.youtube.com/watch?v=khVX_BUnEwU&t=894s), confidence: stated)
- The harness will not disappear as models improve; long-running agents need both a predictive world model and an experiential world model built from their own log. ([15:28](https://www.youtube.com/watch?v=khVX_BUnEwU&t=928s), confidence: stated)
- An agent's identity should be understood as derived from its own event log, analogous to how human identity derives from lived experience rather than raw reasoning capability. ([16:36](https://www.youtube.com/watch?v=khVX_BUnEwU&t=996s), confidence: stated)
- Writing ActiveGraph code by hand is impractically unintuitive for humans, making it viable only because AI writes the code. ([6:33](https://www.youtube.com/watch?v=khVX_BUnEwU&t=393s), confidence: stated)
- Event-sourced agents eliminate the need to restart long runs from the beginning after a failure such as an expired API key. ([8:54](https://www.youtube.com/watch?v=khVX_BUnEwU&t=534s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent skills](../concepts/agent-skills.md)
- [audit trails](../concepts/audit-trails.md)
- [durable execution](../concepts/durable-execution.md)
- [graph rag](../concepts/graph-rag.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)

