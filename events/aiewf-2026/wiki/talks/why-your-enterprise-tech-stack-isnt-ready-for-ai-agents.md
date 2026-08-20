---
title: "Why Your Enterprise Tech Stack Isn’t Ready for AI Agents"
type: "talk"
slug: "why-your-enterprise-tech-stack-isnt-ready-for-ai-agents"
track: "AI in Healthcare"
org: "Anterior"
day: "Day 4 — Session Day 3"
room: "Track 7"
video_id: "mav15aW9lLM"
duration_sec: 1155
word_count: 3399
speakers: ["Christopher Lovejoy", "Saul Howard"]
---

# Why Your Enterprise Tech Stack Isn’t Ready for AI Agents

*Program title: Why Your Enterprise Tech Stack Isn't Ready for AI Agents - And What to Build Instead*

**Speakers:** [Christopher Lovejoy](../speakers/christopher-lovejoy.md), [Saul Howard](../speakers/saul-howard.md)

**Org:** Anterior

**Track:** AI in Healthcare &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 19m 15s

[Watch on YouTube](https://www.youtube.com/watch?v=mav15aW9lLM)

## Summary

Two Anterior engineers — a forward-deployed engineer and a VP of engineering selling agentic AI to US health insurers — argue that the reason enterprise AI pilots stall isn't model quality but architecture. They walk through a familiar failure mode: a four-week POC hits its accuracy metrics, everyone is thrilled, and then the compliance, security, and clinical stakeholders ask for audit trails, PHI handling guarantees, human escalation paths, and ongoing evals — none of which the POC's architecture can support. Their answer is four primitives adopted from finance, defense, and big tech: an immutable event log as the single source of truth, schema-driven object storage held separate from orchestration, human-agent equivalency so any LLM action can be performed by a human, and evals that fall out of those three rather than being bolted on. The framing throughout is that architecture means taking constraints seriously and choosing what you want to be trivially easy, accepting the resulting trade-offs. Worth watching if you're moving agents into a regulated environment and suspect your promising prototype won't survive contact with the security review.

## Key Points

- The hard part of enterprise AI is not the AI: POCs routinely hit their accuracy metrics and then fail productionization on audit, data-handling, escalation, and eval requirements that the prototype architecture cannot retrofit.
- An enterprise audit trail is not a developer log — under SOC 2, HITRUST, and HIPAA it must be a complete record of every agent action, every data access, and every authorization, defensible as a chain of evidence in a legal setting.
- Adopting an event-sourcing pattern — an append-only, complete, unified transaction log — makes auditability trivial because it falls out of the storage paradigm; the trade-off is cheap writes and expensive reads, mitigated by caching and snapshots.
- In healthcare that read cost is actually a feature: later events can change the interpretation of a patient journey, and views being ephemeral computed projections of the log means you can re-derive a different view of the same history.
- Sensitive data belongs in schema-driven, immutable object storage that the event log only references, so developers can debug and retrace agent steps and see the shape of data without ever seeing the PHI.
- Separating orchestration from object storage creates a place to enforce zero trust — agents bear tokens and fetch data at point of use — which is also the lethal-trifecta prompt-injection mitigation: the architecture makes it impossible for one agent process to hold two conflicting data accesses.
- Human escalation is unpredictable in advance, so the platform should define 'agent' broadly enough to cover both LLMs and humans: any action an LLM can take, a human can take, and downstream steps don't care which one acted.
- Because humans and LLMs consume context differently, a shared context definition should be mapped through methods into either a prompt (agent-friendly) or a UI (human-friendly).
- Evals emerge as a byproduct of the other three primitives: the ledger lets you replay and tweak a single prompt/model/code change, human-agent equivalency makes the human-LLM delta the eval score, and object storage lets you run evals on production data inside the customer's environment without exposing it.
- The recommended sequencing is inverted from the usual: take production enterprise constraints as architectural principles from day one and rebuild toward the POC's accuracy on top of those primitives, rather than strapping compliance onto a point solution.

## Notable Quotes

> "health care is a very challenging place to develop and deploy AI"
>
> — [0:01](https://www.youtube.com/watch?v=mav15aW9lLM&t=1s) &middot; *Sets the domain premise the speakers generalize from to finance, defense, and government.*

> "but the problem is that everyone here is assuming that the the hard part is done, that the AI was was the challenging part. But actually, as we know, often getting things into production is really where the challenge lies."
>
> — [3:34](https://www.youtube.com/watch?v=mav15aW9lLM&t=214s) &middot; *The talk's central thesis, stated as the pivot from POC celebration to production reality.*

> "It it has to contain a complete record of absolutely every action that the agent took."
>
> — [5:26](https://www.youtube.com/watch?v=mav15aW9lLM&t=326s) &middot; *Defines the enterprise bar for an audit trail against the developer's weaker mental model of a log.*

> "say our agent's decisions came up in a court of law. Could we show a justifiable chain of evidence for why the particular actions were taken by a decision?"
>
> — [6:07](https://www.youtube.com/watch?v=mav15aW9lLM&t=367s) &middot; *Reframes auditability as a legal-evidence standard rather than an observability nicety.*

> "An immutable record of events that store all of the transactions that happen throughout the system. And this is append-only timestamp log. It's complete. So, this is your source of truth for all of the data of the system."
>
> — [6:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=415s) &middot; *The concrete definition of the first primitive, borrowed from finance.*

> "And architecting this way, the making this trade-off, uh means that auditability becomes trivial. It falls out of your data storage paradigm that you've chosen."
>
> — [6:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=415s) &middot; *States the payoff of event sourcing: compliance as an emergent property, not a feature.*

> "for this kind of event logging or sometimes called event sourcing pattern, writes become very easy. So, you just drop an event. Reads become more difficult because you have to read through all of the events in order to reconstruct a view of what happened."
>
> — [7:44](https://www.youtube.com/watch?v=mav15aW9lLM&t=464s) &middot; *Names the explicit cost of the recommended pattern rather than selling it costlessly.*

> "all of your views of the data are ephemeral computed projections of the event log"
>
> — [8:23](https://www.youtube.com/watch?v=mav15aW9lLM&t=503s) &middot; *The technical claim that turns the read-cost trade-off into an advantage for evolving clinical narratives.*

> "You cannot have your agent, just as you cannot have humans, accessing and reading and utilizing healthcare data that they don't absolutely have a necessity to use at that that point in time for that particular journey."
>
> — [9:09](https://www.youtube.com/watch?v=mav15aW9lLM&t=549s) &middot; *Applies minimum-necessary access rules to agents as first-class principals.*

> "one piece of health care data can easily be over a megabyte in size or or much more than that"
>
> — [9:53](https://www.youtube.com/watch?v=mav15aW9lLM&t=593s) &middot; *A concrete data-shape number that motivates the object-storage choice.*

> "it's possible for developers to go back and debug and have observability over what happened, what particular steps the agent took, why it did that, and and retrace the agent's steps without having access to the personal health information itself"
>
> — [11:16](https://www.youtube.com/watch?v=mav15aW9lLM&t=676s) &middot; *The practical payoff of separating the event stream from the data blobs.*

> "Your agents can bear tokens and use those tokens to access the data at the point of use and not allow data to flow around the system as it likes."
>
> — [12:01](https://www.youtube.com/watch?v=mav15aW9lLM&t=721s) &middot; *Zero trust stated as an agent-architecture rule, not a policy document.*

> "The way I think about the lethal trifecta is can I solve for the constraint if I have an agent at point A with access to this data? Is it possible within my architecture for the agent to be also accessing data over here?"
>
> — [12:01](https://www.youtube.com/watch?v=mav15aW9lLM&t=721s) &middot; *Positions prompt-injection defense as an architectural invariant rather than a guardrail model.*

> "humans and LLMs ultimately process context differently. You know, LLMs will have no problem if you give them massive massive amounts of text, but humans that's not the case."
>
> — [13:29](https://www.youtube.com/watch?v=mav15aW9lLM&t=809s) &middot; *The constraint that forces a shared context definition with two renderings.*

> "you can make it such that any action that can be taken by an LLM could also be taken by a human"
>
> — [13:29](https://www.youtube.com/watch?v=mav15aW9lLM&t=809s) &middot; *The one-line statement of the human-agent equivalency primitive.*

> "you have this human agent equivalency, which means that for any task, you could get both the agent, the LLM agent, and the human to perform it, and your difference is your eval, that gives you the eval scores"
>
> — [15:50](https://www.youtube.com/watch?v=mav15aW9lLM&t=950s) &middot; *Shows how the escalation primitive doubles as an eval-generation mechanism.*

> "You can get your eval results without the sensitive data ever needing to come to where your agent is performing the work."
>
> — [16:28](https://www.youtube.com/watch?v=mav15aW9lLM&t=988s) &middot; *The privacy-preserving eval claim, and the answer to customers who won't let data leave their VPC.*

> "I like to think about architecture as taking your constraints very seriously and thinking about what you want to be simple within the system and then choosing the trade-offs for that."
>
> — [17:13](https://www.youtube.com/watch?v=mav15aW9lLM&t=1033s) &middot; *The generalizable design philosophy underneath all four primitives.*

> "trying to build up from it, strapping on the enterprise requirements as you come across them. Okay, we need eval, we need uh security, we need auditability, and bolting these on as additions to the the the foundations of the POC. You end up with something very brittle"
>
> — [17:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=1075s) &middot; *The named anti-pattern the whole talk is arguing against.*

> "if you take the constraints of a production-ready, scaled enterprise uh system seriously from the beginning and treat those as the architectural principles that you're going to build everything upon and then build back up towards that POC accuracy using your new primitives"
>
> — [17:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=1075s) &middot; *The prescriptive inversion of the normal POC-then-harden sequence.*

## Positions

- The bottleneck for enterprise AI agents is architecture and production requirements, not model accuracy — POCs typically hit their performance metrics and still fail to productionize. ([3:34](https://www.youtube.com/watch?v=mav15aW9lLM&t=214s), confidence: stated)
- A compliance audit trail under SOC 2, HITRUST, or HIPAA is categorically different from a developer log: it must record every action, every data access, and every authorization. ([5:26](https://www.youtube.com/watch?v=mav15aW9lLM&t=326s), confidence: stated)
- Adopting an append-only, unified event log as the system's source of truth makes auditability a free property of the storage design rather than a separate feature. ([6:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=415s), confidence: stated)
- Event sourcing makes writes easy and reads hard, and that read cost is acceptable — even beneficial — in healthcare because later events change the correct interpretation of earlier ones. ([7:44](https://www.youtube.com/watch?v=mav15aW9lLM&t=464s), confidence: stated)
- Sensitive data should live in immutable schema-driven object storage that the event log only references, so orchestration and observability are structurally separated from PHI. ([10:27](https://www.youtube.com/watch?v=mav15aW9lLM&t=627s), confidence: stated)
- Developers can effectively debug and retrace agent behavior while seeing only the schema of the data, never the protected health information itself. ([11:16](https://www.youtube.com/watch?v=mav15aW9lLM&t=676s), confidence: stated)
- Prompt injection and the lethal trifecta should be addressed by making the dangerous combination architecturally impossible — token-bearing agents fetching from segregated object storage — rather than by defending at the model layer. ([12:01](https://www.youtube.com/watch?v=mav15aW9lLM&t=721s), confidence: stated)
- Escalation points cannot be predicted in advance, so systems should treat humans and LLMs as interchangeable agents where any LLM action can also be performed by a human and downstream steps are indifferent to which acted. ([12:48](https://www.youtube.com/watch?v=mav15aW9lLM&t=768s), confidence: stated)
- Context should be defined once independent of consumer, then mapped into a prompt for an LLM or a UI for a human. ([14:15](https://www.youtube.com/watch?v=mav15aW9lLM&t=855s), confidence: stated)
- Offline eval datasets are unreliable because sampling may be unrepresentative and data drifts out of date, which favors replaying real production events instead. ([15:02](https://www.youtube.com/watch?v=mav15aW9lLM&t=902s), confidence: stated)
- Evals should emerge as a first-class property of the architecture rather than being attached to the side of the system. ([16:28](https://www.youtube.com/watch?v=mav15aW9lLM&t=988s), confidence: stated)
- The human-versus-LLM delta on the same task is a valid eval score. ([15:50](https://www.youtube.com/watch?v=mav15aW9lLM&t=950s), confidence: stated)
- Evals can be run on production data inside the customer's own environment without the sensitive data ever reaching the vendor's agent. ([16:28](https://www.youtube.com/watch?v=mav15aW9lLM&t=988s), confidence: stated)
- Good architecture means choosing which properties must be simple, accepting that other things become hard as a deliberate consequence. ([17:13](https://www.youtube.com/watch?v=mav15aW9lLM&t=1033s), confidence: stated)
- The patterns needed for agentic enterprise systems already exist in finance, defense, and big tech; AI requires recombining them, not inventing them from scratch. ([17:13](https://www.youtube.com/watch?v=mav15aW9lLM&t=1033s), confidence: stated)
- Building up from a successful POC and bolting on enterprise requirements as they surface produces brittle systems that don't generalize across use cases; the correct order is constraints first, then rebuild toward POC accuracy. ([17:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=1075s), confidence: stated)
- Lessons from building AI in healthcare transfer to other regulated, process-driven industries such as finance, defense, and government. ([1:10](https://www.youtube.com/watch?v=mav15aW9lLM&t=70s), confidence: stated)
- Some enterprise customers will not permit healthcare data to leave their on-prem VPC at all, forcing vendors into tangential rather than direct data access. ([9:53](https://www.youtube.com/watch?v=mav15aW9lLM&t=593s), confidence: stated)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [audit trails](../concepts/audit-trails.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [durable execution](../concepts/durable-execution.md)
- [go-to-market for ai products](../concepts/go-to-market-for-ai-products.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)

