---
title: "Rayan Garg"
type: "speaker"
slug: "rayan-garg"
role: "CEO"
company: "Theta Software"
talk_count: 1
---

# Rayan Garg

**CEO &middot; Theta Software**

CEO at Theta Software, building RL environments. Previously at DeepSilicon.

[LinkedIn](https://www.linkedin.com/in/rayan-garg/)

## Talks

- [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md) (Data Quality)

## Scheduled Sessions

- **Rethinking Environments for Long Horizon Work** &middot; Day 2 — Session Day 1 &middot; 11:40am-12:00pm &middot; Track 9

## Concepts

- [benchmark saturation](../concepts/benchmark-saturation.md)
- [coding agent benchmarking](../concepts/coding-agent-benchmarking.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [reward design](../concepts/reward-design.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [rubric design](../concepts/rubric-design.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)
- [verifier design](../concepts/verifier-design.md)

## Quotes

> "long horizon is really kind of a scalar metric. Uh, it's useful for kind of measuring relative tasks like one task might be more long than another, but it's really hard to define into kind of a binary category of this task is long and this task is not."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [1:20](https://www.youtube.com/watch?v=2aS7aKoXn64&t=80s)

> "what we consider long horizon a year ago probably isn't really long horizon in our definition today"
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [1:20](https://www.youtube.com/watch?v=2aS7aKoXn64&t=80s)

> "if a task takes GPT model 500,000 tokens, that doesn't really tell you a lot about what that task would look like for cloud models until you actually run on those cloud models."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [2:48](https://www.youtube.com/watch?v=2aS7aKoXn64&t=168s)

> "what's long horizon for a human isn't necessarily that difficult for a model depending on what the actual task you care about is"
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [4:27](https://www.youtube.com/watch?v=2aS7aKoXn64&t=267s)

> "It might take them like days to do that if it's a really big Excel file, but for a model, it can maybe write a Python script or find some other cool trick to do that really quickly."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [4:58](https://www.youtube.com/watch?v=2aS7aKoXn64&t=298s)

> "as you shift towards more long resin tasks and tasks that only the top 10% the top 1% top.1% of humans can really do these estimates start to get really really noisy"
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [5:52](https://www.youtube.com/watch?v=2aS7aKoXn64&t=352s)

> "one task can you know maybe be made by artificially long horizon by chaining together unrelated independent tasks. However, that doesn't actually tell us or meaningfully measure the model capabilities."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [7:56](https://www.youtube.com/watch?v=2aS7aKoXn64&t=476s)

> "we'll see if you have to use a dashboard or logs, a bad early query or a misread can cascade into these downstream steps that really start to have major consequences later on"
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [8:33](https://www.youtube.com/watch?v=2aS7aKoXn64&t=513s)

> "if you are going to have ambiguity in the materials you give, there's a lot more possible paths that the agent could take. There's a lot more ways the agent could be right. And that means that standardized evaluation gets much, much harder."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [9:39](https://www.youtube.com/watch?v=2aS7aKoXn64&t=579s)

> "a lot of the early RL that we were doing in in recent times was really in hard verifiable domains and that's why we saw these gains in in math and kind of uh like data structure style coding problems"
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [10:14](https://www.youtube.com/watch?v=2aS7aKoXn64&t=614s)

> "if we kind of enforce this too tightly, we collapse the state space of how many actual paths the agent actually explores."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [12:35](https://www.youtube.com/watch?v=2aS7aKoXn64&t=755s)

> "that really does not work for these more ambiguous or open-ended tasks because there's so many possible correct solutions. It's basically impossible to account for every single one."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [13:14](https://www.youtube.com/watch?v=2aS7aKoXn64&t=794s)

> "I think the first important uh consideration to make is that judges are agents too."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [13:14](https://www.youtube.com/watch?v=2aS7aKoXn64&t=794s)

> "it's really important that the judge has access to the environment in the same way uh with some important safeguards of course. One is that we don't want the judge to make an accidental mutation in some way to the environment after the agent is done."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [14:36](https://www.youtube.com/watch?v=2aS7aKoXn64&t=876s)

> "you can't just use this really basic approach of taking the trajectory and stuffing it in the context window of the judge and kind of have it be a basic LM call."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [15:03](https://www.youtube.com/watch?v=2aS7aKoXn64&t=903s)

> "These are all different things we want we want to do. And in that sense we need to make the trajectory itself queryable."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [15:44](https://www.youtube.com/watch?v=2aS7aKoXn64&t=944s)

> "especially for frontier problems that models aren't really capable of yet, judges will really struggle to apply that rubric consistently"
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [16:42](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1002s)

> "deterministic verifiers aren't completely dead. oftentimes we use them in tandem with judges."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [17:13](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1033s)

> "a lot of the data being produced right now and being used to train and evaluate models is actually flawed"
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [18:17](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1097s)

> "if you look at the average human hours per task, based on what Meter has defined for a lot of the leading frontier models, a lot of these different average human hours per task fall far below that and so they wouldn't actually be considered long horizon tasks."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [18:45](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1125s)

> "pass at one effectively means that for like 57% of cases, the tasks are 100% solved"
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [18:45](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1125s)

> "a lot of these more important areas for learnability like, you know, credit, debt, risk in the domain of finance don't really get covered"
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [19:23](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1163s)

> "We can see that the human time to complete one task on average is 15 hours over a 50 task sample set."
>
> — [Rethinking Environments for Long-Horizon Work](../talks/rethinking-environments-for-long-horizon-work.md), [20:32](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1232s)

