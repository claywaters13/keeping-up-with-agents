---
title: "Rethinking Environments for Long-Horizon Work"
type: "talk"
slug: "rethinking-environments-for-long-horizon-work"
track: "Data Quality"
org: "Theta Software"
day: "Day 2 — Session Day 1"
room: "Track 9"
video_id: "2aS7aKoXn64"
duration_sec: 1274
word_count: 4802
speakers: ["Rayan Garg"]
---

# Rethinking Environments for Long-Horizon Work

*Program title: Rethinking Environments for Long Horizon Work*

**Speakers:** [Rayan Garg](../speakers/rayan-garg.md)

**Org:** Theta Software

**Track:** Data Quality &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 21m 14s

[Watch on YouTube](https://www.youtube.com/watch?v=2aS7aKoXn64)

## Summary

Two co-founders of Theta Software argue that the field's working definition of "long-horizon" agent work is muddled, and that this muddle is corrupting the environments and benchmarks used to train and evaluate agents. They contrast human-referenced horizon metrics (METR-style "this takes a human 16 hours") with model-referenced ones (tokens, steps, tool calls), showing that each is noisy in different ways and that both are needed. They then lay out the axes they think actually measure capability — tool-coordination complexity, sequential vs. parallelizable state change, and starting ambiguity — and spend the second half on the hardest piece, the verifier: why judge models and rubrics are unavoidable in soft-verifiable domains, and why judges must themselves be agents with environment access and queryable trajectories. The talk closes by criticizing three finance benchmarks (GDPval, ToolBench, Apex Agents) as too short, too saturated, too narrow, and too coarse in reward signal, versus their own 15-hour-per-task finance dataset. Worth watching if you build RL environments, rubrics, or agent evals; less so if you want practical agent-building tips.

## Key Points

- "Long horizon" is a moving scalar, not a binary category — what counted as long horizon a year ago no longer does, so any fixed threshold ages out quickly.
- Human-time-per-task and model-side units (tokens, steps, tool calls) each mislead alone: token counts vary by model family and harness, while human estimates get very noisy once tasks reach the top 1% of human capability.
- Environment complexity should be measured by how many tools and external dependencies the agent must coordinate information across, not just by wall-clock length.
- Chaining unrelated independent subtasks makes a task artificially long without measuring anything; what matters is sequential complexity where an early bad query or misread cascades into later steps.
- Deliberate ambiguity in the starting materials mirrors real human work and forces exploration, but it multiplies valid solution paths and makes standardized evaluation much harder.
- Because economically valuable work lives in soft-verifiable domains, deterministic verifiers must be supplemented by judge/critic models that inspect both final environment state and the agent's trajectory — trajectory inspection is also the main defense against reward hacking like sandbox escapes or peeking at hidden test suites.
- Judges should be treated as agents with their own (read-only) environment access and tooling, since stuffing a long trajectory into a single LLM call no longer works; trajectories need enrichment, phase segmentation, and query interfaces.
- Rubric density drives learnability, but overloading a rubric makes judges apply it inconsistently on frontier problems, so rubrics need QA (gold, no-op, variance, coverage, expert-agreement tests).
- Existing finance benchmarks fall short on four counts — average human hours per task below the long-horizon frontier, near-saturation (57% of Apex Agents IB tasks fully solved at pass@1), narrow domain breadth, and reward signal too coarse for training.

## Notable Quotes

> "long horizon is really kind of a scalar metric. Uh, it's useful for kind of measuring relative tasks like one task might be more long than another, but it's really hard to define into kind of a binary category of this task is long and this task is not."
>
> — [1:20](https://www.youtube.com/watch?v=2aS7aKoXn64&t=80s) &middot; *the talk's central framing claim about how the term should be used*

> "what we consider long horizon a year ago probably isn't really long horizon in our definition today"
>
> — [1:20](https://www.youtube.com/watch?v=2aS7aKoXn64&t=80s) &middot; *compact statement of why fixed horizon thresholds decay*

> "if a task takes GPT model 500,000 tokens, that doesn't really tell you a lot about what that task would look like for cloud models until you actually run on those cloud models."
>
> — [2:48](https://www.youtube.com/watch?v=2aS7aKoXn64&t=168s) &middot; *names the concrete confound that makes token-based horizon metrics non-comparable*

> "what's long horizon for a human isn't necessarily that difficult for a model depending on what the actual task you care about is"
>
> — [4:27](https://www.youtube.com/watch?v=2aS7aKoXn64&t=267s) &middot; *the core objection to human-time-anchored benchmarks*

> "It might take them like days to do that if it's a really big Excel file, but for a model, it can maybe write a Python script or find some other cool trick to do that really quickly."
>
> — [4:58](https://www.youtube.com/watch?v=2aS7aKoXn64&t=298s) &middot; *concrete example of human-time and model-difficulty diverging*

> "as you shift towards more long resin tasks and tasks that only the top 10% the top 1% top.1% of humans can really do these estimates start to get really really noisy"
>
> — [5:52](https://www.youtube.com/watch?v=2aS7aKoXn64&t=352s) &middot; *explains where human-referenced measurement breaks down as capability rises*

> "one task can you know maybe be made by artificially long horizon by chaining together unrelated independent tasks. However, that doesn't actually tell us or meaningfully measure the model capabilities."
>
> — [7:56](https://www.youtube.com/watch?v=2aS7aKoXn64&t=476s) &middot; *identifies a common way environment designers fake difficulty*

> "we'll see if you have to use a dashboard or logs, a bad early query or a misread can cascade into these downstream steps that really start to have major consequences later on"
>
> — [8:33](https://www.youtube.com/watch?v=2aS7aKoXn64&t=513s) &middot; *defines sequential complexity by its failure mode*

> "if you are going to have ambiguity in the materials you give, there's a lot more possible paths that the agent could take. There's a lot more ways the agent could be right. And that means that standardized evaluation gets much, much harder."
>
> — [9:39](https://www.youtube.com/watch?v=2aS7aKoXn64&t=579s) &middot; *states the ambiguity/evaluability tradeoff explicitly*

> "a lot of the early RL that we were doing in in recent times was really in hard verifiable domains and that's why we saw these gains in in math and kind of uh like data structure style coding problems"
>
> — [10:14](https://www.youtube.com/watch?v=2aS7aKoXn64&t=614s) &middot; *situates the verifier problem in the history of RL gains*

> "if we kind of enforce this too tightly, we collapse the state space of how many actual paths the agent actually explores."
>
> — [12:35](https://www.youtube.com/watch?v=2aS7aKoXn64&t=755s) &middot; *the cost of over-specifying acceptable trajectories*

> "that really does not work for these more ambiguous or open-ended tasks because there's so many possible correct solutions. It's basically impossible to account for every single one."
>
> — [13:14](https://www.youtube.com/watch?v=2aS7aKoXn64&t=794s) &middot; *rejects reference-answer comparison as a judging strategy*

> "I think the first important uh consideration to make is that judges are agents too."
>
> — [13:14](https://www.youtube.com/watch?v=2aS7aKoXn64&t=794s) &middot; *the talk's most quotable design principle*

> "it's really important that the judge has access to the environment in the same way uh with some important safeguards of course. One is that we don't want the judge to make an accidental mutation in some way to the environment after the agent is done."
>
> — [14:36](https://www.youtube.com/watch?v=2aS7aKoXn64&t=876s) &middot; *states both the requirement and its safety constraint*

> "you can't just use this really basic approach of taking the trajectory and stuffing it in the context window of the judge and kind of have it be a basic LM call."
>
> — [15:03](https://www.youtube.com/watch?v=2aS7aKoXn64&t=903s) &middot; *names the naive judging pattern that breaks at long horizons*

> "These are all different things we want we want to do. And in that sense we need to make the trajectory itself queryable."
>
> — [15:44](https://www.youtube.com/watch?v=2aS7aKoXn64&t=944s) &middot; *the prescriptive fix for long-trajectory judging*

> "especially for frontier problems that models aren't really capable of yet, judges will really struggle to apply that rubric consistently"
>
> — [16:42](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1002s) &middot; *limits on rubric density, tied to judge reliability*

> "deterministic verifiers aren't completely dead. oftentimes we use them in tandem with judges."
>
> — [17:13](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1033s) &middot; *a hedge against the assumption that judges replace programmatic checks*

> "a lot of the data being produced right now and being used to train and evaluate models is actually flawed"
>
> — [18:17](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1097s) &middot; *the thesis behind the benchmark critique that closes the talk*

> "if you look at the average human hours per task, based on what Meter has defined for a lot of the leading frontier models, a lot of these different average human hours per task fall far below that and so they wouldn't actually be considered long horizon tasks."
>
> — [18:45](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1125s) &middot; *the specific, checkable charge against existing finance benchmarks*

> "pass at one effectively means that for like 57% of cases, the tasks are 100% solved"
>
> — [18:45](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1125s) &middot; *a hard number supporting the saturation claim*

> "a lot of these more important areas for learnability like, you know, credit, debt, risk in the domain of finance don't really get covered"
>
> — [19:23](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1163s) &middot; *the breadth gap, named by domain*

> "We can see that the human time to complete one task on average is 15 hours over a 50 task sample set."
>
> — [20:32](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1232s) &middot; *the headline stat for their own dataset, the implicit contrast to the benchmarks critiqued*

## Positions

- Long horizon should be treated as a relative scalar measure, not a binary category, because the threshold shifts every year. ([1:20](https://www.youtube.com/watch?v=2aS7aKoXn64&t=80s), confidence: stated)
- Token counts as a horizon metric are noisy because they depend heavily on which model family and which harness is used, so cross-model comparisons are uninterpretable without holding those constant. ([2:48](https://www.youtube.com/watch?v=2aS7aKoXn64&t=168s), confidence: stated)
- Neither human-time nor model-side metrics should be used in isolation; both are needed because agent and human capability profiles are diverging. ([3:55](https://www.youtube.com/watch?v=2aS7aKoXn64&t=235s), confidence: stated)
- Cross-organization comparisons of 'average human hours per task' are unreliable because expert quality and measurement methodology vary so much. ([5:22](https://www.youtube.com/watch?v=2aS7aKoXn64&t=322s), confidence: stated)
- Tasks made long by chaining unrelated independent subtasks do not meaningfully measure model capability; earlier decisions must influence later ones. ([7:56](https://www.youtube.com/watch?v=2aS7aKoXn64&t=476s), confidence: stated)
- Sequential, state-changing complexity is a better capability test than parallelizable complexity such as fanning sub-agents across files. ([8:33](https://www.youtube.com/watch?v=2aS7aKoXn64&t=513s), confidence: stated)
- Environments should include starting ambiguity so models must explore, accepting that this makes standardized evaluation harder. ([9:39](https://www.youtube.com/watch?v=2aS7aKoXn64&t=579s), confidence: stated)
- For the economically valuable soft-verifiable domains now being targeted, deterministic verifiers are impractical, brittle, or impossible, so judge models are required. ([11:29](https://www.youtube.com/watch?v=2aS7aKoXn64&t=689s), confidence: stated)
- Judges must inspect the agent's trajectory, not just the final state, because trajectory inspection is how reward hacking such as sandbox escape or reading a hidden test suite is caught. ([12:06](https://www.youtube.com/watch?v=2aS7aKoXn64&t=726s), confidence: stated)
- Comparing agent output against a reference answer or sample trajectory fails on open-ended tasks because there are too many correct solutions to enumerate. ([13:14](https://www.youtube.com/watch?v=2aS7aKoXn64&t=794s), confidence: stated)
- Judges should be built as agents that reuse the task harness and have read-only access to the environment, with permissions preventing them from mutating state after the agent finishes. ([14:36](https://www.youtube.com/watch?v=2aS7aKoXn64&t=876s), confidence: stated)
- Reported tool calls from the agent are usually not reliable evidence of correctness, so the judge must independently check environment state such as GitHub or AWS logs. ([14:36](https://www.youtube.com/watch?v=2aS7aKoXn64&t=876s), confidence: stated)
- Long trajectories cannot be evaluated by a single LLM call; they must be stored, enriched, phase-segmented, and made queryable. ([15:44](https://www.youtube.com/watch?v=2aS7aKoXn64&t=944s), confidence: stated)
- Overly dense rubrics degrade judge consistency on frontier problems, so rubric density must be QA'd rather than maximized. ([16:42](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1002s), confidence: stated)
- Training on environments the model cannot learn from wastes compute, making learnability a first-class design criterion alongside difficulty. ([16:42](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1002s), confidence: stated)
- Dynamic evaluation-time rubrics that grant partial credit by assuming an agent's earlier mistaken assumption was correct are a useful emerging credit-assignment pattern. ([17:13](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1033s), confidence: stated)
- GDPval, ToolBench, and Apex Agents have average human hours per task far below the frontier models' measured horizon, so their tasks do not qualify as long horizon. ([18:45](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1125s), confidence: stated)
- These benchmarks' saturation is a downstream consequence of their short average human task time, not an indication that the underlying capability is solved. ([18:45](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1125s), confidence: stated)
- GDPval's finance coverage is a narrow set of Excel tasks and Apex Agents is largely investment banking, leaving credit, debt, and risk uncovered. ([19:23](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1163s), confidence: stated)
- Public benchmarks provide reward signal too coarse for training; useful rubrics need roughly 20 criteria with about 10 subcriteria each. ([19:57](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1197s), confidence: stated)
- Theta's own finance tasks average 15 hours of human time across a 50-task sample, and frontier models still score around 5 on them. ([20:32](https://www.youtube.com/watch?v=2aS7aKoXn64&t=1232s), confidence: stated)

## Concepts

- [benchmark saturation](../concepts/benchmark-saturation.md)
- [coding agent benchmarking](../concepts/coding-agent-benchmarking.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [reward design](../concepts/reward-design.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [rubric design](../concepts/rubric-design.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)
- [verifier design](../concepts/verifier-design.md)

