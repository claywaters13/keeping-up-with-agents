---
title: "Shreya Rajpal"
type: "speaker"
slug: "shreya-rajpal"
role: "CEO"
company: "Snowglobe"
talk_count: 1
---

# Shreya Rajpal

**CEO &middot; Snowglobe**

Shreya Rajpal is CEO of Snowglobe and co-founder/CEO of Guardrails AI. She created the open-source Guardrails framework and works on tools for validating LLM outputs, preventing hallucinations, detecting policy risks, and generating simulation-based evaluation datasets.

[LinkedIn](https://www.linkedin.com/in/shreya-rajpal/)

## Talks

- [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md) (AI in Finance, co-presented)

## Scheduled Sessions

- **Simulation-Maxxing: How Nubank ships agents 20× faster with simulations** &middot; Day 4 — Session Day 3 &middot; 2:50pm-3:10pm &middot; Track 3

## Concepts

- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [simulation environments](../concepts/simulation-environments.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "If you generate your eval data in sim instead of waiting on production data you can ship agents 20x faster and we'll give you evidence for that."
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [0:49](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=49s)

> "many of them are approaching human quality and this data is a bit stale many of them are exceeding human quality"
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [1:35](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=95s)

> "The thing that's a bottleneck and that still remains very challenging and unsolved is what is the data that you're actually computing these metrics on and that process is very timeconuming and very expensive specifically so for agents."
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [3:04](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=184s)

> "if you're around like machine learning era circa you know 2018 it would be like ML work is 85% data work"
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [3:57](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=237s)

> "now for multi-turn agents each data point is a trajectory with a lot of internal tool calls that all need state"
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [3:57](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=237s)

> "production traces in comparison are almost free. You don't have to pay for them. You're going to get them anyway. But the cost is that you're testing on real live users every time you're testing it."
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [4:37](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=277s)

> "if you run an AB test in production and monitor regressions, see if you get a statistically significant improvement of of a previous version that can take forever because customer feedback is through some kind of a feedback form and it can be sparse, it can be noisy"
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [6:02](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=362s)

> "we have verified in production that yes simulations circuit this timeline short circuit this timeline from a few weeks you can go to less than a day sometimes even a few hours a few minutes"
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [6:02](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=362s)

> "you get like thousands of multi-turn conversations against your real agents. These conversations have you know tools mocked etc."
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [8:14](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=494s)

> "quality of uh with evals from sim and real data the correlation is pretty high and we had human review done where 80% of our domain expert labels confirmed that sims give us usable data not just for uh mature agents but also for green field agents"
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [11:16](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=676s)

> "we caught a regression uh with simulation that could have made it to production, but simulation caught it."
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [11:58](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=718s)

> "one of our agents, the TNPS, has 2xed uh thanks to simulation, robust evals, and investing in something super principled rather than, you know, throwing something at the wall and see what sticks"
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [11:58](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=718s)

> "They don't launch until they're happy with the same output."
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [12:35](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=755s)

> "Now you can just run a bunch of stuff through SIM and launch just one AB test which kind of shortcircuits launching the first five or six."
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [12:35](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=755s)

> "this is often discussed in customer service circles that TNPS can come at the cost of self-service rate. Sometimes there's a trade-off but I'm happy to report that we are not compromising all self- service rate with SIM."
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [12:35](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=755s)

> "with SIM, we have the perfect recipe to just throw a bunch of ideas, open source models at our agent harness and eval setup and see which model versions uh you know really really work for us. Uh this has saved us multiple weeks of effort"
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [13:47](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=827s)

> "in order for any of these gains to really be unlocked uh you know you really need to close out the sim toreal gap"
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [15:01](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=901s)

> "in an enterprise setting when you're building an agent, it really does come down to two things, data and metrics."
>
> — [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [15:01](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=901s)

