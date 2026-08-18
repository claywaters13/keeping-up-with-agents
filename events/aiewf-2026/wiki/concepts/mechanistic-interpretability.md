---
title: "mechanistic interpretability"
type: "concept"
slug: "mechanistic-interpretability"
tier: "supporting"
maturity: "frontier"
talk_count: 4
speaker_count: 7
---

# mechanistic interpretability

**Maturity: FRONTIER** — Frontier — too new or sparse for consensus yet

*Supporting concept* &middot; discussed across **4** talk(s) by **7** speaker(s)

**Definition:** Inspecting model internals — features, activations, circuits — to explain or steer behavior, as opposed to black-box evaluation.

*Also referred to as: sparse autoencoders, crosscoders, activation sparsity, activation deltas, chain of thought visibility, reasoning trace inspection, layer sensitivity analysis*

## State of Practice

Only one talk at this conference did mechanistic interpretability proper, and its central result is that the useful object is not the model's feature space but the *difference* between a base checkpoint and its fine-tune: training a sparse autoencoder on the base-to-fine-tuned activation delta scored ~0.4 on backdoor isolation versus ~0.01 for crosscoder/joint-feature methods on the same models, with non-overlapping confidence intervals. The framing that carried was 'backdoors are directions' — an implanted trigger shows up as an anomalous activation-shift direction you can detect without knowing the trigger string in advance, which is exactly what behavioral evals cannot do. Practically it is cheap enough to be unglamorous: a 4x-expansion SAE matches a 32x one because the signal is genuinely low-dimensional, the best delta feature has zero false positives on benign code (recall is only ~25%, so you ensemble), and the result holds across middle layers and across LoRA vs. full-rank fine-tuning. The rest of the conference touched internals only obliquely — quantization practitioners treat layer-level sensitivity (first/last layers, QKV projections, linear attention) as the actionable internal structure and are migrating from accuracy benchmarks to KL divergence against the BF16 logits, while UX and agent-tooling speakers treat the model as an unopenable box and intervene at the interface and prompt layer instead. The shared thread across all four is distrust of pass/fail behavioral scoring; the disagreement is whether the fix lives inside the weights or outside the model entirely. Nothing here is tooled, benchmarked, or reproduced across labs — the delta-SAE method has not been tested against an adaptive attacker and does not apply at all to a downloaded checkpoint with no base model to diff against.

## Consensus

### Black-box behavioral scoring is insufficient to characterize a model; you have to inspect an internal or distributional signal (activation deltas, output logit distributions, reasoning traces) rather than end-output pass/fail.

Support: **3** talk(s)

> "your current defense mechanisms are essentially blind to this because they are all looking at behavior, and the behavior looks normal until the point where it stops being normal"
>
> — [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [1:19](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=79s)

Supporting talks: [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [Compression at the Edge](../talks/compression-at-the-edge.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)

## Disagreements

### Is the model's observable output — including its reasoning trace — valid evidence about its internal process?

| Position A | Position B |
|---|---|
| Yes: you can confirm an instruction took effect by watching for it in the reasoning trace. If you put the leading word 'vertical slice' in a skill and the agent echoes it back in its thinking tokens, the technique is working; the trace is the verification mechanism.<br>*[Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)* | No: behavior and self-report are exactly what a backdoored model gets right. Surface behavior looks normal until the trigger fires, so the only trustworthy signal is the activation-space difference from the base checkpoint.<br>*[Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)* |

*Why it matters: If traces are trustworthy evidence, prompt-level iteration and eval suites are sufficient engineering practice; if they are not, every organization that fine-tunes or downloads weights needs a white-box gate in CI that no current agent-tooling stack has.*

### What is the meaningful unit of model internals — the layer, or the direction?

| Position A | Position B |
|---|---|
| The layer. Which layer you touch dominates the outcome: first and last layers are critical while middle layers are near-useless, QKV projections must be kept at higher precision, and quantizing linear attention layers destroys long-context behavior while short benchmarks show nothing.<br>*[Compression at the Edge](../talks/compression-at-the-edge.md)* | The direction. The detection signal is independent of which middle layer you probe and independent of the fine-tuning regime (LoRA vs. full-rank) — the backdoor is a low-dimensional direction in activation space, not a property of a layer.<br>*[Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)* |

*Why it matters: It decides where you spend your budget: layer-level sensitivity analysis means per-architecture tooling that breaks every time a new open model ships, whereas direction-level analysis means one cheap probe (a 4x SAE) that generalizes across layers and fine-tuning methods.*

### Where should the intervention for model untrustworthiness live — inside the weights, or in the interface?

| Position A | Position B |
|---|---|
| Inside. There is a clean internal signal with near-zero false positives, so gate it: run the delta-SAE check on every build as a unit test for backdoors, before the model ever reaches a user.<br>*[Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)* | Outside. No tool can be claimed hallucination-free and the model is a black box to the user, so the honest move is interface-layer control: citations and source trails, an action plan approved before execution, an always-available stop control, version history, and explicit AI-generated labeling.<br>*[The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)* |

*Why it matters: One position says trustworthiness is a pre-deployment property you can verify and certify; the other says it is irreducibly a runtime negotiation with the user, which implies you build abort, revocation, and provenance affordances no amount of interpretability lets you skip.*

### How should a modified model be evaluated once you accept benchmarks are inadequate — by a distributional metric, or by human judgment?

| Position A | Position B |
|---|---|
| A distributional metric: compute KL divergence between the modified model's output logits and the BF16 original, and drive that distance toward zero. Accuracy benchmarks are unreliable and arenas are demonstrably gameable.<br>*[Compression at the Edge](../talks/compression-at-the-edge.md)* | Human judgment on real tasks: things that no model optimizer or benchmark captures only show up when you put the checkpoint into an actual coding agent and notice it doesn't feel right — benchmarking only works for verifiable tasks.<br>*[Compression at the Edge](../talks/compression-at-the-edge.md)* |

*Why it matters: KL divergence is automatable and can gate a release pipeline; vibe-testing cannot, so if the second position is right, no amount of internal measurement substitutes for a human in the loop on every checkpoint you ship.*

## Practical Guidance

**Do:**

- Diff, don't inspect: train the sparse autoencoder on the base-to-fine-tuned activation difference rather than on joint features of both models — ~0.4 vs. ~0.01 backdoor isolation score in a direct comparison.
- Use a 4x-expansion SAE, not 32x — the backdoor signal is low-dimensional enough that the small one matches, which makes the check cheap enough to run on every build as a unit test.
- Ensemble delta features: a single feature fires with zero false positives but recalls only ~25% of triggers, so combine several for coverage.
- Pick payloads that a static analyzer can score objectively (SQL injection) instead of subjective harms requiring an LLM judge.
- Procedurally generate poisoning data with a large combination space (~1.6 billion) so the model learns the trigger rule rather than memorizing strings.
- Replace accuracy benchmarks with KL divergence over output logits against the BF16 reference when validating a compressed checkpoint; minimize distance and size jointly.
- Keep the first and last layers, and the attention/QKV projections, at higher precision; treat middle layers as the compressible bulk.
- Check the reasoning trace to confirm a prompt-level technique actually landed — if the agent isn't repeating your leading word back, it isn't working.

**Avoid:**

- Do not rely on behavioral testing or production behavior monitors to catch a backdoor — catching one behaviorally requires already knowing the trigger, and if you know the trigger you don't need the monitor.
- Do not assume scale protects you: larger models retain implanted backdoors more persistently through safety training.
- Do not apply the delta method to an opaque downloaded checkpoint with no corresponding base model — there is nothing to diff against.
- Do not treat detection as remediation; removal is unsolved, and an adaptive attacker who knows you are running the delta check was never tested.
- Do not validate a quantized model on short benchmarks alone — quantized linear attention layers look fine on short evals and produce gibberish under real long-context load.
- Do not run quantization-aware distillation on wrong data; it more commonly breaks the model than helps it.
- Do not compress uniformly — uniformly dropping 86% of weights yields a 100% useless model, not an 86% worse one.

## Notable Outliers

- One number decides the model: the super weights result shows quantizing a single parameter of the entire model makes it ~20% dumber — an extreme case of the 'internals are non-uniform' finding. ([Compression at the Edge](../talks/compression-at-the-edge.md), [14:03](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=843s))
- Compression only works because current models are undertrained; train on ~300 trillion tokens and the quantization headroom largely disappears — implying today's interpretable redundancy is an artifact of the training regime, not a permanent property. ([Compression at the Edge](../talks/compression-at-the-edge.md), [12:33](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=753s))
- Standard sparse coding actively hides backdoors — it wastes its budget on loud generic patterns and the backdoor disappears into the mix, which is why the joint-feature approach scores at chance. ([Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [10:23](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=623s))
- Full-rank fine-tuning produced perfect separation — 100% vulnerability injection in the trigger year and 0% in the benign year — making the implanted behavior a clean binary switch. ([Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [6:44](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=404s))
- Weight quantization is near Pareto-optimal with maybe one to three bits left, so the next gains must come from KV cache compression and sparsity — and sparsity is unadopted despite NVIDIA hardware support because it degrades accuracy more than quantization does. ([Compression at the Edge](../talks/compression-at-the-edge.md), [39:54](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2394s))

## All Talks

- [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)
- [Compression at the Edge](../talks/compression-at-the-edge.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)
- [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)

## Speakers

- [Asma Beevi](../speakers/asma-beevi.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Daniel Han](../speakers/daniel-han.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Merve Noyan](../speakers/merve-noyan.md)
- [Parth Sareen](../speakers/parth-sareen.md)
- [Sachin Kumar](../speakers/sachin-kumar.md)

