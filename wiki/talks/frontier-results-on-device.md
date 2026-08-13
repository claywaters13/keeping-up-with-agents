---
title: "Frontier results, on device"
type: "talk"
slug: "frontier-results-on-device"
org: "Arize"
video_id: "fWXJM-J0ZB8"
duration_sec: 1851
word_count: 4922
speakers: ["RL Nabors"]
---

# Frontier results, on device

**Speakers:** [RL Nabors](../speakers/rl-nabors.md)

**Org:** Arize

**Duration:** 30m 51s

[Watch on YouTube](https://www.youtube.com/watch?v=fWXJM-J0ZB8)

## Summary

RL Nabors argues that most production LLM calls are overkill and can be moved to small, on-device models without a meaningful quality loss. The talk walks through a concrete case study: a thread-summarization feature in a social client, prototyped on Claude Sonnet, then benchmarked against Qwen 2.5/3, Llama 3.2 3B, and Gemma on a 28-example golden dataset using Arize's open-source Phoenix eval tool. Llama 3.2 3B initially trailed the Claude baseline on structural validity and factual consistency, but few-shot prompting plus deterministic post-processing closed the gap entirely while beating Claude on latency and eliminating a dollar a day of inference spend. Along the way it offers a repeatable four-step method — prove it's possible with a big model, define success criteria, test small-to-large, select the 'SAGE' (small and good enough) model — plus warnings about LLM-as-judge bias and the need for regression evals. Worth watching if you ship user-facing LLM features and want a worked, numbers-backed template for downsizing them.

## Key Points

- Cloud inference carries four compounding costs — data exposure risk, latency above the ~4-second believability threshold, uncontrollable per-call spend, and total failure when offline — all of which on-device models eliminate.
- Token prices are falling but total inference spend is rising, because agentic and reasoning workloads consume tokens faster than prices drop.
- Most production tasks (summarizing a thread, detecting toxicity) don't need a model that contains all of human knowledge; SLMs run in the millions-to-billions of parameters and, quantized to 8- or 4-bit, fit on phones.
- The recommended workflow is 'prototype big, deploy small': prove feasibility on the largest model, set explicit success criteria, test models from small to large, and select the smallest one that clears the bar — the 'SAGE' model.
- In the case study, Qwen 2.5 1.5B was fastest (~1s P50) but least accurate, Gemma was slowest (~8s) despite peer recommendations, and Llama 3.2 3B won at ~90% accuracy with latency comparable to Claude Sonnet.
- Of four prompt variants tested (numbered input, few-shot, strict negative rules, chain of thought), few-shot won; strict negative constraints actively hurt performance, and chain of thought cost 600ms for marginal gain.
- Remaining gaps in reference validity and length compliance were closed deterministically in the harness via post-processing rather than by changing models or prompts.
- LLM-as-judge results must be inspected manually: Claude Opus judging Claude Sonnet against Llama was systematically strict toward the smaller model, so part of the measured 'factual inconsistency' was judge bias, not model error.
- Once a small model is in production, regression evals should run like CI tests so a prompt tweak or model upgrade can't silently break behavior.
- Energy use scales down too: an SLM uses roughly 25% of an LLM's energy for the same task, and a task-specific model roughly half of that again.

## Notable Quotes

> "Now, token costs have been falling as of late, but total inference spend has been rising because agent can reasoning workloads consume tokens way faster than prices are dropping."
>
> — [2:11](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=131s) &middot; *The core economic premise of the talk, stated as a counterintuitive trend.*

> "found that 4 seconds is the limit of believability for users, and many calls that you will make to large models are going to take longer than 4 seconds"
>
> — [1:28](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=88s) &middot; *Gives the concrete latency budget she later designs her P95 threshold around.*

> "You don't need history, you don't need philosophy, you don't need all those Reddit chats, you don't need a lot of what the models have learned and been trained on."
>
> — [4:32](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=272s) &middot; *Memorable framing of why frontier capability is wasted on routine tasks.*

> "Nvidia called SLMs the future of agentic AI. Once again, great research paper from 2025 that found that SLMs are sufficiently powerful for running agentic task loads."
>
> — [5:50](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=350s) &middot; *External authority cited for the talk's central claim.*

> "An SLM takes about 25% of that. And a task-specific model takes about half of that over."
>
> — [6:32](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=392s) &middot; *The talk's quantified energy argument.*

> "Now, first off, I like to think of this as prototype big, deploy small. Just repeat this to yourself."
>
> — [8:56](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=536s) &middot; *The talk's thesis compressed into a slogan.*

> "Now, a golden data set is a curated high-quality collection of preferably human-labeled input-output pairs that you're going to use as the ground truth to evaluate, validate, and benchmark your model."
>
> — [10:13](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=613s) &middot; *Defines the artifact the entire migration method depends on.*

> "So, I actually did some math and it turns out I'm using about a dollar worth of inference every day using Mima."
>
> — [14:02](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=842s) &middot; *Grounds the abstract cost argument in a real per-user number.*

> "Good news is the total cost column for all these small local models is absolutely zilch because that inference has been pushed to the consumer."
>
> — [14:02](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=842s) &middot; *Names the tradeoff honestly — the cost doesn't vanish, it moves to the user's battery.*

> "And I think that's important here because if I had just gone with what my buddies told me, I may have given the user What? Pardon. Not may have. I would have given the user an extremely different experience, not a good experience."
>
> — [15:26](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=926s) &middot; *Argues directly against picking models by community consensus instead of evals.*

> "You're going to want to select the smallest model that gives acceptable responses for your use case. Or as I like to call it, the SAGE model, the small and good enough model."
>
> — [15:26](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=926s) &middot; *Coins the selection heuristic the rest of the talk applies.*

> "You want to isolate one variable per prompt variant to test whether what you're trying to accomplish is moving the needle when you're using the different prompts."
>
> — [20:52](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1252s) &middot; *Methodological discipline for prompt optimization, often skipped in practice.*

> "And the hypothesis was that small models respond to literal commands and that they like to be bossed around a bit."
>
> — [21:40](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1300s) &middot; *States a common prompt-engineering intuition that her results then falsify.*

> "The best performing one was the few shot one that provided a couple of threads and a couple of examples."
>
> — [23:21](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1401s) &middot; *The empirical winner among four prompt strategies.*

> "when it came to factual consistency, it turned out that Claude was just being a very strict judge."
>
> — [24:54](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1494s) &middot; *Key caveat about trusting LLM-as-judge scores at face value.*

> "Claude Opus was comparing Claude Sonnet's response to uh Llama 3.2's response, and of course Claude was favoring its little sister"
>
> — [25:57](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1557s) &middot; *Names same-family judge bias explicitly.*

> "So, when we added the post-processing, we're actually able to close that gap pretty solidly."
>
> — [26:45](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1605s) &middot; *Points to deterministic code, not bigger models, as the fix for the last few percent.*

> "It actually ended up meeting and beating Claude's on it after doing this little bit of extra effort, and I'm saving about a dollar a day in inference costs."
>
> — [27:32](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1652s) &middot; *The headline result of the case study.*

> "it's how you keep your CTO from blowing away your agentic experience by accident one morning. True story, happened to a founder friend of mine."
>
> — [28:17](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1697s) &middot; *Makes the case for regression evals with a concrete failure mode.*

> "I challenge you to go home today and take a look at what you're sending to LLM's and ask yourself, is this something that a smaller model could handle and how much money would I save if I did that?"
>
> — [28:17](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1697s) &middot; *The talk's actionable call to action.*

## Positions

- Total inference spend is rising despite falling token prices, because agentic and reasoning workloads consume tokens faster than prices drop. ([2:11](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=131s), confidence: stated)
- Four seconds is the upper limit of believability for users in LLM chat interactions, and many frontier-model calls exceed it. ([1:28](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=88s), confidence: stated)
- SLMs consume about 25% of the energy an LLM uses for the same task, and task-specific models about half of that again. ([6:32](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=392s), confidence: stated)
- SLMs are sufficiently powerful for running agentic task loads, per Nvidia's 2025 research. ([5:50](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=350s), confidence: stated)
- The correct workflow is to prototype on a foundation model and then convert parts of the system to small and specialized models for production. ([8:56](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=536s), confidence: stated)
- You should select the smallest model that produces acceptable responses for your use case, not the most capable one available. ([16:08](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=968s), confidence: stated)
- Picking a model based on peer recommendation rather than evals would have shipped a materially worse user experience — Gemma was the recommended choice but came in around 8 seconds latency. ([15:26](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=926s), confidence: stated)
- Llama 3.2 3B was the best small model for social thread summarization, reaching about 90% accuracy, partly because Meta trains on social human inputs. ([17:40](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1060s), confidence: stated)
- Few-shot examples improve small-model output more than reformatted input, strict negative rules, or chain of thought; explicit negative constraints made results worse. ([23:21](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1401s), confidence: stated)
- Chain-of-thought prompting improved length compliance but added 600ms of latency, while few-shot added only 200ms. ([23:21](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1401s), confidence: stated)
- LLM judges favor models from their own family, so eval scores must be manually inspected rather than trusted numerically. ([25:57](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1557s), confidence: stated)
- Structural and length failures should be fixed with deterministic post-processing in the harness rather than with a larger model. ([26:45](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1605s), confidence: stated)
- Distilled models are a poor fit for mobile apps because every capability change requires retraining and shipping a new 1-2 GB model over users' data plans. ([19:13](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1153s), confidence: stated)
- Regression evals should be run continuously like CI tests to prevent prompt or model changes from silently degrading behavior. ([28:17](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=1697s), confidence: stated)
- Pushing inference on-device shifts the compute cost to the consumer's battery, which is an acceptable but real tradeoff worth evaluating. ([14:44](https://www.youtube.com/watch?v=fWXJM-J0ZB8&t=884s), confidence: implied)

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

