---
title: "The Agentic Web and the Bazaar Era of AI"
type: "talk"
slug: "the-agentic-web-and-the-bazaar-era-of-ai"
org: "MIT Media Lab"
video_id: "sum9DgexFRQ"
duration_sec: 730
word_count: 1916
speakers: ["Ramesh Raskar"]
---

# The Agentic Web and the Bazaar Era of AI

**Speakers:** [Ramesh Raskar](../speakers/ramesh-raskar.md)

**Org:** MIT Media Lab

**Duration:** 12m 10s

[Watch on YouTube](https://www.youtube.com/watch?v=sum9DgexFRQ)

## Summary

Ramesh Raskar (MIT Media Lab) and Maria, a core contributor, pitch Project Nanda — an open research effort building infrastructure for an 'internet of AI agents.' The core argument is historical analogy: today's agent ecosystem is the AOL era, with agents locked inside walled gardens and proprietary agent stores, and it needs the same transition to a permissionless open web that documents got. The talk walks through the concrete pieces already shipped: the Nanda index (a DNS-like but richer discovery layer returning signed 'agent facts' and agent cards, with adaptive resolution and message boxes), hosting options for keeping agents online, and Nanda Town, an open-source discrete-event simulator that models the agentic web as 12 layers so protocols can be stress-tested before they're load-bearing. It's a short, concrete infrastructure overview aimed at someone who wants to publish their own agent on an open index today rather than a research talk about agent capabilities.

## Key Points

- The current agent ecosystem resembles the closed AOL era — developers are forced to build inside walled gardens, proprietary agent stores, and orchestrations that only talk to themselves — and needs an equivalent transition to an open, permissionless web.
- Agents today lack three things across vendor boundaries: a shared way to find each other, a portable identity or trust layer not owned by one platform, and an open way to transact and coordinate.
- The Nanda index is a discovery layer analogous to DNS, but agents need more than an address — they need to know what another agent does, what tools it can use, what rules it follows, and how to talk to it.
- Discovery is made trustworthy by the agent facts record, a signed record stating who the agent is, what it can do, what it is allowed to touch, and who built it, which a caller can check before connecting.
- Resolution is adaptive rather than a fixed name-to-address lookup: one agent can have many endpoints, traffic can be routed to the best one, and results vary by who is asking and what they're allowed to access.
- Messages route through a message box that authenticates senders, filters spam and bad requests, and buffers until the agent is ready, rather than hitting the agent's runtime directly.
- Onboarding is tiered by who you are: enterprises run their own catalog and register a gateway from their domain, existing sites use DNS records, and individuals use a hosted form at host39.org.
- Nanda Town is an open-source discrete-event simulator that decomposes the agentic web into 12 layers (transport, identity, registry, auth, trust, payments, coordination, negotiation, memory, privacy, and more) so you can swap in your own implementation of one layer and test it against the rest.
- The hard problems are not getting one agent online but coordination at scale — thousands of agents discovering each other, proving identity, and deciding whom to trust with no central authority — which is why protocols must be simulated before they carry real traffic.

## Notable Quotes

> "The internet is about to host not millions or billions, but eventually trillions of autonomous agents."
>
> — [0:49](https://www.youtube.com/watch?v=sum9DgexFRQ&t=49s) &middot; *The scale premise the entire infrastructure argument rests on.*

> "They negotiate, they delegate, they migrate between hosts in milliseconds. That's a fundamental different load than the human web, and it strains the identity and discovery system we built for documents, DNS among them."
>
> — [1:41](https://www.youtube.com/watch?v=sum9DgexFRQ&t=101s) &middot; *States the specific technical claim that existing web infrastructure is insufficient.*

> "If you're building agents today, you're mostly building them or you're forced to build them inside walled gardens, closed platforms, proprietary agent stores, and orchestrations that only talk to itself."
>
> — [1:41](https://www.youtube.com/watch?v=sum9DgexFRQ&t=101s) &middot; *The central diagnosis of the present state that others might contest.*

> "This is like the AOL era from the late '90s where it was a closed network."
>
> — [1:41](https://www.youtube.com/watch?v=sum9DgexFRQ&t=101s) &middot; *The framing analogy that gives the talk its 'bazaar era' thesis.*

> "the next era needs what the web needed, an open infrastructure where an agent from one company or one entity can discover agent from another. That agent can hand off work to it, pay it, learn from it across organizational boundaries, no permissions required."
>
> — [2:32](https://www.youtube.com/watch?v=sum9DgexFRQ&t=152s) &middot; *The clearest statement of what the speaker wants built and the permissionless requirement.*

> "an agent is a model that uses tools in a loop. Right, you give it a goal, it decides what to do next, it calls a tool, it looks at the result, then it keeps going until the task is done."
>
> — [3:18](https://www.youtube.com/watch?v=sum9DgexFRQ&t=198s) &middot; *A crisp working definition worth citing across talks.*

> "Everything else, like memory orchestration and multi-agent systems, is built on top of it."
>
> — [3:55](https://www.youtube.com/watch?v=sum9DgexFRQ&t=235s) &middot; *Takes a position that the tool-use loop is primitive and everything else derivative.*

> "if it has access to real tools, we should care about who controls it, where it runs, and how much we can see. And that is why open-source self-hosted agents are super important."
>
> — [3:55](https://www.youtube.com/watch?v=sum9DgexFRQ&t=235s) &middot; *The security/control argument for self-hosting, stated as a normative claim.*

> "But agents need more than an address. They need to know what another agent does, what tools it can use, what rules it follows, and how to talk to it."
>
> — [5:23](https://www.youtube.com/watch?v=sum9DgexFRQ&t=323s) &middot; *Names precisely why DNS is insufficient for agent discovery.*

> "Messages do not go straight to the agent's runtime. They go to the message box first."
>
> — [5:23](https://www.youtube.com/watch?v=sum9DgexFRQ&t=323s) &middot; *A concrete architectural decision with real tradeoffs for latency and control.*

> "It is a signed record that tells other agents who this agent is, what it can do, what it is allowed to touch, who built it, and where to reach it."
>
> — [6:15](https://www.youtube.com/watch?v=sum9DgexFRQ&t=375s) &middot; *Defines the trust primitive of the whole system.*

> "the index is not just a lookup table. It does not point to one name to one fixed address. It can return updated agent facts based on the request."
>
> — [6:15](https://www.youtube.com/watch?v=sum9DgexFRQ&t=375s) &middot; *The key design departure from DNS.*

> "the resolution is adaptive. It changes based on where the agent is, who's asking, and what they are allowed to access."
>
> — [6:54](https://www.youtube.com/watch?v=sum9DgexFRQ&t=414s) &middot; *Compact statement of the adaptive-resolution property.*

> "Hosting one agent can be affordable, but the cost problem starts when you want to run many agents at once, for a team, a product, or a simulation. That is where per agent cost really matters."
>
> — [8:26](https://www.youtube.com/watch?v=sum9DgexFRQ&t=506s) &middot; *Names the economic constraint on multi-agent deployment.*

> "It gives you a simple cloud default for running Open Clo or other agents with sleep and wake architecture, so idle agents do not keep burning compute."
>
> — [8:26](https://www.youtube.com/watch?v=sum9DgexFRQ&t=506s) &middot; *The specific technical answer to the per-agent cost problem.*

> "getting one agent online was always the easy part."
>
> — [8:26](https://www.youtube.com/watch?v=sum9DgexFRQ&t=506s) &middot; *Reframes where the real difficulty of the agentic web lies.*

> "The hard problems of the agent web live between agents at scale. So, how thousands of them discover each other, prove who they are, decide whom to trust, and coordinate with no central authority."
>
> — [9:06](https://www.youtube.com/watch?v=sum9DgexFRQ&t=546s) &middot; *The strongest framing of the open research problem.*

> "you can't just assume that protocols will hold up under the load, and you have to test and run them and watch when they break."
>
> — [9:06](https://www.youtube.com/watch?v=sum9DgexFRQ&t=546s) &middot; *The methodological argument justifying simulation as infrastructure work.*

> "how do you prove an open agent web actually works before it's load bearing on the real internet. You simulate it."
>
> — [9:06](https://www.youtube.com/watch?v=sum9DgexFRQ&t=546s) &middot; *States the thesis behind Nanda Town in one line.*

> "You can take one layer, add your own version, run it inside Nanda Town, and see how it works with the rest of the network."
>
> — [10:41](https://www.youtube.com/watch?v=sum9DgexFRQ&t=641s) &middot; *The concrete invitation to contributors and the modularity claim.*

## Positions

- The internet will eventually host trillions of autonomous agents, not millions or billions. ([0:49](https://www.youtube.com/watch?v=sum9DgexFRQ&t=49s), confidence: stated)
- Existing document-era infrastructure, DNS in particular, cannot handle the identity and discovery load of agents that migrate between hosts in milliseconds. ([1:41](https://www.youtube.com/watch?v=sum9DgexFRQ&t=101s), confidence: stated)
- Today's agent ecosystem is structurally equivalent to the closed AOL network of the late 1990s and will undergo the same transition to an open web. ([2:32](https://www.youtube.com/watch?v=sum9DgexFRQ&t=152s), confidence: stated)
- An agent is fundamentally a model that uses tools in a loop; memory, orchestration, and multi-agent systems are all built on top of that primitive. ([3:55](https://www.youtube.com/watch?v=sum9DgexFRQ&t=235s), confidence: stated)
- Because agents need access to real tools and apps, open-source self-hosted agents are important for retaining control over who runs them and what they can see. ([3:55](https://www.youtube.com/watch?v=sum9DgexFRQ&t=235s), confidence: stated)
- Agent discovery requires more than name-to-address mapping; it requires capability, policy, and protocol metadata carried in a signed agent facts record. ([5:23](https://www.youtube.com/watch?v=sum9DgexFRQ&t=323s), confidence: stated)
- Routing messages through an intermediary message box rather than directly to the agent runtime is the right default, because it enables sender authentication, spam filtering, and buffering. ([5:23](https://www.youtube.com/watch?v=sum9DgexFRQ&t=323s), confidence: implied)
- Index resolution should be adaptive and request-dependent rather than a fixed lookup table, so one agent can expose many endpoints without revealing private details. ([6:54](https://www.youtube.com/watch?v=sum9DgexFRQ&t=414s), confidence: stated)
- For most use cases, hosting an agent in the cloud makes more sense than running it locally, because local hosting makes you responsible for uptime. ([7:36](https://www.youtube.com/watch?v=sum9DgexFRQ&t=456s), confidence: stated)
- Per-agent cost is the binding constraint on running many agents, and sleep-and-wake architecture that stops idle agents from burning compute is the fix. ([8:26](https://www.youtube.com/watch?v=sum9DgexFRQ&t=506s), confidence: stated)
- Getting a single agent online is the easy part; the unsolved problems are discovery, identity, trust, and coordination among thousands of agents with no central authority. ([9:06](https://www.youtube.com/watch?v=sum9DgexFRQ&t=546s), confidence: stated)
- Agent protocols must be tested in simulation before they become load-bearing on the real internet, because you cannot assume they will hold up under load. ([9:06](https://www.youtube.com/watch?v=sum9DgexFRQ&t=546s), confidence: stated)
- The agentic web decomposes into 12 layers — transport, communication, identity, registry, auth, trust, payments, coordination, negotiation, memory, privacy, and data effects — each of which a real agentic platform needs. ([10:41](https://www.youtube.com/watch?v=sum9DgexFRQ&t=641s), confidence: stated)

## Concepts

- [agent identity and authorization](../concepts/agent-identity-and-authorization.md)
- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [entity resolution](../concepts/entity-resolution.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [local inference](../concepts/local-inference.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [simulation environments](../concepts/simulation-environments.md)
- [skill marketplaces](../concepts/skill-marketplaces.md)

