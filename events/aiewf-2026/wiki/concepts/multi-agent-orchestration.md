---
title: "multi-agent orchestration"
type: "concept"
slug: "multi-agent-orchestration"
tier: "core"
maturity: "contested"
talk_count: 26
speaker_count: 28
---

# multi-agent orchestration

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **26** talk(s) by **28** speaker(s)

**Definition:** Coordinating several agents as a system — topology, handoffs, shared state, and consensus — as opposed to one agent calling tools.

*Also referred to as: agent orchestration, multi-agent coordination, multi-agent architecture, hierarchical multi-agent systems, manager-worker agent architecture, supervisor-agent orchestration, agent swarms*

## State of Practice

The field arrived at this conference having actually run multi-agent systems in production, and the mood is corrective rather than expansionist. The dominant finding is that failures blamed on reasoning are usually structural: context lost at handoffs, distributed-state inconsistency, and orchestrator agents that quietly do the work themselves instead of dispatching. The converged design pattern is narrow single-job agents with scoped context, coordinating through durable external state (files, event logs, knowledge graphs, blackboards) rather than through chatty agent-to-agent reasoning exchange; sub-agents return compressed results and evidence, never their reasoning traces, both to protect the parent's context window and to prevent convergent groupthink. Deterministic components — signal detection, statistical checks, SQL, emergency routing, permission enforcement — are being pulled out of the agentic system entirely and run before or above the model, with agents reserved for what rules cannot decide. Parallelism is now understood to require real isolation (git worktrees, per-agent sandboxed filesystems, dedicated cloud workspaces) and, more importantly, to be capped not by tokens or compute but by human attention: several speakers independently described discovering that they had become the scheduler, router, and memory for their own fleet. The live fights are whether to decompose reasoning across agents at all, whether the orchestration harness should be hand-engineered or allowed to emerge (or vanish as models self-orchestrate), and whether coordination needs a new infrastructure layer or a reuse of Kubernetes and CI/CD.

## Consensus

### Deterministic logic belongs outside or above the agentic system — run rules, statistics, and policy checks first, and invoke agents only for what rules cannot decide.

Support: **5** talk(s)

> "Two, deterministic rules belong above the model, not inside it. What can never be wrong cannot be left to probability."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [2:34](https://www.youtube.com/watch?v=YXEqC05WEI0&t=154s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Notion's Token Town](../talks/notions-token-town.md)

### Without explicit orchestration structure, the human collapses into being the scheduler, router, and memory of the fleet, and their attention — not tokens or compute — becomes the binding constraint.

Support: **5** talk(s)

> "I thought I was orchestrating. Really, I was polling. I was the scheduler, the router, and the memory."
>
> — [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [19:19](https://www.youtube.com/watch?v=pMggiOb18tc&t=1159s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)

### Human approval and supervision are permanent architectural components of agent systems, not scaffolding that better models will remove.

Support: **5** talk(s)

> "Many people frame human involvement as temporarily temporary necessity. I don't think that's correct. The most successful systems are likely to remain human supervised."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [4:50](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=290s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)

### Give each agent one job and a minimal tool/skill inventory; a single agent carrying every tool, skill, or prompt responsibility performs measurably worse.

Support: **4** talk(s)

> "So, specialize, don't overload."
>
> — [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [13:02](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=782s)

Supporting talks: [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)

### Handoffs between agents — not prompts, models, or reasoning quality — are where multi-agent systems actually break, because context is silently lost or corrupted at each boundary.

Support: **4** talk(s)

> "Every single handoff is the place where the system can lie to you. And if you're building the system alone, nobody catches the lies except you, usually after the damage is done."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [1:39](https://www.youtube.com/watch?v=WLXxTaPagA8&t=99s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)

### Sub-agents should return compressed findings, results, or claim-plus-evidence to the parent — never their full reasoning traces or raw tool output.

Support: **3** talk(s)

> "That you can still delegate to a sub-agent. You can get back the uh results back, not the reasoning or the judgment."
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [8:30](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=510s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)

### Real parallelism requires isolated execution environments per agent — worktrees, sandboxed filesystems, or dedicated cloud workspaces — because shared local machines collide on resources, credentials, and state.

Support: **4** talk(s)

> "So, we invested in dedicated cloud workspaces where each agent ran in its own isolated environment. And this allowed us to easily run them in parallel and from anywhere."
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [14:16](https://www.youtube.com/watch?v=whue9_YquGA&t=856s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)

### Durable coordination state must live outside the model — in files, an event log, or a shared store — so it survives context wipes, compaction, and crashes.

Support: **4** talk(s)

> "The state lives in files. It is not trapped inside one model. And this is the single most practical thing I learned all year."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)

### Verification should come from an agent with different context than the one that produced the work; a producer evaluating its own output is systematically biased toward approval.

Support: **4** talk(s)

> "that's kind of the benefit you get, where the manager has a different context um than the workers"
>
> — [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [10:07](https://www.youtube.com/watch?v=9arM9b7JgOo&t=607s)

Supporting talks: [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)

## Disagreements

### Should reasoning and judgment be distributed across multiple agents, or consolidated into exactly one agent that owns the end-to-end picture?

| Position A | Position B |
|---|---|
| Consolidate: exactly one agent must own end-to-end reasoning. Splitting judgment across specialized agents produces locally-correct, globally-incoherent output, and the right move before adding another agent is adding a boundary to the one you have. Frontier models increasingly self-orchestrate without any custom decomposition.<br>*[Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* | Decompose: many narrowly-scoped agents outperform one general agent, because a single prompt that must do everything does everything badly and multi-agent structure gives finer control over system behavior. Expanding scope should mean adding an agent, not lengthening a prompt.<br>*[The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)* |

*Why it matters: This determines whether your engineering effort goes into topology and handoff contracts or into context engineering and tooling for a single deep agent — and whether observed incoherence is read as a decomposition bug to fix or as evidence the decomposition itself was the mistake.*

### Should the orchestration harness be explicitly engineered and maintained, or allowed to emerge from agent interaction (or disappear as models improve)?

| Position A | Position B |
|---|---|
| Engineer it deliberately and expect it to persist: hierarchies as real entity types with scoped context and approval boundaries, an event-sourced runtime, an agentic control plane. The harness will not dissolve as models improve, and harness design is the current bottleneck.<br>*[I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* | Don't hand-build it: a carefully built harness can be irrelevant within a month, so the harness should be the output of the process — emerging from agent interaction with roles and governance forming locally — or simply unnecessary, since a sufficiently capable model will spawn, split, and verify work when told to.<br>*[Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* |

*Why it matters: If the harness is durable infrastructure, investment in control planes, entity hierarchies, and event logs compounds; if it is a temporary crutch around model weakness, that investment is written off at every model release.*

### Should agents coordinate exclusively through shared state, or communicate directly with each other?

| Position A | Position B |
|---|---|
| Never let agents message each other. All coordination goes through shared state — an immutable event log, a blackboard, a knowledge-graph control plane — which is what yields replay, rollback, forks, and auditable consistency; sub-agents hand back results into that state rather than conversing.<br>*[Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)* | Direct agent-to-agent messaging is the right primitive: full sub-agents with their own loops and histories talking to their coordinator in plain English, threads that can send messages to each other, and eventually a cross-organizational agent web with signed identity records, message boxes, negotiation, and payments.<br>*[The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)* |

*Why it matters: Shared-state-only coordination makes the system auditable and replayable but confines it to one trust domain; direct messaging scales across organizational boundaries but forces you to solve identity, spam, trust, and consistency yourself — and several speakers attribute multi-agent failures to exactly that consistency gap.*

### Does running more agents in parallel actually increase throughput?

| Position A | Position B |
|---|---|
| Yes, and it is the core unlock: agents in git worktrees, isolated cloud workspaces, five or six parallel approaches with the best selected, thousands of small agents across regions. Once delegation infrastructure exists, adding parallelism costs almost nothing.<br>*[Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* | No — a flat pile of parallel agents does not scale, because human cognitive bandwidth does not parallelize and each additional loop adds routing, merging, and verification decisions. Throughput just relocates the bottleneck to review, and PRs pile up unreviewed.<br>*["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)* |

*Why it matters: If parallelism is the unlock, you invest in sandboxes and dispatch infrastructure; if human attention is the ceiling, you invest instead in hierarchy, scoped context, and automated review gates — and note that the strongest pro-parallelism talk also reports code review becoming the unsolved binding constraint.*

### Does agent orchestration need a new infrastructure layer, or should it reuse existing distributed-systems and CI/CD infrastructure?

| Position A | Position B |
|---|---|
| A new layer is emerging and is where the advantage lies: an agentic control plane analogous to Kubernetes for containers, and a full agentic-web stack of identity, registry, trust, payments, coordination, and negotiation layers that DNS-era infrastructure cannot serve.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)* | Reuse what exists: Kubernetes already solves compute, secrets, tools, and scheduling, so build only orchestration, review flow, and context management on top — and the operational guarantees you keep rediscovering are just contract testing, staging, gates, and audit trails you are rebuilding badly. No framework required.<br>*[I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)* |

*Why it matters: It decides whether teams spend the next year building or buying an agent control plane, or spend it wiring agents into the CI/CD and cluster infrastructure they already operate.*

## Practical Guidance

**Do:**

- Route sub-agent output back to the parent as a summarized finding or claim-plus-evidence, and deliberately withhold the sub-agent's reasoning so peer agents don't converge into groupthink
- Partition workflows so deterministic parts (signal detection, statistical checks, SQL, emergency routing, identity verification) execute outside the agentic system, before the agent is invoked
- Force delegation structurally — expose dispatch as CLI-backed skills so the orchestrator's only available path is to dispatch, since it will otherwise do the work itself
- Keep fleet state in files on disk and recover by clearing context and re-reading self-written handoff/history files, rather than relying on compaction you cannot control
- Separate per-machine state into per-machine directories and require shared state to change only via pull request when running agents across multiple machines
- Run the fleet's single control point on an always-on machine — a laptop that sleeps cannot be a control plane
- Instrument the most expensive handoff first (measured by cost of bad data), not the most technically complex one
- Make gates blocking: a gate that only logs a warning is a suggestion, not a guarantee
- Use a jury of independent agents plus a consensus judge that weighs reasoning quality for questions with no empirically correct answer, and expand the jury when consensus is insufficient
- Require two independent sources to agree before proceeding without human verification, and escalate to a human whenever evidence or confidence is insufficient
- Give each agent its own sandboxed filesystem and sandboxed code execution environment, and run parallel work in git worktrees or dedicated cloud workspaces
- Treat the knowledge graph as a control plane that constrains which paths and hypotheses the agent may pursue, not as a data lookup layer
- Have agents declare their resource requirements and let the system place them, rather than choosing which machine each runs on by hand
- Snapshot real tool responses as checked-in fixtures and run offline evals so multi-agent quality is quantified rather than intuited

**Avoid:**

- Letting sub-agent output spill into the primary thread's context — it burns tokens and degrades answer accuracy even far below the context limit
- Handing one agent a large tool, skill, or MCP inventory; installing many skills into a single agent measurably degrades it
- Distributing judgment across a chain of specialized agents that each derive locally correct facts while no agent owns the end-to-end picture
- Designing agent topology by mimicking the steps a human analyst takes — human process constraints are not architectural constraints
- Uncontrolled retries, which turn a minor API error into exponential resource growth and a compute incident
- Letting the model directly control production systems instead of emitting proposals that infrastructure validates, policy approves, and a gateway enforces
- Running a flat pile of parallel agents, which forces the human into scheduler, memory, and reviewer simultaneously
- Stacking agent and MCP processes on one machine until memory is exhausted and swap fills, or pointing two machines at the same shared context directory
- Treating agent hierarchy as a descriptive metaphor rather than implementing it as real entity types with scoped context and approval boundaries
- Adding another agent when the actual missing thing is one boundary check on the system you already have
- Allowing autonomous outbound communication — keep a human on every send
- Shipping because the artifacts look complete; a polished, plausible artifact is more dangerous than a visibly bad output

## Notable Outliers

- AI models write shared-state/blackboard-style agent code better than LLM-agent-style code, because decades of blackboard-architecture discussion exist in the training data while LLM agent patterns are only about three years old. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [14:54](https://www.youtube.com/watch?v=khVX_BUnEwU&t=894s))
- Agent identity, roles, and specialization should not be assigned by the engineer at all — they should arise from an agent's position relative to other agents and environmental pressure, with governance emerging from local coordination and no central authority. ([Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [23:57](https://www.youtube.com/watch?v=qdZzND79mcg&t=1437s))
- The orchestration infrastructure itself can be built by the agents: an infra team inside the fleet built the review gateway that gates the fleet's own actions. ([I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [3:48](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=228s))
- Consolidating a failed multi-agent pipeline into a single agent produced root-cause analyses in 20-30 minutes and 50+ turns for work that previously took an analyst three to four weeks — accepting very high token and turn counts as the price of coherent end-to-end reasoning. ([Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [13:10](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=790s))
- 2027 will be the year of multi-agent orchestration; domain-specific agents that make it viable do not meaningfully exist in public today. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [21:55](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1315s))
- Pinned persistent threads that can list, rename, and message each other are superior to sub-agents for ongoing work, because sidebar visibility lets you notice state changes. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [58:17](https://www.youtube.com/watch?v=il1c1a2FufU&t=3497s))
- Distributing documents across parallel context caches by domain hurts recall, because the supervisor skips domains that look irrelevant at first glance — documents should be distributed in no particular order. ([When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:50](https://www.youtube.com/watch?v=XovaGv4f39A&t=230s))
- High model throughput matters mainly because it lets you run five or six parallel approaches and pick the best, not because a single answer arrives faster. ([The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [16:07](https://www.youtube.com/watch?v=pMggiOb18tc&t=967s))

## All Talks

- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)
- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)
- [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)
- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)
- [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)
- [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)
- [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)
- [Notion's Token Town](../talks/notions-token-town.md)
- [Perception Agents](../talks/perception-agents.md)
- [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)
- ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)
- [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)
- [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)
- [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)

## Speakers

- [Abhilash Asokan](../speakers/abhilash-asokan.md)
- [Alex Bauer](../speakers/alex-bauer.md)
- [Alexander Embiricos](../speakers/alexander-embiricos.md)
- [Anant Shankhdhar](../speakers/anant-shankhdhar.md)
- [Antje Barth](../speakers/antje-barth.md)
- [Benjamin Guo](../speakers/benjamin-guo.md)
- [Dhruv Batra](../speakers/dhruv-batra.md)
- [Drasko Profirovic](../speakers/drasko-profirovic.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Jeffrey Lee-Chan](../speakers/jeffrey-lee-chan.md)
- [Kyle Jaejun Lee](../speakers/kyle-jaejun-lee.md)
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Rajiv Chandegra](../speakers/rajiv-chandegra.md)
- [Ramesh Raskar](../speakers/ramesh-raskar.md)
- [Rashi Agrawal](../speakers/rashi-agrawal.md)
- [Richard Socher](../speakers/richard-socher.md)
- [Rob Cheung](../speakers/rob-cheung.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

