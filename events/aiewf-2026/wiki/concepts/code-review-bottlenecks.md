---
title: "code review bottlenecks"
type: "concept"
slug: "code-review-bottlenecks"
tier: "supporting"
maturity: "contested"
talk_count: 7
speaker_count: 8
---

# code review bottlenecks

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **7** talk(s) by **8** speaker(s)

**Definition:** Human review becoming the constraint once agents generate code faster than people can read it, and how teams restructure review to cope.

*Also referred to as: code review as bottleneck, code review burden, review debt, code review burden distribution, human attention as bottleneck, pull request sizing and coupling, stacked pull requests*

## State of Practice

The conference treats the review bottleneck as established fact rather than a prediction: eBay's telemetry showed commits up 25% year over year while PR comments dropped 27%, median review time up 441.5%, and 31% more PRs merged with no review at all — while actual PR throughput grew only ~8% against ~65% more AI usage. Speakers agree the binding constraint has moved from token or compute cost to human attention, and that the damage compounds because unreviewed code becomes grounding context for the agent's next suggestion. The dominant structural response is to stop treating review as a downstream filter and instead reshape what arrives at it: decompose monolithic agent output into small independently-reviewable slices (stacked diffs, one migration per context window), apply backpressure so loops cannot outrun reviewers, and move alignment upstream into durable shared docs so reviewers only adjudicate decisions already framed. A second response is measurement — deterministic, non-LLM PR scoring that surfaces structural review cost (cross-file and cross-team sprawl, test-to-code ratio) without blocking merges, on the argument that LLM-judged scores drift when the model changes and are indefensible to leadership. Where the field splits is on the remedy's direction: whether to make humans read less (better verification loops, agents as the inner loop) or to make code more readable and gate throughput on human comprehension. Nearly everyone rejects the pure 'code is read-only now' position as either unproven, unaffordable outside a frontier lab, or an org-level failure mode that dumps review burden on the least AI-adopted engineers.

## Consensus

### Agent code generation now outpaces human review capacity, making review attention — not tokens or compute — the binding constraint on shipping.

Support: **5** talk(s)

> "AI is producing the pull request very fast, but humans cannot responsibly review them at that pace."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [1:40](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=100s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)

### Individual output gains from agents do not convert into team throughput, because the surplus is absorbed by review burden that lands on other people.

Support: **3** talk(s)

> "The problem we work on at Ref is one you might be familiar with where individual engineers are going really fast with AI, but the team as a whole is not."
>
> — [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [0:12](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=12s)

Supporting talks: [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

### Large monolithic agent-authored diffs should be decomposed into small, independently reviewable slices, because review cost rises super-linearly with cross-file and cross-team spread rather than proportionally to line count.

Support: **3** talk(s)

> "We really like Graphite because it allows for asynchronous review, right? I could be working on a PR all the way up here while a domain specialist is still reviewing a different PR."
>
> — [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [11:38](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=698s)

Supporting talks: [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

### The human author must retain and demonstrate ownership of agent-written code before it reaches a reviewer — the agent may write the code, but not the understanding, the PR narrative, or the critical decisions.

Support: **4** talk(s)

> "my rule is I don't send code to uh others on my team to review unless I can pass the quiz about what my agents wrote"
>
> — [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [10:55](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=655s)

Supporting talks: [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)

### Alignment and context should live in durable, shared, version-controlled artifacts rather than in individuals' ephemeral agent sessions, so that review adjudicates already-framed decisions instead of reverse-engineering intent from a diff.

Support: **4** talk(s)

> "What you want is to separate the the agent as the action and the doc as the state."
>
> — [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [13:21](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=801s)

Supporting talks: [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)

## Disagreements

### Is the fix for the review bottleneck to have humans read less code, or to keep reading and make the code easier to read?

| Position A | Position B |
|---|---|
| Reading agent output remains essential and loops should be designed to make code more readable; the 'code is read-only now' thesis is unproven and unaffordable outside a frontier lab, and AI-authored PRs get no exemption from the normal review standard.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)* | Human correctness-checking is legitimately declining and should keep declining; watching or closely reading agent generation is largely wasted attention, and the human role moves to setting direction in an outer loop while automated verification and self-healing pipelines catch defects.<br>*[The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* |

*Why it matters: It decides whether you invest in review capacity, readability, and comprehension gates, or in verifiers, sensors, and slop-detection pipelines — and whether a 40,000-line agent PR is a process failure or an acceptable artifact nobody needs to read.*

### Should teams throttle agent throughput with hard gates, or leave throughput alone and only make its cost visible?

| Position A | Position B |
|---|---|
| Apply hard backpressure: a loop should never open a new PR while its previous one is unreviewed, code should not go out for team review until the author can pass a quiz on it, and plans should be handed to a human teammate before implementation starts.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* | Never block: post a deterministic review-debt score as a comment on every PR and let it merge, invest in detection and self-healing because slop is inevitable, and lean into parallelism — run five or six approaches and pick the best.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* |

*Why it matters: Gating caps throughput at human review speed, which forfeits most of the headline productivity claim; visibility-only preserves throughput but relies on teams voluntarily paying down a debt that eBay's data says they demonstrably do not pay down once leadership has seen the new numbers.*

### Should engineering effort go into preventing bad agent output or into detecting and repairing it after the fact?

| Position A | Position B |
|---|---|
| Slop is inevitable, so build detection and self-healing pipelines to close the loop rather than trying to prevent it upstream; a developer babysitting an agent is itself the defect signal.<br>*[Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* | Bad code is more expensive in the age of agents than ever before, so prevent it: hand-write golden patterns before turning the agent loose, use deterministic sensors like AST-grep that agents cannot disable with inline comments, and never send an agent to do deterministic code's job.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)* |

*Why it matters: Detection-first accepts a steady-state level of unreviewed code in the repo, which is precisely the substrate that grounds tomorrow's agent suggestions; prevention-first costs upfront IC time on patterns and sensors that produce no immediate PRs.*

## Practical Guidance

**Do:**

- Cap any agent loop at one open PR at a time — do not open a new PR while the previous one from that loop is still unreviewed.
- Give each unit of work (e.g. each of 150 RPC migrations) its own context window in a separate implementation phase rather than batching them into one PR.
- Use stacked diffs (Graphite or equivalent) to decompose a proven prototype so domain specialists review their own slice asynchronously.
- Require the human author, not the agent, to write the PR body — that is the moment they commit to understanding what they are shipping.
- Gate sending code out for team review on being able to pass a quiz about what the agent wrote.
- Post a deterministic (not LLM-judged) review-cost score as a comment on every PR, and calibrate its weights by backfilling over your last 200 merged PRs before trusting the defaults.
- Track the slope of review debt over time rather than its absolute level.
- Have the human author verify that agent-written tests assert what the code should do, not merely what it currently does.
- Use out-of-band sensors like AST-grep for loop feedback instead of lint or TypeScript config, which coding agents disable with inline comments.
- Keep loop feedback in a version-controlled markdown file and run loops on existing CI (GitHub Actions/GitLab/CircleCI) rather than a dedicated cluster.
- Write the design/taxonomy doc before software engineers join the project, and put agent plans and conversations in shared commentable spaces rather than individual terminals.
- Standardize the team's agent setup from your best ICs' practices, since uneven adoption dumps review burden on the low-adoption engineers.

**Avoid:**

- Don't treat PR count, PR size, or cycle time as productivity evidence — PR count rises when one PR splits into seven, and cycle time drops when reviewers stop pushing back.
- Don't use an LLM as the PR-scoring judge: the same PR scores differently when the model changes, so the number isn't defensible to leadership.
- Don't grant AI-authored PRs a lower review standard, and don't penalize AI authorship either — measured across 524 PRs, complexity drove review burden, not authorship.
- Don't run blind prompt-in-a-bash-loop setups on team or critical systems; they produce 40,000-line PRs nobody wants to read even with verifier and review agents attached.
- Don't let agent adoption go uneven within a team — the 10-PR-a-day engineers look like gods while the 1-2-PR engineers inherit the review queue and turn hostile to agents.
- Don't rely on chat threads or plan mode as the alignment artifact; they are isolated, ephemeral, and encourage accepting the agent's recommended option without thinking.
- Don't accept agent fixes applied at the call site instead of the root cause — they sprawl across files and teams, and review cost climbs much faster than diff size.
- Don't delegate every bug fix to an agent; you forfeit the peripheral feel for the system that debugging gives you.
- Don't send an agent to do work deterministic code can do.
- Don't let a first prompt balloon to 40-50K tokens of baseline context — that means progressive disclosure has failed.

## Notable Outliers

- Review debt compounds generatively rather than merely accumulating: code that wasn't deeply reviewed yesterday becomes the grounding context for tomorrow's agent-written PR. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [4:46](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=286s))
- Across 524 PRs in three public repos, AI authorship stayed flat at 5-20% while review burden varied widely — so volume and structural complexity drive review cost, not authorship. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [17:56](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1076s))
- Correctness checking is the wrong reason to read agent code; the real reason is understanding-to-participate, and degraded understanding accrues like tech debt until you can no longer contribute to your own project. ([Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [5:09](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=309s))
- Long agent run times are a feature, not a problem — under the reasoning paradigm the longer the agent thinks, the better its output, so a skill running over an hour is fine. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [12:20](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=740s))
- High token throughput (750 tok/s on Cerebras) matters not because one answer arrives faster but because it lets you run five or six parallel approaches and pick the best — which multiplies, rather than relieves, downstream selection work. ([The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [16:07](https://www.youtube.com/watch?v=pMggiOb18tc&t=967s))
- Plans written and then deliberately not implemented are a positive signal, because it means ideas are being explored and prioritized instead of built by default. ([Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [14:08](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=848s))
- 2027 will be the year the industry conversation shifts from AI coding adoption to governance and accountability — who is responsible when an AI-authored change causes an incident, and where the audit trail lives. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [22:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1368s))

## All Talks

- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)
- [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Alexander Embiricos](../speakers/alexander-embiricos.md)
- [Deepak Pathak](../speakers/deepak-pathak.md)
- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [Matt Dailey](../speakers/matt-dailey.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)

