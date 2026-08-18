---
title: "Continual Learning for AI Agents: From Failures to Durable Improvements"
type: "talk"
slug: "continual-learning-for-ai-agents-from-failures-to-durable-improvements"
org: "RELAI"
video_id: "2IxD9OB3XuQ"
duration_sec: 1355
word_count: 3230
speakers: ["Soheil Feizi"]
---

# Continual Learning for AI Agents: From Failures to Durable Improvements

**Speakers:** [Soheil Feizi](../speakers/soheil-feizi.md)

**Org:** RELAI

**Duration:** 22m 35s

[Watch on YouTube](https://www.youtube.com/watch?v=2IxD9OB3XuQ)

## Summary

Soheil Feizi (RELAI) argues that continual learning for AI agents breaks into two hard problems — getting feedback and acting on it — and that the industry's current answers to both are unverified. He frames agent improvement as happening across three layers (model weights, harness/context, memory), and claims the dominant approaches each fail one way: trace-to-harness fixes are 'vibe-based' and untestable, GEPA-style prompt search needs benchmarks that production doesn't have, and memory writes are cheap but unverified. His proposed fix is 'verifiable continual learning' (VCL): lift production logs and feedback into replayable simulation-plus-evaluator learning environments, then route fixes to the smallest durable layer under regression-aware optimization. He grounds it in four principles — replayability, holisticness, lifelongness, efficiency — and demos RELAI's two-command loop on a fictional support-agent benchmark deliberately seeded with regression traps. Worth watching if you run agents in production and want a vocabulary for why log-driven 'improvements' silently break things that used to work.

## Key Points

- Continual learning for agents decomposes into two distinct challenges: how to obtain feedback on agent behavior, and how to act on that feedback by deciding which layer to change and how.
- Improvement can target three layers — model weights (SFT, DPO/GRPO/RLVR, LoRA), the harness (prompts, skills, tools, code, workflow), and memory (facts and distilled skills) — and a good learning engine picks the smallest durable change at the right layer rather than committing to one layer.
- Production logs plus feedback are not a learning environment: they are a single observation of what happened, not a replayable, gradeable distribution, so nothing built from them is testable.
- A learning environment must be inferred from a log by reconstructing tool behavior (real vs. mock), synthetic users and personas, and explicit evaluators defining what success means.
- Existing harness-update methods split badly: trace-to-harness (a coding agent editing the agent from a log) works on logs but is unverifiable and can create hidden regressions, while GEPA-style prompt search is testable but requires a benchmark and explicit evaluators.
- Memory updates are the cheapest and fastest layer and work directly on log-plus-feedback, but are typically unverified for both efficacy and regression risk.
- Verifiable continual learning requires three steps per fix: an executable test replaying the failure, a measured delta scored before and after, and a regression test confirming prior tests still pass.
- Regression avoidance should be a constraint inside the optimization loop rather than a post-hoc check, and must scale sub-linearly in the number of accumulated past environments.
- In RELAI's demo, a support agent scored 78% in a generated 'rude and adversarial caller' environment, and one optimization loop raised the score to 97% — an improvement the speaker described as about 10% on average.

## Notable Quotes

> "Humans learn mainly from experience by interacting with the world and getting feedback. The goal of continual learning is to imitate the same for agents. So they can also learn from experience by acting, getting feedback, and improving without forgetting."
>
> — [0:01](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1s) &middot; *Compact statement of the talk's framing and the 'without forgetting' constraint that drives everything after.*

> "But in production, we don't have such benchmark. We have logs."
>
> — [2:26](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=146s) &middot; *The pivot that motivates the entire learning-environment argument.*

> "Here we have log and feedback, but what we really need is a replayable learning environment, a simulation that we can rerun with defined grading on what success looks like, not one instance of what happened and the feedback on top of it."
>
> — [3:57](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=237s) &middot; *The talk's central definitional claim about why logs are insufficient.*

> "But a good learning is not going to be focusing on any of these components exclusively. A good learning engine should ask for the smallest durable change at the right layer of the agent."
>
> — [6:22](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=382s) &middot; *States the holisticness position against single-layer optimization approaches.*

> "But these methods, they usually need benchmarks and explicit evaluators. They cannot be directly applied on, let's say, if you have a log and feedback, unless we turn those into uh replayable learning environments."
>
> — [8:04](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=484s) &middot; *Names the concrete limitation of weight-update methods in production settings.*

> "So, this works on uh the case where we have log and feedback, but it is wipe-based. We don't know if even for that particular uh sample, if the change is effective, because it is not testable."
>
> — [8:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=536s) &middot; *Direct criticism of trace-to-harness self-improvement, a widely used pattern.*

> "What uh might have been working previously, but with these changes might not work properly, and create some hidden regressions."
>
> — [8:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=536s) &middot; *Names the specific failure mode — hidden regressions — the whole method targets.*

> "So, this layer in terms of the update is cheapest and fastest. It works directly on the cases where you only have log and feedback, but usually it is unverified"
>
> — [9:50](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=590s) &middot; *The tradeoff summary for the memory layer, where most practitioners start.*

> "the goal is to improve an agent from its his own experience where every fix is proven to help and proven to break nothing that already worked"
>
> — [11:01](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=661s) &middot; *The definition of verifiable continual learning in one line.*

> "One failure may have several causes and several possible repairs."
>
> — [11:44](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=704s) &middot; *The crux of the holisticness principle, motivating root-cause routing across layers.*

> "A better approach is a regression aware learning where the regression is not be treated as a post-hoc approach, but as a mechanism within the optimization itself."
>
> — [13:19](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=799s) &middot; *The talk's most contestable design claim — regression as constraint, not test suite.*

> "So, here we are uh fixing the recent failures subject to having no regression on the past uh learning environments."
>
> — [14:09](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=849s) &middot; *States the constrained-optimization formulation underlying lifelongness.*

> "So, sometimes the change can be cheap, like for example, writing something in the memory can be medium in terms of the complexity by changing the prompt or hardness, and sometimes it can be very expensive by changing the weights of the model."
>
> — [14:09](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=849s) &middot; *Ranks the cost of the three layers, which is what makes layer routing economically meaningful.*

> "So, we have deterministic evaluators and we also build this benchmark in a way that it has some regression trap."
>
> — [18:03](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1083s) &middot; *Reports a specific benchmark design choice that tests the paper's central claim.*

> "It is 78% and in particular, there are two um, evaluators that uh, basically show very low scores uh, of agent in this environment."
>
> — [19:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1196s) &middot; *The demo's baseline number.*

> "Uh, it is 10% improvement on average just with one loop and score increases to 97% from 87%."
>
> — [19:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1196s) &middot; *The headline result, and notable that the stated numbers are internally inconsistent with the 78% baseline.*

> "This is verifiable continual learning in practice, where each update is tested, every gain is measured, and nothing that already works breaks during this optimization."
>
> — [20:46](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1246s) &middot; *The strongest form of the product claim.*

> "The first one is agent continual learning is not necessarily model fine-tuning. The updates and many useful updates can happen in the harness and memory layer."
>
> — [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s) &middot; *Takeaway that pushes back on the default assumption that improvement means training.*

> "So, the second takeaway is production logs are not learning environments."
>
> — [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s) &middot; *The single most quotable and transferable claim in the talk.*

> "And the third takeaway is that the frontier is regression-aware continual improvement, where when fixing the new failure, we verify that we don't forget the old ones."
>
> — [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s) &middot; *Positions regression-awareness as the open research frontier.*

## Positions

- Production logs plus feedback are not sufficient for agent learning; they must be lifted into replayable learning environments with simulators and evaluators before any fix can be verified. ([3:57](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=237s), confidence: stated)
- Trace-to-harness approaches, where a coding agent reads a log and edits the agent, are 'vibe-based' and can introduce hidden regressions because the change is not testable. ([8:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=536s), confidence: stated)
- Prompt-search methods like GEPA are testable but cannot be applied in production because they require a benchmark and explicit evaluators. ([9:50](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=590s), confidence: stated)
- Memory-layer updates are the cheapest and fastest way to improve an agent but are typically unverified for both efficacy and regression risk. ([9:50](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=590s), confidence: stated)
- A good learning engine should make the smallest durable change at the right layer rather than optimizing any single layer exclusively. ([6:22](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=382s), confidence: stated)
- Regression prevention must be built into the optimization objective itself rather than run as a post-hoc check. ([13:19](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=799s), confidence: stated)
- Regression-aware optimization must not scale even linearly with the number of accumulated past learning environments, or it becomes computationally infeasible. ([14:09](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=849s), confidence: stated)
- Agent continual learning is not necessarily model fine-tuning; many useful updates happen in the harness and memory layers. ([21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s), confidence: stated)
- Model-weight updates (SFT, RL post-training) are the most expensive improvement layer due to compute intensity, while LoRA makes weight updates cheaper and safer by limiting changeable parameters. ([6:22](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=382s), confidence: stated)
- Automated LLM-generated feedback on logs is scalable but human expert feedback, though lower volume, is critical for capturing domain knowledge and alignment with desired agent behavior. ([3:57](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=237s), confidence: stated)
- A single learning-environment generation plus one optimization loop can raise a support agent's evaluator score from 78% to 97%. ([19:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1196s), confidence: stated)
- Regression-aware continual improvement is currently the research frontier for agent learning, implying it is not yet solved by existing systems. ([21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [continual learning](../concepts/continual-learning.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [post-training](../concepts/post-training.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)

