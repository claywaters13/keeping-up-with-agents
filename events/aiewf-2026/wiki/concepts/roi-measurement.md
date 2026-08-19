---
title: "roi measurement"
type: "concept"
slug: "roi-measurement"
tier: "supporting"
maturity: "contested"
talk_count: 10
speaker_count: 10
---

# roi measurement

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **10** talk(s) by **10** speaker(s)

**Definition:** Quantifying the business return of AI deployments and using it to prioritize, justify, or kill agent investments.

*Also referred to as: enterprise ai roi measurement, agent deployment roi, roi scoring and prioritization, time to value, technical debt roi, revenue per employee, cost governance for agents*

## State of Practice

As of this conference, practitioners have stopped treating model capability as the variable that determines return and moved the question to process design, deployment scope, and measurement discipline — the same weights produce 2X and 100X outcomes depending on how the work is wired. The credibility of AI ROI claims is under active pressure: the MIT figure that 95% of GenAI pilots never reach production and ~87% show no measurable return gets cited approvingly, Google's 2026 DORA data shows individual effectiveness up while team throughput is flat and instability rises, and one forward-deployed lead states flatly that measuring agent ROI is still an unsolved problem. The metrics practitioners are abandoning are explicit — token usage as a KPI, lines of code, raw PR counts, weekly active users — and the replacements are workflow-anchored: time-to-resolution against a modeled manual baseline, delivery-timeline compression, commit rate and breadth of contributing developers, weekly active sessions rising while WAU falls. Reliability is now treated as an ROI term rather than a quality term: a one-hour agent run that completes 50% of the time is a wasted hour, so delegation decisions are made at the 80%+ success band, and autonomous automations are held to roughly 80-90% trust before they run unattended. The sharpest live disputes are about scope (land narrow to prove value fast, or refuse point solutions because they only yield 5-10%) and about whether throughput deltas count as evidence at all when code quality and maintainability degrade underneath them.

## Consensus

### Model capability is no longer the binding constraint on return; the constraint is process design, workflow architecture, and infrastructure around the model.

Support: **5** talk(s)

> "The 2X people and the 100X people are using the exact same Claude. Same weights, same context window, same API. So, the leverage is not in the weights. It's in how you wire the work."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s)

Supporting talks: [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)

### Activity and volume proxies — token usage, lines of code, PR counts, weekly active users — are the wrong ROI metrics and should be replaced with outcome measures tied to the workflow.

Support: **4** talk(s)

> "your actual aim should be the weekly active users go down while weekly active sessions go up"
>
> — [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [13:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=816s)

Supporting talks: [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)

### Plausible-looking agent output is not evidence of return; claimed gains must be verified against a baseline, a runtime check, or repeated runs before being counted.

Support: **4** talk(s)

> "it's very easy to undergo AI psychosis, where you look at a deep research report that's 20 pages long and you say, "Wow, this looks good." And then those features don't actually exist in the product, and you've set yourself back."
>
> — [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [4:24](https://www.youtube.com/watch?v=7vn4WpqNpck&t=264s)

Supporting talks: [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)

### Agents deployed without a specific named problem and pre-agreed success criteria consume budget without producing measurable return.

Support: **3** talk(s)

> "So, if the software development life cycle is extremely complex, deploying the agents for with like no specific direction, you're straight up just token maxing."
>
> — [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [4:46](https://www.youtube.com/watch?v=RVxym6mmIns&t=286s)

Supporting talks: [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)

### Reliability rate is an ROI term: below roughly 80% task completion, delegated agent runs destroy more time than they save, so the delegation threshold should be set at 80%+ rather than the commonly quoted 50%.

Support: **3** talk(s)

> "if you're kicking off a process that is going to take an hour and it has a 50% chance of completing, there's a very high chance you just wasted that hour and you could have been doing something different."
>
> — [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [8:33](https://www.youtube.com/watch?v=7vn4WpqNpck&t=513s)

Supporting talks: [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)

### Realized ROI is gated by adoption, not capability: a deployment that users abandon, distrust, or cannot take control back from returns nothing regardless of measured task performance.

Support: **3** talk(s)

> "I always say, if you put in the latest and greatest tech in your organization, and you don't accompany people, no one's going to use it."
>
> — [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [5:59](https://www.youtube.com/watch?v=APqXGyCoGW4&t=359s)

Supporting talks: [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)

## Disagreements

### Is the ROI of agent deployments actually measurable today?

| Position A | Position B |
|---|---|
| It is an ambiguous, unsolved problem — throughput gains cannot be causally attributed, individual effectiveness gains do not show up as team throughput, and added complexity can silently outrun whatever return was generated.<br>*[How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* | It is tractable with a small set of concrete measures — every enterprise value claim reduces to revenue up, cost down, or risk mitigated; MTTR against a modeled manual baseline; delivery-timeline compression; and historical customer data can rank which workflows to automate first by expected ROI.<br>*[Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)* |

*Why it matters: If ROI is unmeasurable, budget decisions fall back on velocity anecdotes and vendor case studies; if it is measurable, engagements can be scoped against a written target and killed when they miss it.*

### To maximize return, should an agent deployment land narrow and prove value fast, or refuse point solutions and transform a whole department at once?

| Position A | Position B |
|---|---|
| Deliberately narrow the initial scope, keep it directional and phased, and demonstrate value ASAP rather than accepting a multi-month kitchen-sink engagement.<br>*[How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)* | Function-level point solutions cap out around 5-10% ROI; the return only materializes when the whole department or organization is restructured around agents, because single-point tools cannot make an organization faster even if they make engineers faster.<br>*[AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* |

*Why it matters: This determines whether an AI budget buys a six-week pilot with a checkable success metric or a department-wide process redesign, and which of those two failure modes — trivial measured wins, or an unfalsifiable transformation program — you accept.*

### Does increased shipping velocity count as evidence of return?

| Position A | Position B |
|---|---|
| Yes — output deltas are the return: near order-of-magnitude more quality PRs in six months, roughly double the PR output versus single-point tools, ~82% delivery-timeline reduction, revenue per head that never previously existed.<br>*[How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* | No — velocity has risen while product quality, uptime, and maintainability fell; DORA 2026 shows individual effectiveness up with team throughput flat and software breaking more often, and added codebase complexity can outrun the ROI already generated.<br>*[Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)* |

*Why it matters: If velocity is the metric, the correct move is to ship more agent-generated code immediately; if it is not, the correct move is to spend six months on a refactor or on guardrails before the accumulated debt cancels the gains.*

## Practical Guidance

**Do:**

- Get success metrics and communication channels agreed in writing during the earliest deal conversations, before any agent is deployed
- Reduce every enterprise value claim to one of three things: increasing revenue, decreasing cost, or mitigating risk
- Model the manual baseline explicitly (e.g. ~2.5 working days for ETL failure recovery) and benchmark the agent against it across repeated runs — 30 runs, not one favorable run
- Evaluate model time-horizon curves at the 80% success band, ideally 90-99%, not the commonly shared 50%
- Hold autonomous, unattended automations to roughly 80-90% trust; 80% is only acceptable when a human is in the IDE watching
- Rank candidate automations by ROI (impact weighed against review risk), not by raw impact
- Target background-agent work at tasks that take users more than a couple of hours and are repeatable
- Track commit rate and breadth of contributing developers instead of lines of code when judging whether a refactor paid off
- Verify each proposed fix at runtime against the specific production flow it targets before counting it as a win
- Surface one high-ROI, human-readable finding at a time to build the review habit
- Ingest the customer's historical operational data to sequence which workflows to automate first by expected return
- Run in shadow mode on real incident traces before granting an agent execution authority
- Convert every agent task that succeeds into a reusable skill file so the win compounds instead of being one-off
- Insist on a named counterpart working team on the customer side; no counterpart means the engagement is structurally broken

**Avoid:**

- Making token usage the KPI, or deploying agents with no specific direction — that is token maxing, not value
- Selling or buying a fixed allocation of engineers for a fixed period with no defined problem attached
- Layering AI on top of broken, undocumented processes rather than redesigning them first
- Treating a 20-page deep-research report or a capability demo as evidence that features exist or work
- Counting shipping velocity as return while code quality, uptime, and maintainability degrade underneath it
- Shifting the verification burden onto the user via citations and calling the result a time saving — especially in healthcare, legal, and tax
- Collapsing a familiar 11-step workflow into one step; adoption suffers even when efficiency improves
- Optimizing something that runs every three weeks or saves 20 milliseconds
- Requiring the customer to migrate off their system of record (NetSuite, SAP, Dynamics, Salesforce) as a precondition for value
- Measuring an operational agent only by its non-escalation rate — escalation should be a legitimate action, not a failure
- Reaching for RL or a larger model where a hand-defined deterministic policy performs identically
- Auto-opening large volumes of PRs — nobody wants to wake up to a rain of 80 pull requests
- Using an FDE team for product 101/201 training sessions or as staff augmentation for an understaffed customer

## Notable Outliers

- Function-level point solutions yield only 5-10% ROI while department-wide transformation yields 25-75%. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [11:07](https://www.youtube.com/watch?v=l0FLhNqBOic&t=667s))
- Measuring agent ROI is an unsolved problem, and whoever solves it will be a $5 trillion market cap company. ([How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [5:18](https://www.youtube.com/watch?v=RVxym6mmIns&t=318s))
- The RL policy beat an equivalent hand-defined deterministic policy by only 0.19 percentage points; reliability came from state design and external safety constraints, not from learning. ([Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [10:11](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=611s))
- Google's 2026 DORA report shows AI adoption raised individual effectiveness while team throughput stayed flat and software broke more often. ([From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [2:20](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=140s))
- 95% of generative AI pilots fail to reach production and roughly 87% produce no measurable ROI. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [5:05](https://www.youtube.com/watch?v=l0FLhNqBOic&t=305s))
- The biggest value of coding agents is surfacing a class of work that never happened at all, not accelerating work already being done. ([From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [19:19](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1159s))
- A successful engagement is defined by the customer not turning the systems off after the team leaves. ([Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [8:20](https://www.youtube.com/watch?v=APqXGyCoGW4&t=500s))
- AI-generated code cannot be proven to have caused the batch's growth, even though a quarter of the batch was 95% AI-generated and it was YC's fastest-growing. ([Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [3:31](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=211s))

## All Talks

- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)
- [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)
- [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)

## Speakers

- [Anna Marie Benzon](../speakers/anna-marie-benzon.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Denys Linkov](../speakers/denys-linkov.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Jia Wu](../speakers/jia-wu.md)
- [May Walter](../speakers/may-walter.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Pauline Brunet](../speakers/pauline-brunet.md)
- [Sunny Rekhi](../speakers/sunny-rekhi.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)

