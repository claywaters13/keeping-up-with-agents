---
title: "spec-driven development"
type: "concept"
slug: "spec-driven-development"
tier: "core"
maturity: "consolidating"
talk_count: 14
speaker_count: 14
---

# spec-driven development

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **14** talk(s) by **14** speaker(s)

**Definition:** Writing an explicit specification as the durable artifact that agents implement against, making the spec rather than the code the primary human authored input.

*Also referred to as: specification-driven development, document-driven development, ai-assisted specification, spec generation from unstructured requests, acceptance criteria, design specification checking, commander's intent prompting*

## State of Practice

The conference treated the written spec as the load-bearing human artifact and code as increasingly disposable output: multiple speakers stated flatly that implementation is no longer the human's job and that requirements, system design, and eval criteria are now where the engineering difficulty lives. The concrete practice that recurred is a markdown artifact committed into the repo — architecture.md, a requirements/design pair, a research prototype taxonomy doc, or a natural-language automation file whose CI YAML is treated as a compiled artifact — deliberately kept model-agnostic and small so it survives harness churn. Speakers converged on two hard constraints: unguided agents given only a goal fail (they over-engineer, invent architecture, or break under concurrency and failure modes that basic tests miss), and a spec without an executable termination gate — golden dataset, property-based tests derived from the requirements doc, deterministic simulation, binary evals — is not a spec you can hand to an agent. What is still openly argued is the spec's altitude (product/behavior stories vs. engineering-decision docs), its medium (durable doc vs. plan-mode chat), whether generated docs can be trusted at all against source code, and whether a human must gate every spec-to-ship cycle. The counterweight throughout was scoping: Ramp's FDE talk and VisualLabs both argued that a fast agent pipeline on top of bad scoping is a 'token maxing slop cannon,' and that 17 of 21 agent ideas at one hackathon died for lack of business value before any spec mattered.

## Consensus

### The spec, not the code, is now the hard and scarce human input; implementation from a well-shaped spec is the cheap part.

Support: **6** talk(s)

> "Specs are the new code. The art is in defining the product requirements, the system design, and evaluate criteria so you can be confident that your AI coding buddies are building the right thing."
>
> — [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [1:27](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=87s)

Supporting talks: [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

### Structure must be defined before the agent is turned loose; end-to-end generation from an unstructured goal fails today, even with plan mode.

Support: **6** talk(s)

> "And it was obviously a fail, even with using a nice plan mode in Claude first. I'm sure this will work eventually, but it doesn't today. So, you have to do some scaffolding."
>
> — [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [9:45](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=585s)

Supporting talks: [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Content Is Code](../talks/content-is-code.md)

### The durable spec artifact should be plain markdown in the repo, model- and harness-agnostic rather than tied to one vendor's convention.

Support: **6** talk(s)

> "instead of trying to hold standards in our codebase, we did something that is an invariant. We built an architecture.md file. Instead of using Claude.md, just pick something that every model can just understand."
>
> — [fighting slop with slop](../talks/fighting-slop-with-slop.md), [2:03](https://www.youtube.com/watch?v=AMiyLItEtLA&t=123s)

Supporting talks: [fighting slop with slop](../talks/fighting-slop-with-slop.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)

### A spec is only actionable for an agent when it carries an executable termination gate — evals, golden datasets, property-based tests, or a deterministic simulation.

Support: **6** talk(s)

> "after you build for agents, you essentially go into the eval-driven development loop, which I would call. And this is kind of equivalent to test-driven development for building software with agents because then the agents needs uh termination condition, right?"
>
> — [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [11:26](https://www.youtube.com/watch?v=pSto5YaNGUo&t=686s)

Supporting talks: [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Agents Building Agents](../talks/agents-building-agents.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [Perception Agents](../talks/perception-agents.md)

### Generated spec and design documents must be hand-edited and owned by a human before implementation; output quality is bounded by the human's input and the human stays accountable.

Support: **5** talk(s)

> "Now, this is at the point I would highly recommend, if you're trying this at home, to stop and go in and update it with your knowledge and expertise and taste to exactly what you're looking for. Because it's only as good as what you put in."
>
> — [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [11:34](https://www.youtube.com/watch?v=IddXPepIAS4&t=694s)

Supporting talks: [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)

## Disagreements

### Should agents treat written specs and docs as the source of truth, or is source code the only thing that can be trusted?

| Position A | Position B |
|---|---|
| Durable written artifacts — requirements docs, design docs, markdown specs in the repo — are the source of truth agents work from, and the code is the derived output.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)* | Docs, readmes, and architecture files will lie; agents should read nothing but the code, and correctness should be enforced by the type system and invariant tooling rather than by prose. The spec's job is to state a handful of invariants, not to describe the system.<br>*[fighting slop with slop](../talks/fighting-slop-with-slop.md)* |

*Why it matters: If specs are the source of truth you invest in doc discipline, review, and freshness; if code is, you invest in type systems, execution tracing, and language design instead, and you accept that most generated code will never be read.*

### At what altitude does the durable spec live — product/behavior requirements, or engineering decisions?

| Position A | Position B |
|---|---|
| The spec is a product-level artifact: requirements, user stories in persona/need/why form, business problem statements that are deliberately solution-agnostic, plus eval criteria.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)* | Product-level spec-driven development is too far removed from engineering reality to serve as the decision layer; the durable doc must capture the engineering decisions that matter, with the agent stateless around it.<br>*[Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)* |

*Why it matters: It determines who writes the artifact — a PM/analyst or the engineer — and whether the doc can actually resolve the concurrency, failure-mode, and abstraction choices that agents get wrong.*

### Is a written specification sufficient input for an agent to produce a correct implementation?

| Position A | Position B |
|---|---|
| Yes for normal feature work — frontier models can one-shot medium-sized features from a well-shaped spec, so the automation effort belongs upstream in scoping and intake, not in implementation.<br>*[How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)* | No — the gap between an abstract spec and a correct implementation is too large. You need executable intermediates (a deterministic simulated implementation, a concrete spec derived from it) or structured scaffolding, because prose-spec output passes basic tests and then breaks on concurrency, process failure, and network failure.<br>*[The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)* |

*Why it matters: It sets how much machinery you build between spec and code — nothing, a scaffolded structure, or a whole simulation harness — and that cost is only justified for systems where correctness under adversarial execution actually matters.*

### Must a human review each spec-to-production cycle, or can the loop close automatically once evals pass?

| Position A | Position B |
|---|---|
| Human review is the bottleneck to remove: if an optimized variant hits its target eval scores it ships automatically, and coding agents can autonomously iterate a spec/agent from 18% to 83% pass rate without a human in each loop.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Agents Building Agents](../talks/agents-building-agents.md)* | The human is accountable and must personally review both the generated code and the spec documents; taste and judgment over the final output stay human, and letting an agent make a critical decision means ceding ownership of the code.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* |

*Why it matters: The auto-ship position only holds if the eval suite is complete, and both sides agree evals are discovered from production failures rather than written upfront — so the disagreement is really about how much residual risk an incomplete eval suite is allowed to carry into production.*

## Practical Guidance

**Do:**

- Write the requirements and design markdown files, and commit them into the repository, before any code is generated, so agents pick them up as context
- Name the shared spec file something every model understands (architecture.md) rather than a vendor-specific CLAUDE.md, and keep it tiny — only things that will not change for months or years
- Include eval criteria in the spec itself, and generate property-based tests written against the requirements and design documents (e.g. fast-check in TypeScript) to verify each task was implemented correctly
- Keep the business problem statement solution-agnostic — it must not prescribe whether the system will be an agent, a multi-agent system, or something else
- Format requirements as persona/need/why user stories, since models were trained on that structure and pattern-match it better than generic prose
- Stop after the assistant generates the requirements/design docs and hand-edit them with your own knowledge and taste before letting it write code
- For distributed or concurrency-sensitive systems, build a deterministic, repeatable, inspectable simulated implementation as executable design between the abstract spec and the concrete implementation, and let the simulation expose information the real platform hides (e.g. that a read was stale) so the agent learns why it failed
- Require a written design/taxonomy doc from every research prototype before software engineers join, including domain context, data representations, and the explicit type contract between the ML repo and the core product repo
- Require the author to secure actual named readers before a design doc ships, to keep doc volume honest
- Keep the spec independent of the agent framework or harness, on the assumption you will switch harnesses within about a year
- When running an optimization loop against a spec, explicitly forbid the agent from editing the golden dataset or scorers, and run each hypothesis on its own git branch with rollback on regression
- Express automations in natural-language markdown as the source, treating generated CI YAML as a compiled artifact nobody reads or edits

**Avoid:**

- Letting a coding agent choose your system architecture, or jumping to a multi-agent design — you risk an over-engineered system before you know what is actually failing
- YOLOing end-to-end generation from raw sources with only plan mode as a guardrail; define the structure first
- Stuffing agents.md or steering files with everything — there is a Goldilocks amount of context, and too much information degrades results
- Treating plan-mode output as the durable artifact: it is a rich chat message in an isolated, ephemeral environment, not shared state
- Expressing guardrails as prompts to the agent — a third party can prompt-inject past them; guardrails must be deterministic configuration outside the agent
- Asking Claude to improve its own prompt or behavior — it was trained on human material and will micromanage itself
- Building an agent factory on top of undisciplined scoping, which yields a high-volume low-quality 'token maxing slop cannon'
- Skipping validation of basic assumptions in the spec (e.g. which mobile platform the customer actually mandates) — weeks of engineering can be wasted
- Using the spec workflow for small changes and quick fixes where the upfront planning cost is not justified
- Shipping a prototype with good accuracy as if it were production-ready, before iterating on cost, latency, and reliability

## Notable Outliers

- The specification, not the implementation, becomes the shipped product: general-purpose platforms get retired because bespoke implementations can be synthesized on demand from a reusable spec. ([The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [1:00](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=60s))
- Code review is not a necessary control at all — a strong type system plus invariant-enforcing tooling replaces it, and no standardization of AI tooling is imposed on engineers. ([fighting slop with slop](../talks/fighting-slop-with-slop.md), [19:38](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1178s))
- The future unit of software change is an editable specification document that you hand to the AI with the instruction 'make the document true.' ([Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [18:05](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=1085s))
- 17 of 21 agent ideas at an internal hackathon were abandoned for lack of business value or data access — no amount of spec quality rescues an idea that should not be built. ([You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s))
- Plans that get written and then deliberately never implemented are a positive signal, because it means ideas are being explored and prioritized rather than built by default. ([Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [14:08](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=848s))
- Structure — clean tagged PRs, accurate diffs, real internal documentation — not taste, is the expensive scarce input, and almost no organization actually maintains it. ([Content Is Code](../talks/content-is-code.md), [6:42](https://www.youtube.com/watch?v=yv6xovSsB1U&t=402s))
- Minimalism in a specification is the finish line, not the starting point: three years of deliberately removing abstractions and properties were required before agent-driven synthesis worked. ([The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [7:58](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=478s))

## All Talks

- [Agents Building Agents](../talks/agents-building-agents.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Content Is Code](../talks/content-is-code.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
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

