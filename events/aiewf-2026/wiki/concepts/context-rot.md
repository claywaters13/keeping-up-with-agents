---
title: "context rot"
type: "concept"
slug: "context-rot"
tier: "supporting"
maturity: "contested"
talk_count: 12
speaker_count: 13
---

# context rot

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **12** talk(s) by **13** speaker(s)

**Definition:** Degradation of model behavior as context grows or ages — attention dilution, stale facts, and instruction drift over long conversations.

*Also referred to as: context window degradation, lost in the middle, context staleness, context bloat, multi-turn instruction following degradation, context load, context stuffing*

## State of Practice

The field now treats effective context capacity as far smaller than nominal context capacity: agents degrade — contradicting themselves, ignoring parts of the system prompt, mis-selecting tools — long before the window is full. The reported thresholds are concrete and low: performance starts sliding around 25% window utilization and a 'dumb zone' past 40%, keep working context under ~100k tokens even on million-token models, and voice agents lose instruction-following after 15–20 turns. The dominant mitigation is architectural rather than capacity-based: just-in-time loading of tools, skills, and reference material so the catalog can grow while the working set stays small — semantic tool routing cuts 127k tokens of schemas to ~1k while holding selection accuracy above 83%, and skills report roughly 10x less overhead than the equivalent MCP setup. A second, distinct failure mode is aging rather than dilution: hand-maintained .md files, skills, and system prompts accumulate sediment and go stale (columns that no longer exist, KPI definitions that changed), which no amount of window headroom fixes. The sharpest live dispute is whether 'rot' is real model degradation at all: one team's measurements found distinctive facts recalled reliably to 800k tokens and keeping the full untouched history beating every compaction preset on recall, cost, and latency simultaneously — locating the failure in retrieval (dense search collapsing to 0% recall at 400k where BM25 held 100%) rather than in attention.

## Consensus

### Agent quality degrades well before the context window is full — effective usable context is a fraction of nominal context, so window size is not a capacity budget.

Support: **8** talk(s)

> "there was a paper called context rot, and it proves that after 25% usage of the context window, so for example, for 1 million token, if you used 256K of it, the performance starts to degrade."
>
> — [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [1:39](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=99s)

Supporting talks: [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)

### The fix is just-in-time / progressive disclosure — keep pointers and descriptions in context and load the full material only when the current step needs it, so the catalog can grow while the model's working set stays small.

Support: **6** talk(s)

> "This is the core lesson from the benchmark. The catalog can grow, but the model's working set should stay small."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [15:32](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=932s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### A bigger model, a longer context window, or more connected knowledge sources does not fix bad agent answers — the problem is what you put in context, not how much fits.

Support: **4** talk(s)

> "Context is a budget. Context is almost like a limited resource that we need to carefully filter information. Definitely the longer context doesn't mean better."
>
> — [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [25:36](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1536s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)

### The aging half of context rot is a separate failure mode: hand-maintained skills, docs, and system prompts go stale or accumulate sediment, and nothing in the current stack updates them.

Support: **3** talk(s)

> "the context gets rotten, or it gets deprecated, or processes change so often that it's hard to maintain dot MD files, or keep on updating your skills with the most latest context"
>
> — [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [5:18](https://www.youtube.com/watch?v=B8l81jhvHbI&t=318s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)

## Disagreements

### Does model quality actually degrade as raw context length grows, or is the observed failure really a retrieval and tool-catalog problem?

| Position A | Position B |
|---|---|
| Yes — degradation is a property of long context itself. Performance slides past ~25% window utilization and enters a 'dumb zone' past 40%; attention weakens for material in the middle of a long prompt; instruction following breaks after 15–20 conversational turns; filling the window too full degrades answer quality independent of the hard limit. Therefore cap the working context (~100k, under 60k for the hardest problems).<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)* | No — measured on a real deployed tutor agent, distinctive facts were recalled reliably up to 800k tokens with no compaction, and keeping the full untouched history beat every compaction preset on recall, cost, and latency at once. What actually failed at 400k was dense semantic retrieval (0% recall on facts buried mid-context) while BM25 keyword search held 100%.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: If rot is a model property, the correct engineering response is aggressive context capping, routing, and externalization; if it is a retrieval property, capping throws away cached tokens and recall for nothing and the fix is keyword-plus-dense hybrid search over the full history.*

### When context grows, should you compact/prune it, or keep everything and pay for the tokens?

| Position A | Position B |
|---|---|
| Prune or reset. Compaction is lossy but a fresh deterministically re-allocated context each iteration beats compacting; long voice sessions need context pruning or session resets after 15–20 turns; irrelevant tool schemas should be actively removed from the model's choice set.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)* | Do not compact by default. Summarization invalidates the provider's prompt cache, so it only pays off above ~50x compression; clearing old tool outputs makes the agent re-retrieve information it already had, raising total cost. Only compact once you can name the constraint forcing it (e.g. a window too small for caching to apply).<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)* |

*Why it matters: The two policies invert the cost model: with a 97% cache hit rate the largest-token setup was the cheapest to run, so a default compaction step can simultaneously raise spend and lower recall — or, on the other side, an uncapped context can silently degrade every downstream decision.*

### Should context be conserved by model-invoked progressive disclosure, or by explicit user invocation?

| Position A | Position B |
|---|---|
| Model-invoked, many small cross-referencing units loaded on demand — descriptions under 100 tokens at level one, ~5K on activation, scripts at level three. This is what gives skills roughly 10x less context overhead than the equivalent MCP setup, and the field is converging on more and smaller skills.<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)* | User-invoked. Every context pointer is a coin flip the model may decline to follow, which forces you to write evals just to confirm skills fire at the right time. Accept the higher user cognitive load to eliminate that entire class of unpredictability.<br>*[Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)* |

*Why it matters: Model-invoked disclosure minimizes resident tokens but adds a retrieval-reliability problem you must eval; user-invoked disclosure is deterministic but scales its cost onto the human and cannot help an autonomous long-running agent.*

## Practical Guidance

**Do:**

- Keep baseline system prompt plus tool definitions under 40% of the context window before any user turn, and treat 25% as where degradation begins
- Cap agent working context around 100k tokens even on million-token models; ~200k as an upper revision and under 60k for the hardest problems
- Past ~50 tools in production, retrieve tool schemas just-in-time by semantic search; run your test set at K=3, 5, and 10 and pick the smallest K meeting your accuracy target (K=5 is a strong default)
- Below 20 tools, skip the router and just load statically — the machinery is not worth it
- Pair BM25 keyword search with dense retrieval at large context sizes; dense-only dropped to 0% recall on mid-context facts at 400k where BM25 held 100%
- Name the specific constraint forcing compaction before compacting; measure recall, cost, and latency against the do-nothing baseline first
- Push reference material used by only one branch of a skill out of skill.md and behind a context pointer
- Split a procedure into separate skills so the agent sees one step at a time — hiding future steps increases legwork on the current step
- Source agent context from live, continuously updated systems (GitHub, CRM, Tableau, dbt) instead of static .md files, and log correction events back into that context
- Consolidate accumulated memories into skills (~10 memories) so stale system-prompt facts get refreshed without manual prompt rewrites
- Log per-turn tokens, cache hits, cost, TTFT, and tool calls — cheap to implement and most teams skip it
- Treat recall policy as a first-class metric: bad memory costs tokens and sends the agent the wrong way
- Externalize context curation into a programmable environment (REPL/code over the repo) when the corpus is too large and structured to load, as in monorepos
- Write tool descriptions in the words users actually use, with intent, action, and key entities — routing quality is bounded by description quality

**Avoid:**

- Reaching for a bigger model, the latest model, or a longer window when the agent gives a bad answer
- Compacting or summarizing by default — summarization invalidates the prompt cache and needs >50x compression to pay off
- Aggressively clearing old tool outputs; the agent just re-retrieves what it already had and you pay for more tool calls
- Packing hundreds of tool schemas into the middle of the prompt — at 741 tools, selection accuracy falls to 13.6% and TTFT passes 5 seconds around 500 tools
- Connecting an agent to 15 MCP servers and eating 100k+ tokens per session in tool definitions alone
- Adding a memory harness when the task and its relevant context already fit in the window — it adds cost with no capability gain
- Letting shared skill files accumulate sediment, duplication, and no-op instructions the agent would follow anyway if deleted
- Weighting all knowledge bases equally instead of ranking sources of truth cleanest-first
- Letting LLMs write your skills — LLM-generated skills consume more tokens and reasoning time and measurably hurt performance
- Bucketing documents by domain for a supervisor model; with dense inter-document relationships it skips domains that look irrelevant at first glance
- Assuming a local model is a drop-in swap for chat memory — a 32K window cut recall from 92–95% to 33%, and more parameters do not buy more window
- Pulling in community-authored skills without auditing them for duplication, sediment, and no-ops first

## Notable Outliers

- Distinctive facts were recalled reliably up to 800k tokens with no compaction at all — the model was not missing facts buried in a very long history. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [53:53](https://www.youtube.com/watch?v=WP3hjUXd918&t=3233s))
- The setup sending the most tokens was the cheapest to run, because 97% of the tokens were cached — while compacting first dropped correct-answer rate to 32%. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [52:08](https://www.youtube.com/watch?v=WP3hjUXd918&t=3128s))
- Tool-selection accuracy falls to 13.6% at 741 tools — roughly one correct tool out of eight — and the design fails not because any single tool is badly written but because every request carries the whole catalog. ([The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [3:57](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=237s))
- Compaction is lossy enough that deterministically re-allocating a fresh context each iteration beats compacting the existing one. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [31:12](https://www.youtube.com/watch?v=c35YoMdnI78&t=1872s))
- Giving an agent the correct memory does not make it use it — oracle retrieval still fails to reach maximum task performance because the model can ignore or misread the right context. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s))
- A rank-only decisions ledger beat both vector RAG and binary memory gating on long-horizon recall, across two models and two benchmarks. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [7:31](https://www.youtube.com/watch?v=R3-anFK1YM8&t=451s))
- Organizing documents into domain buckets actively hurts recall; distributing them in no particular order works better because the supervisor stops pre-judging which domains are relevant. ([When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [3:50](https://www.youtube.com/watch?v=XovaGv4f39A&t=230s))
- Voice agents start ignoring parts of the system prompt after 15–20 turns, which is a far shorter horizon than token-based rot thresholds suggest. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [19:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1147s))
- Letting the agent browse the knowledge base with bash commands added zero recall over hybrid search and made responses 50% slower. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [30:51](https://www.youtube.com/watch?v=WP3hjUXd918&t=1851s))

## All Talks

- [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)
- [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)
- [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)
- [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)
- [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

## Speakers

- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Ankush Rastogi](../speakers/ankush-rastogi.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [Ishita Daga](../speakers/ishita-daga.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Omar Solano](../speakers/omar-solano.md)
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Shashi](../speakers/shashi.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Stefania Druga](../speakers/stefania-druga.md)

