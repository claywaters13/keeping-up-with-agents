---
title: "Infra behind Krea 2: How to train and serve at scale"
type: "talk"
slug: "infra-behind-krea-2-how-to-train-and-serve-at-scale"
track: "Generative Media"
org: "Krea.ai"
day: "Day 4 — Session Day 3"
room: "Track 1"
video_id: "byn9PURoBNY"
duration_sec: 1015
word_count: 3440
speakers: ["Gabriel Jorge Menezes"]
---

# Infra behind Krea 2: How to train and serve at scale

*Program title: Infra behind Krea 2 - How to train and serve at scale*

**Speakers:** [Gabriel Jorge Menezes](../speakers/gabriel-jorge-menezes.md)

**Org:** Krea.ai

**Track:** Generative Media &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 16m 55s

[Watch on YouTube](https://www.youtube.com/watch?v=byn9PURoBNY)

## Summary

Gabriel Jorge Menezes, infra engineer at Krea, walks through the training and serving infrastructure behind Krea 2 (K2), a text-to-image diffusion transformer pre-trained from scratch on thousands of Infiniband-connected GPUs. The training half is a candid reliability postmortem: runs crashed far more often than Meta's published failure estimates suggested, silent cross-node failures dominated, and the fix was less heroic debugging than aggressive metrics (tensor core utilization, GPU temperature, InfiniBand and NVLink error counters — several of which NVIDIA does not export by default) plus a fast paid filesystem that made 20–30 minute checkpointing free. The serving half describes a scheduler that lets one shared cluster run both research and production: Kueue-style gang scheduling gives trainings absolute priority, and a custom virtual-kubelet provider transparently evicts production inference to external GPU rentals when trainings claim the cluster, migrating it back via taints and a descheduler when GPUs free up. Worth watching if you run a mixed research/production GPU cluster and want concrete, unglamorous operational detail — including why GPU utilization is a lie and why image-model inference will happily run on nearly-dead GPUs.

## Key Points

- Krea 2 was pre-trained entirely from scratch with no base checkpoint, on thousands of Infiniband-connected GPUs, and released open source with both a raw pre-trained checkpoint for post-training and a fast 'turbo' post-trained checkpoint that generates images in under a second.
- Failure rate scaled worse than expected with cluster size: runs that lasted days at small scale dropped to under 8 hours at 128–512+ GPUs, well short of the failure estimates in Meta's published paper, and many failures were silent (NCCL timeouts with healthy-looking metrics).
- The team abandoned paranoid node-swapping on every crash after learning that the same machines, code, and data could crash hourly and then suddenly run 12–24 hours cleanly; the practical fix was checkpointing constantly rather than diagnosing every failure.
- GPU utilization is a misleading metric — it reports time spent doing work, not efficiency — so the team used tensor core utilization as the real proxy, and watched it rise as training resolution scaled from 128 to 1024 pixels.
- InfiniBand metrics are not exported by DCGM by default and had to be custom-collected, but they mattered most because the majority of failures were cross-node communication problems; NVLink error counters (also unexported) caught single-node faults where the GPUs otherwise looked fine.
- Ceph was abandoned after data-trust failures; a paid filesystem doing ~1.8 TB/s reads and ~1 TB/s writes let them dump a terabyte checkpoint in under 30 seconds every 20–30 minutes without stalling training.
- Researchers never think about GPU allocation: jobs go into a Kueue-managed queue with gang scheduling and two priority tiers, where training pods always outrank production inference and forcibly evict it from the shared cluster.
- A custom virtual-kubelet provider makes eviction safe by transparently rescheduling production inference onto external GPU providers, then using taints plus a descheduler (not a NoExecute taint, which would kick everything out at once) to migrate it gradually back when cluster GPUs free up.
- Diffusion transformers don't need multi-node inference like large LLMs, so production inference can run on nearly any GPU — including hot, failing, or 'falling out of the bus' hardware — which is what makes offloading production to cheap external capacity viable.

## Notable Quotes

> "the whole idea about training this model was because we were kind of bored of AI images. They're quite, you know, soulless. They have no spice."
>
> — [0:01](https://www.youtube.com/watch?v=byn9PURoBNY&t=1s) &middot; *States the aesthetic motivation for building a from-scratch model rather than fine-tuning an existing one.*

> "the whole idea was to like kind of bridge the gap between like LLM research and diffusion transformers. Uh, so my AI researchers they ported a lot of research from LLMs into into DiTs."
>
> — [2:02](https://www.youtube.com/watch?v=byn9PURoBNY&t=122s) &middot; *Names the core research bet behind the model architecture.*

> "the whole like like the whole like architecture of the model was meant to be extremely extremely simple. And so like it is very very dumb, but like very effective."
>
> — [2:37](https://www.youtube.com/watch?v=byn9PURoBNY&t=157s) &middot; *Takes a side on architectural complexity in a field prone to elaborate designs.*

> "we learned that like sometimes you just let it crash. It crashes, like it runs for like an hour, crash, runs for an hour, crash, and then runs again on the same set of machines, same code, same data for like 12 hours, 16 hours, 24 hours."
>
> — [3:18](https://www.youtube.com/watch?v=byn9PURoBNY&t=198s) &middot; *The counterintuitive operational lesson: stop debugging every failure, because identical setups behave differently run to run.*

> "you can imagine doing large-scale pre-training on runs that last less than 8 hours, it is a problem, right? You want kept those GPUs fed and if things are crashing, you are not doing progress and losing time and models are going to be late."
>
> — [3:49](https://www.youtube.com/watch?v=byn9PURoBNY&t=229s) &middot; *Quantifies their real mean-time-to-failure and ties it directly to schedule risk.*

> "Metrics are everything. That's how I can support my researchers. That's how I have visibility in the system. And like if you're doing large-scale pre-training, I highly highly recommend for you to invest heavily on metrics."
>
> — [4:25](https://www.youtube.com/watch?v=byn9PURoBNY&t=265s) &middot; *The talk's central prescription, stated plainly.*

> "So for us it was like if there is any GPUs above like 78°, you you remove them. Don't don't think about it. Don't try to fix. Don't don't try to be smart. You just remove the GPU."
>
> — [4:59](https://www.youtube.com/watch?v=byn9PURoBNY&t=299s) &middot; *A concrete, actionable numeric threshold and an explicit anti-cleverness policy.*

> "there is GPU utilization which is a lie. Uh, don't trust this. Uh, this is dumb."
>
> — [4:59](https://www.youtube.com/watch?v=byn9PURoBNY&t=299s) &middot; *Blunt rejection of the metric most teams default to.*

> "What we would use uh, as a proxy was tensor core utilization. This is actually how how much of a tensor core you're using and like how effective they are being."
>
> — [5:32](https://www.youtube.com/watch?v=byn9PURoBNY&t=332s) &middot; *Names the replacement metric and why it's more honest.*

> "if you're doing large-scale pre-training with a bunch of GPUs talking to each other between machines and you have no InfiniBand metrics, you're doing something wrong."
>
> — [6:01](https://www.youtube.com/watch?v=byn9PURoBNY&t=361s) &middot; *Strong normative claim about observability gaps most clusters ship with.*

> "These was probably the most important stuff for us because most of our failures were like related to like cross-node communication."
>
> — [6:39](https://www.youtube.com/watch?v=byn9PURoBNY&t=399s) &middot; *Localizes the dominant failure mode at scale.*

> "At the beginning we use SEF. SEF didn't work well. Was very annoying. It broke. We lost trust in data. So, I recommend if if you have the money go go with something paid and cuz you can trust your data."
>
> — [7:42](https://www.youtube.com/watch?v=byn9PURoBNY&t=462s) &middot; *A rare on-record build-vs-buy recommendation against open-source storage for training clusters.*

> "We can do like 1.8 terabytes of second of reads, almost a terabyte of writes. And the file system would not choke on the training. So, we could checkpoint every like 30 minutes, 20 minutes, produce like a terabyte of data in like less than 30 seconds."
>
> — [8:17](https://www.youtube.com/watch?v=byn9PURoBNY&t=497s) &middot; *Hard numbers connecting storage throughput to checkpoint cadence.*

> "I just want them to launch stuff and this goes into a queue and if we have GPUs we have GPUs. If we don't have GPUs we don't have GPUs."
>
> — [8:54](https://www.youtube.com/watch?v=byn9PURoBNY&t=534s) &middot; *Compresses the whole platform philosophy into one line about researcher experience.*

> "If there's inference running on those machines, the inference gets kicked out. And you'd say, "Oh, this is bad. Production is going to go down." No, you can build on top of that to to make production not go down"
>
> — [9:30](https://www.youtube.com/watch?v=byn9PURoBNY&t=570s) &middot; *Anticipates the obvious objection to training-over-production priority and answers it.*

> "production is lower priority. The site still needs to work. People still need to be use the website. But like the GPUs, they're like the value that we get off the GPUs doing trainings is more like higher than than we get out of production."
>
> — [10:33](https://www.youtube.com/watch?v=byn9PURoBNY&t=633s) &middot; *An explicit and contestable prioritization of research over production capacity.*

> "There's this very nice project called virtual kubelet, also open source. Uh you can build on top of it. It is a very nice code base. Uh and this works by creating a fake machine in Kubernetes."
>
> — [11:45](https://www.youtube.com/watch?v=byn9PURoBNY&t=705s) &middot; *Names the specific mechanism enabling cross-cluster burst scheduling.*

> "If something breaks on your side, something breaks on the the other side, just mark it as failed, let Kubernetes handle it, create a new one, and things keep working."
>
> — [13:26](https://www.youtube.com/watch?v=byn9PURoBNY&t=806s) &middot; *Argues for delegating failure recovery to the orchestrator instead of writing custom reconciliation.*

> "No execute in Kubernetes would kick everything out at the same time. So, as as like at moment you put the tanks, everything will be kicked out and that's bad."
>
> — [14:55](https://www.youtube.com/watch?v=byn9PURoBNY&t=895s) &middot; *Explains a specific Kubernetes design tradeoff that forced a gradual-migration approach.*

> "once you calibrate it was was like very very well and like changed the way we do research cuz no one else needs to care about GPUs."
>
> — [15:26](https://www.youtube.com/watch?v=byn9PURoBNY&t=926s) &middot; *States the payoff of the self-healing scheduler in terms of research velocity.*

> "if you're doing like diffusion transformers, they're not huge like LLMs that need like multi-node like inference. Uh something that we learned like whatever GPU works. Uh the GPU can be hot, falling out of the bus. It can be exploding. Uh inference still going to run."
>
> — [15:57](https://www.youtube.com/watch?v=byn9PURoBNY&t=957s) &middot; *A sharp asymmetry between training and inference hardware requirements that underpins the whole cost strategy.*

## Positions

- GPU utilization is a misleading metric for training efficiency; tensor core utilization is the correct proxy. ([4:59](https://www.youtube.com/watch?v=byn9PURoBNY&t=299s), confidence: stated)
- Any GPU running above roughly 78°C should be removed from the pool immediately rather than debugged or tuned. ([4:59](https://www.youtube.com/watch?v=byn9PURoBNY&t=299s), confidence: stated)
- Anyone doing multi-node large-scale pre-training without InfiniBand metrics is doing it wrong, since most failures at scale are cross-node communication failures. ([6:01](https://www.youtube.com/watch?v=byn9PURoBNY&t=361s), confidence: stated)
- Their training runs failed far more frequently than Meta's published failure-rate estimates predicted, often lasting under 8 hours. ([3:49](https://www.youtube.com/watch?v=byn9PURoBNY&t=229s), confidence: stated)
- Repeatedly swapping nodes in response to crashes is wasted effort; the same machines and code will often run for 12–24 hours after a series of hourly crashes. ([3:18](https://www.youtube.com/watch?v=byn9PURoBNY&t=198s), confidence: stated)
- Teams with budget should buy a commercial parallel filesystem rather than run Ceph, because Ceph broke and cost them trust in their data. ([7:42](https://www.youtube.com/watch?v=byn9PURoBNY&t=462s), confidence: stated)
- Frequent checkpointing is the primary mitigation for unreliable clusters, and a fast enough filesystem makes 20–30 minute checkpoints effectively free. ([8:17](https://www.youtube.com/watch?v=byn9PURoBNY&t=497s), confidence: stated)
- Training workloads should have strictly higher scheduling priority than production inference, because the value extracted from GPUs doing training exceeds that from serving production. ([10:33](https://www.youtube.com/watch?v=byn9PURoBNY&t=633s), confidence: stated)
- Evicting production inference from the training cluster does not have to cause an outage, because inference can be transparently relocated to other clusters or rented GPU capacity. ([9:30](https://www.youtube.com/watch?v=byn9PURoBNY&t=570s), confidence: stated)
- Custom failure-recovery logic in a cross-cluster scheduler is unnecessary; marking the pod failed and letting Kubernetes and the HPA recreate it is sufficient. ([13:26](https://www.youtube.com/watch?v=byn9PURoBNY&t=806s), confidence: stated)
- NoExecute taints are the wrong tool for reclaiming nodes because they evict all pods simultaneously and would take production down; a descheduler with ordinary taints migrates pods gradually instead. ([14:55](https://www.youtube.com/watch?v=byn9PURoBNY&t=895s), confidence: stated)
- Kueue's manually specified queue resource quotas drift out of sync on a fluid cluster where nodes come and go, and this can break gang scheduling. ([9:59](https://www.youtube.com/watch?v=byn9PURoBNY&t=599s), confidence: stated)
- Diffusion transformer inference is robust to bad hardware and does not require multi-node setups, unlike large LLM inference, so degraded GPUs remain usable for serving. ([15:57](https://www.youtube.com/watch?v=byn9PURoBNY&t=957s), confidence: stated)
- A deliberately simple, even 'dumb' model architecture was effective for Krea 2, with LLM research techniques ported over to diffusion transformers. ([2:37](https://www.youtube.com/watch?v=byn9PURoBNY&t=157s), confidence: stated)
- Researchers should never have to reason about GPU availability; the queue should absorb that entirely. ([8:54](https://www.youtube.com/watch?v=byn9PURoBNY&t=534s), confidence: stated)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [durable execution](../concepts/durable-execution.md)
- [scaling laws](../concepts/scaling-laws.md)

