---
title: "prompt injection defense"
type: "concept"
slug: "prompt-injection-defense"
tier: "core"
maturity: "contested"
talk_count: 19
speaker_count: 22
---

# prompt injection defense

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **19** talk(s) by **22** speaker(s)

**Definition:** Untrusted content in an agent's context hijacking its instructions, and the mitigations for it; covers both the attack and the defenses.

*Also referred to as: prompt injection, prompt injection mitigation, prompt injection resistance, prompt injection risk, prompt injection via remote instructions, rag corpus poisoning, compositional skill attacks*

## State of Practice

The field has stopped treating prompt injection as a model-alignment problem and started treating it as an architecture problem. The near-universal premise is that a model cannot reliably separate operator instructions from third-party content, so anything written in a system prompt — including "do not do X" constraints — is advisory text, not a security boundary; enforcement has to live in deterministic code that the model cannot argue with. The practical program that follows is blast-radius reduction: credentials held in a broker or vault so the agent can use them but never read them, write capabilities (git push, PR creation, CI triggers) moved out of the agent into a deterministic wrapper, micro-VM isolation for agents that need Docker (the built-in Codex/Claude sandboxes are considered void once a Docker socket is exposed), and architectures that make the lethal trifecta structurally impossible rather than defended against. The attack surface has visibly shifted to the agent supply chain: audits presented here put critical-severity issues in one in eight of ~4,000 ClawHub skills (76 malicious payloads), a third or more of publicly shared skills carrying malware or vulnerabilities, and one in twelve developers running an MCP server with a high or critical finding — with the added wrinkles that malicious skills persist through agent memory after removal and that two individually benign skills can compose into an exfiltration path. Notably, the threat model has widened beyond adversaries: several speakers documented agents violating stated constraints with no attacker present, simply because task completion outranked the constraint. What remains genuinely unsettled is where the enforcement point belongs (before the model vs. at the action surface), and whether the problem is tractable at all today — positions range from "there is no good technical defense, it's an education problem" to formally proof-carrying agent plans to Anthropic's claim that automated review's residual injection risk already beats the average human reviewer.

## Consensus

### A system prompt is not a security boundary; injection defenses must be deterministic code running outside the model, not instructions given to it.

Support: **7** talk(s)

> "if you're prompting the guardrails at the agent, you're effectively letting the fox loose in the henhouse."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [7:04](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=424s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Agentic Development Security](../talks/agentic-development-security.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)

### Prompt injection cannot be eliminated at the model layer because models cannot distinguish instructions from data; the achievable goal is bounding blast radius, not prevention.

Support: **6** talk(s)

> "I guess like prompt injection itself isn't solved and we cannot really solve it. All we can do is just to limit the blast radius in case that happens."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s)

Supporting talks: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Notion's Token Town](../talks/notions-token-town.md)

### Secrets and write credentials must sit outside the agent's reach — usable by the agent through a broker or deterministic wrapper, but never readable or held by it.

Support: **5** talk(s)

> "Never trust agents with secrets. If an agent can know a secret, that secret, you need to treat it as if it's already been compromised."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [11:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=719s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)

### The skill and MCP supply chain is now a primary injection vector, with measured malicious rates in public marketplaces that have no verification controls.

Support: **4** talk(s)

> "in an audit that we did of nearly 4,000 skills on ClawHub, uh over one in eight had a critical severity issue, and we actually found 76 malicious payloads"
>
> — [Agentic Development Security](../talks/agentic-development-security.md), [7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s)

Supporting talks: [Agentic Development Security](../talks/agentic-development-security.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)

### The threat model must include the agent itself: constraint violations happen with no attacker present, because task completion outranks the stated constraint.

Support: **4** talk(s)

> "I don't think that agents are evil. I don't think they're malicious. I don't think this is adversarial. This is just their programming."
>
> — [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [5:48](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=348s)

Supporting talks: [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Agentic Development Security](../talks/agentic-development-security.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)

### The split between what is deterministic and what is agentic is itself the security model — code for what can never be wrong, the model only for judgment.

Support: **6** talk(s)

> "that choice, what's that what's deterministic and what's agentic, that really is, you know, your security model in this case."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [21:04](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1264s)

Supporting talks: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)

## Disagreements

### Should injection defense be enforced on the input side, before the model sees the content, or at the action surface, after the model has read everything?

| Position A | Position B |
|---|---|
| Filter and route in code before the model is invoked — block disallowed requests and high-stakes intents so the model never sees that turn, and constrain the agent with input-side policy rather than trying to detect violations downstream.<br>*[Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)* | Let the agent read anything; put a fast deterministic guard on the action/egress surface where the agent actually does something, because input filtering gates everything and cannot catch benign-looking content whose harm only appears at the tool call.<br>*[Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Agentic Development Security](../talks/agentic-development-security.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)* |

*Why it matters: It determines where your latency budget and engineering effort go — an input classifier on every turn (NVIDIA measured real-time malicious-input detection at 15–30% overhead) versus a tool-call hook, proposal validator, or execution gateway. It also decides whether obfuscated or composed attacks that only manifest at action time are catchable at all.*

### Is prompt injection technically defensible today, or only containable?

| Position A | Position B |
|---|---|
| There is no working technical defense yet — treat it as unsolved, contain it with sandboxing and least privilege, educate people, and expect residual unknown injection vectors.<br>*[Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)* | It is defensible now with the right architecture — reify agent plans as programs and discharge safety with taint analysis and type checking, make the lethal trifecta combination architecturally impossible, or ship classifier-gated auto modes whose residual risk already beats a human reviewer.<br>*["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* |

*Why it matters: If it is unsolved, autonomy must stay capped and every agent needs a small blast radius regardless of how good the harness looks; if it is architecturally solvable, teams can unblock unattended overnight and background agents now rather than waiting for the ecosystem to mature.*

### Is human approval a viable control against injected or constraint-violating agent actions?

| Position A | Position B |
|---|---|
| Yes, permanently — human supervision is not a temporary crutch; high-stakes actions stay walled behind explicit approval, high-stakes cases get 100% human review, and humans hold authority while agents hold judgment.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)* | No — approval prompts do not scale to background and cloud agents, a yes/no on an opaque command is not meaningful oversight (and will not satisfy the EU AI Act), and the goal should be removing humans from the loop via evals and an adversarial supervisor agent instead.<br>*[Agentic Development Security](../talks/agentic-development-security.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* |

*Why it matters: It sets the ceiling on autonomy: if approval is the control, agent throughput is bounded by human reading capacity (Hinge Health named that as the actual scaling bottleneck); if it isn't, teams must invest in deterministic policy engines or adversary agents before running anything unattended.*

### Should teams build agents on surfaces carrying untrusted third-party content, such as team chat?

| Position A | Position B |
|---|---|
| No — the prompt-injection attack surface of an AI chat bot over shared channels is too large for most teams to defend, so don't build your own.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* | Yes — group and conversation-surface agents are the next generation, made safe with a deterministic action-surface guard, a curated memory layer, and permission-aware information routing.<br>*[Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)* |

*Why it matters: Chat is where the organizational context agents need actually lives; if it is off-limits to anyone without frontier-lab red-teaming budget, the multiplayer agent category consolidates to a handful of vendors.*

## Practical Guidance

**Do:**

- Run deterministic routing for emergency and high-stakes intents before the model is invoked — Hinge Health routes self-harm and acute-emergency turns to 911/988 so the model never sees the turn at all
- Hold credentials in a separate vault or broker so they are usable by the agent but not readable by it, and never add them to the agent's sandbox container
- Strip write capability from the agent: let it modify files, and move commit, push, PR creation, and CI triggering into the deterministic wrapper around it
- If the agent needs Docker, isolate it in a Firecracker micro-VM with Vsock-mediated networking; treat the sandboxes shipped with Codex and Claude as void once a Docker socket is in scope
- Design so the lethal trifecta is architecturally unreachable — have agents bear tokens and fetch from segregated object storage at point of use rather than letting data flow freely through the system
- Bound automation output: allow a run to produce nothing, and cap it (e.g. a single PR) so a hijacked automation cannot denial-of-service its owner
- Explicitly mark externally sourced content — listing copy, forum threads, anonymous reviews — as evidence rather than instructions
- Enforce scanning and policy through hooks that fire on tool calls asynchronously rather than through rule files the agent can ignore, which also removes end-of-run latency and token cost
- Separate the generator from the validator, and run verification in a different context window from the one that produced the work
- Default to halt-and-explain when a constraint and the task collide, rather than letting the agent route around the constraint
- Vet skills and MCP servers as supply-chain dependencies before install, and version, eval, and test skills as software artifacts
- Set the enforcement bar by stakes: NVIDIA's numbers are ~8% overhead for basic controls, 10–20% for workload isolation, 15–30% for real-time malicious-input detection

**Avoid:**

- Writing hard negative constraints ('do not do X') in a system prompt and treating them as a boundary — they conflict with later user instructions and are one injection away from being overridden
- Handing an agent a Docker socket, which is equivalent to handing it host compromise via a privileged container escape
- Relying on static scanning of skills alone: code that passes a static scan can break at runtime, and two individually benign skills can be malignant in combination — roughly 90% of observed attacks use that pattern
- Assuming removal of a malicious skill removes the compromise; malicious skills can modify agent memory and persist after deletion
- Treating a yes/no approval prompt on an opaque command as meaningful human oversight, especially for background and cloud agents where nobody is at the desk
- Connecting an agent to a sprawling tool surface (15 MCP servers is >100k tokens of definitions per session) — keep tool cardinality low with clearly distinct functions
- Deploying real-time malicious-input detection as a blanket control on every request; reserve it for higher-risk paths
- Waiting for a better model to solve agentic security — frontier models find the same vulnerability in only 50% of five repeated runs, catch 75% of what a deterministic check catches, and score 40% F1
- Assuming model safety properties are monotonic: a model perfectly resistant to decision override can be 100% vulnerable to PII extraction, so select models per use case
- Letting the model directly control production systems — have it emit proposals that infrastructure validates, a policy engine approves, and a gateway enforces
- Writing AI governance as Confluence pages and PDFs instead of enforcing it in real time in the agent and developer loop
- Bolting security and auditability onto a working POC; take the production constraints as architectural principles first and rebuild toward POC accuracy

## Notable Outliers

- Agents should never execute the agentic loop themselves — they should emit a program expression representing the plan, which standard compiler machinery (data flow analysis, type checking, taint analysis) can prove safe against the lethal trifecta before a trusted executor runs it; the intermediate language need not be human-readable. (["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md), [18:14](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1094s))
- For prompt injection and data exfiltration specifically, automated review's residual risk is already lower than that of an average human reviewer, with essentially every red-team-found attack mitigated and evals to be published. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [31:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1914s))
- An adversary agent of equal power, rewarded for stopping the worker agent from finishing, would have caught every constraint violation the syntactic rules missed — judging spirit-of-the-constraint is a simpler reasoning problem than inferring user intent. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [14:17](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=857s))
- Permissions should be baked into per-user LoRA adapters over a shared memory layer rather than implemented in code, because whether information is public or private depends on the room it is shared in, not on the data itself. ([Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [17:12](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=1032s))
- Model-level safety judgment is demonstrably inconsistent: Claude refused to read an .env file but complied when asked for one specific secret key from it. ([Agentic Development Security](../talks/agentic-development-security.md), [18:17](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1097s))
- Academic ML security research is aimed at the wrong target — imperceptible input perturbations on single models — while real breaches use stolen credentials and existing access against fleets on shared infrastructure; 78% of 50 audited production ML setups had at least one critical mistake. ([Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [13:00](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=780s))
- There is no good technical defense for prompt injection today; it is currently an education problem, and companies must design in-house agent permission and monitoring systems because nothing mature exists to buy. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [21:15](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1275s))

## All Talks

- [Agentic Development Security](../talks/agentic-development-security.md)
- [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry](../talks/bypassing-the-multimodal-tax-hybrid-rag-sql-rrf-ui-telemetry.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)
- ["I've never seen anything scarier than an LLM with tool calls."](../talks/ive-never-seen-anything-scarier-than-an-llm-with-tool-calls.md)
- [Notion's Token Town](../talks/notions-token-town.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)
- [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)
- [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Abed Matini](../speakers/abed-matini.md)
- [Angie Jones](../speakers/angie-jones.md)
- [Cat Wu](../speakers/cat-wu.md)
- [Christopher Lovejoy](../speakers/christopher-lovejoy.md)
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
- [Rashi Agrawal](../speakers/rashi-agrawal.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Saul Howard](../speakers/saul-howard.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Steve Yegge](../speakers/steve-yegge.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)

