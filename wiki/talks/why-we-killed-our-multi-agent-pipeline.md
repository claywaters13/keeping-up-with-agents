---
title: "Why We Killed Our Multi-Agent Pipeline"
type: "talk"
slug: "why-we-killed-our-multi-agent-pipeline"
track: "Graphs"
org: "ZS Associates"
day: "Day 4 — Session Day 3"
room: "Track 5"
video_id: "u6jJcIFDLE4"
duration_sec: 900
word_count: 2709
speakers: ["Abhilash Asokan", "Subbiah Sethuraman"]
---

# Why We Killed Our Multi-Agent Pipeline

*Program title: Why We Killed Our Multi-Agent Pipeline: Lessons From Pharma Commercial Intelligence*

**Speakers:** [Abhilash Asokan](../speakers/abhilash-asokan.md), [Subbiah Sethuraman](../speakers/subbiah-sethuraman.md)

**Org:** ZS Associates

**Track:** Graphs &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 15m 00s

[Watch on YouTube](https://www.youtube.com/watch?v=u6jJcIFDLE4)

## Summary

Two AI engineering leads at ZS Associates describe why they dismantled a multi-agent pipeline they built for pharma commercial analytics. The original design mirrored a human analyst's four-step workflow — signal detection, source localization, driver attribution, synthesis — with one agent per step behind an orchestrator, and it produced outputs where every individual fact was right but the end-to-end narrative was incoherent (correct payer-coverage root cause, but a sales-rep action recommendation that ignored it). They diagnose three causes: an LLM doing work that statistics should do, context loss at every inter-agent handoff, and no shared business-domain model. The fix came from watching Claude Code work in an empty directory with just bash and a database: pull signal detection into a deterministic pre-agent pipeline, consolidate all reasoning into a single agent that may delegate investigations (but never judgment) to sub-agents, and use a domain knowledge graph as a control plane where every edge is a hypothesis the agent may test. Worth watching if you are deciding how far to decompose an agentic system, or how to bound an agent's search space with domain structure.

## Key Points

- Decomposing an agentic system along the lines of a human workflow is a design smell — the architecture should be derived from what the system needs, not from how analysts happen to divide their labor.
- Their per-step agents each produced factually correct outputs, but no agent owned the end-to-end picture, so the recommended action did not follow from the diagnosed cause.
- Context degrades at every agent-to-agent handoff; the synthesis agent never absorbed the weighting the driver-attribution agent had placed on payer coverage.
- Signal detection was moved out of the agentic system entirely into a deterministic statistical pipeline with thresholds, guardrails, and prioritization, which pushes signals onto a queue that wakes the agent.
- The team redesigned by observing Claude Code operate in an empty directory with only bash and database access, then copying the patterns it exhibited (a query tool, dynamically spawned focused sub-agents).
- They kept parallelism and sub-agents but removed distributed reasoning: sub-agents return investigation results, while all judgment stays with a single main agent.
- A knowledge graph built with in-house pharma domain experts encodes entities (geographies, payers, accounts, brands) and KPI-to-KPI driver relationships that the agent could not reliably infer from tables alone.
- The graph functions as a control plane rather than a lookup layer — it dictates which paths the agent may take and which hypotheses it may evaluate, bounding an otherwise combinatorial search over dimensions.
- The resulting loop (neighborhood → hypothesis → query real data → reason → traverse or stop) takes 50+ turns and many tokens but compresses analysis that took an analyst three to four weeks into 20–30 minutes.

## Notable Quotes

> "obviously it's not the LLM which failed, right? It's the way how we split the work, right? Because we tried mimicking the analyst behavior, and we did it."
>
> — [4:37](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=277s) &middot; *The thesis of the talk: the failure was architectural decomposition, not model capability.*

> "at each level if you see, it has actually derived the right fact, but then there is no single agent which is owning which understands the end-to-end picture basically."
>
> — [4:03](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=243s) &middot; *Names the precise failure mode — locally correct, globally incoherent output.*

> "signals like things like your sales drop is a simple information which you can use statistical methods to actually go and fetch this information. You don't need a language model actually, right? To fetch this information."
>
> — [4:37](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=277s) &middot; *States the boundary between deterministic and agentic work concretely.*

> "as your multi agents, there is a lot of context hand off which is happening, and context is actually getting lost at each of these hand offs"
>
> — [4:37](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=277s) &middot; *The core cost of multi-agent decomposition they identify.*

> "the last big piece is there is no shared understanding of the business domain knowledge for all these agents. All these agents don't understand metrics"
>
> — [5:15](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=315s) &middot; *Sets up the knowledge-graph half of the solution.*

> "We didn't do any of that. We like all of us, we went back to Cloud Code. So, we opened a very plain empty directory. I ran Cloud Code. Then give it just bash and the database."
>
> — [6:26](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=386s) &middot; *Unusual methodology: derive architecture by observing a general coding agent instead of redesigning topology.*

> "This is something we don't want an agent to do. This is a completely deterministic workflow. So, we separated it out from the agentic system."
>
> — [7:08](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=428s) &middot; *The clearest statement of their deterministic/agentic split.*

> "The moment a signal comes to the queue, the agent wakes up. So, the agent's job is to investigate, not to identify."
>
> — [7:49](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=469s) &middot; *A memorable one-line reframing of the agent's scope.*

> "What we removed is, do we need distributed reasoning? We didn't but the judgment to be distributed between agents. That we wanted to consolidate to a single agent."
>
> — [8:30](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=510s) &middot; *Distinguishes parallelism (kept) from distributed reasoning (removed).*

> "That you can still delegate to a sub-agent. You can get back the uh results back, not the reasoning or the judgment."
>
> — [8:30](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=510s) &middot; *Defines exactly what sub-agents are allowed to return.*

> "the agent was looking at data, looking at tables, then trying to infer the relationship. That which was not scalable. And it often produce relationship which which is not actually exist in the data."
>
> — [9:11](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=551s) &middot; *Motivates encoding domain structure explicitly rather than letting the model infer it.*

> "the knowledge graph is not just something the agent looks up for data. It is a control plane for the agent."
>
> — [10:32](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=632s) &middot; *The talk's signature claim about knowledge graphs.*

> "the knowledge graphs dictates what the agent can look into, what path it can take, what investigation hypothesis uh it can evaluate"
>
> — [10:32](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=632s) &middot; *Spells out what 'control plane' means operationally.*

> "every edge is a hypothesis. So, the agent can go and evaluate that hypothe- hypothesis. Uh it doesn't go outside of this."
>
> — [11:48](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=708s) &middot; *Compact statement of how the graph bounds the agent's search.*

> "after like 50 plus turns, a whole lot of tokens, it's able to produce something an analyst was able to produce maybe in three or four weeks in like maybe 20 30 minutes"
>
> — [13:10](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=790s) &middot; *The only quantified outcome claim in the talk, including its token cost.*

> "First thing is I think we should not be introducing human constraints or design constraints into architecture."
>
> — [13:10](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=790s) &middot; *First of four takeaways and the general lesson behind killing the pipeline.*

> "any complex workflows will have deterministic parts and agentic parts. Don't let agents actually run the deterministic part, right?"
>
> — [13:51](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=831s) &middot; *Portable design rule stated as an imperative.*

> "I think graph cannot be treated just as a lookup layer. I think graph has to be treated as a control plane which the agent uses to navigate and takes the next decisions basically."
>
> — [13:51](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=831s) &middot; *The takeaway they flag as most important.*

## Positions

- Their multi-agent pipeline's incoherence was caused by how the work was split, not by any LLM capability limitation. ([4:37](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=277s), confidence: stated)
- Mimicking a human analyst's workflow steps is the wrong basis for agent system architecture; architecture should be derived rather than copied from human process constraints. ([13:10](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=790s), confidence: stated)
- Signal detection over metrics like sales drops should be done with statistical methods, not a language model. ([4:37](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=277s), confidence: stated)
- Every agent-to-agent handoff loses context, and the loss compounds across a chain of specialized agents. ([4:37](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=277s), confidence: stated)
- Complex workflows should be partitioned so that deterministic components run outside the agentic system entirely, before the agent is invoked. ([13:51](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=831s), confidence: stated)
- Exactly one agent should own end-to-end reasoning; parallelism and sub-agents are fine, but judgment must not be distributed. ([8:30](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=510s), confidence: stated)
- Sub-agents should return investigation results only, never reasoning or judgment. ([8:30](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=510s), confidence: stated)
- Agents inferring entity and KPI relationships from raw tables does not scale and produces relationships that do not exist in the data. ([9:11](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=551s), confidence: stated)
- A knowledge graph should act as a control plane that constrains which paths and hypotheses an agent may pursue, not merely as a data lookup layer. ([10:32](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=632s), confidence: stated)
- Observing how a general-purpose coding agent (Claude Code) operates with minimal tools is a valid way to derive production agent architecture. ([6:26](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=386s), confidence: implied)
- The consolidated single-agent system reaches root causes in 20–30 minutes and 50+ turns for analysis that previously took an analyst three to four weeks. ([13:10](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=790s), confidence: stated)
- High token and turn counts are an acceptable cost for correct end-to-end reasoning. ([13:10](https://www.youtube.com/watch?v=u6jJcIFDLE4&t=790s), confidence: implied)

## Concepts

- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [incident response automation](../concepts/incident-response-automation.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [ontology design](../concepts/ontology-design.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

