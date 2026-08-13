---
title: "context window management"
type: "concept"
slug: "context-window-management"
tier: "core"
maturity: "consolidating"
talk_count: 18
speaker_count: 18
---

# context window management

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **18** talk(s) by **18** speaker(s)

**Definition:** Budgeting and allocating a finite context window across system prompt, tools, history, and retrieved material, including policies for what gets evicted when the budget is exceeded.

*Also referred to as: context window budgeting, context budgeting, context token budgeting, context management, sliding window context, context window limits, context exhaustion*

## State of Practice

The field has stopped treating the context window as storage and started treating it as a scarce working set with an explicit budget. The dominant pattern is progressive disclosure: keep a thin index in the first prompt, externalize everything else to a file system, graph, vector store, or a separate execution environment, and pull material in just-in-time — Prosodica measured tool-selection accuracy collapsing from ~78% at 10 tools to 13.6% at 741 tools (127k tokens of schemas alone), recovered to >83% by retrieving K≈5 tools per request. Speakers now cite hard numbers rather than principles: 20-25k tokens of baseline context per first prompt with 40-50k treated as a failure, working context under ~100k even on million-token models (under 60k for hard problems), skill.md capped at 100 lines or skills.md at 500. Large tool outputs are the main leak, and the standard fixes are sub-agent summarization, top-K truncated results with a drill-down tool, and rendering time-series as images so token cost is fixed regardless of job duration. Prefix/prompt caching is treated as settled engineering hygiene (up to 90% cheaper when the first 90% of context is stable). What remains genuinely open is the substrate for the externalized material — plain markdown files versus graph memory versus parallel KV-cached full-document buckets — and whether the model should curate its own context by writing code, or the harness should decide what it is allowed to see.

## Consensus

### Load context just-in-time rather than speculatively: keep the resident set small and defer detail to files, indexes, or tools the agent can pull from on demand.

Support: **7** talk(s)

> "This is the core lesson from the benchmark. The catalog can grow, but the model's working set should stay small."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [15:32](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=932s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### Filling the context window degrades output quality well before the hard token limit, so bigger context windows do not remove the need to budget.

Support: **7** talk(s)

> "The problem here is that the context window is limited, and if you fill the context window too much, the quality of the answer gets degraded, too."
>
> — [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:12](https://www.youtube.com/watch?v=XovaGv4f39A&t=192s)

Supporting talks: [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)

### Raw tool output must never flow straight into the main agent's context; it should be stored externally and returned as a summary, a truncated top-K, or a fixed-size rendering.

Support: **5** talk(s)

> "Our sub agent would summarize its findings and return the results back to the parent agent, thereby ensuring the context window is kept healthy."
>
> — [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s)

Supporting talks: [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)

### Context budgets should be expressed as concrete numeric caps on individual artifacts (system prompt, skill files, tool schemas, resident tokens), not as a vague instruction to be economical.

Support: **4** talk(s)

> "I think like 20, 25K tokens get taken anyway, but like how much more is getting added? If you're coming to like 40K, 50K, like something's wrong. That's not really progressive disclosure."
>
> — [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [15:57](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=957s)

Supporting talks: [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)

### Structure the context so the prefix is byte-stable across calls and cache it; the savings are large enough to be an architectural constraint on how context is ordered.

Support: **3** talk(s)

> "if the beginning of the context you send to the model is the same each time, then you can get up to 90% cheaper, faster inference um depending on the conditions."
>
> — [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [11:22](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=682s)

Supporting talks: [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

## Disagreements

### Who should decide what enters the context window — the model, by writing code and searching its own environment, or the harness, by routing and pre-filtering what the model is allowed to see?

| Position A | Position B |
|---|---|
| Give the model general-purpose arms (bash, a REPL, a coding agent over the data) and let it build and curate its own context; purpose-built tool calls scale worse than an agent that can write loops and summarization scripts.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [Respect The Process](../talks/respect-the-process.md)* | The harness must decide: retrieve a small relevant tool/document set per request, replace direct log or corpus access with constrained tools, and train or instruct the search layer, because agents left to their own devices write bad queries and drown themselves in output.<br>*[The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)* |

*Why it matters: It determines whether you invest in sandboxes and code-execution primitives or in retrieval infrastructure and routers, and it sets whether context cost is bounded by construction or only observed after the fact.*

### What substrate should hold the material that has been pushed out of the context window?

| Position A | Position B |
|---|---|
| Plain markdown files plus a hand-curated reference index; explicitly skip vector databases, knowledge graphs, and semantic search, and invest instead in curation, provenance, and pruning of a file-based brain.<br>*[Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* | File-based memory is a token sink that stops working at scale; use a structured store — vector-seeded graph traversal, or parallel KV-cached document buckets — so retrieval is precise, auditable, and does not require re-reading.<br>*[CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)* |

*Why it matters: One camp reports agents loading 100k tokens per round from markdown and calls it unviable past ~1M tokens of corpus; the other reports token-efficient traversal of a plain index. Picking wrong means either premature graph infrastructure or a memory layer that silently burns the entire budget every turn.*

### When history exceeds the budget, should it be summarized into the context or discarded in favor of a freshly allocated context?

| Position A | Position B |
|---|---|
| Trim the window and summarize what falls out back into context (sliding-window plus summarization; sub-agents returning condensed findings to the parent) so continuity is preserved.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)* | Compaction is a lossy operation that degrades fidelity; deterministically re-allocating a fresh context each iteration beats compacting, and hitting auto-compact on an ordinary task is itself a defect signal.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* |

*Why it matters: It decides whether long-running loops are engineered around a single growing session or around short, disposable sessions with state carried in files — a difference in harness design, not a tuning knob.*

## Practical Guidance

**Do:**

- Target ~20-25k tokens of baseline context on the first prompt and treat 40-50k as evidence that progressive disclosure has failed
- Keep working context under ~100k tokens even on million-token models; ~200k is the upper revision and under 60k is right for the hardest problems
- Cap skill.md at ~100 lines and treat a skill as a folder with detail in linked files; keep skills.md under 500 lines
- Retrieve tools per request instead of loading the catalog: static loading is fine below 20 tools, use a semantic router past 50, start at K=5 and run the test set at K=3/5/10 to pick the smallest K that hits your accuracy target
- Replace direct log consumption with two tools — top-K truncated exceptions and full detail for one specific exception
- Render time-series metrics as images so input token count is fixed regardless of job duration
- Delegate to sub-agents that summarize and return findings, rather than returning raw output to the parent
- Cache the system prompt and, where possible, tool definitions and messages; keep the first ~90% of context identical request to request
- Always set a max-iteration cap on tool loops, and run observability over tool calls before shipping to production
- Instruct search tools to write 'one concise sentence describing what it wants to find' instead of 'write a search query', and cap the search loop at four rounds with parallel searches inside each round
- Keep large combinatorial state (e.g. an 800-person seating arrangement) in deterministic compute, out of the context window
- Layer memory as index → executive summary → derivative wiki → raw source so the agent can stop at the cheapest sufficient level
- Run evals both with and without a skill loaded, and strip no-op instructions even when they do not change eval scores

**Avoid:**

- Speculative loading of all memory files every round in the hope something is useful — one speaker measured 100k tokens per round from markdown memory
- Packing hundreds of tool schemas into every request: 741 tools costs ~127k tokens per call and drops selection accuracy to 13.6% via lost-in-the-middle
- Feeding raw time-series or raw logs directly to the model; it works at small scale and fails on long-running production jobs
- Filling the context window as full as it will go, or routinely blowing through 500k-1M tokens and hitting auto-compact on tasks that are not complicated
- Bucketing documents by domain and letting a supervisor pick buckets — with dense cross-document relationships it skips domains that look irrelevant at first glance; distribute in no particular order instead
- Sliding-window trimming without summarizing the dropped prefix back into context
- Writing 'do not do this' negative instructions where context would do, and padding the system prompt with examples that constrain a more imaginative model
- Installing many skills, MCP servers, and tools into one agent's context — it is inheritance, and it degrades performance measurably
- Recomputing a knowledge graph on every corpus replacement when the underlying data changes frequently

## Notable Outliers

- Keep agent context under roughly 100,000 tokens even with million-token context windows; ~200k is the upper revision, and under 60k is right for the hardest problems. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [28:31](https://www.youtube.com/watch?v=c35YoMdnI78&t=1711s))
- Render Spark metrics as images rather than raw series, because images guarantee a fixed input token count for any job irrespective of its duration. ([Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [7:31](https://www.youtube.com/watch?v=0RNNfxpdbQk&t=451s))
- Forget vector databases, knowledge graphs, and semantic search for a personal research memory — plain markdown plus a simple reference index is enough. ([Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [19:04](https://www.youtube.com/watch?v=ZRM_TfEZcIo&t=1144s))
- Anthropic removed 80% of the Claude Code system prompt, because the newest models perform better with less in-prompt constraint. ([Field Guide to Fable](../talks/field-guide-to-fable.md), [5:47](https://www.youtube.com/watch?v=9fubhllmsBU&t=347s))
- Ask the model for 'one concise sentence describing what it wants to find' to trick it out of the keyword-stuffed BM25 query pattern it was trained into. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [9:05](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=545s))
- The cost of intelligence reversed in 2026 — tokens are up 76% raw and 29% IQ-adjusted at the halfway point of the year — making context budgeting an economic constraint, not just a quality one. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [22:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1357s))

## All Talks

- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [Don't Ship Skills Without Evals](../talks/dont-ship-skills-without-evals.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
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
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)

