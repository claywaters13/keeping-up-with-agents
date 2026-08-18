---
title: "The Messy Reality of Scale: Synthetic Data and Pre-Training"
type: "talk"
slug: "the-messy-reality-of-scale-synthetic-data-and-pre-training"
track: "Data Quality"
org: "poolside"
day: "Day 2 — Session Day 1"
room: "Track 9"
video_id: "KhYifX22yhE"
duration_sec: 1051
word_count: 3454
speakers: ["Marah Abdin", "Robert McHardy"]
---

# The Messy Reality of Scale: Synthetic Data and Pre-Training

*Program title: The Messy Reality of Scale: Synthetic Data and Pre-Training at Poolside*

**Speakers:** [Marah Abdin](../speakers/marah-abdin.md), [Robert McHardy](../speakers/robert-mchardy.md)

**Org:** poolside

**Track:** Data Quality &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 17m 31s

[Watch on YouTube](https://www.youtube.com/watch?v=KhYifX22yhE)

## Summary

Two poolside team members walk through what broke as they scaled their Laguna code models from one generation to the next, and how they fixed it on both the data and systems sides. Marah Abdin argues synthetic data is a complement to organic data rather than a replacement — a way to surface implicit rationale, planning, and structure, and to break the token-uniqueness wall you hit when a high-quality-only mix gets repeated too often at larger training budgets. She gives a modular six-component framing of synthetic pipelines (seeds, primary/secondary inputs, metadata, generator, supplementary functions) and shapes like rephrasing, multi-stage decomposition, cross-domain porting, and multi-turn loops, plus their agent-orchestration infra, Hive. Robert McHardy then shows previously unpublished failure modes from real large runs: a broken GPU causing silent data corruption, BF16 accumulation before the unembedding losing precision as activations grew and stalling convergence, and a race condition in open-source FP8 kernels silently corrupting ~0.5% of gradients. Worth watching if you want concrete, numbers-backed war stories about pre-training at thousands-of-GPU scale and a practical taxonomy for building synthetic data pipelines.

## Key Points

- Synthetic data at poolside is positioned as a complement to organic data, used to extract implicitly hidden features — rationale, planning, structure — and project them into forms that teach the model more directly.
- Over-optimizing for quality over quantity at small scale backfired when training budgets grew: high-quality data had to be repeated, saturating the model too early, which rephrasing-based synthetic data was used to fix.
- Synthetic data made up 13% of the pre-training mix for their XS.2 model, and their continuously growing synthetic corpus now stands at roughly six trillion tokens.
- Every synthetic pipeline is treated as the same six modular components — seeds, primary inputs, metadata, secondary inputs, a generator function, and supplementary filters/validators — which lets a single configurable infrastructure (Hive, with agent queues, orchestrators, and a supervisor) span cheap seed-heavy jobs to complex orchestrated workflows.
- The design rule is to decompose any task that is too hard for the teacher model, since an overloaded generator loses both correctness and diversity; multi-stage generation (e.g. plot and characters before chapters) yields better output than one-shot generation.
- Data quality and training-code correctness must be treated holistically — a bad codebase ruins a run just as surely as bad data.
- Periodic weight hashing across distributed data-parallel replicas catches silent corruption: a single broken GPU produced spiky loss and huge gradient norms on an otherwise identical run.
- BF16 accumulation before the tensor-parallel unembedding ran out of numerical precision as activations grew around 50k steps, flattening the loss curve; moving the accumulation to FP32 from that checkpoint restored convergence.
- Their unreleased Laguna S — 118B total / 8B active parameters, 30 trillion tokens, 4,000 GPUs — beats their larger previous model on coding benchmarks and leads on their agentic proxy eval, while conceding a knowledge-benchmark gap they attribute to data choices.
- Race conditions in FP8 kernels are a blind spot for hash checking, because real training runs have no replica redundancy over identical weights and data to compare forward/backward passes against.

## Notable Quotes

> "at least at Pulsar we don't see it as a way to replace organic data"
>
> — [2:10](https://www.youtube.com/watch?v=KhYifX22yhE&t=130s) &middot; *states the talk's core position on synthetic data's role*

> "organic data has a lot in it that is basically kind of implicitly hidden. A lot of things that could teach the model or not very presented in the most optimal way sometimes."
>
> — [2:10](https://www.youtube.com/watch?v=KhYifX22yhE&t=130s) &middot; *gives the underlying justification for generating synthetic data at all*

> "for access point two in particular, we settled on 13% of the mix. This is only pre-training stages before post-training."
>
> — [2:44](https://www.youtube.com/watch?v=KhYifX22yhE&t=164s) &middot; *a concrete, comparable mix number*

> "Now we have a six trillion token uh corpus that's continuously growing."
>
> — [2:44](https://www.youtube.com/watch?v=KhYifX22yhE&t=164s) &middot; *sizes the synthetic data effort*

> "we were basically focusing on quality versus quantity um maybe a little too much"
>
> — [3:21](https://www.youtube.com/watch?v=KhYifX22yhE&t=201s) &middot; *an admission that the standard quality-first heuristic broke at scale*

> "we started hitting repetition uh like non-optimal repetition on some of our high-quality data which saturated the model a little too early"
>
> — [3:21](https://www.youtube.com/watch?v=KhYifX22yhE&t=201s) &middot; *names the specific failure mode motivating rephrasing*

> "the rule of thumb is if task is too hard for your model, then your model will start to fall on its face. Lose correctness, lose diversity. So break down the task, make it simpler."
>
> — [5:58](https://www.youtube.com/watch?v=KhYifX22yhE&t=358s) &middot; *the design heuristic for generator pipelines, with the named tradeoff*

> "And then and then from there go into generate the chapters one by one. You will absolutely get a better novel."
>
> — [6:37](https://www.youtube.com/watch?v=KhYifX22yhE&t=397s) &middot; *concrete payoff claim for multi-stage generation*

> "If you've got data that sucks, you can't train a good model. If you've got a training code base that sucks, you also can't."
>
> — [8:57](https://www.youtube.com/watch?v=KhYifX22yhE&t=537s) &middot; *the thesis of the second half in one line*

> "the way we we look at things in my team is uh we don't trust anything. There's so many things that can go wrong when you scale models to billions of parameters to hundreds of billions of parameters um training on thousands of GPUs and so on."
>
> — [9:31](https://www.youtube.com/watch?v=KhYifX22yhE&t=571s) &middot; *states the operating philosophy behind the verification tooling*

> "If they're not identical, we know something has gone seriously wrong uh because that should never happen. And we crash the training."
>
> — [10:07](https://www.youtube.com/watch?v=KhYifX22yhE&t=607s) &middot; *describes the replica-hash invariant and the hard-fail policy*

> "They're exactly the same run. Just in one of them we were got unlucky and we had a broken GPU included."
>
> — [10:34](https://www.youtube.com/watch?v=KhYifX22yhE&t=634s) &middot; *the punchline of the broken-GPU loss-curve comparison*

> "That broken GPU caused silent data corruption and um therefore made the training behave the way it did."
>
> — [11:09](https://www.youtube.com/watch?v=KhYifX22yhE&t=669s) &middot; *names silent hardware corruption as a real, observed cause of bad loss curves*

> "we have to perform some sort of accumulation here uh because we use tensor parallel for the uh unembedding. And that accumulation um was performed in BF16 by default."
>
> — [11:42](https://www.youtube.com/watch?v=KhYifX22yhE&t=702s) &middot; *pinpoints the exact numerical defect that stalled the run*

> "We moved that accumulation into FP32 and from there on the model started converging again."
>
> — [12:21](https://www.youtube.com/watch?v=KhYifX22yhE&t=741s) &middot; *the actionable fix, verified by resuming from the failed checkpoint*

> "with Laguna S we scaled this to a model that's 118 billion uh total parameters and 8B active parameters. Again, we trained it on 30 trillion tokens on 4,000 GPUs."
>
> — [13:24](https://www.youtube.com/watch?v=KhYifX22yhE&t=804s) &middot; *the headline scale numbers for the unreleased model*

> "we had a race condition because we added FP8 training uh based on Deep Chem FP8 kernels that are also like open source"
>
> — [13:56](https://www.youtube.com/watch?v=KhYifX22yhE&t=836s) &middot; *identifies a bug in a widely used open-source dependency*

> "in our case, we noticed about 0.5% of the gradient gets silently corrupted, essentially replaced by random values"
>
> — [13:56](https://www.youtube.com/watch?v=KhYifX22yhE&t=836s) &middot; *quantifies an otherwise invisible failure*

> "In real training runs, you don't have any redundancy where you have the same model weights and the same data, so you can never check if forward and backward actually behave the same across different model replicas."
>
> — [14:32](https://www.youtube.com/watch?v=KhYifX22yhE&t=872s) &middot; *explains the structural limit of hash-based verification*

> "these are base model evals, right? They are partly indicative of how the final model will look, but also not perfectly, right?"
>
> — [15:02](https://www.youtube.com/watch?v=KhYifX22yhE&t=902s) &middot; *an explicit caveat on how to read the benchmark slide*

> "MMLU pro knowledge benchmark is something we don't care about that much compared to coding because we want to build the strongest agentic coding models"
>
> — [16:20](https://www.youtube.com/watch?v=KhYifX22yhE&t=980s) &middot; *a deliberate benchmark tradeoff most labs would not state so plainly*

> "The recipe held, it scaled, and we will continue scaling it from here."
>
> — [16:49](https://www.youtube.com/watch?v=KhYifX22yhE&t=1009s) &middot; *the talk's closing verdict on the generation-to-generation transfer*

## Positions

- Synthetic data should complement organic data rather than replace it, at least given the current state of the field. ([2:10](https://www.youtube.com/watch?v=KhYifX22yhE&t=130s), confidence: stated)
- Optimizing pre-training data too heavily for quality over quantity causes harmful repetition and early model saturation once training budgets scale up. ([3:21](https://www.youtube.com/watch?v=KhYifX22yhE&t=201s), confidence: stated)
- Replacing repeated high-quality tokens with rephrased variants consistently improves results over repeating the seeds. ([4:03](https://www.youtube.com/watch?v=KhYifX22yhE&t=243s), confidence: stated)
- Every synthetic data pipeline, cheap or expensive, can be composed from the same six components. ([4:48](https://www.youtube.com/watch?v=KhYifX22yhE&t=288s), confidence: stated)
- Decomposing a task into simpler steps lets you exceed what the teacher model could produce in one shot, avoiding losses in correctness and diversity. ([5:58](https://www.youtube.com/watch?v=KhYifX22yhE&t=358s), confidence: stated)
- Data quality and training-codebase correctness must be treated holistically; either one being bad prevents a good model. ([8:57](https://www.youtube.com/watch?v=KhYifX22yhE&t=537s), confidence: stated)
- Weight hashes across data-parallel replicas must always match, so mismatches should hard-crash the run. ([10:07](https://www.youtube.com/watch?v=KhYifX22yhE&t=607s), confidence: stated)
- A single broken GPU can produce spiky loss curves and exploding gradient norms with no configuration, data, or implementation difference. ([10:34](https://www.youtube.com/watch?v=KhYifX22yhE&t=634s), confidence: stated)
- BF16 accumulation for the tensor-parallel unembedding loses enough precision as activations grow to halt convergence, and moving it to FP32 fixes it. ([11:42](https://www.youtube.com/watch?v=KhYifX22yhE&t=702s), confidence: stated)
- A 33-billion-parameter model is too small to reliably surface these scale-related numerical issues, requiring a much larger test run to validate the recipe. ([12:52](https://www.youtube.com/watch?v=KhYifX22yhE&t=772s), confidence: stated)
- The DeepGEMM-style open-source FP8 kernels contain a race condition that silently corrupts about 0.5% of gradients; poolside has an unmerged public PR fixing it. ([14:32](https://www.youtube.com/watch?v=KhYifX22yhE&t=872s), confidence: stated)
- Replica hash checking cannot detect race conditions in forward/backward passes because real runs lack the required redundancy. ([14:32](https://www.youtube.com/watch?v=KhYifX22yhE&t=872s), confidence: stated)
- Laguna S outperforms both poolside's previous smaller model and its much larger M.1 model on coding benchmarks, and beats all tested open-weight comparisons on their agentic proxy eval. ([15:42](https://www.youtube.com/watch?v=KhYifX22yhE&t=942s), confidence: stated)
- The model's weakness on MMLU-Pro relative to Nemotron and DeepSeek is purely a data gap that poolside could close if it chose to. ([16:20](https://www.youtube.com/watch?v=KhYifX22yhE&t=980s), confidence: stated)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [quantization](../concepts/quantization.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)
- [task decomposition](../concepts/task-decomposition.md)
- [token efficiency](../concepts/token-efficiency.md)

