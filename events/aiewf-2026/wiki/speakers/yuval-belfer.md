---
title: "Yuval Belfer"
type: "speaker"
slug: "yuval-belfer"
role: "Sr. Developer Advocate"
company: "AI21"
talk_count: 1
---

# Yuval Belfer

**Sr. Developer Advocate &middot; AI21**

Yuval is a Senior Developer Advocate at AI21 Labs, where he helps engineers go from "it works in the demo" to "it works in production." He hosts the YAAP podcast (Yet Another AI Podcast) and teaches applied GenAI on various programs. His work spans RAG, fine-tuning, agents, and evaluation (or Yuval-uation, if you're nasty).

[LinkedIn](https://linkedin.com/in/yuval-belfer)

## Talks

- [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md) (Search & Retrieval, co-presented)

## Scheduled Sessions

- **Stop Chunking Like It's 2022** &middot; Day 2 — Session Day 1 &middot; 3:20pm-3:40pm &middot; Track 3
- **Two Bugs That Hid in Plain Sight: A vLLM Debugging Detective Story** &middot; Day 4 — Session Day 3 &middot; 3:20pm-3:40pm &middot; Track 9

## Concepts

- [benchmark contamination](../concepts/benchmark-contamination.md)
- [benchmark design](../concepts/benchmark-design.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "at this moment the state in the industry is counting the number of right answers. That actually has a name. It's classical test theory. And we have by far better tools to do that."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [0:02](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=2s)

> "We are saying that every question is equally important. They should weigh the same, which is kind of insane if you think about that."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [1:17](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=77s)

> "The B parameter is going to be the difficulty of each one of them, and we're going to create a function for each question. That function maps the LLM intelligence, okay? To the probability of getting that answer right"
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [1:56](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=116s)

> "item of B equal zero means that is going to be average. Half of the um models in my data set are going to be able to answer that question 50% of the time."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [4:18](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=258s)

> "Here is going to be on the left side Cloud Opus 4.1, yeah? That has 245 right answers. On the other side we are going to have Gemini 3 Pro, which has 247"
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [6:38](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=398s)

> "if you use item response theory, you can see that the difference between all of them is almost one standard deviation. That means Gemini 3 Pro is by far more intelligent."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [6:38](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=398s)

> "counting the number of right answers is is not a good approach because I can create benchmarks that are not calibrated and even if I get a lot of right answers, I'm not more intelligent than other models."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [6:38](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=398s)

> "you can see that we have items that correlates uh the other way around, that better models are actually getting that answer wrong, which makes no sense."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [9:05](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=545s)

> "The gold answer, the answer that is on the benchmark, is 583, which is the total people killed passengers plus crew. But the right answer, if you pay attention, I'm asking only about passengers, which is another number."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [9:44](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=584s)

> "we're going to get that around 97 items compared with 484. That's almost 5x. We are going to have the same ranking than before or almost the same ranking as before."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [11:10](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=670s)

> "We are like assuming that more questions uh means better estimation, which is not true."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [11:57](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=717s)

> "GPQA, which is a extremely well-designed uh data set, the benchmark here, as you can see, even if you pick at random, you're going to get more or less the same result."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [12:41](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=761s)

> "We can actually find out if we are leaking information, if we are overfitting with the benchmark, and other kinds of contaminations."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [13:25](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=805s)

> "if your for whatever reason your inference platform is not actually running the models or the quantization is actually wrong, you're going to observe things like that, behaviors that are not expected"
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [15:42](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=942s)

> "I'm going to pick uh one individual set. I'm going to call that fingerprint set that I'm going to show only to that specific organization."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [17:00](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1020s)

> "So this is not bulletproof, but this is a extremely good technique that you can use to protect your benchmarks."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [17:45](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1065s)

> "we can find out that there are few items that are better for closed weight of models and better for open weights models. I'm not going to show the items because I don't want to leak them on the internet"
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [19:13](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1153s)

> "Also, we can observe that between distillations and its base model, which could be extremely interesting if you want to detect distillation of your model uh without consent."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [20:39](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1239s)

> "I think we can improve a lot how we benchmark LLMs with very basic maths here."
>
> — [Stop Evaluating Models Like It's the 50s](../talks/stop-evaluating-models-like-its-the-50s.md), [21:29](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1289s)

