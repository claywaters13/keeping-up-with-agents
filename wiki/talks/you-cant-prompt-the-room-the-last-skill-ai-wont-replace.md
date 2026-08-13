---
title: "You Can't Prompt the Room: The Last Skill AI Won't Replace"
type: "talk"
slug: "you-cant-prompt-the-room-the-last-skill-ai-wont-replace"
org: "VisualLabs"
video_id: "6bmM45jkMDY"
duration_sec: 945
word_count: 2339
speakers: ["Balázs Horváth"]
---

# You Can't Prompt the Room: The Last Skill AI Won't Replace

**Speakers:** [Balázs Horváth](../speakers/balazs-horvath.md)

**Org:** VisualLabs

**Duration:** 15m 45s

[Watch on YouTube](https://www.youtube.com/watch?v=6bmM45jkMDY)

## Summary

Balázs Horváth of VisualLabs argues that now that AI has removed coding as the bottleneck in software development, the scarce skill is figuring out what is worth building — which requires human requirements elicitation, not prompting. He grounds this in an internal hackathon where 17 of 21 agent ideas were abandoned for lacking business value or data access, with the surviving four materially changing how the company works. The practical core of the talk is a revival of the classic business-analyst toolkit — user story mapping, business model canvas, four framing questions (whose problem, what winning looks like, what would make them refuse, does it change a decision) — plus his VAD sequence: value, architecture, then design. He argues user stories are a particularly good AI interface because models were trained on that well-known structure, and that these artifacts should live in markdown in the repo as context. Worth watching if you want a concrete, low-tech process for aiming AI-assisted development; it is a product-management talk, not a technical one, and covers little about models or tooling.

## Key Points

- At an internal VisualLabs hackathon, 17 of 21 agent ideas were abandoned because they created no business value or lacked data access, while the remaining four significantly changed how the team works.
- The bottleneck in the software development lifecycle has moved from writing code to getting stakeholders and decision-makers into the room to elicit requirements.
- Because AI is trained to produce the most common answer, using it naively tends to replicate what already exists — the 'faster horse' rather than the car.
- Story mapping is the single most valuable technique the speaker names: lay out process backbones (contact, triage, resolve, close), hang user stories beneath them, and treat the top row as the MVP and lower rows as backlog.
- User stories work well as AI input specifically because the persona/what/why structure plus acceptance criteria is a well-known pattern the models were trained on, and acceptance criteria can be derived into test cases.
- Four framing questions should precede any build: whose problem is this, what does winning look like for them, what would make them refuse to use it, and would it change a decision.
- The VAD sequence — value, architecture, design — insists you understand how value is created and what process supports it before designing the system.
- Anti-patterns of building the wrong thing: high shipping velocity with low adoption, one-time trial without repeat use, the demo becoming the deliverable, and PRDs with no real user testers.
- Concrete Monday actions: replace 'features shipped last quarter' with 'features shipped that are used more than twice', measure activity frequency rather than time on site, and move subject-matter experts into customer-facing decision-making roles.
- Requirements artifacts should be tracked in a markdown file in the repository so AI can read them as context.

## Notable Quotes

> "at a point where writing code is no longer the bottleneck, the real thing is to figure is figuring out what it is that you should be building."
>
> — [0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s) &middot; *The thesis of the talk in one line.*

> "we held an internal hackathon uh where we had about 21 agents uh agent ideas and 17 of those were abandoned because they actually created no um business value."
>
> — [0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s) &middot; *The talk's only hard number, and the empirical basis for its argument.*

> "Now the real bottleneck is getting your people, your stakeholders, your decision-makers into the room and being able to access them and elicit the requirement and being able to spend the time with them."
>
> — [2:25](https://www.youtube.com/watch?v=6bmM45jkMDY&t=145s) &middot; *States precisely where the speaker thinks the constraint moved to.*

> "you can prompt your code, you can prompt your AI, you can prompt your whole specification, but you can't prompt your room."
>
> — [2:25](https://www.youtube.com/watch?v=6bmM45jkMDY&t=145s) &middot; *The title claim, stated in full.*

> "if you're just using AI um to to make things, you know, build things better, um the chances are that you are replicating what already exists because AI by definition is coded to give you the most common answers."
>
> — [3:21](https://www.youtube.com/watch?v=6bmM45jkMDY&t=201s) &middot; *A checkable position about why AI-led ideation regresses to the mean.*

> "the real job is to make sure that AI moves away from that average into what is better for us."
>
> — [3:21](https://www.youtube.com/watch?v=6bmM45jkMDY&t=201s) &middot; *Frames the human role as pulling models off their default distribution.*

> "it's really an interesting word world where being able to write good code is no longer the most important skill to have."
>
> — [3:21](https://www.youtube.com/watch?v=6bmM45jkMDY&t=201s) &middot; *The most contestable claim in the talk, stated plainly.*

> "the real skill now is becoming the analysis analysis toolkit, which is things like story mapping, business model canvas, value canvas"
>
> — [4:13](https://www.youtube.com/watch?v=6bmM45jkMDY&t=253s) &middot; *Names the specific replacement skillset rather than gesturing at 'soft skills'.*

> "It is intended to stay at a fairly high level so you can get a a big picture, and then in you can decide what it is that you want to build and release one"
>
> — [5:12](https://www.youtube.com/watch?v=6bmM45jkMDY&t=312s) &middot; *Specifies the altitude at which story maps are useful.*

> "make sure that every user story covers these is ideally written in this setup because AI is really good at pattern recognition and it was actually trained on the user story structure because it's a very well-known and well-used setup."
>
> — [6:00](https://www.youtube.com/watch?v=6bmM45jkMDY&t=360s) &middot; *The talk's main mechanistic claim about why this format helps models.*

> "if you go back to something that's familiar to AI, it will get get you better better results."
>
> — [6:57](https://www.youtube.com/watch?v=6bmM45jkMDY&t=417s) &middot; *Generalizes the user-story point into a prompting heuristic.*

> "the software development life cycle doesn't change as much as a result of AI. It's actually the toolkit that we are we are using is changing."
>
> — [7:43](https://www.youtube.com/watch?v=6bmM45jkMDY&t=463s) &middot; *A deliberately deflationary take on AI's impact on process.*

> "just make sure that you track all of these in a good old markdown file in your repository so that AI can access it."
>
> — [8:35](https://www.youtube.com/watch?v=6bmM45jkMDY&t=515s) &middot; *The one concrete engineering practice recommended.*

> "if you just did something as generic as build us an agent that handles support, uh you will not get the answer you want."
>
> — [9:17](https://www.youtube.com/watch?v=6bmM45jkMDY&t=557s) &middot; *Names the failure mode the whole method is designed to prevent.*

> "we all have access to the same tools, so the difference will be who can understand the business need better"
>
> — [10:07](https://www.youtube.com/watch?v=6bmM45jkMDY&t=607s) &middot; *The competitive-advantage argument underlying the talk.*

> "it's old skill, but new economics, and it's a real shift towards analyst toolkit."
>
> — [11:03](https://www.youtube.com/watch?v=6bmM45jkMDY&t=663s) &middot; *Preempts the obvious 'this is just product management' objection.*

> "don't look at time of usage and time spent on site. Much rather you got look at the frequency of a certain activity."
>
> — [11:03](https://www.youtube.com/watch?v=6bmM45jkMDY&t=663s) &middot; *A specific, actionable metrics tradeoff.*

> "earlier on before the AI boom, uh we had our smartest people writing our code, but what now we need to be shifting our smartest people towards our customers, towards the business problems"
>
> — [12:38](https://www.youtube.com/watch?v=6bmM45jkMDY&t=758s) &middot; *The organizational recommendation, and the most consequential one.*

> "we need to be spending more time on deciding what to build because that's the expensive part. Building it has actually become very cheap."
>
> — [12:38](https://www.youtube.com/watch?v=6bmM45jkMDY&t=758s) &middot; *States the cost inversion that drives every other recommendation.*

> "the number of features shipped last quarter, that should be should be eliminated and you should just start looking at the number of features that we shipped that is actually used more than twice."
>
> — [13:26](https://www.youtube.com/watch?v=6bmM45jkMDY&t=806s) &middot; *A named KPI replacement anyone can adopt immediately.*

> "So this way we can build the right thing and not just the next thing."
>
> — [15:07](https://www.youtube.com/watch?v=6bmM45jkMDY&t=907s) &middot; *The closing formulation of the thesis.*

## Positions

- Writing code is no longer the bottleneck in software development; deciding what to build is. ([0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s), confidence: stated)
- At VisualLabs' internal hackathon, 17 of 21 agent ideas were abandoned for lack of business value or data access; the remaining 4 had large impact. ([0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s), confidence: stated)
- AI is optimized to return the most common answer, so AI-led ideation replicates what already exists rather than producing step-change improvements. ([3:21](https://www.youtube.com/watch?v=6bmM45jkMDY&t=201s), confidence: stated)
- Writing good code is no longer the most important skill to have. ([3:21](https://www.youtube.com/watch?v=6bmM45jkMDY&t=201s), confidence: stated)
- Because models were trained on the standard persona/need/why user story structure, formatting requirements as user stories yields better AI output than generic prose prompts. ([6:00](https://www.youtube.com/watch?v=6bmM45jkMDY&t=360s), confidence: stated)
- The software development lifecycle itself is largely unchanged by AI; only the toolkit changes. ([7:43](https://www.youtube.com/watch?v=6bmM45jkMDY&t=463s), confidence: stated)
- Requirements artifacts should be committed as markdown in the repository so AI tools can use them as context. ([8:35](https://www.youtube.com/watch?v=6bmM45jkMDY&t=515s), confidence: stated)
- Value must be understood before architecture, and architecture before design (the VAD sequence). ([9:17](https://www.youtube.com/watch?v=6bmM45jkMDY&t=557s), confidence: stated)
- Since everyone has access to the same models and tools, competitive differentiation comes from understanding the business need better. ([10:07](https://www.youtube.com/watch?v=6bmM45jkMDY&t=607s), confidence: stated)
- Repeat-usage frequency is a better product metric than session duration or time on site. ([11:03](https://www.youtube.com/watch?v=6bmM45jkMDY&t=663s), confidence: stated)
- A demo treated as the deliverable, and a PRD with no real user testers, both predict that the software will not be used in production. ([11:48](https://www.youtube.com/watch?v=6bmM45jkMDY&t=708s), confidence: stated)
- Organizations should move their most experienced subject-matter experts out of code and into customer-facing decision-making about what gets built. ([12:38](https://www.youtube.com/watch?v=6bmM45jkMDY&t=758s), confidence: stated)
- 'Features shipped last quarter' should be replaced as a KPI by 'features shipped that are used more than twice'. ([13:26](https://www.youtube.com/watch?v=6bmM45jkMDY&t=806s), confidence: stated)
- Building software with user stories first produces measurably better results than building without them. ([15:07](https://www.youtube.com/watch?v=6bmM45jkMDY&t=907s), confidence: implied)

## Concepts

- [agent configuration files](../concepts/agent-configuration-files.md)
- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [developer productivity metrics](../concepts/developer-productivity-metrics.md)
- [requirements elicitation](../concepts/requirements-elicitation.md)
- [spec-driven development](../concepts/spec-driven-development.md)

