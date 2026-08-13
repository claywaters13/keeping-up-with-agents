---
title: "rlhf and preference training"
type: "concept"
slug: "rlhf-and-preference-training"
tier: "supporting"
maturity: "contested"
talk_count: 7
speaker_count: 8
---

# rlhf and preference training

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **7** talk(s) by **8** speaker(s)

**Definition:** Training on human preference signals — pairwise comparisons, reward models, and the asymmetries they introduce.

*Also referred to as: reinforcement learning from human feedback, rlhf, preference data collection, pairwise preference training, user preference modeling, process reward models, reward model asymmetry, fine-tuning to human distributions*

## State of Practice

Nobody at this conference disputes that preference optimization is what turned base models into products — one speaker puts deployed-LLM coverage at roughly 100% RLHF, and another credits RLHF with a 1B model beating 175B — but the attention has moved entirely to the asymmetries it introduces. The shared diagnosis is that a reward model fit to aggregated human comparisons drops modes: output collapses toward the mean of raters, confident-looking wrong answers score well by construction, and judges grade surface plausibility rather than the axis you meant to measure (9.2 on camera work for a video where the camera never moved; 'physics look great' on hovering ghosts). The remedies converge on decomposition and relative elicitation — break a subjective target into named, codified sub-axes and score each one; train judges on A-vs-B pairs rather than 1–10 scales because humans agree on comparisons and not on absolute scales; keep rater identity attached to the label instead of averaging across unmodeled raters; and set the ceiling empirically by splitting human ground truth in half and correlating human against human (~80% self-consistency). Where the field splits is on the objective itself: one camp is building richer preference-and-RL environments so subjective domains become trainable, another argues preference is structurally the wrong target and the next post-training paradigm is calibrated decision-making, and enterprise practitioners report that per-user preference conflict is simply unsolved — neither semantic layers nor agent memory routes a request to the right team's metric definition. The practical center of gravity is that task and data design, not model scale or algorithm choice, is where the remaining leverage lives.

## Consensus

### Preference optimization collapses outputs toward the mean of the rater distribution; the resulting sameness ('slop', muddled variation, mode dropping) is a property of the training objective, not a capability gap that a bigger model fixes.

Support: **3** talk(s)

> "the reason why this feels like slop and that we have this feeling that we're surrounded by by slop is exactly because of this collapse to the mean and this repetition."
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [8:03](https://www.youtube.com/watch?v=lCBf9slCanI&t=483s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)

### Holistic reward signals get gamed: a judge asked for an overall verdict scores surface gloss instead of the intended property, so quality must be decomposed into named axes and each scored explicitly.

Support: **4** talk(s)

> "The reason it was wrong is because how we generated that data, right? It It um it scored the vibe as opposed to the the the axes."
>
> — [Evaling Video Slop](../talks/evaling-video-slop.md), [11:14](https://www.youtube.com/watch?v=b_PmGocP4rc&t=674s)

Supporting talks: [Evaling Video Slop](../talks/evaling-video-slop.md), [Ending AI Slop](../talks/ending-ai-slop.md), [From RL to IRL](../talks/from-rl-to-irl.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

### Preference is genuinely plural — two raters or two teams can hold incompatible, equally valid preferences — so averaging labels across unmodeled raters destroys signal; preference must be attached to a rater, team, or group identity.

Support: **3** talk(s)

> "while both of these are correct metrics or the correct way to calculate the metric. They both will give you very different answers and it's just about preference."
>
> — [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [9:33](https://www.youtube.com/watch?v=B8l81jhvHbI&t=573s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)

### The binding constraint on preference training is task, environment, and data design — not model scale, context length, or the choice of RL algorithm.

Support: **5** talk(s)

> "I actually think that the full stack is that data matters more than compute and doing the right task matters way more than data."
>
> — [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [15:17](https://www.youtube.com/watch?v=cJ0EOzey--o&t=917s)

Supporting talks: [What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [Ending AI Slop](../talks/ending-ai-slop.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [From RL to IRL](../talks/from-rl-to-irl.md)

### Human judgment remains the calibration anchor for subjective quality: LLM-as-judge cannot be trusted standalone, and human labeling has to be a continuous, resampled process rather than a one-time pass.

Support: **3** talk(s)

> "we believe human judgment is still at a much higher level than any LLM as a judge"
>
> — [Ending AI Slop](../talks/ending-ai-slop.md), [9:44](https://www.youtube.com/watch?v=lCBf9slCanI&t=584s)

Supporting talks: [Ending AI Slop](../talks/ending-ai-slop.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)

## Disagreements

### Is preference optimization the substrate to keep building on, or a detour whose objective must be replaced?

| Position A | Position B |
|---|---|
| RLHF/RL post-training is the decisive ingredient that made models useful, and the path forward is scaling it into harder settings — realistic computer-use sandboxes, long-horizon value-model RL, compaction trained with RL, subjective domains turned into RL environments.<br>*[Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Ending AI Slop](../talks/ending-ai-slop.md)* | Optimizing for human preference structurally produces overconfidence and hallucination via reward-model asymmetry, so it is unfixable from inside; the next paradigm is neither RLHF nor RLVR but optimization for calibrated decision-making, with a different API shape.<br>*[What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: It decides whether the money goes into better environments, reward decomposition, and RL infrastructure, or into a different training objective entirely — and whether today's preference-trained models can ever be trusted for unattended, stakes-bearing automation.*

### Can subjective quality be decomposed into something verifiable enough to train against, or does the field's push toward verifiability define away the tasks that matter?

| Position A | Position B |
|---|---|
| Capability follows measurability: decompose the fuzzy target (brand into codified elements; video into narrative, pacing, physics, character consistency; computer tasks into code) until it becomes gradeable, and most of the domain is solved.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [From RL to IRL](../talks/from-rl-to-irl.md)* | The industry is already over-indexed on procedural, one-or-two-valid-answer tasks; the real gap is open-ended work under uncertainty with multiple players and differing goals, which current benchmarks and decomposition do not capture — all frontier models lost money on a one-year real-world betting benchmark.<br>*[Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: If decomposition works, preference data is an engineering problem and taste vendors win; if not, the field is optimizing a proxy that gets more polished while the economically valuable open-ended tasks stay untouched.*

### At scale, should the preference judge be a distilled model in the generation loop, or expensive human experts on a small high-taste dataset?

| Position A | Position B |
|---|---|
| Distill the committee of frontier judges into one small fast VLM (~3s per 15-second video), accept that the bigger model is more accurate but too slow to be worth it, and put eval inside the generation loop; the model already contains the latent preferences, you just have to elicit them.<br>*[Evaling Video Slop](../talks/evaling-video-slop.md), [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)* | In subjective domains a small volume of expensive expert data beats large volumes of noisy data, human judgment substantially outperforms any LLM judge, and contextual/time-dependent/preference-dependent problems should be routed to humans rather than into a programmatic reward — preference remains an open research problem no lab has solved.<br>*[Ending AI Slop](../talks/ending-ai-slop.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)* |

*Why it matters: This is a direct budget fork: train and serve a judge model, or fund a standing panel of domain experts. The video team's own answer is unit economics — below thousands of items per day the expensive human/committee path is the correct one.*

## Practical Guidance

**Do:**

- Train preference judges on A-vs-B pairs rather than absolute 1–10 scores, because raters agree on comparisons and do not agree on absolute scales
- Score the specific axes you care about (narrative, pacing, physics, character consistency; codified brand elements) instead of asking a judge for a holistic verdict and expecting the axes to emerge
- Grade outputs against the decomposed ground truth rather than against the original reference artifact, so novel-but-valid solutions are not penalized
- Keep rater identity attached to each label as a per-rater preference vector instead of averaging across unmodeled raters
- Tie expert commentary to the specific code component or element that produced the visual, since models struggle to connect a rendered element to its source
- Estimate the accuracy ceiling empirically: split human ground truth in half, treat one half as 'synthetic', correlate, and repeat thousands of times — human self-consistency was measured at ~80%
- Evaluate with both a correlation metric and a distribution-shape metric, because a model can match the average while flattening the variance
- Elicit free-text responses and map them to a scale via semantic similarity to human-written anchors instead of prompting for a naive 1–5 rating
- Distill the judge committee into a small fast model and run it inside the generation loop — but only once volume reaches thousands to tens of thousands of items per day
- Log correction events (when a user overrides or fixes an agent answer) and feed them back into the agent's context as a standing feedback loop
- Treat rater disagreement diagnostically: disagreement on objective attributes means bad data, disagreement on style or aesthetics is the signal you are trying to capture
- Penalize dangerous intermediate actions, not just wrong outcomes — a trajectory can reach 'done' having done something unintended
- Reward handing control back to the user when confidence about risk, reversibility, or authorization is low, rather than treating full autonomy as the objective
- Surface infrastructure errors to the model so recovery becomes a native learned action, instead of resetting the environment
- Keep RL tasks inside a difficulty window — too easy or too hard produces almost no training signal

**Avoid:**

- Averaging preference labels across raters whose identities you have not modeled — opposing valid preferences wash out to 50/50 noise
- Building pairs where human-made is labeled good and AI-made is labeled bad; without matched encoding and annotation you train an AI detector, not a quality detector
- Prompting an LLM as a judge for a holistic property like 'is this on brand' — it reward-hacks; codify the constituent elements first
- Reaching for a bigger model, a longer context window, or more knowledge bases when the actual failure is unresolved preference and unranked sources of truth
- Running more synthetic samples on unchanged inputs to boost statistical significance — it sharpens your estimate of the model, not the accuracy of the forecast
- Piling on demographic detail assuming richer conditioning is closer to reality; past a point it amplifies model bias and moves results further from the humans
- Relying on hand-maintained .md files, skills, or agent memory to hold preference — memory stores the preference but cannot tell which definition applies when
- Giving agents tools that can search prior trajectories or archives, which teaches retrieval of previous answers in place of reasoning
- Using preference-trained models for decisions with stakes to the business where the human has been removed from the loop — the overconfidence is by design
- Treating human annotation as a one-time labeling pass rather than a recurring session that recalibrates the judges

## Notable Outliers

- Hallucination is not a bug to be patched but an intrinsic consequence of optimizing human preference — a mode-dropping asymmetry in the reward model directly analogous to GANs, which is why wrong models still look right. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [14:35](https://www.youtube.com/watch?v=cJ0EOzey--o&t=875s))
- There is a hard ceiling on preference prediction set by human self-inconsistency: one study found humans were only about 80% consistent with themselves. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [17:03](https://www.youtube.com/watch?v=YnNF55QV0zs&t=1023s))
- Adding more demographic detail to a persona construction amplified the model's bias and pushed results further from real human data, inverting the usual 'more grounding is better' intuition. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [11:17](https://www.youtube.com/watch?v=YnNF55QV0zs&t=677s))
- Constructing preference pairs as human-generated=good versus AI-generated=bad overfits the judge into an AI detector rather than a quality detector. ([Evaling Video Slop](../talks/evaling-video-slop.md), [11:58](https://www.youtube.com/watch?v=b_PmGocP4rc&t=718s))
- For long-horizon RL, value models beat GRPO despite the added complexity and bias — they cut gradient variance, work at trajectory level with compaction, and permit bootstrapping; off-policy staleness up to about eight steps is tolerable. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [11:31](https://www.youtube.com/watch?v=2bvtay8wGYI&t=691s))

## All Talks

- [Ending AI Slop](../talks/ending-ai-slop.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [From RL to IRL](../talks/from-rl-to-irl.md)
- [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)
- [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

## Speakers

- [Chengxi Taylor](../speakers/chengxi-taylor.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Gaurav Mishra](../speakers/gaurav-mishra.md)
- [Ishan Anand](../speakers/ishan-anand.md)
- [Ishita Daga](../speakers/ishita-daga.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Ross Taylor](../speakers/ross-taylor.md)
- [Thais Castello Branco](../speakers/thais-castello-branco.md)

