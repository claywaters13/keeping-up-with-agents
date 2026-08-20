---
title: "quantization"
type: "concept"
slug: "quantization"
tier: "supporting"
maturity: "consolidating"
talk_count: 8
speaker_count: 16
---

# quantization

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **8** talk(s) by **16** speaker(s)

**Definition:** Reducing numeric precision of weights or activations to cut memory and cost, and the quality tradeoffs that come with it.

*Also referred to as: post-training quantization, mixed-precision quantization, dynamic mixed-precision quantization, vector quantization, low-precision training, fp8 training kernels, kl divergence as quantization metric*

## State of Practice

4-bit is now the default deployment precision, not an experiment: NVFP4-style block-scaled formats (16 elements sharing one FP8 scale) are held to under 1% aggregate benchmark degradation, and 4-bit-from-16-bit sits alongside speculative decoding and KV cache reuse as one of the three highest-leverage inference optimizations in production voice systems. The field has converged hard on non-uniformity — compression is viable only because layer sensitivity is wildly uneven (first and last layers and attention/QKV projections must stay high-precision while middle layers tolerate 1-2 bit), and uniformly dropping 86% of the bits yields a useless model rather than an 86%-worse one. Edge deployments push this further, mixing 2/4/8-bit to land around 2.9 bits per weight, because DRAM cost — not compute — is the binding constraint and is getting worse, not better. Evaluation is the weakest link: accuracy benchmarks and arenas are considered unreliable acceptance signals, with KL divergence over output logits against the BF16 checkpoint offered as the better metric, and specific silent failures (quantized linear attention passing short benchmarks then emitting gibberish at long context) cited as proof. Open edges: whether the remaining headroom is real or merely an artifact of undertrained models, whether to quantize post-hoc or train in low precision natively, and whether a big model at 4-bit or a fine-tuned tiny model is the right answer for a fixed device budget.

## Consensus

### 4-bit (and FP4-class) quantization is production-viable today, with quality degradation held to roughly 1% or less and treated as a measured, bounded cost rather than an open risk.

Support: **4** talk(s)

> "with FP4 we target for less than 1% accuracy degradation overall on all a benchmarks"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [14:35](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=875s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

### Quantization must be non-uniform: sensitive components (first/last layers, attention-QKV projections, accumulation paths) have to be kept at higher precision, and it is that selectivity — not the average bit width — that determines whether the compressed model survives.

Support: **3** talk(s)

> "if you quantize some layers to you know higher precision and you leave most of the layers in like one bit or two bit and some you know very important layers is 16 bit you can still recover 76% of all accuracy"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [3:15](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=195s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### Standard accuracy benchmarks are an inadequate acceptance test for a compressed or downsized model; they pass while the model fails in real usage, so validation must use distributional metrics, long-context runs, or in-domain human-scale testing.

Support: **3** talk(s)

> "if you quantize the linear attention layers okay it looks like it's doing good but then when you do long context benchmarks you know when you actually use the model in real production it becomes gibberish"
>
> — [Compression at the Edge](../talks/compression-at-the-edge.md), [36:14](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2174s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [Frontier results, on device](../talks/frontier-results-on-device.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)

### Memory footprint, not arithmetic throughput, is the binding constraint for local and edge deployment, which makes quantization the enabling technology rather than a nice-to-have optimization.

Support: **4** talk(s)

> "in order to be able to get AI applications running on the edge, we need to really think a lot about kind of quantization and we also really need to think about what is the smallest possible um model we can use for a given task"
>
> — [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [3:50](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=230s)

Supporting talks: [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Desktop Frontier](../talks/the-desktop-frontier.md)

## Disagreements

### For a fixed device memory budget, should you deploy a large model compressed to 4-bit or a much smaller model fine-tuned for the task?

| Position A | Position B |
|---|---|
| Train big and quantize: a 120B model at 4-bit is meaningfully more capable than a 35B at BF16 for the same disk footprint, and users given the choice preferred one mid-sized checkpoint they could quantize themselves over natively smaller releases.<br>*[Compression at the Edge](../talks/compression-at-the-edge.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* | Pick the smallest model that clears the bar and specialize it: a fine-tuned 50M-500M model matches a 2-4B model on a fixed task with 10K-10M synthetic samples, and you should prototype big but deploy the smallest acceptable model rather than a compressed frontier one.<br>*[Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Frontier results, on device](../talks/frontier-results-on-device.md)* |

*Why it matters: The two paths have opposite throughput profiles — a compressed large model may yield 5-10 tokens/sec on weak hardware where a small one yields 200 — and they imply completely different investments (quantization tooling and eval harnesses versus synthetic data generation and fine-tuning pipelines).*

### Should low precision be applied after training as a compression step, or baked into training itself?

| Position A | Position B |
|---|---|
| Post-training quantization is the default path: it works out of the box above roughly 20-30B parameters, and only sub-20B models need training-based recovery such as quantization-aware distillation — which itself breaks models if run on the wrong data.<br>*[Compression at the Edge](../talks/compression-at-the-edge.md)* | Train in low precision directly — NVFP4 training as demonstrated by Nemotron 3 Ultra makes specialized model creation economically viable sooner, and FP8 pretraining is already in production at 100B+ scale.<br>*[The Desktop Frontier](../talks/the-desktop-frontier.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)* |

*Why it matters: Low-precision training moves the numerical risk from an auditable post-hoc step into the training run itself, where failures are silent — a race condition in open-source FP8 kernels corrupting 0.5% of gradients, or BF16 accumulation halting convergence — and cannot be detected by replica hash checks.*

## Practical Guidance

**Do:**

- Keep the first and last layers plus attention/QKV projection layers at high precision; push middle layers down to 1-2 bit.
- Use FP4 with block scaling — 16 elements sharing one extra FP8 scaling factor — and hold total benchmark degradation under 1%.
- Accept or reject a quantized checkpoint on KL divergence between its output logits and the BF16 model's, targeting distance zero at minimum size, rather than on accuracy scores.
- Run long-context benchmarks after quantizing, specifically to catch layers that pass short evals and then emit gibberish in production.
- Above ~20-30B parameters, use plain post-training quantization; below 20B, budget for quantization-aware distillation to recover accuracy — and only with verified data.
- On edge targets, mix 2-, 4-, and 8-bit to land near 2.9 bits per weight, and size DRAM for ~4GB+ for a 2B-class model once KV cache, runtime, and OS are counted.
- Pair quantization with speculative decoding and warm KV cache reuse; together these were the three most meaningful inference optimizations in a 200M-interaction voice deployment.
- Leave some components at higher precision as a shipping default when user experience matters more than the last increment of size.

**Avoid:**

- Assuming compression degrades linearly — making a model 86% smaller uniformly makes it 100% useless, not 86% worse.
- Trusting public accuracy benchmarks or arenas as the quality gate for a compressed model; arenas have been shown to be gameable and benchmarks only cover verifiable tasks.
- Quantizing linear attention layers at all, regardless of what short-context evals report.
- Running quantization-aware training or distillation on unvetted data — it more commonly breaks the model than helps it.
- Substituting sparsity for quantization as the compression lever: despite NVIDIA hardware support it degrades accuracy more than quantization does.
- Leaving tensor-parallel unembedding accumulation in BF16 during low-precision training — precision loss as activations grow will halt convergence.
- Validating a low-precision training recipe only at ~33B parameters; that scale is too small to surface the numerical issues that appear later.

## Notable Outliers

- Quantizing a single number — one 'super weight' — can make the entire model roughly 20% dumber. ([Compression at the Edge](../talks/compression-at-the-edge.md), [14:03](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=843s))
- Compression headroom exists only because current models are undertrained; train on ~300 trillion tokens and it largely disappears. ([Compression at the Edge](../talks/compression-at-the-edge.md), [12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s))
- Weight quantization is approaching Pareto optimality — maybe one to three bits more — so future gains must come from KV cache compression and sparsity instead. ([Compression at the Edge](../talks/compression-at-the-edge.md), [39:54](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2394s))
- Quality is a hard constraint and speed is the work: every speed optimization, including 4-bit quantization, must be lossless with respect to output quality. ([200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [14:57](https://www.youtube.com/watch?v=AN65uc645mE&t=897s))
- Open-source FP8 training kernels contain a race condition that silently replaces about 0.5% of gradients with random values, and replica hash checking structurally cannot detect it. ([The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [13:56](https://www.youtube.com/watch?v=KhYifX22yhE&t=836s))
- A 550B-parameter model (Nemotron 3 Ultra) runs at 30 tokens/sec across four DGX Sparks using only existing techniques — vLLM backend, quantization, config tuning — for a 10x gain in three weeks with no new research. ([State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [21:43](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=1303s))

## All Talks

- [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)
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
- [Vivek Muppalla](../speakers/vivek-muppalla.md)

