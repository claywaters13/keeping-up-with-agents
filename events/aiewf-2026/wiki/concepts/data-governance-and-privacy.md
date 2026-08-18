---
title: "data governance and privacy"
type: "concept"
slug: "data-governance-and-privacy"
tier: "supporting"
maturity: "contested"
talk_count: 9
speaker_count: 9
---

# data governance and privacy

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **9** talk(s) by **9** speaker(s)

**Definition:** Controlling what data may enter model context and where it may flow — PII handling, redaction, residency, lineage, and ownership.

*Also referred to as: data governance, data governance and pii masking, contextual privacy, data redaction from model context, data ownership, cross-organizational data sharing, data lineage, end-to-end encryption*

## State of Practice

The field has stopped treating privacy as a policy layer bolted onto an LLM and started treating it as an architectural property of the agent harness: agents act on the world, hold personal and enterprise data continuously, and therefore need controls that hold even when the model misbehaves. Three enforcement points are in active use — encryption and attestation at the perimeter (keys generated on-device, forced 7-day expiry, workloads published to a Sigstore transparency log, a ~20k-line memory-safe trusted codebase), curation-pipeline controls (PII masking, sensitivity classification, per-user entitlements and security trimming applied before data reaches the agent), and deterministic guards at the action surface rather than the input. Provenance is the second pillar: signed receipt chains for cross-org work, the append-only agent log as the durable identity of the agent, source code stored alongside derived datasets, and execution traces feeding back into data-source trust scoring — with the corollary that whoever holds the log holds the agent. Enterprise practitioners report that governance metadata cannot be inferred from data alone; it has to be extracted from data owners as field semantics, join logic, limitations and safeguards, and modeled explicitly. The open fights are about mechanism and placement — filter what enters context versus let the agent read everything and gate its actions; enforce permissions in code and crypto versus train them into per-user adapters; markdown-and-metadata-tables versus an ontology-backed graph as the substrate that carries sensitivity and lineage.

## Consensus

### Provenance — a verifiable record of how a result was produced — is a first-class artifact, not exhaust; the trace is as valuable as the output.

Support: **5** talk(s)

> "the value is not just what the agent produced, it's also the log, which indicates how it got there"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [8:45](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=525s)

Supporting talks: [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)

### Agentic systems demand a different security posture than LLMs, because acting on the world plus holding intimate personal/company data enlarges the risk surface beyond what prompt-level controls address.

Support: **4** talk(s)

> "we can't secure an agentic system like we secure a large language model"
>
> — [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [5:32](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=332s)

Supporting talks: [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)

### Privacy boundaries must be enforced structurally — sandboxing, encryption with no opt-out, entitlements, permanently off-limits regions — not by asking the agent to behave well.

Support: **4** talk(s)

> "I think nothing works except like sandboxing and just not giving them a way to hurt themselves."
>
> — [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [13:13](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=793s)

Supporting talks: [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)

### What the model sees should be scoped deliberately per surface and per recipient; data the system holds does not automatically belong in LLM context or in the shared channel.

Support: **4** talk(s)

> "In this case, you can show the UI to the user, but the model won't see the data that you display in the UI, unless you choose so."
>
> — [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [14:52](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=892s)

Supporting talks: [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

### Governance leverage lives in owning the substrate — keys, logs, and the modeled data — rather than the model layer, which is swappable and not defensible.

Support: **4** talk(s)

> "If a provider owns your log, then the provider effectively owns your agent"
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)

## Disagreements

### Should data-flow control be enforced on what enters the agent's context, or on what the agent is allowed to do with it?

| Position A | Position B |
|---|---|
| Control ingress: mask PII and apply entitlements in the curation pipeline before data reaches the agent, keep unencrypted data inside the perimeter (including running your own inference), and split tool output so sensitive fields render in the UI but never enter model context.<br>*[Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)* | Let the agent read everything and place a fast deterministic learned guard at the action surface, because gating the input gates everything and static/regex filtering fails against obfuscation such as character-interspersed text.<br>*[Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)* |

*Why it matters: Ingress control caps capability but makes leakage provably impossible for withheld fields; egress control preserves agent usefulness but makes the guard model itself the single point of failure, with a naive baseline sitting at 50% on the inspect agent benchmark.*

### Should per-user access control be implemented in deterministic code and cryptography, or learned into the model?

| Position A | Position B |
|---|---|
| Implement it deterministically: encryption with no bypass, keys held on the user's device, hardcoded signing keys splitting deployment authority, PII masking and per-user security trimming in the pipeline, and code regions like auth and payments declared permanently off limits to agent adaptation.<br>*[Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)* | Bake permissions into per-user LoRA adapters over a shared memory layer, enforcing them with machine learning rather than code, since in group settings privacy depends on the room a fact was shared in rather than on the data itself.<br>*[Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)* |

*Why it matters: A crypto/code boundary can be audited and proven (one speaker sized the trusted codebase at ~20k lines specifically so it could be fully verified); a learned boundary is context-sensitive but cannot be shown correct, which decides whether the system is defensible to a regulator or security review.*

### Is a flat markdown/metadata-table substrate sufficient for agent data access at scale, or is a modeled semantic layer required?

| Position A | Position B |
|---|---|
| Markdown alone is not the solution — enterprises with a hundred databases plus Snowflake, Databricks and S3 need a business ontology, a technical ontology of data-source metadata, execution traces, and an explicit mapping, exposed as one graph and one semantic layer through MCP with entitlements attached.<br>*[Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)* | A shared knowledge base of plain markdown files per dataset is sufficient dataset memory for agents and humans; the real work is a Pydantic-schema metadata layer transpiled to SQL, with the dataset's source code as the most important stored context.<br>*[When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)* |

*Why it matters: The substrate decides whether sensitivity classification, trust scoring and lineage are modeled centrally and reusable across agents, or re-derived per dataset and per team — the difference between cross-agent learning and paying to solve the same problem repeatedly.*

### Is tightening controls on a general-purpose agent the right path, or should scope be narrowed until trust is earned?

| Position A | Position B |
|---|---|
| Restriction is the answer today: a narrowly sandboxed special-purpose agent beats a general-purpose one tightened down, agents should not get direct access to personal computers, and constrained workflow-shaped experiences should sit alongside open-ended chat.<br>*[Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)* | More control is the wrong long-term target; the recommendations-only, never-autonomous stance is defensible but temporary, and the goal is earning enough trust — via isolation, provenance and per-context blast radius — that humans choose to step back.<br>*[The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)* |

*Why it matters: It sets whether governance investment goes into hard capability limits or into observability and provenance machinery that makes autonomy auditable after the fact.*

## Practical Guidance

**Do:**

- Encrypt with no opt-out, no disable path and no bypass; generate and keep the key on the customer device so the operator cannot read data even when the user's phone is offline
- Force in-memory key expiry at about seven days — 24 hours misses work when a user doesn't open their phone, and seven days covers the realistic horizon of useful agent work
- Keep the security-critical codebase small (~20k lines in a memory-safe language, mostly attestation verification) so it can actually be audited end to end
- Split deployment authority into a separate privacy team whose signing keys are hardcoded into clients and backends, and publish workload attestations to a transparency log (Sigstore) so anyone can verify the running build
- Use a private CA for internal attestation certificates, since public certificates would populate the public transparency log
- Split MCP tool output into a UI channel and a model channel so sensitive data renders for the user without ever entering the LLM provider's context
- Apply PII masking, sensitivity classification and per-user entitlements/security trimming inside the curation pipeline before the agent can query
- Engage data owners directly to capture field semantics, join logic, data limitations, safeguards and security trimming — none of it is inferable from the data alone
- Treat the append-only log as the durable system of record you own and can inspect, rather than as exhaust left on a provider's infrastructure
- Treat compaction as a lossy best-effort fork resumed as a new log, retaining the raw log for audit
- Store the source code and an LLM-enriched description alongside every derived dataset as its provenance record
- Score data-source trustworthiness both top-down by human curation and bottom-up from execution traces of what actually worked
- Declare regions such as auth and payments permanently off limits to agent adaptation while leaving cosmetic regions adaptable
- Route by room: have the agent DM a user rather than answer in a group when the content is private
- Compute eval ground truth by running a stored graph query against the live graph at runtime instead of freezing expected answers over constantly-changing data

**Avoid:**

- Behavioral or prompt-level techniques for taming agents — they do not work; only sandboxing and removing the means to cause harm do
- Giving agents direct access to personal computers
- Relying on static scanning of agent skills: code that passes a static scan can break at runtime, and two individually benign skills can be malignant in combination — about 90% of observed attacks follow that pattern
- Regex and other static filters, which fail against character-interspersed obfuscation
- Building your own crypto instead of reusing trustworthy existing software
- Assuming a provider's customer-facing 'we cannot see your data' guarantee still protects you once you are operating inside that provider
- Fire-and-forget JSONL log writes to local disk (Claude Code, Codex SDK mode) where a failed write silently loses the record, and SQLite-backed state with documented corruption issues
- Dumping millions of per-object metadata JSON files into S3 next to the data, or splitting metadata into a separate database that forces two systems and two languages researchers won't adopt
- Treating markdown files as the whole solution for enterprise agent data access
- Assuming stronger frontier models will fix agent performance on messy data — everyone already uses them; the harness is the differentiator

## Notable Outliers

- An always-on audio wearable captures roughly 10 million tokens per person per year, and one week of recording is enough to learn virtually everything about that person. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [0:01](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=1s))
- Operating inside Amazon required stronger privacy engineering than being an Amazon customer, because the customer-facing guarantee that Amazon cannot see your data no longer applies to you. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [10:06](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=606s))
- Whether information is public or private is a property of the room it was shared in, not of the data — the data hasn't changed, the room has. ([Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [16:06](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=966s))
- Log lock-in is deeper and more durable than model, API or tool lock-in, because the log is the agent's identity rather than a swappable component. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s))
- An enterprise answer is only correct if it matches how the question has historically been answered under existing reporting conventions — factual accuracy is not sufficient. ([Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [6:32](https://www.youtube.com/watch?v=jt1Pbr_n6oU&t=392s))
- After marketplace discovery, cross-organizational data transactions should be peer-to-peer with no third party mediating quote, deal, execution or receipt. ([Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [8:40](https://www.youtube.com/watch?v=Fu45geO3zX8&t=520s))
- Tightening down a general-purpose agent (OpenClaw) destroyed its usefulness, making a narrowly sandboxed special-purpose agent the better tradeoff today. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [14:59](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=899s))

## All Talks

- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)
- [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)
- [The Log Is The Agent](../talks/the-log-is-the-agent.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)
- [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Armanas Povilionis](../speakers/armanas-povilionis.md)
- [Emil Eifrem](../speakers/emil-eifrem.md)
- [Ishaan Sehgal](../speakers/ishaan-sehgal.md)
- [Mike Phipps](../speakers/mike-phipps.md)
- [Pietro Zullo](../speakers/pietro-zullo.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Varun Singh](../speakers/varun-singh.md)

