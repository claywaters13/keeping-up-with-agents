---
title: "sovereign and air-gapped deployment"
type: "concept"
slug: "sovereign-and-air-gapped-deployment"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 12
---

# sovereign and air-gapped deployment

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **12** speaker(s)

**Definition:** Running models under jurisdictional or network isolation — on-prem, VPC, air-gapped, or nationally controlled — and the geopolitics that drive it.

*Also referred to as: sovereign ai, air-gapped deployment, vpc deployment, export controls on frontier models, ai governance and geopolitics, self-hosted inference infrastructure, model access restrictions, confidential computing*

## State of Practice

Sovereignty stopped being a compliance checkbox and became an architecture decision at this conference, and the stated driver is almost never token price — it is revocability. Speakers cited concrete events: Fable access being pulled, GPT-5.6 being unavailable, a retailer walking away after ~$200M of Anthropic inference, a third-party vendor dependency getting redlined in audit and blocking a launch. The practical answer splits into three implementations that are not interchangeable: run open weights on hardware you own (DGX Spark, RTX 3090/5090 clusters, M3 Ultra), take delivery of a vendor's agent sandbox inside your own VPC so production systems never dial out, or keep running on hyperscaler infrastructure but make the data cryptographically unreadable to the operator via customer-held keys, attestation, and a small auditable trust base. What made all three viable this year is that local open-weight models crossed the agentic-usability line — Qwen 3.5/3.6 27B beating Llama 405B, a 4B model at GPT-4o quality on an iPhone, Nemotron 3 Ultra at 550B running 30 tok/s across four Sparks — so "sovereign" no longer means "degraded." The unresolved part is scope: whether sovereignty means moving the whole stack in-house, or tiering frontier models for planning and local models for execution while owning only the trace and data plane.

## Consensus

### Enterprise demand for local/open deployment is driven by control, switchability, and rug-pull avoidance — not primarily by inference cost.

Support: **4** talk(s)

> "they want control, they want sovereignty, they want the ability to switch out models, they don't want to get rugpulled"
>
> — [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [15:08](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=908s)

Supporting talks: [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)

### Frontier model access is revocable — by the vendor or by geopolitics — and that revocability is now a live engineering risk that shapes deployment architecture.

Support: **5** talk(s)

> "how many people were kind of annoyed when access to Fable got pulled? Show of hands. Yeah, a whole lot of people, right?"
>
> — [Security Track Intro](../talks/security-track-intro.md), [2:16](https://www.youtube.com/watch?v=2xJoimgoqBg&t=136s)

Supporting talks: [Security Track Intro](../talks/security-track-intro.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)

### Sovereignty is about owning the data and trace plane — production systems, telemetry, and unencrypted data must not leave the customer's perimeter, even when a vendor's software runs inside it.

Support: **5** talk(s)

> "if you also don't own the traces, the data, everything that flows through your software factory, um then you're probably going to be in trouble as you start to want to evolve your software factory"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [7:32](https://www.youtube.com/watch?v=wpOA-UXynoM&t=452s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)

### Local open-weight models on commodity or desktop hardware are now good enough for real agentic and tool-use workloads, which is what made sovereign deployment practical this year rather than aspirational.

Support: **4** talk(s)

> "a year ago this time a year ago we didn't have any local models that were able to successfully run within clo code"
>
> — [The Desktop Frontier](../talks/the-desktop-frontier.md), [2:43](https://www.youtube.com/watch?v=XV2oYi7kojc&t=163s)

Supporting talks: [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)

## Disagreements

### Does sovereignty require owning the hardware and weights, or can it be achieved cryptographically on infrastructure someone else operates?

| Position A | Position B |
|---|---|
| Sovereignty means physical and legal ownership: buy the GPUs, run open weights on your own hardware end to end, and control every step of the pipeline including evaluation compute. Rented endpoints structurally cannot give you reproducibility, audit standing, or rate-limit control.<br>*[The Desktop Frontier](../talks/the-desktop-frontier.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)* | Sovereignty is a property you engineer, not a place you host: keep keys on the customer device, encrypt with no opt-out, verify workloads via attestation and a transparency log, keep the trust base small enough to audit — or simply install the vendor's sandbox inside the customer's own VPC. You can run on (and inside) a hyperscaler and still make the operator unable to read the data.<br>*[Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* |

*Why it matters: One path costs capex, hardware ops, and inference-tuning headcount; the other costs cryptographic engineering and an organizational split of signing authority. Picking wrong means either buying racks you didn't need or shipping a guarantee auditors won't accept.*

### Should sovereign deployment replace frontier models, or only the execution tier beneath them?

| Position A | Position B |
|---|---|
| Move off the cloud entirely for the workloads that matter — open source AI only wins if enterprises stop subsidizing other people's data centers, and today's cheap tokens are subsidized prices that will disappear. Post-PMF, ownership is the only defensible position.<br>*[The Desktop Frontier](../talks/the-desktop-frontier.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)* | Keep the frontier model for top-level planning and push subtasks to smaller local or open models; most use cases never needed the biggest model. The sovereign boundary sits at the data and production-system edge, not at the model provider.<br>*[State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* |

*Why it matters: It decides whether you provision for peak local inference capacity or build a router with a hard data boundary, and whether losing access to a specific frontier model is an outage or an inconvenience.*

## Practical Guidance

**Do:**

- Ship the vendor's sandbox into the customer's own VPC instead of asking enterprises to route production systems to a third-party managed agent
- Own the traces, data, and telemetry flowing through your agent pipeline, and keep the harness, sandbox, and skills user-selectable rather than a black box
- Keep the security-critical code path small — Bee's is ~20k lines in a memory-safe language, mostly attestation verification — so full audit is actually feasible
- Split deployment authority: hardcode a separate privacy team's signing keys into clients and backends so nothing ships unnoticed
- Publish workload attestations to a transparency log (Sigstore) for third-party verification, but issue the certs from a private CA so you don't leak infrastructure into public transparency logs
- Force expiration on cloud-held in-memory keys at ~7 days — 24 hours breaks agents when a user doesn't open their phone
- Reuse trustworthy existing crypto rather than reintroducing your own
- On Grace Blackwell local hardware (DGX Spark), exhaust config tuning, vLLM backends, and quantization before touching kernels — EXO/NVIDIA got 10x in ~3 weeks with no new research
- Route by workload: frontier model for the plan, smaller local models for the subtasks
- Rent while pre-product-market-fit; own once the use case is validated or the enterprise project is budgeted
- Cut spend before cutting vendors: compress input tokens, fix routing and caching, keep context clean — Coinbase raised AI usage while lowering AI spend this way

**Avoid:**

- Building your software factory on a vendor-locked, single-model platform where the model provider dictates what you can build
- Assuming a rented inference endpoint will survive audit — a third-party vendor dependency getting redlined can stop a launch outright
- Prepaid credit-based inference billing with no periodic-bill anchor; it reads like casino chips and blows year-long budgets by month four
- Letting unencrypted data leave your perimeter, or shipping any encryption opt-out, disable switch, or bypass path
- Assuming the guarantees a cloud provider gives you as a customer still protect you once you're operating inside that provider
- Trying to tame agents behaviorally or granting them direct access to personal computers — only sandboxing and removing the means to cause harm work
- Betting your unit economics on today's subsidized cloud token prices persisting
- Leaving API keys exposed — one speaker watched a stolen key drain his endpoint from $7,000 upward in real time

## Notable Outliers

- Air-gap readiness is already a shipped property, not a roadmap item: 'you could run Droid in a submarine if you wanted to' — and it's literally true. ([How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [8:13](https://www.youtube.com/watch?v=wpOA-UXynoM&t=493s))
- Operating inside Amazon demands stronger privacy engineering than being an Amazon customer, because the customer-facing guarantee that Amazon can't see your data stops applying to you. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [10:06](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=606s))
- Export controls on frontier security-capable models should be lifted — the defender benefit outweighs the adversary risk, since distillation means adversaries already have capable models. ([The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [14:49](https://www.youtube.com/watch?v=7JgIS42mz7U&t=889s))
- Sovereign eval pipelines still pay a real throughput tax: local models like DS4 Flash don't support batch querying, so evaluations run serially on a machine in Tokyo. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [11:48](https://www.youtube.com/watch?v=R3-anFK1YM8&t=708s))
- Sovereign hardware appreciates: the RTX 3090, a 2020 architecture, still sells above MSRP because model efficiency gains make owned GPUs more valuable over time. ([The Desktop Frontier](../talks/the-desktop-frontier.md), [16:33](https://www.youtube.com/watch?v=XV2oYi7kojc&t=993s))
- Tightening down a general-purpose agent is the wrong trade today — restricting OpenClaw destroyed its usefulness; a narrowly sandboxed special-purpose agent is better. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [14:59](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=899s))

## All Talks

- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)
- [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)
- [Security Track Intro](../talks/security-track-intro.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)
- [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)
- [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)
- [The Desktop Frontier](../talks/the-desktop-frontier.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Alex Cheema](../speakers/alex-cheema.md)
- [Eno Reyes](../speakers/eno-reyes.md)
- [Jack Cable](../speakers/jack-cable.md)
- [Jason Lopatecki](../speakers/jason-lopatecki.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Stefania Druga](../speakers/stefania-druga.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)

