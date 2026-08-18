---
title: "Beyond Static Intelligence: Evaluating Continual Learning"
type: "talk"
slug: "beyond-static-intelligence-evaluating-continual-learning"
track: "Memory & Continual Learning"
org: "UC Berkeley"
day: "Day 3 — Session Day 2"
room: "Track 3"
video_id: "iqloyWCGYQQ"
duration_sec: 1230
word_count: 4107
speakers: ["Parth Asawa"]
---

# Beyond Static Intelligence: Evaluating Continual Learning

**Speakers:** [Parth Asawa](../speakers/parth-asawa.md)

**Org:** UC Berkeley

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 20m 30s

[Watch on YouTube](https://www.youtube.com/watch?v=iqloyWCGYQQ)

## Summary

Parth Asawa (UC Berkeley PhD student) argues that the field evaluates language models under an implicit amnesia assumption — every benchmark instance is independent, so models are scored as if their memory were wiped before each task — and that this makes continual learning invisible to current leaderboards. He lays out three design criteria a continual learning benchmark must satisfy (headroom over pretrained frontier models, shared latent structure across instances, and an in-environment learning signal), and argues that chaining existing benchmarks together fundamentally cannot work because their instances are designed to be independent. He introduces Continual Learning Bench 1.0, six domains of sequenced tasks with per-instance rewards plus deliberately injected concept drift, and a 'gain' metric that subtracts a stateless rerun from the stateful run to separate learning ability from base model strength. The headline empirical result is that vanilla in-context learning — just stuffing prior experience into context — topped the leaderboard on reward and on the reward/cost and gain/cost Pareto frontiers, beating more elaborate context-management systems. He closes with a contrarian bet: bolting continual learning onto frozen checkpoints is a sunk cost fallacy, and parametric approaches that design for continual learning from the start are more promising. Worth watching if you care about memory/agent-evaluation methodology or are choosing between memory architectures.

## Key Points

- Today's evaluation paradigm scores models on independent, one-shot task instances, which is equivalent to assuming the model forgets everything between tasks and therefore cannot reveal learning ability at all.
- Chaining existing benchmarks (e.g., a sequence of AIME problems) does not produce a continual learning benchmark, because traditional benchmark instances are deliberately designed to have no shared structure to exploit.
- A valid continual learning benchmark needs three properties: headroom (tasks frontier models can't already solve from pretraining), shared latent structure across instances, and a learning mechanism in the environment such as scalar reward, error messages, or textual feedback.
- Cumulative reward alone confounds continual learning ability with base model strength; a strong-but-non-learning system can outscore a weaker system that is genuinely improving.
- The 'gain' metric runs every system twice — once stateful, once reset between instances — and takes the difference, isolating the benefit of prior experience from initial capability.
- Reward, gain, and cost are reported on Pareto frontiers rather than collapsed into one number, because base capability, learning, and expense all matter.
- Continual Learning Bench 1.0 spans six domains (blind spectrum monitoring, codebase adaptation, epidemiology cohort studies, exploitable poker, database exploration, sales prediction) with domain-expert-validated task sequences and injected concept drift such as database migrations.
- Vanilla in-context learning topped the leaderboard on reward and held up across the reward-vs-cost and gain-vs-cost Pareto frontiers, outperforming more expensive context-management systems — a result the speaker finds surprising and partly attributes to only medium-horizon tasks.
- Observed failure modes fall on one side or the other of the stability–plasticity tradeoff: a forecasting model oscillating back to a prediction it had already been told was too high (stability failure), and a notepad-based system dismissing relevant prior notes as inapplicable (plasticity failure).
- The speaker's broader bet is that current continual learning research is a sunk cost fallacy on frozen checkpoints, and that designing for continual learning as a first-order requirement might collapse the training stack into one learning phase followed by deployment.

## Notable Quotes

> "what we've done is we've kind of told the models, imagine that every time you do something, you completely forget your memory."
>
> — [0:52](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=52s) &middot; *The single-sentence framing of the whole critique of current evaluation.*

> "Continual learning to me is sample efficient online learning that is stable over long horizons."
>
> — [1:28](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=88s) &middot; *The speaker's working definition, which the rest of the benchmark design follows from.*

> "today I'm not going to make a case for which one of these can solve continual learning, though I do have an opinion and I'll share it at the end."
>
> — [2:42](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=162s) &middot; *Sets up the deliberate separation of measurement claims from method claims.*

> "if continual learning doesn't look like point capabilities, we need to be measuring it the right way to optimize for the right objective as a field."
>
> — [3:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=196s) &middot; *The thesis, and the line he returns to as the closing takeaway.*

> "they won't work for frontier language models. And the reason being that frontier language models are pre-trained on vast distributions of the entire internet or economically valuable tasks we care about."
>
> — [4:21](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=261s) &middot; *States why prior continual-learning evals don't transfer to frontier models.*

> "benchmark instances are in traditional language model evaluation are designed to be independent. That means they don't have shared structure across tasks and as a result you can't meaningfully expect them to improve from earlier experience in future instances."
>
> — [5:05](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=305s) &middot; *The core argument against the most common proposed shortcut.*

> "If the model can improve on your tasks by just training offline and not actually require any online learning, then it's not a good task for measuring continual learning."
>
> — [5:48](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=348s) &middot; *Crisp, checkable criterion for headroom that benchmark designers can apply directly.*

> "This could look like scalar reward. It could look like error messages. It could look like textual feedback. The point being, there needs to exist something in the environment that's giving agents signal to learn and improve on future tasks."
>
> — [7:06](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=426s) &middot; *Concretizes the learning-mechanism criterion across multiple feedback modalities.*

> "Gain refers to the difference between stateful reward and stateless reward."
>
> — [8:55](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=535s) &middot; *The benchmark's central methodological contribution, stated in one line.*

> "It isolates out what your benefit of from actually learning was versus your base model's initial capability."
>
> — [10:12](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=612s) &middot; *Explains what gain buys you, verbatim disfluency and all.*

> "There isn't one single metric that I think defines continual learning because we still care about the base model strength."
>
> — [10:12](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=612s) &middot; *Rejects a single-number leaderboard, a position many benchmark authors would resist.*

> "You kind of have an innate ability to maintain the stability and plasticity trade-off in your mind. But this isn't native to a lot of language models."
>
> — [12:15](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=735s) &middot; *Names the tradeoff that organizes his entire failure-mode taxonomy.*

> "It tops the leaderboard and and it's not just on reward. It's actually also when we look at the Pareto frontiers, this kind of holds across reward uh versus cost and gain versus cost."
>
> — [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s) &middot; *The headline empirical result: vanilla ICL wins on every frontier measured.*

> "it was still surprising that these more expensive context management systems perform a lot poorly compared to just vanilla in context learning on these sets of tasks where you have to do real learning."
>
> — [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s) &middot; *Directly challenges the value proposition of memory-management tooling.*

> "I'm going to argue that most failure modes in continual learning fall on one side of the stability plasticity trade-off."
>
> — [14:50](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=890s) &middot; *A generalizable diagnostic claim about why continual learning systems break.*

> "But these models were never designed to be continual learners to begin with."
>
> — [17:37](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1057s) &middot; *The pivot into his contrarian view on methods.*

> "one of my hypotheses here at least is that we're operating in a bit of a sunk cost fallacy that because we've trained models the way we are today, we need continual learning methods that work on top of that."
>
> — [17:37](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1057s) &middot; *The strongest position in the talk, and the one most likely to be contested.*

> "In the purest sense, continual learning might just be one set, one phase of training for continual learning and everything after that is deployment."
>
> — [17:37](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1057s) &middot; *Concrete picture of what a redesigned training stack would look like.*

> "continual learning doesn't look like point capabilities. We need to measure it the right way to optimize for the right objective as a field because that's a history of how machine learning has progressed."
>
> — [19:51](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1191s) &middot; *The closing takeaway he explicitly flags as the one thing to remember.*

## Positions

- Current language model evaluation is effectively a memoryless paradigm and does not measure continual learning at all. ([3:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=196s), confidence: stated)
- Chaining existing independent benchmark instances together cannot produce a valid continual learning benchmark, because those instances lack shared structure to exploit. ([5:05](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=305s), confidence: stated)
- Existing continual learning evaluations (sequential task-distribution training, long-horizon factual recall) are insufficient: they don't treat sample efficiency as first-order, don't always measure learning, and won't work for frontier models. ([4:21](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=261s), confidence: stated)
- A valid continual learning benchmark requires headroom, shared latent structure, and an in-environment learning mechanism. ([5:48](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=348s), confidence: stated)
- Cumulative reward alone confounds learning ability with base model strength, so gain (stateful minus stateless reward) is needed to isolate learning. ([7:45](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=465s), confidence: stated)
- No single metric defines continual learning; reward, gain, and cost should all be reported on Pareto frontiers. ([10:12](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=612s), confidence: stated)
- Vanilla in-context learning outperformed more sophisticated context-management systems on Continual Learning Bench 1.0, topping the leaderboard on reward and holding across the reward-vs-cost and gain-vs-cost Pareto frontiers. ([14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s), confidence: stated)
- The in-context learning result is likely an artifact of medium-horizon tasks and is not the end state of continual learning. ([14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s), confidence: stated)
- Most continual learning failure modes can be classified as failures of either stability or plasticity. ([14:50](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=890s), confidence: stated)
- Building continual learning methods on top of already-trained frozen checkpoints is a sunk cost fallacy; parametric approaches that co-design architecture, data, and algorithms are more promising. ([17:37](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1057s), confidence: stated)
- If continual learning were a first-order design requirement, the multi-stage training stack could collapse into a single learning phase followed by deployment. ([18:10](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1090s), confidence: stated)
- Current models are not capable enough to simulate user personalization environments well enough to benchmark continual learning against them. ([19:18](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1158s), confidence: stated)
- Third-party institutions and open science in AI research need to be reimagined in light of consolidation of power and safety concerns. ([18:45](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=1125s), confidence: implied)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [benchmark design](../concepts/benchmark-design.md)
- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [continual learning](../concepts/continual-learning.md)
- [online evaluation](../concepts/online-evaluation.md)
- [prompt engineering](../concepts/prompt-engineering.md)

