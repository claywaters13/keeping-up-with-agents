---
title: "AI tools for Forward Deployed Engineering"
type: "talk"
slug: "ai-tools-for-forward-deployed-engineering"
track: "Forward Deployed Engineering"
org: "Varick Agents"
day: "Day 2 — Session Day 1"
room: "Track 8"
video_id: "l0FLhNqBOic"
duration_sec: 1222
word_count: 3884
speakers: ["Vasuman Moza"]
---

# AI tools for Forward Deployed Engineering

**Speakers:** [Vasuman Moza](../speakers/vasuman-moza.md)

**Org:** Varick Agents

**Track:** Forward Deployed Engineering &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 20m 22s

[Watch on YouTube](https://www.youtube.com/watch?v=l0FLhNqBOic)

## Summary

Vasuman Moza (CEO) and JD Pruitt (head of engineering) of Varick Agents argue that AI has solved the execution of knowledge work, so the remaining bottleneck is understanding a specific business well enough to redesign its processes around AI — the job of the forward deployed engineer. The first half lays out the FDE role (map how humans actually work including failure paths, re-engineer the process around AI, and deploy agents on top of existing systems of record like NetSuite, SAP, and Salesforce rather than asking enterprises to migrate), and argues that department-wide transformation delivers 25–75% ROI versus 5–10% for point solutions. The second half is a technical walkthrough of their internal 'FDE agent': a dependency-graph representation of a company's processes, a post-trained open-source model that writes consultant-style analysis (because frontier models are too verbose and miss what the client cares about), and an RL environment that trains custom tools for traversing that knowledge graph, e.g. entity resolution across the many 'Mikes' in a company. Watch it for the enterprise-services perspective on why AI pilots fail and for a concrete, if brisk, architecture for tooling that scales FDE headcount sublinearly. It is partly a hiring and sales pitch, and the ROI numbers are asserted without methodology.

## Key Points

- The speaker claims execution is no longer the constraint — models and harnesses can complete end-to-end tasks — so the new bottleneck is understanding and re-engineering how a specific business actually works.
- Forward deployed engineers do three things: map how humans do the work today (especially the exception paths, not the documented golden path), redesign the process around AI, and deploy agents on top of existing systems.
- Most enterprise AI fails because AI is bolted onto broken processes; the talk cites the MIT figure that 95% of generative AI pilots fail to reach production and a similar 87% statistic on measurable ROI.
- Redesigned workflows must be different enough to capture ROI but familiar enough to be adopted — the example given is a process where some steps go fully autonomous, some keep a human in the loop, and at least one stays fully human because of risk.
- Enterprises are married to their systems of record (one client reportedly spent $5M and 5 years migrating to NetSuite), so Varick builds agents on top of Salesforce/NetSuite/Dynamics/SAP rather than requiring migration.
- Point solutions deliver roughly 5–10% ROI in one function, while department-wide transformation is claimed to deliver 25–75%, framed as revenue uplift, cost savings, and risk mitigation.
- The FDE agent has three stages: an engagement agent that synthesizes notes and documents for FDEs, a workflow agent embedded in the platform that flags missed edge cases while a workflow is being built, and a not-yet-built autonomous agent that ships small workflow changes from client emails.
- Technically, they represent company processes as a dependency graph, post-train open-source models (they mention Kimi) because frontier models are too verbose and can't distinguish what a client cares about, and use an RL environment to train custom graph-traversal tools including entity resolution.

## Notable Quotes

> "So, clearly execution is no longer the core bottleneck. The models are improving to the point where intelligence is no longer the constraint"
>
> — [1:24](https://www.youtube.com/watch?v=l0FLhNqBOic&t=84s) &middot; *states the talk's core premise in one line*

> "The difference and the bottleneck that is still here is how much can you understand the business? Because every business, every consumer is different."
>
> — [1:24](https://www.youtube.com/watch?v=l0FLhNqBOic&t=84s) &middot; *names the thesis bottleneck explicitly*

> "There's a lot of, you know, semi-outdated, but still very relevant statistics like the MIT review saying that 95% of generative AI pilots fail to reach production."
>
> — [5:05](https://www.youtube.com/watch?v=l0FLhNqBOic&t=305s) &middot; *the headline number underpinning the failure argument*

> "And the reason for that is a lot of the time, AI is being slapped on top of broken processes in a way that the AI doesn't actually understand how to do things."
>
> — [5:05](https://www.youtube.com/watch?v=l0FLhNqBOic&t=305s) &middot; *the speaker's causal explanation for pilot failure*

> "It needs to be not too different to where they don't understand, you know, how to operate the system. For example, if they're used to an 11-step workflow and you come in and change that with a one-step, they might be taken aback, the adoption rates might suffer"
>
> — [5:53](https://www.youtube.com/watch?v=l0FLhNqBOic&t=353s) &middot; *names the adoption-vs-ROI tradeoff in process redesign*

> "Meaning, you do say, all right, four out of these eight steps will be handled completely autonomously. The other three will be handled with some human-in-the-loop intervention. And one step of that process will be handled by a human, period."
>
> — [6:30](https://www.youtube.com/watch?v=l0FLhNqBOic&t=390s) &middot; *concrete automation-split heuristic rather than abstract advice*

> "One of the quotes from our clients said that they spent $5,000,000 and 5 years migrating to uh NetSuite."
>
> — [7:05](https://www.youtube.com/watch?v=l0FLhNqBOic&t=425s) &middot; *hard number justifying the build-on-systems-of-record stance*

> "So, if you're telling them, "Hey, I have this fancy AI tooling, but by the way, you have to migrate off of NetSuite," they're going to tell you to get out."
>
> — [7:43](https://www.youtube.com/watch?v=l0FLhNqBOic&t=463s) &middot; *blunt statement of enterprise reality that many AI vendors ignore*

> "I will go as so far as to say that knowledge work is almost entirely solved. The difference is and what we're realizing now is that designing how work gets completed around AI is the next bottleneck."
>
> — [10:24](https://www.youtube.com/watch?v=l0FLhNqBOic&t=624s) &middot; *the strongest and most contestable claim in the talk*

> "If you're just doing AP and no other part of your department, you might have a 5 10% ROI. But, at Verek we deliver department-wide transformations, holistically transforming the entire department at a time."
>
> — [11:07](https://www.youtube.com/watch?v=l0FLhNqBOic&t=667s) &middot; *quantifies the point-solution vs department-wide argument*

> ""Well, we you know upload about 150 pages of documentation to Claude and then we prompt Claude and then we wait like 2 minutes and then we get analysis and then it's verbose and incorrect and it kind of sucks.""
>
> — [12:26](https://www.youtube.com/watch?v=l0FLhNqBOic&t=746s) &middot; *the concrete pain point that motivated the whole internal tool*

> "If you were at the booths downstairs this morning, there was, you know, five companies trying to sell you a graph DB, and you can just use Postgres, whatever it is."
>
> — [15:17](https://www.youtube.com/watch?v=l0FLhNqBOic&t=917s) &middot; *deflates infrastructure hype — representation matters more than the store*

> "most of these workflows inside of enterprise are remarkably linear. They just have a lot of cycles in them, but at the at the end of the day, the process owners want things to be as dependency-driven as possible."
>
> — [15:17](https://www.youtube.com/watch?v=l0FLhNqBOic&t=917s) &middot; *justifies the dependency-graph choice with an empirical observation*

> "The first is, given extracted context for the FTE, do we get a good high-quality output? And the answer is, with Claude, honestly, no, which is kind of surprising."
>
> — [15:55](https://www.youtube.com/watch?v=l0FLhNqBOic&t=955s) &middot; *a rare on-stage negative result about frontier model performance*

> "And the reason is they're so good at figuring out what is the part of the detail the client actually cares about, and what is the part that can get glossed over. And frontier models have absolutely no concept of this."
>
> — [16:40](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1000s) &middot; *articulates the specific capability gap driving their post-training*

> "These tools are things like make sure person A and person B are actually the same person because a lot of you know, there's a lot of Mikes in every company we work with and Claude gets very confused by this."
>
> — [17:14](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1034s) &middot; *memorable, concrete example of entity resolution as an agent tool*

> "I think a lot of Silicon Valley starts to go product product product, but what we're building for cannot be solved for with just a product."
>
> — [18:31](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1111s) &middot; *the services-over-product position that defines their bet*

## Positions

- Execution of knowledge work is essentially solved by current models and harnesses; intelligence is no longer the constraint. ([10:24](https://www.youtube.com/watch?v=l0FLhNqBOic&t=624s), confidence: stated)
- The binding constraint on enterprise AI value is understanding and redesigning a company's specific processes, not model capability. ([1:24](https://www.youtube.com/watch?v=l0FLhNqBOic&t=84s), confidence: stated)
- 95% of generative AI pilots fail to reach production, and roughly 87% don't produce measurable ROI. ([5:05](https://www.youtube.com/watch?v=l0FLhNqBOic&t=305s), confidence: stated)
- AI pilots fail primarily because AI is applied on top of broken, undocumented processes rather than redesigned ones. ([5:05](https://www.youtube.com/watch?v=l0FLhNqBOic&t=305s), confidence: stated)
- Non-technical operators in finance, sales, and procurement will not get the same ROI from general AI tooling that software engineers do. ([5:53](https://www.youtube.com/watch?v=l0FLhNqBOic&t=353s), confidence: stated)
- AI vendors should build on top of enterprise systems of record rather than requiring migration off NetSuite, SAP, Dynamics, or Salesforce. ([7:43](https://www.youtube.com/watch?v=l0FLhNqBOic&t=463s), confidence: stated)
- Point solutions yield 5–10% ROI within a function, while department-wide transformation yields 25–75%. ([11:07](https://www.youtube.com/watch?v=l0FLhNqBOic&t=667s), confidence: stated)
- Forward deployed engineers with both top-1% technical ability and strong client-facing communication skills are scarce, which is why the role must be augmented with agents. ([9:13](https://www.youtube.com/watch?v=l0FLhNqBOic&t=553s), confidence: stated)
- Frontier models like Claude produce verbose, low-quality long-form business analysis and cannot judge which details a client cares about. ([15:55](https://www.youtube.com/watch?v=l0FLhNqBOic&t=955s), confidence: stated)
- Post-trained open-source models outperform frontier models for writing normalized process flows from extracted context. ([16:40](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1000s), confidence: stated)
- The choice of graph database is unimportant; what matters is using a dependency-graph representation of the process. ([15:17](https://www.youtube.com/watch?v=l0FLhNqBOic&t=917s), confidence: stated)
- Enterprise workflows are mostly linear with cycles, and process owners prefer dependency-driven ordering. ([15:17](https://www.youtube.com/watch?v=l0FLhNqBOic&t=917s), confidence: stated)
- Extracting the right context from a large knowledge graph is a distinct and harder problem than generating good output from context, and is best solved with RL-trained custom traversal tools. ([17:51](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1071s), confidence: stated)
- A pure product company cannot capture enterprise AI value; a services/forward-deployed motion is required. ([18:31](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1111s), confidence: stated)
- Workflow changes should preserve enough of the original step structure to avoid harming adoption, even at some cost to efficiency. ([5:53](https://www.youtube.com/watch?v=l0FLhNqBOic&t=353s), confidence: implied)

## Concepts

- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [entity resolution](../concepts/entity-resolution.md)
- [forward deployed engineering](../concepts/forward-deployed-engineering.md)
- [graph rag](../concepts/graph-rag.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [post-training](../concepts/post-training.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [roi measurement](../concepts/roi-measurement.md)
- [semantic layer](../concepts/semantic-layer.md)
- [task decomposition](../concepts/task-decomposition.md)

