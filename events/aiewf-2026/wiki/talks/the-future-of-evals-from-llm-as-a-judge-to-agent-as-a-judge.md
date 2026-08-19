---
title: "The Future of Evals: From LLM as a Judge to Agent as a Judge"
type: "talk"
slug: "the-future-of-evals-from-llm-as-a-judge-to-agent-as-a-judge"
track: "Arize Evals Track"
org: "Arize AI"
video_id: "q2JrUKBMf0w"
duration_sec: 366
word_count: 980
speakers: ["Aparna Dhinakaran"]
---

# The Future of Evals: From LLM as a Judge to Agent as a Judge

**Speakers:** [Aparna Dhinakaran](../speakers/aparna-dhinakaran.md)

**Org:** Arize AI

**Track:** Arize Evals Track &nbsp;|&nbsp; **Duration:** 6m 06s

[Watch on YouTube](https://www.youtube.com/watch?v=q2JrUKBMf0w)

## Summary

Aparna Dhinakaran of Arize AI argues that the first generation of evals — deterministic checks and LLM-as-a-judge rubrics — no longer matches what teams are actually building. As systems moved from single-prompt answering (2023) to tool calls and reasoning (2024) to today's long-horizon agent loops with sub-agents, failure modes changed in kind, not just degree: context loss, repeated tool calls, infinite loops, inefficient trajectories, and non-deterministic UI generation. Her proposal is 'agent as a judge': a long-running evaluator agent that reads production traces, discovers failure patterns adaptively rather than scoring against a fixed rubric, and can even open a PR with a fix. She frames this as additive — teams should run all three eval types — and grounds the argument in Arize's own dogfooding of its in-product agent Alex plus platform-scale numbers (100M+ evals/month). Worth watching if you own an eval strategy and are hitting the ceiling of static rubrics on agentic traces; it's a 6-minute keynote-style pitch, not a technical deep dive.

## Key Points

- Evals have shifted from a novel skill individual PMs and AI engineers pick up to the core bet serious AI teams are making on their product quality.
- Arize reports running over 100 million evals per month, with an average team running about 12 eval jobs and top teams running over 3,800 distinct evaluators.
- Online evals run against live production traces are the source of the signal teams need to fuel continual learning loops, distinct from offline pre-ship evals.
- The object of evaluation changed underneath the first generation of eval tooling: prompt answering (2023) → tool calls, reasoning, deep research (2024) → agent loops with sub-agents on long-horizon tasks.
- Increased system complexity produced categorically new failure modes — forgetting context, not knowing when a task is done, getting stuck in loops — that fixed-rubric judges are not built to catch.
- Agent-as-a-judge is characterized as adaptive, dynamic analysis, in contrast to LLM-as-a-judge's fixed rubric and fixed scores, and is the right tool when every user interaction produces a different trajectory.
- The claim is additive, not replacement: deterministic evals and LLM-as-a-judge remain valid, and the future state is teams running all three approaches.
- Arize's product 'Signal' is a long-running agent that reads incoming traces, discovers issue patterns like repeated tool calls and inefficient trajectories, and can open a PR with a fix.

## Notable Quotes

> "Evals have gone from the new skill that every PM and every AI engineer has to learn to the thing that every serious AI team is betting on."
>
> — [0:01](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=1s) &middot; *frames the talk's thesis about evals' shift in organizational status*

> "We run over 100 million evals every month. The average team runs about 12 different eval jobs with the top teams running over 3,800 different evaluators."
>
> — [0:46](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=46s) &middot; *the talk's only hard numbers, and the empirical basis for its claims*

> "This is actually what's helping teams figure out what's working, catch their failures, and that's the type of data you need to fuel your continual learning loops."
>
> — [1:30](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=90s) &middot; *states why production-trace evals matter over offline evals*

> "When we were building all of these first-gen evals, the thing that we were actually evaluating has changed underneath us."
>
> — [1:30](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=90s) &middot; *the core diagnosis motivating the whole argument*

> "Every one of these was actually a massive jump in complexity, and we didn't just make the problem harder, we actually got a fundamentally different type of problem."
>
> — [2:15](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=135s) &middot; *the difference-in-kind claim that justifies a new eval category*

> "It has the ability to create dynamic UIs. It can go search across an enormous volume of traces. But, we also realized that it would forget context. It wouldn't know when something was done."
>
> — [2:56](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=176s) &middot; *concrete failure taxonomy from dogfooding their own agent*

> "the classical LLM as a judge evals, that probably many of you have written in this room, just weren't for us to be able to catch all the types of failures that we were experiencing"
>
> — [2:56](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=176s) &middot; *directly names the limitation of the incumbent approach*

> "What if the best way to an evaluate an agent was actually with an agent."
>
> — [3:40](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=220s) &middot; *the talk's central proposal, stated plainly*

> "Agent as a judge is about adaptive dynamic analysis. LLM as a judge just gives you a fixed rubric with these fixed scores."
>
> — [3:40](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=220s) &middot; *the sharpest statement of the tradeoff between the two eval paradigms*

> "when your agent's doing completely different trajectories every time a user puts in data, it just means that you need a fundamentally different type of eval"
>
> — [3:40](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=220s) &middot; *specifies the exact condition under which static rubrics break down*

> "My take is that most teams today are doing the first two, but the future of evals is actually having all three."
>
> — [4:25](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=265s) &middot; *explicitly marked as the speaker's opinion and clarifies the claim is additive*

> "It's helped us figure out very subtle failures that you wouldn't even think of doing, such as something going on in a loop for multiple times"
>
> — [4:25](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=265s) &middot; *gives a concrete example of what discovery-based evaluation surfaces*

> "And actually what this does is because it has all that analysis, it can go put up a PR and put up a fix."
>
> — [5:12](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=312s) &middot; *extends evaluation from measurement to automated remediation*

## Positions

- Classical LLM-as-a-judge evals with fixed rubrics cannot catch the failure modes of modern multi-step agents. ([2:56](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=176s), confidence: stated)
- The best way to evaluate an agent is with another agent. ([3:40](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=220s), confidence: stated)
- Agent-as-a-judge does not replace deterministic evals or LLM-as-a-judge; mature teams should run all three. ([4:25](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=265s), confidence: stated)
- Most teams today are only doing deterministic evals and LLM-as-a-judge, not agent-as-a-judge. ([4:25](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=265s), confidence: stated)
- Evals run on live production traces, not offline evals, are what generate the data needed for continual learning loops. ([1:30](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=90s), confidence: stated)
- Arize runs over 100 million evals per month across customer teams. ([0:46](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=46s), confidence: stated)
- Each generation of added model capability (tool calls, reasoning, deep research, sub-agents) produced a qualitatively different evaluation problem rather than a harder version of the same one. ([2:15](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=135s), confidence: stated)
- An evaluation agent with full trace analysis can go beyond scoring to automatically open a pull request fixing the issue it found. ([5:12](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=312s), confidence: stated)
- The industry broadly agrees that evals are the critical AI engineering skill, as evidenced by CPOs of Anthropic and OpenAI and Garry Tan. ([1:30](https://www.youtube.com/watch?v=q2JrUKBMf0w&t=90s), confidence: stated)

## Concepts

- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [continual learning](../concepts/continual-learning.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [online evaluation](../concepts/online-evaluation.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [rubric design](../concepts/rubric-design.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

