---
title: "Forward Deployed Engineering 101"
type: "talk"
slug: "forward-deployed-engineering-101"
track: "Forward Deployed Engineering"
org: "Anthropic, ex Palantir & Rippling Founding FDE"
day: "Day 2 — Session Day 1"
room: "Track 8"
video_id: "KwhgfwOSToQ"
duration_sec: 1068
word_count: 3203
speakers: ["Kevin Bai"]
---

# Forward Deployed Engineering 101

**Speakers:** [Kevin Bai](../speakers/kevin-bai.md)

**Org:** Anthropic, ex Palantir & Rippling Founding FDE

**Track:** Forward Deployed Engineering &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 17m 48s

[Watch on YouTube](https://www.youtube.com/watch?v=KwhgfwOSToQ)

## Summary

Kevin Bai, a member of technical staff on Anthropic's applied AI team who previously built Rippling's forward-deployed engineering (FDE) function and worked at Palantir, gives a primer on what FDE actually is and when it applies. His core framework is a quadrant of what you sell versus who buys it: FDE is only the right go-to-market motion in the narrow case where you must sell something highly technical to a non-technical buyer, as Palantir did with Foundry into the Fortune 500. He argues FDE is a design partnership scaled into enterprise, and that the non-negotiable prerequisite is an underlying platform of shared primitives — without it you have a dev shop whose maintenance costs will consume you. He supports the model with ACV numbers (Palantir ~$4M vs. ServiceNow $1.2M vs. Workday ~$600K) and closes with the claim that agentic AI has made nearly every platform customizable, pushing far more companies into the quadrant where FDE matters. Worth watching if you're deciding whether to stand up an FDE team or are selling an agentic platform into non-technical buyers.

## Key Points

- FDE exists to solve one specific quadrant problem: selling a highly technical product to a non-technical buyer, where the customer lacks the engineering depth to extract value on their own.
- If your buyer is technical (GitHub, Datadog selling to CTOs and engineers) or your product is simple and configurable (Slack, Jira, Rippling), you do not need FDE — devrel or a sales-led motion fits better.
- The model reframes the transaction: the customer buys neither software nor hours of someone's time, but an outcome, which shifts the conversation away from implementation details like how data is organized.
- FDE is a design partnership — normally a startup's pre-product-market-fit tactic — deliberately scaled up and run at enterprise scale, which was Palantir's core assertion.
- The essential prerequisite is a platform of shared primitives; if every FDE builds from scratch you have a dev shop, not an FDE function, and maintenance costs will destroy your P&L.
- Bai offers ACV as evidence the model works: Palantir at roughly $4M average contract value, ServiceNow at $1.2M, Workday at ~$600K, with no other public SaaS company cracking half a million.
- How atomic primitives should be depends on the industry — some domains support apps that ship 60% built with 40% customization, others need extremely granular tooling; AWS with DynamoDB is the reference example of broad primitives for a broad customer base.
- Bespoke customer work should stay scoped to that customer, but anything generalizable should be generalized over time, and early FDE work doubles as scouting for what belongs in the platform.
- Bai's hypothesis for FDE's 2026 resurgence is not that the world discovered Palantir was right, but that nearly every platform is now agentic and therefore customizable, so customers no longer understand what the product does.
- The hiring profile is simple: an FDE is a customer-facing software engineer — someone you'd hire onto your engineering team but also trust in front of a customer.

## Notable Quotes

> "instead of selling just services or just products, you sell both. Um, so it's one combined thing where the customer is neither buying a piece of software nor are they buying the time of someone. They are buying an outcome"
>
> — [2:59](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=179s) &middot; *The central reframing of what an FDE engagement sells.*

> "You only need FTE if you are in this weird unique situation of Palunteer where you are having to sell something very technical to a non-technical buyer."
>
> — [4:59](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=299s) &middot; *The talk's one-sentence qualifying criterion for the whole model.*

> "we will loan you some really good engineers that you don't have to hire, recruit, manage or retain"
>
> — [5:42](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=342s) &middot; *Names the concrete value exchange to an enterprise buyer without in-house engineering depth.*

> "Balance is first at 4 million uh last I checked."
>
> — [6:54](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=414s) &middot; *The headline ACV number (transcription of 'Palantir') anchoring the model's business case.*

> "Next biggest is Service Now at 1.2. Next biggest I want to say is workday at 600K. And then there is not a single public SAS company that even cracks half a million ACV."
>
> — [6:54](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=414s) &middot; *The comparative benchmark that makes the ACV claim checkable.*

> "FDE is basically taking this concept of a design partnership and scaling it up into enterprise."
>
> — [7:36](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=456s) &middot; *The cleanest definition of the model in the talk.*

> "who said who said that design partnerships were only for the beginning stages of a company. Why can you not just do that at scale at enterprise?"
>
> — [7:36](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=456s) &middot; *States Palantir's contrarian founding assertion as a challenge to conventional GTM wisdom.*

> "If you were to implement an FTE function where each FTE is building entirely from scratch, my friends, you do not have an FTE function. You have a dev shop."
>
> — [8:12](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=492s) &middot; *The sharpest line in the talk and its central warning.*

> "the thing that makes an FTE program different is that they are building on top of a platform. They are never writing software from scratch."
>
> — [8:40](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=520s) &middot; *States the non-negotiable structural prerequisite.*

> "before you know it your P&L will eat you alive from the maintenance costs um if your engineers don't all quit first."
>
> — [8:40](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=520s) &middot; *Names the concrete failure mode of platformless FDE.*

> "really ask yourselves, do I need an FTE function? Like, do I need one? Not want, right? It's easy to want things that are in vogue."
>
> — [9:17](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=557s) &middot; *The talk's main piece of prescriptive advice, framed against hype-driven adoption.*

> "There's a lot of great things you could do uh with Devril and building a great developer engagement uh team if you're having a technical go to market motion. There's a lot of great things you can do with an SLG salesled motion if you're doing more traditional SAS."
>
> — [9:59](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=599s) &middot; *Names the alternatives, showing FDE is deliberately scoped rather than universal.*

> "do I have a platform or phrased another way am I willing to invest in building one"
>
> — [10:37](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=637s) &middot; *The second of the two gating questions for adopting FDE.*

> "the thing which has changed is that the nature of doing business in the software industry itself is what's changed because now nearly every platform is agentic. And that means nearly every platform is customizable."
>
> — [11:54](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=714s) &middot; *The speaker's explicit hypothesis for why FDE is suddenly relevant in 2026.*

> "nearly all of you are going to have a situation where your customers have no idea what the heck it is that you actually do."
>
> — [11:54](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=714s) &middot; *Extends the non-technical-buyer condition to almost every agentic product company.*

> "Where the app itself is like 60% built and then people are just customizing the other 40%."
>
> — [14:00](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=840s) &middot; *The only quantitative guidance offered on how atomic primitives should be.*

> "anything that's bespoke and unique to a particular customer um is uh something that should really only exist for that one customer. Anything that can be generalizable should be generalized in the long term."
>
> — [16:10](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=970s) &middot; *The governing rule for what graduates from FDE work into the platform.*

> "FD is also a great way to scout ahead and to find what additional product services you can build upon to further enable the success of your business."
>
> — [16:10](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=970s) &middot; *Frames FDE as product discovery, not just delivery.*

> "a FTE is nothing more than a customerfacing software engineer."
>
> — [16:50](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=1010s) &middot; *The closing tagline and the hiring bar in one line.*

## Positions

- FDE is only the right model when you must sell a highly technical product to a non-technical buyer; in the other three quadrants of the what-you-sell/who-buys matrix it is the wrong fit. ([4:59](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=299s), confidence: stated)
- An FDE function without an underlying platform of shared primitives is not an FDE function but a dev shop, and its maintenance costs will destroy the business. ([8:12](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=492s), confidence: stated)
- Palantir has the highest ACV of any public SaaS company in the Fortune 500 at about $4M, ahead of ServiceNow at $1.2M and Workday at about $600K, with no other public SaaS company above $500K. ([6:54](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=414s), confidence: stated)
- Design partnerships, conventionally an early-stage startup tactic, can be scaled into enterprise — this was Palantir's core bet. ([7:36](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=456s), confidence: stated)
- The reason FDE matters now is not that the industry recognized Palantir's model was good, but that agentic platforms are inherently customizable, which puts most software companies into the technical-product/non-technical-buyer situation. ([11:54](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=714s), confidence: stated)
- Leaving product success to the customer's own ability to implement will make it hard to sell up market or expand horizontally or vertically. ([12:33](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=753s), confidence: stated)
- Multiple FDEs should staff a single customer project, because a single-person engagement creates a single point of failure. ([14:35](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=875s), confidence: stated)
- The correct granularity of platform primitives is industry-dependent, not a universal design choice — some spaces tolerate 60%-prebuilt apps while others require extremely granular configuration. ([14:00](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=840s), confidence: stated)
- The right hiring bar for an FDE is someone you would hire as a software engineer on your team and also trust in front of a customer — no separate skill profile is needed. ([16:50](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=1010s), confidence: stated)
- Foundry's app-building platform is inherently less interesting to large tech companies because they have engineers who can build whatever apps they need in-house. ([4:59](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=299s), confidence: stated)
- Selling technology alone fails with enterprise buyers because organized data does not by itself answer what it does for the business. ([2:18](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=138s), confidence: implied)
- Software engineers are among the last people who should be customer-facing, which is what makes the FDE idea counterintuitive. ([3:47](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=227s), confidence: stated)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [build versus buy](../concepts/build-versus-buy.md)
- [forward deployed engineering](../concepts/forward-deployed-engineering.md)
- [go-to-market for ai products](../concepts/go-to-market-for-ai-products.md)

