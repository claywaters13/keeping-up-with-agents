---
title: "prompt optimization"
type: "concept"
slug: "prompt-optimization"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 16
---

# prompt optimization

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **16** speaker(s)

**Definition:** Automated search over prompts against a metric, replacing hand-tuning with an optimizer.

*Also referred to as: automated prompt optimization, automatic prompt optimization, prompt optimization search, system prompt optimization, prompt tuning, declarative signatures, regression-aware optimization*

## State of Practice

The field has largely stopped defending hand-tuned prompts: multiple teams reported that an optimizer — either a formal prompt-search method like GEPA/DSPy or a coding agent running hypothesis-test-rollback loops — beats human iteration once you have a metric, with reported jumps of 18%→83%, 67%→86%, 68%→83%, and 78%→97% on internal eval suites. The consensus is that the hard part has moved off the prompt and onto the objective: you need a golden dataset or replayable learning environment, binary domain-specific checks rather than 0–1 'correctness' scores, and definitions of 'better' negotiated with product, legal, or clinicians before the optimizer runs. Optimizers are treated as adversaries of their own metric — speakers independently reported reward hacking (agents editing scorers, or oversteering into generic outputs that differ in pixels but not in quality), so the standard control structure is per-hypothesis git branches, guardrail metrics with fast rollback, and an explicit prohibition on the optimizer touching evals. Regression is the live research edge: fixing today's failure while provably not breaking last month's is not solved by post-hoc checks, and at least one team argues it must be inside the optimization objective. The system prompt is also no longer seen as the only knob — the same loops now edit tool descriptions, tool logic, retrieval, memory, few-shot sets, and code, with the guidance being to make the smallest durable change at the cheapest layer that fixes the failure.

## Consensus

### Automated optimization against a measured objective beats manual prompt engineering; guess-and-check prompt iteration is obsolete where a metric exists.

Support: **6** talk(s)

> "the reason this self-optimization is so great is because we're not guessing and checking. We're systematically measuring and improving, which is a big leap forward."
>
> — [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [27:30](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1650s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)

### The optimizer's ceiling is set by the target function, so the real work is specifying and validating the metric — evals, golden labels, or a replayable environment — before any search runs.

Support: **5** talk(s)

> "a target that you give an agent is actually also always incomplete"
>
> — [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [1:10](https://www.youtube.com/watch?v=eAXxdtNlK04&t=70s)

Supporting talks: [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)

### Optimizers will game the metric rather than improve the product, so the eval artifacts must be write-protected and the loop must be watched for degenerate wins.

Support: **3** talk(s)

> "updating the golden data sets or the scorers just to let the evals pass is not a good idea, so we want to enforce we want to tell the we want to tell the AI agent to not do that"
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [11:55](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=715s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)

### Every optimization loop needs a regression check and a rollback/escape hatch per iteration, not just a final score comparison.

Support: **4** talk(s)

> "if the metrics improved, then we continue from this branch. Um if the metrics didn't improve or we have a strong regression or something bad happened, uh then we roll back to the previous branch."
>
> — [Agents Building Agents](../talks/agents-building-agents.md), [15:50](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=950s)

Supporting talks: [Agents Building Agents](../talks/agents-building-agents.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)

### 'Prompt optimization' in practice spans several layers — system prompt, tool descriptions, tool logic, few-shot examples, retrieval, memory, and code — and the right move is the cheapest layer that durably fixes the failure.

Support: **4** talk(s)

> "But a good learning is not going to be focusing on any of these components exclusively. A good learning engine should ask for the smallest durable change at the right layer of the agent."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [6:22](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=382s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Agents Building Agents](../talks/agents-building-agents.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)

## Disagreements

### Should prompt optimization be done by a dedicated optimizer/search framework, or by handing a failure and its context to a strong general model and letting it rewrite the prompt?

| Position A | Position B |
|---|---|
| Use a formal optimizer with a declared objective — GEPA, DSPy-style compilation over few-shot examples/prompts/code, or a config-driven auto-retuner — because it is systematic, reproducible, and produces an audit trail (tuning drops from days to 30–60 minutes).<br>*[Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* | Low-level mechanical prompt-tuning harnesses are the less promising path; give a smart model the bad decision plus the context and let it diagnose and rewrite, or let a coding agent form and test hypotheses over the whole agent rather than searching prompt space.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [Agents Building Agents](../talks/agents-building-agents.md)* |

*Why it matters: It decides whether you build and maintain a metric-driven optimizer pipeline or just pay for frontier-model reflection passes, and whether prompt improvements are reproducible artifacts or one-off model judgments.*

### Can the improvement loop run closed, with no human in the loop, or must domain experts sit inside it?

| Position A | Position B |
|---|---|
| The retuning loop can be fully automated and config-driven with no human in the loop, provided you have guardrail observability and fast rollback.<br>*[Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* | Humans are load-bearing: domain experts must surface implicit decision criteria and write the high-signal evaluators, clinicians must define the cost matrix, production data must be reviewed by a human and not only by coding agents, and clustered failure reports must be triaged by SMEs before fixes are implemented because clusters can be false positives.<br>*[Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [Agents Building Agents](../talks/agents-building-agents.md)* |

*Why it matters: Full automation is the only way to keep pace at marketplace scale, but if the evaluator encodes an incomplete target the loop optimizes confidently in the wrong direction — the choice sets both the iteration rate and the blast radius of a bad objective.*

### What data should the optimizer be run against — mined production traces, or synthetic/simulated environments?

| Position A | Position B |
|---|---|
| Production logs and feedback are not learning environments; they must first be lifted into replayable simulations with explicit evaluators, and simulated data is what makes large-scale parallel iteration possible (weeks to under a day) without experimenting on live users.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)* | Run the loop against real production signal: mine traces with negative feedback into clustered failure reports on a per-sprint cadence, and retune components online against observed drift, because a statically tuned offline model will not hold up in production.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* |

*Why it matters: It determines whether your optimization budget goes into building simulators and closing a sim-to-real gap, or into trace instrumentation and online guardrails — and whether you can optimize at all before you have production traffic.*

### Once evals exist, is prompt-layer optimization the right place to spend, or should the budget go to post-training the model?

| Position A | Position B |
|---|---|
| Most of the achievable gain lives in the prompt/harness/memory layers: harness changes alone spread results 52.4%→76.2% at fixed model, coding agents beat already human-optimized production prompts by 10%, and continual learning is 'not necessarily model fine-tuning'.<br>*[What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Agents Building Agents](../talks/agents-building-agents.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)* | Post-training is the more powerful lever on reliability than prompting or harness changes; enforcing behavior through a long list of prompt rules blows up latency, and SFT alone is sufficient for many enterprise cases while also cutting cost and improving throughput.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)* |

*Why it matters: Prompt optimization is cheap and reversible; weight updates require curated data and RL environments and are the most expensive layer — picking wrong either caps your reliability ceiling or burns a training budget on something a system-prompt edit would have fixed.*

## Practical Guidance

**Do:**

- Build the golden dataset plus scorers first — treat it as a test suite for a non-deterministic system — and fold every newly discovered failure mode back into it so the optimizer cannot reintroduce the bug.
- Explicitly forbid the optimizing agent from editing golden datasets or scorers.
- Run each optimization hypothesis on its own git branch, keep the branch if the metric improves, roll back on regression, and tackle one failure class per hypothesis.
- Replace scalar quality scores (correctness/helpfulness on 0–1 or 1–5) with binary domain-specific checks: 'is the answer grounded in the retrieved context, yes/no', 'is the brand name correct', 'which known failure mode is this'.
- Collect roughly a few hundred labeled examples from domain experts, mining them for the implicit decision criteria that become the evaluators.
- Give the loop a validation split and an explicit escape hatch so it stops instead of burning tokens against a plateau — most of the gain often arrives in the first iteration.
- Encode a guardrail metric with an asymmetric cost (recall for a routing gate; over-call hazards rather than under-call them) so the optimizer cannot trade away the error type you actually care about.
- Let the loop edit tool descriptions and tool logic, not just the system prompt — reported wins came from catching edge cases in tool descriptions as much as from prompt text.
- Keep the task interface (signature/input-output contract) fixed so prompts, models, and techniques can be swapped and re-optimized against the same evals.
- Ship the evidence trail — pinned prompts, datasets, judge verdicts mapped to hazards — since automated optimization produces a reproducible audit artifact that manual tuning does not.

**Avoid:**

- Trusting a metric win without inspecting the output: an agent will oversteer into overly conservative, generic outputs that change the pixels and pass the QA gate while carrying no real improvement.
- Running a 'trace-to-harness' fix where a coding agent reads a log and edits the agent with no way to test the change — it is vibe-based and introduces hidden regressions.
- Treating regression prevention as a post-hoc check after the optimization run rather than a constraint inside the objective.
- Hand-tuning prompts and assuming they are stable — formatting changes alone have swung benchmarks by 76 percentage points and few-shot reordering has flipped models from near-random to near-SOTA.
- Optimizing against generic LLM-judge scores whose levels are never defined; the same evaluator returns a different answer on the next run.
- Starting an optimization program before per-stage logging exists — with no traces there is nothing to optimize and no basis for a self-learning loop.
- Assuming the plateau is the model's fault; noise in the ground-truth labels themselves caps achievable accuracy.
- Reviewing production data only with coding agents, since failure modes and usage shift over time and clusters can be false positives or intended behavior.
- Encoding compliance as an ever-growing list of prompt rules — it blows up latency and is the case where post-training is the better path.

## Notable Outliers

- A coding agent found improvements humans had missed on an agent that was already hand-optimized in production, adding +10% on internal benchmarks. ([Agents Building Agents](../talks/agents-building-agents.md), [11:06](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=666s))
- Prompt brittleness is severe enough to invalidate manual tuning outright: formatting changes alone have swung a benchmark by 76 percentage points, and reordering few-shot examples moves a model from near-random to near state-of-the-art. ([Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [11:25](https://www.youtube.com/watch?v=McknwOzbmyg&t=685s))
- Low-level mechanical prompt-tuning harnesses are a dead end compared with handing a smart model the bad decision and its context and asking it to figure out what went wrong. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [42:07](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2527s))
- Auto-improvement loops worked first in coding only because compilation supplies an unusually clear target function — not because the loops themselves generalize. ([Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [0:37](https://www.youtube.com/watch?v=eAXxdtNlK04&t=37s))
- The optimization target is migrating up the stack: DSPy optimization started with few-shot examples, became prompts, and is now becoming code. ([The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [11:10](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=670s))
- Holding evals fixed while swapping an expensive model for a cheap one delivered a 550x cost reduction at Shopify. ([The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [9:49](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=589s))
- A failed hypothesis is not necessarily a wrong hypothesis — the agent may have been onto something and simply implemented the change badly. ([Agents Building Agents](../talks/agents-building-agents.md), [17:24](https://www.youtube.com/watch?v=aHhB3sjGjkI&t=1044s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)
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
- [Jared Joselowitz](../speakers/jared-joselowitz.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Maxime Rivest](../speakers/maxime-rivest.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Shreya Rajpal](../speakers/shreya-rajpal.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Walden Yan](../speakers/walden-yan.md)

