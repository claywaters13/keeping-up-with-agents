---
title: "Robert McHardy"
type: "speaker"
slug: "robert-mchardy"
role: "Pre-training Lead"
company: "poolside"
talk_count: 1
---

# Robert McHardy

**Pre-training Lead &middot; poolside**

Team and tech lead for pre-training at poolside, where he trains large language models for code. Recently led the pre-training of Laguna XS.2 and M.1, poolside's first two public open-weight models. Before that, Robert worked as a Senior Researcher at AssemblyAI where he trained multilingual speech models, and previously built AI for cancer and infectious-disease research at InstaDeep and BioNTech's joint lab. MSc in Machine Learning from UCL.

[LinkedIn](https://www.linkedin.com/in/robert-mchardy)

## Talks

- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md) (Data Quality, co-presented)

## Scheduled Sessions

- **The Messy Reality of Scale: Synthetic Data and Pre-Training at Poolside** &middot; Day 2 — Session Day 1 &middot; 11:10am-11:30am &middot; Track 9

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [quantization](../concepts/quantization.md)
- [synthetic data generation](../concepts/synthetic-data-generation.md)
- [task decomposition](../concepts/task-decomposition.md)
- [token efficiency](../concepts/token-efficiency.md)

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "at least at Pulsar we don't see it as a way to replace organic data"
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [2:10](https://www.youtube.com/watch?v=KhYifX22yhE&t=130s)

> "organic data has a lot in it that is basically kind of implicitly hidden. A lot of things that could teach the model or not very presented in the most optimal way sometimes."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [2:10](https://www.youtube.com/watch?v=KhYifX22yhE&t=130s)

> "for access point two in particular, we settled on 13% of the mix. This is only pre-training stages before post-training."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [2:44](https://www.youtube.com/watch?v=KhYifX22yhE&t=164s)

> "Now we have a six trillion token uh corpus that's continuously growing."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [2:44](https://www.youtube.com/watch?v=KhYifX22yhE&t=164s)

> "we were basically focusing on quality versus quantity um maybe a little too much"
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [3:21](https://www.youtube.com/watch?v=KhYifX22yhE&t=201s)

> "we started hitting repetition uh like non-optimal repetition on some of our high-quality data which saturated the model a little too early"
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [3:21](https://www.youtube.com/watch?v=KhYifX22yhE&t=201s)

> "the rule of thumb is if task is too hard for your model, then your model will start to fall on its face. Lose correctness, lose diversity. So break down the task, make it simpler."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [5:58](https://www.youtube.com/watch?v=KhYifX22yhE&t=358s)

> "And then and then from there go into generate the chapters one by one. You will absolutely get a better novel."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [6:37](https://www.youtube.com/watch?v=KhYifX22yhE&t=397s)

> "If you've got data that sucks, you can't train a good model. If you've got a training code base that sucks, you also can't."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [8:57](https://www.youtube.com/watch?v=KhYifX22yhE&t=537s)

> "the way we we look at things in my team is uh we don't trust anything. There's so many things that can go wrong when you scale models to billions of parameters to hundreds of billions of parameters um training on thousands of GPUs and so on."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [9:31](https://www.youtube.com/watch?v=KhYifX22yhE&t=571s)

> "If they're not identical, we know something has gone seriously wrong uh because that should never happen. And we crash the training."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [10:07](https://www.youtube.com/watch?v=KhYifX22yhE&t=607s)

> "They're exactly the same run. Just in one of them we were got unlucky and we had a broken GPU included."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [10:34](https://www.youtube.com/watch?v=KhYifX22yhE&t=634s)

> "That broken GPU caused silent data corruption and um therefore made the training behave the way it did."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [11:09](https://www.youtube.com/watch?v=KhYifX22yhE&t=669s)

> "we have to perform some sort of accumulation here uh because we use tensor parallel for the uh unembedding. And that accumulation um was performed in BF16 by default."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [11:42](https://www.youtube.com/watch?v=KhYifX22yhE&t=702s)

> "We moved that accumulation into FP32 and from there on the model started converging again."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [12:21](https://www.youtube.com/watch?v=KhYifX22yhE&t=741s)

> "with Laguna S we scaled this to a model that's 118 billion uh total parameters and 8B active parameters. Again, we trained it on 30 trillion tokens on 4,000 GPUs."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [13:24](https://www.youtube.com/watch?v=KhYifX22yhE&t=804s)

> "we had a race condition because we added FP8 training uh based on Deep Chem FP8 kernels that are also like open source"
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [13:56](https://www.youtube.com/watch?v=KhYifX22yhE&t=836s)

> "in our case, we noticed about 0.5% of the gradient gets silently corrupted, essentially replaced by random values"
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [13:56](https://www.youtube.com/watch?v=KhYifX22yhE&t=836s)

> "In real training runs, you don't have any redundancy where you have the same model weights and the same data, so you can never check if forward and backward actually behave the same across different model replicas."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [14:32](https://www.youtube.com/watch?v=KhYifX22yhE&t=872s)

> "these are base model evals, right? They are partly indicative of how the final model will look, but also not perfectly, right?"
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [15:02](https://www.youtube.com/watch?v=KhYifX22yhE&t=902s)

> "MMLU pro knowledge benchmark is something we don't care about that much compared to coding because we want to build the strongest agentic coding models"
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [16:20](https://www.youtube.com/watch?v=KhYifX22yhE&t=980s)

> "The recipe held, it scaled, and we will continue scaling it from here."
>
> — [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [16:49](https://www.youtube.com/watch?v=KhYifX22yhE&t=1009s)

