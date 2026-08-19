---
title: "mechanistic interpretability"
type: "concept"
slug: "mechanistic-interpretability"
tier: "supporting"
maturity: "frontier"
talk_count: 5
speaker_count: 8
---

# mechanistic interpretability

**Maturity: FRONTIER** — Frontier — too new or sparse for consensus yet

*Supporting concept* &middot; discussed across **5** talk(s) by **8** speaker(s)

**Definition:** Inspecting model internals — features, activations, circuits — to explain or steer behavior, as opposed to black-box evaluation.

*Also referred to as: sparse autoencoders, crosscoders, activation sparsity, activation deltas, chain of thought visibility, reasoning trace inspection, layer sensitivity analysis*

## State of Practice

Mechanistic interpretability shows up at this conference not as a research program but as a small number of shipped tools, and only one talk treats it as its central subject. The concrete result is that the base-model-to-fine-tuned activation *difference* — not joint features over both — is where implanted behavior lives: a sparse autoencoder trained on that delta reaches a ~0.4 backdoor isolation score against ~0.01 for crosscoder-style joint features, with non-overlapping confidence intervals, and the signal is invariant to which middle layer is probed and to LoRA vs. full-rank fine-tuning. Because backdoors turn out to be low-dimensional (a 4x-expansion SAE matches a 32x one) and the best delta features fire with zero false positives on benign code, the check is cheap enough to run as a per-build unit test rather than as a research artifact. Outside safety, SAEs appear as production data infrastructure: Krea trains them on vision-model activations to get an unsupervised tagging system for watermarks, signatures, and blur, as one of ~30-40 in-house filters over a 2-10B image corpus. The adjacent, non-interpretability version of the same instinct is everywhere — super-weight sensitivity guiding which layers stay at 16-bit, KL divergence over logits replacing accuracy benchmarks for quantized models — but these inspect weights and output distributions, not circuits. The shared premise across all of it is that aggregate behavioral scores hide the failure you care about; the disagreement is whether you need model internals to find it.

## Disagreements

### To detect a property a model is hiding, do you need to inspect its internals, or are output-level signals (logit distributions, traces, hands-on use) sufficient?

| Position A | Position B |
|---|---|
| Internals are required: the poisoning signal is recorded as a direction in activation space and is invisible behaviorally until it fires, so you train an SAE on the base-vs-fine-tuned activation delta and monitor for anomalous directions; likewise, feature-level tags derived from a vision model's own activations beat off-the-shelf aesthetic and quality scorers for corpus filtering.<br>*[Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)* | Output-level signals are what practitioners actually use and trust: measure KL divergence between the quantized and BF16 model's output logits rather than opening the model up, and fall back to running the model in a real harness because 'it doesn't feel right' catches what no optimizer or benchmark does; similarly, verify a skill's instruction landed by watching the agent repeat the leading word in its reasoning traces.<br>*[Compression at the Edge](../talks/compression-at-the-edge.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)* |

*Why it matters: It decides where verification budget goes — building activation-diff tooling and per-build SAE checks, versus better output-distribution metrics and hands-on eval harnesses. The internals camp's specific counterexample is that output-level checks are structurally blind to trigger-conditional behavior you never sampled, which no amount of better black-box metric fixes.*

## Practical Guidance

**Do:**

- Diff activations between the base checkpoint and your fine-tune and train the sparse autoencoder on the difference, not on both models' features jointly — sparse coding over joint activations spends its budget on loud generic patterns and the backdoor disappears into the mix.
- Use a small expansion factor: a 4x SAE performs like a 32x one on this task, so the per-build cost is eight times fewer features than you would default to.
- Ensemble several delta features rather than shipping one — a single feature has essentially zero false positives but recalls only about a quarter of triggers.
- Run the check on every build as a unit test, which the near-zero false-positive rate makes tolerable in CI.
- Probe any middle layer; the signal is stable across layer choice and across LoRA vs. full-rank fine-tuning, so don't spend time tuning that.
- Pick payloads that a static analyzer can score objectively (e.g. SQL injection) when evaluating a detector, so results don't depend on an LLM judge.
- Generate trigger training data procedurally across a very large combination space (~1.6B) so the model must learn the rule instead of memorizing strings.
- Train an SAE on your vision encoder to harvest unsupervised tags for corpus filtering (watermarks, signatures, blur), then distill the expensive judgments into a SigLip-sized classifier before running them over billions of images.

**Avoid:**

- Treating behavioral evals and production behavior monitors as backdoor coverage — catching a backdoor behaviorally requires knowing the trigger in advance, and if you knew the trigger you wouldn't need the monitor.
- Assuming scale helps: larger models retain implanted backdoors more stubbornly through safety training.
- Applying the delta method to an opaque downloaded checkpoint with no corresponding base model — there is nothing to diff against.
- Treating detection as remediation; removing the backdoor once found is unsolved, and no one has tested an adaptive attacker who knows you are running this check.
- Leaning on aggregate accuracy benchmarks as your fidelity signal for a modified model — short benchmarks looked clean on quantized linear-attention layers that produce gibberish under real long-context load.
- Filtering training data with generic aesthetic or image-quality scorers, which silently strips stylistic diversity that some users specifically want.

## Notable Outliers

- Backdoors are directions in activation space, and the difference between base and fine-tuned model is where those directions are located — detection requires no prior knowledge of the trigger, only the observation of an anomalous direction. ([Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [13:35](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=815s))
- Delta-trained SAE features reach ~0.4 backdoor isolation versus ~0.01 for crosscoder joint features — a 40x gap with non-touching confidence intervals. ([Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [8:12](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=492s))
- Backdoors are low-dimensional enough that a 4x-expansion SAE matches a 32x one with eight times fewer features. ([Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [9:43](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=583s))
- The super weights result: quantizing a single number in the entire model makes it roughly 20% dumber — individual weights, not just layers, carry outsized causal load. ([Compression at the Edge](../talks/compression-at-the-edge.md), [14:03](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=843s))
- Sparse autoencoders trained on a vision model yield a usable unsupervised tagging system, deployed as production data-curation infrastructure over a 2-10 billion image corpus rather than as an interpretability experiment. ([Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md), [11:46](https://www.youtube.com/watch?v=-tviRdpmHvs&t=706s))
- First and last layers are disproportionately important while middle layers are comparatively expendable, which is why a model at 14% of its size can retain ~76% of its accuracy under mixed precision. ([Compression at the Edge](../talks/compression-at-the-edge.md), [12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s))
- A behavioral proxy for internal state that actually works in practice: put a leading word in the skill text and confirm it landed by watching the agent repeat that word back in its reasoning traces. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [13:13](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=793s))

## All Talks

- [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)
- [Compression at the Edge](../talks/compression-at-the-edge.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)
- [Training Krea 2: What matters in generative model training](../talks/training-krea-2-what-matters-in-generative-model-training.md)
- [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)

## Speakers

- [Asma Beevi](../speakers/asma-beevi.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Daniel Han](../speakers/daniel-han.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Merve Noyan](../speakers/merve-noyan.md)
- [Parth Sareen](../speakers/parth-sareen.md)
- [Sachin Kumar](../speakers/sachin-kumar.md)
- [Sangwu Lee](../speakers/sangwu-lee.md)

