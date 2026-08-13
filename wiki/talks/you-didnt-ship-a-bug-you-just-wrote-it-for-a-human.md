---
title: "You Didn't Ship a Bug. You Just Wrote It for a Human."
type: "talk"
slug: "you-didnt-ship-a-bug-you-just-wrote-it-for-a-human"
org: "Scalekit"
video_id: "lMCxVorb9wM"
duration_sec: 770
word_count: 2227
speakers: ["Ravi Madabhushi"]
---

# You Didn't Ship a Bug. You Just Wrote It for a Human.

**Speakers:** [Ravi Madabhushi](../speakers/ravi-madabhushi.md)

**Org:** Scalekit

**Duration:** 12m 50s

[Watch on YouTube](https://www.youtube.com/watch?v=lMCxVorb9wM)

## Summary

Ravi Madabhushi, co-founder of Scalekit, argues that the identity and authorization primitives we built for humans and deterministic programs fundamentally break once agents become the actors. He traces the problem from a small operational symptom — a 'last seen' timestamp being written 60x faster once agents started hitting their APIs — to the deeper architectural assumption that whoever authenticates is also who acts, and that permissions granted at registration time are safe because a human wrote deterministic code that could be code-reviewed. Agents violate both: the principal and the actor diverge, and the program's behavior is probabilistic rather than inspectable. He observes that most agents his customers build carry far more scopes than their job requires, and that most MCP servers surface every available tool regardless of which user authorized the agent. His prescription: bind the actor to the principal at all times, give agents their own identity with attribute-, context-, and principal-level scoping, default to least privilege with just-in-time elevation, and maintain full audit visibility over who authorized what, for how long. Worth watching if you are designing auth for agentic systems or MCP servers and want a concrete critique of why OAuth scopes are necessary but not sufficient.

## Key Points

- A rhythmic latency spike traced to a 'last seen' timestamp update revealed that agent traffic was writing 60 times faster than human traffic, which prompted a broader audit of human-era assumptions in their auth platform.
- Both existing identity slots — the human-acting-through-an-app/API-key model and the service account model — were designed on the premise that whoever authenticates is also who acts.
- Traditional permission models are safe largely because the acting program is deterministic and code-reviewable, which is why processes like Google's developer security review work at all.
- Agents break this on two axes: the principal is no longer the actor (delegated access is required), and there is no determinism guaranteeing the agent will do tomorrow what it did today.
- Agents in customer deployments routinely hold more permissions and scopes than their job requires, not from developer carelessness but because existing primitives cannot express fine-grained agent permissions.
- Most MCP servers do not limit tool surface based on which user authorized the agent, exposing all supported tools and letting the agent choose, which leads to wrong-tool selection.
- The fix requires the actor to be bound to the principal at all times plus agent-specific identity with attribute-level, context-level, and principal-level scoping — e.g. time-of-day limits, sender restrictions, recipient restrictions.
- Agents should be least-privileged by default and request just-in-time authorization for elevated scopes, backed by complete audit visibility into who acted, on behalf of whom, who authorized it, and for how long.
- This is presented as a present-tense problem, not a future one, citing real incidents of agents deleting production databases and a customer (ref.tools) whose product has no human actors at all.

## Notable Quotes

> "when agents started hitting our APIs in the last 12 months or so, we realized that this last seen update is happening 60 times faster than what it would, and that is creating unnecessary pressure in our DB write system"
>
> — [0:54](https://www.youtube.com/watch?v=lMCxVorb9wM&t=54s) &middot; *The concrete number and symptom that motivates the entire talk.*

> "most of the agents our customers are building have way too permissions and scopes than the agent's responsibility or the agent's job is"
>
> — [2:18](https://www.youtube.com/watch?v=lMCxVorb9wM&t=138s) &middot; *States the core empirical claim from a vendor with visibility across many deployments.*

> "We predominantly have two slots, and neither of the slots was built for agents in mind."
>
> — [3:16](https://www.youtube.com/watch?v=lMCxVorb9wM&t=196s) &middot; *Compact framing of the architectural gap.*

> "the fundamental philosophy that we've always maintained is whoever is authenticating is the one that is acting. Every action the program or the human takes is based on fixed set of permissions that actor was granted at some time."
>
> — [3:57](https://www.youtube.com/watch?v=lMCxVorb9wM&t=237s) &middot; *Names the exact assumption the rest of the talk dismantles.*

> "it is still intentional based on what the human wrote"
>
> — [4:44](https://www.youtube.com/watch?v=lMCxVorb9wM&t=284s) &middot; *The crux of why pre-agent permission models were tolerable.*

> "it's a deterministic program, and it always stays in its own lane. It can never do what it was not programmed to do. And you could inspect the code to say, Okay, is the program doing what it's supposed to do?"
>
> — [5:30](https://www.youtube.com/watch?v=lMCxVorb9wM&t=330s) &middot; *Articulates the inspectability guarantee that agents remove.*

> "These programs behave the exact same way a developer programmed them to work. But, agents fundamentally break this assumption."
>
> — [6:18](https://www.youtube.com/watch?v=lMCxVorb9wM&t=378s) &middot; *The pivot point of the argument.*

> "in the case of agents, the principal is not the same as an actor. You need to give delegated access, so that the agent can act on behalf of the user."
>
> — [6:18](https://www.youtube.com/watch?v=lMCxVorb9wM&t=378s) &middot; *States the first of the two structural breaks precisely.*

> "There is no determinism baked in to say what the agent will do or won't do."
>
> — [6:55](https://www.youtube.com/watch?v=lMCxVorb9wM&t=415s) &middot; *The second structural break, stated as a design constraint rather than a complaint.*

> "we go back to the agent acts as the user, which is even worse"
>
> — [7:31](https://www.youtube.com/watch?v=lMCxVorb9wM&t=451s) &middot; *Takes a clear side against the impersonation pattern many teams ship.*

> "most of the MCP servers that we've worked with don't actually limit the tool context access to the agent based on which user authorized the agent"
>
> — [8:22](https://www.youtube.com/watch?v=lMCxVorb9wM&t=502s) &middot; *A specific, checkable indictment of current MCP server practice.*

> "the agent is still seeing the same surface regardless whom it is acting for"
>
> — [8:22](https://www.youtube.com/watch?v=lMCxVorb9wM&t=502s) &middot; *Names the failure mode in one line.*

> "the actor, in this case, an agent, has to be bound to the principal at all times. And the agent should have its own identity."
>
> — [9:08](https://www.youtube.com/watch?v=lMCxVorb9wM&t=548s) &middot; *The central prescription.*

> "There's no extremely fine-grained scoping to say can this agent act at this hour? Can this agent read emails only from these senders? Can this agent send emails to only this recipients?"
>
> — [9:08](https://www.youtube.com/watch?v=lMCxVorb9wM&t=548s) &middot; *Makes the abstract demand for fine-grained scopes concrete with real examples.*

> "gone are the days when the broad scoped auth scopes that we defined is okay because in that case developer was writing a deterministic application and you can review the code"
>
> — [9:47](https://www.youtube.com/watch?v=lMCxVorb9wM&t=587s) &middot; *Ties the prescription back to the determinism argument.*

> "It should be at an attribute level scoping, it should be context level scoping, it should be principal level scoping."
>
> — [10:28](https://www.youtube.com/watch?v=lMCxVorb9wM&t=628s) &middot; *The three axes of the proposed permission model.*

> "agents should be least privileged by default and they should be able to ask for just-in-time authorization if they want elevated scopes"
>
> — [10:28](https://www.youtube.com/watch?v=lMCxVorb9wM&t=628s) &middot; *A named, adoptable pattern.*

> "We have seen enough incidents where agents end up doing rogue things. They end up deleting production databases and stuff like that."
>
> — [11:07](https://www.youtube.com/watch?v=lMCxVorb9wM&t=667s) &middot; *Grounds the risk claim in reported incidents rather than hypotheticals.*

> "you have to have absolute visibility into what your agent can do, every action that's taken in your system, who took it, on behalf of whom, and who authorized it, when was the authorization given, what authorization was given, how long is it given for"
>
> — [11:43](https://www.youtube.com/watch?v=lMCxVorb9wM&t=703s) &middot; *A complete audit requirements checklist in one sentence.*

> "if you can't deterministically control what your agent can or cannot do, then you're just praying that agent doesn't end up doing what it's not supposed to do. And praying is not a strategy, as we all know."
>
> — [11:43](https://www.youtube.com/watch?v=lMCxVorb9wM&t=703s) &middot; *The talk's rhetorical payoff.*

> "OAuth is a good place to start, but you need something beyond OAuth to make sure that the agents have extremely fine-grained access controls"
>
> — [12:31](https://www.youtube.com/watch?v=lMCxVorb9wM&t=751s) &middot; *The closing position: OAuth necessary but insufficient.*

## Positions

- Agent traffic caused a 'last seen' timestamp to be updated 60 times faster than human traffic, creating avoidable database write pressure that batching at one-second granularity resolved. ([0:54](https://www.youtube.com/watch?v=lMCxVorb9wM&t=54s), confidence: stated)
- Most agents that Scalekit's customers build hold more permissions and scopes than their responsibility requires. ([2:18](https://www.youtube.com/watch?v=lMCxVorb9wM&t=138s), confidence: stated)
- Over-permissioned agents are caused by inadequate authorization primitives, not by careless developers. ([2:18](https://www.youtube.com/watch?v=lMCxVorb9wM&t=138s), confidence: stated)
- Existing identity models rest on the assumption that the entity authenticating is the same entity acting, and that permissions fixed at registration time remain adequate. ([3:57](https://www.youtube.com/watch?v=lMCxVorb9wM&t=237s), confidence: stated)
- Traditional service account and OAuth models were acceptable only because the acting program was deterministic and its code could be inspected. ([5:30](https://www.youtube.com/watch?v=lMCxVorb9wM&t=330s), confidence: stated)
- Many systems agents need to reach still do not support OAuth, so there is no on-behalf-of principal and no way to distinguish an agent acting for a user from the user acting directly. ([6:18](https://www.youtube.com/watch?v=lMCxVorb9wM&t=378s), confidence: stated)
- Having an agent act as the user is worse than giving the agent its own client ID and delegated access. ([7:31](https://www.youtube.com/watch?v=lMCxVorb9wM&t=451s), confidence: stated)
- Most MCP servers surface all tools the user or application supports rather than scoping the tool surface to the authorizing user, causing agents to pick wrong tools. ([8:22](https://www.youtube.com/watch?v=lMCxVorb9wM&t=502s), confidence: stated)
- Current OAuth scopes on major providers like Gmail are too coarse — they express 'can send email on your behalf' but not time-of-day, sender, or recipient restrictions. ([9:08](https://www.youtube.com/watch?v=lMCxVorb9wM&t=548s), confidence: stated)
- Agent permissions should be time-bounded to the agent's operating window and restricted to the tools required for its specific job. ([9:47](https://www.youtube.com/watch?v=lMCxVorb9wM&t=587s), confidence: stated)
- Agent authorization requires attribute-level, context-level, and principal-level scoping, with least privilege by default and just-in-time elevation. ([10:28](https://www.youtube.com/watch?v=lMCxVorb9wM&t=628s), confidence: stated)
- Agents have already caused real production incidents, including deleting production databases, making this a present-day rather than future problem. ([11:07](https://www.youtube.com/watch?v=lMCxVorb9wM&t=667s), confidence: stated)
- Without complete audit visibility and deterministic controls over agent capability, a system has no security posture beyond hope. ([11:43](https://www.youtube.com/watch?v=lMCxVorb9wM&t=703s), confidence: stated)
- OAuth is a valid starting point but insufficient for agent authorization; something beyond it is required. ([12:31](https://www.youtube.com/watch?v=lMCxVorb9wM&t=751s), confidence: stated)
- Applications, APIs, and MCP servers must be architected for agents from the ground up because human-focused architecture does not scale to agents. ([0:00](https://www.youtube.com/watch?v=lMCxVorb9wM&t=0s), confidence: stated)

## Concepts

- [agent identity and authorization](../concepts/agent-identity-and-authorization.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [audit trails](../concepts/audit-trails.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [mcp server design](../concepts/mcp-server-design.md)

