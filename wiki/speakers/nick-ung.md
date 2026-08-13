---
title: "Nick Ung"
type: "speaker"
slug: "nick-ung"
talk_count: 1
---

# Nick Ung

## Talks

- [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md) (co-presented)

## Concepts

- [continual learning](../concepts/continual-learning.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [online evaluation](../concepts/online-evaluation.md)
- [rubric design](../concepts/rubric-design.md)
- [simulation environments](../concepts/simulation-environments.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "the real imperative here really is that it we don't want to use our live user as, you know, test data for our AI agents"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [4:23](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=263s)

> "If your LM as a judge is just floating out there, that there's a score, but no one is really using that score as a meaningful gate uh for your development and production environment, then that LM as a judge is not not available."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [6:04](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=364s)

> "in our first pass at running our offline evaluation, what we noticed is that our LM user sounds almost too nice"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [13:40](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=820s)

> "our first attempt at our offline evaluation gave us 90 plus pass rate or accuracy rate, right? Uh this almost sounds too good to be true, and I think it indeed is the too good to be true."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [13:40](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=820s)

> "most user, they are they're impatient, they're already frustrated. So, the verbatim they they they they don't want to explain their issues like a l- LM user well."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [14:27](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=867s)

> "we fine-tune a LLM model with Lyft user verbatim"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [14:27](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=867s)

> "If you have an eval that's too easy, that doesn't give you any real uh, production insights into how your AI agent is actually going to perform."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [15:30](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=930s)

> "They fine-tune a uh, user LLM model until evaluation score goes down."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [16:55](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1015s)

> "the problem with this approach is uh that these metrics are too generic and not actionable"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [17:54](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1074s)

> "If something if let's say a response helpfulness is 0.5, then what do we do with it?"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [18:47](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1127s)

> "we can use these pre-built eval metrics as a baseline, but we shouldn't use them as our core eval metrics because we want eval metrics to be actionable and tied to the business outcome"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [18:47](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1127s)

> "eval should be framed around a task success or failure. And a binary outcome is very easy to calibrate and train um LLM judge that can consistently score your agent trajectory."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [19:32](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1172s)

> "we can hand label around 100 examples with pass fail labels and then split the data into train, dev, and validation sets like how we used to do with machine learning models"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [21:17](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1277s)

> "we are not actually training models. So, we are just using the data to inform judges prompt."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [22:09](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1329s)

> "The key idea is that we actually discover what our evaluation criteria is by looking at the data and grading our outputs."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [23:02](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1382s)

> "We cannot define the criteria beforehand and then evaluate agents against them."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [24:05](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1445s)

> "every score needs an interval"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [25:01](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1501s)

> "If you don't look at the data, you won't be able to create meaningful criteria uh or labels. And if you don't have labels, you won't be able to evaluate your judges. And if you're not evaluating your judges, you don't know if your uh agentic pipeline is working as as expected."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [26:58](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1618s)

> "it is important to know that this loop is something which runs continuously. It's not uh not a one-off audit."
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [27:42](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=1662s)

> "our eval harness is config driven and these are typically stored as YAML file that's easily editable by different contributor and not just by engineers"
>
> — [Build Evals That Actually Matter](../talks/build-evals-that-actually-matter.md), [34:42](https://www.youtube.com/watch?v=3z2uT5aDx_Y&t=2082s)

