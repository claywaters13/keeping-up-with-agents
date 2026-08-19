---
title: "agent skills"
type: "concept"
slug: "agent-skills"
tier: "core"
maturity: "consolidating"
talk_count: 28
speaker_count: 28
---

# agent skills

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **28** talk(s) by **28** speaker(s)

**Definition:** Packaged, model-invocable units of procedural knowledge (instructions plus optional resources) that extend an agent's capabilities without retraining or hard-coding.

*Also referred to as: agent skills design, skill files, agent skills and plugins, skill decomposition, capability vs preference skills, model-invoked vs user-invoked skills, skill triggering and description design*

## State of Practice

Skills have moved from a novelty to the default unit in which teams ship agent capability: FactSet describes them as replacing screens and buttons as the feature primitive, OpenGov has every product team authoring them behind one entry point, and YC-backed companies encode operating procedures as skill files maintained by dedicated engineers. The mechanical craft has converged fast — a skill is a folder, not a file; skill.md stays small (100-line and 500-line caps were both stated as hard limits) with detail deferred behind context pointers; the description is the only part you pay for on every model call, so it is written to match how users phrase requests, includes negative cases, and doubles as the routing signal. Measured results are modest and specific: ~15% average task improvement across ~100 tasks on Skill Bench 1.1, ~10x less context overhead than the equivalent MCP tool definitions, and roughly 50% of skill failures traced to the skill never triggering rather than to bad content. The strongest shared warning is that AI-generated skills actively degrade performance — they accumulate no-ops, duplication, and sediment — so human authorship plus regex-level evals run with and without the skill loaded is the emerging bar. What is not settled is everything above the single-skill level: whether invocation should be model-driven or user-driven, whether a flat markdown folder survives past ten or a hundred skills, and whether the whole layer is a durable company asset or scaffolding that better-post-trained models will absorb.

## Consensus

### Keep skill.md small and defer detail to sibling files: the main file is a thin index, with progressive disclosure doing the work.

Support: **5** talk(s)

> "we've kind of set a hard limit for like 100 lines in your skill.md cuz your skill is really a folder."
>
> — [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [14:29](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=869s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### The description is the permanent per-call tax and the routing signal — it must be written for retrieval (matching user phrasing, distinct from siblings, with negative cases), not as a summary of the skill.

Support: **4** talk(s)

> "the description is the cost you always pay on every model invocation. So, on every model call, the description is part of the model context. So, you always pay that 100 200 tokens cost"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [7:41](https://www.youtube.com/watch?v=0vphxNt4wyk&t=461s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### Human-written skills outperform LLM-generated ones; letting an agent author your skills produces no-ops, bloat, and measurable performance loss.

Support: **4** talk(s)

> "human-written skills are the best we can provide. Uh AI-generated skills can uh impact performance negatively. And that skills or skills.md files should be below 500 lines of words."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [4:46](https://www.youtube.com/watch?v=0vphxNt4wyk&t=286s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Content Is Code](../talks/content-is-code.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)

### If the procedure is a fixed deterministic sequence, write a script or plain code — do not spend model tokens on it via a skill or agent.

Support: **5** talk(s)

> "If you have those type of use cases, you should not use skills. You maybe you should write a script because if the the process or the workflow is always the same, you don't need to waste models and tokens for that exercise."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [8:49](https://www.youtube.com/watch?v=0vphxNt4wyk&t=529s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)

### Skills are software artifacts, not documentation: they require evals gating merges, versioning against a specific model, named owners, and re-testing on model upgrade.

Support: **4** talk(s)

> "it's very important to run evals and skills without evals are really just wishful thinking"
>
> — [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s)

Supporting talks: [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

### Skills should teach taste, conventions, and org-specific procedure — the last 20% the model cannot infer — not language or framework syntax the model already knows.

Support: **5** talk(s)

> "Our skill is focused on taste and video aspects because the LLMs and agents already know how to write HTML and CSS and JavaScript, we don't have to teach them the language, we just teach them how to create good videos."
>
> — [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [9:32](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=572s)

Supporting talks: [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Content Is Code](../talks/content-is-code.md)

### The dominant failure mode is non-invocation, not bad skill content — the model silently declines to follow the pointer or loads the wrong skill.

Support: **4** talk(s)

> "every time you have a context pointer pointing from one resource to another, the model may just choose not to follow it, you know, even if it's absolutely perfect for the task, it may just choose not to invoke the skill."
>
> — [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [6:25](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=385s)

Supporting talks: [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)

## Disagreements

### Is the skills layer a durable competitive asset, or temporary scaffolding that better models will absorb?

| Position A | Position B |
|---|---|
| Skills and the accumulated company brain are the durable moat — model quality is rented, the harness will not disappear, and teachability is becoming a standard enterprise evaluation criterion.<br>*[Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)* | Most of what skills encode is scaffolding for current model weaknesses: capability skills should be retired as models improve, hierarchical decomposition prompting is the new chain-of-thought and will fade with better post-training, and self-orchestrating models already need no custom tooling.<br>*[Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* |

*Why it matters: It determines whether skill authoring is a standing organizational investment with owners, versioning, and governance, or a maintenance cost you should be actively deleting each time a model ships.*

### Does a skill/knowledge library scale as plain markdown files, or does it need retrieval, hierarchy, and governance infrastructure?

| Position A | Position B |
|---|---|
| Flat markdown plus a reference index is sufficient and preferable — skip vector DBs, knowledge graphs, and semantic search entirely.<br>*[Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* | Flat file loading breaks at scale: past ~10 skills you need embedding-based shortlisting, past hundreds you need hierarchy, metadata filters, admission gates and ownership; markdown memory stops working once data exceeds the context window and graph traversal beats speculative loading.<br>*[Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)* |

*Why it matters: It decides whether skill libraries are a git repo of folders or a piece of retrieval infrastructure with its own lifecycle management, and how much a team should build before hitting the wall.*

### Should skills be invoked by the model or explicitly by the user?

| Position A | Position B |
|---|---|
| Prefer user-invoked: it eliminates invocation unpredictability and the eval burden that comes with it, and fits routine dev workflows like PR creation, at the cost of user cognitive load.<br>*[Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)* | Model-driven invocation is required in products, because non-technical end users have no idea skills exist and should not be asked to remember them; the fix is better descriptions and evals, not shifting the burden to users.<br>*[Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* |

*Why it matters: Model-invoked skills force a permanent description tax in context plus trigger evals; user-invoked ones remove that whole failure class but are unavailable in any consumer-facing agent.*

### Are tools plus skills a sufficient abstraction, or must capability be split across separate scoped agents?

| Position A | Position B |
|---|---|
| Tools and skills are all you need — build one general-purpose agent engine and deliver domain specialization through skills.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)* | Piling skills, MCP servers and tools into one agent is inheritance and degrades performance; capability belongs in many narrow domain-specific agents composed together, each with its own loop, context and sandbox.<br>*[The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Build Systems, Not Code](../talks/build-systems-not-code.md)* |

*Why it matters: One side invests in skill-library governance and retrieval for a single agent; the other invests in multi-agent composition and per-agent sandboxing, and reports >80% token savings from narrow scoping.*

## Practical Guidance

**Do:**

- Cap skill.md at ~100 lines (500 max) and treat the skill as a folder, with reference material for a single branch moved out behind a context pointer.
- Budget the baseline first prompt at 20–25K tokens of context; 40–50K means progressive disclosure has failed.
- Write the description to mirror how users phrase requests, keep descriptions distinct from each other, and include explicit negative cases for when not to use the skill.
- Build ~5 happy-path and ~5 should-not-trigger eval cases per skill, run 3–6 trials each because agents are non-deterministic, and block the merge if the diff doesn't improve them.
- Run every eval both with and without the skill loaded, and keep the eval after retiring the skill as a regression test that signals when to bring it back.
- Run skill evals in isolated workspaces — coding agents will otherwise cheat by reading prior chats and executions.
- Use cheap regex assertions for most skill evals rather than LLM-as-judge, and test on task outcome rather than whether the skill loaded on turn one.
- Test skills across multiple harnesses and re-run evals on every model upgrade; skills are contracts versioned to a specific model.
- Use leading words (e.g. 'thin vertical slice') and verify they landed by watching the agent repeat them in its reasoning traces.
- Cut the skill library by user intent (a 'pre-market briefing' skill), not by your data model (an 'analyst rating' skill).
- Wrap data/query access in structured skills instead of letting the agent author queries freely — it cuts eval variance.
- At enterprise scale, gate skill admission with PR-style human review, name an owner per skill, use semantic versioning with deprecation warnings, and allow-list the tools each skill may call.
- Convert every agent task that succeeds into a reusable skill file; capture skills from observed usage rather than shipping a separate skill-authoring UI.

**Avoid:**

- Generating skills with an LLM and shipping them — they hurt performance, and no-ops are especially common when an agent writes your skills.
- Writing a skill for a workflow that is always the same fixed sequence; make it a script.
- Instructions the agent would follow anyway if deleted (no-ops), duplication across steps and reference material, and 'sediment' from contributors who won't delete each other's text.
- Assuming a huge skill is the problem — it is a symptom of duplication, sediment, or no-ops underneath.
- Putting critical instructions at the end of a skill file: a newer model focused on the beginning and ignored them with no other change.
- Keeping all skills in the system prompt past ~10; and expecting flat retrieval to hold at hundreds.
- Pulling community or marketplace skills in unaudited — marketplaces lack verification controls, and remember skills execute unisolated on the agent's machine.
- Treating skills as documentation, or as disposable prompt files exempt from versioning and testing.
- Loading everything speculatively into context (markdown-memory dumps of 100k tokens per round) instead of using progressive disclosure.

## Notable Outliers

- Connecting an agent to 15 MCP servers burns over 100,000 tokens per session in tool definitions alone; skills impose roughly 10x less context overhead for the same capability. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s))
- Roughly 50% of skill failures come from the skill never being triggered, not from bad skill content. ([Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [17:04](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1024s))
- Consolidating accumulated memories into skills after about ten entries lifted tau-bench policy-following from 66% to 76% with memory alone, and to 80% once baked into skills. ([User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s))
- A skill that passed began failing on a newer model with not a single line changed, because the model attended to the beginning of the file and ignored critical instructions at the end. ([Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s))
- Installing many skills into one agent measurably degrades it — loading skills, MCP servers and tools into one context is inheritance, and inheritance eventually breaks down. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [9:03](https://www.youtube.com/watch?v=spNAUEgq_A8&t=543s))
- Splitting a process into separate skills so the agent sees only one step at a time increases the legwork it does on the current step, by hiding the future goal. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [15:46](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=946s))

## All Talks

- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)
- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Autonomous Agents for Scientific Tasks](../talks/autonomous-agents-for-scientific-tasks.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)
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
- [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md)
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
- [Ben Holmes](../speakers/ben-holmes.md)
- [Benjamin Guo](../speakers/benjamin-guo.md)
- [Corey Gallon](../speakers/corey-gallon.md)
- [Ekaterina Deyneka](../speakers/ekaterina-deyneka.md)
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

