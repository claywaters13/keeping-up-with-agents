---
title: "How Web Data Infrastructure Powers the Next Generation of AI"
type: "talk"
slug: "how-web-data-infrastructure-powers-the-next-generation-of-ai"
track: "Computer Use"
org: "Oxylabs"
day: "Day 3 — Session Day 2"
room: "Track 7"
video_id: "1UmZHb_E_SM"
duration_sec: 1143
word_count: 2609
speakers: ["Patricija Žemaitytė"]
---

# How Web Data Infrastructure Powers the Next Generation of AI

**Speakers:** [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)

**Org:** Oxylabs

**Track:** Computer Use &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 19m 03s

[Watch on YouTube](https://www.youtube.com/watch?v=1UmZHb_E_SM)

## Summary

Patricija Žemaitytė, a product manager at Oxylabs, argues that the bottleneck for the next generation of AI is not model quality but the web-data infrastructure that connects models to live reality. She tells three war stories from Oxylabs: building a petabyte-scale video collection API (and its transcript/subtitle/metadata sequels) in two weeks, redesigning search scraping from ~4 second latency down to sub-second for AI retrieval workloads, and scaling a web unblocker from 10,000 to 60,000 requests per second in under two months. Each story lands on the same lesson — innovation is repeated adaptation under pressure, and clients buy your ability to adapt rather than the first product iteration. The talk is light on architecture detail but rich in operational numbers (400 million to ~6 billion daily requests, 550ms average latency, 30 petabytes delivered) and in honest failure moments, including getting blocked live on a customer call. Worth watching if you care about the retrieval/grounding layer beneath agents, or want a vendor-side view of what serving AI data pipelines actually costs operationally.

## Key Points

- The industry is shifting away from static trained knowledge: training still matters, but models now need live search and external data to stay useful, which makes the retrieval layer around the model a first-class infrastructure concern.
- A single customer feature request for video downloads expanded through iteration into a full product suite covering downloaders, transcripts, subtitles, search, channel information, and metadata over roughly three months.
- AI data pipelines are increasingly multimodal, requiring not just text but video, metadata, transcripts, subtitles, and the structural context around content.
- A fast search API for AI deliberately narrows scope to organic results, top stories, and news, cutting away ads, widgets, rich results, and heavy layout that a general-purpose scraper collects.
- Getting from ~4 second to sub-second search latency was a ground-up redesign, not an optimization; the first rebuild hit ~650ms P90 in under two weeks, and the production system now averages 550ms.
- Low latency was won by auditing layouts, parsers, sessions, and proxies for small savings rather than by any single breakthrough, and browsers remained the core tension because they are slow, expensive, and complex.
- Scaling from 10,000 to 60,000 requests per second could not be solved by adding servers; it required architecture, reliable central components, truthful observability, and load tests that resembled real client traffic.
- At high scale, telemetry itself becomes part of the load and part of the complexity, and organic-traffic load testing is far harder than generating synthetic traffic.
- Speed is not just a performance metric but a constraint on what products can exist at all: four seconds gives you a slow pipeline, sub-second gives you something that can sit inside an AI workflow.

## Notable Quotes

> "most AI talks today starts with models. This one starts somewhere less glamorous with infrastructure that decides whether those models get fresh, usable, real-time data at all."
>
> — [0:01](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=1s) &middot; *States the talk's thesis and framing in one line.*

> "the industry is shifting away from static knowledge and training itself still matters of course but training alone is no longer enough and to stay useful models needs to get access to fresh information"
>
> — [1:04](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=64s) &middot; *The core claim about why retrieval infrastructure now matters.*

> "innovation never comes as a neat road map. It comes as a pressure uh as a deadline and sometimes and quite often as a trip report from San Francisco."
>
> — [1:53](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=113s) &middot; *Memorable articulation of how the roadmap actually gets set.*

> "What's the deadline? Two weeks. What's the what's the scale at least five pabytes per month at that point? We have never built nothing like that"
>
> — [2:45](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=165s) &middot; *Concrete constraints that set up the first case study.*

> "this is also a moment when the feature stops sounding like as a product feature. It sounds like infrastructure"
>
> — [2:45](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=165s) &middot; *Names the threshold where a feature request becomes an infrastructure problem.*

> "AI infrastructure is becoming increasingly multimodel is no longer about the text and companies now need pipelines for video metadata transcripts subtitles and another structural context around the content itself"
>
> — [2:45](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=165s) &middot; *Market claim about multimodal data pipeline demand.*

> "That client actually didn't need a transcript. They needed a subtitles."
>
> — [4:35](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=275s) &middot; *The requirements-discovery failure that drove the product suite's expansion.*

> "it's 2026 client already gathered 30 pabytes of data and we're still waiting for a payment"
>
> — [5:27](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=327s) &middot; *Rare candid number on delivered volume plus the commercial punchline.*

> "innovation is actually a repeated adaptation under high pressure. Because once you learn that the client actually doesn't buy the first product iteration, they buy your ability to adapt."
>
> — [5:27](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=327s) &middot; *The talk's central thesis about adaptation as the product.*

> "Google's grounding documentation explicitly positions Google search as a way to connect models to current public knowledge."
>
> — [6:19](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=379s) &middot; *External citation supporting the search-as-grounding-layer argument.*

> "our traditional regular search scraper was around 4 seconds average latency. So the gap was huge but we still decided to go for it just to see if it's possible and we actually did it."
>
> — [7:13](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=433s) &middot; *Baseline number for the latency story.*

> "when your baseline is at 4 seconds, we are not talking about optimization. We are talking about redesign."
>
> — [8:42](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=522s) &middot; *Crisp statement of when incremental tuning stops working.*

> "there is a difference between system that works in development, system that works in a test and system that actually survives reality"
>
> — [9:35](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=575s) &middot; *Lesson drawn from getting blocked live during a customer demo.*

> "browsers also are slow, expensive, complex and deeply incompatible with dreams about low latency"
>
> — [10:18](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=618s) &middot; *Names the central tradeoff in low-latency web collection.*

> "this is how systems becomes fast. Not by giant breakthroughs as we thought at first but by small decision that adds up"
>
> — [10:18](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=618s) &middot; *Concrete methodology claim about latency work.*

> "today we have fast search API that delivers results and fresh data directly into AI workflows with 550 milliseconds average latency and our scale move from 400 million daily requests to almost 6 billion daily requests"
>
> — [11:16](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=676s) &middot; *The headline performance and scale numbers.*

> "in AI era speed is not just performance. speed actually defines what product can exist"
>
> — [11:16](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=676s) &middot; *Sharpest argumentative claim in the talk.*

> "when you kind of scale to that workload even adding up additional 2,000 servers doesn't solve the problem. You need an architecture."
>
> — [13:19](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=799s) &middot; *Rejects the horizontal-scaling reflex explicitly.*

> "everybody loves observability in theory but observability at scale becomes a true work because collecting logs is hard, processing logs is harder"
>
> — [14:11](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=851s) &middot; *Operational tradeoff on telemetry that many talks skip.*

> "the next generation of AI will not be powered by better models. It will be powered by better infrastructure around it."
>
> — [17:39](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=1059s) &middot; *The closing thesis, stated as a direct contrarian position.*

## Positions

- The next generation of AI will be powered by better infrastructure around models rather than by better models themselves. ([17:39](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=1059s), confidence: stated)
- Training alone is no longer enough for models to stay useful; they require access to fresh, live external data. ([1:04](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=64s), confidence: stated)
- Latency is a product constraint, not merely a performance metric: a four-second pipeline cannot support interactive AI workflows while a sub-second one can. ([11:16](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=676s), confidence: stated)
- Moving from a four-second baseline to sub-second latency requires a ground-up redesign, not incremental optimization of the existing scraper. ([8:42](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=522s), confidence: stated)
- Search APIs built for AI should collect a narrower slice of the page — organic results, top stories, news — and discard ads, widgets, rich results, and heavy layout. ([7:56](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=476s), confidence: stated)
- Systems become fast through many small accumulated decisions across layouts, parsers, sessions, and proxies, not through a single breakthrough. ([10:18](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=618s), confidence: stated)
- Scaling from 10,000 to 60,000 requests per second cannot be solved by adding hardware; even 2,000 additional servers would not suffice without architectural change. ([13:19](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=799s), confidence: stated)
- Synthetic traffic load testing is comparatively easy; testing with organic traffic that behaves like real client usage is the hard part, and ultimately production traffic is the real test. ([14:11](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=851s), confidence: stated)
- At sufficient scale, telemetry itself becomes a meaningful part of the system load and complexity. ([14:59](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=899s), confidence: stated)
- Browsers are necessary for reliable collection but are fundamentally in tension with low-latency requirements. ([10:18](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=618s), confidence: stated)
- Customers do not buy the first product iteration; they buy the vendor's ability to adapt to changing requirements. ([5:27](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=327s), confidence: stated)
- Web data collection is an 'adapt forever' business rather than a build-once business, because targets, layouts, detection, and client needs all change continuously. ([16:36](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=996s), confidence: stated)
- Scale has no finish line — hitting 60,000 requests per second immediately produced a 150,000 requests per second target. ([15:46](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=946s), confidence: implied)
- The market was not ready for sub-second search delivery in 2024, since the client who requested it never tested the delivered product. ([7:13](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=433s), confidence: stated)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agentic retrieval](../concepts/agentic-retrieval.md)
- [latency budgets](../concepts/latency-budgets.md)
- [model routing](../concepts/model-routing.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [vision-language models](../concepts/vision-language-models.md)
- [web data infrastructure](../concepts/web-data-infrastructure.md)

