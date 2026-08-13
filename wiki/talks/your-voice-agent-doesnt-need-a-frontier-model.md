---
title: "Your Voice Agent Doesn't Need a Frontier Model"
type: "talk"
slug: "your-voice-agent-doesnt-need-a-frontier-model"
track: "Claws & Personal Agents"
org: "Microsoft"
day: "Day 2 — Session Day 1"
room: "Track 6"
video_id: "fnLBmfsI_Fg"
duration_sec: 344
word_count: 893
speakers: ["Neil Zeghidour"]
---

# Your Voice Agent Doesn't Need a Frontier Model

*Program title: Your Voice Agent is Just a Walkie-Talkie*

**Speakers:** [Neil Zeghidour](../speakers/neil-zeghidour.md)

**Org:** Microsoft

**Track:** Claws & Personal Agents &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 6 &nbsp;|&nbsp; **Duration:** 5m 44s

[Watch on YouTube](https://www.youtube.com/watch?v=fnLBmfsI_Fg)

## Summary

Ornella Bahidika and Joel Allou describe Ace, a live AI voice tutor built deliberately on a small model rather than a frontier one. Their argument is that voice agents are constrained by latency, not intelligence: the model must begin speaking within roughly 950 milliseconds, and a frontier model that reasons for a second has already broken the illusion of conversation. Their fix is to move all the thinking — lesson sequencing, mastery tracking, what to display, how to answer — out of the model and into a state machine plus an intelligence layer in code, handing the model a per-turn summary and leaving it only the job of talking. They show a side-by-side demo: a reasoning frontier model takes several seconds, while the scaffolded Haiku 4.5 setup responds in about 900ms. They are honest about the cost — small models drift over long structure without strict rules — but argue that scaffolding is paid once in code rather than on every turn. Worth watching if you are building real-time voice, low-latency, or high-volume LLM systems and are deciding how much intelligence belongs inside the model.

## Key Points

- For voice agents the binding constraint is latency rather than reasoning quality — the team targets the model starting to speak in about 950 milliseconds, because a longer pause makes users perceive the agent as dead.
- Their architecture strips lesson control flow, student-knowledge tracking, and explanation-sequencing out of the model and into a state machine, leaving the model responsible only for speaking.
- A separate intelligence layer on top of the state machine derives student mastery and decides when a lesson step is complete, so pedagogical decisions never depend on model reasoning.
- The model receives a summary of state on every turn and simply verbalizes the output computed elsewhere in code.
- In their demo, an unscaffolded frontier model (referred to as Opus 4.7) takes several seconds to answer the same question that the scaffolded Haiku 4.5 setup answers in about 900 milliseconds.
- The tradeoff is real: small models drift on long-form structure without scaffolding and require strict rules to stay organized.
- They frame scaffolding cost as a one-time engineering expense paid in code, versus reasoning cost paid on every single turn.
- Their general rule is to pick the fastest model the latency budget allows and invest remaining effort in scaffolding, which they argue generalizes to real-time and high-volume applications where the model is the smallest part of the system.

## Notable Quotes

> "Because our budget was never IQ, it's millisecond."
>
> — [0:00](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=0s) &middot; *Compresses the talk's entire thesis into one line.*

> "When a voice agent pause for even a second, your brain says it's dead."
>
> — [0:00](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=0s) &middot; *States the perceptual reason latency dominates in voice.*

> "The AI model need to start talking in about 950 milliseconds."
>
> — [0:00](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=0s) &middot; *A concrete, checkable latency budget.*

> "A frontier model that think for a full second has already lost the room, no matter how good the answer is."
>
> — [0:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=51s) &middot; *The core contrarian claim against frontier models in voice.*

> "So, we made the model small and took the hardest part jobs away from it."
>
> — [0:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=51s) &middot; *Names the architectural move in one sentence.*

> "What's left for the model is one thing it's really good at, talking."
>
> — [0:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=51s) &middot; *Defines the narrowed role of the model.*

> "But that is actually precisely the problem. Because the reasoning can take couple of seconds and those seconds are really valuable when you are building voice applications."
>
> — [1:38](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=98s) &middot; *Reframes model reasoning capability as a liability, not an asset.*

> "So all of the thinking is extracted into a state machine."
>
> — [1:38](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=98s) &middot; *Names the specific mechanism replacing model reasoning.*

> "So everything when it comes to what happens next, when it comes to what needs to be displayed, when it comes to how to actually answer a question, it's all done outside of the model."
>
> — [2:27](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=147s) &middot; *Enumerates exactly which decisions leave the model.*

> "Same question, but now you see that the answer comes in about 900 milliseconds."
>
> — [3:11](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=191s) &middot; *The measured result of the architecture.*

> "by removing all of the thinking, all of the logic, all of the reasoning from the model and actually putting it within the code, we actually saves a lot of time and allows us to use smaller models which are cost effective and actually better at real-time voice applications"
>
> — [3:11](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=191s) &middot; *States the full claimed payoff: latency, cost, and fit.*

> "A small model like the Haiku 4.5, if it doesn't have any scaffolding, tend to drift on long structure and really needs strict rules in order to be able to stay organized."
>
> — [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s) &middot; *The honest downside of the approach, named specifically.*

> "So the scaffolding piece is the price. But the good thing is you pay it once and in code, right? Not on every single turn."
>
> — [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s) &middot; *Frames the cost tradeoff as one-time versus per-turn.*

> "Pick the fastest model that your latency budget allows and then spend the rest of your time actually building the scaffolding."
>
> — [4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s) &middot; *The talk's transferable design rule.*

> "In those cases, the model is the smallest part of the system."
>
> — [4:53](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=293s) &middot; *Generalizes the architecture beyond voice.*

## Positions

- A voice agent must begin speaking within roughly 950 milliseconds or users perceive the conversation as broken. ([0:00](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=0s), confidence: stated)
- Frontier models are the wrong choice for voice agents because their reasoning latency costs more than their answer quality gains. ([0:51](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=51s), confidence: stated)
- Control flow, state tracking, and answer selection should live in application code (a state machine), not in the model. ([1:38](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=98s), confidence: stated)
- With this scaffolding, Haiku 4.5 responds in about 900 milliseconds versus several seconds for an unscaffolded reasoning frontier model on the same question. ([3:11](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=191s), confidence: stated)
- Small models without scaffolding drift on long structured interactions and require strict rules to stay organized. ([4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s), confidence: stated)
- Scaffolding is a one-time cost paid in code, whereas model reasoning is a cost paid on every turn, making scaffolding the better investment. ([4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s), confidence: stated)
- Teams should select the fastest model their latency budget permits and spend remaining engineering effort on scaffolding. ([4:01](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=241s), confidence: stated)
- This architecture generalizes beyond voice to any real-time or high-volume application, where the model should be the smallest part of the system. ([4:53](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=293s), confidence: stated)
- Using a small model is not a quality compromise when the surrounding system does the thinking. ([0:00](https://www.youtube.com/watch?v=fnLBmfsI_Fg&t=0s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [context compaction](../concepts/context-compaction.md)
- [durable execution](../concepts/durable-execution.md)
- [latency budgets](../concepts/latency-budgets.md)
- [model routing](../concepts/model-routing.md)
- [small language models](../concepts/small-language-models.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)
- [voice agents](../concepts/voice-agents.md)

