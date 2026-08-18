---
title: "Andrew Dumit"
type: "speaker"
slug: "andrew-dumit"
talk_count: 1
---

# Andrew Dumit

## Talks

- [Respect The Process](../talks/respect-the-process.md)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [context window management](../concepts/context-window-management.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [reward hacking](../concepts/reward-hacking.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)
- [verifier design](../concepts/verifier-design.md)

## Quotes

> "In these cases, there are many ways to get the right answer the wrong way and there are also many right answers that experts will disagree on."
>
> — [Respect The Process](../talks/respect-the-process.md), [0:33](https://www.youtube.com/watch?v=CLttOU7n6sI&t=33s)

> "you have to verify the process in addition to the answer because the answer is really only justified in so far as it the process that produced that answer is correct"
>
> — [Respect The Process](../talks/respect-the-process.md), [0:33](https://www.youtube.com/watch?v=CLttOU7n6sI&t=33s)

> "six experts were given the exact same data on the exact same bottle of wine and despite having all access to the exact same things, they came to answers that varied by up to 50%"
>
> — [Respect The Process](../talks/respect-the-process.md), [1:05](https://www.youtube.com/watch?v=CLttOU7n6sI&t=65s)

> "when we first tried to solve this problem a little over a year ago, it worked decently well on one graph"
>
> — [Respect The Process](../talks/respect-the-process.md), [2:22](https://www.youtube.com/watch?v=CLttOU7n6sI&t=142s)

> "But then, when we tried to scale it up to many graphs, or frankly even just a few graphs, it absolutely broke."
>
> — [Respect The Process](../talks/respect-the-process.md), [2:22](https://www.youtube.com/watch?v=CLttOU7n6sI&t=142s)

> "the agent then really started to hallucinate different parts of the schema as those contexts got eaten, and despite those specialized tools, this led to retries and ultimately errors"
>
> — [Respect The Process](../talks/respect-the-process.md), [2:57](https://www.youtube.com/watch?v=CLttOU7n6sI&t=177s)

> "It could write loops over graphs and nodes. It could write scripts to unpack and summarize the node content underneath it all."
>
> — [Respect The Process](../talks/respect-the-process.md), [4:13](https://www.youtube.com/watch?v=CLttOU7n6sI&t=253s)

> "We started to write a bunch of evals for it. And we quickly learned that unconstrained code is quite scary."
>
> — [Respect The Process](../talks/respect-the-process.md), [4:53](https://www.youtube.com/watch?v=CLttOU7n6sI&t=293s)

> "we saw it write Python when we expected TypeScript and and instructed it to write TypeScript because it found Python on the virtual machine that we had given it"
>
> — [Respect The Process](../talks/respect-the-process.md), [4:53](https://www.youtube.com/watch?v=CLttOU7n6sI&t=293s)

> "the agent actually started to gaslight users sometimes saying it had made edits when it hadn't"
>
> — [Respect The Process](../talks/respect-the-process.md), [5:30](https://www.youtube.com/watch?v=CLttOU7n6sI&t=330s)

> "manual review of code is not something that are is in our users' wheelhouse. They are not software engineers"
>
> — [Respect The Process](../talks/respect-the-process.md), [6:08](https://www.youtube.com/watch?v=CLttOU7n6sI&t=368s)

> "We don't want to constrain how the agent reasons. We get so many benefits from these powerful models, but we also can't perfectly verify the answer in our case."
>
> — [Respect The Process](../talks/respect-the-process.md), [7:24](https://www.youtube.com/watch?v=CLttOU7n6sI&t=444s)

> "we frame it as constraining the effects, not the expression"
>
> — [Respect The Process](../talks/respect-the-process.md), [7:24](https://www.youtube.com/watch?v=CLttOU7n6sI&t=444s)

> "we require that all the critical code, really the stuff that edits the graph, goes through a filter of this typed SDK that we've put together where we can lint and check for errors"
>
> — [Respect The Process](../talks/respect-the-process.md), [8:03](https://www.youtube.com/watch?v=CLttOU7n6sI&t=483s)

> "our SDK is the only door"
>
> — [Respect The Process](../talks/respect-the-process.md), [8:38](https://www.youtube.com/watch?v=CLttOU7n6sI&t=518s)

> "even with the typed SDK as our entry point, that really only guides the agent towards the desired end state. And the real guarantee comes from the final script that we orchestrate on agent completion."
>
> — [Respect The Process](../talks/respect-the-process.md), [10:18](https://www.youtube.com/watch?v=CLttOU7n6sI&t=618s)

> "the graph edit function impact analysis ran on 50 graphs. Um there were two functions that it applied that produced 749 edit actions, and it ultimately in this case reduced the overall emissions by 45.6%"
>
> — [Respect The Process](../talks/respect-the-process.md), [11:30](https://www.youtube.com/watch?v=CLttOU7n6sI&t=690s)

> "we've been able to improve our outcomes from about 43% to 92% on our set of internal evals"
>
> — [Respect The Process](../talks/respect-the-process.md), [13:20](https://www.youtube.com/watch?v=CLttOU7n6sI&t=800s)

> "These very smart agents may declare victory in an unexpected way from what you or your user really want them to declare."
>
> — [Respect The Process](../talks/respect-the-process.md), [15:57](https://www.youtube.com/watch?v=CLttOU7n6sI&t=957s)

> "you should use that deterministic final outcome to produce outputs that are easy to validate even for non-coders. The code is kind of just the means to an end."
>
> — [Respect The Process](../talks/respect-the-process.md), [15:57](https://www.youtube.com/watch?v=CLttOU7n6sI&t=957s)

