---
title: "Medic for Apache Spark - First Aid for Failing Jobs"
type: "talk"
slug: "medic-for-apache-spark-first-aid-for-failing-jobs"
org: "Pinterest"
video_id: "0RNNfxpdbQk"
duration_sec: 680
word_count: 1569
speakers: ["Drasko Profirovic"]
---

# Medic for Apache Spark - First Aid for Failing Jobs

**Speakers:** [Drasko Profirovic](../speakers/drasko-profirovic.md)

**Org:** Pinterest

**Duration:** 11m 20s

[Watch on YouTube](https://www.youtube.com/watch?v=0RNNfxpdbQk)

## Summary

Draško Profirovic, a staff engineer at Pinterest, walks through the evolution of Medic for Apache Spark — an agentic diagnostics tool that answers 'why did this job fail?' with an evidence-backed root cause report and grounded suggested fixes. The talk traces the arc from an MCP-plus-single-ReAct-agent prototype, which broke down under prompt tuning conflicts, inconsistent response quality, and context window exhaustion from log tool outputs, to a multi-agent architecture built on LangGraph's deep agents library. The most transferable engineering content is the offline eval story (a record/playback test harness that snapshots production tool responses as checked-in fixtures) and two context-engineering tricks: an exception classifier pipeline that learns which exceptions appear in successful jobs and filters them as red herrings, and rendering time-series metrics as collaged images analyzed in a quarantine sub-agent so token cost is constant regardless of job duration. It's a short, dense, concrete case study worth watching for anyone building diagnostic agents over noisy observability data. Notably, the team tried making the agent more deterministic with LangGraph workflows and found that brittle compared to the ReAct paradigm.

## Key Points

- The motivating insight is that human support rotations force painful prioritization between competing teams, while LLM-based diagnostics can scale knowledge and capacity on demand without ranking asks.
- The single-prompt ReAct agent failed for structural reasons: one prompt had to do everything, so adding detail in one area degraded behavior in another, and quality was inconsistently shallow or verbose.
- Large tool outputs — especially raw logs — consumed the context window and halted the agent's reasoning on production-scale jobs.
- Manual end-to-end testing against production was unreliable because production data gets retentioned away, making it impossible to know whether changes broke earlier wins.
- The team built a record/playback test harness where real tool responses are captured as fixtures and checked in as code, letting offline evals grade generated reports (e.g. penalizing more than three suggested fixes) and quantify quality instead of relying on intuition.
- Log handling moved from regex heuristics to an exception classifier pipeline that fingerprints and clusters exceptions, learns which ones appear in successful jobs as likely red herrings, and ranks the rest by relevance and recency relative to job termination.
- The agent no longer reads logs directly; it gets two MCP tools — top-K truncated exceptions and full details for a specific exception — which reduced anchoring on misleading exceptions.
- Time-series metrics are converted to annotated graph collages and analyzed by a quarantine sub-agent, guaranteeing a fixed input token count regardless of job duration while surfacing signals like executors dropping to zero or long plateaus.
- The final architecture classifies intent, triages job lifecycle state, generates failure hypotheses researched in parallel by scoring research agents, then has a supervisor pick the highest-confidence root cause and invoke a healer agent backed by runbooks in a vector database.
- Decomposing into per-agent prompts made scope expansion cheap — extending Medic to Spark SQL optimization was essentially adding a new prompt.

## Notable Quotes

> "It's not always straightforward to rank these asks, but as humans, we often have to decide how we'll spend our time. The same is not true for LLMs. We can easily scale out knowledge and capabilities on demand."
>
> — [0:52](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=52s) &middot; *States the core economic argument for agentic support tooling.*

> "Our vision for a diagnostics agent was to ask it simply, "Why did a job fail?" and get back a deep research document which provides evidence on the root cause of the failure."
>
> — [0:52](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=52s) &middot; *The product goal in one sentence, framing diagnostics as deep research.*

> "This worked in practice, but it required a lot of careful prompting from the human operator."
>
> — [1:44](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=104s) &middot; *Names the limitation of bare MCP-plus-chat that motivates an agent harness.*

> "Prompt tuning became unsustainable. One prompt had to do everything, and adding detail in one area degraded the behavior in another."
>
> — [2:26](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=146s) &middot; *The clearest statement of why single-prompt agents don't scale in scope.*

> "As an example, large tool outputs from logs would click quickly consume tokens and brought a halt to the agent's reasoning."
>
> — [3:20](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=200s) &middot; *Concrete failure mode driving the whole context-engineering effort.*

> "Lastly, our end-to-end testing strategy up to this point relied on manual tests from production. This felt anecdotal since production data would be retentioned away."
>
> — [3:20](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=200s) &middot; *Underrated eval problem: your production repro disappears on a retention clock.*

> "In record mode, the agent calls real downstream systems, and tool responses are captured as fixtures. These are then saved to the file system and checked in as code."
>
> — [4:15](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=255s) &middot; *The reusable mechanic of the test harness, stated precisely.*

> "For example, an offline eval might check for a limit of three suggested fixes."
>
> — [4:15](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=255s) &middot; *Rare concrete example of encoding output verbosity as a scored eval.*

> "Our end-to-end tests allowed us to quantify quality instead of relying on intuition."
>
> — [5:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=307s) &middot; *Crisp articulation of what eval infrastructure buys a team.*

> "Logs are noisy, and many exceptions we see in logs are benign. So, simply focusing the last exception may not always be suitable."
>
> — [5:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=307s) &middot; *Rejects the naive heuristic most log-diagnosis tools start with.*

> "Initially, we kept it simple with a heuristics based approach using regex to filter out certain exceptions. But, this didn't scale well."
>
> — [5:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=307s) &middot; *Documents the failed simpler approach before the learned classifier.*

> "The core idea was we would learn which exceptions commonly appear in successful jobs, treat those as likely red herrings, and filter them out in the future analysis."
>
> — [5:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=356s) &middot; *The single most portable idea in the talk for noise reduction.*

> "The agent stopped consuming logs directly, and instead was given two MCP tools. Get the top K truncated exceptions, or get full log details for a specific exception."
>
> — [5:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=356s) &middot; *Shows progressive-disclosure tool design instead of dumping raw data.*

> "Raw time series metrics are not context window friendly. Simply feeding the raw data to an LLM works in the small scale, but fails for long-running jobs in production. Not to mention, it's horribly token inefficient."
>
> — [6:44](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=404s) &middot; *Names a tradeoff many teams hit when piping observability data into LLMs.*

> "Images worked better because we could guarantee how many input tokens would be used for analyzing any given Spark job irrespective of its duration."
>
> — [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s) &middot; *The counterintuitive argument for rendering data as images: bounded token cost.*

> "Examples of useful signals we would be able to get included executors dropping down to zero or near zero, long plateaus or bottlenecks, effectively any resource behavior inconsistent with healthy progress."
>
> — [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s) &middot; *Evidence the image approach actually recovers real diagnostic signal.*

> "Our sub agent would summarize its findings and return the results back to the parent agent, thereby ensuring the context window is kept healthy."
>
> — [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s) &middot; *Explains sub-agent quarantine as a context management pattern.*

> "A pleasant consequence of this architecture was that the effort to expand the scope of the project was as simple as adding a new prompt."
>
> — [9:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=547s) &middot; *The payoff claim for multi-agent decomposition, backed by the Spark SQL extension.*

> "The supervisor selects the highest confidence root cause and invokes the healer agent to offer remediations based on runbooks ingested into our vector database."
>
> — [9:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=596s) &middot; *Shows where retrieval fits: remediation grounding, not root cause finding.*

> "We trialed using LangGraph's workflows to make the agent more deterministic, but this approach proved to be brittle compared to the reasoning and acting agent paradigm."
>
> — [9:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=596s) &middot; *A directly contestable position on determinism vs. ReAct that other talks dispute.*

## Positions

- A single ReAct agent with one monolithic prompt cannot scale in scope, because adding detail for one behavior degrades another. ([2:26](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=146s), confidence: stated)
- Manual end-to-end testing against live production is inadequate for agent development because production data is retained only briefly, making regressions undetectable. ([3:20](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=200s), confidence: stated)
- Snapshotting real tool responses as checked-in fixtures plus offline evals lets teams quantify agent quality rather than rely on intuition. ([5:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=307s), confidence: stated)
- Simply taking the last exception in a log is an unreliable root-cause heuristic because many logged exceptions are benign. ([5:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=307s), confidence: stated)
- Regex-based exception filtering does not scale; a learned fingerprint-and-cluster classifier trained on exceptions from successful jobs works better. ([5:07](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=307s), confidence: stated)
- Improved log handling produced a substantial reduction in inaccurate root causes. ([9:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=596s), confidence: stated)
- Rendering time-series metrics as images is superior to feeding raw series to an LLM, because it guarantees a fixed input token count regardless of job duration. ([7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s), confidence: stated)
- Deterministic LangGraph workflows are more brittle than the reasoning-and-acting agent paradigm for this diagnostic task. ([9:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=596s), confidence: stated)
- Multi-agent architecture offers greater control over system behavior than a single-agent design. ([9:56](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=596s), confidence: stated)
- Agent harness features popularized by coding tools — to-do lists, virtual file systems, per-agent tool subsets — transfer usefully to non-coding domains like infrastructure diagnostics. ([8:23](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=503s), confidence: implied)
- This diagnostic agent pattern generalizes to other distributed systems such as Flink and Trino. ([10:57](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=657s), confidence: stated)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [context window management](../concepts/context-window-management.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

