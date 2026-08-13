---
title: "model routing"
type: "concept"
slug: "model-routing"
tier: "core"
maturity: "consolidating"
talk_count: 19
speaker_count: 32
---

# model routing

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **19** talk(s) by **32** speaker(s)

**Definition:** Dispatching requests to different models by task difficulty, cost, or capability, including fallback chains and gateway layers.

*Also referred to as: model routing and fallback, multi-model routing, model routing by task difficulty, cheap model substitution, semantic routing, model right-sizing, model routing and llm gateways*

## State of Practice

Routing has moved from an optimization to a default architectural assumption: 87% of teams surveyed run more than one model, and the live argument is no longer whether to tier but on what signal and at what layer. The dominant pattern is a frontier model held for planning, arbitration, or supervision while a cheaper implementation model does the bulk of token-generating work — Cognition's Devin Fusion claims 40% cost reduction on Fable-level intelligence this way, and Notion routes ~75% of its AI traffic through an auto model. A parallel school argues the routing decision is largely dissolved by scaffolding: with a state machine holding control flow, Haiku 4.5 replaces Opus 4.7 in live voice tutoring at ~900ms, and a compressed markdown page representation lets a cheap model beat Claude at browser tasks. The most consequential correction of the conference is that per-token price is the wrong routing signal — Opus scores 3x better than Haiku on terminal bench at 1/10 the total cost, because out-of-distribution small models burn tokens in tool loops. Cost has become a first-class production constraint monitored like an SLA, and optionality — a routing flag with fallback, open-weight targets, self-hosted or direct-compute capacity — is now framed as commercial leverage against providers that are structurally your competitors. What nobody has settled is the dispatch mechanism itself: static task-type routing, an embedding retriever, a cheap model-as-router, and deterministic harness control are all in production and their advocates make incompatible recommendations.

## Consensus

### Sending all traffic to the most capable available model is a routing failure; workloads should be tiered by difficulty, because most tasks do not need frontier capability.

Support: **8** talk(s)

> "And not all traffic is equal. It is a huge miss to send all of these to the latest opus model."
>
> — [Notion's Token Town](../talks/notions-token-town.md), [10:19](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=619s)

Supporting talks: [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Notion's Token Town](../talks/notions-token-town.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)

### A stronger harness substitutes for a stronger model: with control flow, state, and post-processing engineered outside the model, a small model hits the performance bar a frontier model was being used for.

Support: **7** talk(s)

> "instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn't have as much reasoning capabilities, but because of the harnessing around it, it's still able to perform at the level in which we expect"
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)

### Routing choices must be validated against your own workload and golden data, because public benchmarks, leaderboard rank, and peer recommendation do not predict performance on your stack.

Support: **6** talk(s)

> "Like swe bench is all in Python, we're Ruby on Rails. It is not the case that the benchmarks are identical for them."
>
> — [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [13:37](https://www.youtube.com/watch?v=OL7kfezynJM&t=817s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Notion's Token Town](../talks/notions-token-town.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)

### Keep the routing layer provider-agnostic with an explicit fallback path; a hard dependency on one provider is both an availability risk and a loss of commercial leverage.

Support: **6** talk(s)

> "If your production system has a hard dependency on one model from one provider and it does not have any routing flag, no fallback, you are one provider outage away from a complete agent outage"
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [7:46](https://www.youtube.com/watch?v=zU4EagB311U&t=466s)

Supporting talks: [Notion's Token Town](../talks/notions-token-town.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)

### Route on total trajectory cost and end-to-end outcome, not on per-token price or single-call latency — a cheaper-per-token model can be more expensive per completed task.

Support: **4** talk(s)

> "Like if you run terminal bench on Opus and Haiku, like Opus will do about three times better at 1/10 the cost of Haiku, even though Haiku's significantly cheaper per token."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [15:25](https://www.youtube.com/watch?v=QHBjufYK8TA&t=925s)

Supporting talks: [The State of Model Routing](../talks/the-state-of-model-routing.md), [Notion's Token Town](../talks/notions-token-town.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)

### The productive split is frontier model for high-level planning and delegation, smaller/cheaper models for executing the subtasks.

Support: **3** talk(s)

> "Your most intelligent should provide you with the overall plan and then subtasks for your smaller executioner like executioner models and that's exactly the future"
>
> — [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [14:30](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=870s)

Supporting talks: [The State of Model Routing](../talks/the-state-of-model-routing.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)

### Open-weight models are now viable routing targets for real production work, not just cost-saving toys, and serve as negotiation leverage against closed labs.

Support: **5** talk(s)

> "The other thing is that open weight models are actually pretty good now. We've been really happy with GLM 5.2. They're much cheaper."
>
> — [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [2:14](https://www.youtube.com/watch?v=OL7kfezynJM&t=134s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Notion's Token Town](../talks/notions-token-town.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)

## Disagreements

### Should the dispatch decision be made by a model, or by deterministic code outside the model?

| Position A | Position B |
|---|---|
| Use a model or a learned/semantic component as the router — a cheap model deciding which model handles the request, an embedding retriever selecting K=5 tools, or a dedicated routing agent guardrailed on recall.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)* | Take the dispatch decision out of the model entirely: a state machine or harness decides what happens next, and the model only proposes or speaks. When reliability approaches a coin flip, that is the signal to remove control flow from the model.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)* |

*Why it matters: It determines whether routing quality is an eval-and-retune problem (tool descriptions, embeddings, recall thresholds, drift retuning) or a software-engineering problem (state machines, validators, deterministic post-processing). The two paths have completely different failure modes and different on-call surfaces.*

### Does routing to cheaper models actually reduce total cost?

| Position A | Position B |
|---|---|
| Yes — route by difficulty and cheap models cut spend materially: an internal gateway defaulting to GLM and Kimi cut AI spend nearly in half, GLM used 2x the tokens at half the cost, and swapping to a local 3B model saved a dollar a day of inference per user.<br>*[Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Notion's Token Town](../talks/notions-token-town.md)* | Not reliably — small models called out of distribution inflate cost through excessive tool calls and runaway loops, so an expensive model can produce a cheaper overall system; it is not obvious that more expensive models make systems more expensive.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md)* |

*Why it matters: If cheap-model savings are real, the routing table can be tuned on price. If they invert out of distribution, routing must be gated on measured task-completion cost and every downgrade needs a distribution check before it ships.*

### Is routing by task type or difficulty a stable strategy for agentic workloads?

| Position A | Position B |
|---|---|
| Yes — classify the request up front and dispatch accordingly: Haiku for cheap work and Sonnet for harder work, an auto model absorbing ~75% of traffic, or a routing model that decides which pipeline an input enters.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Notion's Token Town](../talks/notions-token-town.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* | No — naive routing on task type is extremely fragile because complexity shifts mid-session; a frontier model should remain present throughout, watching if not executing, and routing signals should come from model internals like hallucination probes and prefill perplexity.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md)* |

*Why it matters: Front-loaded classification is cheap and easy to reason about; continuous frontier supervision costs frontier tokens on every session but survives tasks whose difficulty is not knowable at dispatch time.*

### For constrained or local deployment, should you quantize a large model or run a natively small, task-specific one?

| Position A | Position B |
|---|---|
| Train big and quantize: a 120B model at 4-bit is meaningfully more capable than a 35B at BF16 for the same disk footprint, and users preferred a mid-sized checkpoint they could quantize themselves over natively smaller releases.<br>*[Compression at the Edge](../talks/compression-at-the-edge.md)* | Select the smallest model that gives acceptable responses — the SAGE model — because latency is the binding product constraint: a compressed large model yields 5-10 tokens/sec without enough GPU, and a small model 200, and voice needs first speech inside ~950ms.<br>*[Frontier results, on device](../talks/frontier-results-on-device.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* |

*Why it matters: The two answers imply different hardware budgets and different eval axes — capability-per-byte versus P95 latency — and pick opposite defaults for on-device agents.*

## Practical Guidance

**Do:**

- Put the frontier model on planning, arbitration, or supervision and delegate implementation to a cheaper model; Devin Fusion reports 40% cost reduction on Fable-level intelligence with this split
- Benchmark candidate models continuously against your own repo and workload, not SWE-bench or Terminal-Bench, and let those numbers drive routing decisions
- Evaluate models on entire trajectories rather than single calls — Notion picked Parallel for web search despite it not being cheapest per call
- Ship a model-routing feature flag with a fallback chain, resolved per turn rather than at session start, and make sub-agents go through the same middleware
- Pick the fastest model your latency budget allows and spend the remaining engineering effort on scaffolding — voice needs first speech in ~950ms, chat degrades past 4 seconds
- Measure P95 latency on the actual serving platform before routing to a model: GPT-5 mini showed 5,000ms typical, 7,000ms P95, sometimes 10,000ms despite being small and cheap
- Use one long-lived sidekick agent with a running context instead of spawning fresh sub-agents, since cached tokens are roughly 10x cheaper
- Keep a stable context prefix across requests — up to 90% cheaper and faster inference when the first ~90% of the window is unchanged
- Cap working context at 200K tokens and preferably under 100K regardless of the advertised window
- Above ~50 tools, retrieve tool schemas just-in-time at K=5 instead of loading the whole catalog; below 20 tools skip the router entirely
- Fix structural and length failures with deterministic post-processing in the harness rather than by routing up to a larger model
- Route non-LLM work off the LLM entirely — CSV-to-PDF conversion, deterministic SQL, CLI-backed tool calls belong on CPU
- Keep an open-weight model in the routing pool now; tasks open weights nearly handle today are likely fully covered within six months

**Avoid:**

- Sending every request to the newest Opus-tier model — triaging an email inbox on Opus overcharges the customer and yourself
- Choosing a model on a colleague's recommendation without evals; the recommended Gemma came in around 8 seconds of latency and would have shipped a materially worse experience
- Trading optionality for a volume discount or a single-lab marketing exclusivity — loud exclusivity is a signal the product is off-frontier much of the time
- Assuming cheaper per token means cheaper per task; out-of-distribution small models raise cost through tool-call thrash and runaway loops
- Routing purely on task type in agentic sessions, where complexity changes mid-session
- Letting sub-agents bypass the routing and flag middleware — a flipped kill switch never reaches them
- Treating compaction as a cost or throughput fix; it forces a cache miss and raises input token cost, and is justified by intelligence not price
- Trusting LLM-judge scores across model families without manual inspection — Claude Opus favored Claude Sonnet's output over Llama 3.2's
- Shipping distilled per-capability models into mobile apps, where each capability change means retraining and pushing a 1-2 GB download over users' data plans
- Quantizing linear attention layers: short benchmarks look fine while long-context production output degenerates into gibberish

## Notable Outliers

- Auto-routing sat unadopted for nearly two years and only exploded in January 2026 because open claw sends a heartbeat to the user's default model every ~10 minutes. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [27:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1623s))
- Rather than paying per token, buy direct compute capacity from providers — the economics of cached tokens made the underlying compute far cheaper than API pricing, which amortizes across all customers' usage shapes. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [36:27](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2187s))
- On a real repo bug, GLM used twice as many tokens at half the cost and verified the build compiled, while Opus left type errors and broke the production build. ([Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [9:44](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=584s))
- A cheaper model given a 1,800-token compressed markdown page representation beats Claude driving by screenshots on both speed and task success — the constraint is the page representation, not the model. ([Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [0:28](https://www.youtube.com/watch?v=JnubYCYunk8&t=28s))
- Tool-selection accuracy collapses from ~78% at 10 tools to 13.6% at 741 tools due to lost-in-the-middle attention, while semantic routing holds above 83% across the same range. ([The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [3:57](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=237s))
- Current routing techniques, including Devin Fusion itself, will look like legacy ideas within a year as delegation capability moves into the models. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [12:29](https://www.youtube.com/watch?v=QHBjufYK8TA&t=749s))
- Your model supplier is structurally your competitor: they serve first-party products at cost while resellers stack surcharges, so tying yourself to one provider leaves no exit. ([Notion's Token Town](../talks/notions-token-town.md), [7:35](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=455s))

## All Talks

- [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)
- [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md)
- [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)
- [Compression at the Edge](../talks/compression-at-the-edge.md)
- [Computer Use at the Edge of the Statistical Precipice](../talks/computer-use-at-the-edge-of-the-statistical-precipice.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)
- [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)
- [Notion's Token Town](../talks/notions-token-town.md)
- [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)
- [OpenClaw in Your Hand: Building a Physical AI Terminal](../talks/openclaw-in-your-hand-building-a-physical-ai-terminal.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)
- [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The State of Model Routing](../talks/the-state-of-model-routing.md)
- [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)
- [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Alex Atallah](../speakers/alex-atallah.md)
- [Alex Cheema](../speakers/alex-cheema.md)
- [Allen Pike](../speakers/allen-pike.md)
- [Ankush Rastogi](../speakers/ankush-rastogi.md)
- [Arjun Singh](../speakers/arjun-singh.md)
- [Asma Beevi](../speakers/asma-beevi.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Daniel Han](../speakers/daniel-han.md)
- [Dat Ngo](../speakers/dat-ngo.md)
- [George Cameron](../speakers/george-cameron.md)
- [Jai Chopra](../speakers/jai-chopra.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Kushan Raj](../speakers/kushan-raj.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Merve Noyan](../speakers/merve-noyan.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Parth Sareen](../speakers/parth-sareen.md)
- [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)
- [Pierluca D'Oro](../speakers/pierluca-d-oro.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Saoud Rizwan](../speakers/saoud-rizwan.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Soumya Gupta](../speakers/soumya-gupta.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Walden Yan](../speakers/walden-yan.md)

