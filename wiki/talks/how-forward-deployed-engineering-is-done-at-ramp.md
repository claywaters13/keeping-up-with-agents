---
title: "How Forward Deployed Engineering is done at Ramp"
type: "talk"
slug: "how-forward-deployed-engineering-is-done-at-ramp"
track: "Forward Deployed Engineering"
org: "Ramp"
day: "Day 2 — Session Day 1"
room: "Track 8"
video_id: "ITMXwI6QL6A"
duration_sec: 844
word_count: 2367
speakers: ["Leo Mehr"]
---

# How Forward Deployed Engineering is done at Ramp

**Speakers:** [Leo Mehr](../speakers/leo-mehr.md)

**Org:** Ramp

**Track:** Forward Deployed Engineering &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 14m 04s

[Watch on YouTube](https://www.youtube.com/watch?v=ITMXwI6QL6A)

## Summary

Leo Mehr, a director of engineering at Ramp, distills two years of building Ramp's forward-deployed engineering (FDE) org — from two engineers to ~30 — into two principles: 'always be scoping' and 'scale with tokens.' He argues FDE is not a technical go-to-market role but an engineering function that makes the core product and agentic features work for the largest enterprise customers, and that saying yes to every customer request produces bad software rather than happy customers. The scoping half is illustrated with concrete failures, including weeks spent shipping an Android reimbursement feature for a customer that mandates iOS company-wide. The second half describes decomposing the FDE lifecycle — context gathering, scoping, spec writing, implementation — into a pipeline of agents, with a working example: a Notion-agent intake bot on their #FDE-requests Slack channel that cut reply latency from days to seconds and roughly 20% of scoping time. Worth watching if you run a customer-facing engineering team and want a concrete, unhyped account of which stages of that work are already automatable and which are still 'gnarly.'

## Key Points

- FDE at Ramp sits inside the engineering organization rather than in go-to-market, with the mandate of helping Ramp win upmarket by making the core product and new agentic features work for the largest enterprise customers.
- The default FDE failure mode is reflexively saying yes to customer requests, which yields poorly-conceived software rather than customer success; the job is to find a way to say yes to the underlying need, not to the literal ask.
- Good scoping means interrogating the source of urgency — an end-of-quarter sales rep chasing quota is a different signal than a customer actually blocked — and exhausting workarounds, manual stopgaps, and API-based self-service before committing to a build.
- The highest-leverage scoping move is looking past the single request to the rest of the pipeline, checking whether other prospects and customers would benefit from the same feature.
- A painful early lesson: two FDEs learned iOS and Android development to ship a mobile reimbursement feature, only to discover after weeks of work that the customer mandated iOS devices for all employees — even trivial-seeming assumptions need validation up front.
- Every stage of the FDE lifecycle — context gathering, scoping, spec writing, implementation — is a candidate for agent replacement, and the problem becomes tractable once broken into those stages.
- Ramp's shipped example is an intake agent on the internal #FDE-requests Slack channel that runs multiple rounds of clarifying questions with the submitter until it judges the request ready for a spec; reply latency dropped from hours or days to seconds and roughly 20% of scoping time was saved.
- The pipeline's ends are the easy parts — intake is now automated and frontier models can one-shot medium-sized features from a well-shaped spec — while the middle stages remain unformed and hard.
- The remaining hard problems are applied AI problems: agent harness reliability, output quality via evals, rubrics and human feedback, and getting product-manager-grade tacit context into an agent when Notion docs and help articles only cover part of it.
- The two principles are complements, not alternatives: scoping without agent investment loses to agent-native competitors, while agent investment without scoping produces a 'token maxing slop cannon.'

## Notable Quotes

> "So, I would say there's this thing where like people many many people think that as an FDE, your job is to just say yes to the customer. But that's wrong."
>
> — [2:14](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=134s) &middot; *States the talk's central contrarian position on the FDE role.*

> "If you were just to say yes, you know, instead of like beautiful Waymos that we have driving us around in San Francisco, you'd have something like this, you know."
>
> — [2:14](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=134s) &middot; *The horses-with-rockets analogy that anchors his argument against pure customer deference.*

> "But you actually want to deliver good software. You need to build the right thing. So, you don't just endlessly say yes to people."
>
> — [2:55](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=175s) &middot; *Compresses the scoping principle into its operative form.*

> "So, it's Friday night and an enterprise sales rep comes to us with an urgent request that this super important strategic logo is only going to close if we build out an SAP S/4HANA integration."
>
> — [2:55](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=175s) &middot; *The concrete scenario the entire first half is reasoned against.*

> "I've seen sales reps who like go kind of crazy because it's like the end of the quarter and they're trying to hit their quota and close the deal and not because the customer is the one driving the urgency."
>
> — [3:48](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=228s) &middot; *Names a specific organizational incentive distortion FDEs must filter for.*

> "But, I'd say the most important thing that an FDE does is also looks beyond this one request and looks at the other prospects that are coming down the pipeline and other customers to see if anyone else would benefit from this as well."
>
> — [4:24](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=264s) &middot; *Identifies what he considers the single highest-value scoping behavior.*

> "And that's when they told us they only they they they require they mandate all of their employees to use iOS devices."
>
> — [5:07](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=307s) &middot; *The punchline of the failure story that justifies front-loaded scoping.*

> "Even some of the most basic assumptions like which you know mobile platform you build on it's it's super important um to validate them"
>
> — [5:51](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=351s) &middot; *The generalized lesson extracted from the Android incident.*

> "So, unless you are scaling with model capabilities, you are going to fall behind. Now, I'm not going to belabor this point too much."
>
> — [6:28](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=388s) &middot; *States the second principle as a competitive necessity.*

> "the point is that we basically have to reinvent our jobs constantly now. So, whatever work we are doing today, you know, for the most part it's knowledge work, we have to figure out how to have models and agents do it for us."
>
> — [6:28](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=388s) &middot; *Frames the automation mandate as continuous self-replacement of knowledge work.*

> "From gathering context to scoping out a request to writing out a spec and then implementing the feature, each stage of that pipeline can be replaced with agents."
>
> — [7:09](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=429s) &middot; *Defines the decomposition that makes the automation problem tractable.*

> "the latency of replies went from like hours or days to like, you know, seconds"
>
> — [9:10](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=550s) &middot; *Reports the concrete effect of the V1 intake agent.*

> "I I would say it's probably saved us like a large percentage, I don't know, 20% of the time that we'd spend on scoping out these requests."
>
> — [9:50](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=590s) &middot; *The talk's only quantified outcome, with its uncertainty stated.*

> "The last step as well, going from a a well-shaped spec to like a working product, obviously like Frontier models can like one-shot medium-size features."
>
> — [10:28](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=628s) &middot; *A claim about current model capability that others might contest.*

> "It's this middle part that I would say is super like gnarly and like unformed and difficult."
>
> — [10:28](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=628s) &middot; *Locates where the real unsolved work sits in the pipeline.*

> "Imagine like all the knowledge that a product manager has in their head about their product. Like, how do you get that into an agent?"
>
> — [11:55](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=715s) &middot; *Frames tacit context transfer as the core unsolved engineering problem.*

> "ultimately the most important thing here is that as an FD, we still have the responsibility of taste and judgment over the final output."
>
> — [11:55](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=715s) &middot; *Marks the boundary he draws around what stays human.*

> "If you don't do a good job of scoping out requests or or building upon the principles of scoping things well, you're going to get a token maxing slop cannon."
>
> — [12:37](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=757s) &middot; *The memorable formulation of why automation without scoping backfires.*

> "If you are, you know, amazing at scoping, but don't invest in building out this, you know, agent factory, you know, it's going to be over for you."
>
> — [12:37](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=757s) &middot; *Completes the symmetry argument that both principles are mandatory.*

> "Always be scoping and scaling with tokens. The future of FD needs both."
>
> — [13:19](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=799s) &middot; *The closing thesis in one line.*

## Positions

- FDE is not the final evolution of technical go-to-market roles; at Ramp it lives inside the engineering organization. ([0:52](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=52s), confidence: stated)
- An FDE's job is not to say yes to every customer request — doing so produces bad software rather than customer success. ([2:14](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=134s), confidence: stated)
- Urgency communicated by a sales rep often originates from quota pressure rather than from the customer, so FDEs must verify what is actually driving it. ([3:48](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=228s), confidence: stated)
- The most valuable scoping action is evaluating whether other prospects and customers in the pipeline would also benefit from the requested feature. ([4:24](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=264s), confidence: stated)
- Even basic assumptions such as which mobile platform a customer uses must be validated before building, or weeks of engineering effort can be wasted. ([5:51](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=351s), confidence: stated)
- Teams that do not scale with model capabilities will fall behind. ([6:28](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=388s), confidence: stated)
- Every stage of the FDE lifecycle — context gathering, scoping, spec writing, implementation — can be replaced with agents. ([7:09](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=429s), confidence: stated)
- Ramp's Notion-based intake agent reduced reply latency from hours or days to seconds and saved roughly 20% of the time spent scoping requests. ([9:50](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=590s), confidence: stated)
- Frontier models can one-shot medium-sized features from a well-shaped spec, making implementation one of the easier pipeline stages to automate. ([10:28](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=628s), confidence: stated)
- The middle stages of the FDE pipeline, between intake and implementation, are the hardest and least formed part of the automation problem. ([10:28](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=628s), confidence: stated)
- Existing knowledge bases such as Notion docs and help articles are insufficient to give an agent the context a product manager holds in their head. ([11:55](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=715s), confidence: stated)
- Humans retain responsibility for taste and judgment over the final output even in a fully agentic pipeline. ([11:55](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=715s), confidence: stated)
- Automating the pipeline without disciplined scoping produces high-volume low-quality output, while scoping discipline without agent investment loses to agent-native competitors. ([12:37](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=757s), confidence: stated)
- Building an agentic intake process improves internal stakeholder engagement, because account managers and reps began interacting with the agent immediately. ([9:10](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=550s), confidence: implied)

## Concepts

- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [cognitive debt](../concepts/cognitive-debt.md)
- [context engineering](../concepts/context-engineering.md)
- [forward deployed engineering](../concepts/forward-deployed-engineering.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [institutional knowledge capture](../concepts/institutional-knowledge-capture.md)
- [parallel agent execution](../concepts/parallel-agent-execution.md)
- [requirements elicitation](../concepts/requirements-elicitation.md)
- [spec-driven development](../concepts/spec-driven-development.md)

