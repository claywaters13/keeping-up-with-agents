---
title: "Data Quality Is the Compute Multiplier"
type: "talk"
slug: "data-quality-is-the-compute-multiplier"
track: "Data Quality"
org: "DatologyAI"
day: "Day 2 — Session Day 1"
room: "Track 9"
video_id: "_PdK6x7PQNM"
duration_sec: 1145
word_count: 4125
speakers: ["Ari Morcos"]
---

# Data Quality Is the Compute Multiplier

*Program title: Data Quality is the Compute Multiplier*

**Speakers:** [Ari Morcos](../speakers/ari-morcos.md)

**Org:** DatologyAI

**Track:** Data Quality &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 19m 05s

[Watch on YouTube](https://www.youtube.com/watch?v=_PdK6x7PQNM)

## Summary

Ari Morcos, CEO of DatologyAI, argues that data quality is the most underexploited multiplier on compute at a moment when compute is getting scarcer — H100 prices are rising again, reasoning models burn ~8x more tokens, and frontier API access is starting to be rationed. His core claim is that better data bends the learning curve itself (not just shifts it), so curation can buy the same performance for 10-145x less training compute. He walks through DatologyAI's 'four C's' pipeline (clean, curate, create, compose) and presents scaling-plot results on vision-language models, multilingual text models, rephrasing-based synthetic data, and two customer case studies (Thomson Reuters legal mid-training, and RCI's 17T-token open model trained for under $20M). Watch it if you're deciding whether to invest in data curation versus more GPUs, or if you want concrete evidence that domain adaptation need not cause catastrophic forgetting and that mid-training amplifies downstream post-training gains.

## Key Points

- Compute scarcity is worsening on both axes: H100 prices are roughly 40% up from their lows after years of decline, and reasoning models consume about eight times the tokens of non-reasoning models with another 5x projected in the coming year.
- Better data doesn't just shift the performance curve, it changes the exponent of the scaling law — the 'Beyond Scaling Laws' NeurIPS best-paper result that DatologyAI was founded on.
- There is no universally optimal dataset; a corpus is only optimal relative to a specific set of downstream tasks, so curation must be task-distribution-matched.
- DatologyAI's pipeline is four stages — clean (heuristic filters, aggressive benchmark decontamination), curate (quality classifiers, taxonomy balancing, semantic redundancy reduction, up/downsampling), create (rephrasing-based synthetic data), and compose (mixing and sequencing across at least three training phases).
- On VLMs, curation alone yielded ~14 absolute percentage points of improvement over the input MAmmoTH dataset and roughly matched Qwen 3.5 4B with 145x less training compute, while also producing markedly more concise responses and better inference-efficiency frontiers.
- Curation transfers across languages: cleaning only the English data improves non-English accuracy, with transfer magnitude correlated to language similarity, and the reverse effect holds more weakly.
- Rephrasing sidesteps model collapse because all information originates in the source document — the rephrasing model only has to reformat, not teach, so the student can exceed the teacher, but only if you rephrase high-quality documents rather than random ones.
- Mid-training Thomson Reuters' model on 100B tokens (<1% of the pre-training budget) raised LegalBench ~5 points with no catastrophic forgetting, and roughly tripled the delta their existing post-training harness produced — evidence that pre-, mid-, and post-training should be designed synergistically.
- RCI trained a fully open US-made model on 17T curated public tokens that is competitive with GLM5 and Kimi for under $20M total including salaries, compute, and failed runs — refuting the claim that custom frontier-class models cost hundreds of millions.

## Notable Quotes

> "Data quality is a compute multiplier because what it does is it it makes the learning curve steeper."
>
> — [1:59](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=119s) &middot; *The thesis of the talk in one sentence.*

> "We saw H100 prices reverse their several year-long drop which is normal for hardware and all of a sudden come up where now they're about 40% up from their lows"
>
> — [0:46](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=46s) &middot; *Concrete market number establishing the compute-scarcity premise.*

> "OpenAI has effectively started selling token futures or you can guarantee token capacity some amount of time into the future."
>
> — [1:23](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=83s) &middot; *Specific, checkable industry observation used as evidence of inference constraints.*

> "there might be a world where access to frontier API tokens is limited not as a business decision but because there's just simply not enough inference and first party products will be prioritized"
>
> — [1:23](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=83s) &middot; *A strong, contestable prediction about API availability.*

> "fundamentally the idea is we want to make it so that we get the maximum signal per token and per batch"
>
> — [2:29](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=149s) &middot; *States the optimization objective behind all the curation techniques.*

> "there's no one golden data set to rule them all that's good for everything no matter what you want to do"
>
> — [3:08](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=188s) &middot; *Directly contradicts the 'one big clean corpus' framing common in pretraining work.*

> "A data set's only going to be optimal with respect to a particular set of output tasks that you want the model to do."
>
> — [3:08](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=188s) &middot; *The precise formulation of task-relative data optimality.*

> "you can think of us as the oil refinery for data. We don't source new tokens like many data providers."
>
> — [4:09](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=249s) &middot; *Clear positioning of curation versus data acquisition as distinct businesses.*

> "benchmaxing has become a real problem and makes it very difficult to interpret model results"
>
> — [4:42](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=282s) &middot; *Names contamination as the reason published results are hard to trust.*

> "if you choose your data correctly you can actually bend the scaling laws itself you can change the exponent"
>
> — [5:52](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=352s) &middot; *The strongest technical claim in the talk, and the research basis for the company.*

> "just through curation you're able to get around a 14 absolute percentage point improvement"
>
> — [7:47](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=467s) &middot; *Headline quantitative result for the VLM experiment.*

> "The internet is an extremely biased view of the world that does not represent the world uniformly at all. And this has major implications for fairness and for the usability of these models across the world."
>
> — [9:24](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=564s) &middot; *Frames multilingual curation as an access and fairness problem, not just a metric.*

> "First off we only use 8% of the data here as multilingual tokens."
>
> — [9:54](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=594s) &middot; *Surprisingly small multilingual budget for the claimed frontier-beating result.*

> "But I just want to show this because I think it's quite interesting that curating English data benefits non-English performance."
>
> — [11:34](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=694s) &middot; *A non-obvious empirical finding about cross-lingual transfer from curation.*

> "Number one, because all the information is coming from the document on the left, you don't have any issue with model collapse."
>
> — [12:46](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=766s) &middot; *Takes a side in the model-collapse debate about synthetic data.*

> "All it needs to do is transform the left document into a true false questions accurately which is a much easier task."
>
> — [12:46](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=766s) &middot; *Explains why a student can exceed its rephrasing teacher.*

> "All documents are not created equal for rephrasing. If you just pick random sets of documents to rephrase, you will not get a great result."
>
> — [13:18](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=798s) &middot; *Names the failure mode of naive synthetic data generation.*

> "showing your model better domain specific data can actually make post- training two to three times more effective out of the box"
>
> — [15:29](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=929s) &middot; *Quantified interaction effect between mid-training and post-training.*

> "it also actually goes to show how we really should be thinking about all these stages synergistically"
>
> — [15:29](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=929s) &middot; *Argues against the common org split between pre-, mid-, and post-training teams.*

> "if you hear this story over and over again, oh, if I want to customize a model, it's going to cost hundreds of millions of dollars"
>
> — [16:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1010s) &middot; *Sets up the talk's cost-debunking claim.*

> "you can train an immensely powerful model especially in a narrow domain for high six figures million dollars. It's very doable to get a model that's extremely performant."
>
> — [17:27](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1047s) &middot; *Puts a concrete price range on custom model training.*

> "it's almost always better to repeat highquality data than it is to show lowquality data"
>
> — [17:27](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1047s) &middot; *A directly actionable heuristic that cuts against pure token-count maximization.*

> "If you're sitting in a world where you want to build a model or customize a model and you're limited on compute, how do you get past that? Invest in data"
>
> — [18:00](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1080s) &middot; *The closing prescription, stated as an explicit alternative to buying more compute.*

## Positions

- Data quality changes the exponent of the scaling law rather than merely shifting the curve, so curation is a multiplier on compute rather than a constant-factor win. ([5:52](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=352s), confidence: stated)
- Access to frontier model APIs may become limited for capacity reasons rather than business reasons, with first-party products prioritized. ([1:23](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=83s), confidence: stated)
- No single dataset is universally optimal; optimality is defined only relative to a target set of downstream tasks. ([3:08](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=188s), confidence: stated)
- Curation alone, with no post-training, can push a VLM past the public Pareto frontier and match Qwen 3.5 4B using 145x less training compute. ([7:47](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=467s), confidence: stated)
- Data curation reduces response length, improving inference efficiency by roughly 35x fewer flops per correct answer versus Qwen 3.5. ([8:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=530s), confidence: stated)
- Curating only the English portion of a corpus measurably improves non-English performance, with transfer magnitude correlated to language similarity. ([11:34](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=694s), confidence: stated)
- Small-scale runs on properly curated data with simulated token scarcity predict large-model performance, letting teams derisk a hero run with 50-100x less compute. ([10:59](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=659s), confidence: stated)
- Rephrasing-based synthetic data avoids model collapse because all information originates in the source document, allowing the trained model to surpass the rephrasing model. ([12:46](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=766s), confidence: stated)
- Domain adaptation does not require sacrificing general capability; keeping most of the mid-training mix representative of the pre-training distribution prevents catastrophic forgetting entirely. ([14:57](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=897s), confidence: stated)
- Mid-training on better domain data makes an unchanged post-training harness two to three times more effective. ([15:29](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=929s), confidence: stated)
- Pre-training, mid-training, and post-training should be designed as one synergistic system rather than handed off between independent teams. ([15:29](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=929s), confidence: stated)
- A model competitive with the open frontier can be trained for under $20 million total including salaries, compute, and all failed attempts, so the 'hundreds of millions' figure is false. ([16:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1010s), confidence: stated)
- Up to some threshold, repeating high-quality data beats showing additional low-quality data. ([17:27](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1047s), confidence: stated)
- Data quality is the single most underleveraged compute multiplier available to teams today. ([18:00](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=1080s), confidence: stated)
- Frontier labs deliberately do not publish their data curation methods because the competitive disincentive to share is strong. ([5:52](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=352s), confidence: stated)

## Concepts

- [benchmark contamination](../concepts/benchmark-contamination.md)
- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [context compaction](../concepts/context-compaction.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [post-training](../concepts/post-training.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [scaling laws](../concepts/scaling-laws.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)

