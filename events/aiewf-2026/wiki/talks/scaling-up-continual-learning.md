---
title: "Scaling up Continual Learning"
type: "talk"
slug: "scaling-up-continual-learning"
track: "Memory & Continual Learning"
org: "Trajectory"
day: "Day 3 — Session Day 2"
room: "Track 3"
video_id: "zL1kLftVTlo"
duration_sec: 1383
word_count: 4242
speakers: ["Ronak Malde"]
---

# Scaling up Continual Learning

**Speakers:** [Ronak Malde](../speakers/ronak-malde.md)

**Org:** Trajectory

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 23m 03s

[Watch on YouTube](https://www.youtube.com/watch?v=zL1kLftVTlo)

## Summary

Ronak Malde (ex-WinSurf research lead, now founder of Trajectory) argues that the field's current best post-training algorithm, GRPO, fails four criteria needed for real continual learning: online task distribution, on-policy sampling, single-rollout parallelism, and per-token dense reward. His proposed alternative is on-policy self-distillation (OPSD), where a student model's rollout is scored against the same model given a 'hint' — privileged information injected into the prompt — so the student matches the hinted teacher's log probs token by token, satisfying all four criteria at once. He reports OPSD pushes past where GRPO saturates on LiveCodeBench (roughly Sonnet-level), collapses tokens-to-solution rather than inflating them, and scales to 120B–1T parameter models on long-horizon tool-calling agents. The bulk of the talk is the failure modes that only appear at scale: the 'wait' problem (teacher endlessly course-correcting a divergent student until everything becomes hedging words) and hint leakage (OPSD's analogue of reward hacking), plus two fixes — step-level KL-divergence token weighting and residual guidance via partial hints. Worth watching if you want a concrete, mechanism-level alternative to RL for learning from production traffic, with honest reporting of where it breaks.

## Key Points

- Malde frames four criteria for a continual learning algorithm — online task distribution, on-policy sampling, parallelism of one, and per-token reward — and walks SFT, DPO/RLHF, and GRPO through them to show each era satisfies only two.
- On-policy self-distillation replaces the smarter teacher model with the same model given 'privileged information' (a hint) in the prompt, so you can push the frontier without access to a stronger model.
- Because distillation matches the full vocabulary distribution rather than sharpening the sampled token, OPSD can shift entire distributions instead of nudging them, which he credits for breaking past GRPO's saturation point.
- Eliminating grouped rollouts removes the environment-infrastructure bottleneck: one example yields training signal, so no one-to-one copies of the real world are needed.
- OPSD reportedly reduces tokens-to-solution on hard tasks, inverting RL's tendency to reward longer thinking traces.
- At the 120B+ scale with 50–100 tool calls, the algorithm degrades: high run-to-run variance, erratic eval accuracy, and tool-call format errors.
- The 'wait' problem arises when a long-horizon student diverges so far that the teacher course-corrects at every opportunity, collapsing the model into hedging tokens and a suboptimal midpoint between two divergent distributions.
- Step-level KL divergence between student and teacher is used as a per-step token weight (not a KL penalty), letting training focus on the first divergence and re-engage when the trajectory recovers.
- Hint leakage is OPSD's reward hacking: a hint containing the answer teaches the model to produce reasoning traces that work backward from a solution it would never have in production.
- Residual guidance takes a linear combination of a half-hint teacher and a full-hint teacher to gauge hint strength and avoid shifting the model into out-of-distribution territory.

## Notable Quotes

> "we are actually spending hundreds of trillions of tokens every single day on inference and we're generating great amounts of data on how models in the real world are are failing, how they're doing well. And that should be signal that we should be capturing and training on."
>
> — [1:41](https://www.youtube.com/watch?v=zL1kLftVTlo&t=101s) &middot; *States the core motivating asymmetry the whole talk builds on.*

> "we are left with a bunch of benchmarks that are getting more time consuming more and more expensive and and perhaps more concerningly they're not tied to real world use cases where people are using AI."
>
> — [0:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=50s) &middot; *The indictment of benchmark scaling that motivates continual learning.*

> "we are shoving every single reward into one scaler in order to train on when the real world is messy."
>
> — [2:54](https://www.youtube.com/watch?v=zL1kLftVTlo&t=174s) &middot; *Compresses the dense-vs-scalar-reward critique of RL into one line.*

> "we basically took a Fouian bargain and wanted to max on on policy rollouts which is extremely powerful right we now have models that are capable of amazing things because they are on policy"
>
> — [4:56](https://www.youtube.com/watch?v=zL1kLftVTlo&t=296s) &middot; *Names GRPO's tradeoff explicitly — gains bought with infrastructure and reward sparsity.*

> "imagine you were trying to write an essay and your teacher just gave you a score of 87 out of 100. You would have to run through so many different examples to get to the idea of what a good essay is"
>
> — [6:43](https://www.youtube.com/watch?v=zL1kLftVTlo&t=403s) &middot; *The talk's clearest intuition pump for why sequence-level reward is inefficient.*

> "when we're trying to push the frontier we don't magically have some smarter model, right?"
>
> — [7:52](https://www.youtube.com/watch?v=zL1kLftVTlo&t=472s) &middot; *The precise gap that self-distillation is designed to fill.*

> "You take what's called this hint, put it into the beginning of the prompt, and now you match the log props of the student without that hint to the teacher with that hint. And this is an extremely powerful algorithm."
>
> — [8:27](https://www.youtube.com/watch?v=zL1kLftVTlo&t=507s) &middot; *The complete mechanism of OPSD in two sentences.*

> "now there's no parallel rollouts. We don't need a group of eight in order to roll out but just from a single example we're able to get information. So that takes away the environment bottleneck"
>
> — [9:40](https://www.youtube.com/watch?v=zL1kLftVTlo&t=580s) &middot; *The infrastructure claim that makes OPSD attractive for production deployment.*

> "we're not just taking now a distribution like RL and slightly sharpening it, but we're instead actually shifting entire distributions."
>
> — [10:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=650s) &middot; *The mechanistic reason he claims OPSD exceeds RL's ceiling.*

> "If you take a look at live codebench actually we found that gpo saturates around sonnet level performance and and doesn't really push the frontier"
>
> — [10:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=650s) &middot; *A specific, checkable empirical claim about GRPO's ceiling.*

> "with RL a fundamental limitation and if you guys have ever trained RL models is the models like to think a lot right the more tokens that you expend it's it's just going to do better but with opsd you don't have that problem"
>
> — [11:29](https://www.youtube.com/watch?v=zL1kLftVTlo&t=689s) &middot; *Reports a token-efficiency result that runs opposite to RL's usual behavior.*

> "this works really well for small models short horizon tasks like something like a chatbot. But this is where academic papers kind of end and where you really need to scale things up to start to to see the limitations."
>
> — [12:10](https://www.youtube.com/watch?v=zL1kLftVTlo&t=730s) &middot; *Sets up the talk's real contribution — the scaling failure modes.*

> "at trajectory we've been scaling up this algorithm to 120bs to 500 bs to one trillion parameter models. And as soon as you get to the 120B range with not just one or two tool calls but 50 or 100 well things start to break apart a little bit."
>
> — [12:10](https://www.youtube.com/watch?v=zL1kLftVTlo&t=730s) &middot; *Concrete scale numbers and the exact point of breakdown.*

> "the teacher model just continuously trying to improve this token of wait or maybe or some of these kind of hedging words"
>
> — [13:28](https://www.youtube.com/watch?v=zL1kLftVTlo&t=808s) &middot; *Names the failure mode that gives the 'wait' problem its name.*

> "not just like normal KL where we use that as a KL penalty, but instead we're actually multiplying the token weight of every single step based on this divergence property."
>
> — [14:45](https://www.youtube.com/watch?v=zL1kLftVTlo&t=885s) &middot; *The specific technical distinction of his first fix.*

> "with RL the number one problem that people face is reward hacking as you guys are are all aware of and that's a game that continuously RL researchers have had to play. Well there is an equivalent for OPSD as well and that is hint leakage."
>
> — [15:28](https://www.youtube.com/watch?v=zL1kLftVTlo&t=928s) &middot; *The talk's most transferable warning — every method has its exploit.*

> "you can have an LLM basically translate that into what is something reasonable that they should have known and that's the process of looking through the logs but not actually giving it the solution that it would shortcut some of its vital reasoning."
>
> — [17:22](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1042s) &middot; *Describes the practical hint-design discipline that makes OPSD workable.*

> "we're actually able to scale this up to a 12b model on mercur apex agents which often requires 100 and or plus tool calls in order to achieve and it's a really powerful algorithm that has even surpassed RL as well."
>
> — [18:38](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1118s) &middot; *The headline result claim, including surpassing RL on long-horizon agents.*

> "there is a really exciting world that is about to come where software in general just gets smarter every single time it's used and that is the most exciting unlock that's going to happen in 2026 2027"
>
> — [19:16](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1156s) &middot; *The dated forecast the talk stakes itself on.*

> "as a research community right now we're in this zone of what I call pseudo continual learning. where there's some still level of like batch updates offline and then re-uploading the model."
>
> — [20:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1250s) &middot; *An honest admission in Q&A that nothing shipped today is truly continual.*

> "the really exciting part is how does the model and the harness interplay with each other as you're both updating them. That's some of the stuff that we're now exploring with our current customers"
>
> — [21:38](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1298s) &middot; *Flags co-evolution of model and harness as open territory.*

## Positions

- Current benchmarks are increasingly expensive and time-consuming to build (4 to 24 hours or several days) while not being tied to real-world AI use cases. ([0:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=50s), confidence: stated)
- A good continual learning algorithm must satisfy four criteria simultaneously: online task distribution, on-policy sampling, parallelism of one, and per-token reward — and no prior method (SFT, DPO/RLHF, GRPO) achieves more than two. ([4:56](https://www.youtube.com/watch?v=zL1kLftVTlo&t=296s), confidence: stated)
- GRPO's requirement of parallel rollouts forces environments to be one-to-one copies of the real world, which introduces bias into the training paradigm. ([2:54](https://www.youtube.com/watch?v=zL1kLftVTlo&t=174s), confidence: stated)
- Giving a model privileged information in its prompt makes it an effective teacher for itself, removing the need for a stronger model to distill from. ([8:27](https://www.youtube.com/watch?v=zL1kLftVTlo&t=507s), confidence: stated)
- GRPO saturates around Sonnet-level performance on LiveCodeBench and does not push the frontier, while OPSD reaches new territory of results. ([10:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=650s), confidence: stated)
- OPSD reduces the number of tokens needed to solve difficult challenges, unlike RL where more expended tokens improve performance. ([11:29](https://www.youtube.com/watch?v=zL1kLftVTlo&t=689s), confidence: stated)
- OPSD degrades at scale: at 120B parameters with 50-100 tool calls, eval accuracy varies widely, run-to-run variance is extremely high, and tool call format errors appear. ([12:49](https://www.youtube.com/watch?v=zL1kLftVTlo&t=769s), confidence: stated)
- On long-horizon tasks the teacher repeatedly course-corrects a divergent student, driving the model into a local optimum dominated by hedging tokens like 'wait', 'but', and 'maybe'. ([13:28](https://www.youtube.com/watch?v=zL1kLftVTlo&t=808s), confidence: stated)
- Hint leakage is the OPSD analogue of reward hacking and requires deliberate hint design, because a leaked answer produces reasoning traces that cannot occur in production. ([16:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1010s), confidence: stated)
- Using an LLM to filter solutions out of hints works decently well but is a trivial solution compared to algorithmic approaches like residual guidance. ([17:22](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1042s), confidence: stated)
- OPSD with these fixes scales to a 12B model on Mercury Apex agents requiring 100+ tool calls and has surpassed RL there. ([18:38](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1118s), confidence: stated)
- Software that gets smarter every time it is used will be the most significant unlock of 2026-2027. ([19:16](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1156s), confidence: stated)
- No one, including Trajectory, is close to true continual learning; the field is doing pseudo continual learning with offline batch updates and model re-uploads. ([20:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1250s), confidence: stated)
- Merging signal from ~10,000 concurrent production rollouts into a single model update is an unsolved infrastructure and algorithmic problem. ([21:38](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1298s), confidence: stated)
- Co-evolution of model and harness during continual learning is completely unexplored territory. ([22:21](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1341s), confidence: stated)

## Concepts

- [benchmark contamination](../concepts/benchmark-contamination.md)
- [benchmark saturation](../concepts/benchmark-saturation.md)
- [continual learning](../concepts/continual-learning.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [post-training](../concepts/post-training.md)
- [reward design](../concepts/reward-design.md)
- [reward hacking](../concepts/reward-hacking.md)
- [tool selection](../concepts/tool-selection.md)

