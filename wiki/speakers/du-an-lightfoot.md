---
title: "Du'an Lightfoot"
type: "speaker"
slug: "du-an-lightfoot"
role: "Senior AI Engineer"
company: "Akamai Technologies"
talk_count: 1
---

# Du'an Lightfoot

**Senior AI Engineer &middot; Akamai Technologies**

Senior AI Engineer at Akamai Technologies specializing in artificial intelligence and network engineering. Previously served as a Senior Developer Advocate at AWS and is the founder of LabEveryDay.

## Talks

- [Agents Building Agents](../talks/agents-building-agents.md)

## Scheduled Sessions

- **Agents That Own Their Inference: Building Production AI Agents on Dedicated GPUs** &middot; Day 1 — Workshop Day &middot; 9:00am-11:00am &middot; Track 7

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [retrieval evaluation](../concepts/retrieval-evaluation.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [spec-driven development](../concepts/spec-driven-development.md)

## Quotes

> "AI is very powerful and very good at building any type of software. And given that AI agents is just one type of software, as you may guess, we are using AI to build AI."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [0:47](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=47s)

> "You can see the golden dataset as a test suite, but in a non-deterministic scenario."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [4:09](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=249s)

> "we have a pass rate of 18%, right? Uh just because a a lot of questions are simple enough, like additions, multiplications, right? Are simple enough so that the actual um LLM has this knowledge in its training data"
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [5:54](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=354s)

> "So, 18% of the questions can be answered by the weights of the LLM, the rest can't."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [5:54](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=354s)

> "in a lot of cases, um a lot of the optimizations will be just to tweak the system prompt and update it so that um you know, our agent has all the information it needs to work on our domain."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [7:27](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=447s)

> "a coding agent tweaking the code of machine learning um of a deep learning algorithm can actually improve the results"
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [8:15](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=495s)

> "we have the baseline accuracy, which was 18%, and we managed to reach up to 83% um in like something around 10 uh 10 iterations."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [10:10](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=610s)

> "we also improved um some evals by 10% on a production agent that was already humanly optimized."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [10:10](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=610s)

> "the the coding agent found new ways that humans didn't find um to improve the agent, and we got plus 10% on some of our internal benchmarks."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [11:06](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=666s)

> "updating the golden data sets or the scorers just to let the evals pass is not a good idea, so we want to enforce we want to tell the we want to tell the AI agent to not do that"
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [11:55](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=715s)

> "the system works by creating an hypothesis. So it's tackling one class of problems at a time. It's updating the the agent and it's running the evals again."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [13:32](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=812s)

> "if the metrics improved, then we continue from this branch. Um if the metrics didn't improve or we have a strong regression or something bad happened, uh then we roll back to the previous branch."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [15:50](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=950s)

> "the baseline accuracy was 67% um but then in something around 10 iterations, we managed to reach 86% in our evals without actually cheating because it found edge cases, it improved the system prompt, it improved the tool descriptions to catch more edge cases, and it also fixed some tools logic."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [18:04](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1084s)

> "Maybe the evals didn't improve after an hypothesis, but maybe that hypothesis was promising, right? Maybe the agent was onto something, but it just didn't implement the system the change in a correct way"
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [17:24](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1044s)

> "we analyze all the traces with both the negative and positive feedback, but we are more interested about the negative feedback here."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [20:20](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1220s)

> "all the failure modes that we are founding during this investigation step, they will become part of the golden dataset that we mentioned earlier and the eval suite is updated to spot those regressions."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [25:33](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1533s)

> "We found out that once per sprint is actually reasonable."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [26:20](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1580s)

> "a coding agent, when instructed, uh has been able to fix an entire suite of issues like the one that we have seen earlier, uh with just one prompt."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [26:57](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1617s)

> "Harness Engineering is the idea of building the environment around our coding agent so that they can work reliably."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [27:46](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1666s)

> "if we don't know what's happening when we ship in production, we are basically blind"
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [29:15](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1755s)

