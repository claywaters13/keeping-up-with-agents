---
title: "task decomposition"
type: "concept"
slug: "task-decomposition"
tier: "supporting"
maturity: "consolidating"
talk_count: 15
speaker_count: 17
---

# task decomposition

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **15** talk(s) by **17** speaker(s)

**Definition:** Breaking a large goal into scoped, independently checkable units sized to what an agent can actually complete.

*Also referred to as: problem decomposition, hierarchical problem decomposition, prompt decomposition, pr decomposition, long-horizon task planning, agent chaining, multi-stage generation pipelines*

## State of Practice

Decomposition has moved from a prompting trick to a first-class architectural artifact: speakers describe writing the breakdown down (spec/design markdown, a research prototype taxonomy document, a linked hierarchy of component docs, a lesson state machine) before any agent runs. The economic argument is now the dominant one — once a task is cut into narrowly scoped units with defined inputs and output shapes, a much cheaper model clears the same bar, with Microsoft replacing Opus 4.7 with Haiku 4.5 behind a strong harness, Abridge post-training small models per clinical-note section, poolside using step-wise generation to beat what the teacher model produces one-shot, and OpenProse reporting a 9B model as an RLM beating frontier models run as plain LLMs. The failure mode everyone names is the opposite: one agent, one giant prompt, four jobs, resulting in drift, skipped steps, and loops that demos never surface. Sizing is driven by checkability rather than by effort — units are cut so that each one terminates in a decidable state (stop, retry, escalate), carries a structured output contract, and can be routed by consequence to code, to an agent, or to a human. The live arguments are about authorship (does a human write the decomposition up front or does the model choose it at runtime) and permanence (is this scaffolding or is it software engineering).

## Consensus

### Cutting work into narrow, scoped units lets a substantially smaller and cheaper model hit the quality bar that a monolithic task would require a frontier model for.

Support: **4** talk(s)

> "instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn't have as much reasoning capabilities, but because of the harnessing around it, it's still able to perform at the level in which we expect"
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)

### Overloading one agent or one prompt with multiple responsibilities is the primary cause of drift and unreliability; build many narrowly scoped agents instead.

Support: **4** talk(s)

> "That's four different jobs crammed into a single prompt. And then you wonder why your agent is drifting and not sticking to the script."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [5:13](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=313s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)

### Decomposition should be an explicit, separately produced written artifact — a spec, taxonomy document, or linked component hierarchy — that exists before execution begins rather than being implied by a single goal prompt.

Support: **4** talk(s)

> "First is to decompose the problem into its subcomponents but it's an explicit act um um action."
>
> — [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [6:56](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=416s)

Supporting talks: [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [Build Systems, Not Code](../talks/build-systems-not-code.md)

### Each decomposed unit needs an explicit completion contract — a defined output shape and a decidable terminal state — because a self-reported boolean 'done' hides distinct claims about what was actually achieved.

Support: **4** talk(s)

> "So, one of the best pieces of advice we have is that you stop treating done as a Boolean and treat it more like an object."
>
> — [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [4:49](https://www.youtube.com/watch?v=7P0elyLIxXo&t=289s)

Supporting talks: [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

### Units should be routed by consequence after decomposition: deterministic code for exact answers, agents for judgment, and human approval for irreversible or high-blast-radius steps.

Support: **5** talk(s)

> "Meaning, you do say, all right, four out of these eight steps will be handled completely autonomously. The other three will be handled with some human-in-the-loop intervention. And one step of that process will be handled by a human, period."
>
> — [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [6:30](https://www.youtube.com/watch?v=l0FLhNqBOic&t=390s)

Supporting talks: [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)

## Disagreements

### Who should choose the decomposition — a human-authored workflow fixed before the run, or the model itself at runtime?

| Position A | Position B |
|---|---|
| The decomposition is engineered outside the model: a state machine, spec document, or workflow defines the path, the harness advances state and decides what comes next, and the model only proposes within a step. Letting a coding agent design the breakdown yields something that works but is unmaintainable.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)* | The model picking its own decomposition into sub-calls is the defining property of the architecture; a hardcoded map-reduce pipeline does not qualify. Agents are better than humans at splitting large changes into atomic reviewable units, and a coding agent asked to emit a linked document hierarchy widens the space of solutions it will then propose.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)* |

*Why it matters: It decides whether you invest in workflow state machines and spec pipelines or in recursive scaffolds and sub-agent primitives, and it determines whether the plan is auditable before execution or only reconstructable after it.*

### Is explicit decomposition scaffolding a durable engineering layer or a transitional crutch that better-post-trained models will make unnecessary?

| Position A | Position B |
|---|---|
| It is a temporary trick, directly analogous to chain-of-thought prompting on GPT-4-era models; as models are post-trained to compartmentalize and break down problems themselves, less and less of this scaffolding will be needed.<br>*[Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)* | Intelligence is not the constraint and will not become one — the missing layer is orchestration, specification, and reuse. Designing these systems is software engineering with different primitives, and rising capability relocates where proof is required rather than removing the requirement.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)* |

*Why it matters: If it is a crutch, orchestration infrastructure is depreciating and should be kept thin; if it is engineering, the workflow layer is the durable asset and deserves the same investment as the codebase.*

### Can a decomposed unit's completion be checked by another model, or does it require human-authored ground truth?

| Position A | Position B |
|---|---|
| Cross-model verification is sufficient and should be standard: separate the verifier from the author by using a different model, gate high-stakes actions on agreement between models, and never let the agent that wrote the code also grade its own tests.<br>*[What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)* | No LLM verifier can serve as ground truth in high-stakes verticals — a verifier good enough to grade would be the better generator, LLM-as-judge produces plausible jargon without understanding, and rubrics-as-rewards creates an echo chamber. Checkability must come from domain-expert-authored rubrics and expert judgment in the loop.<br>*[From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)* |

*Why it matters: It sets the ceiling on how finely you can decompose before verification becomes the bottleneck: automated checking scales to hundreds of units, expert rubrics cap you at what clinicians or traders can author and review.*

## Practical Guidance

**Do:**

- Make decomposition a separate explicit action that produces a durable artifact — linked component documents, a spec plus design markdown, or a research prototype taxonomy document — before any implementation step runs.
- Hold multi-step state in the harness, not the model: model the task as a small state machine (e.g. intro, teach, check, grade, advance, wrap) where the harness validates each returned step and decides the next one.
- Give every unit exactly one of three terminal outcomes — stop, retry, or escalate — so a run can never silently end in an undefined state.
- Define the output shape of each unit as a structured contract whenever another system consumes it; free-form text is acceptable only when a human is the sole reader.
- Send any unit with an exact answer (deduplication, arithmetic, lookups) to plain code, and reserve agents for units that genuinely need interpretation or judgment.
- Wall high-consequence units — emailing counterparties, booking, submitting offers, money movement, permissions, irreversible data changes — behind explicit human approval to bound blast radius.
- Post-train or select a smaller model per unit once the units are narrow: per-section clinical-note models and Haiku-class models behind a strong harness hit the same quality bar at lower cost and latency.
- Use a different model to verify than the one that authored the work, and give the verifier real tools (browser harnesses, screenshots, state diffs) instead of asking the agent whether it is done.
- Cap review units at a size a human can actually inspect — 500-line PRs, stacked diffs sliced so each slice can go to the right subject-matter expert asynchronously.
- Enforce idempotency at the system level so a retried unit does not get reworded into what looks like a new task.
- When decomposing an existing human process, keep roughly the original step structure and mark each step autonomous / human-in-the-loop / human-only, since collapsing an 11-step workflow to one step damages adoption.
- Break generation into ordered sub-steps (outline, then chapters one by one) when the whole task is too hard for the model in one shot — this exceeds what the model produces one-shot rather than merely matching it.

**Avoid:**

- Fixing multi-step unreliability by adding more prompt rules — when reliability approaches a coin flip, the problem is control flow, not prompting.
- Cramming multiple jobs into one giant prompt; it is the agentic equivalent of a god class and is the direct cause of agent drift.
- Letting your coding agent design your agent system for you — it produces something that technically works, typically one giant prompt with poor separation of concerns, and is not maintainable.
- Handing an agent a goal with no path (the 'here's the codebase, here's the objective, optimize' prompt) — it saturates, proposing hyperparameter tweaks rather than the radical restructurings the problem needs.
- Modularizing everything: some instructions are local to one workflow and abstracting them costs more than it saves.
- Letting the same agent both produce the work and grade it — that hides the review rather than removing it.
- Collapsing mergeable, deployable, and announceable into a single green checkmark on a completed unit.
- Relying on exhaustive human sign-off for every unit at high task volume; it degenerates into verification theater.
- Running fully live with no approvals at any step, which produces AI slop that is worse than producing nothing.
- Treating a for-loop over a task manager as an orchestrator once dependency trees, blockers, and multiple agents are involved — the control plane must enforce blockers and bound infinite loops.
- Starting to iterate on vertical output before a domain expert is in the loop to scope queries, curate sources, and decompose the problem, because engineers cannot tell whether the output is good.

## Notable Outliers

- A system only qualifies as an RLM if the model itself picks the decomposition into sub-calls; hardcoded map-reduce pipelines do not count, and coding agents are not automatically RLMs. ([Recursive Coding Agents](../talks/recursive-coding-agents.md), [9:59](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=599s))
- Hierarchical decomposition prompting is the chain-of-thought of this era — a temporary scaffold that newer models post-trained to break down problems will need less and less. ([Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [18:24](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=1104s))
- Decomposing generation into simpler steps lets you exceed what the teacher model could produce in one shot, avoiding the correctness and diversity collapse that happens when a task is too hard for the model. ([The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [5:58](https://www.youtube.com/watch?v=KhYifX22yhE&t=358s))
- Preserve enough of the original step structure when redesigning a workflow around agents, even at a cost to efficiency — replacing an 11-step process with a one-step one tanks adoption. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [5:53](https://www.youtube.com/watch?v=l0FLhNqBOic&t=353s))
- Not everything should be modularized; some instructions are local to a workflow and abstracting them costs more than it saves. ([Build Systems, Not Code](../talks/build-systems-not-code.md), [8:58](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=538s))
- Treating done as a structured object rather than a boolean is claimed to yield roughly 100x more work completed. ([What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [5:25](https://www.youtube.com/watch?v=7P0elyLIxXo&t=325s))
- Agents are better than humans at decomposing large changes into atomic reviewable PRs and should be explicitly asked to do it. ([Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [15:00](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=900s))

## All Talks

- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)
- [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)
- [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)
- [Trading Desks to Clinical Trials: Parallels in Applied Vertical AI](../talks/trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai.md)
- [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)
- [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)

## Speakers

- [Alex Volkov](../speakers/alex-volkov.md)
- [Angie Jones](../speakers/angie-jones.md)
- [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)
- [Chaitanya Asawa](../speakers/chaitanya-asawa.md)
- [Dan Feng](../speakers/dan-feng.md)
- [Deepak Pathak](../speakers/deepak-pathak.md)
- [Dotta](../speakers/dotta.md)
- [Erik Hanchett](../speakers/erik-hanchett.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Kushan Raj](../speakers/kushan-raj.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Marah Abdin](../speakers/marah-abdin.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Robert McHardy](../speakers/robert-mchardy.md)
- [Sajjan Kanukolanu](../speakers/sajjan-kanukolanu.md)
- [Sina Shahandeh](../speakers/sina-shahandeh.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)

