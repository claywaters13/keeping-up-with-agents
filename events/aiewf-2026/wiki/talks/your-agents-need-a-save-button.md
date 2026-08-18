---
title: "Your Agents Need a Save Button"
type: "talk"
slug: "your-agents-need-a-save-button"
track: "AI-Native Enterprises"
org: "ZenML"
day: "Day 4 — Session Day 3"
room: "Leadership 1"
video_id: "bZISsg7H7DA"
duration_sec: 1027
word_count: 2937
speakers: ["Kunal Lanjewar"]
---

# Your Agents Need a Save Button

*Program title: Your Hero Agent Needs a Party*

**Speakers:** [Kunal Lanjewar](../speakers/kunal-lanjewar.md)

**Org:** ZenML

**Track:** AI-Native Enterprises &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Leadership 1 &nbsp;|&nbsp; **Duration:** 17m 07s

[Watch on YouTube](https://www.youtube.com/watch?v=bZISsg7H7DA)

## Summary

Hamza Tahir argues that agents are missing the equivalent of a save button: traces capture emitted telemetry but are disconnected from the runtime, so in-flight variables, filesystem state, and the code itself are lost and frozen into a read-only artifact far from where execution happened. His fix is a durable runtime beneath the agent harness that checkpoints state so any execution can be forked and replayed with one thing changed — a cheaper model, a mocked tool, a different policy — then diffed against the real baseline. He demos this with Kitaru, an open-source tool from ZenML, walking through single replays, side-by-side diffs, cohort replays, and handing the resulting JSON report to an MCP server for LLM analysis. Crucially, he undercuts his own demo: the single replay looked cheaper at equal quality, but the cohort analysis returned 'don't ship,' and he cites a BrainTrust study on the false economy of naive model swaps plus τ-bench data showing a model passing 60% of the time is self-consistent only a quarter of the time. Watch it if you want a concrete methodology — checkpoint, replay, diff, decide — for turning production traces into grounded evals rather than synthetic ones.

## Key Points

- Traces alone are insufficient because they are decoupled from the runtime: variables in state, the in-flight filesystem, the decisions made in code, and the code itself are all lost by the time a read-only span lands in a separate observability tool.
- The missing layer sits between the agent framework/harness and infrastructure: a durable runtime that checkpoints execution state and augments OpenTelemetry spans with the actual code and environment, including the Docker image or sandbox it ran in.
- Once checkpointing runs in production, you already have everything needed for counterfactual evaluation — no synthetic dataset construction required, because replays are grounded in runs that actually happened.
- The methodology is a four-step loop: checkpoint, replay, diff, decide — build a cohort of runs that matter (expensive, slow, or risky), apply one change, diff against the known baseline, then route and ship.
- Replay is cheap because prior checkpoints are reused: in the demo the first three checkpoints are skipped entirely and execution resumes only from the modified point.
- Naive model swaps frequently fail in practice, and Tahir cites a BrainTrust study showing a 'false economy' where cost and latency improve on paper while the value created — such as whether the support bot actually resolves the request — degrades.
- A single replay is an anecdote, not evidence: on τ-bench a model that passes 60% of the time is only self-consistent about a quarter of the time, so cohort-scale replay is required before shipping.
- Cohort analysis at scale outgrows UI diffing, so Tahir emits JSON and points an MCP server at it, using LLMs to analyze thousands of replays and flag red flags — which is why the runtime needs to be queryable and able to fetch artifacts.
- DoorDash's simulated replay environment (per a June 1 blog post) cut a multi-hour process to five minutes across hundreds of simulations, with 90% fewer hallucinations and results within two points of observed production behavior.
- His own demo ends with the agent's verdict being 'don't ship' — the cheaper model looked fine on one sample and failed across the cohort.

## Notable Quotes

> "We've had the save button for documents for decades now. Since the 1980s, people have been used to pressing control S, command S uh or auto saving while you're working to have a persistent state. But agents, they don't have that today."
>
> — [0:00](https://www.youtube.com/watch?v=bZISsg7H7DA&t=0s) &middot; *the framing device the whole talk hangs on*

> "The only thing we have which is closest is a trace. A trace gives you the emitted telemetry data of how an agent calls tools in the input and output of that state."
>
> — [0:00](https://www.youtube.com/watch?v=bZISsg7H7DA&t=0s) &middot; *defines the baseline he's arguing is inadequate*

> "all of that is lost and it is only stamped as a read-only trace by the end, which is sitting in another tool far away from where the actual code is"
>
> — [0:47](https://www.youtube.com/watch?v=bZISsg7H7DA&t=47s) &middot; *the core critique of trace-only observability*

> "I think this is what's missing today in the industry is that we don't have a clear connection between the observability spans that are emitted with Odel and the execution."
>
> — [0:47](https://www.youtube.com/watch?v=bZISsg7H7DA&t=47s) &middot; *states the gap as an industry-level claim, not just a product pitch*

> "Well, save allows you to replay. You can go back in history and ask the what if question."
>
> — [1:25](https://www.youtube.com/watch?v=bZISsg7H7DA&t=85s) &middot; *the payoff that justifies the checkpointing cost*

> "So, checkpoint replay diff decide. And this is really the methodology that that I've seen and I've seen others do, uh which has really scaled."
>
> — [3:37](https://www.youtube.com/watch?v=bZISsg7H7DA&t=217s) &middot; *the talk's reusable four-step recipe*

> "It's It's It's basically evaluating using your production traces. So, it's basically evaluating using your production checkpoints."
>
> — [3:37](https://www.youtube.com/watch?v=bZISsg7H7DA&t=217s) &middot; *reframes replay as an eval strategy rather than a debugging tool*

> "now they've reduced it to 5 minutes uh with hundreds of simulations, have 90% less hallucinations, and they're still two points within what they've seen in production"
>
> — [4:27](https://www.youtube.com/watch?v=bZISsg7H7DA&t=267s) &middot; *the only third-party production numbers in the talk*

> "So, the simulations are pretty good because they're grounded in what's already happened."
>
> — [4:27](https://www.youtube.com/watch?v=bZISsg7H7DA&t=267s) &middot; *the argument for replay over synthetic evals in one line*

> "and this combination of code and the artifacts that it created and the environment in which it ran in, whether it was a Docker image or a sandbox, those are all snapshotted in state here between the checkpoints"
>
> — [5:49](https://www.youtube.com/watch?v=bZISsg7H7DA&t=349s) &middot; *specifies what 'state' actually means in his design*

> "because I have the code, it's very easy for me to do tool calls and to change these particular things and do more experiments than I would have had if I was completely disconnected from the code base"
>
> — [8:01](https://www.youtube.com/watch?v=bZISsg7H7DA&t=481s) &middot; *names the concrete advantage of runtime-coupled replay over external trace tools*

> "is to be using agents and LLMs to analyze these cohorts across a plethora of data because at some point uh, I mean, 10 is probably easy to do, but what if you have thousands?"
>
> — [11:44](https://www.youtube.com/watch?v=bZISsg7H7DA&t=704s) &middot; *explains why cohort analysis has to be delegated to models*

> "this is where skills and MCP servers get really relevant and having the runtime be queryable and go into your execution and fetch the artifacts is very important"
>
> — [12:41](https://www.youtube.com/watch?v=bZISsg7H7DA&t=761s) &middot; *states a design requirement for replay infrastructure*

> "what I've personally seen is that having a naive model swap usually or often times doesn't work"
>
> — [13:24](https://www.youtube.com/watch?v=bZISsg7H7DA&t=804s) &middot; *a firsthand negative result against the most common cost optimization*

> "they saw that there could be a false economy if you do a naive model swap because it might look on paper that you're faster and you're cheaper, but at the end of the day you have to look at the value created"
>
> — [14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s) &middot; *names the tradeoff and attributes it to external research*

> "a model that passes 60% of the time is only self-consistent about a quarter of the time"
>
> — [14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s) &middot; *the hard number behind his methodological warning*

> "So which basically means that one replay is just an anecdote and having a cohort analysis is way way way better."
>
> — [14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s) &middot; *the sharpest methodological claim in the talk*

> "This can get very expensive of course and this is where you have to be really smart about what you replay and have tooling that really helps you."
>
> — [14:44](https://www.youtube.com/watch?v=bZISsg7H7DA&t=884s) &middot; *acknowledges the cost of the approach he's advocating*

> "you can start from real runs, not synthetic, but real runs, real production uh state"
>
> — [14:44](https://www.youtube.com/watch?v=bZISsg7H7DA&t=884s) &middot; *the playbook's first principle, stated as a preference over synthetic data*

> "Um never ship anything by just replaying one or two things. Um and just do this at scale and uh ship, route, and hold, and try to automate that loop as much as possible."
>
> — [15:28](https://www.youtube.com/watch?v=bZISsg7H7DA&t=928s) &middot; *prescriptive rule plus the human-in-the-loop caveat*

> "So, the verdict is don't ship. So, even though it looked like from a single replay that it was cheaper to do and we reached the same result, across a bunch of those support cases, you actually saw that our agent concludes that you shouldn't be using a cheaper model in this particular case for your data."
>
> — [15:28](https://www.youtube.com/watch?v=bZISsg7H7DA&t=928s) &middot; *the demo lands on a negative result, which is the point*

> "you can do this if you model your agent with your harness in a runtime that can checkpoint state and is able to replay that state from code with different scenarios"
>
> — [16:11](https://www.youtube.com/watch?v=bZISsg7H7DA&t=971s) &middot; *the closing statement of the required architecture*

## Positions

- Traces are insufficient for understanding agent behavior because they are disconnected from the runtime and discard in-flight variables, filesystem state, and the executing code. ([0:47](https://www.youtube.com/watch?v=bZISsg7H7DA&t=47s), confidence: stated)
- The industry lacks a clear connection between OpenTelemetry observability spans and the actual execution that produced them. ([0:47](https://www.youtube.com/watch?v=bZISsg7H7DA&t=47s), confidence: stated)
- A new layer of the stack is emerging that sits above agent frameworks/harnesses and provides a durable runtime beneath them. ([2:06](https://www.youtube.com/watch?v=bZISsg7H7DA&t=126s), confidence: stated)
- If a system already checkpoints in production, no additional data collection is needed to answer what-if questions about cost, latency, and quality. ([2:06](https://www.youtube.com/watch?v=bZISsg7H7DA&t=126s), confidence: stated)
- Replay-based evaluation should use real production runs and checkpoints rather than synthetic datasets. ([14:44](https://www.youtube.com/watch?v=bZISsg7H7DA&t=884s), confidence: stated)
- Simulations grounded in previously recorded executions are more trustworthy than ungrounded ones. ([4:27](https://www.youtube.com/watch?v=bZISsg7H7DA&t=267s), confidence: stated)
- DoorDash reduced a multi-hour replay process to 5 minutes with hundreds of simulations, 90% fewer hallucinations, and results within two points of production. ([4:27](https://www.youtube.com/watch?v=bZISsg7H7DA&t=267s), confidence: stated)
- Naive model swaps to cheaper models often fail in practice when evaluated on outcome quality rather than cost alone. ([13:24](https://www.youtube.com/watch?v=bZISsg7H7DA&t=804s), confidence: stated)
- Optimizing on cost as a single dimension produces a false economy, per a BrainTrust study. ([14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s), confidence: stated)
- On τ-bench, a model that passes 60% of the time is self-consistent only about a quarter of the time. ([14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s), confidence: stated)
- A single replay is not evidence; decisions require cohort-level analysis. ([14:05](https://www.youtube.com/watch?v=bZISsg7H7DA&t=845s), confidence: stated)
- Nothing should be shipped on the basis of one or two replays. ([15:28](https://www.youtube.com/watch?v=bZISsg7H7DA&t=928s), confidence: stated)
- Analyzing replay cohorts at thousands-scale requires LLMs and agents, not human inspection of UI diffs. ([11:44](https://www.youtube.com/watch?v=bZISsg7H7DA&t=704s), confidence: stated)
- Replay infrastructure must expose a queryable runtime that can fetch artifacts, so that MCP servers and skills can operate on it. ([12:41](https://www.youtube.com/watch?v=bZISsg7H7DA&t=761s), confidence: stated)
- Replay at scale is expensive enough that selecting what to replay is itself a design problem. ([14:44](https://www.youtube.com/watch?v=bZISsg7H7DA&t=884s), confidence: stated)
- The replay-and-decide loop should be automated, but a human should remain in the loop at the final decision point. ([15:28](https://www.youtube.com/watch?v=bZISsg7H7DA&t=928s), confidence: stated)
- Whether a cheaper model is acceptable is data-dependent and cannot be generalized across deployments. ([16:11](https://www.youtube.com/watch?v=bZISsg7H7DA&t=971s), confidence: stated)
- Coupling replay to the code base enables a wider range of experiments (such as mocking tools with real functions) than trace-only tooling allows. ([8:01](https://www.youtube.com/watch?v=bZISsg7H7DA&t=481s), confidence: stated)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [durable execution](../concepts/durable-execution.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [model portability](../concepts/model-portability.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [simulation environments](../concepts/simulation-environments.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

