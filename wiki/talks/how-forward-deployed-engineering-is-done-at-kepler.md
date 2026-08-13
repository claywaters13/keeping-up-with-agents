---
title: "How Forward Deployed Engineering is done at Kepler"
type: "talk"
slug: "how-forward-deployed-engineering-is-done-at-kepler"
track: "Forward Deployed Engineering"
org: "Kepler"
day: "Day 2 — Session Day 1"
room: "Track 8"
video_id: "1OMHGsUZiqA"
duration_sec: 1340
word_count: 4041
speakers: ["Vinoo Ganesh"]
---

# How Forward Deployed Engineering is done at Kepler

**Speakers:** [Vinoo Ganesh](../speakers/vinoo-ganesh.md)

**Org:** Kepler

**Track:** Forward Deployed Engineering &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 22m 20s

[Watch on YouTube](https://www.youtube.com/watch?v=1OMHGsUZiqA)

## Summary

Vinoo Ganesh, who built Palantir's 'Project Frontline' FDE rotation program and later a similar function at Citadel, argues that forward deployed engineering is fundamentally a product strategy, not a go-to-market role. Drawing on four war stories from Palantir's early days (a Cassandra key-space disaster that needed 14TB of RAM, a 47-page requirements doc that collapsed into a 4-hour Slack alert, an engineer who blocked a Parquet migration because she couldn't double-click the files, and a Groovy hack that ran in production for years), he lays out four moves: detect the real problem and ship the real thing, observe behavior rather than trust stated preferences, define the ontology of nouns and verbs so customers adopt your language, and ship fast but build for production. The through-line is that FDEs earn access to real problems by solving small ones, then generalize those into product leverage — which is how Foundry itself got built. His closing warning is aimed at early-stage companies: treating FDEs as sales extensions is a luxury only a 20-year-old company with unlimited money can afford. Worth watching for anyone standing up an FDE function and deciding whether it reports into product or GTM.

## Key Points

- Forward deployed engineering should sit inside the product function as an extension of the product team, not inside go-to-market; Palantir's GTM framing came later, after Foundry already existed.
- Palantir's Phoenix storage product failed because it was designed in isolation — blank date values defaulted to the 1970 epoch, generating 2.3 million time-bucketed key spaces that would have required 14 terabytes of RAM to start under Cassandra.
- Customers describe solutions, not problems: a 47-page requirements doc for a 14-metric BI dashboard estimated at three months resolved into a Slack alert built in four hours once someone actually asked what the dispatcher does Monday morning.
- Observed behavior beats stated preference — an engineer opposed a Parquet migration for a year not on technical grounds but because Parquet had no double-click viewer; building a viewer overnight unblocked a migration that cut pipeline runtime from 17 hours to about two.
- Concrete tells of opportunity on site: any task repeated more than once, copy-pasting between tools, tab or tool switching, visceral 'well, I have to' exasperation, and users pulling out their phone mid-workflow.
- Enterprises fracture terminology across teams (customers vs. clients vs. billing entities vs. org IDs); building the ontology of nouns (entities) and verbs (operations) is what turns field work into durable product lock-in, since users who adopt your product adopt your language.
- Every hack ships to production and lives forever — 'this is just temporary' is the most dangerous phrase in engineering, so calibrate what you ship by asking whether you'll get a 2am call about it in six months and who owns it after you leave the site.
- Physical presence is non-negotiable: the site badge and contractor email address are the actual data-mining permits, and you cannot survey your way to the insights that only surface inside the customer's walls.

## Notable Quotes

> "the first fundamental truth of FTE is that this is not a role this is a product strategy how we discover the things to build are through the lens of forward deploy engineering"
>
> — [1:32](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=92s) &middot; *the thesis of the entire talk, stated outright*

> "an FTE is judged by their ability to be an extension of the product team to identify areas of opportunity and generalize product solutions out of it"
>
> — [2:23](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=143s) &middot; *gives a concrete evaluation criterion for the role, which is where most orgs get it wrong*

> "Phoenix was built totally in isolation. We didn't talk to customers. We didn't understand our financial banks or any anything else. What we did is we designed a system in perfect isolation that worked perfectly under certain circumstances and crashed and burned when we hit actual real data."
>
> — [2:57](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=177s) &middot; *the founding failure that motivated the FDE model*

> "The problem is Cassandra requires 5 megabytes per file handle, which means with the 2.3 million key spaces we generated to start up our server would require 14 terabytes of RAM and we were dead on arrival."
>
> — [3:35](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=215s) &middot; *hard numbers on how badly isolated design failed against real data*

> "The gap wasn't the fact that we had not looked for information about how customers use our product. It came from the ownership about co-building a piece of software without being directly embedded with a customer."
>
> — [4:17](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=257s) &middot; *distinguishes research from embedding, the talk's core distinction*

> "The whole thing could have been simplified to a trivial Slack alert, which is what we ended up building. In 4 hours, we were able to solve this problem cradle to grave."
>
> — [5:41](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=341s) &middot; *the 3-month-estimate-to-4-hours delta, the talk's most quotable case*

> "Customers describe solutions not problems. Your job as the FTE is to understand what the problem is. Customers don't know what happens next and your job as the FD is to define it."
>
> — [6:54](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=414s) &middot; *compact statement of the XY-problem framing*

> "if solving the problem is under a day of work, just build it and ship it and close the loop. Don't make it a product strategy. Don't expand your product vision and bring in your PMs and everything else."
>
> — [6:54](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=414s) &middot; *an actionable threshold rule that cuts against normal product process*

> "The secret here is whoever defines the problem actually owns the solution."
>
> — [6:54](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=414s) &middot; *the strategic logic behind why FDEs generate leverage*

> "this is why FDES actually become valuable in early sales. It's not because they are really good at talking to customers or we're not socially awkward software engineers as people seem to claim. It is because we actually solve the customer's problems in small bite-sized ways that wins us trust"
>
> — [7:31](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=451s) &middot; *directly rebuts the common characterization of FDEs as sales-adjacent*

> "That night we built a parquet viewer. She approved the migration in the next 2 days massively reducing data costs. I think the pipeline execution time went from 17 hours to about two."
>
> — [9:35](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=575s) &middot; *the payoff of on-site observation, with a measured result*

> "You earn the right to extract user pain and define product strategy by solving small repetitive problems."
>
> — [11:21](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=681s) &middot; *states the exchange rate between small fixes and product access*

> "Your badge on site at a customer site and your email address, your contractor email address, those are your data mining permits."
>
> — [11:21](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=681s) &middot; *vivid framing of why physical access is the real asset*

> "It's very easy to be a forward deployed engineer in name sitting in a nice conference room in New York, but that's not where the actual problems are and that's not where the solutions are."
>
> — [11:59](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=719s) &middot; *a pointed jab at nominal FDE programs*

> "Sales members calls them customers. Ops calls them clients. Finance calls them billing entities. Devs call them org IDs."
>
> — [12:33](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=753s) &middot; *the canonical example of enterprise terminology fracture*

> "In a lot of these enterprises, users don't just adopt your product, they actually adopt your language."
>
> — [14:00](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=840s) &middot; *the ontology argument in one line*

> "How many people are calling things skills right now? How many people are calling things MCPs that are function calls with prompts? And that matters."
>
> — [14:00](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=840s) &middot; *applies the ontology thesis to present-day AI vocabulary*

> "the secret here is if you become the linguistic foundation, you're locked in."
>
> — [15:20](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=920s) &middot; *names the moat that ontology work creates*

> "The most dangerous words in forward deployed engineering or engineering is this is just temporary."
>
> — [19:11](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=1151s) &middot; *the memorable warning behind the ship-for-production rule*

> "ship everything like it's going to run for 18 months because it probably will."
>
> — [19:11](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=1151s) &middot; *a specific, testable heuristic for calibrating hacks*

> "please don't treat FTEEs as go to market extensions. You can do that when you're palunteer and have 20 years and unlimited money. You don't do that when you're an early stage company"
>
> — [21:40](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=1300s) &middot; *the closing prescription, scoped explicitly to startups*

## Positions

- Forward deployed engineering is a product strategy and an extension of the product function, not a go-to-market role. ([4:17](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=257s), confidence: stated)
- Palantir's go-to-market framing of FDE came after the fact; the original purpose was product discovery for building Foundry. ([0:01](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=1s), confidence: stated)
- Customers systematically describe solutions rather than problems, so requirements documents should not be taken at face value. ([6:54](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=414s), confidence: stated)
- If a problem can be solved in under a day of work, an FDE should just build and ship it rather than routing it through product process. ([6:54](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=414s), confidence: stated)
- FDEs are valuable in early sales because they solve small problems and earn trust, not because they have superior social or communication skills. ([7:31](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=451s), confidence: stated)
- You cannot obtain the most valuable customer insights through surveys or documentation; physical presence on site is required. ([11:59](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=719s), confidence: stated)
- Terminology divergence across teams within an enterprise is a feature of how humans work, not a bug to be eliminated by forcing a single schema. ([13:16](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=796s), confidence: stated)
- Controlling an enterprise's vocabulary through your platform's ontology creates lock-in and makes you the foundation other tools build on. ([15:20](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=920s), confidence: stated)
- Any hack that solves a real problem will end up in production permanently and its author will be responsible for supporting it indefinitely. ([19:11](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=1151s), confidence: stated)
- Making customers successful is the job of solutions architects, not FDEs; an FDE who defines their job that way is failing at it. ([17:58](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=1078s), confidence: stated)
- Most organizations building an FDE function mistakenly run it as product management plus customer success, gathering insights without steering the product from them. ([19:49](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=1189s), confidence: stated)
- Early-stage companies specifically cannot afford to use FDEs as go-to-market extensions, even though a mature company like Palantir can. ([21:40](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=1300s), confidence: stated)
- Terms currently in wide use in AI engineering, such as 'skills', 'MCPs', and 'agents', are ill-defined and being contested in real time. ([14:38](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=878s), confidence: implied)

## Concepts

- [ai-generated code quality](../concepts/ai-generated-code-quality.md)
- [forward deployed engineering](../concepts/forward-deployed-engineering.md)
- [go-to-market for ai products](../concepts/go-to-market-for-ai-products.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [online evaluation](../concepts/online-evaluation.md)
- [ontology design](../concepts/ontology-design.md)
- [requirements elicitation](../concepts/requirements-elicitation.md)

