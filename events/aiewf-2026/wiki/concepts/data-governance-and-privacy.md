---
title: "data governance and privacy"
type: "concept"
slug: "data-governance-and-privacy"
tier: "supporting"
maturity: "consolidating"
talk_count: 13
speaker_count: 15
---

# data governance and privacy

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **13** talk(s) by **15** speaker(s)

**Definition:** Controlling what data may enter model context and where it may flow — PII handling, redaction, residency, lineage, and ownership.

*Also referred to as: data governance, data governance and pii masking, contextual privacy, data redaction from model context, data ownership, cross-organizational data sharing, data lineage, end-to-end encryption*

## State of Practice

The dominant view at this conference is that data governance is an architectural property decided before a single token is generated, not a policy layer applied afterward: PHI/PII gets stripped at the ingestion boundary rather than redacted when logs and dashboards are written, sensitive payloads live in segregated immutable object storage that an append-only event log only references, and prod/non-prod have literally zero data pipes between them. Nobody credible now treats a system prompt as a data boundary — authentication, emergency routing, and access decisions run in deterministic code above the model, on every turn, because prompt injection collapses any authority layer expressed in text. The second recurring theme is that agents change the risk surface in kind rather than degree: data that was theoretically accessible is now practically reachable, individually benign skills compose into exfiltration paths (one speaker cites ~90% of observed attacks following that pattern), and always-on personal capture generates ~10M tokens/year per user. Auditability is being solved by making the log the system of record — a complete, append-only trace of every action, data access, and authorization, so compliance under SOC 2/HITRUST/HIPAA falls out of the storage paradigm instead of being a separate feature. The live arguments are about mechanism and locality: deterministic code versus learned permission boundaries, synthetic data versus production replay for evaluation, one discoverable semantic layer versus deliberate segregation, and whether serving your data into ChatGPT/Claude clients is distribution or leakage.

## Consensus

### Privacy and compliance constraints must be architectural primitives chosen before the system is built; bolting them onto a working POC produces brittle systems.

Support: **4** talk(s)

> "You cannot slap on HIPAA on top of, you know, an underlying system or an architecture. You start with it and let the architecture grow around it."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [5:09](https://www.youtube.com/watch?v=YXEqC05WEI0&t=309s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)

### Data boundaries must be enforced by deterministic mechanisms running outside the model — code, crypto, sandboxing, point-of-use tokens — never by instructing the model in a prompt.

Support: **4** talk(s)

> "A model is not a guardrail. A model with a system prompt is also not a guardrail. Code that runs above the model is closer."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [6:48](https://www.youtube.com/watch?v=YXEqC05WEI0&t=408s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)

### Sensitive payloads should never enter the observability, orchestration, or debugging plane; engineers and models should operate on schema, metadata, and references instead of raw regulated data.

Support: **4** talk(s)

> "it's possible for developers to go back and debug and have observability over what happened, what particular steps the agent took, why it did that, and and retrace the agent's steps without having access to the personal health information itself"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [11:16](https://www.youtube.com/watch?v=mav15aW9lLM&t=676s)

Supporting talks: [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)

### An append-only, tamper-evident record of every action, data access, and authorization is the source of truth for agent systems, and lineage/auditability should be a free consequence of that storage choice rather than a bolted-on feature.

Support: **3** talk(s)

> "An immutable record of events that store all of the transactions that happen throughout the system. And this is append-only timestamp log. It's complete. So, this is your source of truth for all of the data of the system."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [6:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=415s)

Supporting talks: [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)

### Agents materially enlarge the risk surface by making previously theoretical data access practical, so masking, sensitivity classification, and per-user entitlements must be pushed into the data curation pipeline rather than assumed from existing system permissions.

Support: **4** talk(s)

> "They're much more accessible now with with AI. And so you have to consider this. Your risk sphere is is larger. So things like PII need to be masked."
>
> — [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [7:59](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=479s)

Supporting talks: [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)

## Disagreements

### Should per-user access control and exfiltration prevention be implemented in deterministic code, or learned into the model itself?

| Position A | Position B |
|---|---|
| Access decisions are security boundaries and must run as deterministic code above the model — authentication checks before every turn, hardcoded signing keys, sandboxing — because anything left to probability will eventually be wrong.<br>*[Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)* | Permissions should be baked in with machine learning — per-user LoRA adapters over a shared memory layer — and the exfiltration guard itself must be a trained model, because regex and static approaches fail against character-interspersed obfuscation and benign-skill composition.<br>*[Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)* |

*Why it matters: A learned permission boundary has a nonzero error rate by construction and cannot be shown to an auditor as a rule; a coded one cannot catch semantic obfuscation. The choice determines whether you can prove to a regulator why a given user's data was or wasn't reachable.*

### When the data you most need is the data you are least allowed to keep, do you synthesize it or replay production?

| Position A | Position B |
|---|---|
| Generate data backwards from sampled labels so records are correct by construction — ~90% of datasets synthetic, no PHI retained, no dependency on customer data before going live, and rare edge cases covered that production sampling would miss.<br>*[Don’t be data poor](../talks/dont-be-data-poor.md)* | Saved offline datasets drift and sample unrepresentatively; what holds up is continuously scoring live traffic, replaying real production events, and computing ground truth from the live system at eval runtime.<br>*[Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)* |

*Why it matters: It decides whether your compliance story is 'we never retain regulated data' or 'we retain it under controls and run evals inside the customer's environment,' and whether your blind spot is distributional realism or edge-case coverage.*

### Should agents get a unified, discoverable view across an organization's data, or should access be deliberately fragmented?

| Position A | Position B |
|---|---|
| Push discovery, mapping, and trust into a shared substrate — a business plus technical ontology, a knowledge graph, a pre-built metadata layer — with PII masking and security trimming applied during curation, so agents stop being individually wired to data sources.<br>*[Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)* | Make the dangerous combination architecturally impossible: segregate sensitive data into storage the agent reaches only with point-of-use tokens, keep unencrypted data inside the perimeter, and split tool output so the model never sees payloads it doesn't need.<br>*[Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)* |

*Why it matters: One approach makes governance a configurable trimming layer over a complete view — powerful, but a misconfiguration exposes everything; the other forecloses whole flows at the cost of agent capability and reuse.*

### Should enterprises serve sensitive capabilities into third-party AI clients, or keep the agent and its log entirely inside their own perimeter?

| Position A | Position B |
|---|---|
| Chat clients are the new distribution surface — expose your platform through MCP into Claude/ChatGPT/Cursor rather than building another UI, since the interface is not the defensible part and store listings drive high-intent traffic.<br>*[Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)* | Whoever owns the log owns the agent; unencrypted data must not leave your perimeter (run your own inference if needed), and some customers will not let regulated data leave their VPC at all, forcing tangential access patterns.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)* |

*Why it matters: Every turn routed through a hosted client puts the organization's most intimate context — and its audit trail — on infrastructure it cannot inspect, which is exactly what residency and lineage requirements are meant to prevent.*

## Practical Guidance

**Do:**

- Strip PHI/PII at the pipeline boundary at ingestion, before data reaches the data lake, so no runtime redaction of logs or dashboards is needed
- Keep sensitive records in immutable, schema-driven object storage that the event log only references, so orchestration and observability contain no regulated data
- Run identity/authentication checks and emergency or high-stakes intent routing in deterministic code before the model sees the turn — for self-harm or acute emergency content, the model should not see that turn at all
- Maintain zero data pipes between production and non-production environments, and give engineers outside the certified geographic region no access to raw PHI
- Make encryption non-optional: keys generated and held only on the user's device, no opt-out, no bypass, with a forced key expiration window (seven days was chosen over 24 hours so agent work isn't lost when a user doesn't open their phone)
- Keep the security-critical codebase small enough to fully audit (~20k lines in a memory-safe language, mostly attestation verification) and reuse existing trustworthy crypto instead of writing your own
- Split deployment authority: hold signing keys in a separate privacy team and hardcode them into clients and backends, and publish workload attestations to a public transparency log so anyone can verify what's running
- Give agents bearer tokens that fetch data at the point of use rather than letting data flow freely through the system, and test explicitly whether the lethal trifecta is reachable within your architecture
- Split MCP tool output between what renders in the widget and what goes to the model, so privacy-sensitive data can be displayed without being sent to an LLM provider
- Run evals on production data inside the customer's own environment so sensitive data never reaches the vendor's agent
- Engage data owners directly to capture field semantics, join logic, data limitations, safeguards, and security trimming — none of it is inferable from the data alone
- Give domain experts the interface (e.g. skills on an agent harness) to add new document types and judge data quality, rather than having AI engineers decide what good looks like
- Own and inspect your agent logs — self-host if necessary — and treat the log, not the running process, as the asset
- Where regulated data can't be retained, generate it backwards from a sampled label so records are labeled correctly by construction and no real PHI is stored

**Avoid:**

- Treating a system prompt, or any authority layer expressed inside a prompt, as a security boundary — if the labs don't trust prompts as one, neither should you
- Redacting at runtime when logs and dashboards are written, instead of stripping at ingestion
- Any single data pipe from production into dev — one is enough to leak member data
- Building a POC first and strapping on eval, security, and auditability as requirements surface; take the production constraints as the architectural primitives and build back up to POC accuracy
- Relying on static scanning or regex to catch exfiltration: code that survives a static scan can break at runtime, two individually benign skills can be malignant in combination, and dotted/interspersed text defeats pattern matching
- Filtering everything the agent reads instead of guarding the action surface where it actually does something
- Assuming a vendor's customer-facing data guarantees still protect you once you are operating inside that vendor
- Letting intimate user disclosures land in the same data infrastructure as search history and product analytics, and judging your privacy bar by what is legally defensible rather than what you'd accept for yourself
- Trying to tame agents behaviorally, or giving them direct access to personal computers — only sandboxing and removing the means to cause harm work
- Treating fire-and-forget local JSONL logs (Claude Code, Codex) or corruption-prone local SQLite state as your audit record
- Assuming markdown files and skills alone give enterprise agents governed access to the right data — they are part of the solution, not the solution
- Optimizing sensitive-domain products for engagement and session depth when the clinically correct goal is for the user to need the product less

## Notable Outliers

- Being inside a hyperscaler is a weaker privacy position than being its customer: the customer-facing guarantee that the provider cannot see your data no longer applies to you, so you must engineer around your own employer. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [10:06](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=606s))
- Whether information is public or private is a property of the room it was shared in, not of the data itself — the same fact is a leak in one group chat and a normal answer in another. ([Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [16:06](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=966s))
- Log lock-in is a deeper form of vendor lock-in than model, API, or tool lock-in: models can be swapped and APIs wrapped, but whoever holds the log holds the agent. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s))
- Synthetic medical records generated backwards from symbolic policy decision trees passed blind clinician review — experts distinguished synthetic from real only about 60% of the time — making ~90% synthetic eval datasets viable under PHI constraints. ([Don’t be data poor](../talks/dont-be-data-poor.md), [14:26](https://www.youtube.com/watch?v=XAsb7MIAzm8&t=866s))
- Consumer AI has no equivalent of therapeutic privilege, so the most sensitive relationship disclosures in existence flow into training pipelines, server logs, and product analytics with no protective doctrine at all. ([AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md), [10:47](https://www.youtube.com/watch?v=yoONZwV2smc&t=647s))

## All Talks

- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [AI is the World’s largest Relationship Therapist](../talks/ai-is-the-worlds-largest-relationship-therapist.md)
- [Don’t be data poor](../talks/dont-be-data-poor.md)
- [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)
- [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)
- [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)
- [The Log Is The Agent](../talks/the-log-is-the-agent.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)
- [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)
- [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Anuj Iravane](../speakers/anuj-iravane.md)
- [Armanas Povilionis](../speakers/armanas-povilionis.md)
- [Christopher Lovejoy](../speakers/christopher-lovejoy.md)
- [Clay Cockrell](../speakers/clay-cockrell.md)
- [Emil Eifrem](../speakers/emil-eifrem.md)
- [Ishaan Sehgal](../speakers/ishaan-sehgal.md)
- [Mike Phipps](../speakers/mike-phipps.md)
- [Pietro Zullo](../speakers/pietro-zullo.md)
- [Rashi Agrawal](../speakers/rashi-agrawal.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Saul Howard](../speakers/saul-howard.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Tony Fabrikant](../speakers/tony-fabrikant.md)
- [Varun Singh](../speakers/varun-singh.md)

