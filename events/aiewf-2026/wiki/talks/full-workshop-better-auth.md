---
title: "Full Workshop: Better Auth"
type: "talk"
slug: "full-workshop-better-auth"
track: "Security"
org: "Better Auth"
video_id: "JvKO40CFq-s"
duration_sec: 2455
word_count: 5648
speakers: ["Paola Estefania"]
---

# Full Workshop: Better Auth

**Speakers:** [Paola Estefania](../speakers/paola-estefania.md)

**Org:** Better Auth

**Track:** Security &nbsp;|&nbsp; **Duration:** 40m 55s

[Watch on YouTube](https://www.youtube.com/watch?v=JvKO40CFq-s)

## Summary

Paola Estefania walks through the Agent Auth protocol, an open draft spec that treats AI agents as first-class security principals rather than as software impersonating the user with the user's own credentials. The workshop is structured around three problems — discovery (how an agent learns what it can do), authorization (how you scope down what it may do), and identity (how you trace and revoke it) — and proposes a well-known agent-configuration endpoint, a capability directory that translates existing OpenAPI specs into fine-grained capabilities, and per-agent private keys for signing tokens. A live demo connects Claude to the project's MCP server, reads Gmail with a read-only default, requests approval to gain send capability, shows the resulting per-agent audit log, and then revokes the agent mid-session. It is heavily interactive and Q&A-driven rather than code-heavy, so it's best for people thinking about agent identity architecture and delegated authorization, not for those wanting an implementation tutorial. Worth watching if you care about how agent permissioning should differ from OAuth scopes; skippable if you want polished slides or production patterns, since the spec is admittedly early and a v2 draft is still in progress.

## Key Points

- Today's common pattern — handing an agent your personal token or connecting an MCP server under your own account — makes the agent act on your behalf by pretending to be you, which is equivalent to giving a new hire the CEO's credentials.
- The proposal reframes the agent as the principal actor with its own identity, rather than an anonymous process hiding behind the user's session.
- The protocol identifies three distinct problems: discovery (agents finding what a service offers), authorization (scoping down what they may do), and identity (attribution, audit, and revocation).
- Capabilities are proposed as a replacement for OAuth scopes because a scope like 'read' is too coarse to express which specific actions an agent may take.
- Because almost no service implements the proposed well-known agent-configuration endpoint yet, the project ships a directory that translates existing OpenAPI JSON specs into per-endpoint capabilities as a bridge.
- Each agent gets its own private key and signs its own tokens, which produces logs showing which agent, from which host, did what on behalf of which user.
- Identity enables granular revocation: instead of disconnecting an entire integration, you revoke a single agent or an entire host, and the demo showed a revoked agent losing access mid-conversation.
- The design deliberately trades some security for usability — read-type capabilities are granted by default per host so users aren't prompted for every action — and policies are being extended to hosts and users in a forthcoming v2 draft.
- The speaker rejects a proxy architecture as unscalable because a proxy handles the data, positioning their component as a directory that only matches intent to capabilities.

## Notable Quotes

> "We're actually doing like the agent is acting on behalf of us but pretending to be us."
>
> — [1:41](https://www.youtube.com/watch?v=JvKO40CFq-s&t=101s) &middot; *states the core problem the entire protocol is designed around*

> "The idea will be hire your agent in a sense of give them your agents authority instead of your credentials."
>
> — [3:12](https://www.youtube.com/watch?v=JvKO40CFq-s&t=192s) &middot; *the talk's central slogan and design principle*

> "for me the most interesting thing of all is we need to stop giving credentials our credentials to our agents we need to give them authority"
>
> — [36:58](https://www.youtube.com/watch?v=JvKO40CFq-s&t=2218s) &middot; *the speaker's own summary of the takeaway*

> "this should we stop saying like pretend to be me instead of saying like act for me within these limits"
>
> — [36:58](https://www.youtube.com/watch?v=JvKO40CFq-s&t=2218s) &middot; *crisp formulation of impersonation versus scoped delegation*

> "we have the discovery issue where the agent can go find the service and read the capabilities authorization what this agent can do can do scope down and who is this agent"
>
> — [8:23](https://www.youtube.com/watch?v=JvKO40CFq-s&t=503s) &middot; *enumerates the three problems the protocol layers map onto*

> "The other capability is what can do, but it's more cap down. So I can actually determine what an action agent can do."
>
> — [9:17](https://www.youtube.com/watch?v=JvKO40CFq-s&t=557s) &middot; *the capabilities-over-scopes argument in the speaker's words*

> "So most of the common services we use they all implement open API."
>
> — [11:49](https://www.youtube.com/watch?v=JvKO40CFq-s&t=709s) &middot; *the assumption that makes the OpenAPI-to-capabilities bridge viable*

> "So the directory will be like a phone directory for the agent."
>
> — [14:54](https://www.youtube.com/watch?v=JvKO40CFq-s&t=894s) &middot; *the governing analogy for the discovery layer*

> "So what we are switching is the principle. We now want that the agents are a principal actor."
>
> — [15:44](https://www.youtube.com/watch?v=JvKO40CFq-s&t=944s) &middot; *names the paradigm shift that distinguishes this from fine-grained OAuth*

> "so what we come is giving agents like a private key like famous private key. So each agent will have its own and that will be attached to the identity."
>
> — [16:34](https://www.youtube.com/watch?v=JvKO40CFq-s&t=994s) &middot; *concrete mechanism behind agent identity*

> "We stop seeing as an agent is like hiding behind the user and now the agent is there as a principal acting."
>
> — [18:38](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1118s) &middot; *restates the identity thesis in terms of what logs will show*

> "Always the token always the agents they always have a user they are reporting to you. They are never detached."
>
> — [19:27](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1167s) &middot; *answers whether agents can be fully autonomous principals — they cannot*

> "because we did this in February, the things changed so much until now. Like for example, Asians are not so ephemeral."
>
> — [20:32](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1232s) &middot; *acknowledges the v1 spec's assumptions have already aged*

> "Our idea is like to be safe but not to be annoying. Imagine every time you had to read something. Oh, I had to approve every time. You're going to hate us"
>
> — [31:51](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1911s) &middot; *names the security-versus-UX tradeoff explicitly*

> "our actually proxy is just a directory. It's not a real proxy for us like proxy is a really bad idea. It's not scalable because proxy uses data."
>
> — [35:56](https://www.youtube.com/watch?v=JvKO40CFq-s&t=2156s) &middot; *a rejected architecture others in the space do adopt*

> "Because they are not still treating ancient as a principle. We are treating nations as a principle. They have their own identity."
>
> — [39:07](https://www.youtube.com/watch?v=JvKO40CFq-s&t=2347s) &middot; *the claimed differentiator from existing solutions (transcript garbles 'agent')*

> "AI gateway doesn't have doesn't do that yet I hope it does but the whole idea is to have like traceability"
>
> — [39:07](https://www.youtube.com/watch?v=JvKO40CFq-s&t=2347s) &middot; *direct comparison against AI gateways as an alternative*

## Positions

- Giving an agent the user's own credentials or personal token is the wrong model; agents should receive delegated authority scoped to specific actions instead. ([3:12](https://www.youtube.com/watch?v=JvKO40CFq-s&t=192s), confidence: stated)
- OAuth-style scopes such as 'read' are too coarse for agents, and fine-grained capabilities should replace them. ([9:17](https://www.youtube.com/watch?v=JvKO40CFq-s&t=557s), confidence: stated)
- Even fine-grained OAuth is insufficient because it still mints a token for the user; the agent must be the principal that holds the token. ([15:44](https://www.youtube.com/watch?v=JvKO40CFq-s&t=944s), confidence: stated)
- Every agent should hold its own private key and sign its own tokens so actions are attributable per agent, per host, and per user. ([16:34](https://www.youtube.com/watch?v=JvKO40CFq-s&t=994s), confidence: stated)
- Agents are never fully detached principals — each one always reports to a user. ([19:27](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1167s), confidence: stated)
- Read-type capabilities should be granted by default per host because prompting for approval on every action would make the system unusable. ([31:51](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1911s), confidence: stated)
- A proxy architecture for agent authorization is a bad idea because handling the data makes it unscalable; a directory that matches intent to capabilities is the right shape. ([35:56](https://www.youtube.com/watch?v=JvKO40CFq-s&t=2156s), confidence: stated)
- AI gateways do not provide per-agent identity or lifecycle traceability, which is what distinguishes this protocol from them. ([39:07](https://www.youtube.com/watch?v=JvKO40CFq-s&t=2347s), confidence: stated)
- Because few or no services implement agent-native auth endpoints today, translating existing OpenAPI specs into capabilities is a necessary interim bridge. ([10:53](https://www.youtube.com/watch?v=JvKO40CFq-s&t=653s), confidence: stated)
- The v1 spec's assumption that agents are ephemeral is outdated, and long-lived and organizational agents require policy support being added in v2. ([20:32](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1232s), confidence: stated)
- Agent security should not be an enterprise-only concern; the protocol is open source so that individual AI users benefit too. ([21:29](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1289s), confidence: stated)

## Concepts

- [agent identity and authorization](../concepts/agent-identity-and-authorization.md)
- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [audit trails](../concepts/audit-trails.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [mcp server design](../concepts/mcp-server-design.md)

