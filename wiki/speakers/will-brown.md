---
title: "Will Brown"
type: "speaker"
slug: "will-brown"
role: "Researcher"
company: "Prime Intellect"
talk_count: 2
---

# Will Brown

**Researcher &middot; Prime Intellect**

Will Brown leads Applied Research at Prime Intellect and builds open research infrastructure to enable every company to train, deploy, and self-improve their own frontier agentic models. He holds a PhD in Computer Science from Columbia University.

[LinkedIn](https://www.linkedin.com/in/willcb/)

## Talks

- [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md) (Post-training)
- [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md) (Posttraining & Midtraining)

## Scheduled Sessions

- **The Prime Intellect Stack** &middot; Day 1 — Workshop Day &middot; 4:30pm-5:30pm &middot; Track 6
- **Reinforcement Learning without Verifiable Rewards** &middot; Day 3 — Session Day 2 &middot; 1:30pm-1:50pm &middot; Track 9

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [benchmark design](../concepts/benchmark-design.md)
- [continual learning](../concepts/continual-learning.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [post-training](../concepts/post-training.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [reward design](../concepts/reward-design.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [rubric design](../concepts/rubric-design.md)
- [simulation environments](../concepts/simulation-environments.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)
- [world models](../concepts/world-models.md)

## Quotes

> "evals are the thing that opens the door to post-training. And so environments and evals are essentially the same thing."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [6:37](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=397s)

> "why should I do post-training if the the frontier models are going to get better? Well, your model should get better, too."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [8:11](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=491s)

> "what you really want is to be able to not just post-train like today, but to be able to uh, have this iterative process of model refinement, and the sort of thing where you can kind of have the training compute end up be a pretty small fraction of your overall inference budget"
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [8:39](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=519s)

> "getting this signal from the real world isn't trivial. Like that's kind of largely an open question as to like how you go about um, getting information from real world feedback into your environments."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [8:39](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=519s)

> "we found ourselves repeating a lot of work of like adding patterns for a CLI agent or adding patterns for MCP."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [9:40](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=580s)

> "we've really embraced this decorator pattern. We found it to be very useful. We also if you were a rubric fan, we killed rubric."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [16:13](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=973s)

> "in in many RL frameworks it's actually quite hard to do group rewards because things are very decoupled and things kind of assume that all rollouts are going to live independently and that they don't need to talk to each other."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [17:22](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1042s)

> "you don't know the optimal length for a problem. Like if I give you a math problem, I could say, "Oh, solve it in less than N tokens." But also like who knows what the right N is."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [18:36](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1116s)

> "juggling multiple objectives simultaneously is kind of one of the hard challenges in RL in reward design."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [19:37](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1177s)

> "the the harness doesn't know that it's doing RL. The harness just is a harness running as if it would be running in a real-world environment."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [22:26](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1346s)

> "chat templates if people have spent time debugging with them, it sucks. Ginger is awful."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [25:14](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1514s)

> "this has revealed to us like going through all of the the things here like why opening eye responses decided to be stateful. There are some kind of like unavoidable issues that kind of come up when you're doing large-scale agentic rollouts"
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [27:23](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1643s)

> "some people I think have their reasons for wanting to do synchronous training. I don't agree with them."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [29:16](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1756s)

> "we can do um a GLM-5 step on 28 nodes in less than 5 minutes for long horizon coding tasks with 131K context, um which means you can do a 1,000-step run in 3 days."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [31:39](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1899s)

> "And that costs for rental prices about 50K. And so 50K is not cheap, but it's like if you're doing a full run on a frontier size model on like a proper real world agent environment, like it's a lot cheaper than what OpenAI's raising for it."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [32:27](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1947s)

> "one of the goals of async RL is to have your like forward progress speed not be tied to the speed of your individual rollout."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [33:25](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2005s)

> "you want to have a system where it's okay if there are pockets of your life cycle that don't use GPU time but do use time um and you can kind of overlap these without kind of wasting GPU cycles."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [33:59](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2039s)

> "Torch Titan is just like really easy to like hack, and Megatron is kind of this monolith"
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [36:45](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2205s)

> "our whole research team that maintains Prim Rels like less than 10 people, um and the company is less than 40 people."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [37:37](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2257s)

> "we do very open research work like all this code is on GitHub if you want to go play with it but we also like our a real company that trains big models and makes money."
>
> — [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [45:43](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2743s)

> "often we don't actually have verifiable rewards. And so messy real world tasks often we're kind of figuring out as we go."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [0:13](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=13s)

> "So I think a lot of people think RL when they think environment, but environments and evals are really the same thing."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [4:05](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=245s)

> "And the goal that we're really trying to enable is more people to be able to become their own research lab"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [3:29](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=209s)

> "classical machine learning will tell you you can train for the distribution, but generalizing outside of the distribution is kind of an undefined problem."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [5:48](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=348s)

> "reward hacking is when you have a kind of loose proxy for your objective that is undefined at the boundaries"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [6:20](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=380s)

> "And I think currently the level of abstraction for doing this is far too low for it to be practical for most people."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [7:11](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=431s)

> "RL's great for refining skills, but less so for incorporating like dense new knowledge."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [7:48](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=468s)

> "grounding is one where you have some source material and the ability to do an AB test of like with and without is a very useful way of creating this kind of capability gap where a model will do better if it has something in context"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [8:25](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=505s)

> "Judges are also really useful. We're relying on the fact that LLMs are already really powerful general reasoners for many things."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [9:06](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=546s)

> "what we found is super helpful is taking existing traces from a deployed agent and treating these as the source material"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [9:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=581s)

> "You can verify the easy problem and then learn on the hard problem."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [11:17](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=677s)

> "this idea of wanting to know that an end state is reachable and that you can then take steps back, throw away the solution, and then learn to find it again"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [11:52](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=712s)

> "There are some MCP tools or CLI tools or websites or applications where we can't actually program them yet. And so, what we want to do is learn to simulate them."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [12:24](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=744s)

> "And so, you can actually do this reverse engineering where you get to kind of plant the answer."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [13:01](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=781s)

> "a lot of times we will have a model that does something and it will make mistakes along the way and it's easier to tell what went wrong in hindsight."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [13:31](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=811s)

> "you want tasks that are not too easy, not too hard and you want to be searching for these and iterating on generating more of them"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [14:08](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=848s)

> "there are things that don't show up until you actually like start doing RL"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [15:54](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=954s)

> "And ultimately what you want is to surface the most important pieces up to the human"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [16:27](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=987s)

> "We have a blog called general agent which is demonstrating this for tool use, this online loop of generating, solving, and synthesizing new tasks and gating based on this pass rate which then we train on and we see a great uplift on popular benchmarks for tool use."
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [16:57](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1017s)

> "in the same way that with coding agents we're kind of going to higher levels of abstraction, we can do this with environment and reward design as well"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [18:04](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1084s)

> "models are then able to stay within the guardrails we give them, they go find the issues in production, and then they turn these back into new tasks that can then be trained on for getting better in the real world"
>
> — [Reinforcement Learning without Verifiable Rewards](../talks/reinforcement-learning-without-verifiable-rewards.md), [18:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1121s)

