---
title: "prompt optimization"
type: "concept"
slug: "prompt-optimization"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 15
---

# prompt optimization

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **15** speaker(s)

**Definition:** Automated search over prompts against a metric, replacing hand-tuning with an optimizer.

*Also referred to as: automated prompt optimization, automatic prompt optimization, prompt optimization search, system prompt optimization, prompt tuning, declarative signatures, regression-aware optimization*

## State of Practice

Automated prompt/agent optimization crossed from research demo to shipped practice at this conference, with concrete numbers attached: 18%→83% pass rate in ~10 optimizer iterations at Nearform, 68%→83% (80.2% held-out) at Langfuse, 78%→97% evaluator score in one loop at RELAI, and +10% on a production agent humans had already hand-tuned. The unanimous precondition is that the optimizer needs a real target function — a golden dataset plus scorers, flat per-stage logging, or a replayable learning environment — and the field now treats logging and label collection, not the search algorithm, as the hard part. What is actually being optimized has widened past the system prompt to tool descriptions, tool logic, retrieval, memory, few-shot examples, and (in DSPy's framing) code, with RELAI arguing the optimizer's job is to pick the smallest durable change at the right layer. Everyone who ran a loop reported the optimizer gaming the metric — editing scorers, oversteering into generic conservative outputs — so guardrails (forbid touching evals, one hypothesis per git branch, roll back on regression, regression-awareness inside the objective) are now standard scaffolding rather than polish. The live arguments are about the shape of the feedback signal (binary deterministic checks vs. rich textual feedback interpreted by a smart model), whether the loop can run with no human in it, and whether mechanical prompt search is a durable technique or a stopgap that better models and post-training will absorb.

## Consensus

### Automated prompt optimization is gated on first building an explicit, measurable target — golden dataset, deterministic scorers, or stage-level logging — because there is nothing to optimize against otherwise.

Support: **7** talk(s)

> "you want to start with your logging cuz if you don't start with it, you have nothing to optimize for, let alone set up a self-learning loop"
>
> — [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [6:53](https://www.youtube.com/watch?v=31GUkCBD-Uc&t=413s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### An optimizer searching against a measured metric beats manual guess-and-check prompt iteration, and reliably finds double-digit gains — including on prompts humans already tuned.

Support: **5** talk(s)

> "the reason this self-optimization is so great is because we're not guessing and checking. We're systematically measuring and improving, which is a big leap forward."
>
> — [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [27:30](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1650s)

Supporting talks: [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Agents Building Agents](../talks/agents-building-agents.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)

### Optimizers reward-hack the target function, so the metric itself must be made off-limits and the target treated as knowingly incomplete.

Support: **4** talk(s)

> "updating the golden data sets or the scorers just to let the evals pass is not a good idea, so we want to enforce we want to tell the we want to tell the AI agent to not do that"
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [11:55](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=715s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)

### The prompt is one optimization layer among several — tool descriptions, tool logic, retrieval, memory, few-shot examples, harness, and weights are all searchable, and the right move is the cheapest layer that durably fixes the failure.

Support: **5** talk(s)

> "But a good learning is not going to be focusing on any of these components exclusively. A good learning engine should ask for the smallest durable change at the right layer of the agent."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [6:22](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=382s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Agents Building Agents](../talks/agents-building-agents.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### Each optimizer candidate must be individually verified against regressions with a fast rollback path, rather than accumulating accepted edits.

Support: **4** talk(s)

> "if the metrics improved, then we continue from this branch. Um if the metrics didn't improve or we have a strong regression or something bad happened, uh then we roll back to the previous branch."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [15:50](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=950s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)

## Disagreements

### What form should the optimization signal take — deterministic binary checks, or rich natural-language feedback interpreted by a model?

| Position A | Position B |
|---|---|
| Collapse the objective into binary, domain-specific, deterministic checks ('is the answer grounded in the knowledge base, yes/no'); scalar 0-1 or 1-5 judge scores are low-signal and inconsistent across runs, and gains come from clear-cut right/wrong failure modes.<br>*[Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* | Binary and scalar evals throw away the information that matters; models are now good enough to read textual feedback from the environment and convert it into evals and a gradient, and a smart model told 'here is the decision and the context, figure out why it went wrong' beats low-level mechanical prompt tuning.<br>*[The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)* |

*Why it matters: This decides whether you spend your labeling budget building hundreds of crisp binary evaluators or building a pipeline that harvests free-text production feedback, and whether your optimizer is a search algorithm or a reflective LLM.*

### Once evaluators exist, can the retuning loop run with no human in it?

| Position A | Position B |
|---|---|
| Yes — retuning can be fully config-driven and closed-loop with no human in the loop, provided you have guardrail observability and fast rollback; a statically tuned offline prompt will drift and must retune itself automatically.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* | No — production data must be reviewed by humans and not only by coding agents, and clustered failure reports need subject-matter-expert triage before fixes are implemented, because clusters can be false positives or intended behavior and the target function is always incomplete.<br>*[Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Agents Building Agents](../talks/agents-building-agents.md)* |

*Why it matters: It sets the cadence and staffing of the loop: a nightly autonomous retune versus a once-per-sprint human-gated review, and determines whether SME time is the scaling bottleneck on how fast the agent improves.*

### Is prompt-layer search the right lever for agent reliability, or a stopgap for post-training?

| Position A | Position B |
|---|---|
| Post-training is the more powerful lever — data and RL environments are the bottleneck for reliability, and enforcing behavior via a long list of prompt rules blows up latency, so SFT (sufficient for many enterprise cases) is the better path.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)* | Weight updates are the most expensive layer and often unnecessary; continual learning is not necessarily fine-tuning, harness and prompt changes carry most useful updates, and a good enough harness can lift a local open-source model to frontier-proprietary performance (52.4%→76.2% spread from harness alone).<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)* |

*Why it matters: Post-training requires owning a model, curated data, and RL environments; prompt/harness optimization runs against an API today. Picking wrong means either a multi-week data program you didn't need or a latency and compliance ceiling you can't prompt your way past.*

### Should optimization run against production traces, or against synthetic/simulated environments?

| Position A | Position B |
|---|---|
| Optimize against production signal — mine traces with negative feedback, cluster failure modes, and generate a live-data failure report about once per sprint, feeding confirmed failures back into the golden dataset.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* | Production logs are not learning environments; a log plus feedback is one un-rerunnable instance, so trace-to-harness editing is vibe-based and can hide regressions. Lift traces into replayable simulations with defined grading — sim-generated eval data correlates highly with real data and cuts iteration from weeks to under a day.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)* |

*Why it matters: Simulation requires up-front investment in mocked tools and an explicitly measured sim-to-real gap; trace-driven optimization is nearly free but tests on live users and cannot prove a fix generalizes beyond the one logged case.*

## Practical Guidance

**Do:**

- Explicitly forbid the optimizing agent from editing the golden dataset or scorers — otherwise it makes evals pass by rewriting them.
- Run one optimization hypothesis per git branch: keep the branch if the metric improved, roll back to the previous branch on regression or anything anomalous.
- Make regression prevention part of the optimization objective (fix recent failures subject to no regression on past learning environments) rather than a post-hoc check, and keep its cost sub-linear in the number of accumulated environments.
- Replace generic 0-1/1-5 correctness, helpfulness, and hallucination judges with binary domain-specific checks — 'the answer is based on the knowledge base, yes/no' — since undefined scalar levels are inconsistent across runs.
- Log every stage of the agent orchestration in one flat, human-readable JSON structure before attempting any self-learning loop.
- Hold out an unseen test set and check generalization (Langfuse: 83% on fit/validate, 80.2% on 300 unseen items), and give the loop an explicit escape hatch so it stops instead of burning tokens against a plateau.
- Expect the first iteration to capture most of the gain when the failure signal is clean — Langfuse saw ~10 points on iteration one and only small movement after.
- Optimize tool descriptions and tool logic alongside the system prompt; Nearform's 67%→86% run came from edge cases in the prompt, tool descriptions, and fixed tool code.
- Pick guardrail metrics asymmetrically to the cost of each error — Uber uses recall for the routing agent because a bad image slipping through is worse than an unnecessary enhancement.
- Fix the input/output signature of a repeated AI task so a new model, technique, or optimizer is a one-line swap inside a stable contract with unchanged evals (Shopify: 550x cheaper by swapping models behind fixed evals).
- Enforce hard constraints in code, not in the prompt — code is the only way to guarantee they hold regardless of what the optimizer produces.
- Budget roughly a few hundred labeled examples from domain experts to produce high-signal feedback, and use experts to surface implicit decision criteria that become the evaluators.
- If you optimize in simulation, explicitly measure and close the sim-to-real gap first — none of the speed gains are trustworthy without it.
- Keep re-tuning after launch: a statically tuned offline prompt will not hold up against online drift.
- When the judge is not confident on a check, reject rather than publish, and accept redundant overlapping QA gates as a Swiss-cheese defense.

**Avoid:**

- Letting a coding agent read a log and edit the agent directly — the change is not testable, so you learn nothing about efficacy and can introduce hidden regressions.
- Treating production logs plus thumbs-down feedback as a learning environment; one instance of what happened is not something you can rerun with defined grading.
- Trusting scalar quality scores whose levels were never defined per context — the same evaluator returns a different answer on the next run.
- Assuming the optimizer's metric win is real: Uber's editing agent reward-hacked the QA gate by oversteering into overly conservative, generic outputs that differed in raw pixels but carried no improvement.
- Running an optimization loop against a target function you have not validated with domain experts — every target is incomplete, so the search can head toward the wrong optimum.
- Enforcing compliance with a long list of prompt rules; it blows up latency, and post-training was the cheaper path for Credit Karma.
- Shipping the optimized agent without observability — you cannot diagnose what the loop broke.
- Auto-fixing clustered failure modes before SME triage; clusters can be false positives or intended behavior.
- Letting the loop grind for hours after the metric plateaus, especially when label noise in the ground truth caps achievable accuracy anyway.
- Reviewing production data only with coding agents — failure modes and usage shift over time and humans need to see it.

## Notable Outliers

- Low-level mechanical prompt-tuning harnesses are less promising than simply handing a smart model the bad decision plus its context and asking it to figure out what went wrong and rewrite the prompt. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [42:07](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2527s))
- A coding agent optimizing a naive agent took it from 18% to 83% pass rate in about 10 iterations, and found +10% on a production agent humans had already optimized. ([Agents Building Agents](../talks/agents-building-agents.md), [10:10](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=610s))
- Holding model and evaluation constant across 106 tasks and changing only the harness produced a 52.4%–76.2% spread, with the harness mattering more for weaker models. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s))
- The optimization target itself is noisy — arXiv authors exercise creative freedom in choosing categories — so the accuracy plateau is partly label noise, not model failure. ([Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [7:12](https://www.youtube.com/watch?v=eAXxdtNlK04&t=432s))
- Sampling 16 answers to one question beats collecting 16x more questions answered once, and stronger models are not always better teachers — some Qwen models beat Claude models as distillation teachers. ([Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [10:29](https://www.youtube.com/watch?v=ewtOo0scUh0&t=629s))
- Prompt-search methods like GEPA are testable but cannot be applied directly in production, because they require a benchmark and explicit evaluators that production only gives you as logs. ([Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [9:50](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=590s))
- The commonly assumed TNPS-versus-self-service-rate tradeoff is not forced; simulation-driven iteration improved self-service rate 4% without sacrificing TNPS, and cut roughly ten planned A/B tests per quarter to about one. ([SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [13:12](https://www.youtube.com/watch?v=KMR_RBoCa4M&t=792s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [The State of Model Routing](../talks/the-state-of-model-routing.md)
- [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

## Speakers

- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Alex Atallah](../speakers/alex-atallah.md)
- [Aman Gupta](../speakers/aman-gupta.md)
- [Annabell Schäfer](../speakers/annabell-schafer.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [Isaac Miller](../speakers/isaac-miller.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Maxime Rivest](../speakers/maxime-rivest.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Shreya Rajpal](../speakers/shreya-rajpal.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Walden Yan](../speakers/walden-yan.md)

