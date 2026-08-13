---
title: "knowledge distillation"
type: "concept"
slug: "knowledge-distillation"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 19
---

# knowledge distillation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **19** speaker(s)

**Definition:** Transferring capability from a larger or stronger teacher model into a smaller student, including on-policy and reasoning-trace variants.

*Also referred to as: on-policy distillation, model distillation, self-distillation, on-policy self-distillation, supervised fine-tuning distillation, reasoning trace distillation, teacher model selection*

## State of Practice

Distillation has become the default way teams ship anything into production that has a latency, cost, or on-device constraint: take an expensive teacher (a frontier LLM, a committee of LLM judges, a large open checkpoint) and compress its behavior into a small student that runs near the generation loop. Character.ai distills a committee of frontier video judges into a small VLM that scores a 15-second video in ~3 seconds; Mixedbread SFTs a small retrieval agent from a larger teacher and then runs on-policy RL with a combined retrieval + trajectory reward; Roboflow distills SAM 3 to a fixed class list rather than fine-tuning it. Two things shifted at this conference. First, the teacher no longer has to be stronger than the student: Bespoke found Qwen teachers beating Claude teachers in Open Thoughts Agents, and Trajectory's on-policy self-distillation gives the same model privileged hints in its prompt and matches the un-hinted student's log-probs to the hinted teacher's — explicitly because 'when we're trying to push the frontier we don't magically have some smarter model.' Second, the failure modes are now well-characterized and all live in the data: students trained on naively generated teacher labels learn surface vibe instead of the axes you asked for, quantization-aware distillation with wrong data breaks models outright, and hint leakage is the self-distillation analogue of reward hacking. The open argument is about ceilings — whether distillation is a durable improvement axis or a bounded transfer that saturates the moment the student has absorbed a fixed teacher-generated dataset.

## Consensus

### Distilling a large teacher (or a committee of expensive judges) into a small student is the standard production path; teams accept measurable accuracy loss in exchange for latency, cost, and deployability.

Support: **5** talk(s)

> "the solution is actually actually to take all these committee of experts and distill it into one small model that is also very very fast, but it is able to give us a response that is not whether or not this video is slap or not, but why is it slap?"
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [7:27](https://www.youtube.com/watch?v=b_PmGocP4rc&t=447s)

Supporting talks: [Evaling Video Slop](../talks/evaling-video-slop.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)

### The teacher does not need to be a stronger model — a same-size or weaker model, or the student itself given privileged information, is often the better teacher.

Support: **4** talk(s)

> "when we're trying to push the frontier we don't magically have some smarter model, right?"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [7:52](https://www.youtube.com/watch?v=zL1kLftVTlo&t=472s)

Supporting talks: [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md)

### Distillation quality is set almost entirely by how the teacher data was generated; naive or contaminated teacher output produces a student that learns the wrong thing rather than a slightly worse student.

Support: **4** talk(s)

> "The reason it was wrong is because how we generated that data, right? It It um it scored the vibe as opposed to the the the axes."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [11:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=674s)

Supporting talks: [Evaling Video Slop](../talks/evaling-video-slop.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)

### Supervised distillation from a teacher carries most of the post-training gain; RL is the expensive add-on that buys the remaining few points.

Support: **3** talk(s)

> "SFT still contributed a lot to the gains um RL was kind of you know it's very comput inensive and for for the last few few percentages it really helped"
>
> — [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [12:12](https://www.youtube.com/watch?v=ewtOo0scUh0&t=732s)

Supporting talks: [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)

## Disagreements

### Should the teacher be the strongest available frontier model, or is teacher selection an empirical question where weaker or same-size teachers often win?

| Position A | Position B |
|---|---|
| Use the biggest frontier model you can afford as the teacher — bootstrapping efficient open/local models off 'monster frontier models' is the dominant 2026-2027 pattern, and SFT from a larger teacher LLM is step one of the recipe.<br>*[State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)* | Teacher strength is not the right selection criterion — Qwen models beat Claude models as teachers in agent distillation, and the strongest results come from the model teaching itself with privileged hints in the prompt rather than importing a stronger model at all.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)* |

*Why it matters: If teacher strength is what matters, distillation is permanently gated on access to (and licensing of) the frontier lab's checkpoints; if it is not, any team can push its own model past its current level with no external teacher and no per-token teacher spend.*

### Is RL with grouped parallel rollouts (GRPO) the right mechanism for pushing a model past its current level, or should on-policy self-distillation replace it?

| Position A | Position B |
|---|---|
| RL is the mechanism: build environments, run async GRPO-style training, accept ~16 steps off-policy, and note that a 1,000-step frontier-scale run on real agentic tasks now costs ~$50K — cheaper than a month of token spend.<br>*[Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)* | GRPO's parallel-rollout requirement cannot be met in real production settings (a customer support chat is not replayable), it collapses messy real-world signal into one scalar, and it saturates around Sonnet-level on LiveCodeBench; on-policy self-distillation learns from a single non-replayable interaction and has surpassed RL on 100+ tool-call agents.<br>*[Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)* |

*Why it matters: The two paths imply opposite infrastructure bets: RL requires building high-fidelity environments and rollout fleets, while self-distillation requires only production traces plus a hint-design and divergence-weighting discipline — and only the latter works when the environment is the customer's live harness.*

### Is distillation a durable axis you can keep pouring compute into, or a bounded transfer that saturates once the student has absorbed a fixed teacher-generated dataset?

| Position A | Position B |
|---|---|
| Durable and sufficient: most business workloads never need frontier capability, a 120B at 4-bit beats a 35B at BF16 for the same disk, and distilled/compressed small models are already the right default for the overwhelming majority of production traffic.<br>*[Compression at the Edge](../talks/compression-at-the-edge.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Evaling Video Slop](../talks/evaling-video-slop.md)* | Bounded: distillation is on the list of approaches that all plateau — once you fix a dataset and train on it, the model learns all of it and stops improving unless it is underparameterized, and self-distillation today only induces narrow, specific behaviors with no known generalization.<br>*[Scaling Compute on Context](../talks/scaling-compute-on-context.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)* |

*Why it matters: If distillation saturates, teams need a self-improvement mechanism that makes its own training data harder over time (the AlphaGo property) rather than more teacher tokens; if it does not, buying more teacher inference is a straightforward and sufficient roadmap.*

## Practical Guidance

**Do:**

- Distill an ensemble of frontier judges into one small model and put it inside the generation loop rather than after assembly — catching defects at the starting-frame and clip level is far cheaper than fixing an assembled output.
- Train distilled judges on A-vs-B pairs, not absolute 1-10 scores: humans do not agree on absolute scales but do agree on comparisons, so the pairwise labels are the ones that transfer.
- Score the specific axes you care about (narrative, pacing, physics, character consistency) in the distillation data — they do not emerge on their own from a general quality label.
- Order the recipe as SFT from a larger teacher first, then on-policy RL with a reward that combines the end metric (retrieval NDCG) with a trajectory reward that grades intermediate behavior.
- For self-distillation, put privileged information in the teacher's prompt and match the un-hinted student's log-probs to the hinted teacher's — this removes the parallel-rollout requirement, so a single example yields signal.
- On long-horizon self-distillation, weight each token by the teacher/student divergence at that step instead of applying a flat KL penalty, to avoid the hedging-token local optimum.
- When distilling for a fixed question set, sample ~16 answers per question rather than collecting 16x more questions answered once.
- For students under ~20B, budget for quantization-aware distillation to recover accuracy; above roughly 20-30B, post-training quantization works out of the box.
- Train several RL experts on a shared base model and distill them into a single checkpoint, rather than training one model across all environments simultaneously.
- Evaluate a distilled or quantized student by KL divergence between its output logits and the BF16 teacher's, not by accuracy benchmarks.
- Distill SAM 3 down to a fixed class list with a lighter detector instead of fine-tuning it directly.
- Check the unit economics before distilling: the committee-of-experts approach is fine at low volume and only pays back at thousands to tens of thousands of items per day.

**Avoid:**

- Generating teacher labels naively and assuming the student inherits your intent — it will score surface gloss and coherence ('the vibe') and rate camera work 9.2 on a static shot.
- Building pairs as human-made = good vs AI-made = bad; unless encoding and annotation methodology match on both sides you train an AI detector, not a quality detector.
- Leaking the solution into the hint during self-distillation — the resulting reasoning traces cannot occur in production, which is the OPSD analogue of reward hacking.
- Running quantization-aware distillation on wrong data: it most commonly breaks the model rather than helping it.
- Assuming the stronger model is the better teacher, or that answer filtering, synthetic rewriting, and task augmentation will improve a distillation set — those curation steps did not work, while synthetic question generation did.
- Expecting self-distillation to generalize — today it only induces narrow, specific behaviors.
- Plain next-token-prediction fine-tuning on your own corpus: loss goes to ~0.0001, generation collapses, and no useful generalization appears.
- Quantizing linear attention layers — short benchmarks look clean while long-context production output turns to gibberish.
- Judging a compressed or distilled student on accuracy benchmarks alone; arenas are gameable and benchmarks only cover verifiable tasks.
- Uniformly compressing weights: 86% uniform compression makes a model 100% useless, not 86% worse — selective per-layer precision is what makes it viable.

## Notable Outliers

- Qwen models outperformed Claude models as distillation teachers in the Open Thoughts Agents work — stronger models are not always better teachers. ([Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [12:12](https://www.youtube.com/watch?v=ewtOo0scUh0&t=732s))
- The trick of on-policy distillation is to show the model text and then make it think the text was in context. ([Scaling Compute on Context](../talks/scaling-compute-on-context.md), [13:01](https://www.youtube.com/watch?v=WiqDvX6isc4&t=781s))
- A model kept at high precision only in the first, last, and attention/QKV layers can be squeezed to 14% of its size and still recover ~76% of accuracy — and compression works at all only because current models are undertrained; at ~300T tokens the headroom largely disappears. ([Compression at the Edge](../talks/compression-at-the-edge.md), [12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s))
- GRPO saturates around Sonnet-level performance on LiveCodeBench, while on-policy self-distillation shifts entire distributions rather than sharpening one — and reduces the tokens needed to solve hard problems instead of increasing them. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [10:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=650s))
- The larger evaluator model was measurably more accurate, and they shipped the smaller distilled one anyway because the accuracy gain did not justify the latency. ([Evaling Video Slop](../talks/evaling-video-slop.md), [8:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=494s))
- SFT data pipelines that export, reformat, and re-upload datasets are unnecessary — SFT is just rollouts in an environment where the actor happens to be a teacher. ([Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [11:27](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=687s))
- Using proprietary frontier models to bootstrap open-source models is legitimate, hard to stop, and will be a defining pattern of 2026-2027. ([State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [38:30](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=2310s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [Compression at the Edge](../talks/compression-at-the-edge.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)
- [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md)
- [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)
- [Scaling Compute on Context](../talks/scaling-compute-on-context.md)
- [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Alex Cheema](../speakers/alex-cheema.md)
- [Asma Beevi](../speakers/asma-beevi.md)
- [Brendan Rappazzo](../speakers/brendan-rappazzo.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Daniel Han](../speakers/daniel-han.md)
- [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)
- [Jack Morris](../speakers/jack-morris.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Merve Noyan](../speakers/merve-noyan.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Parth Sareen](../speakers/parth-sareen.md)
- [Raymond Feng](../speakers/raymond-feng.md)
- [Ronak Malde](../speakers/ronak-malde.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Will Brown](../speakers/will-brown.md)

