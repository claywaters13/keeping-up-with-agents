---
title: "Scaling Compute on Context"
type: "talk"
slug: "scaling-compute-on-context"
track: "Memory & Continual Learning"
org: "Engram"
day: "Day 3 — Session Day 2"
room: "Track 3"
video_id: "WiqDvX6isc4"
duration_sec: 1182
word_count: 3656
speakers: ["Jack Morris"]
---

# Scaling Compute on Context

**Speakers:** [Jack Morris](../speakers/jack-morris.md)

**Org:** Engram

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 19m 42s

[Watch on YouTube](https://www.youtube.com/watch?v=WiqDvX6isc4)

## Summary

Jack Morris of Engram frames what he calls 'scaling compute on context': the problem of making a pretrained model genuinely 'know' a private, fixed corpus D — your emails, meeting transcripts, company documents — rather than just public internet data. He argues the three classic scaling axes (more data, more compute, bigger models) have driven the entire deep learning revolution but have only ever been applied to public data, leaving models with breadth but no depth in any private domain. Since you can't create more of your own data and can't pretrain from scratch on it, compute is the only axis left. He then walks through the candidate techniques — naive next-token training, KV compaction, on-policy distillation and self-study, synthetic continued pretraining, unsupervised RL environments — and argues each saturates against a 'synthetic data wall' where compute stops buying depth. His conclusion is that the missing ingredient is self-improvement in the AlphaGo mold, where the model's own progress makes its training data harder. Watch it for a clear taxonomy of the continual-learning landscape and an honest account of where every approach breaks; skip it if you want experimental results, which he explicitly doesn't present.

## Key Points

- Current models have Terence Tao–style breadth — knowledge of every public mathematical topic — but lack the depth of a graduate student who spent five years in one area, and that depth is what scaling compute on context is meant to buy.
- The core limitation of the present paradigm is not intellectual but structural: models are trained on publicly available data, so they cannot acquire personalized knowledge after training.
- Even post-training data from vendors like Scale AI, Surge AI, and Mercor is public by definition, because it is data the model could repeat to any user.
- Given a fixed private corpus, the data axis is unavailable and training from scratch is off the table, which leaves compute as the only remaining scaling axis.
- Naively running next-token prediction on your own corpus can drive loss to ~0.0001 while the model collapses at generation time and fails to answer anything not literally encoded in the data.
- KV compaction can compress a corpus into a compact representation but only works for data that fits in context and forfeits the benefits of taking gradients.
- On-policy distillation and self-study (from the cartridges paper) train the model to behave as if D were in context, but raise the unsolved question of what data to distill on.
- Synthetic continued pretraining is promising but overwrites pretraining, is hard to scale, and requires post-training afterward — a problem since most practitioners only have post-trained models, not good base models.
- Every technique surveyed hits a synthetic data wall: once you define a dataset and train on it, an adequately parameterized model eventually learns all of it and additional compute stops adding depth.
- The proposed way past the wall is self-improvement in the AlphaGo mold, where the model's own improvement generates progressively harder training data, converting a plateauing curve into a rising one.

## Notable Quotes

> "one of the things that you'll hear him talk about is how AI knows like every single public mathematical topic and it can make connections between things that you wouldn't expect and help sort of like bridge gaps in the literature that in in a way that no human even can know because it's read so much."
>
> — [0:52](https://www.youtube.com/watch?v=WiqDvX6isc4&t=52s) &middot; *States the breadth side of the talk's central breadth-versus-depth framing.*

> "But it maybe lacks the depth that you would look for from like, for example, a graduate student who spent 5 years practicing in in one area that gets this like almost like subconscious intuition for for the problem space."
>
> — [1:47](https://www.youtube.com/watch?v=WiqDvX6isc4&t=107s) &middot; *The depth side of the framing, and the target capability the whole talk is aimed at.*

> "models still are quite bad at writing AMD kernels. There are not that many good kernels written on AMD GPUs that are public. And they're intended to acquire this knowledge through pre-training, but they don't because it doesn't occur very often."
>
> — [3:10](https://www.youtube.com/watch?v=WiqDvX6isc4&t=190s) &middot; *Concrete, checkable example of long-tail skill failure traced to data frequency.*

> "It's like the core problem with the current paradigm in AI that models cannot acquire new knowledge after training in in a personalized way."
>
> — [3:43](https://www.youtube.com/watch?v=WiqDvX6isc4&t=223s) &middot; *The strongest form of the talk's central claim.*

> "by definition, models have to be trained on data that's sort of open to the public and they can't learn the depth of like the things that you know."
>
> — [3:43](https://www.youtube.com/watch?v=WiqDvX6isc4&t=223s) &middot; *Frames the public-data ceiling as structural rather than a temporary engineering gap.*

> "there's a lot of names for this. Like people call it um sleep time compute, continual learning, neural memory, write time compute, note taking, dreaming, studying, machine studying. In classical AI, maybe it's called amortized inference."
>
> — [4:23](https://www.youtube.com/watch?v=WiqDvX6isc4&t=263s) &middot; *Useful cross-talk vocabulary map for a field that hasn't settled on a term.*

> "the reason why it doesn't have like even a set agreed upon name is because the paradigm is like very early and hasn't been solidified the way, for example, pre-training or or post-training have."
>
> — [4:23](https://www.youtube.com/watch?v=WiqDvX6isc4&t=263s) &middot; *Explains the terminological chaos as evidence of the field's immaturity.*

> "now they have this new layer of post training data that's like experts that are hired through data acquisition companies like Scale AI, Surge AI, and Mercor. But, they're still by definition creating publicly available data because it's something that the model could tell to a user."
>
> — [5:45](https://www.youtube.com/watch?v=WiqDvX6isc4&t=345s) &middot; *Names companies and argues a non-obvious point: paid expert data is still public data.*

> "scale is clearly the thing that drives progress, you know, it's not necessarily new algorithms or like great new ideas."
>
> — [6:22](https://www.youtube.com/watch?v=WiqDvX6isc4&t=382s) &middot; *A contestable position on what actually produces capability gains.*

> "models are getting better at, you know, coding in the way that is public on GitHub, they're getting better at doing math in ways that are written in public textbooks, but they're not getting more knowledge of you or your life or your work."
>
> — [6:54](https://www.youtube.com/watch?v=WiqDvX6isc4&t=414s) &middot; *Crisply states the asymmetry that motivates the company's existence.*

> "we can't create new data. So, like the kind of data scaling axis is out the window."
>
> — [7:32](https://www.youtube.com/watch?v=WiqDvX6isc4&t=452s) &middot; *The first-principles move that reduces three scaling axes to one.*

> "this leaves us with essentially one axis of scaling, which is compute. And this brings us to the title of the talk today, which is scaling compute on context."
>
> — [7:32](https://www.youtube.com/watch?v=WiqDvX6isc4&t=452s) &middot; *The talk's thesis stated as a derivation, not an assertion.*

> "one thing that's been beneficial for us to realize is that the amount of data isn't really fixed. There are a lot of ways that you can get more data afterwards."
>
> — [8:11](https://www.youtube.com/watch?v=WiqDvX6isc4&t=491s) &middot; *Self-qualifies the fixed-data-budget premise the argument was built on.*

> "You can get to a loss of like 0.0001. Um and you can end up with a model that knows the data perfectly well. And then when you generate from it, it basically collapses."
>
> — [11:08](https://www.youtube.com/watch?v=WiqDvX6isc4&t=668s) &middot; *Reports a number and a concrete failure mode for the most obvious approach.*

> "just doing this kind of next token prediction on the data you have doesn't produce a model that has interesting generalization properties like normal models."
>
> — [11:08](https://www.youtube.com/watch?v=WiqDvX6isc4&t=668s) &middot; *Rules out naive finetuning as a path to depth.*

> "it can't answer any question unless the question is perfectly encoded in the data with its answer, which is like never the case in in practice."
>
> — [11:50](https://www.youtube.com/watch?v=WiqDvX6isc4&t=710s) &middot; *Names why memorization is not knowing.*

> "The main one being it only applies to things that are in context, but it also misses, I think, some of the magic that you can get from from taking gradients."
>
> — [13:01](https://www.youtube.com/watch?v=WiqDvX6isc4&t=781s) &middot; *Names the specific tradeoff that disqualifies compaction approaches.*

> "you have text and you show it to the model and then you make the model think that the text is in context. That's more or less the trick of on policy distillation."
>
> — [13:01](https://www.youtube.com/watch?v=WiqDvX6isc4&t=781s) &middot; *Compact working definition of on-policy distillation.*

> "pre-training is amazing for knowledge acquisition. Like I can ask Claude what uh I don't know, result I got in in a paper that I've written and it actually knows this, which is incredible."
>
> — [14:17](https://www.youtube.com/watch?v=WiqDvX6isc4&t=857s) &middot; *Grounds the claim that pretraining is the mechanism worth imitating.*

> "one blocker is you then have to post-train the model after doing this. So, a lot of people don't actually start with good pre-trained base models. They have post-trained models, which makes this hard."
>
> — [14:53](https://www.youtube.com/watch?v=WiqDvX6isc4&t=893s) &middot; *A practical constraint on synthetic continued pretraining that practitioners will hit.*

> "whatever you do, you have to define the data set, and then you train on the data set, and eventually things saturate. So, even if it's like really hard, unless your model is under parameterized, eventually it will learn all the data."
>
> — [16:11](https://www.youtube.com/watch?v=WiqDvX6isc4&t=971s) &middot; *The unifying objection he raises against every approach he surveyed, including his own field's.*

> "It's kind of like a data wall in in the synthetic sense, where when you create synthetic data from D and and train on it, you eventually hit this upper bound where like you've learned all of the synthetic data."
>
> — [16:52](https://www.youtube.com/watch?v=WiqDvX6isc4&t=1012s) &middot; *Coins the framing that defines the open problem.*

> "this is actually the magic behind a lot of successful RL systems like AlphaGo is that AlphaGo makes its own training questions harder by getting better through training."
>
> — [17:30](https://www.youtube.com/watch?v=WiqDvX6isc4&t=1050s) &middot; *The mechanism he proposes as the way past the synthetic data wall.*

> "when we started the company, we we generated curves that look just like this blue curve where no matter sort of how much data we generate or how much we train, we kind of do plateau because there's this almost like natural upper bound to how much you can learn in one go from D."
>
> — [17:30](https://www.youtube.com/watch?v=WiqDvX6isc4&t=1050s) &middot; *Candid report of their own negative result, which sets up their current direction.*

> "it turns out that there are more sophisticated things you can do that make the training gradually harder that make the model better over time."
>
> — [18:22](https://www.youtube.com/watch?v=WiqDvX6isc4&t=1102s) &middot; *Engram's claimed positive result, stated without detail — the talk's key withheld card.*

## Positions

- The core problem with the current AI paradigm is that models cannot acquire new knowledge after training in a personalized way. ([3:43](https://www.youtube.com/watch?v=WiqDvX6isc4&t=223s), confidence: stated)
- Post-training data purchased from vendors like Scale AI, Surge AI, and Mercor is still public data by definition, because it is content the model could tell any user. ([5:45](https://www.youtube.com/watch?v=WiqDvX6isc4&t=345s), confidence: stated)
- Scale, not new algorithms or new ideas, is what drives progress in AI capability. ([6:22](https://www.youtube.com/watch?v=WiqDvX6isc4&t=382s), confidence: stated)
- The Meter task-length trend showing models completing longer tasks over time is purely an artifact of scaling. ([5:45](https://www.youtube.com/watch?v=WiqDvX6isc4&t=345s), confidence: stated)
- For a fixed private corpus, compute is the only viable scaling axis, since you cannot create more data and cannot train from scratch. ([7:32](https://www.youtube.com/watch?v=WiqDvX6isc4&t=452s), confidence: stated)
- Plain next-token-prediction finetuning on your own corpus fails: the model reaches near-zero loss, collapses at generation time, and gains no useful generalization. ([11:08](https://www.youtube.com/watch?v=WiqDvX6isc4&t=668s), confidence: stated)
- Training on your own data is not an indefinite scaling axis, because the information transfers into the weights and then learning stops. ([11:08](https://www.youtube.com/watch?v=WiqDvX6isc4&t=668s), confidence: stated)
- KV compaction is limited to data that fits in context and forfeits the benefits of gradient-based learning. ([13:01](https://www.youtube.com/watch?v=WiqDvX6isc4&t=781s), confidence: stated)
- Synthetic continued pretraining partially overwrites pretraining and is difficult to scale, and it requires re-post-training the model afterward. ([14:53](https://www.youtube.com/watch?v=WiqDvX6isc4&t=893s), confidence: stated)
- None of the surveyed approaches — naive finetuning, compaction, distillation, synthetic continued pretraining, unsupervised RL — allow compute to be added arbitrarily for continued gains. ([16:11](https://www.youtube.com/watch?v=WiqDvX6isc4&t=971s), confidence: stated)
- Any approach that fixes a dataset and trains on it will saturate unless the model is underparameterized. ([16:11](https://www.youtube.com/watch?v=WiqDvX6isc4&t=971s), confidence: stated)
- Self-improvement, where model progress makes its own training data harder, is the mechanism behind successful RL systems like AlphaGo and the missing component for scaling compute on context. ([17:30](https://www.youtube.com/watch?v=WiqDvX6isc4&t=1050s), confidence: stated)
- Engram has found more sophisticated methods that gradually increase training difficulty and escape the plateau they initially observed. ([18:22](https://www.youtube.com/watch?v=WiqDvX6isc4&t=1102s), confidence: stated)
- The fixed-data-budget premise is an idealization; in practice you can acquire more data by seeking out related sources and people. ([8:11](https://www.youtube.com/watch?v=WiqDvX6isc4&t=491s), confidence: stated)
- Knowledge in frontier models comes mostly from pretraining rather than from synthetic data tricks applied later. ([14:17](https://www.youtube.com/watch?v=WiqDvX6isc4&t=857s), confidence: implied)

## Concepts

- [context compaction](../concepts/context-compaction.md)
- [continual learning](../concepts/continual-learning.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [scaling laws](../concepts/scaling-laws.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)

