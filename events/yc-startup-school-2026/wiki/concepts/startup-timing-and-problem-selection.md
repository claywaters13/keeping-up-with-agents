---
title: "startup timing and problem selection"
type: "concept"
slug: "startup-timing-and-problem-selection"
tier: "core"
maturity: "consolidating"
talk_count: 5
speaker_count: 5
---

# startup timing and problem selection

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **5** talk(s) by **5** speaker(s)

**Definition:** Choosing what to build and when, based on which technology shift has just made a previously impossible or unattractive problem viable.

*Also referred to as: startup timing and technology shifts, first-principles market timing, problem selection under model progress, launch timing, product overhang*

## State of Practice

The conference's operating assumption is that the AI capability jump has reset the opportunity landscape the way past platform shifts did, and that the correct response is to pick harder, more decorrelated problems rather than smaller ones. Collison reports new-business formation on Stripe up ~2x year-over-year — the largest relative jump Stripe has recorded, versus ~50% at the 2020 COVID inflection — with median business quality rising and Atlas time-to-revenue falling, which is the closest thing here to hard data on timing. The mechanism speakers name is not 'AI is magic' but that incumbents lose their advantages when cycle times shorten and cost falls (Altman), that a small team plus an agentic loop can cover work that previously required an organization (Wang, Cherny), and that this makes the old lean-startup path — find a narrow niche via ads, expand — both crowded and unnecessarily timid (Collison). On problem selection specifically, the sharpest heuristic offered is Dean's: probe candidate problems with the general model and prefer ones where it succeeds 0-1% of the time, because ~20% means the capability is emerging and will be absorbed by the next scale-up; the durable advantages he names are private data, a purpose-built surface, or an AlphaFold-shaped narrow model. The unresolved question underneath everything is what you time against — Wang argues the binding constraint is diffusion, not model progress, and that a frozen frontier still implies decades of upheaval, while Altman, Dean, and Cherny each price in continued rapid capability gains as a design input.

## Consensus

### The current moment is unusually favorable for founding, because the technology shift has stripped incumbents of structural advantages rather than because capital or attention is cheap.

Support: **3** talk(s)

> "the great startups tend to cluster when the ecosystem shifts and incumbents lose a lot of their advantage"
>
> — [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [10:22](https://www.youtube.com/watch?v=ZIaOBAjvc38&t=622s)

Supporting talks: [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [Is AI Breaking the Lean Startup Playbook?](../talks/is-ai-breaking-the-lean-startup-playbook.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)

### Pick a problem you can hold contrarian conviction on and that decorrelates from what everyone else is building; consensus ideas raise easily and rarely produce the large outcome.

Support: **3** talk(s)

> "if you're starting the same startup as everybody else, it's like you get a lot of hype and you can raise a lot of money, but it's it's sort of like those are much less frequently the big option, the big outcomes"
>
> — [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [13:42](https://www.youtube.com/watch?v=ZIaOBAjvc38&t=822s)

Supporting talks: [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Is AI Breaking the Lean Startup Playbook?](../talks/is-ai-breaking-the-lean-startup-playbook.md)

### AI has lowered the cost of standing up broad capability, so founders should start at full ambition rather than starting narrow and expanding — the capital constraint that made lean-startup optimal no longer binds.

Support: **3** talk(s)

> "whereas now I think you can start these much more aggressive and ambitious things up front"
>
> — [Is AI Breaking the Lean Startup Playbook?](../talks/is-ai-breaking-the-lean-startup-playbook.md), [18:30](https://www.youtube.com/watch?v=5d6y3poKwK4&t=1110s)

Supporting talks: [Is AI Breaking the Lean Startup Playbook?](../talks/is-ai-breaking-the-lean-startup-playbook.md), [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)

### As intelligence and execution get cheap, the binding constraint moves to problem selection itself — taste about what to point capability at, not the capability.

Support: **3** talk(s)

> "a researcher can have all the tools and all the techniques, but often most of the battle is what problem are you gonna spend your time on?"
>
> — [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [33:57](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2037s)

Supporting talks: [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md)

### Today's already-shipped models support products nobody has built yet; a large share of the opportunity requires no further model progress, only eliciting capability the product layer currently hobbles.

Support: **3** talk(s)

> "the model is able to do all sorts of things with today's models, not a future model, but today's model, that we have not yet realized."
>
> — [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [10:56](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=656s)

Supporting talks: [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)

## Disagreements

### Should you time your company against continued rapid model progress, or against the diffusion gap in capability that already exists?

| Position A | Position B |
|---|---|
| Assume the frontier keeps moving fast and make that an explicit design input: the next six months will feel like the last two years (Altman), automated ML self-improvement lands around 2027 (Dean), evals saturate within one to three generations and most of your system prompt is obsolete each release, so keep re-throwing the newest model at the task (Cherny).<br>*[Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)* | Treat further model progress as roughly irrelevant to your plan: the bottleneck is diffusing existing capability through the economy, arguing about superintelligence timelines is a waste of time, and even a frozen frontier implies decades of upheaval to build into.<br>*[This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)* |

*Why it matters: It decides whether your roadmap is a bet on next year's model unlocking your product, or a bet on distribution, workflow, and go-to-market into industries that have not adopted what already ships. The two produce different hiring, different burn profiles, and different answers to 'what happens when the labs release the next model.'*

### Should you build where general models currently fail almost completely, or where they already work but no product has captured it?

| Position A | Position B |
|---|---|
| Probe with the general model and pick problems it solves 0-1% of the time; ~20% success means the capability is emerging and will be absorbed by the next scale-up, so any advantage there is measured in months. Durability has to come from private data, a purpose-built surface, or a narrow trained model.<br>*[The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)* | The money is in product overhang — capability the models already have that products fail to elicit. Startups are not capturing it, and the fix is better task framing and verification loops, not waiting for a capability the model lacks.<br>*[We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)* |

*Why it matters: The two heuristics point at disjoint idea sets: one filters out anything a frontier model can partially do today, the other targets exactly that zone. Choosing wrong means either building something the next release obviates, or passing on the categories that are shippable now.*

### Does a long pre-consensus period without users validate an ambitious idea, or is it the failure mode?

| Position A | Position B |
|---|---|
| Being dismissed and obscure for years is a positive signal — it deterred serious competitors and bought OpenAI research time (Altman); successful companies are started long before their core idea is consensus and founders must toil in obscurity (Wang).<br>*[Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)* | A long pre-launch is acceptable only with a continuous stream of real production users — Stripe waited two years to launch but had a paying customer at two months and added customers every month; outside heavily regulated infrastructure, waiting two years is the wrong call, and ideas grounded in imagined customer problems are the failure mode.<br>*[Is AI Breaking the Lean Startup Playbook?](../talks/is-ai-breaking-the-lean-startup-playbook.md)* |

*Why it matters: It determines what counts as evidence during the years before traction. Under one reading, silence from the market is confirmation; under the other, it is the signal that you are extrapolating from your own hypothesized picture of the world instead of learning from reality.*

## Practical Guidance

**Do:**

- Probe candidate ideas against the current general model first: prefer problems where it succeeds 0% or 1% of the time, and treat ~20% success as a warning that the capability is emerging.
- Before committing to a narrow-domain advantage (custom surface, targeted skills, specialized model), explicitly ask whether the gap over general models is durable for years rather than months.
- Anchor the idea in a customer problem you have viscerally felt, not one you inferred — Collison credits this with keeping Stripe survivable through the unglamorous years.
- If you plan a long pre-launch, keep a continuous stream of real production users throughout (Stripe: paying customer at month two, launch at year two).
- Look for access to data the general model cannot see — a user's own personal information is the canonical example — as the basis of a durable product advantage.
- Ask the success-case question before raising significant money: if this works, do you want to do this specific work for 10, 17, or 30 years?
- Apply Dean's outcome filter: if the best possible outcome happens, is the world meaningfully better, or does it get an 'eh, that's kind of cool'?
- Pick the exponential with both the steepest curve and the longest runway, even if its starting point currently looks boring (Wang).
- Train taste deliberately: write down what you think will matter in 12 months, then go back and grade which predictions came true.
- Sanity-check contrarianism in both directions — if literally nobody shares your belief, that is evidence you are wrong; if everybody agrees, that is also a bad sign.
- On every new model release, run a full ablation: delete the system prompt and tools, then restore line by line to see what still earns its place. Non-builders should delete CLAUDE.md, skills, and hooks every six months and watch what happens.
- Give the model a way to verify its own work (run it, screenshot it, compare pixel by pixel, don't stop until done) rather than prescribing steps — this is what enables multi-day autonomous runs.

**Avoid:**

- Starting the same company as everyone else because it fundraises easily — hype correlates poorly with the big outcome.
- The classic lean path of finding a small niche via ads and expanding from it; speakers describe this lane as increasingly crowded and competitive.
- Building on an imagined customer problem — the extrapolated conception of reality rather than what you learn from it.
- Assuming the frontier labs will crush you by competing directly; large organizations cannot aggressively prosecute 100 priorities at once (a distinct risk from raw capability gains obviating your vertical, which is real).
- Treating evals as long-lived assets — they typically survive one to three model generations before saturating and being discarded.
- Adding instructions to a system prompt preemptively; only add one back after observing the model repeatedly fail the same way, because it is read on every call.
- Over-specifying tasks with prescriptive step-by-step instructions — the most common failure mode among engineers with years or decades of experience, and worse than high-level task plus guardrails plus exit criteria.
- Concluding a task is impossible because a previous model generation failed at it; re-run it on the latest model before writing it off.
- Basing decisions on what the herd is saying — going too far with consensus leaves you confused and nowhere.
- Going all in on verbal/language skills at the expense of quantitative and systems thinking, which survives every shift in abstraction layer.

## Notable Outliers

- Probe with the general model and pick problems it fails at almost entirely — ~20% success is a bad sign, not encouragement, because it means the capability is arriving on its own. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [28:01](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1681s))
- New businesses started on Stripe are up around 2x year-over-year, the largest relative jump Stripe has recorded, versus roughly 50% during the 2020 COVID inflection — and median business quality is up, not down. ([Is AI Breaking the Lean Startup Playbook?](../talks/is-ai-breaking-the-lean-startup-playbook.md), [25:12](https://www.youtube.com/watch?v=5d6y3poKwK4&t=1512s))
- Startup growth is accelerating primarily because incumbents now perceive the risk of the status quo as higher than the risk of buying from an unproven vendor. ([Is AI Breaking the Lean Startup Playbook?](../talks/is-ai-breaking-the-lean-startup-playbook.md), [27:57](https://www.youtube.com/watch?v=5d6y3poKwK4&t=1677s))
- Scale's original idea — an AI agent for getting medical care — was right but mistimed, and is only viable now; being early on the right idea is a distinct failure from being wrong. ([This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [3:32](https://www.youtube.com/watch?v=sJ4VJWycX9M&t=212s))
- Being publicly dismissed for years was net-positive for OpenAI: it deterred serious competitors and bought research time. ([Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [12:58](https://www.youtube.com/watch?v=ZIaOBAjvc38&t=778s))
- A single dynamic workflow rewrote the Bun JavaScript runtime from Zig to Rust in 11 days from one prompt with steering — and previous model generations could not do it even with steering, marking a datable capability threshold. ([We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [17:14](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1034s))

## All Talks

- [Is AI Breaking the Lean Startup Playbook?](../talks/is-ai-breaking-the-lean-startup-playbook.md)
- [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md)
- [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)
- [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)
- [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)

## Speakers

- [Alexandr Wang](../speakers/alexandr-wang.md)
- [Boris Cherny](../speakers/boris-cherny.md)
- [Jeff Dean](../speakers/jeff-dean.md)
- [Patrick Collison](../speakers/patrick-collison.md)
- [Sam Altman](../speakers/sam-altman.md)

