---
title: "From Agent Traces to Agent Simulations"
type: "talk"
slug: "from-agent-traces-to-agent-simulations"
track: "Evals"
org: "Snorkel AI"
day: "Day 3 — Session Day 2"
room: "Track 5"
video_id: "Ib5t2RLtxvM"
duration_sec: 1223
word_count: 3186
speakers: ["Rustem Feyzkhanov"]
---

# From Agent Traces to Agent Simulations

*Program title: From Agent Traces to Agent Simulations: The next era of agent evaluation*

**Speakers:** [Rustem Feyzkhanov](../speakers/rustem-feyzkhanov.md)

**Org:** Snorkel AI

**Track:** Evals &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 20m 23s

[Watch on YouTube](https://www.youtube.com/watch?v=Ib5t2RLtxvM)

## Summary

Rustem Feyzkhanov, who leads the AI platform team at Snorkel AI, argues that every company shipping agents needs its own private benchmark built from production traces, and that the way to get one is offline agent simulation rather than trace inspection alone. Traces surface failures that already happened but can't be replayed cleanly — database state and tool versions drift, so A/B comparisons are never apples to apples. Simulation converts traces into repeatable tasks with a containerized mini-production environment (mocked APIs, sidecar databases, LLM-simulated users), an Oracle solution proving the task is solvable, and verifiers that check final world state, trace, and artifacts rather than just output. He walks through the Harbor task format, failure modes of benchmark construction (reward hacking, too-broad verifiers, high variance), and treating the benchmark as software with its own CI. The payoff is a three-way asset: eval, release gate, and training set — including fine-tuning a small planning model to match a large one.

## Key Points

- Public benchmarks like SWE-bench, Terminal-Bench, and computer-use benchmarks are useful for orienting and building priors, but only a private domain-specific benchmark reflects your tools, policies, and use cases well enough to ship on.
- Production traces find real failures but cannot support repeatable comparisons, because each rerun sees different database state and tool versions; offline simulation turns traces into experiments you can rerun in parallel.
- Production evaluation needs more than pass rate — cost per task, latency, and number of retries matter once an agent is live, and simulation lets you hold environment and verifiers fixed while varying them.
- Simulation tests the full agent stack (model, thinking level, prompt, harness, skills, tools), not just which model scores higher, because in production the system is what you actually ship.
- A benchmark task is a small set of files — instruction.md, a Dockerfile/Compose environment, hidden Oracle solution and verifiers, plus metadata — following the Harbor format from the Terminal-Bench team.
- The Oracle solution exists to prove a task is solvable at all before you ask an agent to solve it, and is a required part of task construction.
- Environments should be built like integration tests: database snapshots instead of full production, sidecar containers for APIs and MCP tools, mocked services, LLM-simulated users, and multi-step checkpoints with per-step verifiers for long-horizon tasks that let you terminate early on failure.
- Verifiers must analyze final environment state, trace, and artifacts using a mix of deterministic checks and LLM/agent-as-judge, with subject matter experts reserved for cases where verifiers and agent behavior disagree.
- Benchmark tasks fail in predictable ways — reward hacking, overly broad verifiers, incorrect verifiers, unstable agent success — so benchmarks are code and need their own CI pipeline (pinned dependencies, fixture checks, Oracle passes, difficulty tagging).
- Stuffing fixes into the prompt is an industry anti-pattern; controlling the full stack in simulation lets you place a fix where it belongs — harness for context overload, a skill for a missing procedure, structured output for schema issues.

## Notable Quotes

> "every company needs a benchmark. It's the only way to reliably evaluate, release, and improve your agents."
>
> — [0:01](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=1s) &middot; *the talk's thesis, stated as a hard requirement*

> "It's not a static benchmark. It's a constantly populated data set from your production traces."
>
> — [0:52](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=52s) &middot; *distinguishes his position from conventional benchmark practice*

> "for us, benchmark construction is an engineering discipline. We run millions of agent simulations per month."
>
> — [0:52](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=52s) &middot; *the one concrete scale number in the talk, and it grounds his credibility claim*

> "it is useful to find failures in production, but it's hard to test different variants."
>
> — [1:39](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=99s) &middot; *crisp statement of what traces can and cannot do*

> "it's hard to make sure that everything is repeatable because you will get different database state, different tool versions, and so on. So, never fully compare apples to apples."
>
> — [2:22](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=142s) &middot; *the core technical argument against A/B testing in production*

> "you can compare agents using different metrics, not just success rate, but cost, latency, and retries."
>
> — [2:22](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=142s) &middot; *names the metric set he thinks production teams actually need*

> "public benchmark is useful to orient and build your prior, but your private benchmark is useful to ship."
>
> — [3:11](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=191s) &middot; *the sharpest one-line framing of public vs. private benchmarks*

> "in your production, you don't care about the model, you care about the full system."
>
> — [4:49](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=289s) &middot; *takes a contrarian side against model-centric evaluation*

> "You can put it as a release gate for your agent and verify that any change to agent stack in didn't reduce regression suddenly."
>
> — [5:30](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=330s) &middot; *names the second of the three benchmark use cases*

> "benchmark becomes part part of agent evaluation, becomes part of integration test for agent for release, and it becomes also training set for agent to improve it."
>
> — [5:30](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=330s) &middot; *the trifecta framing that organizes the whole argument*

> "when we construct Oracle ourselves to make sure that task is solvable in the first place. Because if it's not solvable, agent won't be able to solve it."
>
> — [7:02](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=422s) &middot; *explains why Oracle solutions are non-optional in task construction*

> "effectively it has to be mini production, but you don't want to run full production for every experiment."
>
> — [8:27](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=507s) &middot; *states the central environment-design tradeoff*

> "you don't want your agent to know that it's running within simulation. So, it has to be real."
>
> — [8:27](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=507s) &middot; *the fidelity constraint that drives every environment decision he describes*

> "You don't run the full production database. You have a certain snapshot. You can run side containers sidecars in this case."
>
> — [9:06](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=546s) &middot; *concrete implementation pattern for environment construction*

> "Agent can try to reward hack simulation environment because it can understand that it's in simulation and it can hack it."
>
> — [11:51](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=711s) &middot; *names the first and most consequential benchmark failure mode*

> "benchmark is software. It's code. It's files. You need to treat it as such. You need to have a separate CI pipeline for it."
>
> — [12:34](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=754s) &middot; *the operational prescription that follows from treating benchmarks as engineering*

> "There is a bit of an anti-pattern in the industry where like folks try to fix things in the prompt."
>
> — [14:15](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=855s) &middot; *explicitly names a widespread practice he opposes*

> "with simulation, you control the full stack. You can evaluate the full stack. And you can make sure that fix lives in the correct place. You don't push everything to the prompt."
>
> — [14:15](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=855s) &middot; *the constructive alternative to prompt-patching*

> "you don't need subject matter experts to review everything, but you specifically want to find cases where there's disagreement between agent and different verifiers."
>
> — [19:13](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=1153s) &middot; *practical answer on where scarce human review effort should go*

## Positions

- Every company shipping agents needs its own private benchmark; it is the only reliable way to evaluate, release, and improve agents. ([0:01](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=1s), confidence: stated)
- A/B testing agent configurations in production can never be a true apples-to-apples comparison because database state and tool versions differ between runs. ([2:22](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=142s), confidence: stated)
- Public benchmarks are only useful for orientation and priors; you cannot ship on them because they are domain-specific to someone else's tools and policies. ([3:11](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=191s), confidence: stated)
- Pass rate is insufficient as a production metric; cost, latency, and retries must be measured alongside it. ([4:01](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=241s), confidence: stated)
- What matters in production is the full agent system, not the choice of model. ([4:49](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=289s), confidence: stated)
- A benchmark task is not valid unless an Oracle solution demonstrates the task is solvable. ([7:02](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=422s), confidence: stated)
- Simulation environments must be indistinguishable from production to the agent, or the agent will detect and exploit the simulation. ([8:27](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=507s), confidence: stated)
- Real users cannot be included in simulation tasks and must be replaced by an LLM with its own prompt and context mimicking human behavior. ([8:27](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=507s), confidence: stated)
- Long-horizon tasks should be decomposed into multiple steps with separate prompts and verifiers per step, allowing early termination when the agent fails. ([9:52](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=592s), confidence: stated)
- Verifying only the agent's output is insufficient for agent evaluation; final environment state, trace, and artifacts must also be verified. ([10:35](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=635s), confidence: stated)
- Benchmarks are software and require their own CI pipeline checking pinned dependencies, base images, missing fixtures, and Oracle passes. ([12:34](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=754s), confidence: stated)
- Fixing agent failures by adding prohibitions to the prompt is an industry anti-pattern; fixes belong in the harness, skills, or structured output depending on the root cause. ([14:15](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=855s), confidence: stated)
- Simulation environments can be used to fine-tune a small planning model to match the performance of a large planning model on specific tasks. ([5:30](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=330s), confidence: stated)
- An 80/20 train/validation split is a reasonable default for benchmark tasks, and a held-out set the agent has not seen during experimentation is required. ([17:15](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=1035s), confidence: stated)
- Benchmark coverage should include both happy-path 'bread and butter' use cases and edge cases like tool failures and database problems, mirroring integration test design. ([17:57](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=1077s), confidence: stated)
- Observability and experimentation tooling must be connected as a single system rather than operated separately. ([15:38](https://www.youtube.com/watch?v=Ib5t2RLtxvM&t=938s), confidence: stated)

## Concepts

- [benchmark design](../concepts/benchmark-design.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [reward hacking](../concepts/reward-hacking.md)
- [simulation environments](../concepts/simulation-environments.md)
- [verifier design](../concepts/verifier-design.md)

