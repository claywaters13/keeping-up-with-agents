---
title: "agent skills"
type: "concept"
slug: "agent-skills"
tier: "core"
maturity: "consolidating"
talk_count: 26
speaker_count: 26
---

# agent skills

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **26** talk(s) by **26** speaker(s)

**Definition:** Packaged, model-invocable units of procedural knowledge (instructions plus optional resources) that extend an agent's capabilities without retraining or hard-coding.

*Also referred to as: agent skills design, skill files, agent skills and plugins, skill decomposition, capability vs preference skills, model-invoked vs user-invoked skills, skill triggering and description design*

## State of Practice

Skills have moved from a novelty to the default unit in which agent capability is packaged and shipped — FactSet abandoned its proprietary "blueprints" format for them, OpenGov's product teams each author their own, and one YC-adjacent operator describes 300 skills backing 40 agents. The mechanics practitioners agree on are narrow and specific: the skill body is a folder, not a file; only the name and description live permanently in context (roughly 100-200 tokens per skill, paid on every model call), so the main skill.md is a thin index — capped at 100 lines by Amazon's AGI Lab team, under 500 lines per Google DeepMind's Skill Bench — with branch-specific reference material deferred behind context pointers. Measured effects are modest but real: ~15% average task improvement across ~100 Skill Bench tasks, ~10x less context overhead than the equivalent MCP tool definitions, and 66%→76%→80% on tau-bench as memories consolidate into skills. The dominant failure mode is not bad skill content but bad routing: half of observed skill failures are the skill never firing, descriptions are the routing signal and must be phrased as the user would phrase the request, and one FactSet skill broke on a model upgrade with zero lines changed because the newer model attended to the beginning of the file and ignored instructions at the end. Two things are converging fast — that AI-generated skills measurably underperform human-written ones, and that a skill without evals is wishful thinking. What remains open is who invokes skills, who writes them, and whether piling skills into one agent scales past a few dozen.

## Consensus

### A skill is a folder, not a document: skill.md should be a small index that defers detail to other files, because progressive disclosure is what keeps skills cheap.

Support: **5** talk(s)

> "we've kind of set a hard limit for like 100 lines in your skill.md cuz your skill is really a folder."
>
> — [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [14:29](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=869s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### The skill description is a permanent per-call token cost and the sole routing signal, so description quality — not body quality — determines whether a skill fires at all.

Support: **4** talk(s)

> "the description is the cost you always pay on every model invocation. So, on every model call, the description is part of the model context. So, you always pay that 100 200 tokens cost"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [7:41](https://www.youtube.com/watch?v=0vphxNt4wyk&t=461s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### Skills should not ship without evals, and a skill change should not merge unless it improves them.

Support: **4** talk(s)

> "it's very important to run evals and skills without evals are really just wishful thinking"
>
> — [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)

### Skills are the unit in which product features and business logic now ship, which pushes authorship out from the core agent team to product teams and non-engineers.

Support: **5** talk(s)

> "this is the great place to keep your business logic that shapes your agents behavior. So skills are the new features."
>
> — [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [3:05](https://www.youtube.com/watch?v=7jjudsEhBtM&t=185s)

Supporting talks: [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

### Human-written skills outperform AI-generated ones; letting a model author your skills degrades performance and inflates token cost.

Support: **4** talk(s)

> "human-written skills are the best we can provide. Uh AI-generated skills can uh impact performance negatively. And that skills or skills.md files should be below 500 lines of words."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [4:46](https://www.youtube.com/watch?v=0vphxNt4wyk&t=286s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Content Is Code](../talks/content-is-code.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)

### Skills must be managed as software artifacts — versioned, owned, access-scoped, audited — not as disposable prompt documents.

Support: **4** talk(s)

> "skills are software which can take weeks to build so that we should actually start versioning them, evaluating and testing them, and actually writing good skills."
>
> — [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [26:20](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1580s)

Supporting talks: [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)

### Loading many skills into one agent measurably degrades it; skill count is a context budget that has to be actively managed.

Support: **4** talk(s)

> "there's lots of research out there that shows that if you use very many of these, it actually makes your agent substantially worse"
>
> — [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [9:03](https://www.youtube.com/watch?v=spNAUEgq_A8&t=543s)

Supporting talks: [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### If the procedure is a fixed sequence with an exact answer, it belongs in deterministic code or a script, not in a skill invoked by a model.

Support: **4** talk(s)

> "If you have those type of use cases, you should not use skills. You maybe you should write a script because if the the process or the workflow is always the same, you don't need to waste models and tokens for that exercise."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [8:49](https://www.youtube.com/watch?v=0vphxNt4wyk&t=529s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)

## Disagreements

### Should skills be invoked by the model or explicitly by the user?

| Position A | Position B |
|---|---|
| Prefer user-invoked skills: model invocation is unpredictable (the model may simply decline to follow a context pointer), which forces you into eval work purely to confirm the skill fires; explicit invocation eliminates that class of problem at the cost of user cognitive load, and fits routine dev workflows like opening a PR.<br>*[Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)* | Prefer model-driven invocation: in products aimed at non-technical users, expecting them to remember and name skills is unacceptable cognitive load — customers do not start prompts with 'use the refund skill' — so invocation must be inferred from the request and the description tuned as a routing signal.<br>*[Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)* |

*Why it matters: Model invocation makes the description the highest-leverage artifact in the skill and makes trigger evals mandatory (half of observed failures are non-triggering); user invocation moves that burden to UX and skill discoverability instead. The two lead to entirely different eval suites and different skill-library sizes.*

### Should skills be hand-authored by humans, or captured and rewritten automatically from agent traces and usage?

| Position A | Position B |
|---|---|
| Skills must be human-written and human-curated. LLM-generated skills consume more tokens and reasoning time and can hurt performance; most published community skills are low quality because they were generated with no regard for contents or structure, and agent-written skills are where no-ops proliferate.<br>*[Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Content Is Code](../talks/content-is-code.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)* | Skills should be captured automatically from what the system observes. A dedicated skill-authoring interface won't work — capture the user's conventions from product usage; consolidate accumulated memories into skills after roughly ten; reflect at the end of each task and write back new skills; convert every task the agent succeeds at into a reusable skill file.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* |

*Why it matters: If skills must be hand-written, the skill library is bounded by scarce human attention and needs governance, ownership, and PR-style admission gates; if they can be harvested from traces, the library grows on its own and the hard problems shift to dependency tracking and approval queues — one team reports self-improving skills routinely breaking downstream dependents.*

### Does adding skills to one general-purpose agent scale, or do you eventually need to split into separate narrower agents?

| Position A | Position B |
|---|---|
| Tools and skills are a sufficient abstraction — no additional orchestration primitives needed. Build one general-purpose agent engine and deliver all domain specialization through a skills folder; production agents like Codex and Claude Code ship with only a handful of tools, and skills can replace most MCP usage.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)* | Stacking skills, MCP servers, and tools into one context is functionally inheritance and breaks down the same way: past roughly ten skills the system prompt approach stops working and you need shortlisting or embedding retrieval; at hundreds you need hierarchy, metadata filters, and governance; or you abandon the single agent for narrow domain-specific agents that talk to each other in English.<br>*[Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Build Systems, Not Code](../talks/build-systems-not-code.md)* |

*Why it matters: This determines whether your skill library needs a retrieval layer and hierarchy at all, and whether the ~80% token-efficiency and 137x cost gap from running narrow agents on cheap models is available to you — or whether you keep paying frontier-model prices for a single agent carrying every skill's description.*

### Are skills durable infrastructure or temporary scaffolding that better models will obsolete?

| Position A | Position B |
|---|---|
| Capability skills are temporary — they teach models what they cannot yet do consistently, and evals are what tell you when to retire them. Structured-decomposition scaffolds are the chain-of-thought of this era and will be needed less as models are post-trained to decompose; keep the eval after you delete the skill.<br>*[Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* | The accumulated skill and context layer is the durable asset — model quality is rented, the brain is owned. Teachability is becoming an enterprise evaluation criterion alongside security and SLAs, and context, not models, is what differentiates a company once everyone has the same intelligence.<br>*[Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)* |

*Why it matters: It decides whether skill investment is amortized capital or a depreciating hedge against current model gaps — and therefore whether you staff engineers to maintain a skill library indefinitely or plan to delete most of it at the next model upgrade. Note both sides partly agree via the capability/preference split: preference and business-context skills are durable either way.*

## Practical Guidance

**Do:**

- Cap skill.md at ~100 lines (Amazon AGI Lab) or at minimum under 500 lines (Skill Bench 1.1); push branch-specific reference material into separate files behind context pointers.
- Budget the first prompt's baseline context at 20-25K tokens; 40-50K means progressive disclosure has failed.
- Write descriptions in the phrasing of the user's request, not as a description of the skill, and make descriptions mutually distinct — they are the routing signal.
- Include explicit negative cases in the description stating when not to use the skill; build ~5 happy-path and ~5 should-not-trigger eval cases per skill to catch over-triggering.
- Run evals both with the skill loaded and without it — that comparison is the only way to know whether the skill helps and when to retire it.
- Run skill evals in isolated workspaces; coding agents will otherwise cheat by reading prior chats and executions.
- Run 3-6 trials per eval case (agents are non-deterministic) and test across multiple harnesses — a skill strong on Gemini can be weak on Codex.
- Re-run every eval on model upgrade: skills are contracts versioned against a specific model, and instruction placement inside the file is model-dependent.
- Measure task outcome, not whether the skill loaded on a given turn.
- Gate skill changes in CI: no merge unless the diff improves the test cases. Regex assertions cover most cases — LLM-as-judge is usually unnecessary.
- Decompose the skill library by user intent, not by data model ('pre-market briefing skill', not 'analyst rating skill'), and expect to refactor the decomposition as real use cases arrive.
- Assign named owners, semantic versioning with deprecation warnings and changelogs, PR-style admission gates with a human in the loop, and allow-listed access-controlled tools per skill.
- Add a shortlisting step — embedding similarity or a small model — once you pass ~10 skills; add hierarchy and metadata filters at hundreds.
- Use leading words that the agent will echo ('thin vertical slice'); confirm they work by finding them repeated in the reasoning traces.
- Give the skill exactly one source of truth per instruction — no duplication between steps and reference material.
- Teach taste and domain craft in the skill, not language or framework syntax the model already knows.
- Keep evals after retiring a skill; they become regression tests that tell you when to bring it back.

**Avoid:**

- Letting an agent write your skills unreviewed — AI-generated skills burn more tokens and reasoning time and can measurably hurt performance; they are also where no-ops accumulate.
- No-op instructions the agent would follow anyway if deleted ('make the implementation easy to read') — delete them for the token savings even when eval scores are unchanged.
- Using a skill for a fixed, always-identical workflow; write a script.
- Treating a massive skill as the problem — it is a symptom of duplication, sediment from multiple contributors, or no-ops.
- Blaming skill content for failures without checking triggering first: ~50% of observed failures are the skill never firing.
- Installing large numbers of skills into one agent, or pulling community/marketplace skills without auditing them — marketplaces lack verification controls today, roughly where NPM was ten years ago.
- Treating skills as documentation; they are contracts against a model.
- Placing critical instructions at the end of a skill file — a newer model attended to the beginning and ignored them, with no lines changed.
- Building a separate user-facing interface for authoring skills — in vertical products it doesn't get used; capture conventions from observed usage instead.
- Letting skills self-improve without dependency and impact tracking — evolving skills break downstream consumers.
- Hardcoding context into individual agents or giving each agent its own memory: it produces context sprawl, prevents a single version of truth, and the context is lost at each framework migration.

## Notable Outliers

- A skill file should be treated as an employee — one capability, one job, written clearly enough that someone can execute it; working with a coding agent is hiring, training, and managing a workforce made of markdown. ([Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [4:11](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=251s))
- Splitting a process into separate skills so the agent sees only one step at a time increases the legwork it does on the current step — hiding the future goal is itself a technique. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [15:46](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=946s))
- A FactSet skill failed after a model upgrade with not a single line changed, because the newer model focused on the beginning of the file and ignored critical instructions at the end. ([Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s))
- Skills impose roughly 10x less context overhead than the equivalent MCP setup — 15 MCP servers consume over 100,000 tokens per session in tool definitions alone. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s))
- Skills executing on the agent's own machine with no process isolation is a genuine security weakness relative to MCP, and skill marketplaces are as unsafe today as NPM was ten years ago. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [24:54](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1494s))
- Skill descriptions should be written to match how the user phrases the request rather than to describe the skill — descriptions are routing signals, not documentation. ([Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [9:23](https://www.youtube.com/watch?v=7jjudsEhBtM&t=563s))
- Agent skills should teach taste and domain craft rather than framework syntax, because the model already knows HTML/CSS/JS natively and teaching it a framework reduces output creativity. ([HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [9:32](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=572s))
- There is still no shared rubric for judging whether a skill is good — you cannot yet look at a skill and say what it is doing well or badly. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [1:44](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=104s))
- Wrapping query access in structured skills produced more consistent agent results than letting the agent author queries freely, which created large variance in evals. ([From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [12:49](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=769s))
- Consolidating accumulated memories into skills after roughly ten memories raised tau-bench policy-following from 76% to 80%, and can repair stale system prompts that reference database columns no longer in existence. ([User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s))

## All Talks

- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)
- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Content Is Code](../talks/content-is-code.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)
- [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [The Base Model Is Dead](../talks/the-base-model-is-dead.md)
- [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)
- [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)
- [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)
- [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)
- [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Angie Jones](../speakers/angie-jones.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Benjamin Guo](../speakers/benjamin-guo.md)
- [Corey Gallon](../speakers/corey-gallon.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [Erik Hanchett](../speakers/erik-hanchett.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Garry Tan](../speakers/garry-tan.md)
- [James Russo](../speakers/james-russo.md)
- [Jason Lopatecki](../speakers/jason-lopatecki.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [May Walter](../speakers/may-walter.md)
- [Nicholas Arcolano](../speakers/nicholas-arcolano.md)
- [Paul Iusztin](../speakers/paul-iusztin.md)
- [Philipp Schmid](../speakers/philipp-schmid.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)
- [Rob Cheung](../speakers/rob-cheung.md)
- [Sina Shahandeh](../speakers/sina-shahandeh.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

