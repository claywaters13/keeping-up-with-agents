---
title: "Improving Agents is a Data Mining Problem"
type: "talk"
slug: "improving-agents-is-a-data-mining-problem"
track: "Memory & Continual Learning"
org: "LangChain"
day: "Day 3 — Session Day 2"
room: "Track 3"
video_id: "CvRngaQZQ3Y"
duration_sec: 1201
word_count: 3799
speakers: ["Vivek Trivedy"]
---

# Improving Agents is a Data Mining Problem

**Speakers:** [Vivek Trivedy](../speakers/vivek-trivedy.md)

**Org:** LangChain

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 20m 01s

[Watch on YouTube](https://www.youtube.com/watch?v=CvRngaQZQ3Y)

## Summary

Vivek Trivedy, who leads applied research at LangChain, argues that continuously improving agents is fundamentally a data mining problem: ship the agent, collect traces, mine those traces with other agents, then run data-driven experiments on prompts, tools, and orchestration. He frames observability and continual learning as tightly coupled — traces are the substrate that holds the feedback an agent needs to update itself — and warns that reading traces at scale is expensive and that long coding-agent traces no longer fit in a reading agent's context, so context must be treated as an external queryable object. The talk's most concrete payoff is a cost story: LangChain uses trace data to distill Opus-level trace judging onto cheaper open models (work done with Harvey on their legal benchmark) at roughly one to two orders of magnitude lower cost, and to fine-tune base models on narrow vertical tasks past frontier performance. He recommends a 'sandwich' workflow — harness engineering first because feedback arrives in minutes, fine-tuning to break the harness ceiling, then more harness engineering. Worth watching if you have trace volume you aren't using, or are deciding between prompt/harness work and fine-tuning.

## Key Points

- The improvement loop he proposes has four steps: ship the agent into a real environment, collect all trace data from tool calls and outputs, data-mine that trace corpus, then run data-driven experiments comparing new prompts, tools, or orchestrations against prior traces.
- Observability and continual learning are the same problem viewed from two ends — agents acting in environments produce traces, and updating an agent from those traces is what continual learning is, so a continual-learning company necessarily needs traces.
- Unlike code, agent systems (prompts, tools, skills, hooks, middlewares, sub-agent swarms) cannot be reasoned about statically, and the effect of a prompt change varies by domain, so behavior must be observed empirically in traces.
- Two scaling obstacles dominate: input-token cost multiplied across millions of traces, and long coding-agent traces that exceed the reading agent's context — requiring systems that treat trace context as an external object to query rather than something to stuff into a prompt.
- LangChain deliberately picks the minimum sufficient intelligence per task: start with Opus to establish feasibility, then use the resulting traces to port the task onto a cheaper open model via harness engineering, which matched Opus trace-judging on Harvey's legal benchmark at one to two orders of magnitude cheaper.
- Trace mining feeds three concrete outputs: distillation/SFT datasets built from good runs of a larger model, generated evals and environments, and human-readable summaries for high-trust domains like legal and medical where someone must review but nobody can read everything.
- Harness engineering has a ceiling but pays off first because feedback comes back in about two minutes; fine-tuning on narrow vertical tasks breaks through that ceiling, and then further harness engineering follows — a 'sandwich' pattern.
- For high-inference workloads, fine-tuning shifts the economics from per-token cost to hardware cost, which he finds cheaper when you can run a cluster with effectively unlimited inference and spin it down when idle.
- Sparse pass/fail signals like terminal-bench scores give agents almost nothing to act on; densifying feedback from traces is what makes self-improvement loops (auto research) work, though agents will sometimes cheat the score and need checking.
- Continual learning must advance on three axes — observational training data, evolving harnesses, and memory — and memory cannot be an append-only log, which points toward scaling sleep-time compute and 'dreaming' over the full agent lifecycle.

## Notable Quotes

> "if you're continual learning company, you need traces, and if you have traces, then you can try to do continual learning over your agents."
>
> — [2:26](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=146s) &middot; *States the talk's central coupling of observability and continual learning in one line.*

> "It's really really hard for humans to reason about how certain prompts that they change are actually going to affect agent behavior at scale."
>
> — [3:40](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=220s) &middot; *The core justification for why agent development must be empirical rather than read-the-code.*

> "over the last four years since the ChatGPT moment, we've started trading determinism for autonomy"
>
> — [4:18](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=258s) &middot; *Compact framing of the tooling gap the whole talk is trying to fill.*

> "And then what we do is we send agents to read traces from other agents"
>
> — [4:18](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=258s) &middot; *Describes LangChain's actual internal practice, not just a recommendation.*

> "the data that we see today is going to be the smallest that humans have ever seen in their entire lives because we're in this massive exponential shift to our agents are doing more and more work in the economy"
>
> — [5:41](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=341s) &middot; *The scale claim that motivates treating trace analysis as a mining problem.*

> "reading traces at scale is super expensive, uh especially if you have millions of traces and if you have millions of tokens per trace"
>
> — [6:29](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=389s) &middot; *Names the cost constraint that rules out naive trace review.*

> "we need to build agents to efficiently mine data from other agents and it's it's no longer as simple as just like feeding the data into context"
>
> — [7:15](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=435s) &middot; *Rejects the obvious approach and states the engineering requirement.*

> "open models have basically hit an inflection point in intelligence that we at LangChain don't reach for the frontier models for every single use case"
>
> — [7:15](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=435s) &middot; *A dated, checkable claim about open-model viability from a team shipping on it.*

> "And like practically speaking, honestly, yes, we start with Opus, we start with 55 because we just want to know if the task is even possible."
>
> — [7:50](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=470s) &middot; *Concrete methodology: frontier models as feasibility probes, not production defaults.*

> "And the answer is roughly yes at like an order or like two orders of magnitude cheaper."
>
> — [8:25](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=505s) &middot; *The headline number on distilling Opus-level trace judging onto open models.*

> "if we take like base models and we tune them on like very specific vertical tasks, which is what a lot of our customers do, they don't really care about the entire variance of tasks"
>
> — [9:03](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=543s) &middot; *Explains why narrow fine-tuning can exceed frontier performance in practice.*

> "another sort of like economic decision is that you can move from token costs to hardware costs"
>
> — [9:35](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=575s) &middot; *Names a tradeoff teams considering fine-tuning routinely miss.*

> "But for like very high inference workloads, we find it to be way cheaper just to like run a cluster and I get like unlimited inference on that cluster"
>
> — [10:09](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=609s) &middot; *Reports the practical outcome of that token-to-hardware shift.*

> "I think you can basically define agent behavior by showing the evals that you ran on it"
>
> — [11:37](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=697s) &middot; *His self-labeled hot take on evals as a behavioral specification.*

> "Like, the purpose of evals is roughly to try to make them pass"
>
> — [11:37](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=697s) &middot; *A deliberately blunt claim about eval-driven development that others would contest.*

> "So, densifying feedback is uh really good way to improve agents, and like traces are the substrate that hold that feedback."
>
> — [15:23](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=923s) &middot; *Ties the reward-signal argument back to why traces specifically matter.*

> "if you need to do something for improving your agent, the best thing that you can do is collect feedback as quickly as possible"
>
> — [15:54](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=954s) &middot; *His prioritization heuristic for choosing between improvement techniques.*

> "we find a lot of teams are happy with harness engineering and uh it solves their customer use case"
>
> — [15:54](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=954s) &middot; *Tempers the fine-tuning enthusiasm with what actually suffices for most teams.*

> "we humans are like really good at like remembering stuff over time, but we are not append-only logs of information"
>
> — [18:06](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=1086s) &middot; *Sharp critique of prevailing agent memory designs.*

> "I would say like if you have an agent, just turn on tracing and point an agent at it and that's like the easiest thing that you can do"
>
> — [18:46](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=1126s) &middot; *The single actionable takeaway he closes on.*

## Positions

- Continual learning and observability are inseparable — you cannot do continual learning on agents without collecting trace data. ([2:26](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=146s), confidence: stated)
- Agent behavior cannot be reasoned about statically the way code can be, because prompts, tools, hooks, and sub-agent orchestration interact unpredictably and differently per domain. ([3:40](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=220s), confidence: stated)
- Feeding trace data directly into a reading agent's context no longer works at scale; context must be treated as an external object that agents query. ([7:15](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=435s), confidence: stated)
- Open models have reached an intelligence inflection point such that frontier models are unnecessary for many production use cases. ([7:15](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=435s), confidence: stated)
- The right workflow is to start with a frontier model only to establish task feasibility, then use its traces to port the task to a cheaper open model. ([7:50](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=470s), confidence: stated)
- Trace-judging capability comparable to Opus can be achieved with a cheaper open model at one to two orders of magnitude lower cost, demonstrated on Harvey's legal benchmark. ([8:25](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=505s), confidence: stated)
- Base models fine-tuned on narrow vertical tasks can match and exceed frontier model performance on those tasks. ([9:03](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=543s), confidence: stated)
- For high-inference workloads, running your own cluster is cheaper than paying per-token API pricing. ([10:09](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=609s), confidence: stated)
- An agent's evals fully specify its behavior, because teams alter the agent until the evals pass. ([11:37](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=697s), confidence: stated)
- Human review of agent traces remains necessary in high-trust domains like legal and medical, but humans lack the bandwidth to read raw traces, so preparing digestible content for them is valuable work. ([12:13](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=733s), confidence: stated)
- The core principles of classical machine learning still apply in the agent era, reframed as fitting a model, harness, and task together rather than fitting parameters to a dataset. ([13:29](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=809s), confidence: stated)
- Agents optimizing against a score will sometimes cheat, so auto-research loops need human or automated checking. ([14:13](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=853s), confidence: stated)
- Binary pass/fail benchmark output is a poor improvement signal; feedback must be densified from traces for agents to know what to change. ([15:23](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=923s), confidence: stated)
- Harness engineering should be attempted before fine-tuning because its feedback loop is roughly two minutes, and most teams never need to go further. ([15:54](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=954s), confidence: stated)
- Append-only memory files with search over them will not scale to agents working with humans over multi-year timescales; memory entries must be updated and compressed. ([18:06](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=1086s), confidence: stated)
- Agent harnesses themselves must evolve over time alongside models and tasks, rather than being treated as fixed scaffolding. ([17:27](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=1047s), confidence: stated)
- Agent-generated data will soon exceed the total volume of human-generated data, on shrinking timescales. ([5:41](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=341s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [continual learning](../concepts/continual-learning.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [model portability](../concepts/model-portability.md)
- [post-training](../concepts/post-training.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [reward design](../concepts/reward-design.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)

