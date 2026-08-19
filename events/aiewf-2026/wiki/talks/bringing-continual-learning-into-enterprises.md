---
title: "Bringing Continual Learning into Enterprises"
type: "talk"
slug: "bringing-continual-learning-into-enterprises"
track: "Memory & Continual Learning"
org: "Applied Compute"
day: "Day 3 — Session Day 2"
room: "Track 3"
video_id: "ZTA0GwpAUak"
duration_sec: 1142
word_count: 3596
speakers: ["Samuel Denton"]
---

# Bringing Continual Learning into Enterprises

**Speakers:** [Samuel Denton](../speakers/samuel-denton.md)

**Org:** Applied Compute

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 19m 02s

[Watch on YouTube](https://www.youtube.com/watch?v=ZTA0GwpAUak)

## Summary

Samuel Denton of Applied Compute lays out a practical taxonomy for doing continual learning inside enterprises, organized as a 2x2 grid: production traces can be offline (a batch dump) or online (live rollouts), and the 'hint' that makes a teacher model smarter than the student can likewise be offline (a fixed prior about desired behavior) or online (constructed dynamically from what the on-policy model just did). He argues enterprises can get value on day one from quadrant one — offline traces plus offline hints, no replayable environment required — while quadrant four (online traces plus online hints) is the highest-ceiling flywheel where inference and training collapse into one system. Two concrete results anchor the talk: on SWE-bench, nudging a Qwen 3.5 thinking model to submit before turn 40 raised the task-complete call rate from ~22% to ~60% with no regression in test pass rate; and for a customer's out-of-distribution hyperlink format, online hinting drove correct formatting from ~15% to ~80% where offline hinting barely moved it. A recurring theme is doing all of this without a golden answer or rubric, which Denton says most distillation work wrongly assumes. Worth watching if you have production agent traces sitting unused and want a concrete mental model for turning them into model updates.

## Key Points

- Distillation for continual learning spans a spectrum from a one-time offline batch of production traces, through daily batches, to a fully unified engine where serving and training are the same loop.
- A second, independent axis is hinting: the privileged information that makes the teacher smarter than the student can either be a static offline prior about desired behavior or a hint constructed dynamically from the specific online rollout.
- Crossing those axes gives four quadrants; Applied Compute focuses on quadrant one (offline trace, offline hint) for immediate enterprise value and quadrant four (online trace, online hint) for the highest ceiling.
- Quadrant one requires no replayable environment — you can improve an agent from a dump of production traces alone, which is where most enterprises actually are today.
- In the SWE-bench experiment, a model taking up to 80 turns was pushed to call a submit tool before turn 40; the task-complete call rate rose from ~22% to ~60% while test pass rate stayed flat or rose slightly.
- Surprisingly, in the fully offline setting the teacher never forces the tool-call tokens themselves — it reshapes the reasoning path toward the tool call, and the behavior follows.
- Rolling out a single on-policy step from an offline trace ('a little bit of a cheat') gets more of the SWE-bench gain than the fully offline setup, showing that even minimal on-policyness helps.
- For a very out-of-distribution hyperlink format, reward shaping and SFT both degraded general coding performance, while online hinting on on-policy rollouts took correct formatting from ~15% to ~80%; the same hint applied statically to every rollout climbed far less.
- Two practical tricks: use a judge to pick where in the rollout to inject the hint and distill only on the next step or few steps, and use relevance-masked self-distillation to learn only from teacher tokens that matter, avoiding connector-word noise and catastrophic degradation.

## Notable Quotes

> "you get a single batch of traces from a production agent, and you're meant to just do something with it"
>
> — [1:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=80s) &middot; *Frames the offline end of the spectrum as the messy reality most enterprises hand over.*

> "this is sort of the holy grail of continual learning where I have a model that's serving production traffic, it does a rollout, it creates a trace, we figure out how to learn from that trace, we update the model, and then we serve the next production request"
>
> — [1:56](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=116s) &middot; *Crisp definition of the fully online flywheel the whole taxonomy points toward.*

> "our goal at Applied Compute is to meet enterprises where they are, right? So, they're across this spectrum and we want to provide value across both ends of the spectrum."
>
> — [3:08](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=188s) &middot; *States the product thesis: serve the whole spectrum rather than insisting on full online training.*

> "in order to create a teacher that's smarter than this on-policy model, we need to create some kind of hint or have some kind of privileged information"
>
> — [3:46](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=226s) &middot; *The core mechanism of the talk — where teacher advantage actually comes from.*

> "we don't actually have to have replayability of a production environment"
>
> — [7:40](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=460s) &middot; *Names the practical barrier that quadrant one sidesteps, which is why it ships first.*

> "We can improve for free today by using offline production traces. Give us a dump of your production data. We'll find a way to make it valuable."
>
> — [9:05](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=545s) &middot; *The value-accrual pitch in one line, and a checkable claim about what offline traces alone can do.*

> "a lot of distillation work is done assuming you have some kind of golden answer that you can distill into the model. And this is often not the case."
>
> — [9:47](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=587s) &middot; *A direct critique of standard distillation practice and the talk's sharpest contrarian position.*

> "we want to think about how we can do continual learning and distillation without having some beautifully golden rubric to accompany every task"
>
> — [9:47](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=587s) &middot; *States the constraint the entire hinting approach is designed around.*

> "on SWE-bench, we found that this model was essentially taking like up to 80 turns to submit its answer. What we wanted to do was encourage it to call a tool to submit its task before turn 40."
>
> — [10:56](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=656s) &middot; *Concrete setup with numbers for the first experiment.*

> "the task complete call rate increases dramatically from about 22% to 60%"
>
> — [12:39](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=759s) &middot; *Headline result of the offline-trace, offline-hint experiment.*

> "the teacher doesn't force the tool call. It just starts to force the the reasoning path towards the tool call without ever actually changing the tool call."
>
> — [13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s) &middot; *The mechanistically surprising finding: behavior change propagates through reasoning, not through the target tokens.*

> "you can roll out just one step from the on policy model given an offline production trace"
>
> — [13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s) &middot; *Describes the cheap hybrid that recovers much of the benefit of online training.*

> "even doing SFT on traces where we knew the hyperlink was correctly formatted, we saw that there was this sort of degradation in overall coding agent performance"
>
> — [14:35](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=875s) &middot; *Reports the failure of two obvious baselines, motivating online hinting.*

> "the percentage of correct hyperlink formatting jumped drastically from about, I guess, 15% all the way up to around 80%"
>
> — [15:21](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=921s) &middot; *Headline number for the online-trace, online-hint case.*

> "you can see that we do climb the behavior a little bit, but far less than in this online hinting world"
>
> — [15:21](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=921s) &middot; *The head-to-head comparison that justifies dynamic hints over static ones.*

> "rather than injecting a hint to the beginning of a rollout, we use a judge to essentially decide where in the rollout we should be injecting hints"
>
> — [15:53](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=953s) &middot; *Concrete implementation detail the speaker calls essential to making distillation work.*

> "it's best to just do distillation on that next step that occurs or maybe a few steps forward rather than the entire rollout"
>
> — [16:31](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=991s) &middot; *A specific, transferable training recipe backed by the observed KL signal decay.*

> "often, we'll see that the teacher model has preferences of certain connector words that are not really relevant to actually what we're trying to teach the student"
>
> — [17:05](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=1025s) &middot; *Explains why token-level relevance masking is needed in self-distillation.*

> "we use offline hinting with offline production traces to provide value on day one to enterprise clients. Give us production traces and we can teach you a certain behavior."
>
> — [17:48](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=1068s) &middot; *The talk's summary of what is deployable now versus aspirational.*

> "because that judge is able to adapt to whatever the online model does in production"
>
> — [17:48](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=1068s) &middot; *Names the reason online hinting generalizes across behaviors where static hints don't.*

## Positions

- Continual learning setups can be classified along two independent axes — offline vs. online traces and offline vs. online hints — yielding four distinct distillation regimes. ([5:02](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=302s), confidence: stated)
- Enterprises can get real agent improvement from a one-time batch of production traces without any replayable production environment. ([7:40](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=460s), confidence: stated)
- Most distillation work wrongly assumes access to a golden answer or rubric, and useful continual learning must work without one. ([9:47](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=587s), confidence: stated)
- Targeted behavior change via offline hints can be achieved without degrading base task performance — SWE-bench task complete rate rose from ~22% to ~60% while test pass rate held steady or improved slightly. ([12:39](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=759s), confidence: stated)
- A teacher can shift a student toward a tool call purely by reshaping the reasoning path, without ever modifying the tool-call tokens themselves. ([13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s), confidence: stated)
- Adding a single on-policy rollout step to an otherwise offline trace yields a larger SWE-bench pass rate gain than the fully offline setup. ([13:58](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=838s), confidence: stated)
- Reward shaping for a specific output format and SFT on correctly formatted traces both cause degradation in general coding agent performance for out-of-distribution behaviors. ([14:35](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=875s), confidence: stated)
- Online hints constructed per-rollout substantially outperform a fixed offline hint applied uniformly — ~15% to ~80% correct hyperlink formatting versus a small climb. ([15:21](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=921s), confidence: stated)
- Per-step hinting, with a judge choosing the injection point, is critical to making distillation work rather than hinting at the start of a rollout. ([15:53](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=953s), confidence: stated)
- The KL learning signal decays the further a step is from the injected hint, so distillation should be restricted to the next step or a few steps after the hint. ([16:31](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=991s), confidence: stated)
- Using an LLM judge to mask which teacher tokens are learned from improves acquisition of out-of-distribution behavior while reducing catastrophic degradation. ([17:05](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=1025s), confidence: stated)
- The online-trace, online-hint quadrant is the highest-ceiling and most scalable approach because a judge can adapt to whatever the production model does. ([17:48](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=1068s), confidence: stated)
- As serving and training infrastructure converge into a single system, continual improvement of production models becomes automatic rather than a separate batch process. ([10:16](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=616s), confidence: implied)

## Concepts

- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [continual learning](../concepts/continual-learning.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [post-training](../concepts/post-training.md)
- [production trace mining](../concepts/production-trace-mining.md)

