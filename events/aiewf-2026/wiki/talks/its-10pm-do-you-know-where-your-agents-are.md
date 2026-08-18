---
title: "It's 10pm. Do You Know Where Your Agents Are?"
type: "talk"
slug: "its-10pm-do-you-know-where-your-agents-are"
track: "Security"
org: "Keycard"
day: "Day 2 — Session Day 1"
room: "Track 5"
video_id: "I3znWC3MEXM"
duration_sec: 1382
word_count: 3454
speakers: ["Kim Maida"]
---

# It's 10pm. Do You Know Where Your Agents Are?

**Speakers:** [Kim Maida](../speakers/kim-maida.md)

**Org:** Keycard

**Track:** Security &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 23m 02s

[Watch on YouTube](https://www.youtube.com/watch?v=I3znWC3MEXM)

## Summary

Kim Maida (Keycard) argues that the standard way we give agents access — an .env file full of long-lived, broadly-scoped API keys — makes every agent overprivileged and unattributable, and that this is already causing real production damage. She demonstrates the failure mode live with an incident-triage agent that drops a billing database, takes prod offline, and incurs cloud spend, all with the same 'kitchen sink' API key, then re-runs the identical agent with OAuth token exchange (RFC 8693) in place. The fix routes every proposed tool call through a security token service that mints a short-lived, ephemeral, audience-bound token scoped to that one call, with governance policy evaluated *before* the credential is minted — so an out-of-policy credential never exists to leak, replay, or steal. She also argues human-in-the-loop is not a control by itself: her demo blocks a restart-prod action she personally approved, because policy checked the operator's role. Worth watching for a concrete, standards-based architecture diagram of where to insert access control in the agent execution path, and for the demo contrast between the two runs.

## Key Points

- Agents given raw API keys are overprivileged by construction: a single key that can read tickets, renew certificates, restart prod, and scale infrastructure lets the agent take any of those actions on its own judgment.
- API-key-based access produces audit logs with no identity attribution — you can see which endpoint was called but not which user or agent was behind it.
- Supervision does not fix this, because agents act mid-task on decisions the user never asked for, and an increasing share of agents run fully unsupervised.
- Human-in-the-loop is insufficient on its own: consent-fatigued or half-asleep operators will approve anything, so approvals must themselves be checked against policy and the approver's role.
- RFC 8693 token exchange, an existing extension to OAuth 2 rather than a new spec, can be used to issue per-tool-call credentials inside the agent execution path.
- The architecture narrows access twice: first when the user delegates only a subset of their permissions to the agent, then again when the security token service grants a token for one specific tool call.
- Downstream tokens should be audience-bound to the target MCP server, short-lived (minutes), and ephemeral — never stored, discarded immediately after the call.
- Evaluating policy before minting the credential is the key security property: a denied action produces no credential at all, so there is nothing to leak, replay, or steal.
- Because the approach is built on open standards, it composes with off-the-shelf and custom agents, CLIs, third-party and proprietary MCP servers, gateways, agent-to-agent protocols, and any OAuth identity provider.
- For teams starting on scope design, the resource server's existing scopes are the baseline, with tool-call-level scopes layered on top or passed through.

## Notable Quotes

> "we're entrusting agents with more and more responsibility, but we still kind of need that public service announcement that says it's 10 p.m."
>
> — [0:01](https://www.youtube.com/watch?v=I3znWC3MEXM&t=1s) &middot; *States the talk's framing thesis in the speaker's own words.*

> "we know agents without access aren't useful. So, we give them an end file and we give them some API keys and we let them run off and go do their thing. And this is fine until it's not."
>
> — [0:48](https://www.youtube.com/watch?v=I3znWC3MEXM&t=48s) &middot; *Names the default practice the whole talk is arguing against.*

> "it's using the same API key now that it did to renew the certificate, right? Because that API key is a kitchen sink. It can do all of these things with it."
>
> — [3:51](https://www.youtube.com/watch?v=I3znWC3MEXM&t=231s) &middot; *The 'kitchen sink' credential is the concrete mechanism behind overprivilege.*

> "So it goes ahead and it drops the database and then it doesn't have a way to check to see if it was backed up. So it just escalates that for the morning. And this has really happened, right? Like it's happened to high-profile companies."
>
> — [3:09](https://www.youtube.com/watch?v=I3znWC3MEXM&t=189s) &middot; *The demo's most damaging failure, explicitly tied to real-world incidents.*

> "So agents with API keys are indeed outpass 10. They're overprivileged. So this means they are able to act freely on decisions that they make that you may or may not agree with. And they can do this even with your supervision."
>
> — [4:32](https://www.youtube.com/watch?v=I3znWC3MEXM&t=272s) &middot; *Compresses the problem statement and rules out supervision as a fix.*

> "agents want to be helpful. they're going to use all the permissions that they have access to in order to get the job done."
>
> — [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s) &middot; *Explains why capability granted is capability used — the argument for least privilege.*

> "And we can't just solve this with human in the loop. We spent decades solving access management for humans. So just blindly trusting a human who might be a little bit consent fatigued uh or who might be tired enough at night, this isn't really going to be enough."
>
> — [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s) &middot; *The talk's most contestable position, stated directly.*

> "there are a few places in this path where we could implement real access control and we can actually do this with open standards and as kind of a spoiler it's not just OOTH."
>
> — [7:20](https://www.youtube.com/watch?v=I3znWC3MEXM&t=440s) &middot; *Marks the pivot from problem to the standards-based solution.*

> "we have credentials that are being used that aren't attributed to a user or an agent identity. We have an agent that has unrestricted access to any and all permissions that are in an API key."
>
> — [7:59](https://www.youtube.com/watch?v=I3znWC3MEXM&t=479s) &middot; *Enumerates the specific defects the architecture is designed to remove.*

> "the authorization server is then going to prompt the user for their consent to delegate access with a subset of their permissions. And this is the first narrowing of access"
>
> — [8:45](https://www.youtube.com/watch?v=I3znWC3MEXM&t=525s) &middot; *Names the first of the two narrowing steps in the design.*

> "this request is asking for permissions to access the MCP server for that tool call but only that tool call."
>
> — [9:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=567s) &middot; *The precise granularity claim — per-tool-call scoping, not per-session.*

> "We know the identity of the agent that's requesting access. We know the identity of the user on whose behalf is acting. And we know the delegating user's level of access as well."
>
> — [10:11](https://www.youtube.com/watch?v=I3znWC3MEXM&t=611s) &middot; *The three-part identity chain that replaces the anonymous API key.*

> "this token has an audience declaring that only this target MCP server is allowed to use it to make requests."
>
> — [10:11](https://www.youtube.com/watch?v=I3znWC3MEXM&t=611s) &middot; *Specifies audience binding as a concrete containment property.*

> "It should be short-lived uh often expiring within a few minutes and it's also ephemeral meaning it should never be stored."
>
> — [11:03](https://www.youtube.com/watch?v=I3znWC3MEXM&t=663s) &middot; *Gives the actual lifetime recommendation for downstream tokens.*

> "no agent should be able to drop a database"
>
> — [13:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=807s) &middot; *A blunt policy stance that others might argue is context-dependent.*

> "So the policy evaluates before the credential is minted, which means you don't have an overprivileged credential that's just floating around"
>
> — [13:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=807s) &middot; *The central architectural claim distinguishing this from downstream enforcement.*

> "So there's nothing to leak, there's nothing to replay, and there's nothing to steal."
>
> — [14:16](https://www.youtube.com/watch?v=I3znWC3MEXM&t=856s) &middot; *The security payoff of pre-mint policy evaluation, stated as a three-part claim.*

> "there's another policy here that says that the human user needs to have a specific role in order to be able to do this. And I actually do not have that role. So it's going to prevent me from being able to allow the agent to do this. uh even though I approved it."
>
> — [14:54](https://www.youtube.com/watch?v=I3znWC3MEXM&t=894s) &middot; *Demonstrates policy overriding human approval — the answer to consent fatigue.*

> "The agent also has task scoped short-lived ephemeral access and human in the loop actually has access control that is backed by real policy. So an exhausted person can't just accept everything that happens."
>
> — [15:33](https://www.youtube.com/watch?v=I3znWC3MEXM&t=933s) &middot; *Summarizes the end state of the second demo.*

> "It works with OpenClaw and basically anything that might come out next week."
>
> — [16:38](https://www.youtube.com/watch?v=I3znWC3MEXM&t=998s) &middot; *The forward-compatibility argument for choosing open standards over bespoke controls.*

> "So, it's not actually a new spec, which is, you know, it it's kind of one of those things like there was this period of time where people were like, oh, you can just use OOTH for for this."
>
> — [20:35](https://www.youtube.com/watch?v=I3znWC3MEXM&t=1235s) &middot; *Her direct answer to enterprise adoption resistance.*

> "But an agent, you don't want an agent to be using any of those grants that it wants on every single tool call."
>
> — [19:23](https://www.youtube.com/watch?v=I3znWC3MEXM&t=1163s) &middot; *Explains why a user OAuth token can't simply be handed to an agent.*

> "if your resource server already has like specific scopes, that's going to be kind of your place to start because the downstream token, the one that was the OS token for the user is going to have the scopes for the resource"
>
> — [22:02](https://www.youtube.com/watch?v=I3znWC3MEXM&t=1322s) &middot; *Actionable guidance on where to begin scope design.*

## Positions

- Giving agents long-lived API keys makes them overprivileged and lets them act on decisions the user may not agree with, even under supervision. ([4:32](https://www.youtube.com/watch?v=I3znWC3MEXM&t=272s), confidence: stated)
- Human-in-the-loop approval alone is not a sufficient access control, because humans are consent-fatigued and make mistakes, and many agents run autonomously anyway. ([5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s), confidence: stated)
- An agent will use every permission it has access to in order to complete a task. ([5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s), confidence: stated)
- Agent access control does not require a new specification; RFC 8693 token exchange, an existing OAuth 2 extension, is sufficient. ([7:20](https://www.youtube.com/watch?v=I3znWC3MEXM&t=440s), confidence: stated)
- Tokens should be requested per tool call rather than per session, so the agent only receives permissions for the single action it is currently proposing. ([9:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=567s), confidence: stated)
- Downstream access tokens should be audience-bound to a single target MCP server, expire within a few minutes, and never be stored. ([11:03](https://www.youtube.com/watch?v=I3znWC3MEXM&t=663s), confidence: stated)
- No agent should be permitted to drop a database, even when the documented recovery procedure calls for it. ([13:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=807s), confidence: stated)
- Evaluating policy before minting a credential is strictly safer than issuing a broad credential and restricting its use, because a denied action leaves nothing to leak, replay, or steal. ([14:16](https://www.youtube.com/watch?v=I3znWC3MEXM&t=856s), confidence: stated)
- A human's approval of an agent action should itself be checked against policy and the approver's role, and can be overridden. ([14:54](https://www.youtube.com/watch?v=I3znWC3MEXM&t=894s), confidence: stated)
- Building on open standards makes the access-control layer forward-compatible with agent frameworks and protocols that do not exist yet. ([16:38](https://www.youtube.com/watch?v=I3znWC3MEXM&t=998s), confidence: stated)
- Teams defining scopes should start from the scopes their resource server already exposes, then layer tool-call-level scopes on top or pass them through. ([22:02](https://www.youtube.com/watch?v=I3znWC3MEXM&t=1322s), confidence: stated)
- The right place to enforce access control is between the runtime and the MCP server, at the point the token is requested, rather than only at the resource. ([18:20](https://www.youtube.com/watch?v=I3znWC3MEXM&t=1100s), confidence: implied)

## Concepts

- [agent identity and authorization](../concepts/agent-identity-and-authorization.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [automation bias](../concepts/automation-bias.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [mcp server design](../concepts/mcp-server-design.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)

