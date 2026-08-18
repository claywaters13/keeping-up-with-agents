---
title: "Computer-Use 2.0: Agents Just Got Multi-Cursor"
type: "talk"
slug: "computer-use-20-agents-just-got-multi-cursor"
track: "Computer Use"
org: "Cua"
day: "Day 3 — Session Day 2"
room: "Track 7"
video_id: "ZSQb5fzRFPw"
duration_sec: 1001
word_count: 2618
speakers: ["Dillon DuPont", "Francesco Bonacci"]
---

# Computer-Use 2.0: Agents Just Got Multi-Cursor

**Speakers:** [Dillon DuPont](../speakers/dillon-dupont.md), [Francesco Bonacci](../speakers/francesco-bonacci.md)

**Org:** Cua

**Track:** Computer Use &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 16m 41s

[Watch on YouTube](https://www.youtube.com/watch?v=ZSQb5fzRFPw)

## Summary

Three people from Cua — CEO Francesco Bonacci, CTO Dylan, and chief infra officer Robert — walk through their stack for "computer use 2.0": agents that drive a desktop in the background instead of taking over your screen. Bonacci covers Cua Driver, an open-source cross-platform driver (macOS, Windows, Linux) that exposes window state as an accessibility tree plus screenshot and falls back to pixel-level background clicks when accessibility actions fail. Dylan covers Cua Bench, a terminal-bench-style task format (setup, oracle GUI trajectory, evaluator) with 130+ verifiable tasks across 42 environments and five platforms, plus a Snorkel AI collaboration on electrical-engineering CAD tasks where the best agent fully passed only 6 of 25 tasks and no model exceeded 30% reward. Robert argues that RL training for computer use wastes GPU time waiting on sandbox startup, and describes a demand-based autoscaled warm pool that shifts that cost to cheaper infrastructure. Worth watching if you build or evaluate GUI agents and want concrete numbers on background execution, eval integrity, and RL infra economics.

## Key Points

- "Computer use 1.0" mimicked a human loop — screenshot, reason, click/type/scroll — and required the agent to take over the user's screen; Cua Driver instead runs the agent in the background using undocumented Apple framework APIs and equivalents on Windows and Linux.
- The driver's action path is layered: call get window state to obtain an accessibility tree plus screenshot, attempt background execution via the accessibility tree, and fall back to a pixel-level background click when that fails.
- Cua Bench tasks have three parts — a setup function, an oracle function providing a golden trajectory (in GUI actions rather than terminal commands), and an evaluator that probes the environment — and a whole cross-platform GUI environment collapses into a single Python file.
- The catalog currently holds over 130 verifiable tasks across 42 environments and five platforms, with about eight application harnesses used as regression tests between releases.
- Results on the CAD/electrical-engineering dataset built with Snorkel AI are humbling: the top agent fully passed 6 of 25 tasks, all six involved editing an existing schematic, success from a blank schematic was 0%, and no model exceeded 30% reward.
- Swapping an agent's built-in computer tool for Cua Driver raised pass rate from 62% to 80% on Cua Bench basic at 4K while using 34% fewer tokens, attributed to focusing on a single window rather than the whole desktop.
- Evals are themselves adversarially validated: a matrix of agents attempts reward hacking and environment breakage first, results are compiled into a code-review-style report, and only surviving tasks enter the dataset.
- Recorded runs can be forked at any point in a trajectory, letting you probe a model to predict reward or internal state and compare against ground truth — an operational way to measure an agent's world model.
- In RL training, GPUs idle while sandboxes spin up or reset; Cua Fleet uses a demand-based autoscaler to size a warm sandbox pool on the fly, moving startup cost onto infrastructure that can be two to four times cheaper than GPUs.

## Notable Quotes

> "with cooler driver we gave an agent hands but then the question becomes how can you trust the agent to use those hands correctly and not leave anything broken behind"
>
> — [6:21](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=381s) &middot; *frames the pivot from capability to trust that structures the whole middle section*

> "The top agent that we tested only got a full pass on six out of 25 of these tasks."
>
> — [7:52](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=472s) &middot; *hard number on frontier computer-use performance in a professional domain*

> "Of those six, 100% of them involved editing an existing schematic. And when we start the task from a blank schematic, the success rate drops to 0%."
>
> — [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s) &middot; *identifies a specific failure mode — agents edit but cannot originate*

> "across all the models that we tested, the leaderboard is flat. No model has achieved more than 30% reward."
>
> — [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s) &middot; *claims the benchmark is far from saturated and model choice barely matters here*

> "when you switch the agent computer tool from the built-in one to KU driver the pass rate jumps from 62% to 80% using 34% less tokens"
>
> — [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s) &middot; *the central quantitative claim for the driver*

> "this is primarily because KU driver focuses on a window rather than the entire desktop"
>
> — [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s) &middot; *gives the mechanism behind the accuracy and token win*

> "before we test a task against any agent, we first try to break the environment ourselves"
>
> — [9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s) &middot; *states their position on eval integrity as adversarial by default*

> "only tasks that survive our pipeline can enter the data set"
>
> — [9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s) &middot; *concrete admission criterion for the benchmark*

> "if you ask us how we trust that agent, the answer is that it's just evows all the way down"
>
> — [9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s) &middot; *memorable framing of recursive evaluation*

> "to measure the intelligence of an agent, you can't just measure its ability to successfully perform actions."
>
> — [9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s) &middot; *argues task success rate is an incomplete metric*

> "Every run that we record can be forked through any moment in its trajectory to give you the state of the computer at that moment."
>
> — [10:15](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=615s) &middot; *describes the mechanism enabling world-model probing*

> "that prediction is the world model of the agent made measurable"
>
> — [10:15](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=615s) &middot; *the talk's proposal for a second evaluation axis beyond task completion*

> "how you're probably leaving a lot of money on the table uh with idle GPUs if you do RL training uh for computer use agents"
>
> — [10:15](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=615s) &middot; *sets up the infra thesis in one line*

> "your GPU really isn't doing anything useful here and you know I don't know if you've heard but GPU time is pretty expensive right now"
>
> — [11:56](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=716s) &middot; *names the specific waste: rollout GPUs blocked on sandbox lifecycle*

> "we use a demandbased autoscaler to detect um how many GPUs like currently need a sandbox and we can grow the pool to be that size uh on demand"
>
> — [13:12](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=792s) &middot; *the actual design, and why you don't need to size a warm pool upfront*

> "these also could be like, you know, easily uh two to four times cheaper than your GPUs. So having a little bit of redundancy here, uh you still wind up saving money because you're maximizing the use of your GPU time."
>
> — [13:48](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=828s) &middot; *gives the cost-ratio tradeoff that justifies over-provisioning sandboxes*

> "you're paying the cost of that startup time on the infrastructure side not on the GPU side so your GPU workers have full utilization"
>
> — [13:48](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=828s) &middot; *one-sentence statement of the optimization*

> "the trick here is really um not like having your agents like take over your screen"
>
> — [3:18](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=198s) &middot; *the core product distinction of computer use 2.0*

> "the Android ecosystem especially compared to iOS is more inclined to that form of like background uh computer use but it's more towards like tool use than really like controlling GUI interface"
>
> — [14:59](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=899s) &middot; *position on mobile background agents during Q&A*

## Positions

- Computer-use agents should run in the background without taking over the user's screen, unlike the earlier screenshot-and-click 'computer use 1.0' loop. ([3:18](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=198s), confidence: stated)
- A background-first driver should try accessibility-tree execution first and fall back to pixel-level background clicks only when that fails. ([4:49](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=289s), confidence: stated)
- A cross-platform GUI environment and its evaluator can be expressed in a single Python file via the Cua Bench SDK. ([7:09](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=429s), confidence: stated)
- Current computer-use agents can edit existing artifacts but fail entirely at creating from scratch — 0% success starting from a blank schematic. ([8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s), confidence: stated)
- No model tested exceeds 30% reward on the CAD dataset, so the leaderboard is effectively flat. ([8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s), confidence: stated)
- Scoping the agent's view to a single window instead of the full desktop improves pass rate from 62% to 80% and cuts token usage by 34%. ([8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s), confidence: stated)
- Benchmark environments must be adversarially attacked for reward hacking before tasks are admitted, otherwise eval results cannot be trusted. ([9:37](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=577s), confidence: stated)
- Task success rate alone is an insufficient measure of agent intelligence; you must also measure the agent's understanding of the environment state. ([10:15](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=615s), confidence: stated)
- In RL training for computer use, GPU idle time spent waiting on sandbox spin-up or reset is pure cost that compounds with scale. ([11:56](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=716s), confidence: stated)
- Minimizing sandbox startup time is worth doing but impractical alone for computer-use environments, which can be 40 gigabytes. ([12:33](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=753s), confidence: stated)
- Over-provisioning a sandbox warm pool still saves money because sandbox compute is two to four times cheaper than GPU time. ([13:48](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=828s), confidence: stated)
- Optimal warm-pool size cannot be known upfront and shifts during a multi-day training run, so it must be autoscaled on demand. ([13:12](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=792s), confidence: stated)
- Android permits meaningful background agent work via containerization and the activity framework, but it resembles tool use more than GUI control; iOS is less amenable. ([14:59](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=899s), confidence: stated)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [benchmark design](../concepts/benchmark-design.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [post-training](../concepts/post-training.md)
- [reward hacking](../concepts/reward-hacking.md)
- [session management](../concepts/session-management.md)
- [token efficiency](../concepts/token-efficiency.md)
- [world models](../concepts/world-models.md)

