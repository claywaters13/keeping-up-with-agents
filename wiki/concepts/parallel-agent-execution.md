---
title: "parallel agent execution"
type: "concept"
slug: "parallel-agent-execution"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 10
---

# parallel agent execution

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **10** speaker(s)

**Definition:** Running many agents or branches concurrently and merging their results, including workspace isolation and fan-out/fan-in patterns.

*Also referred to as: parallel agent orchestration, multi-agent parallelism, git worktree parallelization, multi-agent fan-out, agentic map reduce, parallel sub-agent orchestration, git worktree isolation, agent pipelines*

## State of Practice

Parallelism is now treated as the primary lever on agent throughput, and the enabling primitive is uncontroversial: one isolated workspace per agent — a git worktree locally, a sandboxed cloud workspace remotely, or a per-rollout sandbox in eval harnesses. Reported scale ranges from ~50 concurrent worktrees on a 48 GB laptop to fire-and-forget batches of 10,000 rollouts on hosted infrastructure, with map/reduce shapes emerging where a cheap fast model handles the wide fan-out and a stronger model handles aggregation. The consistently reported consequence is that fan-out relocates the bottleneck rather than removing it: PR volume triples or quadruples and stalls in review, so teams are stacking AI reviewers, auto-fix loops, and separate 'manager' or arbiter agents with different context from the workers to do fan-in. The unresolved fights are about limits — whether laptops are a legitimate host at all (worktree density versus supply-chain and secrets exposure), whether more concurrent agents actually buys more capacity given that human review bandwidth does not parallelize, and how much of the merge verdict can be delegated to another agent before accountability evaporates. Correctness discipline is thinner than the throughput discipline: only a couple of talks specify what fan-in actually requires (one ordered commit path per mutable state boundary, explicit numeric break conditions, deterministic rather than model-based verification).

## Consensus

### Once fan-out is cheap, review and merge become the binding constraint — parallelism moves the bottleneck downstream rather than eliminating it.

Support: **5** talk(s)

> "Engineers are now tripling, quadrupling the number of PRs that they're producing, but the PRs are stuck waiting for code reviews"
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [12:56](https://www.youtube.com/watch?v=whue9_YquGA&t=776s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### Per-agent workspace isolation (git worktree, dedicated cloud workspace, or per-rollout sandbox) is the concrete enabler of parallelism, not a nice-to-have.

Support: **5** talk(s)

> "So, we invested in dedicated cloud workspaces where each agent ran in its own isolated environment. And this allowed us to easily run them in parallel and from anywhere."
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [14:16](https://www.youtube.com/watch?v=whue9_YquGA&t=856s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md)

### The fan-in step should be performed by a separate agent holding different context from the workers, because a worker judging its own output is biased toward approving it.

Support: **3** talk(s)

> "that's kind of the benefit you get, where the manager has a different context um than the workers"
>
> — [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [10:07](https://www.youtube.com/watch?v=9arM9b7JgOo&t=607s)

Supporting talks: [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [Everything Is a Rollout](../talks/everything-is-a-rollout.md)

### However many agents run in parallel, a named human must remain answerable for what merges; responsibility does not fan out with execution.

Support: **5** talk(s)

> "the only people who have liability are people that can have consequences, right? And that always has to be grounded in it being a human."
>
> — [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [50:15](https://www.youtube.com/watch?v=c35YoMdnI78&t=3015s)

Supporting talks: [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)

### Parallel agent output raises individual throughput without raising team-level impact unless a coordination or alignment layer is added.

Support: **3** talk(s)

> "Um it affects individuals or teams. Um and the result is output without impact."
>
> — [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [4:00](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=240s)

Supporting talks: [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)

## Disagreements

### Should parallel agents run on the developer's local machine or in isolated remote/cloud workspaces?

| Position A | Position B |
|---|---|
| Local is sufficient and preferred: git worktrees on a laptop are the key parallelization mechanism, and a 48 GB MacBook sustains roughly 50 active worktrees with the developer acting as orchestrator; a Docker-style sandbox is unnecessary for personal use.<br>*[Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* | Local machines cannot support real multi-agent parallelism and should not be used at all — each agent needs its own isolated cloud workspace, both for capacity and because running agents on a laptop exposes you to pre-existing NPM supply-chain and secrets-on-disk risk.<br>*[Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md)* |

*Why it matters: It determines whether parallel agent execution is an individual practice you can adopt this afternoon or an infrastructure program requiring provisioned sandboxes, credential brokering, and a per-agent environment budget. It also sets the realistic concurrency ceiling: tens of agents versus thousands of rollouts.*

### Does running more agents concurrently actually increase a team's effective capacity?

| Position A | Position B |
|---|---|
| Yes — parallelization is the main lever for tightening the loop, and the human should orchestrate rather than execute: don't hand-queue tasks, fire and forget large batches, and expect near-zero marginal cost to add parallelism once delegation infrastructure exists.<br>*[Everything Is a Rollout](../talks/everything-is-a-rollout.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)* | No — human cognitive bandwidth does not parallelize, and each additional loop adds routing, merging, and verification decisions that land on the same person; stacking loops and buying quality with tokens is also economically unsustainable, so target 2–3x rather than 100x.<br>*["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* |

*Why it matters: If capacity scales with agent count, the right investment is more concurrent workspaces and token budget; if it saturates at human verification bandwidth, the investment should go into making review cheaper and into deciding what not to build. The two paths produce opposite roadmaps and opposite token bills.*

### Can the merge-time verification of parallel agent output be delegated to another agent?

| Position A | Position B |
|---|---|
| Yes — AI reviewers plus auto-fix loops now beat human reviewers at finding real issues (worth roughly $5 per PR), and a third arbitration agent reading the workers' outputs is preferable to a plain metric or if-condition, which reproduces rule-based false positives.<br>*[Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)* | No — non-deterministic verification stacked on agent output makes correctness worse and verification should be pushed toward static, deterministic checks; the only way to stop loops from compounding slop is to read the output yourself, and in regulated domains agent-to-agent review leaves nobody accountable in production.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)* |

*Why it matters: This is the single decision that sets the sustainable fan-out width: if agents can close the verification loop, parallelism scales with compute; if a human must read every merge, the whole fan-out is capped by one person's reading speed regardless of how many workspaces you provision.*

## Practical Guidance

**Do:**

- Give every concurrent agent its own git worktree or isolated cloud workspace; the reported local ceiling is ~50 active worktrees on 48 GB of RAM.
- Split fan-out by model tier: run the wide map step on a cheap fast model (e.g. cursor CLI) and the reduce/aggregation step on a strong model where accuracy matters.
- Have a separate manager or arbiter agent — with spec/goal/history context rather than implementation context — render the verdict on worker PRs, since the authoring agent is biased toward 'it works'.
- Restrict concurrency only at the commit point: one ordered commit path per mutable state boundary, while leaving parallel reads, sub-agent fan-out, and concurrent sessions unrestricted.
- Give every agent loop an explicit numeric break condition, and make sure every external boundary resolves to success, failure, timeout, cancel, or max attempts — silence is not a terminal state.
- Put an AI review plus auto-fix loop in front of human review so the merge queue keeps moving when PR volume triples; security scanning on PRs runs about $5 per PR.
- Externalize decisions into durable shared docs rather than chat, so each parallel agent starts stateless from the same state and 'agent bankruptcy' stops being a thing.
- Use vertical tab layouts and a notification-driven workflow to manage many concurrent sessions; horizontal tabs lose track at scale.
- Build the eval before optimizing the fan-out, so you can pick models on the cost/performance frontier instead of on brand.
- Keep each agent's context under ~100k tokens (under 60k for the hardest problems) and re-allocate a fresh context per iteration instead of compacting.

**Avoid:**

- Widening fan-out while review capacity is fixed — PRs pile up and the throughput gain evaporates.
- Stacking loops on loops and buying quality with more tokens; ask what a sustainable per-engineer monthly token budget actually is.
- Layering non-deterministic verification on top of agent output; push verification toward static and deterministic checks.
- Storing secrets as files in agent environments — cited as the single most effective concrete hardening step.
- Manually queueing work for agents; the agent schedules its own work better than you do.
- Letting an agent make a critical decision inside a parallel branch — at that point you have ceded ownership of that code.
- Fanning out without scoping discipline, which produces a 'token maxing slop cannon' of high-volume low-quality output.
- Compaction as a context strategy across long parallel runs; it is lossy and degrades fidelity.
- Targeting 100x speedup, which traps you in meta-optimization; 2–3x is the achievable target.
- Running loops in dynamically typed languages like Python or Ruby, where there is no type-level verification to close the loop against.

## Notable Outliers

- A 48 GB MacBook can host roughly 50 active worktrees — i.e. 50 sub-agents in parallel — with the developer acting purely as orchestrator. ([Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [4:22](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=262s))
- Running a coding agent in a loop works out to $10.42 per hour, which is what makes wide parallel looping economically obvious. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [20:42](https://www.youtube.com/watch?v=c35YoMdnI78&t=1242s))
- More agents running does not mean more of you available — cognitive bandwidth does not parallelize. (["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [12:00](https://www.youtube.com/watch?v=n97BCfyFIvw&t=720s))
- The invariant for concurrent agents is not 'no concurrency' but one ordered commit path per mutable state boundary; last-writer-wins is not a consistency model. ([Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [8:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=503s))
- A single rollout primitive (sandbox → agent → verifier → reward) covers evaluation, SFT data collection, RL, and ordinary batch agent workloads, so 'everything is a rollout' and parallel rollouts are the universal unit. ([Everything Is a Rollout](../talks/everything-is-a-rollout.md), [10:08](https://www.youtube.com/watch?v=jRCpXUjz4CI&t=608s))
- Once stage-four delegation infrastructure exists, moving to multi-agent parallelism costs almost nothing additional. ([Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [12:11](https://www.youtube.com/watch?v=whue9_YquGA&t=731s))
- Fan-in over two disagreeing agents should itself be an agent rather than a metric threshold, because a plain if-condition reintroduces rule-based false positives. ([Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [14:30](https://www.youtube.com/watch?v=o6U_2vd967Y&t=870s))

## All Talks

- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)
- [Everything Is a Rollout](../talks/everything-is-a-rollout.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md)
- [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)
- ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)
- [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)
- [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

## Speakers

- [Alex Shaw](../speakers/alex-shaw.md)
- [Divakar Kumar](../speakers/divakar-kumar.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Jeffrey Lee-Chan](../speakers/jeffrey-lee-chan.md)
- [Leo Mehr](../speakers/leo-mehr.md)
- [Matt Dailey](../speakers/matt-dailey.md)
- [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)
- [Ryan Marten](../speakers/ryan-marten.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)

