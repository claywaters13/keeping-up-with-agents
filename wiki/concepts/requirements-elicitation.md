---
title: "requirements elicitation"
type: "concept"
slug: "requirements-elicitation"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 10
---

# requirements elicitation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **10** speaker(s)

**Definition:** Extracting what should actually be built from stakeholders and turning it into a scoped, checkable statement of work.

*Also referred to as: requirements gathering, requirements scoping, requirements specification, domain expert elicitation, product requirements specification, scope definition, mvp scoping*

## State of Practice

The field's consensus this year is that code generation has stopped being the constraint and requirements definition has become it — "specs are the new code" was said in almost those words from three different stages. The practical shape of that work is: get a solution-agnostic problem statement out of stakeholders (who reliably hand you a solution instead of a problem), attach a measurable target with a deadline, enumerate the non-negotiable constraints — latency budget, cost ceiling, regulatory requirements — before any architecture is chosen, and get success criteria in writing before a line is generated. Forward-deployed practitioners are the most explicit that this is an adversarial-ish interrogation: verify who is actually driving the urgency, ask for the named counterpart working team, validate assumptions as basic as which mobile OS the customer mandates, and check whether anyone else in the pipeline wants the same thing. The counterweight to spec discipline is restraint: over-engineering before knowing what is actually failing was named the single most common mistake, and "the scarce skill now that AI coding is so good is exercising restraint" was the line of the FDE track. Where the field is genuinely unsettled is the artifact and the automation — whether elicitation output should be a prose spec, a reference implementation, or a set of binary domain-specific evaluators, and whether the intake-and-scoping stage can itself be handed to agents.

## Consensus

### Deciding what to build, not writing the code, is now the binding constraint on shipping software; the specification is the expensive artifact.

Support: **6** talk(s)

> "at a point where writing code is no longer the bottleneck, the real thing is to figure is figuring out what it is that you should be building."
>
> — [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s)

Supporting talks: [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)

### Stated requirements are solutions in disguise and must not be taken at face value; the elicitor's job is to recover the underlying problem and to verify the stated drivers (urgency, staffing, platform assumptions) independently.

Support: **4** talk(s)

> "Customers describe solutions not problems. Your job as the FTE is to understand what the problem is. Customers don't know what happens next and your job as the FD is to define it."
>
> — [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [6:54](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=414s)

Supporting talks: [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)

### Success criteria and scope must be agreed in writing, narrowed, and made measurable before build starts; open-ended or unanchored scope predicts failure.

Support: **5** talk(s)

> "you want to figure out ahead of time what does success look like for the customer. And really narrowing that down, ideally getting it in writing so that there is like no miscommunication along the way."
>
> — [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [8:56](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=536s)

Supporting talks: [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)

### The highest-value requirements cannot be extracted from documents, surveys, or existing knowledge bases — they require direct, physical access to the stakeholders and domain experts who hold the implicit criteria.

Support: **5** talk(s)

> "Now the real bottleneck is getting your people, your stakeholders, your decision-makers into the room and being able to access them and elicit the requirement and being able to spend the time with them."
>
> — [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [2:25](https://www.youtube.com/watch?v=6bmM45jkMDY&t=145s)

Supporting talks: [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)

### With generation cheap, the discipline that matters is restraint — refusing requests, starting from the simplest design, and not expanding scope before you know what is actually failing.

Support: **5** talk(s)

> "But the scarce skill now that AI coding is so good, the scarce skill is actually exercising restraint."
>
> — [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [7:38](https://www.youtube.com/watch?v=7wu2hsRfvV0&t=458s)

Supporting talks: [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)

### A human must personally author or edit the requirements artifact and retains accountability for the output; review by coding agents alone is insufficient.

Support: **4** talk(s)

> "Now, this is at the point I would highly recommend, if you're trying this at home, to stop and go in and update it with your knowledge and expertise and taste to exactly what you're looking for. Because it's only as good as what you put in."
>
> — [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [11:34](https://www.youtube.com/watch?v=IddXPepIAS4&t=694s)

Supporting talks: [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [Field Guide to Fable](../talks/field-guide-to-fable.md)

## Disagreements

### Should the elicited requirement be expressed as an explicit written prose specification, or is prose the wrong medium for handing intent to a model?

| Position A | Position B |
|---|---|
| Write and hand-edit markdown requirements and design documents before any code — structured user stories committed to the repo, guardrails against the assistant going off the rails, property-based tests derived from the requirements doc.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)* | Prose specs and in-prompt examples constrain current models; give the model another artifact as a map — existing code, an HTML mockup — and give it context rather than instructions. Anthropic removed 80% of the Claude Code system prompt on this reasoning.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md)* |

*Why it matters: It determines whether the elicitation deliverable is a document a human reviews and versions, or a reference implementation plus a list of enumerated unknowns. The first is auditable and reviewable by non-authors; the second is faster but leaves the requirement implicit and unversioned.*

### Can requirements intake and scoping themselves be handed to agents, or is that stage irreducibly human?

| Position A | Position B |
|---|---|
| Every stage of the pipeline — context gathering, scoping, spec writing, implementation — can be replaced with agents, and teams that do not build that agent factory will lose to agent-native competitors. Ramp's intake agent cut reply latency from days to seconds and ~20% of scoping time.<br>*[How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)* | The elicitation bottleneck is stakeholder access, not throughput: you cannot prompt the room, you cannot get it from a badge-less conference room, and the implicit decision criteria only come out of domain experts producing concrete examples. AI ideation regresses to the most common answer rather than the step change you need.<br>*[You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)* |

*Why it matters: If intake is automatable, headcount moves from scoping to building the intake harness; if it isn't, the correct move is to redeploy your most senior people out of code and into customer rooms. Both sides agree the middle of the pipeline is the gnarly part — they disagree on whether more tokens or more access unblocks it.*

### Is an up-front requirements pass always worth its cost, or does shipping something fast teach you the requirement faster?

| Position A | Position B |
|---|---|
| Below a threshold, skip the process — if it takes under a day, build and ship it and don't bring in PMs; small changes and quick fixes are better vibe-coded; launching a project and risking failure teaches more than extended planning.<br>*[How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)* | Anything with real consequences needs the full pass first — constraints gathered before design, eval criteria defined before code — because most ideas die on business value and data access, not on implementation, and 'just ship it' is dangerous once other people depend on the output.<br>*[AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)* |

*Why it matters: This sets the default for every incoming request. Side A's failure mode is permanent 'temporary' hacks you support for 18 months; side B's is a 17-of-21 abandonment rate discovered only after specs were written.*

## Practical Guidance

**Do:**

- Write the business problem statement solution-agnostically — it must not say whether the system will be an agent, a multi-agent system, or anything else.
- State the goal as a measured delta with a deadline, e.g. 'reduce the average processing time for urgent claim review requests from 2 days to 1 hour within 90 days of launch'.
- Ask 'who are the people we're going to work with?' and get named counterparts before accepting an engagement.
- Collect latency budget, cost ceiling, and regulatory requirements before design, since they constrain every downstream architectural decision.
- Check whether other prospects and customers in the pipeline would benefit from the request before building it — architect each customer-specific solution for the next four customers.
- Validate base assumptions explicitly with the customer (e.g. which mobile platform their employees are mandated to use) before engineering starts.
- Format requirements as persona/need/why user stories and commit them as markdown in the repository so tools can read them as context.
- Replace scalar quality scores with binary domain-specific checks — 'the answer is based on the knowledge base, yes/no' instead of a 0-1 correctness score.
- Have domain experts produce a few hundred concrete labeled examples; those examples become the high-signal evaluators.
- Run a 'blind spot pass' to enumerate unknowns — places where the map (your spec) will not match the territory (the actual codebase and constraints).
- Hand a model an existing implementation or HTML mockup as the reference rather than describing it in prose.
- Sequence value, then architecture, then design; and measure shipped features by repeat usage rather than count shipped.

**Avoid:**

- Taking a customer's requirements document at face value — it describes their proposed solution, not their problem.
- Accepting 'we're understaffed' as the justification for an engagement; that is staff augmentation, not a defined problem.
- Selling a fixed number of engineers for a fixed period with no defined problem ('take two FDEs for 6 months, do whatever you want with them').
- Letting a coding agent choose the system architecture — you risk an over-engineered system.
- Over-engineering the solution before knowing what is actually failing, or before evaluating anything at all.
- Prompting at the altitude of 'build us an agent that handles support' — generic asks return generic, average answers.
- Cramming everything into agents.md or steering files; there is a Goldilocks amount of context and too much degrades output.
- Shipping a demo as the deliverable, or writing a PRD with no real user testers — both predict the software will not be used in production.
- Saying yes to every customer request in the belief that it constitutes customer success.
- Calling any hack 'just temporary' — ship everything as if it will run for 18 months, because it will.
- Opening a pitch with category buzzwords ('agentic AI orchestration platform') or abstract benefits ('we increase productivity') instead of the concrete before/after.
- Running an optimization loop against an undefined target function with no validation mechanism or escape hatch.

## Notable Outliers

- Whoever defines the problem owns the solution — and controlling an enterprise's vocabulary through your ontology is lock-in, because users don't just adopt your product, they adopt your language. ([How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [15:20](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=920s))
- More capable models increase rather than decrease the need for upfront specification, because they traverse more territory and therefore hit more unspecified decision points. ([Field Guide to Fable](../talks/field-guide-to-fable.md), [9:37](https://www.youtube.com/watch?v=9fubhllmsBU&t=577s))
- 17 of 21 agent ideas from an internal hackathon were abandoned for lack of business value or data access — the elicitation failure rate, not the build failure rate, is what kills agent projects. ([You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [0:01](https://www.youtube.com/watch?v=6bmM45jkMDY&t=1s))
- Replace 'features shipped last quarter' as a KPI with 'features shipped that are used more than twice'. ([You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [13:26](https://www.youtube.com/watch?v=6bmM45jkMDY&t=806s))
- In a self-improvement loop, the first iteration captured ~10 of the ~15 accuracy points gained; you could have stopped there — the value was in the clear-cut failure signal, not the loop. ([Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md), [11:24](https://www.youtube.com/watch?v=eAXxdtNlK04&t=684s))
- Telling a customer your product is the wrong tool for their use case increases trust and generates future opportunities. ([Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [14:49](https://www.youtube.com/watch?v=APqXGyCoGW4&t=889s))

## All Talks

- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)
- [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)
- [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [Stop Burning Tokens: Why self-improvement needs domain expertise first](../talks/stop-burning-tokens-why-self-improvement-needs-domain-expertise-first.md)
- [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)
- [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)
- [Your AI Product Will Fail Unless You Can Explain It](../talks/your-ai-product-will-fail-unless-you-can-explain-it.md)

## Speakers

- [Annabell Schäfer](../speakers/annabell-schafer.md)
- [Apoorva Joshi](../speakers/apoorva-joshi.md)
- [Balázs Horváth](../speakers/balazs-horvath.md)
- [Erik Hanchett](../speakers/erik-hanchett.md)
- [Leo Mehr](../speakers/leo-mehr.md)
- [Pauline Brunet](../speakers/pauline-brunet.md)
- [Sunny Rekhi](../speakers/sunny-rekhi.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Veronica Hylak](../speakers/veronica-hylak.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)

