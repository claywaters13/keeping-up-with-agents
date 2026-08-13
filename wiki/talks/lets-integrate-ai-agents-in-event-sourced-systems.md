---
title: "Let's integrate AI Agents in Event-Sourced Systems"
type: "talk"
slug: "lets-integrate-ai-agents-in-event-sourced-systems"
track: "AI in Finance"
org: "FlyersSoft"
day: "Day 4 — Session Day 3"
room: "Track 3"
video_id: "o6U_2vd967Y"
duration_sec: 1296
word_count: 3535
speakers: ["Divakar Kumar"]
---

# Let's integrate AI Agents in Event-Sourced Systems

**Speakers:** [Divakar Kumar](../speakers/divakar-kumar.md)

**Org:** FlyersSoft

**Track:** AI in Finance &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 21m 36s

[Watch on YouTube](https://www.youtube.com/watch?v=o6U_2vd967Y)

## Summary

Divakar Kumar of FlyersSoft walks through how his team retrofitted AI agents into an existing event-sourced, domain-driven fraud detection system without ripping out the rule-based and ML engines already in place. The core argument is that traditional fraud engines fail specifically in the 'gray zone' — transactions that are neither clearly legitimate nor clearly fraudulent — not because the models are bad, but because they lack real-time context spread across isolated bounded contexts. The proposed fix is architectural rather than model-centric: use CDC/change feeds and a message broker to project events from transaction, account, device, and payment contexts into a shared semantic layer (materialized view), then expose that layer to agents as tools. Agents sit in a tier-two layer inside the saga orchestrator, fanned out to a risk analyzer and a behavior analyzer, with a third agent arbitrating the verdict. Worth watching if you have an existing DDD/event-sourced system and want a concrete integration pattern with real constraints (sub-500ms SLA, in-memory short-term memory, loop-termination metrics) rather than a greenfield agent demo.

## Key Points

- The real value of AI agents is in business workflows, not just chatbots and coding assistants, and they can be layered onto architectures a business has already invested years in.
- Rule-based fraud engines break down on maintainability because fraudsters keep finding new intrusion paths and the static rules must be updated continuously.
- Both rule-based and ML approaches handle the clear-cut cases well; the failure mode is the 'gray zone' where the system cannot decide between fraudulent and legitimate.
- The team kept the existing engine as tier one and added agentic AI only as tier two for gray-zone cases, deliberately not replacing what already worked.
- The root problem with agents in a DDD system is that bounded contexts (transaction, accounts, device, payment) do not share data, so the agent has no unified view to reason over.
- Events are appended to an event store (Cosmos DB) rather than mutating state, and a change feed / CDC mechanism propagates them into read models optimized for queries.
- The key enabling artifact is a semantic layer — a materialized view built from all bounded contexts via CDC or message broker plus a worker process — that agents access through tools.
- The tier-two layer uses a fan-out pattern to a risk analyzer agent and a behavior analyzer agent, with a third verdict agent reconciling their responses because a pure metric-based verdict reintroduced the false positives of the rule-based system.
- A sub-500ms transaction SLA rules out long-term memory, so the agents use in-memory short-term memory, and an explicit metric threshold breaks the agent loop to avoid infinite iteration.

## Notable Quotes

> "these AI agents are more not just for the chatbots or the coding assistance, right? So, the real value that you could bring out of these AI agents is like when you start to apply these into your business workflows."
>
> — [0:49](https://www.youtube.com/watch?v=o6U_2vd967Y&t=49s) &middot; *States the talk's framing thesis about where agent value actually lives.*

> "And I asked them like, why did you block my transaction? Do you know what the response was? They didn't know"
>
> — [2:05](https://www.youtube.com/watch?v=o6U_2vd967Y&t=125s) &middot; *The concrete anecdote that motivates the entire architecture — opacity of existing fraud decisions.*

> "It was somewhere in the system, either the rule-based engine or the ML-based engine would have taken that decision."
>
> — [2:05](https://www.youtube.com/watch?v=o6U_2vd967Y&t=125s) &middot; *Names the explainability gap in traditional fraud stacks.*

> "you might be thinking like what a great idiot, right? Because it is already an uncertain case like why do you want to introduce an AI agent because it is also a non-deterministic by nature"
>
> — [2:44](https://www.youtube.com/watch?v=o6U_2vd967Y&t=164s) &middot; *Speaker names the strongest objection to his own approach before answering it.*

> "earlier in the rule-based engine or the ML-based engine like we don't have enough context. We don't have enough real-time data that gets passed on to the system."
>
> — [2:44](https://www.youtube.com/watch?v=o6U_2vd967Y&t=164s) &middot; *The counterargument: the bottleneck is context availability, not model determinism.*

> "the problem with this rule-based engine is like the maintainability because the fraudsters are trying to get intruded into a system like by a lot of different ways and you just need to keep on updating these static rules day by day"
>
> — [3:26](https://www.youtube.com/watch?v=o6U_2vd967Y&t=206s) &middot; *Specific diagnosis of why rule engines decay in adversarial domains.*

> "few of the transaction like goes under the gray zone area and this is the area where it is really uncertain for those systems to really come to a conclusion whether it is an fraudulent transaction or a legitimate transaction."
>
> — [4:09](https://www.youtube.com/watch?v=o6U_2vd967Y&t=249s) &middot; *Defines the gray zone, the narrow target the agents are scoped to.*

> "our thought process is not to exclude the systems that we already had. We we are just trying to handle few of the areas like that is the gray zone areas with the help of agentic AI processing."
>
> — [5:05](https://www.youtube.com/watch?v=o6U_2vd967Y&t=305s) &middot; *The central tradeoff: augment rather than replace the incumbent stack.*

> "we are not mutating the state, but instead like we are appending all the events as when it arrives."
>
> — [8:45](https://www.youtube.com/watch?v=o6U_2vd967Y&t=525s) &middot; *Crisp one-line statement of the event sourcing premise the talk builds on.*

> "you won't be able to rely entirely upon the event store for the query operation for the read operation. What you would do is like internal like you will be having different read models which are optimized for the read operations."
>
> — [9:29](https://www.youtube.com/watch?v=o6U_2vd967Y&t=569s) &middot; *Explains the CQRS split that makes agent-time reads feasible.*

> "you can't you can't you can't say other teams to follow the same patterns because even sourcing is not the one that other teams are also following."
>
> — [10:07](https://www.youtube.com/watch?v=o6U_2vd967Y&t=607s) &middot; *Organizational constraint that forces the message-broker path alongside CDC.*

> "the idea is like we need to gather all the data from all these different contexts and to have or build a semantic layer or you could call it as a materialized view which you could further use within your agent"
>
> — [10:49](https://www.youtube.com/watch?v=o6U_2vd967Y&t=649s) &middot; *The load-bearing architectural idea of the whole talk.*

> "this language model it it is not necessary to be a large language model. It could be a SLM. It could be an open-source model."
>
> — [11:32](https://www.youtube.com/watch?v=o6U_2vd967Y&t=692s) &middot; *Takes a side on model sizing for latency-bound agent workloads.*

> "you can't really um rely on the long-term memory because you need to um adhere to the uh SLA that you uh provided to the customers because for for the transaction uh to be processed like it should be sub 500 milliseconds."
>
> — [11:32](https://www.youtube.com/watch?v=o6U_2vd967Y&t=692s) &middot; *Hard latency number that drives the memory design decision.*

> "you should really know like when to stop this loop"
>
> — [12:29](https://www.youtube.com/watch?v=o6U_2vd967Y&t=749s) &middot; *Short but names the agent-loop termination problem explicitly.*

> "For for our use case like we do have a metrics with beyond which like if we go like we we could break out of this loop. And this could be varying for different use cases. So, you should be really careful on avoiding this infinite loop."
>
> — [13:14](https://www.youtube.com/watch?v=o6U_2vd967Y&t=794s) &middot; *Concrete guardrail for runaway agent loops in a latency-critical path.*

> "if we are using just the metrics, it is again going back to the same criteria like where we had this rule-based um mechanism. Uh so, there are many false positive cases that we are that we faced."
>
> — [14:30](https://www.youtube.com/watch?v=o6U_2vd967Y&t=870s) &middot; *Reports an empirical failure that justified adding a third arbitration agent.*

> "we we in turn like we are trying to use a third agent in this verdict layer, which analyzes both the agents' responses and come to a conclusion"
>
> — [14:30](https://www.youtube.com/watch?v=o6U_2vd967Y&t=870s) &middot; *Describes the multi-agent consensus pattern at the decision boundary.*

> "we also have a device trust layer, like all the device information will get stored into this semantic layer and it will just get those chunks alone."
>
> — [16:06](https://www.youtube.com/watch?v=o6U_2vd967Y&t=966s) &middot; *Shows how per-domain signals become retrievable agent tools.*

> "we also had um a business rules trying to migrate some of the rules that we had in the rule base engine over this tools"
>
> — [16:06](https://www.youtube.com/watch?v=o6U_2vd967Y&t=966s) &middot; *Migration path from legacy rules into agent tooling rather than discarding them.*

## Positions

- Agents should be added as a tier-two layer for ambiguous cases rather than replacing existing rule-based and ML fraud engines. ([5:05](https://www.youtube.com/watch?v=o6U_2vd967Y&t=305s), confidence: stated)
- The limitation of traditional rule-based and ML fraud engines is insufficient real-time context, not the algorithms themselves. ([2:44](https://www.youtube.com/watch?v=o6U_2vd967Y&t=164s), confidence: stated)
- Rule-based fraud engines are unmaintainable at scale because static rules must be continuously updated against evolving fraud tactics. ([3:26](https://www.youtube.com/watch?v=o6U_2vd967Y&t=206s), confidence: stated)
- Agents cannot reason usefully over a DDD system without first building a cross-context semantic layer / materialized view. ([10:49](https://www.youtube.com/watch?v=o6U_2vd967Y&t=649s), confidence: stated)
- The agent's model need not be a large language model; an SLM or open-source model suffices for this use case. ([11:32](https://www.youtube.com/watch?v=o6U_2vd967Y&t=692s), confidence: stated)
- Long-term memory is incompatible with a sub-500ms transaction processing SLA, so short-term in-memory context should be used. ([11:32](https://www.youtube.com/watch?v=o6U_2vd967Y&t=692s), confidence: stated)
- Using a plain metric or if-condition for the final verdict reproduces the false-positive problems of rule-based systems, so a third arbitration agent is preferable. ([14:30](https://www.youtube.com/watch?v=o6U_2vd967Y&t=870s), confidence: stated)
- Agent loops need an explicit numeric break condition or they risk running indefinitely. ([13:14](https://www.youtube.com/watch?v=o6U_2vd967Y&t=794s), confidence: stated)
- You cannot expect other teams in an organization to adopt event sourcing, so integration must fall back to asynchronous message-broker communication. ([10:07](https://www.youtube.com/watch?v=o6U_2vd967Y&t=607s), confidence: stated)
- Event stores should not be queried directly for read operations; separate optimized read models are required. ([9:29](https://www.youtube.com/watch?v=o6U_2vd967Y&t=569s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [durable execution](../concepts/durable-execution.md)
- [parallel agent execution](../concepts/parallel-agent-execution.md)
- [semantic layer](../concepts/semantic-layer.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

