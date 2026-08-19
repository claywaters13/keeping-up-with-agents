---
title: "small team leverage"
type: "concept"
slug: "small-team-leverage"
tier: "supporting"
maturity: "consolidating"
talk_count: 4
speaker_count: 4
---

# small team leverage

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **4** talk(s) by **4** speaker(s)

**Definition:** Deliberately keeping headcount low and raising output per person — via AI tooling, talent density, and decision structures that survive without consensus — as a company-design choice.

*Also referred to as: agent-augmented small teams, revenue per employee, team size and consensus decision-making, talent density*

## State of Practice

As of this conference the belief is no longer that small teams can compete despite their size — it is that headcount has become a weak predictor of output, and revenue-per-person figures with no historical analogue (Emergent at $15M ARR with 15 people, Retail at $60M with ~40) are cited as existence proofs rather than curiosities. The mechanism speakers point to is not model access, which is commoditized: every operator has the same weights, context window, and API, so the spread between a 2x and a 100x person is attributed to accumulated context, task selection, and timing. The practical unit of leverage described is mundane and inspectable — markdown skill files, a browser the agent can drive, cron jobs, and an eval or metric the loop optimizes against — with the explicit claim that a correctly specified agentic loop can outproduce a team of 100 engineers. Failure modes are equally concrete: uncurated context ('a garbage dump with great search'), and putting work in latent space that belonged in deterministic code. The unresolved question is whether this makes hiring obsolete or merely raises the bar — the same conference argues both that team, funding, and permission were workarounds for human working-memory limits, and that talent density is the thing that compounds and is worth betting a lab on.

## Consensus

### The differentiator has moved off the model and onto accumulated context and direction — the same weights and APIs produce order-of-magnitude different output depending on who is driving.

Support: **3** talk(s)

> "There are 2X people and there are 100X people who are using the same cloud, same weights, same context window size, same API, but the leverage is not in the weights."
>
> — [Own Your Intelligence](../talks/own-your-intelligence.md), [9:59](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=599s)

Supporting talks: [Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md)

### Small teams that adopt agents now reach output and revenue levels that previously required large organizations, inverting the usual startup-versus-incumbent asymmetry.

Support: **3** talk(s)

> "Emergent out of our summer 24 batch went from public launch to nine figures of revenue in eight months. When they crossed $15 million in annualized revenue, they were 15 people."
>
> — [Own Your Intelligence](../talks/own-your-intelligence.md), [22:20](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1340s)

Supporting talks: [Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md)

### Operating without consensus — internal or external — is treated as a prerequisite for the outsized outcome, not a risk to be managed down.

Support: **3** talk(s)

> "you can't base your business decisions based on what everyone else is saying around you. Like, if you go too much with the herd, you will get immensely confused and you will end up nowhere."
>
> — [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [7:30](https://www.youtube.com/watch?v=sJ4VJWycX9M&t=450s)

Supporting talks: [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Own Your Intelligence](../talks/own-your-intelligence.md)

## Disagreements

### Is the binding constraint on what a small team can achieve still model capability, or is capability already ahead of anyone's ability to deploy it?

| Position A | Position B |
|---|---|
| Capability is the live variable and is still accelerating hard — the next six months will feel like the last two years of progress, and inference demand grows ~10x/year against a compute shortage that effectively never ends, so plan around a moving frontier.<br>*[Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md)* | Model progress is no longer the bottleneck; diffusion and context are. If models froze today there would still be decades of economic upheaval, and model quality is rented while the durable asset is the curated context you own.<br>*[This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Own Your Intelligence](../talks/own-your-intelligence.md)* |

*Why it matters: It determines whether a small team should spend its scarce cycles building durable context, skill files, and distribution — which compound — or staying loosely coupled and rewriting against each new model generation.*

### Does small-team leverage come from removing the need for people, or from concentrating a very small number of exceptional ones?

| Position A | Position B |
|---|---|
| The prerequisites — team, funding, permission, credentials — were workarounds for human working-memory and time limits that agents have removed; the leverage now lives in agentic loops, skill files, and cron jobs, and a correctly specified loop can outproduce 100 engineers.<br>*[Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)* | The bet is still on people: talent density compounds because talented people attract more talented people, co-founder relationships come from years of being broadly helpful, and geography (the Bay Area) still matters for finding them.<br>*[Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [Designing Icons & Graphics For the Original Mac](../talks/designing-icons-graphics-for-the-original-mac.md)* |

*Why it matters: It decides where a founder's first year goes — into recruiting and relationship-building, or into building the personal context library and agent harness — and whether headcount growth is a signal of health or of failure to automate.*

## Practical Guidance

**Do:**

- Keep your process in skill files in a repo you control from day one — markdown that encodes how you do the thing, executable by an agent — rather than in your head or only in an employer's codebase.
- Split work explicitly: taste, judgment, and reading vague human intent go in latent space steered by a markdown file; anything that must be deterministic goes in code.
- Start from the metric or eval the agent loop is optimizing, then assemble the loop from skills, markdown files, and cron jobs.
- Use the smart-intern test to decide what to delegate: if a smart intern could execute it from written instructions, an agent can run it.
- Budget roughly four weeks before the personal-agent flywheel catches and twelve before it pays off — the dropout point is week two.
- Curate the context library actively; retrieval is the easy primitive, being worth retrieving from is the work.
- Keep consensus decision-making (everyone in a room, consensus hiring) only up to about 15 people, and change the structure past that.
- When getting a decision from a strong-opinioned principal, present several options rather than one, so they can reject and still select.
- Sanity-check a contrarian bet by finding at least a few people who share it — total inability to find anyone is evidence you are wrong, and universal agreement is also a bad sign.

**Avoid:**

- Treating model access, weights, or API tier as the source of advantage — they are the commoditized part.
- Assuming compressed wall-clock output equals compressed work: 'you can now do three months of work in 17 minutes, but you better just go do three months of work in three months of work.'
- Letting context accumulate uncurated — a stale fact gets surfaced with total confidence, and a bad skill file encodes a bad process forever.
- Building the same startup as everyone else: it raises money and generates hype but rarely produces the large outcome.
- Going all in on verbal/prompting skill at the expense of quantitative and systems thinking, which survives every shift in abstraction layer.
- Relying on a subscription chatbot as your memory — it resets, knows only what everyone else knows, and improves on the vendor's schedule, not yours.
- Running contests with multiple paid finalists to source creative work.
- Estimating creative work optimistically — nothing takes an hour.

## Notable Outliers

- A correctly designed agentic loop with the right eval can accomplish more than a team of 100 engineers, and building it is mechanically mundane: pick the metric, then use skills, markdown files, and cron jobs. ([This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [27:47](https://www.youtube.com/watch?v=sJ4VJWycX9M&t=1667s))
- Personal code output is roughly 400x a 2013 baseline of ~14 useful lines a day, with an 8x floor even under the most pathological verbosity discount. ([Own Your Intelligence](../talks/own-your-intelligence.md), [8:39](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=519s))
- Knowledge workers were protected because their tools lived in their heads; skill files end that protection — if you don't own your skills, your job becomes a skill file executing without your name in the commit history. ([Own Your Intelligence](../talks/own-your-intelligence.md), [31:26](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1886s))
- Consensus hiring with everyone in one room stays workable up to about 15 people and degrades beyond that. ([Designing Icons & Graphics For the Original Mac](../talks/designing-icons-graphics-for-the-original-mac.md), [47:59](https://www.youtube.com/watch?v=YEvLKzsEwMw&t=2879s))
- Being publicly dismissed for years was net-positive because it deterred serious competitors and bought research time. ([Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md), [12:58](https://www.youtube.com/watch?v=ZIaOBAjvc38&t=778s))
- The old advice to scratch your own itch and hope it's a market should be replaced by building tools for an audience of one, some of which become companies when others ask to borrow them. ([Own Your Intelligence](../talks/own-your-intelligence.md), [23:05](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1385s))

## All Talks

- [Designing Icons & Graphics For the Original Mac](../talks/designing-icons-graphics-for-the-original-mac.md)
- [Never a Better Time to Do a Startup](../talks/never-a-better-time-to-do-a-startup.md)
- [Own Your Intelligence](../talks/own-your-intelligence.md)
- [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)

## Speakers

- [Alexandr Wang](../speakers/alexandr-wang.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Sam Altman](../speakers/sam-altman.md)
- [Susan Kare](../speakers/susan-kare.md)

