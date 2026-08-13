---
title: "Chris Alexiuk"
type: "speaker"
slug: "chris-alexiuk"
role: "Sr. Product Research Engineer"
company: "NVIDIA"
talk_count: 2
---

# Chris Alexiuk

**Sr. Product Research Engineer &middot; NVIDIA**

Chris Alexiuk is a Sr. Product Research Engineer at NVIDIA, he is obsessed with everything and anything about large language models as well as Dungeons & Dragons.

[LinkedIn](https://www.linkedin.com/in/csalexiuk)

## Talks

- [Compression at the Edge](../talks/compression-at-the-edge.md) (Local AI, co-presented)
- [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md) (Local AI, co-presented)

## Scheduled Sessions

- **Local Models: Trust, Control, Optimization** &middot; Day 4 — Session Day 3 &middot; 1:30pm-1:50pm &middot; Track 4
- **Local Models: Trust, Control, Optimization** &middot; Day 4 — Session Day 3 &middot; 1:55pm-2:15pm &middot; Track 4
- **Compression at the Edge** &middot; Day 4 — Session Day 3 &middot; 2:25pm-2:45pm &middot; Track 4
- **Compression at the Edge** &middot; Day 4 — Session Day 3 &middot; 2:50pm-3:10pm &middot; Track 4

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [data flywheels](../concepts/data-flywheels.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [local inference](../concepts/local-inference.md)
- [mechanistic interpretability](../concepts/mechanistic-interpretability.md)
- [model portability](../concepts/model-portability.md)
- [model routing](../concepts/model-routing.md)
- [post-training](../concepts/post-training.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [quantization](../concepts/quantization.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [small language models](../concepts/small-language-models.md)

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

> "we kind of have this mantra that like faster models are smarter models"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [5:06](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=306s)

> "These models are inherently trustworthy. You know much more about what's going on when you hit and talk to these models than you ever will what's going on when you hit an arbitrary API."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [8:04](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=484s)

> "You had a tremendous number of enterprises and developers and companies start going to these new Chinese models because they could trust that they would always have access to them."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [9:16](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=556s)

> "take an open model and like specialize it to automate finance within like a week or two to get like better performance than like Opus at a fraction of the cost of Haiku"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [13:39](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=819s)

> "If you go back to trust, it's how you can make your CFO trust you by knowing exactly how much something's going to cost all the time."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [14:13](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=853s)

> "You can look at it, you know, the difference between GPT-4 when it first launched and GPT-5.5 is is is much, much cheaper per token, but at the same time the amount of tokens in an individual session has gone up exponentially as well."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [14:13](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=853s)

> "And if they're doing that, if their off-the-shelf GPT-5 isn't good enough for, you know, their Atlas web browser, why should it be good enough for our apps?"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [16:19](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=979s)

> "We're we're leaving a lot of like a lot of important capability on the table because we're just not we're not fitting the models into the harness"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [18:04](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1084s)

> "if you kind of want to build the next like cloud code, the next like cursor or perplexity, I think the easiest way to get started is like take the best open model like and and then post rate on your harness like that you care about"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [19:00](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1140s)

> "as much as using open models is like owning your stack, owning your intelligence, it's also owning your outputs, right? Owning your data."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [21:20](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1280s)

> "we wanted to make sure there's a license that exists that not encourages you, but makes it crystal clear that it is it is permitted it is permissible."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [21:57](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1317s)

> "most people probably do not need frontier level intelligence for like 90% of their tasks"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [26:45](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1605s)

> "And I think this is something you don't obviously get with the closed APIs, where like they have like a huge margin on top. Like they might drive down the optimization, but then might not pass through those savings."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [26:45](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1605s)

> "And open models let you choose those one or two things and then make the model just very good at those things at the expense of at the expense sorry of almost everything else."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [27:17](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1637s)

> "I think it's, in fact, not possible to do it behind closed doors cuz you're shutting too many people, uh, that could make that one small contribution, uh, out of the room."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [29:21](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=1761s)

> "I think we'll like in in 12 months I think it's pretty likely that we'll have like better than fable metals level capabilities and open models."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [34:10](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=2050s)

> "this is probably going to be the most consequential year for like the future of how AI gets distributed"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [35:18](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=2118s)

> "That's probably been the most frustrating thing about the last couple weeks is that all of these conversations around capabilities and who gets to use them and who doesn't have been happening behind closed doors."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [36:45](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=2205s)

> "I think that we will not be needing to go to an API for most of the tasks that we all do each day with AI. I think it's likely to assume that you'll be running a model that is sufficiently capable in let's call it day-to-day work on your on your MacBook within the year."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [38:18](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=2298s)

> "I think you're going to buy computers with agent operating systems on them instead of traditional operating systems."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [39:06](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=2346s)

> "You can run a 4 billion parameter model on your on your phone right now that is way more useful than GPT-4 was when it came out."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [40:56](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=2456s)

