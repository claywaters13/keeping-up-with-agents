---
title: "From Ambient Documentation to Clinical Intelligence"
type: "talk"
slug: "from-ambient-documentation-to-clinical-intelligence"
track: "AI in Healthcare"
org: "Abridge"
day: "Day 4 — Session Day 3"
room: "Track 7"
video_id: "u6q-byPWUuo"
duration_sec: 1295
word_count: 3980
speakers: ["Chaitanya Asawa"]
---

# From Ambient Documentation to Clinical Intelligence

**Speakers:** [Chaitanya Asawa](../speakers/chaitanya-asawa.md)

**Org:** Abridge

**Track:** AI in Healthcare &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 21m 35s

[Watch on YouTube](https://www.youtube.com/watch?v=u6q-byPWUuo)

## Summary

Chaitanya Asawa, who leads clinical decision support and agentic experiences engineering at Abridge, traces the company's path from ambient clinical documentation — turning the doctor-patient conversation into a SOAP note — to a broader 'clinical intelligence' layer that pends orders, matches clinical trials, and answers contextual clinical questions during the visit. His framing is that healthcare is 'hard mode' on all three agentic-product KPIs at once: quality (being wrong destroys trust), latency (you must act live in the conversation), and cost (at a run rate of 100 million medical conversations a year). Most of the talk is the engineering answer to that: evals as the company's operating system, physician-authored rubrics adjudicated across four clinicians and encoded into LLM judges, staged rollouts with continual monitoring, and decomposition of the note into section-level workflows served by post-trained small models rather than a frontier model. He also argues Abridge has a defensible 'right to win' in training because of a proprietary conversation dataset no one else has. Watch it if you want a concrete, high-stakes case study in judge design when the generator–verifier gap is small, and in cost gating for always-listening agents.

## Key Points

- Abridge started with clinical documentation because it is a long-standing, well-understood pain point — clinicians spend roughly two hours a day writing notes, often as after-hours 'pajama time' — and high-quality automated notes became the wedge into a technology-reticent industry, reaching 300 health systems in two to three years.
- The company's core thesis is that everything in healthcare is downstream of the doctor-patient conversation — billing, clinical trial matching, clinical decision support — so capturing that conversation lets you automate the administrative machinery built around it.
- Healthcare puts an agentic product on hard mode for all three standard KPIs simultaneously: quality (an incorrect answer has clinical consequences and forfeits trust), latency (information must arrive live and at the right moment), and cost (at 100 million conversations per year).
- Abridge treats evals as its operating system: internal pre-deployment benchmarks, staged rollout through trusted alpha clinicians to beta and A/B tests at scale, and continual monitoring even after full rollout.
- Because most of the company are not clinicians, embedded clinicians' judgment is encoded into expert-calibrated LLM judges, which creates a feedback loop any engineer can hill-climb against.
- For contextual clinical decision support the generator–verifier gap is small — a verifier good enough to grade answers would itself be the generator — so Abridge triangulates with multiple judges: clinical quality, boundary/adversarial, clinical safety, and product judges for tone and style.
- Rather than a single golden answer, physicians independently author rubrics of required response elements for real clinical cases; a third physician adjudicates the two rubrics into a final one and a fourth does QA, after which an LLM judge semantically matches agent responses against the rubric elements.
- On cost, Abridge decomposes note generation into per-section workflows served by post-trained smaller models instead of a frontier model, and gates always-on order detection behind cheap fast triggers that hand off to larger models only at the right conversational events.
- Asawa argues the data flywheel of 100 million annual medical conversations gives Abridge a 'right to win' that can outpace the rate of change of frontier models on problems the labs are not focused on.

## Notable Quotes

> "a bridge in the matter of 2 to 3 years got its way into 300 of the largest health systems in the United States, Kaiser, Mayo, Johns Hopkins, Sutter, and so forth."
>
> — [4:49](https://www.youtube.com/watch?v=u6q-byPWUuo&t=289s) &middot; *Concrete scale claim that anchors the credibility of everything after it.*

> "in health care, we actually see administrative costs have only gone up over the past a few decades and productivity hasn't necessarily increased"
>
> — [5:23](https://www.youtube.com/watch?v=u6q-byPWUuo&t=323s) &middot; *States the macro problem the product is aimed at, invoking Baumol's cost disease.*

> "we hear all the time that doctors are burnt out and they actually often don't recommend it as a profession to to their children"
>
> — [6:02](https://www.youtube.com/watch?v=u6q-byPWUuo&t=362s) &middot; *The human motivation behind the documentation product, stated bluntly.*

> "it takes like 2 hours a day to write just write these notes and you often do it with what's known as pajama time after work itself"
>
> — [6:39](https://www.youtube.com/watch?v=u6q-byPWUuo&t=399s) &middot; *Quantifies the burden the product removes and names the industry term for it.*

> "It's all about the conversation, that sacred doctor and patient conversation, and we've just built all this administrative machinery around that."
>
> — [8:34](https://www.youtube.com/watch?v=u6q-byPWUuo&t=514s) &middot; *The company's core strategic thesis in one sentence.*

> "In healthcare, I feel that we're actually playing on hard mode for all of these three KPIs."
>
> — [11:34](https://www.youtube.com/watch?v=u6q-byPWUuo&t=694s) &middot; *The organizing claim of the technical half of the talk.*

> "When I used to work at Glynn, you know, while I loved that product, I could be wrong and it would have been fine. Maybe we answered a question incorrectly. But in healthcare, if we answer something incorrectly, there's actually consequences and we entirely lose our trust."
>
> — [11:34](https://www.youtube.com/watch?v=u6q-byPWUuo&t=694s) &middot; *Sharp contrast between enterprise search and clinical stakes, drawn from his own career.*

> "we have a motto inside the company that our goal is to save lives, save time, save money for uh, for the hospital system and for the healthcare industry as a whole"
>
> — [12:05](https://www.youtube.com/watch?v=u6q-byPWUuo&t=725s) &middot; *Maps the company mission onto quality, latency, and cost.*

> "For us, we really treat evals as the operating system, the life's blood of the of the company."
>
> — [12:40](https://www.youtube.com/watch?v=u6q-byPWUuo&t=760s) &middot; *The strongest statement of eval-centric development in the talk.*

> "you cannot get away with just being like a prototype that you ship out there and be like, "Yeah, I mean I tested on a few cases and it works.""
>
> — [13:22](https://www.youtube.com/watch?v=u6q-byPWUuo&t=802s) &middot; *Positions against demo-driven shipping in a high-stakes domain.*

> "How we do this is we always have expert calibrated LM judges. So, we have clinicians embedded throughout the entire company."
>
> — [13:22](https://www.youtube.com/watch?v=u6q-byPWUuo&t=802s) &middot; *Names the mechanism that lets non-clinicians ship clinical products.*

> "I think a really great evaluation system has a property that it reflects the behaviors that you want in your product."
>
> — [13:58](https://www.youtube.com/watch?v=u6q-byPWUuo&t=838s) &middot; *A transferable definition of eval quality, not specific to healthcare.*

> "If I had a really really good generator verifier, then that would just be my generator itself."
>
> — [15:58](https://www.youtube.com/watch?v=u6q-byPWUuo&t=958s) &middot; *Crisp statement of why LLM-as-judge fails when the generator-verifier gap collapses.*

> "And then we had a separate physician that actually adjudicated it, brought these two independent rubrics together, created a final rubric, and we actually had a fourth clinician do QA on these rubrics."
>
> — [17:05](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1025s) &middot; *Details the four-clinician rubric pipeline that grounds the eval in human reference.*

> "we do this on the live in the conversation, and we do on the run rate of 100 million medical conversations a year"
>
> — [17:38](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1058s) &middot; *The scale number that makes the cost and latency constraints real.*

> "Health care is actually many specific workflows. You don't need, you know, Fable 5 to actually solve all of your clinical notes. We we don't need frontier level intelligence for every problem."
>
> — [18:11](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1091s) &middot; *Direct argument for workflow decomposition over frontier-model-for-everything.*

> "we actually post train a lot of smaller models for different problems, such as different actually even to the granularity of different sections in the clinical note"
>
> — [18:48](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1128s) &middot; *Shows how far down the decomposition goes in practice.*

> "we have this unique data set of a hundred million medical conversations a year. And as far as we know, no one else has such a large data set."
>
> — [18:48](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1128s) &middot; *The data-moat claim underpinning the post-training strategy.*

> "Our key insight is we can actually potentially beat the rate of change on the frontier model if we have the right to win by having the right data that they may not have and the focus on a problem that they may not be focusing on."
>
> — [19:23](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1163s) &middot; *Explicit rebuttal to the 'frontier models will steamroll you' objection.*

> "how do we find the right events in the conversation to actually trigger heavier models that will actually do the order matching"
>
> — [19:59](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1199s) &middot; *Describes the cheap-gate-then-escalate pattern for always-listening agents.*

> "healthcare is a domain that needs frontier AI and actually puts it to the test at high stakes"
>
> — [20:33](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1233s) &middot; *The closing recruiting argument and thesis of the whole talk.*

## Positions

- Administrative costs in healthcare have risen over recent decades without corresponding productivity gains, unlike other industries where good prices fall. ([5:23](https://www.youtube.com/watch?v=u6q-byPWUuo&t=323s), confidence: stated)
- Clinical notes are high stakes not only because they underpin billing but because they carry the patient's longitudinal record forward to the next clinician. ([7:14](https://www.youtube.com/watch?v=u6q-byPWUuo&t=434s), confidence: stated)
- Everything downstream in healthcare — billing, trial matching, decision support — derives from the doctor-patient conversation, so capturing that conversation is the right foundation to build on. ([8:34](https://www.youtube.com/watch?v=u6q-byPWUuo&t=514s), confidence: stated)
- Healthcare agentic products face harder constraints than other verticals on all three of quality, latency, and cost simultaneously. ([11:34](https://www.youtube.com/watch?v=u6q-byPWUuo&t=694s), confidence: stated)
- Evals should be treated as the operating system of the company rather than a testing afterthought. ([12:40](https://www.youtube.com/watch?v=u6q-byPWUuo&t=760s), confidence: stated)
- Encoding embedded clinicians' judgment into LLM judges is what lets non-clinician engineers move fast on clinical products. ([13:58](https://www.youtube.com/watch?v=u6q-byPWUuo&t=838s), confidence: stated)
- For contextual clinical decision support, no single LLM verifier can be trusted as ground truth, because a verifier good enough to grade would already be the best generator. ([15:58](https://www.youtube.com/watch?v=u6q-byPWUuo&t=958s), confidence: stated)
- A single human golden response is the wrong reference format for open-ended clinical answers; physician-authored rubrics of required elements are needed instead because the space of acceptable responses is effectively infinite. ([17:05](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1025s), confidence: stated)
- Frontier-level intelligence is unnecessary for most clinical documentation work; decomposing into per-section workflows served by post-trained smaller models achieves the quality bar at much lower cost and latency. ([18:11](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1091s), confidence: stated)
- Abridge's proprietary dataset of roughly 100 million medical conversations per year is larger than anyone else's and constitutes a right to win in model training. ([18:48](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1128s), confidence: stated)
- On problems where quality is already maxed out, the reason to train your own model is to reduce cost and latency rather than to improve quality. ([19:23](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1163s), confidence: stated)
- A specialized team with unique data can outpace the rate of improvement of frontier models on a narrow problem the labs are not focused on. ([19:23](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1163s), confidence: stated)
- Continuously running heavy models to detect in-visit orders would be prohibitively expensive, so cheap event gates must decide when to escalate to larger models. ([19:59](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1199s), confidence: stated)
- Healthcare is an attractive rather than a technically unambitious domain for AI engineers, contrary to the stigma the speaker himself once held. ([20:33](https://www.youtube.com/watch?v=u6q-byPWUuo&t=1233s), confidence: stated)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [data flywheels](../concepts/data-flywheels.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [rubric design](../concepts/rubric-design.md)
- [small language models](../concepts/small-language-models.md)
- [task decomposition](../concepts/task-decomposition.md)
- [verifier design](../concepts/verifier-design.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

