---
title: "Compression at the Edge"
type: "talk"
slug: "compression-at-the-edge"
track: "Local AI"
org: "Unsloth, HuggingFace, Ollama"
day: "Day 4 — Session Day 3"
room: "Track 4"
video_id: "J4_jCrTxMkk"
duration_sec: 2760
word_count: 8481
speakers: ["Asma Beevi", "Chris Alexiuk", "Daniel Han", "Merve Noyan", "Parth Sareen"]
---

# Compression at the Edge

**Speakers:** [Asma Beevi](../speakers/asma-beevi.md), [Chris Alexiuk](../speakers/chris-alexiuk.md), [Daniel Han](../speakers/daniel-han.md), [Merve Noyan](../speakers/merve-noyan.md), [Parth Sareen](../speakers/parth-sareen.md)

**Org:** Unsloth, HuggingFace, Ollama

**Track:** Local AI &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 4 &nbsp;|&nbsp; **Duration:** 46m 00s

[Watch on YouTube](https://www.youtube.com/watch?v=J4_jCrTxMkk)

## Summary

A panel moderated by NVIDIA's Chris Alex with participants from Unsloth (Daniel), NVIDIA Model Optimizer, Hugging Face (Merve), and Ollama (Parth) on why quantization and compression are what actually make frontier-scale open models usable locally. The core argument is that a large model quantized aggressively beats a natively small model of the same on-disk size, so the future is 'train huge, then compress' rather than 'train small.' Panelists get concrete about how this works — layer-wise sensitivity, dynamic/mixed-precision quantization, NVFP4's micro-block scaling, and the fact that some layers (linear attention, QKV projections) simply cannot be quantized without silently breaking long-context behavior. They also concede the weak spot: evaluating quantized models is mostly benchmark-running plus vibes, with KL divergence against the BF16 logits offered as a better metric, and no comprehensive public resource exists for comparing the quality of community quants. Worth watching if you deploy local models and want to know which compression tradeoffs are real versus folklore.

## Key Points

- Compressing a model by 86% does not make it 86% worse — Unsloth's dynamic quantization keeps a few critical layers at high precision while pushing most layers to one or two bits, recovering roughly 76% of accuracy on a model shrunk from 1.5TB to 250GB.
- Layer importance is highly uneven: first and last layers matter a lot, middle layers are comparatively expendable, and a 'super weights' paper shows quantizing a single specific number can make a model 20% dumber.
- The reason compression works at all is that models are undertrained relative to their parameter count — many weights sit near zero and can be zeroed out, which implies compression headroom may shrink if training token counts grow by orders of magnitude.
- NVIDIA's NVFP4 is not just a 4-bit float but a micro-block-scaled format where every 16 elements share an extra FP8 scaling factor, and NVIDIA targets under 1% accuracy degradation across benchmarks with it.
- Post-training quantization works out of the box for models above roughly 20-30B parameters, but smaller models need quantization-aware distillation, which is increasingly painful because modern models are multi-stage RL-trained with multiple expert teachers and the wrong training data breaks the model rather than helping it.
- Given equal on-disk size, a 120B model at 4-bit outperforms a 35B model at 16-bit, which argues for a 'train big then quantize' path over training natively small models — though small models still win on tokens/sec.
- The proliferation of architectures (linear attention, sliding-window, hybrid, MoE) has made quantization substantially harder: quantizing linear attention layers looks fine on standard benchmarks but produces gibberish under long context in production.
- Evaluation is the unsolved part — benchmarks only capture verifiable tasks, arenas are hackable, and Unsloth advocates KL divergence between BF16 and quantized output logits as a more reliable signal than accuracy benchmarks with their sampling and averaging problems.
- Beyond weight quantization, the panel expects the field to broaden into KV cache compression and dynamic activation sparsity (a Rubin hardware feature), since weight quantization alone may be near Pareto-optimal at 1-3 bits.

## Notable Quotes

> "shrinking something without losing information. But there's absolutely zero free lunch. So at the end of the day, you still spend on something whether it's latency or uh quality"
>
> — [1:46](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=106s) &middot; *states the core tradeoff framing the whole panel*

> "the way I think about is same cost more intelligence. So compression accelerates and enables to give like u like a quick example originally we started with training in FP32 right and now we are talking about FP4"
>
> — [2:29](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=149s) &middot; *compact statement of NVIDIA's thesis plus the 8x historical arc*

> "you can make it 86% smaller. Um but with tricks of quantization it will not become 86%. So it's not 86% dumber"
>
> — [3:15](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=195s) &middot; *the panel's headline claim, stated numerically*

> "if you quantize some layers to you know higher precision and you leave most of the layers in like one bit or two bit and some you know very important layers is 16 bit you can still recover 76% of all accuracy"
>
> — [3:15](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=195s) &middot; *names the actual dynamic-quantization recipe and its measured recovery*

> "the first layer is actually very important and then the last layer is also very important but then the middle layers are kind of useless"
>
> — [12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s) &middot; *the load-bearing heuristic behind mixed-precision quantization*

> "there is a super weights paper which shows that if you quantize one number just one of the entire model your model becomes 20% dumber"
>
> — [14:03](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=843s) &middot; *striking counterexample to uniform quantization, with a number*

> "with FP4 we target for less than 1% accuracy degradation overall on all a benchmarks"
>
> — [14:35](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=875s) &middot; *NVIDIA's stated acceptance threshold for shipping quantized checkpoints*

> "In in the case of FP4, you choose 16 elements and you can share one scaling fac one one extra um FP8 number between these 16 elements"
>
> — [16:55](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1015s) &middot; *the actual mechanism of NVFP4, not just the name*

> "there's so many things that I feel can't be captured by a uh model optimizer or after quantizing it or you know certain benchmarks and it's literally me you know running through putting it in cloud code or something and running the model it's like no it doesn't feel just right"
>
> — [18:32](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1112s) &middot; *concedes that benchmarks miss the failure modes practitioners actually hit*

> "I think benchmarking often times only work for the verifiable tasks rather than the, you know, the Vive itself."
>
> — [19:30](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1170s) &middot; *names the eval gap directly*

> "there was a paper last year by um singal I think from cohhere uh that showed that arenas are very much hacked"
>
> — [19:30](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1170s) &middot; *closes off the obvious alternative to benchmarks*

> "they show that the bigger model quantized to 4bit is actually much better um than a 35 billion 16 bit"
>
> — [22:50](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1370s) &middot; *the panel's most consequential and contestable claim about model selection*

> "even if you have a big one and you compress it down you'll probably get like five tokens to 10 tokens per second if you don't have enough GPU power. Um and for the small ones you can get 200 tokens per second"
>
> — [23:40](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1420s) &middot; *the throughput counterargument to 'always compress the big model'*

> "we sometimes leave it in higher precision um as a default just because we actually want people to have a better experience"
>
> — [34:39](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2079s) &middot; *Ollama's product-level rule for when not to quantize*

> "for medium and large models PDQ works out of the box very easy relatively super easy to do. Uh then if it is smaller model say like you know less than 20B size model we have to do some uh quantization aware distillation etc to recover accuracy"
>
> — [30:36](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1836s) &middot; *gives the practical size threshold where PTQ stops being enough*

> "If we if we train if we do QA with wrong data it uh it most commonly breaks the model rather than helping it."
>
> — [31:20](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1880s) &middot; *warns that QAT is not a safe default without the original data*

> "if you quantize the linear attention layers okay it looks like it's doing good but then when you do long context benchmarks you know when you actually use the model in real production it becomes gibberish"
>
> — [36:14](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2174s) &middot; *concrete architecture-specific failure that standard evals hide*

> "in terms of weight compression we might be able to go to like one maybe two or three bit more but in terms of u quantization alone we might be like close like close to the par optimality"
>
> — [39:54](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2394s) &middot; *a falsifiable forecast that weight quantization is nearing its limit*

> "quantization does not degrade accuracy that much but spec uh sparity causes accuracy degradation a bit more"
>
> — [40:43](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2443s) &middot; *explains why sparsity has lagged quantization in adoption despite hardware support*

> "So KOD is the distance between the uncontized version which is Bflat 16 and your quantized version. And you can calculate some sort of distance between the quantized version and the uncquantized version. And your goal is to make the distance zero and the size smaller."
>
> — [44:21](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2661s) &middot; *proposes a concrete alternative to benchmark-based quant evaluation*

## Positions

- A model compressed to 14% of its size retains roughly 76% of its accuracy if the right layers are kept at high precision. ([3:15](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=195s), confidence: stated)
- Uniformly compressing 86% of a model's weights would make it 100% useless, not 86% worse — selective layer choice is what makes compression viable. ([12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s), confidence: stated)
- Compression works because current models are undertrained; if models were trained on ~300 trillion tokens, compression headroom would largely disappear. ([12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s), confidence: stated)
- For a fixed disk footprint, a 120B model at 4-bit is meaningfully more capable than a 35B model at BF16. ([22:50](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1370s), confidence: stated)
- Training big and then quantizing is a better use of resources than training a small model natively. ([21:47](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1307s), confidence: stated)
- NVFP4 quantization can hold total accuracy degradation under 1% across standard benchmarks. ([14:35](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=875s), confidence: stated)
- Attention/QKV projection layers are disproportionately sensitive and should be kept at higher precision than other layers. ([15:14](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=914s), confidence: stated)
- Post-training quantization works out of the box above roughly 20-30B parameters, but sub-20B models require training-based recovery methods. ([30:36](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1836s), confidence: stated)
- Linear attention layers cannot be quantized without breaking long-context behavior, even though short benchmarks show no problem. ([36:14](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2174s), confidence: stated)
- Accuracy benchmarks are an unreliable way to evaluate quantized models; KL divergence over output logits against the BF16 model is a better metric. ([44:21](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2661s), confidence: stated)
- No comprehensive public resource currently exists for comparing the quality of community-produced quantized checkpoints. ([44:21](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2661s), confidence: stated)
- Weight quantization is approaching Pareto optimality, so future gains will come from KV cache compression and sparsity instead. ([39:54](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2394s), confidence: stated)
- Sparsity has not been broadly adopted despite NVIDIA hardware support because it degrades accuracy more than quantization does. ([40:43](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2443s), confidence: stated)
- Architectural diversity among open models is net positive even though it materially complicates quantization tooling. ([36:48](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2208s), confidence: stated)
- Most business workloads do not require frontier-level model capability, so compressed or distilled smaller models are sufficient. ([20:06](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1206s), confidence: stated)
- Users given a choice preferred a single mid-sized checkpoint they could quantize themselves over natively smaller model releases. ([28:05](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1685s), confidence: stated)

## Concepts

- [knowledge distillation](../concepts/knowledge-distillation.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [local inference](../concepts/local-inference.md)
- [mechanistic interpretability](../concepts/mechanistic-interpretability.md)
- [model routing](../concepts/model-routing.md)
- [quantization](../concepts/quantization.md)

