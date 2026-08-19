---
title: "context window management"
type: "concept"
slug: "context-window-management"
tier: "core"
maturity: "consolidating"
talk_count: 19
speaker_count: 19
---

# context window management

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **19** talk(s) by **19** speaker(s)

**Definition:** Budgeting and allocating a finite context window across system prompt, tools, history, and retrieved material, including policies for what gets evicted when the budget is exceeded.

*Also referred to as: context window budgeting, context budgeting, context token budgeting, context management, sliding window context, context window limits, context exhaustion*

## State of Practice

The field has stopped treating context length as headroom to be filled and started treating it as a budget with a usable ceiling far below the advertised limit. Speakers converged on a working set well under 100K tokens even on million-token models, on the grounds that quality degrades from attention dilution long before the hard limit — the 100-tool benchmark put tool-selection accuracy at ~78% with 10 tools and 13.6% at 741, and a 741-tool catalog at ~127K tokens of schema on every single request. The dominant technique is just-in-time loading over speculative preloading: a thin index in the first prompt (20–25K baseline, with 40–50K read as a failure of progressive disclosure), skill files capped at 100–500 lines with detail deferred to linked files, and tool schemas retrieved per-request (K≈5) rather than statically mounted. The second technique is externalization: large tool outputs, logs, time-series, and combinatorial state never enter the main context — they live in a file system, a REPL, a graph, or a sub-agent, and only summaries or top-K truncations cross back. Where the field is still arguing is what sits behind the window — a semantic/graph index versus plain markdown the agent navigates with bash — and whether an overflowing context should be compacted or thrown away and rebuilt. Cost pressure sharpens all of this: several speakers reported token prices rising in 2026, so context frugality is now an economic argument, not just a quality one.

## Consensus

### The context window degrades in quality well before it hits its token limit, so the working set must be kept small regardless of how large the window is.

Support: **6** talk(s)

> "The problem here is that the context window is limited, and if you fill the context window too much, the quality of the answer gets degraded, too."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:12](https://www.youtube.com/watch?v=XovaGv4f39A&t=192s)

Supporting talks: [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)

### Context should be loaded just-in-time behind a thin index rather than speculatively front-loaded in the hope something proves useful.

Support: **6** talk(s)

> "they they basically load up everything in the hopes that something will be useful in the context. At small scale that works where you get the results you want with a high quality model. It doesn't work at large scale"
>
> — [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [3:32](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=212s)

Supporting talks: [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)

### Large tool outputs must be stored outside the context and returned as truncations, summaries, or fixed-size renderings rather than piped in raw.

Support: **5** talk(s)

> "Raw time series metrics are not context window friendly. Simply feeding the raw data to an LLM works in the small scale, but fails for long-running jobs in production. Not to mention, it's horribly token inefficient."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [6:44](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=404s)

Supporting talks: [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Respect The Process](../talks/respect-the-process.md)

### Give the model tools and an execution environment to assemble its own context, instead of the harness deciding up front what to stuff in.

Support: **5** talk(s)

> "if you give it arms, like you give it the bash tool and ways to work with the environment, it can build and search its own context. And that's sort of like the insight that led to Claude Code"
>
> — [Field Guide to Fable](../talks/field-guide-to-fable.md), [5:14](https://www.youtube.com/watch?v=9fubhllmsBU&t=314s)

Supporting talks: [Field Guide to Fable](../talks/field-guide-to-fable.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [Respect The Process](../talks/respect-the-process.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### Sub-agents with isolated contexts that return only summaries are the primary mechanism for keeping the parent context healthy on long tasks.

Support: **3** talk(s)

> "Our sub agent would summarize its findings and return the results back to the parent agent, thereby ensuring the context window is kept healthy."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s)

Supporting talks: [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

### Context should be laid out so the prefix is stable across requests, because caching the invariant head is the cheapest available latency and cost win.

Support: **3** talk(s)

> "if the beginning of the context you send to the model is the same each time, then you can get up to 90% cheaper, faster inference um depending on the conditions."
>
> — [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [11:22](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=682s)

Supporting talks: [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

## Disagreements

### When the budget is exceeded, should the existing context be compacted, or discarded and rebuilt from scratch?

| Position A | Position B |
|---|---|
| Compaction is lossy and degrades fidelity; deterministically re-allocate a fresh context each iteration rather than summarizing the old one forward.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* | Summarize what falls out of the window and inject the summary back — sliding-window trimming plus summarization of the dropped history, and sub-agents that hand summarized findings to the parent, are the standard mitigation.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)* |

*Why it matters: If compaction is fundamentally lossy, long-horizon agents need deterministic re-seeding from durable artifacts (files, specs, task lists) and the whole auto-compact path is a bug rather than a feature; if summarization is adequate, the engineering effort goes into better summarizers instead.*

### What should hold the knowledge that does not fit in the window — a structured index (vector or graph) or plain files the agent navigates itself?

| Position A | Position B |
|---|---|
| A structured retrieval layer is required at scale: markdown-file memory wastes tokens and stops working past the 1M-token mark, vector seeds plus graph traversal give precise and auditable context, and semantic retrieval over tool descriptions is what keeps the working set small.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)* | Skip vector databases, knowledge graphs, and semantic search; a hierarchy of plain markdown files plus a reference index the agent reads with ordinary file and shell tools is more token-efficient, inspectable, and owned by you.<br>*[Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)* |

*Why it matters: This decides whether teams stand up and maintain retrieval infrastructure with its own indexing, staleness, and eval burden, or invest instead in file layout, naming, and progressive-disclosure conventions the agent traverses at inference time.*

### When every document in a corpus may be relevant, should you retrieve a subset or load the whole corpus into cached context?

| Position A | Position B |
|---|---|
| Thresholded similarity retrieval cannot return a whole collection; load all documents into parallel KV-cached context buckets and let a supervisor interrogate the buckets, which builds knowledge faster than GraphRAG and answers more accurately than simple RAG.<br>*[When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* | The gap is a retrieval-quality problem, not a capacity problem — swapping in better search closes most of the distance to oracle performance without touching the reasoning model or expanding what is loaded.<br>*[How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)* |

*Why it matters: One path spends money on cache residency and large-window inference per query; the other spends it on embedding/ranking quality and agent search training, and the two lead to entirely different serving cost curves as the corpus grows.*

## Practical Guidance

**Do:**

- Target roughly 20–25K tokens of baseline context in the first prompt; treat 40–50K as evidence that progressive disclosure has failed
- Keep working context under ~100K tokens even on million-token models, and under ~60K for the hardest problems
- Cap skill.md at ~100 lines (a skill is a folder) and keep SKILL/skills.md files under 500 lines, deferring detail to linked files
- Past ~50 tools in production, retrieve tool schemas just-in-time with a semantic router at K≈5; under 20 tools, just load them statically
- Give the agent two log tools — top-K truncated exceptions and full detail for one exception — instead of letting it read logs directly
- Render time-series metrics as images so input token count is fixed regardless of job duration
- Keep the first ~90% of the context identical request-to-request so prefix caching applies; cache the system prompt and, where possible, tool definitions and messages
- Push exploratory work into sub-agents or a separate REPL/execution environment and return only summaries to the parent context
- Always set a max-iteration cap on the tool loop, and run observability over tool calls before production to find repeated calls and oversized payloads
- Instruct search tools to write 'one concise sentence describing what it wants to find' rather than 'write a search query', to avoid keyword-stuffed BM25-style queries
- Delete no-ops from instruction files — they save tokens even when eval scores are unchanged

**Avoid:**

- Loading all memory or documentation files every round on the chance something is useful — one speaker measured ~100K tokens per round from markdown-file memory alone
- Packing hundreds of tool schemas into one prompt: 741 tools costs ~127K tokens per request and drops tool-selection accuracy to 13.6%, and pushes time-to-first-token past 5 seconds around 500 tools
- Holding large combinatorial state (e.g. a seating arrangement for 800 people) in the context window instead of in deterministic compute
- Resending the full conversation history and full tool results on every loop iteration
- Letting auto-compaction be the budget policy — silently blowing through 500K–1M tokens on a task that did not need it
- Bucketing documents by domain for a supervisor to select from: with dense inter-document relationships the supervisor skips domains that look irrelevant at first glance
- Writing long negative-constraint and example-heavy system prompts for the newest models — examples constrain a model more imaginative than the examples, and 80% of the Claude Code system prompt was removed
- Exposing memory as raw MCP tools without guarding destructive commands — the agent is one call away from wiping its own memory

## Notable Outliers

- Long agent runtimes and heavy token spend are good, not bad — under the reasoning paradigm the longer the agent thinks the better the output — even while the same talk treats silent context burn as a defect. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [12:20](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=740s))
- Forget the infrastructure you think you need — no vector databases, no knowledge graphs, no semantic search, no text search; just a simple index based on references over markdown files. ([Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [19:04](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1144s))
- Abstracting payment, negotiation, and execution behind a single protocol is itself a context-management technique: the agent sees a few services instead of the underlying protocols. ([Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [17:48](https://www.youtube.com/watch?v=Fu45geO3zX8&t=1068s))
- Loading skills, MCP servers, and tools into one agent's context is functionally inheritance, and like inheritance it hits diminishing returns and breaks down — the fix is composition into narrow agents that talk to each other in plain English. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [12:45](https://www.youtube.com/watch?v=spNAUEgq_A8&t=765s))
- The cost of intelligence reversed in 2026 — tokens are up 76% raw and 29% IQ-adjusted at the halfway point of the year — making context frugality an economic requirement, not an optimization. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [22:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1357s))

## All Talks

- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)
- [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)
- [Respect The Process](../talks/respect-the-process.md)
- [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)
- [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)
- [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)
- [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)
- [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)
- [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)
- [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)
- [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)
- [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Allen Pike](../speakers/allen-pike.md)
- [Andrew Dumit](../speakers/andrew-dumit.md)
- [Ankush Rastogi](../speakers/ankush-rastogi.md)
- [Armanas Povilionis](../speakers/armanas-povilionis.md)
- [Dat Ngo](../speakers/dat-ngo.md)
- [Drasko Profirovic](../speakers/drasko-profirovic.md)
- [Erik Hanchett](../speakers/erik-hanchett.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Paul Iusztin](../speakers/paul-iusztin.md)
- [Philipp Schmid](../speakers/philipp-schmid.md)
- [Shashi](../speakers/shashi.md)
- [Shlok Khemani](../speakers/shlok-khemani.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)

