---
title: "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer"
type: "talk"
slug: "thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer"
track: "Graphs"
org: "Neo4j"
day: "Day 4 — Session Day 3"
room: "Main Stage"
video_id: "VGN22pPpb-8"
duration_sec: 666
word_count: 1870
speakers: ["Emil Eifrem"]
---

# Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer

**Speakers:** [Emil Eifrem](../speakers/emil-eifrem.md)

**Org:** Neo4j

**Track:** Graphs &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 11m 06s

[Watch on YouTube](https://www.youtube.com/watch?v=VGN22pPpb-8)

## Summary

Emil Eifrem of Neo4j argues that the common pattern of building agents by hand-wiring each one to enterprise data sources doesn't scale, and proposes an 'ontology-based semantic layer' as shared infrastructure underneath many thin agents. Using a bank-account-opening agent as the running example, he identifies four failure modes of the thick-agent approach: rediscovering where data lives from scratch every time, being unable to judge trust or freshness, violating DRY so that schema changes force manual rewiring across every agent, and having no mechanism for learning across invocations or across agents. His blueprint has three pillars — a business-facing ontology of company concepts in human language, a technical ontology of all data source metadata, and runtime execution traces from agents — plus a mapping between the first two. He explicitly pushes back on the idea that Markdown files and skills solve this, calling them part of the solution but not the solution. Worth watching if you're deciding how to structure data access for a fleet of agents in a large organization; it's a short vendor keynote, so treat the pattern as the takeaway rather than expecting implementation detail.

## Key Points

- Hand-wiring data sources into each agent works fine at startup scale with one Postgres database, but breaks in enterprises with hundreds of databases, warehouses, and object stores.
- The thick-agent pattern fails in four specific ways: repeated from-scratch data discovery, no trust/versioning signal, DRY violations that force manual rewiring when anything changes, and no learning across time or across agents.
- Markdown files and skills are part of the answer but not sufficient — teams that tried to solve enterprise data access with Markdown alone did not get there.
- The proposed architecture is 'thin agents on a smarter shared substrate,' where the substrate is an ontology-based semantic layer rather than logic embedded in each agent's code and prompts.
- Pillar one is a business-facing ontology: the key concepts of the organization (customer, account, transaction) and their relationships, named the way humans in the company actually talk, not the way columns are named.
- Pillar two is a technical ontology capturing metadata for every data source and asset — locations, schemas — with an explicit mapping from business concepts down to systems of record (e.g. 'first name' → an Oracle column called F_name).
- Pillar three is runtime execution traces: what the agent tried, in what context, and whether it succeeded, rolled into a score that biases future data source selection.
- Trustworthiness of a data source is established two ways at once — top-down via human-curated administrator knowledge, and bottom-up via what execution traces show actually worked in practice.
- Eifrem reports the pattern emerged from work with a Fortune 20 global bank, a large Bay Area tech platform company, and a leading fintech over roughly the prior 6–9 months.

## Notable Quotes

> "the pattern that is emerging is that in order to do things at scale, we need thin agents on a smarter shared substrate."
>
> — [4:13](https://www.youtube.com/watch?v=VGN22pPpb-8&t=253s) &middot; *The talk's thesis in one line.*

> "we've seen a ton of team that tried to solve this problem using just Markdown files. And the summary is it is part of the solution, but it is not the solution."
>
> — [3:31](https://www.youtube.com/watch?v=VGN22pPpb-8&t=211s) &middot; *Direct pushback on the skills/Markdown consensus that many other 2026 talks take for granted.*

> "Hey guys, you got to learn your databases. You cannot vibe code with just markdown files."
>
> — [3:31](https://www.youtube.com/watch?v=VGN22pPpb-8&t=211s) &middot; *The sharpest phrasing of the anti-Markdown position, attributed in the talk to swyx on Latent Space.*

> "if you work at a startup and you have one application, it sits on top of one Postgres database, that's not hard."
>
> — [1:30](https://www.youtube.com/watch?v=VGN22pPpb-8&t=90s) &middot; *Scopes the problem honestly — he concedes the pattern is unnecessary at small scale.*

> "in an enterprise ecosystem, you don't have one database, you have a hundred databases, and you have Snowflake and Databricks, probably, and you have S3 buckets"
>
> — [2:18](https://www.youtube.com/watch?v=VGN22pPpb-8&t=138s) &middot; *Quantifies the enterprise data sprawl that motivates the whole architecture.*

> "It also violates one of the core principles of software engineering, the DRY principle, don't repeat yourself."
>
> — [2:18](https://www.youtube.com/watch?v=VGN22pPpb-8&t=138s) &middot; *Frames per-agent data wiring as a software engineering defect, not just an inconvenience.*

> "when your agent wake up wakes up tomorrow, it's not smarter than it was today, and there certainly isn't any cross-agent learning because all of that wiring between business intent and the data sources is encoded in a combination of code and prompts."
>
> — [2:52](https://www.youtube.com/watch?v=VGN22pPpb-8&t=172s) &middot; *Names the root cause — logic trapped in code and prompts can't be learned from or shared.*

> "So, we've been solving this problem at scale for some really massive organizations recently, including a Fortune 20 global bank"
>
> — [3:31](https://www.youtube.com/watch?v=VGN22pPpb-8&t=211s) &middot; *The evidence base behind the claimed pattern.*

> "there's a lot of people who want to make ontologies really complex. But the core concepts are actually super simple."
>
> — [4:13](https://www.youtube.com/watch?v=VGN22pPpb-8&t=253s) &middot; *Positions against the heavyweight semantic-web framing of ontologies.*

> "you don't say if underscore name. No, you have a customer and they have a first name."
>
> — [4:56](https://www.youtube.com/watch?v=VGN22pPpb-8&t=296s) &middot; *Concrete illustration of the business-vs-technical naming split that the mapping layer bridges.*

> "The second pillar is a technical ontology. This is all the metadata of all the data sources and data assets in your enterprise ecosystem."
>
> — [4:56](https://www.youtube.com/watch?v=VGN22pPpb-8&t=296s) &middot; *Defines the second pillar precisely.*

> "And then the third pillar is the run time signals out of your agents. When they walk this graph and they execute, they leave the traces around."
>
> — [5:45](https://www.youtube.com/watch?v=VGN22pPpb-8&t=345s) &middot; *Introduces execution traces as first-class architecture, not just observability.*

> "I've been very successful using the DMV lookup, for example, then I'm more likely to choose one if I'm in the right context in my next invocation."
>
> — [7:40](https://www.youtube.com/watch?v=VGN22pPpb-8&t=460s) &middot; *Spells out the feedback loop mechanism concretely.*

> "We also know it bottom-up through the execution traces. This is what actually worked in reality, in practice."
>
> — [8:19](https://www.youtube.com/watch?v=VGN22pPpb-8&t=499s) &middot; *The empirical half of the trust model, contrasted with human curation.*

> "we're moving from this world, a world of thick agents with manually wired data sources, into this world where we have thin agents on a smarter shared ontology-based semantic layer."
>
> — [8:19](https://www.youtube.com/watch?v=VGN22pPpb-8&t=499s) &middot; *States the before/after architecture shift explicitly.*

> "And this allows us to do a ton more agents without having to re-engineer them every time."
>
> — [9:04](https://www.youtube.com/watch?v=VGN22pPpb-8&t=544s) &middot; *The claimed payoff — agent count scaling without per-agent engineering cost.*

## Positions

- Markdown files and skills alone are insufficient for giving enterprise agents reliable access to the right data; they are part of the solution but not the solution. ([3:31](https://www.youtube.com/watch?v=VGN22pPpb-8&t=211s), confidence: stated)
- Agents should be thin, with data discovery, mapping, and trust logic pushed down into a shared substrate rather than encoded per-agent in code and prompts. ([4:13](https://www.youtube.com/watch?v=VGN22pPpb-8&t=253s), confidence: stated)
- An effective semantic layer requires exactly three pillars — a business-facing ontology, a technical ontology of data source metadata, and runtime execution traces — plus a mapping between the first two. ([4:13](https://www.youtube.com/watch?v=VGN22pPpb-8&t=253s), confidence: stated)
- The business ontology must be expressed in language that all humans in the organization understand, not in database-level naming. ([4:56](https://www.youtube.com/watch?v=VGN22pPpb-8&t=296s), confidence: stated)
- Ontologies do not need to be complex; their core concepts are simple, and the complexity people add to them is unnecessary. ([4:13](https://www.youtube.com/watch?v=VGN22pPpb-8&t=253s), confidence: stated)
- Data source trustworthiness should be determined both top-down by human curation and bottom-up by what execution traces show actually worked. ([8:19](https://www.youtube.com/watch?v=VGN22pPpb-8&t=499s), confidence: stated)
- Agents can improve over time and across each other by scoring past data-source choices from execution traces and weighting future selection by context. ([7:40](https://www.youtube.com/watch?v=VGN22pPpb-8&t=460s), confidence: stated)
- This problem is specific to organizations with many data sources and many agents; single-application startups on one Postgres database do not need this architecture. ([9:47](https://www.youtube.com/watch?v=VGN22pPpb-8&t=587s), confidence: stated)
- A graph is the right representation for this substrate, since business concepts, technical assets, processes, and traces are all linked and traversed together. ([6:21](https://www.youtube.com/watch?v=VGN22pPpb-8&t=381s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [ontology design](../concepts/ontology-design.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [semantic layer](../concepts/semantic-layer.md)

