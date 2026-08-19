---
title: "context engineering"
type: "concept"
slug: "context-engineering"
tier: "core"
maturity: "consolidating"
talk_count: 31
speaker_count: 36
---

# context engineering

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **31** talk(s) by **36** speaker(s)

**Definition:** The practice of deciding what information enters a model's context and in what form, treating context assembly as a first-class engineering discipline rather than prompt wording.

*Also referred to as: context construction, context assembly and working sets, context scaffolding, just-in-time context injection, prompt and context optimization, content engineering, web context engineering*

## State of Practice

By this conference the field has stopped treating context as prompt wording and started treating it as a budgeted, versioned, auditable resource: what enters the window, in what form, from which ranked source, and who owns it after the turn ends. The dominant framing across tracks is that model capability is no longer the binding constraint — harnesses, retrieval, and organization-specific knowledge are — and speakers back this with numbers rather than vibes (Codex caps its available-skills list at 2% of the context window; a 741-tool catalog costs ~127k tokens per request and drops tool-selection accuracy to 13.6%; 15 MCP servers burn >100k tokens per session in tool definitions alone; ~90% of AI coding spend is input tokens). The consensus mechanics are progressive disclosure and just-in-time loading (deferred tools, tool search, semantic routing to K≈5, small cross-referencing skills), hybrid retrieval rather than dense-vector-only, and durable state on disk so a context can be cleared and rehydrated instead of summarized. Where the field is genuinely split is on whether long context actually degrades: one camp cites context rot and lost-in-the-middle and engineers hard to keep the working set small, while a team that ran controlled experiments reports reliable recall of distinctive facts to 800k tokens and found that never compacting won simultaneously on recall, cost, and latency because 97% of tokens stayed cached. A second live split is whether context scaffolding is permanent architecture or temporary compensation — Anthropic and OpenAI speakers report harness fixes becoming pure overhead and prompts shrinking ~50% per model step-jump, while brand-voice and enterprise-data speakers argue deterministic layers and semantic hierarchies are load-bearing regardless of model quality. Underneath all of it, the strategic claim repeated across GTM, infra, and startup tracks is that context is the owned asset and the model is rented.

## Consensus

### Model capability is no longer the binding constraint on agent quality; the context and harness surrounding the model are.

Support: **10** talk(s)

> "The 2X people and the 100X people are using the exact same Claude. Same weights, same context window, same API. So, the leverage is not in the weights. It's in how you wire the work."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)

### Filling the context window degrades output quality, not merely cost — irrelevant or contradictory material actively makes decisions worse.

Support: **8** talk(s)

> "the more context you have in your in your context, the higher it is that you have contradicting information and it causes confusion for the model."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)

### Tools, skills, and scene detail should be loaded just-in-time through progressive disclosure rather than declared up front in the system prompt.

Support: **5** talk(s)

> "And with just-in-time routing, the prompt may include only three to five relevant schemas, closer to about 1,000 tokens."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [5:40](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=340s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)

### Durable agent state belongs in files and external systems outside the context window and outside any one agent framework, so it survives resets, crashes, and tool migrations.

Support: **6** talk(s)

> "The state lives in files. It is not trapped inside one model. And this is the single most practical thing I learned all year."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md)

### Dense vector similarity alone is not sufficient retrieval; keyword/lexical methods must be combined with it.

Support: **3** talk(s)

> "By themselves, both searches miss about one in four results. Together, they miss about one in 10."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [4:35](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=275s)

Supporting talks: [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### Agent output quality is capped by the structure and hygiene of the organization's written context — documentation, definitions, provenance, and lifecycle management — which most companies do not maintain.

Support: **6** talk(s)

> "Even if you have really good agents, they're not going to know how to solve these problems if they don't have documentation or skills"
>
> — [Content Is Code](../talks/content-is-code.md), [7:22](https://www.youtube.com/watch?v=yv6xovSsB1U&t=442s)

Supporting talks: [Content Is Code](../talks/content-is-code.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### Verification should be done by a separate agent deliberately denied the producing agent's context, reasoning traces, or model, because self-review is biased.

Support: **5** talk(s)

> "Independent means that the verification agent doesn't see the reasoning traces, doesn't see all the work that the discovery agent has done."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [11:46](https://www.youtube.com/watch?v=imFedndyXYQ&t=706s)

Supporting talks: [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)

## Disagreements

### Does long context actually degrade model performance enough to justify aggressively shrinking the working set?

| Position A | Position B |
|---|---|
| Yes — performance falls off well before the window is full (degradation from ~25% utilization, a 'dumb zone' past 40%, lost-in-the-middle collapsing tool selection to 13.6% at 741 tools), so builders must keep the working set small and never dump whole codebases or scenes into context.<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)* | Not necessarily — controlled experiments recalled distinctive facts reliably up to 800k tokens with no compaction, and the setup sending the most tokens was the cheapest to run because 97% of tokens were cached; the real failure mode is dense retrieval, not context length.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: If length itself is benign, the engineering effort belongs in retrieval quality and cache preservation rather than in routers, truncation, and eviction policies — and much of the tooling built to shrink context is wasted overhead.*

### When a conversation outgrows the window, should the agent compact/summarize it?

| Position A | Position B |
|---|---|
| Yes, but compaction must be server-side and in the exact form the model was trained on, so post-compaction performance is unchanged; auto-compaction runs by default.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* | No — do not compact by default. Either keep the full history (which measured cheaper, faster, and higher-recall than every compaction preset) or clear the context entirely and rehydrate from self-written handoff and state documents, because summarization invalidates the prompt cache and permanently discards content you cannot choose.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* |

*Why it matters: Compaction is on by default in most harnesses; if summarization is a cache-invalidating net loss, the default is costing teams money and recall, and the correct investment is durable file-backed state plus a reset command instead of a summarizer.*

### With hundreds of available capabilities, do you retrieve tools dynamically or eliminate most tools in favor of filesystem skills?

| Position A | Position B |
|---|---|
| Build a semantic router or deferred-tool search: embed the catalog, retrieve K≈5 schemas per request, and keep the full catalog available but out of the prompt (~99% token reduction, TTFT stays flat past 500 tools).<br>*[The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* | Don't route a large tool catalog — collapse it. Production agents ship with only a handful of tools, and a skills folder with progressive disclosure replaces MCP for most use cases at roughly 10x less context overhead; MCP is reserved for auth, process isolation, restricted-environment data, and compute the local machine lacks.<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)* |

*Why it matters: One path buys embedding infrastructure and a retrieval-quality problem tied to tool-description wording; the other buys a filesystem convention with a real security gap (skills execute unisolated on the agent's own machine, from marketplaces with no verification).*

### Should the context an agent needs be precomputed offline into a structured layer, or assembled at query time by an exploring agent?

| Position A | Position B |
|---|---|
| Precompute. Understanding cannot be constructed at query time — build a ranked source-of-truth hierarchy, a semantic layer, and slow/fast profile engines ahead of the question, fed from live systems rather than hand-maintained docs.<br>*[From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* | Let the agent retrieve and explore at request time — agentic retrieval beats single-shot on hard cases with a user-tunable effort knob, and precollected context is structurally capped: if the field wasn't collected, the agent can never get it, whereas a searching agent keeps going.<br>*[On AI and Knowledge](../talks/on-ai-and-knowledge.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)* |

*Why it matters: This determines whether the spend goes into an offline pipeline with cold-start gaps and compounding coverage, or into per-query latency and token burn where frequency, not volume, becomes the cost killer.*

### Does context scaffolding become thinner as models improve, or is layered structure permanent architecture?

| Position A | Position B |
|---|---|
| Thinner. Harness fixes encoding yesterday's model limitations become pure overhead (added latency, broken caching) once the limitation disappears, and prompts should be cut ~50% and made less prescriptive with each step-jump model version.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)* | Permanent. Instructions are probabilistic and a prompt will eventually lose, so identity rules, deterministic output vetoes, ranked semantic layers, and pre-built scaffolding must exist as structure the model physically cannot override — you scaffold first, then turn the model loose.<br>*[Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* |

*Why it matters: It decides whether teams should be deleting context machinery at each model release or hardening it — and whether a migration to a new model is a week of cleanup or a rewrite of load-bearing safety layers.*

## Practical Guidance

**Do:**

- Budget context blocks as an explicit fraction of the window — Codex caps the available-skills list at 2% and truncates beyond it; keep baseline system prompt plus tool definitions under 40% before the first user turn.
- Mark tools as deferred / retrieve them via search or a semantic router once the catalog passes ~50 tools; below 20 tools just load them statically.
- Start K at 5 retrieved tools, run the test set at K=3, 5, and 10, and pick the smallest K that hits your accuracy target.
- Pair BM25/keyword retrieval with dense search — at 400k tokens dense recall dropped to 0% on buried facts while BM25 held 100%.
- Before summarizing anything, check the compression ratio against the prompt cache: you need better than ~50x compression for summarization to pay for the cache invalidation.
- Write agent state to files (handoff docs, history, per-machine directories, shared state changed only via PR) so you can clear context and rehydrate instead of compacting.
- Rank knowledge sources into an explicit hierarchy — semantic layer, then canonical queries, then the database graph — and consult cleanest-first instead of weighting all knowledge bases equally.
- Source agent context from live systems (GitHub, CRM, dbt, Tableau) and log correction events back into it, rather than hand-maintaining .md files against fast-changing enterprise definitions.
- Give the model a fixed catalog to select from rather than open generation — e.g. UI components gated by client app version so a 2.0 card is only offered to 2.0+ clients.
- Grade context by relevance the way rendering grades level-of-detail: send detail near the editing focus, stubs for what's far away.
- Give verification agents a different model, a different methodology, and no access to the producing agent's reasoning traces; default to assuming the finding is false.
- Instrument every turn — tokens, cache hit rate, cost, TTFT, tool calls, user frustration — since it is cheap and most teams skip it, then measure savings against a fixed counterfactual baseline instead of estimating.
- Externalize instructions, tool definitions, and skills as configuration so they can be evaluated and hill-climbed automatically against production traces.
- Supply agents explicit codebase context and constraints up front; Sonar measured >30% fewer tokens consumed per problem.

**Avoid:**

- Dumping the entire codebase, the entire scene, or every connected knowledge base into the agent and letting it thrash.
- Compacting by default — name the specific constraint (e.g. the conversation no longer fits and caching stopped helping) before you compact anything.
- Aggressively clearing old tool outputs: the agent re-retrieves what it already had, raising total cost and tool-call count.
- Connecting an agent to 15 MCP servers, which spends over 100,000 tokens per session on tool definitions alone.
- Assuming a bigger model, a longer context window, or another knowledge base will fix a wrong answer — it won't tell the agent which source is authoritative.
- Adding prompt instructions asking the model to use less context; the context was transmitted and billed before the model read the prompt.
- Hardcoding context into individual agents or giving each agent its own memory system — it produces context sprawl, no single version of truth, and total loss on each framework migration.
- Shipping LLM-generated skills unreviewed; they measurably burn more tokens and reasoning time than human-written ones, and a skill is only as good as the human who wrote it.
- Letting the agent that produced the work grade the work — it self-censors, loses recall, and reports that its own PR is great.
- Holding large combinatorial state (e.g. a seating arrangement for 800 people) in the context window instead of in deterministic compute.
- Keeping a memory layer without provenance, contradiction checks, and active pruning — it degrades into a garbage dump with great search that surfaces stale facts confidently.

## Notable Outliers

- Doing nothing beat every compaction preset at once: keeping the full untouched conversation was cheaper, faster, and higher-recall, because 97% of tokens were cached — while summarizing first dropped correct answers to 32%. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s))
- Distinctive facts were still recalled reliably at 800k tokens with no compaction at all — long context did not rot. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [53:53](https://www.youtube.com/watch?v=WP3hjUXd918&t=3233s))
- Tool-selection accuracy falls from ~78% at 10 tools to 13.6% at 741 tools — roughly one correct tool out of eight — purely from catalog size, not from badly written tools. ([The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [3:57](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=237s))
- About 90% of AI coding spend is input tokens, so shorter answers, max-token caps, and temperature tuning cannot move the bill. ([We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [1:57](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=117s))
- Prompts should shrink about 50% with every step-jump model version — for newer models 'look for where untrusted data hits the trust boundary' is enough. ([Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [9:51](https://www.youtube.com/watch?v=imFedndyXYQ&t=591s))
- Ordering soft human context before numeric constraints in the prompt produces less mechanically slotted prose, because the model commits to the numeric framing first if you reverse it. ([Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [9:58](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=598s))
- Context-window anchoring beats fine-tuning for personas: fine-tuning layers a thin personal signal over vast cultural sediment in the base weights and removes it from audit — the persona is the configuration, not the checkpoint. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [27:12](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1632s))
- Build-vs-rent break-even for web context arrives at just over 15,000 entities or queries, because frequency rather than record volume is the cost driver — owned context compounds while rented decays. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [18:59](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1139s))
- Feeding session transcripts plus current memory state through a periodic batch 'dreaming' process makes the next day's agent sessions measurably more intelligent with no retraining. ([Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [27:07](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1627s))
- Letting the agent browse the knowledge base with bash commands added zero recall over hybrid search and made responses 50% slower. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [30:51](https://www.youtube.com/watch?v=WP3hjUXd918&t=1851s))

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
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Yu Su](../speakers/yu-su.md)

