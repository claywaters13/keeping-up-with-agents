---
title: "From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization"
type: "talk"
slug: "from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization"
org: "Hud"
video_id: "JJGbw4ggaFs"
duration_sec: 1365
word_count: 3732
speakers: ["May Walter"]
---

# From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization

**Speakers:** [May Walter](../speakers/may-walter.md)

**Org:** Hud

**Duration:** 22m 45s

[Watch on YouTube](https://www.youtube.com/watch?v=JJGbw4ggaFs)

## Summary

May Walter (Hud) describes an agentic workflow that continuously hunts for performance and stability wins in production code, closing the gap between 'we know this is slow' and 'we know what to fix.' The core argument is that the investigation phase — not the fix — is the unbounded cost that keeps performance work perpetually deprioritized, and that this phase is what agents should automate. The talk walks through the concrete stack (GitHub Agent Workflows on a weekly cron, Claude Code as the harness, runtime intelligence exposed over MCP, ClickHouse-backed query language plus skills, report to Slack) and is unusually candid about what failed: plausible-but-wrong fixes, query variance blowing up evals, agents 'fixing' exceptions by catching them, and humans ignoring a flood of auto-opened PRs. The key design move is function-level production context ('prod-to-code') so the agent reasons in the same units as code, plus ROI scoring that gates what reaches a human. Worth watching if you're building autonomous agent workflows and need a worked example of the trust threshold that separates an IDE copilot from an unattended automation.

## Key Points

- Teams can estimate how long a performance fix takes but never how long the investigation takes, which is why performance work is chronically deprioritized until it becomes a crisis — a leaky-bucket cycle of ignore, escalate, emergency-fix, ignore.
- The 2026 DORA data shows AI adoption mainly boosts individual effectiveness while software delivery instability rises and team throughput is largely unchanged, which motivates using AI on the fix/verify side rather than only on the build side.
- The workflow is deliberately vendor-neutral across compute, harness, and model, because expectations and tooling evolve and the ability to maintain and update the workflow over time matters more than the initial choice.
- A suggested fix is not the deliverable: the agent reproduces the issue from production traces, applies the fix, reruns tests, and measures the impact on the specific flow before a human ever sees it.
- Service- and endpoint-level metrics (CPU, memory, P90s) don't map onto how coding agents reason; Hud's 'prod-to-code' approach captures function-level context linked back to the triggering endpoint, cron job, or consumer.
- Context has two failure modes simultaneously in production observability — too much low-signal data to reason over and too few traces to avoid speculation — so forensic detail is captured selectively, only above a P99 or defined threshold.
- Raw query access produced high eval variance; wrapping the ClickHouse query language in a set of skills (e.g. how to trace an HTTP 500, how to diff a memory spike against a baseline) made results consistent.
- Auto-opening PRs failed on human grounds — nobody triages 80 PRs — so the system scores by hot-path frequency, business criticality, and change risk, surfaces the highest-ROI (not highest-impact) item one at a time, and delivers a short human-readable gist that argues for its own priority.
- Autonomous agentic engineering demands 80–90% trust, a categorically higher bar than IDE-based agent use where an 80% success rate is fine because the engineer is in context to steer.
- The most interesting gain isn't doing existing work faster — it's automating a phase (the proactive weekly performance sweep) that simply never happened in engineers' day-to-day.

## Notable Quotes

> "we would know how much time it takes to do a specific optimization, but we never know how long it's going to take to investigate it and to find it"
>
> — [0:40](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=40s) &middot; *states the central diagnosis the whole talk is built on*

> "Google just published their Dora metrics for 2026 and we can see that the biggest impact of AI adoption on engineering is individual effectiveness"
>
> — [2:20](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=140s) &middot; *cites external data to frame the problem*

> "we basically feel more effective, we're more effective individually, but as a team, our throughput is kind of the same and our software breaks more often"
>
> — [2:20](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=140s) &middot; *sharp summary of the AI productivity gap, a claim others contest*

> "We fix it in emergency mode and then we go straight back to ignoring, which is a leaky bucket by definition."
>
> — [3:40](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=220s) &middot; *names the failure loop the automation targets*

> "that mostly happens because the research phase is a black box. It could take an hour or weeks"
>
> — [3:40](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=220s) &middot; *pinpoints which phase is worth automating and why*

> "if you can optimize something, but it runs every 3 weeks or you can like reduce 20 milliseconds, then it doesn't matter"
>
> — [7:13](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=433s) &middot; *concrete statement of the relevance filter*

> "So it's not hey, I have this idea of something that you can do. It's here's something that works."
>
> — [8:01](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=481s) &middot; *defines the bar for what gets handed to a human*

> "the first hurdle we had along the way is what we call the plausible unverified. So the agent would suggest a fix. It sounds right."
>
> — [8:01](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=481s) &middot; *names a reusable failure mode of agentic debugging*

> "when something throws an exception and then the agent says, "Well, maybe we can just catch that exception and then everything will be fine.""
>
> — [8:43](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=523s) &middot; *vivid example of the lazy-fix failure mode*

> "There are only two problems with context. You either have too much of it or you have too little of it."
>
> — [9:35](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=575s) &middot; *memorable framing of the context engineering tradeoff*

> "our coding agents reason over code and they look at these metrics and there are some relations between them, but they don't exactly speak the same language"
>
> — [10:26](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=626s) &middot; *explains why standard observability data underserves coding agents*

> "the agent's context lies on a function and file level, not on an service and endpoint level"
>
> — [11:13](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=673s) &middot; *the technical thesis behind prod-to-code*

> "being able to get to the right query and to ask it again and again really created a lot of variance in our eval"
>
> — [12:49](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=769s) &middot; *reports a concrete eval finding that motivated skills over raw queries*

> "no one wants to wake up for, you know, a rain of 80 pull requests, as small as small as they can be"
>
> — [15:18](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=918s) &middot; *the human-factors failure that killed the naive auto-PR design*

> "we're not necessarily looking for the highest impact ones, but for the highest ROI ones"
>
> — [16:36](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=996s) &middot; *states the prioritization tradeoff explicitly*

> "context over cleverness works almost every time"
>
> — [18:25](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1105s) &middot; *the talk's compressed takeaway*

> "We're automating a phase that just did not happen in the day-to-day lives of engineers."
>
> — [19:19](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1159s) &middot; *reframes agent value as new work, not faster work*

> "I do believe that at least for most of the cases, the models are good enough already to be able to to automate that"
>
> — [20:09](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1209s) &middot; *takes a side on whether model capability is the bottleneck*

> "agentic engineering is not like coding with an agent. If something works 80% of the time and you're using it with your cursor in your IDE, that's fine because you're there, you're in context"
>
> — [20:49](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1249s) &middot; *the sharpest distinction in the talk, and directly comparable across talks*

> "getting to that agentic engineering automation level requires crossing towards the 80-90% trust"
>
> — [21:39](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1299s) &middot; *puts a number on the autonomy threshold*

## Positions

- The bottleneck in performance work is the unbounded investigation phase, not the fix itself, so investigation is what should be automated. ([0:40](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=40s), confidence: stated)
- AI adoption has increased individual effectiveness and software delivery instability while leaving team throughput roughly unchanged, per Google's 2026 DORA report. ([2:20](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=140s), confidence: stated)
- Agentic workflow infrastructure should be vendor-neutral across compute, harness, and model rather than committed to one provider. ([4:26](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=266s), confidence: stated)
- An agent-proposed fix is insufficient without runtime verification that the fix actually improved the specific production flow. ([7:13](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=433s), confidence: stated)
- Production observability suffers from too much low-signal data and too little targeted forensic data at the same time. ([9:35](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=575s), confidence: stated)
- Service- and endpoint-level metrics are the wrong granularity for coding agents, which reason at the function and file level. ([11:13](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=673s), confidence: stated)
- Wrapping query access in structured skills produces more consistent agent results than letting the agent author queries freely. ([12:49](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=769s), confidence: stated)
- Runtime production context finds real performance problems that static code analysis can only guess at. ([14:29](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=869s), confidence: stated)
- Auto-opening large volumes of PRs is counterproductive; surfacing one high-ROI, human-readable finding at a time builds the habit instead. ([16:01](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=961s), confidence: stated)
- Prioritization should weigh impact against review risk, favoring highest-ROI changes over highest-impact ones. ([16:36](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=996s), confidence: stated)
- Current models are already good enough to automate this class of work; the remaining work is steering, context, and guardrails. ([20:09](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1209s), confidence: stated)
- Autonomous agent automations require roughly 80-90% trust, whereas an 80% success rate is acceptable for interactive IDE agent use. ([20:49](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1249s), confidence: stated)
- The biggest value of coding agents is surfacing work teams would otherwise never do, not just accelerating existing work. ([19:19](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1159s), confidence: stated)
- Scoring and guardrails, not model capability, are what make an autonomous workflow reliable enough to trust. ([18:25](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1105s), confidence: implied)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [context engineering](../concepts/context-engineering.md)
- [developer productivity metrics](../concepts/developer-productivity-metrics.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [roi measurement](../concepts/roi-measurement.md)
- [verifier design](../concepts/verifier-design.md)

