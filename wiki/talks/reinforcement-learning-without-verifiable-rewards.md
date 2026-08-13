---
title: "Reinforcement Learning without Verifiable Rewards"
type: "talk"
slug: "reinforcement-learning-without-verifiable-rewards"
track: "Posttraining & Midtraining"
org: "Prime Intellect"
day: "Day 3 — Session Day 2"
room: "Track 9"
video_id: "AQv3qRCG6Gw"
duration_sec: 1166
word_count: 4154
speakers: ["Will Brown"]
---

# Reinforcement Learning without Verifiable Rewards

**Speakers:** [Will Brown](../speakers/will-brown.md)

**Org:** Prime Intellect

**Track:** Posttraining & Midtraining &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 19m 26s

[Watch on YouTube](https://www.youtube.com/watch?v=AQv3qRCG6Gw)

## Summary

Will Brown of Prime Intellect argues that RL with verifiable rewards (RLVR) covers only the easy cases — math, code tests, deterministic tool state — while most real agent work (reports, bookings, refunds, browser and tool use) has no clean check for correctness. The talk is a practical catalogue of how to manufacture training signal anyway: ground tasks in real source material (production traces, doc corpora, repos), work backwards from known-reachable end states so you can verify the easy problem and train on the hard one, build high-fidelity simulators of back-ends you can't program, and spend test-time compute on judges, rubrics, difficulty calibration, and reward-hack mining. He frames environments as the unifying artifact — the same object serves evals, SFT data generation, prompt optimization, and RL — and positions continual learning as the goal: agents deployed in production that turn their own failures into new trainable tasks. Worth watching if you're trying to move RL past benchmark-shaped tasks and want a concrete menu of signal-generation techniques plus the failure modes (reward hacking, out-of-distribution generalization) that come with them.

## Key Points

- Most valuable real-world agent tasks lack verifiable rewards, so the hard problem is manufacturing supervision rather than running the RL algorithm itself.
- Environments (tasks + harness + rewards) are the same objects as evals, and can be reused for static SFT data generation, on-policy distillation, prompt optimization, and as a scientific test bed for harness iteration.
- The 'work backwards' principle — start from a solution or known-reachable end state, throw it away, and train the model to rediscover it — yields free supervision and generalizes from doc QA to code PRs to simulated web apps.
- Production agent traces are the preferred source material because they define the real task distribution before you have any labels, which is what makes continual learning possible.
- When back-end systems (MCP tools, CLIs, websites) can't be programmatically controlled, learn to simulate them; simulators give full back-end controllability so you can plant answers and bake in verifiability the real deployment lacks.
- Test-time compute can be spent across the whole pipeline — mining traces, calibrating task difficulty into the not-too-easy/not-too-hard band RL needs, refining simulators, extracting rubrics, and red-teaming for reward hacks.
- Reward hacking is treated as a boundary problem: loose proxies undefined at the edges get exploited, and hindsight review with accumulated hack corpora catches what in-context instructions to judges do not.
- RL refines skills but doesn't inject dense new knowledge; blending it with supervised signal from the environment gives the model a native world model of what to expect from its tools.
- Small training runs must be folded into environment design, since some pathologies only surface once you actually start doing RL.

## Notable Quotes

> "often we don't actually have verifiable rewards. And so messy real world tasks often we're kind of figuring out as we go."
>
> — [0:13](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=13s) &middot; *States the talk's premise and the gap it targets.*

> "So I think a lot of people think RL when they think environment, but environments and evals are really the same thing."
>
> — [4:05](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=245s) &middot; *A reframing others might contest, and the basis for reusing one artifact across evals, SFT, and RL.*

> "And the goal that we're really trying to enable is more people to be able to become their own research lab"
>
> — [3:29](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=209s) &middot; *Names the thesis behind Prime Intellect's tooling stack.*

> "classical machine learning will tell you you can train for the distribution, but generalizing outside of the distribution is kind of an undefined problem."
>
> — [5:48](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=348s) &middot; *Concise statement of why unbounded real-world tasks resist standard eval construction.*

> "reward hacking is when you have a kind of loose proxy for your objective that is undefined at the boundaries"
>
> — [6:20](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=380s) &middot; *A crisp working definition that pins the failure to reward design, not model malice.*

> "And I think currently the level of abstraction for doing this is far too low for it to be practical for most people."
>
> — [7:11](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=431s) &middot; *The core critique of the current continual-learning tooling landscape.*

> "RL's great for refining skills, but less so for incorporating like dense new knowledge."
>
> — [7:48](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=468s) &middot; *Names a tradeoff that motivates blending RL with supervised environment signal.*

> "grounding is one where you have some source material and the ability to do an AB test of like with and without is a very useful way of creating this kind of capability gap where a model will do better if it has something in context"
>
> — [8:25](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=505s) &middot; *Explains the mechanism by which grounding produces learnable signal.*

> "Judges are also really useful. We're relying on the fact that LLMs are already really powerful general reasoners for many things."
>
> — [9:06](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=546s) &middot; *States the assumption underpinning LLM-as-judge reward design.*

> "what we found is super helpful is taking existing traces from a deployed agent and treating these as the source material"
>
> — [9:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=581s) &middot; *The concrete recommendation for where to get tasks when no benchmark exists.*

> "You can verify the easy problem and then learn on the hard problem."
>
> — [11:17](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=677s) &middot; *The single sentence that captures the working-backwards technique.*

> "this idea of wanting to know that an end state is reachable and that you can then take steps back, throw away the solution, and then learn to find it again"
>
> — [11:52](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=712s) &middot; *Generalizes the code-PR construction into a reusable recipe.*

> "There are some MCP tools or CLI tools or websites or applications where we can't actually program them yet. And so, what we want to do is learn to simulate them."
>
> — [12:24](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=744s) &middot; *Frames world simulators as the answer to uncontrollable back-ends.*

> "And so, you can actually do this reverse engineering where you get to kind of plant the answer."
>
> — [13:01](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=781s) &middot; *Names the concrete advantage simulators hold over real production environments.*

> "a lot of times we will have a model that does something and it will make mistakes along the way and it's easier to tell what went wrong in hindsight."
>
> — [13:31](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=811s) &middot; *The asymmetry that justifies spending compute on retrospective judging and rubric extraction.*

> "you want tasks that are not too easy, not too hard and you want to be searching for these and iterating on generating more of them"
>
> — [14:08](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=848s) &middot; *States the difficulty-calibration requirement that follows from how advantages are computed.*

> "there are things that don't show up until you actually like start doing RL"
>
> — [15:54](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=954s) &middot; *Argues environment design can't be validated offline alone.*

> "And ultimately what you want is to surface the most important pieces up to the human"
>
> — [16:27](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=987s) &middot; *Defines where human expertise should sit in an otherwise automated loop.*

> "We have a blog called general agent which is demonstrating this for tool use, this online loop of generating, solving, and synthesizing new tasks and gating based on this pass rate which then we train on and we see a great uplift on popular benchmarks for tool use."
>
> — [16:57](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1017s) &middot; *The one concrete empirical result cited for the whole pipeline.*

> "in the same way that with coding agents we're kind of going to higher levels of abstraction, we can do this with environment and reward design as well"
>
> — [18:04](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1084s) &middot; *The analogy that frames the talk's bet about where post-training tooling is headed.*

> "models are then able to stay within the guardrails we give them, they go find the issues in production, and then they turn these back into new tasks that can then be trained on for getting better in the real world"
>
> — [18:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1121s) &middot; *Closes the continual-learning loop the talk builds toward.*

## Positions

- Environments and evals are the same objects, and one environment can serve RL, SFT data generation, on-policy distillation, and prompt optimization. ([4:05](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=245s), confidence: stated)
- Most real-world agent tasks are not verifiable; verifiable rewards (math answers, code tests, database state) are the easy special case. ([4:38](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=278s), confidence: stated)
- Handcrafted benchmarks of a few hundred expert-built tasks are not a scalable basis for training on open-ended real-world work. ([5:13](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=313s), confidence: stated)
- Generalizing outside the training distribution is an undefined problem in classical ML terms, so the distribution must be discovered from deployment rather than specified up front. ([5:48](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=348s), confidence: stated)
- Reward hacking arises specifically from proxies that are undefined at the boundaries, and models trained with RL will find those weaknesses. ([6:20](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=380s), confidence: stated)
- The current level of abstraction for continual learning is too low to be practical for most practitioners, and most of the difficult steps are in fact automatable. ([7:11](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=431s), confidence: stated)
- RL is effective at refining existing skills but poor at incorporating dense new knowledge into the model. ([7:48](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=468s), confidence: stated)
- Deployed production traces are the best available source material for constructing tasks when no labels exist. ([9:41](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=581s), confidence: stated)
- Working backwards from a known-reachable end state yields supervision for free and applies well beyond code. ([11:17](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=677s), confidence: stated)
- Learned simulators are better RL environments than real production systems because full back-end controllability lets you plant answers and guarantee solvability. ([12:24](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=744s), confidence: stated)
- Judging in hindsight — after seeing the full chain of events, or by polling several models — is more reliable than judging or instructing against failures in advance. ([13:31](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=811s), confidence: stated)
- RL requires tasks calibrated to intermediate difficulty, because the advantage signal depends on separation across a set of rollouts. ([14:08](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=848s), confidence: stated)
- Simple hindsight review catches most reward hacks in practice, whereas telling a judge model not to allow a behavior does not prevent it in the rollout. ([15:15](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=915s), confidence: stated)
- Small training runs must be part of environment design because some problems only appear once RL is actually running. ([15:54](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=954s), confidence: stated)
- Humans should be reserved for the highest-level judgments about goals and quality, with compute handling the rest of environment refinement. ([16:27](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=987s), confidence: stated)
- An online loop of generating, solving, and synthesizing tasks gated on pass rate produced a large uplift on popular tool-use benchmarks. ([16:57](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1017s), confidence: stated)
- Supervised learning signal from the environment gives the model a likelihood model of environment tokens — a native world model — which RL alone would not produce. ([17:35](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1055s), confidence: stated)
- Environment and reward design will follow coding agents up the abstraction ladder, becoming largely automated. ([18:04](https://www.youtube.com/watch?v=AQv3qRCG6Gw&t=1084s), confidence: implied)

## Concepts

- [benchmark design](../concepts/benchmark-design.md)
- [continual learning](../concepts/continual-learning.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [post-training](../concepts/post-training.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [reward design](../concepts/reward-design.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [rubric design](../concepts/rubric-design.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)
- [world models](../concepts/world-models.md)

