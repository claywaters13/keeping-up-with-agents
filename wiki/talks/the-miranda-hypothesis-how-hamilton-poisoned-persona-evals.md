---
title: "The Miranda Hypothesis: How Hamilton Poisoned Persona Evals"
type: "talk"
slug: "the-miranda-hypothesis-how-hamilton-poisoned-persona-evals"
org: "Results Gen"
video_id: "IJXjTLPzvAU"
duration_sec: 3497
word_count: 7031
speakers: ["Jacob E. Thomas"]
---

# The Miranda Hypothesis: How Hamilton Poisoned Persona Evals

**Speakers:** [Jacob E. Thomas](../speakers/jacob-e-thomas.md)

**Org:** Results Gen

**Duration:** 58m 17s

[Watch on YouTube](https://www.youtube.com/watch?v=IJXjTLPzvAU)

## Summary

Jacob E. Thomas argues that the evaluation stack for role-playing language agents measures the wrong property: benchmarks like InCharacter score personality fidelity and stylistic naturalness, but have no mechanism to check whether a persona's reasoning is bounded by what that historical figure could actually have known or argued at a given moment. His 'Miranda hypothesis' holds that culturally dominant representations (the Hamilton musical, Spielberg's Lincoln) vastly outweigh primary documents in training corpora, so models default to a salience-weighted composite that is fluent, morally legible to modern audiences, and corresponds to the figure at no verifiable point in their life — and RLHF amplifies this rather than correcting it, because raters carry the same myths. He proposes a fourth paradigm, 'epistemic simulation' (corpus-bounded, temporally anchored, expert-loop evaluated), argues context-window anchoring beats fine-tuning on auditability, accessibility, and accuracy grounds, and presents a pre-registered Lincoln experiment (4 moments × 3 seeding conditions, 5 historian-written diagnostic questions, 3-axis rubric) built with working historians. He has no results yet — the talk is an instrument and an open invitation to run it in parallel. Worth watching if you ship character bots, companion AI, or pedagogical personas, or if you care about eval design where fluency and truth diverge.

## Key Points

- State-of-the-art RPLA benchmarks report ~80.7% alignment with human-perceived personality, but that number measures whether output sounds like the figure, not whether the figure's reasoning is consistent with their documentary record at a specific moment.
- The Miranda hypothesis has three parts: culturally dominant representations outweigh primary sources in training corpora; autoregressive pretraining has no architectural capacity to distinguish a 1789 letter from a 2019 tweet; so the output is a salience-weighted composite that matches the figure at no verifiable moment in their life.
- RLHF makes compositing worse, not better — human raters judge with the same mythologized frameworks that saturate the corpus, so preference optimization rewards handing users the Hamilton they already believe in (algorithmic sycophancy).
- Time-locked models trained to a fixed cutoff solve substrate-level future contamination but not the underlying problem: you still get a composite, merely averaged over a different textual period, because period anchoring is not persona anchoring.
- For role-playing specifically, Thomas rejects the word 'agent' and proposes 'role-playing language system' — a five-component configured encounter (prompt, primary-source anchor, temporal anchor, swappable off-the-shelf model, human curator) that is versionable, auditable, and reproducible, unlike a persona smeared across weights.
- Context-window anchoring beats fine-tuning for personas on three grounds: documents survive as inspectable documents rather than being dissolved into parameters; the empirical record (a 2026 Nature Medicine study, plus biomedical fine-tuning underperforming base models via catastrophic forgetting) contradicts the assumption that specialization helps; and context windows are a 'kitchen table capability' accessible to archivists and grad students, while fine-tuning is institutional.
- The pre-registered experiment instantiates four Lincolns (1847 Whig, 1858 Free Soil Republican, 1860 constitutional unionist, 1862–65 emancipator) across three seeding conditions (primary sources, modern biography, bare model), scoring 60 responses on anachronism detection (40%), documentary consistency (35%), and contextual plausibility (25%).
- The rubric deliberately excludes rhetorical authenticity as a scoring axis, because rewarding 'sounds like Lincoln' would validate the exact failure the instrument exists to catch; plain-but-faithful outranks fluent-but-anachronistic.
- Domain experts are a build-time and gate-time requirement, not a runtime cost — the historian, classicist, or theologian authors the questions, gold set, and rubric once, which then functions as a pipeline gate re-run whenever the base model changes.

## Notable Quotes

> "evaluates personality fidelity in RPLAs, and it reports state-of-the-art systems hitting 80.7% alignment with human-perceived personalities of that target character"
>
> — [3:44](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=224s) &middot; *the headline benchmark number the whole talk is built to reinterpret*

> "If a dominant failure mode is anachronistic compositing, and your evals measure fluency and personality consistency, then your evals cannot detect the dominant failure."
>
> — [4:43](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=283s) &middot; *the thesis in one conditional, stated twice in the talk*

> "Convincingness and fidelity are independent properties. A system can score perfectly on personality consistency and still produce a figure reasoning from knowledge his historical counterpart never possessed."
>
> — [9:50](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=590s) &middot; *the structural claim that separates the two things evals conflate*

> "The point is that the model gives you none of the complication. It sands a genuinely disputed record down to a single comfortable hero."
>
> — [14:06](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=846s) &middot; *names the concrete harm using the Hamilton-on-slavery example*

> "the composite Hamilton knows he will be the subject of a Broadway musical. The composite Lincoln has already read the Gettysburg Address, even if he was summoned before he wrote it."
>
> — [17:31](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1051s) &middot; *the sharpest illustration of temporal leakage in persona instantiation*

> "Compositing is not a bug that you patch in post training. Post training reinforces it."
>
> — [20:23](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1223s) &middot; *directly contradicts the assumption that alignment mitigates the problem*

> "Period anchoring is not persona anchoring. The temporal frame of the contamination changes, but the contamination persists."
>
> — [21:19](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1279s) &middot; *concise rebuttal to time-locked models as a fix*

> "The persona is the configuration, not the checkpoint. No more located in the weights than Hamlet is located in Laurence Olivier's body."
>
> — [25:13](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1513s) &middot; *the reframe from agent to configured encounter, in one line*

> "Fine-tuning tries to make the model be the persona. The context window lets the model speak through the persona's record."
>
> — [27:12](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1632s) &middot; *states the architectural tradeoff the talk asks engineers to decide*

> "Fine-tuning suppresses random distortion at the surface while amplifying it underneath."
>
> — [28:10](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1690s) &middot; *counterintuitive claim aimed squarely at engineers who assume fine-tuning is better*

> "In a 2026 Nature Medicine study, general-purpose frontier models from Google, OpenAI, and Anthropic outperformed dedicated specialized clinical AI tools on physician-reviewed tasks blinded across 12 clinics."
>
> — [29:05](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1745s) &middot; *the empirical citation supporting the anti-fine-tuning position*

> "It's an institutional capability. The context window requires literacy, a set of documents and access to any frontier model, including a free tier. It's a kitchen table capability."
>
> — [32:12](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1932s) &middot; *the accessibility argument that Thomas insists is technical rather than political*

> "You cannot accuse a pre-registered instrument of cherry-picking because the instrument and the predictions were fixed before the data existed."
>
> — [41:10](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=2470s) &middot; *the methodological standard he proposes eval talks should adopt*

> "A response that sounds like Lincoln but reasons unlikes him fails. No matter how fluent."
>
> — [48:19](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=2899s) &middot; *the scoring inversion current eval stacks cannot perform*

> "A persona system without a domain expert in its evaluation loop is a thermometer that cannot read temperature. It returns a confident number, but it's measuring something else."
>
> — [51:05](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=3065s) &middot; *the talk's central metaphor for miscalibrated persona benchmarks*

> "The domain expert is a build time and gate time requirement, not a runtime cost."
>
> — [52:48](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=3168s) &middot; *the practical answer to 'do I need a historian on staff?'*

> "We are not bringing historians into AI architecture, we are bringing language models into the archive."
>
> — [53:43](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=3223s) &middot; *the inversion that organizes the entire framework*

> "You do not want a model that is your mother. You want a model that can speak with your mother's documents in the room."
>
> — [55:23](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=3323s) &middot; *the personal origin story that grounds the abstract argument in stakes*

> "A framework that cannot meet a grandchild at her grandmother's letters is not a framework at all. It's just another failed product."
>
> — [56:10](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=3370s) &middot; *states the hardest-use-case standard he holds the framework to*

## Positions

- Existing persona benchmarks (e.g. InCharacter) measure personality consistency and fluency and have no mechanism to detect whether a persona's reasoning is constrained to its documentary record. ([8:49](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=529s), confidence: stated)
- Convincingness and historical fidelity are independent properties, so a system can score perfectly on personality consistency while reasoning from knowledge the figure never possessed. ([9:50](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=590s), confidence: stated)
- Culturally dominant representations of a figure exceed that figure's primary documentary record in training corpora by orders of magnitude, and are more recent and more recurrent. ([17:31](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1051s), confidence: stated)
- RLHF and post-training amplify compositing rather than correcting it, because human raters' frameworks were formed by the same dominant narratives. ([19:25](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1165s), confidence: stated)
- Time-locked models trained to a fixed cutoff do not solve persona compositing; they only relocate the contamination to an earlier textual moment. ([21:19](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1279s), confidence: stated)
- For role-playing systems specifically, the word 'agent' is an error because it locates the persona in the weights, where it cannot be inspected, versioned, or handed to a qualified reviewer. ([24:19](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1459s), confidence: stated)
- Fine-tuning a persona is worse than context-window anchoring: it layers a thin personal signal over vast cultural sediment in the base weights in ways no longer open to audit. ([28:10](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1690s), confidence: stated)
- General-purpose frontier models outperformed specialized clinical AI tools in a 2026 Nature Medicine study, and biomedically fine-tuned models underperformed their general-purpose base models due to catastrophic forgetting. ([29:05](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1745s), confidence: stated)
- The property that makes context-window architecture ethical (preserved provenance, reversible encounter, human interpretive custody) is the same property that makes it auditable and debuggable. ([31:05](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1865s), confidence: stated)
- Accessibility is a technical argument, not a populist one: the architecture admitting the most diverse population of curators is most likely over time to surface the documentary anchorings the field needs. ([33:09](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1989s), confidence: stated)
- Rhetorical authenticity ('does it sound like Lincoln?') must be excluded as a scoring axis, because rewarding voice validates the exact failure the instrument exists to catch. ([47:19](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=2839s), confidence: stated)
- Automated metrics structurally cannot adjudicate fidelity, because fidelity is a relation between output and archive and the metric cannot see the archive. ([51:05](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=3065s), confidence: stated)
- Expert-in-the-loop persona evaluation is practical at product scale because the expert builds the instrument once and it functions as a pre-ship gate, re-run when the base model changes. ([52:03](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=3123s), confidence: stated)
- A modern interpretive biography used as anchor material will produce a persona that sounds more coherent than the figure's own strategically ambiguous words, making it a subtler contamination source than a bare model. ([39:02](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=2342s), confidence: stated)
- The composite failure is reproducible today on any frontier model — a bare-model Lincoln dated 1847 reasons from 20th-century 'inherent executive authority' premises he would not hold for fifteen years. ([44:29](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=2669s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [context engineering](../concepts/context-engineering.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [reward hacking](../concepts/reward-hacking.md)
- [scaling laws](../concepts/scaling-laws.md)
- [simulation environments](../concepts/simulation-environments.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)

