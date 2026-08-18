---
title: "The Agentic AI Engineer"
type: "talk"
slug: "the-agentic-ai-engineer"
track: "Security"
org: "Mutagent"
day: "Day 2 — Session Day 1"
room: "Track 5"
video_id: "pSto5YaNGUo"
duration_sec: 2089
word_count: 4340
speakers: ["Manoj Nair"]
---

# The Agentic AI Engineer

*Program title: Through the AI Fog: The architectural decision the next 24 months of agentic security depends on.*

**Speakers:** [Manoj Nair](../speakers/manoj-nair.md)

**Org:** Mutagent

**Track:** Security &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 34m 49s

[Watch on YouTube](https://www.youtube.com/watch?v=pSto5YaNGUo)

## Summary

Benedikt Sanftl (CEO) and Burak (CTO) of Mutagent argue that the manual build-test-ship-monitor loop for AI agents doesn't scale once an organization runs more than a handful of agents, because human review of traces and evals becomes the bottleneck. Their proposal is the "agentic AI engineer": decompose the agent lifecycle into stages — spec, build, evaluate, ship, monitor, diagnose, optimize — and assign agents to each stage so the whole loop runs autonomously with an eval suite as the termination gate. Much of the talk is practical eval and diagnostics advice: keep the spec isolated from the framework so you can switch harnesses, prefer binary criteria over score rubrics because they give actionable feedback, calibrate LLM judges against run-to-run variance, and sample traces via learned code-checkable failure indicators rather than reading everything. The last third is a product demo of Mutagent's two research-preview agents (evaluator and diagnostics), showing an HTML root-cause report with why-chains, an explicit assumptions block, and remedies that export as a markdown task for your coding agent. Worth watching if you run agents in production and are drowning in trace review; skip if you want novel research rather than lifecycle tooling.

## Key Points

- The agent lifecycle splits into an offline loop (spec, build, evaluate, ship) and an online loop (monitor, diagnose, optimize), and both can be driven by agents rather than humans.
- Human review of traces and evals is the scaling bottleneck: once you have many agents or AI features, the per-iteration loop time makes parallel experimentation impossible.
- Specs should capture context requirements, tools and integrations, in-scope and out-of-scope responsibilities, and constraints — and stay isolated from implementation details so the target harness can be swapped later.
- The speakers expect teams to change agent frameworks within about a year, because harnesses regularly hit capability roadblocks you can't fix yourself.
- A complete eval suite cannot be pre-written by domain experts; it is a product of discovery built up from production failures and user feedback over time.
- Binary pass/fail criteria are preferred over score-based LLM-as-judge metrics because a failing binary criterion tells you exactly what to fix, while an unclear rubric score does not.
- LLM judges must be calibrated to control run-to-run scoring variance, otherwise experiments can't conclusively show that version B beats version A.
- Agent evaluation should cover the whole trajectory — context completeness, every tool output, and the harness itself — rather than any component in isolation.
- Reading all production traces costs more than the executions themselves; instead collect code-checkable indicators per failure mode and sample representatively via multi-tier segmentation.
- Mutagent's product runs an orchestrator plus sub-agents in your own coding environment, connecting to trace sources (e.g. LangFuse, local Claude Code transcripts, JSONL exports) and emitting fixes as GitHub PRs or MD-file edits.

## Notable Quotes

> "once you reach a certain number of agents or AI-based features, the human performing this loop again cannot really scale in enough time. So, this is why doing this agentically is the key to increasing the throughput because then you can fit many more cycles into the same time window."
>
> — [2:19](https://www.youtube.com/watch?v=pSto5YaNGUo&t=139s) &middot; *the core thesis of the talk in one passage*

> "the bottleneck basically becomes the human review and the human yeah, building time"
>
> — [1:33](https://www.youtube.com/watch?v=pSto5YaNGUo&t=93s) &middot; *names the problem the whole architecture is designed around*

> "essentially because of that spec is isolated from the implementation details"
>
> — [9:25](https://www.youtube.com/watch?v=pSto5YaNGUo&t=565s) &middot; *states the portability principle behind spec-driven agent development*

> "sometimes the agent framework or the harness does not always have the capabilities. So, occasionally you hit um like a bottleneck or a roadblock, and then you have to rely on the underlying framework to kind of get rid of that, and this can sometimes take a while."
>
> — [10:31](https://www.youtube.com/watch?v=pSto5YaNGUo&t=631s) &middot; *concrete experience-based justification for framework-agnostic specs*

> "after you build for agents, you essentially go into the eval-driven development loop, which I would call. And this is kind of equivalent to test-driven development for building software with agents because then the agents needs uh termination condition, right?"
>
> — [11:26](https://www.youtube.com/watch?v=pSto5YaNGUo&t=686s) &middot; *frames evals as the termination condition for autonomous loops*

> "you cannot pre-guess the entire evaluation suite from the beginning"
>
> — [11:26](https://www.youtube.com/watch?v=pSto5YaNGUo&t=686s) &middot; *direct pushback on upfront eval design with domain experts*

> "But essentially, the real and the complete eval suite is a product of discovery."
>
> — [12:40](https://www.youtube.com/watch?v=pSto5YaNGUo&t=760s) &middot; *compact statement of their eval philosophy*

> "imagine you have a data set item of 200. Here, without automated evals, running this and evaluating by like human eyes takes quite a while."
>
> — [13:36](https://www.youtube.com/watch?v=pSto5YaNGUo&t=816s) &middot; *puts a number on where manual review breaks down*

> "you design loops for your agent so then they can autonomously work as many of these things in the background. Uh and then your job becomes designing these loops with a clear eval or termination gate."
>
> — [14:38](https://www.youtube.com/watch?v=pSto5YaNGUo&t=878s) &middot; *redefines the AI engineer's job as loop design*

> "did the agent have all the required context to perform the task end to end?"
>
> — [15:46](https://www.youtube.com/watch?v=pSto5YaNGUo&t=946s) &middot; *names context completeness as a primary eval dimension*

> "every wrong tool output in session can in the end lead to our wrong output as the final output"
>
> — [15:46](https://www.youtube.com/watch?v=pSto5YaNGUo&t=946s) &middot; *argues for trajectory-level rather than output-only evaluation*

> "these days also the harness that the agent is operating on has quite drastic effects on the agent behavior. And this is again another vector of optimization."
>
> — [15:46](https://www.youtube.com/watch?v=pSto5YaNGUo&t=946s) &middot; *treats harness choice as a tunable variable, not a fixed substrate*

> "when you use score-based evals, unless your rubric is very well defined, then this does not exactly tell you what to fix"
>
> — [16:53](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1013s) &middot; *the tradeoff behind their binary-eval preference*

> "using uh, binary type of evals or criteria, is preferred because there you have a kind of a call to action"
>
> — [16:53](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1013s) &middot; *an explicit, contestable methodological position*

> "your LLM as a judge solution should be calibrated so that you don't have the, uh, scoring noise between judges because since LLM LLMs are undeterministic, what you will mostly encounter is the same judge can, uh, evaluate a problem different ways on each run."
>
> — [18:03](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1083s) &middot; *identifies judge variance as the blocker to conclusive experiments*

> "Over time, you can collect code-checkable indicators per failure mode."
>
> — [20:30](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1230s) &middot; *the key technique for making diagnosis cheap at scale*

> "if you have let's say millions of agent traces and to read all of these uh it actually costs more than the execution itself"
>
> — [21:28](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1288s) &middot; *a cost argument that reframes observability economics*

> "As long as you can reach that then it's automatically shipped to production."
>
> — [22:47](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1367s) &middot; *states the boldest claim — autonomous deploy gated only by evals*

> "we learned from our users that reading through these traces took them a lot of time"
>
> — [25:04](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1504s) &middot; *the user-research motivation for the diagnostics agent*

> "most of the time you don't want to read all of your traces because this is not cost-efficient"
>
> — [30:03](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1803s) &middot; *restates the sampling principle as implemented in the product*

> "when you are reading traces, sometimes you don't always have access to the code, so this helps us detect uh, LLM or let's say the diagnostics agent makes certain assumptions that are also not correct and we can see and correct them here"
>
> — [32:03](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1923s) &middot; *explains why an explicit assumptions block is a necessary safeguard on automated root-cause analysis*

## Positions

- Manual human-in-the-loop agent iteration stops scaling once an organization runs a large number of agents or AI features, making agentic automation of the loop necessary. ([2:19](https://www.youtube.com/watch?v=pSto5YaNGUo&t=139s), confidence: stated)
- The agent spec should be kept independent of the implementation framework, because teams will likely need to switch harnesses within roughly a year. ([9:25](https://www.youtube.com/watch?v=pSto5YaNGUo&t=565s), confidence: stated)
- A complete eval suite cannot be written upfront by domain experts; it must be discovered incrementally from production failures and user feedback. ([12:40](https://www.youtube.com/watch?v=pSto5YaNGUo&t=760s), confidence: stated)
- Binary pass/fail eval criteria are preferable to score-based rubrics because they yield actionable, fixable feedback. ([16:53](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1013s), confidence: stated)
- Uncalibrated LLM judges produce enough run-to-run variance that you cannot conclusively compare agent versions. ([18:03](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1083s), confidence: stated)
- Agents must be evaluated across the full trajectory — context completeness, every tool output, and the harness — not on final output alone. ([15:46](https://www.youtube.com/watch?v=pSto5YaNGUo&t=946s), confidence: stated)
- At millions of traces, reading all traces with an LLM costs more than the original agent executions, so representative sampling with learned indicators is required. ([21:28](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1288s), confidence: stated)
- If an optimized agent variant meets target eval scores, it can be shipped to production automatically without human review. ([22:47](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1367s), confidence: stated)
- The harness an agent runs on is itself a legitimate optimization variable, alongside prompts and tools. ([15:46](https://www.youtube.com/watch?v=pSto5YaNGUo&t=946s), confidence: stated)
- Automated diagnostics reports must surface their assumptions explicitly, because agents reading traces without code access will infer things that are wrong. ([32:03](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1923s), confidence: implied)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [model portability](../concepts/model-portability.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [spec-driven development](../concepts/spec-driven-development.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

