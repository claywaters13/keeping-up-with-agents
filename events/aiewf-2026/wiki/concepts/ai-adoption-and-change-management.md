---
title: "ai adoption and change management"
type: "concept"
slug: "ai-adoption-and-change-management"
tier: "supporting"
maturity: "consolidating"
talk_count: 13
speaker_count: 14
---

# ai adoption and change management

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **13** talk(s) by **14** speaker(s)

**Definition:** Getting an organization to actually work differently with AI — enablement, champions, process redesign, and the org shapes that result.

*Also referred to as: organizational change management, ai adoption maturity model, ai enablement programs, team-wide agent adoption, internal champions programs, process re-engineering around ai, agentic org design, ai-native company operating model*

## State of Practice

The field has stopped treating AI adoption as a tooling problem and started treating it as an organizational design problem: every speaker who ran a real rollout reported that seat licenses, token spend, and even measured usage failed to translate into faster delivery or customer value. The consensus diagnosis is that the constraint moved from code generation to two other places — deciding what is worth building, and redesigning the process the work flows through — with MIT-style figures (95% of pilots never reach production, ~87% show no measurable ROI) cited as evidence that AI dropped onto undocumented, broken processes does nothing. The leading practical answer is to stop trying to level up individuals one at a time and instead embed the capability into shared artifacts — agent config and skills committed into repos, requirements written as markdown user stories in the codebase, curated company knowledge behind an MCP server — so that the 90% who will never read a prompt-engineering blog benefit anyway. Rollout mechanics have concrete shape now: hand-picked champions at ≥30% time allocation, a standing percentage of IC time on harness work that produces no PRs, adoption surfaces where requirements already arrive (Slack, Jira/Linear, GitHub issues), and skeptic buy-in as the success metric rather than usage dashboards. The unsolved edges are ROI measurement, the review bottleneck created when PR volume triples, whether standardization or per-team customization wins, and — raised explicitly by one speaker whose program preceded layoffs — what the org shape is actually for.

## Consensus

### Tool access and usage mandates do not produce behavior change; adoption is a human problem requiring champions, accompaniment, and psychological safety.

Support: **4** talk(s)

> "the third most important thing is treat it like a human problem, guys. Like, this isn't It's not, you know, oh, it's this tool. Like, people will figure it out. Let's just mandate our way through life. Like, that's just not going to work."
>
> — [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [8:30](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=510s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)

### Code generation is no longer the bottleneck; deciding what to build and understanding the business process is, which is where adoption effort should be spent.

Support: **6** talk(s)

> "at a point where writing code is no longer the bottleneck, the real thing is to figure is figuring out what it is that you should be building."
>
> — [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s)

Supporting talks: [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)

### Embedding AI assets into shared artifacts (repo-level agent config, skill files, markdown requirements, curated knowledge) scales adoption far better than training individuals.

Support: **5** talk(s)

> "My theory here was if I can get engineers to embed AI directly into their repos, then not only would the agents perform better but the entire team would benefit, not just the 1%."
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [6:40](https://www.youtube.com/watch?v=whue9_YquGA&t=400s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)

### Usage metrics and token spend are not adoption success; the token-maxing era is over and outcome measurement replaced it.

Support: **4** talk(s)

> "I had the numbers, both the metrics and the token bills. So, I knew that engineering was, in fact, using AI, but he was right. Features certainly weren't making it to our customers any faster."
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [0:42](https://www.youtube.com/watch?v=whue9_YquGA&t=42s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)

### The target of adoption is the whole organization, not the engineering function; non-technical staff building their own automations is where the larger multiplier sits.

Support: **4** talk(s)

> "You can make engineers like 10x faster. That's fine. That's still valuable. But can you make an organization 10x faster, including every single person that might be technical or non-technical uh across the company?"
>
> — [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [11:20](https://www.youtube.com/watch?v=RVxym6mmIns&t=680s)

Supporting talks: [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

### Once agents multiply PR volume, human code review becomes the binding constraint, and the answer is automated review plus auto-fix/self-healing loops rather than more reviewers.

Support: **3** talk(s)

> "Engineers are now tripling, quadrupling the number of PRs that they're producing, but the PRs are stuck waiting for code reviews"
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [12:56](https://www.youtube.com/watch?v=whue9_YquGA&t=776s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)

## Disagreements

### Does AI adoption require redesigning the process itself, or only re-tooling the existing process?

| Position A | Position B |
|---|---|
| The software development lifecycle and enterprise workflows are largely unchanged by AI; what changes is the toolkit, and workflows should be preserved closely enough that operators still recognize them (replacing an 11-step workflow with a 1-step one damages adoption).<br>*[You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)* | The process is the thing that has to change: design-then-build inverts to build-then-design, planning and review stop being phases that bracket the work, and the unit of change becomes an editable spec document — AI layered on an unchanged process is exactly why pilots fail.<br>*[500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)* |

*Why it matters: If only the toolkit changes, enablement is training plus better artifacts and existing roles survive intact; if the process changes, the org has to fund process redesign, accept temporary throughput loss, and redraw role boundaries. Note that ai-tools-for-forward-deployed-engineering holds both sides: redesign the process, but keep its step structure legible to the people who operate it.*

### Should teams converge on one standardized agent setup, or let each repo and team customize their own?

| Position A | Position B |
|---|---|
| Find your best ICs, extract their practices, and force everyone onto a single shared setup; personal bespoke configurations are a liability and engineers must accept that their own setup is imperfect.<br>*[Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* | Refuse one-size-fits-all: each champion figures out what works for their repo (web, mobile, monorepo need different approaches) and convergence happens naturally between repos of similar shape; agency and ownership, not the tooling, was the actual enabler of behavior change.<br>*[Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)* |

*Why it matters: Standardization makes harness investment compound and keeps review burden even across a team, but a mandated shared setup is the same top-down pressure that all three speakers say turns engineers off — the choice determines whether enablement is a platform team's deliverable or a champion network's.*

### Who should own change management and broad rollout for an AI product — the vendor's own deployed engineers, or partners and self-service?

| Position A | Position B |
|---|---|
| Change management, product 101/201 workshops, and broad rollouts should be handed to system integrators and consulting partners; burning 10x engineers on training sessions is misuse of the function and they will quit.<br>*[Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)* | The vendor's deployed engineers must own the transformation end-to-end — embedding for months, redesigning departments, and guaranteeing the outcome — because a pure product motion cannot capture enterprise AI value.<br>*[AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)* |

*Why it matters: This decides headcount model and pricing: partner-led rollout keeps the vendor a software company with seat pricing, while vendor-owned transformation implies a services margin and makes outcome-based pricing defensible.*

### Is producing broad AI capability an organizational program or an individual responsibility?

| Position A | Position B |
|---|---|
| It is leadership's job, not an IC's; a strategy that depends on every individual leveling themselves up will never produce broad impact, and uneven adoption within a team actively harms the low-adoption engineers.<br>*[Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)* | The leverage is in how each person wires their own work — the 2X and 100X people use identical models — and the correct response to displacement fear is for individuals to multiply their own output.<br>*[Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* |

*Why it matters: It determines where budget goes: a standing percentage of IC time and a champion program with headcount, versus tooling access plus the expectation that motivated people will figure it out and the rest will lag.*

## Practical Guidance

**Do:**

- Hand-pick champions strategically rather than opening the program to volunteers, and require at least 30% of their time committed to AI enablement
- Budget a standing percentage of IC time to harness and codebase setup work that produces no immediate PRs, and treat it as never finished
- Put delegation where requirements already land — Slack, Jira/Linear, GitHub issues — so engineers need to learn no new skill to adopt it
- Track whether skeptics start editing and modifying the shared setup; that, not usage volume, is the signal the rollout is working
- Run the first enablement push on work unrelated to the existing product so risk is removed and the team can focus on learning
- Cap skill.md files at ~100 lines with detail deferred to sibling files, and keep first-prompt baseline context at 20-25K tokens (40-50K means progressive disclosure failed)
- Convert every agent task that succeeds into a reusable skill file instead of leaving it as one-off work
- Specify process redesign step by step — e.g. four of eight steps fully autonomous, three human-in-the-loop, one human-only — rather than replacing the workflow wholesale
- Commit requirements as markdown user stories in the repo (persona/need/why), since models were trained on that structure
- Pair AI code review with an auto-fix loop that commits the fixes back to the PR, and give each agent an isolated cloud workspace so parallelism is real
- Replace 'features shipped last quarter' as a KPI with 'features shipped that are used more than twice'
- Build on top of the customer's existing systems of record (NetSuite, SAP, Salesforce) rather than requiring migration off them

**Avoid:**

- Mandating agent usage company-wide or setting token consumption as the KPI — fear and human emotion are the actual blockers and budgets eventually arrive
- Letting adoption go uneven inside a team: the 10-PR-a-day engineers offload review burden onto the 1-2-PR engineers, who become more hostile to agents as a result
- Slapping AI on top of broken, undocumented processes and expecting a pilot to reach production
- Rolling out AI code reviewers before repos are ready — bad reviewers early on just anger engineers and poison the later rollout
- Assuming a strategy where each individual levels themselves up will reach beyond the top 1% of adopters
- Treating agent babysitting as normal; it is a signal the codebase and harness setup is wrong
- Spending elite deployed engineers on product 101/201 training sessions and bug write-ups — they will get bored and leave
- Selling or assigning a fixed number of engineers for a fixed period with no defined problem; keep scope problem-anchored and directional
- Running a customer engagement with no named counterpart working team on the customer side
- Changing an operator's workflow so drastically that they no longer recognize how to run the system
- Letting a shared knowledge layer accumulate without provenance, contradiction checks, and active pruning — it becomes confidently wrong

## Notable Outliers

- Building an autonomous engineering org may directly contribute to the layoffs of the very people who built it, and the industry has not reckoned with where this leads. ([Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [16:49](https://www.youtube.com/watch?v=whue9_YquGA&t=1009s))
- Fear of AI-driven job loss is a failure of imagination; the correct response is for individuals to multiply their own output. ([Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [17:56](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=1076s))
- An engineer's impact from enabling non-engineer teammates can exceed the impact of doing more engineering themselves, so the role shifts from builder to enabler and teacher. ([500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [8:01](https://www.youtube.com/watch?v=UcYoMg-8-L8&t=481s))
- Point solutions inside one function return only 5-10% ROI while department-wide transformation returns 25-75%, and non-technical operators in finance, sales, and procurement will not get the same ROI from general AI tooling that software engineers do. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [11:07](https://www.youtube.com/watch?v=l0FLhNqBOic&t=667s))
- Of 21 agent ideas at an internal hackathon, 17 were abandoned for lack of business value or data access; the surviving 4 had large impact. ([You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s))
- Slop is inevitable, so the correct organizational investment is detection and self-healing pipelines rather than prevention. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [7:58](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=478s))
- Long agent run times are a feature, not a problem — the fear they provoke in engineers disappears once people see the output value. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [12:20](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=740s))

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
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md)
- [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Balázs Horváth](../speakers/balazs-horvath.md)
- [Cat Wu](../speakers/cat-wu.md)
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

