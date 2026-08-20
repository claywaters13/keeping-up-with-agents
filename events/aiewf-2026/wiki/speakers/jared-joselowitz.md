---
title: "Jared Joselowitz"
type: "speaker"
slug: "jared-joselowitz"
role: "AI Research Engineer"
company: "Ufonia"
talk_count: 1
---

# Jared Joselowitz

**AI Research Engineer &middot; Ufonia**

Jared Joselowitz is the Lead AI Research Engineer at Ufonia, where Dora (an AI voice agent) makes clinical follow-up calls on the NHS and across US health systems; over 200,000 patient calls delivered, with signed contracts to scale past a million. He builds the evaluation and hazard-analysis stack for clinical voice AI: multi-agent simulation, prompt-optimisation pipelines, and the audit infrastructure that has to hold up when there's a patient on the other end of the call. His research on clinical AI safety and evaluation has been published at ACL, COLM and IWSDS, most recently an LLM judge that matches clinician safety assessments of speech-recognition errors. Originally from Johannesburg, South Africa, Jared studied electrical engineer before completing an MSc in Applied Machine Learning at Imperial College London, where his thesis used inverse reinforcement learning to recover the implicit reward models of RLHF-trained LLMs.

[LinkedIn](https://www.linkedin.com/in/jaredjoselowitz/)

## Talks

- [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md) (AI in Healthcare)

## Scheduled Sessions

- **Shipping AI to a Million Patients Without an A/B Test** &middot; Day 4 — Session Day 3 &middot; 11:40am-12:00pm &middot; Track 7

## Concepts

- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [simulation environments](../concepts/simulation-environments.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)
- [voice agents](../concepts/voice-agents.md)

## Quotes

> "you can't actually AB test on patients of course. Randomizing patients into a worse variant is unethical and often illegal."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [0:47](https://www.youtube.com/watch?v=McknwOzbmyg&t=47s)

> "you can't undo a call. Once Dora says it, it's been said and there is no rollback."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [0:47](https://www.youtube.com/watch?v=McknwOzbmyg&t=47s)

> "And very importantly the model card won't save you. Um you can't claim like some model vendors said that they have 92% on some benchmark."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [0:47](https://www.youtube.com/watch?v=McknwOzbmyg&t=47s)

> "so far we've done around 200,000 real clinical calls within the UK across 20 hospitals. And we are contracted to scale to a million patients in the next 2 years."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [1:25](https://www.youtube.com/watch?v=McknwOzbmyg&t=85s)

> "Roll back. You can't really roll back. The call has already happened. The person has already been harmed."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [4:46](https://www.youtube.com/watch?v=McknwOzbmyg&t=286s)

> "Well, they didn't just drive around crashing into walls and say, "We won't do that again." and then doing another RL loop."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [5:18](https://www.youtube.com/watch?v=McknwOzbmyg&t=318s)

> "Simulation is only the real ethical option we can go with. You can't run all the hazard the hazards I just mentioned on real people as a first grasp."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [5:56](https://www.youtube.com/watch?v=McknwOzbmyg&t=356s)

> "We use a simulated patient and not a hired actor because hired actors don't scale."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [6:29](https://www.youtube.com/watch?v=McknwOzbmyg&t=389s)

> "In three out of the four, the majority of people actually thought that the simulated patient was more realistic."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [8:27](https://www.youtube.com/watch?v=McknwOzbmyg&t=507s)

> "The top model, which as of a year ago when we wrote the paper, was Gemini 2.5 Pro. Now we've maybe updated the models. Um it achieved an F1 score of of 0.96."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [10:13](https://www.youtube.com/watch?v=McknwOzbmyg&t=613s)

> "You would rather overcall hazards that aren't there than undercall hazards that are there."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [10:51](https://www.youtube.com/watch?v=McknwOzbmyg&t=651s)

> "grading isn't technically improving the product. A pile of pass/fails tells you where Dora breaks and where it's not safe, but doesn't actually make the product better."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [10:51](https://www.youtube.com/watch?v=McknwOzbmyg&t=651s)

> "Formatting changes alone have been seen to swing benchmark by 76 percentage points. And reordering few-shot examples flips a model from near random, so near 50%, to near state-of-the-art on some benchmarks."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [11:25](https://www.youtube.com/watch?v=McknwOzbmyg&t=685s)

> "Simulation is the inner loop. It's fast, it's free, you can do thousands of runs before anyone actually real is is exposed."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [15:07](https://www.youtube.com/watch?v=McknwOzbmyg&t=907s)

> "But, real patients are the outer loop, and that's where the only real proof is. So, simulation is necessary, but it's not sufficient."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [15:44](https://www.youtube.com/watch?v=McknwOzbmyg&t=944s)

> "And how much autonomy you allow the system to do depends on your evidence. As the system gets more evidence, you can give it more independence."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [16:18](https://www.youtube.com/watch?v=McknwOzbmyg&t=978s)

> "The important thing is that you don't ship the model, you ship the evidence when trying to regulate."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [16:18](https://www.youtube.com/watch?v=McknwOzbmyg&t=978s)

> "You first have to define exactly what harm is for your product. You have to manufacture your rare but then but dangerous cases. Don't wait for them just to happen naturally."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [16:55](https://www.youtube.com/watch?v=McknwOzbmyg&t=1015s)

> "Voice is just a new module in the same safety case"
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [18:14](https://www.youtube.com/watch?v=McknwOzbmyg&t=1094s)

