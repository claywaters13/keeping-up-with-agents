---
title: "agent memory"
type: "concept"
slug: "agent-memory"
tier: "core"
maturity: "contested"
talk_count: 36
speaker_count: 36
---

# agent memory

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **36** talk(s) by **36** speaker(s)

**Definition:** Persisting and recalling information across an agent's turns, sessions, or lifetime — storage substrate, write policy, and retrieval policy.

*Also referred to as: agent memory systems, agent memory architecture, persistent agent memory, episodic memory for agents, agent long-term memory, memory layering, external memory stores*

## State of Practice

The field has largely stopped treating memory as a storage problem and started treating it as a control loop — write policy, management policy, and recall policy sitting around a stateless model. The strongest convergence is architectural rather than algorithmic: durable state belongs in an append-only event log or files on disk outside the agent process, so a dead container, a wiped context window, or a crashed laptop loses nothing. On substrate, the practitioner consensus has swung hard away from vector databases toward plain markdown in a Git repo, structured session logs, and hierarchical indexes — with Netflix, Sakana, and DataChain all reporting that simple stores plus a good recall policy beat embedding infrastructure, and Yohei Nakajima reporting that a raw structured log with no fact or entity extraction scored well on LongMemEval. The live methodological question is whether a memory system earns its cost at all: Berkeley's Continual Learning Bench had vanilla in-context learning top the leaderboard over sophisticated context-management systems on reward, cost, and gain Pareto frontiers, and Sakana found a memory harness added zero capability and pure cost when the task fit in context. Where the field does agree beyond storage: in-band memory writing produces locally-optimal and wrong entries, so an offline consolidation pass (Anthropic's 'dreaming', Machinecraft's nightly sleep cycle, Hermes-style post-task reflection) is needed to correct them. The unsolved edges are verification (RELAI: memory updates are the cheapest layer to change and the least verified), access control on shared memory, and whether stored preference facts can ever resolve which of two equally-correct metric definitions a given team means.

## Consensus

### Durable agent state must live outside the model's context window and outside the process running the harness — in an append-only log or files on disk — so that context wipes, compaction, and container death do not destroy work.

Support: **6** talk(s)

> "The state lives in files. It is not trapped inside one model. And this is the single most practical thing I learned all year."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)

### Simple, highly programmable stores — plain markdown in a central Git repo, a structured event log, a reference index — are sufficient memory substrates; specialized vector infrastructure is not a prerequisite and is often the wrong first move.

Support: **5** talk(s)

> "The solution that I mentioned so far of a memory is not very fancy vector search or or a vector database that needs to store all the catalog of patterns and anti-patterns. Rather, you can start with just a markdown files in a in a centralized Git repo."
>
> — [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [17:04](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=1024s)

Supporting talks: [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)

### Writing memory in-band during a session is insufficient on its own; a scheduled out-of-band consolidation pass over transcripts plus current memory state is required to correct wrong or locally-optimal entries and to promote recurring reasoning into reusable skills.

Support: **5** talk(s)

> "Every night, Eira runs a sleep cycle. It replays the day, locks in useful stuff, hunts for contradictions, gently forgets the stale junk, and turns the day's work into reusable skills."
>
> — [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [6:49](https://www.youtube.com/watch?v=jtzh-GBXBWc&t=409s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)

### Model capability is no longer the binding constraint on agent usefulness; the constraint is durable, environment-specific memory and context, which has not scaled alongside intelligence.

Support: **6** talk(s)

> "Intelligence has 1,000x'd in the last decade. Just in the last 6 months, we have 2x'd on that axis. On the other hand, context, the situated knowledge of your business, that's barely moved."
>
> — [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [3:17](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=197s)

Supporting talks: [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)

### Memory should be scoped to the organization and shared across agents and developers, not siloed per-agent or per-user, because separate memory stores learn separately and diverge.

Support: **5** talk(s)

> "Because it crosses developer boundaries, not per developer, the agent can have more context than any single developer."
>
> — [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [19:13](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1153s)

Supporting talks: [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### Storing user preferences, profiles, and conversation history is the wrong abstraction for production agent memory; what needs persisting is task reasoning and precomputed understanding of the domain.

Support: **3** talk(s)

> "current memory is that they basically store user preferences, profile, conversation history, or long-lived personalization. So, chat experience is not self-improving learning systems for production."
>
> — [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [3:32](https://www.youtube.com/watch?v=Jx4ZFEAq6bY&t=212s)

Supporting talks: [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)

## Disagreements

### Should long conversations be carried forward by compacting or summarizing history, or by keeping an immutable log and resetting context to re-read it?

| Position A | Position B |
|---|---|
| Compaction is inherently lossy — you cannot control what survives and what it drops is gone — so keep an append-only immutable log and either fetch old context back or clear context entirely and re-read self-written handoff files. Deterministically re-allocating a fresh context each iteration beats compacting.<br>*[Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)* | Compaction now works well enough that the old advice to start a fresh thread is obsolete — threads five weeks old with hundreds of sub-agents stay coherent — and rolling summarization plus a truncated recent window beats always stuffing in the latest messages.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)* |

*Why it matters: This decides whether you build session infrastructure (durable event log, restore/fork/replay, handoff files) or just rely on the harness's built-in compaction and one long-lived thread. The first is a real engineering investment; the second is free but silently discards state you cannot get back.*

### Do plain files loaded into context scale as agent memory, or does memory require an engineered retrieval structure (graph traversal, ranked ledger, precomputed context model)?

| Position A | Position B |
|---|---|
| Markdown files plus a reference index are enough; skip vector databases, knowledge graphs, and semantic search. The store should be simple and programmable and the model should read it directly.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)* | File-based memory loads everything speculatively and burns 100k+ tokens per round; it works at small scale with a good model and fails past the context window. Memory needs structure — graph traversal seeded by vector search, a rank-only decisions ledger, or an offline-computed context model — because similarity is not relationship and hand-maintained .md files cannot keep pace with changing definitions.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)* |

*Why it matters: The two camps are separated mostly by corpus size and query shape: the file camp reports success on catalogs and personal note collections, the structure camp on multi-hop enterprise questions and archives that exceed a million tokens. Picking wrong costs either months of graph-building you didn't need, or a memory system that silently degrades once your data outgrows the window.*

### Should the model manage its own memory structure, or should the system impose a schema, salience gate, and scoring policy?

| Position A | Position B |
|---|---|
| Let the model structure and maintain its own memory. Prescribing memory schemas measurably drops performance, and a raw structured log with no fact or entity extraction performs well on LongMemEval — models reason about their own memory structure better than you can specify it.<br>*[Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* | Memory needs explicit engineered structure: a salience gate deciding what is worth remembering, atomic fact extraction rather than storing everything, a source-of-truth hierarchy, a utility score weighting retrieval by whether a memory historically helped or hurt, and a tiered index → summary → derivative → raw layout.<br>*[The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)* |

*Why it matters: Structure is where the engineering budget goes. If the free-rein camp is right, curation machinery is dead weight that degrades as models improve; if the structured camp is right, unstructured memory accumulates junk and contradictions that no amount of model capability recovers from.*

### Can memory updates be applied autonomously, or must every write be verified against regressions or approved by a human?

| Position A | Position B |
|---|---|
| Memory-layer updates are the cheapest and fastest way to improve an agent and are typically unverified for both efficacy and regression risk; regression prevention belongs inside the optimization objective, and self-improving skills that evolve on their own break downstream dependents unless learnings are routed to a human maintainer to approve or reject.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)* | Autonomous memory evolution is the point: feed transcripts and memory state through a periodic batch process that edits memory as needed so the next day's sessions are automatically smarter, and let a skill edit itself after failures so it improves over time.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)* |

*Why it matters: Autonomous consolidation is what makes memory compound without human cost; gating it is what stops a bad memory from silently regressing behavior that already worked. Which you pick determines whether you need replayable learning environments and evaluators before a memory write can land.*

## Practical Guidance

**Do:**

- Back every session with an append-only, immutable event log that the harness process can die and reattach to; keep the harness stateless and treat sandboxes as disposable hands.
- Run a scheduled offline consolidation pass over the day's transcripts plus current memory state, specifically to correct memories that were locally optimal or wrong when written in-band.
- Start memory as hierarchically indexed markdown in a centralized Git repo and only add graph or vector retrieval when the corpus provably exceeds the context window.
- Verify agent work in a separate context window from the one that produced it — self-grading in the same context produces confabulation.
- Report gain (stateful reward minus stateless reward) alongside raw reward, so you can tell whether the memory system is contributing or the base model is.
- Skip the memory harness when the task and its relevant context fit in the window — Sakana measured identical performance with and without memory in that regime, at strictly higher cost.
- Treat recall policy as a first-class metric and measure it in tokens as well as accuracy; bad recall both misleads the agent and costs more.
- Keep hand-authored source notes immutable and write all generated content into a separate derivative layer the LLM owns.
- Resolve conflicting stored facts by letting human corrections permanently win over model-derived ones, and gate what enters memory with an explicit salience check.
- Weight retrieval by whether a memory historically helped or hurt the outcome, and once ~10 memories accumulate on a topic, bake the reasoning into a skill so operating instructions stay current.
- Make memory a governed surface: give it its own flag type resolved per turn, and ensure sub-agents go through the same middleware as the parent.

**Avoid:**

- Prescribing an explicit memory schema for the model — specifying what types of memories to save measurably drops performance versus letting the model manage its own store.
- Making destructive compaction your default long-context strategy; whatever it drops cannot be fetched back.
- Exposing memory mutation through MCP tools without guardrails — an agent one step from a forget command can wipe its own memory.
- Per-agent memory silos: each agent learning separately and differently makes it impossible to trace whether an error came from the model, the agent, or the context.
- Treating production logs plus feedback as a learning environment; they must be lifted into replayable simulations with evaluators before any memory fix can be shown to help and shown to break nothing.
- Assuming that retrieving the right memory means the agent will use it — oracle retrieval does not reach maximum task performance.
- Speculatively loading the entire memory directory every round; Neo4j measured agents pulling 100k+ tokens per round this way.
- Expecting stored user preferences to disambiguate which of two equally-correct metric definitions applies — memory stores the preference but cannot tell which one to use when.
- Attaching long-term memory to a latency-bound path; a sub-500ms transaction SLA leaves room only for short-term in-memory context.
- Shipping unverified memory writes as your improvement mechanism — it is the cheapest layer to change and the one where hidden regressions are least likely to be caught.

## Notable Outliers

- A structured session log used directly as memory — no semantic ingestion, no fact extraction, no entity extraction, just embed the query, grab neighboring messages, and fit them to context — performed well on LongMemEval. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [8:17](https://www.youtube.com/watch?v=khVX_BUnEwU&t=497s))
- Vanilla in-context learning topped the Continual Learning Bench 1.0 leaderboard over more expensive purpose-built context-management systems, and held across both the reward-vs-cost and gain-vs-cost Pareto frontiers. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s))
- Giving the model the correct memory does not make it use the memory — oracle retrieval still fails to reach maximum task performance because the model can retrieve wrong, ignore it, or get confused. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s))
- An unmodified default RLM harness, with no memory engineering at all, performs comparably to a top-10 purpose-built memory system despite billions of dollars going into custom memory systems. ([Recursive Coding Agents](../talks/recursive-coding-agents.md), [5:01](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=301s))
- Long-term memory is incompatible with a sub-500ms fraud-decision SLA, so the agent runs on short-term in-memory context over a precomputed cross-context semantic layer instead. ([Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [11:32](https://www.youtube.com/watch?v=o6U_2vd967Y&t=692s))
- Exposing memory as MCP tools puts the agent one step away from calling the forget command and wiping out its own memory. ([CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [6:23](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=383s))
- In group deployments memory, not the model, determines the agent's behavior and identity — and whether a fact is public or private is a property of the room it was shared in, not of the data, so permissions should be enforced by per-user LoRA adapters over shared memory rather than in code. ([Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [12:29](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=749s))
- For persona systems, fine-tuning is strictly worse than context-window anchoring, because it layers a thin personal signal over vast cultural sediment in the base weights in ways no longer open to audit — the persona is the configuration, not the checkpoint. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [28:10](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1690s))
- Augmenting an agent with semantic and episodic memory made 15 of 25 percentage points of flip-flopping cybersecurity verdicts consistent — comparable to fine-tuning, at far lower cost — while 10% stayed inconsistent. ([Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [22:10](https://www.youtube.com/watch?v=wEc9aG7cRQc&t=1330s))

## All Talks

- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)
- [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)
- [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)
- [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)
- [On AI and Knowledge](../talks/on-ai-and-knowledge.md)
- [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)
- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)
- [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)
- [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md)
- [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)

## Speakers

- [Angie Jones](../speakers/angie-jones.md)
- [Dan Farrelly](../speakers/dan-farrelly.md)
- [Diane Lin](../speakers/diane-lin.md)
- [Divakar Kumar](../speakers/divakar-kumar.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Ishita Daga](../speakers/ishita-daga.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [James Le](../speakers/james-le.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Jeffrey Lee-Chan](../speakers/jeffrey-lee-chan.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Kyle Jaejun Lee](../speakers/kyle-jaejun-lee.md)
- [Lance Martin](../speakers/lance-martin.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Parth Asawa](../speakers/parth-asawa.md)
- [Paul Iusztin](../speakers/paul-iusztin.md)
- [Paul Klein IV](../speakers/paul-klein-iv.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Rajat Shah](../speakers/rajat-shah.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Stefania Druga](../speakers/stefania-druga.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Victor Savkin](../speakers/victor-savkin.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

