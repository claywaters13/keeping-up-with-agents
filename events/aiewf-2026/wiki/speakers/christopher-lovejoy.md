---
title: "Christopher Lovejoy"
type: "speaker"
slug: "christopher-lovejoy"
role: "Member of Technical Staff"
company: "Anthropic"
talk_count: 1
---

# Christopher Lovejoy

**Member of Technical Staff &middot; Anthropic**

Member of Technical Staff at Anthropic. Previously Anterior, Billions Health, Medical Doctor.

[LinkedIn](https://linkedin.com/in/dr-christopher-lovejoy)

## Talks

- [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md) (AI in Healthcare, co-presented)

## Scheduled Sessions

- **Why Your Enterprise Tech Stack Isn't Ready for AI Agents - And What to Build Instead** &middot; Day 4 — Session Day 3 &middot; 3:45pm-4:05pm &middot; Track 7

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

## From Talks This Speaker Co-Presented

*These quotes come from talks with multiple speakers. The extraction is talk-level only and does not identify which co-presenter said which line — do not read these as this person's individual words.*

> "health care is a very challenging place to develop and deploy AI"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [0:01](https://www.youtube.com/watch?v=mav15aW9lLM&t=1s)

> "but the problem is that everyone here is assuming that the the hard part is done, that the AI was was the challenging part. But actually, as we know, often getting things into production is really where the challenge lies."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [3:34](https://www.youtube.com/watch?v=mav15aW9lLM&t=214s)

> "It it has to contain a complete record of absolutely every action that the agent took."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [5:26](https://www.youtube.com/watch?v=mav15aW9lLM&t=326s)

> "say our agent's decisions came up in a court of law. Could we show a justifiable chain of evidence for why the particular actions were taken by a decision?"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [6:07](https://www.youtube.com/watch?v=mav15aW9lLM&t=367s)

> "An immutable record of events that store all of the transactions that happen throughout the system. And this is append-only timestamp log. It's complete. So, this is your source of truth for all of the data of the system."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [6:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=415s)

> "And architecting this way, the making this trade-off, uh means that auditability becomes trivial. It falls out of your data storage paradigm that you've chosen."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [6:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=415s)

> "for this kind of event logging or sometimes called event sourcing pattern, writes become very easy. So, you just drop an event. Reads become more difficult because you have to read through all of the events in order to reconstruct a view of what happened."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [7:44](https://www.youtube.com/watch?v=mav15aW9lLM&t=464s)

> "all of your views of the data are ephemeral computed projections of the event log"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [8:23](https://www.youtube.com/watch?v=mav15aW9lLM&t=503s)

> "You cannot have your agent, just as you cannot have humans, accessing and reading and utilizing healthcare data that they don't absolutely have a necessity to use at that that point in time for that particular journey."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [9:09](https://www.youtube.com/watch?v=mav15aW9lLM&t=549s)

> "one piece of health care data can easily be over a megabyte in size or or much more than that"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [9:53](https://www.youtube.com/watch?v=mav15aW9lLM&t=593s)

> "it's possible for developers to go back and debug and have observability over what happened, what particular steps the agent took, why it did that, and and retrace the agent's steps without having access to the personal health information itself"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [11:16](https://www.youtube.com/watch?v=mav15aW9lLM&t=676s)

> "Your agents can bear tokens and use those tokens to access the data at the point of use and not allow data to flow around the system as it likes."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [12:01](https://www.youtube.com/watch?v=mav15aW9lLM&t=721s)

> "The way I think about the lethal trifecta is can I solve for the constraint if I have an agent at point A with access to this data? Is it possible within my architecture for the agent to be also accessing data over here?"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [12:01](https://www.youtube.com/watch?v=mav15aW9lLM&t=721s)

> "humans and LLMs ultimately process context differently. You know, LLMs will have no problem if you give them massive massive amounts of text, but humans that's not the case."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [13:29](https://www.youtube.com/watch?v=mav15aW9lLM&t=809s)

> "you can make it such that any action that can be taken by an LLM could also be taken by a human"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [13:29](https://www.youtube.com/watch?v=mav15aW9lLM&t=809s)

> "you have this human agent equivalency, which means that for any task, you could get both the agent, the LLM agent, and the human to perform it, and your difference is your eval, that gives you the eval scores"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [15:50](https://www.youtube.com/watch?v=mav15aW9lLM&t=950s)

> "You can get your eval results without the sensitive data ever needing to come to where your agent is performing the work."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [16:28](https://www.youtube.com/watch?v=mav15aW9lLM&t=988s)

> "I like to think about architecture as taking your constraints very seriously and thinking about what you want to be simple within the system and then choosing the trade-offs for that."
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [17:13](https://www.youtube.com/watch?v=mav15aW9lLM&t=1033s)

> "trying to build up from it, strapping on the enterprise requirements as you come across them. Okay, we need eval, we need uh security, we need auditability, and bolting these on as additions to the the the foundations of the POC. You end up with something very brittle"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [17:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=1075s)

> "if you take the constraints of a production-ready, scaled enterprise uh system seriously from the beginning and treat those as the architectural principles that you're going to build everything upon and then build back up towards that POC accuracy using your new primitives"
>
> — [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [17:55](https://www.youtube.com/watch?v=mav15aW9lLM&t=1075s)

