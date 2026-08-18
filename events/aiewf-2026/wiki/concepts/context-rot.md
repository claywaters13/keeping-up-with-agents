---
title: "context rot"
type: "concept"
slug: "context-rot"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 10
---

# context rot

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **10** speaker(s)

**Definition:** Degradation of model behavior as context grows or ages — attention dilution, stale facts, and instruction drift over long conversations.

*Also referred to as: context window degradation, lost in the middle, context staleness, context bloat, multi-turn instruction following degradation, context load, context stuffing*

## State of Practice

Context rot is treated as an established, measurable failure mode rather than a hypothesis: speakers cite degradation starting around 25% of window utilization, a "dumb zone" past 40%, tool-selection accuracy falling from ~78% at 10 tools to 13.6% at 741, and voice agents dropping system-prompt instructions after 15-20 turns. The field has largely stopped treating a longer context window or a newer model as the remedy — context is framed as a budget to be spent, with the always-resident portion (system prompt, tool schemas, skill descriptions) as the first thing to audit, since 15 MCP servers or a 741-tool catalog can consume 100k-127k tokens before the user says anything. The dominant mitigation is architectural: keep the model's working set small and push everything else behind an on-demand boundary — semantic tool routing at K≈5, progressive-disclosure skills (sub-100-token descriptions, sub-5k activation), sub-agents, external REPL environments the model programs against, or a write-manage-read memory harness. A second, less-solved dimension is aging rather than volume: hand-maintained .md files, skills, and system prompts go stale (a column that no longer exists still sits in the prompt), and almost nobody has a feedback loop wiring eval traces or correction events back into context. Open engineering questions concentrate on where to draw the retrieval boundary, whether budgets should be expressed as a fraction of the window or a fixed token ceiling, and whether compaction is a legitimate tool or a lossy operation to be replaced by deterministic fresh context per iteration.

## Consensus

### Model quality degrades well before the context window is full — filling the window is a quality decision, not just a limit question.

Support: **8** talk(s)

> "there was a paper called context rot, and it proves that after 25% usage of the context window, so for example, for 1 million token, if you used 256K of it, the performance starts to degrade."
>
> — [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [1:39](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=99s)

Supporting talks: [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### A bigger model, a longer context window, or more knowledge sources is not the fix; context must be treated as a scarce budget that is actively filtered.

Support: **5** talk(s)

> "Context is a budget. Context is almost like a limited resource that we need to carefully filter information. Definitely the longer context doesn't mean better."
>
> — [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [25:36](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1536s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)

### The always-resident block — tool schemas, MCP definitions, model-invoked skill descriptions — is the largest and most fixable source of rot, because every request pays for the entire catalog whether or not it is relevant.

Support: **4** talk(s)

> "The important point is, basically, the design does not fail because one tool is badly written. It fails because every request is forced to carry the entire catalog."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [2:52](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=172s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### The right architecture keeps the model's working set small and holds the rest behind an on-demand boundary (routing, progressive disclosure, sub-agents, external execution environments, or a memory harness).

Support: **5** talk(s)

> "This is the core lesson from the benchmark. The catalog can grow, but the model's working set should stay small."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [15:32](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=932s)

Supporting talks: [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### Context rots by aging as well as by growing: hand-maintained skills, .md files, and system prompts drift out of date faster than teams can update them, and there is no standard mechanism that refreshes them.

Support: **3** talk(s)

> "the context gets rotten, or it gets deprecated, or processes change so often that it's hard to maintain dot MD files, or keep on updating your skills with the most latest context"
>
> — [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [5:18](https://www.youtube.com/watch?v=B8l81jhvHbI&t=318s)

Supporting talks: [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)

## Disagreements

### Should the response to context rot be to select less context up front, or to keep the whole corpus reachable and let the model curate it at runtime?

| Position A | Position B |
|---|---|
| Cut aggressively before the model sees anything: retrieve a small relevant subset (K≈5 tool schemas), keep skill.md minimal, put branch-specific reference material behind context pointers, and remove wrong options from the choice set entirely.<br>*[The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)* | The selection step is itself where the signal dies: similarity-thresholded retrieval cannot return a collection where everything is relevant, so keep the full corpus reachable — parallel KV-cached buckets with a supervisor, a programmable REPL the model writes code against, or outcome-weighted retrieval that learns rather than a static similarity cut.<br>*[When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)* |

*Why it matters: It decides whether you invest in a retrieval/routing layer with an accuracy target, or in cache lifetime management and sandboxed execution environments — completely different infrastructure and cost curves. It also determines whether recall failures are debugged as embedding-quality problems or as supervisor-exploration problems.*

### Is the safe context budget a fraction of the model's window, or a fixed absolute ceiling independent of window size?

| Position A | Position B |
|---|---|
| Express it as a percentage: under 25% is safe, 40% is the boundary of the smart zone, so keep system prompt plus tool definitions under 40% of whatever window you have before the first user turn.<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)* | Percentages do not survive bigger windows: keep working context under roughly 100k tokens (under 60k for hard problems) even with million-token windows, and in voice track turns rather than tokens, pruning or resetting after 15-20 turns.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md)* |

*Why it matters: With a 1M-token window the two rules differ by 300k tokens of allowed context — one says 400k is fine, the other says you are deep into failure. It also changes whether upgrading to a larger-window model buys you headroom or nothing at all.*

### Should the agent's durable operating context be hand-authored and reviewed, or automatically derived from live systems and runtime outcomes?

| Position A | Position B |
|---|---|
| Skills are software: hand-write them, keep a single source of truth, delete no-ops, audit community skills before pulling them in, and version and test them — LLM-generated skills measurably hurt performance by burning more tokens and reasoning time.<br>*[Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)* | Hand-maintenance cannot keep pace with changing KPIs, definitions, and schemas: source context from live systems (dbt, GitHub, CRM, Tableau) and log correction events back into it, and once ~10 memories accumulate, bake the learned reasoning into skills automatically so the agent stays current without prompt rewrites.<br>*[Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [User Signal Dies at the Retrieval Boundary](../talks/user-signal-dies-at-the-retrieval-boundary.md)* |

*Why it matters: One path spends human review time to keep the resident context small and correct; the other accepts machine-written context in exchange for freshness, and inherits a new failure mode where noisy review labels propagate into the agent's operating instructions.*

## Practical Guidance

**Do:**

- Keep baseline system prompt plus tool definitions under 40% of the context window before any user turn; under 25% is where performance is still intact.
- Cap agent working context near 100k tokens even on million-token windows, and under 60k for the hardest problems.
- Past ~50 tools in production, replace static tool loading with a semantic router that injects K≈5 schemas; run the test set at K=3, 5, and 10 and pick the smallest K meeting your accuracy target.
- Below 20 tools, skip the router entirely and load statically — the machinery is not worth it at 10-15 tools.
- Structure skills for progressive disclosure: level-one description under 100 tokens, activation under 5k, scripts below that.
- Move reference material used by only one branch of a skill out of skill.md and behind a context pointer.
- Give every part of a skill a single source of truth and delete instructions the agent would follow anyway (no-ops), which are especially common when an agent wrote the skill.
- Rank knowledge sources cleanest-first — semantic layer, then canonical queries, then the database graph — instead of weighting all knowledge bases equally.
- Prune context or reset the session after 15-20 turns in long voice conversations, before instruction following degrades.
- Prefer deterministically re-allocating a fresh context each iteration over compacting the existing one.
- Treat recall policy as a first-class metric: a good policy lowers total token spend as well as raising accuracy.
- Write tool descriptions in the words users actually use, including intent, action, and key entities — routing quality is bounded by description quality.
- Log correction events and eval outcomes back into the agent's context instead of letting the signal die in a dashboard.

**Avoid:**

- Reaching for a bigger model, a longer window, or more knowledge bases and MCP servers when the agent gives bad answers.
- Connecting an agent to ~15 MCP servers, which burns 100k+ tokens per session in tool definitions alone before any work happens.
- Assuming failures that appear as tools are added are prompt problems — accuracy collapse from lost-in-the-middle is architectural.
- Relying on compaction to survive long runs; it is lossy and degrades fidelity.
- Adding a memory harness when the task and its relevant context already fit in the window — it adds cost and no capability.
- Assuming the model will use correct context once it is retrieved; oracle retrieval still does not reach maximum task performance.
- Bucketing documents by domain across parallel caches — with dense cross-document relationships the supervisor skips domains that look irrelevant at first glance.
- Letting shared skill and prompt files accumulate sediment because contributors add but never delete others' text.
- Shipping LLM-generated skills as-is; they consume more tokens and reasoning time than human-written equivalents.
- Pulling community skills into your agent's context without auditing them first.

## Notable Outliers

- Providing the agent with exactly the right memory does not guarantee it uses it — oracle retrieval still falls short of maximum task performance, so retrieval quality is not the whole story. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [8:29](https://www.youtube.com/watch?v=R3-anFK1YM8&t=509s))
- Tool-selection accuracy falls to 13.6% at 741 tools — roughly one correct tool out of eight — while semantic routing holds above 83% across the same catalog sizes. ([The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [3:57](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=237s))
- Holding model and eval constant across 106 tasks, swapping only the harness moves scores from 52.4% to 76.2%, and the harness matters more for weaker models than stronger ones. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s))
- Deliberately hiding future steps by splitting a process into separate skills, so the agent sees only one step at a time, increases the legwork it does on the current step. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [15:46](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=946s))
- A rank-only decisions ledger beats both vector RAG and binary memory gating on long-horizon recall, and bad memory is expensive because it spends tokens and sends the agent the wrong way. ([Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [7:31](https://www.youtube.com/watch?v=R3-anFK1YM8&t=451s))
- User-invoked skills are preferable to model-invoked ones: the higher user cognitive load buys you the elimination of invocation unpredictability and the evals needed to police it. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [6:25](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=385s))
- Instruction following in voice agents degrades after roughly 15-20 turns — models start ignoring parts of the system prompt, get verbose, and go off script. ([Voice Agents That Handle Interrupts](../talks/voice-agents-that-handle-interrupts.md), [19:07](https://www.youtube.com/watch?v=hMlLw1LeIK8&t=1147s))

## All Talks

- [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)
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
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Shashi](../speakers/shashi.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Sonam Pankaj](../speakers/sonam-pankaj.md)
- [Stefania Druga](../speakers/stefania-druga.md)

