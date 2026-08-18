---
title: "Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data"
type: "talk"
slug: "your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data"
org: "LexisNexis"
video_id: "IQkVMvXQKLY"
duration_sec: 837
word_count: 2246
speakers: ["Sachin Kumar"]
---

# Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data

**Speakers:** [Sachin Kumar](../speakers/sachin-kumar.md)

**Org:** LexisNexis

**Duration:** 13m 57s

[Watch on YouTube](https://www.youtube.com/watch?v=IQkVMvXQKLY)

## Summary

Sachin Kumar (LexisNexis, presenting independent peer-reviewed work accepted at IJCNN) argues that behavioral monitoring cannot catch 'sleeper agent' backdoors in fine-tuned LLMs, because such models behave normally on every test until a trigger fires. He proposes a detection method that requires no prior knowledge of the trigger: subtract base-model activations from fine-tuned activations, then train a sparse autoencoder on that difference (a 'diff SAE') rather than on joint/concatenated activations. In a controlled experiment planting a year-triggered SQL injection backdoor into a 360M-parameter model, the delta approach scored ~0.4 on a backdoor isolation metric versus ~0.01 for the cross-coding baseline — a 40x gap with non-overlapping confidence intervals and zero false positives. The result held across middle layers and across LoRA vs. full fine-tuning, and worked with an 8x smaller SAE, making it cheap enough to run as a per-build unit test. Worth watching if you fine-tune or ingest third-party checkpoints and want a concrete, low-cost supply-chain check; the honest caveats are ~25% single-feature recall, one backdoor type, small model, and no adaptive-attacker evaluation.

## Key Points

- A fine-tuned model can pass every behavioral eval and every production behavior monitor while still carrying a backdoor that activates on an untested trigger, so testing alone cannot establish safety.
- The attack surface is broader than a frontier-lab red team problem: poisoned training/RLHF data, fine-tuning vendors who return weights you cannot verify, checkpoints downloaded from hubs of unknown origin, and insiders with pipeline access.
- Behavioral testing is circular for backdoor detection — you need the exact trigger in advance to catch it, and if you already knew the trigger you would not need the monitor.
- Interpretability via cross-coding (concatenating base and fine-tuned activations and studying shared features) scores near chance because the backdoor direction has to compete with all of the model's other semantics for sparse-coding budget.
- The proposed fix is to compute delta activations (fine-tuned minus base) per input and train a sparse autoencoder on that difference, so the backdoor surfaces as a single distinct feature that fires only on triggers.
- The testbed used a procedurally generated dataset (~1.6 billion possible combinations, >95% verified-unique samples, 5,000 training samples at 60% benign/40% poisoned) with SQL injection as the payload because static analysis measures vulnerability objectively without an LLM judge.
- Full-rank fine-tuning produced perfect behavioral separation (100% vulnerable code in the trigger year, 0% in the benign year) while LoRA leaked more (100% vs. 40%) and the unmodified base model sat at 53% regardless.
- The diff-SAE signal is layer-independent, regime-independent (LoRA and full-rank alike), and works with a 4x expansion SAE matching a 32x one, evidence that the backdoor is genuinely low-dimensional.
- Stated limitations: you need a base model to diff against, one feature catches only ~25% of triggers so ensembling is needed, only one backdoor type on a 360M model was tested, and no adaptive attacker was evaluated.

## Notable Quotes

> "a model can pass every assessment you have in every behavior monitor you run and still carry a backdoor that turns it malicious on a trigger you never tested"
>
> — [0:00](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=0s) &middot; *States the core threat claim in one line.*

> "there is a clean signal that detects it, and it is in something you already have, which is the difference between the base model and your fine-tuned one"
>
> — [0:39](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=39s) &middot; *The thesis: the detector needs no new artifacts, just the two checkpoints you already hold.*

> "your current defense mechanisms are essentially blind to this because they are all looking at behavior, and the behavior looks normal until the point where it stops being normal"
>
> — [1:19](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=79s) &middot; *Names the structural reason behavioral monitoring fails.*

> "if you don't control every learning token yourself, you are exposed"
>
> — [2:01](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=121s) &middot; *Compact statement of the supply-chain exposure condition.*

> "Larger models hold the backdoor more stubbornly."
>
> — [2:48](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=168s) &middot; *A scaling claim that cuts against the hope that capability growth dilutes the problem.*

> "You can't test your way out of this, which is the problem."
>
> — [2:48](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=168s) &middot; *The talk's central negative claim about evaluation.*

> "to catch a backdoor, you need a precise trigger in advance, and if you know the trigger , you won't need a monitor"
>
> — [3:31](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=211s) &middot; *The circularity argument against behavioral backdoor testing.*

> "The poisoning training data records the backdoor into the model as the direction of its activation shift. So stop looking at the commonalities, take the difference."
>
> — [4:15](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=255s) &middot; *The method's whole premise in two sentences.*

> "we choose SQL injection because the vulnerabilities were objectively measured by static analysis, without any judgment"
>
> — [5:04](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=304s) &middot; *Explains the deliberate avoidance of subjective/LLM-judge scoring in the eval design.*

> "The point of all this variety is that the model can remember strings. She has to learn the rule."
>
> — [5:56](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=356s) &middot; *Justifies the procedural data generation — forcing rule learning over memorization.*

> "full fine- tuning of the rank gives a perfect separation, 100% vulnerability in the launch year and 0% in the benign year"
>
> — [6:44](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=404s) &middot; *Reports the sanity-check number showing the backdoor was actually installed.*

> "the cross- orders are essentially at zero around 0.01 , barely better than chance"
>
> — [7:28](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=448s) &middot; *The headline negative result against the joint-feature baseline.*

> "That's a 40-fold gap, and the confidence intervals don't even touch."
>
> — [8:12](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=492s) &middot; *The paper's central quantitative claim, with a statistical-separation assertion attached.*

> "when the delta function fires, it is always a real trigger. She never cried wolf on a benign code."
>
> — [8:58](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=538s) &middot; *The zero-false-positive claim that makes per-build deployment viable.*

> "One function catches about a quarter of the triggers, so you would combine several for coverage."
>
> — [8:58](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=538s) &middot; *The honest recall tradeoff, volunteered by the speaker rather than buried.*

> "A 4-fold sparse autoencoder corresponds to a 32- fold one. Eight times fewer functions because the backdoor is truly low-dimensional."
>
> — [9:43](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=583s) &middot; *Ties the cost argument to a structural claim about backdoor dimensionality.*

> "sparse coding wastes its budget on loud generic patterns, and the backdoor disappears into the mix"
>
> — [10:23](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=623s) &middot; *The mechanistic explanation for why concatenation-based interpretability fails here.*

> "since there are almost zero false positives, it is sufficient to leave it running on every build as a unit test for backdoors"
>
> — [11:16](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=676s) &middot; *The concrete deployment recommendation.*

> "None of this knowledge requires you to know in advance what exactly works. You are observing an anomalous direction , not a known line."
>
> — [12:02](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=722s) &middot; *States the key property that escapes the trigger-circularity trap.*

> "we didn't test an adaptive attacker who knows you're doing this and tries to minimize the data. So, this is a big open problem."
>
> — [12:50](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=770s) &middot; *The most important unaddressed threat model, named explicitly.*

> "Backdoors are directions, and the difference is where they are located."
>
> — [13:35](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=815s) &middot; *The talk's one-sentence summary.*

## Positions

- Behavioral testing and production behavior monitors cannot detect backdoored models, because catching a backdoor behaviorally requires knowing the trigger in advance. ([3:31](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=211s), confidence: stated)
- Crosscoder / joint-feature interpretability on base and fine-tuned activations performs barely better than chance (~0.01 backdoor isolation score) at isolating backdoors. ([7:28](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=448s), confidence: stated)
- Training a sparse autoencoder on the base-to-fine-tuned activation difference yields a ~0.4 backdoor isolation score, roughly a 40x improvement over the joint-feature approach, with non-overlapping confidence intervals. ([8:12](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=492s), confidence: stated)
- The best delta feature fires with zero false positives on benign inputs, but a single feature only recalls about 25% of triggers, so ensembles are required for coverage. ([8:58](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=538s), confidence: stated)
- The detection signal is independent of which middle layer is probed and of the fine-tuning regime (LoRA vs. full-rank). ([9:43](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=583s), confidence: stated)
- Backdoors are low-dimensional enough that a 4x-expansion SAE matches a 32x one, making the check cheap enough to run on every build. ([9:43](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=583s), confidence: stated)
- Larger models retain implanted backdoors more persistently through safety training, so the problem worsens with scale. ([2:48](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=168s), confidence: stated)
- Any organization that does not control every training token — via poisoned data, fine-tuning vendors, downloaded checkpoints, or insiders — is exposed to this attack. ([2:01](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=121s), confidence: stated)
- The method is inapplicable to opaque downloaded models with no corresponding base checkpoint to diff against. ([12:02](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=722s), confidence: stated)
- Detection alone is insufficient; pairing detection with actual backdoor removal is future work. ([12:50](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=770s), confidence: implied)
- SQL injection is a better backdoor payload for research than subjective harms because static analysis measures it objectively without an LLM judge. ([5:04](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=304s), confidence: stated)
- Procedurally generated training data with ~1.6 billion possible combinations forces the model to learn the trigger rule rather than memorize strings. ([5:56](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=356s), confidence: stated)

## Concepts

- [adversarial agent supervision](../concepts/adversarial-agent-supervision.md)
- [mechanistic interpretability](../concepts/mechanistic-interpretability.md)
- [post-training](../concepts/post-training.md)
- [software supply chain security](../concepts/software-supply-chain-security.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)

