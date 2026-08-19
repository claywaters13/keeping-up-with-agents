---
title: "The 1% Rule for Building in AI"
type: "talk"
slug: "the-1-rule-for-building-in-ai"
org: "Google"
video_id: "CxXgV54KzpQ"
duration_sec: 3427
word_count: 9671
speakers: ["Jeff Dean"]
---

# The 1% Rule for Building in AI

**Speakers:** [Jeff Dean](../speakers/jeff-dean.md)

**Org:** Google

**Duration:** 57m 07s

[Watch on YouTube](https://www.youtube.com/watch?v=CxXgV54KzpQ)

## Summary

Jeff Dean, in a fireside at YC Startup School 2026, walks from Google's hardware history (the napkin math behind the TPU, MapReduce, distillation) to concrete advice on what founders should build in 2026. His central founder heuristic is a filter on problem selection: pick problems where today's general models succeed 0% or 1% of the time, because a 20% success rate signals the capability is emerging and frontier models will absorb it within six to twelve months. He argues the binding constraints in AI systems are increasingly energy and data movement rather than model quality, that specialized low-latency inference hardware is the next big opening, and that automated experiment loops — propose, implement, evaluate, iterate — will drive ML and scientific progress. On the human side, he claims taste (choosing what to point agents at) is the scarce skill once agents write the code, and that clear specs matter more, not less, in the agent era. Worth watching for anyone deciding what to build against a frontier lab, or thinking about hardware, agent orchestration, or AI-for-science loops.

## Key Points

- The practical test for durable startup ideas is to probe general models on your problem: near-total failure (0-1% success) is a good sign, while partial success (~20%) suggests the frontier will cover it within six to twelve months.
- Dean expects the next major shift to be automated ML research loops, where systems decompose problems into subproblems, run many experiments automatically, and integrate results — extending to any domain with a measurable objective.
- Agent-based systems can already run for days or weeks on some problem domains, and Dean thinks most people have not internalized how big a deal that is.
- Inference, not training, is where he sees the most hardware headroom: minimizing data movement, committing to a small set of low precisions, and chasing latency improvements on the order of 50x.
- Moving data from accelerator memory into the processor costs roughly a thousand times more energy than the arithmetic itself, which is why batching exists — an energy/IO constraint founders often misread as a model problem.
- The TPU came from back-of-the-envelope math in 2013: if users dictated three minutes a day to a newly accurate speech model, Google would have to double its server fleet; the resulting chip was 30-80x more energy efficient and 20-30x lower latency than contemporary CPUs and GPUs.
- Context engineering — skills, guidelines, tool definitions, retrieval — is how outsiders improve model behavior without touching parameters, and Dean gives a concrete example of a skill he and Sanjay Ghemawat wrote to automate a microbenchmark measure-change-remeasure loop.
- Once agents write the code, the scarce skill is taste in choosing what to work on, which Dean says models are not likely to be good at; he suggests building it by writing down predictions for the next 12 months and grading yourself.
- Learned surrogate evaluators can restructure entire research loops: a neural approximation to a density functional theory simulator ran 300,000 times faster while staying nearly as accurate, turning an overnight computation into something that screens 10 million candidates over lunch.
- Frontier models see roughly a thousand times more data than a human does by age 18 yet are only on par in many things, which Dean names as an open invitation to invent far more data-efficient and continually learning algorithms.

## Notable Quotes

> "look for something where the model succeeds 0% or 1% of the time not not 20%"
>
> — [28:01](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1681s) &middot; *the title heuristic, stated as a hard numeric filter for idea selection*

> "If they're kind of able to do some of it but not very well, that's maybe not a great sign because that's a probably a a sign that the capability is starting to be present in those models"
>
> — [28:01](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1681s) &middot; *explains the counterintuitive logic behind the 1% rule*

> "I would also caution that the general models are definitely getting better at a broader and broader range of things"
>
> — [26:37](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1597s) &middot; *the durability warning a founder building on a model gap needs to hear*

> "the most important thing is to pick something you're super excited about and want to build and you think would be useful in the world"
>
> — [27:15](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1635s) &middot; *his stated number-one selection criterion, placed above any market analysis*

> "for some problem domains and with highly capable models underlying them you can get them to run for days or weeks and do really really complicated tasks"
>
> — [4:21](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=261s) &middot; *his answer for the widely held assumption that is already false*

> "everyone is now realizing that inference is the key to making you know these agent-based systems be available to more and more people and that latency is really important"
>
> — [3:17](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=197s) &middot; *frames inference hardware as the current 'it fits in memory' moment*

> "30 to 80 times more energy efficient than CPUs and GPUs of the day and also much much lower latency like 20 to 30x lower latency"
>
> — [7:44](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=464s) &middot; *the payoff numbers from the original TPU bet*

> "they were computationally expensive compared to the old speech system but they haved the error rate. So that was like the equivalent of 20 years of advances in speech recognition in just a few months"
>
> — [6:59](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=419s) &middot; *the capability jump that forced the napkin math behind the TPU*

> "if you didn't have that thousandx difference then you know you wouldn't have to do batching but you have to do batching of you know many examples or maybe many tokens at once in order to amortize that data movement"
>
> — [12:47](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=767s) &middot; *names batching as an artifact of energy economics rather than a modeling choice*

> "you can actually make the model work better and succeed at that kind of problem by not just adjusting the model parameters which is hard to do from the outside but from you know creating better guidelines for the model"
>
> — [18:34](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1114s) &middot; *the case for context engineering as the lever available to teams without training compute*

> "we actually published a document maybe a few months ago called performance hints that Sanjay and I wrote that's like a 30-page document about you know various kinds of performance tricks"
>
> — [21:12](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1272s) &middot; *a concrete, publicly available artifact people are already feeding to models*

> "that's a very very useful general technique is you know inference time compute to perform search over plausible ways of solving the problem"
>
> — [24:10](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1450s) &middot; *his prescription for agents that go off the rails at step 30*

> "you can ask today's models to translate software from one computer language to another very effectively because in that case you actually have a incredibly detailed specification"
>
> — [32:23](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1943s) &middot; *sharp illustration of why spec clarity, not model capability, gates agent success*

> "it's really having incredibly good taste in what you ask your agents to work on"
>
> — [33:57](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2037s) &middot; *his direct answer to what becomes scarce when agents write all the code*

> "a researcher can have all the tools and all the techniques, but often most of the battle is what problem are you gonna spend your time on?"
>
> — [33:57](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2037s) &middot; *grounds the taste claim in his own research experience*

> "basically a interesting thought experiment is what would happen if you tried to build a system out of transistors that might have you know 20 errors per day"
>
> — [38:26](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2306s) &middot; *a worked example of the assumption-questioning method he recommends*

> "So this is now a validation device, but instead of it taking a night, they made something that was 300,000 times faster"
>
> — [45:16](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2716s) &middot; *quantifies how learned surrogates collapse the cost of an experimental loop*

> "effectively you want to optimize you know your discoveries per unit of compute input"
>
> — [47:02](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2822s) &middot; *compact statement of the objective function for automated research*

> "when we wrote the paper we actually saw this was a super important problem because we knew making cheaper highly capable models from larger scale models was something we desperately wanted to do"
>
> — [48:50](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2930s) &middot; *the conviction behind a distillation paper that reviewers called unlikely to have significant impact*

> "If you think about our large scale models today, they probably see a thousand times as much data as a human does by the age of 18. Yet, the human by the age of 18 is better in a lot of things"
>
> — [55:50](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=3350s) &middot; *frames data efficiency as the biggest open algorithmic gap*

> "you also want to find people that are people you delight being around, right? because you're going to spend a lot of time around people working on really hard problems and you want people who are low ego that are team players"
>
> — [53:15](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=3195s) &middot; *his hiring criterion for small teams, weighted alongside raw skill*

> "ask yourself if I work on this problem and the best possible outcome happens you know will the world be a lot better in some way or will the world go eh that's kind of cool but whatever"
>
> — [52:40](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=3160s) &middot; *a usable test for whether a startup idea is worth years of your life*

## Positions

- The 2025 prediction that AI is at the level of a junior engineer has held up, and complex-task capability grew faster than Dean expected. ([0:46](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=46s), confidence: stated)
- By 2027 the big shift will be automated ML self-improvement: systems decomposing problems into subproblems and running tight automated experimentation loops. ([1:41](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=101s), confidence: stated)
- Any domain with a measurable objective is now amenable to rapid automated progress. ([2:30](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=150s), confidence: stated)
- Specialized inference hardware can be more energy efficient and lower latency than general-purpose devices including GPUs and TPUs, and that is where the next wave of systems work lies. ([3:17](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=197s), confidence: stated)
- Agents can run for days or weeks on some problem domains today, and most people have not internalized this. ([4:21](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=261s), confidence: stated)
- The first TPU was 30-80x more energy efficient than contemporary CPUs and GPUs and 20-30x lower latency. ([7:44](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=464s), confidence: stated)
- TPUs were deliberately built as general-purpose linear algebra machines rather than over-specialized ones, because ML algorithms were still evolving — which is why they survived the arrival of transformers. ([8:30](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=510s), confidence: stated)
- Moving data into the processor costs about 1000x more energy than computing on it, and batching exists to amortize that cost rather than for modeling reasons. ([12:47](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=767s), confidence: stated)
- There is substantial room to specialize hardware for inference beyond what exists today, particularly by fixing a small set of very low precisions in hardware. ([14:49](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=889s), confidence: stated)
- Information in a model's context is far clearer to the model than knowledge absorbed into parameters during training. ([16:57](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1017s), confidence: stated)
- Agents fail around step 10 or beyond mainly because they drift off the distribution of tasks they were trained on, and skills plus hints keep them on the well-lit path. ([22:32](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1352s), confidence: stated)
- Multi-agent search with an evaluator model, spending inference-time compute over candidate solutions, materially improves reliability in long-running agent flows. ([24:10](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1450s), confidence: stated)
- Small teams can beat general models in narrow domains via a well-designed surface, targeted skills, or a specialized model, but must check whether the gap is durable for years rather than months. ([26:37](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1597s), confidence: stated)
- Founders should pick problems where general models succeed 0% or 1% of the time; roughly 20% success means the capability is emerging and will improve with scale or data. ([28:01](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1681s), confidence: stated)
- Access to data the general model cannot see — for example a user's own personal information — is a real advantage for a product. ([29:31](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1771s), confidence: stated)
- AlphaFold-shaped bets — narrow, highly accurate, affordably trained domain models — remain viable in areas like material science and chip design. ([31:03](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1863s), confidence: stated)
- The importance of writing a clear specification has gone up in the agent era, not down, because agents have less ability than a human colleague to ask clarifying questions. ([32:23](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1943s), confidence: stated)
- Cross-language code translation is a task today's models do extremely well, precisely because the existing source code is an exhaustive specification. ([33:18](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1998s), confidence: stated)
- Taste — knowing what to point agents at — becomes the scarce skill, and models are not necessarily going to be good at it. ([34:44](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2084s), confidence: stated)
- Taste can be trained deliberately by writing down what you think will matter in 12 months and later grading which predictions came true. ([35:23](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2123s), confidence: stated)
- Chip design's 60-year assumption of near-perfect transistors is worth questioning; reliability could be handled at a higher level as it is in distributed storage systems. ([37:38](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2258s), confidence: stated)
- Fast learned approximations to expensive simulators — one was 300,000x faster and nearly as accurate as density functional theory — change what science is feasible. ([45:16](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2716s), confidence: stated)
- There is no real impediment to making the model-improvement research loop largely automated, with humans nudging at the highest level. ([47:02](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2822s), confidence: stated)
- Distillation, whose paper was rejected as unlikely to have significant impact, is part of why Gemini Flash models are so capable for their size and speed. ([48:50](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=2930s), confidence: stated)
- Frontier models see about a thousand times more data than a human does by age 18 yet are only on par in many respects, so far more data-efficient and continually learning algorithms are possible. ([55:50](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=3350s), confidence: stated)
- Hiring for small teams should weight low ego, complementary skills, and enjoyment of each other's company alongside raw technical ability. ([53:15](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=3195s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [agentic science](../concepts/agentic-science.md)
- [ai compute infrastructure](../concepts/ai-compute-infrastructure.md)
- [context engineering](../concepts/context-engineering.md)
- [contrarian conviction](../concepts/contrarian-conviction.md)
- [evaluation as competitive moat](../concepts/evaluation-as-competitive-moat.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [research taste](../concepts/research-taste.md)
- [startup timing and problem selection](../concepts/startup-timing-and-problem-selection.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)
- [the bitter lesson](../concepts/the-bitter-lesson.md)

