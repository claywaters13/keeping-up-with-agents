---
title: "Tanay Varshney"
type: "speaker"
slug: "tanay-varshney"
role: "Principal Engineer"
company: "NVIDIA"
talk_count: 1
---

# Tanay Varshney

**Principal Engineer &middot; NVIDIA**

Tanay Varshney is a principal engineer at NVIDIA working on NeMotron models, NeMo Platform and LLM inference architecture at NVIDIA.

[LinkedIn](https://www.linkedin.com/in/tanayvarshney)

## Talks

- [The State of Model Routing](../talks/the-state-of-model-routing.md) (Local AI, co-presented)

## Scheduled Sessions

- **Model Routing** &middot; Day 4 — Session Day 3 &middot; 3:20pm-3:40pm &middot; Track 4
- **Model Routing** &middot; Day 4 — Session Day 3 &middot; 3:45pm-4:05pm &middot; Track 4

## Concepts

- [context compaction](../concepts/context-compaction.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [local inference](../concepts/local-inference.md)
- [model routing](../concepts/model-routing.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "we're reducing the cost of Fable level intelligence by 40%. The way we do that is we allow Fable to still do like the planning and the the hard decision making but delegate a lot of the work to an implementation model."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [4:32](https://www.youtube.com/watch?v=QHBjufYK8TA&t=272s)

> "I think actually there's this really unintuitive dynamic where smarter models actually get better and better at delegating work."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [3:53](https://www.youtube.com/watch?v=QHBjufYK8TA&t=233s)

> "this kind of like naive like initial routing to based on the task type is extremely fragile, especially the more agentic the task you you work on is."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [9:02](https://www.youtube.com/watch?v=QHBjufYK8TA&t=542s)

> "routing is a task of intimately intimately understanding of behavior of and strengths and weaknesses of different models, and then applying them thusly, right?"
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [6:26](https://www.youtube.com/watch?v=QHBjufYK8TA&t=386s)

> "if you use these techniques, you can get like up to 10% higher accuracy even, right? It depends on the model pool. Depends on the task at hand."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [8:27](https://www.youtube.com/watch?v=QHBjufYK8TA&t=507s)

> "overall, just the guarantee of always having frontier intelligence present, I think reduces the the fragility of of these systems quite a lot."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [10:14](https://www.youtube.com/watch?v=QHBjufYK8TA&t=614s)

> "you can use small models pretty easily and get a cost savings but if it's out of distribution small models may actually increase your cost because of how often they'll like call tools and how crazy their loops will be."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [14:05](https://www.youtube.com/watch?v=QHBjufYK8TA&t=845s)

> "Like if you run terminal bench on Opus and Haiku, like Opus will do about three times better at 1/10 the cost of Haiku, even though Haiku's significantly cheaper per token."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [15:25](https://www.youtube.com/watch?v=QHBjufYK8TA&t=925s)

> "we don't use sub agents. We use what we call a sidekick, which is um, one sub agent that continually has a running context. So the main agent doesn't need to re-provide uh, context from earlier."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [18:04](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1084s)

> "don't just like take models as they are and orchestrate them, but like can you actually co-design your models with the orchestration system?"
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [19:13](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1153s)

> "It's not obvious that actually more expensive models are actually creating an overall cheaper system."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [23:41](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1421s)

> "we've had a an auto router for like 2 years almost. Um but when we launched it, there was like no adoption of it. It was people really wanted to use specific models."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [26:31](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1591s)

> "at around like January this year with open claw, it exploded. And the reason it exploded is because there's this fundamental um idiosyncrasy in open claw where it sends heartbeats every like 10 minutes to your model of choice"
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [27:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1623s)

> "you're actually then now like paying 10 times as much for the for those input tokens if you didn't compact. Um the main reason we compact is actually intelligence."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s)

> "I would like never recommend using like these models past like 200K tokens, under 100K if you can."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s)

> "the 5-minute uh window is what a lot of providers right now put, but that's uh that's that's more an operational operational operational determination rather than a like a science-based or like a core physics law determination."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [34:46](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2086s)

> "If you self-host, you can optimize specifically for your use, and you'll likely pay much less."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [35:37](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2137s)

> "we actually bought direct compute capacity from these providers, and instead of paying on a per-token basis, we just paid for the underlying compute, knowing that the economics of the compute was that we were actually paying far less for for the cash tokens that we'd send over."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [36:27](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2187s)

> "I'm actually personally less bullish on these kind of like low level mechanical prompt tuning harnesses versus just telling like a smart model like here is the decision that was made and the context figure out why it went wrong."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [42:07](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2527s)

> "There's not going to be a thing as like a really great harness that is in absence of a really great model and vice versa."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [44:25](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2665s)

