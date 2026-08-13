---
title: "context engineering"
type: "concept"
slug: "context-engineering"
tier: "core"
maturity: "consolidating"
talk_count: 29
speaker_count: 32
---

# context engineering

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **29** talk(s) by **32** speaker(s)

**Definition:** The practice of deciding what information enters a model's context and in what form, treating context assembly as a first-class engineering discipline rather than prompt wording.

*Also referred to as: context construction, context assembly and working sets, context scaffolding, just-in-time context injection, prompt and context optimization, content engineering, web context engineering*

## State of Practice

The consensus position at this conference is that model capability has stopped being the binding constraint and context assembly has become it — speakers from OpenAI, Anthropic, Tesla, Microsoft, Snapchat and half a dozen startups independently made some version of the claim that the same weights produce 2x or 100x results depending on how the work is wired. The second consensus is that context is a strictly finite budget to be spent, not a window to be filled: the referenced context-rot result (degradation past ~25% utilization), Codex's 2% cap on the available-skills list, the lost-in-the-middle collapse of tool-selection accuracy from ~78% at 10 tools to 13.6% at 741, and the observation that CLAUDE.md plus skills plus MCPs can consume ~25% of context before the task even arrives, all converge on the same engineering move — load less, later. Progressive disclosure is now the default technique: deferred tools behind a tool-search call, semantic tool routing at K≈5, skill frontmatter under 100 tokens, local code indexes replacing whole-file reads. State is moving out of the context window entirely and into durable artifacts — files on disk, session logs, planning docs, semantic layers, 'company brains' — on the theory that anything living only in the model's context is lost at compaction, crash, or harness migration. Where the field is genuinely unsettled is authorship and timing: whether that durable context should be hand-written markdown a human prunes or a pipeline that derives it from systems of record, and whether understanding should be precomputed offline or retrieved just-in-time.

## Consensus

### Model capability is no longer the limiting factor for production agents; the context and harness around the model are.

Support: **10** talk(s)

> "The 2X people and the 100X people are using the exact same Claude. Same weights, same context window, same API. So, the leverage is not in the weights. It's in how you wire the work."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)

### Context is a finite budget, not a container to fill — more context actively degrades output quality, and a bigger context window is not a fix for bad answers.

Support: **9** talk(s)

> "Context is a budget. Context is almost like a limited resource that we need to carefully filter information. Definitely the longer context doesn't mean better."
>
> — [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [25:36](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=1536s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)

### Capabilities (tools, skills, code) should be disclosed progressively and loaded just-in-time rather than declared up front in every request.

Support: **5** talk(s)

> "I mean, this is not a new software idea. We have used lazy loading, just-in-time compilation, and on-demand resource loading from years. We are just applying the simple and same principle to the LLM context."
>
> — [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [11:13](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=673s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)

### Durable agent state belongs in files, docs, or session logs outside the context window, so that work survives compaction, crashes, and harness migrations.

Support: **5** talk(s)

> "The state lives in files. It is not trapped inside one model. And this is the single most practical thing I learned all year."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### A context corpus without curation, provenance, and active pruning degrades into confidently wrong output; context needs lifecycle management like code.

Support: **6** talk(s)

> "a brain nobody curates becomes a garbage dump with great search. Retrieval will surface a stale fact with total confidence."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [13:58](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=838s)

Supporting talks: [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Content Is Code](../talks/content-is-code.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)

### Retrieval itself is largely solved; the hard and valuable part is structuring, ranking, and understanding what gets retrieved.

Support: **4** talk(s)

> "The problem was never the missing of data, the retrieval. The problem is like the missing understanding."
>
> — [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [1:46](https://www.youtube.com/watch?v=Btk8wDUVs74&t=106s)

Supporting talks: [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md)

### Verification must run in a context separate from generation — the agent that produced the work should not be the one that checks it, and ideally should not even expose its reasoning to the checker.

Support: **5** talk(s)

> "Independent means that the verification agent doesn't see the reasoning traces, doesn't see all the work that the discovery agent has done."
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [11:46](https://www.youtube.com/watch?v=imFedndyXYQ&t=706s)

Supporting talks: [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)

## Disagreements

### Should an agent's context be hand-authored and human-maintained, or continuously derived from live systems and self-improvement loops?

| Position A | Position B |
|---|---|
| Context artifacts are written and pruned by humans. Skill files are the unit of work — one capability, written down clearly — and machine-generated ones are measurably worse; asking the model to improve its own instructions yields micromanagement.<br>*[Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [Content Is Code](../talks/content-is-code.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)* | Hand-maintained markdown cannot keep pace with how fast enterprise definitions and processes change; context should be sourced from live systems (dbt, CRM, GitHub, Tableau) and instructions should be hill-climbed automatically from evals and production traces, which outperform handwritten ones.<br>*[Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* |

*Why it matters: It determines whether you staff humans to write and prune skills as a permanent job, or build a derivation pipeline plus approval gate — and whether your context goes stale between releases or drifts without anyone noticing.*

### When context fills up, should the system summarize what happened or discard it and re-read durable artifacts?

| Position A | Position B |
|---|---|
| Compact automatically, server-side, in the form the model was trained on so post-compaction performance is unchanged; periodic batch summarization of transcripts into memory ('dreaming') makes later sessions smarter.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* | Never compact. Compaction is slow, you cannot choose what survives, and what it drops is gone — clear context entirely and re-read self-written handoff files; extracting decisions into durable docs up front beats letting an LLM summarize the session afterward.<br>*[I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* |

*Why it matters: If summarization is lossy in ways you cannot control, every long-running agent silently loses the specific constraint that mattered; if it is not, writing and maintaining handoff files is wasted engineering.*

### Should contextual understanding be precomputed offline, or assembled just-in-time at query time?

| Position A | Position B |
|---|---|
| Understanding cannot be constructed at query time and must be computed ahead of time — slow and fast engines running offline over user history, a curated semantic layer consulted cleanest-first, structure defined before the agent is turned loose, and an owned context pipeline rather than rented per-query lookups.<br>*[From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)* | Assemble at runtime: retrieve tool schemas semantically per request, defer tools behind a search call, disclose skills progressively, and let an agentic retrieval loop reflect on whether the information need is satisfied before returning.<br>*[The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md)* |

*Why it matters: Precomputation buys latency and consistency but has a cold-start hole and cannot answer what it did not anticipate; runtime assembly covers the long tail but pays per-request latency and can silently retrieve the wrong slice.*

### Does adding another data source or knowledge base make an agent better or worse?

| Position A | Position B |
|---|---|
| Additional sources are cheap and purely additive — the surface only grows, and combining retrieval methods and company-wide ambient grounding measurably beats narrow curated datasets.<br>*[From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)* | Adding knowledge bases and MCP servers is precisely what does not fix bad answers; sources must be ranked into a hierarchy, irrelevant tools removed from the choice set, and the corpus actively pruned.<br>*[Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* |

*Why it matters: It decides whether the roadmap for a struggling agent is 'connect more systems' or 'rank and cut what is already connected' — and the two spend engineering effort in opposite directions.*

## Practical Guidance

**Do:**

- Cap the available-skills/tool-description block as a fraction of the context window — Codex caps it at 2% and progressively truncates beyond that.
- Mark rarely-used tools as deferred so they are reachable via tool search rather than resident in the context window.
- Keep baseline system prompt plus tool definitions under 40% of the context window before the first user turn.
- Past ~50 tools in production, route semantically and inject only the top-K schemas; K=5 is the recommended default, and below 20 tools skip the router entirely.
- Keep agent state in files on disk and recover by clearing context and re-reading handoff/history files rather than compacting.
- Rank sources of truth explicitly — semantic layer and canonical queries first (~80% of cases), database graph last.
- Give the verifier a different context than the generator: deny it the discovery agent's reasoning traces and have it assume the finding is false by default.
- Supply the model a fixed catalog to select from (e.g. UI components gated by client app version) so it can never emit something the client cannot render.
- Write goal prompts that are concrete and verifiable rather than long essays, since the loop only terminates when the model can detect the goal is met.
- Use commander's intent — tell the agent why it should do something, not just what to do.
- Attach citations back to source systems so a human can follow a claim to its origin.
- Combine retrieval methods rather than relying on vector similarity alone; one team weighted 50% semantic / 30% keyword / 20% recency.
- Log correction events and feed them back into agent context as an explicit feedback loop.
- Build your own eval before optimizing context, so model and harness choices are made on your own cost/performance frontier.
- Write tool descriptions in the words users actually use, including intent, action, and key entities — routing quality is bounded by description quality.
- Remove harness workarounds once a model no longer needs them; stale compensations become pure latency and cache-invalidation overhead.

**Avoid:**

- Dumping the entire codebase into the agent's context — it thrashes, explores, and burns tokens.
- Connecting an agent to ~15 MCP servers, which can cost over 100,000 tokens per session in tool definitions alone.
- Reaching for a bigger model or a longer context window when the agent gives a bad answer.
- Letting each agent keep its own memory system, which causes context sprawl and prevents a single version of truth.
- Hardcoding context into agents or trapping it inside one agent framework, since the framework will churn within about a year.
- Optimizing output tokens, max_tokens, or temperature to cut coding spend — roughly 90% of the cost is input.
- Instructing the model in the prompt to send less context; the context was transmitted and billed before the prompt was read.
- Mass-generating skills with an LLM — published measurements show generated skills consume more tokens and more reasoning time than human-written ones.
- Asking one system prompt to do four different jobs (situational mode, expressive voice, hard identity rules, output check).
- Asking the model to improve its own prompts, which produces micromanagement because it was trained on human-produced management material.
- Holding large combinatorial state (e.g. an 800-person seating arrangement) in the context window instead of deterministic code.
- Treating a transcript as proof of what happened instead of a receipt recording what was allowed, attempted, executed, and confirmed.

## Notable Outliers

- Tool-selection accuracy collapses from ~78% at 10 tools to ~40% at 100 tools to 13.6% at 741 tools — roughly one correct tool in eight — and the cause is lost-in-the-middle attention, not badly written tools. ([The 100-Tool Agent Is a Trap](../talks/the-100-tool-agent-is-a-trap.md), [3:57](https://www.youtube.com/watch?v=vh2VGuQ3zhY&t=237s))
- Roughly 25% of a coding agent's context is consumed by CLAUDE.md, skills, and MCPs before any task-specific content arrives, which is the argument for keeping spec/goal/history context in a separate orchestration layer. ([Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [5:19](https://www.youtube.com/watch?v=9arM9b7JgOo&t=319s))
- Prompts should shrink about 50% with each step-jump model version; for newer models 'look for where untrusted data hits the trust boundary' replaces a long prescriptive prompt. ([Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [9:51](https://www.youtube.com/watch?v=imFedndyXYQ&t=591s))
- For persona systems, context-window anchoring is strictly better than fine-tuning, because fine-tuning layers a thin personal signal over vast cultural sediment in ways no longer open to audit — the persona is the configuration, not the checkpoint. ([The Miranda Hypothesis: How Hamilton Poisoned Persona Evals](../talks/the-miranda-hypothesis-how-hamilton-poisoned-persona-evals.md), [27:12](https://www.youtube.com/watch?v=IJXjTLPzvAU&t=1632s))
- Supplying explicit codebase context and constraints cut tokens consumed per problem by over 30%, and cleaning a codebase measurably reduced the tokens and reasoning needed for identical agentic tasks. ([In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [10:45](https://www.youtube.com/watch?v=VrpEyglYgeU&t=645s))
- Routing to the right metric definition based on who is asking — per-team and per-individual preference — is an open research problem that neither semantic layers nor agent memory solves. ([Enterprise Agents Have a Structure Problem](../talks/enterprise-agents-have-a-structure-problem.md), [11:03](https://www.youtube.com/watch?v=B8l81jhvHbI&t=663s))
- Retrieval effort should be a user-facing knob because it is a direct latency-versus-quality tradeoff, and retrieval should be optimized for information density per token rather than relevance alone. ([On AI and Knowledge](../talks/on-ai-and-knowledge.md), [10:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=624s))
- Owning a scraping pipeline beats renting context-as-a-service past roughly 15,000 entities or queries, because query frequency rather than record volume is the cost driver — owned context compounds while rented decays. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [18:59](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=1139s))
- Whether an action should be approved cannot be decided from the action alone — deleting a file is acceptable or not depending on whether the user asked for it, so approval requires task context. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [14:25](https://www.youtube.com/watch?v=shRR1e2HXMk&t=865s))

## All Talks

- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Content Is Code](../talks/content-is-code.md)
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
- [Matt Dailey](../speakers/matt-dailey.md)
- [May Walter](../speakers/may-walter.md)
- [Nicholas Arcolano](../speakers/nicholas-arcolano.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Ryan Marten](../speakers/ryan-marten.md)
- [Sohail Shaikh](../speakers/sohail-shaikh.md)
- [Tariq Shaukat](../speakers/tariq-shaukat.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Yu Su](../speakers/yu-su.md)

