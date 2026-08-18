---
title: "How Forward Deployed Engineering is done at Decagon"
type: "talk"
slug: "how-forward-deployed-engineering-is-done-at-decagon"
track: "Forward Deployed Engineering"
org: "Decagon"
day: "Day 2 — Session Day 1"
room: "Track 8"
video_id: "7wu2hsRfvV0"
duration_sec: 1088
word_count: 3356
speakers: ["Sunny Rekhi"]
---

# How Forward Deployed Engineering is done at Decagon

**Speakers:** [Sunny Rekhi](../speakers/sunny-rekhi.md)

**Org:** Decagon

**Track:** Forward Deployed Engineering &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 18m 08s

[Watch on YouTube](https://www.youtube.com/watch?v=7wu2hsRfvV0)

## Summary

Sunny Rekhi, CTO of Forward Deployed Engineering at Decagon (an AI customer-service agent company), explains how Decagon's forward deployed motion works and how it was restructured as the company went from 50 to 500 people in a year. His central structural claim is that forward deployed engineering and product engineering are the same job at Decagon — same bar, same reporting structure, often the same people — because a Fortune 20 pain point is usually a product feature in disguise. He argues the newly scarce skill, now that AI coding makes one-off customization nearly free, is restraint: refusing to prompt Codex or Claude Code into a bespoke patch and instead architecting each customer ask so the next four customers benefit. Practical advice covers pinning down success metrics in writing before building, staffing vertical-specific industry experts so knowledge compounds across similar logos, proving value fast rather than boiling the ocean, and systematically converting custom work into self-serve product (their 25th custom CRM integration became a self-serve builder). Worth watching if you run or work in a deployment/solutions org at an agent company and want a concrete account of the custom-to-product funnel.

## Key Points

- Decagon splits forward deployment into two motions: configuring the customer-facing agent brain (tone, intents, handoff rules, backend actions) and acting as the front line that routes customer product asks back into the core platform.
- Forward deployed engineering at Decagon is organizationally identical to product engineering — same hiring bar, same reporting structure, often the same team — because the historical line between the two has blurred.
- As headcount went from 50 to 500 in a year, the generalist 'agent software engineer' role was split into two specialized lanes: agent builders who live in the UI and have model intuition, and agent software engineers who upstream customer asks into the product.
- Because AI coding tools make one-off customization cheap, the scarce skill is now restraint — declining to ship a brittle black box of prompts and patches for a single important customer.
- Deals should start with an explicit, ideally written definition of success (metrics, channels, pain points) because AI coding has shifted engineering effort toward up-front requirements gathering.
- Staffing vertical-specific industry experts across similar customers compounds knowledge, buys credibility through shared lingo, and makes each deployment faster than the last.
- Enterprises will present the entire kitchen sink; the counter-move is to demonstrate value ASAP on a narrow slice, then expand into broader support and revenue-generating workflows over a multi-year partnership.
- Forward deployed people should act as advisors, not just executors — Decagon ingests customers' historical support data and tells them which workflows to automate first for highest ROI, sometimes contradicting what the customer originally asked for.
- The guiding ethos is 'custom becomes self-serve': after roughly 25 hand-built CRM-style integrations, Decagon built a self-serve integration path so customers or agent builders could do what previously required engineer-written custom code.

## Notable Quotes

> "But the scarce skill now that AI coding is so good, the scarce skill is actually exercising restraint."
>
> — [7:38](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=458s) &middot; *The talk's sharpest thesis about how AI coding changes the FDE job.*

> "at Decagon, forward deployment engineering is identical to product engineering. Uh it's the same bar, it's the same reporting structure, uh often like the same team"
>
> — [5:01](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=301s) &middot; *States the org-design position most directly, and one many companies structure the opposite way.*

> "And this happens with stunning regularity. So, I want to make sure when I solve enterprise A's problem, I'm solving it for B, C, D, and E before they've even had a chance to express it."
>
> — [4:18](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=258s) &middot; *Names the generalization heuristic that drives the rest of the talk.*

> "we build agents to be owned by the customer and so if it turns into a black box of like prompts and patches and that's not good for us or them. It's far too brittle."
>
> — [8:21](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=501s) &middot; *Gives the product rationale, not just the engineering one, for refusing one-off hacks.*

> "Uh early on in our history, we were actually like building custom integrations time and time again. And then we thought enough is enough. After like the 25th one"
>
> — [12:09](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=729s) &middot; *Concrete number attached to the custom-to-self-serve turning point.*

> "And now what took an engineer custom code writing can now be self-served by the customer or built by our agent building team."
>
> — [12:09](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=729s) &middot; *Describes the payoff of productizing custom work in operational terms.*

> "Every time at Akkio gone, someone has to do something manually, we try to make sure it gets upstream back into the product."
>
> — [14:42](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=882s) &middot; *The reusable mental model the speaker recommends to the audience.*

> "you're you should treat yourself as an advisor rather than just an executor, right?"
>
> — [13:19](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=799s) &middot; *Core role definition the speaker returns to twice.*

> "what we do at Akkio gone is we actually ingest your historical support data uh and we tell customers that hey, like if you automate this first or this first, this is where actually you'll see the highest ROI."
>
> — [14:05](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=845s) &middot; *Makes the advisor claim concrete and checkable rather than aspirational.*

> "but now there's a lot of effort that has to go up front in requirements gathering, making sure you're aligned on what actually has to get built uh before before going to do it."
>
> — [9:36](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=576s) &middot; *Claims AI coding shifted engineering effort toward specification, a contestable position.*

> "you want to figure out ahead of time what does success look like for the customer. And really narrowing that down, ideally getting it in writing so that there is like no miscommunication along the way."
>
> — [8:56](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=536s) &middot; *Specific, actionable process advice for deal scoping.*

> "we have found it's really helpful to have industry experts that get staffed, the same kind of deal."
>
> — [10:19](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=619s) &middot; *Names the vertical-specialization staffing model.*

> "We try to figure out how do we demonstrate value ASAP and not have like a multi-month deal or sorry, multi-month uh time to prove value."
>
> — [12:37](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=757s) &middot; *States the time-to-value tradeoff against enterprise scope creep.*

> "uh Deckagon's ethos is you should be able to configure this agent completely via natural language."
>
> — [11:34](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=694s) &middot; *Product principle that determines what counts as a defect in their deployment process.*

> "And effectively we we we broke apart this agent software engineering role into two specialized lanes."
>
> — [7:03](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=423s) &middot; *The pivotal org change caused by 10x headcount growth.*

> "Degagon is is an example of sort of canonical hypergrowth. A year ago we were at 50 people."
>
> — [5:40](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=340s) &middot; *The growth number that contextualizes every structural decision in the talk.*

> "And I think one is we're known in the industry to move really really fast on customer asks."
>
> — [15:59](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=959s) &middot; *Speaker's own account of what made the company competitive.*

> "making sure the agent compounds every single time it interfaces with the customer. So, if the agent interfaces with customer A, you improve that for customer B."
>
> — [16:36](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=996s) &middot; *Summarizes the compounding-knowledge design goal in one line.*

> "we land in our customers to help them with the kinds of complex support workflows that today have to go to humans"
>
> — [1:27](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=87s) &middot; *Defines the land-and-expand wedge the whole FDE motion is built around.*

## Positions

- Forward deployed engineering and product engineering should be the same role, with the same hiring bar and reporting structure, rather than separate organizations. ([5:01](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=301s), confidence: stated)
- Now that AI coding tools are good, the scarce engineering skill is restraint — not building the fast one-off solution. ([7:38](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=458s), confidence: stated)
- An agent built as a pile of customer-specific prompts and patches is too brittle and bad for both vendor and customer. ([8:21](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=501s), confidence: stated)
- Enterprise product asks recur across customers with high regularity, so every customer-specific solution should be architected for the next four customers. ([4:18](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=258s), confidence: stated)
- AI coding has shifted engineering effort toward up-front requirements gathering and alignment rather than starting to build immediately. ([9:36](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=576s), confidence: stated)
- Success metrics and channels should be agreed in writing during the earliest deal conversations. ([8:56](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=536s), confidence: stated)
- Staffing the same industry-expert group across customers in a vertical produces faster ramp-up and more credibility than generalist staffing. ([10:19](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=619s), confidence: stated)
- In enterprise deployments you should deliberately narrow initial scope to prove value fast, then expand, rather than accepting the full kitchen-sink scope. ([12:37](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=757s), confidence: stated)
- Forward deployed people accumulate cross-customer domain expertise that makes them advisors, and this expertise is routinely underrated. ([14:42](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=882s), confidence: stated)
- Any task a Decagon engineer has to do manually is a signal that a product capability is missing and should be upstreamed. ([14:42](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=882s), confidence: stated)
- Building custom integrations one at a time does not scale; after about 25 of them a self-serve path was the correct investment. ([12:09](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=729s), confidence: stated)
- Decagon's speed on customer asks, advisor positioning, and productization of custom work are the three reasons it won its market position. ([15:59](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=959s), confidence: stated)
- The kind of forward deployment required differs substantially by enterprise size and by vertical. ([2:52](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=172s), confidence: stated)
- Companies at 500 people must design the deployment system itself, whereas at 50 people ad hoc knowledge sharing was sufficient. ([16:36](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=996s), confidence: implied)

## Concepts

- [agent configuration files](../concepts/agent-configuration-files.md)
- [build versus buy](../concepts/build-versus-buy.md)
- [forward deployed engineering](../concepts/forward-deployed-engineering.md)
- [go-to-market for ai products](../concepts/go-to-market-for-ai-products.md)
- [requirements elicitation](../concepts/requirements-elicitation.md)
- [roi measurement](../concepts/roi-measurement.md)
- [rubric design](../concepts/rubric-design.md)

