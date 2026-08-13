---
title: "synthetic data generation"
type: "concept"
slug: "synthetic-data-generation"
tier: "core"
maturity: "consolidating"
talk_count: 12
speaker_count: 15
---

# synthetic data generation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **12** talk(s) by **15** speaker(s)

**Definition:** Model-generated training, fine-tuning, or evaluation data, including quality control and the risks of training on generated distributions.

*Also referred to as: synthetic data generation for fine-tuning, synthetic eval data generation, synthetic data quality, synthetic rephrasing, data rephrasing, synthetic personas, learning environment synthesis*

## State of Practice

The conference treated synthetic data as the default production technique, not an experiment — but with a sharp split between the two things it is used for. In pre-training, the consensus recipe is *rephrasing*: take real seed documents and generate variants rather than repeating the seed tokens, which sidesteps the model-collapse objection because all information still originates in a human-authored source (poolside runs ~13% synthetic in its pre-training mix; Arcee and Datology report the same pattern, and web text has fallen from ~85% of GPT-3's mix to ~15% in recent models). In evaluation and post-training, the technique is *simulation*: generating multi-turn trajectories, user simulators, personas, and RL environments because production traces are too slow, too sparse, and too costly to experiment on. What separates teams that got value from teams that fooled themselves is whether they measured the sim-to-real gap: Lyft's first offline eval reported a 90%+ pass rate that turned out to be an artifact of an unrealistically polite LLM user, while Nubank validated sim-derived evals against production and had 80% of domain-expert labels confirm the data was usable. Pipeline design is now understood to matter more than generator strength — decompose the task, sample many completions per seed, choose seeds deliberately, and run per-stage ablations, because stronger teacher models are not reliably better teachers. The live argument is whether generated data is an indefinite scaling axis or hits an information ceiling once a fixed corpus has been fully exploited.

## Consensus

### Data and environments, not compute or model architecture, are the binding constraint on model and agent quality — capability gaps are data gaps.

Support: **4** talk(s)

> "the gap in models is usually a gap in data. Models typically are only as good at as data is."
>
> — [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [2:20](https://www.youtube.com/watch?v=zkX03APVj0M&t=140s)

Supporting talks: [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### Rephrasing real seed documents into synthetic variants is the safe, working form of synthetic pre-training data: it avoids model collapse because all information originates in the source document, and it beats simply repeating high-quality tokens.

Support: **3** talk(s)

> "Number one, because all the information is coming from the document on the left, you don't have any issue with model collapse."
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [12:46](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=766s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### Synthetic evaluation data must be explicitly validated against real user behavior or production traces before its scores are trusted; unvalidated simulators produce flattering, unrealistically easy results.

Support: **4** talk(s)

> "our first attempt at our offline evaluation gave us 90 plus pass rate or accuracy rate, right? Uh this almost sounds too good to be true, and I think it indeed is the too good to be true."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [13:40](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=820s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)

### How you structure the generation pipeline matters more than which model generates — decompose hard tasks, sample multiple completions per seed, and select seeds deliberately, because a stronger generator is not automatically a better teacher.

Support: **4** talk(s)

> "the stronger teachers are not always the best uh uh stronger models are not always the better teachers"
>
> — [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [11:16](https://www.youtube.com/watch?v=ewtOo0scUh0&t=676s)

Supporting talks: [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)

### Synthetic data amplifies real data rather than replacing it; a human-authored or human-graded anchor has to stay in the loop, whether as the seed corpus, the labeling set, or the ground-truth comparison.

Support: **4** talk(s)

> "at least at Pulsar we don't see it as a way to replace organic data"
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [2:10](https://www.youtube.com/watch?v=KhYifX22yhE&t=130s)

Supporting talks: [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md)

## Disagreements

### Is synthetic data generation an indefinite scaling axis, or does generating from a fixed corpus hit a hard information ceiling?

| Position A | Position B |
|---|---|
| Synthetic generation scales: curation recipes show a scaling law where metrics keep improving as the generated dataset grows, synthetic mixes now make up a large and growing share of pre-training corpora, and recipes validated at 33B held at 118B/30T tokens — so keep scaling generation.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)* | Any approach that fixes a dataset and generates from it saturates — there is a 'data wall in the synthetic sense' where the model has learned all of the synthetic data, and naive next-token finetuning on your own corpus drives loss to ~0 while the model collapses at generation time; escaping the plateau requires self-improvement mechanisms that make the training data progressively harder, not more generation.<br>*[Scaling Compute on Context](../talks/scaling-compute-on-context.md)* |

*Why it matters: If generation scales, the right investment is a bigger generation pipeline and more compute against a fixed seed corpus; if it saturates, that spend plateaus and the real work is difficulty-escalation machinery or acquiring genuinely new source data.*

### Can simulated agent data substitute for production experiments, or is the fidelity gap still too large to trust?

| Position A | Position B |
|---|---|
| Yes, today: sim-derived eval results correlate highly with production, 80% of domain-expert labels confirmed sim data was usable for greenfield as well as mature agents, and simulation collapsed roughly ten planned A/B tests per quarter down to about one while catching a regression and a self-service-rate degradation before launch.<br>*[SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)* | Not off the shelf: frontier models make systematically unrealistic user simulators because they are trained to be helpful, so the simulator itself must be fine-tuned on real user verbatim until eval scores fall; and for infrastructure-scale work, industry emulation is 'incredibly contrived and low fidelity' — a sim-to-real gap persists even when environments provision real cloud resources, because live customer traffic and scale-dependent failures are absent.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)* |

*Why it matters: It decides whether a simulated pass rate is a shipping gate or merely a smoke test, and whether the budget goes into generating more simulated trajectories or into raising the fidelity of the environment itself.*

### Is human-generated data still the ground truth that synthetic data must be measured against?

| Position A | Position B |
|---|---|
| Yes — human evaluation is the ground truth benchmarks are lossily approximating, you cannot push the frontier from within the frontier without injecting external human expertise, and judges/criteria only become valid after a human hand-labels ~100 examples and looks at raw data; domain-expert feedback, though low volume, is what captures the knowledge automated feedback misses.<br>*[When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* | Not unconditionally — human-only studies are losing their claim to ground truth now that purchase and consideration decisions are mediated by AI agents, the realistic counterfactual to synthetic data is usually no research or somebody's opinion rather than a human study, and AI agents in production are already meeting or exceeding human-level customer satisfaction.<br>*[Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)* |

*Why it matters: It sets the cost floor for any synthetic-data program: either every generated dataset needs a paid human validation set attached to it, or synthetic data can be validated once against a human baseline and then run unattended at scale.*

## Practical Guidance

**Do:**

- Replace repeated high-quality tokens with rephrased synthetic variants of the same seed documents instead of repeating the seeds; poolside settled on 13% synthetic in the pre-training mix (pre-training stages only) over a 6T-token corpus.
- Choose which documents get rephrased — picking random documents to rephrase does not produce good results.
- Decompose a generation task into simpler steps (outline first, then chapters one by one) so output exceeds what the teacher model can produce in one shot without losing correctness or diversity.
- Sample multiple completions per question (e.g. 16x on one question) rather than spending the same budget on many more questions answered once.
- Run ablations stage by stage through the curation pipeline and only proceed to the next stage once you know what worked.
- Fine-tune your user simulator on real user verbatim until evaluation scores go down — a falling score means the eval got more realistic.
- Measure and report the sim-to-real gap explicitly: correlate sim-computed evals against production-computed evals and get domain experts to label whether sim data is usable.
- Ground personas in personality, context, and the study's own construction — the opposite of the human-subject norm of hiding study design — because the LLM has no universe outside the prompt and will otherwise invent confounders.
- Elicit free-text persona responses and map them to a scale via semantic similarity to human-written anchors instead of prompting for a naive 1-5 rating, to recover distribution shape.
- Score persona fidelity with at least two metrics — a correlation metric plus a distribution-shape metric — since a model can match the average and still muddle the variance into the middle.
- Estimate your accuracy ceiling by splitting real human data in two, treating one half as 'synthetic', and repeating the correlation measurement thousands of times.
- Add structural tags to prompt-response pairs when fine-tuning on imbalanced data so the model attends to form rather than hallucinating specific numbers (e.g. APR values).
- De-risk a large training run with small-scale runs on curated data plus simulated token scarcity, at 50-100x less compute.
- Build regression traps into generated benchmarks and make no-regression-on-past-environments part of the optimization objective, not a post-hoc check.
- Hand-label ~100 examples pass/fail, split into train/dev/test, and validate LLM judges on precision and recall like binary classifiers.
- For a tiny model on a single fixed task, generate 10,000 to 10 million synthetic samples and fine-tune — that reaches the quality of a 2-4B model.

**Avoid:**

- Prompting an LLM to produce ~50 test queries and calling that an offline eval dataset — sample from production traffic and mutate instead.
- Using off-the-shelf frontier models as user simulators for support scenarios; they are trained to be helpful and produce unrealistically polite, articulate complaints while real users are impatient and already frustrated.
- Accepting a 90%+ pass rate on a first-pass simulated eval as a signal of quality.
- Piling on more demographic detail in a persona construction on the assumption that specificity improves fidelity — it can amplify model bias and move results further from reality.
- Re-running the same synthetic sample with unchanged inputs to boost statistical significance; it sharpens your estimate of the model, not the accuracy of the forecast.
- Shipping obviously synthetic benchmark data — it increases eval awareness and pushes the model out of distribution, invalidating the measurement.
- Plain next-token-prediction finetuning on your own corpus: loss goes to ~0.0001, generation collapses, and you get no useful generalization.
- Answer filtering, synthetic rewriting, and task augmentation as curation steps — these underperformed in Bespoke's ablations, while synthetic question generation worked.
- Over-optimizing for quality over quantity, which causes non-optimal repetition of high-quality data and saturates the model too early once budgets scale.
- Single-node containerized sandboxes for infrastructure tasks — you cannot simulate provisioning EC2 or Cloud Run inside one node, and deterministic network-failure simulation doesn't represent AWS-scale reality.
- Treating production logs plus feedback as a learning environment; without a replayable simulator and defined grading, a fix is not testable and can introduce hidden regressions.
- Using LLM-as-a-judge to evaluate writing quality — LLMs don't have good taste in writing.
- Assuming public benchmark data is uncontaminated; contamination is the default outcome, and model cards report SWE scores without disclosing memorization.

## Notable Outliers

- 10,000 to 10 million synthetically generated samples is enough to fine-tune a 50M-500M parameter model to high reliability on a fixed task (e.g. 10 output functions callable at over 86% reliability), shipping features that previously required a server subscription entirely offline. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [16:49](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=1009s))
- Curating only the English portion of a corpus measurably improves non-English performance, with transfer magnitude correlated to language similarity — with multilingual tokens at just 8% of the data. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [11:34](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=694s))
- There is a hard ceiling on synthetic persona accuracy set by human self-inconsistency: one study measured humans as only about 80% consistent with themselves. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [17:03](https://www.youtube.com/watch?v=YnNF55QV0zs&t=1023s))
- The correct stopping criterion for a fine-tuned user simulator is that evaluation scores go down — a falling score is evidence of realism, not degradation. ([Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [16:55](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1015s))
- The alternative to a synthetic persona is usually not human research — it's no research, or somebody's opinion. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [19:17](https://www.youtube.com/watch?v=YnNF55QV0zs&t=1157s))
- A model competitive with the open frontier can be trained for under $20 million total, including salaries, compute, and all failed attempts — the 'hundreds of millions to customize a model' figure is false. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [16:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1010s))
- The next step for training environments is multi-node sandboxes that provision real cloud infrastructure — 'a cloud in a box' — because a critical mass of real infra work simply cannot be sandboxed on one node. ([Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [10:46](https://www.youtube.com/watch?v=zkX03APVj0M&t=646s))
- A serious 1,000-task agentic coding benchmark costs about $15M to build and ~$5M/year to maintain, and you cannot substitute AI assistance or cheap labor for the human expertise required. ([When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s))

## All Talks

- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)
- [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)
- [Scaling Compute on Context](../talks/scaling-compute-on-context.md)
- [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)
- [The Base Model Is Dead](../talks/the-base-model-is-dead.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)
- [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)
- [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

## Speakers

- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Aman Gupta](../speakers/aman-gupta.md)
- [Ari Morcos](../speakers/ari-morcos.md)
- [Cormac Brick](../speakers/cormac-brick.md)
- [Ishan Anand](../speakers/ishan-anand.md)
- [Jack Morris](../speakers/jack-morris.md)
- [Joseph Wang](../speakers/joseph-wang.md)
- [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)
- [Marah Abdin](../speakers/marah-abdin.md)
- [Nick Heiner](../speakers/nick-heiner.md)
- [Nick Ung](../speakers/nick-ung.md)
- [Robert McHardy](../speakers/robert-mchardy.md)
- [Shreya Rajpal](../speakers/shreya-rajpal.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Varun Singh](../speakers/varun-singh.md)

