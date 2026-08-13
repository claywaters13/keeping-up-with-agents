---
title: "Stop Renting Your Cognitive Infrastructure"
type: "talk"
slug: "stop-renting-your-cognitive-infrastructure"
org: "Kalmantic Labs"
video_id: "Bck7ABCZRZI"
duration_sec: 471
word_count: 1561
speakers: ["Thiyagarajan Maruthavanan"]
---

# Stop Renting Your Cognitive Infrastructure

**Speakers:** [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)

**Org:** Kalmantic Labs

**Duration:** 7m 51s

[Watch on YouTube](https://www.youtube.com/watch?v=Bck7ABCZRZI)

## Summary

Thiyagarajan Maruthavanan argues that renting inference from frontier labs is a trap that scales badly once you have product-market fit, and that at some point you must own your inference infrastructure. He opens with cautionary cost stories — a large retailer that spent ~$200M with Anthropic before building its own stack, Uber burning a year's token budget by month four, and his own app Ultrazone (a reverse-Suno tool that turns songs back into prompts) racking up hundreds of thousands of dollars in inference, plus a stolen API key that cost $10K before it was stopped. He then argues that 'token factories' (open-source models on neoclouds, endpoint providers, or a GPU rig in your garage) are only a partial answer: enterprises he worked with — a fund, a hospital, and a tax practice — each hit non-cost walls around rate-limit control, third-party vendor dependency in audit, and reproducibility of model recommendations. His decision rule is positional: pre-PMF startups can rent, but post-PMF companies and enterprises with budgeted projects should build. The talk closes on his slogan 'rent to learn, own to earn,' plus pointers to his open-source project just token max and his book on inference infra economics.

## Key Points

- Inference pricing is structured like prepaid casino credits rather than a monthly utility bill, which removes the mental anchor that would normally cap spend and leads teams to blow past their intended threshold.
- Real-world blowups are already common: one of the largest US retailers spent close to $200 million with Anthropic before building its own infrastructure, and Uber exhausted a full year's token budget by month four.
- The speaker's own consumer app Ultrazone — which inverts Suno by inferring the prompt that could have generated a given song — reached hundreds of thousands of users and cost hundreds of thousands of dollars in inference.
- Waste is structural, not just careless: teams skip input-token compression and agent loops generate many wasteful calls, because the inference endpoint has no awareness of the shape of the workload.
- Security exposure compounds the cost problem — a stolen key used from China drove spend from $7,000 toward $10,000 in a short window before the team arrested it, with $100,000 a plausible worst case.
- Token factories (open-source models on neoclouds, inference endpoint providers, or a local GPU rig / DGX box) work for personal and agent workloads but the speaker hit memory as the bottleneck and found them unreliable for enterprise.
- For enterprises the blockers are not primarily the bill: a fund wanted control over its own rate limits, a hospital was redlined in audit for third-party vendor dependency, and a tax practice needed to recreate a recommendation, which requires access into the model internals.
- The decision rule is positional rather than technical — pre-product-market-fit founders can rent, but post-PMF startups and enterprises with an already-budgeted use case should build their own inference infrastructure.
- The market is too noisy to follow vendor consensus, since Jensen Huang pitches token factories, Satya Nadella pitches unmetered local intelligence, and endpoint providers pitch themselves, with the rules of the game changing every three to six months.

## Notable Quotes

> "One of the largest retailers in the country spent close to $200 million on inference with Anthropic and decided that things got way out of hand and built their own infrastructure."
>
> — [0:00](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=0s) &middot; *Opens with the headline number that frames the entire argument.*

> "I'm pretty sure most of you have read the news from Uber CTO on how they had planned a budget of their tokens for an entire year and it got over in month four."
>
> — [0:00](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=0s) &middot; *Second concrete datapoint that token budgeting is failing at scale.*

> "But in case of using these rented intelligence platform, they are like prepaid. You load credits. It's almost as if you're loading credits inside a casino."
>
> — [0:38](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=38s) &middot; *The central metaphor for why inference spend escapes control.*

> "I had hundreds of thousands of users, but then the cost ballooned way more than what I had anticipated. Hundreds of thousands of dollars I had to spend on inference."
>
> — [1:15](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=75s) &middot; *First-person cost report, not secondhand news.*

> "And many people forget about doing compression of their input token. And when there are agent loops, then there are many of these calls that are happening which are very, very wasteful."
>
> — [1:47](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=107s) &middot; *Names the specific engineering causes of runaway inference cost.*

> "The inference endpoint that is consuming this is is completely unaware of the shape of the workload and which is why this happens."
>
> — [1:47](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=107s) &middot; *States a structural, architectural cause rather than blaming user discipline.*

> "3 weeks ago, my key got stolen. Someone in China got hold of it and then was sucking my endpoint dry. I could see the cost rise up from 7,000 to 7,500 dollars to 8,000 and going and so forth."
>
> — [1:47](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=107s) &middot; *Concrete security-as-cost incident with numbers and a timeline.*

> "Token factory is is basically saying that why are you paying money to Anthropic and OpenAI? Instead, go open source, have these open source models that are already deployed somewhere in the cloud, and then they are provisioned as tokens per second."
>
> — [2:26](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=146s) &middot; *Defines the main alternative the talk goes on to qualify.*

> "I bought my own DGX box and then I first moved Ulta Sono from Anthropic to DGX box. It worked well. I ran into this one issue of memory being the bottleneck."
>
> — [3:01](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=181s) &middot; *Reports what actually broke when he self-hosted.*

> "The issue though is is that, you know, it may not be reliable for enterprise, which is what I exactly faced."
>
> — [3:35](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=215s) &middot; *The pivot from personal token factory to the enterprise objection.*

> "But for enterprises, renting and leasing don't cut it. Bill is a problem, but then there are secondary set of problems that makes it extremely ineffective approach."
>
> — [3:35](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=215s) &middot; *Explicitly argues cost is not the primary enterprise driver.*

> "they didn't want somebody else to dictate as to what the rate limit that they could consume."
>
> — [3:35](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=215s) &middot; *Names control over rate limits as a distinct non-cost reason to own.*

> "later when they went through an audit, a third-party vendor dependency was redlined, and then they couldn't go forward."
>
> — [4:15](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=255s) &middot; *Compliance failure mode that no amount of price optimization fixes.*

> "when an intelligent generates a recommendation, you want to be able to recreate it. And when you don't have access to the in-depth of the model, you will not be able to do this"
>
> — [4:15](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=255s) &middot; *Reproducibility argument for model-level access in regulated work.*

> "If you're a startup, if you're a founder who is doing pre-product market fit work, so you're still figuring out that the use case that you have, if there is demand for it, you can get by by renting."
>
> — [4:51](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=291s) &middot; *The concession half of his decision rule, which keeps it checkable.*

> "You experience the environment, you experience the city, the neighborhood, but then eventually you have to buy the house. You cannot raise a family in an Airbnb."
>
> — [5:30](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=330s) &middot; *The analogy that carries his thesis for the audience.*

> "We benchmarked against headroom and on many parameters, just token maxes is far superior."
>
> — [6:08](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=368s) &middot; *A specific comparative claim about his open-source tool.*

> "The AI market is is very different compared to the rest of the technology market that used to exist because here the rules of the game change every three to six months, which means it becomes a very noisy marketplace."
>
> — [6:08](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=368s) &middot; *Justifies why he distrusts vendor consensus on architecture.*

> "You talk to someone like Jensen, he would say token factory is the future. You hear someone like a Satya Nadella, he will say unmetered intelligence is the future, it is going to be local."
>
> — [6:50](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=410s) &middot; *Frames the industry disagreement the talk is intervening in.*

> "if you want to learn, you can rent, but if you want to earn, then you have to own. And if there was the one sentence that you had to take away from this entire presentation, it is that."
>
> — [6:50](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=410s) &middot; *The speaker's own designated thesis statement.*

## Positions

- Post-product-market-fit startups and enterprises with budgeted AI projects cannot afford to keep renting inference and should build their own infrastructure. ([4:51](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=291s), confidence: stated)
- Pre-product-market-fit founders should rent inference rather than build, because they are still validating demand. ([4:51](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=291s), confidence: stated)
- Prepaid credit-based inference pricing systematically causes overspend because it lacks the periodic-bill anchor of a normal utility. ([0:38](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=38s), confidence: stated)
- Token factories are not a sufficient answer for enterprises, because control, audit, and reproducibility problems remain even when cost improves. ([3:35](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=215s), confidence: stated)
- Inference waste is structural: endpoints cannot see the shape of the workload, so agent loops and uncompressed inputs generate avoidable calls. ([1:47](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=107s), confidence: stated)
- Reproducing a model-generated recommendation requires access into the model itself, which rented endpoints do not provide. ([4:15](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=255s), confidence: stated)
- His open-source project just token max outperforms Netflix's headroom on many benchmark parameters. ([6:08](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=368s), confidence: stated)
- Vendor guidance on inference architecture should be discounted because each major player advocates the architecture that favors its own business. ([6:50](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=410s), confidence: implied)
- Meaningful cost optimization is available even inside the rent/lease model, at the token-management and context-management layers. ([5:30](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=330s), confidence: stated)
- Owning inference infrastructure materially reduces exposure to key-theft-driven cost blowouts. ([1:47](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=107s), confidence: implied)

## Concepts

- [audit trails](../concepts/audit-trails.md)
- [build versus buy](../concepts/build-versus-buy.md)
- [context compaction](../concepts/context-compaction.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [software supply chain security](../concepts/software-supply-chain-security.md)
- [sovereign and air-gapped deployment](../concepts/sovereign-and-air-gapped-deployment.md)
- [token efficiency](../concepts/token-efficiency.md)

