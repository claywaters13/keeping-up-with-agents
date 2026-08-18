---
title: "Ronak Malde"
type: "speaker"
slug: "ronak-malde"
role: "Co-Founder and CEO"
company: "Trajectory"
talk_count: 1
---

# Ronak Malde

**Co-Founder and CEO &middot; Trajectory**

Co-Founder & CEO of Trajectory.
Previously trained SWE-1 at Windsurf, then gemini post-training at DeepMind after acquisition

[LinkedIn](https://www.linkedin.com/in/ronak-malde)

## Talks

- [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md) (Memory & Continual Learning)

## Scheduled Sessions

- **Scaling up Continual Learning** &middot; Day 3 — Session Day 2 &middot; 11:10am-11:30am &middot; Track 3

## Concepts

- [benchmark contamination](../concepts/benchmark-contamination.md)
- [benchmark saturation](../concepts/benchmark-saturation.md)
- [continual learning](../concepts/continual-learning.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [post-training](../concepts/post-training.md)
- [reward design](../concepts/reward-design.md)
- [reward hacking](../concepts/reward-hacking.md)
- [tool selection](../concepts/tool-selection.md)

## Quotes

> "we are actually spending hundreds of trillions of tokens every single day on inference and we're generating great amounts of data on how models in the real world are are failing, how they're doing well. And that should be signal that we should be capturing and training on."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [1:41](https://www.youtube.com/watch?v=zL1kLftVTlo&t=101s)

> "we are left with a bunch of benchmarks that are getting more time consuming more and more expensive and and perhaps more concerningly they're not tied to real world use cases where people are using AI."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [0:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=50s)

> "we are shoving every single reward into one scaler in order to train on when the real world is messy."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [2:54](https://www.youtube.com/watch?v=zL1kLftVTlo&t=174s)

> "we basically took a Fouian bargain and wanted to max on on policy rollouts which is extremely powerful right we now have models that are capable of amazing things because they are on policy"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [4:56](https://www.youtube.com/watch?v=zL1kLftVTlo&t=296s)

> "imagine you were trying to write an essay and your teacher just gave you a score of 87 out of 100. You would have to run through so many different examples to get to the idea of what a good essay is"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [6:43](https://www.youtube.com/watch?v=zL1kLftVTlo&t=403s)

> "when we're trying to push the frontier we don't magically have some smarter model, right?"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [7:52](https://www.youtube.com/watch?v=zL1kLftVTlo&t=472s)

> "You take what's called this hint, put it into the beginning of the prompt, and now you match the log props of the student without that hint to the teacher with that hint. And this is an extremely powerful algorithm."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [8:27](https://www.youtube.com/watch?v=zL1kLftVTlo&t=507s)

> "now there's no parallel rollouts. We don't need a group of eight in order to roll out but just from a single example we're able to get information. So that takes away the environment bottleneck"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [9:40](https://www.youtube.com/watch?v=zL1kLftVTlo&t=580s)

> "we're not just taking now a distribution like RL and slightly sharpening it, but we're instead actually shifting entire distributions."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [10:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=650s)

> "If you take a look at live codebench actually we found that gpo saturates around sonnet level performance and and doesn't really push the frontier"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [10:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=650s)

> "with RL a fundamental limitation and if you guys have ever trained RL models is the models like to think a lot right the more tokens that you expend it's it's just going to do better but with opsd you don't have that problem"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [11:29](https://www.youtube.com/watch?v=zL1kLftVTlo&t=689s)

> "this works really well for small models short horizon tasks like something like a chatbot. But this is where academic papers kind of end and where you really need to scale things up to start to to see the limitations."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [12:10](https://www.youtube.com/watch?v=zL1kLftVTlo&t=730s)

> "at trajectory we've been scaling up this algorithm to 120bs to 500 bs to one trillion parameter models. And as soon as you get to the 120B range with not just one or two tool calls but 50 or 100 well things start to break apart a little bit."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [12:10](https://www.youtube.com/watch?v=zL1kLftVTlo&t=730s)

> "the teacher model just continuously trying to improve this token of wait or maybe or some of these kind of hedging words"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [13:28](https://www.youtube.com/watch?v=zL1kLftVTlo&t=808s)

> "not just like normal KL where we use that as a KL penalty, but instead we're actually multiplying the token weight of every single step based on this divergence property."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [14:45](https://www.youtube.com/watch?v=zL1kLftVTlo&t=885s)

> "with RL the number one problem that people face is reward hacking as you guys are are all aware of and that's a game that continuously RL researchers have had to play. Well there is an equivalent for OPSD as well and that is hint leakage."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [15:28](https://www.youtube.com/watch?v=zL1kLftVTlo&t=928s)

> "you can have an LLM basically translate that into what is something reasonable that they should have known and that's the process of looking through the logs but not actually giving it the solution that it would shortcut some of its vital reasoning."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [17:22](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1042s)

> "we're actually able to scale this up to a 12b model on mercur apex agents which often requires 100 and or plus tool calls in order to achieve and it's a really powerful algorithm that has even surpassed RL as well."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [18:38](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1118s)

> "there is a really exciting world that is about to come where software in general just gets smarter every single time it's used and that is the most exciting unlock that's going to happen in 2026 2027"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [19:16](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1156s)

> "as a research community right now we're in this zone of what I call pseudo continual learning. where there's some still level of like batch updates offline and then re-uploading the model."
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [20:50](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1250s)

> "the really exciting part is how does the model and the harness interplay with each other as you're both updating them. That's some of the stuff that we're now exploring with our current customers"
>
> — [Scaling up Continual Learning](../talks/scaling-up-continual-learning.md), [21:38](https://www.youtube.com/watch?v=zL1kLftVTlo&t=1298s)

