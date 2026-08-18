---
title: "Building an Autonomous Engineering Org"
type: "talk"
slug: "building-an-autonomous-engineering-org"
track: "Design Engineering"
org: "Agentic AI Foundation"
day: "Day 3 — Session Day 2"
room: "Track 6"
video_id: "whue9_YquGA"
duration_sec: 1056
word_count: 2725
speakers: ["Eve Bouffard"]
---

# Building an Autonomous Engineering Org

*Program title: Imagination Engineering*

**Speakers:** [Eve Bouffard](../speakers/eve-bouffard.md)

**Org:** Agentic AI Foundation

**Track:** Design Engineering &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 6 &nbsp;|&nbsp; **Duration:** 17m 36s

[Watch on YouTube](https://www.youtube.com/watch?v=whue9_YquGA)

## Summary

Angie Jones recounts a two-year effort to convert Block's 3,500-person engineering organization from AI-curious to autonomous, and the uncomfortable ending that came with it. The core problem she diagnoses is that ~90% adoption of coding agents produced no faster shipping, because engineers were using AI inside the IDE rather than delegating real work to it. Her answer was a five-stage maturity model plus a deliberately elitist strategy: hand-pick ~50 'AI champions' from the most critical repos, have them make those repos agent-ready (context files, rules, slash commands, AI reviewers, PR attribution), then let that foundation lift everyone else. She walks through the concrete unlocks at each stage — delegation from Slack/Jira/GitHub issues, an auto-fix loop on top of Codex reviews, isolated cloud workspaces for parallel agents, and a machine-readable 'world model' of 25,000 repos powering an in-house orchestrator — with reported gains of 69% more AI-authored code and 21x automated PRs. It is worth watching both as one of the few end-to-end org-level playbooks and for its ending, where the success is followed by layoffs and Jones openly asks whether she helped cause them.

## Key Points

- High AI tool adoption is not the same as impact: 90% of Block's engineers were using Goose or Claude Code regularly, yet the CEO correctly observed that features weren't reaching customers any faster.
- Jones frames AI enablement in three phases — experimentation, adoption, impact — and defines an agentic engineering org as one where engineers use agents as their primary means of producing engineering outcomes.
- Her maturity model runs from stage zero (no AI) through autocomplete, chat, delegating-and-reviewing, multi-agent parallelism, up to stage five where agents produce shippable results without human hand-holding.
- Rather than trying to level up all 3,500 engineers, she applied the 1/9/90 rule and hand-picked ~50 champions from critical repos who committed at least 30% of their time, so the work of the 1% would lift everyone else.
- Repo readiness was the leverage point: context files (agents.md/claude.md), rules files, slash commands and skills, an enabled AI code reviewer with instructions, and AI attribution on PRs — standardized as components but customized per repo rather than mandated top-down.
- Delegation had to meet engineers where requirements already arrive — Slack, Jira/Linear, and GitHub issues — so adoption required no new skill; in one case a bug went from Slack discussion to merged-ready PR in about five minutes.
- Stage four exposed second-order bottlenecks: PR review queues backed up under 3-4x PR volume, and laptops ran out of memory running parallel agents, answered with a Codex auto-fix loop and dedicated isolated cloud workspaces.
- Reaching stage five required a machine-readable 'world model' of all 25,000 repos so orchestrators and sub-agents could pull context and plan across multiple codebases; the resulting Builder Bot let anyone at the company, not just engineers, ship fixes from Slack.
- The talk ends unresolved rather than triumphant: layoffs followed the success, and Jones asks publicly whether enabling people to do the best work of their careers contributed to their dismissal.

## Notable Quotes

> "But our CEO was convinced that engineering wasn't using AI at all."
>
> — [0:42](https://www.youtube.com/watch?v=whue9_YquGA&t=42s) &middot; *The inciting tension of the whole talk, stated in one line.*

> "I had the numbers, both the metrics and the token bills. So, I knew that engineering was, in fact, using AI, but he was right. Features certainly weren't making it to our customers any faster."
>
> — [0:42](https://www.youtube.com/watch?v=whue9_YquGA&t=42s) &middot; *Names the adoption-vs-impact gap that motivates the entire program.*

> "I defined an agentic engineering org as one where engineers leverage AI agents as their primary means of producing engineering outcomes."
>
> — [2:15](https://www.youtube.com/watch?v=whue9_YquGA&t=135s) &middot; *The operating definition everything else is measured against.*

> "There's no playbook for any of this stuff, right? And I know because I went looking at your blogs hoping that you all had it all figured out. But, I only saw a bunch of posts saying how you all were making it up as you went along."
>
> — [2:15](https://www.youtube.com/watch?v=whue9_YquGA&t=135s) &middot; *Candid statement of how immature the field is, from someone at the frontier of it.*

> "stage five is that final boss where engineers are delegating complete tasks to agents and the agent is able to produce shippable results without the human necessarily needing to guide it"
>
> — [3:42](https://www.youtube.com/watch?v=whue9_YquGA&t=222s) &middot; *Defines the top of the maturity model that structures the talk.*

> "people were already feeling turned off by the top-down pressure from leadership to essentially AI or die"
>
> — [4:26](https://www.youtube.com/watch?v=whue9_YquGA&t=266s) &middot; *Names the cultural failure mode her strategy is designed to avoid.*

> "So, I realized that if my AI strategy depends on every individual leveling themselves up, I'm never going to see that broad impact."
>
> — [5:13](https://www.youtube.com/watch?v=whue9_YquGA&t=313s) &middot; *The strategic pivot from mass training to concentrated leverage.*

> "I needed engineers who were willing to dedicate at least 30% of their time to investing in AI enablement."
>
> — [5:59](https://www.youtube.com/watch?v=whue9_YquGA&t=359s) &middot; *A concrete, checkable resourcing number others can compare against.*

> "My theory here was if I can get engineers to embed AI directly into their repos, then not only would the agents perform better but the entire team would benefit, not just the 1%."
>
> — [6:40](https://www.youtube.com/watch?v=whue9_YquGA&t=400s) &middot; *States the mechanism by which champion work is supposed to scale.*

> "So instead of forcing a one-size-fits-all solution, each champion figured out what worked for their repo, and then teams with similar shapes and sizes naturally converged on the same tools and patterns."
>
> — [8:17](https://www.youtube.com/watch?v=whue9_YquGA&t=497s) &middot; *A clear tradeoff position on standardization versus local autonomy.*

> "So, the entire cycle from discussion, diagnosis, issue creation, alignment, and the fix took like 5 minutes all right there in Slack. Very cool party trick, by the way."
>
> — [11:27](https://www.youtube.com/watch?v=whue9_YquGA&t=687s) &middot; *The concrete demo of Slack-native delegation, with her own hedge attached.*

> "AI-authored code was up by 69%, reported time savings increased 37%, and automated PRs increased 21 times."
>
> — [12:11](https://www.youtube.com/watch?v=whue9_YquGA&t=731s) &middot; *The headline results after three months of the champions program.*

> "Engineers are now tripling, quadrupling the number of PRs that they're producing, but the PRs are stuck waiting for code reviews"
>
> — [12:56](https://www.youtube.com/watch?v=whue9_YquGA&t=776s) &middot; *Identifies review as the bottleneck that parallel agents immediately expose.*

> "Mostly because the AI code reviewers sucked so badly, and we were just pissing the engineers off by having them use them."
>
> — [13:35](https://www.youtube.com/watch?v=whue9_YquGA&t=815s) &middot; *Rare honesty about AI reviewers being net-negative until recently.*

> "we also created an auto-fix loop where if Codex identified issues, another agent will automatically fix those issues and commit them to the PR"
>
> — [13:35](https://www.youtube.com/watch?v=whue9_YquGA&t=815s) &middot; *A specific, reusable pattern for keeping bot PRs reviewable.*

> "So, we invested in dedicated cloud workspaces where each agent ran in its own isolated environment. And this allowed us to easily run them in parallel and from anywhere."
>
> — [14:16](https://www.youtube.com/watch?v=whue9_YquGA&t=856s) &middot; *The infrastructure prerequisite for multi-agent parallelism.*

> "So, we built a company world modeled based on the entirety of our 25,000 repo code base, right? And this was a machine-readable view of every single service and how they all connect."
>
> — [15:04](https://www.youtube.com/watch?v=whue9_YquGA&t=904s) &middot; *The context-layer investment that made cross-repo autonomy possible.*

> "Anyone at the company could act Build-A-Bot in Slack and have it fix a bug or implement a new feature. They didn't even need GitHub."
>
> — [16:00](https://www.youtube.com/watch?v=whue9_YquGA&t=960s) &middot; *Marks the point where software changes stopped requiring engineers at all.*

> "This felt like a dream. Until it became a nightmare. You know, of course, all layoffs are tough, but this one felt different."
>
> — [16:00](https://www.youtube.com/watch?v=whue9_YquGA&t=960s) &middot; *The pivot that separates this talk from every other adoption success story.*

> "Did enabling employees to do the most incredible work of their careers ultimately result in their dismissal?"
>
> — [16:49](https://www.youtube.com/watch?v=whue9_YquGA&t=1009s) &middot; *The unresolved ethical question the talk closes on.*

## Positions

- Widespread AI tool usage does not by itself produce faster delivery; impact requires integrating agents into how software is built and shipped. ([0:42](https://www.youtube.com/watch?v=whue9_YquGA&t=42s), confidence: stated)
- An org-wide AI strategy that depends on every individual leveling themselves up will never produce broad impact. ([5:13](https://www.youtube.com/watch?v=whue9_YquGA&t=313s), confidence: stated)
- The 1/9/90 participation rule maps almost perfectly onto how engineers adopt AI. ([4:26](https://www.youtube.com/watch?v=whue9_YquGA&t=266s), confidence: stated)
- Champion programs should be hand-picked strategically rather than opened to volunteers, and members need at least 30% time commitment. ([5:59](https://www.youtube.com/watch?v=whue9_YquGA&t=359s), confidence: stated)
- Embedding AI assets into repos is higher leverage than training individuals, because repos are the central reference point for everyone contributing code. ([6:40](https://www.youtube.com/watch?v=whue9_YquGA&t=400s), confidence: stated)
- Agent configuration should be customized per repo rather than mandated top-down; web, mobile, and monorepos need different approaches. ([8:17](https://www.youtube.com/watch?v=whue9_YquGA&t=497s), confidence: stated)
- Delegation adoption succeeds when it happens where requirements already arrive (Slack, Jira/Linear, GitHub issues), because it requires engineers to learn no new skill. ([12:11](https://www.youtube.com/watch?v=whue9_YquGA&t=731s), confidence: stated)
- As of mid-2025 models could write features but would not conform to team conventions, which is why engineers did not yet trust delegation. ([6:40](https://www.youtube.com/watch?v=whue9_YquGA&t=400s), confidence: stated)
- AI code reviewers were bad enough earlier that mandating them was counterproductive, but repo readiness plus better models made them viable. ([13:35](https://www.youtube.com/watch?v=whue9_YquGA&t=815s), confidence: stated)
- Code review throughput, not code generation, becomes the binding constraint once engineers run multiple agents in parallel, and it is not fully solved. ([12:56](https://www.youtube.com/watch?v=whue9_YquGA&t=776s), confidence: stated)
- Local developer machines cannot support real multi-agent parallelism; isolated cloud workspaces per agent are required. ([14:16](https://www.youtube.com/watch?v=whue9_YquGA&t=856s), confidence: stated)
- Autonomous engineering at scale requires a machine-readable model of the entire codebase and its service dependencies. ([15:04](https://www.youtube.com/watch?v=whue9_YquGA&t=904s), confidence: stated)
- Once stage four delegation infrastructure is in place, moving to multi-agent parallelism costs almost nothing additional. ([12:11](https://www.youtube.com/watch?v=whue9_YquGA&t=731s), confidence: stated)
- Building an autonomous engineering org may directly contribute to the layoffs of the people who built it, and the industry has not reckoned with where this leads. ([16:49](https://www.youtube.com/watch?v=whue9_YquGA&t=1009s), confidence: implied)

## Concepts

- [agent configuration files](../concepts/agent-configuration-files.md)
- [agent-readable codebases](../concepts/agent-readable-codebases.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [cognitive debt](../concepts/cognitive-debt.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [parallel agent execution](../concepts/parallel-agent-execution.md)
- [world models](../concepts/world-models.md)

