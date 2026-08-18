---
title: "Stop Burning Tokens: Why self-improvement needs domain expertise first"
type: "talk"
slug: "stop-burning-tokens-why-self-improvement-needs-domain-expertise-first"
org: "Langfuse"
video_id: "eAXxdtNlK04"
duration_sec: 1059
word_count: 3409
speakers: ["Annabell Schäfer"]
---

# Stop Burning Tokens: Why self-improvement needs domain expertise first

**Speakers:** [Annabell Schäfer](../speakers/annabell-schafer.md)

**Org:** Langfuse

**Duration:** 17m 39s

[Watch on YouTube](https://www.youtube.com/watch?v=eAXxdtNlK04)

## Summary

Annabell Schäfer (growth engineer at Langfuse) argues that the current enthusiasm for self-improving agent loops is borrowed from coding, where a clear target function — does the code compile — makes auto-optimization work, and that this doesn't transfer to domains like healthcare, compliance, or support chatbots without deliberate work. To isolate the role of the target function, her team ran a minimal self-optimization loop: a cheap GPT-5-nano classifier labeling arXiv papers, with Claude Opus 4.8 in Claude Code proposing prompt updates against fit/validate/test splits of 200/100/300 items. Accuracy rose from 68% to about 83% and generalized to 80.2% on the held-out test set, but roughly 10 points of the gain came on the very first iteration — the payoff came from having a high-signal, clearly quantifiable failure signal, not from many loop iterations. She then generalizes: replace vague 0–1 scores like correctness or helpfulness with binary, domain-specific checks (is the answer grounded in the retrieved context, is the brand name spelled right, which of five known failure modes occurred), derived by sitting with domain experts and reviewing production data as a human. Worth watching if you're deciding whether to invest in agent self-improvement loops versus first building the evaluation substrate they depend on.

## Key Points

- Coding agents made self-improvement look easy because they inherited an unusually clean target function — whether the code compiles — that most domains simply do not have.
- Any target you hand an agent is inherently incomplete, so the optimization can converge confidently on the wrong destination.
- In a controlled experiment on arXiv paper classification (GPT-5-nano classifier, Claude Opus 4.8 as optimizer via Claude Code), accuracy went from a 68% baseline to ~83%, plateauing around 80% and reaching 80.2% on a 300-item untouched test set.
- Roughly 10 of the ~15 percentage points of improvement arrived on the first iteration, suggesting the value came from the quality of the error signal rather than from prolonged looping.
- Even a supposedly clean label set was noisy in practice, because arXiv authors have creative freedom in choosing a primary category, capping achievable accuracy.
- Generic scalar evaluators (correctness, helpfulness, hallucination on a 0–1 or 1–5 scale) are low-signal for auto-improvement because the numeric levels are rarely defined and scores are inconsistent across runs.
- The replacement is binary, application-specific quality criteria — is the claim present in the retrieved context, was the brand name preserved, which known failure mode fired — plus enough volume of examples to give the optimizer a pattern to cluster on.
- Getting there requires encoding domain expertise into concrete examples with experts, reviewing production data as a human rather than delegating it to coding agents, and baking in ML-style validation splits and an escape hatch so the loop stops instead of burning tokens against a wall.

## Notable Quotes

> "So we have Boris Journey saying he doesn't write any prompts anymore. He has loops and Peter Steinberger being like you should be designing loops and not prompt your agents."
>
> — [0:00](https://www.youtube.com/watch?v=eAXxdtNlK04&t=0s) &middot; *Frames the industry moment the talk is pushing back on.*

> "a target that you give an agent is actually also always incomplete"
>
> — [1:10](https://www.youtube.com/watch?v=eAXxdtNlK04&t=70s) &middot; *The core theoretical claim underpinning the whole argument.*

> "So we put this target function together with an agent and also with an optimizer."
>
> — [3:07](https://www.youtube.com/watch?v=eAXxdtNlK04&t=187s) &middot; *States the experimental setup in one line.*

> "Um the first run ended at uh 68% accuracy and on our third fourth iteration um we went all the way to 83% which then also afterwards um plateaued a bit."
>
> — [7:12](https://www.youtube.com/watch?v=eAXxdtNlK04&t=432s) &middot; *The headline numbers of the experiment.*

> "we also saw this uh improvement then generalized to the um test data set on yeah to 80.2%."
>
> — [7:50](https://www.youtube.com/watch?v=eAXxdtNlK04&t=470s) &middot; *Reports the held-out generalization result.*

> "the most interesting thing uh we thought is that the first iteration immediately gained 10% and then it was only a little bit movement."
>
> — [7:50](https://www.youtube.com/watch?v=eAXxdtNlK04&t=470s) &middot; *The central empirical surprise driving the talk's thesis.*

> "so overall the approach was um improvement loop added rules and examples"
>
> — [9:20](https://www.youtube.com/watch?v=eAXxdtNlK04&t=560s) &middot; *Summarizes what the optimizer actually changed in the prompt.*

> "it got a very clearcut um clearly quantifiable and reliable failure mode because they were just wrong on a yes no right wrong basis."
>
> — [10:36](https://www.youtube.com/watch?v=eAXxdtNlK04&t=636s) &middot; *Names the precondition that made auto-optimization work.*

> "but the biggest jump was uh just the very first one from a very clear-cut signal, we could have probably stopped there and already have very good baseline."
>
> — [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s) &middot; *A pointed tradeoff claim about diminishing returns from looping.*

> "next time you run the same evaluator you get a different answer from the same kind of evaluation you ran"
>
> — [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s) &middot; *States the nondeterminism problem that blocks transfer to other domains.*

> "for this to really work properly you need to define each of those numbers. What does it mean in which context would you need which number?"
>
> — [12:12](https://www.youtube.com/watch?v=eAXxdtNlK04&t=732s) &middot; *The concrete objection to scalar rubric evaluators.*

> "So it's just choosing a number between zero and one and um depending on the uh context it might just uh totally change perspective and is therefore rather low signal and also probably inconsistent um across runs."
>
> — [12:51](https://www.youtube.com/watch?v=eAXxdtNlK04&t=771s) &middot; *Sharpest critique of the market-standard evaluator pattern.*

> "Uh so for example instead of correctness the answer is based on the knowledge base yes no."
>
> — [12:51](https://www.youtube.com/watch?v=eAXxdtNlK04&t=771s) &middot; *The prescriptive replacement, stated concretely.*

> "because if you can't do code compiles, you need to wrap your head a little bit differently around um what is good and what is not."
>
> — [14:22](https://www.youtube.com/watch?v=eAXxdtNlK04&t=862s) &middot; *One-line statement of the talk's thesis.*

> "Um but here it's something you can actually start to encode the domain expertise into very concrete examples."
>
> — [15:00](https://www.youtube.com/watch?v=eAXxdtNlK04&t=900s) &middot; *Explains what 'talk to your experts' should concretely produce.*

> "review this data and don't review it only with your coding agents but review it as a human."
>
> — [15:49](https://www.youtube.com/watch?v=eAXxdtNlK04&t=949s) &middot; *A direct process prescription others might dispute.*

> "for this to properly generalize, you need to uh bake in mechanisms for validation."
>
> — [16:23](https://www.youtube.com/watch?v=eAXxdtNlK04&t=983s) &middot; *Ties agent loops back to traditional ML discipline.*

> "giving the system an escape hatch instead of having it work for hours and hours uh hitting a wall and uh burning tokens."
>
> — [16:23](https://www.youtube.com/watch?v=eAXxdtNlK04&t=983s) &middot; *The titular point, stated as a design requirement.*

## Positions

- Auto-improvement loops worked first in coding because compilation gives an unusually clear target function, not because loops generalize well. ([0:37](https://www.youtube.com/watch?v=eAXxdtNlK04&t=37s), confidence: stated)
- Any target function given to an agent is always incomplete, so optimizing against it can head toward the wrong optimum. ([1:10](https://www.youtube.com/watch?v=eAXxdtNlK04&t=70s), confidence: stated)
- Teams that invest in capturing their target function and building good evaluators are the ones that continuously improve their applications and ship with confidence. ([1:58](https://www.youtube.com/watch?v=eAXxdtNlK04&t=118s), confidence: stated)
- A single-label classification task with ground-truth labels is the clearest-cut target function available for testing auto-optimization. ([2:36](https://www.youtube.com/watch?v=eAXxdtNlK04&t=156s), confidence: stated)
- The prompt optimization loop improved accuracy from 68% to about 83% on fit/validate and 80.2% on a 300-item unseen test set. ([7:50](https://www.youtube.com/watch?v=eAXxdtNlK04&t=470s), confidence: stated)
- Most of the gain from a self-improvement loop comes from the first iteration when the failure signal is clear; you could have stopped there. ([11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s), confidence: stated)
- Almost no real-world application has deterministic yes/no target functions, and LLM-as-a-judge evaluators return different answers across runs. ([11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s), confidence: stated)
- Generic evaluators like correctness, helpfulness, and hallucination scored on a 0-1 or 1-5 scale are low-signal for auto-improvement because the levels are almost never defined. ([12:12](https://www.youtube.com/watch?v=eAXxdtNlK04&t=732s), confidence: stated)
- Binary, domain-specific checks (groundedness in retrieved context, brand-name correctness, categorization into known failure modes) are the right substitute for scalar quality scores. ([12:51](https://www.youtube.com/watch?v=eAXxdtNlK04&t=771s), confidence: stated)
- Roughly a few hundred labeled examples were enough to produce high-signal feedback, though the needed volume depends on application complexity. ([14:22](https://www.youtube.com/watch?v=eAXxdtNlK04&t=862s), confidence: stated)
- Domain experts should be used to create concrete examples and surface implicit decision criteria, which then become the high-signal evaluators. ([15:00](https://www.youtube.com/watch?v=eAXxdtNlK04&t=900s), confidence: stated)
- Production data must be reviewed by humans, not only by coding agents, because failure modes and usage shift over time. ([15:49](https://www.youtube.com/watch?v=eAXxdtNlK04&t=949s), confidence: stated)
- Optimization loops need traditional-ML validation mechanisms plus an explicit escape hatch to avoid burning tokens against a plateau. ([16:23](https://www.youtube.com/watch?v=eAXxdtNlK04&t=983s), confidence: stated)
- Noise in the ground-truth labels themselves (authors' creative freedom in choosing arXiv categories) caps how high accuracy can go, so plateaus are not purely a model failure. ([7:12](https://www.youtube.com/watch?v=eAXxdtNlK04&t=432s), confidence: implied)

## Concepts

- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [offline evaluation](../concepts/offline-evaluation.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [requirements elicitation](../concepts/requirements-elicitation.md)
- [reward design](../concepts/reward-design.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)

