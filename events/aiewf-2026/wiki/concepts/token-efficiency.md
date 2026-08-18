---
title: "token efficiency"
type: "concept"
slug: "token-efficiency"
tier: "core"
maturity: "consolidating"
talk_count: 15
speaker_count: 18
---

# token efficiency

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **15** talk(s) by **18** speaker(s)

**Definition:** Reducing tokens spent per unit of useful work — trimming tool schemas, prompts, and outputs — treated as a design constraint on agent architecture.

*Also referred to as: token budget optimization, context efficiency, tool schema token overhead, input token compression, token cost accounting, prompt pruning and no-ops, tool definition overhead*

## State of Practice

Token efficiency has moved from a billing concern to a load-bearing architectural constraint, and the field now argues about it with numbers rather than adjectives: 29 tool schemas cost ~3,000 tokens on every call, 15 MCP servers burn 100k tokens per session in definitions alone, a full DOM runs ~20,000 tokens against ~1,800 for a compressed markdown view, and Anthropic cut the Claude Code system prompt by 80%. The consistent empirical finding is that trimming is not a cost-versus-quality tradeoff — narrowing what the model sees usually raises task success too (window-scoped computer use: 62%→80% pass rate at 34% fewer tokens; semantic tool filtering to top-3 both cuts context below 300 tokens and stops wrong-tool selection), which practitioners explain via context rot and a '40% dumb zone'. The dominant mechanisms are progressive disclosure (a ~100-token skill description as a context pointer, ~5k on activation, scripts below that), low tool cardinality with clearly distinct functions, compressed environment representations (accessibility tree or markdown rather than raw DOM or screenshot loops), and routing deterministic work — arithmetic, aggregation, replayable network calls — out of the model into code. Economics sharpened the pressure: at least one speaker tracks token prices as up 76% raw and 29% IQ-adjusted in 2026, reversing the assumed deflation, and frequency rather than record volume is identified as the real cost driver for agentic web context. Unsettled: whether the savings should buy you a cheaper model, whether capability belongs in one context or in isolated sub-agents, and whether spending tokens on model-checking-model verification is efficiency or waste.

## Consensus

### Aggressively narrowing what the model sees improves task accuracy as well as cost — compression is not a quality tradeoff.

Support: **6** talk(s)

> "when you switch the agent computer tool from the built-in one to KU driver the pass rate jumps from 62% to 80% using 34% less tokens"
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s)

Supporting talks: [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### Tool and skill definitions are a per-request tax paid on every call, and the resident definition surface must be budgeted and capped.

Support: **5** talk(s)

> "If it's connected to 15 MCP server, I'm pretty sure it's consuming over 100,000 tokens per session just in tool definitions itself."
>
> — [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s)

Supporting talks: [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)

### Capability should be exposed through progressive disclosure — a short pointer resident in context, with the bulk of the material loaded only when the branch is actually taken.

Support: **4** talk(s)

> "So, this description serves as a kind of context pointer. It sits in the agent's context pointing to another file where the agent can go if it wants more context."
>
> — [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [4:03](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=243s)

Supporting talks: [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md)

### Deterministic work — arithmetic, aggregation, repeatable operations — should be routed out of the model into code or a query engine, which is simultaneously cheaper and more correct.

Support: **3** talk(s)

> "Why would I run 1 + 1 through a multi-billion parameter model instead of one CPU cycle?"
>
> — [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [12:12](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=732s)

Supporting talks: [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)

### Token spend is now a first-order economic constraint on what can ship, not a line item that model-price deflation will absorb.

Support: **4** talk(s)

> "You can't put Fable in front of a customer, um unless that customer has a massive lifetime value. It's just too expensive. So, you need to find a way to create great efficacy while being efficient."
>
> — [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [23:23](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1403s)

Supporting talks: [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)

## Disagreements

### Does a token-efficient harness let you drop to a cheaper model, or does aggressive context trimming only work because a frontier model is filling in the gaps?

| Position A | Position B |
|---|---|
| A well-designed representation and a narrow task scope let a much cheaper model beat a stronger one — compressed markdown plus a cheap model outruns Claude driving by screenshots, DeepSeek V4 Flash is 137x cheaper per task than Fable and narrow scoping makes it reliable, and the harness routinely produces above-baseline results for the model underneath it.<br>*[Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)* | Minimal prompting and thin tool surfaces are a frontier-model privilege: the 80% Claude Code system-prompt reduction ships only to frontier models while older models still receive the full prompt, and replacing MCP with a skills folder is conditioned on having a good base reasoning model.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)* |

*Why it matters: If A is right, token efficiency work compounds into a model-cost reduction and you should engineer the harness and downgrade the model; if B is right, trimming context on a cheap model silently removes the judgment that made the trimming safe, and the savings evaporate into retries.*

### Where should capability live to keep context small — inside one agent via progressive disclosure, or split across isolated small agents that never share a context window?

| Position A | Position B |
|---|---|
| Keep a single general-purpose engine with a handful of tools and layer domain capability on as skills, since production agents like Codex and Claude Code ship with only a handful of tools and skills impose roughly 10x less overhead than the equivalent MCP setup; keep tool cardinality low and each tool's function distinct.<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)* | Piling skills, MCP servers, and tools into one context is inheritance and hits diminishing returns before breaking down; instead compose many narrow domain-specific agents, each a full agent with its own loop and minimal context, talking to each other in English — worth over 80% token efficiency on a given task.<br>*[The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* |

*Why it matters: This determines whether the unit of reuse is a markdown skill file inside one harness or a deployable agent with its own sandbox and model choice, and whether your token budget is spent on resident descriptions or on inter-agent English message passing.*

### Is spending extra tokens on model-checking-model verification a good use of budget?

| Position A | Position B |
|---|---|
| Yes — verify with different models than the generator because every model has its own biases, and route through an executor/validator/critic chain that catches fabricated success responses a single agent reports as done; customers running multi-layered verification report 44% fewer AI-derived production outages.<br>*[In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)* | No — probabilistic systems evaluating each other's work is not verification at all; the only thing that buys real assurance is a deterministic substrate where the model writes a reference to a number and never computes or manipulates it.<br>*[How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)* |

*Why it matters: Cross-model checking multiplies token spend per unit of work by the number of passes; if it does not actually reduce residual error, that entire multiplier is waste that should have gone into deterministic tooling instead.*

## Practical Guidance

**Do:**

- Measure the resident cost of your definition surface before anything else — tool schemas run ~17-200 tokens each and 29 tools cost ~3,000 tokens on every single call.
- Filter tools per request by semantic search to the top three, dropping per-query tool context from thousands of tokens to under 300; in multi-turn conversations actively clear and re-add the registry, since filtering alone does not bound growth.
- Keep baseline system prompt plus tool definitions under 40% of the context window before the first user turn, on the argument that performance degrades past ~25% utilization and a 'dumb zone' begins around 40%.
- Structure skills as three disclosure levels: a description under ~100 tokens, activation content under ~5K, and scripts below that; move reference material used by only one branch out of skill.md behind a context pointer.
- Feed the agent a compressed page representation — accessibility tree or markdown at ~1,800 tokens instead of ~20,000 for the full DOM — supplied alongside a screenshot rather than replacing it.
- Scope the agent's view to a single window rather than the whole desktop; this alone moved pass rate 62%→80% at 34% fewer tokens.
- Let the model decide what to compute and never compute it itself: send arithmetic and aggregation to code or a graph query, which returns a verified result instead of an estimate over top-k chunks and consumes fewer output tokens.
- Supply explicit codebase context and constraints to coding agents — measured at over 30% fewer tokens consumed per problem — and keep the codebase clean, since agents pay a token and reasoning tax to understand messy code.
- Delete no-ops: if the agent would do the thing anyway after you remove the paragraph, remove the paragraph.
- Optimize retrieval for information density per token, not relevance alone, and expose retrieval effort as a latency-versus-quality knob rather than fixing it — single-shot is adequate for easy cases.
- Compress input tokens explicitly and audit agent loops for redundant calls; the inference endpoint cannot see the shape of your workload and will not do this for you.
- Model your cost by query frequency, not record volume — every repeated query costs the same as the first even when nothing changed.

**Avoid:**

- Dumping full page content, raw DOM, or screenshot-scroll loops into the model — subpar results at higher cost, and one screenshot shows only a viewport-sized snippet.
- Attaching many MCP servers by reflex; 15 servers is 100k+ tokens of definitions per session before any work happens.
- Adding model-invoked skills freely — each one's description sits permanently in context, so 100 skills means 100 descriptions on every request, plus evals to prove they fire at the right time.
- Shipping LLM-generated skills unreviewed: they measurably hurt performance by consuming more tokens and more reasoning time than human-written ones.
- Putting examples or hard 'do not do X' constraints in frontier-model system prompts — examples now cap the model's creativity, and negative constraints conflict with later user instructions; give context instead.
- Adding tools with overlapping functions; with all 29 tools visible the model sometimes picks the wrong generic one.
- Treating longer context windows as headroom — context is a budget, and more context is not better.
- Assuming token prices will keep falling; at least one tracker has them up 76% raw and 29% IQ-adjusted in 2026.
- Letting an agent act and validate in the same loop — it rationalizes tool errors into confident success responses, so the tokens spent on self-checking buy nothing.
- Cutting refresh frequency or capping result counts to control cost — that degrades the knowledge work itself rather than the pipeline.

## Notable Outliers

- Token inefficiency is a symptom of missing expertise, not a prompting problem: intelligence brute-forces the search space, while expertise compresses it by having learned the shortcuts — so continual learning, not context engineering, is the real fix. ([Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md), [9:17](https://www.youtube.com/watch?v=I6aiEf3aEFQ&t=557s))
- The 80% system-prompt token reduction ships only to frontier models; older models still receive the full prompt, because the minimized version depends on frontier-level judgment. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [24:53](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1493s))
- The file edit tool exists for UI rendering reasons, not model capability, and could probably be removed today for experienced auto-mode users without harm. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [30:08](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1808s))
- Query frequency, not record volume, is the dominant cost driver for agentic web context — every repeated query costs the same as the first even when the answer is unchanged. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [13:32](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=812s))
- Comparing context-as-a-service to web search on sticker price is unfair, because search-based approaches incur significant additional token burn just to structure raw results into usable data. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [12:14](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=734s))
- Splitting a process into separate skills so the agent sees only one step at a time increases the legwork it does on the current step — hiding future context improves behavior, not just cost. ([Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md), [15:46](https://www.youtube.com/watch?v=UNzCG3lw6O0&t=946s))
- The industry will swing from maximizing token consumption to cost optimization, repeating the ROI reckoning that followed Snowflake and Databricks adoption. ([How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [18:03](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=1083s))
- Over-provisioning a sandbox warm pool still saves money in RL training because sandbox compute is two to four times cheaper than GPU time — efficiency means moving idle cost off the expensive resource, not minimizing it everywhere. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [13:48](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=828s))

## All Talks

- [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)
- [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md)
- [Building Great Agent Skills: The Missing Manual](../talks/building-great-agent-skills-the-missing-manual.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)
- [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md)
- [Intelligence + Continual Learning = Expertise](../talks/intelligence-continual-learning-expertise.md)
- [On AI and Knowledge](../talks/on-ai-and-knowledge.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)
- [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)

## Speakers

- [Cat Wu](../speakers/cat-wu.md)
- [Dillon DuPont](../speakers/dillon-dupont.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [Francesco Bonacci](../speakers/francesco-bonacci.md)
- [Kushan Raj](../speakers/kushan-raj.md)
- [Marah Abdin](../speakers/marah-abdin.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Paul Klein IV](../speakers/paul-klein-iv.md)
- [Robert McHardy](../speakers/robert-mchardy.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Tariq Shaukat](../speakers/tariq-shaukat.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yu Su](../speakers/yu-su.md)

