---
title: "multi-agent orchestration"
type: "concept"
slug: "multi-agent-orchestration"
tier: "core"
maturity: "contested"
talk_count: 25
speaker_count: 27
---

# multi-agent orchestration

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **25** talk(s) by **27** speaker(s)

**Definition:** Coordinating several agents as a system — topology, handoffs, shared state, and consensus — as opposed to one agent calling tools.

*Also referred to as: agent orchestration, multi-agent coordination, multi-agent architecture, hierarchical multi-agent systems, manager-worker agent architecture, supervisor-agent orchestration, agent swarms*

## State of Practice

The field has moved from "more agents" to "fewer agents with harder boundaries." The dominant lesson reported this year is that decomposition modeled on human workflow steps loses context at every handoff and produces systems where each agent is locally right and the whole is incoherent — so judgment is being re-consolidated into a single owning agent while sub-agents are demoted to investigators that return findings, never reasoning. Around that, practitioners converged on a small set of load-bearing mechanics: per-agent scoped context (one job, one or two tools, its own slice), durable state in files or an immutable event log rather than in a context window, deterministic work lifted out of the agentic system entirely and run before the agent is invoked, and blocking gates at the most expensive handoff. Infrastructure people report that most "reasoning failures" in multi-agent systems are actually distributed-state consistency failures, and that the model should emit proposals a policy layer approves rather than act directly. The unresolved center of gravity is where orchestration lives: in an explicit engineered control plane, in emergent agent-to-agent coordination, or increasingly inside the model itself — with Mythos-class self-orchestration used as evidence that the scaffolding is temporary and control-plane advocates arguing the opposite.

## Consensus

### Sub-agents should return compressed results or findings to the parent, never their full output or the reasoning that produced it.

Support: **3** talk(s)

> "That you can still delegate to a sub-agent. You can get back the uh results back, not the reasoning or the judgment."
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [8:30](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=510s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)

### Each agent must have its own scoped context slice; sub-agent context must not spill into the parent thread.

Support: **5** talk(s)

> "These are real entity types in the system. It is not a cute metaphor. Each one is its own agent with its own scoped context and its own approval boundary."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [1:51](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=111s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)

### One agent, one job: a single monolithic prompt or a tool-heavy generalist agent degrades as scope grows, so narrow agents with few tools outperform it.

Support: **4** talk(s)

> "one prompt that's supposed to do everything ends up doing everything badly"
>
> — [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [3:25](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=205s)

Supporting talks: [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)

### Deterministic steps (signal detection, SQL, file conversion, rule checks) should be partitioned out of the agentic system and run before the agent is invoked.

Support: **4** talk(s)

> "any complex workflows will have deterministic parts and agentic parts. Don't let agents actually run the deterministic part, right?"
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [13:51](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=831s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Notion's Token Town](../talks/notions-token-town.md)

### Handoffs between steps — not prompts, models, or reasoning — are where multi-agent systems actually corrupt data, so boundaries need explicit validation.

Support: **3** talk(s)

> "Every single handoff is the place where the system can lie to you. And if you're building the system alone, nobody catches the lies except you, usually after the damage is done."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [1:39](https://www.youtube.com/watch?v=WLXxTaPagA8&t=99s)

Supporting talks: [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)

### A human approval boundary is a permanent structural component of agent fleets, not scaffolding that better models will remove.

Support: **5** talk(s)

> "Many people frame human involvement as temporarily temporary necessity. I don't think that's correct. The most successful systems are likely to remain human supervised."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [4:50](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=290s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)

### Without a real orchestration layer the human silently becomes the scheduler, router, and memory of the fleet, and their attention — not tokens or compute — becomes the binding constraint.

Support: **4** talk(s)

> "I thought I was orchestrating. Really, I was polling. I was the scheduler, the router, and the memory."
>
> — [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [19:19](https://www.youtube.com/watch?v=pMggiOb18tc&t=1159s)

Supporting talks: [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)

### Fleet state belongs in durable external artifacts (files on disk, an immutable event log) rather than inside any model's context window, so context wipes and crashes are recoverable.

Support: **3** talk(s)

> "The state lives in files. It is not trapped inside one model. And this is the single most practical thing I learned all year."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)

## Disagreements

### Does splitting work across multiple reasoning agents improve results, or degrade them relative to one agent that owns the whole problem?

| Position A | Position B |
|---|---|
| Decompose: many narrowly scoped agents (or a jury of independent analysts) beat one agent, because a single prompt cannot be tuned for everything and independent perspectives catch what one agent misses.<br>*[Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* | Consolidate: exactly one agent should hold end-to-end judgment, because context is lost at every handoff and each agent can derive a locally correct fact while nobody understands the whole picture; add a boundary, not another agent.<br>*[Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* |

*Why it matters: This decides whether your engineering budget goes into orchestration, handoff contracts, and consensus machinery, or into giving one agent better tools, a knowledge graph, and a longer leash. Teams that guessed wrong report rewriting the whole system.*

### Should the topology of a multi-agent system be specified by the engineer up front, or allowed to emerge from agent interaction at runtime?

| Position A | Position B |
|---|---|
| Engineer it explicitly: hierarchies as real entity types with approval boundaries, a knowledge graph acting as a control plane that dictates which paths and hypotheses the agent may pursue, and a policy layer that validates every proposed action.<br>*[I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Can Oncology Workflows Run Without Human Touch?](../talks/can-oncology-workflows-run-without-human-touch.md)* | Let it emerge: the harness should be the output of the process rather than its input, with agent roles arising from position relative to other agents; a fixed harness buys reliability by suppressing the variance novelty requires and can be obsolete within a month.<br>*[Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* |

*Why it matters: Explicit topology gives you replay, audit, and a debuggable chain of decisions; emergent topology gives adaptability but, as its own advocates concede, legibility degrades as adaptability rises. You cannot have both, and the choice is made at architecture time.*

### How should agents coordinate — by messaging each other, or only through shared state?

| Position A | Position B |
|---|---|
| Never let LLM components message each other; all coordination goes through shared state (an event log, files, a blackboard), which is what yields replays, rollbacks, and forks.<br>*[Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)* | Agents should talk to each other directly — sub-agents conversing with their coordinator in plain English, threads sending messages to other threads, and cross-organization agents discovering, delegating to, and paying each other via signed identity records.<br>*[The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)* |

*Why it matters: Shared-state coordination is auditable and recoverable but cannot cross organizational boundaries; direct messaging composes across vendors and the open web but reintroduces the untraceable handoffs that multiple teams identified as their primary failure source.*

### Does multi-agent work need a dedicated orchestration/control-plane layer, or is a frontier model plus good thread management already sufficient?

| Position A | Position B |
|---|---|
| A distinct layer is required and is the next locus of competitive advantage — an agentic control plane analogous to Kubernetes for containers, plus registry, identity, and trust layers for anything beyond a single machine.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* | No framework or software factory is needed — tell a self-orchestrating model to spawn workers, split the work, and verify it, or keep one long-lived pinned thread whose compaction now holds hundreds of sub-agents' worth of state.<br>*[Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)* |

*Why it matters: If orchestration is absorbed by the model, control-plane investment is written off at the next release; if it is not, teams relying on the model will hit the multi-machine, identity, and scheduling walls that the infrastructure camp is already reporting.*

### When a long-running agent's context fills, should you compact it or reset and re-read written state?

| Position A | Position B |
|---|---|
| Compact. Compaction now works well enough that the old advice to start fresh threads is obsolete, and a compact at roughly 150,000 tokens is the standard move.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)* | Never compact. It is slow, you get no control over what survives, and what it drops is permanently gone; clear the context entirely and have the agent re-read its own handoff and history files.<br>*[I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)* |

*Why it matters: The answer determines whether an orchestrator needs to continuously write recovery artifacts to disk, or can treat its own conversation as durable memory — which in turn decides whether a crashed machine costs you a run or a boot command.*

## Practical Guidance

**Do:**

- Consolidate end-to-end judgment in exactly one agent; parallelize investigation via sub-agents but have them return results only
- Give each agent one job and one or two tools rather than a large tool inventory
- Lift deterministic components (statistical signal detection, SQL, CSV-to-PDF, rule checks) out of the agentic system and run them before the agent wakes up
- Put a blocking gate at the highest-cost handoff first — not the most technically complex one — and make it halt the pipeline rather than log a warning
- Keep fleet state in files on disk (handoff docs, history, per-machine dirs) so a context wipe or machine crash is recoverable via a single boot command
- Force delegation structurally: expose only CLI-dispatch skills so the orchestrator cannot do the work itself
- Run each parallel agent in an isolated cloud workspace or git worktree; local machines cannot support real parallelism
- Have a manager agent with different context judge worker output, since a coding agent evaluating its own PR is biased toward declaring success
- Require two independent sources to agree before proceeding unsupervised, and route low-confidence cases to human escalation by default
- For questions with no empirically correct answer, run independent analysts plus a consensus judge that weighs reasoning quality, and expand the jury when consensus is insufficient
- Have the model emit proposals that infrastructure validates, policy approves, and an execution gateway enforces — never let it touch production directly
- Trace the chain of decisions and state transitions, not just final outputs, because that is what you need to debug an autonomous workflow
- Keep shared fleet state changing only through pull requests, with machine-specific state in per-machine directories
- Run the control point on an always-on machine, not a laptop that sleeps
- Snapshot real tool responses as checked-in fixtures and run offline evals so you can quantify agent quality instead of relying on intuition

**Avoid:**

- Deriving your agent architecture by mimicking a human analyst's workflow steps — human process constraints are not system constraints
- Letting every subtask dump its full output into the primary thread, crowding out the context
- Sharing agents' reasoning across a collaborating group; pass the claim and evidence only, or they converge into groupthink
- Uncontrolled retries, which turn a minor API error into exponential resource growth and a compute incident
- Gates that only log warnings — a gate that cannot block the artifact is a suggestion
- Adding another agent when the actual missing piece is a boundary
- Installing many skills and MCP servers into one agent; the research shows it makes the agent substantially worse
- Filling a million-token context window because you can — accuracy degrades well before the hard limit
- Stacking many agent and MCP processes on one machine (memory exhaustion, swap, credentials binding to the wrong workspaces)
- Pointing two machines at the same shared context directory without separating machine-specific state — they diverge silently
- Assuming more parallel agents equals more capacity; human cognitive bandwidth does not parallelize and each loop adds routing, merging, and verification decisions
- Forcing a diagnostic agent into a deterministic graph workflow, which proved more brittle than the reasoning-and-acting paradigm
- Having agents infer entity and KPI relationships from raw tables — it does not scale and invents relationships that do not exist in the data

## Notable Outliers

- AI writes shared-state/blackboard-style agent code better than LLM-agent-style code, because decades of blackboard-architecture discussion sit in the training data while LLM agent patterns are only three years old. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [14:54](https://www.youtube.com/watch?v=khVX_BUnEwU&t=894s))
- Kubernetes already answers compute, secrets, tools, and scheduling for agent fleets, so the only layer worth building is orchestration, review flow, and context management. ([I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s))
- Frontier models now self-orchestrate — tell one to spawn additional models, split the work, and verify it afterward, and it just does, with no custom tooling or software factory. ([Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [2:28](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=148s))
- Domain-specific agents do not meaningfully exist in public today, and 2027 will be the year of multi-agent orchestration. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [21:55](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1315s))
- Many multi-agent failures blamed on reasoning are actually distributed-state consistency failures. ([Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:58](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=238s))
- A 39-agent production system was built with no framework, no fine-tuning, and no data scientists for roughly $30,000 against a $230,000 agency quote. ([The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [8:28](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=508s))

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
- [Richard Socher](../speakers/richard-socher.md)
- [Rob Cheung](../speakers/rob-cheung.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

