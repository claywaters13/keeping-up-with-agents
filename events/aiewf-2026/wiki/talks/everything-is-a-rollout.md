---
title: "Everything Is a Rollout"
type: "talk"
slug: "everything-is-a-rollout"
track: "Evals"
org: "Terminal-Bench, Harbor, Laude Institute"
day: "Day 3 — Session Day 2"
room: "Track 5"
video_id: "jRCpXUjz4CI"
duration_sec: 1271
word_count: 3665
speakers: ["Alex Shaw", "Ryan Marten"]
---

# Everything Is a Rollout

**Speakers:** [Alex Shaw](../speakers/alex-shaw.md), [Ryan Marten](../speakers/ryan-marten.md)

**Org:** Terminal-Bench, Harbor, Laude Institute

**Track:** Evals &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 21m 11s

[Watch on YouTube](https://www.youtube.com/watch?v=jRCpXUjz4CI)

## Summary

Alex Shaw of the Laude Institute argues that building agents is far closer to machine learning than to traditional software engineering, and that the tooling ecosystem for this shift barely exists yet. He maps ML primitives onto agent development — training data becomes environments, weights become skills/prompts/tools/model choice, the loss function becomes environment rewards, gradient descent becomes a pull request, and overfitting becomes reward hacking — and argues each needs its own tooling. He then introduces Harbor, an open-source format, framework, and registry for agentic environments, where an environment is an instruction plus a sandbox plus a verifier, and every operation is a 'rollout': start a sandbox, hand it to an agent, hand it to a verifier, collect a reward. The claim with the widest reach is that every company using computers should build its own evals, because owning an eval moves the power from vendor brand to your own cost/performance decisions. Worth watching if you're deciding how to evaluate agents, or want a survey of what teams (Cognition, Ramp, Scale, Poolside, Snorkel, LangChain) are actually building on shared environment formats.

## Key Points

- Traditional software engineering is defined by knowing what code will do before running it; swapping a regex for a model call breaks that guarantee, and uncertainty compounds as task complexity grows.
- Agent development should be treated as machine learning, with a direct mapping: environments as training and validation data, skills/prompts/tools/model as weights, environment rewards as the loss function, context-based optimization (GEPA, agent-in-a-loop) as the optimizer, pull requests as gradient steps, and reward hacking as overfitting.
- An environment is three things: an instruction, a sandbox for the agent to act in, and a verifier (programmatic tests, rubrics, or a judging agent) that decides whether the task was accomplished.
- The Harbor rollout — start sandbox, pass to agent, run to a stopping condition, pass sandbox to verifier, collect reward, aggregate across a dataset — is a single universal primitive underlying eval, training data collection, RL, and batch agent work.
- Harbor's directory layout for specifying environments has become a de facto standard, which makes environments interoperable and transferable between organizations.
- Shaw argues every company that uses computers needs its own evals, and identifies four eval types teams actually build: how well agents build your product, how well agents use your product, how well agents power product features, and how well agents automate internal processes.
- Owning an eval shifts power to the buyer — you can compare every model on your own use cases instead of trusting brand or public benchmarks, and pick your own point on the cost/performance frontier.
- An emergent, unplanned use case is 'agentic map reduce': running thousands of agents on distributed sandboxes in parallel and intelligently aggregating results, using a cheap model for the map step and a stronger one for the reduce step.
- There is already a multibillion-dollar market in authored environment/task data sold to labs training models.

## Notable Quotes

> "one thing for sure that they'll say is software engineering was when you knew what the code would do before you ran it"
>
> — [2:21](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=141s) &middot; *The talk's central framing of what has changed, stated as an epitaph for an era.*

> "Generated code is best treated as a blackbox artifact whose behavior and generalization should be managed via empirical evaluation like with any ML model."
>
> — [3:00](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=180s) &middot; *The Chollet tweet the entire argument is built on and later generalized.*

> "And I can say with 100% confidence what will happen if I run this program 1 million times in a row."
>
> — [3:43](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=223s) &middot; *Sets up the determinism baseline that the model-call version destroys.*

> "however, if I ran this exact program one million times, I'm not 100% confident that it will print the same thing every single time or that I know exactly what it will print"
>
> — [4:29](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=269s) &middot; *The concrete before/after that motivates empirical evaluation over reasoning about code.*

> "and I say agent performance itself is best treated as a blackbox artifact"
>
> — [5:12](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=312s) &middot; *Shaw's own generalization beyond code generation to all agent behavior.*

> "your gradient descent step looks like a pull request into your repo. And overfitting looks like reward hacking"
>
> — [6:01](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=361s) &middot; *The sharpest instance of the ML-to-agents mapping that structures the talk.*

> "already the number of people using and building agents is probably magnitudes larger than the number of people that ever uh were doing machine learning and that trend will will only continue"
>
> — [6:49](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=409s) &middot; *The market-size argument for why this tooling gap matters.*

> "And then we need some way of telling whether or not the agent actually did the thing that we told it to do in the sandbox within some amount of time or other stopping condition. And that's your verifier"
>
> — [8:13](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=493s) &middot; *Defines the verifier, the load-bearing component of an environment.*

> "this uh specific directory layout has become relatively standard in a lot of the environment space"
>
> — [8:51](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=531s) &middot; *Claims de facto standardization, the basis for the interoperability pitch.*

> "Two, it's an open-source framework for performing rollouts in parallel using any agent with any model in any sandbox on any task."
>
> — [10:49](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=649s) &middot; *The clearest one-line statement of what Harbor is.*

> "I think we have like three or 400 Aval sets by now. And in fact, I think two or three benchmarks even came out today that run with Harbor."
>
> — [10:49](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=649s) &middot; *Concrete adoption numbers as of the talk.*

> "And the answer is every single company that uses computers. And I think that's probably close to all of the companies in the world."
>
> — [11:22](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=682s) &middot; *The talk's boldest and most contestable prescription about who needs evals.*

> "if you want to build an agentic system start with the aval that matters and your ability to grade the outcome and then say I welcome all models"
>
> — [11:22](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=682s) &middot; *Cited Nadella quote used as the strategic case for eval-first development.*

> "as soon as you have an aval the power is now in your hands. You can consider every single model. You don't have to trust brand. You don't have to trust somebody else's aval."
>
> — [12:06](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=726s) &middot; *States the buyer-power thesis behind owning evals rather than reading leaderboards.*

> "what that allows them to do is pick the coding agent or the model that performs best on their internal use cases and they don't have to you know maximize token spend"
>
> — [12:45](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=765s) &middot; *Names the cost/performance tradeoff internal benchmarks are meant to resolve.*

> "if you can make an aval to see how well agents use your product and then iterate on your product to make it more usable for agents, you're going to get more usage"
>
> — [13:24](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=804s) &middot; *Extends evals from model selection to product design for agent consumers.*

> "which allows you to launch the rollouts on harbor servers which means you can just fire and forget and go to sleep and then come back the next day and 10,000 rollouts are done for you"
>
> — [14:35](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=875s) &middot; *Describes the throughput model that makes large-scale rollouts practical.*

> "there's actually like a multibillion dollar market right now that exists probably around harbor data and also other types of data"
>
> — [15:09](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=909s) &middot; *Reports the scale of the environment-authoring economy.*

> "agentic map reduce which is you just want to run a ton of agents on distributed compute"
>
> — [15:49](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=949s) &middot; *Names an emergent use case the framework wasn't designed for.*

> "I do the map step with cursor CLI because it's cheap and fast. And then I do the reduce step with fable 5 because I wanted to have like an accurate summary"
>
> — [17:19](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=1039s) &middot; *Concrete model-routing tradeoff inside a single distributed job.*

## Positions

- Agent development is more similar to machine learning than to software engineering, and should use ML-style tooling and guard against ML-style pitfalls. ([5:12](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=312s), confidence: stated)
- Agent performance, not just generated code, should be treated as a black-box artifact managed through empirical evaluation. ([5:12](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=312s), confidence: stated)
- The tooling layer for agent development (environments, rewards, optimizers, eval platforms) is essentially unbuilt compared to the mature ML tooling ecosystem. ([6:49](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=409s), confidence: stated)
- The population of people building agents already exceeds the population that ever did machine learning by orders of magnitude. ([6:49](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=409s), confidence: stated)
- Every company that uses computers should be building its own evals. ([11:22](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=682s), confidence: stated)
- Public benchmarks and vendor brand are insufficient bases for model selection; only your own eval lets you choose on the cost/performance frontier. ([12:06](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=726s), confidence: stated)
- The correct order of operations is build the eval first, then optimize against it. ([12:06](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=726s), confidence: stated)
- Software products are moving toward offering headless modes, and making a product more usable by agents will increase its usage and value. ([13:24](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=804s), confidence: stated)
- A single rollout primitive (sandbox → agent → verifier → reward) is universal enough to serve evaluation, SFT data collection, reinforcement learning, and non-eval batch agent workloads. ([10:08](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=608s), confidence: stated)
- A shared, interoperable environment format increases data velocity and accelerates industry-wide progress. ([10:49](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=649s), confidence: stated)
- Because rollouts are slow, parallelization is the main lever for tightening the agent development loop. ([15:09](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=909s), confidence: stated)
- Cheap fast models suffice for wide parallel map steps while stronger models should be reserved for aggregation/reduce steps where accuracy matters. ([17:19](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=1039s), confidence: implied)

## Concepts

- [agent sandboxing](../concepts/agent-sandboxing.md)
- [benchmark design](../concepts/benchmark-design.md)
- [context engineering](../concepts/context-engineering.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [parallel agent execution](../concepts/parallel-agent-execution.md)
- [post-training](../concepts/post-training.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)
- [verifier design](../concepts/verifier-design.md)

