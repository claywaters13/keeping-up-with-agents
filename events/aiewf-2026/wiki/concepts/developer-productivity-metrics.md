---
title: "developer productivity metrics"
type: "concept"
slug: "developer-productivity-metrics"
tier: "supporting"
maturity: "contested"
talk_count: 8
speaker_count: 8
---

# developer productivity metrics

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **8** talk(s) by **8** speaker(s)

**Definition:** Measuring whether AI tooling actually made engineering faster or better — velocity, delivery, and adoption instrumentation.

*Also referred to as: developer velocity metrics, engineering productivity metrics, dora metrics, developer adoption metrics, software delivery metrics, engineering leverage metrics, dev loop velocity, adoption metrics*

## State of Practice

The field arrived at this conference having stopped believing its own throughput dashboards. Every speaker who cited hard numbers reported the same split: individual output metrics — commits, PR count, lines shipped, code deleted — are up sharply (25% more commits YoY, 14x commits at Anthropic, 861% more code deletion per PR), while the quality and team-level signals move the other way (PR comments down 27%, median review time up 441.5%, 31% more PRs merged with zero review, 242% more incidents per PR, and Google's 2026 DORA report showing individual effectiveness up but team throughput flat and delivery instability worse). The consequence is a rejection of the standard AI-productivity scorecard as vanity instrumentation: PR count rises when one change splits into seven, median PR size rising is bloat not benefit, and cycle time falls precisely when reviewers stop pushing back. Proposed replacements cluster into three families — review-side debt scoring computed deterministically per PR (eBay), engineering-throughput proxies less gameable than LOC such as commit rate and breadth of contributing developers (Wisedocs), and product-outcome metrics such as features used more than twice and repeat-usage frequency (VisualLabs). Against this, vendor-side speakers report large, concrete delivery multiples — roughly double the PRs versus single-point tools, 82% delivery-timeline compression, ~150% equivalent headcount from a three-month embed — which is exactly the number that the measurement skeptics say nobody has yet learned to verify. Cognition stated flatly that measuring agent ROI is an unsolved problem, and priced the solution at a $5 trillion market cap.

## Consensus

### AI adoption has raised individual output and code volume while degrading quality, stability, or team-level throughput — the gains and the costs land on different ledgers.

Support: **4** talk(s)

> "we basically feel more effective, we're more effective individually, but as a team, our throughput is kind of the same and our software breaks more often"
>
> — [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [2:20](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=140s)

Supporting talks: [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)

### Volume metrics — PR count, PR size, cycle time, lines of code, features shipped per quarter — are real numbers that no longer measure anything useful once an agent authors the code, and must be replaced.

Support: **3** talk(s)

> "Every one of these numbers are real. None of them is a lie, but everyone is a vanity metric."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [2:25](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=145s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)

### Human review attention, not model capability or code-writing speed, is the binding constraint on delivery, and throughput measured without accounting for it overstates the gain.

Support: **4** talk(s)

> "AI is producing the pull request very fast, but humans cannot responsibly review them at that pace."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [1:40](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=100s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)

### Writing code is a minority of the software engineering problem, so metrics anchored on code production measure the cheap part; the expensive parts are deciding what to build, investigating, testing, reviewing, and maintaining.

Support: **5** talk(s)

> "Because code got cheap, attention didn't."
>
> — [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [0:01](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1s)

Supporting talks: [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

### The ROI of agent deployment is currently not measured by anyone credibly — the costs being incurred (review burden, incidents, unreviewed code) have no instrumentation at all.

Support: **3** talk(s)

> "But most importantly, as forward deployed engineer, how do you measure the return on investment? And it's very ambiguous. And it's an unsolved problem because the company that will solve this will be um you know, $5 trillion market cap."
>
> — [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [5:18](https://www.youtube.com/watch?v=RVxym6mmIns&t=318s)

Supporting talks: [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)

## Disagreements

### Has agentic tooling actually delivered large team-level delivery gains, or only individual-level output gains that wash out in aggregate?

| Position A | Position B |
|---|---|
| The multiples are real and measurable at the org level: roughly double the PRs versus single-point tools, ~82% delivery-timeline compression, an ETL migration done in a third of the timeline with a three-month embed worth ~150% additional headcount, an order-of-magnitude increase in internal PR volume over six months, and features that previously took months now shipping in under a week.<br>*[How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)* | Aggregate gains are modest and partly offset: PR throughput grew ~8% while AI usage rose ~65%, DORA 2026 shows team throughput flat with delivery instability up, incidents per PR are up 242%, and bugs per developer are 6x 2025 — the visible multiples are production speed, not delivered value.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)* |

*Why it matters: This decides whether an engineering org sizes its agent budget against a 2-10x delivery multiple or against a single-digit throughput bump plus a new incident and review-debt liability. It also determines whether leadership is entitled to hold headcount flat after seeing the new throughput numbers.*

### Is model capability still the limiting factor on autonomous engineering work, or is the harness the only thing left to fix?

| Position A | Position B |
|---|---|
| Models are already good enough for most of this class of work; what remains is steering, context, scoring, and guardrails — and waiting on capability is a worse investment than automating your own dev loop, since a new frontier model lands roughly every 3.5 months.<br>*[From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)* | Frontier models still cannot self-validate or one-shot substantial multi-repo work — GPT 5.5 extra high produced 2,000 lines of scaffolding and silently omitted the model implementations — so reliability at 80%+ success, not harness polish, is the gate; that capability is roughly six months out.<br>*[Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)* |

*Why it matters: If the harness is the constraint, the right spend is on context plumbing, skills, and verification scoring you own. If capability is the constraint, that engineering is partly wasted work that the next model release absorbs, and the correct move is to keep humans in the loop and re-benchmark quarterly.*

### Should the human stay in the loop on each change, or should the human be engineered out of the middle of the loop entirely?

| Position A | Position B |
|---|---|
| Humans must verify each change: human PR review during a refactor spreads codebase context as well as gating quality, the human author must write the PR body and confirm the tests assert intended behavior, authentication/money/permissions/irreversible data get read line by line, and an agent must never grade its own work.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)* | Human attention is the throughput ceiling and should be removed from the interior of the loop: in a nine-step bug-fix-to-stage pipeline the human is needed only at steps 1 and 9, developers should not even queue their own agent tasks, and autonomous automations that pass an 80-90% trust bar should run without per-change human authorship.<br>*[Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)* |

*Why it matters: The answer sets what you can legitimately count as shipped work: if every change needs a human verifier, delivery scales with reviewer headcount and the review-debt metric is the real ceiling; if not, throughput scales with compute and the metric to instrument becomes trust rate and post-merge incident rate instead.*

## Practical Guidance

**Do:**

- Post a deterministic review-debt score as a comment on every PR — traceable to a computation, never LLM-judged — and never let it block a merge.
- Calibrate the scoring weights against your own reviewers' experience by backfilling over your last 200 merged PRs instead of adopting defaults.
- Track the slope of review debt over time rather than its absolute level.
- Read model time-horizon graphs at the 80% success rate, and ideally 90-99%, not the commonly published 50% — a 1-hour task at 50% is a coin flip on a wasted hour.
- Require 80-90% trust before letting an automation run unattended; 80% is fine for an agent you're supervising in the IDE.
- Replace 'features shipped last quarter' with 'features shipped that are used more than twice', and track repeat-usage frequency rather than session duration or time on site.
- Use commit rate and the breadth of developers contributing as refactor-payoff signals instead of lines of code.
- Verify an agent's performance fix against the actual production flow at runtime before merging — a plausible-looking diff is not evidence.
- Prioritize findings by ROI (impact weighed against review risk), not by raw impact, and surface one high-ROI human-readable finding at a time.
- Feed coding agents function- and file-level metrics; service- and endpoint-level granularity does not match how the agent reasons about code.
- Have the human author write the PR body — that is the moment they commit to understanding what they are shipping.
- Read every line of authentication, money movement, permissions, and irreversible data changes regardless of who wrote them.

**Avoid:**

- Reporting PR count, median PR size, or cycle time as evidence of AI productivity — PR count rises when one change splits into seven, and cycle time falls when reviewers stop pushing back.
- Scoring PRs with an LLM judge: the same PR scores differently when the model changes, and the number is not defensible to leadership.
- Merging PRs with no review at all, human or agentic.
- Letting the same agent write the code and write or grade its own tests — that hides the review rather than removing it.
- Treating token usage as the KPI, or deploying agents with no specific direction, which is just token maxing.
- Trusting a 20-page deep research report or an impressive demo as evidence — the features described may not exist, and demos carry almost no signal about production readiness.
- Auto-opening large volumes of agent PRs; a rain of 80 small pull requests destroys the habit you are trying to build.
- Accepting a lower test-to-code ratio on agent PRs, or tests that assert what the code currently does including its bugs.
- Making the human the throughput ceiling of the system while still keeping them as verifier.
- Shipping AI-native code without guardrails — high volume that nobody on the team understands reproduces exactly the legacy-codebase pathology you were escaping.

## Notable Outliers

- Across 524 PRs in three public repos, AI authorship stayed flat at 5-20% while review burden varied widely — so structural complexity, not who wrote the code, drives review cost; AI authorship contributed only 5 of 60 points on the worst example. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [17:56](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1076s))
- Median PR review time is up 441.5% among teams on the AI adoption curve — reviewed PRs now take 5.4x longer than they used to. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [0:43](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=43s))
- The largest value of coding agents is not accelerating existing work but automating an investigation phase that simply never happened in engineers' day-to-day lives — meaning the baseline for measuring it is zero, not 'slower'. ([From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [19:19](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1159s))
- At an internal hackathon, 17 of 21 agent ideas were abandoned for lack of business value or data access — the four survivors carried all the impact, so counting agents built measures nothing. ([You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s))
- The forward-deployed KPI has already flipped once: from maximizing token usage during the subsidized era to measurable delivery outcomes, because enterprises started asking whether they were getting real value. ([How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [10:32](https://www.youtube.com/watch?v=RVxym6mmIns&t=632s))
- The same refactor that took 3 hours and 10 major corrections with O3 now takes roughly one-fifth the time with Sonnet 4.6 / Opus 4.8 — slightly higher model cost, far less human intervention — which makes any productivity baseline older than a few months uncomparable. ([Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [6:13](https://www.youtube.com/watch?v=7vn4WpqNpck&t=373s))
- Package-download and language-share curves are being used as the field's adoption instrumentation: the Vercel AI SDK went from 1.6M to 15.1M weekly downloads in a year, and TypeScript passed Python on GitHub in August 2025. ([A Song of Types and Agents](../talks/a-song-of-types-and-agents.md), [11:03](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=663s))
- 2027 will be the year the industry conversation shifts from AI coding adoption to governance and accountability — who is accountable when an AI-authored change causes an incident, and where the audit trail lives. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [22:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1368s))

## All Talks

- [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)
- [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)
- [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

## Speakers

- [Alex Volkov](../speakers/alex-volkov.md)
- [Balázs Horváth](../speakers/balazs-horvath.md)
- [Denys Linkov](../speakers/denys-linkov.md)
- [Jia Wu](../speakers/jia-wu.md)
- [May Walter](../speakers/may-walter.md)
- [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)
- [Roberto Stagi](../speakers/roberto-stagi.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)

