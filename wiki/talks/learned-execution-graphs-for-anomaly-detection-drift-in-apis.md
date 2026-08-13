---
title: "Learned Execution Graphs for Anomaly Detection & Drift in APIs"
type: "talk"
slug: "learned-execution-graphs-for-anomaly-detection-drift-in-apis"
track: "Graphs"
org: "JP Morgan Chase"
day: "Day 4 — Session Day 3"
room: "Track 5"
video_id: "u1yaOeEX4e8"
duration_sec: 1178
word_count: 2723
speakers: ["Ritvik Pandya"]
---

# Learned Execution Graphs for Anomaly Detection & Drift in APIs

*Program title: AI : Learned Execution Graphs for Real-Time Anomaly Detection & Drift Classification in APIs*

**Speakers:** [Ritvik Pandya](../speakers/ritvik-pandya.md)

**Org:** JP Morgan Chase

**Track:** Graphs &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 19m 38s

[Watch on YouTube](https://www.youtube.com/watch?v=u1yaOeEX4e8)

## Summary

Ritvik Pandya, who leads a payments team at JP Morgan Chase, argues that request processing should be modeled as a short-lived 'execution graph' (a DAG of service hops) rather than only as persistent property graphs, so that latency problems can be localized to a specific node instead of an entire request path. He lays out a tiered detection pipeline: build a per-client, per-endpoint baseline from OpenTelemetry traces, detect deviation, localize it, then classify whether it is a one-off anomaly or a sustained drift. Drift is broken into structural (a node added or removed), scale/volume, and covariate (traffic mix shifts, e.g. domestic vs. cross-border payments) categories, each demanding a different remedy — rebaselining, scaling, or splitting into separate baselines. He closes with the operational realities: tail-based sampling, cold-start endpoints, delayed telemetry masquerading as structural change, deployment awareness for rollback decisions, and explainability so an alert is more than an opaque score. The talk is deliberately statistical rather than ML-heavy, and is most useful to engineers running latency-critical, multi-hop services who want fewer noisy alerts and faster mean time to discovery.

## Key Points

- Representing end-to-end request processing as a DAG makes execution order and inter-node context explicit, and lets you attribute a slowdown to a specific node rather than to the request as a whole.
- Detection should be tiered: a cheap first-pass baseline check on every request, with deeper structural and statistical analysis only triggered when the fast check shows deviation, so monitoring does not consume disproportionate resources.
- Anomalies (a one-off slow run) and drift (a sustained shift in the pattern) require different responses — drift usually means the baseline itself must be recomputed, not that an incident should be opened.
- Drift is categorized as structural (a node added or removed), scale/volume-driven, or covariate (the mix of traffic changed, e.g. more cross-border requests), and each category maps to a different action: rebaseline, scale out or go async, or split into separate per-segment graphs.
- Baselines must be scoped narrowly — per client, per endpoint, per payment type — rather than one global baseline for 'all POST requests', because a generic threshold produces noise.
- Telemetry must be fed asynchronously (OpenTelemetry into Kafka with stream processing) so that observability never adds latency to real-time payment processing, with a fast hot path for automatable decisions and a slower, more accurate reconciliation path.
- Delayed telemetry from one node looks identical to a node being removed, so the system needs tuned windows to avoid raising false structural-change alarms.
- Automated remediation should be risk-assessed and rolled out progressively — 5% or 10% of machines, verify, then 100% — and the system must know about new deployments so rollback is an option.
- Alerts need explainability: a bare anomaly score is as useless as a doctor telling you your health score is 22.

## Notable Quotes

> "what I'm talking about today is execution graph"
>
> — [0:01](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=1s) &middot; *Names the core object of the talk and distinguishes it from persistent property graphs.*

> "It's short-lived graph."
>
> — [1:23](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=83s) &middot; *The defining property that separates an execution graph from a Neo4j-style stored graph.*

> "idea here is holistically try to identify how the request processing happens and if there is any deviation on that and how to detect that and how to fix that"
>
> — [1:23](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=83s) &middot; *States the end-to-end goal in one line: detect deviation and act on it.*

> "if you know the baseline of your request execution end to end if uh everything looks Good. You don't need to go to the tier two uh or next tier of check."
>
> — [3:15](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=195s) &middot; *Articulates the tiered, cost-aware detection design.*

> "One of the uh the drift here could be because of the structural change. So if any new node or new step added which you are not aware of that could be one of the thing or one of the step which is removed that could be the another reason"
>
> — [4:05](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=245s) &middot; *Defines structural drift, the first classification the system makes.*

> "First you uh represent the entire request processing as DAG. You come up with the baseline. You find out the deviation and then you try to find out where exactly the issue is."
>
> — [5:00](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=300s) &middot; *The complete method in four steps.*

> "open telemetry and that star bench were used and say for 7 days of the time millions of uh traces were um you know injected or uh in the system then you inject the problem or uh anomaly there and based on that you train your system before anything goes on live"
>
> — [6:46](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=406s) &middot; *The only concrete benchmark setup described: fault injection over millions of traces.*

> "a year back it used to take one hour for you from your home to office but nowadays it it is taking 20 more minutes"
>
> — [7:41](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=461s) &middot; *The commute analogy that cleanly separates drift from a one-off anomaly.*

> "when you started the business uh you were seeing around 60% of local request but uh and 40% uh request from you know out of the country"
>
> — [11:04](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=664s) &middot; *Concrete numbers grounding the covariate-drift category.*

> "So nothing changed. Your system is working fine, right? But now you need to come up with the criteria and reassess your baselines again."
>
> — [11:52](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=712s) &middot; *The key counterintuitive claim: a healthy system can still invalidate its own baselines.*

> "This whole talk is mostly about statistical uh uh you know part of uh the solution."
>
> — [11:52](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=712s) &middot; *Explicitly scopes the approach as statistical rather than model-driven.*

> "once you know the risk either you can go with uh roll out that system uh um solution for say 5% or 10% of your uh machines monitor it verify everything looks good and then you roll out for your 100% of the nodes"
>
> — [12:55](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=775s) &middot; *Gives the specific progressive-rollout percentages for automated remediation.*

> "in the payments and the real time uh payment processing we want to keep it very faster right so we don't want delay the actual request processing"
>
> — [13:54](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=834s) &middot; *The latency constraint that forces asynchronous telemetry.*

> "There could be two different paths. One is say hot path where you can take a decision very faster and uh um work on the solution or automate that solution."
>
> — [14:55](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=895s) &middot; *Names the hot-path / reconciliation-path split in the processing architecture.*

> "What if one of the system is delaying the event? Should we consider it as a structural change because now what you have data in your system is for six nodes"
>
> — [14:55](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=895s) &middot; *Identifies the sharpest failure mode of the whole approach: late telemetry is indistinguishable from a missing node.*

> "here in this use case u we should go with tail by based system"
>
> — [15:52](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=952s) &middot; *A concrete architectural recommendation (tail-based sampling) others might contest.*

> "the cold start uh if there is a new endpoint consider the new baseline don't make it very generic"
>
> — [15:52](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=952s) &middot; *Prescribes per-endpoint baselines over generic ones.*

> "on the detect side any MMD or KL uh could be used"
>
> — [16:36](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=996s) &middot; *The only named statistical detection methods in the talk.*

> "mean time to uh discovery reduced a lot to make it very real time"
>
> — [16:36](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=996s) &middot; *The claimed operational payoff of the system.*

> "If you go to the doctor and doctor says your health score is 22, it doesn't make much sense to you."
>
> — [18:13](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=1093s) &middot; *The talk's argument for explainability over opaque anomaly scores.*

## Positions

- Request processing should be modeled as a short-lived DAG (an execution graph) rather than only as a persistent property graph, because the DAG makes execution order and per-node context explicit. ([1:23](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=83s), confidence: stated)
- A cheap tier-one baseline check should gate deeper analysis; if end-to-end execution matches the baseline, no further tier of checking is needed. ([3:15](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=195s), confidence: stated)
- Retries and loops should each be represented as a separate entity in the graph so they can be tracked individually. ([2:26](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=146s), confidence: stated)
- Baselines must be per-client, since a local client and a foreign client legitimately have different normal latencies, and using one shared baseline generates alert noise. ([4:05](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=245s), confidence: stated)
- A shift in traffic mix (covariate drift) requires either splitting into two separate comparison graphs or raising the average request time baseline, even though nothing in the system has broken. ([11:04](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=664s), confidence: stated)
- Telemetry must be fed asynchronously to OpenTelemetry, with Kafka and stream processing downstream, so observability does not slow real-time payment processing. ([13:54](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=834s), confidence: stated)
- Detection should run on two paths: a hot path for fast, automatable decisions and a slower reconciliation path that is more accurate. ([14:55](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=895s), confidence: stated)
- For this use case tail-based sampling is the right choice, because what matters is when the service request started and ended for each node. ([15:52](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=952s), confidence: stated)
- New endpoints should get their own new baseline rather than inheriting a generic one, to avoid cold-start false positives. ([15:52](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=952s), confidence: stated)
- Statistical divergence measures such as MMD or KL divergence are sufficient for the detection stage. ([16:36](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=996s), confidence: stated)
- Baselines defined at the HTTP-method level (e.g. all POST requests) are too coarse; thresholds should be scoped to specific payment types such as real-time payments or wire payments. ([17:28](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=1048s), confidence: stated)
- Automated remediation should be rolled out to 5-10% of machines and verified before going to 100% of nodes. ([12:55](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=775s), confidence: stated)
- Collapsing detection from multiple time windows to a single window substantially reduced mean time to discovery. ([16:36](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=996s), confidence: stated)
- The monitoring system must be aware of new deployments in order to make correct rollback decisions. ([19:00](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=1140s), confidence: stated)
- Anomaly outputs must be explainable with supporting data rather than reduced to a single opaque score. ([18:13](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=1093s), confidence: stated)
- This graph-based drift detection is only one statistical module within a larger neural/algorithmic system, not a complete solution on its own. ([11:52](https://www.youtube.com/watch?v=u1yaOeEX4e8&t=712s), confidence: stated)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [online evaluation](../concepts/online-evaluation.md)

