---
title: "Rishi Desai"
type: "speaker"
slug: "rishi-desai"
talk_count: 1
---

# Rishi Desai

## Talks

- [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [coding agent benchmarking](../concepts/coding-agent-benchmarking.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)
- [verifier design](../concepts/verifier-design.md)

## Quotes

> "Can coding agents stay coherent over a billion token budget? Can they build Slack from scratch? Can they rewrite an entire JAX code base in PyTorch? Can they build a C compiler in Rust?"
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [0:01](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=1s)

> "The pattern is that coding agents are being pointed at whole projects, not just GitHub issues or linear tickets."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [0:48](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=48s)

> "These are literally hundreds of hours of human work compressed into a single agent rollout."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [1:52](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=112s)

> "In a short benchmark, a weak test could just be considered as noise. But, in a multi-hour environment, a weak verifier becomes an attack surface."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [1:52](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=112s)

> "The agent has hours, a file system, unrestricted network access potentially, and a reward signal."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [2:51](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=171s)

> "We wanted independent verified channels that fail in different ways."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [2:51](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=171s)

> "Unit test can pass, but the product is probably still unusable and the front end looks terrible."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [3:56](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=236s)

> "The verifier isn't reading code or calling an API directly. It's driving the submitted slack clone through the UI."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [3:56](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=236s)

> "full stack eval's are hard because correctness is not just an API contract. It's whether the user can actually complete the product's intended workflow."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [4:50](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=290s)

> "The best configuration here is Claude Opus 4.8 with Claude Code, and it only achieves a 26% resolution rate."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [5:45](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=345s)

> "The average trial used 31 million tokens, and the longest rollout consumed 877 million tokens."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [5:45](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=345s)

> "current agents are very impressive, but end-to-end project ownership ownership is still very far from being solved"
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [6:43](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=403s)

> "Whereas GPT 4.5 with Codex is far cheaper and only gets 12%. So, the model isn't just the full picture. The agent scaffold makes a huge difference"
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [6:43](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=403s)

> "Reward hacking is an arms race between coding agents and our environment. This is why strong verifiers are are central to Sweep Marathon's task design and not an afterthought."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [8:44](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=524s)

> "we found 12.8% had suspicious shortcut behavior, and 9% had the clear verifier bypass"
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [9:42](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=582s)

> "Zero rollouts earned reward through an exploit, because our defenses caught them. That should be the bar for long-horizon evals."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [9:42](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=582s)

> "But Gemini found a much shorter implementation strategy, which is call GCC from inside the Rust program."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [9:42](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=582s)

> "So, even though the partial scores look high, the final reward is zero."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [10:43](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=643s)

> "the future of SWE evals is not just harder unit tests. Once agents run for hours, each task becomes a complex environment"
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [10:43](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=643s)

> "I've released 320 GB of trajectories that are especially important because they make SWE-bench fully inspectable and transparent."
>
> — [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [11:45](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=705s)

