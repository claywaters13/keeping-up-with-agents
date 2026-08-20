---
title: "roi measurement"
type: "concept"
slug: "roi-measurement"
tier: "supporting"
maturity: "contested"
talk_count: 11
speaker_count: 11
---

# roi measurement

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **11** talk(s) by **11** speaker(s)

**Definition:** Quantifying the business return of AI deployments and using it to prioritize, justify, or kill agent investments.

*Also referred to as: enterprise ai roi measurement, agent deployment roi, roi scoring and prioritization, time to value, technical debt roi, revenue per employee, cost governance for agents*

## State of Practice

As of this conference, the field treats "did it reach production?" as the wrong question and "does it justify its cost?" as the right one — and openly admits it does not yet know how to answer the second. Practitioners cite the MIT/Stanford failure statistics (95% of pilots never reach production, 87% show no measurable ROI, 89% of agents never productionized) but several speakers explicitly reject the framing: agents ship fine, they just fail to pay for themselves. The diagnosis is near-unanimous and specific: model capability is no longer the binding constraint, so ROI is determined by process redesign, context plumbing, reliability infrastructure, and workflow architecture — the 2x and 100x users are running identical weights. The proxy metrics the industry used through 2025 are being retired: token consumption, lines of code, weekly active users, and self-reported individual effectiveness are all called out as actively misleading, with Google's 2026 DORA data cited as evidence that individual effectiveness rose while team throughput stayed flat and delivery instability increased. What replaces them is unsettled: FDE-side speakers reduce everything to revenue up / cost down / risk mitigated agreed in writing before build; engineering-side speakers demand runtime verification against a measured baseline across repeated runs, and reliability thresholds around 80–90% rather than the 50% success rate typically graphed. Nobody claimed a general solution; one speaker said flatly that whoever solves ROI measurement for agents becomes a $5 trillion company.

## Consensus

### Model capability is no longer the binding constraint on returns; ROI is determined by workflow architecture, process redesign, context, and reliability infrastructure sitting around the model.

Support: **6** talk(s)

> "The 2X people and the 100X people are using the exact same Claude. Same weights, same context window, same API. So, the leverage is not in the weights. It's in how you wire the work."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s)

Supporting talks: [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)

### The dominant failure mode of enterprise AI is not deployment failure but economic failure — systems that run in production and never justify their cost.

Support: **3** talk(s)

> "The question to ask is whether they actually work, whether they actually make or save money, whether they justify their ROI"
>
> — [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [3:02](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=182s)

Supporting talks: [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)

### Activity proxies — token spend, lines of code, weekly active users, self-reported individual effectiveness — are the wrong ROI metrics and should be replaced with delivery/outcome measures.

Support: **4** talk(s)

> "we basically feel more effective, we're more effective individually, but as a team, our throughput is kind of the same and our software breaks more often"
>
> — [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [2:20](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=140s)

Supporting talks: [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)

### A plausible-looking agent output is not evidence of value; claimed gains must be verified against actual runtime behavior or a measured baseline before being counted.

Support: **4** talk(s)

> "it's very easy to undergo AI psychosis, where you look at a deep research report that's 20 pages long and you say, "Wow, this looks good." And then those features don't actually exist in the product, and you've set yourself back."
>
> — [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [4:24](https://www.youtube.com/watch?v=7vn4WpqNpck&t=264s)

Supporting talks: [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)

### Enterprise AI value must be tied to a small fixed set of business outcomes — revenue increase, cost decrease, risk mitigation — and the success definition should be agreed with the customer before building.

Support: **3** talk(s)

> "It's always three things, super simple. Am I increasing revenue? Am I decreasing costs? Or am I mitigating risks? That's it. Every company, as complex as they are, that's what they care about."
>
> — [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [19:32](https://www.youtube.com/watch?v=APqXGyCoGW4&t=1172s)

Supporting talks: [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)

## Disagreements

### To generate real ROI, should an initial deployment be scoped narrowly to prove value fast, or scoped department-wide from the start?

| Position A | Position B |
|---|---|
| Narrow the scope deliberately: pick a single narrow task per agent, compress time-to-proven-value, then expand. Many small agents beat one broad one, and multi-month time-to-value kills deals.<br>*[How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* | Point solutions cap out at low single-digit-to-10% ROI; only holistic department- or organization-wide transformation reaches 25–75%, and single-point tools structurally cannot make a whole organization faster.<br>*[AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)* |

*Why it matters: This determines whether you sell a six-week narrow pilot or a multi-quarter transformation engagement, and whether the ROI you can honestly promise is 5–10% or 25–75%. Narrow scoping de-risks the deal but may structurally cap the return below the threshold that justifies the program at all.*

### Are headline agent-productivity multipliers valid ROI evidence, or must every claim be reported against an equivalent non-AI baseline across repeated runs?

| Position A | Position B |
|---|---|
| Headline multipliers are the reportable result: ~82% delivery-time reduction, ~150% additional effective headcount, double the PR output, an order-of-magnitude more PRs in six months, 400X coding output since 2013.<br>*[How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* | A single favorable run is a demo, not evidence. Report against an equivalent deterministic or pre-AI baseline across repeated runs, and label synthetic/benchmark results as feasibility only — the RL policy beat the hand-written deterministic policy by 0.19 percentage points across 30 runs.<br>*[Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)* |

*Why it matters: If baselines are mandatory, most published agent ROI numbers are unverifiable and a large share of the measured gain may be attributable to the non-AI parts of the system (state design, decision logic, safety constraints) rather than the model.*

### Should an ROI model assume human review and supervision costs decline as models improve?

| Position A | Position B |
|---|---|
| No — human supervision is permanent, not a transitional cost. The goal is allocating human attention where it pays, and in high-stakes verticals the correct model is AI-in-the-loop, where the expert still decides and AI only compresses their time. Self-service controls must stay in the product because users only delegate when they can take the wheel back.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* | Yes — models are already good enough to automate whole classes of work given the right steering and context, and within roughly six months they will complete substantial multi-repo refactors consistently, so review overhead should be modeled as shrinking.<br>*[From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)* |

*Why it matters: It decides whether the payback calculation amortizes human review cost to near zero over a year or carries it permanently as a fixed line item — which flips the sign on many autonomous-agent business cases, especially in regulated verticals.*

## Practical Guidance

**Do:**

- Write the success definition — the specific metric and communication channel — into the deal before any building starts, and reduce it to revenue up, cost down, or risk mitigated.
- Verify a proposed fix at runtime against the specific production flow it claims to improve; ship 'here is something that works,' not 'here is an idea.'
- Evaluate model time-horizon claims at the 80% (ideally 90–99%) success rate rather than the commonly-graphed 50% — a 50%-reliable one-hour job usually just costs you the hour.
- Require roughly 80–90% trust before promoting an agent workflow from interactive IDE use to autonomous automation; 80% is fine when a human is sitting in context, not when they aren't.
- Benchmark the agent against an equivalent hand-written deterministic policy across repeated runs (30 runs in the ETL case) before crediting the learned component with the gain.
- Rank candidate automations by ROI — impact weighed against review risk — not by raw impact, and surface one high-ROI, human-readable finding at a time.
- Ingest the customer's historical operational data and use it to tell them which workflow to automate first for highest return.
- For delegation products, track weekly active sessions rising while weekly active users falls; treat rising WAU as a signal the product is still demanding participation.
- Use commit rate and the breadth of developers contributing as the payoff signal for a refactor, not lines of code.
- Hire the domain expert before you start iterating — engineers cannot tell whether vertical output is good, and this is where vertical AI projects quietly die.
- Run error analysis over your observability logs before reaching for any weight-touching technique; it is the cheapest and highest-ROI improvement path.
- Upstream every task an engineer had to do manually into the product, so per-customer work amortizes across the next four customers.

**Avoid:**

- Layering AI on top of broken, undocumented processes and expecting measurable return — this is cited as the primary reason pilots produce no ROI.
- Optimizing for token consumption as a KPI; that was a subsidized-era target and enterprises are now asking whether they got value.
- Deploying agents without specific direction — with a complex SDLC that is straight-up token maxing with no tangible outcome.
- Requiring the customer to migrate off their system of record (NetSuite, SAP, Dynamics, Salesforce) as a precondition — they spent millions and years getting there.
- Collapsing a familiar 11-step workflow into one step; the efficiency gain is erased by the adoption collapse.
- Adding enough complexity to the codebase that you outrun the ROI you already generated.
- Using LLM-as-judge to score quality in domains without answer keys (finance, pharma) — the model emits plausible jargon and rubrics-as-rewards become an echo chamber where the AI grades itself into agreement.
- Auto-opening large batches of PRs; nobody wants to wake up to 80 pull requests, however small.
- Selling a fixed allocation of engineers for a fixed period without a defined problem, or running an engagement with no named counterpart team on the customer side.
- Optimizing an operational agent for non-escalation rate — escalation is a correct action, not a failure.
- Treating citations as the value delivery mechanism; they shift verification burden back onto the customer and add net work.
- Measuring only the fix and not the investigation phase — the unbounded research black box is where the time actually goes.

## Notable Outliers

- Measuring the ROI of agent deployments is currently an unsolved problem, and whoever solves it will be a $5 trillion market cap company. ([How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [5:18](https://www.youtube.com/watch?v=RVxym6mmIns&t=318s))
- The '89% of enterprise AI agents never reach production' statistic is wrong in framing — every AI reaches production; it just fails to justify its own cost. ([Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [16:20](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=980s))
- Point solutions confined to one function yield 5–10% ROI; department-wide transformation yields 25–75%. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [11:07](https://www.youtube.com/watch?v=l0FLhNqBOic&t=667s))
- The RL policy beat an equivalent hand-defined deterministic policy by only 0.19 percentage points on this compact state space — reliability came from state design and external safety constraints, not from RL. ([Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [10:11](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=611s))
- For agentic products, the target is weekly active users going down while weekly active sessions go up. ([Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [13:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=816s))
- A successful engagement is defined by the customer not turning the deployed systems off after the team walks away — that is the strict ROI test. ([Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [8:20](https://www.youtube.com/watch?v=APqXGyCoGW4&t=500s))
- The biggest value of coding agents is surfacing work teams would otherwise never do at all, not accelerating work already on the backlog. ([From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [19:19](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1159s))

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
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)

## Speakers

- [Anna Marie Benzon](../speakers/anna-marie-benzon.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
- [Denys Linkov](../speakers/denys-linkov.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Jia Wu](../speakers/jia-wu.md)
- [May Walter](../speakers/may-walter.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Pauline Brunet](../speakers/pauline-brunet.md)
- [Sunny Rekhi](../speakers/sunny-rekhi.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)

