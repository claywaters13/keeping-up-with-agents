---
title: "Loop Engineering from First Principles"
type: "talk"
slug: "loop-engineering-from-first-principles"
track: "Software Factories"
org: "HumanLayer"
day: "Day 2 — Session Day 1"
room: "Main Stage"
video_id: "xIt_mTQp6mY"
duration_sec: 1077
word_count: 3493
speakers: ["Kyle Mistele"]
---

# Loop Engineering from First Principles

*Program title: Loop Engineering from first principles*

**Speakers:** [Kyle Mistele](../speakers/kyle-mistele.md)

**Org:** HumanLayer

**Track:** Software Factories &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 17m 57s

[Watch on YouTube](https://www.youtube.com/watch?v=xIt_mTQp6mY)

## Summary

Kyle Mistele argues that the current hype around agentic loops — piping a prompt into a coding agent and letting it run — produces 40,000-line PRs nobody reads, and doesn't survive contact with real teams, real customers, and real compliance obligations. His alternative is to borrow classical control theory: define a set point (the desired codebase property), build a sensor (AST-grep rules, lint, or an agent), a controller that picks one small incremental change, and an actuator agent that applies it. He walks through a production example from HumanLayer — incrementally migrating 150 RPC procedures to Effect — including a 'disturbance dampener' that blocks teammates from adding new violations, a version-controlled feedback file for low-friction human re-steering, and flow control that refuses to open a new PR while the previous one is unreviewed. The payoff he claims is loops that are cheap, low-risk, and produce diffs humans actually read, rather than a read-only code future. Worth watching if you're trying to run autonomous agents against a large, mission-critical codebase and want a concrete, GitHub-Actions-shaped blueprint rather than a manifesto.

## Key Points

- Blind 'Ralph'-style bash loops work for solo work on non-critical systems but break down on teams with real customers, SLAs, and regulatory obligations, because they generate PRs too large to review.
- Control theory maps cleanly onto agentic coding: set point (desired codebase state), sensor (measures current state), controller (decides an incremental change), actuator (applies it), with the codebase undergoing disturbances from teammates.
- Sensors can be deterministic (ESLint, AST-grep, packwerk), non-deterministic (agent plus skill plus natural-language rules), or a pipeline combining both; AST-grep is favored because it's language-agnostic and out-of-band from configs agents can disable with inline comments.
- Before migrating incrementally, run a full scan on main, sort violations deterministically, and commit the list to version control so every new PR can be checked for newly added violations — a 'disturbance dampener' that stops the bleeding.
- A smarter controller can enrich the control signal with telemetry — which procedures have the most errors or worst instrumentation — so the actuator improves the code rather than doing a one-to-one migration.
- Hand-written 'golden patterns' committed before the loop runs give the pattern-replicating agent idiomatic examples instead of leaving it to reproduce docs or internet knowledge.
- A markdown feedback file loaded into the actuator's context each run, updated via a `/iterate` PR comment trigger, puts a human on the loop with low friction and gives the steering instructions version history and revertability.
- Flow control — refusing to run if any PR carrying the loop's label is still open — caps each loop at one open PR, preventing stacked, duplicated, and conflicting work when humans are away.
- Loops should run on existing CI (GitHub Actions, GitLab, CircleCI) which already has code access, secrets, and scheduling primitives; no new cluster is needed.
- Throughput scales by batching multiple targets per run, splitting each into its own implementation phase and context window (cheaper and more reliable), or fanning out one PR per team member.

## Notable Quotes

> "I think we've all been building loops lately. And I realized recently, I think we're all doing it wrong."
>
> — [0:01](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=1s) &middot; *states the talk's contrarian thesis in one line*

> "if we're doing this, we're still building 40,000 line PRs that just nobody wants to read"
>
> — [1:00](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=60s) &middot; *names the concrete failure mode the whole talk is organized against*

> "It works very well if you're not building on a team. And it works very well if you're not working on critical systems. But most of us are working on teams and we don't fit in that box."
>
> — [1:00](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=60s) &middot; *precise scoping of where Ralph loops do and don't apply*

> "Peter Steinberger said that we shouldn't be prompting coding agents anymore, right? We should just be designing loops that prompt our agents."
>
> — [1:37](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=97s) &middot; *captures the industry position the speaker is responding to*

> "bad code is much more expensive in the age of agents than it it has ever been at any point in the past"
>
> — [3:31](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=211s) &middot; *the economic argument against unread generated code*

> "I think loops are super powerful, but we can design loops and still read the code. In fact, we can design loops to make it easier to read the code because the loops are making the code better."
>
> — [4:10](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=250s) &middot; *the constructive counter-thesis to 'code is read-only now'*

> "Control theory is all about how we drive a dynamic system, which would be your codebase, towards some desired, stable, or optimal end state"
>
> — [4:10](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=250s) &middot; *the central analogy the talk builds on*

> "Control loops are ideal when we have a system that we want to change, a problem we can measure, and a way to get feedback on the result of that change."
>
> — [5:20](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=320s) &middot; *gives the applicability test for whether this pattern fits your problem*

> "So, control loops are the opposite of what I'm going to call a blind Ralph loop."
>
> — [6:09](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=369s) &middot; *coins the contrast term used throughout*

> "The best Ralphs are actually applying control theory."
>
> — [6:09](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=369s) &middot; *concedes the steelman rather than strawmanning the opposing approach*

> "The key questions are, can we find something we can measure? Can we apply changes incrementally?"
>
> — [8:26](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=506s) &middot; *the reusable checklist for picking loop-suitable tasks*

> "we're going to run a full scan once on main, sort all the violations deterministically, and track it in our version control"
>
> — [10:16](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=616s) &middot; *the concrete mechanism behind the disturbance dampener*

> "I don't think you should ever send an agent to do deterministic code's job, but you certainly can."
>
> — [11:19](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=679s) &middot; *a clear design principle others might disagree with*

> "At Human Layer, we like to build out what we call golden patterns by hand before setting the agent loose."
>
> — [12:26](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=746s) &middot; *names a transferable practice for steering pattern-replicating agents*

> "my recommendation is to use GitHub actions or your GitLab or your CircleCI or whatever else you're using because it has access to your code, it has access to your secrets"
>
> — [12:59](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=779s) &middot; *concrete infrastructure recommendation against building new systems*

> "the way to do this is to just create a feedback file that's tracked in version control just as a markdown file"
>
> — [14:11](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=851s) &middot; *the human-on-the-loop mechanism, stated as a simple implementable artifact*

> "No human reviewed the last output, so there's no reason to stack up even more work for humans to review."
>
> — [15:57](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=957s) &middot; *the reasoning behind flow control, generalizable to any autonomous agent fleet*

> "I have 150 RPC procedures to migrate. If I do one at a time, it's going to take 6 months, which is way longer than I want to wait."
>
> — [15:57](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=957s) &middot; *reports the real numbers behind the throughput problem*

> "we could have our controller pick three or five and then do each of those in a separate implementation phase, which will be both cheaper and more reliable since each migration gets its own context window"
>
> — [16:29](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=989s) &middot; *names the cost/reliability tradeoff of per-task context isolation*

## Positions

- Blind prompt-in-a-bash-loop agent setups are the wrong pattern for teams working on critical systems, even with multiple verifier and code-review agents attached. ([1:00](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=60s), confidence: stated)
- The 'code is read-only now' thesis is unproven and prohibitively expensive for anyone without a Frontier Lab's unlimited token budget. ([3:31](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=211s), confidence: stated)
- Bad code is more expensive in the age of agents than at any previous point. ([3:31](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=211s), confidence: stated)
- Well-designed loops make code easier to read rather than making reading unnecessary. ([4:10](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=250s), confidence: stated)
- Ralph loops are not inherently wrong — the good ones already apply control theory; the failure is reading Ralph too literally as a bash loop. ([6:46](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=406s), confidence: stated)
- A task is suitable for a control loop only if you can measure the property, apply changes incrementally, and get feedback on change quality. ([9:04](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=544s), confidence: stated)
- AST-grep is preferable to lint/TypeScript config for loop sensors because it is language-agnostic and out-of-band from configs that coding agents disable with inline comments. ([9:35](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=575s), confidence: stated)
- You should never use an agent to do a job deterministic code can do. ([11:19](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=679s), confidence: stated)
- Existing CI systems are the right runtime for agent loops; a dedicated cluster is unnecessary. ([12:59](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=779s), confidence: stated)
- A loop should never open a new PR while a previous PR from that loop remains unreviewed, capping it at one open PR at a time. ([15:25](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=925s), confidence: stated)
- Giving each migration its own context window in a separate implementation phase is both cheaper and more reliable than batching them into one. ([16:29](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=989s), confidence: stated)
- Coding agents are pattern replicators, so hand-written idiomatic examples in the repo outperform relying on the agent's internet-derived knowledge or library docs. ([12:26](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=746s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent skills](../concepts/agent-skills.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [code review bottlenecks](../concepts/code-review-bottlenecks.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [legacy code migration](../concepts/legacy-code-migration.md)
- [secure code generation](../concepts/secure-code-generation.md)

