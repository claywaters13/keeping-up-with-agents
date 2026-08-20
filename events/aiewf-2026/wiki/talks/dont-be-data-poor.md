---
title: "Don’t be data poor"
type: "talk"
slug: "dont-be-data-poor"
track: "AI in Healthcare"
org: "Anterior"
day: "Day 4 — Session Day 3"
room: "Track 7"
video_id: "XAsb7MIAzm8"
duration_sec: 1005
word_count: 3026
speakers: ["Anuj Iravane"]
---

# Don’t be data poor

*Program title: Don't be data poor*

**Speakers:** [Anuj Iravane](../speakers/anuj-iravane.md)

**Org:** Anterior

**Track:** AI in Healthcare &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 16m 45s

[Watch on YouTube](https://www.youtube.com/watch?v=XAsb7MIAzm8)

## Summary

Anuj Iravane, who leads AI at Anterior, describes how his team builds eval datasets for high-stakes healthcare workflows (prior authorization, payment integrity, HEDIS) when the data they most need — scanned fax bundles of medical records — is PHI they are contractually forbidden to retain, reuse, or even derive from. His answer is to reverse the inference task: sample a label, deterministically sample a reasoning trace from a policy modeled as a symbolic decision tree, then generate a synthetic patient record backwards from that conditioning input, layer by layer (patient invariants → patient journey → document plan → hydrated documents → eval-driven refinement). The talk argues this beats one-shotting records with an LLM, which mode-collapses because medical records are barely represented in pretraining and current objectives reward helpfulness rather than diversity. Concretely: ~90% of Anterior's eval datasets are now synthetic, clinicians in blind review distinguish synthetic from real only ~60% of the time, and datasets can be built just-in-time for a customer deployment instead of waiting on real data. The closing argument is organizational — the pipeline is modeled as skills on an internal agent harness so clinicians, not AI engineers, own its logic. Worth watching if you face data you can't keep, can't get, or can't afford to label.

## Key Points

- Anterior's workflows are policy-guided decision-making over highly unstructured data — 300+ page scanned fax bundles with handwriting, tables, and checkboxes — where ~70% of medical communication still arrives by fax and 95% accuracy is not an acceptable bar.
- The core constraint is legal, not technical: the medical records they need for evals are PHI that contracts forbid them to retain, reuse, or derive from, so even redacted or anonymized derivative copies are off the table.
- One-shotting a synthetic record with an LLM fails on diversity; Iravane attributes the mode collapse to thin representation of this data type in pretraining corpora and to pre/post-training objectives that reward helpfulness rather than creativity or diversity.
- Their pipeline reverses the forward task: sample a random label, sample a reasoning trace, then generate the record backwards — which yields correct labels by construction and skips expensive ground-truth labeling.
- Because Anterior already models policies as explicit symbolic decision trees (which they say improves accuracy and consistency in LLM execution), they can deterministically sample reasoning traces and get a more uniform prior distribution than an LLM would produce.
- Generation is coarse-to-fine — patient invariants, then a patient journey of provider encounters, then a per-encounter document plan, then parallel document hydration — which keeps prompt payloads token-efficient and lets the pipeline scale to long patient histories without blowing context windows.
- A refinement loop runs evals over the output, including an LLM cross-document consistency check (needed because documents are fanned out in parallel) and a round-trip check that re-executes the original task against the generated record.
- Everything stays in markdown text rather than rendered PDFs, on the grounds that state-of-the-art PDF parsers already collapse complex PDFs into markdown, so the extra rendering step buys little.
- Clinicians own the pipeline in two ways: human-in-the-loop steering at each generation step (often seeded by interesting production cases), and skill files on an internal agent harness so a new document type needs no engineering change.
- Results: ~90% of their datasets are synthetic, clinicians in blind review distinguish synthetic from real only about 60% of the time, and datasets are created just-in-time for customer deployments — though synthetic data is currently used only for evaluation, not training.

## Notable Quotes

> "But the problem is we can't really keep this data. It's PHI, it's highly protected. We can't retain it, we can't reuse it, we can't even derive information from it."
>
> — [2:15](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=135s) &middot; *States the hard constraint that motivates the entire approach.*

> "So, so what this talk is about is like what do you do when the dataset you most need is also the data you're least allowed to keep."
>
> — [2:52](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=172s) &middot; *The talk's thesis question in one line.*

> "I think around 70% of medical communication still happens via fax."
>
> — [0:52](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=52s) &middot; *Concrete number that grounds why the input data is so hostile.*

> "in healthcare the the baselines for accuracy are just exceptionally high. 95% is not good enough."
>
> — [1:34](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=94s) &middot; *Names the accuracy bar that makes edge-case coverage non-negotiable.*

> "often times these medical records are over 300 pages long and it's like imagining if you wouldn't ask an LLM to write a novel for you in one shot"
>
> — [3:32](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=212s) &middot; *The analogy for why one-shot synthetic generation breaks down, with the scale figure attached.*

> "there's very little exposure to this data source in the pre-training data corpus"
>
> — [4:17](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=257s) &middot; *First of two stated causes of mode collapse on this data type.*

> "the idea we had was to try and reverse this process"
>
> — [4:57](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=297s) &middot; *The central technical move of the talk.*

> "And at Antheir, actually, we we spend a lot of time and energy in trying to model these policies explicitly as decision trees."
>
> — [6:24](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=384s) &middot; *An architectural commitment others might skip, and the enabler for deterministic trace sampling.*

> "in theory, you're able to test uh for far more scenarios than you would likely get from production data sources"
>
> — [7:07](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=427s) &middot; *The coverage argument for synthetic data over sampled production cases.*

> "There'll always be rare edge cases uh that are outside the distribution just because of the fact that our data is so uh highly variant."
>
> — [7:44](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=464s) &middot; *Explains why a 95% score on a 200-case customer sample tells you little.*

> "So, you can scale this pipeline. You can have a much longer patient journey and you can just fan out and generate documents that way without overloading the context windows of your LLMs."
>
> — [9:40](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=580s) &middot; *The scaling payoff of coarse-to-fine layering, stated as a tradeoff against context limits.*

> "So, we can do this sort of round trip check to ensure that our data is actually in sync and by default get the correct labels by construction."
>
> — [10:22](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=622s) &middot; *The labeling-cost argument for reverse generation.*

> "It is possible to go from that to a rendered PDF. But we don't really see much value in doing that because we have state of the art PDF parsers today available to everyone"
>
> — [11:00](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=660s) &middot; *A specific scope decision — stay in text — that others building document pipelines might contest.*

> "Like you want your domain experts to be the ones telling you what's good, what's not good."
>
> — [11:38](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=698s) &middot; *Answers the fidelity-validation question by refusing to answer it as an engineer.*

> "I feel like skills are really an amazing interface between AI engineers and domain experts, especially in vertical AI."
>
> — [13:43](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=823s) &middot; *Generalizes the implementation detail into a claim about vertical AI tooling.*

> "Roughly 90% of our data sets are already made of synthetic data."
>
> — [13:43](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=823s) &middot; *The headline adoption number.*

> "In a blind review, clinicians were not able were only able to distinguish synthetic from real about 60% of the time."
>
> — [14:26](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=866s) &middot; *The one quantified fidelity result, honestly framed as room for improvement.*

> "well, most of our data sets today then are created just in time for these customer deployments"
>
> — [14:26](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=866s) &middot; *The operational payoff — no longer blocked on customer data before go-live.*

> "try reversing your inference workflow. Diversity should always be sampled from a from an appropriate distribution for your use case. Try to emulate the process in which data was actually generated."
>
> — [15:02](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=902s) &middot; *The three transferable design rules, compressed.*

> "it's really important to give your domain experts the keys because these are the people who know about your data"
>
> — [15:42](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=942s) &middot; *The organizational takeaway he ranks as most important.*

> "So, you don't need a PHI problem for this anywhere. The data you need is ephemeral, sensitive, or even expensive to label."
>
> — [16:19](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=979s) &middot; *Generalizes the healthcare case to any domain with unavailable or costly data.*

## Positions

- In healthcare AI, a 95% accuracy score is not good enough to ship on. ([1:34](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=94s), confidence: stated)
- LLMs are a good tool for generating synthetic data, but asking one to one-shot a full 300-page medical record does not work. ([3:32](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=212s), confidence: stated)
- LLM mode collapse on this data stems from two causes: little exposure to medical records in pretraining corpora, and pre/post-training objectives that optimize for helpfulness rather than creativity or diversity. ([4:17](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=257s), confidence: stated)
- Modeling policies explicitly as symbolic decision trees improves accuracy and consistency when executing them in LLM-based workflows. ([6:24](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=384s), confidence: stated)
- Sampling reasoning traces from a symbolic policy yields a more uniform and effective prior distribution than what an LLM would produce on its own. ([7:07](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=427s), confidence: stated)
- A synthetic pipeline can test more scenarios than production data sources, because a sampled set of real customer cases leaves rare edge cases untested. ([7:07](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=427s), confidence: stated)
- Generating a record backwards from a sampled label yields correct labels by construction, removing the need for an expensive ground-truth labeling process. ([10:22](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=622s), confidence: stated)
- Rendering synthetic records into PDFs adds little value, because current state-of-the-art PDF parsers already convert complex PDFs into clean markdown. ([11:00](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=660s), confidence: stated)
- AI engineers cannot judge whether a synthetic medical record is good; only domain experts can. ([11:38](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=698s), confidence: stated)
- Skills running on an agent harness let a clinician add a new document type to the pipeline with no engineering changes required. ([13:43](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=823s), confidence: stated)
- Skills are an effective interface between AI engineers and domain experts, particularly in vertical AI. ([13:43](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=823s), confidence: stated)
- About 90% of Anterior's datasets are synthetic, and they currently use synthetic data only for evaluation rather than training. ([13:43](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=823s), confidence: stated)
- In blind review, clinicians distinguished synthetic records from real ones only about 60% of the time. ([14:26](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=866s), confidence: stated)
- Being able to generate data from scratch removes the dependency on waiting for customer data before going live in production. ([15:02](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=902s), confidence: stated)
- Synthetic pipelines should emulate the real-world process by which the data was originally generated — here, documentation produced during provider encounters. ([15:42](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=942s), confidence: stated)
- Domain experts, not AI engineers, are what drive a data pipeline toward recursive self-improvement. ([15:42](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=942s), confidence: stated)
- This approach applies beyond PHI to any domain where the needed data is ephemeral, sensitive, or expensive to label. ([16:19](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=979s), confidence: stated)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [benchmark design](../concepts/benchmark-design.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)

