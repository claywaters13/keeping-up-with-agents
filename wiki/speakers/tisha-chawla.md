---
title: "Tisha Chawla"
type: "speaker"
slug: "tisha-chawla"
role: "Software Engineer"
company: "Microsoft"
talk_count: 1
---

# Tisha Chawla

**Software Engineer &middot; Microsoft**

Tisha Chawla is a Software Engineer at Microsoft, where she builds production-grade agentic systems designed to perform reliably against real enterprise data. Moving past isolated AI demos, her work targets the core infrastructure of agent engineering: durable state management, deterministic execution, and self-healing workflows that recover without manual intervention.
As an architect rather than a consumer of AI, Tisha designs the orchestration layers that allow coding agents, reliability agents, and spec-driven development workflows to scale. She is a published applied machine learning researcher and regularly delivers deep-dive technical sessions on deploying resilient, enterprise-scale AI architecture.

[LinkedIn](https://www.linkedin.com/in/tisha-chawla)

## Talks

- [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md) (co-presented)

## Scheduled Sessions

- **FinOps for AI Agents: Who Spent All the Tokens?** &middot; Day 4 — Session Day 3 &middot; 11:10am-11:30am &middot; Leadership 2

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [durable execution](../concepts/durable-execution.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "You can't reproduce it. And if you can't reproduce it, you can't debug it. And if you can't debug it, you can't promise it won't happen to your next customer or user, right?"
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [0:45](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=45s)

> "Instead of doing the math, the agent sells the raw number 1,000 and dumps it straight into the quantity field. Guess what? It sells 1,000 shares instead."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [1:22](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=82s)

> "We got zero exceptions, zero alerts. If you see the trade is completely wrong. But, your dashboards are sitting there perfectly green, perfectly flawless."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [2:12](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=132s)

> "Setting the temperature to zero doesn't fix a broken reasoning path. It just means the model is going to make the exact same logical error, the exact same way, at the exact same time"
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [2:12](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=132s)

> "Running the same prompt a thousand times can still return dozens of completely different responses just due to the underlying GPU non-determinism and the MOE architectures which are there."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [3:03](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=183s)

> "a tiny shift in matrix operation alters the final logits and which in turn will flip the winning token"
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [3:53](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=233s)

> "So the real culprit is batch invariance here because a request gets grouped with whatever else hits the server that millisecond."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [3:53](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=233s)

> "Whether the token makes the cut depends entirely on the traffic you got batched with."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [3:53](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=233s)

> "We don't need the model to return the exact same token back every time. We just need our system to execute the exact same state transition."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [4:49](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=289s)

> "The right question is how do I debug and retest a run I can't reproduce because determinism was never the North Star. Debugging was."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [4:49](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=289s)

> "You're not getting it from a hosted API, and you don't actually want it because the randomness is what makes the model good."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [5:39](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=339s)

> "You don't need the model deterministic. You need the run recorded, and you don't freeze the model. You capture what it did."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [5:39](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=339s)

> "For sure, not at the network layer because half your agent will never touch the network, the local retrieval, the in-process tools, the memory"
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [5:39](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=339s)

> "Record at the boundary instead because you need to capture what enters each node and what leaves it. The meaning of each step and not the packets."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [6:31](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=391s)

> "You stub every node other than the node that you changed, and you let Boundary handle the rest, right?"
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [10:14](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=614s)

> "This is rerun-able, and since it never calls the model, it is free."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [12:51](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=771s)

> "On the behavioral side of things, you measure things like the tone of the agent or whether the trajectory it took was right. This is more subjective, and this is where techniques like LLM as a judge are better off."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [12:51](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=771s)

> "stop chasing bitwise determinism through the API. The fundamental principles on which the APIs are built today do not make this possible."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [12:51](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=771s)

> "Third, capture the full envelope. Don't focus on just the prompt."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [13:25](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=805s)

> "keep the generation time variation alive. Don't try to pin the temperature to zero. After all, that is what brings the agency into your agent."
>
> — [Your Agent Failed in Prod. Good Luck Reproducing It.](../talks/your-agent-failed-in-prod-good-luck-reproducing-it.md), [13:25](https://www.youtube.com/watch?v=Lc8zRh9muoY&t=805s)

