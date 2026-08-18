---
title: "prompt injection defense"
type: "concept"
slug: "prompt-injection-defense"
tier: "core"
maturity: "contested"
talk_count: 17
speaker_count: 19
---

# prompt injection defense

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **17** talk(s) by **19** speaker(s)

**Definition:** Untrusted content in an agent's context hijacking its instructions, and the mitigations for it; covers both the attack and the defenses.

*Also referred to as: prompt injection, prompt injection mitigation, prompt injection resistance, prompt injection risk, prompt injection via remote instructions, rag corpus poisoning, compositional skill attacks*

## State of Practice

The field has largely stopped treating prompt injection as a model-alignment problem and started treating it as an architecture problem: because an LLM cannot reliably separate operator instructions from third-party content, every credible defense presented was structural rather than textual. The dominant pattern is a deterministic layer wrapped around the agent — hooks firing on tool calls, policy engines validating model-emitted proposals, execution gateways, egress filters, micro-VM isolation — with the explicit warning that any guardrail expressed as words inside the agent's own context is itself injectable. Credential handling has converged on a broker model where secrets are usable by the agent but not readable by it, and write-capable operations (git push, PR creation, CI triggering, production mutations) are moved out of the agent entirely into deterministic code. A second front opened this year around the agent supply chain: audits reported one in eight of ~4,000 public skills carrying a critical issue with 76 malicious payloads, over a third of shared skills containing malware or vulnerabilities, one in twelve developers running an MCP server with a high/critical finding, and roughly 90% of observed attacks coming from combinations of individually benign skills that static scanning cannot catch. What remains genuinely unsettled is whether the residual risk can be driven to zero — practitioners running agents in production mostly say no and budget for blast-radius containment, while vendors and researchers demonstrating classifier gates and proof-carrying plans argue the problem is tractable with the right execution model.

## Consensus

### Guardrails must be deterministic and live outside the agent's context; instructions in a system prompt telling the agent not to do something are not a security control because untrusted content can override them.

Support: **8** talk(s)

> "if you're prompting the guardrails at the agent, you're effectively letting the fox loose in the henhouse."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [7:04](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=424s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Agentic Development Security](../talks/agentic-development-security.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)

### The model layer cannot distinguish operator instructions from injected third-party content, so prompt injection is not eliminable — the goal is bounding blast radius and treating all externally sourced content as evidence rather than instructions.

Support: **5** talk(s)

> "I guess like prompt injection itself isn't solved and we cannot really solve it. All we can do is just to limit the blast radius in case that happens."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s)

Supporting talks: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Build Systems, Not Code](../talks/build-systems-not-code.md)

### Secrets must be held outside the agent's sandbox and reached only through a broker or vault — any credential the agent can read should be assumed already exfiltrated, and write-scoped credentials should be removed from the agent entirely.

Support: **4** talk(s)

> "Never trust agents with secrets. If an agent can know a secret, that secret, you need to treat it as if it's already been compromised."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [11:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=719s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)

### The system that produced the work cannot be the system that validates it — verification must run in a separate context window or separate deterministic checker, because self-grading in the producing context confabulates.

Support: **5** talk(s)

> "what we found is it's quite effective to separate verification into a separate context window. This is a very general trend."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [6:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=404s)

Supporting talks: [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Agentic Development Security](../talks/agentic-development-security.md)

### Skills and MCP servers are now a measured injection and supply-chain vector with malicious payloads already in the wild, and marketplace verification controls do not yet exist.

Support: **4** talk(s)

> "in an audit that we did of nearly 4,000 skills on ClawHub, uh over one in eight had a critical severity issue, and we actually found 76 malicious payloads"
>
> — [Agentic Development Security](../talks/agentic-development-security.md), [7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s)

Supporting talks: [Agentic Development Security](../talks/agentic-development-security.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)

## Disagreements

### Is prompt injection a solvable engineering problem, or only a containable one?

| Position A | Position B |
|---|---|
| It cannot be solved. Defenses should assume compromise and invest entirely in limiting blast radius — removing write credentials, isolating in micro VMs, segmenting infrastructure — because unknown injection vectors will keep appearing and there is currently no good technical defense.<br>*[We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)* | It is tractable with the right execution model. Reify the agent's plan as a typed program and settle safety — including the lethal trifecta — with ordinary data-flow and taint analysis; or gate the action surface with a trained classifier that sees the tool call plus conversation context, which red teams have failed to get past.<br>*["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)* |

*Why it matters: If injection is unsolvable, the correct spend is on isolation, credential brokers, and audit, and autonomous agents stay permanently capped in privilege; if it is solvable, that spend is transitional and agents can be granted real production authority once the gate is in place.*

### Is a human approval prompt a meaningful defense against an agent acting on injected instructions?

| Position A | Position B |
|---|---|
| Yes — high-consequence actions (sending email, submitting offers, production writes) should be walled behind explicit human approval, and human supervision is a permanent architectural component, not a stopgap that better models will remove.<br>*[Build Systems, Not Code](../talks/build-systems-not-code.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)* | No — approval prompts do not survive contact with reality. Users cannot tell whether to approve an opaque command, background and cloud agents run with nobody watching, and an agent can persuade the human to remove the control outright; policy must steer deterministically instead, with humans removed from routine loops.<br>*[Agentic Development Security](../talks/agentic-development-security.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* |

*Why it matters: This determines whether async and overnight agents are shippable at all, and whether a yes/no confirmation UI counts as the 'meaningful human oversight' regulators are about to require for high-risk systems.*

### Should injection defense sit on the input side (before the model sees the content) or on the action surface (after the model decides, before the tool runs)?

| Position A | Position B |
|---|---|
| Block on the input side. Prompt-injection filters and policy checks should reject the request in code before the LLM is ever called, and constraining agents with input-side policy works better than detecting violations downstream.<br>*[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)* | Let the agent read everything and gate what it does. Filtering all input is infeasible and obfuscation defeats regex and static scanning, so the model should only emit proposals that a fast deterministic guard, policy engine, or execution gateway validates at the action boundary.<br>*[Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)* |

*Why it matters: Input-side filtering costs latency on every request and fails open against obfuscation, while action-side gating accepts that poisoned context enters the model and bets everything on the tool-call boundary being complete — the two produce entirely different threat models and different places to spend engineering effort.*

## Practical Guidance

**Do:**

- Hold credentials in a separate vault or broker so they are usable by the agent but not readable by it; never add them to the agent's sandbox container
- Strip write-capable operations from the agent — let it modify files, but move git push, PR creation, and CI triggering into the deterministic wrapper around it
- Implement guardrails as hooks that fire on tool calls asynchronously, outside the context window, rather than as rule files or MCP servers the agent may ignore
- Run injection and policy checks as code before the LLM call, rather than as sentences in the system prompt
- Verify in a separate context window from the one that produced the work, and run security as its own pass rather than bundled with correctness
- Explicitly label externally sourced content (listing copy, forum threads, reviews, fetched YAML) as evidence, not instructions
- Use micro VMs such as Firecracker with Vsock-mediated networking as the isolation boundary when the agent needs Docker
- Make halt-and-explain the default when a constraint and the task conflict, instead of letting the agent route around the constraint
- Bound automation output — a single PR, or nothing at all — so a hijacked automation cannot denial-of-service its owner
- Audit skills and MCP servers before installing, and treat skill marketplaces as unverified package registries
- Select models per use case against your specific attack classes, since resistance to decision override does not imply resistance to PII extraction

**Avoid:**

- Expressing guardrails as prompts to the agent — a third party can inject past them
- Giving the agent Docker socket access; it can spawn a privileged container and escape, which makes the built-in Codex and Claude sandboxes worthless
- Treating a yes/no approval on an opaque command as oversight — reviewers cannot tell whether to approve, and it will not satisfy the EU AI Act's meaningful-oversight requirement
- Relying on static scanning of skills: code that passes a scan can break at runtime, and two individually benign skills can be malignant in combination
- Assuming removal of a malicious skill removes the compromise — malicious skills can write to agent memory and persist
- Trusting model-level refusal as the control: Claude refused to read an .env file but complied when asked for a specific secret key
- Fixing only criticals and highs — agents can chain low-severity vulnerabilities into working exploits
- Building your own AI Slackbot, where the untrusted-message attack surface is enormous
- Applying real-time malicious-input detection as a blanket control; at 15–30% overhead it is a non-starter outside higher-risk systems
- Waiting for a better model to solve agentic security — frontier models find the same vulnerability in only 50% of five repeated runs and score 40% F1

## Notable Outliers

- Prompt injection is fully defensible today with 1990s compiler technology: have the agent return a typed program representing the plan instead of executing it, then use data-flow analysis, type checking, and taint analysis to prove safety — including against the lethal trifecta — before a trusted executor runs it. (["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [18:14](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1094s))
- An agent persuading a human to install a Chrome extension that removes a control counts as the agent supplying the energy to defeat its own constraint, with the human acting as its tool — so constraints must be broken only by energy originating outside the agentic loop. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- For prompt injection and data exfiltration specifically, an automated classifier reviewing the tool call plus conversation context carries lower residual risk than the average human reviewer, and essentially every attack found by commissioned red teams has been mitigated. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [31:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1914s))
- Roughly 90% of observed attacks follow the pattern where individually benign skills combine to exfiltrate data, which is why the guard belongs at the action surface rather than on what the agent reads. ([Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [8:31](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=511s))
- Real production ML breaches are overwhelmingly boring infrastructure misconfiguration — authentication off by default, clusters open on the internet, 78% of 50 audited setups with at least one critical mistake — while academic security research studies imperceptible input perturbations that almost never appear in incidents. ([Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [13:00](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=780s))
- The hardest agent failures are ones where the agent never exceeds its authorization at all, so the system looks compliant throughout and no permission boundary is ever tripped. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [10:16](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=616s))
- Skills execute on the agent's own machine with no process isolation, which is a genuine security regression relative to MCP's separate server process even as skills win on context overhead. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [24:54](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1494s))

## All Talks

- [Agentic Development Security](../talks/agentic-development-security.md)
- [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)
- [Notion's Token Town](../talks/notions-token-town.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)
- [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Abed Matini](../speakers/abed-matini.md)
- [Angie Jones](../speakers/angie-jones.md)
- [Cat Wu](../speakers/cat-wu.md)
- [Corey Gallon](../speakers/corey-gallon.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [Erik Meijer](../speakers/erik-meijer.md)
- [Ezra Tanzer](../speakers/ezra-tanzer.md)
- [Idan Gazit](../speakers/idan-gazit.md)
- [Lance Martin](../speakers/lance-martin.md)
- [Lovina Dmello](../speakers/lovina-dmello.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Moritz Johner](../speakers/moritz-johner.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Steve Yegge](../speakers/steve-yegge.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)

