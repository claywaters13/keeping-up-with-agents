---
title: "Rustem Feyzkhanov"
type: "speaker"
slug: "rustem-feyzkhanov"
role: "Senior Engineering Manager - AI Platform"
company: "Snorkel AI"
talk_count: 1
---

# Rustem Feyzkhanov

**Senior Engineering Manager - AI Platform &middot; Snorkel AI**

Rustem Feyzkhanov is a Senior Engineering Manager on the AI Platform Engineering team at Snorkel AI, where he leads work on infrastructure and platform systems for building expert-authored datasets, simulation environments, and evaluation pipelines for frontier AI models and production agents. His work focuses on scalable agent evaluation, secure sandboxed execution, benchmark quality, and the systems needed to run large volumes of agent simulations reliably. Before Snorkel, Rustem was an ML Engineering Manager at Instrumental, applying AI to manufacturing, and an engineer at Astro Digital, building AI systems for satellite imagery. He is passionate about AI agents, evaluation infrastructure, serverless computing, and practical machine learning systems. Rustem is the author of the course and book Serverless Deep Learning with TensorFlow and AWS Lambda and Practical Deep Learning on the Cloud, and he is the main contributor to the open-source lambda-packs repository for serverless Python packages.

[LinkedIn](https://www.linkedin.com/in/ryfeus)

## Talks

- [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md) (Evals)

## Scheduled Sessions

- **From Agent Traces to Agent Simulations: The next era of agent evaluation** &middot; Day 3 — Session Day 2 &middot; 12:05pm-12:25pm &middot; Track 5

## Concepts

- [benchmark design](../concepts/benchmark-design.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [reward hacking](../concepts/reward-hacking.md)
- [simulation environments](../concepts/simulation-environments.md)
- [verifier design](../concepts/verifier-design.md)

## Quotes

> "every company needs a benchmark. It's the only way to reliably evaluate, release, and improve your agents."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [0:01](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=1s)

> "It's not a static benchmark. It's a constantly populated data set from your production traces."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [0:52](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=52s)

> "for us, benchmark construction is an engineering discipline. We run millions of agent simulations per month."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [0:52](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=52s)

> "it is useful to find failures in production, but it's hard to test different variants."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [1:39](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=99s)

> "it's hard to make sure that everything is repeatable because you will get different database state, different tool versions, and so on. So, never fully compare apples to apples."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [2:22](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=142s)

> "you can compare agents using different metrics, not just success rate, but cost, latency, and retries."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [2:22](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=142s)

> "public benchmark is useful to orient and build your prior, but your private benchmark is useful to ship."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [3:11](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=191s)

> "in your production, you don't care about the model, you care about the full system."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [4:49](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=289s)

> "You can put it as a release gate for your agent and verify that any change to agent stack in didn't reduce regression suddenly."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [5:30](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=330s)

> "benchmark becomes part part of agent evaluation, becomes part of integration test for agent for release, and it becomes also training set for agent to improve it."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [5:30](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=330s)

> "when we construct Oracle ourselves to make sure that task is solvable in the first place. Because if it's not solvable, agent won't be able to solve it."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [7:02](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=422s)

> "effectively it has to be mini production, but you don't want to run full production for every experiment."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [8:27](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=507s)

> "you don't want your agent to know that it's running within simulation. So, it has to be real."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [8:27](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=507s)

> "You don't run the full production database. You have a certain snapshot. You can run side containers sidecars in this case."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [9:06](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=546s)

> "Agent can try to reward hack simulation environment because it can understand that it's in simulation and it can hack it."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [11:51](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=711s)

> "benchmark is software. It's code. It's files. You need to treat it as such. You need to have a separate CI pipeline for it."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [12:34](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=754s)

> "There is a bit of an anti-pattern in the industry where like folks try to fix things in the prompt."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [14:15](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=855s)

> "with simulation, you control the full stack. You can evaluate the full stack. And you can make sure that fix lives in the correct place. You don't push everything to the prompt."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [14:15](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=855s)

> "you don't need subject matter experts to review everything, but you specifically want to find cases where there's disagreement between agent and different verifiers."
>
> — [From Agent Traces to Agent Simulations](../talks/from-agent-traces-to-agent-simulations.md), [19:13](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=1153s)

