---
title: "Vivek Muppalla"
type: "speaker"
slug: "vivek-muppalla"
role: "VP AI Engineering"
company: "Hippocratic AI"
talk_count: 1
---

# Vivek Muppalla

**VP AI Engineering &middot; Hippocratic AI**

Vivek Raju Muppalla is VP of AI Engineering at Hippocratic AI, where he leads product engineering for healthcare agents powering AI Front Door, Nurse Co-Pilot, and over 200 million patient-agent interactions. His focus is on turning frontier models into clinically safe, production-grade voice agents across real-time orchestration, evaluation, reliability, and patient-facing workflows.

Vivek has spent over a decade building applied AI and large-scale production systems across Cohere, Scale AI, Unity Technologies, Amazon, Groupon, and Expedia. His work has spanned GenAI applications, synthetic data, computer vision, simulation, and production ML at scale. At Cohere, as VP of AI Engineering and Custom Models, he launched GenAI products across Fortune 500 enterprises and co-developed Takane, a high-performing Japanese LLM built in partnership with Fujitsu.

Throughout his career, Vivek has focused on the hardest part of shipping AI: building systems that are reliable, measurable, and useful in production.

[LinkedIn](https://www.linkedin.com/in/vivekmuppalla/)

## Talks

- [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md) (AI in Healthcare)

## Scheduled Sessions

- **200 Million Patient Interactions Later: What the Generic Voice Stack Misses** &middot; Day 4 — Session Day 3 &middot; 12:05pm-12:25pm &middot; Track 7

## Concepts

- [eval harness design](../concepts/eval-harness-design.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [latency budgets](../concepts/latency-budgets.md)
- [model routing](../concepts/model-routing.md)
- [quantization](../concepts/quantization.md)
- [rubric design](../concepts/rubric-design.md)
- [subjective and non-verifiable task evaluation](../concepts/subjective-and-non-verifiable-task-evaluation.md)
- [verifier design](../concepts/verifier-design.md)
- [voice agents](../concepts/voice-agents.md)

## Quotes

> "We can stop rationing, and you don't have to have calls just for the sickest 5%, but you can call everyone."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [0:49](https://www.youtube.com/watch?v=AN65uc645mE&t=49s)

> "we've had 200 million clinical interactions. We've had zero significant safety incidents. We've deployed in over 60 plus health systems and have an 8.5 on 10 patient satisfaction rating."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [2:06](https://www.youtube.com/watch?v=AN65uc645mE&t=126s)

> "many of these models take tens of seconds to respond, sometimes over a minute. And that's completely useless when we're trying to have a two-way conversation on a telephone."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [5:24](https://www.youtube.com/watch?v=AN65uc645mE&t=324s)

> "every time we work on an optimization, we buy back some latency, and we just don't bank that latency. We use that extra gap now to pack more intelligence into the overall system"
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [7:00](https://www.youtube.com/watch?v=AN65uc645mE&t=420s)

> "So, what seems like a tug-of-war between latency and intelligence for us is a compounding flywheel."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [7:41](https://www.youtube.com/watch?v=AN65uc645mE&t=461s)

> "We in fact run 31 models at any given point of time for every conversation."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [8:26](https://www.youtube.com/watch?v=AN65uc645mE&t=506s)

> "The reason we have the system is because we see a singular model being as like one point of failure, and that's just unacceptable for a patient conversation."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [8:26](https://www.youtube.com/watch?v=AN65uc645mE&t=506s)

> "most of what looks like model reasoning failures end up actually being model mishearing things"
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [9:12](https://www.youtube.com/watch?v=AN65uc645mE&t=552s)

> "So, the model hears not just the what, but also the how."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [10:42](https://www.youtube.com/watch?v=AN65uc645mE&t=642s)

> "when a patient mentions a medication name, we aren't guessing from like an infinite list of medications, but we have the chance to optimize around a finite list, and that helps in getting the word error rate down"
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [10:42](https://www.youtube.com/watch?v=AN65uc645mE&t=642s)

> "A now becomes a no, or a five becomes a fine. And in a patient conversation, that's catastrophic."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [12:21](https://www.youtube.com/watch?v=AN65uc645mE&t=741s)

> "every specialist first decides, "Hey, do I need to speak?" If not, it's a short circuit and that's what helps us keep us in the budget."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [13:00](https://www.youtube.com/watch?v=AN65uc645mE&t=780s)

> "for inference itself, quality is our constraint and speed is the work. So, we can never compromise on the quality of the output. Every speed optimization has to be lossless."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [14:57](https://www.youtube.com/watch?v=AN65uc645mE&t=897s)

> "we've figured out a way to keep a large chunk of these conversations warm on cache, giving us an over 96% hit rate"
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [15:43](https://www.youtube.com/watch?v=AN65uc645mE&t=943s)

> "Most agentic systems would claim 80%, 90% accuracy, and that's great for them. For us, even the 99% is pretty bad because 1% error means 100 people a day are going to get the wrong appointment type"
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [16:28](https://www.youtube.com/watch?v=AN65uc645mE&t=988s)

> "You need about 450 tests to be 99% sure that you can catch this like 1% error rate and and 1900 tests to be able to see that you've caught it like 10 times."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [17:13](https://www.youtube.com/watch?v=AN65uc645mE&t=1033s)

> "So you can't purely rely on synthetic data from our experience to be able to get to the scale of accuracy."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [17:13](https://www.youtube.com/watch?v=AN65uc645mE&t=1033s)

> "across five generations where we're at with our Polaris system is a 99.89% accuracy with respect to like no harm. And humans on the same rubric are at about 81%."
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [17:50](https://www.youtube.com/watch?v=AN65uc645mE&t=1070s)

> "It's not because like we're terrible, but AI systems don't get tired and unfortunately we do"
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [17:50](https://www.youtube.com/watch?v=AN65uc645mE&t=1070s)

> "We're told you got to pick two of these options around quality, speed, and safety. We didn't and we decided to go with all of them"
>
> — [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [20:07](https://www.youtube.com/watch?v=AN65uc645mE&t=1207s)

