---
title: "iteration speed"
type: "concept"
slug: "iteration-speed"
tier: "core"
maturity: "consolidating"
talk_count: 4
speaker_count: 4
---

# iteration speed

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **4** talk(s) by **4** speaker(s)

**Definition:** Shortening the build–measure–learn cycle — in software, hardware, design, or research — treated as the startup's primary competitive lever rather than an efficiency nicety.

*Also referred to as: iteration speed as competitive advantage, hardware iteration speed, design iteration, empirical model iteration, advanced manufacturing and tooling*

## State of Practice

Across software, hardware, and design, speakers treated cycle time as the single compounding variable that decides outcomes, and they were unusually concrete about where it actually comes from: not from hiring smarter people, but from owned infrastructure — a custom icon editor that renders hex codes straight to screen, an in-house machine shop and test stands, a purchasing process that doesn't stall a week to save half on a power supply. The dominant technical move in hardware is to stop treating engineering models as spreadsheets and rebuild them as real code with automated testing and CI, so that iteration in atoms starts to look like iteration in bits. On the AI side the framing inverted: cycle time is now limited less by the model than by the scaffolding teams wrap around it, so the recommended practice is a periodic delete-and-restore ablation of prompts, skills, and hooks on every model release, adding instructions back only after observing repeated failure. A second thread runs through every talk — accumulated expertise is a decelerator, because priors formed on last generation's constraints are the main reason people stop retrying things that would now work. Where speakers actually diverge is on the unit of iteration: drive the per-experiment cost toward zero and run many cheap sub-scale trials, versus integrate and iterate at the whole-product level because component-level wins don't compose. Nobody argued for slow.

## Consensus

### Iteration rate compounds and therefore dominates every other comparable advantage; when two approaches are otherwise equal, pick the one with the shorter cycle.

Support: **4** talk(s)

> "if you can learn one thing every week and there's a competitor that's learning a thing every month, they will they will never matter."
>
> — [Average Is Not Good Enough](../talks/average-is-not-good-enough.md), [18:44](https://www.youtube.com/watch?v=Xc4klGbq8v8&t=1124s)

Supporting talks: [Average Is Not Good Enough](../talks/average-is-not-good-enough.md), [How 50 People Built a Supersonic Jet](../talks/how-50-people-built-a-supersonic-jet.md), [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [Designing Icons & Graphics For the Original Mac](../talks/designing-icons-graphics-for-the-original-mac.md)

### Cycle time is set by tooling and operational infrastructure you own, not by team intelligence — so build the shop, the test stand, or the editor yourself rather than routing iterations through outside suppliers or commercial products.

Support: **3** talk(s)

> "It is mostly not that we are smarter. It is infrastructure like this."
>
> — [Average Is Not Good Enough](../talks/average-is-not-good-enough.md), [5:57](https://www.youtube.com/watch?v=Xc4klGbq8v8&t=357s)

Supporting talks: [Average Is Not Good Enough](../talks/average-is-not-good-enough.md), [How 50 People Built a Supersonic Jet](../talks/how-50-people-built-a-supersonic-jet.md), [Designing Icons & Graphics For the Original Mac](../talks/designing-icons-graphics-for-the-original-mac.md)

### Accumulated expertise and priors are a brake on iteration; the operative skill is discarding what you learned and retrying things that previously failed.

Support: **3** talk(s)

> "The moment you become an expert, what you're steeped in is the past and then you're completely useless."
>
> — [How 50 People Built a Supersonic Jet](../talks/how-50-people-built-a-supersonic-jet.md), [43:13](https://www.youtube.com/watch?v=byAj35QlGbs&t=2593s)

Supporting talks: [How 50 People Built a Supersonic Jet](../talks/how-50-people-built-a-supersonic-jet.md), [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [Average Is Not Good Enough](../talks/average-is-not-good-enough.md)

### Periodically deleting accumulated scope — instructions, features, prototype ambition — raises iteration throughput more than adding capability does.

Support: **3** talk(s)

> "for people that aren't building agentic products, but you're using Claude code, every 6 months delete your Claude MD. Delete your skills. Delete your hooks. See what the model does and it might surprise you."
>
> — [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [6:49](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=409s)

Supporting talks: [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [Designing Icons & Graphics For the Original Mac](../talks/designing-icons-graphics-for-the-original-mac.md), [How 50 People Built a Supersonic Jet](../talks/how-50-people-built-a-supersonic-jet.md)

## Disagreements

### Does iteration speed come from adding formal process and structure, or from stripping it away?

| Position A | Position B |
|---|---|
| Speed is a product of deliberate operating machinery: religiously-observed company rituals, a fixed four-stage hiring funnel treated as the irreducible minimum, eigenvector-weighted continuous peer review, and hardware models rebuilt as code with automated testing and continuous integration. Structure is what makes the cycle short.<br>*[Average Is Not Good Enough](../talks/average-is-not-good-enough.md), [How 50 People Built a Supersonic Jet](../talks/how-50-people-built-a-supersonic-jet.md)* | Accumulated structure is the thing slowing you down. Delete the whole system prompt and restore line by line; add an instruction only after observing repeated failure; skip the scaffolding entirely (no slash goal, no slash loop) in favor of a hard task plus a verification mechanism. The Mac icon editor had no shapes, no undo, and no eraser, and that was why it was fast.<br>*[We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [Designing Icons & Graphics For the Original Mac](../talks/designing-icons-graphics-for-the-original-mac.md)* |

*Why it matters: It determines whether a team's response to slow iteration is to build tooling and process or to audit and delete what it already has — opposite budgets and opposite headcount. Under the deletion view, the CI-and-process investment is itself the accumulated cruft that will need removing next generation.*

### Should you drive down the cost of the smallest possible experiment, or iterate end-to-end at the whole-product level?

| Position A | Position B |
|---|---|
| Attack per-experiment unit cost so experiments become effectively free — sub-scale trials where the only input is media out of the fridge, versus $40,000 per wafer iteration. Cheap units let you run many in parallel and learn weekly.<br>*[Average Is Not Good Enough](../talks/average-is-not-good-enough.md)* | Integrate and iterate at the product level. XB-1 failed as a strategy not because it was expensive but because it was too ambitious for one shot; a simpler whole prototype would have given multiple shots on goal in two to three years instead of ten. Equivalently, hand the model one hard end-to-end task with exit criteria rather than prescriptive step-by-step decomposition — an 11-day Zig-to-Rust runtime rewrite from a single prompt.<br>*[How 50 People Built a Supersonic Jet](../talks/how-50-people-built-a-supersonic-jet.md), [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)* |

*Why it matters: The two views allocate engineering effort in opposite directions: one toward cheap decomposed test rigs and per-component instrumentation, the other toward integration harnesses and self-verification so the full loop can run unattended. Choosing wrong means fast local iterations whose gains never compose, or slow whole-system loops you can only afford to run a few times.*

## Practical Guidance

**Do:**

- On every new model release, run a full ablation: delete the entire system prompt, skills, and hooks, then restore line by line to measure each line's contribution; for non-agentic users, do this to CLAUDE.md every six months.
- Add an instruction back to a system prompt only after observing the model fail at that same thing repeatedly — it is paid for on every single call.
- Give the model a mechanism to verify its own work (run the app in a VM, screenshot, compare pixel by pixel) rather than more detailed instructions — the verification loop is what sustains multi-day autonomous runs.
- Rewrite hardware engineering models that currently live in spreadsheets as real software with automated testing and continuous integration.
- Bring iteration-critical fabrication in-house — own machine shop and test stands — and accept the capital cost, because supplier turnaround sets your cycle time.
- Move spending review to the budgeting stage rather than per-purchase approval; waiting a week to get a power supply half off destroys more value than it saves.
- Design prototypes for multiple shots on goal rather than one maximally ambitious article — Boom's XB-1 cost ten years where a simpler aircraft would have proven the concept in two to three.
- Re-run tasks that failed on previous model generations against the newest model without changing anything else; treat the exercise as empirical, not theoretical.
- Present a powerful reviewer several options instead of one, so the review cycle terminates in a selection rather than a redo.
- Budget the experiments needed to reach the next value inflection point, raise twice that, and treat 20–30% waste as a good outcome.

**Avoid:**

- Writing highly prescriptive step-by-step instructions for modern models — describe the task, the guardrails, and the exit criteria instead; long-tenured engineers are the most prone to this failure mode.
- Treating evals as durable assets: they typically saturate within one to three model generations and must be thrown away.
- Assuming a slow team is an insufficiently smart team — check purchasing, recruiting, spending, and budgeting processes first, since that is where the latency actually lives.
- Buying commercial ERP/ATS-class software that forces its own bottlenecks into your workflow, now that agents make building internal equivalents viable.
- Expecting build-it-and-see-if-anyone-likes-it to yield product-market fit in capital-heavy hardware — that loop does not exist for a supersonic jet.
- Deferring an idea on 'why now' grounds; many multi-billion-dollar ideas were technically feasible years before anyone started them.
- Estimating creative work at an hour — nothing takes an hour — and scheduling the next iteration against that estimate.
- Adding detail to an artifact past the point of recognition: over-detailed icons pinned to a specific product design date faster and shorten the work's lifespan.
- Following 'one weird trick' prompt advice from LinkedIn and Twitter influencers.

## Notable Outliers

- In sub-scale biology, experiments are effectively free — the cost is media out of the fridge — while a single wafer iteration for the same protocol costs $40,000, so the entire discipline is choosing which regime to run your learning in. ([Average Is Not Good Enough](../talks/average-is-not-good-enough.md), [7:04](https://www.youtube.com/watch?v=Xc4klGbq8v8&t=424s))
- A single prompt with steering ran for 11 days and rewrote the Bun JavaScript runtime from Zig to Rust — work estimated at well over a year of engineer time — and that rewrite now runs in production Claude Code. ([We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [17:14](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1034s))
- The model is measurably slightly more intelligent with no system prompt at all; prompts exist to serve the product experience, not raw capability. ([We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [5:02](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=302s))
- Regulation is not a hard constraint on iteration — you change regulations by building the thing and explaining why it's safe, and making the regulators part of the team. ([How 50 People Built a Supersonic Jet](../talks/how-50-people-built-a-supersonic-jet.md), [10:52](https://www.youtube.com/watch?v=byAj35QlGbs&t=652s))
- Retail feedback loops can be minutes long: whether a digital good would be a bestseller was readable from unit sales in the first 15 minutes after launch. ([Designing Icons & Graphics For the Original Mac](../talks/designing-icons-graphics-for-the-original-mac.md), [32:01](https://www.youtube.com/watch?v=YEvLKzsEwMw&t=1921s))
- AI lowering the cost of writing software increased rather than decreased Boom's need for software engineers, because someone must keep architectures coherent when everyone can code. ([How 50 People Built a Supersonic Jet](../talks/how-50-people-built-a-supersonic-jet.md), [41:50](https://www.youtube.com/watch?v=byAj35QlGbs&t=2510s))

## All Talks

- [Average Is Not Good Enough](../talks/average-is-not-good-enough.md)
- [Designing Icons & Graphics For the Original Mac](../talks/designing-icons-graphics-for-the-original-mac.md)
- [How 50 People Built a Supersonic Jet](../talks/how-50-people-built-a-supersonic-jet.md)
- [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)

## Speakers

- [Blake Scholl](../speakers/blake-scholl.md)
- [Boris Cherny](../speakers/boris-cherny.md)
- [Max Hodak](../speakers/max-hodak.md)
- [Susan Kare](../speakers/susan-kare.md)

