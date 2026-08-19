---
title: "Samuel Denton"
type: "speaker"
slug: "samuel-denton"
role: "Platform Research Lead"
company: "Applied Compute"
talk_count: 1
---

# Samuel Denton

**Platform Research Lead &middot; Applied Compute**

Leading Platform Research at Applied Compute — focused primarily on continual learning, context, synthetic users/tasks, and more around our RL stack. Previously at Scale AI and Amazon.

[LinkedIn](https://www.linkedin.com/in/sam-denton-161b50126/)

## Talks

- [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md) (Memory & Continual Learning)

## Scheduled Sessions

- **Bringing Continual Learning into Enterprises** &middot; Day 3 — Session Day 2 &middot; 2:25pm-2:45pm &middot; Track 3

## Concepts

- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [continual learning](../concepts/continual-learning.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [post-training](../concepts/post-training.md)
- [production trace mining](../concepts/production-trace-mining.md)

## Quotes

> "you get a single batch of traces from a production agent, and you're meant to just do something with it"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [1:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=80s)

> "this is sort of the holy grail of continual learning where I have a model that's serving production traffic, it does a rollout, it creates a trace, we figure out how to learn from that trace, we update the model, and then we serve the next production request"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [1:56](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=116s)

> "our goal at Applied Compute is to meet enterprises where they are, right? So, they're across this spectrum and we want to provide value across both ends of the spectrum."
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [3:08](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=188s)

> "in order to create a teacher that's smarter than this on-policy model, we need to create some kind of hint or have some kind of privileged information"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [3:46](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=226s)

> "we don't actually have to have replayability of a production environment"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [7:40](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=460s)

> "We can improve for free today by using offline production traces. Give us a dump of your production data. We'll find a way to make it valuable."
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [9:05](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=545s)

> "a lot of distillation work is done assuming you have some kind of golden answer that you can distill into the model. And this is often not the case."
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [9:47](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=587s)

> "we want to think about how we can do continual learning and distillation without having some beautifully golden rubric to accompany every task"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [9:47](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=587s)

> "on SWE-bench, we found that this model was essentially taking like up to 80 turns to submit its answer. What we wanted to do was encourage it to call a tool to submit its task before turn 40."
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [10:56](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=656s)

> "the task complete call rate increases dramatically from about 22% to 60%"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [12:39](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=759s)

> "the teacher doesn't force the tool call. It just starts to force the the reasoning path towards the tool call without ever actually changing the tool call."
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s)

> "you can roll out just one step from the on policy model given an offline production trace"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [13:20](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=800s)

> "even doing SFT on traces where we knew the hyperlink was correctly formatted, we saw that there was this sort of degradation in overall coding agent performance"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [14:35](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=875s)

> "the percentage of correct hyperlink formatting jumped drastically from about, I guess, 15% all the way up to around 80%"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [15:21](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=921s)

> "you can see that we do climb the behavior a little bit, but far less than in this online hinting world"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [15:21](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=921s)

> "rather than injecting a hint to the beginning of a rollout, we use a judge to essentially decide where in the rollout we should be injecting hints"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [15:53](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=953s)

> "it's best to just do distillation on that next step that occurs or maybe a few steps forward rather than the entire rollout"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [16:31](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=991s)

> "often, we'll see that the teacher model has preferences of certain connector words that are not really relevant to actually what we're trying to teach the student"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [17:05](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=1025s)

> "we use offline hinting with offline production traces to provide value on day one to enterprise clients. Give us production traces and we can teach you a certain behavior."
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [17:48](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=1068s)

> "because that judge is able to adapt to whatever the online model does in production"
>
> — [Bringing Continual Learning into Enterprises](../talks/bringing-continual-learning-into-enterprises.md), [17:48](https://www.youtube.com/watch?v=ZTA0GwpAUak&t=1068s)

