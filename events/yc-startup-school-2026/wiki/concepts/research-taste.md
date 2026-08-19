---
title: "research taste"
type: "concept"
slug: "research-taste"
tier: "supporting"
maturity: "consolidating"
talk_count: 4
speaker_count: 4
---

# research taste

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **4** talk(s) by **4** speaker(s)

**Definition:** The judgment that decides which experiments and problems are worth pursuing, and the operating model a lab or founder builds around that judgment.

*Also referred to as: frontier lab operating model, systems thinking, latent versus deterministic computation*

## State of Practice

Across these four talks the field converged on a single premise: model access is no longer the differentiator, so the binding input is judgment about what to point capability at. Jeff Dean states it flatly — a researcher has all the tools, and most of the battle is which problem to spend time on — and adds that models are not necessarily going to be good at this, making taste the scarce human skill. Garry Tan makes the same argument from the operator side: 2x and 100x people run the same weights, cloud, context window and API, so leverage lives in context selection and timing. Alexandr Wang extends it to company strategy — intelligence and agency become abundant, vision and ambition become scarce — and reframes frontier AI work as scientific research requiring a research operating model, not an internet-product one. The operational answer everyone reaches for is the same: externalize judgment into written artifacts — skill files, markdown, specs, performance hints, evals — because that is the only interface through which taste reaches an agent. Where they diverge sharply is on aim: Dean says target problems where today's models succeed 0–1% and treat 20% as a warning sign, while Wang, Huang and Tan point founders at the enormous diffusion gap in what models already do well.

## Consensus

### Problem selection, not tooling or model access, is the scarce input — taste about what to work on is now the differentiating skill.

Support: **4** talk(s)

> "a researcher can have all the tools and all the techniques, but often most of the battle is what problem are you gonna spend your time on?"
>
> — [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [33:57](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2037s)

Supporting talks: [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md)

### Judgment only becomes leverage once it is written down as an executable artifact — skill files, markdown, hints, specs, or an eval an agent loop optimizes.

Support: **4** talk(s)

> "if you can develop the right agentic loop and you have the right eval or the right metric for the agents to optimize, you can have a swarm of agents accomplish more than like a team of 100 engineers"
>
> — [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [27:47](https://www.youtube.com/watch?v=sJ4VJWycX9M&t=1667s)

Supporting talks: [Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)

### Correct problem choice starts from a non-consensus conviction held before the market agrees, and survives being wrong on the initial technical bet.

Support: **3** talk(s)

> "you need to develop conviction in a set of beliefs that nobody else um agrees with."
>
> — [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [6:53](https://www.youtube.com/watch?v=sJ4VJWycX9M&t=413s)

Supporting talks: [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)

### Model capability is commoditizing, so durable advantage moves to accumulated context, ambition, and problem framing rather than to weights or compute access.

Support: **3** talk(s)

> "The better the models get, the more the differentiator moves to context. When everyone's engine is a thousand horsepower, the race is won on the driver and the map."
>
> — [Own Your Intelligence](../talks/own-your-intelligence.md), [33:18](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1998s)

Supporting talks: [Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md)

## Disagreements

### Should founders aim at problems current models fail at almost entirely, or at deploying what models already do well?

| Position A | Position B |
|---|---|
| Pick problems where general models succeed 0% or 1% of the time; ~20% success means the capability is already emerging and will be absorbed by the next scaling step, so check whether the gap is durable for years rather than months.<br>*[The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)* | The bottleneck is diffusion, not capability — if models froze today there would still be decades of upheaval, so the highest-value work is building products and tools on top of what already works, including tools built for an audience of one and domain-specific AI any company can now train.<br>*[This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Own Your Intelligence](../talks/own-your-intelligence.md), [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md)* |

*Why it matters: It decides whether a team spends its scarce judgment hunting capability gaps that survive the next model release, or racing on distribution and workflow in territory the frontier labs will keep improving underneath them. The two strategies produce opposite reactions to a demo that half-works.*

### What is the actual constraint on AI's near-term impact — remaining model capability, or getting existing capability into the world?

| Position A | Position B |
|---|---|
| Diffusion. Model progress is no longer the limiting factor; the work is pushing existing capability through the economy, and debating when superintelligence arrives is largely a waste of time.<br>*[This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)* | Capability. Fine-grained controllability is the single biggest breakthrough agents still need, and agents fail past step 10 because they drift off their training distribution — with data efficiency and automated research loops still to come.<br>*[The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)* |

*Why it matters: If diffusion is the constraint, research taste means picking underserved domains and shipping. If controllability and off-distribution failure are the constraint, the same taste should be spent on harness design, skills, and eval infrastructure that keep agents on the well-lit path.*

## Practical Guidance

**Do:**

- Train taste explicitly: write down what you think will matter in 12 months, then go back and grade which predictions came true (the-1-rule-for-building-in-ai, 2123).
- Before committing, ask whether the best possible outcome of the project would make the world materially better or just draw an 'that's kind of cool but whatever' (the-1-rule-for-building-in-ai, 3160).
- Screen candidate problems by current model success rate: 0–1% is the target zone; treat partial success as evidence the capability is arriving on its own.
- Extract your own process into skill files / markdown you own and version, rather than leaving it as tacit knowledge — the artifact is what an agent can actually execute.
- Use inference-time search with an evaluator model over candidate solutions in long-running agent flows, instead of trying to fix reliability by adjusting model parameters.
- Optimize for discoveries per unit of compute when designing a research loop, not for raw experiment count.
- Write the specification as if for an agent that cannot ask clarifying questions — spec quality has gone up in importance, not down.
- Let the team pick their own AI coding tools during rapid change and learn from the spread, rather than standardizing early (the-mindset-that-built-nvidia, 1497).
- Hire for talent density and low-ego complementary skills; both Dean and Wang treat team composition as part of the research operating model, not a separate HR concern.

**Avoid:**

- Chasing capabilities where models already succeed ~20% of the time — that gap is closing without you.
- Accumulating an uncurated knowledge base: 'a brain nobody curates is a garbage dump with great search' and a bad skill file encodes a bad process forever.
- Putting into latent space what belongs in deterministic code (and vice versa) — Tan attributes every agent failure he has seen to this confusion.
- Running a frontier-AI effort on internet-product operating assumptions; Wang argues it is scientific research and needs a different mindset.
- Over-specializing infrastructure to the current algorithm — TPUs survived transformers because they were built as general linear-algebra machines while ML was still evolving.
- Basing decisions on what everyone around you is saying; herd-following produces confusion and ends nowhere.
- Going all-in on verbal/prompting skill at the expense of quantitative and systems thinking, which survives every shift in abstraction layer.
- Assuming a narrow-domain advantage over general models is permanent — verify it is durable for years, not months.

## Notable Outliers

- Taste is trainable as a deliberate practice: write down what you believe will matter in 12 months, then grade yourself later on which predictions came true. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [35:23](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2123s))
- A 20% model success rate is a worse founding signal than a 0% one, because partial competence means the capability is already emerging. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [28:01](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1681s))
- NVIDIA's founding technical bet was simply wrong, and the company survived by admitting it in 1995 and relearning graphics from textbooks — judgment is a recovery discipline, not a prediction record. ([The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md), [1:17](https://www.youtube.com/watch?v=I4B37S1dyQQ&t=77s))
- Scale's original idea — an AI agent for getting medical care — was right but mistimed, and only becomes viable now; taste includes timing, not just problem choice. ([This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [3:32](https://www.youtube.com/watch?v=sJ4VJWycX9M&t=212s))
- The personal-context flywheel only catches around week four and pays off around week twelve, which is why most people quit in week two. ([Own Your Intelligence](../talks/own-your-intelligence.md), [28:32](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1712s))
- Chip design's 60-year assumption of near-perfect transistors is itself worth questioning — reliability could be handled at a higher level, as distributed storage systems already do. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [37:38](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2258s))
- The distillation paper was rejected as unlikely to have significant impact, and now underpins Gemini Flash — peer judgment about what matters is demonstrably unreliable. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [48:50](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2930s))

## All Talks

- [Own Your Intelligence](../talks/own-your-intelligence.md)
- [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)
- [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md)
- [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)

## Speakers

- [Alexandr Wang](../speakers/alexandr-wang.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Jeff Dean](../speakers/jeff-dean.md)
- [Jensen Huang](../speakers/jensen-huang.md)

