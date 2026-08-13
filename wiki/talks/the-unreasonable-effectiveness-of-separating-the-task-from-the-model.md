---
title: "The Unreasonable Effectiveness of Separating the Task from the Model"
type: "talk"
slug: "the-unreasonable-effectiveness-of-separating-the-task-from-the-model"
track: "Harness Engineering"
org: "DSPy"
day: "Day 4 — Session Day 3"
room: "Main Stage"
video_id: "GgLQ02aO-hs"
duration_sec: 1031
word_count: 2757
speakers: ["Isaac Miller", "Maxime Rivest"]
---

# The Unreasonable Effectiveness of Separating the Task from the Model

**Speakers:** [Isaac Miller](../speakers/isaac-miller.md), [Maxime Rivest](../speakers/maxime-rivest.md)

**Org:** DSPy

**Track:** Harness Engineering &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 17m 11s

[Watch on YouTube](https://www.youtube.com/watch?v=GgLQ02aO-hs)

## Summary

Maxime Rivest and Isaac Miller of the DSPy project argue that AI programs should be built like functions: fix an input/output contract for a repeated task, then treat everything inside — prompt, model, agent loop, tools — as swappable implementation detail. They frame a fully specified task as three languages working together: instructions (specs) for what should happen, code for what must happen, and evals for what good looks like. Once a task is specified this way, optimization can be automated and delegated, which is how enterprises like Shopify reportedly cut costs dramatically by swapping an expensive model for a cheap one while keeping evals and business logic constant. The second half previews DSPy 4 work: dspy.flex, a module that learns a harness (code) rather than just few-shots or prompts, and qualitative learning, a research direction that converts textual feedback from production into evals automatically. The closing argument is that even AGI won't know your context or relationships, so 'last mile learning' against a fixed interface remains the durable engineering unit. Watch it for the conceptual framing and the DSPy roadmap; it is light on code detail and benchmarks.

## Key Points

- Treating a repeated AI task as a function with a fixed input/output signature makes it reusable, composable, testable, optimizable, and distributable as a black box.
- The parade of new models and techniques released every few weeks are just implementation tactics; putting them inside a fixed contract lets you try each one without touching integration code.
- A signature alone is insufficient to specify a task — you need three languages: natural-language instructions (what should happen), code (what must happen, as enforced constraints), and evals/examples (what good looks like).
- Code-level constraints exist precisely because model quality does not eliminate them: the speaker keeps a hard rule to escalate to a human on negative values even in an AGI world.
- Examples matter for latent, hard-to-articulate criteria — the maple tree analogy — and for the long tail of successful behaviors you cannot write down as instructions or code.
- DSPy's optimization target has evolved over time: from code-selected few-shot examples, to automatically optimized instructions, to learning the harness/code itself in dspy.flex.
- Shopify reportedly achieved a 550x cost reduction by moving from an expensive to a cheap model while keeping the same evals and iterating on business logic inside the boundary.
- Qualitative learning is an open research direction: use models to interpret textual feedback already present in production (traces, user actions, product analytics) and convert it into evals, rather than hand-building a proxy hill.
- New research techniques like recursive language models or GEPA can be adopted in one line without changing your signature, which is the practical payoff of the flexible-implementation ecosystem.

## Notable Quotes

> "in programming, if we want to repeat a task often, we make it a function. We believe the same should be true for AI programs."
>
> — [0:01](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=1s) &middot; *states the thesis of the whole talk in two sentences*

> "Functions are reusable, composable, testable, and optimizable."
>
> — [0:01](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=1s) &middot; *the property list that motivates the entire abstraction*

> "will any of these new specific techniques coming out at a different time really help on your task, on your job? Well, these are all just implementation tactics."
>
> — [1:48](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=108s) &middot; *takes a contrarian side against technique-chasing in a fast-moving field*

> "If for your repeated AI task, you define an input interface and an output interface, you get to play in the internals."
>
> — [1:48](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=108s) &middot; *the concrete mechanism behind the argument*

> "A new model comes out, and I can change that. It's super easy cuz my interface is fixed like that."
>
> — [3:12](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=192s) &middot; *grounds the abstraction in the model-churn problem everyone has*

> "when you fix that boundary, you can focus on the how on the top, and then inside of it, you can I have a little chat with just a simple prompt."
>
> — [3:48](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=228s) &middot; *describes the progression from prompt to agent to loop inside a stable boundary*

> "even before ChatGPT came out, the creator of DSPy had started to land on this idea that you need three things to specify your task."
>
> — [4:25](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=265s) &middot; *dates the specs/code/evals framing and claims priority for it*

> "if you have a friend over coming to play a board game with you, and you give them the instructions and they're ready to play. But if you want to do like AlphaGo or AlphaZero, and you tell them you're just going to learn from example, you're going to have a long night."
>
> — [5:49](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=349s) &middot; *argues instructions are far more sample-efficient than pure example-based learning*

> "There's some constraints you have that they have to be listened to. They have to be enforced. The best way to do that is with code."
>
> — [5:49](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=349s) &middot; *a clear position on where determinism belongs in an AI program*

> "This will not change. Like, even if I have AGI, I would hope it doesn't make mistake. But whatever is in the predictor, if they make these mistakes, I still want these things to be true."
>
> — [7:03](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=423s) &middot; *defends hard-coded constraints against the argument that better models make them obsolete*

> "when I was young, was on the farm with my dad, and I asked him, "How do you know that this tree is a maple?" And he couldn't tell me."
>
> — [7:03](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=423s) &middot; *the memorable analogy for why some criteria can only be taught by example*

> "It's also for all of the long tails in your specifications that are things that are more latent."
>
> — [7:38](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=458s) &middot; *generalizes the maple example to real production specs*

> "When you're flexible to what the implementation is, you can use the bitter lesson to search over different solutions, find something that solves your problem cheaply."
>
> — [9:02](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=542s) &middot; *connects the abstraction to a cost argument and to the bitter lesson*

> "Shopify, 550 times cheaper. They're able to do that because they went from an expensive model to a cheap model, but they could keep the same eval's, keep iterating on their business logic inside, and try new things."
>
> — [9:49](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=589s) &middot; *the talk's only hard number and its main enterprise evidence*

> "none of these techniques we add will definitely solve your problem, because that's your job. What we can do is we can solve sub problems for you that make your implementation easier."
>
> — [10:29](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=629s) &middot; *unusually candid about the limits of a framework*

> "Maybe it will, maybe it won't. But the thing is, it's one line, and your signature stays the same. That's what's important here."
>
> — [10:29](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=629s) &middot; *names the real value proposition as cheap experimentation, not any single technique*

> "In DSPy, when we let you optimize things, it started with few-shot examples. Then it became prompts. And now that's becoming code."
>
> — [11:10](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=670s) &middot; *compresses the framework's three-generation arc into one line*

> "If an email is good or bad, contains a lot less information than if you know what could change in that email in order to improve."
>
> — [11:51](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=711s) &middot; *the information-loss critique of scalar evals that motivates qualitative learning*

> "whenever you create a hill in a dataset, you're really trying to create a proxy for reality. What if instead we could use reality to inform our evals automatically?"
>
> — [11:51](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=711s) &middot; *states the qualitative learning research bet*

> "models are now good enough to interpret whatever textual feedback is present in the environment and convert that into evals and a hill that the model can climb."
>
> — [12:37](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=757s) &middot; *the load-bearing capability assumption behind the DSPy 4 direction*

> "even when we have an incredibly smart model, the model won't know how to solve your problems. It won't know how to do your tasks or have your context."
>
> — [14:02](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=842s) &middot; *the argument for why this work survives AGI*

> "Intelligence is very different from being all-knowing."
>
> — [14:02](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=842s) &middot; *the sharpest one-line formulation of the last-mile thesis*

> "you should hold your prompts, models, and code accountable to the problem that you need them to solve."
>
> — [15:32](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=932s) &middot; *the practical instruction the talk closes on*

## Positions

- Repeated AI tasks should be encapsulated as functions with fixed input/output interfaces, exactly as in traditional programming. ([0:01](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=1s), confidence: stated)
- New AI techniques, models, and strategies are implementation tactics that belong inside a fixed contract, not architectural decisions that reshape your program. ([1:48](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=108s), confidence: stated)
- A signature alone is not enough to specify a task well enough to automatically optimize it; you need instructions, code, and evals together. ([4:25](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=265s), confidence: stated)
- Hard constraints should be enforced in code rather than left to the model, because code is the best way to guarantee they hold. ([5:49](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=349s), confidence: stated)
- Natural-language instructions are dramatically more sample-efficient than teaching purely from examples. ([5:49](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=349s), confidence: implied)
- Code-level guardrails will remain necessary even with AGI-level models. ([7:03](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=423s), confidence: stated)
- Some specification criteria are latent and can only be conveyed through examples, not through instructions or code. ([7:03](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=423s), confidence: stated)
- Shopify achieved a 550x cost reduction by swapping an expensive model for a cheap one while keeping evals fixed. ([9:49](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=589s), confidence: stated)
- No framework technique will solve your problem for you; frameworks only solve sub-problems, and defining the problem remains the engineer's job. ([10:29](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=629s), confidence: stated)
- Scalar or binary evals discard information that richer, change-oriented feedback would preserve. ([11:51](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=711s), confidence: stated)
- Current models are good enough to convert textual production feedback into usable evals. ([12:37](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=757s), confidence: stated)
- Even a maximally intelligent model will not know your context, tasks, or relationships, so last-mile learning remains necessary. ([14:44](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=884s), confidence: stated)
- New techniques should be adopted only after data-driven evaluation against your specific business problem. ([15:32](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=932s), confidence: stated)

## Concepts

- [continual learning](../concepts/continual-learning.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [long-context processing](../concepts/long-context-processing.md)
- [model portability](../concepts/model-portability.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [prompt optimization](../concepts/prompt-optimization.md)

