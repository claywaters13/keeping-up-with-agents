---
title: "quantization"
type: "concept"
slug: "quantization"
tier: "supporting"
maturity: "consolidating"
talk_count: 7
speaker_count: 15
---

# quantization

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **7** talk(s) by **15** speaker(s)

**Definition:** Reducing numeric precision of weights or activations to cut memory and cost, and the quality tradeoffs that come with it.

*Also referred to as: post-training quantization, mixed-precision quantization, dynamic mixed-precision quantization, vector quantization, low-precision training, fp8 training kernels, kl divergence as quantization metric*

## State of Practice

Four-bit-class quantization has stopped being an experiment and become the default deployment step: NVFP4/FP4 with block scaling (16 elements sharing one FP8 scale) is targeted at under 1% aggregate benchmark degradation, mixed 2/4/8-bit schemes land production models around 2.9 bits per weight, and quantization was one of the three off-the-shelf levers (with a vLLM backend and config tuning) that produced a 10x inference gain on DGX Spark with no new research. The operative insight is that precision must be allocated non-uniformly — first and last layers, attention/QKV projections, and a handful of 'super weights' carry disproportionate signal, so uniform 86% compression destroys a model while selective compression to the same size retains ~76% of accuracy. Above roughly 20-30B parameters post-training quantization works out of the box; below that you need quantization-aware distillation, and doing it with the wrong data breaks the model outright. The field is openly skeptical of its own evaluation methods: accuracy benchmarks and arenas are considered hackable and insensitive, KL divergence of output logits against the BF16 parent is the proposed replacement, and there is no public resource comparing the quality of community quants. Two structural questions remain live — whether weight quantization is already near Pareto optimality (with future gains coming from KV cache compression and sparsity) and whether a big quantized model or a natively tiny fine-tuned model is the right answer at the edge.

## Consensus

### Sub-8-bit quantization is production-viable today, not an experimental quality sacrifice — FP4-class formats are being shipped with accuracy loss targeted under 1%.

Support: **4** talk(s)

> "with FP4 we target for less than 1% accuracy degradation overall on all a benchmarks"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [14:35](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=875s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Desktop Frontier](../talks/the-desktop-frontier.md)

### Precision must be allocated non-uniformly across the model; a mixed-precision scheme that keeps a few sensitive tensors high is what makes aggressive compression work at all.

Support: **3** talk(s)

> "if you quantize some layers to you know higher precision and you leave most of the layers in like one bit or two bit and some you know very important layers is 16 bit you can still recover 76% of all accuracy"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [3:15](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=195s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### The constraint quantization actually buys against is memory — DRAM/VRAM footprint and bytes read per token — not arithmetic throughput.

Support: **4** talk(s)

> "So here that kind of jumps up to 45 tokens per second because we need to read less uh from memory each time."
>
> — [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [14:44](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=884s)

Supporting talks: [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

### Standard accuracy benchmarks are an unreliable acceptance test for a compressed model; validation requires distributional comparison to the full-precision parent plus hands-on use in the real harness.

Support: **3** talk(s)

> "there's so many things that I feel can't be captured by a uh model optimizer or after quantizing it or you know certain benchmarks and it's literally me you know running through putting it in cloud code or something and running the model it's like no it doesn't feel just right"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [18:32](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1112s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### Most production workloads do not need frontier-precision, frontier-scale models; the correct default is the smallest/most-compressed model that clears your quality bar.

Support: **4** talk(s)

> "You don't need the top model for every single use case and in fact most use cases you don't"
>
> — [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [13:39](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=819s)

Supporting talks: [Frontier results, on device](../talks/frontier-results-on-device.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

## Disagreements

### For a fixed device budget, should you quantize a large model down or train/fine-tune a natively small model up?

| Position A | Position B |
|---|---|
| Train big and quantize: a 120B model at 4-bit is meaningfully more capable than a 35B at BF16 for the same footprint, and users would rather get one mid-sized checkpoint they quantize themselves than a natively smaller release.<br>*[Compression at the Edge](../talks/compression-at-the-edge.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* | Compressed large models are still too big and too slow for the real device population; a 50M-500M model fine-tuned on 10k-10M synthetic samples matches a 2-4B model on a fixed task, and you should prototype big but deploy a small specialized model.<br>*[Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* |

*Why it matters: It decides whether your edge roadmap is a quantization/kernel problem or a synthetic-data-and-fine-tuning problem, and whether you ship one general checkpoint or a fleet of task-specific ones with the retraining and redistribution cost that implies.*

### Is weight quantization close to exhausted as a source of efficiency gains?

| Position A | Position B |
|---|---|
| Weight quantization is near Pareto optimality — maybe one to three more bits of headroom — and it only works at all because today's models are undertrained; future gains must come from KV cache compression and sparsity.<br>*[Compression at the Edge](../talks/compression-at-the-edge.md)* | Compression and capability density are compounding on a fast, predictable curve (~50% fewer parameters for equivalent capability every 3.5 months), so better compression will keep pulling frontier-class models onto consumer hardware and make local the default.<br>*[The Desktop Frontier](../talks/the-desktop-frontier.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* |

*Why it matters: If the headroom is nearly gone, roadmaps should shift investment to KV cache, sparsity, and architecture; if the curve holds, waiting 18 months is a legitimate substitute for engineering effort.*

### Are low-precision formats trustworthy inside the training loop, or only at inference?

| Position A | Position B |
|---|---|
| Low-precision training is ready and economically transformative — NVFP4 training as demonstrated by Nemotron 3 Ultra makes fine-tuning and specialized model creation cheap enough to be viable now, and quantization-aware distillation is the standard recovery path for sub-20B models.<br>*[The Desktop Frontier](../talks/the-desktop-frontier.md), [Compression at the Edge](../talks/compression-at-the-edge.md)* | Low-precision training paths fail silently and must be distrusted by default: open-source FP8 kernels carried a race condition corrupting ~0.5% of gradients, and BF16 accumulation in the tensor-parallel unembedding halted convergence until moved to FP32.<br>*[The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)* |

*Why it matters: Whether you adopt FP8/FP4 training as-is or build hash checks, FP32 fallbacks for sensitive accumulations, and large-scale validation runs first is the difference between a cheap recipe and a run that quietly fails to converge at scale.*

## Practical Guidance

**Do:**

- Keep the first and last layers plus attention/QKV projections at high precision while pushing middle layers to 1-2 bits
- Use a mixed 2/4/8-bit scheme to hit ~2.9 bits per weight when a 2B-class model must fit a device with ~4GB of usable DRAM after KV cache, runtime, and OS
- Score quantized checkpoints by KL divergence between the quantized and BF16 output logits — minimize distance while minimizing size — rather than by benchmark accuracy
- Run explicit long-context evals after quantizing, because short benchmarks look fine on models whose long-context behavior is already broken
- Assume post-training quantization works out of the box above ~20-30B parameters, and budget for quantization-aware distillation below ~20B
- For FP4, share one FP8 scaling factor across each block of 16 elements
- For a fixed disk or VRAM budget, prefer the larger model at 4-bit over the smaller model at BF16
- Ship a higher-precision default quant when the user experience matters more than the last increment of size
- In low-precision training, hash weights across data-parallel replicas and hard-crash on mismatch, and keep the tensor-parallel unembedding accumulation in FP32
- Fix structural and length failures in a small model with deterministic post-processing in the harness instead of escalating to a bigger model
- Run regression evals continuously, like CI, so a prompt or checkpoint swap can't silently degrade behavior

**Avoid:**

- Compressing all layers uniformly — an 86%-smaller model built that way is useless, not 86% worse
- Trusting accuracy benchmarks, public arenas, or LLM judges to certify a quantized model; judges favor models from their own family and arenas have been shown to be gameable
- Quantizing linear attention layers — short benchmarks pass and production long-context output turns to gibberish
- Running quantization-aware training on the wrong data, which more commonly breaks the model than helps it
- Treating sparsity as an equivalent lever to quantization; despite hardware support it degrades accuracy noticeably more
- Validating a low-precision training recipe only at 33B and assuming the numerics hold at hundreds of billions of parameters
- Relying on replica hash checks to catch forward/backward race conditions — real runs have no redundancy to compare against
- Shipping distilled task-specific models into mobile apps where every capability change means pushing a new 1-2GB download over users' data plans
- Picking a model on peer recommendation instead of latency and quality evals

## Notable Outliers

- Quantizing a single 'super weight' — one number in the entire model — makes the model roughly 20% dumber. ([Compression at the Edge](../talks/compression-at-the-edge.md), [14:03](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=843s))
- Compression only works because current models are undertrained; train on ~300 trillion tokens and the quantization headroom largely disappears. ([Compression at the Edge](../talks/compression-at-the-edge.md), [12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s))
- Weight quantization is nearing Pareto optimality, so the next round of gains has to come from KV cache compression and sparsity instead. ([Compression at the Edge](../talks/compression-at-the-edge.md), [39:54](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2394s))
- Widely used open-source FP8 GEMM kernels contain a race condition that silently replaces ~0.5% of gradients with random values. ([The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [14:32](https://www.youtube.com/watch?v=KhYifX22yhE&t=872s))
- No comprehensive public resource exists for comparing the quality of community-produced quantized checkpoints. ([Compression at the Edge](../talks/compression-at-the-edge.md), [44:21](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2661s))
- Given the choice, users preferred a single mid-sized checkpoint they could quantize themselves over natively smaller model releases. ([Compression at the Edge](../talks/compression-at-the-edge.md), [28:05](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=1685s))
- Architectural diversity among open models is net positive even though it materially complicates quantization tooling. ([Compression at the Edge](../talks/compression-at-the-edge.md), [36:48](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2208s))

## All Talks

- [Compression at the Edge](../talks/compression-at-the-edge.md)
- [Frontier results, on device](../talks/frontier-results-on-device.md)
- [On AI and Knowledge](../talks/on-ai-and-knowledge.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)
- [The Desktop Frontier](../talks/the-desktop-frontier.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)
- [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Alex Cheema](../speakers/alex-cheema.md)
- [Asma Beevi](../speakers/asma-beevi.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Cormac Brick](../speakers/cormac-brick.md)
- [Daniel Han](../speakers/daniel-han.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Marah Abdin](../speakers/marah-abdin.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Merve Noyan](../speakers/merve-noyan.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Parth Sareen](../speakers/parth-sareen.md)
- [RL Nabors](../speakers/rl-nabors.md)
- [Robert McHardy](../speakers/robert-mchardy.md)

