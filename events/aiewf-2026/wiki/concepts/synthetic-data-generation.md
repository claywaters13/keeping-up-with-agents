---
title: "synthetic data generation"
type: "concept"
slug: "synthetic-data-generation"
tier: "core"
maturity: "contested"
talk_count: 15
speaker_count: 18
---

# synthetic data generation

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **15** talk(s) by **18** speaker(s)

**Definition:** Model-generated training, fine-tuning, or evaluation data, including quality control and the risks of training on generated distributions.

*Also referred to as: synthetic data generation for fine-tuning, synthetic eval data generation, synthetic data quality, synthetic rephrasing, data rephrasing, synthetic personas, learning environment synthesis*

## State of Practice

Synthetic data has moved from a suspect shortcut to the default supply line for both training corpora and evaluation sets, but the field now generates it structurally rather than by asking a model for examples. The reliable pattern across pre-training, post-training, and eval work is the same: anchor generation in something real (a source document to rephrase, a symbolic policy tree to sample from, a real production log lifted into a replayable environment), decompose long artifacts into steps rather than one-shotting them, and inject diversity from an explicit distribution because models left to themselves mode-collapse toward the average. poolside runs synthetic at 13% of a 6T-token pre-training mix; Anterior's datasets are ~90% synthetic; Nubank replaced most pre-launch A/B tests with simulation; Google fine-tunes 50M–500M-parameter edge models on 10k–10M synthetic samples. Model collapse is now understood as a property of ungrounded generation rather than of synthetic data per se — if all the information originates in a source document, the student can exceed the generator. The live fault lines are whether generated data belongs in model weights or only in eval sets, whether generation from a fixed seed corpus saturates at an information ceiling, and how much environment fidelity a simulation needs before its numbers transfer.

## Consensus

### Data and environments, not compute, architecture, or model choice, are the binding constraint on model and agent quality.

Support: **5** talk(s)

> "ultimately for post training be it SFT or or uh reinforcement learning data is the bottleneck"
>
> — [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [3:47](https://www.youtube.com/watch?v=ewtOo0scUh0&t=227s)

Supporting talks: [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### Domain experts, not AI engineers or automated scores, must be the ones who judge whether generated data is good enough to use.

Support: **5** talk(s)

> "Like you can't push the frontier forward from within the frontier. You need to inject that external human expertise and it needs to be good expertise."
>
> — [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [3:33](https://www.youtube.com/watch?v=-npY6XjM8CQ&t=213s)

Supporting talks: [Don’t be data poor](../talks/dont-be-data-poor.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md), [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)

### Asking a model to produce a large or complex artifact in one shot destroys correctness and diversity; generation must be decomposed into steps and its diversity sampled from an explicit distribution rather than left to the model.

Support: **4** talk(s)

> "the rule of thumb is if task is too hard for your model, then your model will start to fall on its face. Lose correctness, lose diversity. So break down the task, make it simpler."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [5:58](https://www.youtube.com/watch?v=KhYifX22yhE&t=358s)

Supporting talks: [Don’t be data poor](../talks/dont-be-data-poor.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)

### Off-the-shelf frontier models are unrealistic simulators of humans because helpfulness training makes them polite, articulate, and average; they must be calibrated or fine-tuned against real human data before their output can be trusted as evidence.

Support: **4** talk(s)

> "in our first pass at running our offline evaluation, what we noticed is that our LM user sounds almost too nice"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [13:40](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=820s)

Supporting talks: [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [Don’t be data poor](../talks/dont-be-data-poor.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)

### Production logs and traces are not directly usable as training or eval data; they must be lifted into regenerable environments with defined grading before anything can be verified against them.

Support: **4** talk(s)

> "Here we have log and feedback, but what we really need is a replayable learning environment, a simulation that we can rerun with defined grading on what success looks like, not one instance of what happened and the feedback on top of it."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [3:57](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=237s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [Don’t be data poor](../talks/dont-be-data-poor.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)

### Model collapse is avoidable when every fact in the generated sample originates in a real source document, which is why rephrasing seed data beats repeating it and lets the student surpass the generator.

Support: **3** talk(s)

> "Number one, because all the information is coming from the document on the left, you don't have any issue with model collapse."
>
> — [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [12:46](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=766s)

Supporting talks: [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [The Base Model Is Dead](../talks/the-base-model-is-dead.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

## Disagreements

### Should model-generated data be used to update model weights, or restricted to evaluation and validation?

| Position A | Position B |
|---|---|
| Synthetic data belongs in the training mix, including pre-training: rephrase seeds into it, pull post-training-shaped data forward into it, and fine-tune small models entirely on it. poolside runs it at 13% of a 6T-token pre-training corpus; Google fine-tunes tiny edge models on 10k–10M generated samples.<br>*[The Base Model Is Dead](../talks/the-base-model-is-dead.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)* | Generated data is safe for evaluation but should be kept out of weights: Anterior's datasets are ~90% synthetic and used only for eval, and Krea deliberately excluded all AI-generated images because a teacher's aesthetic imprints permanently and is visible to a trained observer.<br>*[Don’t be data poor](../talks/dont-be-data-poor.md), [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md)* |

*Why it matters: If generated data is weight-safe, a team with a small seed corpus can bootstrap a competitive model for single-digit millions; if it is not, organic data acquisition remains the gating cost and generation only buys you faster testing.*

### Where should evaluation data come from — simulation, or sampled production traffic?

| Position A | Position B |
|---|---|
| Generate it in simulation. Waiting on production traces means experimenting on live users, and a sampled slice of real cases leaves rare edge cases untested; Nubank cut iteration from weeks to under a day and reduced ~10 planned A/B tests per quarter to about one.<br>*[SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [Don’t be data poor](../talks/dont-be-data-poor.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* | Prompting a model for a few dozen test cases is an inadequate eval set; datasets should be sampled from production traffic and mutated, and obviously-generated eval items trigger eval awareness and push the model out of distribution, invalidating the measurement.<br>*[Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)* |

*Why it matters: This decides whether a team can gate releases before any real traffic exists, or must ship to users first to earn the data that gates the next release — a difference of weeks per iteration and of whether greenfield agents can be validated at all.*

### Does generating more synthetic data from a fixed seed corpus keep producing gains, or does it saturate?

| Position A | Position B |
|---|---|
| It scales: a curation recipe shows a scaling law where metrics keep improving with dataset size, rephrasing keeps a growing 6T-token corpus from saturating the model, and repeating high-quality data beats adding low-quality data.<br>*[Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)* | It hits a ceiling: any fixed dataset saturates unless the model is underparameterized, generating from corpus D produces a synthetic data wall, and rerunning a persona a thousand times with unchanged inputs adds no information at all. Escaping the plateau requires self-improvement that makes the generated task progressively harder.<br>*[Scaling Compute on Context](../talks/scaling-compute-on-context.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)* |

*Why it matters: If generation saturates, buying more generation compute against a private corpus is wasted spend and the effort belongs in acquiring adjacent real data or building difficulty-escalating loops instead.*

### How much fidelity does a synthetic environment need before its results transfer to production?

| Position A | Position B |
|---|---|
| Mocked tools in a containerized simulation are enough when the sim-to-real gap is explicitly measured: eval scores from simulation correlate highly with production, 80% of domain-expert labels confirmed the data was usable, and clinicians could distinguish synthetic from real records only ~60% of the time.<br>*[SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md), [Don’t be data poor](../talks/dont-be-data-poor.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* | Current emulation is contrived and low-fidelity. A single-node sandbox cannot provision EC2 or Cloud Run, deterministic network-failure simulation does not resemble AWS-scale behavior, and frontier-quality task data costs roughly $15M per 1,000-task benchmark precisely because it cannot be faked.<br>*[Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)* |

*Why it matters: The answer sets the cost floor for an environment program — mocked single-node sandboxes are cheap and parallelizable, while multi-node real-cloud rollouts that take hours to provision require rethinking post-training infrastructure entirely.*

## Practical Guidance

**Do:**

- Generate the artifact backwards from a sampled label so labels are correct by construction, then round-trip the generated artifact back through your extractor to confirm they stay in sync
- Sample diversity from an explicit structure — a symbolic policy decision tree, a page-rank over Wikipedia concepts — rather than asking the model to be diverse
- Fine-tune your user simulator on real user verbatims until evaluation scores go *down*; a falling score means the eval got more realistic
- Replace repeated high-quality tokens with rephrased variants of the same seed rather than showing the seed again
- Sample multiple answers per question (16x) instead of collecting proportionally more questions answered once
- Distill an expensive VLM/LLM filtering judgment into a SigLip-sized classifier before running it across a billion-item corpus
- Measure and publish the sim-to-real gap, and validate it with blind domain-expert review before trusting any simulation-derived number
- Score generated distributions with two metrics — a correlation metric and a distribution-shape metric — because a model can match the average and still muddle the variance into the middle
- Add structural tags to prompt-response pairs so a fine-tuned model attends to form rather than hallucinating specific numbers on imbalanced data
- Keep most of the mid-training mix representative of the pre-training distribution when adapting to a domain; done this way, better domain data makes an unchanged post-training harness 2–3x more effective
- For a fixed single task on edge hardware, budget 10k–10M synthetic samples to fine-tune a 50M–500M-parameter model to task quality matching a 2–4B model
- Run ablations stage by stage to find which curation steps actually move metrics, and derisk a hero run with small-scale runs under simulated token scarcity (50–100x less compute)

**Avoid:**

- Prompting a model for ~50 test queries and treating that as an offline eval dataset
- Assuming the strongest available model is the best teacher — Qwen models outperformed Claude models as teachers in the Open Thoughts Agents work
- Training an image model on frontier-model outputs: synthetic aesthetic is sticky and permanently imprints a recognizable ChatGPT/Nano Banana look
- Filtering a corpus with generic aesthetic or image-quality scores, which silently strips out the stylistic diversity you were training for
- Piling more demographic detail into a persona construction — past a point it amplifies model bias and moves results further from reality
- Rerunning a synthetic persona a thousand times on unchanged inputs to claim statistical significance; that sharpens your estimate of the model, not of the world
- Reporting an 84% vs 88% alignment difference on 50 traces as a real gain — every score needs an interval
- Plain next-token-prediction finetuning on your own corpus: loss goes to ~0, generation collapses, and no useful generalization appears
- Making benchmark items obviously synthetic, which increases eval awareness and pushes the model out of distribution
- Rendering synthetic documents into PDFs — state-of-the-art parsers already produce clean markdown, so the extra step buys nothing
- Over-optimizing pre-training data for quality over quantity, which forces harmful repetition and saturates the model early once budgets scale
- Letting AI engineers, rather than clinicians or other domain experts, decide whether a generated domain artifact is realistic

## Notable Outliers

- In blind review, clinicians could distinguish Anterior's fully synthetic medical records from real ones only about 60% of the time — and ~90% of their datasets are now synthetic. ([Don’t be data poor](../talks/dont-be-data-poor.md), [14:26](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=866s))
- Curating only the English portion of a corpus measurably improves non-English performance, with transfer magnitude tracking language similarity — with multilingual data at just 8% of the mix. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [11:34](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=694s))
- Synthetic data is so sticky that training on AI-generated images at all is disqualifying: a trained observer can identify a model heavily distilled on ChatGPT or Nano Banana Pro outputs. ([Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [7:27](https://www.youtube.com/watch?v=-tviRdpmHvs&t=447s))
- Synthetic personas have a hard accuracy ceiling set by human self-inconsistency — one study found humans were only 80% consistent with themselves. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [17:03](https://www.youtube.com/watch?v=YnNF55QV0zs&t=1023s))
- Generating synthetic data from a corpus D hits a data wall in the synthetic sense: you eventually learn all of it, so no amount of added compute buys further gains without a mechanism that makes the generated tasks harder. ([Scaling Compute on Context](../talks/scaling-compute-on-context.md), [16:52](https://www.youtube.com/watch?v=WiqDvX6isc4&t=1012s))
- Synthetic rewriting and task augmentation were expected to work as curation steps and did not, while synthetic *question* generation did. ([Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md), [12:12](https://www.youtube.com/watch?v=ewtOo0scUh0&t=732s))

## All Talks

- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Data and Environment Curation for Post-Training LLMs](../talks/data-and-environment-curation-for-post-training-llms.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Don’t be data poor](../talks/dont-be-data-poor.md)
- [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)
- [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)
- [Scaling Compute on Context](../talks/scaling-compute-on-context.md)
- [SimulationMaxxing: How we ship agents 20× faster](../talks/simulationmaxxing-how-we-ship-agents-20-faster.md)
- [The Base Model Is Dead](../talks/the-base-model-is-dead.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)
- [The Next Medium: Why Real-Time Interactive Video Changes Everything](../talks/the-next-medium-why-real-time-interactive-video-changes-everything.md)
- [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)
- [When Will The Benchmaxxing Plague End?](../talks/when-will-the-benchmaxxing-plague-end.md)
- [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)

## Speakers

- [Ahmed Ahres](../speakers/ahmed-ahres.md)
- [Akshay Sharma](../speakers/akshay-sharma.md)
- [Aman Gupta](../speakers/aman-gupta.md)
- [Anuj Iravane](../speakers/anuj-iravane.md)
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
- [Sangwu Lee](../speakers/sangwu-lee.md)
- [Shreya Rajpal](../speakers/shreya-rajpal.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Varun Singh](../speakers/varun-singh.md)

