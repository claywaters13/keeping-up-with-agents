---
title: "Soheil Feizi"
type: "speaker"
slug: "soheil-feizi"
talk_count: 1
---

# Soheil Feizi

## Talks

- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [continual learning](../concepts/continual-learning.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [post-training](../concepts/post-training.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)

## Quotes

> "Humans learn mainly from experience by interacting with the world and getting feedback. The goal of continual learning is to imitate the same for agents. So they can also learn from experience by acting, getting feedback, and improving without forgetting."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [0:01](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1s)

> "But in production, we don't have such benchmark. We have logs."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [2:26](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=146s)

> "Here we have log and feedback, but what we really need is a replayable learning environment, a simulation that we can rerun with defined grading on what success looks like, not one instance of what happened and the feedback on top of it."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [3:57](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=237s)

> "But a good learning is not going to be focusing on any of these components exclusively. A good learning engine should ask for the smallest durable change at the right layer of the agent."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [6:22](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=382s)

> "But these methods, they usually need benchmarks and explicit evaluators. They cannot be directly applied on, let's say, if you have a log and feedback, unless we turn those into uh replayable learning environments."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [8:04](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=484s)

> "So, this works on uh the case where we have log and feedback, but it is wipe-based. We don't know if even for that particular uh sample, if the change is effective, because it is not testable."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [8:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=536s)

> "What uh might have been working previously, but with these changes might not work properly, and create some hidden regressions."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [8:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=536s)

> "So, this layer in terms of the update is cheapest and fastest. It works directly on the cases where you only have log and feedback, but usually it is unverified"
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [9:50](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=590s)

> "the goal is to improve an agent from its his own experience where every fix is proven to help and proven to break nothing that already worked"
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [11:01](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=661s)

> "One failure may have several causes and several possible repairs."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [11:44](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=704s)

> "A better approach is a regression aware learning where the regression is not be treated as a post-hoc approach, but as a mechanism within the optimization itself."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [13:19](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=799s)

> "So, here we are uh fixing the recent failures subject to having no regression on the past uh learning environments."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [14:09](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=849s)

> "So, sometimes the change can be cheap, like for example, writing something in the memory can be medium in terms of the complexity by changing the prompt or hardness, and sometimes it can be very expensive by changing the weights of the model."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [14:09](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=849s)

> "So, we have deterministic evaluators and we also build this benchmark in a way that it has some regression trap."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [18:03](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1083s)

> "It is 78% and in particular, there are two um, evaluators that uh, basically show very low scores uh, of agent in this environment."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [19:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1196s)

> "Uh, it is 10% improvement on average just with one loop and score increases to 97% from 87%."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [19:56](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1196s)

> "This is verifiable continual learning in practice, where each update is tested, every gain is measured, and nothing that already works breaks during this optimization."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [20:46](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1246s)

> "The first one is agent continual learning is not necessarily model fine-tuning. The updates and many useful updates can happen in the harness and memory layer."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s)

> "So, the second takeaway is production logs are not learning environments."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s)

> "And the third takeaway is that the frontier is regression-aware continual improvement, where when fixing the new failure, we verify that we don't forget the old ones."
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [21:31](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=1291s)

