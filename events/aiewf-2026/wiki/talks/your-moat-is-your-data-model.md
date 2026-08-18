---
title: "Your Moat Is Your Data Model"
type: "talk"
slug: "your-moat-is-your-data-model"
track: "Graphs"
org: "Gates Foundation"
day: "Day 4 — Session Day 3"
room: "Track 5"
video_id: "jt1Pbr_n6oU"
duration_sec: 1229
word_count: 3443
speakers: ["Mike Phipps"]
---

# Your Moat Is Your Data Model

**Speakers:** [Mike Phipps](../speakers/mike-phipps.md)

**Org:** Gates Foundation

**Track:** Graphs &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 20m 29s

[Watch on YouTube](https://www.youtube.com/watch?v=jt1Pbr_n6oU)

## Summary

Mike Phipps of the Gates Foundation argues that in a world where frontier models and chat UIs are commoditized, the durable competitive advantage for an enterprise AI team is the modeled understanding of its own internal processes — the tacit knowledge encoded in a data model. He walks through the Strategic Intelligence Platform (SIP), rolled out to ~4,000 Gates Foundation staff, which unifies siloed systems of record into a data lakehouse and then a Neo4j knowledge graph designed for agent consumption, exposed via a forked MCP server so users can query it from Claude or ChatGPT rather than yet another chat app. Most of the talk is a concrete walkthrough of the graph schema: multiple hierarchy types (an additive DAG for funding, a level-meaningful hierarchy for investment management with precomputed rollup edges), a people/org hierarchy, and unstructured meeting documents chunked and indexed alongside the structured entities. He closes with an eval loop that compares agent answers against live graph queries (since structured data constantly changes), measuring pass@1 and stability with an LLM judge, and feeding gaps back into the data model and schema descriptions. Worth watching if you're building agentic retrieval over messy enterprise systems of record and want a worked example of graph modeling plus governance and eval practice.

## Key Points

- The defensible moat in enterprise AI is not the model or the chat interface but the organization's tacit procedural knowledge modeled into a data structure agents can traverse.
- The Gates Foundation built SIP, an enterprise-wide platform now in production for about 4,000 staff, layering a data lakehouse, curation pipeline, and knowledge graph beneath agentic chat and workflows.
- Correctness in enterprise retrieval means matching established reporting conventions, not merely producing a defensible answer — which requires engaging data owners to extract field meanings, join logic, limitations, and security trimming.
- The team models multiple distinct hierarchy types in one graph: an additive five-level DAG for funding where all levels matter together, and a contains/manages hierarchy where each level is independently meaningful and rollup edges can be precomputed.
- Stitching previously siloed source systems (funding, investment management, HR org charts, meeting documents) into common entities lets an agent dynamically discover and reason across the full organizational structure at query time.
- Governance becomes more acute with AI because data that was technically accessible before is now practically accessible, widening the risk surface and forcing PII masking, sensitivity classification, and per-user entitlements.
- Because structured data changes constantly, evals store a graph query per question and pull ground truth from the live graph at runtime, comparing it to the agent's answer with an LLM judge measuring pass@1 and stability.
- The eval loop is a data-modeling tool: remaining failures are mostly ambiguity rather than wrongness, and they feed back into schema descriptions and domain rules.
- Rather than compete on UI, SIP serves the platform where users already are — through MCP into Claude and ChatGPT — with constrained MCP-app workflows as a complement to open-ended chat.

## Notable Quotes

> "but our moat here was our understanding of our internal processes the tacet knowledge that you need to to run successful AI and this is true I think no matter how good AI gets how good models get"
>
> — [1:09](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=69s) &middot; *The thesis of the talk, stated in the speaker's own framing.*

> "I'm not I'm not worried because the part that we've built is the defensible part that that's that's durable."
>
> — [2:07](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=127s) &middot; *States the strategic bet plainly: model releases don't threaten the layer they own.*

> "these are the the processes tacet knowledge that we've modeled into what we call the strategic intelligence platform or SIP. and it rolled out here this past month in production for enterprise use across uh the Gates Foundation. So about 4,000 people."
>
> — [2:07](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=127s) &middot; *Establishes production scope and scale rather than a prototype.*

> "So there's 4,000 different employees of the foundation. Um you know many different strategies within the foundation the US within the US across almost all the states grantees the total annual dispersement over 7 billion dollars."
>
> — [4:17](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=257s) &middot; *Concrete numbers on the data domain being modeled.*

> "in a in a in a nutshell here structuring operational data for agentic retrieval. So we're building a knowledge graph with the idea of the agent consumer"
>
> — [5:02](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=302s) &middot; *One-line definition of the architecture's design goal — agent as the consumer, not humans.*

> "when you're dealing with systems of record with lots of complexity engagement ment is critical. This is something that we've we've found here repeatedly. We have to engage data owners to understand, you know, this tacet knowledge we're trying to to model."
>
> — [5:51](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=351s) &middot; *Names the human process work as the hard prerequisite, not an afterthought.*

> "it's not enough just to answer it a question a certain way. You have to answer it the way that it's been answered in the past."
>
> — [6:32](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=392s) &middot; *Sharp statement of what enterprise correctness actually means.*

> "This is the procedural understanding tacet knowledge that AI needs and it's yeah it's the part that we that we own"
>
> — [6:32](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=392s) &middot; *Links the reporting-conventions problem back to the moat argument.*

> "the third bucket here, governance. This is a important one that I think AI makes more acute things that were that were accessible previously."
>
> — [7:16](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=436s) &middot; *A specific claim about how AI changes an existing access-control problem.*

> "They're much more accessible now with with AI. And so you have to consider this. Your risk sphere is is larger. So things like PII need to be masked."
>
> — [7:59](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=479s) &middot; *Concrete governance consequence of agentic retrieval over enterprise data.*

> "the just the the entry point here we have over 80 different strategy teams. These teams have annual reviews that happen. This is how the budgeting for each year is derived."
>
> — [8:46](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=526s) &middot; *Shows the entry node of the graph and why the meeting is the modeling anchor.*

> "four different systems one graph uh one semantic layer that's exposed through an MCP then to the to the agents. And so this is the so if you think of the agent's perspective, this is the the structure that it can dynamically discover and reason across at query time."
>
> — [14:16](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=856s) &middot; *Summarizes the end-to-end architecture and the agent's runtime view.*

> "for the developer, it's also a very cool thing because it exposes, you know, what you don't know about your your the thing you're modeling."
>
> — [15:03](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=903s) &middot; *Argues graph modeling has diagnostic value independent of the AI use case.*

> "What was not defensible was the was the the chat interface was the UI and even in some cases the the general chat cases"
>
> — [15:43](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=943s) &middot; *Explicitly names what they chose not to build, which is the strategic tradeoff.*

> "the way eval relate to data modeling is that as you're doing eval, you find you find gaps. You find ambiguities in your data model."
>
> — [17:04](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1024s) &middot; *Reframes evals as a data-modeling instrument rather than a scoreboard.*

> "One challenge is that the the structured data is constantly changing. So we have to have the graph query itself that we that we create for each of these different questions and then at runtime for the eval we we pull from the live graph and then we compare that to what the agent is delivering"
>
> — [17:50](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1070s) &middot; *A specific, transferable technique for evaluating agents over mutable structured data.*

> "So if you ask the same question multiple times, you get the same answer back, you can use LLM as a judge to to to measure this."
>
> — [18:31](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1111s) &middot; *Defines their stability metric concretely.*

> "the the questions that we that we end up do missing, it tends to be things that are ambiguous in some way. And so it's not wrong, it's just that it's things that might be right but not what the user intended."
>
> — [19:08](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1148s) &middot; *Characterizes the residual failure mode after evals get strong.*

> "There's a lot of there's a lot of demand for a federated graph experience."
>
> — [19:08](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1148s) &middot; *Signals the next architectural problem: team-owned data linking into the enterprise graph.*

## Positions

- The defensible moat for an enterprise AI team is its modeled understanding of internal processes and tacit knowledge, not the models, agents, or UI. ([1:09](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=69s), confidence: stated)
- Chat interfaces and UIs are not defensible, so enterprises should serve their platform into tools users already have (Claude, ChatGPT) via MCP rather than building another chat app. ([15:43](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=943s), confidence: stated)
- An answer is only correct in an enterprise setting if it matches how the question has historically been answered under existing reporting conventions. ([6:32](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=392s), confidence: stated)
- A property graph is the right representation for cross-system operational data because agents can dynamically discover and traverse the schema at query time. ([14:16](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=856s), confidence: implied)
- AI expands an organization's risk surface by making previously theoretically-accessible data practically accessible, requiring PII masking, sensitivity classification, and per-user entitlements in the curation pipeline. ([7:16](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=436s), confidence: stated)
- Evals over constantly-changing structured data must compute ground truth from a stored graph query against the live graph at runtime, rather than from frozen expected answers. ([17:50](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1070s), confidence: stated)
- Eval failures should be fed back into the data model, domain rules, and schema descriptions — evals are a data-modeling feedback loop, not just a quality score. ([17:04](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1024s), confidence: stated)
- Once eval scores are strong, the remaining failures are dominated by user-intent ambiguity rather than factually wrong answers. ([19:08](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=1148s), confidence: stated)
- Data owners must be engaged directly to capture field semantics, join logic, data limitations, safeguards, and security trimming — this cannot be inferred from the data alone. ([5:51](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=351s), confidence: stated)
- Constrained, workflow-shaped agent experiences (e.g. MCP apps with sandboxed agents) are a valuable complement to open-ended chat over the same knowledge graph backend. ([16:24](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=984s), confidence: stated)
- Off-the-shelf MCP servers require substantial modification (forking, schema updates, state passing like conversation and message IDs) for production enterprise use. ([15:43](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=943s), confidence: stated)

## Concepts

- [agentic retrieval](../concepts/agentic-retrieval.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [entity resolution](../concepts/entity-resolution.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [institutional knowledge capture](../concepts/institutional-knowledge-capture.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [semantic layer](../concepts/semantic-layer.md)

