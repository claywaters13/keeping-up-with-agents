---
title: "pre-training data curation"
type: "concept"
slug: "pre-training-data-curation"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 19
---

# pre-training data curation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **19** speaker(s)

**Definition:** Selecting, mixing, filtering, and sequencing training corpora, and the ablations used to attribute capability to data choices.

*Also referred to as: pre-training data mixture, post-training data curation, data curation, data mixing and curricula, curation ablations, training data exhaustion, data efficiency in pre-training, contrived vs captured training data*

## State of Practice

The field has stopped treating the corpus as a scrape and started treating it as a designed artifact: web text fell from ~85% of GPT-3's mix to ~15% in recent frontier recipes, displaced by code, STEM, and task-shaped data that used to live only in post-training. The strongest claim on offer is that curation changes the exponent of the scaling law rather than shifting the curve — DatologyAI reports matching Qwen 3.5 4B on a VLM with 145x less training compute through curation alone, and mid-training on better domain data making an unchanged post-training harness 2-3x more effective. Rephrasing-based synthetic data has become the accepted way to stretch a scarce high-quality corpus, on the argument that all information originates in the source document so the trained model can surpass the rephraser; poolside caps it at 13% of the pre-training mix, Arcee argues it is the way forward outright. Method is converging on staged ablations — change one curation stage, measure, proceed — with small-scale proxy runs under simulated token scarcity used to derisk hero runs, though poolside's experience is that a 33B validation run is too small to surface the numerical and systems failures (BF16 unembedding accumulation, a race condition in open-source FP8 kernels corrupting 0.5% of gradients, a single broken GPU) that actually kill a recipe at scale. The live fault line is whether pre-training data is still where capability comes from at all, or whether the base model is now just a prior that needs exposure to the atomic skills RL will later compose.

## Consensus

### Data quality, not compute or model size, is the binding constraint on model capability, and it acts as a multiplier on compute rather than a constant-factor win.

Support: **6** talk(s)

> "if you choose your data correctly you can actually bend the scaling laws itself you can change the exponent"
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [5:52](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=352s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [State of Data](../talks/state-of-data.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### The 'train on a representative crawl of the internet' recipe is over; corpora are now deliberately composed, with code, STEM, and curated domain text displacing general web text.

Support: **4** talk(s)

> "web text, which used to make up like up to 85% of the train data in GPT uh 3, is now all the way down at 15%"
>
> — [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [6:46](https://www.youtube.com/watch?v=xbPriQWXtWM&t=406s)

Supporting talks: [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [State of Data](../talks/state-of-data.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)

### Rephrasing source documents into synthetic variants is a safe way to expand a high-quality corpus, because the information originates in the source document rather than in the generating model.

Support: **3** talk(s)

> "Number one, because all the information is coming from the document on the left, you don't have any issue with model collapse."
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [12:46](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=766s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### Pre-training, mid-training, and post-training should be designed as one system with data flowing backward across the boundaries, not handed off between independent teams.

Support: **3** talk(s)

> "it also actually goes to show how we really should be thinking about all these stages synergistically"
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [15:29](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=929s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)

### Curation choices must be attributed by staged ablations — change one stage, measure, then proceed — rather than by intuition or by a single end-of-run benchmark number.

Support: **3** talk(s)

> "the systematic way of doing this is like you run ablations and figure out which uh you know in each of these stages what works and you kind of proceed to the next"
>
> — [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [9:38](https://www.youtube.com/watch?v=ewtOo0scUh0&t=578s)

Supporting talks: [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [How Evals and Prompts Shape Agent Behavior](../talks/how-evals-and-prompts-shape-agent-behavior.md)

## Disagreements

### Does the next unit of model capability come from the pre-training corpus, or from RL and post-training with pre-training reduced to a prior?

| Position A | Position B |
|---|---|
| Pre-training scale and pre-training data are saturated as a lever; supervised next-token training exists to build representations for RL, the base model only needs exposure to the atomic skills RL will compose, and compute should move backward into post-training. Sara Hooker states no frontier lab will supersize a model again under the current architecture.<br>*[Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* | The pre-training and mid-training corpus is still where capability is created: curation alone, with no post-training at all, pushed a VLM past the public Pareto frontier, and better mid-training data makes an unchanged post-training harness 2-3x more effective. poolside scaled a 118B/8B-active model on 30T tokens and says the recipe held and will keep scaling.<br>*[Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)* |

*Why it matters: It decides whether a team's marginal dollar buys curated pre-training tokens or RL environments and rollouts, and whether a small team can compete without co-located pre-training compute.*

### Should synthetic data replace organic data in the pre-training mix, or only complement a bounded fraction of it?

| Position A | Position B |
|---|---|
| Synthetic data is the way forward for pre-training; rephrasing avoids collapse because the information comes from the source, and self-play generating its own problems and judgments is what will produce superhuman capability with compute as the only limit.<br>*[The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)* | Synthetic data complements organic data and does not replace it, because organic data carries implicitly hidden signal that a generator will not reproduce; poolside settled on 13% synthetic in the pre-training stages.<br>*[The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)* |

*Why it matters: It sets the ceiling on how far a team can go once organic high-quality tokens run out, and determines whether generator-model spend or token-sourcing spend dominates the data budget.*

### When high-quality tokens run short, should you repeat them or replace the repeats with rephrased variants?

| Position A | Position B |
|---|---|
| Up to some threshold it is almost always better to repeat high-quality data than to show additional low-quality data; multi-epoch training on a small curated corpus was Galactica's core empirical result against the one-epoch consensus.<br>*[Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)* | Optimizing too hard for quality over quantity causes non-optimal repetition that saturates the model early once training budgets scale; replacing repeated high-quality tokens with rephrased variants consistently beats repeating the seeds.<br>*[The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)* |

*Why it matters: It determines the epoch policy and whether a rephrasing pipeline is optional tooling or a prerequisite for any large token budget on a small curated corpus.*

### Can small-scale runs validate a pre-training data recipe before the hero run?

| Position A | Position B |
|---|---|
| Yes — small-scale runs on properly curated data with simulated token scarcity predict large-model performance, letting a team derisk a hero run with 50-100x less compute; ablation ladders at small scale are the systematic method.<br>*[Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)* | A 33B model is too small to reliably surface the failures that actually break a recipe at scale — BF16 accumulation loss, silent GPU corruption, kernel race conditions — so a much larger validation run is required.<br>*[The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)* |

*Why it matters: It sets how much compute must be spent on validation before committing, and whether a proxy-scale win on a data mix is trustworthy evidence at all.*

## Practical Guidance

**Do:**

- Define the target set of downstream tasks before curating — a dataset is only optimal with respect to the outputs you want, and there is no universal best corpus.
- Rephrase and upsample deliberately selected seed documents instead of repeating them verbatim; document selection matters, random documents rephrase badly.
- Break synthetic generation into simpler decomposed steps (outline, then chapters) so the pipeline exceeds what the teacher model produces in one shot without losing correctness or diversity.
- When domain-adapting, keep most of the mid-training mix representative of the pre-training distribution — this prevented catastrophic forgetting entirely in DatologyAI's runs.
- Curate the English portion of a multilingual corpus even if you care about non-English performance; the gain transfers, scaled by language similarity (8% multilingual tokens sufficed).
- Pull post-training-shaped data — chat pairs, agentic traces, long-context sets — back into pre-training so the model learns the shape of downstream conversations from the start.
- Fix MoE expert load imbalance by mixing data better early rather than cranking the load-balancing coefficient during SFT.
- Sample multiple answers per question (16x) instead of collecting proportionally more questions answered once.
- Hash weights across data-parallel replicas every step and hard-crash the run on any mismatch.
- Perform the tensor-parallel unembedding accumulation in FP32, not BF16 — BF16 loses enough precision as activations grow to halt convergence.
- Attach preference data to per-rater preference vectors instead of averaging across unmodeled raters, and tie expert commentary to the specific code component that produced the visual element.

**Avoid:**

- Assuming a stronger model is a better teacher for distillation — some Qwen models outperformed Claude models as teachers.
- Over-indexing on quality at the expense of quantity; it produces harmful repetition that saturates the model early once the token budget scales.
- Rephrasing randomly selected documents — 'All documents are not created equal for rephrasing.'
- Reading a single benchmark number under a single scaffold as recipe signal; benchmaxing and cross-harness differences make model results hard to interpret.
- Buying your evals and your definition of task realism from the same vendor that sells you the training data.
- Sourcing frontier data from defunct startups' codebases instead of an ongoing partnership with a live business — contrived data is routinely sold as captured data.
- Prompting an LLM-as-judge for holistic quality in subjective domains; decompose the target into codified elements and use human judgment for the rest.
- Handing pre-training, mid-training, and post-training to independent teams with clean handoffs.
- Trusting open-source FP8 kernels without checking — a DeepGEMM-style race condition silently corrupted ~0.5% of gradients, and replica hash checks cannot catch forward/backward race conditions.
- Grading model outputs only against the original artifact rather than against decomposed ground truth, which penalizes novel-but-valid solutions and drives collapse to the mean.

## Notable Outliers

- Curating only the English portion of a corpus measurably improves non-English performance, with transfer magnitude correlated to language similarity — with multilingual data at just 8% of tokens. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [11:34](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=694s))
- Curation alone, with no post-training, matched Qwen 3.5 4B using 145x less training compute and ~35x fewer flops per correct answer, because curation also shortens responses. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [7:47](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=467s))
- A model competitive with the open frontier can be trained for under $20 million total including salaries, compute, and all failed attempts — the 'hundreds of millions' figure is false. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [16:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1010s))
- Roughly 80% of new code added to GitHub is now machine-generated, so mining human-written code as a training corpus is reaching an end and self-play must replace it. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [9:33](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=573s))
- Essentially every data vendor sells contrived type-two data while marketing it as captured type-one data, and the same vendors then sell the data to hill-climb the benchmarks they authored. ([State of Data](../talks/state-of-data.md), [5:41](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=341s))
- Stronger models are not always better teachers; answer filtering, synthetic rewriting, and task augmentation all failed as curation steps while synthetic question generation worked. ([Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [11:16](https://www.youtube.com/watch?v=ewtOo0scUh0&t=676s))
- A single broken GPU produced spiky loss curves and exploding gradient norms with no configuration, data, or implementation difference from the healthy run. ([The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [10:34](https://www.youtube.com/watch?v=KhYifX22yhE&t=634s))
- Galactica trained on 105B curated tokens beat Palm, Chinchilla, and GPT-3.5 in scientific domains with far less compute, and was the first major result for multi-epoch training when the consensus was one epoch. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [5:21](https://www.youtube.com/watch?v=2bvtay8wGYI&t=321s))
- Automated architecture search only yielded significant returns once data quality was co-optimized with the model rather than left to the agent's discretion. ([Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md), [5:59](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=359s))
- In subjective domains the most likely output is not the optimal one — quality lives at the tails, so training toward the mode is precisely what manufactures slop. ([Ending AI Slop](../talks/ending-ai-slop.md), [8:03](https://www.youtube.com/watch?v=lCBf9slCanI&t=483s))

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
- [Sara Hooker](../speakers/sara-hooker.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)

