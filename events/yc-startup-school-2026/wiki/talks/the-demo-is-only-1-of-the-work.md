---
title: "The Demo Is Only 1% Of The Work"
type: "talk"
slug: "the-demo-is-only-1-of-the-work"
org: "Waymo"
video_id: "Gp4zrV3-6N8"
duration_sec: 2964
word_count: 7752
speakers: ["Dmitri Dolgov"]
---

# The Demo Is Only 1% Of The Work

**Speakers:** [Dmitri Dolgov](../speakers/dmitri-dolgov.md)

**Org:** Waymo

**Duration:** 49m 24s

[Watch on YouTube](https://www.youtube.com/watch?v=Gp4zrV3-6N8)

## Summary

Waymo co-CEO Dmitri Dolgov distills roughly two decades of autonomous driving into seven technical lessons about building AI that operates in the physical world rather than on a screen. His central argument is that a working demo is at most 1% of the work: Waymo hit 'capability complete' driving in 2010 after 18 months, but needed about 15 more years to ship a real product, because reliability lives on an exponential ladder of nines where each additional nine costs 10x and demands a fundamentally different approach. He argues physical AI differs from digital AI along four gaps — error cost, latency, data, and validation — and that these force choices most founders get wrong: redundant multimodal sensing over camera-only, structure-augmented end-to-end models over black-box end-to-end, and closed-loop generative simulation as a first-class AI system rather than tooling. The talk closes on the claim that evals and metrics, not models, are the durable moat, backed by Waymo's published safety data (17x fewer serious-injury crashes than human drivers over 220M+ autonomous miles). Worth watching if you are building anything where mistakes cost more than a retry, or if you want a concrete account of how a hype-cycle-surviving company repeatedly absorbs new AI waves into production.

## Key Points

- A working demo is at most 1% of the work; Waymo achieved its initial autonomous driving milestones in about 18 months in 2009-2010, then spent roughly 15 years reaching a scalable driverless product, and now serves half a million trips per week across 15 US cities.
- Reliability sits on an exponential ladder of nines where each additional nine costs about 10x more effort and requires a fundamentally different technical approach — redundancy and backup architectures, not more of the same bug fixing — so founders should determine how many nines their product needs before choosing an architecture.
- Physical AI differs from digital AI along four gaps: the cost of errors (lives, not tokens), latency (a car moves 100 feet per second at freeway speed, and inference must run on a computer in the trunk), data (there is no internet-scale corpus of the physical world), and validation (you need high confidence on day one rather than shipping 'good enough' and letting users find edge cases).
- Every AI breakthrough makes demos ~100x easier while barely moving the long tail, which is why each hype cycle produces spectacular demos and very few products; the recurring mistake is spending on the demo when you should be saving for the nines.
- Waymo uses cameras, lidar, and radar with complementary physics — not as backups but fused through per-modality encoders — because camera-only sensing yields a safety curve that flattens well below superhuman performance, and redundancy is needed anyway so a single leaf on a sensor cannot halt the robot.
- The Waymo Foundation Model is a multimodal world-action-language model with an encoder-decoder, system-1/system-2 architecture: a fast path fusing raw sensor data for millisecond reactions, and a slow path using VLM world knowledge for semantic reasoning (e.g. recognizing a burning car and rerouting even when the path ahead is geometrically clear).
- Waymo's 'structure-augmented end-to-end' approach augments learned embeddings with materialized structured representations, buying inference-time safety validation, cheaper large-scale training and evaluation in a compact representation space, and verifiable reward signals for RL — the principle being that structure which channels scale wins while structure that fights scale loses.
- Closed-loop simulation is mandatory, and a real simulator is itself a large AI model as hard to build as the agent; Waymo pairs a behavioral world model operating on structured representations with a sensor world model (leveraging Google DeepMind's Genie 3) to generate never-observed scenarios like a plane landing on the freeway or an elephant in an intersection.
- The system is three AIs plus a flywheel — agent, simulator, and critic sharing one foundation model — where deployment generates data that grounds the simulator, which generates harder edge cases for the critic and agent, and metrics are what steer the flywheel in the right direction.
- Evals and metrics are the strategic moat rather than the model: build them before the product, extend validation beyond model level to every physical, behavioral, onboard, offboard, and operational component (Waymo's 'safety and readiness framework'), and publish the results, because hundreds of millions of audited real-world miles are far harder to replicate than an architecture.

## Notable Quotes

> "the best AI moments will look like nothing happened. It's just the task got done safely and smoothly."
>
> — [1:37](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=97s) &middot; *Frames the entire thesis about physical AI success being invisible.*

> "Now, in Silicon Valley, there's a common mantra to move fast and break things. However, when you're dealing with atoms instead of bits, breaking things is not really okay. So, the thing you have to do is to move fast and ship safely."
>
> — [2:28](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=148s) &middot; *Direct rejection of the dominant startup mantra for physical products.*

> "In the physical world, the cost of a mistake can be measured in human lives, not tokens. There's simply not an undo and a retry button."
>
> — [4:08](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=248s) &middot; *The sharpest statement of the error-cost gap between digital and physical AI.*

> "There's no digitized version of the internet for the physical world."
>
> — [4:55](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=295s) &middot; *Names the data gap that makes physical AI unable to copy the LLM playbook.*

> "And a working demo is 1% at best of the work that you have to do. The many nines of performance, the many nines of reliability that follow, that's where the real work happens."
>
> — [8:19](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=499s) &middot; *The title claim, stated plainly.*

> "So, the demo took 18 months, the product took about 15 years."
>
> — [10:25](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=625s) &middot; *Concrete numbers behind the demo-to-product gap from the canonical example.*

> "that reliability and performance lives on this exponential ladder of nines. So, getting to that first 90% or 99%, that's the easy part. But then every next nine that you want to add, that takes about 10 times more effort."
>
> — [11:25](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=685s) &middot; *States the 10x-per-nine cost model that drives the rest of the talk.*

> "And at scale, the long tail is the problem space, is your entire problem statement. When you drive millions of miles per week, a rare event that might happen once in a million miles, that just becomes your daily reality."
>
> — [12:20](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=740s) &middot; *Explains why scale converts rare events into the core engineering problem.*

> "And that's why every hype cycle produces a wave of absolutely spectacular demos and very few real products. And the recurring mistake of every cycle is spending on the demo when you should be saving for the nines."
>
> — [13:48](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=828s) &middot; *A pointed diagnosis of the current AI demo boom, from someone who lived three prior cycles.*

> "So, count your nines before you count your demo views."
>
> — [14:24](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=864s) &middot; *Compact, memorable version of the talk's founder advice.*

> "However, if you are targeting full autonomy, and you're targeting superhuman, strongly superhuman performance, you find that weak sensing just leads to a safety curve that flattens out way too early."
>
> — [16:01](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=961s) &middot; *Takes an explicit side in the camera-only versus multimodal sensing debate.*

> "if you don't have redundancy in sensing, you can have, you know, a single leaf land on your sensors and bring your robot to a full stop."
>
> — [18:48](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=1128s) &middot; *Vivid, checkable justification for hardware redundancy over cost minimization.*

> "So, betting your company, betting your approach on today's hardware prices is just betting your company on a number that has a fairly short shelf life and is going to expire."
>
> — [20:23](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=1223s) &middot; *Names a specific strategic trap for hardware and deep-tech founders.*

> "The much harder muscle to build is to carry that bleeding edge research into production and deploy it in a safety critical environment without regressions."
>
> — [22:51](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=1371s) &middot; *Separates applied research capability from the organizational muscle that actually ships.*

> "Essentially, structure that fights scale will always lose. And structure that channels scale always wins."
>
> — [30:45](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=1845s) &middot; *A crisp refinement of the bitter lesson that other speakers might contest.*

> "So, the lesson here is to bet on a system that's maximally learned and minimally constrained and leverage structure intentionally to boost performance and scaling laws both in training and in evaluation."
>
> — [35:37](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2137s) &middot; *States Waymo's architectural position on end-to-end versus structured models.*

> "the problem of building a good realistic simulator is just as hard as building the agent itself."
>
> — [37:58](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2278s) &middot; *Counters the common view of simulation as supporting tooling.*

> "that your model is really table stakes, but eval and metrics, that's your most important. That's your strategic moat."
>
> — [42:42](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2562s) &middot; *The talk's most transferable claim about where durable advantage lives.*

> "If you can't quantitatively define what good enough means, you're not really building a product, you're just iterating on your demo."
>
> — [42:42](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2562s) &middot; *Turns the eval argument into a test founders can apply immediately.*

> "Your your models can be leaked, algorithms can be replicated, but hundreds of millions of miles of fully autonomous operations in the real world, backed by evidence-grade evaluation and publicly audited proof, that is much, much more difficult to replicate."
>
> — [45:19](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2719s) &middot; *Defines the moat in terms of accumulated evidence rather than technology.*

> "And at the current scale, what that means is that Waymo is preventing a serious injury every 8 days."
>
> — [47:00](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2820s) &middot; *Converts the safety statistics into a concrete, checkable outcome claim.*

> "And the last decade of AI happened in the digital world, and the next decade will also happen in the physical world."
>
> — [47:43](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2863s) &middot; *The forward-looking bet the whole playbook is offered in service of.*

## Positions

- A working demo represents at most 1% of the work required to ship a real product in the physical world. ([8:19](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=499s), confidence: stated)
- Each additional nine of reliability costs roughly 10x more effort and requires a fundamentally different technical approach, not more of the same work. ([11:25](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=685s), confidence: stated)
- Every AI breakthrough makes prototypes about 100 times easier while barely improving the long tail, which is why hype cycles yield demos rather than products. ([13:48](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=828s), confidence: stated)
- Camera-only sensing is adequate for driver-assist or roughly human-level performance but its safety curve flattens out before reaching strongly superhuman full autonomy. ([16:01](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=961s), confidence: stated)
- Because redundancy is required regardless, teams should use multiple sensing modalities with complementary physics rather than duplicating a single modality. ([19:31](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=1171s), confidence: stated)
- Anchoring a company's strategy to today's hardware component prices is a mistake because components will commoditize and drop in price. ([20:23](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=1223s), confidence: stated)
- New technology adoption should be judged on whether it simplifies and unifies the stack, not only on capability and performance gains. ([24:10](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=1450s), confidence: stated)
- Betting on a high-capacity foundation model and distilling into smaller onboard models yields better scaling laws than training small models directly. ([30:45](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=1845s), confidence: stated)
- Vanilla black-box end-to-end models are sufficient for some products but not for superhuman performance in a safety-critical fully autonomous agent. ([32:07](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=1927s), confidence: stated)
- Structured intermediate representations enable inference-time safety validation, cheaper training and evaluation, and verifiable reward signals that a pure black-box model cannot provide. ([34:45](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2085s), confidence: stated)
- Closed-loop simulation, not open-loop evaluation, is required to evaluate counterfactual actions for safety-critical physical agents. ([37:13](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2233s), confidence: stated)
- Building an end-to-end driving model has been relatively easy for a while; evaluating it in closed loop was the hard part. ([38:40](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2320s), confidence: stated)
- Evals and metrics, not model architecture or data, constitute a company's strategic moat, and should be built before the product. ([42:42](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2562s), confidence: stated)
- In Waymo's operating areas, the Waymo driver is about 17 times better than human drivers on crashes causing serious injury, based on over 220 million fully autonomous miles. ([46:06](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2766s), confidence: stated)
- Physical AI today is roughly where digital AI was a few years ago, and the necessary ingredients — world models, architectures, affordable compute and sensing, scaling laws — are now in place. ([47:43](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2863s), confidence: stated)
- Publishing safety data openly, rather than proving results internally, is necessary to earn public and regulatory trust. ([45:19](https://www.youtube.com/watch?v=Gp4zrV3-6N8&t=2719s), confidence: implied)

## Concepts

- [physical ai](../concepts/physical-ai.md)
- [platform dependency risk](../concepts/platform-dependency-risk.md)
- [safety-critical reliability](../concepts/safety-critical-reliability.md)
- [simulation and sim-to-real transfer](../concepts/simulation-and-sim-to-real-transfer.md)
- [the bitter lesson](../concepts/the-bitter-lesson.md)

