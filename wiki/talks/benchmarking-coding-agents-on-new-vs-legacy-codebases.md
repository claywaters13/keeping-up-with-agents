---
title: "Benchmarking Coding Agents on New vs Legacy Codebases"
type: "talk"
slug: "benchmarking-coding-agents-on-new-vs-legacy-codebases"
track: "Agentic Engineering"
org: "Wisedocs"
day: "Day 4 — Session Day 3"
room: "Track 8"
video_id: "7vn4WpqNpck"
duration_sec: 1087
word_count: 3481
speakers: ["Denys Linkov"]
---

# Benchmarking Coding Agents on New vs Legacy Codebases

*Program title: Benchmarking Coding Agents on New vs Legacy Code bases*

**Speakers:** [Denys Linkov](../speakers/denys-linkov.md)

**Org:** Wisedocs

**Track:** Agentic Engineering &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 18m 07s

[Watch on YouTube](https://www.youtube.com/watch?v=7vn4WpqNpck)

## Summary

Denys Linkov of Wisedocs recounts a six-month refactor that consolidated 10+ legacy repos into a monorepo for an AI pipeline that processes 10,000+ page medical claim PDFs, and asks whether the team should have simply waited for better coding agents instead. He re-runs his April benchmarks on current models to quantify the improvement: a Temporal refactor that took 3 hours of back-and-forth with O3 and produced 10 major mistakes is now nearly one-shot by Opus 4.8, and the equivalent work would take about 1/5 the time. But when he asks GPT 5.5 to zero-shot the whole refactor, it finishes in 10 minutes with 2,000 lines of scaffolding and no actual model implementations — evidence that self-validating, end-to-end refactors are close but not here. He argues teams should reason about METR-style time-horizon curves at 90-99% success rather than 50%, because a coin-flip on a long agent run wastes both compute and human attention. His verdict: the refactor was worth doing now — pipeline time and cost dropped, features that took months ship in under a week, and nearly every developer in the company now commits to the clean monorepo.

## Key Points

- The business trigger for the refactor was threefold: too slow to meet customer demand, an AI pipeline too complicated to update, and a legacy codebase spread across 10+ repos that nobody wanted to touch.
- Re-running the same refactor benchmark across model generations shows a step change: O3 required 3 hours of manual guidance and made 10 major mistakes, Sonnet 4.6 needed one extra iteration, and Opus 4.8 essentially one-shot it.
- The change is as much about harnesses as models — modern runs show sub-agents, plan calls, shell commands, and verification steps that were absent with O3, making execution more expensive in tokens but far less manual.
- Asking a frontier model to zero-shot the entire refactor produced only 2,000 lines of scaffolding in 10 minutes, with the actual ML model deployments skipped, showing models still cannot self-validate large refactors.
- Time-horizon graphs should be read at 90% or 99% success rather than the standard 50%, because a one-hour agent run with a 50% completion rate likely wastes the hour and the developer's attention.
- Shipping velocity in the new monorepo rose sharply and stayed high after reaching parity, with the commit rate increasing and nearly every developer in the company now contributing even outside their area of expertise.
- AI-native development can regenerate legacy conditions — large volumes of low-quality code nobody understands — so guardrails matter whether you refactor fully or partially.
- Concrete outcomes beyond velocity: reduced pipeline runtime, lower cost, support for larger files, features shipping in under a week that previously took months, and patterns from the monorepo spreading to other repos.
- Multi-repo setups are now easier for models to navigate if nested under a common folder, but end-to-end testing, verification, deployment, and sandbox setup remain materially harder than in a monorepo.

## Notable Quotes

> "we're too slow to meet customer demand. The second one is that this AI pipeline that we've built is too complicated to update. And the third one is because it's a legacy code base, or actually more than 10 repos, nobody actually wants to touch the code."
>
> — [0:01](https://www.youtube.com/watch?v=7vn4WpqNpck&t=1s) &middot; *states the business case for the refactor in the speaker's own framing*

> "the company I work at, WiseDocs, processes complex medical claims, which are PDFs that are more than 10,000 pages in size. Some of these files are bigger than video files."
>
> — [0:42](https://www.youtube.com/watch?v=7vn4WpqNpck&t=42s) &middot; *establishes the unusual scale constraint that shapes the whole pipeline*

> "If we introduce additional complexity into our code base, we can very quickly outrun the ROI we've generated."
>
> — [1:46](https://www.youtube.com/watch?v=7vn4WpqNpck&t=106s) &middot; *compact statement of his tech-debt-as-financial-debt thesis*

> "So even though we're shipping faster and faster, the code quality and the product quality has not necessarily gone up."
>
> — [3:04](https://www.youtube.com/watch?v=7vn4WpqNpck&t=184s) &middot; *the contrarian counterweight to the velocity case studies he just showed*

> "it's very easy to undergo AI psychosis, where you look at a deep research report that's 20 pages long and you say, "Wow, this looks good." And then those features don't actually exist in the product, and you've set yourself back."
>
> — [4:24](https://www.youtube.com/watch?v=7vn4WpqNpck&t=264s) &middot; *names a specific failure mode of agentic research workflows*

> "This refactor took uh 3 hours of back and forth chatting with Incursr, but it made 10 major mistakes."
>
> — [4:59](https://www.youtube.com/watch?v=7vn4WpqNpck&t=299s) &middot; *the 2025 baseline number the whole benchmark comparison rests on*

> "Sonnet 4.6 with one additional iteration was able to solve the task. And with Opus, it was basically able to one-shot this problem. So, models are getting significantly better along with harnesses."
>
> — [5:34](https://www.youtube.com/watch?v=7vn4WpqNpck&t=334s) &middot; *the headline benchmark result across model generations*

> "if I was rebuilding the same task that I had for for this refactor, it would take around 1/5 of the time to accomplish, which is pretty good progress."
>
> — [6:13](https://www.youtube.com/watch?v=7vn4WpqNpck&t=373s) &middot; *quantifies the productivity delta on an identical task*

> "typically this graph is shared with the 50% accuracy rate, but I think it's much better to actually look at the 80% accuracy rate or higher."
>
> — [7:55](https://www.youtube.com/watch?v=7vn4WpqNpck&t=475s) &middot; *takes a methodological side on how to read METR time-horizon results*

> "if you're kicking off a process that is going to take an hour and it has a 50% chance of completing, there's a very high chance you just wasted that hour and you could have been doing something different."
>
> — [8:33](https://www.youtube.com/watch?v=7vn4WpqNpck&t=513s) &middot; *the practical argument for high-reliability thresholds over median success*

> "we're making rapid progress in in the AI model space, but we're still not there where you can just kick off an agent and have something be completed reliably."
>
> — [9:02](https://www.youtube.com/watch?v=7vn4WpqNpck&t=542s) &middot; *his overall calibration claim about current agent reliability*

> "it completed its goal in in 10 minutes and 22 seconds. And it only wrote 2,000 lines of code, which was a little bit fishy."
>
> — [11:31](https://www.youtube.com/watch?v=7vn4WpqNpck&t=691s) &middot; *the zero-shot experiment result, and the tell that exposed it*

> "we're still not there where models can self-validate and just one-shot these kinds of problems, but we're getting close. I think in in 6 months, we'll get to the point that we can complete pretty substantial refactors"
>
> — [12:13](https://www.youtube.com/watch?v=7vn4WpqNpck&t=733s) &middot; *a dated, falsifiable forecast about large-refactor capability*

> "taking on technical debt and refactoring later is getting exponentially easier as the days go by."
>
> — [12:45](https://www.youtube.com/watch?v=7vn4WpqNpck&t=765s) &middot; *steelmans the wait-for-better-models position he ultimately rejects*

> "when you build a lot of code and you do this kind of development in an AI AI-native world, it starts looking like some of the legacy code we've we've seen in the past."
>
> — [12:45](https://www.youtube.com/watch?v=7vn4WpqNpck&t=765s) &middot; *argues AI-generated code reproduces the legacy problem rather than solving it*

> "now we can ship features that would take multiple months in under a week"
>
> — [13:51](https://www.youtube.com/watch?v=7vn4WpqNpck&t=831s) &middot; *the concrete payoff metric justifying the refactor decision*

> "beyond just shipping velocity, developers actually want to work in this codebase"
>
> — [13:51](https://www.youtube.com/watch?v=7vn4WpqNpck&t=831s) &middot; *names a non-velocity benefit that motivated the original problem statement*

> "models will continue to get better, uh but sometimes it's good to pause, build a monorepo, and forge ahead."
>
> — [14:24](https://www.youtube.com/watch?v=7vn4WpqNpck&t=864s) &middot; *the talk's closing verdict in one line*

> "But, for doing that end-to-end testing and verification and deployment, it's still much harder to do with multiple repos."
>
> — [15:00](https://www.youtube.com/watch?v=7vn4WpqNpck&t=900s) &middot; *the specific tradeoff that survives even as models get better at multi-repo navigation*

> "So, our PR reviews were all all human PR reviews during that refactor."
>
> — [16:05](https://www.youtube.com/watch?v=7vn4WpqNpck&t=965s) &middot; *reveals the human-in-the-loop discipline behind the reported velocity gains*

> "I think we got uh 15 out of 17 requirements right when we were going ahead with the refactor."
>
> — [16:05](https://www.youtube.com/watch?v=7vn4WpqNpck&t=965s) &middot; *a rare number on how well up-front requirements held up*

## Positions

- The six-month monorepo refactor was worth doing in 2025 rather than deferring a year to wait for better models and harnesses. ([13:18](https://www.youtube.com/watch?v=7vn4WpqNpck&t=798s), confidence: stated)
- Model time-horizon graphs should be evaluated at 80%, and ideally 90-99%, success rates rather than the commonly shared 50%, because that is where the developer's mental model of delegation actually works. ([7:55](https://www.youtube.com/watch?v=7vn4WpqNpck&t=475s), confidence: stated)
- Frontier models cannot yet self-validate or one-shot a substantial multi-repo refactor; GPT 5.5 extra high produced only scaffolding and omitted the model implementations. ([12:13](https://www.youtube.com/watch?v=7vn4WpqNpck&t=733s), confidence: stated)
- Within about six months, models will be able to complete substantial refactors consistently. ([12:13](https://www.youtube.com/watch?v=7vn4WpqNpck&t=733s), confidence: stated)
- Software shipping speed has increased over the past five years while product quality, maintainability, and reliability have degraded — cited uptimes at two leading companies fall below three or four nines. ([3:04](https://www.youtube.com/watch?v=7vn4WpqNpck&t=184s), confidence: stated)
- AI-native development without guardrails reproduces legacy-codebase pathologies: large volumes of low-quality code that nobody on the team understands. ([13:18](https://www.youtube.com/watch?v=7vn4WpqNpck&t=798s), confidence: stated)
- The same refactor task that took 3 hours and 10 major corrections with O3 now takes roughly one-fifth the time with Sonnet 4.6 / Opus 4.8, with model cost slightly higher but far less manual intervention. ([6:13](https://www.youtube.com/watch?v=7vn4WpqNpck&t=373s), confidence: stated)
- A monorepo still beats multiple repos for agentic development because end-to-end testing, verification, deployment, and sandbox cloning are harder across repos, even though models now navigate multi-repo directory trees well. ([15:00](https://www.youtube.com/watch?v=7vn4WpqNpck&t=900s), confidence: stated)
- The two-month, five-project orchestrator evaluation the team ran manually could now be done roughly 90% faster with deep research plus per-criterion sub-agents. ([3:45](https://www.youtube.com/watch?v=7vn4WpqNpck&t=225s), confidence: stated)
- Human PR review remains valuable during a refactor not just as a quality gate but as a mechanism for spreading context about the codebase among developers. ([16:46](https://www.youtube.com/watch?v=7vn4WpqNpck&t=1006s), confidence: implied)
- Lines of code is a poor productivity metric, so commit rate and breadth of contributing developers are better signals of the refactor's payoff. ([10:50](https://www.youtube.com/watch?v=7vn4WpqNpck&t=650s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [ai-generated code quality](../concepts/ai-generated-code-quality.md)
- [coding agent benchmarking](../concepts/coding-agent-benchmarking.md)
- [developer productivity metrics](../concepts/developer-productivity-metrics.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [legacy code migration](../concepts/legacy-code-migration.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [roi measurement](../concepts/roi-measurement.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

