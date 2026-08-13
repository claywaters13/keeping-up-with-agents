---
title: "Nishant Gupta"
type: "speaker"
slug: "nishant-gupta"
role: "Software Engineer, Tech Lead"
company: "Meta"
talk_count: 2
---

# Nishant Gupta

**Software Engineer, Tech Lead &middot; Meta**

I am a Staff Software Engineer and Researcher at Meta, specializing in large-scale distributed systems, AI infrastructure, and operational resilience. Within Meta Superintelligence Labs, I build agentic infrastructure that enables AI systems to operate reliably in production through evaluation, auditing, safety controls, feedback loops, and human oversight.

I previously led the development of Meta’s next-generation elastic compute infrastructure, managing roughly 30% of fleet capacity across tens of millions of servers in 20+ geo-distributed datacenters, delivering billions of dollars in infrastructure savings while shaping multi-year strategy with executive leadership.

My research focuses on resource optimization, reliability, and safe AI deployment at scale. I designed and deployed Dynamic Idle Resource Leasing, a production system that safely oversubscribes datacenter capacity while preserving strict reliability guarantees. I have authored research papers with 90+ citations.

I am passionate about building scalable, fault-tolerant systems and translating cutting-edge research into real-world infrastructure that delivers measurable impact.

[LinkedIn](https://www.linkedin.com/in/nishantgupta-ai/)

## Talks

- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)

## Scheduled Sessions

- **Operating Distributed Inference Systems at Scale** &middot; Day 4 — Session Day 3 &middot; 10:45am-11:05am &middot; Track 9

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [online evaluation](../concepts/online-evaluation.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [roi measurement](../concepts/roi-measurement.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

## Quotes

> "The challenge is no longer in intelligence. The challenge is is reliability."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [0:03](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=3s)

> "These systems are fundamentally probabilistic. Infrastructure is not allowed to be."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [0:44](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=44s)

> "This is what I call the great mismatch. We're trying to run autonomous systems on infrastructure that was designed for deterministic workflows."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [0:44](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=44s)

> "Most AI demos showcase capability."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [0:44](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=44s)

> "Production systems be have a different objective. Can it do it reliably? Can it do it 10,000 times, 100,000 times, million times?"
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [1:34](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=94s)

> "The majority of the engineering effort moves below the model layer into orchestration, monitoring, safety evaluation, and recovery systems."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [1:34](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=94s)

> "When people hear AI failures, they immediately think hallucinations. In reality In reality, hallucinations are often the least interesting failure mode."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [1:34](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=94s)

> "The model makes a mistake, but however, the infrastructure turns that mistake into an outage. That's the real challenge."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [2:23](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=143s)

> "What started as a minor API error became a compute incident. This is why unco- uncontrolled retries are one of the biggest risk in agentic systems."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [2:23](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=143s)

> "Never let the model directly control production systems. The model should generate proposals, infrastructure validates them, policy engine approves them, execution gateway enforces them."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:09](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=189s)

> "The model just suggests, the platform decides."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:09](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=189s)

> "containers gave rise to Kubernetes, microservices created service meshes. AI agents are creating something new, an agentic control plane."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:09](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=189s)

> "The organizations that build this layer will have significantly more competitive advantages."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:09](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=189s)

> "traditional logs tell us what happened."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:09](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=189s)

> "When debugging an autonomous workflow, understanding the chain of decisions and reasoning is often more important than the final output."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:58](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=238s)

> "Many multi-agent failures are actually consistency failures masquerading as reasoning failures."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:58](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=238s)

> "Many people frame human involvement as temporarily temporary necessity. I don't think that's correct. The most successful systems are likely to remain human supervised."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [4:50](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=290s)

> "The goal is not to remove humans. The goal is allocating human attention where it provides the maximum value."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [4:50](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=290s)

> "Inference is no longer just a model problem. It becomes a resource orchestration problem."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [5:39](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=339s)

> "Instead of inventing entirely new infrastructure, we can adapt to reliability patterns for autonomous systems."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [5:39](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=339s)

> "The initially prompts were the differentiator. Then the models became the differentiator. And both are rapid rapidly commoditizing. The next frontier is infrastructure."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [6:29](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=389s)

> "Models are stochastic. Infrastructures must be deterministic."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [6:29](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=389s)

> "the future of the AI AI won't be won by better prompts. It will be won by better systems."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [6:29](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=389s)

> "Because benchmarks measure model capability. Production measures system behavior."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [0:47](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=47s)

> "A benchmark doesn't capture tool failure, API outage, context changes, user variability, long running workflows."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [0:47](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=47s)

> "And as systems become more autonomous, the gap between the benchmark performance and production performance grows."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [0:47](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=47s)

> "In other words, we are moving from evaluating answers to evaluating workflows. And that requires fundamentally different evaluation architectures."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [1:43](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=103s)

> "Many teams still think hallucinations are the primary AI failure modes. In production, they are often just one category."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [1:43](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=103s)

> "One of the most useful mindset shifts is to stop thinking like researchers and start thinking like a SRE or a production engineer."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [2:30](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=150s)

> "SREs don't measure success using accuracy. They measure reliability, availability, latency, cost, recovery."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [2:30](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=150s)

> "The goal is not maximizing the benchmark scores. The goal is to maximize dependable outcomes. Reliability becomes the North Star metric."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [2:30](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=150s)

> "The surprising insight is that the most evaluation data often comes from real users interacting with real systems."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:17](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=197s)

> "The key takeaway, agent evaluation should be scenario driven, not prompt driven."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

> "Production is the largest and the most representative evaluation data any organization will ever have."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

> "Many organizations view humans as fallback systems. I think that's a wrong framing. Humans are the evaluators."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [3:58](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=238s)

> "The challenge is that no longer single change appear catastrophic. Reliability slowly degrades."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [4:48](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=288s)

> "Without continuous evaluation, teams often don't discover drift until users complain."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [4:48](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=288s)

> "Agent traces become the equivalent of distributed tracing for autonomous workloads. Without observability, evaluation becomes the guesswork."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s)

> "Historically, evaluation always happened before deployment, but now evaluation continues after deployment"
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [5:49](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=349s)

> "And notice but notice that accuracy is missing. It's not because accuracy doesn't matter, but because business success depends on much more than just accuracy."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [6:40](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=400s)

> "Evaluation becomes part of the control plane, not a separate tool, not an offline process."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [6:40](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=400s)

> "First, benchmarks remains necessary, but they are insufficient."
>
> — [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md), [7:30](https://www.youtube.com/watch?v=vljxQZfJ9wY&t=450s)

