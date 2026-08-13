---
title: "Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It"
type: "talk"
slug: "agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it"
track: "Posttraining & Midtraining"
org: "Together AI (Dan Fu) and MiniMax (Olive Song)"
day: "Day 3 — Session Day 2"
room: "Track 9"
video_id: "AVMr9PMINyo"
duration_sec: 1214
word_count: 3975
speakers: ["Dan Fu", "Olive Song"]
---

# Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It

**Speakers:** [Dan Fu](../speakers/dan-fu.md), [Olive Song](../speakers/olive-song.md)

**Org:** Together AI (Dan Fu) and MiniMax (Olive Song)

**Track:** Posttraining & Midtraining &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 20m 14s

[Watch on YouTube](https://www.youtube.com/watch?v=AVMr9PMINyo)

## Summary

A conference panel pairing Olive Song (RL research lead at MiniMax, responsible for final training and shipping of the models) with Dan Fu (VP of Kernels at Together AI, responsible for inference and GPU optimization) to trace an open-weight model from post-training to day-zero serving. Song explains why MiniMax open-sources its strongest model, what changed in M3 (multimodal from step zero, ~1M context, MiniMax sparse attention), and how long-horizon agentic capabilities — replicating an ICLR paper in a 12-hour run, optimizing kernels, computer use — come down to environment design, reward formulation, and catching reward hacking. Fu describes the other half: getting architecture details pre-launch, writing or adapting kernels, and grinding out weekly speedups after launch, plus how agentic and million-token workloads turn KV cache management into a distributed-systems problem. The most contrarian thread is Fu's argument that benchmarks worth overfitting to are good benchmarks — Together's parallel kernel bench deliberately contains unsolved problems whose solutions they would ship. Worth watching if you want a concrete picture of the model-lab/inference-provider handoff and where both sides think open weights stand versus closed frontier labs.

## Key Points

- MiniMax open-sources its strongest models both on mission grounds ("intelligence with everyone") and on practical grounds: external developers contribute PRs and feedback, and inference partners like Together AI make the same weights faster for everyone.
- M3 differs from the M2 series by being trained multimodal from step zero rather than bolted on later; Song says other labs commonly see the model collapse in this regime and MiniMax solved that, yielding attention maps where text tokens naturally attend to visual tokens.
- Multimodal training pays off for agentic web development specifically: the model can look at the rendered website, understand how it looks, and optimize against that during reinforcement learning.
- Training long-horizon agentic tasks (kernel optimization, paper replication) is bottlenecked not by the algorithm but by environment and data design — how you formulate the problem, the rewards, and the environment, plus adapting the RL algorithm for efficiency.
- Evaluation of 12-hour tasks uses intermediate submissions rather than a single terminal signal, with held-out validation and test checks because models sometimes hack the reward.
- Together AI released parallel kernel bench containing deliberately unsolved kernel problems, inverting the usual bench-maxing worry: if you overfit to it, they will take the resulting kernels and ship them in production inference.
- Day-zero serving depends on getting architecture details early — M3's sparse attention, MoE choices, and quantization all differ from other open models — and quality at launch is treated as a first-class constraint alongside speed, with weeks of KV cache, attention kernel, and quantization work following launch.
- The shift from chat to agentic workloads changes where you optimize: a few-thousand-token system prompt plus chat logs is a different routing, caching, and kernel problem than uploading an entire codebase across hundreds of tool-calling turns.
- At 500K–1M context with concurrent requests, KV cache management becomes essentially a distributed file system or large database problem — conceptually simple, but rediscovered in industry rather than borrowed from systems training.
- Both speakers argue the open-weight frontier (M3, GLM, Kimi) is close behind closed labs, and Fu hopes the 'are open models far behind' question is settled within three years; he also thinks GPUs are badly underutilized today.

## Notable Quotes

> "I'm the VP of Kernels Together AI. I lead inference, GPU optimization, trying to figure out how to use GPUs most effectively to serve AI models."
>
> — [0:12](https://www.youtube.com/watch?v=AVMr9PMINyo&t=12s) &middot; *establishes Fu's vantage point on the inference side of the handoff*

> "I am the research lead of RL at MiniMax and I am responsible for the final training of the model and the shipping of the model."
>
> — [0:42](https://www.youtube.com/watch?v=AVMr9PMINyo&t=42s) &middot; *establishes Song's vantage point as the post-training counterpart*

> "We do believe that the open source community as a whole is very strong and powerful. While we open source the model, everyone can use it. So it aligns with our mission that we want to have intelligence with everyone"
>
> — [1:17](https://www.youtube.com/watch?v=AVMr9PMINyo&t=77s) &middot; *MiniMax's stated rationale for open-sourcing its strongest model*

> "how do you make intelligence abundant? So how do you get more tokens to more people to do more useful things"
>
> — [2:31](https://www.youtube.com/watch?v=AVMr9PMINyo&t=151s) &middot; *Together AI's framing of why it invests in serving open models*

> "it not only understands text and it not only writes code, it also understands videos and images"
>
> — [4:11](https://www.youtube.com/watch?v=AVMr9PMINyo&t=251s) &middot; *the headline capability change from M2 to M3*

> "It would be very important to design the environments of the data so that we can deliberately train reinforcement learning in those very complex environments and let the model to optimize the kernels themselves and iteratively improve the performance."
>
> — [5:24](https://www.youtube.com/watch?v=AVMr9PMINyo&t=324s) &middot; *names environment design as the lever for domain-specific RL*

> "one of the interesting things that we found is that there's a lot of things that we can think of that would actually speed models up that there don't exist good kernels for"
>
> — [6:02](https://www.youtube.com/watch?v=AVMr9PMINyo&t=362s) &middot; *reports the concrete gap that motivated a new kernel benchmark*

> "One of our intentions with this benchmark was that if you overfit to it, that's great cuz we'll go take those kernels and use them to to to accelerate the the the the inference and the development."
>
> — [6:41](https://www.youtube.com/watch?v=AVMr9PMINyo&t=401s) &middot; *the talk's sharpest contrarian position on bench-maxing*

> "there are things like the minimax sparse attention and and some of those choices that were a little bit different from any model that's out there"
>
> — [7:13](https://www.youtube.com/watch?v=AVMr9PMINyo&t=433s) &middot; *explains why day-zero serving requires pre-launch architecture access*

> "and then we start working on it and start optimizing over the course of weeks so that when you use these models, they actually get faster between day zero and day seven and day 14 and etc."
>
> — [8:23](https://www.youtube.com/watch?v=AVMr9PMINyo&t=503s) &middot; *concrete description of the post-launch optimization cadence*

> "with the coding base agentic workflows, you'll upload your whole code base to the model, and that's a very different optimization and routing and kernel challenge than than just the the chat base workload"
>
> — [9:39](https://www.youtube.com/watch?v=AVMr9PMINyo&t=579s) &middot; *names the tradeoff that agentic workloads impose on the inference stack*

> "So, from step zero, we trained not only text data, we also trained image data. And it was normal for many other labs that the model would collapse after training a little bit, and we managed to solve that problem."
>
> — [10:44](https://www.youtube.com/watch?v=AVMr9PMINyo&t=644s) &middot; *a specific claim of technical differentiation in multimodal pretraining*

> "if you look at the attention map, it actually the visual of the the text tokens would attend to the visual tokens"
>
> — [10:44](https://www.youtube.com/watch?v=AVMr9PMINyo&t=644s) &middot; *the mechanistic evidence Song offers for training multimodal from scratch*

> "I mean, you focus on a thousand and one things, yeah. Like you just you just go and you keep you keep doing it. You find every edge that you can, um and and you go and and you push on it."
>
> — [12:03](https://www.youtube.com/watch?v=AVMr9PMINyo&t=723s) &middot; *Fu's answer to 'where's the biggest bang for the buck' is that there isn't one*

> "the key there is still the environments and the data and how you formulate the problem, how you formulate the rewards, how you formulate the environment"
>
> — [14:17](https://www.youtube.com/watch?v=AVMr9PMINyo&t=857s) &middot; *restates the environment-over-algorithm thesis for long-horizon RL*

> "Some of them some of the times the models would hack, and we do do like validation and test with for it to test if it's really improving on the performance or it's hacking."
>
> — [15:08](https://www.youtube.com/watch?v=AVMr9PMINyo&t=908s) &middot; *concrete admission of reward hacking and the validation response*

> "we're actively using the model to improve the speed of development internally, which like out of it out of it we can build our own evaluations that are closely related to our own work"
>
> — [15:46](https://www.youtube.com/watch?v=AVMr9PMINyo&t=946s) &middot; *describes the self-evolution loop as both a productivity and an eval source*

> "Like in in some sense, it's like recreating a distributed file system. So, we we're in some sense building something like that or a very big database."
>
> — [16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s) &middot; *the clearest framing of KV cache at long context as a systems problem*

> "it's like the type of thing that you should have done in your third year of undergrad or something like that, but most of us actually skipped that class, so now we're rediscovering it live in in industry"
>
> — [16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s) &middot; *memorable line on the ML/systems knowledge gap*

> "I think we underutilize our GPUs a lot right now."
>
> — [17:38](https://www.youtube.com/watch?v=AVMr9PMINyo&t=1058s) &middot; *Fu's headline prediction about what will look embarrassing in three years*

> "we're seeing with models like M3 and GLM and Kimmy and and all those models that um the open-source frontier really can catch up. Um and and it's it's not even that far behind"
>
> — [18:09](https://www.youtube.com/watch?v=AVMr9PMINyo&t=1089s) &middot; *the panel's central claim about open weights vs closed labs*

## Positions

- Overfitting to a benchmark is desirable when the benchmark's tasks are themselves the useful artifact — Together AI's parallel kernel bench contains unsolved problems whose solutions they would deploy in production inference. ([6:41](https://www.youtube.com/watch?v=AVMr9PMINyo&t=401s), confidence: stated)
- Together AI serves the largest share of MiniMax M3 token usage among providers. ([2:31](https://www.youtube.com/watch?v=AVMr9PMINyo&t=151s), confidence: stated)
- Training multimodal from step zero, rather than adding vision later, produces text tokens that naturally attend to visual tokens — and other labs typically see model collapse in this regime, a problem MiniMax says it solved. ([10:44](https://www.youtube.com/watch?v=AVMr9PMINyo&t=644s), confidence: stated)
- For long-horizon agentic RL (kernel optimization, paper replication), the decisive factors are data, environment design, and reward formulation rather than the model architecture or base algorithm. ([14:17](https://www.youtube.com/watch?v=AVMr9PMINyo&t=857s), confidence: stated)
- Long-horizon RL evaluation must use intermediate per-iteration scoring plus held-out validation, because models hack the reward and terminal success alone is not trustworthy. ([15:08](https://www.youtube.com/watch?v=AVMr9PMINyo&t=908s), confidence: stated)
- Agentic and coding workloads require a materially different inference stack than chat workloads, because whole codebases in context change the caching, routing, and kernel optimization targets. ([9:39](https://www.youtube.com/watch?v=AVMr9PMINyo&t=579s), confidence: stated)
- There is no single highest-leverage inference optimization; the correct strategy is to exhaustively pursue every available edge rather than prioritize a few. ([12:03](https://www.youtube.com/watch?v=AVMr9PMINyo&t=723s), confidence: stated)
- KV cache handling at 500K–1M context under concurrency is fundamentally a distributed file system / database problem, and is not conceptually hard — just unfamiliar to most ML practitioners. ([16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s), confidence: stated)
- GPUs are significantly underutilized today, and current flop utilization levels should already be considered embarrassing. ([17:38](https://www.youtube.com/watch?v=AVMr9PMINyo&t=1058s), confidence: stated)
- The open-source frontier has largely caught up with closed frontier labs, and the recurring claim that OpenAI and Anthropic are far ahead should be put to rest. ([18:09](https://www.youtube.com/watch?v=AVMr9PMINyo&t=1089s), confidence: stated)
- Lessons from optimizing one model's sparse attention transfer to other models' sparse attention variants, so inference work does not restart from scratch per model. ([13:02](https://www.youtube.com/watch?v=AVMr9PMINyo&t=782s), confidence: stated)
- Using models to accelerate internal development compounds, and that acceleration is the mechanism by which open-weight labs close the gap with frontier labs. ([19:29](https://www.youtube.com/watch?v=AVMr9PMINyo&t=1169s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [benchmark saturation](../concepts/benchmark-saturation.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [long-context processing](../concepts/long-context-processing.md)
- [model portability](../concepts/model-portability.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [vision-language models](../concepts/vision-language-models.md)

