---
title: "ReviewDebt: a practical framework for scoring every pull request"
type: "talk"
slug: "reviewdebt-a-practical-framework-for-scoring-every-pull-request"
org: "Ebay"
video_id: "TJPInBjhE4Q"
duration_sec: 1500
word_count: 3885
speakers: ["Sachin Gupta"]
---

# ReviewDebt: a practical framework for scoring every pull request

**Speakers:** [Sachin Gupta](../speakers/sachin-gupta.md)

**Org:** Ebay

**Duration:** 25m 00s

[Watch on YouTube](https://www.youtube.com/watch?v=TJPInBjhE4Q)

## Summary

Sachin Gupta (eBay) argues that coding agents are generating a measurable but untracked liability he calls 'review debt' — the accumulating gap between code agents produce and code humans have actually reviewed, trusted, and understood. He backs this with industry data (commits up 25% year over year while PR comments dropped 27%; 31% more PRs merged with no review at all) and argues that headline productivity metrics like PR count, PR size, and cycle time are vanity metrics that measure speed of production rather than speed of trust. The core contribution is a deterministic scoring framework: five signal families (diff size and coupling, test evidence gap, directory/ownership spread, AI authorship indicators, and evidence/rationale gaps) with ten checks that compute a 0–100 review-burden score without any LLM in the loop, so scores stay stable and defensible to leadership. He walks three scored PRs — a clean one at 0, a high-debt one at 60, and a well-shaped AI-authored one at 7 — to show the framework penalizes PR shape, not agent authorship. A scan of 524 PRs across three public repos found AI authorship flat at 5–20% while review burden tracked volume and structural complexity instead, leading to his practical prescription: backfill the score over your last 200 PRs, calibrate weights against reviewer intuition, surface without blocking, and bring the number to retros.

## Key Points

- Review debt is defined as the accumulating gap between code an agent produced and code humans have actually reviewed, trusted, and understood, and it compounds like financial debt with interest paid in human attention rather than money.
- Industry data shows production and review attention moving in opposite directions: commits up 25% year over year while comments on PRs dropped 27%, median PR review time up 441.5%, and 31% more PRs merged with no review at all.
- Common AI-productivity metrics are vanity metrics — PR count rises when one PR splits into seven, larger median PR size is bloating rather than benefit, and falling cycle time can mean reviewers stopped pushing back.
- The debt compounds through three feedback loops: unreviewed code grounds tomorrow's agent suggestions, reviewer attention contracts to syntax when most of a PR was generated, and leadership resets velocity expectations without hiring proportional reviewers.
- All ten checks across the five signal families are deterministic and computable from the PR and its repo, deliberately avoiding LLM-as-judge because model changes make scores a moving target and undefensible in an engineering review.
- Agent-generated tests tend to assert what the code does rather than what it should do, locking in existing bugs, so the test-to-code ratio only measures whether tests showed up at all, not their quality.
- The AI authorship indicator is an amplifier, not a penalty — it contributed only 5 of 60 points on the high-debt example and 2 points on a well-shaped AI PR that scored 7, with the remaining burden coming from diff size, claim mismatch, and missing tests.
- Across 524 PRs in three public repos, AI authorship stayed flat at 5–20% while review burden varied with volume and structural complexity; one repo accumulated 186 senior reviewer hours in 27 days versus 43 for another over the same window.
- The recommended adoption path is backfill over the last 200 merged PRs, calibrate weights against reviewer gut feel, set a justify threshold (default 50), surface the score as a non-blocking PR comment, aggregate weekly per team, and discuss the slope in retros.

## Notable Quotes

> "I'm not saying that coding agents are bad. I'm not saying they don't make us faster. I'm saying they they're creating a kind of debt that nobody is measuring."
>
> — [0:00](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=0s) &middot; *Sets the talk's precise thesis and heads off the anti-AI reading.*

> "the commits climbed 25% year over year. And now over the same year, comments on the comments dropped 27%"
>
> — [0:43](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=43s) &middot; *The headline divergence the whole framework is built to measure.*

> "Median PR review time is up by 441.5% and if you see like if you calculate, you'll figure out that the reviewed PRs take 5.4 times longer than what they used to."
>
> — [0:43](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=43s) &middot; *Concrete magnitude on how much slower human review has become.*

> "AI is producing the pull request very fast, but humans cannot responsibly review them at that pace."
>
> — [1:40](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=100s) &middot; *One-sentence statement of the bottleneck.*

> "Every one of these numbers are real. None of them is a lie, but everyone is a vanity metric."
>
> — [2:25](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=145s) &middot; *The core methodological critique of current AI productivity reporting.*

> "PR count goes up when one PR splits into seven PRs. Median PR size going up is not a benefit, it's actually a bloating. Cycle time going down when reviewers stop pushing back."
>
> — [3:11](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=191s) &middot; *Names the specific mechanism by which each vanity metric misleads.*

> "These things tell you the speed of production. They do not tell you the speed of trust."
>
> — [3:11](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=191s) &middot; *The talk's most quotable framing of what's actually being measured.*

> "Tests are getting added, but they're actually asserting what the code did, not what the code should do. They lack in behavior, including bugs."
>
> — [4:01](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=241s) &middot; *Explains why test-count metrics give false assurance on agent PRs.*

> "It rhymes with technical debt, but it is more like a financial debt because it compounds. It actually accrues interest, but this interest is not money. This interest is paid in human attention."
>
> — [4:46](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=286s) &middot; *The definitional core of the concept.*

> "Code that was not deeply reviewed yesterday grounds tomorrow's PR. This debt becomes generative in nature."
>
> — [4:46](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=286s) &middot; *Identifies the feedback loop that distinguishes review debt from ordinary tech debt.*

> "Once leadership sees the new throughput, you don't get to hire reviewers in proportion. There is no slack left to pay the debt back."
>
> — [5:35](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=335s) &middot; *The organizational reason the debt can't be worked off.*

> "The same PR, basically the score that you got for the same PR, will score differently when your model will change."
>
> — [6:20](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=380s) &middot; *The central argument against LLM-as-judge for PR scoring.*

> "You want a number that is traceable to a deterministic computation"
>
> — [6:20](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=380s) &middot; *States the design constraint behind the entire framework.*

> "Agents are biased toward fix at the call site. A human engineer routes a fix to the root cause."
>
> — [7:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=429s) &middot; *A specific behavioral difference that explains why agent diffs sprawl.*

> "The review cost of a sprawling difference is not proportional to the size. It is actually much steeper."
>
> — [7:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=429s) &middot; *Nonlinearity claim that justifies weighting coupling separately from size.*

> "The agent gave you three hours of typing. You spend those three hours by multi-party reviewer attention."
>
> — [9:17](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=557s) &middot; *Crisply frames the economics of cross-team PR spread.*

> "A healthy PR produces a tiny, almost ceremonial report. That's exactly what you want."
>
> — [14:02](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=842s) &middot; *Design principle for keeping the tool from becoming noise.*

> "The score alone is useful. The structured advice is what actually moves the team behavior."
>
> — [14:51](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=891s) &middot; *Distinguishes this from score-only PR quality tools.*

> "The agent did not cause the score, but the shape of the PR that is created by the agent did this."
>
> — [15:33](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=933s) &middot; *The precise attribution claim that keeps the framework from being anti-AI.*

> "complexity drives burden, not authorship"
>
> — [17:56](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1076s) &middot; *The headline empirical finding from the 524-PR scan.*

> "Even if the agent wrote the code, even if the agent wrote the test, the human author confirms the test assert what the code should do"
>
> — [19:34](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1174s) &middot; *The concrete human-in-the-loop obligation he prescribes.*

> "The agent should not write the PR body. That's the moment the human author commits to understanding what they are actually shipping."
>
> — [20:24](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1224s) &middot; *A sharp, actionable rule others might disagree with.*

> "Post the score as a PR comment on every PR. Don't block it."
>
> — [21:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1269s) &middot; *The adoption stance — visibility over enforcement.*

> "That moves the discussion from feeling to measurement."
>
> — [22:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1368s) &middot; *Summarizes the purpose of having a number at all.*

> "who is accountable when an AI authored change causes an incident? Where is the audit trail?"
>
> — [22:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1368s) &middot; *Frames the 2027 governance shift the framework is meant to prepare for.*

> "The slope of a reviewed it over time matters most than the level."
>
> — [23:36](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1416s) &middot; *The key measurement guidance — trend over absolute score.*

## Positions

- Code production volume rose while review attention fell in the same year — commits up 25% year over year, PR comments down 27%. ([0:43](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=43s), confidence: stated)
- Among teams on the AI adoption curve, median PR review time is up 441.5% and 31% more PRs are merged with no review at all. ([0:43](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=43s), confidence: stated)
- Standard AI productivity metrics (PR count, PR size, cycle time) are real numbers but are vanity metrics that measure production speed, not trust. ([2:25](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=145s), confidence: stated)
- AI productivity gains are real but smaller than the hype — PR throughput grew about 8% while AI usage rose about 65%. ([2:25](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=145s), confidence: stated)
- Review debt compounds generatively because unreviewed code becomes grounding for the agent's future suggestions. ([4:46](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=286s), confidence: stated)
- PR scoring should be fully deterministic rather than LLM-judged, because LLM scores shift when the model changes and are not defensible to leadership. ([6:20](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=380s), confidence: stated)
- Agents preferentially fix at the call site rather than the root cause, producing diffs that sprawl across files. ([7:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=429s), confidence: stated)
- Agent-authored PRs ship with a consistently lower test-to-code ratio, and the tests they do write assert current behavior including bugs. ([7:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=468s), confidence: stated)
- Review cost grows super-linearly with cross-file and cross-team spread, not proportionally to diff size. ([7:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=429s), confidence: stated)
- AI authorship should be treated as an amplifier that adds reviewer attention, not as a penalty — it contributed only 5 of 60 points on the high-debt example. ([15:33](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=933s), confidence: stated)
- Across 524 PRs in three public repos, AI authorship stayed flat at 5–20% while review burden varied, so volume and structural complexity drive burden rather than authorship. ([17:56](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1076s), confidence: stated)
- Co-authored footers are the strongest AI authorship signal, but detection can be defeated — one repo showed 0% despite agent-authored code. ([10:41](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=641s), confidence: stated)
- Teams should calibrate the scoring weights against their own reviewer experience by backfilling over the last 200 merged PRs rather than adopting defaults blindly. ([12:37](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=757s), confidence: stated)
- The score should be surfaced on every PR but should never block merges. ([21:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1269s), confidence: stated)
- The agent should never write the PR body, because writing the 'why' is what commits the human author to understanding the change. ([20:24](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1224s), confidence: stated)
- AI PRs should be held to the same review standard as human PRs, with no exceptions. ([20:24](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1224s), confidence: stated)
- The slope of review debt over time is a more important signal than its absolute level. ([23:36](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1416s), confidence: stated)
- 2027 will be the year the industry conversation shifts from AI coding adoption to governance and accountability. ([22:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1368s), confidence: stated)
- None of the recommended practices require new tooling — teams already know these moves and simply fail to implement them. ([20:24](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1224s), confidence: stated)

## Concepts

- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [ai-generated code quality](../concepts/ai-generated-code-quality.md)
- [code review bottlenecks](../concepts/code-review-bottlenecks.md)
- [cognitive debt](../concepts/cognitive-debt.md)
- [developer productivity metrics](../concepts/developer-productivity-metrics.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [verifier design](../concepts/verifier-design.md)

