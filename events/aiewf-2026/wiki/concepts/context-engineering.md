---
title: "context engineering"
type: "concept"
slug: "context-engineering"
tier: "core"
maturity: "consolidating"
talk_count: 32
speaker_count: 37
---

# context engineering

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **32** talk(s) by **37** speaker(s)

**Definition:** The practice of deciding what information enters a model's context and in what form, treating context assembly as a first-class engineering discipline rather than prompt wording.

*Also referred to as: context construction, context assembly and working sets, context scaffolding, just-in-time context injection, prompt and context optimization, content engineering, web context engineering*

## State of Practice

By this conference the field treats context assembly, not model selection, as the primary lever on agent quality — speakers repeatedly showed identical models producing wildly different outcomes depending on what entered the window and in what form. The operating model is a budget: Codex caps its available-skills list at 2% of the context window and marks rarely-used tools as deferred behind tool search; DataRobot's rule of thumb is to keep system prompt plus tool definitions under 40% before the first user turn; Prosodica measured tool-selection accuracy falling from ~78% at 10 tools to 13.6% at 741, with 127k tokens spent on schemas alone, and recovered 83%+ accuracy by semantically routing to ~5 schemas per request. Retrieval mechanics have converged on hybrid: dense-only search collapsed to 0% recall on facts buried at 400k tokens where BM25 held 100%, and Microsoft, Towards AI, and Tesco independently reported combined methods beating either alone. The second half of the discipline is upstream of retrieval — provenance, contradiction checks, freshness, and active pruning of what is retrievable, since a stale fact is returned with the same confidence as a correct one. Durable state is moving out of the window entirely: files on disk, session logs, databases, and shared docs, so that context can be wiped and rebuilt rather than summarized. What remains genuinely unsettled is compaction: at least one team's measurements say keeping the full history beats every compaction preset on recall, cost, and latency simultaneously, because prompt caching makes the biggest context the cheapest to run.

## Consensus

### Context assembly, not model capability or context-window size, is the binding constraint on agent quality — the same model produces 2x or 100x results depending on how context is wired.

Support: **8** talk(s)

> "The 2X people and the 100X people are using the exact same Claude. Same weights, same context window, same API. So, the leverage is not in the weights. It's in how you wire the work."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### Context is a finite budget to be allocated, not a container to be filled — oversized context degrades output quality (contradictions, lost-in-the-middle attention, thrashing), not merely cost.

Support: **8** talk(s)

> "Context is a budget. Context is almost like a limited resource that we need to carefully filter information. Definitely the longer context doesn't mean better."
>
> — [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [25:36](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1536s)

Supporting talks: [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)

### Tools, skills, and knowledge should be loaded lazily via progressive disclosure or retrieval, not enumerated up front in the system prompt.

Support: **5** talk(s)

> "I mean, this is not a new software idea. We have used lazy loading, just-in-time compilation, and on-demand resource loading from years. We are just applying the simple and same principle to the LLM context."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [11:13](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=673s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)

### Durable agent state belongs outside the context window — in files, session logs, docs, or a database — so that context can be wiped or a machine can crash without losing work.

Support: **7** talk(s)

> "The state lives in files. It is not trapped inside one model. And this is the single most practical thing I learned all year."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)

### Dense vector similarity alone is insufficient for feeding context; keyword/lexical retrieval must be combined with it, and the gap widens as the corpus or context grows.

Support: **3** talk(s)

> "By themselves, both searches miss about one in four results. Together, they miss about one in 10."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [4:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=275s)

Supporting talks: [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### The hard part is curating what is worth retrieving — ranked sources of truth, provenance, contradiction checks, freshness, and pruning — not the retrieval mechanism itself.

Support: **6** talk(s)

> "Retrieval is easy. Being worth retrieving from is the product."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [12:37](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=757s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Content Is Code](../talks/content-is-code.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)

## Disagreements

### Should long-running agents compact or summarize their context by default?

| Position A | Position B |
|---|---|
| No. Compaction should be off by default and only enabled once a named constraint forces it — summarization invalidates the prompt cache (requiring >50x compression to break even), aggressively clearing tool outputs makes the agent re-retrieve what it already had, and keeping the full history beat every compaction preset simultaneously on recall, cost, and latency. Recover by clearing context entirely and re-reading self-written handoff files rather than summarizing history.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)* | Yes, automatically. Codex has run server-side auto-compaction since late last year, performed in the form the model was trained on specifically so that performance is unchanged after compaction, and it is exposed as a default in the Responses API.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* |

*Why it matters: Compaction defaults determine whether prompt caching (up to 97% of tokens cached in one team's DeepSeek runs, making the largest-context setup the cheapest) applies at all, which flips the cost curve by more than an order of magnitude. It also decides whether harness vendors should ship compaction on by default or make it an explicit opt-in.*

### Does model performance actually degrade as the context window fills, and should teams therefore trim aggressively?

| Position A | Position B |
|---|---|
| Yes — 'context rot' is real and starts early. Performance begins degrading after roughly 25% of the window is used and agents enter a 'dumb zone' past 40%; more content raises the chance of contradicting information confusing the model; and hundreds of tool schemas packed into the middle of a long prompt are not reliably attended to, collapsing tool-selection accuracy to 13.6% at 741 tools.<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* | Not necessarily. In measured multi-turn experiments, distinctive facts were recalled reliably up to 800k tokens with no compaction at all, and untouched full history outperformed every trimmed variant; what fails at scale is the retrieval method (dense search dropped to 0% recall on facts buried at 400k where BM25 held 100%), not the model's use of a long context.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: If degradation is a property of window occupancy, the right investment is aggressive pruning, routing, and compaction infrastructure; if it is a property of how information was retrieved and placed, the right investment is better hybrid retrieval plus cache-friendly append-only contexts, and pruning is actively harmful to cost and recall.*

### Should durable agent context be hand-authored (skills, CLAUDE.md, markdown) or generated from live systems?

| Position A | Position B |
|---|---|
| Hand-authored and human-curated. A skill file is the unit of institutional knowledge — every successful agent task should be converted into a reusable skill, teams should hire engineers whose job is maintaining them, and skills should be versioned, evaluated, and tested like software because a skill is only as good as the human who wrote it (LLM-generated skills measurably hurt performance).<br>*[Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)* | Generated and continuously refreshed. Hand-maintained .md files and skills cannot keep pace with how fast enterprise definitions, KPIs, and processes change; context should be sourced from live systems (dbt, GitHub, CRM, Tableau) and per-user offline preprocessing, with corrections logged back in — and hardcoding context into agents is the dominant practice today precisely because it does not scale.<br>*[Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)* |

*Why it matters: It decides whether the durable artifact is a repo of markdown you own and prune, or a pipeline that reverse-constructs context from systems of record. The first fails by going stale; the second fails on cold start and on the tacit knowledge no system records, and each demands a completely different staffing and tooling investment.*

### Should the context an agent needs be precomputed offline or assembled at request time?

| Position A | Position B |
|---|---|
| Precomputed. Contextual understanding cannot be constructed at query time and must be built long before anyone asks the question — via slow/fast engines running on different time windows, periodic batch 'dreaming' over session transcripts and memory state, or owning your own extraction pipeline, because owned context compounds while rented context decays and repeated queries cost the same every time.<br>*[From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)* | Assembled just in time. Retrieve only the ~5 relevant tool schemas per request via an embedding call and a vector search, defer tools behind tool search, and have a librarian layer inject company semantics at the moment of the query — a roughly 99% reduction in tool-context tokens with negligible runtime overhead.<br>*[The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)* |

*Why it matters: Precomputation buys latency and cross-source understanding but has an explicit cold-start hole for new users and a standing batch-compute bill; just-in-time assembly is cheap and adapts to any query but can only surface relationships that were already indexed. Choosing wrong means either paying to precompute context nobody asks for, or being unable to answer questions that require connections no single retrieval hop can see.*

## Practical Guidance

**Do:**

- Budget the fixed part of context explicitly: cap the available-skills/tool-description block at ~2% of the context window (Codex progressively truncates beyond that), and keep system prompt plus tool definitions under 40% of the window before the first user turn.
- Once past ~50 tools in production, retrieve tool schemas semantically instead of loading them; run your test set at K=3, 5, and 10 and pick the smallest K that hits your accuracy target (K=5 is the reported default). Below 20 tools, skip the router and load statically.
- Combine lexical/BM25 with dense retrieval; one team weighted 50% semantic, 30% keyword, 20% recency with an adaptive threshold, running in 0.4ms versus 2-3 seconds for LLM reranking.
- Keep task state in files, session logs, or a database and recover by clearing the context and re-reading self-written handoff files, rather than compacting.
- Rank knowledge sources into an explicit hierarchy — semantic layer first, then canonical queries, then a database graph — instead of weighting all knowledge bases and MCP servers equally; the first two tiers reportedly cover ~80% of enterprise data-agent questions.
- Attach provenance and citations to every fact, run contradiction checks when new information collides with old, and assign a named human-plus-agent librarian whose actual job is pruning.
- Give the model a fixed catalog to select from — a component menu gated by client app version, standard public schemas like X12, asset intent tags — rather than letting it invent structures.
- Instrument every turn: tokens, cache hit rate, cost, TTFT, tool calls, and user frustration signals. It is cheap to implement and most teams skip it, then tune context by vibes.
- Verify with a separate agent that cannot see the generator's reasoning traces and assumes the finding is false by default; a discovery agent verifying its own work self-censors and loses recall.
- Write goal prompts that are concrete and verifiable rather than long essays, since the agent loop only terminates when the model can detect the goal was achieved.
- Shrink prompts by roughly 50% on each step-jump model version, and delete harness workarounds written for limitations the new model no longer has — they become latency and cache-invalidation overhead.
- Grade context by relevance the way rendering grades level of detail: feed the agent the near/edited slice of the scene or codebase, not the whole thing.
- Extract decisions into a durable shared doc up front so every agent starts stateless from the same place, rather than having an LLM summarize the session afterward and risk picking the wrong things.

**Avoid:**

- Compacting or summarizing by default — summarization invalidates the provider's prompt cache, so you must compress by more than 50x for it to pay off; name the constraint that forces compaction before enabling it.
- Aggressively clearing old tool outputs: the agent re-retrieves information it already had, so total cost goes up, not down.
- Connecting an agent to 15 MCP servers indiscriminately — that alone consumes over 100,000 tokens per session in tool definitions before any user turn.
- Throwing the entire codebase, the entire scene, or every knowledge base at the agent up front; it thrashes, explores, and burns tokens doing it.
- Reaching for a bigger model, a longer context window, or another knowledge base when an agent gives a bad answer — none of those tell it which source is authoritative.
- Relying on hand-maintained .md files and skills as the sole source of enterprise definitions and KPIs, which go stale faster than anyone updates them.
- Shipping LLM-generated skills unreviewed: they were measured to consume more tokens and more reasoning time than human-written equivalents, and public skill marketplaces still lack verification controls.
- Trying to cut AI coding spend by shortening outputs or tuning max_tokens and temperature — roughly 90% of the cost is input tokens, already billed before the model reads your prompt.
- Using single-turn benchmarks to compare context-management strategies; they never accumulate enough tokens to trigger compaction, so they cannot distinguish the strategies at all.
- Adding a second, more agentic retrieval path 'just in case' — letting the agent browse the knowledge base with bash on top of hybrid search added no recall and made responses 50% slower.
- Holding large combinatorial state (e.g. a seating arrangement for 800 people) in the context window; put the deterministic computation in deterministic space and let the model do the human part.
- Assuming a bigger local model fixes context: a 32K window cut chat recall from 92-95% to 33%, and increasing parameter count does not expand the window.

## Notable Outliers

- Keeping the full untouched conversation history beat every compaction preset on recall, cost, AND latency at once — on DeepSeek the setup sending the most tokens was the cheapest to run, because 97% of its tokens were cached. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s))
- Distinctive facts were recalled reliably up to 800k tokens with no compaction, directly contradicting the 'context rot' framing used elsewhere at the conference. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [53:53](https://www.youtube.com/watch?v=WP3hjUXd918&t=3233s))
- Fat-agent tool-selection accuracy falls from ~78% at 10 tools to 13.6% at 741 tools — roughly one correct tool out of eight — while semantic routing holds above 83% across the same catalog sizes. ([The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [3:57](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=237s))
- Simply loading CLAUDE.md, skills, and MCPs consumes about 25% of a coding agent's context on task-independent 'how to do the task' material before any work begins, which is why an orchestration layer should hold spec/goal/history context separately from implementation context. ([Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [5:19](https://www.youtube.com/watch?v=9arM9b7JgOo&t=319s))
- Supplying agents with explicit codebase context and constraints reduced tokens consumed per problem by over 30%, and customers using multi-layered verification report 44% fewer AI-derived production outages. ([In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [10:45](https://www.youtube.com/watch?v=VrpEyglYgeU&t=645s))
- For persona systems, fine-tuning is strictly worse than context-window anchoring: it layers a thin personal signal over vast cultural sediment in the base weights in a way that is no longer open to audit, whereas the persona-as-configuration can be inspected, versioned, and handed to a qualified reviewer. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [28:10](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1690s))
- The honest caveat on a headline number: the reported 94% context reduction is against a worst-case full-file-read baseline, and recall dropped to nearly zero on a 396-file codebase where individual files carry many responsibilities. ([We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [7:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=455s))
- Query frequency, not record volume, is the dominant cost driver for web context — every repeated query costs the same as the first even when nothing changed — and self-built extraction broke even against rented context at just over 15,000 entities. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [13:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=812s))
- Preference is an unsolved context problem: two teams can compute the same metric in different but equally correct ways, and neither semantic layers nor agent memory resolves it — the requesting individual's or team's identity must route to the right definition. ([Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [11:03](https://www.youtube.com/watch?v=B8l81jhvHbI&t=663s))
- Rendering soft human context before numeric constraints in the prompt produces less mechanical prose, because reversing the order commits the model to the numeric framing before it reads the qualitative tone fuel. ([Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [9:58](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=598s))

## All Talks

- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Content Is Code](../talks/content-is-code.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)
- [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [Everything Is a Rollout](../talks/everything-is-a-rollout.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [Guide, Verify, Solve](../talks/guide-verify-solve.md)
- [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)
- [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [On AI and Knowledge](../talks/on-ai-and-knowledge.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)
- [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md)
- [The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md)
- [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)
- [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)
- [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)
- [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)
- [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)

## Speakers

- [Alex Bauer](../speakers/alex-bauer.md)
- [Alex Shaw](../speakers/alex-shaw.md)
- [Anirban Chatterjee](../speakers/anirban-chatterjee.md)
- [Ankush Rastogi](../speakers/ankush-rastogi.md)
- [Arturo Nunez](../speakers/arturo-nunez.md)
- [Bala Ramdoss](../speakers/bala-ramdoss.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [Eugene Yan](../speakers/eugene-yan.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)
- [Ishita Daga](../speakers/ishita-daga.md)
- [Jacob E. Thomas](../speakers/jacob-e-thomas.md)
- [Jeffrey Lee-Chan](../speakers/jeffrey-lee-chan.md)
- [Jia Wu](../speakers/jia-wu.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Kyle Jaejun Lee](../speakers/kyle-jaejun-lee.md)
- [Leo Mehr](../speakers/leo-mehr.md)
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Matt Dailey](../speakers/matt-dailey.md)
- [May Walter](../speakers/may-walter.md)
- [Nicholas Arcolano](../speakers/nicholas-arcolano.md)
- [Omar Solano](../speakers/omar-solano.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Ryan Marten](../speakers/ryan-marten.md)
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Tariq Shaukat](../speakers/tariq-shaukat.md)
- [Vasant Kearney](../speakers/vasant-kearney.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Yu Su](../speakers/yu-su.md)

