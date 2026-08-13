---
title: "Agents Building Agents"
type: "talk"
slug: "agents-building-agents"
org: "Nearform"
day: "Day 1 — Workshop Day"
room: "Track 7"
video_id: "aHhB3sjGjkI"
duration_sec: 1814
word_count: 4742
speakers: ["Du'an Lightfoot"]
---

# Agents Building Agents

*Program title: Agents That Own Their Inference: Building Production AI Agents on Dedicated GPUs*

**Speakers:** [Du'an Lightfoot](../speakers/du-an-lightfoot.md)

**Org:** Nearform

**Day/Room:** Day 1 — Workshop Day &middot; Track 7 &nbsp;|&nbsp; **Duration:** 30m 14s

[Watch on YouTube](https://www.youtube.com/watch?v=aHhB3sjGjkI)

## Summary

Alfonso Graziano, a tech lead at Nearform, describes a repeatable process for using coding agents (primarily Claude Code) to iteratively improve production AI agents. The talk covers two failure modes: poor scores on an eval suite backed by a golden dataset, and poor behavior on live user data. For the first, he presents 'AutoAgent' — a Karpathy-auto-research-inspired loop where a coding agent forms a hypothesis, branches, edits the target agent's prompts/tools/code, reruns evals, and keeps or rolls back the branch; it took a toy agent from 18% to 83% and a real production agent from 67% to 86% in roughly 10 iterations each. For the second, he outlines a trace-collection pipeline: user feedback and SME annotations are clustered into failure modes, root-caused against the code, triaged with subject matter experts, fixed by a coding agent, and folded back into the golden dataset as regressions. The unifying frame is 'harness engineering' — building the specs, quality gates, context, and observability around a coding agent so it can validate its own changes.

## Key Points

- A golden dataset — inputs plus expected outputs, co-developed with subject matter experts — acts as a test suite for a non-deterministic system, where expected output may be a specific tool call, tool parameters, or a chain of tool calls rather than just text.
- The AutoAgent loop mirrors Karpathy's auto-research idea but targets agent code instead of ML hyperparameters: it runs evals, generates a hypothesis, edits system prompts and tools, reruns evals, and decides to keep or roll back.
- Each iteration runs on its own git branch, so improvements compound from the last good branch and regressions are discarded, producing a full changelog of hypotheses and outcomes.
- A naive tool-less agent went from 18% to 83% pass rate in about 10 iterations, and a real production agent already optimized by humans went from 67% to 86% by finding edge cases, improving tool descriptions, and fixing tool logic.
- Human-in-the-loop steering matters mainly at setup: giving the coding agent context and explicitly forbidding it from editing golden datasets or scorers just to make evals pass.
- For live-data failures, the pipeline collects traces with thumbs up/down feedback or SME annotations, clusters failure modes, does root-cause analysis against the actual agent code, and outputs a markdown report with proposed fixes.
- Clustered reports must still be triaged and validated with subject matter experts, since clusters can be false positives, intended behavior, or unhelpful feedback; the team found generating one report per sprint reasonable.
- Every validated failure mode is added to the golden dataset and eval suite so the same regression is caught automatically if reintroduced.
- Even failed hypotheses are useful artifacts — a human can read the hypothesis report, see what the agent was attempting, and steer it better next time.
- 'Harness engineering' — specs per failure mode, quality gates (lint, unit tests, evals, LLM code review), context engineering, and observability — is what makes autonomous self-improvement work at all.

## Notable Quotes

> "AI is very powerful and very good at building any type of software. And given that AI agents is just one type of software, as you may guess, we are using AI to build AI."
>
> — [0:47](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=47s) &middot; *States the talk's core premise in one line*

> "You can see the golden dataset as a test suite, but in a non-deterministic scenario."
>
> — [4:09](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=249s) &middot; *Crisp reframing of evals for people coming from deterministic testing*

> "we have a pass rate of 18%, right? Uh just because a a lot of questions are simple enough, like additions, multiplications, right? Are simple enough so that the actual um LLM has this knowledge in its training data"
>
> — [5:54](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=354s) &middot; *Reports the baseline number and explains what a trivial baseline actually measures*

> "So, 18% of the questions can be answered by the weights of the LLM, the rest can't."
>
> — [5:54](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=354s) &middot; *Sharp framing of the gap that tools and context must close*

> "in a lot of cases, um a lot of the optimizations will be just to tweak the system prompt and update it so that um you know, our agent has all the information it needs to work on our domain."
>
> — [7:27](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=447s) &middot; *Names prompt tweaking as the dominant lever, a position others contest*

> "a coding agent tweaking the code of machine learning um of a deep learning algorithm can actually improve the results"
>
> — [8:15](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=495s) &middot; *The prior work that licenses the whole approach*

> "we have the baseline accuracy, which was 18%, and we managed to reach up to 83% um in like something around 10 uh 10 iterations."
>
> — [10:10](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=610s) &middot; *Headline result for the toy case, with iteration count*

> "we also improved um some evals by 10% on a production agent that was already humanly optimized."
>
> — [10:10](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=610s) &middot; *The claim that matters most — gains beyond human optimization*

> "the the coding agent found new ways that humans didn't find um to improve the agent, and we got plus 10% on some of our internal benchmarks."
>
> — [11:06](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=666s) &middot; *Explicit assertion that the agent outperformed human optimizers*

> "updating the golden data sets or the scorers just to let the evals pass is not a good idea, so we want to enforce we want to tell the we want to tell the AI agent to not do that"
>
> — [11:55](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=715s) &middot; *Names the central reward-hacking failure mode and the guardrail against it*

> "the system works by creating an hypothesis. So it's tackling one class of problems at a time. It's updating the the agent and it's running the evals again."
>
> — [13:32](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=812s) &middot; *The mechanism of the optimization loop, stated compactly*

> "if the metrics improved, then we continue from this branch. Um if the metrics didn't improve or we have a strong regression or something bad happened, uh then we roll back to the previous branch."
>
> — [15:50](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=950s) &middot; *The accept/reject rule that makes the search safe*

> "the baseline accuracy was 67% um but then in something around 10 iterations, we managed to reach 86% in our evals without actually cheating because it found edge cases, it improved the system prompt, it improved the tool descriptions to catch more edge cases, and it also fixed some tools logic."
>
> — [18:04](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1084s) &middot; *The production result plus the specific categories of change that produced it*

> "Maybe the evals didn't improve after an hypothesis, but maybe that hypothesis was promising, right? Maybe the agent was onto something, but it just didn't implement the system the change in a correct way"
>
> — [17:24](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1044s) &middot; *Argues failed iterations still carry signal for humans*

> "we analyze all the traces with both the negative and positive feedback, but we are more interested about the negative feedback here."
>
> — [20:20](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1220s) &middot; *Concrete triage priority in the live-data pipeline*

> "all the failure modes that we are founding during this investigation step, they will become part of the golden dataset that we mentioned earlier and the eval suite is updated to spot those regressions."
>
> — [25:33](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1533s) &middot; *Closes the loop between production failures and the eval suite*

> "We found out that once per sprint is actually reasonable."
>
> — [26:20](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1580s) &middot; *A rare operational cadence number for feedback analysis*

> "a coding agent, when instructed, uh has been able to fix an entire suite of issues like the one that we have seen earlier, uh with just one prompt."
>
> — [26:57](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1617s) &middot; *Strong claim about how far a well-contextualized single prompt goes*

> "Harness Engineering is the idea of building the environment around our coding agent so that they can work reliably."
>
> — [27:46](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1666s) &middot; *Defines the term the talk ends on*

> "if we don't know what's happening when we ship in production, we are basically blind"
>
> — [29:15](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1755s) &middot; *The observability argument stated bluntly*

## Positions

- An AI agent is fundamentally just an LLM in an agentic loop with tools and context retrieval. ([2:20](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=140s), confidence: stated)
- A golden dataset plus scorers is the right analogue of a test suite for non-deterministic agent systems. ([4:09](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=249s), confidence: stated)
- A coding agent can autonomously improve another agent's accuracy, taking a naive agent from 18% to 83% pass rate in about 10 iterations. ([10:10](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=610s), confidence: stated)
- Coding agents can find improvements that human engineers missed, yielding +10% on internal benchmarks for an already human-optimized production agent. ([11:06](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=666s), confidence: stated)
- The optimizing agent must be explicitly forbidden from editing golden datasets or scorers, or it will make evals pass by cheating. ([11:55](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=715s), confidence: stated)
- Running each optimization hypothesis on its own git branch, with rollback on regression, is the correct control structure for autonomous agent optimization. ([15:50](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=950s), confidence: stated)
- Most agent optimization work reduces to tweaking the system prompt, adding missing tools, and improving context retrieval. ([7:27](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=447s), confidence: implied)
- Clustered failure reports should be triaged and validated by human subject matter experts before fixes are implemented, because clusters can be false positives or intended behavior. ([25:33](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1533s), confidence: stated)
- Generating a live-data failure report once per sprint is a reasonable cadence for most use cases. ([26:20](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1580s), confidence: stated)
- Giving a coding agent the ability to test its own changes against regression tests is what makes single-prompt fixes of whole issue suites possible. ([26:57](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1617s), confidence: stated)
- Autonomous agent self-improvement is only possible when a sufficient harness — specs, quality gates, context engineering, observability — exists around the coding agent. ([27:46](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1666s), confidence: stated)
- Shipping agents to production without observability leaves the team unable to diagnose failures. ([29:15](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1755s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [retrieval evaluation](../concepts/retrieval-evaluation.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [spec-driven development](../concepts/spec-driven-development.md)

