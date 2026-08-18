---
title: "code comprehension and indexing"
type: "concept"
slug: "code-comprehension-and-indexing"
tier: "supporting"
maturity: "contested"
talk_count: 6
speaker_count: 6
---

# code comprehension and indexing

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **6** talk(s) by **6** speaker(s)

**Definition:** Making a codebase queryable for agents — indexing, symbol and call graphs, and cross-repo search that feeds context.

*Also referred to as: code comprehension, code indexing, cross-repo code search, call graph traversal, codebase as structured data, context retrieval from source code, dependency graph invariants, cross-repo dependency graphs*

## State of Practice

The field has converged on a diagnosis: the binding constraint on coding agents is not model quality but what the agent can see — one repo at a time, one session at a time, with no persistent model of how the code fits together. Concretely, teams report agents degrading as context grows on monorepos, a typical query shipping 45K tokens where ~5K mattered, and ~90% of AI coding spend landing on the input side, which means retrieval quality is a cost line, not just a quality line. The mechanisms being shipped are wildly divergent: a cross-repo dependency graph built from metadata extraction (Nx's Polygraph), a local hybrid keyword+embedding index with a weighted heuristic score (Tesco), a REPL where the model writes Python to slice the repo instead of loading it (RLM), a markdown anti-pattern catalog in a central git repo plus cross-repo grep (Netflix), and a new language whose compiler infers error types through the call graph so comprehension is structural rather than retrieved (Boundary). Nearly everyone builds this as a layer above the agent rather than inside it, and nearly everyone distrusts prose: source code, call stacks, execution traces, and canary results are treated as ground truth while READMEs and architecture files are treated as lies waiting to happen. The unresolved question underneath all of it is who the index is for — the agent, so humans can stop reading code, or the human, whose understanding Notion argues is the actual bottleneck.

## Consensus

### Better models will not fix code comprehension; the limit is what context the system can assemble, and that is where the cost and the failure modes live.

Support: **4** talk(s)

> "The answer was not a better model. The answer was sending less."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [9:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=571s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)

### The comprehension layer belongs outside any single agent — a model-agnostic harness, index, or artifact that multiple tools and sessions share, rather than per-tool state that starts from zero each time.

Support: **4** talk(s)

> "Polygraph isn't an agent. It's a meta harness around an agent that makes them uh more capable."
>
> — [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [10:49](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=649s)

Supporting talks: [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md)

### Ground truth for comprehension is the executable artifact — source, call stacks, execution traces, canary results — not natural-language documentation, which drifts or lies.

Support: **3** talk(s)

> "Don't read anything but the code itself. The docs may lie, the um the actual description or architecture file or readme file will definitely lie, but the code cannot lie."
>
> — [fighting slop with slop](../talks/fighting-slop-with-slop.md), [13:06](https://www.youtube.com/watch?v=AMiyLItEtLA&t=786s)

Supporting talks: [fighting slop with slop](../talks/fighting-slop-with-slop.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)

### The retrieval substrate should be cheap and deterministic — markdown in git, weighted keyword/structural scoring, compiler-derived tools — rather than a vector database or an LLM reranker in the request path.

Support: **3** talk(s)

> "It runs 0.4 milliseconds, no extra AI calls needed. The lesson we learned, simple formula beats the complex model most of the time."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [5:33](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=333s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md)

## Disagreements

### Should relevant context be retrieved from a persistent precomputed index, or computed on demand by giving the model a programmable environment over the repo?

| Position A | Position B |
|---|---|
| Build a durable artifact ahead of time — a hybrid semantic+keyword+recency index that re-indexes in under a second, or a unified cross-repo dependency graph extracted from metadata — and query it per request.<br>*[We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)* | Don't precompute an index at all: existing grep-style and semantic search are insufficient for monorepos, so externalize context management into a REPL or language-level tooling where the model writes code to inspect, slice, and compute the relevant chunks at query time.<br>*[RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md)* |

*Why it matters: The index camp pays maintenance and staleness cost but gets millisecond, token-cheap lookups; the on-demand camp pays latency and sub-call budget per query but never goes stale and degrades more gracefully as files accumulate responsibilities — exactly the case where Tesco measured recall collapsing to near zero.*

### Is the goal of code indexing to let agents comprehend the code so humans don't have to, or to help humans keep understanding code that agents wrote?

| Position A | Position B |
|---|---|
| Human understanding is the real bottleneck and must be actively defended: gate sending code for review on passing a quiz about what the agent wrote, debug some bugs yourself to retain peripheral feel for the system, and build throwaway software purely to understand other software.<br>*[Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)* | Engineers will not read the code regardless of policy, so remove the human from the comprehension loop: drop code review in favor of type-system-enforced invariants, and treat the human acting as the system's research and memory layer as the defect to be engineered away.<br>*[fighting slop with slop](../talks/fighting-slop-with-slop.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)* |

*Why it matters: It decides what the index optimizes for — token-minimal machine-readable slices, or human-legible explanations and shared, commentable agent transcripts — and whether review gates stay in the pipeline at all.*

### Can code be made agent-comprehensible by layering tooling on top of existing languages and repos, or does the substrate itself have to be rebuilt?

| Position A | Position B |
|---|---|
| Retrofitting is patching a broken foundation: languages, git, and databases need rebuilding for an agent-first world, with error types inferred through the call graph and zero-cost full-program execution tracing designed in from first principles.<br>*[fighting slop with slop](../talks/fighting-slop-with-slop.md)* | Comprehension can be added without touching the analyzed code — a dependency graph from pure metadata extraction with zero lines changed, a local index over the existing tree, a profiling workflow that works identically across Java, Python, and Go.<br>*[A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)* |

*Why it matters: One path is deployable against the codebase you already have this quarter; the other requires an embeddable new language and concedes that current comprehension tooling is a ceiling, not a gap.*

## Practical Guidance

**Do:**

- Build the cross-repo dependency graph purely from metadata extraction, without changing a line of code in the analyzed repositories.
- Score hybrid retrieval with a fixed weighted formula — 50% semantic, 30% keyword, 20% recency — plus an adaptive threshold, and skip LLM reranking: 0.4ms versus 2-3 seconds added per query.
- Combine semantic and keyword search rather than picking one; each alone misses about one in four relevant results, together about one in ten.
- Store the pattern/memory catalog as plain markdown in a central git repo before reaching for a vector database, and structure it hierarchically with an index so consulting it doesn't fill agent context.
- When an anti-pattern is confirmed, run cross-repo code search to find every other instance — Netflix found the same Spectator counter bug in seven services, worth 0.5-4.6% of CPU cycles each.
- Load the real open-source repository into the session instead of a documentation-retrieval tool when diagnosing deep problems.
- Give the model a dedicated execution environment where it writes code to inspect and slice the repo, feeding only the computed chunks back into the main context window.
- Keep the shared architecture file tiny, model-agnostic (architecture.md, not CLAUDE.md), and limited to invariants that will not change for months or years.
- Measure token savings by instrumenting real queries against a stated baseline, and disclose which baseline — the 94% figure is against worst-case full-file reads, not against a modern agentic tool.
- Gate sending agent-written code to teammates on being able to pass a quiz about what it does.

**Avoid:**

- Don't try to cut cost by shortening outputs or tuning max tokens and temperature — roughly 90% of spend is input tokens.
- Don't prompt the agent to 'send less context'; the context is transmitted and billed before the model reads the instruction.
- Don't assume an index generalizes: recall dropped to nearly zero on a 396-file project where individual files carried many responsibilities.
- Don't treat READMEs, architecture files, or descriptions as authoritative when the source or an execution trace is available.
- Don't expect a newer model to supply knowledge of your internal platforms, frameworks, and codebase patterns.
- Don't let the human be the cross-repo research and memory layer — re-explaining one change across 20 repos burns both developer time and tokens.
- Don't fully delegate every bug fix if you need to retain feel for the system; you forfeit the peripheral understanding debugging would have given you.
- Don't let each tool keep its own private context — Claude Code, Cursor, and Copilot each starting fresh means explaining the same codebase three times.

## Notable Outliers

- Grep should not be used anywhere — ripgrep supersedes it, and a semantic 'describe' tool derived from language tooling supersedes both for agents. ([fighting slop with slop](../talks/fighting-slop-with-slop.md), [11:52](https://www.youtube.com/watch?v=AMiyLItEtLA&t=712s))
- Honest negative result: the local index's recall collapsed to nearly zero at 396 files when individual files had many responsibilities. ([We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [7:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=455s))
- An agent identified an O(n²) pattern purely from the profiler's call stack, without reading the source code first. ([AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [8:53](https://www.youtube.com/watch?v=CgsWxRUY5Eo&t=533s))
- Pooling sessions across every developer means the agent ends up with more context about the organization than any single developer has. ([A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [19:13](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=1153s))
- Because generating code is nearly free, writing throwaway software purely to understand other software is now an everyday technique, not a luxury. ([Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [18:27](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=1107s))
- Since we don't read all the code, the only remaining way to understand it is the execution trace — which requires a language designed for zero-cost full-program tracing. ([fighting slop with slop](../talks/fighting-slop-with-slop.md), [10:39](https://www.youtube.com/watch?v=AMiyLItEtLA&t=639s))

## All Talks

- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)
- [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

## Speakers

- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [Rajat Shah](../speakers/rajat-shah.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Shashi](../speakers/shashi.md)
- [Vaibhav Gupta](../speakers/vaibhav-gupta.md)
- [Victor Savkin](../speakers/victor-savkin.md)

