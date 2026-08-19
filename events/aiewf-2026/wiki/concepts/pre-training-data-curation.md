---
title: "pre-training data curation"
type: "concept"
slug: "pre-training-data-curation"
tier: "supporting"
maturity: "consolidating"
talk_count: 13
speaker_count: 20
---

# pre-training data curation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **13** talk(s) by **20** speaker(s)

**Definition:** Selecting, mixing, filtering, and sequencing training corpora, and the ablations used to attribute capability to data choices.

*Also referred to as: pre-training data mixture, post-training data curation, data curation, data mixing and curricula, curation ablations, training data exhaustion, data efficiency in pre-training, contrived vs captured training data*

## State of Practice

The conference treated curation, not corpus size, as the live variable in pre-training: Datology's claim that data quality changes the exponent of the scaling law rather than shifting the curve went essentially unchallenged, and Sara Hooker's position that pre-training size is no longer the most lucrative axis of scale was echoed by Arcee's argument that supervised pre-training now exists mainly to build representations for RL. The composition of the mix has visibly shifted — web text from ~85% of GPT-3 to ~15% in current recipes, with code and STEM dominating, and chat, agentic-trace, and long-context data being pulled backward out of post-training into pre-training. Synthetic data has moved from taboo to standard practice in text, but only in the specific form of rephrasing seed documents into new shapes (Q&A, true/false, restructured prose), which practitioners argue is collapse-safe because all information originates in the source document; poolside uses it at 13% of the mix over a 6T-token corpus, and Datology and Arcee both endorse it, while Krea refuses model-generated data entirely in image because the teacher's aesthetic is permanently sticky. Method is converging on staged ablations, small proxy runs with simulated token scarcity, and distilling expensive LLM/VLM filter judgments into small classifiers before sweeping billion-item corpora. The strongest counter-current is the recognition that scalar quality filters actively destroy the tail — aesthetic scores collapse stylistic diversity, and over-indexing on quality forces harmful repetition that saturates a model early. Nobody publishes their actual recipe: the competitive disincentive is explicit, which is why so much of the practical detail at this conference came from vendors and small labs rather than frontier labs.

## Consensus

### Data curation is a compute multiplier, not a constant-factor win — with architecture and compute fixed, the curation recipe is what determines model quality.

Support: **6** talk(s)

> "if you choose your data correctly you can actually bend the scaling laws itself you can change the exponent"
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [5:52](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=352s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [State of Data](../talks/state-of-data.md)

### There is no universally optimal corpus; a mix is only optimal relative to the downstream tasks you intend the model to do, so deliberate capability gaps (e.g. weak MMLU-Pro in a coding model) are a curation choice rather than a defect.

Support: **4** talk(s)

> "A data set's only going to be optimal with respect to a particular set of output tasks that you want the model to do."
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [3:08](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=188s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)

### Rephrasing seed documents into new formats is the collapse-safe way to use synthetic data at pre-training scale, because all information originates in the source document rather than in the generating model.

Support: **3** talk(s)

> "Number one, because all the information is coming from the document on the left, you don't have any issue with model collapse."
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [12:46](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=766s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### Filtering on a single scalar quality or aesthetic score is harmful: it collapses the tail of the distribution that produces good outputs, so curation must explicitly preserve coverage and diversity.

Support: **3** talk(s)

> "some people like think I know like low-resolution CRT videos are like a bad image, but some people like that kind of like aesthetics, so making sure that we have like good coverage"
>
> — [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [5:48](https://www.youtube.com/watch?v=-tviRdpmHvs&t=348s)

Supporting talks: [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [Ending AI Slop](../talks/ending-ai-slop.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### The pre-training / mid-training / post-training boundary is dissolving — data traditionally reserved for later stages (chat, agentic traces, long context) belongs earlier, and the stages should be designed as one system.

Support: **3** talk(s)

> "it also actually goes to show how we really should be thinking about all these stages synergistically"
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [15:29](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=929s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)

## Disagreements

### Should model-generated data be a first-class ingredient in the pre-training mix, or excluded on principle?

| Position A | Position B |
|---|---|
| Synthetic data is the way forward: rephrase and upsample seeds, decompose generation tasks so output exceeds what the teacher could produce one-shot, and ship it as a meaningful fraction of the mix (poolside settled on 13%).<br>*[The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)* | Avoid model-generated data entirely — it is a shortcut that permanently imprints the teacher's distribution on your model, and the resulting collapse to the mean is exactly what 'slop' is; a trained observer can identify a heavily distilled model on sight.<br>*[Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [Ending AI Slop](../talks/ending-ai-slop.md)* |

*Why it matters: It decides whether a small lab can bootstrap a competitive corpus from a frontier teacher, or must invest in expensive organic and human-expert data it cannot generate. The split tracks modality — text practitioners accept rephrasing, image practitioners reject distillation — so the resolution may be that 'synthetic' means two different things in the two camps.*

### Where does the marginal curation dollar buy more capability: the pre-training corpus, or post-training data and RL environments?

| Position A | Position B |
|---|---|
| Pre-training scale and pre-training data are saturating; supervised training now mainly builds representations for RL, the base model only needs exposure to the atomic skills RL will compose, and labs are pushing post-training further back. Data and RL environments — not compute or models — are the post-training bottleneck.<br>*[The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)* | Pre-training and mid-training data remain the highest-leverage input, and better domain data at mid-training makes an unchanged post-training harness two to three times more effective; the recipe still scales (poolside trained 118B/8B-active on 30T tokens and is continuing to scale it).<br>*[Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)* |

*Why it matters: It determines whether a team building a custom model buys tokens and a pre-training run, or buys RL environments and expert trajectories — very different cost structures, hiring, and timelines. Datology's framing implies the post-training gains people attribute to RL are partly mis-attributed mid-training data gains.*

### When you run out of high-quality tokens, should you repeat them or replace the repeats with rephrased variants?

| Position A | Position B |
|---|---|
| Repeat: up to some threshold it is almost always better to repeat high-quality data than to show additional low-quality data, and multi-epoch training on a small curated corpus was validated as far back as Galactica's 105B curated tokens.<br>*[Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* | Repetition has a real cost that only appears once training budgets scale: poolside over-optimized quality against quantity, hit non-optimal repetition on its high-quality data, and saturated the model too early — replacing repeated seeds with rephrased variants consistently improved results.<br>*[The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)* |

*Why it matters: It sets the token budget a curation pipeline must hit before a hero run is safe, and whether a rephrasing pipeline is optional tooling or a prerequisite for scaling. The two sides may only differ on where the epoch threshold sits, but nobody published a number for it.*

## Practical Guidance

**Do:**

- Replace repeated high-quality seeds with rephrased variants when upsampling, and choose which documents get rephrased — random document selection for rephrasing produces poor results.
- Decompose synthetic generation into simpler steps (outline, then chapters) so the pipeline exceeds what the teacher model produces one-shot without losing correctness or diversity.
- Distill expensive LLM/VLM filter judgments into a small SigLIP-scale classifier before running a filter over a billion-item corpus; Krea ended up with 30-40 in-house classifiers and heuristics over a 2-10B image corpus.
- Keep most of the mid-training mix representative of the pre-training distribution when doing domain adaptation — this prevents catastrophic forgetting outright rather than trading general capability for domain capability.
- Pull chat, agentic-trace, and long-context data backward into pre-training so the model learns downstream task shapes from the start instead of meeting a distribution shift at SFT.
- Run staged ablations, deciding what works at each curation stage before proceeding to the next, and use small runs with simulated token scarcity to derisk the hero run at 50-100x less compute.
- Curate the majority-language (English) portion of the corpus even when the target is multilingual — the gains transfer, with magnitude correlated to language similarity, at only 8% multilingual tokens.
- Filter or undersample items whose key attributes your captioning model consistently fails to describe, even when the item itself is fine — bad captions poison the pair, not just the caption.
- Verify training-code and hardware correctness (cross-replica weight hashes, FP32 accumulation for tensor-parallel unembedding) before attributing a bad loss curve to the data mix — a single broken GPU reproduces the same symptoms.
- When collecting reasoning or preference data, sample many answers per question (16x) rather than proportionally more questions answered once, and attach preferences to per-rater vectors rather than averaging across unmodeled raters.

**Avoid:**

- Filtering with off-the-shelf aesthetic or image-quality scores — it silently deletes the styles a meaningful share of users actually want.
- Training on frontier-model outputs as a shortcut in generative media: the teacher's aesthetic is sticky and permanent, and it is recognizable to a trained observer.
- Optimizing quality over quantity so hard that you must repeat your high-quality subset, which saturates the model early once the training budget grows.
- Assuming a single golden dataset exists, or that a benchmark number under one scaffold means anything — cross-harness and cross-infrastructure differences drive much of the observed benchmark divergence.
- Buying dead startups' codebases as a frontier-data source; the only durable supply of realistic type-one data is an ongoing partnership with a live business.
- Buying your evals and your definition of task realism from the same vendor that sells you the training data to hill-climb them.
- Treating answer filtering, synthetic rewriting, and task augmentation as reliable curation steps — Bespoke found they underdelivered, while synthetic question generation worked.
- Fixing MoE expert load imbalance by cranking the load-balancing coefficient during SFT — it is a symptom of pre/post-training distribution mismatch that should have been fixed in the early mix.

## Notable Outliers

- Roughly 80% of new code added to GitHub is now machine-generated, so mining human-written code as training data is reaching its end and self-play — models generating and judging their own coding challenges — is what produces superhuman coding. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [9:33](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=573s))
- Curating only the English portion of a corpus measurably improves non-English performance, with transfer magnitude correlated to language similarity. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [11:34](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=694s))
- A 33B-parameter validation run is too small to surface the numerical and race-condition failures that appear at scale — open-source FP8 kernels silently corrupted ~0.5% of gradients, and cross-replica hash checks structurally cannot catch it. ([The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [14:32](https://www.youtube.com/watch?v=KhYifX22yhE&t=872s))
- Essentially every data vendor sells contrived (type two) data while marketing it as captured (type one) data, and then sells the benchmark built from it plus the data to hill-climb that benchmark. ([State of Data](../talks/state-of-data.md), [5:41](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=341s))
- Sparse autoencoders trained on vision models yield an unsupervised tagging system usable for filtering watermarks, signatures, and blur out of a pre-training corpus. ([Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [12:33](https://www.youtube.com/watch?v=-tviRdpmHvs&t=753s))
- A model competitive with the open frontier can be trained for under $20 million total including salaries, compute, and all failed attempts — the 'hundreds of millions' figure is false. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [16:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1010s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)
- [Ending AI Slop](../talks/ending-ai-slop.md)
- [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)
- [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)
- [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)
- ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)
- [State of Data](../talks/state-of-data.md)
- [The Base Model Is Dead](../talks/the-base-model-is-dead.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)
- [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)

## Speakers

- [Ari Morcos](../speakers/ari-morcos.md)
- [Benoit Schillings](../speakers/benoit-schillings.md)
- [Carter Abdallah](../speakers/carter-abdallah.md)
- [Chengxi Taylor](../speakers/chengxi-taylor.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Chris Souza](../speakers/chris-souza.md)
- [Daniel Bump](../speakers/daniel-bump.md)
- [Lucas Atkins](../speakers/lucas-atkins.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Marah Abdin](../speakers/marah-abdin.md)
- [Philipp Schmid](../speakers/philipp-schmid.md)
- [Preetika Bhateja](../speakers/preetika-bhateja.md)
- [Robert McHardy](../speakers/robert-mchardy.md)
- [Ross Taylor](../speakers/ross-taylor.md)
- [Sangwu Lee](../speakers/sangwu-lee.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)

