---
title: "Ali Khial"
type: "speaker"
slug: "ali-khial"
role: "Head of AI/ML"
company: "G2i"
talk_count: 1
---

# Ali Khial

**Head of AI/ML &middot; G2i**

Ali Khial is an engineering leader focused on building AI-native systems that work beyond the demo stage. He currently leads AI/ML at G2i, where he works across frontier AI evaluation, software engineering benchmarks, agentic workflows, and human-data quality systems. His current work centers on the gap between impressive AI prototypes and reliable production systems. He is especially interested in AI evaluation, data quality, tool-using applications, and the engineering practices needed to ship model-powered products in real-world environments.

[LinkedIn](https://www.linkedin.com/in/ali-khial/)

## Talks

- [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md) (Posttraining & Midtraining)

## Scheduled Sessions

- **Benchmarks: The Good, the Bad, and the Ugly** &middot; Day 3 — Session Day 2 &middot; 3:20pm-3:40pm &middot; Track 9

## Concepts

- [benchmark contamination](../concepts/benchmark-contamination.md)
- [benchmark design](../concepts/benchmark-design.md)
- [coding agent benchmarking](../concepts/coding-agent-benchmarking.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rubric design](../concepts/rubric-design.md)
- [verifier design](../concepts/verifier-design.md)

## Quotes

> "I did a quick research on SweetBench Pro, and um there's 481 words per instruction in average. That's a two-pager per task. That is not how people write prompts."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [3:09](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=189s)

> "the instruction is pointing directly to the test file, which basically means that the LLM has all the ingredient it needs to go and find that test file and implement based on that"
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [4:04](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=244s)

> "it's basically providing a complete interface of the implementation. Basically locking the LLM from any kind of uh creativity and it's forcing it to do it that way."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [4:04](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=244s)

> "It's abstracted enough to allow for the LLM to do its work, but it's asking it to build a C compiler in Rust. So, I don't know if any of you ever tried to do that, but I don't think it's a good idea."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [4:45](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=285s)

> "In Sweet Bench Pro, 8.5 of 8.5% of all the tasks uh accepted wrong implementation in one hand and more than 20 24% of the tasks uh rejected um correct implementations."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [5:30](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=330s)

> "the test is is basically expecting a variable to exist. But that variable is first not specified in the instruction, and two, why would we expect an LLM to write the variable name this way?"
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [5:30](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=330s)

> "the test is basically checking functions that are unexported. So, if that was a PR in any of our projects, and exposed these type of tests, we would not accept it. So, this is what a weak verifier looks like."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [6:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=387s)

> "instead of actually trying to fix the to to apply a patch to a task, they try to go and find dot git folders, or they look up the internet for any kind of traces that would allow them to um to do the task"
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [6:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=387s)

> "as models evolve, they are now more smarter and smarter in being able to do reward hacking, but that's what we want. We want LLMs to be smart. The benchmarks are lacking behind and they're not preventing from from that to happen."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [7:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=447s)

> "the conclusion here is there's a quality gap and it's causing a trust gap. I have not met an engineer in the last 6 months that would choose a model or choose um an LLM based on the leaderboards."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [7:27](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=447s)

> "The instructions given to an agent or an LLM should lean towards expressing desired behaviors, objectives, and hard constraints, not implement details"
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [8:20](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=500s)

> "We want to have the most surface covered without being too prescriptive, but we also want to be precise where needed."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [9:20](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=560s)

> "for the rest of the the rest of the the software, we don't want to have 100% coverage because that's um not efficient"
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [9:20](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=560s)

> "It is one thing to have a test a task that is failing the LLM proven that the LLM is not there yet. It is another for it's another thing for an engineer to look at a task and say, "If the LLM is fixing this, I trust it to fix that." Currently, we don't have that."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [10:14](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=614s)

> "We want to do novel tasks only and we want to make sure that we keep private holdout sets."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [10:14](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=614s)

> "currently the tasks that are existing in benchmarks are all put from GitHub repos or from um from from public repos"
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [10:14](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=614s)

> "The benchmark needs to tell a story and needs to help people make decisions. Leaderboards are what we see in benchmarks today. They tell you who wins, but they don't to you why."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [11:04](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=664s)

> "This is a call to action to software engineers. Um benchmarks are not hard. We need to look under the hood. And we need to understand them and join the Discord because engineers' input is valuable."
>
> — [Benchmarks: The Good, the Bad, and the Ugly](../talks/benchmarks-the-good-the-bad-and-the-ugly.md), [11:47](https://www.youtube.com/watch?v=jWq-aZIU0kM&t=707s)

