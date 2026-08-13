---
title: "agent autonomy levels"
type: "concept"
slug: "agent-autonomy-levels"
tier: "supporting"
maturity: "contested"
talk_count: 14
speaker_count: 14
---

# agent autonomy levels

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **14** talk(s) by **14** speaker(s)

**Definition:** Explicit gradations of how much an agent may decide and act unsupervised, and how systems move up or down that ladder.

*Also referred to as: agentic autonomy spectrum, autonomy maturity model, goal-and-loop autonomy, agent operating envelope, autonomy versus human-in-the-loop control, agent corrigibility, agent initiative and heartbeats*

## State of Practice

The field has converged on treating autonomy as a discrete, per-surface ladder rather than a binary: suggest → auto-approve → auto-execute (Gupta), or level 1 → 2 → 3 where level 3 means the agent plans and acts freely (Shah at Netflix). Nearly everyone shipping to production says the same thing about where to start — default to the lowest rung, earn promotions per tool, and stage rollouts (5–10% of nodes, then 100%; a prompt variant whose error rate rises >2% over baseline at 5% doesn't get promoted). The most load-bearing claim of the conference is that the autonomy ceiling is set by verification infrastructure, not model capability: Factory defines 'agent readiness' as the density of deterministic validation loops in a codebase, Netflix requires an automated canary comparing CPU/latency/error rate before a human ever sees the diff, and Bugcrowd shows LLM-as-a-judge collapses entirely on security tasks. There is broad agreement that a yes/no approval prompt on an opaque command is not a control — it is slow, it doesn't scale, and it won't satisfy the EU AI Act's 'meaningful human oversight' bar. What is genuinely unresolved is the top of the ladder: whether human approval is a permanent architectural element (Netflix stops at level 2; Auditoria says accountability in finance can't be assigned to a model) or a temporary artifact of insufficient trust (Sky Valley calls recommendations-only 'the wrong long-term target'; Factory reports an autonomy ratio in the upper 80s and expects constrained internal tools to hit 100% first).

## Consensus

### Autonomy should be entered at the lowest rung and ratcheted up per surface with staged, measured rollout — never granted wholesale at launch.

Support: **4** talk(s)

> "start with level one. Try to move to level two and you get maximum benefits"
>
> — [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [32:18](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1938s)

Supporting talks: [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)

### How much autonomy an agent can safely be given is determined by the density and quality of deterministic verification around it, not by model capability — better models do not raise the ceiling.

Support: **5** talk(s)

> "the quality of the output of these very long-running harnesses of advanced agents is directly proportional to the degree to which you can validate their work"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [12:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=777s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)

### Per-action human approval prompts are not a workable autonomy control: they are too slow to scale and the approving human usually lacks the context to answer, so capability must be constrained structurally instead.

Support: **3** talk(s)

> "even when the agent knows that it should ask permission and and I get a nice block of, "Hey, Aaron, do you agree? Should I do this thing?" I'm honestly not sure if I should say yes or no"
>
> — [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [5:48](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=348s)

Supporting talks: [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

### The mechanism that revokes or narrows autonomy must live outside the agent loop and take effect on an in-flight run without a redeploy.

Support: **3** talk(s)

> "First, you flip it and the change takes effect in seconds, not in a deployment pipeline. Second, inflight request respect the flag at the next decision point."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [9:12](https://www.youtube.com/watch?v=zU4EagB311U&t=552s)

Supporting talks: [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)

## Disagreements

### Is a permanent human approval step a necessary feature of production agent systems, or a temporary scaffold to be removed as trust is earned?

| Position A | Position B |
|---|---|
| Human approval is a structural requirement, not a trust deficit. Netflix deliberately caps at level 2 — the agent opens a code review, never pushes — because modifying working production code is inherently risky, and says level 3 needs eval/sandbox/prompt-injection investment most teams cannot make. Auditoria argues agent-to-agent review is unacceptable in finance because accountability cannot be assigned to a model. TypeSafe AI generalizes it: don't use AI for decisions with stakes to your business.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* | The approval step is the thing to engineer away. Sky Valley calls the recommendations-only posture defensible but the wrong long-term target — the challenge is winning enough trust that control isn't needed. Factory reports an autonomy ratio in the upper 80% and expects constrained internal tools to reach 100% autonomy before general codebases. Mastra argues harnesses inevitably expand into always-on agents with initiative. Corridor frames security as guardrails rather than gates, because acceleration always wins.<br>*[The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)* |

*Why it matters: It determines whether you invest in making human review fast (one pane of glass, batched diffs, autonomy ratio metrics) or in making it unnecessary (canaries, blast-radius isolation, adversary agents). The two roadmaps diverge almost immediately and share very little infrastructure.*

### How much planning latitude should an agent have at its working autonomy level — should it decide what to do next, or execute a fixed workflow?

| Position A | Position B |
|---|---|
| Zero planning latitude is often sufficient and preferable. Netflix runs a fixed, predefined workflow with no LLM planning or reasoning on a weekly per-service schedule and still gets 0.5–4.6% CPU savings. TwelveLabs insists a worker needs an explicit deterministic harness with an operating envelope and output contracts because a bare model is stateless and unconstrained. Gupta's failure catalog includes a four-agent pipeline that free-ran into $47,000 of spend.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)* | Initiative and self-scheduling are the point. Mastra defines the harness-to-claw transition as imbuing agents with initiative and learning plus a heartbeat that wakes them up. Auditoria says developers should stop queuing tasks because the agent schedules its own work better, and runs background 'dreaming' to self-upgrade. Sky Valley goes furthest: the agent is the runtime and modifies software live per user.<br>*[Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)* |

*Why it matters: Fixed workflows are auditable, cheap, and need no eval harness; initiative-taking agents need continual-learning infrastructure, budget enforcement, and sandboxing that speakers on both sides agree does not reliably exist yet.*

### Can the autonomy ceiling be raised by engineering around today's models, or does it require a different post-training objective?

| Position A | Position B |
|---|---|
| Engineering around the model is what moves the needle. Etsy shows a 52.4%→76.2% swing on 106 tasks from changing only the harness, and argues a good enough harness lets a local open-source model match a frontier one. Factory says any problem framable as a set of verification systems is solvable with AI today. Netflix says the hard prerequisites — observability, canary, verify logic — are ordinary engineering, not AI problems.<br>*[What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)* | The limit is baked into post-training. TypeSafe AI argues overconfidence and hallucination are by construction in RLHF — the reward model rewards apparent confidence, so models are excellent at human-in-the-loop and structurally wrong for automation, and the fix is optimizing for calibrated decision-making. dbt Labs argues the task-completion imperative is the agent's programming, so deterministic controls (egress filters, gVisor, telemetry) are necessary but not sufficient and an equal-power adversary agent is needed.<br>*[What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)* |

*Why it matters: If the ceiling is a harness problem, autonomy scales with your own engineering investment starting now; if it is a post-training problem, high-autonomy deployments on current models are structurally miscalibrated no matter how good the scaffolding is.*

## Practical Guidance

**Do:**

- Default every tool to 'suggest'; make auto-approve earned per surface and auto-execute opt-in per individual tool.
- Build the kill switch before tool wrapping, autonomy staging, or prompt variants — target under 5 minutes from decision to mitigation.
- Resolve autonomy and kill-switch flags per turn, not at session start, so in-flight conversations honor a revocation at the next decision point.
- Route sub-agents through the same flag/policy middleware as the parent; a parent-only control is not a control.
- Require an automated canary comparing CPU, latency, and error rate before a code review reaches a human — passing tests are not sufficient verification.
- Measure agent readiness as the count of deterministic validation loops in the codebase and raise autonomy only as that count rises.
- Roll automated remediation to 5–10% of machines, verify, then go to 100% of nodes.
- Lock sensitive tool arguments via partial function application so the model cannot see or change them — autonomy without per-action approval latency.
- Declare regions like auth and payments permanently off limits to agent adaptation while leaving lower-stakes regions adaptable.
- Keep humans at the endpoints of the pipeline (task framing and final approval) and treat them as verifiers, never as the throughput ceiling.
- Track an explicit autonomy ratio — actions done by AI vs humans before interruption — as the metric for whether autonomy is actually increasing.
- Set an explicit constraint-conflict default of halt-and-explain rather than route-around when a task and a constraint collide.
- Use deterministic graders, not LLM-as-judge, to decide whether an agent's autonomous work succeeded.
- Keep a 100% complete audit trail of who changed which autonomy setting and when.

**Avoid:**

- Treating a yes/no approval prompt on an opaque command as your human-oversight story — it will not meet the EU AI Act's meaningful-oversight bar.
- Letting an agent push changes directly to production, even performance-only ones, on code that currently runs fine.
- Assuming a newer, better model raises the autonomy ceiling — it has no knowledge of your internal platforms, frameworks, or codebase patterns.
- Jumping to level-3 autonomy (agent plans and acts freely) without evaluation, sandboxing, and prompt-injection defenses in place.
- Free-running multi-agent loops with no budget cap or kill switch — a four-agent pipeline with two continuous loops cost $47,000.
- Shipping prompt changes to 100% of users with no canary, no segment, and no rollback button.
- Hard-dependence on a single model from a single provider with no routing flag or fallback.
- Leaving temporary rollout flags in place after rollout; every flag needs an owner and a removal date.
- Building an autonomy showcase far ahead of the org's current practice — it gets dismissed as a theme park rather than copied.
- Deploying agents into a workflow lacking observability and verification foundations; it produces more friction and more production bugs than it removes.

## Notable Outliers

- An agent persuading a human to disable a control counts as the agent supplying the energy to defeat its own constraint, with the human acting merely as its tool — so the energy to overcome a constraint must come from outside the agentic loop. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- The hardest agent failures are ones where the agent never exceeds its authorization at all — the system looks compliant the entire time, which is exactly why permission-based autonomy levels miss them. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [10:16](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=616s))
- More than two kill-switch fires per week indicates a problem worth investigating; the target is zero. ([Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [14:41](https://www.youtube.com/watch?v=zU4EagB311U&t=881s))
- The challenge is not building more control but winning enough trust that you don't have to — recommendations-only is defensible today and the wrong long-term target. ([The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [16:20](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=980s))
- Highly constrained internal tools will reach 100% autonomy before general product codebases, because validators exist for them and not for hard visual problems like a terminal-based harness. ([How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [18:52](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1132s))
- Today's AI is excellent at human-in-the-loop work and bad at automation by construction, because RLHF optimizes for human preference rather than calibrated correctness — so the lesson businesses have learned is not to use AI for decisions with stakes. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [5:23](https://www.youtube.com/watch?v=cJ0EOzey--o&t=323s))
- Most organizations do not have an autonomy maturity model at all — no roadmap and no conception of what an autonomous software organization would be. ([How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [9:41](https://www.youtube.com/watch?v=wpOA-UXynoM&t=581s))

## All Talks

- [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)
- [Security Track Intro](../talks/security-track-intro.md)
- [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md)
- [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)
- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [David Brumley](../speakers/david-brumley.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Eno Reyes](../speakers/eno-reyes.md)
- [Jack Cable](../speakers/jack-cable.md)
- [James Le](../speakers/james-le.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Rajat Shah](../speakers/rajat-shah.md)
- [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)
- [Ritvik Pandya](../speakers/ritvik-pandya.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Varun Singh](../speakers/varun-singh.md)

