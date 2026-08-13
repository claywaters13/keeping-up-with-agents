---
title: "Build AI Systems for Discernment, Not Approval"
type: "talk"
slug: "build-ai-systems-for-discernment-not-approval"
org: "Duolingo"
video_id: "CDqzWpwkSls"
duration_sec: 1553
word_count: 4325
speakers: ["Angel Ortmann Lee"]
---

# Build AI Systems for Discernment, Not Approval

**Speakers:** [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)

**Org:** Duolingo

**Duration:** 25m 53s

[Watch on YouTube](https://www.youtube.com/watch?v=CDqzWpwkSls)

## Summary

Angel Ortmann Lee, a security engineer on the Duolingo English Test, argues that most human-in-the-loop AI fails not because the model or the reviewer is bad, but because the interaction was never designed to require thinking. She presents an internal experiment in which expert proctors — who score above 90% on accuracy calibration — accepted 50% of deliberately fabricated cheating flags, a coin-flip rate she reads as automation bias. The fix was not a model change or a UI rebuild but a copy change to the proctoring guidelines telling reviewers the AI signal is only a preliminary alert and that they must find independent evidence in the video before upholding a flag; rejection rates moved 21%. From there she generalizes: the human-AI loop is cyclical rather than linear, every interaction is already a training label, and interfaces that elicit rubber-stamping poison the data that trains the next model. The talk is worth watching for the concrete experiment plus design principles — match friction to stakes, split conflated yes/no questions, capture the diff when a human overrides — illustrated with headphone detection, a writing tutor, and coding agents.

## Key Points

- A Wharton study on "cognitive surrender" found human performance rose 25 percentage points when the AI was right and fell 15 when it was wrong, with 80% of participants accepting AI answers even when those answers were wrong.
- In Duolingo's own study, proctors who consistently calibrate above 90% accuracy upheld 50% of fabricated copy-typing flags on sessions with no cheating at all — a coin-flip rate diagnostic of automation bias, not of reviewer skill.
- The failure was isolated to the interface rather than the model (1% false positive rate) or the people (highly trained proctors), so the intervention targeted the interaction loop.
- A pure copy change — telling proctors the AI signal is preliminary, that they are the final decision-maker, and that they must find independent corroborating evidence in the footage — shifted rejection rates by 21% with no model or UI work.
- The human-in-the-loop pipeline is cyclical, not linear: model output shapes interaction, interaction shapes human behavior, and that behavior becomes the eval and training data for the next model, so rubber-stamped approvals get logged as ground truth and inflate model confidence.
- Conflated calls-to-action corrupt labels: a single yes/no on "headphones detected — flag?" mixes a perception question with a policy question, so a hearing-aid case forces a "no" that wrongly teaches the model it mispredicted.
- Friction should be matched to stakes — deliberate review gates and speed bumps for high-consequence decisions like exam proctoring, near-frictionless flow for low-oversight consumer chat experiences.
- Coding agents that either dump a giant diff or ping for approval on every file both reduce the developer to a rubber stamp and yield only thin accepted/rejected binaries; an agent that plans, surfaces assumptions, and ships reviewable PRs generates structured data about bad assumptions, tradeoffs, and stylistic preferences.
- Systems that log a yes/no but not the subsequent manual edit capture a false positive signal; measuring the diff between what the AI proposed and what the human shipped is where the real signal lives.

## Notable Quotes

> "When a human foregoes deliberation and adopts AI output as their own with minimal scrutiny."
>
> — [2:14](https://www.youtube.com/watch?v=CDqzWpwkSls&t=134s) &middot; *The talk's operating definition of cognitive surrender, the phenomenon everything else responds to.*

> "For example, for questions where the AI was right, the human performance increased by 25 percentage points. Whereas when the AI was wrong, it decreased by 15."
>
> — [2:14](https://www.youtube.com/watch?v=CDqzWpwkSls&t=134s) &middot; *Quantifies the asymmetric amplification effect of deferring to AI.*

> "Most interestingly, they saw that 80% of participants were accepting those AI answers even when they were wrong."
>
> — [3:11](https://www.youtube.com/watch?v=CDqzWpwkSls&t=191s) &middot; *The external benchmark that motivated Duolingo's replication.*

> "So, for experiments, we wanted to answer the question, would a skilled reviewer catch a false alarm or would they just rubber stamp it?"
>
> — [4:56](https://www.youtube.com/watch?v=CDqzWpwkSls&t=296s) &middot; *States the experimental question in one line.*

> "despite the fact that our human reviewers are consistently scoring above 90% on their accuracy calibration metrics, they actually accepted 50% of these fake signals"
>
> — [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s) &middot; *The headline result: expert calibration did not survive contact with a fabricated AI flag.*

> "And this coin flip rate is something that is a strong suggestion of automation bias."
>
> — [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s) &middot; *Names the diagnosis the number supports.*

> "We knew that the problem was not the model. Our model has a 1% false positive rate, and also these were sessions that were negatively predicted."
>
> — [7:03](https://www.youtube.com/watch?v=CDqzWpwkSls&t=423s) &middot; *Rules out the model, which is what makes the interface the target.*

> "First, the AI signal is just a preliminary alert. They're the final decision-maker."
>
> — [7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s) &middot; *The exact copy change that produced the effect.*

> "This simple copy change led a 21% increase in rejection rates"
>
> — [7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s) &middot; *Reports the intervention's measured effect size.*

> "As an AI engineer, your interaction loop determines how effective your AI system is and also what you can learn from it."
>
> — [8:27](https://www.youtube.com/watch?v=CDqzWpwkSls&t=507s) &middot; *The generalizable thesis stated directly to the engineering audience.*

> "You can't really change the way a human behaves unless you are that human. But, what you can do is tweak that interaction such that it can elicit different results from that human behavior."
>
> — [9:11](https://www.youtube.com/watch?v=CDqzWpwkSls&t=551s) &middot; *The core leverage argument: design the interaction, not the person.*

> "Think of your structured interactions as a system property that specifically yields high-quality data."
>
> — [9:56](https://www.youtube.com/watch?v=CDqzWpwkSls&t=596s) &middot; *Reframes UX as a data-engineering concern.*

> "So, over time, your model becomes more confident, and the human is not encouraged to think further."
>
> — [10:39](https://www.youtube.com/watch?v=CDqzWpwkSls&t=639s) &middot; *Describes the vicious feedback loop that bad interfaces create.*

> "So, they continue to defer to the AI, and the AI becomes the person in the driving seat."
>
> — [11:24](https://www.youtube.com/watch?v=CDqzWpwkSls&t=684s) &middot; *The end state of unexamined deference, stated bluntly.*

> "That means that you have true positive and negative labels that are honest and get logged to then continue to have model improvements that are targeting exactly where the model goes wrong."
>
> — [11:24](https://www.youtube.com/watch?v=CDqzWpwkSls&t=684s) &middot; *Explains why forced independent judgment pays off in label quality.*

> "For example, if there's somebody who has a hearing aid, that means that the model correctly predicted that there are headphones or earbuds detected."
>
> — [12:44](https://www.youtube.com/watch?v=CDqzWpwkSls&t=764s) &middot; *The concrete case showing how a conflated question destroys a label.*

> "Either way, in both of these cases, you're just becoming a rubber stamp."
>
> — [16:06](https://www.youtube.com/watch?v=CDqzWpwkSls&t=966s) &middot; *Applies the thesis to coding agents, the audience's own tooling.*

> "Instead, you probably want a coding agent that acts like a junior developer."
>
> — [16:45](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1005s) &middot; *The prescriptive model for agent interaction design.*

> "Lastly, for sustained attention, you want to build in friction exactly where the stakes are high."
>
> — [19:02](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1142s) &middot; *States the friction-to-stakes design rule.*

> "reframe your system to think of the human as investigator, not just a validator"
>
> — [19:02](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1142s) &middot; *Compresses the whole talk into a role change.*

> "Next principle is every interaction is already a label."
>
> — [21:10](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1270s) &middot; *The most portable single principle in the talk.*

> "Another principle is to stop asking how to evaluate the model."
>
> — [22:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1361s) &middot; *A deliberately contrarian framing aimed at eval-focused engineers.*

> "Sometimes the fix is not a better model or more oversight, it's just engineering the interaction itself."
>
> — [25:37](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1537s) &middot; *The closing thesis, and the claim most likely to be contested.*

## Positions

- Expert human reviewers with >90% calibration accuracy will uphold roughly half of fabricated AI flags, so reviewer skill does not protect against automation bias. ([6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s), confidence: stated)
- The rubber-stamping failure was caused by the interface, not by the model (1% false positive rate) or by insufficiently skilled proctors. ([7:03](https://www.youtube.com/watch?v=CDqzWpwkSls&t=423s), confidence: stated)
- Changing only the guideline copy — framing the AI signal as preliminary and requiring independent evidence — shifted rejection rates 21% without any model or UI change. ([7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s), confidence: stated)
- The human-in-the-loop process is cyclical, not linear: interaction design determines human behavior, which determines the training and eval data for the next model. ([9:11](https://www.youtube.com/watch?v=CDqzWpwkSls&t=551s), confidence: stated)
- You cannot change human behavior directly, so the only real lever an engineer has is the interaction. ([9:11](https://www.youtube.com/watch?v=CDqzWpwkSls&t=551s), confidence: stated)
- Rubber-stamped approvals get logged as truth and make models spuriously more confident over time. ([10:39](https://www.youtube.com/watch?v=CDqzWpwkSls&t=639s), confidence: stated)
- A single yes/no CTA that conflates 'was the model's perception correct' with 'should we penalize this user' produces false labels and degrades the model. ([12:44](https://www.youtube.com/watch?v=CDqzWpwkSls&t=764s), confidence: stated)
- LLM writing feedback should be inline and anchored to specific spans rather than delivered as a long block that rewrites the user's passage. ([14:37](https://www.youtube.com/watch?v=CDqzWpwkSls&t=877s), confidence: stated)
- Both dominant coding-agent patterns — one giant diff, or per-file approval prompts — reduce the developer to a rubber stamp and produce low-information accept/reject data. ([16:06](https://www.youtube.com/watch?v=CDqzWpwkSls&t=966s), confidence: stated)
- Friction is desirable and should be deliberately added where stakes are high, and removed where oversight is low. ([19:51](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1191s), confidence: stated)
- Systems that record a yes/no decision but not the human's subsequent manual edit capture a false signal that pollutes datasets. ([22:00](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1320s), confidence: stated)
- Success metrics and required data should be defined before the system is built, rather than asking afterward how to evaluate the model. ([22:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1361s), confidence: stated)
- Thumbs up/down feedback is insufficient; explicit feedback must be collected at the right touch points with enough nuance to drive improvements. ([24:38](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1478s), confidence: stated)
- Adding more human oversight is not by itself a fix for AI system quality. ([25:37](https://www.youtube.com/watch?v=CDqzWpwkSls&t=1537s), confidence: stated)

## Concepts

- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [automation bias](../concepts/automation-bias.md)
- [cognitive debt](../concepts/cognitive-debt.md)
- [data flywheels](../concepts/data-flywheels.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [online evaluation](../concepts/online-evaluation.md)

