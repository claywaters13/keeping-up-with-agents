---
title: "long-context processing"
type: "concept"
slug: "long-context-processing"
tier: "supporting"
maturity: "consolidating"
talk_count: 6
speaker_count: 9
---

# long-context processing

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **6** talk(s) by **9** speaker(s)

**Definition:** Handling inputs far larger than a normal window — long-context architectures, sparse attention, and recursive decomposition over the input.

*Also referred to as: long context handling, long-context inference, recursive language models, recursive llm sub-calls, sparse attention, context window scaling limits, latent space compression*

## State of Practice

The field has largely stopped treating "long context" as a window-size problem and started treating it as a systems problem: the dominant answer at this conference was to keep the large artifact outside the model and let the model write code that inspects, slices, and summarizes it, then feed only the curated result into the main window. This is the Recursive Language Model (RLM) pattern — repo-as-data in a REPL, model-chosen decomposition into sub-calls, symbolic intermediate state — and it showed up independently in coding-agent harnesses, in a production data-center telemetry system, and (as a caution) in single-cell biology, where flattening structured records into token sequences underperforms. Practitioners reported concrete degradation curves rather than vibes: correctness falling from 80% at 64 entities to ~30% at 460,000, monorepo performance decaying as context grows, and a 300x token reduction (116M → 390K per validation pass) once context was made to scale with hierarchy depth instead of instance count. The counterweight is infrastructure: MiniMax/Together are betting on serving whole codebases at 500K–1M context with sparse attention, where the hard part becomes KV-cache management that looks like a distributed file system. The live argument is over control flow — whether the model should freely choose its own recursive decomposition, or whether the pipeline should be a bounded two-or-three-step plan-then-resolve with flat, predictable cost.

## Consensus

### Context management should be externalized into a programmable execution environment — the large artifact stays outside the window and the model writes code to curate what enters it.

Support: **3** talk(s)

> "Core thesis of the RLM is you need to externalize the context management into programmable execution environment."
>
> — [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [1:27](https://www.youtube.com/watch?v=8oyalrfwgjw&t=87s)

Supporting talks: [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)

### Naive in-context approaches degrade measurably as input size grows — this is a quantified failure curve, not a soft limit at the token count.

Support: **3** talk(s)

> "So, we got 80% correctness at 64 GPUs, and that dropped to about 30% when the GPU grew to 400 460,000."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [10:57](https://www.youtube.com/watch?v=EUsPvBeIx70&t=657s)

Supporting talks: [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md)

### Split the labor: the model plans and decomposes, deterministic code performs the exact traversal, enumeration, and set operations over the large input.

Support: **4** talk(s)

> "The second insight that we had was LLMs are good for planning but not good for searching."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [6:29](https://www.youtube.com/watch?v=EUsPvBeIx70&t=389s)

Supporting talks: [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [Recursive Coding Agents](../talks/recursive-coding-agents.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)

### Structured inputs (codebases, equipment hierarchies, single-cell matrices) should not be flattened into a token stream or compressed into a latent vector; the structure is the thing that makes long-context tractable.

Support: **3** talk(s)

> "If your data has structure, call it a hierarchy, graph, or a schema, a language model scanning it token by token is definitely the wrong tool."
>
> — [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:04](https://www.youtube.com/watch?v=EUsPvBeIx70&t=844s)

Supporting talks: [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [From Tokens to Cells: Foundation Models for Single-Cell Biology](../talks/from-tokens-to-cells-foundation-models-for-single-cell-biology.md)

## Disagreements

### Should the recursive decomposition be chosen freely by the model at runtime, or fixed as a bounded plan-then-resolve pipeline?

| Position A | Position B |
|---|---|
| The model itself must choose how to decompose the problem into sub-calls — a hardcoded map-reduce pipeline does not qualify as an RLM, and the harness should expose planning, coding, observation, and a sub-call budget for the model to drive.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)* | Use a two- or three-step plan-then-resolve pipeline instead of a multi-step agentic loop, so cost stays flat and bounded (~9,000 tokens per query at any scale); anything that must be 100% reproducible is deterministic code, and hard constraints belong in code rather than in the model's discretion.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)* |

*Why it matters: Model-chosen decomposition generalizes to unseen query shapes but makes per-query cost and worst-case correctness unbounded; a fixed pipeline gives constant cost and reproducible set logic but breaks on inputs its author did not anticipate. The choice determines whether you can put the system in front of mission-critical infrastructure.*

### Is the path to handling huge inputs a harness that keeps them out of the window, or an inference stack that serves them inside it?

| Position A | Position B |
|---|---|
| Keep the artifact out of the window: RLMs can process inputs many orders of magnitude larger than the context window, and context should grow with tree depth rather than instance count.<br>*[Recursive Coding Agents](../talks/recursive-coding-agents.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)* | Put it in the window and make the stack pay for it: agentic/coding workloads upload whole codebases, so the real work is sparse attention plus KV-cache handling at 500K–1M context under concurrency, treated as a distributed file system problem.<br>*[Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)* |

*Why it matters: It decides where engineering effort and cost land — in application-layer decomposition code you own, or in serving infrastructure and per-token spend you buy. It also decides whether harness authors should keep optimizing around a window limit that the serving side expects to erase.*

## Practical Guidance

**Do:**

- Treat the repository or corpus as data in a separate REPL/execution environment and have the model write code to inspect, slice, and compute the relevant chunks before anything enters the main context window
- Size context by hierarchy depth, not instance count — describe all root-to-leaf paths, so a 64-GPU system and a 460,000-GPU system yield roughly the same summary
- Use deterministic set operations for counting, dedup, and exact set logic over near-identical names, where perfect recall is required
- Give the harness explicit stages and a sub-call budget (planning, coding, observation, final output) rather than an open-ended loop
- Prototype by throwing everything into the context window first — it is the fastest way to find what is worth building — then migrate the hot, rule-expressible paths to deterministic code
- Fix the input/output interface of each repeated AI task so decomposition strategy, model, and technique can be swapped underneath without reshaping the program (Shopify: 550x cost reduction from a model swap with evals held fixed)
- If you do serve very long contexts, plan for KV-cache handling under concurrency as a distributed file system / database problem, not an ML problem
- Capture a successful 'golden session' as a reusable declarative workflow so the decomposition is repeatable rather than rediscovered each run

**Avoid:**

- Vector-embedding retrieval over near-identical entity names — the embeddings are indistinguishable and recall collapses
- Sharding entity names across parallel LLM calls and merging the results: it produces phantom entities that do not exist and silently drops ones that do
- Asking a single LLM call to enumerate many similar names — frequency penalties cause the model to truncate or shut off mid-output
- Compressing high-dimensional structured records into a single latent vector; the information loss is why transformer-based single-cell models lose to simple linear baselines
- Multi-step agentic loops for validation passes whose cost grows with entity count (116M tokens for one pass, still with many errors)
- Treating RLM as a framework rather than a pattern — different implementations (DSPy's, RLM Code, Codex's REPL) are not interchangeable
- Assuming a smarter or larger-context model removes the need for last-mile context: intelligence is not the same as knowing your tasks, data, and relationships
- Scaling up existing low-quality data and expecting generalization — measurement quality has to improve alongside volume

## Notable Outliers

- Qwen 3.5 9B run as an RLM beats Opus and GPT-5.4 run as plain LLMs on long-reasoning tasks — harness structure outweighs a ~100x parameter gap on long-context work. ([Recursive Coding Agents](../talks/recursive-coding-agents.md), [6:35](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=395s))
- An unmodified default RLM harness, with no custom engineering, performs comparably to a top-10 purpose-built memory system in a category attracting billions in funding. ([Recursive Coding Agents](../talks/recursive-coding-agents.md), [5:01](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=301s))
- A restructured pipeline cost a flat ~9,000 tokens per query whether the system had 64 GPUs or 460,000 — roughly a 300x total reduction versus the in-context baseline, with 100% correctness held across all tested scales. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s))
- KV cache handling at 500K–1M context under concurrency is essentially rebuilding a distributed file system — undergrad systems material that most ML practitioners skipped and are now rediscovering live in industry. ([Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s))
- Karpathy's drift of software 1.0 into 3.0 runs backwards for AI-native systems: start at 3.0 (everything in context) and mature toward 1.0, because every deterministic function you add is more reliable ground for the LLM to stand on. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s))
- Simple linear models sometimes match or outperform compute-expensive transformer foundation models on single-cell data, because treating cells as sentences and genes as tokens destroys information under compression. ([From Tokens to Cells: Foundation Models for Single-Cell Biology](../talks/from-tokens-to-cells-foundation-models-for-single-cell-biology.md), [12:24](https://www.youtube.com/watch?v=-561cZmir5Q&t=744s))

## All Talks

- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [From Tokens to Cells: Foundation Models for Single-Cell Biology](../talks/from-tokens-to-cells-foundation-models-for-single-cell-biology.md)
- [Recursive Coding Agents](../talks/recursive-coding-agents.md)
- [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)
- [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)
- [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)

## Speakers

- [Akram Baharlouei](../speakers/akram-baharlouei.md)
- [Dan Fu](../speakers/dan-fu.md)
- [Isaac Miller](../speakers/isaac-miller.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Maxime Rivest](../speakers/maxime-rivest.md)
- [Olive Song](../speakers/olive-song.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Shashi](../speakers/shashi.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)

