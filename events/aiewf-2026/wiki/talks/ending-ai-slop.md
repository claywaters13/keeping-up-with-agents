---
title: "Ending AI Slop"
type: "talk"
slug: "ending-ai-slop"
track: "Data Quality"
org: "Taste Labs"
day: "Day 2 — Session Day 1"
room: "Track 9"
video_id: "lCBf9slCanI"
duration_sec: 990
word_count: 3372
speakers: ["Thais Castello Branco"]
---

# Ending AI Slop

**Speakers:** [Thais Castello Branco](../speakers/thais-castello-branco.md)

**Org:** Taste Labs

**Track:** Data Quality &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 16m 30s

[Watch on YouTube](https://www.youtube.com/watch?v=lCBf9slCanI)

## Summary

Thais Castello Branco, founder of Taste Labs, argues that AI feels like "slop" for structural reasons, not incidental ones: models are strong at code and math because those domains are verifiable and decomposable, and weak at design, writing, and taste because those domains resist measurement. Her core claim is that capability follows measurability, so the work is to pull fuzzy capabilities toward verification — e.g. decomposing "is this on brand?" into codified color, typography, motion, and spacing checks that can become an RL environment's ground truth. The second half diagnoses mode collapse: models predict the most likely output, but in subjective domains greatness lives at the tails of the distribution, and naively pooled preference data averages distinct tastes into noise. She proposes a routing framework — push what you can toward programmatic verification, route the genuinely contextual and preference-dependent parts to high-quality human judgment — plus concrete data-quality levers like forced expert distribution, specificity checks, and tying expert commentary to specific code components. Worth watching if you work on evals, RL environments, or preference data for creative and design tasks; it's a compact, opinionated framework rather than a results talk.

## Key Points

- Code's tractability for AI is a property of code, not of models — it decomposes, verifies, and executes — so subjective domains are hard for structural reasons rather than because of insufficient training effort.
- Capability follows measurability: solving even part of the measurement problem for a subjective domain unlocks a large share of the capability.
- Subjective quality is contextual (the same slide is great for a startup and wrong for a finance firm) and non-stationary (what is good today differs from five years ago), unlike math or code.
- "Make something great" is untrainable, but "make something on brand" is tractable, because a brand has already been decomposed by designers into colors, typography, spacing, motion, and texture that can be verified against.
- In an RL environment for brand adherence, the decomposition — not the original artifact — should be the ground truth, so that genuinely novel-but-valid outputs are not penalized for failing to replicate the source.
- Slop is mode collapse: models emit the most likely output, but in writing and design the optimal output is often at the tails of the distribution, produced by intentionally breaking patterns.
- Traditional preference data collapses to the mean because it pools raters without modeling who they are; the world is multi-preference and preferences should be attached to a per-person preference vector rather than averaged.
- Expert disagreement in human QA is diagnostic, not uniformly bad: disagreement on alignment signals flawed data, while disagreement on style or aesthetics is real signal about preference pluralism.
- Practical data-quality levers the team can fully control include forced expert distribution, specificity of expert reasoning, and tying an expert's commentary to the exact code component it refers to, since models struggle to connect code to visuals.
- For subjective domains, a small amount of expensive, high-taste data beats large volumes of noisy data.

## Notable Quotes

> "our whole mission is basically how do we end AI slop? And we believe that to really solve this problem, we have to first decompose and understand subjective domains."
>
> — [0:13](https://www.youtube.com/watch?v=lCBf9slCanI&t=13s) &middot; *States the thesis and the method in one line.*

> "we treat for example the fact that code is verifiable and measurable as something that is a property about models and models are great at at coding um because we've made them great at coding but realistically it's actually a fact about code."
>
> — [1:57](https://www.youtube.com/watch?v=lCBf9slCanI&t=117s) &middot; *The talk's central reframing — the bottleneck is the domain, not the model.*

> "Code is something that decomposes, it verifies, it executes and so it makes it a lot easier for us to be able to train on these domains"
>
> — [2:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=163s) &middot; *Names the three properties that make a domain trainable.*

> "One is that capability follows measurability. So if we can solve the measurability problem or at least part of it, then we can solve a big portion of these domains."
>
> — [2:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=163s) &middot; *The slogan the rest of the talk builds on.*

> "The same slide could be amazing. for example, if you are a startup and completely inappropriate if you are a finance firm."
>
> — [3:21](https://www.youtube.com/watch?v=lCBf9slCanI&t=201s) &middot; *Concrete illustration that subjective quality is context-relative, defeating a single global judge.*

> "What is considered good today is different than five years ago and different than five years from now. In code that's not necessarily true or in math, right? That's something that is way more consistent over time."
>
> — [4:05](https://www.youtube.com/watch?v=lCBf9slCanI&t=245s) &middot; *Identifies non-stationarity as a distinct hazard for benchmarks in subjective domains.*

> "But suddenly if I'm like okay make something that is on brand that is a much easier problem to define and a brand is something that can become decomposable."
>
> — [5:07](https://www.youtube.com/watch?v=lCBf9slCanI&t=307s) &middot; *The key move: swap an unspecifiable objective for a decomposable proxy.*

> "Verifying in general if something's on brand and you can try this uh by prompting an LLM as a judge to do it is quite hard. But once you start picking apart the exact elements that represent what great is, then it suddenly becomes the shape of something that is codifiable and verifiable."
>
> — [5:07](https://www.youtube.com/watch?v=lCBf9slCanI&t=307s) &middot; *Direct claim that decomposition beats holistic LLM judging.*

> "LLM LLM as a judge might not necessarily always be the best method. We know that there's a lot of reward hacking."
>
> — [5:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=344s) &middot; *Takes a side against the default eval tool for subjective domains.*

> "So in this case the task design itself is really kind of the hardest part of the problem of how do you turn something that appears very fuzzy into something that actually can be arled."
>
> — [5:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=344s) &middot; *Locates the difficulty in environment/task design rather than training method.*

> "you would want that output to not only be graded versus the original but to be graded on this ground truth"
>
> — [6:21](https://www.youtube.com/watch?v=lCBf9slCanI&t=381s) &middot; *A specific, actionable design rule for RL environments in creative domains.*

> "they're basically predicting what's the most likely outcome to show up next. And they assume that that outcome is the ideal outcome."
>
> — [7:30](https://www.youtube.com/watch?v=lCBf9slCanI&t=450s) &middot; *Compact statement of the mechanism behind slop.*

> "a lot of greatness and creativity happens actually at the ends of the distribution. It's not the most likely outcome. It's when you actually actively break from rules and actively break from patterns that you can create things that are subjective and and great."
>
> — [8:03](https://www.youtube.com/watch?v=lCBf9slCanI&t=483s) &middot; *The tails-not-mean argument, which cuts against standard likelihood-maximizing objectives.*

> "the reason why this feels like slop and that we have this feeling that we're surrounded by by slop is exactly because of this collapse to the mean and this repetition."
>
> — [8:03](https://www.youtube.com/watch?v=lCBf9slCanI&t=483s) &middot; *Defines slop causally rather than aesthetically.*

> "we work, for example, with a community of designers, um, over like a thousand experts that are experts in different types of medium, different styles, and we purposely want to force that distribution when we're breaking down the problem."
>
> — [8:36](https://www.youtube.com/watch?v=lCBf9slCanI&t=516s) &middot; *Only concrete scale number in the talk, plus the anti-collapse tactic.*

> "we believe human judgment is still at a much higher level than any LLM as a judge"
>
> — [9:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=584s) &middot; *Explicit, contestable position on human vs. model judging.*

> "And that doesn't mean either of those things are wrong or it doesn't mean that the best answer is the average of what two people might like."
>
> — [10:45](https://www.youtube.com/watch?v=lCBf9slCanI&t=645s) &middot; *The core objection to conventional pooled preference data.*

> "It means that we need to fundamentally understand that the world is multi-preference and how do we do that matching accordingly."
>
> — [11:15](https://www.youtube.com/watch?v=lCBf9slCanI&t=675s) &middot; *Names the pluralism position that drives their preference-vector approach.*

> "we know that models have a tricky time kind of actually connecting the piece of the code to the visual. And so if you can find for example a method to tie that exact code component to the commentary of the expert, suddenly you have data that is way less noisy and way more clear."
>
> — [13:28](https://www.youtube.com/watch?v=lCBf9slCanI&t=808s) &middot; *A specific annotation technique with a stated mechanism.*

> "if they're disagreeing on things like sty style or um aesthetics that is not necessarily bad data that's actually good data. It shows you that there is a distinction for what people like."
>
> — [14:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=883s) &middot; *Inverts the usual treatment of low inter-annotator agreement.*

> "when it comes to subjective domains I would advocate for a quality over quantity approach. I think creating high quality data is expensive. It's difficult."
>
> — [15:28](https://www.youtube.com/watch?v=lCBf9slCanI&t=928s) &middot; *The closing recommendation, stated as a tradeoff.*

## Positions

- Models' strength at coding is a property of code (decomposable, verifiable, executable), not primarily a property of the models. ([1:57](https://www.youtube.com/watch?v=lCBf9slCanI&t=117s), confidence: stated)
- Capability follows measurability — solving the measurement problem for a subjective domain is most of solving the domain. ([2:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=163s), confidence: stated)
- Standards of quality in design change over time, unlike in code or math, so subjective benchmarks decay. ([4:05](https://www.youtube.com/watch?v=lCBf9slCanI&t=245s), confidence: stated)
- Prompting an LLM as a judge to assess holistic brand adherence works poorly; decomposing the brand into codified elements is the better approach. ([5:07](https://www.youtube.com/watch?v=lCBf9slCanI&t=307s), confidence: stated)
- Task design, not the choice of training algorithm, is the hardest part of turning a fuzzy capability into an RL environment. ([5:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=344s), confidence: stated)
- Outputs should be graded against the decomposed ground truth rather than against the original artifact, so novel-but-valid solutions aren't penalized. ([6:21](https://www.youtube.com/watch?v=lCBf9slCanI&t=381s), confidence: stated)
- In creative and design domains, the most likely output is not the optimal one; quality lives at the tails of the distribution. ([8:03](https://www.youtube.com/watch?v=lCBf9slCanI&t=483s), confidence: stated)
- AI slop is caused by collapse to the mean and repetition, not by lack of raw model capability. ([8:03](https://www.youtube.com/watch?v=lCBf9slCanI&t=483s), confidence: stated)
- Problems that are contextual, time-dependent, or preference-dependent should be routed to human judgment and data methods rather than to programmatic RL environments. ([9:11](https://www.youtube.com/watch?v=lCBf9slCanI&t=551s), confidence: stated)
- Human judgment is currently substantially better than any LLM-as-a-judge for subjective domains. ([9:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=584s), confidence: stated)
- Averaging preference data across unmodeled raters produces noise; preferences should be attached to per-rater preference vectors to preserve pluralism. ([11:15](https://www.youtube.com/watch?v=lCBf9slCanI&t=675s), confidence: stated)
- Expert disagreement on objective attributes like alignment indicates bad data, while disagreement on style or aesthetics indicates valuable signal. ([14:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=883s), confidence: stated)
- Specificity of an expert's language is a measurable proxy for the value of a data point. ([12:53](https://www.youtube.com/watch?v=lCBf9slCanI&t=773s), confidence: stated)
- Models struggle to connect a visual element to the code that produces it, so linking expert commentary to specific code components materially reduces data noise. ([13:28](https://www.youtube.com/watch?v=lCBf9slCanI&t=808s), confidence: stated)
- In subjective domains, a smaller volume of expensive high-taste data yields far better results than large volumes of noisy data. ([15:28](https://www.youtube.com/watch?v=lCBf9slCanI&t=928s), confidence: stated)
- Labs rarely provide the feedback loop showing which data caused which capability change, so vendors should optimize the data-quality factors they can measure themselves. ([14:43](https://www.youtube.com/watch?v=lCBf9slCanI&t=883s), confidence: stated)

## Concepts

- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [rlhf and preference training](../concepts/rlhf-and-preference-training.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)

