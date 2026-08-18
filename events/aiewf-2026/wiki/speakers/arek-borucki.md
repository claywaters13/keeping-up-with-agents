---
title: "Arek Borucki"
type: "speaker"
slug: "arek-borucki"
role: "Machine Learning Platform & Database Engineer"
company: "Hugging Face"
talk_count: 1
---

# Arek Borucki

**Machine Learning Platform & Database Engineer &middot; Hugging Face**

Arek Borucki is a Machine Learning Platform & Database Engineer at Hugging Face, where he helps keep the infrastructure behind one of the world's largest open-source AI platforms running at scale. He is the author of MongoDB in Action 8.0 and co-author of Mastering MongoDB 7.0. With over 10 years of experience in SRE, Kubernetes, AWS, GCP, and managing MongoDB in production, from 100TB+ sharded clusters to cloud-native deployments, he brings deep expertise in databases, platform engineering, and infrastructure at scale.

[LinkedIn](https://www.linkedin.com/in/arekborucki/)

## Talks

- [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md) (AI Architects: Show my Workflow)

## Scheduled Sessions

- **Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub** &middot; Day 2 — Session Day 1 &middot; 1:30pm-1:50pm &middot; Leadership 2

## Concepts

- [latency budgets](../concepts/latency-budgets.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)

## Quotes

> "Just to give you some perspective, few years ago we had 20,000 models. Today 3 million. It is around 150x increase in just last couple of years."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [1:26](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=86s)

> "In 2022, we had 10K. In 2024, 100K. Less than a year ago, we had 500K. Today, 1 million."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [2:59](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=179s)

> "All this data must be stored, indexed, and also must be searchable. And that's the hardest part."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [2:59](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=179s)

> "At 20,000 models, any query is fast. Even without an index, trust me, no one would notice."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [2:59](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=179s)

> "With 14 million users, even 1% is a not small number. It is 140,000 of people hitting slow search at scale. P99 is much more important than P50"
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [4:17](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=257s)

> "MongoDB does not store the models themselves. It stores everything about the models."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [5:51](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=351s)

> "This separation of concern let us scale metadata independently from binary storage and compute independently from both."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [7:31](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=451s)

> "We tokenize model names on insert time, not at query time."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [7:31](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=451s)

> "This solution was working well as long as data set was small. Reax doesn't scale well."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [9:58](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=598s)

> "this solution is much more efficient and is so far scale well, so we don't have any more latency issues in our search bar."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [11:15](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=675s)

> "First all queries which doesn't require the latest data goes to secondaries. Only queries that must have strong consistency stay on primary"
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [13:56](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=836s)

> "Aggregations pipelines that scan large amount of data, sort, group or transform the data should not go on primary. They are heavy. Secondaries are better placed for them."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [15:07](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=907s)

> "The pattern is simple. Primary should focus on what only primary can do. Anything else can be pushed to different machines."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [16:19](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=979s)

> "The key difference between replica set cluster and sharded cluster is replica set keep full data set on each node."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [16:19](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=979s)

> "There is also shard key which must be selected. This is not trivial operation but this talk is not about choosing short key."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [17:31](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1051s)

> "Our deployment hub deployment can scale from 10 to 500 bots depends of on the traffic."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [18:37](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1117s)

> "HPA scale only based on CPU and memory. KDA scale on real application metrics like request per second or event loop utilization."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [19:44](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1184s)

> "This is what scaling medium models is really about. Keeping the user experience simple no matter how complex it gets under the hood."
>
> — [Serving 2 Million Models Without Melting: Scaling the Hugging Face Hub](../talks/serving-2-million-models-without-melting-scaling-the-hugging-face-hub.md), [20:57](https://www.youtube.com/watch?v=lyL5QhgIOxc&t=1257s)

