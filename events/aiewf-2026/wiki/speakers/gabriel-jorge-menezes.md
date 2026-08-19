---
title: "Gabriel Jorge Menezes"
type: "speaker"
slug: "gabriel-jorge-menezes"
role: "Core Infrastructure Engineer"
company: "Krea.ai"
talk_count: 1
---

# Gabriel Jorge Menezes

**Core Infrastructure Engineer &middot; Krea.ai**

Infrastructure and performance engineer at Krea. creating, managing and improving infrastructure for trainings and inference.

[LinkedIn](https://www.linkedin.com/in/gabriel-jorge-menezes/)

## Talks

- [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md) (Generative Media)

## Scheduled Sessions

- **Infra behind Krea 2 - How to train and serve at scale** &middot; Day 4 — Session Day 3 &middot; 2:50pm-3:10pm &middot; Track 1

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [durable execution](../concepts/durable-execution.md)
- [scaling laws](../concepts/scaling-laws.md)

## Quotes

> "the whole idea about training this model was because we were kind of bored of AI images. They're quite, you know, soulless. They have no spice."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [0:01](https://www.youtube.com/watch?v=byn9PURoBNY&t=1s)

> "the whole idea was to like kind of bridge the gap between like LLM research and diffusion transformers. Uh, so my AI researchers they ported a lot of research from LLMs into into DiTs."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [2:02](https://www.youtube.com/watch?v=byn9PURoBNY&t=122s)

> "the whole like like the whole like architecture of the model was meant to be extremely extremely simple. And so like it is very very dumb, but like very effective."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [2:37](https://www.youtube.com/watch?v=byn9PURoBNY&t=157s)

> "we learned that like sometimes you just let it crash. It crashes, like it runs for like an hour, crash, runs for an hour, crash, and then runs again on the same set of machines, same code, same data for like 12 hours, 16 hours, 24 hours."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [3:18](https://www.youtube.com/watch?v=byn9PURoBNY&t=198s)

> "you can imagine doing large-scale pre-training on runs that last less than 8 hours, it is a problem, right? You want kept those GPUs fed and if things are crashing, you are not doing progress and losing time and models are going to be late."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [3:49](https://www.youtube.com/watch?v=byn9PURoBNY&t=229s)

> "Metrics are everything. That's how I can support my researchers. That's how I have visibility in the system. And like if you're doing large-scale pre-training, I highly highly recommend for you to invest heavily on metrics."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [4:25](https://www.youtube.com/watch?v=byn9PURoBNY&t=265s)

> "So for us it was like if there is any GPUs above like 78°, you you remove them. Don't don't think about it. Don't try to fix. Don't don't try to be smart. You just remove the GPU."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [4:59](https://www.youtube.com/watch?v=byn9PURoBNY&t=299s)

> "there is GPU utilization which is a lie. Uh, don't trust this. Uh, this is dumb."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [4:59](https://www.youtube.com/watch?v=byn9PURoBNY&t=299s)

> "What we would use uh, as a proxy was tensor core utilization. This is actually how how much of a tensor core you're using and like how effective they are being."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [5:32](https://www.youtube.com/watch?v=byn9PURoBNY&t=332s)

> "if you're doing large-scale pre-training with a bunch of GPUs talking to each other between machines and you have no InfiniBand metrics, you're doing something wrong."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [6:01](https://www.youtube.com/watch?v=byn9PURoBNY&t=361s)

> "These was probably the most important stuff for us because most of our failures were like related to like cross-node communication."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [6:39](https://www.youtube.com/watch?v=byn9PURoBNY&t=399s)

> "At the beginning we use SEF. SEF didn't work well. Was very annoying. It broke. We lost trust in data. So, I recommend if if you have the money go go with something paid and cuz you can trust your data."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [7:42](https://www.youtube.com/watch?v=byn9PURoBNY&t=462s)

> "We can do like 1.8 terabytes of second of reads, almost a terabyte of writes. And the file system would not choke on the training. So, we could checkpoint every like 30 minutes, 20 minutes, produce like a terabyte of data in like less than 30 seconds."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [8:17](https://www.youtube.com/watch?v=byn9PURoBNY&t=497s)

> "I just want them to launch stuff and this goes into a queue and if we have GPUs we have GPUs. If we don't have GPUs we don't have GPUs."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [8:54](https://www.youtube.com/watch?v=byn9PURoBNY&t=534s)

> "If there's inference running on those machines, the inference gets kicked out. And you'd say, "Oh, this is bad. Production is going to go down." No, you can build on top of that to to make production not go down"
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [9:30](https://www.youtube.com/watch?v=byn9PURoBNY&t=570s)

> "production is lower priority. The site still needs to work. People still need to be use the website. But like the GPUs, they're like the value that we get off the GPUs doing trainings is more like higher than than we get out of production."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [10:33](https://www.youtube.com/watch?v=byn9PURoBNY&t=633s)

> "There's this very nice project called virtual kubelet, also open source. Uh you can build on top of it. It is a very nice code base. Uh and this works by creating a fake machine in Kubernetes."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [11:45](https://www.youtube.com/watch?v=byn9PURoBNY&t=705s)

> "If something breaks on your side, something breaks on the the other side, just mark it as failed, let Kubernetes handle it, create a new one, and things keep working."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [13:26](https://www.youtube.com/watch?v=byn9PURoBNY&t=806s)

> "No execute in Kubernetes would kick everything out at the same time. So, as as like at moment you put the tanks, everything will be kicked out and that's bad."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [14:55](https://www.youtube.com/watch?v=byn9PURoBNY&t=895s)

> "once you calibrate it was was like very very well and like changed the way we do research cuz no one else needs to care about GPUs."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [15:26](https://www.youtube.com/watch?v=byn9PURoBNY&t=926s)

> "if you're doing like diffusion transformers, they're not huge like LLMs that need like multi-node like inference. Uh something that we learned like whatever GPU works. Uh the GPU can be hot, falling out of the bus. It can be exploding. Uh inference still going to run."
>
> — [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [15:57](https://www.youtube.com/watch?v=byn9PURoBNY&t=957s)

