---
title: "progressive disclosure"
type: "concept"
slug: "progressive-disclosure"
tier: "core"
maturity: "consolidating"
talk_count: 10
speaker_count: 9
---

# progressive disclosure

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **10** talk(s) by **9** speaker(s)

**Definition:** Loading instructions, tools, or reference material into context only when needed, keeping the default context small and expanding it on demand.

*Also referred to as: progressive disclosure of reference material, deferred tool loading, context pointers, tool result offloading, just-in-time memory retrieval, salience filtering, context externalization*

## State of Practice

Progressive disclosure is now the default architecture for agent context, and the field has converged on a concrete mechanism: only a skill's name and description sit in the system prompt permanently, the body loads on invocation, and anything used by a single branch lives in a separate file behind a context pointer. Practitioners have started attaching numbers to it rather than treating it as a principle — Codex caps the available-skills list at 2% of the max context window and progressively truncates past that, Amazon's AGI Lab treats a 20-25K-token first prompt as healthy and 40-50K as a failed setup, and DataRobot argues baseline system prompt plus tool definitions should stay under 40% of the window before the user's first turn. The justification has also shifted from cost to quality: speakers cite context rot and contradictory-information confusion, not token bills, as the reason to keep the default small. The same logic has spread from skills to tools — deferred tool loading behind tool search, large tool results stored outside context and summarized — and is the main argument for skills over MCP, where 15 connected servers can burn 100K tokens per session in definitions alone. The unresolved edges are who pulls the trigger (model-invoked descriptions vs. explicit user invocation) and what happens past a few dozen skills, where a flat description list stops being a viable index at all.

## Consensus

### Only the skill's name and description belong in the always-loaded context; the body loads on demand, and that description is a permanent per-call tax you pay on every model invocation whether or not the skill fires.

Support: **5** talk(s)

> "we are only using the name and description path in in this system prompt and not the skill body and that's what what they call about is progressive disclosure"
>
> — [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [7:27](https://www.youtube.com/watch?v=7jjudsEhBtM&t=447s)

Supporting talks: [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### The main skill file should be aggressively small and act as a thin index — the skill is a folder, not a document — with detail deferred to sibling files.

Support: **4** talk(s)

> "we've kind of set a hard limit for like 100 lines in your skill.md cuz your skill is really a folder."
>
> — [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [14:29](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=869s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### Oversized context degrades output quality, not merely cost — the reason to disclose progressively is model confusion and context rot, not the token bill.

Support: **3** talk(s)

> "the more context you have in your in your context, the higher it is that you have contradicting information and it causes confusion for the model."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)

### Baseline context before the user's first turn should be held to an explicit numeric budget, and exceeding it is treated as a defect in the setup rather than a cost tradeoff.

Support: **3** talk(s)

> "I think like 20, 25K tokens get taken anyway, but like how much more is getting added? If you're coming to like 40K, 50K, like something's wrong. That's not really progressive disclosure."
>
> — [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [15:57](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=957s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### The same deferral applies to tools and tool output: definitions should be lazily discoverable rather than front-loaded, and large tool results should live outside the context with only a summary passed back.

Support: **4** talk(s)

> "we're marking some of these tools as deferred, and that means that they're not added directly to the context window, but instead are available through tool search later on."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)

### Agent-authored skills defeat progressive disclosure — they pad instructions with no-ops and consume more tokens and reasoning time than human-written equivalents, so generated skills must be audited and trimmed.

Support: **3** talk(s)

> "human-written skills are the best we can provide. Uh AI-generated skills can uh impact performance negatively. And that skills or skills.md files should be below 500 lines of words."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [4:46](https://www.youtube.com/watch?v=0vphxNt4wyk&t=286s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)

## Disagreements

### Should the decision to load a skill's body be made by the model (from a description in context) or by the user (explicit invocation)?

| Position A | Position B |
|---|---|
| Prefer user-invoked skills: explicit invocation removes routing unpredictability entirely and eliminates the need to eval whether a skill fires at the right time, at the price of user cognitive load. User invocation is the right default for routine dev workflows like opening PRs or staging docs.<br>*[Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)* | Prefer model-invoked skills: end users of a product have no idea skills exist and should not be asked to remember them, so routing must be model-driven off descriptions, with the description block budgeted (e.g. capped at 2% of the context window and truncated beyond that) to keep the cost bounded.<br>*[Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* |

*Why it matters: Model invocation makes description quality a first-class engineering artifact requiring trigger evals and negative cases, since roughly half of skill failures are non-triggering; user invocation moves that cost onto documentation and user habit instead. It also determines whether progressive disclosure is even viable for consumer-facing agents, where explicit invocation is not an option.*

### Does a flat description list in the system prompt remain a workable index as the skill library grows, or must it be replaced by retrieval?

| Position A | Position B |
|---|---|
| Keep the flat list and manage it by budget: cap the available-skills block as a fraction of the context window, progressively truncate descriptions past the cap, and keep the entry point a thin index that points to the right files.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* | The flat list stops working past roughly ten skills; beyond that you need embedding similarity search or a smaller shortlisting model to pick candidates, and at hundreds of skills flat retrieval fails outright and requires a skill hierarchy plus metadata filters and governance.<br>*[Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)* |

*Why it matters: If the flat list scales, progressive disclosure is a prompt-authoring discipline; if it does not, every enterprise harness needs a retrieval layer, skill owners, semantic versioning, and admission gates before the library is usable at all.*

### When the always-loaded baseline is large, is the right fix to shrink it or to make it cheap?

| Position A | Position B |
|---|---|
| Make it cheap: cache the system prompt (and where possible the tool prompt and messages) so only a much reduced payload is sent after the first call, trim history with a sliding window, and summarize what falls out.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)* | Shrink it: a large baseline is a defect regardless of price, because performance degrades past roughly 25-40% context utilization and extra content raises the odds of contradictory information — so defer tools, cap the skills block, and hold the first prompt to 20-25K tokens.<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* |

*Why it matters: Caching optimizes the bill while leaving the window full, which is exactly the failure the context-rot camp says silently degrades output; teams that treat cache hit rate as the success metric will ship agents that are cheap and quietly dumber.*

## Practical Guidance

**Do:**

- Cap the available-skills description block as a share of the context window — Codex uses 2% of the max window and progressively truncates descriptions beyond it.
- Hold the first prompt's baseline context to roughly 20-25K tokens; treat 40-50K as evidence progressive disclosure has failed.
- Keep system prompt plus tool definitions under 40% of the context window before the user's first turn.
- Cap skill.md at ~100 lines (or at minimum under 500 lines) and treat the skill as a folder whose .md is a thin index pointing to other files.
- Move any reference material used by only one branch of a skill out of skill.md into an external file behind a context pointer.
- Mark rarely used tools as deferred and expose them through tool search rather than loading their definitions up front.
- Store large tool results outside the context and pass a summary, instead of re-sending the full result on every loop iteration.
- Write skill descriptions in the phrasing users actually use, keep them mutually distinct, and include five negative 'do not use this when' cases alongside five happy-path cases to stop over-triggering.
- Once past ~10 skills, shortlist with embedding similarity search or a smaller model instead of listing every description in the system prompt.
- Delete no-ops — instructions the agent would follow anyway — even when removing them does not move eval scores, because the tokens are saved regardless.
- Run evals both with and without the skill loaded, so you can tell when a capability skill has been obsoleted by the model and can be retired.
- Split a multi-step process into separate skills so the agent sees only the current step, which increases the legwork it does on that step by hiding the future goal.
- Put documentation in code comments so an agent that reaches the code finds the pointer to the rest of the information.

**Avoid:**

- Don't assume the model will follow a context pointer — it may simply choose not to invoke a perfectly matching skill, and roughly 50% of observed skill failures are non-triggering rather than bad content.
- Don't connect an agent to many MCP servers casually: 15 servers can consume over 100,000 tokens per session in tool definitions alone.
- Don't write a skill for a workflow that is always the same fixed sequence of steps — write a script and stop spending model tokens on it.
- Don't let an agent author your skills unaudited; agent-written skills are where no-ops cluster most heavily.
- Don't let a shared skill file accumulate sediment — contributors adding their own text without deleting anyone else's — or duplication across steps and reference material.
- Don't rely on a naive sliding window over conversation history without summarizing the dropped prefix into context, or you lose the beginning of the conversation entirely.
- Don't treat a large static baseline as acceptable just because it is cached; the window is still full when the model reasons.
- Don't pull in community-authored skills without auditing them against a rubric first — they may not be any good.
- Don't assume a skill that discloses correctly on one harness or model does so on another; instruction placement inside the file is model-dependent, and a newer model ignored critical instructions placed at the end of an unchanged skill.

## Notable Outliers

- Hiding future steps is itself a technique, not just a cost: splitting a process into separate skills so the agent sees one step at a time measurably increases the legwork it does on the current step. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [15:46](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=946s))
- Massive skills are never the real problem — they are always a symptom of duplication, sediment, or no-ops, so shrinking by editing for size rather than diagnosing the cause misses the defect. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [16:23](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=983s))
- Skills impose roughly 10x less context overhead than the equivalent MCP setup purely because of progressive disclosure, and a skills folder can replace MCP for most use cases given a strong base reasoning model. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s))
- Silently blowing through context is the failure mode to watch for — a setup can burn 500K to a million tokens and hit auto-compact on a task that was never complicated. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [4:30](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=270s))
- Compaction should be done server-side in the exact form the model was trained on, so that performance stays the same after context is compressed. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [18:49](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1129s))
- Progressive disclosure has an organizational analogue: a librarian layer that supplies company-specific semantics just in time, rather than preloading all business definitions, prevents agents from silently applying wrong definitions to business data. ([Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [12:40](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=760s))

## All Talks

- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Alex Bauer](../speakers/alex-bauer.md)
- [Dat Ngo](../speakers/dat-ngo.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Philipp Schmid](../speakers/philipp-schmid.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

