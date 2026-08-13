---
title: "Memory Harnesses for Long-Running Research Agents"
type: "talk"
slug: "memory-harnesses-for-long-running-research-agents"
track: "Memory & Continual Learning"
org: "Sakana.ai"
day: "Day 3 — Session Day 2"
room: "Main Stage"
video_id: "R3-anFK1YM8"
duration_sec: 784
word_count: 1919
speakers: ["Stefania Druga"]
---

# Memory Harnesses for Long-Running Research Agents

**Speakers:** [Stefania Druga](../speakers/stefania-druga.md)

**Org:** Sakana.ai

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 13m 04s

[Watch on YouTube](https://www.youtube.com/watch?v=R3-anFK1YM8)

## Summary

Stefania Druga, a research scientist at Sakana AI, presents experiments on building memory harnesses for long-horizon research agents running entirely on local models on a single M3 Ultra Mac. She frames memory not as a database but as a write-manage-read control loop wrapped around a stateless agent, and tests a ladder of recall policies — no memory, vector RAG, a ranked decisions ledger, and an oracle ground-truth condition — across X-Bench and Spider V2. The headline findings: when a task fits in context, memory adds cost without adding capability; when it doesn't, a ranked ledger beats both vector RAG and simple gating, and it costs fewer tokens than bad memory. She also argues that running the whole pipeline locally is a form of sovereignty — you control the data, the traces, and every step of evaluation — at the price of serial-only inference and very slow eval runs. Worth watching if you are designing recall policies and want empirical, reproducible evidence rather than architecture diagrams.

## Key Points

- Context rot — models contradicting themselves, redoing finished work, or drifting from the original question — is becoming more urgent as task horizons lengthen while model release cadence slows, converging later this year per METR projections.
- Memory should be modeled as a write-manage-read control loop around the model rather than as a passive database store.
- The harness design starts from agents with zero durable memory so that all memory behavior is attributable to the harness, with a core always-visible trace block, a recall block, and an archival block across sessions.
- The recall ladder tested four modes — no memory, vector RAG, a ranked decisions ledger, and an oracle that supplies ground-truth memory — with the model held fixed so only the recall variable changes.
- On a literature-review task where the entire corpus fit in context, memory produced identical performance with and without it while adding cost, showing harnesses only pay off past the context boundary.
- On X-Bench, where the answer sat at step 124 but the question was asked at step 500, the rank-only ledger performed best across 68 questions with multiple cells and seeds, beating gated memory.
- The oracle condition does not reach maximum performance because supplying the correct memory does not force the model to use it — it can still ignore or misread it.
- Ranked recall generalizes across models (Qwen 27B 4-bit, Deep Seek V4 Flash) and benchmarks (X-Bench, Spider V2), and reduces token spend rather than increasing it.
- Local-only evaluation gives full control over data, compute traces, and evals — Druga's framing of sovereignty — but Deep Seek V4 Flash lacks batch querying, forcing serial runs that take days.

## Notable Quotes

> "if you work with long horizon tasks, you probably run into this issue of context blow. Right? Like when the model starts contradicting itself, or it has to redo the work because it forgot it did that task in the first place, or it starts to drift from your questions because it forgot them."
>
> — [0:01](https://www.youtube.com/watch?v=R3-anFK1YM8&t=1s) &middot; *Defines the failure mode the whole talk is organized around, in concrete symptoms rather than abstraction.*

> "we see that the trend is to solve longer and longer uh horizon tasks, and also that we're getting fewer and fewer model releases. So, at some point later this year, we're going to have this convergence"
>
> — [1:01](https://www.youtube.com/watch?v=R3-anFK1YM8&t=61s) &middot; *States the timing argument for why harness work matters now, a claim other speakers might contest.*

> "the CEO of Coinbase actually shared how their company managed to reduce their AI spent while actually increasing uh the AI usage."
>
> — [1:01](https://www.youtube.com/watch?v=R3-anFK1YM8&t=61s) &middot; *The industry data point motivating the local-model framing.*

> "the way they did that was by transitioning to use many more local models, but also having better practices, like using better routing, better caching, keeping the context clean"
>
> — [1:56](https://www.youtube.com/watch?v=R3-anFK1YM8&t=116s) &middot; *Names the specific practices credited with the cost reduction.*

> "these local models are starting to be useful for agentic tasks and for tool use."
>
> — [1:56](https://www.youtube.com/watch?v=R3-anFK1YM8&t=116s) &middot; *A compact statement of the talk's premise about local model viability.*

> "on this M3 Ultra with 96 GB and 28 core CPUs, I'm using two models. I'm using the Qwen 27B quantized at 4-bit and the Deep Seek V4 Flash."
>
> — [2:42](https://www.youtube.com/watch?v=R3-anFK1YM8&t=162s) &middot; *Full hardware and model spec, which makes the results reproducible.*

> "you can think of memory as a write-manage-read loop. So, it's not just a database store. It's actually this control loop around the model."
>
> — [3:25](https://www.youtube.com/watch?v=R3-anFK1YM8&t=205s) &middot; *The core conceptual reframing the talk offers.*

> "I started with research agents that are the small agents because they have zero durable memory, and I wanted all the memory to come from the harness."
>
> — [3:25](https://www.youtube.com/watch?v=R3-anFK1YM8&t=205s) &middot; *Explains the experimental control that makes the ablations meaningful.*

> "the memory actually didn't add more capability. It was the same performance with memory and without memory, and it only added more cost. So, when your task fits in context, the harness doesn't add much."
>
> — [5:43](https://www.youtube.com/watch?v=R3-anFK1YM8&t=343s) &middot; *The negative result, and the most actionable boundary condition in the talk.*

> "if I start to run tasks that are longer term horizon, and the entire task and the relevant context doesn't uh fit, then having a good memory harness really starts to pay off."
>
> — [6:36](https://www.youtube.com/watch?v=R3-anFK1YM8&t=396s) &middot; *States the complementary positive condition.*

> "the right answer is in a like step 124, but the moment when I ask the question, I'm asking it like at step 500. So, it's completely outside of the context window"
>
> — [6:36](https://www.youtube.com/watch?v=R3-anFK1YM8&t=396s) &middot; *Concrete illustration of what a long-horizon memory benchmark item looks like.*

> "I ran over 68 questions and for each of these questions there were like multiple cells and lots of different seeds. And what I found was that the rank only ledger performed the best."
>
> — [7:31](https://www.youtube.com/watch?v=R3-anFK1YM8&t=451s) &middot; *The headline empirical result with its sample size.*

> "it performed better than like just gating the harness by saying do you need to use memory or do you not need to use memory."
>
> — [7:31](https://www.youtube.com/watch?v=R3-anFK1YM8&t=451s) &middot; *Directly rejects the common gating heuristic in favor of ranking.*

> "The Oracle what it does, it provides the right information, the right memory to the model but it doesn't force it to use it. So the model can get the right memory but still retrieve the wrong information or choose to ignore it or be confused."
>
> — [8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s) &middot; *Explains why perfect retrieval is not a performance ceiling — a subtle point many memory pitches miss.*

> "this actually works on several models, not only on the Qwen 27B but also on the DS4 flash and it also works across different benchmarks. I also tried it on the Spider V2 benchmark."
>
> — [9:10](https://www.youtube.com/watch?v=R3-anFK1YM8&t=550s) &middot; *Generalization evidence beyond a single model and benchmark.*

> "bad memory is expensive because it spends more token and it can send the agent the wrong way. But having like a good structural policy for recall can save you a lot of tokens and uh budget."
>
> — [9:10](https://www.youtube.com/watch?v=R3-anFK1YM8&t=550s) &middot; *The talk's compressed heuristic, tying recall quality directly to cost.*

> "one thing that I want to encourage you from this experiment is to consider the recall policy as a first-class metric"
>
> — [10:01](https://www.youtube.com/watch?v=R3-anFK1YM8&t=601s) &middot; *The explicit prescriptive takeaway for practitioners.*

> "going from simple file system retrieval to training memory models um there's there's a wide spectrum of solutions from less structural to completely structured."
>
> — [10:54](https://www.youtube.com/watch?v=R3-anFK1YM8&t=654s) &middot; *Situates the experiment within the broader design space.*

> "these local models I can only what run them in serial, like they don't support batch querying for the deep seed 4 flash. So, that's why I am still running evaluations back on my computer in Tokyo"
>
> — [11:48](https://www.youtube.com/watch?v=R3-anFK1YM8&t=708s) &middot; *Honest accounting of the cost of the local-only approach.*

> "it's a very good test for what memory can do when you can control every single step of the pipeline. And this sovereign capability is part of a bigger ecosystem that is very important for us at Sakana AI in Japan."
>
> — [11:48](https://www.youtube.com/watch?v=R3-anFK1YM8&t=708s) &middot; *Connects the technical choice to the organizational thesis about sovereign AI.*

## Positions

- Memory is best understood as a write-manage-read control loop around the model, not as a database store. ([3:25](https://www.youtube.com/watch?v=R3-anFK1YM8&t=205s), confidence: stated)
- When a task and its relevant context fit inside the context window, a memory harness adds no capability and only adds cost. ([5:43](https://www.youtube.com/watch?v=R3-anFK1YM8&t=343s), confidence: stated)
- A rank-only decisions ledger outperforms vector RAG and binary memory gating on long-horizon recall tasks. ([7:31](https://www.youtube.com/watch?v=R3-anFK1YM8&t=451s), confidence: stated)
- Providing an agent with the correct memory does not guarantee it will use it, so oracle retrieval does not reach maximum task performance. ([8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s), confidence: stated)
- Good recall policy reduces total token spend, so memory quality is a cost lever and not just an accuracy lever. ([9:10](https://www.youtube.com/watch?v=R3-anFK1YM8&t=550s), confidence: stated)
- Recall policy should be treated as a first-class metric in agent system design. ([10:01](https://www.youtube.com/watch?v=R3-anFK1YM8&t=601s), confidence: stated)
- Lengthening task horizons combined with a slowing model release cadence will make context management a critical bottleneck later this year. ([1:01](https://www.youtube.com/watch?v=R3-anFK1YM8&t=61s), confidence: stated)
- Local open-weight models such as Qwen 27B and Deep Seek V4 Flash are now capable enough for real agentic and tool-use workloads. ([1:56](https://www.youtube.com/watch?v=R3-anFK1YM8&t=116s), confidence: stated)
- Running the full evaluation pipeline locally is worth its serial-execution cost because controlling data, traces, and compute constitutes sovereignty. ([11:48](https://www.youtube.com/watch?v=R3-anFK1YM8&t=708s), confidence: implied)
- Shifting workloads to local models alongside better routing, caching, and context hygiene can cut AI spend while increasing AI usage. ([1:56](https://www.youtube.com/watch?v=R3-anFK1YM8&t=116s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [audit trails](../concepts/audit-trails.md)
- [benchmark design](../concepts/benchmark-design.md)
- [context rot](../concepts/context-rot.md)
- [local inference](../concepts/local-inference.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [sovereign and air-gapped deployment](../concepts/sovereign-and-air-gapped-deployment.md)

