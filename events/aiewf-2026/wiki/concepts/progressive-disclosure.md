---
title: "progressive disclosure"
type: "concept"
slug: "progressive-disclosure"
tier: "core"
maturity: "consolidating"
talk_count: 12
speaker_count: 13
---

# progressive disclosure

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **12** talk(s) by **13** speaker(s)

**Definition:** Loading instructions, tools, or reference material into context only when needed, keeping the default context small and expanding it on demand.

*Also referred to as: progressive disclosure of reference material, deferred tool loading, context pointers, tool result offloading, just-in-time memory retrieval, salience filtering, context externalization*

## State of Practice

Progressive disclosure has become the default architecture for agent context: a thin always-resident index (skill names and descriptions, tool stubs, a top-level index file) that points to bodies, reference files, and scripts the agent loads only if it decides it needs them. The field has moved past the principle to arguing over the numbers — Codex caps the available-skills list at 2% of the context window and progressively truncates beyond it, Amazon AGI Lab treats a 40–50K-token first prompt as proof that progressive disclosure has failed (20–25K is the expected baseline), DataRobot puts system prompt plus tool definitions under 40% of the window, and skill.md line caps of 100 (Amazon) to 500 (DeepMind) are being enforced in review. The economic argument is now framed as a permanent tax: a model-invoked skill's description is paid on every single model call, so 15 MCP servers can burn 100K+ tokens per session in tool definitions alone while an equivalent skills folder costs roughly an order of magnitude less. The unresolved cost is routing: descriptions are the only routing signal the model ever sees, roughly half of skill failures are non-triggering rather than bad content, and the model may simply decline to follow a context pointer — which is why the same conference produced both 'make everything model-invoked' and 'make everything user-invoked so you never have to eval invocation.' A minority but well-instrumented position (Towards AI) pushes back on the premise entirely, reporting that keeping full history untouched beat every compaction preset on recall, cost, and latency simultaneously, and that distinctive facts survived to 800K tokens.

## Consensus

### The always-loaded surface should be a thin index — skill name plus description, or a pointer file — with bodies, reference material, and scripts loaded only on demand.

Support: **6** talk(s)

> "we are only using the name and description path in in this system prompt and not the skill body and that's what what they call about is progressive disclosure"
>
> — [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [7:27](https://www.youtube.com/watch?v=7jjudsEhBtM&t=447s)

Supporting talks: [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)

### The resident description block is a per-call tax paid on every model invocation, so it must be explicitly budgeted rather than allowed to grow.

Support: **5** talk(s)

> "the description is the cost you always pay on every model invocation. So, on every model call, the description is part of the model context. So, you always pay that 100 200 tokens cost"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [7:41](https://www.youtube.com/watch?v=0vphxNt4wyk&t=461s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)

### Enforce a hard size limit on the entry-point skill file and push everything else behind pointers — a skill is a folder, not a document.

Support: **4** talk(s)

> "we've kind of set a hard limit for like 100 lines in your skill.md cuz your skill is really a folder."
>
> — [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [14:29](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=869s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)

### Instructions the agent would follow anyway (no-ops) and duplicated material are the main source of context bloat and should be deleted outright.

Support: **3** talk(s)

> "Let's imagine we have an implement skill and we have an entire paragraph of the skill that tells the agent to write a long detailed commit message. What would happen if you just deleted that paragraph? Well, the agent would probably still write a decent like long commit message."
>
> — [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [18:12](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=1092s)

Supporting talks: [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### LLM-generated skills are worse than human-written ones specifically because they bloat the disclosed surface — more tokens, more no-ops, more reasoning time.

Support: **3** talk(s)

> "human-written skills are the best we can provide. Uh AI-generated skills can uh impact performance negatively. And that skills or skills.md files should be below 500 lines of words."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [4:46](https://www.youtube.com/watch?v=0vphxNt4wyk&t=286s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)

## Disagreements

### Should skill invocation be model-driven (descriptions in context, model decides) or user-driven (explicit invocation, no resident description)?

| Position A | Position B |
|---|---|
| Prefer user-invoked skills: they eliminate the resident description cost and the entire class of invocation-unpredictability problems, at the price of user cognitive load. Model-invoked skills force you to run evals just to confirm they fire at the right time.<br>*[Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)* | Prefer model-driven invocation: end users of a product have no idea what a skill is and will never type 'use the refund skill,' so the routing burden belongs on the description, not the user.<br>*[Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)* |

*Why it matters: It determines whether your engineering budget goes into description-tuning and trigger evals (model-invoked) or into user documentation and discoverability (user-invoked) — and whether progressive disclosure costs you resident tokens at all. Note that DeepMind endorses user-invoked skills for internal dev workflows while insisting model-invoked routing is unavoidable in customer-facing products, so the split is partly about audience.*

### Does a large resident context actually degrade model quality, or is that assumption wrong?

| Position A | Position B |
|---|---|
| Yes — oversized context confuses the model with contradicting information, and quality falls off well before the window is full (degradation past ~25% utilization, a 'dumb zone' past 40%), so keep the baseline small and aggressively deferred.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* | Not necessarily — distinctive facts were recalled reliably to 800K tokens with no compaction, and keeping the full untouched history beat every compaction preset on recall, cost, and latency at once because 97% of tokens were cached.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: If context rot is real at 25–40% utilization, deferred loading is a quality mechanism and every resident token is worth fighting over; if it is not, progressive disclosure is only a cost optimization and aggressive pruning can actively lose money by forcing re-retrieval and invalidating the prompt cache.*

### Is a large skill a problem to be fixed by splitting, or a symptom of a different defect?

| Position A | Position B |
|---|---|
| Enforce a line ceiling and split — 100 lines for skill.md, under 500 for skills.md, many small cross-referencing skills over monoliths.<br>*[Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)* | Size is never the real problem: massive skills are always a symptom of duplication, sediment, or no-ops, so fix the source-of-truth violation rather than targeting a line count.<br>*[Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)* |

*Why it matters: Line caps are cheap to enforce in review but can push teams to shard a coherent procedure into pointer chains the model may decline to follow; the diagnostic view says a 400-line skill that is genuinely one source of truth should be left alone.*

### At what scale does a flat description list stop working, and what replaces it?

| Position A | Position B |
|---|---|
| Keep a flat list under a fixed budget and truncate mechanically — cap available skills at 2% of the context window, and mark tools as deferred so they surface through tool search.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* | Flat listing breaks around ten skills; past that you need embedding similarity search or a smaller shortlisting model to pick what enters the system prompt, and at hundreds of skills you need a hierarchy plus metadata filters and governance.<br>*[Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)* |

*Why it matters: A truncation budget is a few lines of harness code; a retrieval-and-governance layer is a subsystem with its own evals, owners, and failure modes — and picking the wrong one either silently drops skills or over-engineers a ten-skill library.*

## Practical Guidance

**Do:**

- Budget the first prompt: 20–25K tokens of baseline context is expected; 40–50K means progressive disclosure has failed.
- Cap the available-skills list as a fraction of the context window (Codex uses 2%) and truncate descriptions progressively past it.
- Keep system prompt plus tool definitions under 40% of the window before the user's first turn.
- Enforce a line ceiling on the entry file — 100 lines (skill is a folder) to 500 lines — and move branch-specific reference material into external files behind a context pointer.
- Mark tools as deferred so they are reachable via tool search instead of loaded into the window up front.
- Write descriptions in the phrasing of a user request, not as a description of the skill, and make them mutually distinct — descriptions are the only routing signal.
- Include negative cases in the description (roughly five happy-path and five 'do not use this' eval cases) to stop over-triggering.
- Delete any instruction the agent would follow anyway; no-ops are especially common when an agent wrote the skill.
- Test the disclosed skill across multiple harnesses and rerun evals on every model upgrade — instruction placement inside the file is model-dependent.
- Grade context by relevance the way rendering grades level of detail: near/focused objects in full, distant ones as stubs.
- Store large tool results outside the window and pass a summary, rather than re-sending them on every loop iteration.
- Start thinking about a shortlisting mechanism (embedding search or a small model) once you pass roughly ten skills.

**Avoid:**

- Don't turn a fixed sequence of steps into a skill — write a script; you pay description tokens on every call for something deterministic.
- Don't let an LLM author your skills unreviewed: generated skills consume more tokens and reasoning time and can degrade performance outright.
- Don't wire 15 MCP servers into an agent — that alone is 100K+ tokens per session in tool definitions.
- Don't assume a context pointer will be followed; the model may skip a perfectly relevant file, so measure task outcomes rather than whether the skill loaded.
- Don't compact by default — name the constraint forcing it first; summarization invalidates the prompt cache and needs >50x compression to pay off.
- Don't aggressively clear old tool outputs; the agent re-retrieves what it already had and total cost goes up.
- Don't judge progressive disclosure with single-turn benchmarks — they never accumulate enough tokens to exercise it.
- Don't let a shared skill file accumulate sediment: contributors add and never delete, and the disclosed surface silently grows.
- Don't test skills in an existing workspace — coding agents will cheat by reading prior chats and executions.

## Notable Outliers

- Keeping the entire conversation history untouched beat every compaction preset simultaneously on recall, cost, and latency, because 97% of tokens were cached — the setup sending the most tokens was the cheapest to run. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s))
- Distinctive facts were recalled reliably up to 800K tokens with no compaction, but dense semantic search collapsed to 0% recall at 400K where BM25 held 100%. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [58:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=3538s))
- Deliberately splitting a process into separate skills so the agent sees only one step at a time — hiding future steps — increases the legwork it does on the current step. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [15:46](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=946s))
- Skills impose roughly 10x less context overhead than the equivalent MCP setup purely because of progressive disclosure: <100 tokens at listing, <5K on activation, scripts below that. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s))
- Context should be assembled like level-of-detail rendering — anything far from the camera or the editing focus becomes a cube, and the model can't tell. ([The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md), [15:32](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=932s))
- Roughly 50% of skill failures are the skill never being triggered, not bad skill content — the disclosure boundary, not the disclosed material, is the dominant failure mode. ([Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [17:04](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1024s))
- A newer model focused on the beginning of the skill file and ignored critical instructions placed at the end, with no line of the skill changed — placement inside the disclosed file is a versioned contract against a specific model. ([Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s))
- Documentation should live in code comments so that any agent that greps into the code is handed the pointer to the full context automatically. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [7:23](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=443s))

## All Talks

- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)
- [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Alex Bauer](../speakers/alex-bauer.md)
- [Arturo Nunez](../speakers/arturo-nunez.md)
- [Dat Ngo](../speakers/dat-ngo.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Omar Solano](../speakers/omar-solano.md)
- [Philipp Schmid](../speakers/philipp-schmid.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

