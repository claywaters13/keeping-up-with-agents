---
title: "Modern Post-Training: A Deep Dive"
type: "talk"
slug: "modern-post-training-a-deep-dive"
track: "Post-training"
org: "Prime Intellect"
video_id: "V-EDrhIhHzQ"
duration_sec: 2812
word_count: 10237
speakers: ["Will Brown"]
---

# Modern Post-Training: A Deep Dive

**Speakers:** [Will Brown](../speakers/will-brown.md)

**Org:** Prime Intellect

**Track:** Post-training &nbsp;|&nbsp; **Duration:** 46m 52s

[Watch on YouTube](https://www.youtube.com/watch?v=V-EDrhIhHzQ)

## Summary

Will Brown of Prime Intellect walks through what modern post-training actually looks like in practice, using the company's open-source stack (Verifiers for environments, Prime-RL for training) as the concrete example. The core argument is that environments — decomposed into task sets, harnesses, and runtimes — are the universal unit for evals, SFT, RL, and on-policy distillation alike, so building evals is the on-ramp to post-training rather than a separate activity. He details the V1 Verifiers refactor, including an 'interception server' that lets unmodified real agent harnesses (Codex, Claude Code) be trained without knowing they're doing RL, and a 'renderers' library that fixes the chat-template/tokenizer mismatches that silently corrupt long training runs. On the systems side he argues async RL is the only sane choice once rollouts have hours-long tails, and reports a GLM-5 RL run at 28 nodes doing a step in under 5 minutes with 131K context — a 1,000-step run in 3 days for about $50K. Worth watching if you're deciding whether in-house post-training is economically and operationally reachable, or want a map of how RL infrastructure is being factored today.

## Key Points

- Environments should be understood as a general specification language — data, harness, interaction, and scoring — that serves evaluation, SFT data generation, RL, and on-policy distillation with the same primitives, so evals are the natural entry point to post-training.
- Verifiers V1 decomposes environments into three composable pieces — task set (agent-agnostic data and rules), harness (the agent loop, possibly a real CLI agent), and runtime (local, Docker, or sandboxes) — replacing the older monolithic multi-turn/tool environment pattern.
- The interception server gives each harness rollout a fake OpenAI- or Anthropic-compatible base URL so unmodified production harnesses can be used for RL without retrofitting, letting the same code move between training and deployment.
- Tokenization mismatches between chat templates and re-tokenized messages cause subtle numerical problems late in large training runs; Prime Intellect released a standalone 'renderers' library that turns chat templates into programmable artifacts to keep message space and token space cleanly interoperable.
- Group-level rewards are treated as first class because they enable things most RL frameworks make hard — pairwise judging, ranking, and conciseness bonuses that exploit within-group variance to control runaway chain-of-thought length without knowing the optimal token budget in advance.
- Prime-RL is async from the ground up and Brown explicitly rejects synchronous training: overlapping long-tail agent rollouts (30 seconds to 3 hours) means accepting some off-policyness, typically around 16 steps of staleness on average.
- Reported scale numbers: a GLM-5 step on 28 nodes in under 5 minutes at 131K context for long-horizon coding tasks, so a 1,000-step run takes 3 days at roughly $50K rental cost — which he argues is justifiable for enterprises already spending comparable amounts on inference tokens.
- Training algorithms are factored into a 'loss' (what takes the gradient) and an 'algorithm' (what prepares the data), so GRPO, SFT, on-policy distillation, self-distillation, and Echo-style objectives can be mixed and matched per environment without changing the infrastructure.
- The hosted platform ships multi-tenant LoRA today — enabling token-based pricing without reserving GPUs — with full fine-tuning coming within weeks for cases like large-scale SFT or mid-training where an adapter isn't enough.

## Notable Quotes

> "evals are the thing that opens the door to post-training. And so environments and evals are essentially the same thing."
>
> — [6:37](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=397s) &middot; *compresses the talk's central framing into one line*

> "why should I do post-training if the the frontier models are going to get better? Well, your model should get better, too."
>
> — [8:11](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=491s) &middot; *answers the most common objection to investing in post-training*

> "what you really want is to be able to not just post-train like today, but to be able to uh, have this iterative process of model refinement, and the sort of thing where you can kind of have the training compute end up be a pretty small fraction of your overall inference budget"
>
> — [8:39](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=519s) &middot; *states the economic case as a ratio rather than a slogan*

> "getting this signal from the real world isn't trivial. Like that's kind of largely an open question as to like how you go about um, getting information from real world feedback into your environments."
>
> — [8:39](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=519s) &middot; *an honest admission of the unsolved part of the flywheel*

> "we found ourselves repeating a lot of work of like adding patterns for a CLI agent or adding patterns for MCP."
>
> — [9:40](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=580s) &middot; *the concrete motivation for the V1 refactor*

> "we've really embraced this decorator pattern. We found it to be very useful. We also if you were a rubric fan, we killed rubric."
>
> — [16:13](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=973s) &middot; *a breaking API decision stated bluntly*

> "in in many RL frameworks it's actually quite hard to do group rewards because things are very decoupled and things kind of assume that all rollouts are going to live independently and that they don't need to talk to each other."
>
> — [17:22](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1042s) &middot; *names a specific gap in competing tooling*

> "you don't know the optimal length for a problem. Like if I give you a math problem, I could say, "Oh, solve it in less than N tokens." But also like who knows what the right N is."
>
> — [18:36](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1116s) &middot; *clean statement of why length penalties need group-relative design*

> "juggling multiple objectives simultaneously is kind of one of the hard challenges in RL in reward design."
>
> — [19:37](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1177s) &middot; *names the core difficulty of reward engineering*

> "the the harness doesn't know that it's doing RL. The harness just is a harness running as if it would be running in a real-world environment."
>
> — [22:26](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1346s) &middot; *the design principle behind the interception server*

> "chat templates if people have spent time debugging with them, it sucks. Ginger is awful."
>
> — [25:14](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1514s) &middot; *the visceral motivation for the renderers library (Jinja, mis-transcribed)*

> "this has revealed to us like going through all of the the things here like why opening eye responses decided to be stateful. There are some kind of like unavoidable issues that kind of come up when you're doing large-scale agentic rollouts"
>
> — [27:23](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1643s) &middot; *a changed mind on stateless vs stateful LLM APIs*

> "some people I think have their reasons for wanting to do synchronous training. I don't agree with them."
>
> — [29:16](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1756s) &middot; *the talk's sharpest contested position*

> "we can do um a GLM-5 step on 28 nodes in less than 5 minutes for long horizon coding tasks with 131K context, um which means you can do a 1,000-step run in 3 days."
>
> — [31:39](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1899s) &middot; *the headline performance number*

> "And that costs for rental prices about 50K. And so 50K is not cheap, but it's like if you're doing a full run on a frontier size model on like a proper real world agent environment, like it's a lot cheaper than what OpenAI's raising for it."
>
> — [32:27](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1947s) &middot; *puts a dollar figure on frontier-scale RL for enterprises*

> "one of the goals of async RL is to have your like forward progress speed not be tied to the speed of your individual rollout."
>
> — [33:25](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2005s) &middot; *the one-sentence rationale for async*

> "you want to have a system where it's okay if there are pockets of your life cycle that don't use GPU time but do use time um and you can kind of overlap these without kind of wasting GPU cycles."
>
> — [33:59](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2039s) &middot; *reframes async RL as GPU utilization rather than algorithmic purity*

> "Torch Titan is just like really easy to like hack, and Megatron is kind of this monolith"
>
> — [36:45](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2205s) &middot; *a defensible framework choice most training stacks answer differently*

> "our whole research team that maintains Prim Rels like less than 10 people, um and the company is less than 40 people."
>
> — [37:37](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2257s) &middot; *sizes the team behind all the claimed infrastructure*

> "we do very open research work like all this code is on GitHub if you want to go play with it but we also like our a real company that trains big models and makes money."
>
> — [45:43](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2743s) &middot; *states the open-source business thesis explicitly*

## Positions

- Environments and evals are the same unit of logic, so building evals is a prerequisite for and on-ramp to post-training rather than a separate track. ([6:37](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=397s), confidence: stated)
- Synchronous RL training is the wrong choice; the off-policyness of async is worth accepting because agent rollouts have long tails. ([29:16](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1756s), confidence: stated)
- Running roughly 16 steps off-policy on average is empirically fine for RL stability. ([33:59](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2039s), confidence: stated)
- SFT data pipelines that export, reformat, and re-upload datasets are unnecessary — SFT is just rollouts in an environment where the actor is a teacher. ([11:27](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=687s), confidence: stated)
- Frontier-scale RL is now economically accessible to enterprises: ~$50K buys a 1,000-step GLM-5 run on real agentic coding tasks, comparable to a month of token spend. ([32:27](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1947s), confidence: stated)
- Torch Titan is a better base for a hackable training framework than Megatron. ([36:45](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=2205s), confidence: stated)
- Chat templates and Jinja are a significant source of trainer/inference mismatch, and replacing them with programmable renderers is necessary for stable large-scale runs. ([25:14](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1514s), confidence: stated)
- Stateful LLM APIs like OpenAI's Responses API were the right call, because agentic rollouts make token-level state management unavoidable. ([27:23](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1643s), confidence: stated)
- Training multiple RL experts on a shared base model and distilling them into one checkpoint is more reliable than training a single model on many environments at once. ([7:42](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=462s), confidence: stated)
- Models will grow their chains of thought without bound unless reward design actively counteracts it. ([18:36](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1116s), confidence: stated)
- Coupling training, inference, and environments into one stack is a design mistake because it prevents using environments as standalone evals. ([30:56](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1856s), confidence: implied)
- The right architecture keeps harness code ignorant of RL entirely, so the same harness runs in training and production. ([22:26](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1346s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [post-training](../concepts/post-training.md)
- [reward design](../concepts/reward-design.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [simulation environments](../concepts/simulation-environments.md)

