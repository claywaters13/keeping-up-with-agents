---
title: "The Rise of CaaS: Context-as-a-Service for Agentic AI"
type: "talk"
slug: "the-rise-of-caas-context-as-a-service-for-agentic-ai"
track: "Computer Use"
org: "Bright Data"
day: "Day 3 — Session Day 2"
room: "Track 7"
video_id: "Ot4OPrPH4xY"
duration_sec: 1339
word_count: 4193
speakers: ["Omer Primor"]
---

# The Rise of CaaS: Context-as-a-Service for Agentic AI

**Speakers:** [Omer Primor](../speakers/omer-primor.md)

**Org:** Bright Data

**Track:** Computer Use &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 22m 19s

[Watch on YouTube](https://www.youtube.com/watch?v=Ot4OPrPH4xY)

## Summary

Omer Primor of Bright Data argues that the web should be treated not just as a data source but as a live context layer for agents, and maps the emerging category he calls CaaS — context-as-a-service — vertical providers that crawl, structure into knowledge graphs, and serve enriched entity data to agents via MCP, CLI, or API. He contrasts CaaS with AI search (Exa, Parallel, Tavily, plus new entrants from Amazon and Microsoft) and reports a small in-house test enriching 25 fields for 100 companies across search, CaaS, and Google/SERP paths. The counterintuitive result: CaaS providers didn't dominate coverage, because they can only return what they already collected, while search agents can keep exploring; cost, meanwhile, varied enormously and search paths carry heavy token burn for structuring. His central claim is that frequency, not volume, is the cost killer — every repeated query costs the same as the first — which pushes teams to cut corners on refresh rates and result counts. A day's worth of direct scraping of known sources (LinkedIn, Crunchbase) hit a break-even against renting context at roughly 15,000 queries, leading to his closing line: owned context compounds while rented decays.

## Key Points

- The web should be reframed from a source of data to a source of context for agents doing knowledge work, where retrieval is a step toward downstream action rather than the deliverable itself.
- Web data decays fast — social media content is stale in under a day, and news, finance, and retail data is mostly irrelevant 30 days out — so context extraction is an ongoing process, not a one-time snapshot.
- Search-based access answers point-in-time questions well but cannot answer historical or longitudinal ones, such as how a price or a company's headcount changed over the past six months.
- CaaS providers behave like vertical search engines: they crawl, index, build knowledge graphs of deduplicated entities, and enrich from multiple sources for a specific domain (e-commerce, finance, HR, real estate, GTM).
- In a 100-company, 25-field enrichment test using Opus 4.8 as the harness, search-based approaches and plain Google/SERP converged on good coverage while two CaaS providers underperformed, because CaaS can only return fields it already collected.
- Cost comparison is misleading unless token burn is counted: CaaS pricing is the vendor fee alone, while search approaches add substantial token cost to structure raw results into usable data.
- Frequency, not record count, drives cost — every repeated query costs the same as the first even when nothing changed, which causes teams to cut corners by refreshing less often or capping results.
- Building your own pipeline by scraping known structured sources directly has an upfront setup cost (estimated at a week / $5,000) but near-zero marginal retrieval cost, with a break-even around 15,000 entities in this test.
- The right architecture depends on the workload: use AI search for ad hoc and changing questions, and consider owning the pipeline when knowledge-work needs are persistent, consistent, and growing.

## Notable Quotes

> "we help more than 20,000 teams around the world, including more than 70% of the world's biggest AI labs to extract data from the web"
>
> — [0:12](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=12s) &middot; *Establishes the speaker's vantage point with a concrete number.*

> "we're talking well over 50 billion pages, HTMLs every day. More than 20 pabytes of video, audio, and other media data"
>
> — [0:45](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=45s) &middot; *Reports the scale claim underpinning the company's authority on web data.*

> "The web is no longer just a source of data. We can actually start looking at it as a source of context."
>
> — [1:42](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=102s) &middot; *The talk's framing thesis in one line.*

> "The web is messy. It's unstructured. And most importantly, it changes all the time."
>
> — [2:41](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=161s) &middot; *Sets up the data-decay argument that drives everything after it.*

> "But also news, finance, retail, 30 days later, data that was collected, it's mostly no longer relevant."
>
> — [2:41](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=161s) &middot; *Concrete decay figure by vertical.*

> "extracting context from the web or relying on the web is not a snapshot. It's not a one-time effort."
>
> — [2:41](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=161s) &middot; *States the position that context acquisition is a process, not a task.*

> "They are purely built and indexing the web especially for agents. They're not even looking at the humans involved anymore."
>
> — [4:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=272s) &middot; *Names the structural shift in the search market from human to agent consumers.*

> "So Google's dominance when it comes to search, if Google was synonymous of web search, that is very much shaking."
>
> — [4:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=272s) &middot; *A checkable market claim others might contest.*

> "I cannot really search for how has that price changed over the last six months, what discounts it had"
>
> — [5:54](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=354s) &middot; *The clearest statement of what search structurally cannot do.*

> "We like to call them internally casts, context as a service because that's what they do. They allow agents to tap into them MCP, CLI, uh just pure good old API"
>
> — [6:33](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=393s) &middot; *Defines the talk's titular category.*

> "they kind of behave like vertical search engines, right? they are a very very very good search engine for something very specific"
>
> — [7:14](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=434s) &middot; *Compact mental model for what CaaS actually is.*

> "It's very tempting to throw AI search at all of them but maybe that's not optimal maybe I need a combination of both"
>
> — [8:53](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=533s) &middot; *The architectural recommendation, stated as a hedge against a default choice.*

> "I expected cast to dominate this thing because that's you know you had one job right to map out all these companies."
>
> — [11:34](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=694s) &middot; *Names the surprising result honestly rather than burying it.*

> "If they didn't collect data about the recent job hiring, it will never be there, right? So, it makes sense that they are a bit behind"
>
> — [11:34](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=694s) &middot; *Explains the fundamental coverage ceiling of pre-indexed context providers.*

> "All of the other search solutions, you also needed a lot of token burn it burn to actually structure that data"
>
> — [12:14](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=734s) &middot; *Names the hidden cost that makes headline vendor pricing misleading.*

> "we're seeing even within this industry niche players that have, you know, lower quality data but much cheaper"
>
> — [12:54](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=774s) &middot; *Observes market segmentation forming inside the new category.*

> "frequency is the cost killer when we talk about these and we need to acknowledge that"
>
> — [13:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=812s) &middot; *The talk's central economic claim.*

> "every repeated query costs the same as the first even if it brought back the exact same answers nothing changed pay up"
>
> — [13:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=812s) &middot; *The mechanism behind the frequency argument, stated bluntly.*

> "this is where we see teams that are starting to cut corners so I won't research this company every day I'll look at it once a week or once a month"
>
> — [13:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=812s) &middot; *Identifies the behavioral consequence of per-query pricing on knowledge work quality.*

> "Basically, we're renting context. We're not owning the context that we use. That is a very important distinction."
>
> — [15:36](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=936s) &middot; *The rent-vs-own frame the whole second half rests on.*

> "we all know these sources we all know where that data comes from the cast also bring it from them zoom info bring it from them it's the same thing over and over again why not just go straight to the source"
>
> — [16:13](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=973s) &middot; *The build-it-yourself argument in its sharpest form.*

> "if you think about for example LinkedIn, the data is already structured in form of entities. There's an entity for a company, there's entity for a person, there's entity for a job"
>
> — [17:40](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1060s) &middot; *Argues the knowledge graph often already exists at the source.*

> "everything to the left of that dot in this case it was just over 15,000 entities or queries"
>
> — [18:59](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1139s) &middot; *The one hard break-even number in the talk.*

> "whatever retrieval happens later on from the from the agents, right, is free. Not really free, but you get what I mean, right? There's no added cost."
>
> — [19:42](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1182s) &middot; *States the core economic advantage of owned context.*

> "I'll ask it a hundred times until I get what I need. I I have no more fear, no more cutting corners, which is maybe the most important thing."
>
> — [19:42](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1182s) &middot; *Frames the benefit as behavioral freedom rather than just savings.*

> "eventually the frequency will come and bite you in the ass when it comes to cost and that's something to be mindful of and there's a fair chance that that tipping point is much lower than you think"
>
> — [20:15](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1215s) &middot; *The closing warning, with an explicit prediction about where teams misjudge.*

> "owned context compounds while rented decays"
>
> — [21:24](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1284s) &middot; *The thesis compressed into the talk's takeaway line.*

## Positions

- The web should be treated as a source of context for agents rather than merely a source of data, because retrieval feeds downstream reasoning and action. ([1:42](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=102s), confidence: stated)
- Web data decays fast enough — under a day for social media, roughly 30 days for news, finance, and retail — that context acquisition must be a recurring process, not a snapshot. ([2:41](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=161s), confidence: stated)
- Google's long-standing dominance of web search is genuinely eroding as AI search companies and cloud providers build agent-specific indexes. ([4:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=272s), confidence: stated)
- Web search alone cannot supply longitudinal context, such as how a price or a company's headcount changed over time, even though that information existed on the web. ([5:54](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=354s), confidence: stated)
- CaaS providers are structurally capped in coverage: if they didn't already collect a field, an agent can never obtain it from them, whereas search-based agents can keep exploring. ([11:34](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=694s), confidence: stated)
- Comparing CaaS to search on price alone is unfair because search approaches incur significant additional token cost to structure raw results into usable data. ([12:14](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=734s), confidence: stated)
- Query frequency, not record volume, is the dominant cost driver for agentic web context, since every repeated query costs the same as the first even when nothing has changed. ([13:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=812s), confidence: stated)
- Per-query pricing causes teams to degrade their own knowledge work by refreshing less often and capping result counts. ([13:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=812s), confidence: stated)
- For company enrichment specifically, going directly to the known underlying sources with scrapers is viable because CaaS vendors and ZoomInfo pull from those same sources anyway. ([16:13](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=973s), confidence: stated)
- A self-built scraping pipeline for this task reached break-even against renting context at just over 15,000 entities or queries, assuming roughly a week and $5,000 of setup. ([18:59](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1139s), confidence: stated)
- AI search and CaaS are the right choice for ad hoc, changing, or one-time questions, while persistent and repeated knowledge-work needs favor owning the pipeline. ([19:42](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1182s), confidence: stated)
- The build-vs-rent tipping point is lower than most teams assume. ([20:15](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1215s), confidence: stated)
- Cheaper CaaS vendors trade data quality for price and are deliberately capturing a long tail of small-volume users. ([12:54](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=774s), confidence: implied)
- Owning context creates compounding value over time while rented context loses value as the underlying web changes. ([21:24](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1284s), confidence: stated)

## Concepts

- [agentic retrieval](../concepts/agentic-retrieval.md)
- [build versus buy](../concepts/build-versus-buy.md)
- [context engineering](../concepts/context-engineering.md)
- [entity resolution](../concepts/entity-resolution.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [retrieval evaluation](../concepts/retrieval-evaluation.md)
- [token efficiency](../concepts/token-efficiency.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)
- [web data infrastructure](../concepts/web-data-infrastructure.md)

