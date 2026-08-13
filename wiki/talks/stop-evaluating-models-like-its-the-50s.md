---
title: "Stop Evaluating Models Like It's the 50s"
type: "talk"
slug: "stop-evaluating-models-like-its-the-50s"
track: "Search & Retrieval"
org: "Mindmakers"
day: "Day 2 — Session Day 1"
room: "Track 3"
video_id: "O3FEoMYvUf8"
duration_sec: 1414
word_count: 3878
speakers: ["Niv Granot", "Yuval Belfer"]
---

# Stop Evaluating Models Like It's the 50s

*Program title: Stop Chunking Like It's 2022*

**Speakers:** [Niv Granot](../speakers/niv-granot.md), [Yuval Belfer](../speakers/yuval-belfer.md)

**Org:** Mindmakers

**Track:** Search & Retrieval &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 23m 34s

[Watch on YouTube](https://www.youtube.com/watch?v=O3FEoMYvUf8)

## Summary

Alejandro Vidal, founder of Mindmakers, argues that the industry's standard practice of scoring LLM benchmarks by counting correct answers is classical test theory — a 1950s-era method — and that item response theory (IRT) from psychometrics is a strictly better tool. IRT models each benchmark question as a curve with a difficulty parameter (B) and a discrimination parameter (A), and estimates each model's latent 'intelligence' (theta) with likelihood intervals rather than a raw percentage. He demonstrates with real epoch.ai data that two models separated by only 2 correct answers out of 337 differ by nearly a full standard deviation in theta, showing raw accuracy can hide real capability gaps. He then walks through five practical applications: auditing benchmarks to find mislabeled or negatively-discriminating items, shrinking a benchmark ~5x while preserving 99% ranking correlation, using residuals to detect contamination and broken inference, adaptive-testing 'fingerprint sets' to catch benchmark leakage by specific labs, and correlating residuals to detect distillation and model lineage. Worth watching if you build or maintain internal evals and want concrete statistical machinery rather than another leaderboard critique.

## Key Points

- Summing correct answers assumes every benchmark item is equally important, which is a strong and usually wrong assumption since items vary in difficulty and some are outright mislabeled.
- Item response theory assigns each item a difficulty parameter B and a discrimination parameter A, and maps model intelligence (theta) to the probability of answering that item correctly.
- Because theta and B are on a shared normal-distribution scale, a model's score becomes interpretable on its own rather than only relative to whatever other models were run on the benchmark.
- In real epoch.ai data, Claude Opus 4.1 (245 correct) and Gemini 3 Pro (247 correct) out of 337 questions differ by almost one standard deviation of theta, because the harder items count more.
- Items with negative discrimination — where better models are more likely to get them wrong — flag mislabeled gold answers, such as a question asking for passengers whose gold answer was passengers plus crew.
- Selecting items by highest discrimination shrank one benchmark from 484 items to roughly 97 while retaining 99% correlation with the original ranking, nearly a 5x cost saving; random selection performed far worse.
- Well-designed benchmarks like GPQA show no such compression benefit, because their items are all highly discriminative and non-overlapping, so random subsets perform about as well.
- Per-item residuals expose outliers that can indicate contamination, overfitting, or a misconfigured inference platform such as bad quantization.
- Adaptive testing with a shared anchor set plus per-organization 'fingerprint sets' of hard items lets a benchmark owner detect which lab trained on leaked questions, via unusually low residuals on that lab's private set.
- Correlating residuals across models produces a lineage fingerprint that clusters same-lab models, distillations and their base models, and effort-level variants of the same model.

## Notable Quotes

> "at this moment the state in the industry is counting the number of right answers. That actually has a name. It's classical test theory. And we have by far better tools to do that."
>
> — [0:02](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=2s) &middot; *States the talk's thesis and the specific method it targets.*

> "We are saying that every question is equally important. They should weigh the same, which is kind of insane if you think about that."
>
> — [1:17](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=77s) &middot; *Names the buried assumption in accuracy scoring.*

> "The B parameter is going to be the difficulty of each one of them, and we're going to create a function for each question. That function maps the LLM intelligence, okay? To the probability of getting that answer right"
>
> — [1:56](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=116s) &middot; *The core mechanic of IRT stated compactly.*

> "item of B equal zero means that is going to be average. Half of the um models in my data set are going to be able to answer that question 50% of the time."
>
> — [4:18](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=258s) &middot; *Explains why the shared scale makes scores interpretable.*

> "Here is going to be on the left side Cloud Opus 4.1, yeah? That has 245 right answers. On the other side we are going to have Gemini 3 Pro, which has 247"
>
> — [6:38](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=398s) &middot; *The concrete numbers behind the talk's headline demonstration.*

> "if you use item response theory, you can see that the difference between all of them is almost one standard deviation. That means Gemini 3 Pro is by far more intelligent."
>
> — [6:38](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=398s) &middot; *The payoff claim: raw accuracy hid a large capability gap.*

> "counting the number of right answers is is not a good approach because I can create benchmarks that are not calibrated and even if I get a lot of right answers, I'm not more intelligent than other models."
>
> — [6:38](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=398s) &middot; *Restates the position with the calibration argument attached.*

> "you can see that we have items that correlates uh the other way around, that better models are actually getting that answer wrong, which makes no sense."
>
> — [9:05](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=545s) &middot; *Defines the negative-discrimination signal used for benchmark auditing.*

> "The gold answer, the answer that is on the benchmark, is 583, which is the total people killed passengers plus crew. But the right answer, if you pay attention, I'm asking only about passengers, which is another number."
>
> — [9:44](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=584s) &middot; *A concrete mislabeled item found by the method.*

> "we're going to get that around 97 items compared with 484. That's almost 5x. We are going to have the same ranking than before or almost the same ranking as before."
>
> — [11:10](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=670s) &middot; *The headline cost-reduction number.*

> "We are like assuming that more questions uh means better estimation, which is not true."
>
> — [11:57](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=717s) &middot; *Directly contradicts a widespread eval intuition.*

> "GPQA, which is a extremely well-designed uh data set, the benchmark here, as you can see, even if you pick at random, you're going to get more or less the same result."
>
> — [12:41](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=761s) &middot; *Important caveat: the compression trick doesn't apply to all benchmarks.*

> "We can actually find out if we are leaking information, if we are overfitting with the benchmark, and other kinds of contaminations."
>
> — [13:25](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=805s) &middot; *Frames residuals as a contamination-detection tool.*

> "if your for whatever reason your inference platform is not actually running the models or the quantization is actually wrong, you're going to observe things like that, behaviors that are not expected"
>
> — [15:42](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=942s) &middot; *An unexpected ops-level use for consistency analysis.*

> "I'm going to pick uh one individual set. I'm going to call that fingerprint set that I'm going to show only to that specific organization."
>
> — [17:00](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1020s) &middot; *The mechanism of the benchmark-leak detection scheme.*

> "So this is not bulletproof, but this is a extremely good technique that you can use to protect your benchmarks."
>
> — [17:45](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1065s) &middot; *Speaker explicitly bounds the strength of his own claim.*

> "we can find out that there are few items that are better for closed weight of models and better for open weights models. I'm not going to show the items because I don't want to leak them on the internet"
>
> — [19:13](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1153s) &middot; *Reports a real differential-item-functioning finding across open vs closed weights.*

> "Also, we can observe that between distillations and its base model, which could be extremely interesting if you want to detect distillation of your model uh without consent."
>
> — [20:39](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1239s) &middot; *The most provocative downstream application: unconsented distillation detection.*

> "I think we can improve a lot how we benchmark LLMs with very basic maths here."
>
> — [21:29](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1289s) &middot; *The closing argument that the barrier is adoption, not sophistication.*

## Positions

- Counting the number of right answers on a benchmark is classical test theory and is an inferior evaluation method compared to item response theory. ([0:02](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=2s), confidence: stated)
- Treating every benchmark question as equally important is an unjustified assumption because items differ in difficulty and quality. ([1:17](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=77s), confidence: stated)
- Claude Opus 4.1 and Gemini 3 Pro differ by only 2 correct answers out of 337 on a real benchmark, yet differ by almost one standard deviation in IRT-estimated ability. ([6:38](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=398s), confidence: stated)
- Benchmarks contain items with negative discrimination, and these reliably indicate mislabeled gold answers or otherwise broken questions. ([9:05](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=545s), confidence: stated)
- Selecting items by highest discrimination can reduce a benchmark from 484 to ~97 items while preserving 99% ranking correlation. ([11:10](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=670s), confidence: stated)
- More benchmark questions does not mean a better ability estimate, because overlapping items add little additional information. ([11:57](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=717s), confidence: stated)
- Benchmark compression gains depend on benchmark quality — GPQA cannot be compressed this way because its items are uniformly discriminative and non-overlapping. ([12:41](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=761s), confidence: stated)
- Anomalous residual patterns can reveal inference-platform problems such as incorrect quantization, not just model capability. ([15:42](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=942s), confidence: stated)
- Per-organization fingerprint sets of hard items can detect benchmark leakage, though the technique is not bulletproof. ([17:45](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1065s), confidence: stated)
- Residual correlation patterns encode model lineage and can be used to detect distillation performed without consent. ([20:39](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1239s), confidence: stated)
- Differential item functioning between open-weight and closed-weight models exists and could be used to infer how labs train their models. ([19:50](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1190s), confidence: implied)
- The mathematics required to substantially improve LLM benchmarking is basic and already available, so the gap is adoption rather than research. ([21:29](https://www.youtube.com/watch?v=O3FEoMYvUf8&t=1289s), confidence: stated)

## Concepts

- [benchmark contamination](../concepts/benchmark-contamination.md)
- [benchmark design](../concepts/benchmark-design.md)

