---
title: "ai adoption and change management"
type: "concept"
slug: "ai-adoption-and-change-management"
tier: "supporting"
maturity: "consolidating"
talk_count: 14
speaker_count: 15
---

# ai adoption and change management

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **14** talk(s) by **15** speaker(s)

**Definition:** Getting an organization to actually work differently with AI — enablement, champions, process redesign, and the org shapes that result.

*Also referred to as: organizational change management, ai adoption maturity model, ai enablement programs, team-wide agent adoption, internal champions programs, process re-engineering around ai, agentic org design, ai-native company operating model*

## State of Practice

By this conference the field had stopped treating AI adoption as a tooling procurement problem and started treating it as an organizational redesign problem. Multiple speakers reported the same failure signature: token bills and usage metrics go up, features do not ship faster, and 95% of enterprise pilots never reach production because AI was layered onto undocumented, unredesigned processes. The consensus intervention is to stop leveling up individuals and instead encode practice into shared, machine-readable artifacts that live in the repo — skill files, per-repo agent configs, committed markdown requirements, and MCP-exposed institutional knowledge — so the whole team inherits the improvement rather than the top 1%. Rollout mechanics that speakers converged on: hand-picked champions with a real time allocation (30%+), a standing tax on IC time for harness work that produces no PRs, low-risk verified starting tasks, and skeptic buy-in as the success metric — not mandates, which several speakers said actively backfire by making low-adoption engineers absorb the review burden of high-adoption ones. The second-order consequence is now the live operational problem: once generation is cheap, human code review becomes the binding constraint, and roles shift from building to enabling, reviewing, specifying, and deciding what is worth building at all.

## Consensus

### Model capability is no longer the binding constraint on organizational value; the constraint is the surrounding process, harness, and decision about what to build.

Support: **6** talk(s)

> "The 2X people and the 100X people are using the exact same Claude. Same weights, same context window, same API. So, the leverage is not in the weights. It's in how you wire the work."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [Field Guide to Fable](../talks/field-guide-to-fable.md)

### High AI tool usage does not by itself produce faster delivery; usage metrics and token spend are not evidence of impact.

Support: **4** talk(s)

> "I had the numbers, both the metrics and the token bills. So, I knew that engineering was, in fact, using AI, but he was right. Features certainly weren't making it to our customers any faster."
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [0:42](https://www.youtube.com/watch?v=whue9_YquGA&t=42s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)

### Top-down mandates fail; adoption is a human behavior-change problem requiring champions, agency, and skeptic buy-in.

Support: **3** talk(s)

> "the third most important thing is treat it like a human problem, guys. Like, this isn't It's not, you know, oh, it's this tool. Like, people will figure it out. Let's just mandate our way through life. Like, that's just not going to work."
>
> — [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [8:30](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=510s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)

### Enablement should be embedded into shared repo-level artifacts (skills, conventions, committed markdown) rather than delivered as individual training, because artifacts scale to the whole team.

Support: **5** talk(s)

> "My theory here was if I can get engineers to embed AI directly into their repos, then not only would the agents perform better but the entire team would benefit, not just the 1%."
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [6:40](https://www.youtube.com/watch?v=whue9_YquGA&t=400s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)

### Once agents multiply code output, human code review becomes the new organizational bottleneck.

Support: **4** talk(s)

> "Engineers are now tripling, quadrupling the number of PRs that they're producing, but the PRs are stuck waiting for code reviews"
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [12:56](https://www.youtube.com/watch?v=whue9_YquGA&t=776s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)

### Engineering roles shift away from writing implementation toward enabling others, specifying, reviewing, and deciding what to build; product judgment becomes the scarce skill.

Support: **6** talk(s)

> "if you're an engineer, the impact that you have when you enable others may be far greater than the impact of doing more engineering yourself"
>
> — [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [8:01](https://www.youtube.com/watch?v=UcYoMg-8-L8&t=481s)

Supporting talks: [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)

## Disagreements

### Should an organization standardize on one shared agent setup, or let configuration vary by repo, team, and individual preference?

| Position A | Position B |
|---|---|
| Converge on a single standardized setup derived from the team's best ICs; engineers must give up bespoke personal configurations because the highest-leverage codebase changes require team buy-in and uneven setups create review-burden asymmetry.<br>*[Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* | Deliberately avoid one-size-fits-all: let each champion tune agent configuration to their repo's shape (web, mobile, monorepo) and support multiple competing coding tools because engineer preference shifts year to year — meet engineers where they are.<br>*[Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)* |

*Why it matters: Standardization makes harness investment compound and keeps review load even, but a mandated setup reproduces exactly the top-down pressure all three speakers say kills adoption. The choice determines whether platform teams ship one golden config or a toolkit of per-repo patterns.*

### Can humans be removed from the code review loop, or must a named human stay accountable for every merge?

| Position A | Position B |
|---|---|
| Yes — invest in evals, classifiers, and self-healing auto-fix pipelines until automated review catches the issues, then take humans out for non-core changes; slop is inevitable so build detection rather than gatekeeping, and residual prompt-injection/exfiltration risk is already below that of an average human reviewer.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* | Not yet — AI reviewers are not trustworthy enough to rely on 100%; keep a human accountable, cap PRs at 500 lines so review is actually possible, and treat mandated AI review before the tooling is ready as counterproductive.<br>*[How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)* |

*Why it matters: This is the single decision that determines whether the review bottleneck is solved or merely relocated. If humans must stay in the loop, headcount and PR-size discipline cap throughput; if not, the org's constraint moves to eval quality and infrastructure investment.*

### Should process redesign preserve the shape of the existing workflow, or is deep restructuring the point?

| Position A | Position B |
|---|---|
| Preserve enough of the original structure to protect adoption — collapsing an 11-step workflow into one step makes operators unable to operate the system and adoption rates suffer; the SDLC itself is largely unchanged, only the toolkit changes.<br>*[AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)* | Restructure fundamentally — abandon 3-6 month planning horizons, treat rewrites as good, converge creation and collaboration into one surface, and rebuild the org around delegation and multi-agent parallelism, because orgs designed for a single human brain are the wrong shape.<br>*[How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)* |

*Why it matters: It sets the unit of change: incremental step-by-step automation with human-in-the-loop handoffs, versus wholesale re-architecture of planning, review, and delivery. The incrementalists are optimizing for adoption by non-technical operators; the restructurers are optimizing for engineering throughput and accept the disruption.*

### Should the vendor own enablement and change management inside the customer organization, or push it to partners and self-service?

| Position A | Position B |
|---|---|
| Own it — department-wide process transformation is the product (5-10% ROI for point solutions vs 25-75% for department-wide), a pure product company cannot capture enterprise AI value, and multi-month embeds are how outcomes get guaranteed.<br>*[AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md)* | Do not — change management and broad product rollouts belong with system integrators and consulting partners; running 101/201 workshops is a bad use of 10X engineers, and mature customers should get self-service documentation instead of an FDE engagement.<br>*[Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)* |

*Why it matters: This determines whether an AI company staffs a services organization that scales linearly with customers or a product organization with a partner channel, and whether outcome-based pricing is underwritable at all.*

## Practical Guidance

**Do:**

- Hand-pick champions strategically rather than opening enablement to volunteers, and require at least 30% of their time committed to AI enablement
- Budget a standing percentage of IC time for harness and setup work that produces no immediate PRs, and treat it as never finished
- Cap skill.md files at roughly 100 lines and treat a skill as a folder, deferring detail to linked files
- Keep first-prompt baseline context around 20-25K tokens; treat 40-50K as evidence that progressive disclosure has failed
- Start adoption with lowest-risk, easily verified tasks — unit tests and documentation — before expanding scope
- Cap PRs at 500 lines because meaningful human review of thousand-line PRs is impossible
- Put delegation entry points where requirements already arrive (Slack, Jira/Linear, GitHub issues) so engineers learn no new skill
- Use skeptics editing and modifying the shared setup as the indicator that a rollout is actually working
- Convert every agent task that succeeds into a reusable skill file rather than leaving it as one-off work
- Give agents isolated cloud workspaces per agent instead of relying on local developer machines for parallelism
- Replace 'features shipped last quarter' as a KPI with 'features shipped that are used more than twice'
- Plan one year directionally and two-to-four weeks concretely; skip the three-to-six-month horizon entirely
- Run each LLM integration test many times against a sustained pass-rate bar such as 90%, rather than passing once
- Explicitly exempt experimental and prototype code from the codebase's rigorous standards
- Remove risk from the first pilot project — build something unrelated to existing products so the team can focus on learning
- Commit requirements and user stories as markdown in the repository so agents can use them as context

**Avoid:**

- Mandating agent usage company-wide or 'token maxing' — fear and human emotion are the real blockers, and budgets eventually get bolted on
- Letting adoption go uneven within a team, which leaves low-adoption engineers absorbing the review burden for high-adoption engineers' PRs and turns them hostile
- Applying AI on top of broken, undocumented processes instead of redesigning them first
- Treating usage metrics and token bills as evidence of delivery velocity
- Rubber-stamp approvals of AI-authored PRs, which produce false confidence
- Babysitting agents — it is a defect signal that the codebase and harness setup is wrong, not normal practice
- Expressing guardrails as prompts to the agent, since a third party can prompt-inject past them; guardrails must be deterministic configuration outside the agent
- Building your own AI Slackbot — the prompt-injection attack surface is too large
- Requiring enterprise customers to migrate off their systems of record (NetSuite, SAP, Salesforce) as a condition of adopting AI tooling
- Selling a fixed allocation of forward-deployed engineers for a fixed period with no defined problem
- Running product 101/201 training workshops as the forward-deployed engineering function
- Letting automations produce unbounded output — cap them (e.g. a single PR) and allow them to produce nothing, or they become a denial-of-service on their owner
- Depending on an AI strategy where every individual must level themselves up
- Collapsing a familiar 11-step operator workflow into a single step, which tanks adoption even when it is more efficient

## Notable Outliers

- Building a successful autonomous engineering org may directly contribute to the layoffs of the people who built it, and the industry has not reckoned with where that leads. ([Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [16:49](https://www.youtube.com/watch?v=whue9_YquGA&t=1009s))
- Long agent run times are a feature, not a defect — under the reasoning paradigm the longer the agent thinks, the better the output, and hour-long skill runs scared people until they saw the value. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [12:20](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=740s))
- 17 of 21 agent ideas from an internal hackathon were abandoned for lack of business value or data access; the surviving 4 had large impact. ([You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s))
- Post-trained open-source models outperform frontier models at writing normalized enterprise process flows, because frontier models have no concept of which details the client actually cares about. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [16:40](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1000s))
- The memory/company-brain layer should be open source infrastructure rather than a proprietary profit center, analogous to Linux. ([Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [17:22](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=1042s))
- A non-engineer designer shipped to production in a large legacy system in 2.5 weeks, and attributed the shift more to owning the whole process than to the AI tooling. ([500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [12:12](https://www.youtube.com/watch?v=UcYoMg-8-L8&t=732s))

## All Talks

- [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)
- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)
- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md)
- [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Balázs Horváth](../speakers/balazs-horvath.md)
- [Cat Wu](../speakers/cat-wu.md)
- [Dan Feng](../speakers/dan-feng.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Idan Gazit](../speakers/idan-gazit.md)
- [Jia Wu](../speakers/jia-wu.md)
- [Natalie Meurer](../speakers/natalie-meurer.md)
- [Paul Klein IV](../speakers/paul-klein-iv.md)
- [Pauline Brunet](../speakers/pauline-brunet.md)
- [Sanja Grbic](../speakers/sanja-grbic.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)

