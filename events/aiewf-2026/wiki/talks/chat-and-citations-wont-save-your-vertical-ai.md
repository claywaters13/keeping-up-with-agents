---
title: "Chat and citations won't save your vertical AI"
type: "talk"
slug: "chat-and-citations-wont-save-your-vertical-ai"
org: "Filed Inc"
video_id: "RGiXcVxSD3s"
duration_sec: 912
word_count: 2891
speakers: ["Atul Ramachandran"]
---

# Chat and citations won't save your vertical AI

**Speakers:** [Atul Ramachandran](../speakers/atul-ramachandran.md)

**Org:** Filed Inc

**Duration:** 15m 12s

[Watch on YouTube](https://www.youtube.com/watch?v=RGiXcVxSD3s)

## Summary

Atul Ramachandran, CTO of Filed Inc (tax software for US tax professionals), argues that chat and citations — the default interface pattern for vertical AI products — structurally fail the promise those products sell. Chat is synchronous, so it keeps users tethered to the platform instead of freeing them; citations shift verification burden back onto the customer, adding work rather than removing it. He proposes a third abstraction layer he calls 'agentic delegation,' after physical branches and digital self-service, where the bottleneck on value creation shifts from headcount to user visits to neither. The concrete design metaphor is a conveyor belt: agents are workers, users are supervisors, and the product needs four components — delegatable long-running tasks, skills that teach agents user-specific conventions, monitoring/traces, and control mechanisms for pause-and-intervene. He closes with a metrics argument: weekly active users should go down while weekly active sessions go up. Worth watching for anyone shipping vertical AI who has defaulted to a chat UI and is hearing that agents aren't actually saving customers time.

## Key Points

- Chat is a synchronous medium, which means users cannot delegate work and leave the platform — the core promise of AI agents doing work while you sleep is broken by the interface itself.
- Citations improve grounding and reduce hallucinations, but they transfer the verification burden back to the customer, which is especially costly in high-stakes verticals like healthcare, legal, and tax.
- Product history has moved through three abstraction layers — physical branch (bottleneck: number of employees), digital self-service (bottleneck: number of users), and now agentic delegation (neither is the bottleneck).
- The governing design principle is 'design for delegation, not participation': ask what the interface looks like when a user hands a task off rather than performing it.
- Delegatable tasks should be ones that take users more than an hour or two and are at least somewhat repeatable; Filed identified three such tasks in the tax workflow.
- A generic background agent gets 80–90% of the way there, but the remaining 20% — user-specific quirks and conventions — must be captured through skills, and those skills should be inferred automatically from product usage rather than authored in a separate interface.
- Traces that show how the agent produced each value are where trust and visibility are built, and where most customer complaints get resolved.
- Level-two (self-service) features don't disappear under agentic delegation — users only delegate when they're confident they can take the wheel back, so pause/intervene and plan-approval flows for irreversible actions are prerequisites for trust.
- The right success metric flips: weekly active sessions should rise while weekly active users falls, because time on platform no longer measures delivered value.

## Notable Quotes

> "I'm here to tell you that citations and chat alone will not keep allow you to keep the promise that you made to the customers."
>
> — [0:35](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=35s) &middot; *The thesis of the talk, stated plainly.*

> "Chat is synchronous. If you think about it, even when you're coding, you're Let's say you're using product code as as as long as you're typing the request. Once the request is typed, you're waiting for the agent to respond."
>
> — [1:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=111s) &middot; *Names the specific structural defect in chat rather than just criticizing it.*

> "This synchronous medium does not allow the customers to leave the platform and go and do their work."
>
> — [1:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=111s) &middot; *The consequence that connects interface choice to broken customer promise.*

> "Similarly, citations also puts the verification burden back into the customer."
>
> — [2:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=156s) &middot; *The counterintuitive half of the argument — citations as a cost, not just a feature.*

> "last just last month, we closed more revenue than what we have done in the one year alone before that"
>
> — [1:12](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=72s) &middot; *The only hard business number backing the speaker's credibility.*

> "this essentially meant the bottleneck was the number of users number of employees that a company had. That's the bottleneck for creating value"
>
> — [3:17](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=197s) &middot; *Sets up the bottleneck framing that drives the three-layer model.*

> "the bottleneck moved from the number of employees a company have to number of users that the company have. The more users meant more value you can generate."
>
> — [3:47](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=227s) &middot; *The middle rung of the abstraction ladder, explaining why WAU became the default metric.*

> "the bottleneck of number of users also goes away. So, it's no longer than amount of value that you generate is the amount of the number of times the user have visited your platform"
>
> — [4:26](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=266s) &middot; *The core economic claim of agentic delegation.*

> "AI agents are your workers in that conveyor belt, while, you know, the conveyor belt and the entire infrastructure around it is your product."
>
> — [5:02](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=302s) &middot; *The central metaphor the rest of the talk's architecture hangs on.*

> "Essentially, design for delegation, not participation."
>
> — [5:43](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=343s) &middot; *The most portable takeaway, repeated as the first key takeaway at the close.*

> "you as a developer or a product engineer have to find tasks that your users do that take more than a couple of hours"
>
> — [7:00](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=420s) &middot; *A concrete, checkable selection criterion for what to build agents around.*

> "it will produce output, sure, right? It produce It will get you most of like 80 to 90% there, but think of it this way, like that will not yet solve the problems of of the user"
>
> — [8:29](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=509s) &middot; *Quantifies the gap that skills are meant to close.*

> "This is the last 20% of the of the work that you need to take care of. This is where the real value is, the quirks of the work"
>
> — [9:05](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=545s) &middot; *Locates the defensible value in personalization rather than base capability.*

> "You do not need to have like a complete separate interface where users you go and create skills, that won't work."
>
> — [9:05](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=545s) &middot; *A direct design prohibition others would disagree with.*

> "in our case we trace back each and every value that the AI agent produced in a particular, you know, in the format that the users can easily see. This is where the trust is built."
>
> — [10:15](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=615s) &middot; *Ties a specific implementation practice to the trust outcome.*

> "if they don't have the confidence that, you know, if something goes wrong they can take them back control then then the users will completely lose trust."
>
> — [10:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=651s) &middot; *The argument for why control mechanisms are load-bearing, not optional polish.*

> "it should feel like, you know, they're taking the users are taking the wheel, not abandoning the car and, you know, creating a new car"
>
> — [10:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=651s) &middot; *Memorable framing of what graceful intervention should feel like.*

> "In our case we could do it very simply by, you know, pausing whenever the agent was trying to make an assumption, we pause."
>
> — [10:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=651s) &middot; *A specific, implementable heuristic for when to interrupt an autonomous agent.*

> "some actions are usually irreversible and are dangerous actions. And in those cases, you need to present a plan."
>
> — [12:13](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=733s) &middot; *States the plan-approval tradeoff for destructive operations.*

> "your actual aim should be the weekly active users go down while weekly active sessions go up"
>
> — [13:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=816s) &middot; *The talk's most contrarian and most checkable prescription.*

## Positions

- Chat and citations alone are insufficient for vertical AI products to deliver the time-and-cost savings they promise customers. ([0:35](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=35s), confidence: stated)
- Chat's synchronicity is the specific defect: it prevents customers from leaving the platform while work is done. ([1:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=111s), confidence: stated)
- Citations add net work for the user by shifting verification burden onto them, which is especially problematic in healthcare, legal, and tax. ([2:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=156s), confidence: stated)
- Product abstraction has progressed through three levels — physical presence, digital self-service, and agentic delegation — each removing the prior bottleneck on value creation. ([3:17](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=197s), confidence: stated)
- Agentic products should be architected as a conveyor belt with agents as workers and users as supervisors, not operators. ([5:02](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=302s), confidence: stated)
- The right tasks to build background agents around are ones taking users more than a couple of hours and that are repeatable. ([7:00](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=420s), confidence: stated)
- A generic end-to-end background agent gets only 80–90% of the way to solving the user's problem; the remaining value lies in user-specific conventions. ([8:29](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=509s), confidence: stated)
- Skills should be captured automatically from observed product usage rather than authored by users in a dedicated skill-creation interface, which won't work. ([9:05](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=545s), confidence: stated)
- Traces showing how the agent produced each output are the primary mechanism for building trust and are where most customer complaints get resolved. ([10:15](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=615s), confidence: stated)
- Pausing the agent whenever it is about to make an assumption is a workable interruption heuristic. ([10:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=651s), confidence: stated)
- Level-two self-service features must remain in the product, because users only delegate when confident they can take control back. ([11:32](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=692s), confidence: stated)
- Irreversible or dangerous actions require presenting a plan for user approval before execution. ([12:13](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=733s), confidence: stated)
- Weekly active users is the wrong success metric for agentic products; weekly active sessions should rise while WAU declines (though not to zero). ([13:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=816s), confidence: stated)
- Lessons from building tax AI agents transfer to AI products in other verticals. ([1:12](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=72s), confidence: stated)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent skills](../concepts/agent-skills.md)
- [background agents](../concepts/background-agents.md)
- [citation and grounding](../concepts/citation-and-grounding.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [roi measurement](../concepts/roi-measurement.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

