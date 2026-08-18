---
title: "Ravi Madabhushi"
type: "speaker"
slug: "ravi-madabhushi"
talk_count: 1
---

# Ravi Madabhushi

## Talks

- [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)

## Concepts

- [agent identity and authorization](../concepts/agent-identity-and-authorization.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [audit trails](../concepts/audit-trails.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [mcp server design](../concepts/mcp-server-design.md)

## Quotes

> "when agents started hitting our APIs in the last 12 months or so, we realized that this last seen update is happening 60 times faster than what it would, and that is creating unnecessary pressure in our DB write system"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [0:54](https://www.youtube.com/watch?v=lMCxVorb9wM&t=54s)

> "most of the agents our customers are building have way too permissions and scopes than the agent's responsibility or the agent's job is"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [2:18](https://www.youtube.com/watch?v=lMCxVorb9wM&t=138s)

> "We predominantly have two slots, and neither of the slots was built for agents in mind."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [3:16](https://www.youtube.com/watch?v=lMCxVorb9wM&t=196s)

> "the fundamental philosophy that we've always maintained is whoever is authenticating is the one that is acting. Every action the program or the human takes is based on fixed set of permissions that actor was granted at some time."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [3:57](https://www.youtube.com/watch?v=lMCxVorb9wM&t=237s)

> "it is still intentional based on what the human wrote"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [4:44](https://www.youtube.com/watch?v=lMCxVorb9wM&t=284s)

> "it's a deterministic program, and it always stays in its own lane. It can never do what it was not programmed to do. And you could inspect the code to say, Okay, is the program doing what it's supposed to do?"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [5:30](https://www.youtube.com/watch?v=lMCxVorb9wM&t=330s)

> "These programs behave the exact same way a developer programmed them to work. But, agents fundamentally break this assumption."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [6:18](https://www.youtube.com/watch?v=lMCxVorb9wM&t=378s)

> "in the case of agents, the principal is not the same as an actor. You need to give delegated access, so that the agent can act on behalf of the user."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [6:18](https://www.youtube.com/watch?v=lMCxVorb9wM&t=378s)

> "There is no determinism baked in to say what the agent will do or won't do."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [6:55](https://www.youtube.com/watch?v=lMCxVorb9wM&t=415s)

> "we go back to the agent acts as the user, which is even worse"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [7:31](https://www.youtube.com/watch?v=lMCxVorb9wM&t=451s)

> "most of the MCP servers that we've worked with don't actually limit the tool context access to the agent based on which user authorized the agent"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [8:22](https://www.youtube.com/watch?v=lMCxVorb9wM&t=502s)

> "the agent is still seeing the same surface regardless whom it is acting for"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [8:22](https://www.youtube.com/watch?v=lMCxVorb9wM&t=502s)

> "the actor, in this case, an agent, has to be bound to the principal at all times. And the agent should have its own identity."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [9:08](https://www.youtube.com/watch?v=lMCxVorb9wM&t=548s)

> "There's no extremely fine-grained scoping to say can this agent act at this hour? Can this agent read emails only from these senders? Can this agent send emails to only this recipients?"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [9:08](https://www.youtube.com/watch?v=lMCxVorb9wM&t=548s)

> "gone are the days when the broad scoped auth scopes that we defined is okay because in that case developer was writing a deterministic application and you can review the code"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [9:47](https://www.youtube.com/watch?v=lMCxVorb9wM&t=587s)

> "It should be at an attribute level scoping, it should be context level scoping, it should be principal level scoping."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [10:28](https://www.youtube.com/watch?v=lMCxVorb9wM&t=628s)

> "agents should be least privileged by default and they should be able to ask for just-in-time authorization if they want elevated scopes"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [10:28](https://www.youtube.com/watch?v=lMCxVorb9wM&t=628s)

> "We have seen enough incidents where agents end up doing rogue things. They end up deleting production databases and stuff like that."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [11:07](https://www.youtube.com/watch?v=lMCxVorb9wM&t=667s)

> "you have to have absolute visibility into what your agent can do, every action that's taken in your system, who took it, on behalf of whom, and who authorized it, when was the authorization given, what authorization was given, how long is it given for"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [11:43](https://www.youtube.com/watch?v=lMCxVorb9wM&t=703s)

> "if you can't deterministically control what your agent can or cannot do, then you're just praying that agent doesn't end up doing what it's not supposed to do. And praying is not a strategy, as we all know."
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [11:43](https://www.youtube.com/watch?v=lMCxVorb9wM&t=703s)

> "OAuth is a good place to start, but you need something beyond OAuth to make sure that the agents have extremely fine-grained access controls"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [12:31](https://www.youtube.com/watch?v=lMCxVorb9wM&t=751s)

