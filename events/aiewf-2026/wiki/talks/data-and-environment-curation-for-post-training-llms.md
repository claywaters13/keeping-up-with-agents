---
title: "Data and Environment Curation for Post-Training LLMs"
type: "talk"
slug: "data-and-environment-curation-for-post-training-llms"
track: "Data Quality"
org: "Bespoke Labs"
day: "Day 2 — Session Day 1"
room: "Track 9"
video_id: "ewtOo0scUh0"
duration_sec: 1151
word_count: 3085
speakers: ["Mahesh Sathiamoorthy"]
---

# Data and Environment Curation for Post-Training LLMs

*Program title: Data and Environment Curation for Post-training LLMs*

**Speakers:** [Mahesh Sathiamoorthy](../speakers/mahesh-sathiamoorthy.md)

**Org:** Bespoke Labs

**Track:** Data Quality &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 19m 11s

[Watch on YouTube](https://www.youtube.com/watch?v=ewtOo0scUh0)

## Summary

Mahesh Sathiamoorthy, co-founder and CEO of Bespoke Labs, argues that data and RL environments — not compute, models, or training infrastructure — are the binding constraint on post-training LLMs and agents today. He traces the field's shift from evaluating what models know to whether agents can act autonomously for long durations, and identifies reliability as the blocker, with post-training as a powerful lever on it. The bulk of the talk walks through Bespoke's open-source curation recipes: Open Thoughts (reasoning data) and Open Thoughts Agents (agentic trajectories and environments), including counterintuitive ablation findings like sampling many answers per question beating more unique questions, and stronger models not necessarily making better teachers. He closes with a production case study at Intuit's Credit Karma where a tag-based curation recipe fixed hallucinated APR numbers and improved compliance, latency, and throughput, plus a proposed reference stack for building RL environments and post-training agents. Worth watching if you want concrete, ablation-backed curation heuristics rather than theory.

## Key Points

- Data and RL environments are the bottleneck for post-training, since compute, base models, and training infrastructure (Fireworks, Tinker, slime) are all comparatively well-defined and available.
- The field has moved from evaluating what models know (knowledge benchmarks) to whether agents can do things autonomously over long horizons, and the thing blocking that autonomy is reliability.
- Prompting and harness/tool changes can improve agent reliability, but post-training is the mechanism frontier labs primarily rely on for capability gains.
- Open Thoughts established a reasoning-data curation recipe with a demonstrated scaling law: as dataset size grows under the recipe, benchmark metrics keep improving.
- Sampling multiple answers per question (e.g. 16 completions on one question) outperforms collecting many more questions answered once, likely because diversity of reasoning traces helps during fine-tuning.
- Stronger models are not always better teachers — this held in both the reasoning and the agents work, where some Qwen models outperformed larger frontier models as teachers.
- Techniques that intuitively should work often don't: answer filtering, synthetic rewriting, and task augmentation underperformed, while synthetic question generation did work.
- In the Open Thoughts Agents work, SFT contributed most of the gains and RL was compute-intensive and mainly bought the last few percent, so SFT is often sufficient in enterprise settings.
- In the Credit Karma deployment, imbalanced data caused the fine-tuned model to hallucinate numbers like 0% APR; replacing plain-language prompt-response pairs with tagged structure made the model focus on form over specific numbers and gave a large improvement in compliance, latency, and throughput.
- The emerging reference stack has three layers: RL environment building/quality measurement/versioning on top, sandbox and rollout orchestration with checkpointing and rollback below, and SFT/RL/GEPA-style prompt optimization as the training methods.

## Notable Quotes

> "bespoke is an applied data research lab with a mission to help enterprises and frontier labs access high quality data and RL environments for their post training needs"
>
> — [0:12](https://www.youtube.com/watch?v=ewtOo0scUh0&t=12s) &middot; *States the org's thesis and framing for everything that follows.*

> "there are a lot of people who create data uh create RL environments and then there are the uh researchers who consume this. But I feel like there is this slight mismatch and it's kind of beneficial for someone to kind of go do both at the same time."
>
> — [1:25](https://www.youtube.com/watch?v=ewtOo0scUh0&t=85s) &middot; *Names a structural gap between data producers and model researchers.*

> "as you're curating data you want to put yourself in the shoes of the researcher to see what what does it take to you know uh actually move the metrics on the models"
>
> — [2:06](https://www.youtube.com/watch?v=ewtOo0scUh0&t=126s) &middot; *The talk's methodological stance: curation judged by downstream metric movement.*

> "early on we used to think about and evaluate models on what they know"
>
> — [2:06](https://www.youtube.com/watch?v=ewtOo0scUh0&t=126s) &middot; *Sets up the knowing-to-doing framing of the field's evolution.*

> "we have moved on from knowing to doing right so that's the idea of agents"
>
> — [2:42](https://www.youtube.com/watch?v=ewtOo0scUh0&t=162s) &middot; *Compact statement of the benchmark shift.*

> "what is it that's blocking the uh autonomy of agents. It's basically reliability, right?"
>
> — [2:42](https://www.youtube.com/watch?v=ewtOo0scUh0&t=162s) &middot; *The central diagnosis that motivates post-training as the lever.*

> "postraining is a very powerful tool to improve reliability or or maybe even pre-train good models right so if you think of frontier labs this is one of their primary mechanisms of improving agents"
>
> — [3:47](https://www.youtube.com/watch?v=ewtOo0scUh0&t=227s) &middot; *Positions post-training against prompting and harness fixes.*

> "ultimately for post training be it SFT or or uh reinforcement learning data is the bottleneck"
>
> — [3:47](https://www.youtube.com/watch?v=ewtOo0scUh0&t=227s) &middot; *The thesis sentence of the talk.*

> "when I talk about data RLNs are also something I'm calling it as data it's just the data is now in a very different shape"
>
> — [3:47](https://www.youtube.com/watch?v=ewtOo0scUh0&t=227s) &middot; *Explicitly folds RL environments into the category of data.*

> "Most of the places where people struggle especially enterprises is that they don't have access to good quality data and RLNs"
>
> — [5:36](https://www.youtube.com/watch?v=ewtOo0scUh0&t=336s) &middot; *Locates the constraint at enterprises specifically, not just labs.*

> "there are many other benefits of post- training for example you can reduce latency or improve cost throughput"
>
> — [5:36](https://www.youtube.com/watch?v=ewtOo0scUh0&t=336s) &middot; *Non-capability motivations for post-training that the case study later confirms.*

> "we figured out a curation recipe and it shows the scaling law right. So again this is last year when Amy uh and and uh live codebench and these these were some of the popular benchmarks."
>
> — [7:10](https://www.youtube.com/watch?v=ewtOo0scUh0&t=430s) &middot; *The empirical claim underpinning Open Thoughts.*

> "if you keep you know scaling up the data set size the the you know the the it's a scalable recipe right the the metrics also improve"
>
> — [7:50](https://www.youtube.com/watch?v=ewtOo0scUh0&t=470s) &middot; *States the scaling result in the speaker's own terms.*

> "the systematic way of doing this is like you run ablations and figure out which uh you know in each of these stages what works and you kind of proceed to the next"
>
> — [9:38](https://www.youtube.com/watch?v=ewtOo0scUh0&t=578s) &middot; *The methodology behind every finding in the talk.*

> "sampling um multiple answers per question works pretty well. This is something that uh we it's it's kind of counterintuitive."
>
> — [10:29](https://www.youtube.com/watch?v=ewtOo0scUh0&t=629s) &middot; *Headline counterintuitive curation finding.*

> "we could have had more much many more questions and then just answered them exactly once versus taking one question and answering them 16 times"
>
> — [10:29](https://www.youtube.com/watch?v=ewtOo0scUh0&t=629s) &middot; *Names the concrete tradeoff and the sampling ratio involved.*

> "the stronger teachers are not always the best uh uh stronger models are not always the better teachers"
>
> — [11:16](https://www.youtube.com/watch?v=ewtOo0scUh0&t=676s) &middot; *Directly contradicts a common distillation assumption; replicated in the agents work.*

> "synthetic rewriting and task augmentation um is something we thought will work but it didn't very work work very well"
>
> — [12:12](https://www.youtube.com/watch?v=ewtOo0scUh0&t=732s) &middot; *Negative result that saves others wasted effort.*

> "SFT still contributed a lot to the gains um RL was kind of you know it's very comput inensive and for for the last few few percentages it really helped"
>
> — [12:12](https://www.youtube.com/watch?v=ewtOo0scUh0&t=732s) &middot; *Takes a side in the SFT-vs-RL debate with a cost argument.*

> "you have to have a long list of rules to make sure the responses are compliant and that actually blows up the latency"
>
> — [14:28](https://www.youtube.com/watch?v=ewtOo0scUh0&t=868s) &middot; *The concrete failure mode that motivated post-training over prompting at Credit Karma.*

> "the data set can be quite impa imbalance and lot lots and lots of places for example you will have 0% APR and the model after fine-tuning can kind of hallucinate the these uh numbers"
>
> — [14:28](https://www.youtube.com/watch?v=ewtOo0scUh0&t=868s) &middot; *Specific, transferable failure mode of naive fine-tuning data.*

> "we added these uh tags which helped the model to focus on you know uh the the kind of form rather than the specific numbers itself and that gave a big boost"
>
> — [14:28](https://www.youtube.com/watch?v=ewtOo0scUh0&t=868s) &middot; *The actual fix, stated as a reusable curation technique.*

> "you can use LLMs itself to uh to to kind of optimize the prompts based on reflection. Um so that also works pretty well for updating the system prompts and also the harnesses."
>
> — [18:11](https://www.youtube.com/watch?v=ewtOo0scUh0&t=1091s) &middot; *Places prompt optimization alongside SFT and RL in the post-training stack.*

## Positions

- Data and RL environments are the bottleneck for post-training, not compute, models, or training infrastructure. ([3:47](https://www.youtube.com/watch?v=ewtOo0scUh0&t=227s), confidence: stated)
- Reliability is what blocks agents from being autonomous over long durations. ([2:42](https://www.youtube.com/watch?v=ewtOo0scUh0&t=162s), confidence: stated)
- Post-training is a more powerful lever on agent reliability than prompting or harness changes. ([3:47](https://www.youtube.com/watch?v=ewtOo0scUh0&t=227s), confidence: implied)
- RL environments should be treated as a form of data, just in a different shape. ([3:47](https://www.youtube.com/watch?v=ewtOo0scUh0&t=227s), confidence: stated)
- Sampling multiple answers per question (e.g. 16x) beats collecting proportionally more questions answered once. ([10:29](https://www.youtube.com/watch?v=ewtOo0scUh0&t=629s), confidence: stated)
- Stronger models are not always better teachers for distillation. ([11:16](https://www.youtube.com/watch?v=ewtOo0scUh0&t=676s), confidence: stated)
- Some Qwen models outperformed Claude models as teachers in the Open Thoughts Agents work. ([12:12](https://www.youtube.com/watch?v=ewtOo0scUh0&t=732s), confidence: stated)
- Answer filtering, synthetic rewriting, and task augmentation did not work well as curation steps, while synthetic question generation did. ([11:16](https://www.youtube.com/watch?v=ewtOo0scUh0&t=676s), confidence: stated)
- SFT contributed most of the gains in agent post-training; RL is compute-intensive and only worth it for the last few percentage points. ([12:12](https://www.youtube.com/watch?v=ewtOo0scUh0&t=732s), confidence: stated)
- SFT alone is sufficient for many enterprise post-training situations. ([12:12](https://www.youtube.com/watch?v=ewtOo0scUh0&t=732s), confidence: stated)
- Enforcing compliance via a long list of prompt rules blows up latency, making post-training the better path. ([14:28](https://www.youtube.com/watch?v=ewtOo0scUh0&t=868s), confidence: stated)
- Adding structural tags to prompt-response pairs prevents fine-tuned models from hallucinating numbers in imbalanced datasets. ([14:28](https://www.youtube.com/watch?v=ewtOo0scUh0&t=868s), confidence: stated)
- The Credit Karma post-training deployment improved compliance metrics, latency, and throughput simultaneously. ([14:28](https://www.youtube.com/watch?v=ewtOo0scUh0&t=868s), confidence: stated)
- Owning a post-trained model is increasingly attractive because frontier models are getting more expensive. ([14:28](https://www.youtube.com/watch?v=ewtOo0scUh0&t=868s), confidence: stated)
- Open Thoughts demonstrates a scaling law where metrics improve as curated dataset size increases under the recipe. ([7:50](https://www.youtube.com/watch?v=ewtOo0scUh0&t=470s), confidence: stated)
- Long-horizon rollouts require checkpointing plus snapshot/rollback support in the environment infrastructure layer. ([17:37](https://www.youtube.com/watch?v=ewtOo0scUh0&t=1057s), confidence: stated)
- The people creating data/RL environments and the researchers consuming them are mismatched, and doing both is beneficial. ([1:25](https://www.youtube.com/watch?v=ewtOo0scUh0&t=85s), confidence: stated)

## Concepts

- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [scaling laws](../concepts/scaling-laws.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)

