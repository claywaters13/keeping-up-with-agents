---
title: "agent configuration files"
type: "concept"
slug: "agent-configuration-files"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 8
---

# agent configuration files

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **8** speaker(s)

**Definition:** Checked-in files that persistently steer an agent's behavior — rules, instructions, and voice — as versioned artifacts a team edits together.

*Also referred to as: agent configuration, shared agent configuration, context and rules files, markdown context files, agent steering documents, natural language agent configuration, voice and tone files, personal context artifacts*

## State of Practice

The field has settled on checked-in markdown as the substrate for steering agents: AGENTS.md/steering files, skill folders, spec and design documents, glossaries, and voice files all live in the repo next to the code and are edited like source. The live argument is no longer whether to write them but how much to load and when — Amazon AGI Lab caps skill.md at ~100 lines (the skill is a folder, not a file), treats the entry file as a thin index, and calls a first prompt above 40–50K tokens a progressive-disclosure failure against a ~20–25K baseline; AWS frames the same tradeoff as a Goldilocks zone where over-stuffing agents.md actively hurts. A second consensus is that these files are team artifacts, not personal dotfiles: embedding them in repos beats training individuals, and getting skeptics to edit the shared setup is the adoption signal that matters. The sharpest technical position is that instruction files are probabilistic and cannot carry guarantees — hard identity rules, disclosure requirements, and claim verification belong in code paths the prompt cannot override, whether that's Isadora Martin-Dye's deterministic layer-four veto or blocking pipeline gates. Unresolved: whether config should be standardized across a team or diverge per repo, whether critical constraints can ever be expressed in natural language, and whether these files should be hand-written or synthesized by the agent itself.

## Consensus

### Agent-steering context belongs in versioned markdown checked into the repo alongside the code, not in tickets, chat, or individuals' heads.

Support: **4** talk(s)

> "just make sure that you track all of these in a good old markdown file in your repository so that AI can access it."
>
> — [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [8:35](https://www.youtube.com/watch?v=6bmM45jkMDY&t=515s)

Supporting talks: [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md)

### One catch-all instruction file or system prompt underperforms narrowly scoped, on-demand files; more instruction text is not better, and the always-loaded entry point must stay thin.

Support: **4** talk(s)

> "I would be very careful not to put too much information or too little information in that. Kind of like that Goldilocks zone of information is what you need."
>
> — [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [4:16](https://www.youtube.com/watch?v=IddXPepIAS4&t=256s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)

### Instruction files cannot enforce anything on their own; anything that must not happen needs a deterministic check outside the prompt — a blocking gate, a human review step, or a post-generation veto.

Support: **4** talk(s)

> "Everything before layer four is prompt engineering. You're asking nicely and hoping. Layer four is systems engineering. You're checking, and you are sure."
>
> — [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [17:51](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1071s)

Supporting talks: [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)

### Agent config is a shared team asset whose leverage comes from being edited collectively — investing in the repo's files beats leveling up individual engineers.

Support: **3** talk(s)

> "My theory here was if I can get engineers to embed AI directly into their repos, then not only would the agents perform better but the entire team would benefit, not just the 1%."
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [6:40](https://www.youtube.com/watch?v=whue9_YquGA&t=400s)

Supporting talks: [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)

## Disagreements

### Should agent configuration be standardized into one shared setup, or allowed to diverge per repo, team, or individual?

| Position A | Position B |
|---|---|
| Converge on a single standardized setup: find the best ICs, extract their practices, and require everyone to abandon their personal bespoke configs; likewise, upstream any customer-specific configuration back into the product rather than letting per-customer prompt piles accumulate.<br>*[Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)* | Do not force one-size-fits-all: let each repo's champion figure out what works for web vs. mobile vs. monorepo and let convergence happen naturally; personal, individually-tuned config (a voice.md distilled from your own writing, a hand-maintained glossary) is a legitimate first-class artifact.<br>*[Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md)* |

*Why it matters: It determines whether config lives in one org-wide template that leadership funds and enforces, or in per-repo files that a platform team can only seed and never own. Standardizing early buys robustness to harness changes; standardizing wrong produces exactly the top-down mandate both speakers warn kills adoption.*

### Can an agent's critical constraints be expressed in natural-language configuration, or must they be moved out of the prompt into code?

| Position A | Position B |
|---|---|
| No — a prompt will eventually lose. Hard identity rules must sit in a layer the voice layer physically cannot override, output must pass a deterministic regex veto wired as a shared service, gates must block rather than warn, and slop should be assumed inevitable so investment goes into detection and self-healing.<br>*[Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* | Yes — the product goal is that the entire agent be configurable in natural language by non-engineers, and values/guardrails can live as a written soul file that acts as the agent's conscience in production.<br>*[How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)* |

*Why it matters: If constraints can live in text, customers and non-engineers can own the config and iterate in minutes; if they cannot, every safety-relevant rule needs an engineer, a code path, and a test, and the natural-language surface is limited to preferences rather than guarantees.*

### Should configuration files be hand-authored by humans, or synthesized and maintained by the agent itself?

| Position A | Position B |
|---|---|
| Human-authored and human-edited: stop after generation and rewrite the requirements and design docs with your own knowledge and taste, because output quality is bounded by input quality and you — not the agent — get blamed; the shared setup should be distilled from your best engineers' actual practices.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* | Agent-synthesized and self-updating: have the model distill a voice.md from your existing public writing, auto-update a glossary file whenever a component changes, and run a nightly cycle that turns the day's work into reusable skills and resolves contradictions.<br>*[Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)* |

*Why it matters: Self-maintaining config scales with usage and stops going stale, but it removes the human review point that spec-driven practitioners treat as the accountability boundary — nobody has reviewed the rules the agent is now following.*

## Practical Guidance

**Do:**

- Cap skill.md at roughly 100 lines and treat a skill as a folder, deferring detail to sibling files the agent loads only when needed
- Budget the always-loaded first-prompt context at ~20–25K tokens; treat 40–50K as evidence progressive disclosure has failed
- Make the top-level config a thin index that points to the right files rather than containing the content itself
- Split voice/behavior config into distinct layers and put hard identity rules where the voice layer cannot override them
- Commit requirements as user stories in the persona/need/why structure, since models were trained on that format
- Hand-edit generated spec and design documents before any implementation starts
- Route every output surface through one shared deterministic veto service so no surface can accidentally opt out
- In multi-tenant config, make a missing brand identity field throw rather than silently default
- Generate property-based tests directly from the requirements and design documents to verify tasks were implemented as specified
- Encode a precedence rule that human corrections permanently win over model-derived stored facts
- Explicitly exempt experimental and prototype code from the codebase's rigorous standards in the config
- Customize the config per repo shape (web, mobile, monorepo) and let similar repos converge, rather than mandating one template
- Track skeptics editing the shared config as the leading indicator that adoption is working

**Avoid:**

- Asking one system prompt to be situational, expressive, and self-checking at once — Isadora's system had 24 scattered system prompts before layering
- Over-stuffing agents.md or steering files; too much context is a documented failure mode, not a safety margin
- Letting an agent become a black box of customer-specific prompts and patches — it is too brittle for both vendor and customer
- Shipping a gate that only logs warnings; if it cannot halt the artifact it is a suggestion, not a gate
- Relying on few-shot examples for guarantees — they teach quality on anticipated inputs and nothing on unanticipated ones
- Mandating a shared setup top-down, which triggers the fear response that actually blocks adoption
- Treating config work as an IC side project instead of a standing percentage of team time that produces no immediate PRs
- Babysitting the agent — that is a defect signal about the codebase setup, not normal practice
- Blaming the model when behavior degrades; the harness changed, and a well-configured codebase should absorb small harness changes

## Notable Outliers

- The agent's values file is a 'soul file' written from the principles of a three-generation Jain family business — ancient philosophy running as production guardrails, explicitly not 'be helpful, be harmless'. ([The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [7:43](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=463s))
- Documentation should live in code comments rather than separate files, so that any time the agent grabs that code it reads the comment and can navigate to the full context. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [7:23](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=443s))
- A voice.md can be generated by pointing a model at everything you have publicly written, distilling your tone into a file the agent reuses. ([Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md), [7:39](https://www.youtube.com/watch?v=Z2Erdirpudo&t=459s))
- Deterministic regex checks are preferred over a probabilistic classifier for the output veto — an explicit, acknowledged trade of coverage for reliability. ([Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [20:38](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1238s))
- A hand-maintained markdown glossary of a project's content is more token-efficient for an agent than having it read the rendered page. ([Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md), [11:29](https://www.youtube.com/watch?v=Z2Erdirpudo&t=689s))
- A skill running for over an hour is a feature, not a bug — under the reasoning paradigm, longer agent runs produce better output. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [12:20](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=740s))

## All Talks

- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)
- [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)
- [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md)
- [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)
- [You Can't Prompt the Room: The Last Skill AI Won't Replace](../talks/you-cant-prompt-the-room-the-last-skill-ai-wont-replace.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Balázs Horváth](../speakers/balazs-horvath.md)
- [Erik Hanchett](../speakers/erik-hanchett.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Sunny Rekhi](../speakers/sunny-rekhi.md)

