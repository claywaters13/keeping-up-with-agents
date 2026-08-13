---
title: "Adaption Labs: Gradient-Free Continual Learning"
type: "talk"
slug: "adaption-labs-gradient-free-continual-learning"
track: "Memory & Continual Learning"
org: "Adaption"
day: "Day 3 — Session Day 2"
room: "Track 3"
video_id: "XEd_SRVHBgU"
duration_sec: 1250
word_count: 3814
speakers: ["Sara Hooker"]
---

# Adaption Labs: Gradient-Free Continual Learning

*Program title: Adaption Labs — Gradient-Free Continual Learning*

**Speakers:** [Sara Hooker](../speakers/sara-hooker.md)

**Org:** Adaption

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 20m 50s

[Watch on YouTube](https://www.youtube.com/watch?v=XEd_SRVHBgU)

## Summary

Sara Hooker argues that the narrow, credential-gated path to doing frontier AI research — right PhD, right lab, right moment, plus thousands of co-located GPUs — is breaking down, and that this is the most interesting thing happening in AI right now. She presents two reasons: Auto Scientist, her team's system that automates the full model-training loop (data, hyperparameters, alignment) and reportedly beats human research staff by exploiting a search space humans are too cautious to explore, and the empirical claim that pre-training scale is no longer the most lucrative axis of return, shifting the action to post-training, agentic, and inference compute that doesn't require hoarding GPUs. Her key methodological point is that automated training search only paid off once data was co-optimized alongside the model, not treated as an agent-selected side input. Roughly half the runtime is unscripted Q&A covering open-source safety tradeoffs, whether small models still depend on large ones for distillation, and where the parametric/non-parametric storage boundary should sit. Worth watching if you care about who can realistically train frontier models in 2026, or want a working researcher's case that the scaling-by-size era has hit an architectural ceiling.

## Key Points

- The professionalization of AI research created what Hooker calls an "unreasonably narrow path" — right PhD program, right industry lab, right problem at the right time — that aggressively filtered who could contribute to the frontier, and compute requirements compounded that filter.
- Auto Scientist automates the training of models end to end, co-optimizing data through alignment and self-evolving its approach based on domain and data type, and it outperformed the team's own research staff across architectures, model sizes, and dense versus mixture-of-experts setups.
- The system only produced real returns once data quality was co-optimized with the model rather than left as a choice the agent could make; Hooker treats controlling the entire flow as the load-bearing design decision.
- Automated search changes hyperparameters humans are wary of changing all at once, yielding heavy exploitation of the search space, more predictable training, and therefore less compute wasted on customization.
- Hooker claims pre-training size is no longer the most lucrative axis of scale because architectures are saturated — evidenced by small sub-13B models climbing past larger ones on the Open LLM Leaderboard, and by recent large models failing to deliver stepwise gains.
- Because pre-training compute must be co-located and over-provisioned for redundancy while post-training, agentic, and inference compute can be distributed, the shift in where returns live directly changes who can build frontier AI.
- Fewer than about 5,000 people worldwide know how to train frontier models at scale, and Hooker frames that apprentice-passed tacit knowledge as an exploitable search space — automating it lowers the cost of asking research questions, which changes which questions get asked at all.
- On safety, Hooker refuses the binary: wider access carries real risk, but the risk argument also restrains who can participate, and Auto Scientist is framed as customization and ownership of intelligence rather than an open-source release question.
- In Q&A she concedes frontier models remain large and distillation from big models still helps — her narrower claim is that no lab will supersize again for this architecture, so innovation must happen within the current ceiling.

## Notable Quotes

> "most people intuitively understand that you shouldn't ship the same model to billions of people. And they also understand that it's not a particularly good use of compute, right? You're spending the same amount of compute on everything. And some problems are hard and some are very easy."
>
> — [4:02](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=242s) &middot; *the compute-allocation case against one-model-for-everyone, stated plainly*

> "And we are ripe for a revolution in who gets to participate at the frontier of AI."
>
> — [4:02](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=242s) &middot; *the talk's thesis in one line*

> "Frankly, we did not get the returns for like how much you can squeeze out of performance until you control for data quality."
>
> — [5:59](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=359s) &middot; *the central negative result behind co-optimizing data with the model*

> "it actually outperforms research staff. And mainly because like a lot of our research staff has experience with certain model types, and we're testing it across many different model architectures"
>
> — [5:14](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=314s) &middot; *the headline claim plus the mechanism she credits for it*

> "You'll notice all these percentages for win rates are like 60 plus."
>
> — [6:35](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=395s) &middot; *sets up her admission that the 60% figure was an artifact of a budget stopping rule*

> "it changes a lot of the hyperparameters. Typically, that humans are much more wary about changing all at once. And so, you get massive exploitation of the search space."
>
> — [7:08](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=428s) &middot; *names the specific advantage automated search has over human researchers*

> "But these are like domains where typically current models fall short."
>
> — [7:40](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=460s) &middot; *explains why medical, legal, science, and code drove beta demand*

> "Like we decided okay, we're going to cover languages from day one, 242 languages. And also like a big interest for us is actually non-verifiable tasks."
>
> — [8:55](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=535s) &middot; *concrete scope commitment, and a bet against verifiable-reward-only training*

> "pre-training size in particular is not your most lucrative axis of scale."
>
> — [10:38](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=638s) &middot; *the load-bearing empirical claim of the second half*

> "Like if pre-training scale isn't going to dominate performance, it actually really greatly changes who can create the best recipes for innovation, because pre-training compute typically has to be co-located."
>
> — [10:38](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=638s) &middot; *links the scaling claim to the access claim via infrastructure geography*

> "we know it's not giving the same returns largely because our architecture is saturated."
>
> — [11:22](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=682s) &middot; *attributes the slowdown to architecture rather than data or compute limits*

> "a lot of that is because where the most returns for performance are now are on a broader action space."
>
> — [12:05](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=725s) &middot; *her account of where optimization has migrated*

> "One is there's very few people who know how to train frontier models. I would say realistically probably less than 5,000 in the world at scale."
>
> — [13:58](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=838s) &middot; *a hard number on the size of the frontier-training talent pool*

> "the cost of asking something informs what is asked. And if you make it cheaper to ask something, you change like the volume of things that are asked"
>
> — [13:58](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=838s) &middot; *the economic argument for why automation broadens the research agenda*

> "agentic compute, post-training compute matters a significant amount for performance. That does not require the same type of"
>
> — [14:43](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=883s) &middot; *the compute-dynamics half of her democratization argument*

> "it means that the person with the best idea has a higher chance of winning."
>
> — [14:43](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=883s) &middot; *the payoff she claims from shifting compute away from pre-training*

> "So when you make a tool more readily available, there's a profile of risk associated with it."
>
> — [15:18](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=918s) &middot; *concedes open-access risk rather than dismissing it*

> "And I think you have to acknowledge risk by also navigating that and acknowledging that it limits who can participate."
>
> — [16:40](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1000s) &middot; *her stated middle position on the safety-versus-access binary*

> "it will only work to do like an AutoScientist for harnesses if you also co-optimize it with a model."
>
> — [16:40](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1000s) &middot; *extends the co-optimization principle to agent harnesses*

> "the architecture determines your ceiling, and I'm saying we are probably at the ceiling of size"
>
> — [18:39](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1119s) &middot; *the most precise formulation of her scaling position*

> "what you will see in pre-training is instead of the size people are just moving post-training further back, which is very fascinating and a bigger lever."
>
> — [19:19](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1159s) &middot; *a concrete prediction about how labs are reallocating the training pipeline*

## Positions

- Pre-training size is no longer the most lucrative axis of scale, and current architectures are at or near their size ceiling. ([10:38](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=638s), confidence: stated)
- No frontier AI lab will supersize its model again for pre-training under the current architecture; a new architecture would change that. ([18:39](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1119s), confidence: stated)
- Automated training search only yields significant performance returns if data quality is co-optimized with the model rather than left to agent discretion. ([5:59](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=359s), confidence: stated)
- Auto Scientist outperforms the team's own human research staff across model architectures, sizes, and dense/MoE variants. ([5:14](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=314s), confidence: stated)
- Fewer than roughly 5,000 people in the world know how to train frontier models at scale, and that tacit knowledge is an exploitable search space. ([13:58](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=838s), confidence: stated)
- Shipping the same model to billions of people is both a poor fit for users and an inefficient allocation of compute. ([4:02](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=242s), confidence: stated)
- Agentic and post-training compute do not require hoarding co-located GPUs, so they favor distributed actors with better ideas over incumbents with more hardware. ([14:43](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=883s), confidence: stated)
- Open access to models carries genuine risk, but safety-based restriction also limits who can participate, and binary views on both sides miss the tradeoff. ([16:40](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1000s), confidence: stated)
- Distillation from larger models is genuinely helpful, but spending much more pre-training compute to serve the long tail of the distribution is of unclear benefit. ([19:19](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=1159s), confidence: stated)
- Non-verifiable tasks, not verifiable ones, are where the bulk of everyday value and the next year of progress lie. ([8:55](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=535s), confidence: stated)
- Test-time compute should be adaptive to the task rather than uniform. ([8:18](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=498s), confidence: implied)
- Small models under 13B have overtaken larger models on the Open LLM Leaderboard, with the ratio flipping over time. ([11:22](https://www.youtube.com/watch?v=XEd_SRVHBgU&t=682s), confidence: stated)

## Concepts

- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [benchmark saturation](../concepts/benchmark-saturation.md)
- [continual learning](../concepts/continual-learning.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [post-training](../concepts/post-training.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [scaling laws](../concepts/scaling-laws.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)

