---
title: "Raymond Feng"
type: "speaker"
slug: "raymond-feng"
role: "Researcher"
company: "Applied Compute"
talk_count: 1
---

# Raymond Feng

**Researcher &middot; Applied Compute**

Researcher at Applied Compute. Building the post-training stack, training specialized workhorse models for enterprises, and researching new techniques for model customization. Graduated from MIT.

## Talks

- [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md) (Posttraining & Midtraining)

## Scheduled Sessions

- **Learning on the job: the future of post-training** &middot; Day 3 — Session Day 2 &middot; 12:05pm-12:25pm &middot; Track 9

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [continual learning](../concepts/continual-learning.md)
- [knowledge distillation](../concepts/knowledge-distillation.md)
- [post-training](../concepts/post-training.md)
- [reward hacking](../concepts/reward-hacking.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [simulation environments](../concepts/simulation-environments.md)

## Quotes

> "The key thing to note here is that the only thing you need for improving your model is the graded chats in some format, and once you have those, the training engine can compute weight updates to improve your model."
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [3:26](https://www.youtube.com/watch?v=k35LeKZEhiE&t=206s)

> "the main sort of method that we use for reinforcement learning today is GRPO, and that involves comparing many rollouts for the same prompt"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [6:14](https://www.youtube.com/watch?v=k35LeKZEhiE&t=374s)

> "And the main sort of problem is like has kind of two names, which are both the same problem, environment fidelity and reward hacking."
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [7:03](https://www.youtube.com/watch?v=k35LeKZEhiE&t=423s)

> "we had some like networking issues causing our environment to have tool calls that failed maybe around 10% of the time. If that is the case, then we actually saw that the model would then start outputting shorter and shorter responses."
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [7:03](https://www.youtube.com/watch?v=k35LeKZEhiE&t=423s)

> "if you think about maybe the model is like a human like walking along a sidewalk and like the tool call failures are like potholes in the sidewalk"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [7:46](https://www.youtube.com/watch?v=k35LeKZEhiE&t=466s)

> "if the model feels like the problem is really hard, it will actually just be incentivized to like abuse the tool calls and just like call a lot of them in quick succession and try to time out the sandbox so it avoids getting a reward of zero"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [8:25](https://www.youtube.com/watch?v=k35LeKZEhiE&t=505s)

> "it's very, very difficult to like perfectly simulate reality and sort of any mistake that you make, even if it's not intentional, will end up inducing these like subtle undesirable behaviors in your model"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [8:25](https://www.youtube.com/watch?v=k35LeKZEhiE&t=505s)

> "if the agent learns the exact environment distribution, why don't we just use that for our training?"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [9:21](https://www.youtube.com/watch?v=k35LeKZEhiE&t=561s)

> "The only thing we have left is the model completion endpoint and some way to uh record the requests and responses that go in and out of the model."
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [9:21](https://www.youtube.com/watch?v=k35LeKZEhiE&t=561s)

> "essentially the reason this is nice is because we can meet customers where they're at"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [10:01](https://www.youtube.com/watch?v=k35LeKZEhiE&t=601s)

> "some challenges we face in this setting are non-re-playability and offline or off-policy data. I think both of these are describing the same issue"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [11:37](https://www.youtube.com/watch?v=k35LeKZEhiE&t=697s)

> "there's not really a way that you could then go back and think, "Oh, if I like said or if I responded in this other way, like would the user have been happier?""
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [12:21](https://www.youtube.com/watch?v=k35LeKZEhiE&t=741s)

> "But, we're optimistic because like we think that humans can do this kind of learning, and so it should be possible to like formulate some kind of method that would work for models as well."
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [12:21](https://www.youtube.com/watch?v=k35LeKZEhiE&t=741s)

> "There's kind of three main topics, which are self-distillation, automated data pipelines, and qualitative feedback ingestion."
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [13:04](https://www.youtube.com/watch?v=k35LeKZEhiE&t=784s)

> "Currently, this is like pretty manual or like human in the loop, where like we go through traces ourselves"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [13:52](https://www.youtube.com/watch?v=k35LeKZEhiE&t=832s)

> "as you move to these like production settings, sometimes you don't have access to like a clear-cut binary grade or like a numerical grade"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [14:37](https://www.youtube.com/watch?v=k35LeKZEhiE&t=877s)

> "what if like the environment was just like every interaction that the agent ever has?"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [16:10](https://www.youtube.com/watch?v=k35LeKZEhiE&t=970s)

> "you're kind of playing a game of Whac-A-Mole where as soon as a new thing pops up, you need to scramble and like create new data or new environments and improve the model that way"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [16:10](https://www.youtube.com/watch?v=k35LeKZEhiE&t=970s)

> "AI is at the cusp of a new period in which experience will become the dominant medium of improvement and ultimately dwarf the scale of human data used in today's systems"
>
> — [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [17:09](https://www.youtube.com/watch?v=k35LeKZEhiE&t=1029s)

