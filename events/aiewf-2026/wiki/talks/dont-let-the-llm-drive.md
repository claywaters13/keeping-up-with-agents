---
title: "Don't Let the LLM Drive"
type: "talk"
slug: "dont-let-the-llm-drive"
org: "Microsoft"
video_id: "m24UKZomm7k"
duration_sec: 367
word_count: 990
speakers: ["Joel Allou", "Ornella Bahidika"]
---

# Don't Let the LLM Drive

**Speakers:** [Joel Allou](../speakers/joel-allou.md), [Ornella Bahidika](../speakers/ornella-bahidika.md)

**Org:** Microsoft

**Duration:** 6m 07s

[Watch on YouTube](https://www.youtube.com/watch?v=m24UKZomm7k)

## Summary

Ornella Bahidika and Joel Allou describe Ace, a live AI voice tutor that runs an entire lesson start to finish by removing the LLM from the control flow. Their argument is that multi-step agent unreliability — agents that declare themselves done, skip steps, or loop — is a control problem, not a prompting problem, and that piling on more prompt rules is the wrong first fix. Instead they model a lesson as an explicit state machine (intro, teach, check, grade, advance, wrap) where each step hands the model a narrow contract, the harness validates the output, and the harness alone decides what comes next. The payoff they report is not just reliability: with the harness carrying the state, they were able to swap a frontier model for Haiku 4.5 and still hit their bar, cutting cost and latency for a real-time voice product. Worth watching if you're deciding how much decision-making to leave inside the model in any multi-step agent — they claim the pattern generalizes to coding agents, ops runbooks, and onboarding flows.

## Key Points

- Multi-step agents fail in production in characteristic ways — the agent decides it's done early, skips a step, or loops — and demos systematically hide these failures.
- The speakers frame reliability as a control-flow problem rather than a prompting problem, so adding more rules to the prompt is treated as the wrong instinct.
- Their governing metaphor is that the model is the talent and the harness is the director: the model is good at delivering a line but bad at tracking which step it's on.
- Ace models a lesson as a small state machine with explicit steps (intro, teach, check, grade, advance, wrap), where each step gives the model a narrow contract to execute and return.
- The harness validates the model's returned output, advances state, and decides what happens next; the model proposes but never determines where the conversation is.
- Because the harness supplies the structure, a smaller model (Haiku 4.5) can substitute for a frontier model (Opus 4.7) and still meet the reliability bar, saving cost and latency — which matters for real-time voice.
- Ace externalizes three specific decisions from the model: whether the lesson is done, whether the student actually learned it, and what comes next.
- Their heuristic for adopting the pattern: if your agent's reliability is close to a coin flip, take the control flow out of the model.
- The speakers claim the pattern is domain-general — applicable to voice tutors, coding agents, ops runbooks, and onboarding flows alike.

## Notable Quotes

> "we built Ace, a live AI voice tutor that runs a full lesson start to finish reliably. The trick is LLM is not in charge."
>
> — [0:00](https://www.youtube.com/watch?v=m24UKZomm7k&t=0s) &middot; *States the product and the thesis in one breath.*

> "It's near the demo, then a real user gets in and halfway through the agent decide it's done. Or skip a step, or even loops. The demo never show you that."
>
> — [0:00](https://www.youtube.com/watch?v=m24UKZomm7k&t=0s) &middot; *Names the concrete failure mode the whole talk is organized around.*

> "the first fix everyone reaches for is prompt this harder, add more holes. But reliability was never a prompting problem. It's a control problem."
>
> — [0:00](https://www.youtube.com/watch?v=m24UKZomm7k&t=0s) &middot; *The central contrarian claim — prompting versus control.*

> "The model is the talent, and the harness is the director."
>
> — [0:00](https://www.youtube.com/watch?v=m24UKZomm7k&t=0s) &middot; *The talk's memorable framing device.*

> "The model is brilliant at delivering a line, but it's really terrible at remembering if it's on step three of six. So we stop asking it to."
>
> — [0:44](https://www.youtube.com/watch?v=m24UKZomm7k&t=44s) &middot; *Diagnoses precisely which capability the harness is compensating for.*

> "A lesson is a small state machine with intro, teach, check, grade, advance, and wrap."
>
> — [0:44](https://www.youtube.com/watch?v=m24UKZomm7k&t=44s) &middot; *The concrete architecture, enumerated.*

> "The harness validates what's comes back, advance the state, and decide what's next. The model never decide where we are. That's the design."
>
> — [0:44](https://www.youtube.com/watch?v=m24UKZomm7k&t=44s) &middot; *Defines the harness's exact responsibilities and the boundary it enforces.*

> "you see that oftentimes people leverage the model for essentially everything. For the thinking, for the processing, right? And for everything in between."
>
> — [0:44](https://www.youtube.com/watch?v=m24UKZomm7k&t=44s) &middot; *Characterizes the default practice they're arguing against.*

> "we had a need to actually build something that is reliable, something that is cost-effective, and something that is fast."
>
> — [1:37](https://www.youtube.com/watch?v=m24UKZomm7k&t=97s) &middot; *States the three constraints that motivate harness engineering here.*

> "instead of having a model that is really intelligent, sort of go through everything for us, we will build all of these steps that are needed and provide only the input required for the model to execute a specific scenario."
>
> — [1:37](https://www.youtube.com/watch?v=m24UKZomm7k&t=97s) &middot; *Clearest single definition of the harness-engineering approach.*

> "instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn't have as much reasoning capabilities, but because of the harnessing around it, it's still able to perform at the level in which we expect"
>
> — [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s) &middot; *The talk's key empirical payoff: harness structure substitutes for model capability.*

> "we see that there's harnessing for a section, which provides input to the model about exactly what to speak about, what to do. We have harnessing about drawing on the whiteboard. We have harnessing that deals with clearing the queue."
>
> — [3:16](https://www.youtube.com/watch?v=m24UKZomm7k&t=196s) &middot; *Shows the granularity at which harnessing is actually implemented.*

> "the model never really um has to think. It proposes, but ultimately it is the harness that decides."
>
> — [4:04](https://www.youtube.com/watch?v=m24UKZomm7k&t=244s) &middot; *The propose/decide split is the reusable design rule.*

> "when is the lesson done is one, right? Did the student actually get it right? Like, did they actually learn in the way they were supposed to?"
>
> — [4:04](https://www.youtube.com/watch?v=m24UKZomm7k&t=244s) &middot; *Enumerates the specific judgments they refused to delegate to the model.*

> "It's applicable to coding agents, to Ops Run Books. Um it's applicable to onboarding flows, right? The same rule applies"
>
> — [4:39](https://www.youtube.com/watch?v=m24UKZomm7k&t=279s) &middot; *The generalization claim beyond voice.*

> "If it's somewhat of a coin flip, then you want to take the control flow out of the model."
>
> — [5:17](https://www.youtube.com/watch?v=m24UKZomm7k&t=317s) &middot; *An actionable adoption heuristic.*

> "don't let the model talk, right? Or actually let it talk, but don't let it drive."
>
> — [5:17](https://www.youtube.com/watch?v=m24UKZomm7k&t=317s) &middot; *The title thesis, delivered as the closing line.*

## Positions

- Multi-step agent unreliability is a control problem, not a prompting problem, so adding more prompt rules is the wrong fix. ([0:00](https://www.youtube.com/watch?v=m24UKZomm7k&t=0s), confidence: stated)
- LLMs should never hold the state of a multi-step workflow — the harness must track and advance state. ([0:44](https://www.youtube.com/watch?v=m24UKZomm7k&t=44s), confidence: stated)
- Using a frontier model for the thinking, processing, and everything in between is common practice but ineffective for live voice tutoring. ([1:37](https://www.youtube.com/watch?v=m24UKZomm7k&t=97s), confidence: stated)
- A sufficiently strong harness lets a smaller model (Haiku 4.5) replace a frontier model (Opus 4.7) at the expected performance level, while saving money, time, and latency. ([2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s), confidence: stated)
- The model should only propose; the harness should decide. ([4:04](https://www.youtube.com/watch?v=m24UKZomm7k&t=244s), confidence: stated)
- Judgments like whether a task is complete, whether the user succeeded, and what step comes next should be engineered outside the model. ([4:39](https://www.youtube.com/watch?v=m24UKZomm7k&t=279s), confidence: stated)
- The harness pattern generalizes beyond voice agents to coding agents, ops runbooks, and onboarding flows. ([4:39](https://www.youtube.com/watch?v=m24UKZomm7k&t=279s), confidence: stated)
- When an agent's reliability approaches a coin flip, that is the signal to remove control flow from the model. ([5:17](https://www.youtube.com/watch?v=m24UKZomm7k&t=317s), confidence: stated)
- Demo conditions systematically fail to surface the step-skipping and looping failures that real users trigger. ([0:00](https://www.youtube.com/watch?v=m24UKZomm7k&t=0s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [durable execution](../concepts/durable-execution.md)
- [model routing](../concepts/model-routing.md)
- [output guardrails](../concepts/output-guardrails.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [small language models](../concepts/small-language-models.md)
- [task decomposition](../concepts/task-decomposition.md)
- [voice agents](../concepts/voice-agents.md)

