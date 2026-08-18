---
title: "skill marketplaces"
type: "concept"
slug: "skill-marketplaces"
tier: "supporting"
maturity: "contested"
talk_count: 11
speaker_count: 13
---

# skill marketplaces

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **11** talk(s) by **13** speaker(s)

**Definition:** Distribution and governance of agent extensions — registries, app stores, vetting, and internal catalogs.

*Also referred to as: internal skill marketplace, skill registry, agent app stores, agent distribution channels, skill library governance, agent discovery, decentralized agent registries*

## State of Practice

As of this conference the distribution layer for agent extensions has gone live faster than the governance layer beneath it: MCP Apps became the official Model Context Protocol UI extension in January 2026, ChatGPT, Claude, and Cursor all opened self-serve submission, Claude began doing dynamic MCP registry lookups when it lacks a tool for a task, and 26+ harnesses now load Anthropic-format skills. The field has converged on treating skills, plugins, MCP servers, hooks, and agent rules as supply-chain dependencies rather than config files — because a skill author is effectively writing code on other engineers' machines — and the empirical picture backs the alarm: a Snyk audit of nearly 4,000 ClawHub skills found over one in eight with a critical issue and 76 malicious payloads, and Nubank's scan of 2,000+ internal skills surfaced 1,500+ risks. The practical response has split into two camps that do not agree: an open-bazaar camp (open registries, signed agent facts, permissionless cross-org discovery, platform-level sandboxing that makes extension code untrusted-by-default) and a gated-catalog camp (a single internal marketplace as chokepoint, PR-style admission gates, hybrid deterministic+LLM scanning re-enforced in CI, named owners and semver). Underneath that is a live argument about the distribution unit itself — filesystem skills that run unsandboxed in the agent's own environment with ~10x less context overhead, versus hosted or iframe-sandboxed MCP apps that are process-isolated but heavier. Everyone agrees the catalog entry's description is the routing signal and that flat retrieval breaks somewhere around ten skills, requiring shortlisting, then hierarchy and metadata filters at hundreds.

## Consensus

### Agent extensions (skills, plugins, MCP servers, hooks, rules) are a software supply chain and must be vetted like dependencies, not treated as configuration — and today's public marketplaces have no meaningful verification.

Support: **4** talk(s)

> "in an audit that we did of nearly 4,000 skills on ClawHub, uh over one in eight had a critical severity issue, and we actually found 76 malicious payloads"
>
> — [Agentic Development Security](../talks/agentic-development-security.md), [7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s)

Supporting talks: [Agentic Development Security](../talks/agentic-development-security.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)

### Skills are software artifacts with a lifecycle — versioning, named owners, evals, and deprecation — not disposable prompt or documentation files.

Support: **3** talk(s)

> "skills are software which can take weeks to build so that we should actually start versioning them, evaluating and testing them, and actually writing good skills."
>
> — [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [26:20](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1580s)

Supporting talks: [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)

### The catalog entry's natural-language metadata is the routing mechanism — selection happens by description match, so entries must be phrased for how users ask and be mutually distinct, and flat lookup stops working as the catalog grows.

Support: **4** talk(s)

> "the descriptions are really the routing signals"
>
> — [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [8:26](https://www.youtube.com/watch?v=7jjudsEhBtM&t=506s)

Supporting talks: [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)

### Store and registry listing is now a real distribution channel with commercial consequences — presence in the catalog drives high-intent traffic and is becoming a buying criterion for the underlying product.

Support: **3** talk(s)

> "First, MCP apps. MCP servers are not only returning JSON. And that allows much richer experiences. And the second thing, maybe even bigger, is that the stores opened."
>
> — [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [4:10](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=250s)

Supporting talks: [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

## Disagreements

### Should agent extensions be distributed through an open, permissionless network, or through a curated catalog that gates admission?

| Position A | Position B |
|---|---|
| Open by default: walled gardens and proprietary agent stores are the AOL era repeating, and the right architecture is an open registry with signed agent facts, self-hosted agents, and peer-to-peer transactions after discovery. The open web proved permissionless publishing does not produce the security disaster platform gatekeepers predict; App Store-style curation shrank mobile development to ~5 companies. Safety comes from platform-level isolation (null-origin iframes, sandboxed server workers), not from vetting the publisher.<br>*[The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md), [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)* | Gate before distribution: an internal marketplace is the security boundary, every upload passes a hybrid deterministic + LLM scanner in a PR-style admission gate that can require remediation or block outright, third-party skills pulled from outside must be re-uploaded internally to get scanned, and enterprise skill libraries need named owners, allow-listed access-controlled tools, semantic versioning, and periodic audits.<br>*[We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Agentic Development Security](../talks/agentic-development-security.md)* |

*Why it matters: It decides whether the trust primitive is a cryptographic/architectural one (signed capability records, sandboxes that make malicious code inert) or an organizational one (a scanner and a human reviewer standing between publisher and consumer). The first scales across organizational boundaries and the second does not; the second catches natural-language injection and over-permissioned skills that no sandbox will flag.*

### Is the unit of distribution a filesystem skill that runs inside the agent's own environment, or a hosted/sandboxed MCP app?

| Position A | Position B |
|---|---|
| Skills. A skills folder replaces MCP for most use cases given a good base reasoning model — progressive disclosure costs ~10x less context than the equivalent MCP setup (15 MCP servers burn 100k+ tokens per session in tool definitions alone), production agents like Codex and Claude Code ship with only a handful of tools, and a custom harness needs only a skill registry, a system prompt, and a file read tool to participate. Vendors should ship one general agent engine and deliver domain specialization as skills.<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* | Hosted, isolated apps. MCP Apps is the distribution channel — write once, run everywhere across ChatGPT, Claude, and Cursor, with the widget in a sandboxed iframe, the host retaining control of the interaction flow, and the ability to split output so the model never sees privacy-sensitive data. Isolation is the point: with a null-origin iframe client and an isolated server sandbox that can only talk to each other, no security bug in the distributed code matters.<br>*[MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md)* |

*Why it matters: Skills execute on the agent's own machine with its OAuth tokens, credentials, and filesystem and no process isolation — which is exactly why one in eight audited public skills carried a critical finding. Choosing skills makes vetting the only defense; choosing sandboxed apps moves the defense into the runtime but costs context, host dependency, and the ability to reach local state.*

### Can in-band controls — a rules file, a 'ask for confirmation' instruction, an approval prompt — govern what a distributed extension is allowed to do?

| Position A | Position B |
|---|---|
| No; enforcement must be deterministic and out-of-band. Agents ignore rule files, a prompt-level confirmation request is not a human in the loop because the agent can satisfy the confirmation itself, and approval prompts stop working entirely for background and cloud agents. Model-level judgment is unreliable — Claude refused to read an .env file but complied when asked for a specific secret key — so guardrails belong in async hooks on tool calls and in CI, which re-runs local scans because you cannot assume the engineer ran them or ran the latest version.<br>*[Agentic Development Security](../talks/agentic-development-security.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)* | For individual use, AGENTS.md rules plus auto-review are sufficient, with org-level admin settings reserved for external-facing actions; current models err toward being too reluctant to take destructive actions, so over-restriction is the bigger day-to-day cost than under-restriction.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* |

*Why it matters: This sets where the marketplace's cost lands: a scanning-and-CI regime imposes latency, false positives, and a review queue on every publisher, while in-band controls impose nothing but leave a determined agent free to route around a blocked connector using computer use — a failure mode both sides acknowledge exists.*

## Practical Guidance

**Do:**

- Route third-party skills downloaded from outside through the internal marketplace so they are scanned before any engineer uses them.
- Combine deterministic scanning with LLM review — neither alone is sufficient, and LLM verdicts vary with temperature.
- Re-run the local scan again in CI after upload, since you cannot verify the engineer ran the checks or ran the current version.
- Deliver scan findings in the same pull request that uploads the skill, and always pair a finding with concrete remediation guidance.
- Emit SARIF from the skill scanner so results feed existing security tooling and the vulnerability management program.
- Grade shell-command risk per command instead of treating all shell invocations as equally dangerous.
- Have skills declare allow-listed tools, and access-control those tools, so each skill's blast radius is bounded.
- Write skill descriptions in the phrasing of the user's request rather than describing the skill, and make them mutually distinct — otherwise routing picks the wrong one.
- Decompose the catalog by user intent, not by data model (an 'earnings preparation' skill, not an 'estimate analysis' skill).
- Start shortlisting via embedding search or a small router model past ~10 skills; add hierarchy plus metadata filters at hundreds.
- Keep baseline system prompt plus tool definitions under 40% of the context window before the first user turn.
- Re-run evals on every model upgrade — a skill is a contract versioned against a specific model, and an unchanged skill file failed on a newer model that read only the beginning of the file.
- Assign named owning teams, semantic versions, deprecation warnings, and changelogs to catalog entries, and audit periodically.
- Proactively look for marketplaces other teams have spun up and instrument those too, rather than assuming one canonical catalog.
- Return alternate non-UI tool output alongside a widget so clients that lack MCP Apps support do not starve the model of information.
- Submit to the ChatGPT, Claude, and Cursor stores even if your server returns no UI — UI is not a submission requirement.
- Measure an internal AI champion by how often teammates use the plugins and skills they built, not by personal token consumption.

**Avoid:**

- Treating an 'ask for confirmation' instruction inside a skill as a human in the loop — the agent can issue and satisfy that confirmation itself.
- Assuming removal of a malicious skill undoes it: skills can modify agent memory and persist after deletion.
- Shipping low-context, weak-signal rules in a skill scanner — they cause more trouble than they are worth, and a warning that is harmless locally may be severe in production.
- Publishing findings with no remediation path.
- Relying on human approval as the governance mechanism for background and cloud agents.
- Treating skills as documentation — they are contracts versioned to a model, and skills without evals are wishful thinking.
- Publishing LLM-generated skills wholesale: they consume more tokens and reasoning time than human-written equivalents.
- Wiring an agent to 15 MCP servers — that alone burns 100,000+ tokens per session in tool definitions.
- Maintaining a proprietary skill-like format now that the skills standard is open (FactSet abandoned its 'blueprints' format).
- Expecting zero false positives from any agent-security vendor — it is not achievable, only asymptotically improvable.
- Re-rendering a heavy app view on every turn instead of persisting and updating one identified view.

## Notable Outliers

- Malicious skills can modify agent memory, so removing the skill does not remove the compromise — a persistence mechanism package ecosystems do not have. ([Agentic Development Security](../talks/agentic-development-security.md), [7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s))
- A prompt-level 'ask for confirmation' is not a human in the loop, because the AI can ask and answer the confirmation on its own behalf. ([We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [12:33](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=753s))
- LLM-generated skills measurably hurt LLM performance versus human-written ones; a skill is only as good as the human who wrote it. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [24:09](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1449s))
- Claude is currently the only client that searches the MCP registry for a connector when assigned a task it has no tool for — making registry ranking, not install count, the demand channel. ([MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [25:39](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1539s))
- One in 12 developers observed had an MCP server with a high or critical severity finding in the server itself — the risk is in the extension, not just the code it generates. ([Agentic Development Security](../talks/agentic-development-security.md), [8:29](https://www.youtube.com/watch?v=cgimkNGNjvU&t=509s))
- Slack won as an extension platform not because it is a good product but because it is the right shape for users to build the features they want into it. ([Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [14:55](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=895s))
- MCP Apps addresses a market roughly 170x the size of the Apple App Store at its launch, framing agent extensions as a distribution channel rather than a UI feature. ([MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [17:26](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1046s))
- A skill personally used for months and allowed to edit itself after failures should only then be shared with the team — the opposite of publish-early. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [14:35](https://www.youtube.com/watch?v=il1c1a2FufU&t=875s))

## All Talks

- [Agentic Development Security](../talks/agentic-development-security.md)
- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md)
- [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)
- [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)
- [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)
- [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)

## Speakers

- [Armanas Povilionis](../speakers/armanas-povilionis.md)
- [Benjamin Guo](../speakers/benjamin-guo.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [Ezra Tanzer](../speakers/ezra-tanzer.md)
- [Ido Salomon](../speakers/ido-salomon.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Kenton Varda](../speakers/kenton-varda.md)
- [Liad Yosef](../speakers/liad-yosef.md)
- [Lucas Palma](../speakers/lucas-palma.md)
- [Pietro Zullo](../speakers/pietro-zullo.md)
- [Ramesh Raskar](../speakers/ramesh-raskar.md)
- [Rob Cheung](../speakers/rob-cheung.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

