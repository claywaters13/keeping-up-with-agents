---
title: "The Base Model Is Dead"
type: "talk"
slug: "the-base-model-is-dead"
track: "Data Quality"
org: "Arcee AI"
day: "Day 2 — Session Day 1"
room: "Track 9"
video_id: "xbPriQWXtWM"
duration_sec: 1064
word_count: 2491
speakers: ["Varun Singh"]
---

# The Base Model Is Dead

*Program title: The Base Model is Dead*

**Speakers:** [Varun Singh](../speakers/varun-singh.md)

**Org:** Arcee AI

**Track:** Data Quality &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 17m 44s

[Watch on YouTube](https://www.youtube.com/watch?v=xbPriQWXtWM)

## Summary

Varun Singh, pre-training lead at Arcee AI, argues that the classic notion of a base model — a compressed reflection of the human internet built from web text — is obsolete. Where GPT-3 drew roughly 85% of its training mix from web text, modern recipes like MAI Thinking 1 push it down to ~15%, replacing it with code, STEM, and (in NeMoTron 3 Ultra's case) large volumes of synthetic and SFT-style data pulled backward into pre-training. He frames the whole pipeline as just two paradigms — supervised next-token prediction and RL — and contends that supervised learning's job is now to install the atomic skills RL will later compose, not to be the endpoint. The talk surveys a live disagreement in the field (NeMoTron leaning hard into synthetic data, MAI refusing it entirely) and touches on practical consequences like MoE load-balancing instability when pre-training and post-training distributions diverge. Worth watching if you care about how frontier pre-training data recipes are actually shifting and why.

## Key Points

- Web text has collapsed as a share of pre-training data: it was ~85% of GPT-3's mix and ~50% of Llama 3's general-knowledge tokens, but only ~15% in MAI Thinking 1, displaced largely by code and STEM data.
- The field is split on synthetic data: NeMoTron 3 Ultra leans heavily into it while MAI Thinking 1 explicitly refuses any synthetic or model-generated data and even filters its web scrapes for it.
- Labs are pulling post-training-shaped data (SFT question-answer sets, agentic traces, long-context data) backward into pre-training so the model learns downstream task shapes from the very beginning.
- Synthetic rephrasing — generating multiple restatements of the same seed information — was used at web scale in Arcee's Trinity model and in Kimi K2, countering the assumption that synthetic data necessarily causes model collapse.
- For MoE models, a large distribution gap between pre-training and post-training data creates severe expert load-imbalance; MAI had to crank up its load-balancing coefficient during SFT, which the speaker considers a symptom of a fixable data problem.
- The speaker proposes discarding the pre-training / mid-training / post-training / RL taxonomy in favor of two paradigms: supervised learning via next-token prediction, and RL.
- Compute allocation has shifted dramatically — Xiaomi's MiMo reports roughly equal pre- and post-training compute, and Composer 2.5 spent far more on RL than on supervised learning.
- Base models should be understood as priors for whatever interaction paradigm comes next — currently reasoning and agentic behavior — rather than as compressed archives of human knowledge.

## Notable Quotes

> "the idea of the base model that we have um kind of is like built on uh this idea of like training on super large-scale web text and the base model kind of being a reflection of like the whole knowledge of like the uh human internet"
>
> — [0:12](https://www.youtube.com/watch?v=xbPriQWXtWM&t=12s) &middot; *states the premise the entire talk sets out to dismantle*

> "RL was mostly just a cherry on top, um shaping the, you know, flavor of the interactions more than conferring extra um knowledge or quality onto the base model itself."
>
> — [3:09](https://www.youtube.com/watch?v=xbPriQWXtWM&t=189s) &middot; *crisp characterization of the old regime that RL has since escaped*

> "pre-training um and the base model kind of defined how good you were able to get a model. Um it was like the bulk of the compute uh budget and it was um, the the like core of the training process."
>
> — [3:09](https://www.youtube.com/watch?v=xbPriQWXtWM&t=189s) &middot; *names the specific claim about compute and quality that has since inverted*

> "now we have this new uh, new um, use for reinforcement learning, which is no longer a cherry on top, but it can dramatically improve the performance of of the model on various different tasks"
>
> — [3:58](https://www.youtube.com/watch?v=xbPriQWXtWM&t=238s) &middot; *marks the O1/R1 turning point as the talk's causal hinge*

> "is your standard base model still uh, what the best uh, what will be the best um, prior for the for the this large-scale reinforcement learning phase"
>
> — [5:10](https://www.youtube.com/watch?v=xbPriQWXtWM&t=310s) &middot; *the talk's central research question, stated plainly*

> "I have my opinions on like synthetic data being the way forward, but I'm I've got like two contrasting uh perspectives here kind of in the slide."
>
> — [6:05](https://www.youtube.com/watch?v=xbPriQWXtWM&t=365s) &middot; *the speaker declares his side on the field's live disagreement*

> "they make a make it really large point to not use any synthetic data or any uh data from any other language model. Um and they really try to, you know, filter their web scripts for this as well."
>
> — [6:05](https://www.youtube.com/watch?v=xbPriQWXtWM&t=365s) &middot; *documents the strongest counterposition to the speaker's own view*

> "web text, which used to make up like up to 85% of the train data in GPT uh 3, is now all the way down at 15%"
>
> — [6:46](https://www.youtube.com/watch?v=xbPriQWXtWM&t=406s) &middot; *the single hardest number in the talk and its main evidentiary anchor*

> "it it's still important, but taking a backseat to things like code and stem abilities as the models kind of gain more real-world use cases related to to those"
>
> — [6:46](https://www.youtube.com/watch?v=xbPriQWXtWM&t=406s) &middot; *names what displaced web text and why*

> "that's the type of question and answer kind of chat data set that you'd you'd expect to see only in post-training, but by pulling it back into the process, they're able to like get the model to learn um the shape of these conversations"
>
> — [7:42](https://www.youtube.com/watch?v=xbPriQWXtWM&t=462s) &middot; *explains the mechanism behind the pre/post-training boundary dissolving*

> "GPT-3 didn't even used to have any specific code data sets, but now code is like the dominating um data data subset that we have in uh pre-training recipes."
>
> — [8:42](https://www.youtube.com/watch?v=xbPriQWXtWM&t=522s) &middot; *a sharp before/after on the most consequential data category shift*

> "There's a lot of uh talk around synthetic data that, you know, blindly tossing it into a model can cause the model to collapse and uh and performance to tank, but there's been a lot of work and uh even at like a large scale, you know, example of this uh turning out really well."
>
> — [9:38](https://www.youtube.com/watch?v=xbPriQWXtWM&t=578s) &middot; *directly rebuts the standard model-collapse objection*

> "you take a seed data item and you sort of upsample it in the mix by uh generating synthetic rephrases of the same information"
>
> — [9:38](https://www.youtube.com/watch?v=xbPriQWXtWM&t=578s) &middot; *concrete recipe detail for the synthetic technique the speaker endorses*

> "the data distribution that the model sees uh in post-training is really really different uh compared to what it sees in pre-training"
>
> — [11:22](https://www.youtube.com/watch?v=xbPriQWXtWM&t=682s) &middot; *identifies the failure mode motivating the whole data-mixing argument*

> "MAI overcame it by uh really cranking up the load balancing coefficient during the SFT stages. Um but I mean, ideally you don't want to mess with the balance that far into training"
>
> — [12:17](https://www.youtube.com/watch?v=xbPriQWXtWM&t=737s) &middot; *a specific engineering tradeoff with a named alternative*

> "there's two broad paradigms that are like that really help build a LM today, and that's supervised learning to next token prediction and RL"
>
> — [13:05](https://www.youtube.com/watch?v=xbPriQWXtWM&t=785s) &middot; *the talk's proposed replacement taxonomy for the training pipeline*

> "it makes sense to view supervised learning as a way specifically to prepare the model for to build useful representations for for RL instead of it being the bulk of like um what the model would be used for like previously"
>
> — [14:02](https://www.youtube.com/watch?v=xbPriQWXtWM&t=842s) &middot; *the thesis restated as a prescription for how to think about pre-training*

> "the base model needs to have some exposure to like uh like the atomic skills that it would need to compose during RL, and um the model can learn to extrapolate from there during RL given like the environment has a sufficient level of difficulty"
>
> — [14:48](https://www.youtube.com/watch?v=xbPriQWXtWM&t=888s) &middot; *the most actionable design principle in the talk, with a stated precondition*

> "it's unclear if we'll see something like for language models because of course, you know, uh, human language is such an insane distribution to have to like learn through reinforcement learning alone"
>
> — [14:48](https://www.youtube.com/watch?v=xbPriQWXtWM&t=888s) &middot; *an honest limit on the AlphaGo analogy the speaker just invoked*

> "base models have kind of moved from general, uh, human knowledge and world priors to reasoning and agentic behavior priors"
>
> — [16:17](https://www.youtube.com/watch?v=xbPriQWXtWM&t=977s) &middot; *the conclusion in one line*

## Positions

- Synthetic data is the way forward for pre-training, despite the common warning that it causes model collapse. ([6:05](https://www.youtube.com/watch?v=xbPriQWXtWM&t=365s), confidence: stated)
- Web text has fallen from ~85% of GPT-3's training mix to ~15% in MAI Thinking 1, with code and STEM data taking its place. ([6:46](https://www.youtube.com/watch?v=xbPriQWXtWM&t=406s), confidence: stated)
- Post-training-style SFT and agentic data should be pulled back into pre-training so the model learns downstream task shapes from the beginning. ([7:42](https://www.youtube.com/watch?v=xbPriQWXtWM&t=462s), confidence: stated)
- Code is now the dominating data subset in pre-training recipes, whereas GPT-3 had no dedicated code datasets. ([8:42](https://www.youtube.com/watch?v=xbPriQWXtWM&t=522s), confidence: stated)
- MoE expert load imbalance during post-training is a symptom of pre/post-training distribution mismatch, and raising the load-balancing coefficient late in training is an inferior fix compared to better early data mixing. ([12:17](https://www.youtube.com/watch?v=xbPriQWXtWM&t=737s), confidence: stated)
- The pre-training / mid-training / post-training / RL taxonomy is muddy and should be replaced with two paradigms: supervised next-token prediction and RL. ([13:05](https://www.youtube.com/watch?v=xbPriQWXtWM&t=785s), confidence: stated)
- Because RL now dominates the compute budget, supervised learning's purpose is to build useful representations for RL rather than to be the model's main capability source. ([14:02](https://www.youtube.com/watch?v=xbPriQWXtWM&t=842s), confidence: stated)
- A base model only needs exposure to the atomic skills RL will later compose; RL can extrapolate from there if the environment is difficult enough. ([14:48](https://www.youtube.com/watch?v=xbPriQWXtWM&t=888s), confidence: stated)
- Language models are unlikely to follow AlphaGo's trajectory of RL fully overtaking supervised learning, because human language is too broad a distribution to learn from RL alone. ([14:48](https://www.youtube.com/watch?v=xbPriQWXtWM&t=888s), confidence: stated)
- If a new interaction paradigm replaces reasoning and agents, base models should be redesigned as priors for that paradigm rather than as web-text archives. ([16:17](https://www.youtube.com/watch?v=xbPriQWXtWM&t=977s), confidence: stated)
- Long-context and agentic-trace datasets currently reserved for mid-training could be moved into pre-training without harm, yielding more stable representations. ([13:05](https://www.youtube.com/watch?v=xbPriQWXtWM&t=785s), confidence: implied)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [post-training](../concepts/post-training.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [scaling laws](../concepts/scaling-laws.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)

