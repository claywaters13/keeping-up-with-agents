---
title: "inference cost optimization"
type: "concept"
slug: "inference-cost-optimization"
tier: "supporting"
maturity: "consolidating"
talk_count: 32
speaker_count: 43
---

# inference cost optimization

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **32** talk(s) by **43** speaker(s)

**Definition:** Managing the unit economics of serving models — cost per token, per query, and per agent run — as a first-order product constraint.

*Also referred to as: inference cost management, inference cost economics, token economics, cost efficiency per token, token cost optimization, batch inference pricing, cost and latency optimization*

## State of Practice

Cost has moved from a finance concern to an architectural one — it is now monitored in production like an SLA and ranks second only to quality in model selection. The dominant technical finding is that spend is an input-side problem: roughly 90% of coding-agent cost is context rather than generation, so the levers that actually move the bill are prompt/KV caching, retrieval that sends 5K tokens instead of 45K, and structuring context to grow with hierarchy depth rather than instance count. Second is heterogeneity — nobody credible defends sending all traffic to the top model, and the working pattern is a cheap router or event gate in front of tiered models, with post-trained small or open-weight models absorbing the large majority of tasks that do not need frontier intelligence. Third, a surprising amount of what teams pay LLMs to do (arithmetic, set operations, dedup, deterministic SQL, format conversion, reranking) belongs in ordinary code, which is simultaneously cheaper and more correct. The uncomfortable macro fact several speakers independently reported: per-token prices keep falling while per-session token consumption grows faster, so bills rise anyway — Uber exhausted an annual token budget in month four, and one company spent $500M on Claude in a single month because usage limits were never set. What remains genuinely unsettled is whether the cure is owning the inference stack or staying a disciplined, model-agnostic buyer.

## Consensus

### Routing traffic across tiered models by task difficulty — rather than sending everything to the frontier model — is the highest-leverage cost lever available to application teams.

Support: **7** talk(s)

> "When you triage an email inbox, if we're charging you to do that on Opus, we're ripping you off and ourselves."
>
> — [Notion's Token Town](../talks/notions-token-town.md), [10:19](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=619s)

Supporting talks: [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Notion's Token Town](../talks/notions-token-town.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)

### Cost is overwhelmingly an input-token problem, so reducing what you send (retrieval, context structure, compression) dominates any optimization of the model's output.

Support: **6** talk(s)

> "This is the most important slide. 90% of your AI cost is input."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [1:57](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=117s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)

### Per-token prices keep falling while per-session token consumption grows faster, so total spend rises and must be budgeted and instrumented explicitly.

Support: **6** talk(s)

> "You can look at it, you know, the difference between GPT-4 when it first launched and GPT-5.5 is is is much, much cheaper per token, but at the same time the amount of tokens in an individual session has gone up exponentially as well."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [14:13](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=853s)

Supporting talks: [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Notion's Token Town](../talks/notions-token-town.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)

### Work that is exact and reproducible — arithmetic, set operations, counting, dedup, deterministic SQL, format conversion, reranking — should be deterministic code, not model calls; this is cheaper and more correct at the same time.

Support: **4** talk(s)

> "Why would I run 1 + 1 through a multi-billion parameter model instead of one CPU cycle?"
>
> — [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [12:12](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=732s)

Supporting talks: [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Notion's Token Town](../talks/notions-token-town.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### Post-training or curating a smaller/open model for a narrow task reaches the quality bar at a fraction of frontier cost and latency, and is now cheap enough to be a routine engineering decision rather than a research program.

Support: **5** talk(s)

> "take an open model and like specialize it to automate finance within like a week or two to get like better performance than like Opus at a fraction of the cost of Haiku"
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [13:39](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=819s)

Supporting talks: [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md)

### Prompt and KV cache hit rate is a first-order economic variable — high cache rates can make the token-heaviest configuration the cheapest to run.

Support: **4** talk(s)

> "we were still getting the best results out of it because 97% of the tokens that we had were cached"
>
> — [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [52:08](https://www.youtube.com/watch?v=WP3hjUXd918&t=3128s)

Supporting talks: [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)

## Disagreements

### Does compacting, summarizing, or trimming conversation history and tool outputs actually reduce agent cost?

| Position A | Position B |
|---|---|
| Yes — cache the system prompt, cap history with a sliding window, summarize what falls out, store large tool results outside the context, and compact once you cross a token threshold (e.g. ~150K).<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)* | No — compaction invalidates the provider's prompt cache (you must compress >50x to break even) and clearing tool outputs makes the agent re-retrieve what it already had, so keeping the full history won on cost, latency, and recall simultaneously; compaction is only justified once a named constraint like a too-small context window forces it.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* |

*Why it matters: These prescribe opposite defaults for every agent framework's context manager: one ships compaction on by default, the other treats it as a regression that silently raises the bill and lowers recall. The answer depends entirely on whether your provider's cache is live, which most teams never measure.*

### Should a company past product-market fit own its inference stack, or keep buying inference and compete on product?

| Position A | Position B |
|---|---|
| Own it. Rented endpoints cannot see the shape of your workload, prepaid credits remove the periodic-bill anchor that disciplines spend, audits red-line third-party dependencies, and closed providers capture optimization gains as margin rather than passing them through — so unit costs only fall reliably if you run open weights yourself.<br>*[Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)* | Keep buying. Applied AI companies should not try to win on token economics at all — win on product, data flywheels, UI, and orchestration; inference and model serving is the clear buy market, and hosted providers are shipping large step-function price cuts (frontier-level intelligence at half the prior cost, $1/$6 per million tokens) that a self-hosted team cannot match.<br>*[Notion's Token Town](../talks/notions-token-town.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)* |

*Why it matters: This determines whether you hire an inference/kernel team and buy hardware, or spend that headcount on evals and product. It also changes your negotiating posture: the buy camp's leverage comes from retained optionality across labs, the own camp's from not needing a lab at all.*

### Is uncapped agent looping a rational purchase, or should agent runs be bounded by construction?

| Position A | Position B |
|---|---|
| Bound it. Replace multi-step agentic loops with two-or-three-step plan-then-resolve pipelines so per-query cost stays flat regardless of system scale, always set a max-iteration cap on tool loops, and profile per-tool call counts with observability before shipping.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)* | Spend it. Running a coding agent in a loop works out to about $10.42/hour against engineer salaries, high throughput is worth it precisely because it lets you run five or six parallel approaches and pick the best, and duplicating work across local plus staging agents doubles token usage but buys reliability.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)* |

*Why it matters: The bounded camp is optimizing a production per-query unit cost that must hold at 460,000-entity scale; the spend camp is optimizing internal developer throughput where labor is the expensive input. Applying either discipline to the other's workload is a large, avoidable error.*

## Practical Guidance

**Do:**

- Cache the system prompt (and tool definitions and message prefixes where the provider supports it) and treat cache hit rate as a monitored metric — 96-97% hit rates were reported as the thing that made token-heavy configurations affordable.
- Put a cheap model or a cheap event detector in front of expensive ones as the router; Notion's auto-model absorbs ~75% of AI traffic and Abridge gates heavy order-matching models behind cheap in-conversation event triggers.
- Fix retrieval before touching model choice: hybrid semantic + keyword search cut miss rate from ~25% each alone to ~10% combined, taking a coding query from 83K to 4.9K tokens.
- Use a weighted heuristic reranker (e.g. 50% semantic / 30% keyword / 20% recency) at 0.4ms instead of LLM-based reranking that adds 2-3 seconds per query.
- Design context to scale with hierarchy depth rather than instance count — Phaidra held ~9,000 tokens per query at both 64 GPUs and 460,000 GPUs.
- Cap max tool-loop iterations and run observability over per-tool call counts and durations before deploying to production.
- Use batch mode for non-urgent work: 50% fewer token cost with results inside 24 hours.
- Pull exact operations out of the model entirely — set logic, counting, dedup across near-identical names, deterministic SQL, CSV-to-PDF conversion, and all arithmetic.
- Post-train a small or open-weight model on your own harness for narrow tasks; a 1,000-step GLM-5 RL run on real agentic coding tasks costs ~$50K, and 10,000-10M synthetic samples suffices to fine-tune a tiny (50M-500M param) model to high reliability.
- Stack the standard serving optimizations: 4-bit quantization from 16-bit, speculative decoding, and KV cache reuse (reported 18x faster prefill at 96%+ hit rate).
- Evaluate vendors on whole trajectories, not single-call price or latency — Notion chose Parallel for web search despite it not being cheapest per call.
- Set per-employee and per-org usage limits on lab dashboards before rollout, and instrument actual queries against a counterfactual baseline rather than estimating savings.

**Avoid:**

- Instructing the model in the prompt to 'send less context' — the context was already transmitted and billed before the model read the instruction.
- Tuning max_tokens, temperature, or answer length as a cost strategy when ~90% of spend is on the input side.
- Compacting or clearing tool outputs by default; summarization only pays if you compress more than 50x, and clearing outputs makes the agent re-retrieve information it already had.
- Sending all traffic to the newest frontier model, and specifically using an overpowered model for high-frequency routine transactions — that defeats the entire cost-reduction purpose of the system.
- Leaving tool loops uncapped; they can run 10-20 times or go infinite.
- Vector/semantic search alone over near-identical entity names — recall collapses and models invent phantom entities while silently dropping real ones. BM25 kept 100% recall at 400K tokens where dense retrieval hit 0%.
- Sharding long entity enumerations across parallel LLM calls in mission-critical paths — it produces hallucinated and silently omitted items.
- Assuming a per-token price cut lowers your bill; a reasoning-model upgrade at identical per-token pricing burned 3x the output tokens.
- Taking a volume discount that locks you to one provider — the optionality to walk is the leverage, and your model supplier is structurally your competitor.
- Prepaid credit purchases with no periodic-bill anchor, and unsecured API keys — one speaker watched a stolen key drain $7,000 to $8,000 and climbing.
- Assuming local or on-device inference is automatically cheaper: DRAM cost, not compute, is the binding edge constraint and it is getting worse, and a 32K local window cut chat recall from 92-95% to 33%.
- Buying a headline savings number without checking the baseline — the widely-cited 94% token cut was measured against a worst-case full-file-read baseline, not against a modern agentic tool.

## Notable Outliers

- On DeepSeek, the configuration that sent the most tokens was the cheapest to run, because 97% of those tokens were cache hits — inverting the intuition that fewer tokens means lower cost. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [52:08](https://www.youtube.com/watch?v=WP3hjUXd918&t=3128s))
- GLM used twice as many tokens as Opus on a real repo bug but cost half as much, cleaned up dead code, and verified the build — while Opus left type errors and broke the production build. ([Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [9:44](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=584s))
- Restructuring context around hierarchy depth cut a 1GW-scale validation pass from 116 million tokens to 390,000 — roughly 300x — while correctness went from ~30% to 100%. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s))
- On 20-30 step browser tasks, a small purpose-built computer-use model costs about 80 cents per task versus $230 for a frontier model — the accuracy edge is statistical noise, the cost gap is the product. ([Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [18:07](https://www.youtube.com/watch?v=Ki980nV0__0&t=1087s))
- Data curation alone reduces inference cost by shortening responses — roughly 35x fewer flops per correct answer versus Qwen 3.5 — making pre-training data quality an inference-economics lever, not just a training one. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [8:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=530s))
- DRAM cost, not compute, is the binding constraint on edge inference, and it is moving the wrong way — Raspberry Pi 6GB is up ~2.5x since launch and some phone makers are shipping less RAM this year than last. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [3:04](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=184s))
- One of the largest US retailers spent close to $200 million on inference with Anthropic before deciding to build its own infrastructure; a separate company spent $500 million on Claude in a single month purely because usage limits were never set on the dashboard. ([Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [0:00](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=0s))

## All Talks

- [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)
- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)
- [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)
- [From Ambient Documentation to Clinical Intelligence](../talks/from-ambient-documentation-to-clinical-intelligence.md)
- [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)
- [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)
- [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)
- [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)
- [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)
- [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)
- [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md)
- [Notion's Token Town](../talks/notions-token-town.md)
- [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)
- [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)
- [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)
- [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)
- [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)
- [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)
- [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)
- [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)
- [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)
- [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Alex Cheema](../speakers/alex-cheema.md)
- [Alexander Embiricos](../speakers/alexander-embiricos.md)
- [Apoorva Joshi](../speakers/apoorva-joshi.md)
- [Ari Morcos](../speakers/ari-morcos.md)
- [Armanas Povilionis](../speakers/armanas-povilionis.md)
- [Carter Abdallah](../speakers/carter-abdallah.md)
- [Chaitanya Asawa](../speakers/chaitanya-asawa.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Cormac Brick](../speakers/cormac-brick.md)
- [Dan Fu](../speakers/dan-fu.md)
- [Dat Ngo](../speakers/dat-ngo.md)
- [Dhruv Batra](../speakers/dhruv-batra.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Jeffrey Lee-Chan](../speakers/jeffrey-lee-chan.md)
- [Joanne Song](../speakers/joanne-song.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Keegan McCallum](../speakers/keegan-mccallum.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Lucas Atkins](../speakers/lucas-atkins.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Olive Song](../speakers/olive-song.md)
- [Omar Solano](../speakers/omar-solano.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Ramesh Raskar](../speakers/ramesh-raskar.md)
- [Richard Socher](../speakers/richard-socher.md)
- [Rishi Desai](../speakers/rishi-desai.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Saoud Rizwan](../speakers/saoud-rizwan.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Shafik Quoraishee](../speakers/shafik-quoraishee.md)
- [Shlok Khemani](../speakers/shlok-khemani.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)
- [Vasant Kearney](../speakers/vasant-kearney.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)
- [Vivek Muppalla](../speakers/vivek-muppalla.md)
- [Will Brown](../speakers/will-brown.md)

