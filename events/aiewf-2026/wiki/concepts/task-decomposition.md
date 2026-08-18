---
title: "task decomposition"
type: "concept"
slug: "task-decomposition"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 14
---

# task decomposition

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **14** speaker(s)

**Definition:** Breaking a large goal into scoped, independently checkable units sized to what an agent can actually complete.

*Also referred to as: problem decomposition, hierarchical problem decomposition, prompt decomposition, pr decomposition, long-horizon task planning, agent chaining, multi-stage generation pipelines*

## State of Practice

The field has moved from arguing about whether agents need decomposition to arguing about who performs it and how each resulting unit gets closed out. Speakers across coding, browser, scientific, GTM, and enterprise-process work converged on the same diagnosis: model intelligence is no longer the binding constraint, so the missing layer is specifying, scoping, and verifying units of work — Robinson's "mismanaged geniuses," Raj's "the infra around them that sucks," Bahidika/Allou's "reliability was never a prompting problem. It's a control problem." The concrete techniques on offer are unusually specific: model a workflow as a named state machine the harness advances (intro/teach/check/grade/advance/wrap), make decomposition an explicit action that emits a linked hierarchy of component documents rather than an implicit step inside one prompt, write spec and design markdown that a human hand-edits before any code is generated, use stacked diffs to slice a proven prototype into per-domain reviewable PRs, and assign each step an execution mode — fully autonomous, human-in-the-loop, or human-only. A second, harder consensus is that a decomposed unit is worthless without a completion contract: Dotta's argument that "done" is a bundle of distinct operational claims (mergeable, deployable, announceable) flattened into one green checkmark, and Volkov's rule that the builder must not grade itself, are the same point from opposite ends of the stack. The live fights are about ownership — Robinson insists a system only counts as an RLM if the model itself picks the decomposition, while Bahidika/Allou insist the model must never hold workflow state — and about durability, with Shahandeh calling hierarchical decomposition prompting a temporary chain-of-thought-style scaffold that post-training will absorb, against a majority who treat it as permanent software-engineering discipline.

## Consensus

### A goal alone is not a usable instruction to an agent; decomposition must be an explicit artifact (path, state machine, spec document, component hierarchy) produced before execution, not left implicit inside a single large prompt.

Support: **6** talk(s)

> "As much as we all love the slash goal command, an agent needs more than a goal, it needs a path."
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [3:08](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=188s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)

### The constraint on long-horizon agent work is orchestration and scaffolding, not model intelligence — better decomposition, not a smarter model, is what raises task completion.

Support: **5** talk(s)

> "today's agents are mismanaged geniuses. The intelligence is there, and the missing layer is how do we specify and manage and reuse and verify the work."
>
> — [Recursive Coding Agents](../talks/recursive-coding-agents.md), [1:38](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=98s)

Supporting talks: [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)

### Each decomposed unit needs an explicit, structured completion contract — a defined output shape and terminal conditions — because a boolean 'done' collapses distinct claims (correct, mergeable, deployable, announceable) that the system needs to distinguish.

Support: **5** talk(s)

> "So, one of the best pieces of advice we have is that you stop treating done as a Boolean and treat it more like an object."
>
> — [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [4:49](https://www.youtube.com/watch?v=7P0elyLIxXo&t=289s)

Supporting talks: [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

### The component that verifies a completed unit must be separate from the one that produced it; an agent grading its own work hides review rather than eliminating it.

Support: **4** talk(s)

> "You definitely want to separate the verifier from the author. Often, this means you're using a different model. So, if you're coding using Claude, have Codex verify."
>
> — [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [5:59](https://www.youtube.com/watch?v=7P0elyLIxXo&t=359s)

Supporting talks: [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Build Systems, Not Code](../talks/build-systems-not-code.md)

### Units should be scoped to a single responsibility — one job per subagent, prompt, microservice, or PR — because multi-job units are the direct cause of drift and unreviewable output.

Support: **4** talk(s)

> "Architecturally, they're sort of like functions, right? So, you give them one specific task to do. You call them when it needs to be done. And they can do it really well because that's all that they have in scope, right?"
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [8:15](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=495s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)

### Once work is decomposed into narrowly scoped steps, a smaller and cheaper model driven by a strong harness matches or beats a frontier model running the task end to end.

Support: **4** talk(s)

> "instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn't have as much reasoning capabilities, but because of the harnessing around it, it's still able to perform at the level in which we expect"
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)

## Disagreements

### Should the model choose how a task is decomposed, or should the decomposition be fixed in advance by a harness or a human?

| Position A | Position B |
|---|---|
| The model must pick the decomposition at runtime — that dynamic choice is what makes a system agent-native, and agents are in fact better than humans at slicing a large change into atomic units. Robinson goes so far as to disqualify hardcoded map-reduce pipelines from counting as RLMs at all.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)* | The decomposition is authored outside the model and the model only fills in leaf steps: the harness holds workflow state and decides what comes next, the workflow defines the path, research teams write a taxonomy document before engineers touch the project, and generated spec/design docs are hand-edited by the developer before implementation.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)* |

*Why it matters: It determines where reliability engineering goes: side A invests in prompting, sub-agent wiring, and test-time compute so the model can search a wider space of plans; side B invests in state machines, structured contracts, and review gates and accepts a narrower plan space in exchange for reproducibility. It also changes which model you can afford — a model that must plan cannot be Haiku.*

### Does every decomposed unit require a human sign-off, or should verification itself be delegated to agents?

| Position A | Position B |
|---|---|
| A human is accountable for each unit and must personally review it. Hanchett: you must be the code reviewer of all generated code and of the spec documents; Jones walls high-consequence actions (emailing sellers, submitting offers) behind explicit approval and reserves authority for humans; Volkov calls merging with no review at all — human or agentic — unacceptable and demands line-by-line reading for auth, money, permissions, and irreversible data.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)* | Human review of every unit does not scale and degenerates into verification theater; the control plane should route units to agent verifiers with evidence-producing tools (browser harnesses, screenshots, hooks) and reserve human attention for units the rubric flags, letting productive work continue in the meantime.<br>*[What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)* |

*Why it matters: This sets the ceiling on throughput: if every unit needs a human, decomposition into more units makes the human the bottleneck faster, so you decompose coarsely; if agents can verify, you decompose finely and invest in evidence tooling and rubrics instead of reviewer headcount.*

### Is explicit decomposition scaffolding a permanent architectural layer or a temporary crutch that post-training will absorb?

| Position A | Position B |
|---|---|
| It is temporary. Shahandeh frames hierarchical decomposition prompting as directly analogous to chain-of-thought on GPT-4-era models — a trick that newer models post-trained to compartmentalize problems will need less and less.<br>*[Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)* | It is permanent engineering discipline. Hanchett states that better frontier models and built-in planning modes have not removed the need for human-reviewed spec documents; Volkov argues rising capability relocates where proof is required but never removes the requirement; Jones treats agentic decomposition as ordinary software architecture with different primitives.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)* |

*Why it matters: It decides whether to build durable decomposition infrastructure — state machines, spec pipelines, control planes — or to treat today's scaffolding as throwaway tooling you will delete at the next model release.*

### When you decompose, which steps deserve the strongest available model?

| Position A | Position B |
|---|---|
| Decomposition is what lets you downgrade: with good structure and a good environment representation, a cheap model outperforms a frontier one. Raj beats screenshot-driven Claude with a compressed-markdown representation and a cheaper model; Robinson reports Qwen 3.5 9B as an RLM beating Opus and GPT-5.4 as plain LLMs; Moza reports post-trained open-source models beating frontier models at writing normalized process flows.<br>*[Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)* | The decomposition and critique steps are exactly where you spend on the strongest model — Shahandeh routes hypothesis generation and post-implementation critique to GPT-5.x Pro via Oracle CLI and reports much better improvements, and calls in a stronger multimodal model to review images as part of the metric.<br>*[Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)* |

*Why it matters: It changes the cost model of a decomposed pipeline: uniformly cheap leaf execution versus a barbell where planning and verification calls are expensive and only execution is cheap.*

## Practical Guidance

**Do:**

- Make decomposition a separate, explicit action that emits a linked hierarchy of component documents over the codebase, then have the reasoning model propose improvements against each component.
- Model multi-step workflows as a named state machine (e.g. intro, teach, check, grade, advance, wrap) and have the harness — not the model — validate returns, advance state, and decide what is next.
- Give every run exactly three terminal outcomes: stop, retry, or escalate.
- Label each step of an existing human process with its execution mode — fully autonomous, human-in-the-loop, or human-only — rather than replacing the whole process at once.
- Send exact-answer subtasks (deduplication, commute calculation) to plain code, judgment subtasks to agents, and authority to humans.
- Define the output shape of each unit as a structured contract whenever another system consumes it; reserve free-form text for units a human is the sole reader of.
- Model 'done' as an object with artifact, scope, rubric, evidence, verifier, approver, residual risk, and next action.
- Have a different model verify than the one that authored, and give the verifier real evidence tools (browser harness, screenshots, custom hooks) instead of asking it whether it is done.
- Ask the agent to split a large change into atomic reviewable PRs, and use stacked diffs so domain specialists can review slices asynchronously.
- For generation tasks, split into outline-then-chapters rather than one shot — the decomposed pipeline exceeds what the teacher model produces in a single pass.
- Write the spec and design markdown before code, then hand-edit them with your own knowledge and taste before implementation begins.
- Enforce blockers and dependencies in the control plane as first-class objects, with watchdog agents that keep work moving until the goal is met and bound infinite loops.
- Enforce idempotency at the system level so a retried unit is not treated as a new task.
- Read every line of authentication, money movement, permissions, and irreversible data changes regardless of how the work was sliced.

**Avoid:**

- Cramming four jobs into a single prompt — this is the agentic equivalent of a god class and the direct cause of drift.
- Letting your coding agent design your other agents; it produces something that technically works but is not maintainable.
- Letting the model hold or report workflow state — it is terrible at remembering whether it is on step three of six.
- The 'here's the codebase, here's the objective, optimize' prompt: it produces hyperparameter tweaks rather than radical changes and saturates after a while.
- Writing a plain for-loop over a task manager and expecting it to survive dependency trees, blockers, multiple agents, and idempotent checkouts.
- Collapsing an 11-step human workflow into one step — adoption suffers even when the efficiency win is real.
- Over-modularizing: instructions local to one workflow cost more to abstract than they save.
- Overstuffing agents.md or steering files; there is a Goldilocks amount of context and too much is harmful.
- Running the spec/decomposition workflow on small changes and quick fixes where it does not pay for itself.
- Merging PRs with no review at all, human or agentic — up 31% per the Faros AI survey, alongside 242% more incidents per PR.
- Letting the builder grade itself — that hides the review rather than removing it.
- Running units fully live with no approvals at all, which produces slop that is worse than producing nothing.

## Notable Outliers

- A system only qualifies as an RLM if the model itself picks the decomposition — hardcoded map-reduce pipelines like lambda RLM do not count, because runtime choice of decomposition is the agent-native element. ([Recursive Coding Agents](../talks/recursive-coding-agents.md), [9:59](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=599s))
- Hierarchical decomposition prompting is a temporary scaffold analogous to chain-of-thought on GPT-4-era models, and will be needed less as models are post-trained to break down problems themselves. ([Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [18:24](https://www.youtube.com/watch?v=XLEYtv3cMlw&t=1104s))
- Preserve the original step structure of a human workflow even at a cost to efficiency — replacing an 11-step process with a one-step one takes operators aback and hurts adoption. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [5:53](https://www.youtube.com/watch?v=l0FLhNqBOic&t=353s))
- If a task is too hard for the model it loses both correctness and diversity, so decomposing into simpler steps lets the pipeline exceed what the teacher model could produce in one shot. ([The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md), [5:58](https://www.youtube.com/watch?v=KhYifX22yhE&t=358s))
- Not everything should be modularized — some instructions are local to a workflow and abstracting them costs more than it saves. ([Build Systems, Not Code](../talks/build-systems-not-code.md), [8:58](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=538s))
- A one-to-one researcher-to-microservice ratio with fully decoupled services is the right decomposition unit for productionizing research, because it lets each initiative iterate independently. ([Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [7:06](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=426s))
- Treating done as a structured object rather than a boolean can yield roughly 100x more work completed. ([What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [5:25](https://www.youtube.com/watch?v=7P0elyLIxXo&t=325s))
- Inability to reliably estimate delivery dates for decomposed research work points upstream to research coordination or the codebase, not to the decomposition step itself. ([Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [14:09](https://www.youtube.com/watch?v=OXMMN-XbxwA&t=849s))

## All Talks

- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)
- [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)
- [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)
- [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)

## Speakers

- [Alex Volkov](../speakers/alex-volkov.md)
- [Angie Jones](../speakers/angie-jones.md)
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

