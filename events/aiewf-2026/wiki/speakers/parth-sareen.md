---
title: "Parth Sareen"
type: "speaker"
slug: "parth-sareen"
company: "Ollama"
talk_count: 1
---

# Parth Sareen

**Ollama**

## Talks

- [Compression at the Edge](../talks/compression-at-the-edge.md) (Local AI, co-presented)

## Scheduled Sessions

- **Compression at the Edge** &middot; Day 4 — Session Day 3 &middot; 2:25pm-2:45pm &middot; Track 4
- **Compression at the Edge** &middot; Day 4 — Session Day 3 &middot; 2:50pm-3:10pm &middot; Track 4

## Concepts

- [knowledge distillation](../concepts/knowledge-distillation.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [local inference](../concepts/local-inference.md)
- [mechanistic interpretability](../concepts/mechanistic-interpretability.md)
- [model routing](../concepts/model-routing.md)
- [quantization](../concepts/quantization.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "shrinking something without losing information. But there's absolutely zero free lunch. So at the end of the day, you still spend on something whether it's latency or uh quality"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [1:46](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=106s)

> "the way I think about is same cost more intelligence. So compression accelerates and enables to give like u like a quick example originally we started with training in FP32 right and now we are talking about FP4"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [2:29](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=149s)

> "you can make it 86% smaller. Um but with tricks of quantization it will not become 86%. So it's not 86% dumber"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [3:15](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=195s)

> "if you quantize some layers to you know higher precision and you leave most of the layers in like one bit or two bit and some you know very important layers is 16 bit you can still recover 76% of all accuracy"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [3:15](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=195s)

> "the first layer is actually very important and then the last layer is also very important but then the middle layers are kind of useless"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s)

> "there is a super weights paper which shows that if you quantize one number just one of the entire model your model becomes 20% dumber"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [14:03](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=843s)

> "with FP4 we target for less than 1% accuracy degradation overall on all a benchmarks"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [14:35](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=875s)

> "In in the case of FP4, you choose 16 elements and you can share one scaling fac one one extra um FP8 number between these 16 elements"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [16:55](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1015s)

> "there's so many things that I feel can't be captured by a uh model optimizer or after quantizing it or you know certain benchmarks and it's literally me you know running through putting it in cloud code or something and running the model it's like no it doesn't feel just right"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [18:32](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1112s)

> "I think benchmarking often times only work for the verifiable tasks rather than the, you know, the Vive itself."
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [19:30](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1170s)

> "there was a paper last year by um singal I think from cohhere uh that showed that arenas are very much hacked"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [19:30](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1170s)

> "they show that the bigger model quantized to 4bit is actually much better um than a 35 billion 16 bit"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [22:50](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1370s)

> "even if you have a big one and you compress it down you'll probably get like five tokens to 10 tokens per second if you don't have enough GPU power. Um and for the small ones you can get 200 tokens per second"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [23:40](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1420s)

> "we sometimes leave it in higher precision um as a default just because we actually want people to have a better experience"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [34:39](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2079s)

> "for medium and large models PDQ works out of the box very easy relatively super easy to do. Uh then if it is smaller model say like you know less than 20B size model we have to do some uh quantization aware distillation etc to recover accuracy"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [30:36](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1836s)

> "If we if we train if we do QA with wrong data it uh it most commonly breaks the model rather than helping it."
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [31:20](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1880s)

> "if you quantize the linear attention layers okay it looks like it's doing good but then when you do long context benchmarks you know when you actually use the model in real production it becomes gibberish"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [36:14](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2174s)

> "in terms of weight compression we might be able to go to like one maybe two or three bit more but in terms of u quantization alone we might be like close like close to the par optimality"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [39:54](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2394s)

> "quantization does not degrade accuracy that much but spec uh sparity causes accuracy degradation a bit more"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [40:43](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2443s)

> "So KOD is the distance between the uncontized version which is Bflat 16 and your quantized version. And you can calculate some sort of distance between the quantized version and the uncquantized version. And your goal is to make the distance zero and the size smaller."
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [44:21](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2661s)

