---
title: "sub-agent delegation"
type: "concept"
slug: "sub-agent-delegation"
tier: "core"
maturity: "contested"
talk_count: 15
speaker_count: 20
---

# sub-agent delegation

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **15** talk(s) by **20** speaker(s)

**Definition:** A parent agent spawning scoped child agents to isolate context and specialize work, then folding their results back into its own trajectory.

*Also referred to as: sub-agent orchestration, subagent spawning, subagent specialization, parallel subagents, sub-agent context quarantine, agentic delegation, single-responsibility agents*

## State of Practice

Delegation is now treated primarily as a context-management technique rather than a capability-scaling one: you spawn a child agent to keep tokens and unrelated concepts out of the parent's window, not because the child is smarter. The mechanics have largely converged — each sub-agent gets one job and a small tool set, its own scoped context slice, and returns a compressed result rather than dumping its transcript into the primary thread; Codex enforces this at the harness level (read-only subagents that cannot spawn further subagents, skills capped at 2% of the context window, deferred tools behind tool search). What remains genuinely unsettled is how much of the *reasoning* may be split. ZS Associates killed a four-stage analyst-mimicking pipeline after finding that no single agent held the end-to-end picture and that every handoff shed context, while Cognition reports not using sub-agents at all, preferring one long-lived 'sidekick' with a running context because cached tokens are ~10x cheaper than re-priming fresh children. Pinterest moved in the opposite direction — from one monolithic ReAct prompt to a supervisor plus specialist agents — for exactly the control that ZS gave up. The emerging synthesis is 'distribute investigation, centralize judgment': parallelize evidence gathering, keep planning and adjudication in one place, and treat any child agent that escapes the parent's permission, flag, and kill-switch middleware as an architectural defect.

## Consensus

### Sub-agents should return only compressed results or findings to the parent, never their full transcript or intermediate reasoning; letting subtask output flow into the primary thread is an anti-pattern.

Support: **4** talk(s)

> "That you can still delegate to a sub-agent. You can get back the uh results back, not the reasoning or the judgment."
>
> — [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [8:30](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=510s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### Context isolation — not added intelligence — is the reason to delegate; oversized context degrades answer accuracy, so each agent should see only its own slice.

Support: **6** talk(s)

> "don't let your agents context spill over into the main context because context means tokens, tokens mean money, and the more context you have, the more confused the LLM is going to be in giving you an answer"
>
> — [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [13:02](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=782s)

Supporting talks: [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)

### One monolithic prompt attempting several jobs performs measurably worse than several narrowly scoped agents each given a single job and one or two tools.

Support: **4** talk(s)

> "Prompt tuning became unsustainable. One prompt had to do everything, and adding detail in one area degraded the behavior in another."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [2:26](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=146s)

Supporting talks: [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Build Systems, Not Code](../talks/build-systems-not-code.md)

### A spawned child agent must inherit the parent's controls — the same flag/kill-switch middleware, an explicit approval boundary, and a restricted tool/permission set (read-only by default).

Support: **5** talk(s)

> "Sub agents must go through the same middleware. The biggest failure mode I see is a parent agent with flags properly applied that spawns a child agent."
>
> — [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [13:07](https://www.youtube.com/watch?v=zU4EagB311U&t=787s)

Supporting talks: [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### Execution should be delegated but judgment should not: one agent (or the strongest model) retains planning and final adjudication while children do bounded investigation or implementation.

Support: **3** talk(s)

> "we're reducing the cost of Fable level intelligence by 40%. The way we do that is we allow Fable to still do like the planning and the the hard decision making but delegate a lot of the work to an implementation model."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [4:32](https://www.youtube.com/watch?v=QHBjufYK8TA&t=272s)

Supporting talks: [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)

## Disagreements

### Does splitting a complex task across multiple specialized agents improve or destroy the quality of the result?

| Position A | Position B |
|---|---|
| Decompose: a team of narrowly scoped agents gives more control over system behavior and lets you expand scope by adding a prompt, whereas a single agent hits a prompt-tuning ceiling.<br>*[Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Build Systems, Not Code](../talks/build-systems-not-code.md)* | Consolidate: every agent-to-agent handoff loses context and the loss compounds, so exactly one agent must own end-to-end reasoning — ZS deleted its four-stage pipeline, and Cognition replaced sub-agents entirely with a single long-lived sidekick.<br>*[Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)* |

*Why it matters: The two camps are running the same migration in opposite directions — Pinterest went single-agent to multi-agent for controllability, ZS went multi-agent to single-agent for coherence — so the choice determines whether your reliability work goes into handoff contracts or into keeping one context coherent for 50+ turns.*

### Should the delegation topology be designed by the engineer up front, or chosen by the model at runtime?

| Position A | Position B |
|---|---|
| The engineer specifies it: hierarchies should be real entity types with scoped context and approval boundaries, workflows must define the path with explicit stop/retry/escalate terminals, and you should not let a coding agent design your agent system.<br>*[I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)* | The model picks it: a system only counts as recursive if the model itself chooses the decomposition, Mythos will spawn models, split work, and verify it if simply asked, and agent roles should emerge from position relative to other agents rather than being assigned.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)* |

*Why it matters: If topology is engineered, your investment goes into workflow definitions, entity types, and control planes that stay auditable; if it emerges, that scaffolding is obsolete within a model generation and the engineering work shifts to designing constraints and selection pressure instead.*

### Is it cheaper to spawn fresh scoped sub-agents per task or to keep one long-lived delegate with a persistent context?

| Position A | Position B |
|---|---|
| Fresh per-task children: every agent gets its own slice, the parent stays clean, and expanding scope means adding another scoped agent.<br>*[Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)* | One persistent sidekick: re-providing earlier context to each new child forces cache misses, and cached tokens are roughly 10x cheaper, so a single delegate with a running context wins on cost.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md)* |

*Why it matters: KV-cache economics can dominate the token bill of a delegating system; a fan-out architecture that looks context-efficient per agent can be an order of magnitude more expensive in input tokens than a single warm delegate.*

### Should a sub-agent be allowed to spawn its own sub-agents?

| Position A | Position B |
|---|---|
| No — depth must be capped in the harness. Codex's subagent runs entirely separate, has read permissions only, and cannot spin up further subagents; unbounded child spawning is exactly the failure mode kill switches exist to catch (a four-agent pipeline with two agents looping cost $47,000).<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)* | Yes — recursion is the point. An RLM is defined by the model decomposing problems into sub-calls or sub-agents at arbitrary depth, and Mythos spawning and verifying its own workers is the headline capability jump.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* |

*Why it matters: Recursion depth sets your worst-case blast radius and cost ceiling: unbounded spawning is what turns a bad prompt into a runaway loop, but capping depth forecloses the RLM-style processing of inputs far larger than the context window.*

## Practical Guidance

**Do:**

- Define the sub-agent return contract as findings only — claim plus evidence, or a summary — and have the child summarize before returning to the parent
- Give each sub-agent a single job and one or two tools rather than a shared tool inventory
- Route every child spawn through the same flag/kill-switch middleware as the parent, and resolve flags per turn so an in-flight sub-agent honors a flip at its next decision point
- Default child agents to read-only permissions and their own explicit approval boundary; lock tool arguments by partial application so the model cannot widen scope and no per-action human prompt is needed
- Keep one agent owning end-to-end judgment; parallelize investigation across children but not adjudication
- Budget the delegation surface against the context window explicitly — cap the available-skills list at ~2% of max context and mark rarely-used tools deferred behind tool search
- Keep working context under ~200K tokens and ideally under 100K regardless of the advertised window
- Persist each agent's state in files on disk so you can clear context and re-read handoff files instead of compacting
- Make dispatch the only available path in the orchestrator's harness (CLI plus skills that call it), because an orchestrator with the ability to do the work itself will do the work itself
- Pull deterministic steps — signal detection over metrics, deduplication, anything with an exact answer — out of the agent graph and run them before the agent is invoked
- Constrain what a sub-agent may investigate with an explicit control plane (e.g. a knowledge graph where every edge is a hypothesis it may evaluate)
- Give parallel agents only the claim and evidence, not the reasoning that produced them, to keep them from converging on one idea
- Snapshot real tool responses as checked-in fixtures and run offline evals so multi-agent regressions are detectable

**Avoid:**

- Sub-agents that bypass the parent's flag middleware — a flipped kill switch never reaches them
- Letting every subtask dump its full output into the primary thread
- Distributing judgment across a chain of specialized agents; each handoff loses context and the loss compounds
- Copying a human analyst's workflow steps or an org chart as your agent architecture
- One prompt doing four jobs — the agentic equivalent of a god class, and the cause of drift
- Unbounded or continuously looping agent pipelines with no spend ceiling (a four-agent researcher/analyzer/verifier/synthesizer pipeline with two looping agents cost $47,000)
- Filling a million-token window because it exists
- Using context compaction as the default recovery mechanism — it is slow, you cannot choose what survives, and it forces a cache miss that raises input token cost
- Letting a coding agent design your other agents; it produces something that works but is unmaintainable
- Routing sub-agent work by task type alone — extremely fragile once complexity shifts mid-session
- Stacking many agent and MCP processes on one laptop, or using a machine that sleeps as the fleet's control point
- Having agents infer entity and KPI relationships from raw tables — it does not scale and invents relationships not in the data

## Notable Outliers

- Cognition does not use sub-agents at all — one 'sidekick' with a continuously running context so the main agent never re-provides earlier context, because cached tokens are ~10x cheaper. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [18:04](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1084s))
- A four-agent pipeline (researcher, analyzer, verifier, synthesizer) with two agents in a continuous loop cost $47,000. ([Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [2:25](https://www.youtube.com/watch?v=zU4EagB311U&t=145s))
- Sub-agents should receive only the claim and evidence, never the reasoning behind them, because collaborating agents otherwise devolve into groupthink around a single idea. ([Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [13:52](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=832s))
- An orchestrator will do the work itself rather than delegate unless the harness makes dispatching the only path it can take. ([I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [4:29](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=269s))
- An infra team of agents inside the fleet built the review gateway that governs the fleet — agents building the tools that run the agents. ([I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [3:48](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=228s))
- Agent identity, role, and specialization should not be assigned by the engineer at all — they should arise from an agent's position relative to other agents and environmental pressure. ([Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [23:57](https://www.youtube.com/watch?v=qdZzND79mcg&t=1437s))
- Modeling a sub-agent as an ordinary function you call like any other tool is better than frameworks that make sub-agents a distinct first-class concept. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [22:13](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1333s))
- On terminal bench, Opus scores ~3x better than Haiku at 1/10 the total cost despite being far more expensive per token — cheap models delegated out-of-distribution work can raise total cost through tool-call churn. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [15:25](https://www.youtube.com/watch?v=QHBjufYK8TA&t=925s))

## All Talks

- [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)
- [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [The State of Model Routing](../talks/the-state-of-model-routing.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [Why We Killed Our Multi-Agent Pipeline](../talks/why-we-killed-our-multi-agent-pipeline.md)

## Speakers

- [Abhilash Asokan](../speakers/abhilash-asokan.md)
- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Alex Atallah](../speakers/alex-atallah.md)
- [Angie Jones](../speakers/angie-jones.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Benjamin Guo](../speakers/benjamin-guo.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Drasko Profirovic](../speakers/drasko-profirovic.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Kyle Jaejun Lee](../speakers/kyle-jaejun-lee.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Rajiv Chandegra](../speakers/rajiv-chandegra.md)
- [Rob Cheung](../speakers/rob-cheung.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Walden Yan](../speakers/walden-yan.md)

