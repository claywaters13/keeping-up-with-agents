---
title: "Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub"
type: "talk"
slug: "serving-2-million-models-without-melting-scaling-the-hugging-face-hub"
track: "AI Architects: Show my Workflow"
org: "Hugging Face"
day: "Day 2 — Session Day 1"
room: "Leadership 2"
video_id: "lyL5QhgIOxc"
duration_sec: 1299
word_count: 1956
speakers: ["Arek Borucki"]
---

# Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub

**Speakers:** [Arek Borucki](../speakers/arek-borucki.md)

**Org:** Hugging Face

**Track:** AI Architects: Show my Workflow &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Leadership 2 &nbsp;|&nbsp; **Duration:** 21m 39s

[Watch on YouTube](https://www.youtube.com/watch?v=lyL5QhgIOxc)

## Summary

Arek Borucki, a machine learning platform and database engineer at Hugging Face, walks through the infrastructure that lets the Hub serve 14 million users and 3 million public models — roughly a 150x growth in models over a few years. The core argument is that scale broke search first: regex queries over MongoDB were fine at 20,000 models and unusable at 3 million, so the team moved to precomputed tokens stored on insert, a denormalized read-only collection, and Atlas Search (Apache Lucene) with autocomplete, sorted by a trending score recomputed every five minutes. He then details the data layer separation (MongoDB holds all metadata, S3 holds model artifacts), a seven-node replica set with read routing rules and a hidden analytics node, and the upcoming move to sharding. On the compute side, the Hub scales from 10 to 500 pods via HPA plus Cast AI for node autoscaling, with a planned migration to KEDA so scaling reacts to request rate rather than CPU. Worth watching if you operate a metadata-heavy, read-dominated platform and want a concrete, numbers-first case study rather than architecture generalities.

## Key Points

- Hugging Face serves more than 14 million users, 3 million public models, 1 million datasets, and 50,000 organizations, with over 30% of the Fortune 500 using it in AI workflows.
- Search was the first thing to break at scale: MongoDB find with a regex operator over a search-tokens array worked while the dataset was small but did not scale, forcing a switch to Atlas Search backed by Apache Lucene.
- The team shifts work to write time rather than query time — model names like 'meta-llama/Llama-3.1-8B' are split into prefix tokens on insert and stored as an array in the document, so autocomplete matches instantly.
- Reads and listings are served from a separate denormalized copy of the data rather than the main repo collection, and results are ranked by a trending score (downloads plus likes over roughly the last seven days) recomputed every five minutes.
- Tail latency is the operative metric: at 14 million users, 1% of traffic hitting slow search is 140,000 people, so the team optimizes P99 rather than P50.
- MongoDB stores everything about the models — users, repositories, buckets, spaces, configuration, billing, access control — but never the model weights, which live in cloud object storage such as S3, letting metadata, binary storage, and compute scale independently.
- Read traffic is deliberately partitioned across a seven-node replica set: only strongly-consistent queries stay on the primary, heavy aggregations and change streams go to secondaries, and ad hoc or reporting queries go to a hidden node invisible to the driver.
- Sharding is the next step because a single replica set will not be enough; unlike a replica set, each shard holds only part of the dataset with its own primary and secondaries, scaling CPU, memory, storage, reads, and writes together.
- Compute scaling has two layers — HPA scales the Hub deployment from 10 to 500 pods, and Cast AI adds Kubernetes nodes when pods are pending for lack of capacity — with a planned migration from HPA to KEDA so scaling follows application metrics like requests per second instead of CPU and memory alone.

## Notable Quotes

> "Just to give you some perspective, few years ago we had 20,000 models. Today 3 million. It is around 150x increase in just last couple of years."
>
> — [1:26](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=86s) &middot; *anchors the entire talk in a single growth number*

> "In 2022, we had 10K. In 2024, 100K. Less than a year ago, we had 500K. Today, 1 million."
>
> — [2:59](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=179s) &middot; *dataset growth curve, showing models are not the only scaling axis*

> "All this data must be stored, indexed, and also must be searchable. And that's the hardest part."
>
> — [2:59](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=179s) &middot; *names searchability, not storage, as the real bottleneck*

> "At 20,000 models, any query is fast. Even without an index, trust me, no one would notice."
>
> — [2:59](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=179s) &middot; *crisp statement that scale, not design, exposed the problem*

> "With 14 million users, even 1% is a not small number. It is 140,000 of people hitting slow search at scale. P99 is much more important than P50"
>
> — [4:17](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=257s) &middot; *the tail-latency argument stated with arithmetic*

> "MongoDB does not store the models themselves. It stores everything about the models."
>
> — [5:51](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=351s) &middot; *the architectural distinction people most often get wrong*

> "This separation of concern let us scale metadata independently from binary storage and compute independently from both."
>
> — [7:31](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=451s) &middot; *states the payoff of the metadata/blob split*

> "We tokenize model names on insert time, not at query time."
>
> — [7:31](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=451s) &middot; *the core write-time-versus-query-time tradeoff*

> "This solution was working well as long as data set was small. Reax doesn't scale well."
>
> — [9:58](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=598s) &middot; *explicit verdict on regex search*

> "this solution is much more efficient and is so far scale well, so we don't have any more latency issues in our search bar."
>
> — [11:15](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=675s) &middot; *reports the outcome of the Lucene migration*

> "First all queries which doesn't require the latest data goes to secondaries. Only queries that must have strong consistency stay on primary"
>
> — [13:56](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=836s) &middot; *the consistency rule that governs their read routing*

> "Aggregations pipelines that scan large amount of data, sort, group or transform the data should not go on primary. They are heavy. Secondaries are better placed for them."
>
> — [15:07](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=907s) &middot; *concrete prescription for where heavy analytical work belongs*

> "The pattern is simple. Primary should focus on what only primary can do. Anything else can be pushed to different machines."
>
> — [16:19](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=979s) &middot; *the talk's most portable design heuristic*

> "The key difference between replica set cluster and sharded cluster is replica set keep full data set on each node."
>
> — [16:19](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=979s) &middot; *clean framing of why replication alone stops working*

> "There is also shard key which must be selected. This is not trivial operation but this talk is not about choosing short key."
>
> — [17:31](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1051s) &middot; *flags the hardest part of sharding while explicitly scoping it out*

> "Our deployment hub deployment can scale from 10 to 500 bots depends of on the traffic."
>
> — [18:37](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1117s) &middot; *concrete autoscaling range for the Hub*

> "HPA scale only based on CPU and memory. KDA scale on real application metrics like request per second or event loop utilization."
>
> — [19:44](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1184s) &middot; *the stated reason for migrating autoscalers*

> "This is what scaling medium models is really about. Keeping the user experience simple no matter how complex it gets under the hood."
>
> — [20:57](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1257s) &middot; *the closing thesis of the talk*

## Positions

- Regex-based search in MongoDB does not scale, and full-text search on Apache Lucene (Atlas Search) is the right replacement once the dataset grows large. ([9:58](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=598s), confidence: stated)
- P99 latency matters more than P50 for user-facing search at Hugging Face's scale. ([4:17](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=257s), confidence: stated)
- Tokenization should happen at insert time rather than query time so autocomplete can match instantly. ([7:31](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=451s), confidence: stated)
- Reads and listings should be served from a separate denormalized collection rather than the primary source-of-truth repo collection. ([7:31](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=451s), confidence: stated)
- Model artifacts belong in object storage while metadata belongs in a database, so the two can scale independently. ([7:31](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=451s), confidence: stated)
- The database primary should only handle writes and queries requiring strong consistency; everything else — heavy aggregations, change streams, ad hoc and reporting queries — should be pushed to secondaries or a hidden node. ([16:19](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=979s), confidence: stated)
- A single MongoDB replica set will soon be insufficient for Hugging Face's growth, making sharding the necessary next step. ([16:19](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=979s), confidence: stated)
- Choosing a shard key is a non-trivial decision. ([17:31](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1051s), confidence: stated)
- Two-layer autoscaling (pod-level plus node-level via Cast AI) keeps the Hub healthy without manual intervention and without overprovisioning, making it cost effective. ([18:37](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1117s), confidence: stated)
- KEDA is superior to HPA for this workload because scaling on application metrics like request rate captures load that CPU and memory thresholds miss, such as a pod with low CPU but a high request queue. ([19:44](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1184s), confidence: stated)
- Slow search causes users to leave for alternatives, which is why search latency is treated as a first-order infrastructure priority. ([4:17](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=257s), confidence: stated)
- Good infrastructure at this scale is invisible — success means users never think about it. ([19:44](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1184s), confidence: implied)

## Concepts

- [latency budgets](../concepts/latency-budgets.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)

