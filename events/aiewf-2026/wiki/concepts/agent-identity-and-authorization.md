---
title: "agent identity and authorization"
type: "concept"
slug: "agent-identity-and-authorization"
tier: "supporting"
maturity: "contested"
talk_count: 7
speaker_count: 6
---

# agent identity and authorization

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **7** talk(s) by **6** speaker(s)

**Definition:** Giving agents their own principals, credentials, and delegated authority so their actions are attributable and scoped to a user's grant.

*Also referred to as: agent identity, agent authentication and identity, delegated authorization, delegated authority, oauth scopes, capability-based authorization, just-in-time authorization, principal-actor binding*

## State of Practice

The field has converged on a diagnosis and is still arguing about the substrate. Everyone agrees the current deployment pattern — hand the agent a long-lived API key or replay the user's own OAuth token so the agent "pretends to be" the user — is broken, because the authenticating principal is no longer the acting principal and the acting program is no longer deterministic or inspectable. The emerging shape is: the agent gets its own identity bound at all times to a delegating user, credentials are minted per tool call rather than per session, tokens are audience-bound to a single resource, expire in minutes, and are never stored, and policy is evaluated before the credential is issued rather than enforced after. Fine-grained beats scope-grained: speakers repeatedly attacked coarse grants like Gmail's "send email on your behalf" for having no notion of time window, sender, recipient, or per-tool restriction, and pushed attribute-, context-, and principal-level scoping with least privilege by default and just-in-time elevation. The open dispute is whether this is an OAuth extension problem (Keycard: RFC 8693 token exchange, no new spec) or requires a new agent-native protocol where the agent itself is the token-holding principal (Better Auth, Scalekit). Separately, the inbound half of the problem — how a website tells a good agent from a bad bot, now that CAPTCHAs no longer discriminate — is universally acknowledged as unbuilt: there is no certificate-authority-equivalent for agents, and DNS-era discovery does not survive agents that migrate between hosts in milliseconds.

## Consensus

### An agent must be its own principal with its own identity, bound to the delegating user, rather than acting as the user with the user's credentials.

Support: **4** talk(s)

> "the actor, in this case, an agent, has to be bound to the principal at all times. And the agent should have its own identity."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [9:08](https://www.youtube.com/watch?v=lMCxVorb9wM&t=548s)

Supporting talks: [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)

### Long-lived broad credentials (a "kitchen sink" API key or a session-long OAuth grant) are the specific mechanism by which agents cause production incidents; credentials must be narrowed to the single action being taken and made short-lived.

Support: **4** talk(s)

> "it's using the same API key now that it did to renew the certificate, right? Because that API key is a kitchen sink. It can do all of these things with it."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [3:51](https://www.youtube.com/watch?v=I3znWC3MEXM&t=231s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### Existing OAuth scope granularity is too coarse for agents — it cannot express time-of-day, per-recipient, per-sender, or per-tool-call constraints — so authorization must move to fine-grained capabilities.

Support: **3** talk(s)

> "There's no extremely fine-grained scoping to say can this agent act at this hour? Can this agent read emails only from these senders? Can this agent send emails to only this recipients?"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [9:08](https://www.youtube.com/watch?v=lMCxVorb9wM&t=548s)

Supporting talks: [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)

### Human-in-the-loop approval is not a sufficient access control, because approvers are consent-fatigued and reliably rubber-stamp confidently-wrong agent output.

Support: **3** talk(s)

> "And we can't just solve this with human in the loop. We spent decades solving access management for humans. So just blindly trusting a human who might be a little bit consent fatigued uh or who might be tired enough at night, this isn't really going to be enough."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)

### An agent will exercise every permission it holds, and unlike a deterministic service account its behavior cannot be bounded by code review — so over-permissioning is a design defect, not a developer mistake.

Support: **3** talk(s)

> "agents want to be helpful. they're going to use all the permissions that they have access to in order to get the job done."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### Full attribution is a hard requirement: every action must record which agent acted, on whose behalf, who authorized it, what was authorized, and for how long.

Support: **3** talk(s)

> "you have to have absolute visibility into what your agent can do, every action that's taken in your system, who took it, on behalf of whom, and who authorized it, when was the authorization given, what authorization was given, how long is it given for"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [11:43](https://www.youtube.com/watch?v=lMCxVorb9wM&t=703s)

Supporting talks: [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)

### The inbound side — a service verifying that an incoming agent is a legitimate delegate rather than a bad bot — has no working infrastructure today; CAPTCHA no longer discriminates and no trust issuer or agent-native auth endpoint is widely deployed.

Support: **3** talk(s)

> "The web was built to stop bad bots, but now there's good agents and bad bots. How do we delineate between the two?"
>
> — [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [12:41](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=761s)

Supporting talks: [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)

## Disagreements

### Is agent authorization an extension of existing OAuth, or does it require a new agent-native protocol?

| Position A | Position B |
|---|---|
| No new specification is needed — RFC 8693 token exchange, an existing OAuth 2 extension, already expresses agent identity, delegating user identity, audience binding, and per-tool-call narrowing, and building on it keeps you forward-compatible with frameworks that don't exist yet.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)* | OAuth is a starting point but structurally insufficient, because even fine-grained OAuth still mints a token for the user; a new protocol is required in which the agent itself is the token-holding principal, discovering services and capabilities through a directory.<br>*[Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)* |

*Why it matters: It determines whether teams can ship agent access control today on their existing authorization server and IdP, or must wait on (and adopt) a new spec plus ecosystem-wide service support that essentially no provider implements yet.*

### Should an agent hold its own long-lived key material, or should it hold no resident credentials at all?

| Position A | Position B |
|---|---|
| Every agent should be issued its own private key and sign its own tokens, so actions are attributable per agent, per host, and per user.<br>*[Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)* | The agent should never hold durable credentials; tokens are minted per tool call after policy evaluation, expire in minutes, and are never stored — and secrets should not exist as files in the agent's environment at all.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* |

*Why it matters: A resident signing key gives strong cryptographic attribution and works offline, but reintroduces exactly the exfiltratable long-lived secret that prompt injection and supply-chain compromise target; the ephemeral-mint model removes the theft surface but makes every action depend on a reachable authorization server.*

### Should low-risk capabilities like reads be granted to an agent by default, or must every action pass policy first?

| Position A | Position B |
|---|---|
| Read-type capabilities should be granted by default per host, because prompting for approval on every action makes the system unusable and users will reject it.<br>*[Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)* | Least privilege by default with just-in-time elevation, and a policy decision at the moment each token is requested — no standing grant, not even for reads.<br>*[You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)* |

*Why it matters: Default read grants are where prompt-injection-driven data exfiltration lives; the tradeoff sets both the exfiltration blast radius and whether the product is tolerable to use at all.*

### Should an intermediary sit between the agent and the resource it is calling?

| Position A | Position B |
|---|---|
| A proxy is the wrong architecture because it has to handle the data and therefore does not scale; the intermediary should be a directory that matches intent to capabilities and then gets out of the way.<br>*[Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)* | Traffic should be mediated — messages route to a message box before the agent runtime to enable sender authentication, spam filtering, and buffering, and access control belongs at the interception point between the agent runtime and the MCP server.<br>*[The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)* |

*Why it matters: It decides whether agent authorization is a control-plane component you can adopt incrementally or a data-plane hop that becomes a latency, cost, and confidentiality chokepoint for every agent call.*

## Practical Guidance

**Do:**

- Give the agent its own client ID and delegated access bound to the user, rather than replaying the user's credentials or personal token.
- Request an access token per tool call, audience-bound so only the one target MCP server can use it, expiring within a few minutes, and never persisted.
- Evaluate policy before minting the credential, so a denied action leaves nothing to leak, replay, or steal.
- Treat a human's approval as an input to policy, not the decision: check the approver's role and allow policy to override an approval they lack authority to give.
- Time-bound agent permissions to the agent's actual operating window and restrict the tool set to its specific job; make least privilege the default with just-in-time elevation for higher scopes.
- Scope the MCP server's exposed tool surface to the authorizing user, instead of surfacing every tool the application supports to every agent.
- Start scope design from the scopes your resource server already exposes, then layer tool-call-level scopes on top or pass them through.
- Log who acted, on behalf of whom, who authorized it, what was authorized, when, and for how long — treat missing attribution as a security gap.
- Publish signed metadata about an agent (capabilities, policy, protocol, who built it) rather than just a resolvable address.
- Design an explicit agent-first signup and login flow for your product, on the assumption agents will use it regardless.
- Batch high-frequency incidental writes triggered by agent traffic — Scalekit found 'last seen' updating 60x faster under agents and fixed it with one-second-granularity batching.

**Avoid:**

- Handing an agent a long-lived API key that can do everything; it is a kitchen sink and the agent will use all of it.
- Having the agent authenticate as the user — 'pretend to be me' instead of 'act for me within these limits' destroys attribution and any hope of scoping.
- Treating human-in-the-loop approval as your access control; consent-fatigued reviewers accept wrong output roughly 80% of the time.
- Assuming coarse scopes like 'read' or 'can send email on your behalf' are adequate expressions of an agent's authority.
- Letting an agent use any of the grants in its session token on every tool call.
- Storing secrets as files in the agent's environment, or running coding agents on a local laptop where NPM supply-chain compromise reaches them.
- Assuming an agent behaves like a service account you can bound by inspecting code — there is no determinism baked in.
- Permitting destructive operations at all: no agent should be able to drop a database, even when the documented recovery runbook calls for it.
- Relying on CAPTCHAs to distinguish agents from bad bots.

## Notable Outliers

- Some capabilities should be unconditionally denied regardless of policy or approval: no agent should be able to drop a database, even when the documented recovery procedure calls for exactly that. ([It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [13:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=807s))
- Agents are never fully detached principals — every agent always reports to a user, so agent identity is always a delegation chain rather than a standalone account. ([Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [19:27](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1167s))
- Liability for agent-produced work must ground out in a human or corporation, and Git's single-signer commit model is inadequate for attributing agent-authored code. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [50:15](https://www.youtube.com/watch?v=c35YoMdnI78&t=3015s))
- The web needs a certificate-authority-like trust issuer for agents, and no one has built it yet. ([Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [13:12](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=792s))
- DNS and document-era discovery cannot carry agent identity, because agents negotiate, delegate, and migrate between hosts in milliseconds; resolution must be adaptive to who is asking rather than a fixed name-to-address table. ([The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [1:41](https://www.youtube.com/watch?v=sum9DgexFRQ&t=101s))
- A v1 spec written in February already aged out because it assumed agents are ephemeral; long-lived and organizational agents now need their own policy support. ([Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [20:32](https://www.youtube.com/watch?v=JvKO40CFq-s&t=1232s))

## All Talks

- [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)
- [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)
- [Guide, Verify, Solve](../talks/guide-verify-solve.md)
- [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)
- [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)
- [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)
- [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)

## Speakers

- [Anirban Chatterjee](../speakers/anirban-chatterjee.md)
- [Kim Maida](../speakers/kim-maida.md)
- [Paola Estefania](../speakers/paola-estefania.md)
- [Paul Klein IV](../speakers/paul-klein-iv.md)
- [Ramesh Raskar](../speakers/ramesh-raskar.md)
- [Ravi Madabhushi](../speakers/ravi-madabhushi.md)

