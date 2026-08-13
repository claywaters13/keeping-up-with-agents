---
title: "How Forward Deployed Engineering is done at Cognition"
type: "talk"
slug: "how-forward-deployed-engineering-is-done-at-cognition"
track: "Forward Deployed Engineering"
org: "Cognition"
day: "Day 2 — Session Day 1"
room: "Track 8"
video_id: "RVxym6mmIns"
duration_sec: 1058
word_count: 3534
speakers: ["Jia Wu"]
---

# How Forward Deployed Engineering is done at Cognition

**Speakers:** [Jia Wu](../speakers/jia-wu.md)

**Org:** Cognition

**Track:** Forward Deployed Engineering &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 17m 38s

[Watch on YouTube](https://www.youtube.com/watch?v=RVxym6mmIns)

## Summary

Jia Wu, a forward-deployed engineering lead at Cognition (the company behind Devin), explains how Cognition structures its FDE function and why that motion is what makes enterprise agent deployments actually deliver. The core argument is that writing code is now roughly a solved problem — only ~20% of the work — so the real value sits in testing, review, deployment, and maintenance across legacy enterprise codebases, and FDEs exist to map agent capabilities onto those specific high-leverage problems rather than 'token maxing.' The second half of the loop is bringing field signal back to product: Wu frames customer engagements as the company's highest-fidelity evaluation set and the mechanism for de-risking the roadmap. He closes with anonymized and named proof points (150%+ effective headcount over a 3-month embed, ~82% delivery-timeline compression, ~2x PR throughput, Nubank ETL migration, a LatAm bank COBOL/JCL tax-system migration, 10x weekly engineering output at Bolt). Worth watching if you're building or hiring an FDE function for an agent product, or want a view on how agent ROI gets measured in regulated enterprises.

## Key Points

- Cognition's forward-deployed motion is framed as maximizing the overlap between the product they build and the problems customers actually have — solving the customer's problem is only half the job, propagating feedback into the roadmap is the other half.
- Wu argues coding is mostly solved by current models given enough context engineering, and that writing code faster addresses only about 20% of the software engineering problem; testing, review, deployment, and maintenance are where the business value sits.
- Deploying agents without specific direction is 'token maxing' — burning spend without tangible outcomes — so FDEs first identify which strategic initiatives are highest leverage before setting up automation.
- The FDE job is roughly half customer conversation and half hands-on keyboard work; Wu describes days of four to five hours of calls plus four to five hours of building.
- Measuring ROI on agent deployments is explicitly called an unsolved problem, and Wu claims whoever solves it becomes a $5 trillion market cap company.
- Field engagements function as the highest-fidelity eval set the company has, feeding back questions like whether a challenge is enterprise-wide or user-specific and whether workarounds should become features.
- Cognition hires T-shaped FDEs — wide across people, business, process, and technology, with a deep spike — drawing from product management and founder/engineer backgrounds, on the theory that business sense is teachable but deep technicality is not.
- The differentiator claimed against CLI-only or IDE-only tools is organizational leverage: making the whole company 10x faster, including non-technical people, rather than just individual engineers.
- Proof points cited include ~150%+ added effective headcount over a 3-month embed, ~82% delivery-timeline compression, roughly double the PR volume versus single-point tools, and an internal near-order-of-magnitude PR increase over six months.

## Notable Quotes

> "Coding itself, at least from our perspective, is a mostly solved problem, right? These models are so good now that like with any type of context, with enough context engineering, you can get the code blocks that you really care about."
>
> — [4:08](https://www.youtube.com/watch?v=RVxym6mmIns&t=248s) &middot; *The talk's central premise about where engineering value has moved.*

> "But the problem isn't like writing code faster, that's usually only 20% of the problem. The problem really just becomes like how do you test this code? How do you review and deploy this code? And how do you maintain this code across the enterprise?"
>
> — [4:46](https://www.youtube.com/watch?v=RVxym6mmIns&t=286s) &middot; *Puts a number on the claim and names the actual bottleneck.*

> "So, if the software development life cycle is extremely complex, deploying the agents for with like no specific direction, you're straight up just token maxing."
>
> — [4:46](https://www.youtube.com/watch?v=RVxym6mmIns&t=286s) &middot; *Coins the talk's recurring anti-pattern for undirected agent deployment.*

> "my day might look like four or five hours of customer calls, and then four or five hours of like actual hands-on keyboard work"
>
> — [5:18](https://www.youtube.com/watch?v=RVxym6mmIns&t=318s) &middot; *Concrete shape of the FDE role, useful for anyone hiring for it.*

> "But most importantly, as forward deployed engineer, how do you measure the return on investment? And it's very ambiguous. And it's an unsolved problem because the company that will solve this will be um you know, $5 trillion market cap."
>
> — [5:18](https://www.youtube.com/watch?v=RVxym6mmIns&t=318s) &middot; *Rare admission that agent ROI measurement remains unsolved, from a vendor.*

> "We have the highest fidelity evaluation set that comes back from our customers, right? We are in the field every single day."
>
> — [7:08](https://www.youtube.com/watch?v=RVxym6mmIns&t=428s) &middot; *Frames field deployment as an eval mechanism, not just delivery.*

> "Because if the cost of software engineering is going to zero, you actually need to know how to like design a product that makes sense."
>
> — [8:50](https://www.youtube.com/watch?v=RVxym6mmIns&t=530s) &middot; *The hiring rationale for pulling FDEs from product backgrounds.*

> "It's fine if you don't have like the strongest business sense, that can be learned, but it's also very hard to teach like technicality and being the expert in the room while you're on the job."
>
> — [9:23](https://www.youtube.com/watch?v=RVxym6mmIns&t=563s) &middot; *A checkable hiring tradeoff others might dispute.*

> "the target or KPI for whatever deployed engineers were trying to do is maximize token usage, right? It was It was like the perfect time. Didn't have to worry about budgets. Everything was subsidized."
>
> — [10:32](https://www.youtube.com/watch?v=RVxym6mmIns&t=632s) &middot; *Describes the prior era of deployment incentives being replaced.*

> "You can make engineers like 10x faster. That's fine. That's still valuable. But can you make an organization 10x faster, including every single person that might be technical or non-technical uh across the company?"
>
> — [11:20](https://www.youtube.com/watch?v=RVxym6mmIns&t=680s) &middot; *The competitive positioning in one line.*

> "And that's why like single point tools that are just like CLIs or just IDEs, they fail to do that."
>
> — [11:20](https://www.youtube.com/watch?v=RVxym6mmIns&t=680s) &middot; *Direct swipe at the coding-assistant category; a clear side taken.*

> "one of these examples is a case study where we embedded ourselves within a customer for 3 months. We brought them on board. And functionally, over the course of those 3 months, we delivered about 150% like plus headcount."
>
> — [11:58](https://www.youtube.com/watch?v=RVxym6mmIns&t=718s) &middot; *First of the three headline metrics.*

> "So, about like 82% reduction across like delivery."
>
> — [12:32](https://www.youtube.com/watch?v=RVxym6mmIns&t=752s) &middot; *The delivery-timeline number, stated plainly.*

> "we deliver almost double the amount of PRs that engineers were able to do with single-point tools and before you brought in an agent harness like Devin"
>
> — [13:39](https://www.youtube.com/watch?v=RVxym6mmIns&t=819s) &middot; *Quantifies the claimed gap versus point tools.*

> "So, specifically, like we can say that there was an ETL migration. They had 50 engineers staffing this migration. We were able to deliver this within, um, I think like 1/3 of the timeline."
>
> — [14:15](https://www.youtube.com/watch?v=RVxym6mmIns&t=855s) &middot; *Named public reference (Nubank) with staffing and timeline detail.*

> "if you think about like legacy languages like COBOL, if you think about things like JCLs, you think about things that like people don't learn anymore just because it's like not fun and not interesting, we're able to operate across some of the most complicated codebases in the world"
>
> — [14:49](https://www.youtube.com/watch?v=RVxym6mmIns&t=889s) &middot; *Stakes out legacy migration as the differentiating use case.*

> "We deliver like 10x per sub like worth of engineering talent like every single week. And then we're actually able to, you know, generate the weekly output of like over 10 engineers at the organization."
>
> — [15:21](https://www.youtube.com/watch?v=RVxym6mmIns&t=921s) &middot; *The Bolt proof point, with a weekly-output framing.*

> "We've deployed somebody in Brazil for like 10 months."
>
> — [16:00](https://www.youtube.com/watch?v=RVxym6mmIns&t=960s) &middot; *Shows literally how far 'forward deployed' goes at Cognition.*

> "But, everybody is go-to-market because the target is to make the customer successful at all costs."
>
> — [16:38](https://www.youtube.com/watch?v=RVxym6mmIns&t=998s) &middot; *Resolves the recurring 'is FDE sales or engineering' ambiguity.*

> "over the last 6 months, for better or worse, we might have been behind on hiring, but using our agent, we were able to ship almost an order of magnitude more good quality robust PRs across the organization"
>
> — [1:50](https://www.youtube.com/watch?v=RVxym6mmIns&t=110s) &middot; *Internal dogfooding number that anchors the whole leverage argument.*

## Positions

- Coding itself is a mostly solved problem given sufficient context engineering; writing code faster addresses only about 20% of the software engineering problem. ([4:08](https://www.youtube.com/watch?v=RVxym6mmIns&t=248s), confidence: stated)
- Deploying agents without specific direction produces no tangible outcomes and merely burns tokens and spend. ([4:46](https://www.youtube.com/watch?v=RVxym6mmIns&t=286s), confidence: stated)
- Measuring the return on investment of agent deployments is currently an unsolved problem. ([5:18](https://www.youtube.com/watch?v=RVxym6mmIns&t=318s), confidence: stated)
- Customer field engagements are the company's highest-fidelity evaluation set for the product. ([7:08](https://www.youtube.com/watch?v=RVxym6mmIns&t=428s), confidence: stated)
- Business sense can be taught to a technically spiky hire, but deep technical expertise cannot be taught on the job. ([9:23](https://www.youtube.com/watch?v=RVxym6mmIns&t=563s), confidence: stated)
- Single-point tools such as standalone CLIs or IDEs cannot make an entire organization, including non-technical staff, 10x faster. ([11:20](https://www.youtube.com/watch?v=RVxym6mmIns&t=680s), confidence: stated)
- The KPI for deployed engineering has shifted from maximizing token usage to measurable delivery outcomes, driven by enterprises questioning whether they are getting real value. ([10:32](https://www.youtube.com/watch?v=RVxym6mmIns&t=632s), confidence: stated)
- A three-month customer embed delivered the equivalent of roughly 150%+ additional headcount. ([11:58](https://www.youtube.com/watch?v=RVxym6mmIns&t=718s), confidence: stated)
- Delivery timelines can be compressed by roughly 82% after deploying Devin. ([12:32](https://www.youtube.com/watch?v=RVxym6mmIns&t=752s), confidence: stated)
- Deploying an agent harness roughly doubles raw PR output compared to engineers using single-point tools. ([13:39](https://www.youtube.com/watch?v=RVxym6mmIns&t=819s), confidence: stated)
- Cognition's internal PR output rose almost an order of magnitude over six months by using its own agent, compensating for being behind on hiring. ([1:50](https://www.youtube.com/watch?v=RVxym6mmIns&t=110s), confidence: stated)
- Solving a customer's problem completely is only half the FDE's job; the other half is closing the feedback loop into product to de-risk the roadmap. ([6:27](https://www.youtube.com/watch?v=RVxym6mmIns&t=387s), confidence: stated)
- Because the cost of software engineering is trending toward zero, product design skill becomes the scarce and valuable capability. ([8:50](https://www.youtube.com/watch?v=RVxym6mmIns&t=530s), confidence: implied)
- Every role at the company, including forward deployed engineering, is effectively go-to-market. ([16:38](https://www.youtube.com/watch?v=RVxym6mmIns&t=998s), confidence: stated)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [context engineering](../concepts/context-engineering.md)
- [data flywheels](../concepts/data-flywheels.md)
- [developer productivity metrics](../concepts/developer-productivity-metrics.md)
- [forward deployed engineering](../concepts/forward-deployed-engineering.md)
- [legacy code migration](../concepts/legacy-code-migration.md)
- [roi measurement](../concepts/roi-measurement.md)

