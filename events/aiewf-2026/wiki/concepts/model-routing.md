---
title: "model routing"
type: "concept"
slug: "model-routing"
tier: "core"
maturity: "contested"
talk_count: 20
speaker_count: 33
---

# model routing

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **20** talk(s) by **33** speaker(s)

**Definition:** Dispatching requests to different models by task difficulty, cost, or capability, including fallback chains and gateway layers.

*Also referred to as: model routing and fallback, multi-model routing, model routing by task difficulty, cheap model substitution, semantic routing, model right-sizing, model routing and llm gateways*

## State of Practice

Routing has moved from a cost hack to a default architectural layer: 87% of surveyed teams run more than one model, and the question is no longer whether to route but on what signal. The dominant pattern is role-based rather than request-based — a frontier model for planning, hard decisions, or supervision, with cheaper/smaller/open-weight models doing execution — with Cognition reporting 40% cost reduction on Fable-level intelligence and Notion reporting that its auto model absorbs ~75% of AI traffic. A second, equally strong current holds that the routing win comes less from model selection than from the scaffolding around the model: teams at Microsoft, Arize, and ARK all report replacing a frontier model with Haiku-class or open-source models once state tracking, deterministic post-processing, or page representation moved into the harness. Latency has become a first-class routing key alongside cost — 950ms to first speech for voice, ~4s as the limit of user believability — and serving platform matters as much as parameter count (GPT-5 mini measured at 5-10s P95 despite being small). The load-bearing counter-evidence is that per-token price does not predict trajectory cost: on terminal bench Opus scored 3x better than Haiku at 1/10 the total cost, and out-of-distribution small models can raise spend through tool-call loops. Nobody claims the current techniques are stable — the OpenRouter/Cognition panel expects today's routing approaches, including Devin Fusion, to look like legacy ideas within a year.

## Consensus

### Sending all traffic to the newest frontier model is a mistake; requests should be dispatched by difficulty, and most workloads do not need frontier capability.

Support: **6** talk(s)

> "And not all traffic is equal. It is a huge miss to send all of these to the latest opus model."
>
> — [Notion's Token Town](../talks/notions-token-town.md), [10:19](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=619s)

Supporting talks: [Notion's Token Town](../talks/notions-token-town.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)

### A hard dependency on one provider is an availability and commercial liability; systems need a switching/fallback layer and teams should preserve the ability to walk.

Support: **5** talk(s)

> "If your production system has a hard dependency on one model from one provider and it does not have any routing flag, no fallback, you are one provider outage away from a complete agent outage"
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [7:46](https://www.youtube.com/watch?v=zU4EagB311U&t=466s)

Supporting talks: [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [Notion's Token Town](../talks/notions-token-town.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)

### A strong harness lets a materially smaller model hit the performance bar a frontier model was being used for, so engineering effort should go into scaffolding before model upgrades.

Support: **5** talk(s)

> "instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn't have as much reasoning capabilities, but because of the harnessing around it, it's still able to perform at the level in which we expect"
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Frontier results, on device](../talks/frontier-results-on-device.md)

### Latency budget, not capability ranking, should select the model for interactive paths — pick the fastest model that clears the budget and engineer around it.

Support: **4** talk(s)

> "Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding."
>
> — [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s)

Supporting talks: [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)

### The productive split is by role, not by request: the strongest model plans, decides, or supervises, and cheaper/faster models execute the subtasks.

Support: **3** talk(s)

> "Your most intelligent should provide you with the overall plan and then subtasks for your smaller executioner like executioner models and that's exactly the future"
>
> — [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [14:30](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=870s)

Supporting talks: [The State of Model Routing](../talks/the-state-of-model-routing.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)

### Open-weight models are now good enough to be a real routing destination for production work, not just a cost experiment, and they provide negotiating leverage against closed labs.

Support: **5** talk(s)

> "we'll notice that although they've lagged behind the American closed source competitors, we're at an inflection point where raw intelligence lead doesn't matter as much anymore"
>
> — [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [8:25](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=505s)

Supporting talks: [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Notion's Token Town](../talks/notions-token-town.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)

## Disagreements

### Does routing work to cheaper-per-token models actually lower total cost?

| Position A | Position B |
|---|---|
| Per-token price is a misleading routing signal: cheaper models can cost more per completed task because they loop, over-call tools, and burn more turns — Opus beat Haiku 3x on terminal bench at 1/10 the total cost, so vendor selection must be evaluated over whole trajectories rather than single calls.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [Notion's Token Town](../talks/notions-token-town.md)* | Cheaper models deliver real, measured savings even when they consume more tokens — GLM used 2x the tokens at half the cost and produced better code than Opus on a real repo bug, enterprises defaulting to GLM/Kimi in an internal gateway cut AI spend nearly in half, and Codex ran 4x the sessions of Claude Code at lower total cost.<br>*[Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)* |

*Why it matters: It determines whether routing is a cost lever at all, or only a latency and availability lever — and whether teams should invest in cheap-model dispatch or in trajectory-level evals that may send them back to the expensive model.*

### Should a request be dispatched to one selected model, or should a frontier model stay present in every session?

| Position A | Position B |
|---|---|
| Classify-then-dispatch on task type is too fragile for agentic work because complexity shifts mid-session; frontier intelligence should always remain in the system, watching if not executing, and single-model dependence is itself a failure mode worth answering with redundancy (31 models run in parallel on every patient conversation).<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)* | Pick one model per request by difficulty or use case — a cheap model can even be the router deciding which model handles the request, and the right target is the smallest model that produces acceptable output, with a recall-guardrailed routing agent deciding whether the expensive path runs at all.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [Building Closed-Loop Evals for a Multimodal Agent at Scale](../talks/building-closed-loop-evals-for-a-multimodal-agent-at-scale.md)* |

*Why it matters: Keeping a frontier model resident forfeits most of the theoretical cost savings but buys robustness on out-of-distribution turns; dispatching to a single cheap model maximizes savings but concentrates failure at the moment the task gets hard.*

### Should the routing and control decisions live in engineered code, or inside the models themselves?

| Position A | Position B |
|---|---|
| Routing capability is migrating into the models — newer frontier models are naturally collaborative and get better at delegating work, and low-level mechanical prompt-tuning harnesses are less promising than letting a smart model inspect a bad decision and rewrite the logic itself.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* | The model must never hold control flow or state — the harness validates, advances state, and decides what comes next; the model only proposes, and structural failures get fixed with deterministic post-processing rather than by escalating to a bigger model.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Frontier results, on device](../talks/frontier-results-on-device.md)* |

*Why it matters: If delegation lives in the model, teams should buy the best orchestrator model and keep the scaffolding thin; if it lives in code, the scaffolding is a one-time investment that permanently lowers the capability floor of every model you route to.*

## Practical Guidance

**Do:**

- Put a routing flag / gateway in front of every model call so you can fail over to another provider in seconds without a deployment, and resolve the flag per turn rather than at session start
- Force sub-agents through the same routing middleware as the parent — a bypassed child agent never sees the flip
- Evaluate model choices on entire trajectories rather than single-call cost or latency (Notion chose Parallel for web search despite it not being cheapest)
- Benchmark candidate models continuously on your own codebase, not on SWE-bench or Terminal-Bench — a Python benchmark does not predict Ruby on Rails performance
- Set an explicit latency budget first (≈950ms to start speaking for voice, ~4s as the limit of user believability) and select the fastest model that clears it
- Check the serving platform's latency prioritization, not just parameter count — GPT-5 mini measured 5,000ms typical and 10,000ms worst case
- Use a cheap model as the router that decides which model handles the request
- Route around the LLM entirely for deterministic work — CSV-to-PDF conversion, CLI tool calls, deterministic SQL
- Fix structural and length failures with deterministic post-processing in the harness instead of upgrading the model
- Keep one long-lived sidekick with a running context instead of spawning fresh sub-agents, since cached tokens are ~10x cheaper
- Cache the stable context prefix — up to 90% cheaper and faster inference when the first ~90% of the context is identical between requests
- Stay under 100-200K tokens of context regardless of advertised window sizes, and remember compaction forces a cache miss
- Cap tool-call loop iterations and run observability on tool calls before shipping
- Use recall as the guardrail metric when routing away from the expensive path costs more than an unnecessary invocation
- For a fixed local footprint, route to a 120B model at 4-bit rather than a 35B at BF16
- Explore self-hosting or buying direct compute when your workload shape differs from the average API customer's

**Avoid:**

- Routing on task type alone — complexity shifts mid-session and the classification goes stale
- Assuming cheaper per token means cheaper per task; out-of-distribution small models call tools erratically and can increase total cost
- Public marketing exclusivity with a single lab, or accepting a volume discount that costs you the ability to walk
- Picking a model on peer recommendation instead of evals — the socially recommended model (Gemma) came in around 8 seconds of latency
- Trusting LLM-judge scores across model families; Claude Opus favored Claude Sonnet's output over Llama 3.2's
- Adding more prompt rules to fix step-skipping and looping — that is a control problem, not a prompting problem
- Shipping distilled on-device models into mobile apps where each capability change means pushing a new 1-2GB artifact over users' data plans
- Treating pass@k on static deterministic benchmarks as evidence of model quality — a blind replay agent matches or beats the frontier model it was extracted from
- Leaving temporary routing/rollout flags in place after rollout; every flag needs an owner and a removal date

## Notable Outliers

- Rather than routing to one model, run 31 models in parallel on every single patient conversation, because a singular model is an unacceptable single point of failure. ([200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [8:26](https://www.youtube.com/watch?v=AN65uc645mE&t=506s))
- Opus scores about 3x better than Haiku on terminal bench at 1/10 the total cost, despite Haiku being significantly cheaper per token. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [15:25](https://www.youtube.com/watch?v=QHBjufYK8TA&t=925s))
- Auto-routing sat unused for nearly two years; adoption exploded in January 2026 specifically because open claw sends a heartbeat to the user's model of choice every 10 minutes. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [27:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1623s))
- Model internals — hallucination probes, linear probes, perplexity over prefill vectors — can act as a proxy for how lost a model is and therefore as the routing trigger. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [38:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2283s))
- Today's routing techniques, Devin Fusion included, will look like legacy ideas within a year. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [12:29](https://www.youtube.com/watch?v=QHBjufYK8TA&t=749s))
- A cheaper model given a compressed markdown page representation (~1,800 tokens vs ~20,000 for the DOM) beats a stronger model doing screenshot-driven browsing on both speed and task success. ([Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [0:28](https://www.youtube.com/watch?v=JnubYCYunk8&t=28s))
- The 5-minute KV cache lifetime that shapes routing and compaction economics is an operational pricing decision by providers, not a physical constraint. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [34:46](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2086s))

## All Talks

- [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)
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
- [Vivek Muppalla](../speakers/vivek-muppalla.md)
- [Walden Yan](../speakers/walden-yan.md)

