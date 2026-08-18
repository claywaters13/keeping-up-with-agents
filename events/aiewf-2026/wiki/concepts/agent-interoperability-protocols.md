---
title: "agent interoperability protocols"
type: "concept"
slug: "agent-interoperability-protocols"
tier: "supporting"
maturity: "contested"
talk_count: 10
speaker_count: 11
---

# agent interoperability protocols

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **10** talk(s) by **11** speaker(s)

**Definition:** Open protocols letting agents, clients, and services from different vendors talk to each other, and the open-versus-walled-garden dynamics around them.

*Also referred to as: agent-to-agent protocol, agent client protocol, protocol interoperability, open protocols vs walled gardens, protocol extensions, interface protocol design, json-rpc protocol design, client capability negotiation*

## State of Practice

The field has settled on the shape of the answer — a vendor-neutral, JSON-RPC-style spec layer that lets heterogeneous agents, clients, and services interoperate without sharing a runtime — and is now fighting over which specs win and who holds power in the resulting topology. MCP is treated as the substrate, with MCP Apps ratified as the official extension for returning UI (sandboxed iframe widgets) and ChatGPT/Claude/Cursor self-serve app stores now open; ACP fills the parallel niche for coding-agent-to-editor interop with ~40 client implementations and an explicit LSP analogy; A2A and A2UI show up as front-end/back-end contracts inside production systems. The consistent technical lesson is that the protocol should transmit typed intent and let the host own rendering, filesystem access, terminals, and interaction control — servers that return only text are described as "factually correct but useless." The layers above transport are visibly unfinished: MCP tasks (async/durable execution) has zero client implementations and is mid-rewrite from stateful V1 to stateless V2, agent identity is still being argued (OAuth scopes vs. per-agent keypairs where the agent is the principal), and payments, discovery registries, and cross-org trust exist mostly as new proposals (NANDA's agent facts, Froglet's signed receipts). The loudest unresolved question is political rather than technical: whether the endgame is an open agent web or a handful of proprietary assistant app stores that own every user journey.

## Consensus

### Interoperability belongs at a vendor-neutral wire protocol, not a shared runtime or SDK — different implementations should interoperate through a spec, explicitly modeled on LSP/HTTP.

Support: **5** talk(s)

> "And so that's why we decided we need some kind of type of protocol uh called agent client protocol, uh which is similar to like MCP or uh LSP."
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [0:14](https://www.youtube.com/watch?v=HsxQICTLF84&t=14s)

Supporting talks: [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)

### A protocol that carries only text or raw JSON back to the user is inadequate; tool responses must be able to carry structured UI that the client renders.

Support: **3** talk(s)

> "So, it reached out to the PostHog server, got back the textual response. It's factually correct, but it's useless."
>
> — [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [6:49](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=409s)

Supporting talks: [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)

### The host/client keeps control of presentation and side effects — rendering, diffing, filesystem access, terminals, interaction routing — while the agent side sends only intent and data.

Support: **3** talk(s)

> "The host decides what to do. The host keeps this control of the flow."
>
> — [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [6:09](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=369s)

Supporting talks: [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)

### Cross-organizational discovery, identity, and trust — not local tool capability — are the binding constraints, and they require signed, machine-readable capability metadata rather than name-to-address lookup.

Support: **4** talk(s)

> "The hard problems of the agent web live between agents at scale. So, how thousands of them discover each other, prove who they are, decide whom to trust, and coordinate with no central authority."
>
> — [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [9:06](https://www.youtube.com/watch?v=sum9DgexFRQ&t=546s)

Supporting talks: [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)

### These specs are moving faster than implementations: multiple speakers reported shipping against specs that were experimental, already superseded, or missing transports and lifecycle guarantees they needed.

Support: **4** talk(s)

> "back to the question of why the heck aren't there any clients that are supporting this protocol? Yeah. That's why. Super involved. It's still involved with V2, but it gets better."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [15:14](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=914s)

Supporting talks: [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)

## Disagreements

### Should agent interop consolidate inside a few assistant hosts and their app stores, or route around them via open peer-to-peer infrastructure?

| Position A | Position B |
|---|---|
| Build into the hosts: MCP Apps is the distribution channel, the ChatGPT/Claude/Cursor stores are where discovery happens, and websites will dissolve into UI chunks composed by a personal assistant that owns the whole user journey.<br>*[MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)* | That topology is the AOL era repeating — proprietary agent stores are walled gardens; discovery should run over an open registry of signed agent facts, and once two parties find each other the transaction should be direct with no third party mediating quote, execution, or receipt.<br>*[The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)* |

*Why it matters: It determines whether your interop investment is a store listing subject to a host's submission process and ranking, or a self-hosted node with its own identity and payment rails. One side predicts brands regain identity through host-rendered UI; the other predicts they lose all visibility into the user journey.*

### Who owns the UI vocabulary in an agent-to-client protocol — the server that ships arbitrary UI, or the client that publishes a fixed component catalog?

| Position A | Position B |
|---|---|
| The server sends its own interface (a sandboxed iframe widget), and the protocol should be agnostic to how that UI was produced — predefined, declarative, or fully generative.<br>*[MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)* | The model must only select from a fixed catalog the client supplied in context, gated by client app version; open-ended generation is wrong for production clients because an unrecognized content type crashes an unpatchable app for weeks.<br>*[Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)* |

*Why it matters: Server-owned UI makes brand identity and write-once-run-everywhere possible but pushes trust and version-skew risk onto every client; client-owned catalogs are safe on mobile but mean each host must implement components before any server can use them.*

### Can an agent be a transacting principal that commits to work autonomously, or must every consequential action route back through a human?

| Position A | Position B |
|---|---|
| Organizations will give agents budgets, and agents will discover services, negotiate terms, pay, and collect signed receipts across organizational boundaries — the receipt chain, not human review, is what makes the result trustworthy.<br>*[Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)* | Agents get delegated authority and their own key, but they are never detached — every agent reports to a user, and the loop should deterministically interrupt for approval on mutating tool calls rather than letting the model judge.<br>*[Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)* |

*Why it matters: It decides whether the protocol needs a payments/negotiation layer with cryptographic non-repudiation, or an approval and capability-scoping layer with a human in the driver's seat — and which of the two your audit story rests on.*

## Practical Guidance

**Do:**

- Implement ACP's four required functions over JSON-RPC on stdio to make an existing CLI agent work in any of the ~40 compatible clients; a bare-minimum coding agent needs only read-file and edit-file tools.
- Read files through the client's proxied filesystem capability rather than native fs APIs, so the agent sees unsaved editor buffer state.
- Send old text and new text as a diff content type and let the client compute and render the diff; likewise let the client create and manage terminals.
- Gate component availability by client app version inside the model's context (e.g. offer the 2.0 flight card only to 2.0+ clients), and give the model a fixed component menu it can select from but never extend.
- Return alternate non-UI output alongside a widget, so clients that don't support MCP Apps degrade gracefully and the model isn't starved of the data.
- Split tool output into UI-visible and model-visible channels when working in privacy-sensitive domains, so displayed data never reaches the LLM provider unless you choose.
- Adopt an external spec (A2A, ACP, MCP Apps) as the literal front-end/back-end contract — speakers reported it drove team alignment faster than a house-designed interface.
- Deterministically interrupt the agent loop when a tool call requires approval, especially for mutating operations, instead of leaving the decision to the model.
- Give each agent its own private key and identity so actions are attributable per agent, per host, and per user; grant read-type capabilities by default per host to avoid approval fatigue.
- Persist task IDs on the client side for async MCP tasks — the spec says 'should,' but an unpersisted ID is permanently unrecoverable.
- Use the official mcp-apps SDK rather than a wrapper, since maintainers reflect spec changes there immediately.
- Simulate a protocol under load before it becomes load-bearing on real infrastructure.

**Avoid:**

- Handing an agent your own credentials or personal token so it can pretend to be you — delegate scoped authority instead.
- Relying on coarse OAuth scopes like 'read' for agent authorization; they don't express what a specific action is allowed to do.
- Building a proxy that handles the data in the authorization path — it doesn't scale; a directory that matches intent to capabilities does.
- Prompting the user for approval on every action, including reads — it makes the system unusable.
- Building against MCP tasks V1: the stateful tasks/list endpoint has no filter (unusable at a million tasks) and input_required tunneled through a long-lived tasks/result connection with server-to-client elicitation is why no client shipped it. The V1 reference client handles input_required FIFO, so only the first in-flight task can be answered.
- Assuming per-client polling scales — even V2's model breaks down at a million concurrent tasks without a notifications protocol.
- Sending unknown content types to mobile clients: they don't degrade gracefully, they crash, and you cannot meaningfully patch them.
- Re-rendering a heavy app view on every turn instead of persisting and updating one view via a server-supplied identifier.
- Treating chat, prompting, or voice as the universal interface — all three are the same single-slot batch protocol with a faster clock.

## Notable Outliers

- Making an existing agent ACP-compatible takes about 15 minutes and four functions, and ACP already has ~40 client implementations including JetBrains and Obsidian. ([Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [16:38](https://www.youtube.com/watch?v=HsxQICTLF84&t=998s))
- Zero MCP clients support MCP tasks — and that is the correct engineering call, not a failure of adoption. ([MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [0:01](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1s))
- Claude is currently the only client that performs dynamic MCP registry discovery, searching the registry for a connector when a task has no matching tool. ([MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [25:39](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1539s))
- Whether a product ships an MCP server has become a primary purchasing criterion. ([MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [26:31](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1591s))
- MCP Apps addresses roughly 170 times the total addressable market the Apple App Store had at launch. ([MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [17:26](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1046s))
- Closed-source data collaboration takes years and millions before a reusable workflow exists; exposing the same resource behind an open protocol costs a few thousand tokens and minutes. ([Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [5:37](https://www.youtube.com/watch?v=Fu45geO3zX8&t=337s))
- Loss of brand identity — being reduced to a textual database — is the main reason companies have not built MCP servers. ([MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [0:55](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=55s))
- Prompt engineering is not a power-user skill but a packaging ritual for a batch protocol, the same mastery a punch-card operator had. ([The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [7:56](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=476s))
- Tools and skills are a sufficient abstraction — no further orchestration primitives are needed on top. ([Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [16:16](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=976s))

## All Talks

- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)
- [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)
- [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)
- [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)
- [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)
- [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)
- [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)

## Speakers

- [Armanas Povilionis](../speakers/armanas-povilionis.md)
- [Bala Ramdoss](../speakers/bala-ramdoss.md)
- [Bennet Fenner](../speakers/bennet-fenner.md)
- [Cornelia Davis](../speakers/cornelia-davis.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Ido Salomon](../speakers/ido-salomon.md)
- [Liad Yosef](../speakers/liad-yosef.md)
- [Paola Estefania](../speakers/paola-estefania.md)
- [Pietro Zullo](../speakers/pietro-zullo.md)
- [Ramesh Raskar](../speakers/ramesh-raskar.md)
- [Ted Johnson](../speakers/ted-johnson.md)

