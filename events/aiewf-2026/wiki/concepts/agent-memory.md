---
title: "agent memory"
type: "concept"
slug: "agent-memory"
tier: "core"
maturity: "contested"
talk_count: 39
speaker_count: 41
---

# agent memory

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **39** talk(s) by **41** speaker(s)

**Definition:** Persisting and recalling information across an agent's turns, sessions, or lifetime — storage substrate, write policy, and retrieval policy.

*Also referred to as: agent memory systems, agent memory architecture, persistent agent memory, episodic memory for agents, agent long-term memory, memory layering, external memory stores*

## State of Practice

As of this conference the field has stopped treating memory as a database problem and started treating it as a control loop — write policy, consolidation policy, recall policy — layered on top of a durable substrate that lives outside the model's context window. The dominant architecture is an append-only session or event log (Anthropic's managed-agents session log, ActiveGraph's immutable event log, files-on-disk fleets) that survives harness death, container death, and context wipes, plus a smaller derived artifact — a running profile, a decisions ledger, a pattern catalog, a skills directory — that gets injected or retrieved per turn. Two findings recur independently: in-band memory writing produces incorrect and locally-optimal entries that only an out-of-band consolidation pass ("dreaming", a nightly sleep cycle, a 24-hour profile rebuild) corrects, and pure dense-vector recall is not a sufficient retrieval policy — BM25, graph traversal, rank-only ledgers, and outcome-weighted scores all beat it on someone's benchmark. Costs are now measured explicitly: memory is a compute-allocation tradeoff between update frequency and per-turn serving tokens (ChatGPT ~4k tokens every few days vs. Claude ~1k every 24 hours), and bad recall shows up as token spend, not just wrong answers. What is genuinely unsettled is whether an engineered memory system beats simply keeping everything in context — vanilla in-context learning topped the Continual Learning Bench leaderboard, and one team found untouched full history won on recall, cost, and latency at once — and whether markdown files remain viable past the million-token mark or must be replaced by graphs and precomputed world models.

## Consensus

### Durable agent state must live outside the model's context window — in an append-only log or files on disk — so that compaction, container death, or a machine crash cannot destroy the work.

Support: **6** talk(s)

> "The context can get wiped, the machine can even crash, and the work still survives because it was never only in the model."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [3:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=190s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)

### Memory written in-band during a session is unreliable on its own; a periodic out-of-band consolidation pass is required to correct wrong entries, resolve contradictions, and compress experience into reusable abstractions.

Support: **6** talk(s)

> "those mistakes get stuck in memory unless you have an offline process to kind of correct them"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [15:40](https://www.youtube.com/watch?v=9QebvrrY3KY&t=940s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)

### Dense vector similarity alone is an inadequate recall policy; production memory systems combine it with keyword/lexical search, graph traversal, or outcome weighting.

Support: **7** talk(s)

> "when we increased it to like 400k tokens it was not able to facts that were buried in the middle and it started giving us like 0% recall whereas uh you know something like BM25 it still got 100% every time."
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [58:58](https://www.youtube.com/watch?v=WP3hjUXd918&t=3538s)

Supporting talks: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)

### Model capability is no longer the binding constraint on agent usefulness; the absence of persistent, environment-specific memory is — which currently forces the human to act as the system's memory layer.

Support: **7** talk(s)

> "Second is amnesia. Agent forget the work. Every session start with a blank slate. The human becomes the memory in this case."
>
> — [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [2:41](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=161s)

Supporting talks: [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md)

### Recall policy is a cost lever, not only an accuracy lever: speculative loading and bad retrieval directly inflate token spend, while a good structural recall policy reduces it.

Support: **5** talk(s)

> "bad memory is expensive because it spends more token and it can send the agent the wrong way. But having like a good structural policy for recall can save you a lot of tokens and uh budget."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [9:10](https://www.youtube.com/watch?v=R3-anFK1YM8&t=550s)

Supporting talks: [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)

### Correction and outcome events are first-class memory writes: human corrections should take precedence over model-derived facts, and eval/feedback signal must be routed back into memory rather than dying in a dashboard.

Support: **5** talk(s)

> "All of these events need to be captured, logged, and used to update your data agent context."
>
> — [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [6:54](https://www.youtube.com/watch?v=B8l81jhvHbI&t=414s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)

## Disagreements

### Should agents compact or summarize conversation history by default, or preserve it and recover context another way?

| Position A | Position B |
|---|---|
| Do not compact. Compaction is lossy and destructive — what it discards is gone, it invalidates the prompt cache, and keeping the full history wins on recall, cost, and latency simultaneously. Prefer an append-only log the model can fetch back from, or clear context entirely and re-read self-written handoff files.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* | Compaction works and should be the default. Rolling summarization plus a truncated recent window beat always stuffing the latest messages, compaction is now good enough to keep five-week-old threads with 400 sub-agents coherent, and relevance-scored knowledge-based compaction saves substantially more tokens than naive approaches.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)* |

*Why it matters: This decides whether you build a summarizer and tune its presets or build an append-only session store plus a fetch-back tool — opposite engineering investments — and it determines whether prompt-cache economics (97% cached tokens making the largest-context setup the cheapest) work for or against you.*

### Is a purpose-built memory system worth building, or does keeping everything in context already match it?

| Position A | Position B |
|---|---|
| Engineered memory systems underperform the naive baseline. Vanilla in-context learning topped Continual Learning Bench on reward and held across the reward-vs-cost and gain-vs-cost Pareto frontiers; an unmodified RLM harness scores like a top-10 memory system; and when the task and its context fit the window, a memory harness adds cost and zero capability.<br>*[Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)* | Structured memory produces measurable gains that context stuffing does not. Outcome-weighted retrieval moved tau-bench policy-following from 66% to 76% (80% with consolidation to skills); episodic memory made 15% of flip-flopping security alerts consistent; a rank-only decisions ledger beat vector RAG and gating on long-horizon recall; graph traversal surfaced actionable answers a vector store on identical data missed.<br>*[User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* |

*Why it matters: It determines whether memory engineering is a real capability investment or premature optimization — and the sides may only be reconcilable by task horizon, since the pro-memory results come from tasks whose evidence sits outside the window while the anti-memory results come from medium-horizon tasks that still fit.*

### Is plain markdown-on-disk an adequate memory substrate, or does it break down and require a structured graph or precomputed model?

| Position A | Position B |
|---|---|
| Files are enough, and the substrate barely matters as long as it is highly programmable with simple primitives. A central Git repo of markdown beat reaching for a vector database for a fleet-wide performance pattern catalog; a personal research memory of 10,000 notes runs on markdown plus a reference index with no vector DB, knowledge graph, or semantic search; per-dataset markdown suffices as a shared agent/human knowledge base.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)* | File-based memory is a scale trap. Everything gets loaded speculatively (100k tokens per round), multi-hop chains are unreachable by similarity even when all the facts are stored, hand-maintained .md files cannot keep pace with changing enterprise definitions, and past the ~1M-token context window markdown memory is no longer viable — you need a graph or an offline-computed structured model.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)* |

*Why it matters: The two camps imply very different build costs and ceilings: files are a weekend of work with a hard scaling wall, while graphs and precomputed context models require an ingestion pipeline, entity extraction, and ongoing maintenance that only pays off above a corpus size most teams have not reached.*

### Should agents learn durably in the harness and memory layer, or in the model weights?

| Position A | Position B |
|---|---|
| Keep learning out of the weights. Agent continual learning is not necessarily fine-tuning — the cheapest durable change is usually at the memory or harness layer, harness engineering has a roughly two-minute feedback loop and satisfies most teams, augmenting with semantic and episodic memory matches fine-tuning at lower cost, and the running-profile loop already outside the weights is continual learning that has shipped.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)* | Non-parametric memory is a ceiling, not a solution. Building continual learning on already-trained frozen checkpoints is a sunk cost fallacy — the models were never designed to be continual learners, and architecture, data, and algorithms should be co-designed instead; per-user LoRA adapters over a shared memory layer enforce permissions and personalization that code-level access control cannot.<br>*[Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)* |

*Why it matters: If harness-layer memory is a stopgap, teams investing years in retrieval policies and consolidation passes are building infrastructure that a differently-trained model generation obsoletes; if it is the answer, weight-level continual learning is an expensive detour that only amortizes at enterprise scale.*

## Practical Guidance

**Do:**

- Back every session with an append-only event log stored outside the harness and the sandbox, so harness death or container death loses nothing and credentials never enter the sandbox.
- Run an out-of-band consolidation pass over transcripts plus current memory state (nightly or per-task), and confirm with evals in your own context that the offline compute is worth it.
- Let the model structure and maintain its own memory — prescribing an explicit memory schema measurably degrades performance.
- Pair dense retrieval with lexical/BM25 search: at 400k tokens dense recall on buried facts fell to 0% while BM25 held 100%.
- Score retrieved memories by whether they historically helped or hurt the outcome, and once roughly ten memories accumulate on a pattern, bake the reasoning into a skill so the operating instructions stay current.
- Measure the memory harness against a no-memory baseline before shipping it — when the task and its relevant context fit in the window, memory adds cost and no capability.
- Store memory as reasoning and decisions ("check settlement before issuing a refund"), not context-free user facts.
- When stored facts conflict, make human corrections permanently win over model-derived facts, and log correction events back into agent context.
- Keep hand-authored source notes immutable and write all model-generated content into a separate derivative layer the agent may edit.
- Structure the recall path hierarchically (index → summary → derivative → raw source) so consulting the catalog does not fill the context window.
- Separate verification into its own context window — self-grading in the context that produced the work causes confabulation.
- Instrument per-turn logging (tokens, cache hits, cost, TTFT, tool calls) — it is cheap and most teams skip it.

**Avoid:**

- Compacting by default: name the specific constraint forcing it (a window too small for caching to apply) before reaching for summarization, since summarization invalidates the prompt cache and needs >50x compression to pay off.
- Aggressively clearing old tool outputs — the agent re-retrieves what it already had and total cost rises.
- Speculatively loading the whole memory store every round; one practitioner measured at least 100k tokens per turn from markdown-file memory alone.
- Exposing memory mutation as MCP tools the agent can call freely — you are one `forget` call away from wiping your own memory.
- Planning on append-only memory files plus search as the long-term architecture; humans are not append-only logs and entries must be updated and compressed to survive multi-year timescales.
- Treating LLM self-reported uncertainty as the signal for routing cases to human review; use disagreement across runs or across models instead.
- Giving each agent its own memory system — it produces context sprawl, separate and divergent learning, and no single version of truth.
- Trapping memory inside a specific agent framework, since teams churn frameworks roughly annually and the context is lost at each migration.
- Putting long-term memory in a latency-critical path — it is incompatible with a sub-500ms transaction SLA.
- Assuming a bigger model, a longer context window, or more knowledge bases will fix bad answers caused by missing source-of-truth ranking.

## Notable Outliers

- Keeping the full conversation history untouched beat every compaction preset simultaneously on memory recall, cost, and latency — and distinctive facts stayed reliably recallable up to 800k tokens with no compaction at all, because 97% of tokens were cached. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s))
- A structured log used directly as memory — no semantic ingestion, no fact extraction, no entity extraction, just embed the query, grab neighboring messages, fit the window — performed well on LongMemEval. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [8:17](https://www.youtube.com/watch?v=khVX_BUnEwU&t=497s))
- Oracle retrieval does not reach maximum task performance: handing the model the correct memory does not make it use the memory, so recall policy and utilization are separate failure modes. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s))
- Memory design is a compute allocation problem with no right answer — ChatGPT runs a ~4,000-token profile updated every few days, Claude a ~1,000-token profile updated every 24 hours, the exact opposite tradeoff of serving cost against update cost. ([Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [13:18](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=798s))
- ChatGPT failing to notice contradictions in its own stored memories is a product problem, not a technology problem — nothing at the LLM level prevents solving it. ([Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [16:46](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1006s))
- Long-term memory is incompatible with a sub-500ms fraud-decision SLA, so the agent runs on short-term in-memory context over a precomputed semantic layer instead. ([Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [11:32](https://www.youtube.com/watch?v=o6U_2vd967Y&t=692s))
- An agent's identity is derived from its own event log the way human identity derives from lived experience rather than raw reasoning capability — so the harness will not disappear as models improve. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [16:36](https://www.youtube.com/watch?v=khVX_BUnEwU&t=996s))

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
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
- [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)
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
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Omar Solano](../speakers/omar-solano.md)
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
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Shlok Khemani](../speakers/shlok-khemani.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Stefania Druga](../speakers/stefania-druga.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Victor Savkin](../speakers/victor-savkin.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

