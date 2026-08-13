---
title: "Eugene Yan"
type: "speaker"
slug: "eugene-yan"
role: "Member of Technical Staff"
company: "Anthropic"
talk_count: 1
---

# Eugene Yan

**Member of Technical Staff &middot; Anthropic**

Eugene Yan is a Member of Technical Staff at Anthropic, where he works on safe and reliable AI systems at scale. He previously led ML/AI teams at Amazon, Alibaba, Lazada, and a healthtech Series A, and writes about LLMs, recommender systems, and engineering.

## Talks

- [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md) (Security)

## Scheduled Sessions

- **Using LLMs to Secure Source Code** &middot; Day 2 — Session Day 1 &middot; 1:30pm-1:50pm &middot; Track 5

## Concepts

- [adversarial agent supervision](../concepts/adversarial-agent-supervision.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [ai-assisted vulnerability discovery](../concepts/ai-assisted-vulnerability-discovery.md)
- [context engineering](../concepts/context-engineering.md)
- [legacy code migration](../concepts/legacy-code-migration.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [retrieval evaluation](../concepts/retrieval-evaluation.md)

## Quotes

> "We shared our observation that finding vulnerabilities now is quite straightforward. The bottleneck has now shifted to verification, triage, and patching."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [3:11](https://www.youtube.com/watch?v=imFedndyXYQ&t=191s)

> "So what this means is that what's happened in April is 20x of last year's average."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [1:49](https://www.youtube.com/watch?v=imFedndyXYQ&t=109s)

> "they attributed about twothirds of this to mess preview about 271 which shows that frontier models can help defenders like yourself find and fix vulnerabilities at scale"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [1:49](https://www.youtube.com/watch?v=imFedndyXYQ&t=109s)

> "from 23,000 candidates uh 6,200 of them were rated as high or critical and at the time of the update 1,600 of them were reported to maintainers and about 100 patch upstream"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [3:11](https://www.youtube.com/watch?v=imFedndyXYQ&t=191s)

> "Early experiments showed that some promise, but the high rates of false positives made it impractical to scale. But the introduction of agentic harnesses that can reliably detect security issues has changed this."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [3:58](https://www.youtube.com/watch?v=imFedndyXYQ&t=238s)

> "having a well doumented thread model really increases your true positive rate to 90%"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [5:48](https://www.youtube.com/watch?v=imFedndyXYQ&t=348s)

> "the model has great context of the code but poor context of the system"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [5:48](https://www.youtube.com/watch?v=imFedndyXYQ&t=348s)

> "the biggest lever we had is having the model test beds essentially sandboxes with live systems and where they can run and detonate the pox to confirm that they are true positives"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [8:38](https://www.youtube.com/watch?v=imFedndyXYQ&t=518s)

> "That's what I found with every new model version of StepJum, I actually have to cut my prompt size by maybe about 50%."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [9:51](https://www.youtube.com/watch?v=imFedndyXYQ&t=591s)

> "for newer models you can just probably say something like look for where untrusted data hits the trust boundary and the model is very good at inferring this"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [9:51](https://www.youtube.com/watch?v=imFedndyXYQ&t=591s)

> "A lot of times you expect the model to just read the code. That doesn't quite work."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [10:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=631s)

> "And when they did this, their true positive rate was almost 100%, because the model could actually verify in the loop."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [10:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=631s)

> "when the discovery agent is trying to verify its own work in the loop, trying to debate against itself in the loop, it may actually self censor and this may actually hurt recall"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [11:46](https://www.youtube.com/watch?v=imFedndyXYQ&t=706s)

> "Independent means that the verification agent doesn't see the reasoning traces, doesn't see all the work that the discovery agent has done."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [11:46](https://www.youtube.com/watch?v=imFedndyXYQ&t=706s)

> "you can lose trust with product engineers by sending them all the vulnerabilities that are true, even those that are medium or low severity because those engineers can't cope. And as we've seen so many times, the scars resource now is engineer attention."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [13:19](https://www.youtube.com/watch?v=imFedndyXYQ&t=799s)

> "first the original PC has to stop working that's basic second the existing test suite should stay green no regression"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [15:43](https://www.youtube.com/watch?v=imFedndyXYQ&t=943s)

> "when you're building the building harnesses, right? You're building loops. They're operational expense, but when you close the loop, they now become capital expense. You get better with each iteration you run."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [16:50](https://www.youtube.com/watch?v=imFedndyXYQ&t=1010s)

> "non-technical problems are an order of magnitude harder than technical problems"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [17:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=1051s)

> "You spend more compute. You pay more money. Things that can be solved with money are not really problems."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [17:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=1051s)

> "But human attention doesn't scale. Your deaf, your product engineers and your security engineers, what if they don't agree on what high severity or uh critical severity is?"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [18:14](https://www.youtube.com/watch?v=imFedndyXYQ&t=1094s)

> "Don't try to aim for automation immediately. Right? Start interactively. Do it hands on the wheel with uh claw code or your favorite ID."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [20:09](https://www.youtube.com/watch?v=imFedndyXYQ&t=1209s)

