---
title: "The Future Is Domain-Specific Agents"
type: "talk"
slug: "the-future-is-domain-specific-agents"
track: "AI Architects: Tokenmaxxing"
org: "StandardAgents"
day: "Day 3 — Session Day 2"
room: "Leadership 2"
video_id: "spNAUEgq_A8"
duration_sec: 1838
word_count: 5176
speakers: ["Vlad Luzin"]
---

# The Future Is Domain-Specific Agents

*Program title: Is Orchestration the Future?*

**Speakers:** [Vlad Luzin](../speakers/vlad-luzin.md)

**Org:** StandardAgents

**Track:** AI Architects: Tokenmaxxing &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Leadership 2 &nbsp;|&nbsp; **Duration:** 30m 38s

[Watch on YouTube](https://www.youtube.com/watch?v=spNAUEgq_A8)

## Summary

Justin Schroeder of StandardAgents argues that the dominant pattern for extending agents — piling MCP servers, skills, and tools into one large general-purpose agent's context — is inheritance, and that it breaks down as the context layer inflates. His alternative is composition: many small domain-specific agents, each a full agent with its own system prompt, narrow tool set, isolated message history, and agentic loop, coordinated by a higher-level agent that talks to them in plain English. He claims this yields over 80% token efficiency on typical tasks, makes small/cheap models viable (citing a 137x cost gap between DeepSeek V4 Flash and Fable 5), tightens the permission surface because a narrow agent structurally cannot do everything, and parallelizes cleanly. He also pushes back on the assumption that intelligence keeps getting cheaper, claiming token costs are up 76% in 2026 (29% IQ-adjusted) at the halfway mark. Worth watching for the composition-over-inheritance framing and the concrete spec of what an 'ideal' domain-specific agent should include (hooks, agent rules, sandboxed filesystem and code execution); skip if you want implementation detail, since no product or code is shown.

## Key Points

- Schroeder defines an agent as deterministic software that harnesses non-deterministic model output toward an objective, and argues the agent-vs-harness distinction is pedantic enough to ignore.
- Nearly every organization he encounters — from local real estate agencies to Fortune 500s — is trying to build custom agents, and the underlying motive is integrating their own data with AI rather than any dissatisfaction with existing chatbots.
- MCP has in practice become only a tool-distribution mechanism: on MCP's own client support matrix, tools is the one column filled out all the way down, and tools alone are insufficient for large projects.
- Stacking skills, MCP servers, and tools onto one agent is inheritance applied to context, and like software inheritance it delivers diminishing returns past some number of additions — he notes research showing many skills makes agents substantially worse.
- The composition alternative is a coordinator agent delegating to isolated domain agents that each carry only their own system prompt, tools, and message history, communicating in English rather than structured protocol.
- Claimed benefits are over 80% token efficiency per task, viability of much cheaper or non-language models for narrow subtasks, structurally enforced capability limits instead of blanket permission bypassing, and easy horizontal parallelization without geographic co-location.
- He predicts domain-specific agents become a mainstream topic through the back half of 2026 and that 2027 is the year of multi-agent orchestration, citing Vercel's Eve release as an early signal.
- Contrary to consensus, he claims the cost of intelligence reversed direction in 2026 — tokens up 76% raw and 29% IQ-adjusted at the halfway point — which raises the stakes on efficiency for customer-facing AI.
- An ideal agent primitive, in his spec, includes functions, prompts-as-tools, agents-as-tools, hooks for injecting messages or side effects, agent rules like turn limits, plus a sandboxed filesystem and code execution environment baked in.

## Notable Quotes

> "agents are deterministic software that harness the non-deterministic results produced by models in pursuit of some desired objective"
>
> — [2:09](https://www.youtube.com/watch?v=spNAUEgq_A8&t=129s) &middot; *His working definition, offered against his own point that the field still lacks one.*

> "A harness is an agent and an agent is a harness, okay? And for the for the purposes of this talk, we're going to go ahead and just move forward with that."
>
> — [2:55](https://www.youtube.com/watch?v=spNAUEgq_A8&t=175s) &middot; *Takes an explicit side on a definitional debate others treat as meaningful.*

> "it comes down to integration. Businesses want their data properly integrated into AI. They They believe, and are probably right, that if they appropriately leverage AI, they're going to have these dramatic gains in their business"
>
> — [4:19](https://www.youtube.com/watch?v=spNAUEgq_A8&t=259s) &middot; *Names the actual driver behind the custom-agent rush.*

> "there's no defined way to build an agent right now. Like, actually no defined way. The closest thing maybe is, uh, Eve that just came out from Vercel is maybe like the closest thing."
>
> — [6:15](https://www.youtube.com/watch?v=spNAUEgq_A8&t=375s) &middot; *Concrete claim about the state of the ecosystem, with a named exception.*

> "if I do get a good agent working, if I've managed to climb to the top of, you know, this mountain and I've got a good agent that's finally working well, well, it works well on my machine."
>
> — [6:50](https://www.youtube.com/watch?v=spNAUEgq_A8&t=410s) &middot; *Frames agent portability as the classic reproducibility problem.*

> "So, MCP has become a de facto tool distribution mechanism for agents. So, if I need to get my company's tools into that other agent, then MCP's a good way to do that. It has not proven to be great at providing other value yet."
>
> — [8:13](https://www.youtube.com/watch?v=spNAUEgq_A8&t=493s) &middot; *A pointed, checkable verdict on MCP's realized scope.*

> "I I I I like to joke that we didn't land a man on the moon by giving one guy a ton of tools."
>
> — [8:13](https://www.youtube.com/watch?v=spNAUEgq_A8&t=493s) &middot; *The talk's central analogy for why tool-stacking hits a ceiling.*

> "there's lots of research out there that shows that if you use very many of these, it actually makes your agent substantially worse"
>
> — [9:03](https://www.youtube.com/watch?v=spNAUEgq_A8&t=543s) &middot; *Empirical claim against the prevailing skill-stacking habit.*

> "there's an old saying, "Composition over inheritance." And it turns out this this is as old as time. Eventually, inheritance starts to break down."
>
> — [12:45](https://www.youtube.com/watch?v=spNAUEgq_A8&t=765s) &middot; *The organizing thesis, imported from software design into agent architecture.*

> "each of them is a separate isolated agent, a full agent. Not just a little server with tools on it. It's a full agent with its own message history, its own agentic loop."
>
> — [14:11](https://www.youtube.com/watch?v=spNAUEgq_A8&t=851s) &middot; *Draws the sharp line between his proposal and an MCP server.*

> "the communication mechanism for all of these small agents speaking to the larger agent above it is just English. They just talk to each other the way a human does."
>
> — [14:11](https://www.youtube.com/watch?v=spNAUEgq_A8&t=851s) &middot; *A design decision others would contest in favor of structured interfaces.*

> "First of all, they are far more token efficient. Far more token efficient. We regularly see over 80% token efficiency for any given task."
>
> — [16:49](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1009s) &middot; *The headline number backing the architecture.*

> "If you look at the difference in two models like DeepSeek uh V4 Flash and uh Fable 5, the cost difference is mind-boggling. It is 137 times cheaper than Fable per task."
>
> — [17:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1057s) &middot; *Quantifies the economic argument for routing narrow tasks to small models.*

> "In a world that would be powered by smaller domain-specific agents, those agents can't do everything. They can only do the things that are already explicitly approved for them to do."
>
> — [19:34](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1174s) &middot; *Reframes narrow scope as a security property, not a limitation.*

> "Unfortunately, they don't exist. That's the downside."
>
> — [20:24](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1224s) &middot; *Rare candor about the maturity of the thing he is advocating.*

> "2027, I would say, is basically the year of multi-agent orchestration. That's another word you'll start to hear a lot, I think. So, that's my big bold public prediction."
>
> — [21:55](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1315s) &middot; *The talk's dated, falsifiable prediction.*

> "most people believe right now is that the cost of intelligence is going down. That trend reversed in 2026, actually. We track this on on a website. Tokens are not getting cheaper anymore. They are actually going up even when adjusted for IQ."
>
> — [22:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1357s) &middot; *Directly contradicts a near-universal industry assumption.*

> "if you don't account for IQ, tokens are up 76% this year, almost 100% increase in tokens just this year. Um and we're we're not even halfway through it."
>
> — [23:23](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1403s) &middot; *The raw cost figure behind his efficiency urgency.*

> "You can't put Fable in front of a customer, um unless that customer has a massive lifetime value. It's just too expensive. So, you need to find a way to create great efficacy while being efficient."
>
> — [23:23](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1403s) &middot; *Names the unit-economics constraint driving customer-facing agent design.*

> "every agent should have its own little sandbox file system. And also, every agent should have a sandboxed code execution location."
>
> — [27:31](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1651s) &middot; *A prescriptive architectural requirement, stated as a primitive rather than an option.*

> "You kind of get the idea. You can end up with all kinds of highly efficient, small little agents that are all working together, but maintaining small minimal context windows all the way through."
>
> — [29:31](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1771s) &middot; *The closing statement of the thesis in one line.*

## Positions

- The distinction between an agent and a harness is pedantic and the two can be conflated in practice. ([2:55](https://www.youtube.com/watch?v=spNAUEgq_A8&t=175s), confidence: stated)
- The reason organizations build custom agents is data integration, not dissatisfaction with existing general-purpose AI products. ([4:19](https://www.youtube.com/watch?v=spNAUEgq_A8&t=259s), confidence: stated)
- There is currently no defined, standard way to build an agent; Vercel's Eve is the closest thing. ([6:15](https://www.youtube.com/watch?v=spNAUEgq_A8&t=375s), confidence: stated)
- MCP has succeeded only as a tool distribution mechanism and has not delivered value beyond tools, as shown by tools being the only fully supported column on MCP's own client support matrix. ([8:13](https://www.youtube.com/watch?v=spNAUEgq_A8&t=493s), confidence: stated)
- Installing many skills into one agent measurably degrades its performance. ([9:03](https://www.youtube.com/watch?v=spNAUEgq_A8&t=543s), confidence: stated)
- Loading skills, MCP servers, and tools into a single agent's context is functionally inheritance, and like inheritance it hits diminishing returns and eventually breaks down. ([12:45](https://www.youtube.com/watch?v=spNAUEgq_A8&t=765s), confidence: stated)
- Sub-agents should communicate with their coordinator in natural English rather than a structured protocol. ([14:11](https://www.youtube.com/watch?v=spNAUEgq_A8&t=851s), confidence: stated)
- Domain-specific agents deliver over 80% token efficiency for a given task compared to the general-purpose alternative. ([16:49](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1009s), confidence: stated)
- DeepSeek V4 Flash is 137 times cheaper per task than Fable 5, and narrow task scoping makes the cheaper model reliable enough to use. ([17:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1057s), confidence: stated)
- Narrow, capability-limited agents are a better answer to the permission-bypass problem than permission dialogs on a maximally capable coding agent. ([19:34](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1174s), confidence: stated)
- Domain-specific agents do not meaningfully exist in public today. ([20:24](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1224s), confidence: stated)
- Adoption of domain-specific agents will accelerate rapidly through the second half of 2026, and 2027 will be the year of multi-agent orchestration. ([21:55](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1315s), confidence: stated)
- The cost of intelligence stopped falling and reversed in 2026: tokens are up 76% raw and 29% IQ-adjusted at the halfway point of the year. ([22:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1357s), confidence: stated)
- Frontier models like Fable are too expensive to place in front of customers unless those customers have very high lifetime value. ([23:23](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1403s), confidence: stated)
- A sandboxed filesystem and sandboxed code execution should be built-in primitives of every domain-specific agent, not optional add-ons. ([27:31](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1651s), confidence: stated)
- Full agents, not just functions, should be usable as tools within another agent, allowing recursive sub-agent hierarchies. ([28:17](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1697s), confidence: stated)
- Because each domain-specific agent is a small isolated execution environment, thousands can be run in parallel across regions without heavy shared infrastructure. ([20:24](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1224s), confidence: stated)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [context window management](../concepts/context-window-management.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [model portability](../concepts/model-portability.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [small language models](../concepts/small-language-models.md)
- [token efficiency](../concepts/token-efficiency.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

