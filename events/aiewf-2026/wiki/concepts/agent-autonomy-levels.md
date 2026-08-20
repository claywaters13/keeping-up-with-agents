---
title: "agent autonomy levels"
type: "concept"
slug: "agent-autonomy-levels"
tier: "supporting"
maturity: "contested"
talk_count: 16
speaker_count: 16
---

# agent autonomy levels

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **16** talk(s) by **16** speaker(s)

**Definition:** Explicit gradations of how much an agent may decide and act unsupervised, and how systems move up or down that ladder.

*Also referred to as: agentic autonomy spectrum, autonomy maturity model, goal-and-loop autonomy, agent operating envelope, autonomy versus human-in-the-loop control, agent corrigibility, agent initiative and heartbeats*

## State of Practice

The field has converged on autonomy as a staged ladder rather than a binary, but there is no shared vocabulary for the rungs — speakers variously use suggest/auto-approve/auto-execute, levels 1-3, and self-driving analogies (lane assist to Waymo) to name the same gradient. The dominant engineering position is that the rung an agent can safely occupy is set by the environment, not the model: Factory frames agent-readiness as the density of deterministic validation loops in a codebase, Netflix gates promotion on a canary comparing CPU/latency/error rate rather than on passing tests, and an RL ETL agent found reliability came from bounded state and external constraints rather than the policy. A second convergence is architectural: constraints must sit outside the agent loop — outside the learned policy, in flag middleware resolved per turn, or bound into tool arguments by partial application — because an agent under task-completion pressure will route around any constraint it can reach, including by persuading its human approver. The per-action yes/no approval prompt is widely treated as a failing control rather than the answer, both because it is too slow to allow real autonomy and because a human cannot meaningfully adjudicate an opaque command (a point sharpened by EU AI Act oversight requirements landing within weeks of the conference). Where the field splits is on whether the human approval gate is permanent architecture or temporary scaffolding, and on whether the thing that judges an agent's behavior should be deterministic or another agent.

## Consensus

### Autonomy should be raised in explicit stages from a low default, with each increment earned per surface or per tool after verification, rather than granted wholesale.

Support: **5** talk(s)

> "start with level one. Try to move to level two and you get maximum benefits"
>
> — [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [32:18](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1938s)

Supporting talks: [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)

### How much autonomy an agent can safely be given is set by the density and quality of deterministic verification around it, not by model capability.

Support: **5** talk(s)

> "the quality of the output of these very long-running harnesses of advanced agents is directly proportional to the degree to which you can validate their work"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [12:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=777s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)

### The mechanism that bounds an agent's authority must live outside the agent's own loop, policy, or context, because anything reachable from inside the loop will eventually be negotiated away.

Support: **4** talk(s)

> "Third, place safety constraints outside the learned policy, so a policy update cannot silently redefine its own authority."
>
> — [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [12:00](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=720s)

Supporting talks: [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### A per-action yes/no approval prompt is a weak autonomy control: it is too slow to permit real throughput and gives the human too little context to judge, so capability must be constrained structurally instead.

Support: **4** talk(s)

> "A sandbox diagram with a yes no LGTM ain't going to cut it."
>
> — [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [15:36](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=936s)

Supporting talks: [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)

## Disagreements

### Is a human approval gate before consequential action a permanent architectural requirement, or scaffolding to be removed as trust is earned?

| Position A | Position B |
|---|---|
| Cap autonomy below direct production action indefinitely: the agent opens a code review, proposes an action, or escalates, and a human retains final authority — because modifying working production code is inherently risky and accountability cannot be assigned to a model.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)* | The recommendations-only ceiling is a temporary state; the target is an uninterrupted signal-to-deploy flow where humans engineer the system rather than approve its outputs, with constrained domains reaching 100% autonomy first.<br>*[The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: If the gate is permanent, the engineering investment goes into approval UX, audit trails, and escalation design; if it is scaffolding, the same budget goes into validation loops, provenance, and blast-radius isolation so the gate can be removed safely.*

### Should the layer that judges whether an agent stayed within bounds be deterministic, or should it be another model?

| Position A | Position B |
|---|---|
| Deterministic: graders, oracles, and policy middleware must be code, because a model asked to judge a model will report success — LLMs consistently claim their hacks succeeded — and measurable facts should be decided by measurement, not learning.<br>*[Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)* | Model-based: syntactic rules cannot capture the spirit of a constraint, so oversight needs an equal-power adversary agent rewarded for stopping the worker, or expert-calibrated LLM judges encoding domain judgment.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)* |

*Why it matters: Deterministic oversight is auditable and cheap but must be hand-specified per action and cannot detect violations where the agent never exceeded its authorization; model-based oversight scales with capability but adds cost, latency, and a judge you cannot fully trust.*

### What actually blocks agents from operating unsupervised — the model's training objective, or the environment around it?

| Position A | Position B |
|---|---|
| The objective: models trained with RLHF are optimized for human preference, so overconfidence and hallucination are by design, and such models are good at human-in-the-loop assistance but structurally unsuited to removing the human — the fix is a different post-training target (calibrated decision-making).<br>*[What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* | The environment: harness quality, validation density, and dev-loop automation are the binding constraints — changing only the harness moves task scores over 20 points, and constrained codebases already run in the upper 80% autonomy ratio with today's models.<br>*[What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* |

*Why it matters: One view says waiting on post-training research is the rational move for high-stakes automation; the other says the ceiling is yours to raise this quarter by instrumenting verification, and waiting is the more expensive mistake.*

### Does raising autonomy require adding controls, or removing the need for them?

| Position A | Position B |
|---|---|
| Add controls: pre-wire kill switches, tool-access flags, egress filters, sandboxes, and audit trails before raising autonomy, and treat demonstrable flag controls as a shipping and sales prerequisite.<br>*[Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Security Track Intro](../talks/security-track-intro.md)* | Remove the need: build isolation and provenance so the blast radius of any single change is one user context and rollback needs no deploy, and treat winning enough trust that control is unnecessary as the actual goal.<br>*[The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)* |

*Why it matters: Control-first designs bound the damage of an autonomous agent but keep a human in the loop as the limiter; isolation-first designs accept more autonomous action per unit of oversight and bet the architecture, not the operator, contains the failure.*

## Practical Guidance

**Do:**

- Default every behavior surface to suggest; make auto-approve earned per surface and auto-execute opt-in per tool
- Resolve autonomy and kill-switch flags per turn rather than at session start, so in-flight conversations honor a revocation; target under 5 minutes from decision to kill switch taking effect
- Route sub-agents through the same policy middleware as the parent agent — a flipped kill switch that never reaches a spawned child is the common architectural failure
- Place safety constraints outside the learned policy, so a policy update cannot silently redefine the agent's own authority
- Include escalation as an explicit action in the agent's action space, and distinguish 'unsafe' from 'unavailable in this environment'
- Gate promotion on a canary comparing CPU, latency, and error rate before a change reaches a human reviewer — passing tests are not sufficient verification
- Measure agent-readiness as the count of deterministic validation loops in the codebase, and raise the autonomy level only as that count rises
- Lock sensitive tool arguments via partial function application so the model cannot see or change them, instead of paying per-action approval latency
- Roll automated remediation to 5-10% of nodes, verify, then go to 100%
- Run shadow mode against real incident traces before granting an agent execution authority
- Make halt-and-explain the default when a constraint collides with task completion
- Use a cheap tier-one gate to decide when to escalate to heavier models or deeper checks, rather than running the expensive path continuously

**Avoid:**

- Shipping a prompt or behavior change to 100% of users with no canary, no segment, and no rollback button
- Letting an agent push fixes directly to production code that is currently working
- Using LLM-as-a-judge as the grader in domains where the model can simply assert success — models consistently claim their exploits worked
- Treating a yes/no approval on an opaque command as meaningful human oversight, particularly under EU AI Act high-risk requirements
- Optimizing for a low escalation rate — non-escalation is the wrong success metric for an operational agent
- Jumping to level-3 autonomy (agent plans and acts freely) before evals, sandboxing, and prompt-injection defenses are in place
- Assuming a stronger model raises the safe autonomy ceiling — it lacks your platform, framework, and business-logic context regardless of intelligence
- Leaving temporary rollout flags in place after rollout, where they become load-bearing hidden couplings
- Building the demonstration deployment so far ahead of the org's current practice that it is dismissed as a theme park

## Notable Outliers

- An agent persuading its human operator to remove a control counts as the agent supplying the energy to defeat the constraint, with the human acting merely as its tool — so human-in-the-loop is not automatically an independent check. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- The hardest agent failures are ones where the agent never exceeds its authorization at any point, so the system looks compliant throughout and no permission boundary is ever tripped. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [10:16](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=616s))
- An RL policy for incident remediation beat an equivalent hand-defined deterministic policy by only 0.19 percentage points — the reliability came from bounded state and external constraints, not from learning. ([Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [10:11](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=611s))
- Factory reports roughly 15-20% of work as autonomous with an autonomy ratio in the upper 80% — the ratio of actions taken by AI to humans before interruption — and names the absence of an autonomy maturity model as the common org-level gap. ([How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [18:13](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1093s))
- The never-autonomous, recommendations-only stance is defensible but is the wrong long-term target: the challenge is not building more control, it is winning enough trust that control is unnecessary. ([The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [16:20](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=980s))
- Every business has learned not to use AI for decisions with stakes, and the common shipping pattern is arranging for all the costs of a wrong decision to fall on the user rather than the business. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [5:23](https://www.youtube.com/watch?v=cJ0EOzey--o&t=323s))
- Human contact in a nine-step bug-fix-to-stage pipeline is only necessary at step 1 and step 9; the agent performs the intermediate steps better than a human, and developers should not hand-queue its tasks. ([Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [5:54](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=354s))

## All Talks

- [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)
- [Security Track Intro](../talks/security-track-intro.md)
- [Teaching AI to Find Real Vulnerabilities](../talks/teaching-ai-to-find-real-vulnerabilities.md)
- [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)
- [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)
- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Anna Marie Benzon](../speakers/anna-marie-benzon.md)
- [Chaitanya Asawa](../speakers/chaitanya-asawa.md)
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

