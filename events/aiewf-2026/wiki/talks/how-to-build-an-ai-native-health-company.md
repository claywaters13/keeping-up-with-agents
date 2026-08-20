---
title: "How to build an AI-Native Health Company"
type: "talk"
slug: "how-to-build-an-ai-native-health-company"
track: "AI in Healthcare"
org: "Maven Clinic"
day: "Day 4 — Session Day 3"
room: "Track 7"
video_id: "WJRdLNhrsLQ"
duration_sec: 1038
word_count: 2725
speakers: ["Dan Feng"]
---

# How to build an AI-Native Health Company

**Speakers:** [Dan Feng](../speakers/dan-feng.md)

**Org:** Maven Clinic

**Track:** AI in Healthcare &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 17m 18s

[Watch on YouTube](https://www.youtube.com/watch?v=WJRdLNhrsLQ)

## Summary

Dan Feng of Maven Clinic walks through how a traditional digital health company retrofitted itself into an "AI-native" one over roughly two years, arguing there is no single definition or playbook for the transition. His framework has three legs: use AI internally wherever possible, build AI into the product to improve user experience and cut operational cost, and — hardest of all — change hiring, rewards, and planning process to match. The most concrete material covers software process: sprint-length planning instead of quarterly roadmaps because model capability three months out is unknowable, PRDs shrunk to one or two pages, engineers self-certifying whether a PR needs review, a 500-line PR cap, and stacked PRs to keep review meaningful. The reliability section is the other payoff: rather than chasing zero hallucination, Maven classifies failures by tolerability, runs multi-model agreement checks on high-stakes flows like reimbursement claims, requires a 90% pass rate across repeated runs of hundreds of integration tests, and grades live conversations against predefined rubrics. Worth watching if you're a healthcare or regulated-domain engineering leader trying to translate "adopt AI" into specific changes to planning, code review, and release gates.

## Key Points

- Being AI-native, in Maven's framing, is three things at once: internal tool adoption, AI built into the product for both UX and cost reasons, and deliberate changes to culture and process — the third being the hardest and most neglected.
- Adoption strategy should be segmented by user type: early adopters just need tools enabled, the majority needs shared infrastructure and low-friction tooling, and slow adopters need their concerns heard plus clarity about where the company is going.
- Tooling support must follow engineers rather than dictate to them — Maven's team moved largely from Cursor last year to Claude Code this year, and the company supports both.
- The senior-engineer-delegates-implementation model is breaking down: senior engineers now solve problems with AI directly because delegation adds overhead, so new hires must be able to work independently from a technical lead memo.
- Hiring criteria have shifted toward genuine interest in AI, product understanding (the PM/engineer boundary is blurring), deep system knowledge, and comfort with ambiguous problems — and performance reviews now explicitly ask what someone did on the AI side.
- Because building is now cheap and requirements-gathering is the expensive part, planning should be one-year directional dreams plus concrete two-to-four-week deliverables, skipping the three-to-six-month horizon that model releases make unplannable.
- AI coding adoption should start with low-risk, easy-to-verify work (unit tests, documentation) to build confidence and accumulate rules and skills before mandating it across all tasks.
- Code review had to be redesigned for AI-scale output: engineers self-identify when a PR needs review (while remaining accountable), PRs are capped at 500 lines, big features are split into stacked PRs, and rubber-stamp approvals are treated as the worst outcome because they manufacture false confidence.
- Reliability engineering starts by classifying which failures are acceptable — a failed appointment booking one time in a thousand is survivable, a wrong reimbursement amount is not — and spending extra safeguards only where the cost of error is high.
- Release gates for LLM systems are statistical, not binary: hundreds of integration tests run many times each with a sustained ~90% pass rate requirement, followed by post-launch rubric-based auto-evaluation of conversations plus a dedicated human team spot-checking, escalating to ~20% review for new features.

## Notable Quotes

> "AI is here and improving every day. I think adopting it is not an optional. Even you choose not to, your competitors will do."
>
> — [0:54](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=54s) &middot; *States the talk's premise as a competitive inevitability rather than a technology preference.*

> "Like a tractors aren't to replace farmers, but the farmers who can operate the tractor will replace the ones who cannot."
>
> — [0:54](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=54s) &middot; *The framing metaphor the rest of the talk's hiring and rewards advice rests on.*

> "I don't think there's a one single definition what it means by AI native. And more importantly, there's no predefined playbook you can just follow and bingo, you become AI native."
>
> — [1:37](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=97s) &middot; *Explicitly refuses the tidy answer the talk title invites.*

> "Whenever you want to ask other people to do something for you, you should be saying with yourself I can use AI to do it."
>
> — [1:37](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=97s) &middot; *The concrete behavioral rule Maven pushed internally, including to sales leadership.*

> "Last year, most of folks and Maven they are using cursor. This year, a lot of them switch to cloud codes. For us, we need to support the both. We need to meet where they are."
>
> — [4:01](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=241s) &middot; *A dated, checkable data point on internal tool churn and a stance against standardizing on one vendor.*

> "They just use AI to solve it instantly. Delegating to other people means more overheads and less efficient."
>
> — [4:42](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=282s) &middot; *Names the specific mechanism by which AI erodes the traditional senior-engineer delegation model.*

> "With AI, building is super fast. It's probably couple minutes you can get it done."
>
> — [6:56](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=416s) &middot; *The cost inversion that justifies the entire planning-process argument that follows.*

> "It's still okay, you can think about what you want to deliver in one year. You can assume AI models can do anything you want in one year."
>
> — [7:41](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=461s) &middot; *An unusually strong assumption about model capability, offered as a planning heuristic.*

> "The really awkward part is mid-term goals. Those like a three months, six months. It's very hard to plan these days. The reason is I don't know what AI models will be capable in three months."
>
> — [8:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=507s) &middot; *Direct attack on quarterly planning, the norm most of the audience still operates under.*

> "we prefer people not write pages or pages of PRD or TDD anymore. We prefer them to write just a short one or two pages."
>
> — [8:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=507s) &middot; *Specific, adoptable process change with a stated page limit.*

> "We started with the lowest risk task, like starting with writing unit tests, documentation. Those things are very easy to verify and the risk is super low."
>
> — [9:58](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=598s) &middot; *Describes the verification-cost logic behind sequencing AI coding adoption.*

> "at this moment, we pretty much use the AI coding tools to do all our implementation."
>
> — [9:58](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=598s) &middot; *The end state of that adoption arc, stated without hedging.*

> "for good engineer, used to they probably write hundreds of lines code every day. These days, they can easily write like thousands. If we keep do the code review as we used to do, we won't be able to keep up."
>
> — [10:50](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=650s) &middot; *Quantifies the throughput change that broke their review process.*

> "We also tried the multiple like AI coding review review tools. It helps a little bit, but we don't feel comfortable 100% rely on them yet."
>
> — [10:50](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=650s) &middot; *A negative result on AI code review from a team otherwise all-in on AI coding.*

> "each PR shouldn't have more than 500 lines of code because nobody can do a meaningful code review with the ones has like thousands of lines code."
>
> — [11:35](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=695s) &middot; *A hard, checkable threshold with the reasoning attached.*

> "One thing we really want to avoid is a rubber stamp, we call it. Means like people submit code review, you cannot really do anything to it. You just say blindly approve it. This is the worst case, we should really avoid because that's just give us false confidence."
>
> — [12:14](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=734s) &middot; *Argues that no review beats fake review — the justification for letting engineers skip review entirely.*

> "But for the Genex solutions, hallucination is there. We cannot ignore it. And there completely eliminating them is can be very costly. Sometimes is not necessary, either."
>
> — [13:41](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=821s) &middot; *Takes the contrarian position that eliminating hallucination is not always worth paying for.*

> "if we help user to like submit their reimbursement claim, we cannot tolerate a failure because if people ask of $200, we issue them 50 or they ask 50, we give them 200. Each case will cause a escalation right away."
>
> — [14:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=867s) &middot; *Grounds failure-tolerance tiering in a concrete healthcare workflow with real dollar consequences.*

> "when we receive their receipt, we will use different models to review the same receipt. We only move forward if the results from different models agree with each other."
>
> — [14:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=867s) &middot; *Describes their specific cross-model agreement safeguard for high-stakes tasks.*

> "for each test case, we run it to many times. We consistently requires the high pass rate, like for example, 90% for all the time."
>
> — [15:09](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=909s) &middot; *Concrete release gate showing how nondeterminism changes what 'tests pass' means.*

> "after we launch the software, we have our auto evolve system evaluate carefully evaluate each conversation. We have predefined a lot of rubrics, what we think is good, what is bad."
>
> — [15:49](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=949s) &middot; *The production-side half of their eval strategy, paired with human spot-checking.*

## Positions

- There is no single definition of "AI-native" and no playbook a company can simply follow to become one. ([1:37](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=97s), confidence: stated)
- AI adoption is not optional, because competitors will adopt it whether or not you do. ([0:54](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=54s), confidence: stated)
- AI chatbots handle customer issues better and more cheaply than human agents, with 24/7 availability. ([2:25](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=145s), confidence: stated)
- Companies should support multiple competing AI coding tools rather than standardizing, because engineer preference shifts year to year. ([4:01](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=241s), confidence: stated)
- Senior engineers should no longer delegate implementation to other engineers, because delegation now costs more in overhead than solving it directly with AI. ([4:42](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=282s), confidence: stated)
- New engineering hires must be able to work independently from a technical lead memo, since there is no implementation work to hand them. ([5:29](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=329s), confidence: stated)
- Engineers who understand the product contribute far more than engineers focused only on the software side, as the PM/engineer boundary blurs. ([6:16](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=376s), confidence: stated)
- Performance reviews should explicitly evaluate and reward employees for leveraging AI to multiply their impact. ([6:16](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=376s), confidence: stated)
- Requirements-gathering, not implementation, is now the expensive part of software development. ([6:56](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=416s), confidence: stated)
- Three-to-six-month planning horizons should be abandoned because model capability at that horizon is unknowable; plan one year directionally and two to four weeks concretely. ([8:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=507s), confidence: stated)
- PRDs and TDDs should be one or two pages, serving as communication artifacts to iterate on rather than finalized specs. ([8:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=507s), confidence: stated)
- Discovering two weeks in that a decision was wrong is acceptable and cheap to correct under AI-accelerated development. ([8:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=507s), confidence: stated)
- AI coding tools are the most successful AI application to date. ([9:11](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=551s), confidence: stated)
- Teams should begin AI coding adoption with low-risk, easily verified tasks like unit tests and documentation before mandating broader use. ([9:58](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=598s), confidence: stated)
- Engineers' role has shifted to reviewing, architecting, and evaluation, with AI tools doing essentially all implementation at Maven. ([10:50](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=650s), confidence: stated)
- Current AI code review tools help somewhat but are not yet trustworthy enough to rely on 100%; human engineer feedback remains very valuable. ([10:50](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=650s), confidence: stated)
- Engineers should be allowed to self-identify whether a PR needs review and merge without one, while remaining accountable for the outcome. ([11:35](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=695s), confidence: stated)
- PRs should be capped at 500 lines, because meaningful review of thousand-line PRs is impossible. ([11:35](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=695s), confidence: stated)
- AI code review is the future even though it isn't reliable enough today, so teams should keep investing in it. ([12:56](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=776s), confidence: stated)
- Completely eliminating hallucination is very costly and sometimes unnecessary; classify which failures are acceptable instead. ([13:41](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=821s), confidence: stated)
- A one-in-a-thousand failure rate is acceptable for appointment scheduling because the user can simply retry, but zero failures are tolerable for reimbursement claims. ([13:41](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=821s), confidence: stated)
- High-stakes AI decisions should be gated on agreement between different models, with handoff to a human agent when they disagree. ([14:27](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=867s), confidence: stated)
- Passing an integration test once is no longer sufficient for LLM systems; each test must be run many times against a sustained pass-rate bar such as 90%. ([15:09](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=909s), confidence: stated)
- Automated rubric scoring of production conversations must be paired with a dedicated human review group, partly to check whether the rubrics themselves are too strict or too loose. ([15:49](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=949s), confidence: stated)
- Fully automating the software lifecycle end to end — including monitoring live traffic and auto-fixing issues — is the goal, but Maven has not achieved it. ([12:56](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=776s), confidence: stated)

## Concepts

- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [code review bottlenecks](../concepts/code-review-bottlenecks.md)
- [cross-model verification](../concepts/cross-model-verification.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [rubric design](../concepts/rubric-design.md)
- [spec-driven development](../concepts/spec-driven-development.md)
- [task decomposition](../concepts/task-decomposition.md)

