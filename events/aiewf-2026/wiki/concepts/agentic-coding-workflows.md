---
title: "agentic coding workflows"
type: "concept"
slug: "agentic-coding-workflows"
tier: "core"
maturity: "consolidating"
talk_count: 26
speaker_count: 28
---

# agentic coding workflows

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **26** talk(s) by **28** speaker(s)

**Definition:** How engineers actually work with coding agents day to day — delegation patterns, review rhythm, parallelism, and the shape of the resulting dev loop.

*Also referred to as: agentic coding, coding agents, agentic coding loops, coding agent workflows, agentic code generation, vibe coding, multi-repo agentic workflows*

## State of Practice

The conference's center of gravity moved off the model and onto the repository and the harness around it: speakers converged on "agent readiness" — dense deterministic validation loops, in-code documentation, clean PR/tagging hygiene, hand-written golden patterns — as the variable that actually determines whether frontier agents produce shippable work. The day-to-day loop has inverted: implementation is delegated, and the human's work is upstream (deciding what matters, writing the map) and downstream (review), with review throughput now the explicit binding constraint once engineers run three or four agents at once. Context discipline has hardened into numbers — ~100-line skill.md files that index into folders, 20–25K tokens of baseline first-prompt context, 80% of the Claude Code system prompt deleted, negative constraints ("do not do X") replaced with context. Durable files beat chat sessions as the unit of state: markdown in git for agent memory and pattern catalogs, decision docs that make agents effectively stateless, session state portable across agent products. Adoption is understood as an organizational problem — mandates and token-maxxing failed, champions with 30% time and repo-embedded assets worked — and money now visibly constrains the loop, with per-repo benchmarking and open-weight models used to escape single-vendor cost curves. The unresolved fights are about how far to push autonomy: whether humans stay in every review, and whether parallelism should be capped at what humans can read.

## Consensus

### Agent performance is gated by how the codebase and repo are set up — documentation, conventions, and machine-readable context embedded in the repo — not by model capability.

Support: **7** talk(s)

> "Even if you have really good agents, they're not going to know how to solve these problems if they don't have documentation or skills"
>
> — [Content Is Code](../talks/content-is-code.md), [7:22](https://www.youtube.com/watch?v=yv6xovSsB1U&t=442s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Content Is Code](../talks/content-is-code.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Field Guide to Fable](../talks/field-guide-to-fable.md)

### Autonomy is bounded by verification: long-running agents only produce trustworthy output where deterministic checks can validate their work, so verification must be built into the generation loop rather than bolted on afterward.

Support: **8** talk(s)

> "the quality of the output of these very long-running harnesses of advanced agents is directly proportional to the degree to which you can validate their work"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [12:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=777s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [Evaling Video Slop](../talks/evaling-video-slop.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)

### Code review, not code generation, is now the binding constraint on team throughput once engineers run agents in parallel.

Support: **5** talk(s)

> "Engineers are now tripling, quadrupling the number of PRs that they're producing, but the PRs are stuck waiting for code reviews"
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [12:56](https://www.youtube.com/watch?v=whue9_YquGA&t=776s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)

### Agent rollout is a human behavior problem: top-down mandates fail, and adoption succeeds through champions, repo-embedded assets, and winning over skeptics.

Support: **4** talk(s)

> "changing processes or tools in large organizations requires shifting the human behavior behind them"
>
> — [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [17:12](https://www.youtube.com/watch?v=UcYoMg-8-L8&t=1032s)

Supporting talks: [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)

### Less prompt/context is better with frontier models: use progressive disclosure and a thin index instead of front-loading instructions, examples, and negative constraints.

Support: **5** talk(s)

> "I think like 20, 25K tokens get taken anyway, but like how much more is getting added? If you're coming to like 40K, 50K, like something's wrong. That's not really progressive disclosure."
>
> — [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [15:57](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=957s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)

### State belongs in durable version-controlled files (markdown docs, feedback files, pattern catalogs), not in ephemeral chat sessions — which makes agents effectively stateless and restartable.

Support: **6** talk(s)

> "What you want is to separate the the agent as the action and the doc as the state."
>
> — [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [13:21](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=801s)

Supporting talks: [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)

## Disagreements

### Should a human review every agent-authored change, or should humans be removed from the review loop for most changes?

| Position A | Position B |
|---|---|
| A human must approve every agent-generated change; agents open code reviews but never merge or push to production themselves, and the human remains accountable for what ships.<br>*[Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)* | The goal is a world where humans are not in the loop for non-core changes; with enough eval and infrastructure investment, agent review already catches 100% of issues in those categories and residual prompt-injection/exfiltration risk is lower than an average human reviewer's.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)* |

*Why it matters: If human sign-off is permanent, review capacity permanently caps team throughput and every parallelism investment eventually hits that wall; if it is removable, the investment shifts entirely into evals, classifiers, and auto-fix loops.*

### Should agent parallelism be maximized, or deliberately capped at what humans can actually review?

| Position A | Position B |
|---|---|
| Cap concurrency: a loop should never open a new PR while the previous one is unreviewed, and add friction where stakes are high — otherwise you generate 40,000-line PRs nobody reads and low-information accept/reject data.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* | Scale out: isolated cloud workspaces per agent, tripled or quadrupled PR counts, ~99.9% agent-generated PRs, and Slack-triggered agents for non-technical staff are the point of the exercise.<br>*[Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* |

*Why it matters: This determines whether you spend the next quarter buying agent-runner infrastructure or building review-side tooling and alignment artifacts; the two roadmaps barely overlap.*

### Do frontier models' self-orchestration abilities make custom orchestration harnesses unnecessary?

| Position A | Position B |
|---|---|
| The harness is the durable value layer: you must build (not buy) a meta-harness, control loops, cross-repo graphs, and monitoring, because everyone has the same models and the model alone is not the differentiator.<br>*[A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* | The newest models spawn sub-agents, split work, and verify it if you simply ask — no custom tooling, custom system, or fancy software factory required; the correct response to better models is more ambitious projects, not more scaffolding.<br>*[Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* |

*Why it matters: Harness engineering is a standing tax on IC time that produces no immediate PRs; if model self-orchestration keeps improving, that investment is written off, and if it doesn't, teams without it stall at the babysitting stage.*

### What is the right upfront artifact for a delegated task — a written specification, or an existing implementation to imitate?

| Position A | Position B |
|---|---|
| Write requirements and design documents in prose before any code, hand-edit them, and derive property-based tests from them; more capable models increase rather than decrease the need for upfront specification.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [Field Guide to Fable](../talks/field-guide-to-fable.md)* | Prose specs are the weak form — hand-build golden patterns or pass an existing implementation or HTML mockup as the reference, because coding agents are pattern replicators; and product-level spec-driven development is too far from engineering reality to be the decision layer at all.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Field Guide to Fable](../talks/field-guide-to-fable.md)* |

*Why it matters: It decides where scarce human time goes — into writing documents, or into hand-crafting one exemplary implementation — and whether the spec or the codebase is treated as the source of truth.*

### In the agent era, is bad code cheap enough to tolerate, or more expensive than ever?

| Position A | Position B |
|---|---|
| Bad code is more expensive than at any point in the past: agents must read the codebase to operate on it, clean code measurably reduces tokens and reasoning, and 3-5x velocity gains dissipate within three months without quality control.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)* | Code is increasingly disposable — rewrites are now good given a strong test suite, deleting and resetting is underused, and slop is inevitable so invest in detection and self-healing rather than prevention.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* |

*Why it matters: It sets whether quality gates run before merge as blocking constraints or after merge as cleanup loops, and whether tech-debt remediation is a first-class agent workload or an obsolete concern.*

## Practical Guidance

**Do:**

- Cap skill.md at ~100 lines and treat a skill as a folder — make the loaded file a thin index that points to other files, and keep first-prompt baseline context in the 20–25K token range.
- Store agent memory and pattern catalogs as plain markdown in a central Git repo rather than a vector database or vector search.
- Run agent loops on your existing CI (GitHub Actions, GitLab, CircleCI), which already has access to your code and secrets, instead of standing up a dedicated cluster.
- Use out-of-band sensors like AST-grep for loop measurement rather than lint or TypeScript config, which coding agents disable with inline comments.
- Give each item in a batch migration its own context window and separate implementation phase — it is both cheaper and more reliable than batching.
- Verify generated code with a different model than the one that generated it, since every model has its own biases.
- Gate performance or optimization PRs behind an automated canary comparing CPU, latency, and error rate before a human sees them — the profiler gives an estimate, the canary gives ground truth.
- Benchmark models and harnesses on your own repository; SWE-bench is all Python and will not predict results on a Ruby on Rails or other stack.
- Run agents in isolated cloud sandboxes with least-privilege credentials so they cannot reach laptop tokens, production credentials, or exfiltrate source.
- Hand-write golden patterns or idiomatic examples in the repo before setting an agent loose, since coding agents are pattern replicators.
- Replace hard negative constraints ('do not do X') in system prompts with context, and remove in-prompt examples that constrain a more imaginative frontier model.
- Hand-edit generated requirements and design documents with your own expertise before implementation begins.
- Use a separate agent with fresh context to review fixes, since the fix-generating agent is biased toward its own diagnosis and eager to ship PRs.
- Bootstrap a performance/quality pattern catalog from the reactive post-production path first, then shift it left into review-time and authoring-time.
- Deliver delegation where requirements already arrive — Slack, Jira/Linear, GitHub issues — so engineers need to learn no new skill.
- Budget a standing percentage of IC time for harness and codebase setup work that produces no immediate PRs.

**Avoid:**

- Babysitting an agent — treat it as a defect signal that the codebase or harness is wrong, not as normal practice.
- Mandating agent usage top-down or making token consumption the KPI; both provoke backlash and burn budget without delivery outcomes.
- Blind Ralph loops — a prompt in a bash loop with no measurable property, no incremental application, and no feedback on change quality.
- Letting agents use developer laptop credentials or relying on YOLO-mode auto-approval and ad-hoc sandbox config to keep them safe.
- Presenting review as one giant diff or as per-file yes/no prompts — both reduce the developer to a rubber stamp and produce low-information accept/reject labels.
- Overstuffing agents.md or steering files; there is a Goldilocks amount of context and too much is actively harmful.
- Sending an agent to do a job deterministic code can do.
- Treating passing tests or functional correctness as sufficient verification — state-of-the-art models pass functional checks while emitting high-complexity, buggy, insecure code.
- Allowing uneven adoption within a team, where low-adoption engineers inherit the review burden for high-adoption engineers' PRs and grow hostile to agents.
- Logging a human's yes/no decision without capturing the manual edit that followed — that records a false signal and pollutes your dataset.
- Holding experimental or prototype code to the same rigorous standards as production code instead of explicitly exempting it.
- Building a demo deployment so far ahead of the org's current practice that it gets dismissed as a theme park rather than copied.
- Building your own AI Slackbot — the prompt-injection attack surface is too large.

## Notable Outliers

- One anti-pattern — repeated Spectator counter object creation in a hot path — was found by cross-repo search in seven Netflix services, worth 0.5–4.6% of CPU cycles per service. ([AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [13:48](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=828s))
- An auto-research agent set seven leaderboard records in 22 days versus the best human's three, using at most 4% of total competition compute — and nearly all of its winning ideas were traced back to human papers and participants. ([How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [4:30](https://www.youtube.com/watch?v=iCj_ATyThvc&t=270s))
- 3,300 Claude Code runs cost $10,000/day in tokens while Codex ran 4x as many sessions for less total cost; Anthropic agents got consistently better but not faster on their Rails codebase. ([Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [16:20](https://www.youtube.com/watch?v=OL7kfezynJM&t=980s))
- The 3-5x velocity boost from coding agents dissipates within three months absent deliberate quality controls, and benchmark task-length claims measured at 50% success rate drop from ~18 hours to ~3.5 hours at 80% accuracy. ([In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [6:14](https://www.youtube.com/watch?v=VrpEyglYgeU&t=374s))
- Terminals are not good interfaces and natural language has no place in one — developers use them out of familiarity and professional identity, a skeuomorphic phase the field has not exited. ([Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [6:28](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=388s))
- Writing plans that never get implemented is a positive signal, because it means ideas are being explored and prioritized rather than built by default — a shift from code velocity to idea velocity. ([Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [14:08](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=848s))
- Building an autonomous engineering org may directly contribute to the layoffs of the people who built it, and the industry has not reckoned with where this leads. ([Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [16:49](https://www.youtube.com/watch?v=whue9_YquGA&t=1009s))

## All Talks

- [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)
- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)
- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)
- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Content Is Code](../talks/content-is-code.md)
- [Evaling Video Slop](../talks/evaling-video-slop.md)
- [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md)
- [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)
- [The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)
- [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Arjun Singh](../speakers/arjun-singh.md)
- [Benjamin Guo](../speakers/benjamin-guo.md)
- [Bennet Fenner](../speakers/bennet-fenner.md)
- [Cat Wu](../speakers/cat-wu.md)
- [Dominik Tornow](../speakers/dominik-tornow.md)
- [Eno Reyes](../speakers/eno-reyes.md)
- [Erik Hanchett](../speakers/erik-hanchett.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [James Russo](../speakers/james-russo.md)
- [Jia Wu](../speakers/jia-wu.md)
- [Kenton Varda](../speakers/kenton-varda.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [Maor Bril](../speakers/maor-bril.md)
- [Matt Dailey](../speakers/matt-dailey.md)
- [Natalie Meurer](../speakers/natalie-meurer.md)
- [Nicholas Arcolano](../speakers/nicholas-arcolano.md)
- [Rajat Shah](../speakers/rajat-shah.md)
- [Rob Cheung](../speakers/rob-cheung.md)
- [Roberto Stagi](../speakers/roberto-stagi.md)
- [Sanja Grbic](../speakers/sanja-grbic.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Tariq Shaukat](../speakers/tariq-shaukat.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Victor Savkin](../speakers/victor-savkin.md)
- [Zubin Aysola](../speakers/zubin-aysola.md)

