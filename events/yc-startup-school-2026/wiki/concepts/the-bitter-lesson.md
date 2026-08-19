---
title: "the bitter lesson"
type: "concept"
slug: "the-bitter-lesson"
tier: "supporting"
maturity: "consolidating"
talk_count: 3
speaker_count: 3
---

# the bitter lesson

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **3** talk(s) by **3** speaker(s)

**Definition:** The argument that general methods which scale with compute beat hand-engineered structure, and the counter-pressure from data-efficient and distilled approaches.

*Also referred to as: algorithm domains, data-efficient learning, model distillation*

## State of Practice

Nobody at this conference argued against scale — the live argument is about what kind of hand-built structure survives it. The formulation that landed hardest was Waymo's: structure that fights scale loses, structure that channels scale wins, so you build the maximally learned, minimally constrained system and then add structure only where it buys you something scale cannot (inference-time safety validation, cheap evaluation, verifiable reward). Jeff Dean's TPU history is the same lesson told from hardware: the first TPU was deliberately built as a general linear-algebra machine rather than an over-specialized one, which is why it survived the arrival of transformers, and Huang frames NVIDIA's entire business as accelerating an algorithm domain rather than building chips. The counter-pressure is now concentrated in two places — distillation from a high-capacity teacher (Dean on Gemini Flash, Dolgov on onboard driving models) as the way to get small models with better scaling laws than training small directly, and data efficiency, where Dean notes frontier models see ~1000x the data a human sees by 18 and are still only on par. The binding constraint has shifted from model quality to measurement: Dean says any domain with a measurable objective is now amenable to rapid automated progress, Dolgov says evals and metrics are the moat and that building a realistic closed-loop simulator is as hard as building the agent, and Huang says robotics is gated on real-to-sim environments and grounded physics rather than on model capability.

## Consensus

### Bet on the maximally learned system and use hand-designed structure only where it channels scale — as an interface, constraint, or evaluation surface — never as a substitute for learning.

Support: **3** talk(s)

> "Essentially, structure that fights scale will always lose. And structure that channels scale always wins."
>
> — [The Demo Is Only 1% Of The Work](../talks/the-demo-is-only-1-of-the-work.md), [30:45](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=1845s)

Supporting talks: [The Demo Is Only 1% Of The Work](../talks/the-demo-is-only-1-of-the-work.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md)

### Evaluation, not architecture or data, is now the binding constraint: scaling only pays off in domains where you can measure the objective, and building the measurement apparatus is as hard as building the system.

Support: **3** talk(s)

> "that your model is really table stakes, but eval and metrics, that's your most important. That's your strategic moat."
>
> — [The Demo Is Only 1% Of The Work](../talks/the-demo-is-only-1-of-the-work.md), [42:42](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2562s)

Supporting talks: [The Demo Is Only 1% Of The Work](../talks/the-demo-is-only-1-of-the-work.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md)

### Hardware and system commitments must be made against where the algorithms are heading, not against today's algorithm or today's component prices — specialize only on the parts that have stopped moving.

Support: **3** talk(s)

> "it's not about building a great chip, it's about accelerating an algorithm domain"
>
> — [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md), [6:03](https://www.youtube.com/watch?v=I4B37S1dyQQ&t=363s)

Supporting talks: [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [The Demo Is Only 1% Of The Work](../talks/the-demo-is-only-1-of-the-work.md)

## Disagreements

### Will scaling general models absorb the long tail of a hard domain, or does each additional nine require a categorically different, hand-built approach?

| Position A | Position B |
|---|---|
| Capability sweeps forward with scale, so you should position ahead of it: pick problems where general models succeed 0-1% of the time (20% means the capability is already emerging and scale will take it), and expect useful systems well before full accuracy since agents at 80% plus human completion are already valuable.<br>*[The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md)* | Every AI breakthrough makes prototypes ~100x easier while barely improving the long tail; each further nine of reliability costs ~10x more effort and demands a fundamentally different technical approach, so the demo is at most 1% of the work and scale does not retire the remaining 99%.<br>*[The Demo Is Only 1% Of The Work](../talks/the-demo-is-only-1-of-the-work.md)* |

*Why it matters: It determines whether you spend your capital riding the next model release or building the closed-loop evaluation, redundancy, and long-tail engineering that a model release will not hand you.*

### How much domain data does a superhuman physical agent actually need once the model brings strong priors?

| Position A | Position B |
|---|---|
| Prior knowledge and reasoning collapse the data requirement — a couple million miles is enough for an incredibly good self-driving car — and more broadly, models already consume ~1000x the data a human sees by age 18 while remaining only on par, so far more data-efficient algorithms are available.<br>*[The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)* | At scale the long tail is the entire problem statement: a once-in-a-million-miles event is a daily occurrence, weak sensing produces a safety curve that flattens before strongly superhuman performance, and the credible claim rests on 220+ million fully autonomous miles.<br>*[The Demo Is Only 1% Of The Work](../talks/the-demo-is-only-1-of-the-work.md)* |

*Why it matters: It sets whether a physical-AI startup can be built on priors plus modest fleet data and cheap sensing, or whether the entry cost is hundreds of millions of real-world miles and redundant multi-modality sensing.*

## Practical Guidance

**Do:**

- Train a high-capacity foundation model and distill into the small deployed model rather than training the small model directly — the scaling laws are better (Dolgov on onboard driving models, Dean on Gemini Flash).
- Keep specialized hardware general enough to survive an algorithm shift: build linear-algebra machines, and reserve true specialization for stable properties like a small fixed set of very low inference precisions.
- Use inference-time compute to search over candidate solutions with an evaluator model instead of trying to fix behavior by adjusting model parameters.
- Steer general models from outside the weights — skills, hints, and guidelines in context — since information in the context window is far clearer to the model than knowledge absorbed into parameters.
- Build closed-loop simulation and metrics before the product; open-loop evaluation cannot score counterfactual actions.
- Choose structured intermediate representations where you need inference-time validation, cheaper training/eval, or verifiable reward signals — not as a way to hand-code behavior.
- Write the specification explicitly: agents cannot ask clarifying questions the way a colleague can, which is why cross-language code translation works so well (the source is an exhaustive spec).
- Pick problems where the general model succeeds 0-1% of the time, and when a narrow-domain advantage exists, check whether it is durable for years rather than months.

**Avoid:**

- Over-specializing hardware or systems to the current algorithm — the reason TPUs survived transformers is that they were not.
- Anchoring strategy to today's component prices; sensing and compute commoditize on a short shelf life.
- Building on a capability where general models already succeed ~20% of the time — that is the signal the capability is emerging and will be absorbed by the next scale step.
- Shipping vanilla black-box end-to-end models into safety-critical settings where you need superhuman performance and cannot validate an action before taking it.
- Adding redundancy by duplicating one sensing modality instead of combining modalities with complementary physics.
- Spending on the demo when you should be saving for the nines — every hype cycle produces spectacular demos and few products.
- Assuming a stack upgrade is worth it on capability gains alone; judge whether it simplifies and unifies the stack.

## Notable Outliers

- The right founder heuristic is inverted from intuition: target tasks where the model succeeds 0% or 1% of the time, because ~20% success means the capability is already emerging and scale will take it from you. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [28:01](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1681s))
- Chip design's 60-year assumption of near-perfect transistors is worth abandoning — build a system out of transistors that make ~20 errors per day and handle reliability at a higher level, as distributed storage does. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [37:38](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2258s))
- Moving data into the processor costs ~1000x more energy than computing on it, so batching is an energy-amortization artifact, not a modeling decision. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [12:47](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=767s))
- The distillation paper was rejected as unlikely to have significant impact, and is now a core reason Gemini Flash models are as capable as they are for their size and speed. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [48:50](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2930s))
- Coarse-grained recursive self-improvement already ships today — markdown files, long-term memory compaction, and knowledge graphs — and the missing piece is fine-grained controllability, not accuracy. ([The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md), [21:40](https://www.youtube.com/watch?v=I4B37S1dyQQ&t=1300s))
- Building a good end-to-end driving model has been relatively easy for a while; evaluating it in closed loop was the hard part, and a realistic simulator is as hard to build as the agent itself. ([The Demo Is Only 1% Of The Work](../talks/the-demo-is-only-1-of-the-work.md), [38:40](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2320s))

## All Talks

- [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)
- [The Demo Is Only 1% Of The Work](../talks/the-demo-is-only-1-of-the-work.md)
- [The Mindset That Built NVIDIA](../talks/the-mindset-that-built-nvidia.md)

## Speakers

- [Dmitri Dolgov](../speakers/dmitri-dolgov.md)
- [Jeff Dean](../speakers/jeff-dean.md)
- [Jensen Huang](../speakers/jensen-huang.md)

