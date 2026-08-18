---
title: "Your Agent Failed in Prod. Good Luck Reproducing It."
type: "talk"
slug: "your-agent-failed-in-prod-good-luck-reproducing-it"
org: "Microsoft"
video_id: "Lc8zRh9muoY"
duration_sec: 849
word_count: 2387
speakers: ["Susheem Koul", "Tisha Chawla"]
---

# Your Agent Failed in Prod. Good Luck Reproducing It.

**Speakers:** [Susheem Koul](../speakers/susheem-koul.md), [Tisha Chawla](../speakers/tisha-chawla.md)

**Org:** Microsoft

**Duration:** 14m 09s

[Watch on YouTube](https://www.youtube.com/watch?v=Lc8zRh9muoY)

## Summary

Tisha Chawla and Susheem Koul argue that the standard reflex for debugging agent failures in production — pull the prompt from telemetry, set temperature to zero, and rerun — is a dead end, because hosted LLM inference is non-deterministic for reasons that have nothing to do with sampling. They walk through the first-principles causes (non-associative floating point, lack of batch invariance, mixture-of-experts capacity routing) and use a stock-trading agent that sells 1,000 shares instead of $1,000 worth as the running example of a silent failure that returns a clean 200 OK while dashboards stay green. Their reframe: stop chasing bitwise determinism and pursue replayability instead — record what enters and leaves every node of the agent graph, not network packets, and freeze the whole envelope (model version, build ID, RAG chunks) as a trace. They demo Chronicle, a proof-of-concept library whose `boundary` annotation both records these traces and later replays them as test cases, stubbing every node except the one you changed so you can verify a guardrail fix with zero model calls. Worth watching if you own an agent that touches real backends and need a concrete pattern for turning production incidents into free, rerunnable regression tests.

## Key Points

- Temperature zero does not make hosted LLM inference reproducible; it only guarantees argmax selection, not that the underlying logits stay identical between runs.
- The real sources of non-determinism are floating-point non-associativity, lack of batch invariance (your request is batched with whatever else arrives that millisecond), and mixture-of-experts capacity limits that reroute tokens depending on batch composition — not GPU concurrency, which is bit-identical for an isolated matmul.
- The dangerous production failures are silent: the broker API returned 200 OK in 30 milliseconds with zero exceptions and zero alerts while executing a $190,000 mistake.
- The speakers distinguish bitwise determinism (controllability, unobtainable from a hosted API and undesirable anyway) from replayability (observability, which is what debugging actually requires).
- Recording should happen at node boundaries rather than the network layer, because much of an agent — local retrieval, in-process tools, memory — never touches the network, and streaming/async shreds packet-level capture.
- Chronicle's `boundary` annotation wraps any method (tool, LLM call, RAG retrieval), records its input/output pair plus metadata like model version and code version, and freezes the run as a trace.
- The same trace doubles as a test fixture: enable replay mode, stub every node except the one you fixed, and assert on the live node's output — a deterministic CI run that costs nothing because it never calls a model.
- Testing agents splits in two: deterministic testing for guardrails and tool calls (where trace replay applies) and behavioral testing for tone and trajectory (where LLM-as-a-judge is the right tool).

## Notable Quotes

> "You can't reproduce it. And if you can't reproduce it, you can't debug it. And if you can't debug it, you can't promise it won't happen to your next customer or user, right?"
>
> — [0:45](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=45s) &middot; *states the talk's core stakes in one chain of consequences*

> "Instead of doing the math, the agent sells the raw number 1,000 and dumps it straight into the quantity field. Guess what? It sells 1,000 shares instead."
>
> — [1:22](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=82s) &middot; *the concrete failure the whole talk is built around*

> "We got zero exceptions, zero alerts. If you see the trade is completely wrong. But, your dashboards are sitting there perfectly green, perfectly flawless."
>
> — [2:12](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=132s) &middot; *names the silent-failure problem that conventional monitoring misses*

> "Setting the temperature to zero doesn't fix a broken reasoning path. It just means the model is going to make the exact same logical error, the exact same way, at the exact same time"
>
> — [2:12](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=132s) &middot; *attacks the most common reflex fix directly*

> "Running the same prompt a thousand times can still return dozens of completely different responses just due to the underlying GPU non-determinism and the MOE architectures which are there."
>
> — [3:03](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=183s) &middot; *reports the empirical claim underpinning the argument*

> "a tiny shift in matrix operation alters the final logits and which in turn will flip the winning token"
>
> — [3:53](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=233s) &middot; *the mechanism linking floating-point noise to different outputs*

> "So the real culprit is batch invariance here because a request gets grouped with whatever else hits the server that millisecond."
>
> — [3:53](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=233s) &middot; *identifies the specific culprit, ruling out the concurrency explanation*

> "Whether the token makes the cut depends entirely on the traffic you got batched with."
>
> — [3:53](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=233s) &middot; *crisp statement of how MoE routing makes your output depend on other users*

> "We don't need the model to return the exact same token back every time. We just need our system to execute the exact same state transition."
>
> — [4:49](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=289s) &middot; *the central reframe of the talk*

> "The right question is how do I debug and retest a run I can't reproduce because determinism was never the North Star. Debugging was."
>
> — [4:49](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=289s) &middot; *restates the reframe as a change of engineering goal*

> "You're not getting it from a hosted API, and you don't actually want it because the randomness is what makes the model good."
>
> — [5:39](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=339s) &middot; *takes the contrarian side that non-determinism is a feature*

> "You don't need the model deterministic. You need the run recorded, and you don't freeze the model. You capture what it did."
>
> — [5:39](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=339s) &middot; *the actionable one-line prescription*

> "For sure, not at the network layer because half your agent will never touch the network, the local retrieval, the in-process tools, the memory"
>
> — [5:39](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=339s) &middot; *names a specific instrumentation tradeoff others get wrong*

> "Record at the boundary instead because you need to capture what enters each node and what leaves it. The meaning of each step and not the packets."
>
> — [6:31](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=391s) &middot; *defines the boundary abstraction that the tool is built on*

> "You stub every node other than the node that you changed, and you let Boundary handle the rest, right?"
>
> — [10:14](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=614s) &middot; *the replay-as-test methodology in one sentence*

> "This is rerun-able, and since it never calls the model, it is free."
>
> — [12:51](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=771s) &middot; *the cost argument for trace-based deterministic testing*

> "On the behavioral side of things, you measure things like the tone of the agent or whether the trajectory it took was right. This is more subjective, and this is where techniques like LLM as a judge are better off."
>
> — [12:51](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=771s) &middot; *bounds where replay testing applies and where judges belong*

> "stop chasing bitwise determinism through the API. The fundamental principles on which the APIs are built today do not make this possible."
>
> — [12:51](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=771s) &middot; *the first and strongest takeaway, stated as a flat impossibility claim*

> "Third, capture the full envelope. Don't focus on just the prompt."
>
> — [13:25](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=805s) &middot; *concise correction to prompt-only logging practice*

> "keep the generation time variation alive. Don't try to pin the temperature to zero. After all, that is what brings the agency into your agent."
>
> — [13:25](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=805s) &middot; *closes the loop on why suppressing randomness is the wrong goal*

## Positions

- Setting temperature to zero does not produce reproducible LLM outputs, because greedy decoding only fixes the selection rule and not the underlying scores. ([2:12](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=132s), confidence: stated)
- GPU concurrency is not the cause of non-determinism — an isolated matrix multiplication run a thousand times returns bit-identical results. ([3:53](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=233s), confidence: stated)
- The actual causes of run-to-run variation are non-associative floating-point math, batching of your request with other traffic, and MoE expert capacity overflow causing token rerouting. ([3:53](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=233s), confidence: stated)
- Bitwise determinism is unobtainable from any hosted LLM API today. ([12:51](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=771s), confidence: stated)
- Model randomness is desirable and should be preserved, because it is what produces creative answers and gives an agent its agency. ([5:39](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=339s), confidence: stated)
- Teams that pursue model determinism waste weeks and conclude the system is unknowable. ([4:49](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=289s), confidence: stated)
- Recording at the network layer is the wrong instrumentation point for agents, because local retrieval, in-process tools, and memory never cross the network and streaming/async breaks packet capture. ([5:39](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=339s), confidence: stated)
- Because you cannot control the LLM, correctness must be enforced with guardrails on the tools rather than on model output. ([9:37](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=577s), confidence: stated)
- A recorded production trace can be reused directly as a regression test by stubbing every node except the one under change, giving a deterministic and zero-cost test run. ([10:52](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=652s), confidence: stated)
- Deterministic replay testing and behavioral testing are complementary and both necessary; LLM-as-a-judge is only appropriate for the subjective behavioral half. ([12:14](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=734s), confidence: stated)
- Session variables such as LLM version, build ID, and RAG chunks must be logged alongside the prompt for a trace to be replayable. ([12:51](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=771s), confidence: stated)
- Green dashboards and 200 OK responses are insufficient signals for agent correctness, since a catastrophic wrong action produces no exception or alert. ([2:12](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=132s), confidence: implied)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [durable execution](../concepts/durable-execution.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)

