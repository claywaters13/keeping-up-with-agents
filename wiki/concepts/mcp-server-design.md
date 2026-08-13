---
title: "mcp server design"
type: "concept"
slug: "mcp-server-design"
tier: "supporting"
maturity: "contested"
talk_count: 9
speaker_count: 10
---

# mcp server design

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **9** talk(s) by **10** speaker(s)

**Definition:** Building and operating MCP servers well — tool surface, resource modeling, statefulness, and server-side security posture.

*Also referred to as: mcp server integration, mcp server security, host-mediated tool invocation, resource-linked tool calls, openapi spec translation, stateless protocol design, protocol minimalism*

## State of Practice

The dominant question about MCP servers at this conference was not how to expose tools but who is allowed to call them and with what authority. Four independent security talks converged on the same diagnosis: today's servers are reached with a human's own credential or a kitchen-sink API key, they return the same tool surface regardless of which user authorized the agent, and they lean on a human approval click as the actual access control. The emerging pattern is that the agent is a distinct principal bound to a user, that grants are minted per tool call — audience-bound to one target server, minutes-long, never stored — and that policy is evaluated before a credential exists rather than after. Underneath the security layer, the protocol itself is still moving: MCP tasks (async, long-running) has zero client implementations and a V1-to-V2 rewrite that removes tasks/list and makes the protocol stateless, while MCP Apps extends servers to return host-controlled UI instead of text. Server-surface design is also being treated as a context-budget problem — every tool, relationship type, and re-rendered view spends client tokens — so the advice trends toward fewer, higher-level, per-caller-scoped surfaces. Servers are also now treated as attack surface in their own right: one Snyk cohort found one in twelve developers running an MCP server with a high or critical finding inside the server itself.

## Consensus

### The agent must be its own principal with its own identity, bound to the user it acts for — not operate by holding the user's credentials or impersonating the user.

Support: **3** talk(s)

> "the actor, in this case, an agent, has to be bound to the principal at all times. And the agent should have its own identity."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [9:08](https://www.youtube.com/watch?v=lMCxVorb9wM&t=548s)

Supporting talks: [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)

### Human-in-the-loop approval is not an access control; enforcement must be deterministic policy, because approvers are consent-fatigued and background/cloud agents have no human present at all.

Support: **4** talk(s)

> "And we can't just solve this with human in the loop. We spent decades solving access management for humans. So just blindly trusting a human who might be a little bit consent fatigued uh or who might be tired enough at night, this isn't really going to be enough."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Agentic Development Security](../talks/agentic-development-security.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)

### Authority granted to an agent must be narrowed to the specific action and time window it is currently performing — per tool call, least privilege by default, just-in-time elevation — because an agent will use every permission it holds.

Support: **3** talk(s)

> "this request is asking for permissions to access the MCP server for that tool call but only that tool call."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [9:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=567s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)

### A server's surface is a context budget: every tool, schema, relationship type, scan result, and re-rendered view costs client tokens, so servers should hand agents a small number of high-level things rather than everything they could expose.

Support: **4** talk(s)

> "it packages a lot of um underlying protocols and underlying tools where now you're not shoving everything into a uh LLM context. It just has a services that it needs to interact."
>
> — [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [17:48](https://www.youtube.com/watch?v=Fu45geO3zX8&t=1068s)

Supporting talks: [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [Agentic Development Security](../talks/agentic-development-security.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)

## Disagreements

### Can agent-to-MCP-server access control be built on existing OAuth machinery, or does it require new agent-native protocol primitives?

| Position A | Position B |
|---|---|
| No new spec is needed: RFC 8693 token exchange, an existing OAuth 2 extension, already provides delegation, agent identity, audience binding and per-tool-call token minting — start from the scopes your resource server already exposes and layer tool-call scopes on top.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)* | OAuth is only a starting point and is structurally inadequate: scopes like 'read' are too coarse, and even fine-grained OAuth still mints the token for the user rather than the agent — so agents need their own keypairs, a capability directory, and attribute/context/principal-level scoping that OAuth does not express.<br>*[Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)* |

*Why it matters: If existing standards suffice, teams can ship agent access control today on their current IdP; if not, every service must adopt new endpoints and a new principal model before agents can be safely authorized, and the interim depends on translating OpenAPI specs into capabilities.*

### Where should the enforcement point for agent actions live — inside the MCP server/service, or in an external layer between the agent runtime and the server?

| Position A | Position B |
|---|---|
| In the service itself: the server declares fine-grained capabilities that agents discover and scope down against, and MCP servers must limit the tool surface they return based on which user authorized the agent. A data-handling proxy is explicitly rejected as unscalable — the intermediary should only be a directory.<br>*[Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)* | Outside the server: put the chokepoint where the credential is requested (between runtime and MCP server, evaluating policy before minting a token) or in local deterministic hooks that fire asynchronously on tool calls — Snyk explicitly moved off an MCP-server-plus-rule-files integration because agents ignored rule files and scans burned context.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Agentic Development Security](../talks/agentic-development-security.md)* |

*Why it matters: It decides who has to change: thousands of MCP server authors implementing per-user tool filtering and capability declarations, versus a single broker or hook layer that works with servers as they exist today. It also determines whether coverage extends to servers you do not control.*

### Should a server expose narrow, purpose-built, per-caller-scoped tools, or a broad general-purpose surface the agent composes itself?

| Position A | Position B |
|---|---|
| Narrow and curated: package underlying protocols behind a small set of high-level services so the agent is not carrying everything in context, and filter the exposed tool list per authorizing user — a full surface makes agents pick the wrong tools.<br>*[Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)* | Broad and general: text-to-Cypher via CLI plus skills is now dramatically better than a year ago, and as that improves agents will increasingly prefer writing free-form queries over calling prebuilt shape scripts — so expose the query surface and the schema rather than pre-baked tools.<br>*[AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)* |

*Why it matters: It sets whether server maintainers invest in a growing catalog of curated tools or in schema/semantic-layer quality plus guardrails — and a general query surface makes per-user permission scoping much harder to express as tool-level scopes.*

## Practical Guidance

**Do:**

- Audience-bind every downstream access token to a single target MCP server, expire it within a few minutes, and never persist it
- Request a token per tool call rather than per session, so the agent holds permissions only for the action it is currently proposing
- Start scope design from the scopes your resource server already exposes, then layer tool-call-level scopes on top or pass them through
- Filter the tool list an MCP server returns based on which user authorized the agent, instead of returning every tool the application supports
- Give each agent its own private key and identity so actions are attributable per agent, per host, and per user
- Grant read-type capabilities by default per host so approval prompts stay rare enough that users don't reflexively accept everything
- Time-bound agent permissions to the agent's operating window and default to least privilege with just-in-time elevation
- Check the human's approval itself against policy and the approver's role — an approval from someone lacking the role should be overridden
- Batch high-frequency writes triggered by agent traffic (Scalekit batched 'last seen' at one-second granularity after seeing 60x human write rates)
- Run security scanning in asynchronous hooks on tool calls rather than through the model's context window, which adds latency and burns tokens
- For long-running work, return a handle and make the task durable across client, server, and network failure — and persist the task ID, since an unpersisted ID is permanently unrecoverable
- Use graph as a metadata semantic layer over the warehouse; ETL data into the graph only when you need recursive-join performance, graph algorithms, embeddings, or clustering
- Prefer deterministic, structure-based document ingest over LLM entity extraction when the documents already have structure — it is idempotent and faster
- Use one generic containment relationship name across hierarchy levels rather than per-level names, to keep generated Cypher simple
- Return host-rendered UI resources for dense results instead of walls of text, and let the host keep control of what happens on user interaction
- Build agent-facing infrastructure on open standards so it stays compatible with runtimes and protocols that don't exist yet

**Avoid:**

- Handing an agent a .env file or a long-lived kitchen-sink API key that can renew a certificate and drop a database with the same credential
- Treating a human approval click as the access control — approvers are consent-fatigued and background/cloud agents have no human watching
- Relying on model-level refusal as a safety boundary: Claude refused to read a .env file but complied when asked for a specific secret key
- Coarse OAuth scopes like 'read' or 'send email on your behalf' that cannot express time-of-day, sender, or recipient restrictions
- Stateful protocol surfaces — MCP tasks V1's tasks/list had no filter, making it unusable when a million tasks are in flight
- Tunneling input_required through a long-lived tasks/result connection with server-to-client elicitation; the V1 reference client handled these FIFO, so only the first task in flight could be answered
- A per-client polling model for task status, which will not scale to millions of concurrent tasks even under V2
- A proxy that handles the data in the authorization path — it does not scale; make the intermediary a directory instead
- Re-rendering heavy app views on every conversational turn instead of persisting and updating one identified view
- Shipping or installing MCP servers without auditing them — one in twelve developers in Snyk's cohort had a high or critical finding in the server itself
- Defining hundreds of distinct relationship types in a production data model — they stop fitting the model's context window and degrade query generation
- Asking an agent to go straight from an abstract specification to a production distributed implementation; it passes basic tests and breaks on concurrency, process failure, and network failure

## Notable Outliers

- No agent should ever be permitted to drop a database, even when the documented recovery runbook calls for it — the policy should deny it outright rather than escalate. ([It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [13:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=807s))
- One in 12 developers observed had an MCP server with a high or critical severity finding in the server itself; more than half of the group were using MCP servers. ([Agentic Development Security](../talks/agentic-development-security.md), [8:29](https://www.youtube.com/watch?v=cgimkNGNjvU&t=509s))
- The reason no MCP client implements tasks is that client authors are being smart — the spec shipped experimental and is about to change substantially, so not implementing it was the correct call. ([MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [0:01](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1s))
- The main blocker stopping companies from building MCP servers is not technical — it is refusing to be reduced to a textual database and lose brand identity. ([MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [0:55](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=55s))
- For infrastructure vendors the product stops being the server implementation and becomes the specification itself, with bespoke implementations synthesized on demand from an abstract spec plus a deterministic simulation. ([The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [2:02](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=122s))
- Protocol minimalism is a finish line, not a starting point — three years of deliberately removing abstractions was the precondition for an agent being able to synthesize a correct implementation. ([The Prompt is the Platform](../talks/the-prompt-is-the-platform.md), [7:58](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=478s))
- Agents are never fully detached principals — every agent token always reports to a user — but the v1 assumption that agents are ephemeral is already outdated, and long-lived organizational agents need their own policy model. ([Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [20:32](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1232s))
- Servers should not ETL warehouse data into a graph for most agent use cases; pull only metadata, partly because security posture often forbids moving sensitive data across systems at all. ([AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md), [37:30](https://www.youtube.com/watch?v=kRkcNOsRyYg&t=2250s))

## All Talks

- [Agentic Development Security](../talks/agentic-development-security.md)
- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [AI on Your Lakehouse: Context Comes in Shapes, Not Queries](../talks/ai-on-your-lakehouse-context-comes-in-shapes-not-queries.md)
- [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)
- [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)
- [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)
- [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)
- [The Prompt is the Platform](../talks/the-prompt-is-the-platform.md)
- [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)

## Speakers

- [Armanas Povilionis](../speakers/armanas-povilionis.md)
- [Cornelia Davis](../speakers/cornelia-davis.md)
- [Dominik Tornow](../speakers/dominik-tornow.md)
- [Ezra Tanzer](../speakers/ezra-tanzer.md)
- [Ido Salomon](../speakers/ido-salomon.md)
- [Kim Maida](../speakers/kim-maida.md)
- [Liad Yosef](../speakers/liad-yosef.md)
- [Paola Estefania](../speakers/paola-estefania.md)
- [Ravi Madabhushi](../speakers/ravi-madabhushi.md)
- [Zach Blumenfeld](../speakers/zach-blumenfeld.md)

