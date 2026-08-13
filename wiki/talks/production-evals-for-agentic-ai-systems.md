---
title: "Production Evals For Agentic AI Systems"
type: "talk"
slug: "production-evals-for-agentic-ai-systems"
org: "Meta Superintelligence Labs"
video_id: "vljxQZfJ9wY"
duration_sec: 492
word_count: 1143
speakers: ["Nishant Gupta"]
---

# Production Evals For Agentic AI Systems

**Speakers:** [Nishant Gupta](../speakers/nishant-gupta.md)

**Org:** Meta Superintelligence Labs

**Duration:** 8m 12s

[Watch on YouTube](https://www.youtube.com/watch?v=vljxQZfJ9wY)

## Summary

Nishant Gupta, a tech lead at Meta working on training and inference infrastructure, argues that evaluation for agentic AI systems must move from model benchmarking to production infrastructure. His core claim is that benchmarks measure model capability while production measures system behavior, and the gap between the two widens as systems become more autonomous. He proposes an evaluation pyramid — benchmarks at the base, scenario-based evals in the middle, production telemetry at the top — and urges teams to adopt an SRE mindset where reliability, not accuracy, is the North Star. The talk is a short, slide-driven conceptual overview with no code, benchmarks, or company-specific case studies, so it's best for teams framing an eval strategy rather than engineers looking for implementation detail.

## Key Points

- Agentic systems shift the evaluation question from 'did the model generate the right answer?' to 'did the system behave correctly?', which means evaluating workflows rather than individual outputs.
- Benchmarks measure model capability while production measures system behavior, and benchmarks cannot capture tool failures, API outages, context changes, user variability, or long-running workflows.
- Agentic failure modes form a hierarchy: memory, retrieval, and safety failures at the foundation; reasoning and planning mistakes and incorrect tool execution above that; and multi-agent coordination failures at the top — hallucination is only one category.
- Teams should think like SREs rather than researchers, measuring reliability, availability, latency, cost, and recovery instead of maximizing benchmark scores.
- Offline evaluation should be scenario-driven rather than prompt-driven, running agents inside simulated workflows (customer support, code generation, research) and measuring task completion rate, tool correctness, planning quality, and resource usage.
- Production traffic becomes evaluation data — execution traces, user outcomes, escalations, failures, and feedback signals form the largest and most representative eval set an organization will have.
- Humans should be treated as evaluators rather than fallback systems, providing correctness, trust, usefulness, and safety signals that calibrate automated pipelines and surface blind spots.
- Agentic systems drift continuously as models, prompts, tools, and user behavior change, and because no single change looks catastrophic, degradation is often only discovered when users complain.
- Agent traces are the equivalent of distributed tracing for autonomous workloads; traditional logs are insufficient for evaluating reasoning paths, tool calls, memory access, and state transitions.
- The emerging architecture separates a control plane that observes, simulates, and coordinates human review from an execution plane that performs the work.

## Notable Quotes

> "Because benchmarks measure model capability. Production measures system behavior."
>
> — [0:47](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=47s) &middot; *The talk's central distinction, stated in its most compressed form.*

> "A benchmark doesn't capture tool failure, API outage, context changes, user variability, long running workflows."
>
> — [0:47](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=47s) &middot; *Enumerates exactly what falls outside benchmark coverage.*

> "And as systems become more autonomous, the gap between the benchmark performance and production performance grows."
>
> — [0:47](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=47s) &middot; *A directional claim others might contest, and the basis for the whole argument.*

> "In other words, we are moving from evaluating answers to evaluating workflows. And that requires fundamentally different evaluation architectures."
>
> — [1:43](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=103s) &middot; *States the reframing and its architectural consequence.*

> "Many teams still think hallucinations are the primary AI failure modes. In production, they are often just one category."
>
> — [1:43](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=103s) &middot; *Directly pushes back on a widespread industry framing.*

> "One of the most useful mindset shifts is to stop thinking like researchers and start thinking like a SRE or a production engineer."
>
> — [2:30](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=150s) &middot; *Names the discipline transfer the talk advocates.*

> "SREs don't measure success using accuracy. They measure reliability, availability, latency, cost, recovery."
>
> — [2:30](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=150s) &middot; *Specifies the replacement metric set concretely.*

> "The goal is not maximizing the benchmark scores. The goal is to maximize dependable outcomes. Reliability becomes the North Star metric."
>
> — [2:30](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=150s) &middot; *The talk's clearest statement of what to optimize.*

> "The surprising insight is that the most evaluation data often comes from real users interacting with real systems."
>
> — [3:17](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=197s) &middot; *Justifies putting production telemetry at the top of the eval pyramid.*

> "The key takeaway, agent evaluation should be scenario driven, not prompt driven."
>
> — [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s) &middot; *A prescriptive, actionable position on offline eval design.*

> "Production is the largest and the most representative evaluation data any organization will ever have."
>
> — [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s) &middot; *Strong superlative claim about where eval signal actually lives.*

> "Many organizations view humans as fallback systems. I think that's a wrong framing. Humans are the evaluators."
>
> — [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s) &middot; *Explicit disagreement with a common operating assumption.*

> "The challenge is that no longer single change appear catastrophic. Reliability slowly degrades."
>
> — [4:48](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=288s) &middot; *Names the mechanism that makes agentic drift hard to detect.*

> "Without continuous evaluation, teams often don't discover drift until users complain."
>
> — [4:48](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=288s) &middot; *States the failure consequence of skipping continuous eval.*

> "Agent traces become the equivalent of distributed tracing for autonomous workloads. Without observability, evaluation becomes the guesswork."
>
> — [5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s) &middot; *The observability analogy most likely to transfer to other teams.*

> "Historically, evaluation always happened before deployment, but now evaluation continues after deployment"
>
> — [5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s) &middot; *Marks the lifecycle change from testing phase to running service.*

> "And notice but notice that accuracy is missing. It's not because accuracy doesn't matter, but because business success depends on much more than just accuracy."
>
> — [6:40](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=400s) &middot; *The deliberate omission of accuracy from the business metric set is the talk's sharpest move.*

> "Evaluation becomes part of the control plane, not a separate tool, not an offline process."
>
> — [6:40](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=400s) &middot; *States the architectural end-state the speaker predicts for the industry.*

> "First, benchmarks remains necessary, but they are insufficient."
>
> — [7:30](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=450s) &middot; *The nuanced version of the thesis — not anti-benchmark, just anti-benchmark-only.*

## Positions

- Benchmarks are necessary but insufficient for agentic systems; high benchmark scores routinely coexist with unreliable production behavior. ([0:47](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=47s), confidence: stated)
- The gap between benchmark performance and production performance grows as systems become more autonomous. ([0:47](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=47s), confidence: stated)
- Hallucination is only one of many agentic failure categories and is not the primary production risk. ([1:43](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=103s), confidence: stated)
- Reliability, not accuracy, should be the North Star metric for agentic systems. ([2:30](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=150s), confidence: stated)
- Production telemetry yields higher-value evaluation signal than either scenario-based evals or benchmarks. ([3:17](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=197s), confidence: stated)
- Offline agent evaluation should be organized around simulated scenarios rather than individual prompts. ([3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s), confidence: stated)
- Humans in an agentic system should be positioned as evaluators, not as fallback handlers. ([3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s), confidence: stated)
- Traditional logs are insufficient for agent evaluation; detailed traces of reasoning paths, tool calls, memory access, and state transitions are required. ([5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s), confidence: stated)
- Evaluation should run continuously as an always-on service rather than as a pre-deployment testing phase. ([5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s), confidence: stated)
- The industry is converging on an architecture where evaluation lives in a control plane that is separated from the execution plane. ([6:40](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=400s), confidence: stated)
- Accuracy does not belong in the set of metrics that map to business outcomes for agentic systems. ([6:40](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=400s), confidence: implied)
- Every organization building agentic AI will eventually have to treat evaluation as infrastructure rather than QA. ([7:30](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=450s), confidence: stated)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [online evaluation](../concepts/online-evaluation.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

