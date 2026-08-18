---
title: "Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)"
type: "talk"
slug: "building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo"
track: "Search & Retrieval"
org: "Turbopuffer"
video_id: "jQDXzEVHMSE"
duration_sec: 3389
word_count: 11830
speakers: []
---

# Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)

**Speakers:** unknown / not credited

**Org:** Turbopuffer

**Track:** Search & Retrieval &nbsp;|&nbsp; **Duration:** 56m 29s

[Watch on YouTube](https://www.youtube.com/watch?v=jQDXzEVHMSE)

## Summary

Gergely Orosz interviews Simon Eskildsen, co-founder and CEO of Turbopuffer, about the path from self-taught teenage programmer to eight years on Shopify's infrastructure team to building a vector/search database on top of S3. The through-line is 'napkin math': Eskildsen argues that first-principles calculations about DRAM bandwidth, fsync latency, and S3 round-trip costs beat benchmarks for making infrastructure decisions, and that this discipline is what let him promise Cursor a 95% bill reduction before the software was actually good. He explains the original architecture (cluster the vectors, put clusters in S3 objects, cache with an nginx reverse proxy on a single instance), why Cursor became customer number one, and why CPUs are now genuinely scarce because RL environments and agents consume them. He also lays out an unusually candid framework for venture capital — six reasons to raise, one of which is founder ego — and describes Turbopuffer's fully remote 'campfire' culture. Watch it for infrastructure reasoning and company-building philosophy; it is nearly AI-free despite Turbopuffer sitting under many AI products.

## Key Points

- Napkin math — memorized figures for DRAM bandwidth, SSD read latency, S3 round-trip cost, and per-gigabyte pricing across storage tiers — is presented as a better basis for infrastructure decisions than benchmarks, which frequently measure the wrong thing.
- Turbopuffer's core insight was economic before it was technical: storing vectors in DRAM made a recommendation feature cost $30k/month for a company spending $5k/month on all other infrastructure, so Eskildsen asked whether the same workload could live in S3 with clustering.
- The first shipped version was deliberately crude — cluster files plus a centroid file in S3, no real LSM implementation, an nginx reverse proxy as the cache, cache eviction via shelling out to rm — running on a single instance, because the goal was to find out whether anyone cared.
- Because S3's P99 for a 256–512KB object is around 200ms and tree navigation multiplies round trips, the system must be designed against P99 and even P999 by minimizing round trips rather than optimizing the median.
- Cursor became the first customer after reaching out on Twitter; Eskildsen flew to San Francisco, debugged their Postgres autovacuum problems on the spot, and won trust that way, then delivered a first bill 95% below their previous vendor's last one.
- CPUs, not just GPUs, are now scarce: RL training environments and agent workloads consume large amounts of general-purpose compute, and Eskildsen expects CPU availability to get worse before it gets better, with capacity ultimately gated by power availability per region.
- Turbopuffer survived on almost no capital — a ~$700k raise to hire two engineers, with an explicit promise to return the money and shut down if there was no PMF by year end — and Eskildsen enumerates six reasons to raise, calling founder ego a popular and dangerous one because it dilutes employees.
- The company is fully remote by design, using twice-yearly offsites plus opt-in 'campfires' (ad hoc gatherings anyone may join) and 'turbo credits' that buy business-class upgrades, so in-person time is encouraged but never mandatory.

## Notable Quotes

> "used to say you can't cache rights. So there's a fundamental point where you you just you have to move beyond a single shard."
>
> — [10:06](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=606s) &middot; *The scaling maxim that pushed Shopify to sharding, in one line.*

> "What does a gigabyte of memory cost? $2. What does a gigabyte of S3 cost? 2 cents."
>
> — [16:28](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=988s) &middot; *The 100x price gap that is the entire economic premise of Turbopuffer.*

> "So I just found myself in these discussions repeatedly where people were making infrastructure decisions based on poor benchmarks."
>
> — [18:02](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1082s) &middot; *States his central methodological position against benchmark-driven architecture choices.*

> "So in aggregate you have like you want to look at the P99 probably even the P999 to design the system properly because you will need to minimize the number of round trips that you had to make."
>
> — [25:34](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1534s) &middot; *Concrete design rule for building latency-sensitive systems on object storage.*

> "the simplest way you could do this is you run some clustering algorithm on the vectors."
>
> — [26:38](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1598s) &middot; *The whole v1 architecture reduced to its irreducible core.*

> "It was like the MVP of MVP. Anyone who's actually worked in the internal on databases would never have had like would have had too much pride to ship anything like that."
>
> — [30:01](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1801s) &middot; *Argues that database outsider status was an advantage, not a handicap.*

> "you could do a million vectors for a dollar. And before that, I think the the cheapest was maybe $100 per million for something that actually worked."
>
> — [30:32](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1832s) &middot; *The specific 100x pricing claim that drove the initial launch response.*

> "the unit economics of what we have right now where all the vectors are in DRAM are not working why hasn't anyone built it where we can put it in S3"
>
> — [30:32](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1832s) &middot; *Reconstructs the buyer-side pain that made Cursor an instant fit.*

> "they came on and their last bill with their previous vendor and the first bill with us, it was 95% lower."
>
> — [33:39](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2019s) &middot; *Reports the headline number behind the first customer relationship.*

> "I think as as RL is becoming a very very large amount of the workloads that needs a lot of CPUs. So, the labs are sucking up a lot of CPUs"
>
> — [39:06](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2346s) &middot; *Names a non-obvious cause of CPU scarcity that most people attribute only to GPUs.*

> "but I would assume that it gets a lot worse before it gets a lot better on the on the CPU side"
>
> — [39:40](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2380s) &middot; *A dated, checkable forecast about compute supply.*

> "The the clouds are not infinite as they seem when you're small."
>
> — [43:00](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2580s) &middot; *Compresses the capacity-planning reality that only shows up at scale.*

> "that's like a core engineering principle of me is simplicity above everything"
>
> — [44:17](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2657s) &middot; *His stated design value, which the nginx-cache v1 story concretely backs up.*

> "if this doesn't have PMF and is a big opportunity by the end of the year, I don't think we're going to bother and we'll just shut the whole thing down and we won't have it taking a dime."
>
> — [47:53](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2873s) &middot; *The unusual terms he offered his first investor, and the discipline behind them.*

> "I told some other VCs that at the time and that was terrifying to them. I think to someone on the West Coast this sounds like you have low ambition or something like that."
>
> — [48:27](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2907s) &middot; *Marks an explicit clash between his approach and Silicon Valley norms.*

> "I think this is a very very dangerous reason to raise money. And I wish that it was more talked about because you're diluting all of your employees when you do it."
>
> — [49:54](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2994s) &middot; *Takes a contrarian side on ego-driven fundraising that many founders would dispute.*

> "I think there's kind of maybe two cities where you can build a database company fast, and that's San Francisco and and and maybe New York."
>
> — [52:26](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=3146s) &middot; *The geographic premise that forced the fully remote model.*

> "when a couple of people just sort of randomly congregate in a place, you call it a campfire and you encourage as many people as you want to come and join"
>
> — [53:25](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=3205s) &middot; *Defines the specific remote-culture mechanism the company runs on.*

> "we give you a turbo credit and a turbo credit allows you to upgrade your next flight to business class which again encourages spending time together with the team"
>
> — [54:34](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=3274s) &middot; *A concrete incentive design for opt-in in-person time in a remote company.*

> "this is something that I now look for when we interview engineers is that you just you can't help yourself but trying to peel back the layers"
>
> — [7:19](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=439s) &middot; *States an explicit hiring criterion derived from his own self-taught path.*

## Positions

- First-principles napkin math is a more reliable basis for infrastructure decisions than benchmarks, because benchmarks often measure the wrong thing (e.g. an unnoticed distributed query inflating P99). ([17:02](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1022s), confidence: stated)
- Systems built on S3 must be designed against P99/P999 rather than P50, because a single logical operation issues many requests and tree traversal compounds ~200ms object latencies. ([25:05](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1505s), confidence: stated)
- The P99 for a 256–512KB object read from S3 is around 200 milliseconds. ([24:29](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1469s), confidence: stated)
- Storing vectors in object storage with a memory cache for actively-used data is roughly 100x cheaper than DRAM-resident vector databases — a million vectors for a dollar versus ~$100 per million. ([30:32](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1832s), confidence: stated)
- Using S3 for KV caching and similar workloads is still very uncommon, but it will happen because the economics favor it. ([31:23](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1883s), confidence: stated)
- Simplicity almost always wins in software, a lesson that becomes visible mainly through long tenures at one company. ([44:17](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2657s), confidence: stated)
- CPUs are now scarce, not just GPUs, because RL training environments and agent workloads consume large amounts of general-purpose compute, and the shortage will worsen before it improves. ([39:06](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2346s), confidence: stated)
- Cloud capacity allocation is ultimately determined by where power is available, and even large companies compete for regional allocations. ([41:12](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2472s), confidence: stated)
- There are exactly six legitimate reasons to raise capital — R&D, growth, founder ego, employee liquidity, strategic partnership, and M&A — and founders should be honest about which applies. ([49:17](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2957s), confidence: stated)
- Raising for founder ego is common and dangerous because it dilutes employees and sets a price that caps future employees' upside. ([49:54](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2994s), confidence: stated)
- A database company can be built quickly in-person essentially only in San Francisco or New York, so companies outside those cities must commit fully to a distributed model. ([52:26](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=3146s), confidence: stated)
- Remote work succeeds when in-person time is opt-in and incentivized rather than mandated — twice-yearly offsites plus voluntary campfires are sufficient. ([52:59](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=3179s), confidence: implied)
- Shipping a deliberately unsophisticated first version (no proper LSM, nginx as cache, single instance) was correct because durability invariants were preserved and demand was unproven. ([30:01](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1801s), confidence: implied)
- Engineers should be hired for an irrepressible instinct to peel back abstraction layers rather than for credentials. ([7:19](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=439s), confidence: stated)
- Application-layer scaling problems ultimately land at the database layer, and connection-level failure handling across drivers and frameworks is systematically untested. ([12:48](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=768s), confidence: stated)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [latency budgets](../concepts/latency-budgets.md)

