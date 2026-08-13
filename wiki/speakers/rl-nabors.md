---
title: "RL Nabors"
type: "speaker"
slug: "rl-nabors"
talk_count: 1
---

# RL Nabors

## Talks

- [Frontier results, on device](../talks/frontier-results-on-device.md)

## Concepts

- [eval harness design](../concepts/eval-harness-design.md)
- [latency budgets](../concepts/latency-budgets.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [local inference](../concepts/local-inference.md)
- [model routing](../concepts/model-routing.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [quantization](../concepts/quantization.md)
- [retrieval evaluation](../concepts/retrieval-evaluation.md)
- [small language models](../concepts/small-language-models.md)

## Quotes

> "Now, token costs have been falling as of late, but total inference spend has been rising because agent can reasoning workloads consume tokens way faster than prices are dropping."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [2:11](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=131s)

> "found that 4 seconds is the limit of believability for users, and many calls that you will make to large models are going to take longer than 4 seconds"
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [1:28](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=88s)

> "You don't need history, you don't need philosophy, you don't need all those Reddit chats, you don't need a lot of what the models have learned and been trained on."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [4:32](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=272s)

> "Nvidia called SLMs the future of agentic AI. Once again, great research paper from 2025 that found that SLMs are sufficiently powerful for running agentic task loads."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [5:50](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=350s)

> "An SLM takes about 25% of that. And a task-specific model takes about half of that over."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [6:32](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=392s)

> "Now, first off, I like to think of this as prototype big, deploy small. Just repeat this to yourself."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [8:56](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=536s)

> "Now, a golden data set is a curated high-quality collection of preferably human-labeled input-output pairs that you're going to use as the ground truth to evaluate, validate, and benchmark your model."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [10:13](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=613s)

> "So, I actually did some math and it turns out I'm using about a dollar worth of inference every day using Mima."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [14:02](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=842s)

> "Good news is the total cost column for all these small local models is absolutely zilch because that inference has been pushed to the consumer."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [14:02](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=842s)

> "And I think that's important here because if I had just gone with what my buddies told me, I may have given the user What? Pardon. Not may have. I would have given the user an extremely different experience, not a good experience."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [15:26](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=926s)

> "You're going to want to select the smallest model that gives acceptable responses for your use case. Or as I like to call it, the SAGE model, the small and good enough model."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [15:26](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=926s)

> "You want to isolate one variable per prompt variant to test whether what you're trying to accomplish is moving the needle when you're using the different prompts."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [20:52](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1252s)

> "And the hypothesis was that small models respond to literal commands and that they like to be bossed around a bit."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [21:40](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1300s)

> "The best performing one was the few shot one that provided a couple of threads and a couple of examples."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [23:21](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1401s)

> "when it came to factual consistency, it turned out that Claude was just being a very strict judge."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [24:54](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1494s)

> "Claude Opus was comparing Claude Sonnet's response to uh Llama 3.2's response, and of course Claude was favoring its little sister"
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [25:57](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1557s)

> "So, when we added the post-processing, we're actually able to close that gap pretty solidly."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [26:45](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1605s)

> "It actually ended up meeting and beating Claude's on it after doing this little bit of extra effort, and I'm saving about a dollar a day in inference costs."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [27:32](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1652s)

> "it's how you keep your CTO from blowing away your agentic experience by accident one morning. True story, happened to a founder friend of mine."
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [28:17](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1697s)

> "I challenge you to go home today and take a look at what you're sending to LLM's and ask yourself, is this something that a smaller model could handle and how much money would I save if I did that?"
>
> — [Frontier results, on device](../talks/frontier-results-on-device.md), [28:17](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1697s)

