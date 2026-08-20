---
title: "agent memory"
type: "concept"
slug: "agent-memory"
tier: "core"
maturity: "contested"
talk_count: 40
speaker_count: 42
---

# agent memory

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **40** talk(s) by **42** speaker(s)

**Definition:** Persisting and recalling information across an agent's turns, sessions, or lifetime — storage substrate, write policy, and retrieval policy.

*Also referred to as: agent memory systems, agent memory architecture, persistent agent memory, episodic memory for agents, agent long-term memory, memory layering, external memory stores*

## State of Practice

The field has converged on one structural answer — durable agent state belongs outside the model, in an append-only session/event log or files on disk that survive compaction, container death, and harness restarts — and on one operational answer: writing memory in-band during a session is necessary but not sufficient, so leading systems run a periodic offline consolidation pass (Anthropic's "dreaming", nightly sleep cycles, profile refresh loops) to correct locally-optimal or contradictory memories. Beyond that, almost everything is contested. Substrate choices range from plain markdown in a git repo (Netflix, Sakana, DataChain) to property graphs (Neo4j, TwelveLabs) to enterprise databases and semantic layers (Onlay, Tesla), with credible measurements on both sides. The most uncomfortable results of the conference were negative ones: vanilla in-context learning topped Continual Learning Bench over sophisticated context-management systems, keeping the full conversation untouched beat every compaction preset on recall, cost, and latency simultaneously, and oracle retrieval — handing the agent exactly the right memory — still did not reach maximum task performance, because the model can ignore what it is given. Practitioners increasingly treat recall policy as a cost lever rather than an accuracy lever, and treat siloed per-agent memory as an architectural error: memory that does not cross developer, product, and org boundaries is a bottleneck rather than an asset. Retrieval by embedding similarity alone is now widely regarded as inadequate; hybrid lexical+dense, graph traversal from vector seed nodes, and outcome-weighted (utility-scored) ranking are the replacements being tried.

## Consensus

### Durable agent state must live outside the model's context window — in an append-only event log or files on disk — so the work survives context wipes, compaction, and machine or container crashes.

Support: **6** talk(s)

> "The state lives in files. It is not trapped inside one model. And this is the single most practical thing I learned all year."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)

### In-band memory writing during a session is insufficient; a periodic out-of-band consolidation pass over transcripts plus current memory state is required to correct wrong or only-locally-optimal memories.

Support: **4** talk(s)

> "those mistakes get stuck in memory unless you have an offline process to kind of correct them"
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [15:40](https://www.youtube.com/watch?v=9QebvrrY3KY&t=940s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)

### Vector/semantic similarity alone is an inadequate recall policy; production memory requires hybrid lexical retrieval, graph traversal, or outcome-weighted ranking on top of embeddings.

Support: **6** talk(s)

> "the challenge here is similar what what vectors give you, which is similarity in vector space, is not the same as actual relationships."
>
> — [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [7:57](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=477s)

Supporting talks: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)

### Memory scoped per-agent, per-developer, or per-product is an architectural error; the substrate should be shared across the org, the fleet, and multiple agent products.

Support: **6** talk(s)

> "agents all had their own memory systems to a certain extent. So, they were learning They were all learning separately and they were learning differently."
>
> — [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [9:53](https://www.youtube.com/watch?v=8G_1-3IO4ZQ&t=593s)

Supporting talks: [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)

### Memory-layer updates are the cheapest place to change agent behavior and are therefore the layer most often shipped unverified, so writes need explicit gating, conflict resolution, or regression checks.

Support: **5** talk(s)

> "So, this layer in terms of the update is cheapest and fastest. It works directly on the cases where you only have log and feedback, but usually it is unverified"
>
> — [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [9:50](https://www.youtube.com/watch?v=2IxD9OB3XuQ&t=590s)

Supporting talks: [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)

### Recall policy is a cost lever, not only an accuracy lever: bad memory burns tokens by triggering re-retrieval and wrong turns, while a good structural recall policy reduces total spend.

Support: **4** talk(s)

> "bad memory is expensive because it spends more token and it can send the agent the wrong way. But having like a good structural policy for recall can save you a lot of tokens and uh budget."
>
> — [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [9:10](https://www.youtube.com/watch?v=R3-anFK1YM8&t=550s)

Supporting talks: [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

## Disagreements

### Should an agent compact or summarize its conversation history, or retain it verbatim and reset instead?

| Position A | Position B |
|---|---|
| Do not compact by default. Compaction is lossy and destructive, it invalidates the prompt cache (you must compress >50x to break even), and keeping the full untouched history beat every compaction preset simultaneously on recall, cost, and latency. When context must be shed, clear entirely and re-read self-written handoff files, or deterministically allocate a fresh context each iteration.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* | Compaction and rolling summarization work and should be the default path. Rolling summarization plus a truncated recent window outperformed always stuffing the latest messages, compaction is now good enough that five-week-old threads with 400 sub-agents stay coherent, and knowledge-based compaction driven by a continually adapting relevance scorer saves substantially more tokens than naive approaches.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)* |

*Why it matters: This decides whether you invest in summarization machinery and per-turn context budgets, or in cheap durable storage plus cache-friendly append-only prompts — and the two architectures have opposite cost curves, since one pays to shrink context while the other pays to keep it cached.*

### What substrate should agent memory use — plain markdown files, or a structured store such as a graph, database, or semantic layer?

| Position A | Position B |
|---|---|
| Plain markdown in a central git repo with a reference index is enough; skip vector databases, knowledge graphs, and semantic search. The substrate choice matters far less than whether it is highly programmable with simple primitives, and structured stores cost more to set up for a tie on results.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)* | Markdown memory is speculatively loaded (100k+ tokens per round) and stops working once data exceeds the million-token window; multi-hop reasoning chains cannot be resolved by similarity over files at all. Enterprise and video workloads need a graph, database, or ranked semantic layer with explicit relationships and provenance.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)* |

*Why it matters: The file-based camp can ship memory in an afternoon and audit it in a text editor; the structured camp requires an ingestion pipeline, entity extraction, and a query layer. Choosing wrong either caps you at small scale or spends months of infrastructure work you did not need.*

### Does an engineered memory harness actually beat simply keeping everything in the context window?

| Position A | Position B |
|---|---|
| Not until the task genuinely overflows the window. A memory harness added zero capability and only cost when the task and its context fit; vanilla in-context learning topped the Continual Learning Bench leaderboard on reward and held across both reward-vs-cost and gain-vs-cost Pareto frontiers, beating more expensive context-management systems; and distinctive facts were recalled reliably up to 800k tokens with no compaction at all.<br>*[Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)* | Engineered memory produces measurable wins that raw context does not. Outcome-weighted retrieval lifted tau-bench policy-following from 66% to 76% and to 80% when consolidated into skills; episodic memory made 15% of previously flip-flopping cybersecurity verdicts consistent; and a graph store returned precise actionable answers where a vector store on identical data did not.<br>*[User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)* |

*Why it matters: If memory only pays off past the context window, most teams should ship nothing and revisit at 1M tokens; if it pays off inside the window, the benchmark results above mean teams shipping raw context are leaving 10-14 accuracy points on the table.*

### Should the memory store hold the raw interaction log, or distilled facts and profiles extracted from it?

| Position A | Position B |
|---|---|
| Keep the log raw. A structured log used directly as memory — no semantic ingestion, no fact extraction, no entity extraction, just embedding the query and grabbing neighboring messages — performed well on LongMemEval, and prescriptive memory schemas measurably degrade performance versus letting the model manage its own memory.<br>*[Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)* | Extract and curate. Atomic fact extraction beats storing everything and compacting on overflow; memory should encode task reasoning rather than context-free facts; a salience gate should decide what is even worth remembering; and the leading consumer systems maintain dense running profiles (~1k-4k tokens) rather than searchable raw history.<br>*[Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)* |

*Why it matters: Extraction adds a write-time compute bill and a whole class of extraction errors that are invisible until retrieval fails; raw logs push all the cost and risk to read time. The two also fail differently — extraction loses nuance permanently, raw logs lose the ability to notice contradictions.*

### Can memory- and harness-layer updates substitute for changing model weights, or is external memory a workaround for models that were never designed to learn?

| Position A | Position B |
|---|---|
| Memory and harness updates are sufficient for most real improvement. Continual learning is not necessarily fine-tuning — many useful updates happen in the harness and memory layers; augmenting an agent with semantic and episodic memory is cheaper and easier to iterate on than fine-tuning with comparable gains; and the running-profile loop already deployed in ChatGPT and Claude is continual learning operating outside the weights.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Why Your Agent Disagrees With Itself (And What To Do About It)](../talks/why-your-agent-disagrees-with-itself-and-what-to-do-about-it.md), [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)* | Building continual learning on top of frozen checkpoints is a sunk cost fallacy — these models were never designed to be continual learners, and parametric approaches that co-design architecture, data, and algorithms are more promising. In practice, base models tuned on narrow vertical tasks match and exceed frontier models on those tasks at one to two orders of magnitude lower cost.<br>*[Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)* |

*Why it matters: It determines whether a team's continual-learning roadmap is a retrieval and consolidation problem solvable with today's APIs, or a training-infrastructure problem requiring traces, GPUs, and a fine-tuning pipeline.*

## Practical Guidance

**Do:**

- Keep the session as an append-only event log that lives outside both the harness process and the sandbox container, so a harness or sandbox death loses nothing and credentials are never in the sandbox at all.
- Run an offline consolidation pass over the day's transcripts plus current memory state on a fixed cadence (Claude's profile updates every 24 hours; ChatGPT's every few days) and validate the offline compute cost with evals in your own context.
- Measure the memory harness against a no-memory baseline before shipping it — if the task and its relevant context fit in the window, the harness adds cost and no capability.
- Treat recall policy as a first-class metric alongside accuracy and cost, reported on Pareto frontiers rather than as a single number.
- Pair dense retrieval with BM25 keyword search: at 400k tokens dense recall dropped to 0% on facts buried in the middle while BM25 held 100%.
- Let the model structure and maintain its own memory rather than imposing a schema — prescribed memory structures measurably drop performance.
- Make human corrections permanently outrank model-derived facts when two stored facts disagree, and gate what enters memory with an explicit salience check.
- Weight retrieval by whether a memory historically helped or hurt the outcome (a utility score), and after roughly ten accumulated memories bake the reasoning into skills so the operating instructions stay current.
- Keep the shared pattern/knowledge catalog centralized and hierarchically indexed so consulting it does not fill the agent's context window.
- Separate immutable human-authored notes from an LLM-writable derivative layer — the agent reads your notes, it never writes to them.
- Select cases for human review by cross-run or cross-model disagreement rather than by the model's self-reported uncertainty.
- Verify each memory update against accumulated past learning environments, treating regression prevention as part of the optimization objective rather than a post-hoc check.

**Avoid:**

- Compacting by default — name the specific constraint forcing it (e.g. the conversation no longer fits the window so caching stops helping) before you reach for it.
- Aggressively clearing old tool outputs: the agent re-retrieves information it already had, raising total cost rather than lowering it.
- Speculatively loading the whole markdown memory each turn — one practitioner measured 100k tokens per round loaded on the chance something is useful.
- Exposing memory management through MCP tools that include a forget command, which puts the agent one call away from wiping its own memory.
- Assuming that supplying the correct memory means the agent will use it — oracle retrieval still did not reach maximum task performance.
- Self-grading memory or work in the same context window that produced it; verification belongs in a separate, separately tuned context.
- Relying on long-term memory under a hard latency SLA (a sub-500ms transaction path needs short-term in-memory context instead).
- Treating an append-only memory file with search over it as the long-term plan — it will not scale to agents working with humans over multi-year timescales.
- Outsourcing memory to a third-party provider if you are a serious product team; every top consumer AI product builds it in-house and evolves it with the product.
- Shipping persistent cross-session memory without a way for users to break out of it, since it biases the agent toward repeating yesterday's action.
- Assuming a bigger model, a longer context window, or more knowledge bases will fix bad answers that are actually caused by an unranked, unprioritized memory layer.

## Notable Outliers

- Memory is a compute allocation problem: ChatGPT runs a ~4,000-token profile updated every few days (high serving cost, low update cost) while Claude runs a ~1,000-token profile updated every 24 hours — the exact opposite tradeoff on the same axis. ([Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [13:18](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=798s))
- A structured log used directly as memory — no semantic ingestion, no fact extraction, no entity extraction, just embedding the query and grabbing a couple of messages before and after — did well on LongMemEval. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [8:17](https://www.youtube.com/watch?v=khVX_BUnEwU&t=497s))
- Oracle retrieval does not reach maximum task performance: given the right memory, the model can still retrieve the wrong information from it, ignore it, or be confused by it. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s))
- Vanilla in-context learning topped Continual Learning Bench 1.0 over purpose-built context-management systems, and held across both the reward-vs-cost and gain-vs-cost Pareto frontiers. ([Beyond Static Intelligence: Evaluating Continual Learning](../talks/beyond-static-intelligence-evaluating-continual-learning.md), [14:16](https://www.youtube.com/watch?v=iqloyWCGYQQ&t=856s))
- Permissions over shared group memory should be enforced with per-user LoRA adapters rather than in code — baking access control into the weights instead of the retrieval layer. ([Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [17:12](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=1032s))
- The failure of memory systems to notice that two stored facts contradict each other is a product problem, not a technology problem — nothing at the LLM level prevents solving it. ([Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [16:46](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1006s))

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
- [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)
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
- [Vasant Kearney](../speakers/vasant-kearney.md)
- [Victor Savkin](../speakers/victor-savkin.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

