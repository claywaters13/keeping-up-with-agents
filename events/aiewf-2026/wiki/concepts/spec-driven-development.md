---
title: "spec-driven development"
type: "concept"
slug: "spec-driven-development"
tier: "core"
maturity: "consolidating"
talk_count: 15
speaker_count: 15
---

# spec-driven development

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **15** talk(s) by **15** speaker(s)

**Definition:** Writing an explicit specification as the durable artifact that agents implement against, making the spec rather than the code the primary human authored input.

*Also referred to as: specification-driven development, document-driven development, ai-assisted specification, spec generation from unstructured requests, acceptance criteria, design specification checking, commander's intent prompting*

## State of Practice

Across this conference the spec has clearly displaced code as the primary human-authored artifact: speakers from MongoDB, Ramp, Maven Clinic, GitHub and VisualLabs all independently reported that implementation is now cheap (frontier models one-shot medium features from a well-shaped spec) and that requirements, system design, and eval criteria are where the remaining human work lives. The practical form is converging on version-controlled markdown in the repo — requirements, design, and task documents plus a small model-agnostic architecture file — rather than chat transcripts or plan-mode output, because chat is isolated, ephemeral, and non-shareable. Two hard constraints recur: the spec must be bounded (one-to-two-page PRDs; an architecture.md containing only invariants stable for months or years) because oversized steering files degrade output, and it must be paired with a machine-checkable termination gate (golden datasets, binary pass/fail evals, property-based tests generated from the requirements doc, sustained ~90% pass rates over repeated runs) because a spec with no verifiable exit condition cannot drive an agent loop. The open frontier is altitude and authorship: whether the durable artifact should sit at product-behavior level or engineering-decision level, whether agents may write and revise the spec themselves or only implement against it, and how to bridge the gap from an abstract spec to a correct concrete implementation for anything concurrent or distributed. Nobody at this conference argued for going back to code-first; the arguments are about the shape and ownership of the document.

## Consensus

### Writing the spec — requirements, system design, eval criteria — is now the expensive and hard part of engineering; implementation is the cheap part.

Support: **7** talk(s)

> "Specs are the new code. The art is in defining the product requirements, the system design, and evaluate criteria so you can be confident that your AI coding buddies are building the right thing."
>
> — [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [1:27](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=87s)

Supporting talks: [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

### The spec must be a durable, version-controlled document in the repository (markdown), not a chat session or plan-mode message.

Support: **6** talk(s)

> "just make sure that you track all of these in a good old markdown file in your repository so that AI can access it."
>
> — [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [8:35](https://www.youtube.com/watch?v=6bmM45jkMDY&t=515s)

Supporting talks: [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)

### Turning an agent loose on a vague or generic goal fails; you must define structure and scaffolding first, and never let the agent pick the architecture.

Support: **5** talk(s)

> "So, the step here was define the structure first, and then turn Claude loose. Don't try and YOLO it from the beginning."
>
> — [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [10:59](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=659s)

Supporting talks: [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)

### A spec is only operational when paired with an explicit machine-checkable termination gate — evals, golden datasets, or tests derived from the spec itself.

Support: **6** talk(s)

> "after you build for agents, you essentially go into the eval-driven development loop, which I would call. And this is kind of equivalent to test-driven development for building software with agents because then the agents needs uh termination condition, right?"
>
> — [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [11:26](https://www.youtube.com/watch?v=pSto5YaNGUo&t=686s)

Supporting talks: [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Agents Building Agents](../talks/agents-building-agents.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Perception Agents](../talks/perception-agents.md)

### Spec artifacts must be small and tool/model-agnostic — bounded context, no vendor-specific filenames, no framework assumptions — because oversized or harness-coupled specs degrade output and expire quickly.

Support: **4** talk(s)

> "This file has to be incredibly small, and it can only have things that will not change for months or for years."
>
> — [fighting slop with slop](../talks/fighting-slop-with-slop.md), [2:03](https://www.youtube.com/watch?v=AMiyLItEtLA&t=123s)

Supporting talks: [fighting slop with slop](../talks/fighting-slop-with-slop.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)

### Generated spec and design documents must be hand-edited and owned by a human before implementation begins; accountability does not transfer to the agent.

Support: **5** talk(s)

> "Now, this is at the point I would highly recommend, if you're trying this at home, to stop and go in and update it with your knowledge and expertise and taste to exactly what you're looking for. Because it's only as good as what you put in."
>
> — [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [11:34](https://www.youtube.com/watch?v=IddXPepIAS4&t=694s)

Supporting talks: [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md), [Agents Building Agents](../talks/agents-building-agents.md)

## Disagreements

### May agents author and revise the spec layer themselves, or must the spec remain human-authored with a human gate before anything ships?

| Position A | Position B |
|---|---|
| Agents should be moved upstream into design and allowed to optimize their own specs, prompts, and tools; if the optimized variant hits its eval targets it can ship to production automatically with no human review.<br>*[The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [Agents Building Agents](../talks/agents-building-agents.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)* | Humans must write or personally rewrite the spec and remain the accountable reviewer; asking the model to improve its own instructions yields micromanagement, and taste and judgment over the final output stay with the person.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* |

*Why it matters: This decides whether spec-driven development is a human authoring discipline or a closed autonomous loop, and therefore whether your throughput ceiling is human review bandwidth or eval coverage. Get it wrong in the autonomous direction without airtight scorers and the agent optimizes the gate instead of the product.*

### How much specification should be written up front — a full requirements-plus-design package before any code, or a thin one-to-two-page artifact iterated continuously alongside the agent?

| Position A | Position B |
|---|---|
| Think deeply and produce the full requirements, design, and eval-criteria documents before the model generates any code; upfront analysis (story mapping, value/architecture/design sequencing) is the differentiator.<br>*[AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)* | Cap PRDs/TDDs at one or two pages as communication artifacts, plan concretely only two to four weeks out, and iterate direction with the agent as it works — discovering two weeks in that a decision was wrong is cheap now, and planning isn't a phase that precedes building.<br>*[How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md)* |

*Why it matters: It sets where the spec workflow pays off versus where it becomes ceremony, and how teams plan: a heavy-upfront shop budgets weeks of analysis before generation, a thin-spec shop budgets for cheap rework and rapid direction changes.*

### Is a well-shaped spec sufficient input for an agent to produce a correct implementation, or does the spec-to-code gap require an intermediate executable artifact?

| Position A | Position B |
|---|---|
| Frontier models can one-shot medium-sized features from a well-shaped spec; implementation is one of the easiest stages to automate, and AI now does essentially all of it.<br>*[How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* | Abstract spec straight to production fails — it passes basic tests but breaks on concurrency, process failure, and network failure; you must insert a deterministic simulation implementation as executable design and then a concrete spec before the real implementation.<br>*[The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)* |

*Why it matters: Whether you invest in simulation/fuzz infrastructure between spec and code determines your correctness ceiling for concurrent and distributed systems; the one-shot view holds for CRUD features but the simulation camp reports it demonstrably failing where legal-but-inconvenient platform behavior matters.*

### When the spec and the code disagree, which is the source of truth?

| Position A | Position B |
|---|---|
| Only the code is trustworthy — docs, readmes, and architecture files will lie; the type system, not the document, is what prevents invariant violations, so agents should read the code itself.<br>*[fighting slop with slop](../talks/fighting-slop-with-slop.md)* | The document is the state and the unit of change: you edit the spec and instruct the AI to make it true, with the doc holding the context (political, commercial, aesthetic) that code cannot express.<br>*[Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)* |

*Why it matters: It determines where you invest: doc-as-truth teams build spec pipelines and context-engineering docs, code-as-truth teams build rigid type systems, execution tracing, and semantic code-search tools instead — and the two produce opposite answers about whether stale documentation is a crisis or an expected condition.*

### At what altitude should the durable artifact sit — product behavior, or engineering decisions?

| Position A | Position B |
|---|---|
| Spec-driven development at the product/behavior level is too far removed from engineering reality to serve as the decision layer; what needs to be durable is the set of engineering decisions that matter, extracted into a doc up front so agents are stateless.<br>*[Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* | The durable artifact is the product-level requirements document — user stories with persona/need/why, a solution-agnostic problem statement, requirements plus design plus tasks — and it should not prescribe implementation or architecture at all.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)* |

*Why it matters: It decides who owns the artifact (PM/analyst versus engineer) and what code review then checks against; product-level specs leave architectural decisions to whoever prompts, which is exactly the failure the decision-layer camp is trying to prevent.*

## Practical Guidance

**Do:**

- Commit requirements, design, and task documents as markdown in the repo so agents load them as context and humans can diff them
- Keep the always-loaded architecture file model-agnostic (architecture.md, not CLAUDE.md), incredibly small, and limited to invariants that will not change for months or years
- Cap PRDs and TDDs at one to two pages and treat them as communication artifacts to iterate on, not finalized specs
- Write the business problem statement solution-agnostic — do not prescribe agent, multi-agent, or any architecture in it
- Format requirements as persona/need/why user stories, since models were trained on that structure and pattern-match it better than generic prose
- Stop after the assistant generates the requirements and design documents and hand-edit them with your own expertise before any code is generated
- Generate property-based tests from the requirements and design documents (e.g. fast-check) so tasks are verified against the spec, not against themselves
- Attach a termination gate to every spec: binary pass/fail criteria rather than score rubrics, a golden dataset that grows from production failures, and repeated runs against a sustained bar such as 90%
- Explicitly forbid any optimizing agent from editing the golden dataset or the scorers
- Keep the spec independent of the agent framework/harness, since you will likely switch harnesses within about a year
- Require a written taxonomy/design document from every research prototype before software engineers join, including domain context, data representations, and the type contract between the ML repo and the product repo
- For concurrent or distributed targets, insert a deterministic, inspectable simulation implementation between the abstract spec and the concrete implementation, and expose to the agent why an invariant failed, not just that it failed
- Validate the spec's basic assumptions with the actual customer (which platform, what is driving urgency, who else in the pipeline wants this) before writing it
- Share the plan with a human teammate before implementation, even though it feels unnatural
- Keep PRs under 500 lines so review against the spec stays meaningful

**Avoid:**

- End-to-end YOLO generation from a vague goal to a production system — even with plan mode it passes basic tests and then breaks on concurrency, process failure, and network failure
- Letting a coding agent choose your system architecture; it produces an over-engineered system before you know what is actually failing
- Stuffing agents.md or steering files with everything — there is a Goldilocks amount of context, and too much is as harmful as too little
- Using chat, or plan mode, as the durable decision layer: it is isolated, ephemeral, and encourages accepting the recommended option without thinking
- Asking the model to improve its own prompts or behavior — it was trained on human material and will micromanage itself
- Running the full spec workflow for small changes and quick fixes where vibe coding is the right tool
- Expressing guardrails as prompt text inside the spec instead of deterministic configuration outside the agent, since a third party can prompt-inject past them
- Rubber-stamping review because the spec exists — blind approval gives false confidence
- Automating the pipeline without scoping discipline (a token-maxxing slop cannon) or scoping well without investing in agents (you lose to agent-native competitors)
- Treating a demo as the deliverable, or shipping a PRD that no real user has tested against
- Saying yes to every customer request in the spec instead of checking whether other prospects in the pipeline would benefit

## Notable Outliers

- For infrastructure vendors the shipped product stops being the implementation and becomes the specification/protocol itself, with bespoke implementations synthesized on demand from it. ([The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [2:02](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=122s))
- Read nothing but the code — docs, readmes, and architecture files will definitely lie, and only the code cannot. ([fighting slop with slop](../talks/fighting-slop-with-slop.md), [13:06](https://www.youtube.com/watch?v=AMiyLItEtLA&t=786s))
- 17 of 21 agent ideas at an internal hackathon were abandoned for lack of business value or data access, and the surviving 4 carried all the impact — the spec's job is to kill the other 17 earlier. ([You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s))
- An optimized agent variant that meets its target eval scores is shipped to production automatically, with no human in the loop. ([The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [22:47](https://www.youtube.com/watch?v=pSto5YaNGUo&t=1367s))
- Plans that get written and then never implemented are a positive signal, because it means ideas are being explored and prioritized rather than built by default. ([Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [14:08](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=848s))
- The future unit of software change is editing a document and telling the AI to make the document true; the generated CI YAML is a compiled artifact nobody reads. ([Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [18:05](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=1085s))
- Structure — clean tagged PRs, accurate diffs, real internal documentation — not taste, is the expensive and scarce input, and almost no organization actually maintains it. ([Content Is Code](../talks/content-is-code.md), [6:42](https://www.youtube.com/watch?v=yv6xovSsB1U&t=402s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Content Is Code](../talks/content-is-code.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)
- [Perception Agents](../talks/perception-agents.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)
- [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)
- [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)
- [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)
- [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)

## Speakers

- [Alex Bauer](../speakers/alex-bauer.md)
- [Antje Barth](../speakers/antje-barth.md)
- [Apoorva Joshi](../speakers/apoorva-joshi.md)
- [Balázs Horváth](../speakers/balazs-horvath.md)
- [Dan Feng](../speakers/dan-feng.md)
- [Deepak Pathak](../speakers/deepak-pathak.md)
- [Dominik Tornow](../speakers/dominik-tornow.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [Erik Hanchett](../speakers/erik-hanchett.md)
- [Idan Gazit](../speakers/idan-gazit.md)
- [Leo Mehr](../speakers/leo-mehr.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Matt Dailey](../speakers/matt-dailey.md)
- [Nicholas Arcolano](../speakers/nicholas-arcolano.md)
- [Vaibhav Gupta](../speakers/vaibhav-gupta.md)

