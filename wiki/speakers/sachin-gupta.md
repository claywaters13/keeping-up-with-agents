---
title: "Sachin Gupta"
type: "speaker"
slug: "sachin-gupta"
talk_count: 2
---

# Sachin Gupta

## Talks

- [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [agent memory](../concepts/agent-memory.md)
- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [ai-generated code quality](../concepts/ai-generated-code-quality.md)
- [audit trails](../concepts/audit-trails.md)
- [code review bottlenecks](../concepts/code-review-bottlenecks.md)
- [cognitive debt](../concepts/cognitive-debt.md)
- [developer productivity metrics](../concepts/developer-productivity-metrics.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [model routing](../concepts/model-routing.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)
- [verifier design](../concepts/verifier-design.md)

## Quotes

> "What is new is that we are shipping the most behavior changing systems we have ever built agents that send money, agent that send mail, agent that modify databases, agent that spawn child processes and we are shipping them with none of that infrastructure."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [0:00](https://www.youtube.com/watch?v=zU4EagB311U&t=0s)

> "We are shipping them the way web team used to ship in 2008."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [0:45](https://www.youtube.com/watch?v=zU4EagB311U&t=45s)

> "The moment your prompt change merges, 100% of your users see the new behavior. There is no canary, no segment, and no roll back button."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [0:45](https://www.youtube.com/watch?v=zU4EagB311U&t=45s)

> "Web teams stopped doing this back in 2012 and they stopped doing it for changes that were less risky than this."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [1:30](https://www.youtube.com/watch?v=zU4EagB311U&t=90s)

> "The agent did not follow the instructions and ended up deleting the production database and then fabricated over 4,000 fake users to conceal what it had done."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [2:25](https://www.youtube.com/watch?v=zU4EagB311U&t=145s)

> "It had a four agent pipeline researcher, analyzer, verifier, and synthesizer where two of them ran in continuous loop and costed $47,000."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [2:25](https://www.youtube.com/watch?v=zU4EagB311U&t=145s)

> "But agent has six behavior surfaces that a cred app does not have and each one needs its own kind of flag."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [4:00](https://www.youtube.com/watch?v=zU4EagB311U&t=240s)

> "The system prompt is your most behavioral altering code. It changes weekly sometimes daily often outside your normal deploy processes."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [4:40](https://www.youtube.com/watch?v=zU4EagB311U&t=280s)

> "Autonomy, suggest versus auto approve versus autoexecute. The single largest blast radius tile you own."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [4:40](https://www.youtube.com/watch?v=zU4EagB311U&t=280s)

> "If your production system has a hard dependency on one model from one provider and it does not have any routing flag, no fallback, you are one provider outage away from a complete agent outage"
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [7:46](https://www.youtube.com/watch?v=zU4EagB311U&t=466s)

> "The privacy posture of your product lives here. The consistency of your agent behavior lives here. Your compliance story with GDPR and EU AI act lives here."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [8:31](https://www.youtube.com/watch?v=zU4EagB311U&t=511s)

> "First, you flip it and the change takes effect in seconds, not in a deployment pipeline. Second, inflight request respect the flag at the next decision point."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [9:12](https://www.youtube.com/watch?v=zU4EagB311U&t=552s)

> "30 seconds from problem to mitigation without any deployment, without any restart, without any code changes, no incident channel paging."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [11:27](https://www.youtube.com/watch?v=zU4EagB311U&t=687s)

> "Sub agents must go through the same middleware. The biggest failure mode I see is a parent agent with flags properly applied that spawns a child agent."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [13:07](https://www.youtube.com/watch?v=zU4EagB311U&t=787s)

> "Target is under 5 minutes for a kill switch and under 30 minutes for a prompt roll back."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [14:41](https://www.youtube.com/watch?v=zU4EagB311U&t=881s)

> "If you cannot demo all five, you are going to lose the deal. Flags are the demo."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [16:16](https://www.youtube.com/watch?v=zU4EagB311U&t=976s)

> "Every flag needs an owner and a removal date."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [16:59](https://www.youtube.com/watch?v=zU4EagB311U&t=1019s)

> "Remember, 2026 was all about adoption. 2027 is all about control."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [18:31](https://www.youtube.com/watch?v=zU4EagB311U&t=1111s)

> "I'm not saying that coding agents are bad. I'm not saying they don't make us faster. I'm saying they they're creating a kind of debt that nobody is measuring."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [0:00](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=0s)

> "the commits climbed 25% year over year. And now over the same year, comments on the comments dropped 27%"
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [0:43](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=43s)

> "Median PR review time is up by 441.5% and if you see like if you calculate, you'll figure out that the reviewed PRs take 5.4 times longer than what they used to."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [0:43](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=43s)

> "AI is producing the pull request very fast, but humans cannot responsibly review them at that pace."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [1:40](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=100s)

> "Every one of these numbers are real. None of them is a lie, but everyone is a vanity metric."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [2:25](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=145s)

> "PR count goes up when one PR splits into seven PRs. Median PR size going up is not a benefit, it's actually a bloating. Cycle time going down when reviewers stop pushing back."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [3:11](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=191s)

> "These things tell you the speed of production. They do not tell you the speed of trust."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [3:11](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=191s)

> "Tests are getting added, but they're actually asserting what the code did, not what the code should do. They lack in behavior, including bugs."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [4:01](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=241s)

> "It rhymes with technical debt, but it is more like a financial debt because it compounds. It actually accrues interest, but this interest is not money. This interest is paid in human attention."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [4:46](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=286s)

> "Code that was not deeply reviewed yesterday grounds tomorrow's PR. This debt becomes generative in nature."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [4:46](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=286s)

> "Once leadership sees the new throughput, you don't get to hire reviewers in proportion. There is no slack left to pay the debt back."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [5:35](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=335s)

> "The same PR, basically the score that you got for the same PR, will score differently when your model will change."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [6:20](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=380s)

> "You want a number that is traceable to a deterministic computation"
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [6:20](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=380s)

> "Agents are biased toward fix at the call site. A human engineer routes a fix to the root cause."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [7:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=429s)

> "The review cost of a sprawling difference is not proportional to the size. It is actually much steeper."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [7:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=429s)

> "The agent gave you three hours of typing. You spend those three hours by multi-party reviewer attention."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [9:17](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=557s)

> "A healthy PR produces a tiny, almost ceremonial report. That's exactly what you want."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [14:02](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=842s)

> "The score alone is useful. The structured advice is what actually moves the team behavior."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [14:51](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=891s)

> "The agent did not cause the score, but the shape of the PR that is created by the agent did this."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [15:33](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=933s)

> "complexity drives burden, not authorship"
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [17:56](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1076s)

> "Even if the agent wrote the code, even if the agent wrote the test, the human author confirms the test assert what the code should do"
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [19:34](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1174s)

> "The agent should not write the PR body. That's the moment the human author commits to understanding what they are actually shipping."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [20:24](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1224s)

> "Post the score as a PR comment on every PR. Don't block it."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [21:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1269s)

> "That moves the discussion from feeling to measurement."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [22:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1368s)

> "who is accountable when an AI authored change causes an incident? Where is the audit trail?"
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [22:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1368s)

> "The slope of a reviewed it over time matters most than the level."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [23:36](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1416s)

