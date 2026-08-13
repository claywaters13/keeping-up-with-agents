---
title: "User Signal Dies at the Retrieval Boundary"
type: "talk"
slug: "user-signal-dies-at-the-retrieval-boundary"
org: "StarlightSearch"
video_id: "Jx4ZFEAq6bY"
duration_sec: 937
word_count: 1867
speakers: ["Sonam Pankaj"]
---

# User Signal Dies at the Retrieval Boundary

**Speakers:** [Sonam Pankaj](../speakers/sonam-pankaj.md)

**Org:** StarlightSearch

**Duration:** 15m 37s

[Watch on YouTube](https://www.youtube.com/watch?v=Jx4ZFEAq6bY)

## Summary

Sonam Pankaj, CEO and co-founder of StarlightSearch, argues that agent failures are predominantly retrieval failures, not generation failures, and that the eval signal produced by observability and eval suites never makes it back into what the agent retrieves at runtime — it 'dies in the dashboard.' The talk proposes a missing layer between evals and action: a runtime experience system (Agent RX / 'reflect') that consumes traces and eval outcomes and converts them into retrieval guidance, ranking memories by a 'utility score' — semantic similarity weighted by whether a memory historically helped or hurt task outcomes. It positions this against existing memory products (LangChain, Mem0) which store user preferences and personalization facts and retrieve purely by embedding similarity, arguing memory should encode reasoning about tasks rather than static facts. Benchmarks are cited on tau-bench (66% → 76%, and 80% once memories are baked into skills) and an agentic benchmark (35.7 baseline → 58.2 with other memory systems → 61.3 with theirs), followed by a live SQL-agent demo where a failed 'gaming mouse' query is corrected by feedback and a changed tool trajectory. Worth watching if you are building self-improving agents and want a concrete design for closing the eval-to-retrieval loop; the demo is rough and the numbers are presented quickly without much methodology.

## Key Points

- The speaker claims 73% of agent pipeline failures come from retrieval and context stuffing rather than from generation, citing Gartner's 85% AI project failure figure and a McKinsey 2025 report as framing.
- There is a missing layer between evals/observability and agent action: traces and pass/fail eval verdicts exist but never feed back into the agent's context, skills, or retrieval, so agents keep failing the same task.
- Today the feedback loop is manual — an engineer reads the evals, rewrites the prompt, redeploys, upgrades to a more expensive model, restructures the harness, or fine-tunes.
- Existing memory systems (LangChain, Mem0) store preferences and conversation history and retrieve by embedding similarity alone, which suits chat personalization but is not a self-improving system for production agents.
- The proposed 'utility score' re-ranks retrieval by semantic similarity weighted by whether each memory historically helped or hurt execution outcomes, making eval outcome a first-class retrieval signal.
- Memory should store reasoning about tasks (e.g. check the settlement before issuing a refund so the customer isn't paid twice), not static user facts like theme preference.
- Once roughly ten memories accumulate, the system bakes the learned reasoning into skills — which lets the agent drop stale assumptions, like a SQL column referenced in a system prompt that no longer exists, without rewriting the prompt.
- Reported gains: tau-bench 66% → 76% with memory and 80% with skills; an agentic benchmark from a 35.7 baseline to 58.2 with other memory systems and 61.3 with theirs.
- Acknowledged limitations are cold start (pure semantic search until reviews accumulate), utility drift, near-duplicate memories, noisy review labels, and a lambda hyperparameter for credit assignment and re-ranking — cold start being the one they say they cannot fix.
- This is a runtime approach explicitly contrasted with compile-time optimization (e.g. DSPy-style prompt baking): learning happens while the task executes rather than being pre-compiled into the prompt.

## Notable Quotes

> "An agent is an LLM that has agency to reason, invoke tools, uh, interact with the real world, retrieve uh the memory to complete the task. One major loop here is missing is uh learning."
>
> — [0:01](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=1s) &middot; *sets the thesis — the missing loop in the standard agent definition is learning*

> "Gartner reported 85% of AI just failing traction. So, it's in McKinsey's 2025 report. The problem came out to be most of the time is that retrieval is static."
>
> — [0:48](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=48s) &middot; *cites the headline failure statistic and names the diagnosed cause*

> "73% of our uh pipelines fails because of retrieval, not generation, and context stuffing."
>
> — [1:39](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=99s) &middot; *the central quantified claim of the talk — failures are retrieval-side*

> "We made wrong answers appear faster and cheaper, but we forgot to make retrieval learn."
>
> — [1:39](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=99s) &middot; *the quoted framing (from Pinecone's ex-CTO) that the whole approach responds to*

> "The eval signal dies in the dashboard. This is a missing layer, a system that consume traces, absorb eval, and convert both into retrieval guidance for future runs."
>
> — [2:35](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=155s) &middot; *names the gap in the title and defines the proposed layer in one sentence*

> "current memory is that they basically store user preferences, profile, conversation history, or long-lived personalization. So, chat experience is not self-improving learning systems for production."
>
> — [3:32](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=212s) &middot; *the direct critique of existing memory products*

> "we have come up with something called utility score, which is a similarity weighted by how useful it is for the agent to execute the task."
>
> — [3:32](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=212s) &middot; *defines the core mechanism*

> "It's a runtime layer that let the large language agent improve from experiences without retraining, fine-tuning, or manual prompt engineering."
>
> — [4:37](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=277s) &middot; *states the product claim and what it replaces*

> "How it's a little different from compile time like DS5 because of you bake in all the lessons in the prompt, here is actually improving while it is executing the task."
>
> — [4:37](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=277s) &middot; *positions runtime learning against compile-time prompt optimization*

> "you do not retrieve by keyword, you do retrieve by semantic similarity to the current task weighted by whether those memories have historically helped or hurt the execution or the outcome."
>
> — [4:37](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=277s) &middot; *the most precise statement of the retrieval algorithm*

> "The event outcome becomes a first-class signal in the retrieval re-ranking and not just for retrieval."
>
> — [5:29](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=329s) &middot; *the architectural position — outcomes belong in ranking, not just dashboards*

> "One of the key things is it treat memory as reasoning, not as facts, statistics, fact with no context and no history, but reasoning."
>
> — [5:29](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=329s) &middot; *the contested design claim about what memory should contain*

> "So, we have seen the performance improve from 66 to 76% without baking in uh skills and with skills reflect performance at 80."
>
> — [6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s) &middot; *the headline tau-bench numbers*

> "once there are enough memory like 10 memories, uh what we do is we bake in the reasoning and the understanding into skills so that your agent always remains updated."
>
> — [6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s) &middot; *gives the concrete threshold for memory-to-skill consolidation*

> "Even though that column is no useful anymore, it remains in the system prompt. So, there's no system right now that can update that"
>
> — [7:22](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=442s) &middot; *concrete failure case for stale system prompts that motivates skill updating*

> "with the other memory system, it gets to 58.2. But with the refined memory system, uh, it gets to 61.3%."
>
> — [8:14](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=494s) &middot; *reports the comparative agentic-benchmark margin over competing memory systems*

> "First of all, there's a cold start. So, in the beginning, it's pure semantic search until, uh, enough reviews have been accumulated."
>
> — [8:14](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=494s) &middot; *honest statement of the approach's structural limitation*

> "So, we have built reflect in such a way that most of these problems and most of these elements are now reduced except for cold start which we cannot do much about it."
>
> — [9:07](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=547s) &middot; *concedes cold start is unsolved while claiming the other limitations are mitigated*

> "it's forming memories which is retrieved based on the utility score that is the score which basically keeps improving keeps re-ranking itself on the basis of how useful that memory was."
>
> — [13:39](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=819s) &middot; *ties the demo back to the mechanism — scores mutate from observed usefulness*

## Positions

- The majority of agent pipeline failures (73%) are caused by retrieval and context stuffing, not by generation. ([1:39](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=99s), confidence: stated)
- Eval results and observability traces currently have no path back into the agent's context, skills, or retrieval, so agents cannot learn from yesterday's passes and failures. ([2:35](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=155s), confidence: stated)
- Existing memory products like LangChain and Mem0 retrieve purely by embedding similarity and do not learn from outcomes. ([3:32](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=212s), confidence: stated)
- Chat-oriented memory (preferences, profiles, conversation history) is the wrong abstraction for self-improving production agents. ([3:32](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=212s), confidence: stated)
- Retrieval should rank by semantic similarity weighted by whether a memory historically helped or hurt the outcome, rather than by similarity or keywords alone. ([4:37](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=277s), confidence: stated)
- Runtime learning during task execution is preferable to compile-time approaches that bake lessons into the prompt ahead of time. ([4:37](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=277s), confidence: implied)
- Memory entries should encode task reasoning (e.g. check settlement before issuing a refund) rather than context-free user facts. ([5:29](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=329s), confidence: stated)
- On tau-bench, their memory system raises policy-following performance from 66% to 76%, and to 80% when memories are consolidated into skills. ([6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s), confidence: stated)
- After roughly ten accumulated memories, reasoning should be baked into skills so the agent's operating instructions stay current without prompt rewrites. ([6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s), confidence: stated)
- Stale system prompts (e.g. referencing a database column that no longer exists) are a real and currently unaddressed failure mode that updated skills can fix. ([7:22](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=442s), confidence: stated)
- On an agentic benchmark, their system reaches 61.3 versus 58.2 for other memory systems and a 35.7 baseline. ([8:14](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=494s), confidence: stated)
- Cold start is an inherent, unfixable limitation of outcome-weighted retrieval — early behavior is necessarily pure semantic search. ([9:07](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=547s), confidence: stated)
- Noisy human review labels propagate into noisy utility scores, making review quality a limiting factor for the approach. ([9:07](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=547s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent skills](../concepts/agent-skills.md)
- [context rot](../concepts/context-rot.md)
- [data flywheels](../concepts/data-flywheels.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [rubric design](../concepts/rubric-design.md)

