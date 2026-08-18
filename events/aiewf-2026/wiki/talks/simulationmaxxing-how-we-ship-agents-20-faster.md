---
title: "SimulationMaxxing: How we ship agents 20× faster"
type: "talk"
slug: "simulationmaxxing-how-we-ship-agents-20-faster"
track: "AI in Finance"
org: "Nubank (Aman Gupta) and Snowglobe (Shreya Rajpal)"
day: "Day 4 — Session Day 3"
room: "Track 3"
video_id: "KMR_RBoCa4M"
duration_sec: 989
word_count: 3094
speakers: ["Aman Gupta", "Shreya Rajpal"]
---

# SimulationMaxxing: How we ship agents 20× faster

*Program title: Simulation-Maxxing: How Nubank ships agents 20× faster with simulations*

**Speakers:** [Aman Gupta](../speakers/aman-gupta.md), [Shreya Rajpal](../speakers/shreya-rajpal.md)

**Org:** Nubank (Aman Gupta) and Snowglobe (Shreya Rajpal)

**Track:** AI in Finance &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 16m 29s

[Watch on YouTube](https://www.youtube.com/watch?v=KMR_RBoCa4M)

## Summary

Aman Gupta (Nubank) and Shreya Rajpal (Snowglobe) argue that the real bottleneck in agent evaluation is not metrics but eval data, and that generating that data through simulation instead of waiting on production traces lets teams ship agents roughly 20× faster. They open with production results: TNPS (a customer-satisfaction measure) across five of Nubank's customer-support agents rose over several quarters to approach and in some cases exceed human quality. Shreya explains mechanically what an agent simulation is — wrap the agent via SDK with no code changes, mock tools, define personas and use cases, then generate thousands of multi-turn conversations with consistent synthetic grounding data (fake addresses, accounts) that judges score per turn. Aman reports validation numbers: high correlation between sim-derived and real eval quality, 80% of domain-expert labels confirming sims yield usable data, one agent's TNPS doubling, self-service rate improving 4% in one case, and simulation catching a regression before it hit production. The closing argument is that enterprise self-improving agents reduce to two things — aligned metrics and a reliable data generator — plus the discipline of measuring the sim-to-real gap.

## Key Points

- Evals reduce to metrics and data; metrics now have a reasonable playbook (LLM-as-judge aligned to human labels, auto prompt optimization), while eval data remains the expensive, unsolved bottleneck.
- Agent eval data is far costlier than classic ML or single-turn QA data because each data point is a multi-turn trajectory with internal tool calls whose state must stay consistent.
- The two standard sources of eval data both fail: manual authoring is prohibitively time-consuming, and production traces are nearly free but mean experimenting on live users, which makes parallel experiments impractical.
- Simulation compresses the release cycle from weeks to under a day — sometimes hours or minutes — because offline evals no longer wait on hand-curated data and pre-launch confidence no longer waits on a sparse, noisy A/B feedback signal.
- A simulation run wraps the existing agent without code changes, mocks the required tools, and is steered by personas and use cases to produce thousands of multi-turn conversations with consistent synthetic grounding data.
- Nubank validated the sim-to-real gap explicitly: eval quality from simulated and real data correlated highly, and 80% of domain-expert labels confirmed sims produced usable data for both greenfield and mature agents.
- Concrete wins include one agent's TNPS doubling, a 4% self-service-rate improvement, and a caught regression plus a self-service-rate issue that would otherwise have reached production.
- Teams now run many candidate changes — including swapping in newly released open-source models — through simulation first and only launch a single A/B test once the sim output looks good, saving multiple weeks per evaluation cycle.
- The speakers argue that TNPS and self-service rate are commonly assumed to trade off in customer service, but Nubank improved both simultaneously using simulation-driven iteration.

## Notable Quotes

> "If you generate your eval data in sim instead of waiting on production data you can ship agents 20x faster and we'll give you evidence for that."
>
> — [0:49](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=49s) &middot; *The talk's thesis stated in a single sentence, with an explicit promise of evidence.*

> "many of them are approaching human quality and this data is a bit stale many of them are exceeding human quality"
>
> — [1:35](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=95s) &middot; *The headline production result that motivates the entire method.*

> "The thing that's a bottleneck and that still remains very challenging and unsolved is what is the data that you're actually computing these metrics on and that process is very timeconuming and very expensive specifically so for agents."
>
> — [3:04](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=184s) &middot; *Names the specific bottleneck the talk claims to solve, and takes a side against metrics-focused eval work.*

> "if you're around like machine learning era circa you know 2018 it would be like ML work is 85% data work"
>
> — [3:57](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=237s) &middot; *Anchors the data-cost claim to a familiar prior-era number.*

> "now for multi-turn agents each data point is a trajectory with a lot of internal tool calls that all need state"
>
> — [3:57](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=237s) &middot; *Explains precisely why agent eval data is more expensive than prior generations of ML data.*

> "production traces in comparison are almost free. You don't have to pay for them. You're going to get them anyway. But the cost is that you're testing on real live users every time you're testing it."
>
> — [4:37](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=277s) &middot; *The clearest statement of the tradeoff that makes production-trace evals unattractive.*

> "if you run an AB test in production and monitor regressions, see if you get a statistically significant improvement of of a previous version that can take forever because customer feedback is through some kind of a feedback form and it can be sparse, it can be noisy"
>
> — [6:02](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=362s) &middot; *Quantifies the pain of the production feedback loop in operational terms.*

> "we have verified in production that yes simulations circuit this timeline short circuit this timeline from a few weeks you can go to less than a day sometimes even a few hours a few minutes"
>
> — [6:02](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=362s) &middot; *The concrete speedup claim, framed as production-verified rather than theoretical.*

> "you get like thousands of multi-turn conversations against your real agents. These conversations have you know tools mocked etc."
>
> — [8:14](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=494s) &middot; *Defines the actual output of a simulation run.*

> "quality of uh with evals from sim and real data the correlation is pretty high and we had human review done where 80% of our domain expert labels confirmed that sims give us usable data not just for uh mature agents but also for green field agents"
>
> — [11:16](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=676s) &middot; *The load-bearing validation number for the whole sim-to-real argument.*

> "we caught a regression uh with simulation that could have made it to production, but simulation caught it."
>
> — [11:58](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=718s) &middot; *Names a concrete derisking outcome beyond speed.*

> "one of our agents, the TNPS, has 2xed uh thanks to simulation, robust evals, and investing in something super principled rather than, you know, throwing something at the wall and see what sticks"
>
> — [11:58](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=718s) &middot; *The strongest single quality number, tied to a methodological stance.*

> "They don't launch until they're happy with the same output."
>
> — [12:35](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=755s) &middot; *Describes the actual workflow change simulation caused inside the team.*

> "Now you can just run a bunch of stuff through SIM and launch just one AB test which kind of shortcircuits launching the first five or six."
>
> — [12:35](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=755s) &middot; *Makes the experimentation-throughput gain concrete in A/B test counts.*

> "this is often discussed in customer service circles that TNPS can come at the cost of self-service rate. Sometimes there's a trade-off but I'm happy to report that we are not compromising all self- service rate with SIM."
>
> — [12:35](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=755s) &middot; *Directly contests a received tradeoff in the domain.*

> "with SIM, we have the perfect recipe to just throw a bunch of ideas, open source models at our agent harness and eval setup and see which model versions uh you know really really work for us. Uh this has saved us multiple weeks of effort"
>
> — [13:47](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=827s) &middot; *Shows a second-order use case — model selection — with a time-saved estimate.*

> "in order for any of these gains to really be unlocked uh you know you really need to close out the sim toreal gap"
>
> — [15:01](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=901s) &middot; *The talk's main caveat, and the thing most teams adopting simulation would skip.*

> "in an enterprise setting when you're building an agent, it really does come down to two things, data and metrics."
>
> — [15:01](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=901s) &middot; *Reduces the self-improving-agents hype to a checkable two-part claim.*

## Positions

- Generating eval data in simulation rather than waiting on production data lets teams ship agents 20× faster. ([0:49](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=49s), confidence: stated)
- Metrics for agent evaluation are largely a solved playbook (LLM-as-judge aligned to human judgment plus auto-optimization); eval data is the remaining unsolved bottleneck. ([3:04](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=184s), confidence: stated)
- Multi-turn agent data points are substantially more expensive to generate and annotate than structured ML data or single-turn QA data because of trajectory and tool-call state consistency requirements. ([3:57](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=237s), confidence: stated)
- Relying on production traces means running experiments on real live users, which makes large-scale parallel experimentation impractical. ([5:24](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=324s), confidence: stated)
- Simulation shortens the agent iteration cycle from a few weeks to less than a day, sometimes hours or minutes. ([6:02](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=362s), confidence: stated)
- Eval results computed on simulated data correlate highly with those computed on real production data. ([11:16](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=676s), confidence: stated)
- 80% of Nubank domain-expert labels confirmed that simulations produce usable data, for greenfield as well as mature agents. ([11:16](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=676s), confidence: stated)
- Simulation caught a regression and a self-service-rate degradation that would otherwise have shipped to production. ([11:58](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=718s), confidence: stated)
- One Nubank agent's TNPS doubled as a result of simulation plus robust evals. ([11:58](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=718s), confidence: stated)
- The commonly assumed tradeoff between TNPS and self-service rate is not forced; Nubank improved self-service rate by 4% in one case without sacrificing TNPS. ([13:12](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=792s), confidence: stated)
- Simulation-based evaluation of candidate open-source models saved Nubank multiple weeks of effort versus running production A/B tests for each. ([13:47](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=827s), confidence: stated)
- Adopting simulation without explicitly measuring and closing the sim-to-real gap will not deliver the claimed gains, because the results cannot be trusted. ([15:01](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=901s), confidence: stated)
- Simulation is a viable substitute for most pre-launch A/B tests, reducing roughly ten planned A/B tests per quarter to about one. ([12:35](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=755s), confidence: implied)
- AI customer-support agents can reach and exceed human-level customer satisfaction in production. ([1:35](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=95s), confidence: stated)

## Concepts

- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [simulation environments](../concepts/simulation-environments.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

