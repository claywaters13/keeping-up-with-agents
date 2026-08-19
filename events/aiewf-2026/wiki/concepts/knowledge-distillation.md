---
title: "knowledge distillation"
type: "concept"
slug: "knowledge-distillation"
tier: "supporting"
maturity: "consolidating"
talk_count: 16
speaker_count: 24
---

# knowledge distillation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **16** talk(s) by **24** speaker(s)

**Definition:** Transferring capability from a larger or stronger teacher model into a smaller student, including on-policy and reasoning-trace variants.

*Also referred to as: on-policy distillation, model distillation, self-distillation, on-policy self-distillation, supervised fine-tuning distillation, reasoning trace distillation, teacher model selection*

## State of Practice

Distillation has stopped being a compression trick and become the default production path: teams use a frontier model only long enough to prove a task is possible, then move the task onto a cheaper open or in-house student trained on the frontier model's traces — LangChain reports Opus-comparable trace judging one to two orders of magnitude cheaper, Character.ai distills a committee of expensive video judges into a small VLM that scores a 15-second clip in ~3 seconds, and Krea distills large-VLM filtering decisions into a SigLip-sized classifier to survive a 2-10B image corpus. The sharpest technical movement of the conference was away from offline SFT on teacher traces and toward on-policy variants, where the student generates the rollout and a teacher with privileged information (a 'hint') supervises it: Applied Compute and Trajectory both report that a hint given to the same model makes it a competent teacher of itself, removing the requirement for a stronger model at all. The engineering details that make this work are specific — a judge picks where in the rollout to inject the hint, the KL signal decays with distance so loss is restricted to the next step or few, and an LLM judge masks teacher tokens (connector words) that carry the teacher's idiosyncrasies rather than the target behavior. The known failure modes now have names: hint leakage (OPSD's analogue of reward hacking), catastrophic degradation of out-of-distribution behavior from naive SFT, and a local optimum of hedging tokens ('wait', 'but', 'maybe') when a teacher repeatedly course-corrects a divergent student on long-horizon tasks. What remains genuinely open is whether distillation is a ceiling-raiser or only a compressor: Engram argues any fixed dataset saturates, Trajectory claims OPSD shifts entire distributions and has surpassed RL on 12B agents at 100+ tool calls.

## Consensus

### The right workflow is to use a frontier model to establish that a task is feasible, then distill its traces into a smaller or open model for production serving.

Support: **4** talk(s)

> "this year and and next year you're going to see a lot of using these like monster frontier models to bootstrap, you know, like a more efficient setup that runs on open source"
>
> — [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [38:30](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=2310s)

Supporting talks: [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [Compression at the Edge](../talks/compression-at-the-edge.md)

### Purely offline SFT on teacher-generated traces degrades the student's general and out-of-distribution performance, even when every training trace exhibits the desired behavior; on-policy rollouts under teacher supervision avoid this.

Support: **4** talk(s)

> "even doing SFT on traces where we knew the hyperlink was correctly formatted, we saw that there was this sort of degradation in overall coding agent performance"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [14:35](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=875s)

Supporting talks: [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)

### Distilling an expensive committee of large judges/filters into one small student model is the standard way to make evaluation and data curation affordable at production volume.

Support: **3** talk(s)

> "the solution is actually actually to take all these committee of experts and distill it into one small model that is also very very fast, but it is able to give us a response that is not whether or not this video is slap or not, but why is it slap?"
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [7:27](https://www.youtube.com/watch?v=b_PmGocP4rc&t=447s)

Supporting talks: [Evaling Video Slop](../talks/evaling-video-slop.md), [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)

### A teacher does not have to be a separate, stronger model — giving the same model privileged information (a hint, the answer's context, the future of the trace) makes it a usable teacher for itself.

Support: **3** talk(s)

> "in order to create a teacher that's smarter than this on-policy model, we need to create some kind of hint or have some kind of privileged information"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [3:46](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=226s)

Supporting talks: [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)

### Distilled or compressed smaller models are capability-sufficient for the majority of production workloads; frontier-level models are not needed per-use-case.

Support: **4** talk(s)

> "open models have basically hit an inflection point in intelligence that we at LangChain don't reach for the frontier models for every single use case"
>
> — [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [7:15](https://www.youtube.com/watch?v=CvRngaQZQ3Y&t=435s)

Supporting talks: [Compression at the Edge](../talks/compression-at-the-edge.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)

### Distillation reliably transfers narrow, specific behaviors but breaks down as you scale to large students and long-horizon agentic tasks, where run-to-run variance, format errors, and degenerate token preferences appear.

Support: **4** talk(s)

> "this works really well for small models short horizon tasks like something like a chatbot. But this is where academic papers kind of end and where you really need to scale things up to start to to see the limitations."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [12:10](https://www.youtube.com/watch?v=zL1kLftVTlo&t=730s)

Supporting talks: [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)

## Disagreements

### Does an effective teacher need to be a stronger model than the student?

| Position A | Position B |
|---|---|
| Yes — reach for the strongest available frontier model as the teacher and bootstrap the student from its traces; that is where the capability you are transferring comes from.<br>*[Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)* | No — stronger models are frequently worse teachers empirically (Qwen beat Claude as a teacher in Open Thoughts Agents), and when pushing the frontier no smarter model exists, so the teacher should be the same model conditioned on privileged information.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)* |

*Why it matters: If the teacher must be stronger, distillation is permanently gated on frontier API access and your student's ceiling is someone else's model; if privileged information suffices, distillation becomes a self-improvement loop that any team with production traces can run.*

### Can distillation push a student past its teacher's capability, or does it only compress capability that already exists?

| Position A | Position B |
|---|---|
| It only compresses and saturates — any approach that fixes a dataset and trains on it hits an upper bound once the information transfers into the weights, and self-distillation today works only for narrow induced behaviors.<br>*[Scaling Compute on Context](../talks/scaling-compute-on-context.md), [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)* | It raises the ceiling — on-policy self-distillation shifts entire distributions rather than sharpening one, reaches territory GRPO cannot (which saturates around Sonnet-level on LiveCodeBench), and has surpassed RL on 12B agents requiring 100+ tool calls.<br>*[Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)* |

*Why it matters: This determines whether post-training budget should go into distillation at all or into RL environments and data acquisition; if distillation saturates, every dollar past the plateau is wasted and self-improving difficulty curricula are the only path forward.*

### Is training a student on a teacher model's generated outputs acceptable, or does it permanently imprint the teacher's characteristics?

| Position A | Position B |
|---|---|
| Avoid it — synthetic teacher outputs are 'sticky': training on AI-generated images permanently stamps a recognizable ChatGPT/Nano Banana aesthetic on the model, and evaluator models trained on naively generated data learn surface gloss rather than the axes you intended to measure.<br>*[Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [Evaling Video Slop](../talks/evaling-video-slop.md)* | Embrace it — bootstrapping open models from frontier model outputs is the dominant efficiency pattern, legitimate, and practically impossible to stop.<br>*[State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)* |

*Why it matters: In generative media the teacher's fingerprint is the product — a distilled model that looks like everyone else's has no differentiation — whereas in agentic text tasks the teacher's style is irrelevant next to task completion, so the same technique is a shortcut in one domain and a trap in the other.*

## Practical Guidance

**Do:**

- Use a judge to choose where in the rollout to inject the hint rather than hinting at the start, and restrict the distillation loss to the next step or a few steps forward, because the KL learning signal decays with distance from the hint.
- Mask which teacher tokens the student learns from with an LLM judge, so the student acquires the target behavior instead of the teacher's preferred connector words.
- Design hints as 'what the model should reasonably have known' — filter the actual solution out — to prevent hint leakage producing reasoning traces that can never occur in production.
- Add a single on-policy rollout step to an otherwise offline production trace; that alone yields a larger SWE-bench pass-rate gain than the fully offline setup.
- Train distilled judges on A-vs-B pairs rather than absolute 1-10 scores, since humans agree on comparisons but not on absolute scales.
- Ablate teacher choice explicitly instead of defaulting to the strongest model, and sample many answers per question (e.g. 16x) rather than collecting proportionally more questions answered once.
- For students under ~20B parameters, use quantization-aware distillation to recover accuracy; post-training quantization only works out of the box above ~20-30B.
- Evaluate a compressed or distilled student by KL divergence against the BF16 teacher's output logits, not by accuracy benchmarks.
- Distill large-VLM filtering judgments into a SigLip-sized classifier before running data curation over billions of images.
- Train separate specialist experts (photography, text rendering; or per-environment RL experts) and merge/distill them into a single student, which is more reliable than training one model on everything at once.
- Only train and serve a distilled evaluator once volume justifies it — thousands to tens of thousands of items per day; below that the expensive committee of experts is cheaper.

**Avoid:**

- Do not do plain next-token-prediction finetuning on your own corpus: loss goes to ~0.0001, generation collapses, and the model answers nothing that is not verbatim encoded in the data.
- Do not assume SFT on format-correct teacher traces is safe — it degrades out-of-distribution coding agent performance, as does reward shaping for the same output format.
- Do not distill over the entire rollout following a hint.
- Do not train image models on AI-generated images; a trained observer can identify heavily distilled models, and the teacher's aesthetic cannot be removed later.
- Do not build judge training data by pairing human footage as 'good' against AI footage as 'bad' — you will train an AI detector, not a quality detector.
- Do not treat distillation as an unbounded scaling axis; a fixed dataset saturates unless the model is underparameterized or training difficulty escalates.
- Do not assume distillation results from small-model, short-horizon papers transfer — at 120B with 50-100 tool calls, eval accuracy varies widely, run-to-run variance is extreme, and tool-call format errors appear.
- Do not assume a distillation setup needs a golden answer or rubric; most enterprise continual-learning situations have neither, and methods that require one do not deploy.
- Do not quantize linear attention layers when compressing a student — short benchmarks look fine while long-context output becomes gibberish.

## Notable Outliers

- Stronger models are not always better teachers — some Qwen models outperformed Claude models as distillation teachers in the Open Thoughts Agents work. ([Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [11:16](https://www.youtube.com/watch?v=ewtOo0scUh0&t=676s))
- A teacher can move a student toward calling a tool purely by reshaping the reasoning path leading up to it, without ever modifying the tool-call tokens themselves — task-complete call rate went from ~22% to ~60%. ([Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s))
- On long-horizon tasks the teacher repeatedly course-corrects a divergent student, driving it into a local optimum dominated by hedging tokens like 'wait', 'but', and 'maybe'. ([Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [13:28](https://www.youtube.com/watch?v=zL1kLftVTlo&t=808s))
- Compression and distillation headroom exists only because current models are undertrained; if models were trained on ~300 trillion tokens that headroom would largely disappear. ([Compression at the Edge](../talks/compression-at-the-edge.md), [12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s))
- Real-time video is a distillation problem in disguise: collapsing ~30 denoising steps into a single step is what makes interactive avatar generation cost the same as a voice model. ([Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md), [11:22](https://www.youtube.com/watch?v=z1dqv74SpUs&t=682s))
- On-policy distillation is essentially a trick — you show the model text and make it think the text was in context — and it forfeits the benefits you get from taking gradients over genuinely new data. ([Scaling Compute on Context](../talks/scaling-compute-on-context.md), [13:01](https://www.youtube.com/watch?v=WiqDvX6isc4&t=781s))
- SFT data pipelines that export, reformat, and re-upload datasets are unnecessary; SFT is just rollouts in an environment where the actor happens to be a teacher. ([Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [11:27](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=687s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md)
- [Compression at the Edge](../talks/compression-at-the-edge.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
- [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)
- [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md)
- [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)
- [Scaling Compute on Context](../talks/scaling-compute-on-context.md)
- [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)
- [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)
- [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)

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
- [Keegan McCallum](../speakers/keegan-mccallum.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Merve Noyan](../speakers/merve-noyan.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Parth Sareen](../speakers/parth-sareen.md)
- [Raymond Feng](../speakers/raymond-feng.md)
- [Ronak Malde](../speakers/ronak-malde.md)
- [Samuel Denton](../speakers/samuel-denton.md)
- [Sangwu Lee](../speakers/sangwu-lee.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Will Brown](../speakers/will-brown.md)

