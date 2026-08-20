---
title: "code review bottlenecks"
type: "concept"
slug: "code-review-bottlenecks"
tier: "supporting"
maturity: "contested"
talk_count: 8
speaker_count: 9
---

# code review bottlenecks

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **8** talk(s) by **9** speaker(s)

**Definition:** Human review becoming the constraint once agents generate code faster than people can read it, and how teams restructure review to cope.

*Also referred to as: code review as bottleneck, code review burden, review debt, code review burden distribution, human attention as bottleneck, pull request sizing and coupling, stacked pull requests*

## State of Practice

The conference treated review capacity as the confirmed binding constraint of agent-assisted engineering: eBay's telemetry showed commits up 25% year over year while PR comments fell 27%, median review time up 441.5%, and 31% more PRs merged with no review at all, against only ~8% PR throughput gain for ~65% more AI usage. The framing has shifted from 'is there a bottleneck' to 'what exactly is scarce' — OpenAI named attention rather than tokens or compute, Notion's Geoffrey Litt argued correctness-checking is the wrong thing to protect and understanding is the real scarce good, and Ref framed the problem as output without impact. The practical remedies converge on backpressure and decomposition: hard caps on PR size (500 lines at Maven), one open PR at a time per loop at HumanLayer, stacked diffs with per-slice subject-matter reviewers at Higharc, and deterministic per-PR debt scores posted as comments rather than merge blocks at eBay. A second, structural remedy is to move human judgment upstream of code — durable decision docs, one-to-two-page PRDs, hand-written golden patterns, research taxonomy documents — on the theory that the expensive part of review is deciding what matters, which is cheaper to settle before the diff exists. AI code reviewers were universally described as helpful but not yet trustworthy enough to be the gate, and the second-order harm nobody has solved is compounding: unreviewed code becomes grounding context for the next agent's suggestions, and review burden silently migrates onto the lowest-adoption engineers on a team.

## Consensus

### Generation now outpaces human review capacity, so review — not writing code — is the constraint on shipping.

Support: **5** talk(s)

> "AI is producing the pull request very fast, but humans cannot responsibly review them at that pace."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [1:40](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=100s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)

### Large agent-authored PRs are effectively unreviewable and must be decomposed into small, independently reviewable slices before they reach a human.

Support: **4** talk(s)

> "each PR shouldn't have more than 500 lines of code because nobody can do a meaningful code review with the ones has like thousands of lines code."
>
> — [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [11:35](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=695s)

Supporting talks: [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)

### The dominant failure mode is not bad agent code but silent approval — rubber-stamped or unreviewed merges that give false confidence and then compound as grounding for future agent output.

Support: **4** talk(s)

> "One thing we really want to avoid is a rubber stamp, we call it. Means like people submit code review, you cannot really do anything to it. You just say blindly approve it. This is the worst case, we should really avoid because that's just give us false confidence."
>
> — [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [12:14](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=734s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)

### The way to shrink review cost is to move human judgment upstream — into durable plans, specs, taxonomy docs, and hand-written reference patterns — because the expensive part of review is deciding what matters.

Support: **5** talk(s)

> "the code review is easier because the hardest part of any code review is, you know, what actually matters here."
>
> — [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [15:58](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=958s)

Supporting talks: [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)

### AI code-review tools materially help but are not yet trustworthy enough to be the gate; stacking verifier and reviewer agents does not by itself make a large PR safe to merge.

Support: **3** talk(s)

> "We also tried the multiple like AI coding review review tools. It helps a little bit, but we don't feel comfortable 100% rely on them yet."
>
> — [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [10:50](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=650s)

Supporting talks: [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

### Whatever the review process, the human author must remain the accountable owner and demonstrate understanding of the change before handing it to reviewers.

Support: **4** talk(s)

> "The agent should not write the PR body. That's the moment the human author commits to understanding what they are actually shipping."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [20:24](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1224s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)

## Disagreements

### Do humans still need to read agent-generated code, or should human attention move off correctness entirely?

| Position A | Position B |
|---|---|
| Humans must keep reading the code. Bad code is more expensive than ever in the agent era, loops should be designed to make code easier to read rather than to make reading unnecessary, AI-authored PRs get the same review standard as human ones with no exceptions, and letting the agent make a decision you did not read means you no longer own that code.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* | Human correctness-checking is declining and should decline. Watching agents generate code is a waste of time now that models understand intent, verification loops should absorb correctness, AI does essentially all implementation, and engineers can self-identify that a PR needs no review and merge it while staying accountable.<br>*[The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)* |

*Why it matters: If reading is optional, the fix is more automated verification and higher parallelism; if reading is mandatory, throughput must be throttled to human absorption rate and review headcount becomes the hard ceiling on shipping.*

### Should agent output be throttled to what humans can absorb, or should teams accept the volume and invest in detection and cleanup?

| Position A | Position B |
|---|---|
| Apply backpressure at the source: never open a new PR while the previous one from that loop is unreviewed, cap PRs at 500 lines, score every PR for review debt and watch the slope, and shape the diff so reviewer attention stays bounded.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)* | Volume is fine and slop is inevitable, so invest in detection and self-healing pipelines rather than prevention; long agent runs are good, and high throughput is valuable precisely because it lets you run five or six parallel approaches and pick the best.<br>*[Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* |

*Why it matters: Backpressure caps team throughput at reviewer capacity but keeps the codebase legible; the accept-and-clean-up path bets that automated detection catches what humans no longer read, and eBay's data suggests unreviewed code compounds into future agent context if that bet is wrong.*

## Practical Guidance

**Do:**

- Cap PRs at 500 lines; treat thousand-line diffs as unreviewable by construction
- Have a loop or agent hold at one open PR at a time — never open a new one while the previous output is still unreviewed
- Use stacked diffs to decompose a proven prototype so specific subject-matter experts review specific slices asynchronously
- Score every PR deterministically (not with an LLM judge, whose scores shift when the model changes) and post the score as a comment without blocking the merge
- Backfill the scoring weights over your last 200 merged PRs to calibrate against your own reviewers' experience before adopting defaults
- Track the slope of review debt over time rather than its absolute level
- Require the human author to write the PR body themselves, and to confirm the tests assert what the code should do rather than what it currently does
- Gate sending code to teammates on being able to pass a quiz about what the agent wrote
- Settle the decisions that matter in a durable, shared, commentable doc before implementation, so agents start stateless from the same state and review only checks execution
- Hand-write golden/idiomatic patterns in the repo before turning a loop loose, since coding agents are pattern replicators
- Start adoption on low-risk, easily verified work (unit tests, documentation) before widening scope
- Watch for review burden migrating onto low-adoption engineers, who end up reviewing the high-adopters' PRs and grow hostile to agents as a result
- Give each unit of work (e.g. each migration) its own context window in a separate implementation phase — cheaper and more reliable than batching

**Avoid:**

- Rubber-stamping: approving a PR you cannot meaningfully evaluate, which buys false confidence rather than review
- Treating PR count, PR size, and cycle time as proof of AI value — they measure production speed, not trust, and cycle time drops when reviewers stop pushing back
- Blind prompt-in-a-bash-loop setups on team-owned critical systems; multiple verifier and code-review agents still yield 40,000-line PRs nobody reads
- Assuming AI code-review tools are reliable enough to be the merge gate today
- Penalizing PRs for AI authorship — complexity and cross-file/cross-team spread drive review cost, and authorship detection is defeatable (one repo read 0% despite agent-authored code)
- Letting the agent fix at the call site instead of the root cause, which sprawls the diff across files and makes review cost grow super-linearly
- Delegating a bug fix entirely to an agent when you needed the peripheral understanding of the system that debugging it yourself would have given you
- Expecting to hire reviewers in proportion to the new throughput — once leadership sees it, there is no slack left to pay the debt back
- Letting agent conversations and plans live only in individuals' local terminals, when understanding is a team-level property

## Notable Outliers

- Review debt is financial rather than technical debt: it compounds generatively because code that was not deeply reviewed yesterday becomes the grounding context for tomorrow's agent-authored PR. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [4:46](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=286s))
- Across 524 PRs in three public repos, AI authorship stayed flat at 5–20% while review burden varied widely — complexity drives burden, not authorship. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [17:56](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1076s))
- A personal rule: don't send code to teammates for review unless you can pass a quiz about what your agents wrote — the quiz is the speed regulator that keeps you moving at the speed of understanding, not just correctness. ([Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [10:55](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=655s))
- A loop must never stack unreviewed work: no human reviewed the last output, so there is no reason to pile up more for humans to review. ([Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [15:57](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=957s))
- Uneven agent adoption is actively harmful — the engineer shipping one or two PRs a day inherits the review burden for the engineer shipping ten. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [5:49](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=349s))
- Plans that get written and then never implemented are a positive signal, because ideas are being explored and prioritized rather than built by default — shifting from code velocity to idea velocity. ([Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [14:08](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=848s))
- Attention, not tokens or compute, is the binding constraint — and unlike tokens, you cannot simply add more of it. ([The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [21:16](https://www.youtube.com/watch?v=pMggiOb18tc&t=1276s))

## All Talks

- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)
- [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Alexander Embiricos](../speakers/alexander-embiricos.md)
- [Dan Feng](../speakers/dan-feng.md)
- [Deepak Pathak](../speakers/deepak-pathak.md)
- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [Matt Dailey](../speakers/matt-dailey.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)

