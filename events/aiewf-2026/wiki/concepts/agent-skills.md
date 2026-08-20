---
title: "agent skills"
type: "concept"
slug: "agent-skills"
tier: "core"
maturity: "consolidating"
talk_count: 29
speaker_count: 29
---

# agent skills

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **29** talk(s) by **29** speaker(s)

**Definition:** Packaged, model-invocable units of procedural knowledge (instructions plus optional resources) that extend an agent's capabilities without retraining or hard-coding.

*Also referred to as: agent skills design, skill files, agent skills and plugins, skill decomposition, capability vs preference skills, model-invoked vs user-invoked skills, skill triggering and description design*

## State of Practice

Skills have crossed from novelty to default packaging unit for procedural knowledge: they are the progressive-disclosure answer to context pressure (a ~100-token description in the system prompt, a body loaded on demand, scripts behind that), and multiple speakers now treat them as the shipping unit of product features rather than as prompt scraps. The measured effect is real but modest — roughly 15% average improvement across ~100 tasks on Skill Bench 1.1 — and it is fragile: human-written skills beat AI-generated ones, which can actively degrade performance by burning tokens and reasoning time. The dominant failure mode is not bad skill content but bad routing: about half of observed skill failures are the skill never triggering, which makes the description (written in the user's phrasing, with explicit negative cases) the highest-leverage line in the file. Size discipline is near-universal — hard caps cited at 100 lines (skill.md as a thin index into a folder) and under 500 lines — with duplication, sediment, and no-op instructions named as the reasons skills bloat. At enterprise scale the problems shift from authoring to library management: past ~10 skills the system prompt stops being a viable registry and you need shortlisting/embedding retrieval; at hundreds you need hierarchy, metadata filters, named owners, semantic versioning, and admission gates. Everyone building seriously says the same thing about verification: skills are model-versioned contracts, so they need evals run with and without the skill loaded, in isolated workspaces, across multiple harnesses.

## Consensus

### Skills must be kept small and use progressive disclosure — a short description plus a thin index file that points to detail elsewhere — because the description is a permanent per-request context cost.

Support: **6** talk(s)

> "we've kind of set a hard limit for like 100 lines in your skill.md cuz your skill is really a folder."
>
> — [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [14:29](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=869s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)

### Human-written skills outperform LLM-generated ones; auto-generated skills are typically low quality and can hurt performance.

Support: **4** talk(s)

> "human-written skills are the best we can provide. Uh AI-generated skills can uh impact performance negatively. And that skills or skills.md files should be below 500 lines of words."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [4:46](https://www.youtube.com/watch?v=0vphxNt4wyk&t=286s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Content Is Code](../talks/content-is-code.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)

### Skills are software artifacts and must be evaluated, versioned, and governed like code — not treated as disposable documentation.

Support: **4** talk(s)

> "Skills are not the documentation and a lot of people treat them like that and skills are really the contracts versioned to a model."
>
> — [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

### The skill description is the routing signal and the primary point of failure: it must match how users phrase requests and be distinct from sibling skills, or the right skill never fires.

Support: **3** talk(s)

> "we have seen 50% of the failures uh because the skill was not triggered correctly because the prompt of the user was not uh detailed enough"
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [17:04](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1024s)

Supporting talks: [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)

### Skills are the interface that lets non-engineers — domain experts, product staff, clinicians, finance teams — extend an agent's capability without engineering changes.

Support: **5** talk(s)

> "I feel like skills are really an amazing interface between AI engineers and domain experts, especially in vertical AI."
>
> — [Don’t be data poor](../talks/dont-be-data-poor.md), [13:43](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=823s)

Supporting talks: [Don’t be data poor](../talks/dont-be-data-poor.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)

### Skills should encode domain judgment, taste, and organizational conventions — not restate framework syntax or things the model would do anyway.

Support: **4** talk(s)

> "Our skill is focused on taste and video aspects because the LLMs and agents already know how to write HTML and CSS and JavaScript, we don't have to teach them the language, we just teach them how to create good videos."
>
> — [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [9:32](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=572s)

Supporting talks: [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)

### A fixed, fully deterministic sequence of steps should be a script or plain code, not a skill or an agent.

Support: **4** talk(s)

> "If you have those type of use cases, you should not use skills. You maybe you should write a script because if the the process or the workflow is always the same, you don't need to waste models and tokens for that exercise."
>
> — [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [8:49](https://www.youtube.com/watch?v=0vphxNt4wyk&t=529s)

Supporting talks: [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)

### Successful agent runs should be captured back as reusable skills so the organization compounds knowledge rather than repeating one-off work.

Support: **4** talk(s)

> "The organization that captures what it learns like this gets smarter every single day. The one that doesn't wakes up every morning with amnesia, no matter how good the model is. Model quality is rented, but if you build your brain, you you own that brain."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [16:06](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=966s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

## Disagreements

### Should skills be invoked by the model automatically, or explicitly by the user?

| Position A | Position B |
|---|---|
| Prefer user-invoked skills: model invocation is unpredictable, forces you to eval trigger behavior, and puts a permanent description tax in context for every skill you install. Accept higher user cognitive load in exchange for determinism.<br>*[Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)* | Model-driven invocation is required in products, because end users of a customer-facing agent have no idea skills exist and cannot be asked to name one; the fix is better descriptions and retrieval, not shifting the burden to users.<br>*[Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* |

*Why it matters: It determines whether you invest in trigger evals and a routing layer (embedding shortlisting, hierarchy, negative cases) or in a slash-command surface and user education — and whether your skill library can scale past ten entries at all.*

### Can a skills folder replace MCP servers for most agent capability?

| Position A | Position B |
|---|---|
| Skills largely supersede MCP: they impose ~10x less context overhead via progressive disclosure, and production agents like Codex and Claude Code ship with only a handful of tools — MCP stays only for auth, process isolation, restricted-environment data, and remote compute. Similarly, CLI tools beat MCP servers on reuse, speed, and token cost for the same success rate.<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* | MCP is still maturing and remains valuable — including as the practical distribution and integration layer — and skills executing unsandboxed on the agent's own machine are a real security regression relative to MCP's separate process.<br>*[Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* |

*Why it matters: It decides where a vendor invests integration effort — publishing a skills package versus hosting an MCP server — and whether skill marketplaces need NPM-style verification before enterprises can safely install third-party skills.*

### Does adding more skills to an agent make it better or measurably worse?

| Position A | Position B |
|---|---|
| Loading many skills into one agent degrades it: it is effectively inheritance, hits diminishing returns, and breaks down; the answer is many narrow domain-specific agents each carrying a minimal context.<br>*[The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)* | One general agent entry point with a large, governed skill library is workable — hundreds of skills across dozens of agents, scaled via shortlisting, hierarchy, metadata filters, and ownership rather than by splitting the agent.<br>*[Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)* |

*Why it matters: One path invests in per-domain agent fleets and inter-agent communication; the other invests in retrieval and governance over a shared library. They produce incompatible platform architectures and very different token cost profiles.*

### Should skills be authored deliberately by humans, or captured/evolved automatically from usage and traces?

| Position A | Position B |
|---|---|
| Author them by hand: human-written skills measurably outperform generated ones, a skill is only as good as the human who wrote it, and no-ops and sediment are especially common when an agent writes your skills.<br>*[Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Content Is Code](../talks/content-is-code.md)* | Capture them automatically: a dedicated skill-authoring interface won't work for users, so skills should be derived from observed product usage, reflection at end of task, or consolidated from accumulated memories after ~10 entries.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* |

*Why it matters: Automatic capture is the only route to skills that reflect each user's last-20% conventions at scale, but if generated skills genuinely degrade performance, the capture pipeline needs an eval gate and a human approver — which is exactly the compromise the context-layer talk proposes.*

## Practical Guidance

**Do:**

- Cap skill.md at ~100 lines (hard limit) or at minimum under 500 lines, treating the skill as a folder with the main file as a thin index into reference files.
- Write descriptions in the phrasing of user requests rather than describing the skill itself, and make sibling descriptions clearly distinct from one another.
- Include explicit negative cases in the description — roughly five happy-path and five 'do not use this skill' eval cases — to stop over-triggering.
- Run evals both with the skill loaded and without it, so you know whether the skill helps and when the model has outgrown it.
- Run skill evals in isolated workspaces; coding agents will otherwise cheat by reading prior chats or previous executions in the environment.
- Run 3–6 trials per eval case, since agents are non-deterministic, and test across multiple harnesses because a skill good on Gemini may fail on Codex.
- Gate skill merges on eval improvement in CI — do not merge a skill diff that fails to improve the test cases.
- Rerun all skill evals on every model upgrade; skills are contracts versioned against a specific model, and instruction placement inside the file is model-dependent.
- Keep evals after retiring a skill; they become regression tests that tell you when to bring it back.
- Prefer cheap regex assertions over LLM-as-judge for most skill evals.
- Move reference material used by only one branch out of skill.md and behind a context pointer.
- Use leading words (e.g. 'thin vertical slice') and confirm they are working by looking for the agent echoing them in its reasoning traces.
- Split a multi-step process into separate skills so the agent sees only one step at a time — hiding future steps increases the legwork it does on the current one.
- Decompose the skill library by user intent (a 'pre-market briefing' skill), not by data model (an 'analyst rating' skill), and refactor the decomposition as real use cases arrive.
- Introduce shortlisting — embedding similarity or a small routing model — once you pass roughly ten skills; add hierarchy, metadata filters, and governance at hundreds.
- Assign named owners, semantic versioning with deprecation warnings and changelogs, PR-style admission gates, and periodic audits to the enterprise skill library.
- Declare an allow-list of tools per skill and access-control those tools.
- Focus skills on taste, domain craft, and organizational conventions the model does not already know, rather than on language or framework syntax.
- Wrap data/query access in structured skills instead of letting the agent author queries freely — it cuts eval variance substantially.
- Audit community-authored skills against a rubric before pulling them into your environment.
- Budget the first prompt's baseline context at ~20–25K tokens; 40–50K means progressive disclosure has failed.
- Give domain experts (clinicians, finance staff, product teams) direct ownership of the skills that encode their judgment.

**Avoid:**

- Do not let an LLM generate your skills unreviewed — generated skills consume more tokens and reasoning time and can degrade performance outright.
- Do not use a skill for a fixed, always-identical workflow; write a script.
- Do not leave no-ops in a skill — if deleting the instruction wouldn't change agent behavior, delete it; the token savings stand even when evals are flat.
- Do not duplicate content across steps and reference material; every part of a skill needs a single source of truth.
- Do not let skill files accumulate sediment from many contributors who add but never delete; massive skills are always a symptom of duplication, sediment, or no-ops.
- Do not eval whether the skill loaded on turn one; eval whether the task outcome was achieved.
- Do not build a separate user-facing skill-creation interface and expect users to fill it — capture conventions from observed usage instead.
- Do not maintain a proprietary skill-like format now that the skills standard is open — FactSet abandoned its own 'blueprints' format.
- Do not install large numbers of skills, MCP servers, and tools into a single agent's context and expect it to hold up.
- Do not let self-improving skills evolve autonomously without dependency and impact tracking — evolving skills break downstream dependents.
- Do not install skills from marketplaces without verification controls; the ecosystem is where NPM was ten years ago.
- Do not assume a skill that works in your harness works elsewhere, or that instructions at the end of the file will be read — a newer model focused on the beginning and ignored critical trailing instructions.
- Do not treat skills as documentation; they are model-versioned contracts and skills without evals are wishful thinking.

## Notable Outliers

- About 50% of skill failures come from the skill not being triggered at all, rather than from bad skill content — making description quality, not body quality, the dominant lever. ([Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [17:04](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1024s))
- Skills divide into capability skills (teaching models what they can't yet do consistently — temporary, will be obsoleted by better models) and preference skills (durable), and evals are what tell you when a capability skill can be retired. ([Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [3:12](https://www.youtube.com/watch?v=0vphxNt4wyk&t=192s))
- Skills impose roughly 10x less context overhead than the equivalent MCP setup; connecting an agent to 15 MCP servers burns over 100,000 tokens per session in tool definitions alone. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s))
- In agent-fronted products, skills replace UI surfaces as the unit in which features ship, and the engineer's job shifts from shipping features to shipping harnesses. ([Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [4:01](https://www.youtube.com/watch?v=7jjudsEhBtM&t=241s))
- A skill file is an employee — one capability, one job, written down clearly enough that someone can execute it — so working with a coding agent is hiring and managing a workforce made of markdown. ([Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [4:11](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=251s))
- Splitting a process into separate skills so the agent sees only one step at a time increases the legwork it does on the current step, by hiding the future goal from it. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [15:46](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=946s))
- Skills running on an agent harness let a clinician add an entirely new document type to a synthetic-data pipeline with zero engineering changes. ([Don’t be data poor](../talks/dont-be-data-poor.md), [13:43](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=823s))
- Skills executing on the agent's own machine with no process isolation is a genuine security weakness relative to MCP, and today's skill marketplaces lack verification controls. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [24:54](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1494s))
- There is still no shared rubric for judging whether a skill is good — organizations have no way to turn their operating procedures into things an agent can reliably do. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [1:44](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=104s))
- After roughly ten accumulated memories, the agent should bake the learned reasoning into skills — measured as tau-bench policy-following going from 66% to 76% with memory, and to 80% once consolidated into skills. ([User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [6:23](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=383s))

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
- [Don’t be data poor](../talks/dont-be-data-poor.md)
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
- [Anuj Iravane](../speakers/anuj-iravane.md)
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

