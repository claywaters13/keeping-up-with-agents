---
title: "Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains"
type: "talk"
slug: "morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains"
track: "AI in Finance"
org: "Morgan Stanley"
day: "Day 4 — Session Day 3"
room: "Track 3"
video_id: "kiqubc5b5Yo"
duration_sec: 1206
word_count: 3586
speakers: ["Brendan Rappazzo"]
---

# Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains

*Program title: ALPHALAB: Autonomous Multi-Agent Research Across Optimization Domains with Frontier LLMs*

**Speakers:** [Brendan Rappazzo](../speakers/brendan-rappazzo.md)

**Org:** Morgan Stanley

**Track:** AI in Finance &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 20m 06s

[Watch on YouTube](https://www.youtube.com/watch?v=kiqubc5b5Yo)

## Summary

Brendan Rappazzo describes ALPHALAB, Morgan Stanley's in-house agentic harness for automating quantitative research, built by a ~30-person team of PhD AI researchers. Version 1.0 runs three phases — an open-ended research phase with web search and to-do scaffolding, a multi-agent eval-building phase with builder and critic agents, and a Jira/Kanban-style mass experimentation loop where a strategist agent queues experiments and worker agents implement, submit them to a Slurm GPU cluster, and write postmortems. Results were mixed-to-promising: top 12% on an NVIDIA Kaggle fine-tuning competition with only 10 iterations, better LLM training configs than a Karpathy-style single-agent loop, and several internal model improvements now moving through risk toward production. The bigger argument is the pivot to 2.0: the harness design itself is arbitrary and should be meta-optimized by an LLM against a strict Kaggle-style eval, so all durable enterprise value moves into building 10–20 careful environments with verifiable metrics and qualitative research-process rubrics. Worth watching if you care about auto-research agents, harness self-improvement, or how a regulated financial firm encodes domain expertise into RL environments rather than prompts.

## Key Points

- Morgan Stanley's quant problems are shaped like Kaggle tasks — time series in, calibrated predictions out — which makes them unusually amenable to automated research agents, and being on the sell side reduces adversarial selection pressure.
- The team judged long-horizon auto-research to have become genuinely feasible only around December 2025, with Opus 4.5 plus harnesses like Claude Code and Codex.
- ALPHALAB 1.0 uses no off-the-shelf agent framework; the harness was written from scratch (largely by Claude) with functional tool calling to stay provider-agnostic across closed and open-source models.
- The three core tools are full shell access, web search for reading arXiv and technical blogs, and a Slurm abstraction that lets the agent request hardware without doing orchestration itself.
- Eval construction in 1.0 is a multi-agent loop: a builder agent writes the eval, a conceptual critic hunts for forward leakage and design errors, a programmatic critic writes unit and integration tests, and the loop only ends when all agents are satisfied.
- The experimentation phase is formulated as a Kanban board specifically so humans can steer — cancelling cards, adding their own, and chatting with the strategist agent.
- Reported results include top 12% on an NVIDIA NeMoTron reasoning fine-tune Kaggle competition (with only 10 iterations), beating a single-agent loop on LLM speedrunning, and internal model improvements heading to production.
- ALPHALAB 2.0 inverts the emphasis: the harness in the middle becomes almost disposable and self-improving, while 10–20 carefully built environments serve as the RL signal, combining verifiable metrics with qualitative rubrics that grade rollouts on research process.
- The speaker's thesis is that general auto-research capability will commoditize, so an enterprise's remaining moat is proprietary data plus the hard work of environment design.

## Notable Quotes

> "our group are relatively small. We're about 30 uh PhD AI researchers, and we kind of operate both like kind of half academic, so we're encouraged to um you know, publish papers, open-source code, share our research."
>
> — [0:01](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=1s) &middot; *establishes the unusual half-academic structure of the team behind the work*

> "it wasn't really until December of 2025, and I think this is a pretty common sentiment now that um it really felt possible for the first time with like with Opus 4.5 and with, you know, these harnesses like Claude Code and Codex"
>
> — [2:52](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=172s) &middot; *dates the capability threshold that made the whole project viable*

> "we wanted to build it in a way that you know, as these models get better and better, it's not sort of consuming what we built."
>
> — [3:41](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=221s) &middot; *names the design constraint of not being obsoleted by model progress*

> "so the harness is actually all our own code. So we decided not to use any off-the-shelf agent framework. Um we wrote it all and really Claude wrote it all"
>
> — [6:29](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=389s) &middot; *a concrete, contestable build-vs-adopt decision*

> "I I like this approach of kind of building your own from scratch because you get sort of max freedom and max like, you know, you're you're free to kind of tweak anything you care about."
>
> — [6:29](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=389s) &middot; *states the rationale against agent frameworks*

> "of course the evaluation is the most important piece and LLMs aren't malicious, but they can make, you know, very silly mistakes and if you're optimizing against a bad a bad eval, the whole thing kind of falls apart."
>
> — [9:18](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=558s) &middot; *the central failure mode motivating the 2.0 redesign*

> "One that's told to be more high-level, like are there conceptual errors in our evaluation or any kind of forward leakage of information, and then one that's more programmatic. So it's like writing unit tests and integration tests."
>
> — [10:03](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=603s) &middot; *concretely describes the two-critic eval verification pattern*

> "there's this sort of strategist agent that gets to look and query all the context from the previous steps, and it's just supposed to keep coming up with experiments it wants to try"
>
> — [10:40](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=640s) &middot; *defines the core orchestration role in the experimentation loop*

> "it got in the top 12% of submissions."
>
> — [12:55](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=775s) &middot; *the headline external benchmark number*

> "it only had sort of 10 iterations to work with because we joined late, and I think, you know, AlphaLab works best the more iterations it can explore."
>
> — [13:43](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=823s) &middot; *caveats the benchmark and states a scaling claim about iteration count*

> "isn't it sort of arbitrary, you know, like, how do you motivate these design choices?"
>
> — [14:17](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=857s) &middot; *the speaker voicing the strongest objection to his own architecture*

> "should we be making these decisions at all? Like, this itself is a verifiable loop. Like, an LLM should be doing this this meta-optimization itself."
>
> — [15:00](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=900s) &middot; *the pivot thesis toward meta harness optimization*

> "this is a lesson I learned over and over, like monthly, working with these models, you have to start with good eval."
>
> — [15:40](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=940s) &middot; *hard-won practitioner lesson stated bluntly*

> "we treat it as data and description in, the harness lives in the middle, and its only job is to submit containerized models."
>
> — [15:40](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=940s) &middot; *compresses the entire 2.0 architecture into one sentence*

> "to me evals and environments are the same thing. It's just you train in environments."
>
> — [16:21](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=981s) &middot; *a reusable conceptual claim others might dispute*

> "now what we've done is built on the order of like 10 to 20 really careful environments, and that becomes a reinforcement learning signal."
>
> — [16:21](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=981s) &middot; *reports the scale of the environment investment*

> "we're also doing this qualitative rubrics, where we kind of look at the traces and say, you know, what makes a good researcher, what's the thought process, and we can grade each roll out on, you know, how well it's following our research process."
>
> — [17:39](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=1059s) &middot; *explains the mechanism for encoding human expertise beyond verifiable metrics*

> "whatever lives in the middle, we almost in the limit kind of don't care about."
>
> — [18:25](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=1105s) &middot; *the most provocative framing of harness disposability*

> "this ability to do general auto research, I think will kind of become a commodity."
>
> — [18:25](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=1105s) &middot; *the talk's central forward-looking prediction*

> "I really think all of your value as like an enterprise or human expert comes from building environments."
>
> — [19:06](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=1146s) &middot; *the thesis statement of where enterprise moat lives*

## Positions

- Long-horizon auto-research agents only became genuinely viable around December 2025, with Opus 4.5 and harnesses like Claude Code and Codex. ([2:52](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=172s), confidence: stated)
- Building your own agent harness from scratch is preferable to using an off-the-shelf agent framework, because it gives maximum freedom to tweak anything. ([6:29](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=389s), confidence: stated)
- The evaluation is the most important component of an auto-research system; optimizing against a bad eval makes the whole system fall apart. ([9:18](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=558s), confidence: stated)
- Human-chosen harness architecture decisions (number of strategists, agent roles) are arbitrary and should be meta-optimized by an LLM rather than hand-designed. ([15:00](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=900s), confidence: stated)
- Evals and environments are the same thing — an eval becomes an environment once you train in it. ([16:21](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=981s), confidence: stated)
- General auto-research capability will become a commodity, so an enterprise's durable value comes from building environments rather than harnesses. ([18:25](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=1105s), confidence: stated)
- ALPHALAB reached the top 12% of submissions on an NVIDIA-hosted Kaggle competition to fine-tune NeMoTron into a reasoning model, using only 10 iterations. ([12:55](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=775s), confidence: stated)
- ALPHALAB found a better LLM training config than a Karpathy-style single-agent-in-a-loop baseline. ([12:55](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=775s), confidence: stated)
- ALPHALAB's performance improves monotonically with the number of experimentation iterations it is allowed. ([13:43](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=823s), confidence: implied)
- Designing verifiable metrics is the easy part of environment building; the hard part is proprietary data and qualitative process rubrics. ([17:39](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=1059s), confidence: stated)
- The best-performing system will likely be an orchestration of both open-source and closed-source models optimized together. ([16:55](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=1015s), confidence: stated)
- Morgan Stanley's sell-side position means less adversarial selection, making its problems better suited to auto-research than typical trading contexts. ([0:51](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=51s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agentic science](../concepts/agentic-science.md)
- [cross-model verification](../concepts/cross-model-verification.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [rubric design](../concepts/rubric-design.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)

