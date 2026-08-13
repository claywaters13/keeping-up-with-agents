---
title: "inference cost optimization"
type: "concept"
slug: "inference-cost-optimization"
tier: "supporting"
maturity: "consolidating"
talk_count: 25
speaker_count: 34
---

# inference cost optimization

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **25** talk(s) by **34** speaker(s)

**Definition:** Managing the unit economics of serving models — cost per token, per query, and per agent run — as a first-order product constraint.

*Also referred to as: inference cost management, inference cost economics, token economics, cost efficiency per token, token cost optimization, batch inference pricing, cost and latency optimization*

## State of Practice

Cost stopped being a finance problem and became an engineering constraint monitored in production like an SLA — second only to quality in the 2026 survey, with 40% of respondents saying it regularly shapes how ambitiously they use AI. The dominant realization is that per-token price is the wrong unit: prices fall every generation while per-session token consumption grows exponentially (reasoning upgrades that keep list price flat but emit 3x output tokens, agent loops that resend full histories), so the levers that actually move spend are input-side — prompt caching, capping tool-loop iterations, keeping tool results out of context, and architecting retrieval so context grows with hierarchy depth rather than instance count. Tesco's measurement that ~90% of AI coding spend is input tokens and Phaidra's 116M→390K tokens per validation pass are the canonical numbers. A second consensus is that difficulty-based routing is mandatory — nobody credible defends sending inbox triage to Opus — and that a large class of work (arithmetic, deterministic SQL, set logic, file conversion, reranking) should never touch a model at all; a 50/30/20 weighted heuristic reranker at 0.4ms beat LLM-as-judge reranking outright. Open-weight and post-trained small models are now the standard cost floor: GLM using 2x tokens at half the cost of Opus and beating it on build correctness, internal LLM gateways cutting spend nearly in half, a post-trained open model beating Opus on a finance task at a fraction of Haiku's price. What remains genuinely unsettled is the ownership question — whether to rent frontier APIs, self-host, or run locally — and whether deliberately buying reliability with redundant tokens (parallel attempts, verification agents, loops at $10.42/hour) is good economics or the thing that produces $200M inference bills and annual budgets exhausted in month four.

## Consensus

### Not all traffic deserves the frontier model; agents must route by task difficulty across a tier of models, and a cheap model can serve as the router.

Support: **5** talk(s)

> "And not all traffic is equal. It is a huge miss to send all of these to the latest opus model."
>
> — [Notion's Token Town](../talks/notions-token-town.md), [10:19](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=619s)

Supporting talks: [Notion's Token Town](../talks/notions-token-town.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)

### Cost is dominated by what you put into the context window, not by model choice or output length, so the highest-leverage optimization is sending less input.

Support: **6** talk(s)

> "This is the most important slide. 90% of your AI cost is input."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [1:57](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=117s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)

### Work that can be expressed as deterministic code — arithmetic, set operations, SQL, file conversion, reranking — should be routed to code rather than run through a model, because it is simultaneously cheaper and more correct.

Support: **4** talk(s)

> "Why would I run 1 + 1 through a multi-billion parameter model instead of one CPU cycle?"
>
> — [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [12:12](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=732s)

Supporting talks: [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Notion's Token Town](../talks/notions-token-town.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### Falling per-token prices do not translate into falling bills, because tokens consumed per session grow faster than prices drop — so cost must be budgeted and monitored as a first-class production constraint.

Support: **6** talk(s)

> "it turns out that infinite intelligence still comes with a usagebased bill."
>
> — ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [8:16](https://www.youtube.com/watch?v=RGe6EjucbzI&t=496s)

Supporting talks: ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Notion's Token Town](../talks/notions-token-town.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)

### Open-weight and specialized small models now deliver comparable task outcomes at a fraction of frontier cost, even when they burn more tokens to get there.

Support: **6** talk(s)

> "GLM used twice as many tokens but only cost half as much."
>
> — [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [9:44](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=584s)

Supporting talks: [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Notion's Token Town](../talks/notions-token-town.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)

## Disagreements

### Should serious AI products rent inference from frontier APIs, or own the inference stack?

| Position A | Position B |
|---|---|
| Own it. Rented endpoints are structurally wasteful (the endpoint cannot see the shape of the workload), prepaid credits remove the utility-bill anchor that disciplines spend, closed providers capture optimization gains as margin rather than passing them through, and audit/reproducibility requirements fail third-party dependency review. Enterprises should stand up their own infrastructure or internal gateways over open models.<br>*[Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* | Rent, and don't try to compete on token economics. Applied AI companies should win on product, data flywheels, UI, and orchestration while staying model-agnostic across providers; inference and model serving is the clear buy market, and frontier vendors are cutting prices fast enough (GPT-5.5-level intelligence at half cost, $1/$6 per million) that owning the stack is a distraction.<br>*[Notion's Token Town](../talks/notions-token-town.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* |

*Why it matters: This determines whether an AI org staffs a GPU/serving team and takes on capex, or invests the same headcount in eval infrastructure and multi-provider routing. It also changes the negotiating posture with labs: owners bargain on credible walk-away, renters bargain on eval partnerships and volume.*

### Should inference default to cloud, or move to local and on-device execution?

| Position A | Position B |
|---|---|
| Local. Cloud round-trips are expensive and too slow for real-time budgets (a 16ms frame at 60Hz), most daily tasks will run on a laptop within a year, ~90% of tasks don't need frontier intelligence, and reaching the majority of devices requires 50M–500M parameter models rather than cloud calls at all. Running the index and search locally is itself a design advantage.<br>*[Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)* | Cloud. For most use cases hosting in the cloud makes more sense than running locally, because local hosting makes you responsible for uptime; the per-agent cost problem is better solved by sleep-and-wake architecture than by relocating compute, and the local-vs-cloud distinction should disappear entirely with the agent choosing its own environment.<br>*[The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* |

*Why it matters: It decides whether cost engineering targets DRAM and quantization on constrained devices or scheduling and idle-compute reclamation in a datacenter — and whether product teams must ship a per-hardware model configuration story at all.*

### Is deliberately spending more tokens to buy reliability — parallel attempts, redundant reviewer agents, uncapped loops — good economics?

| Position A | Position B |
|---|---|
| Yes. Running local plus staging agents roughly doubles token usage and is worth it for reliability; high throughput matters precisely because it lets you run five or six parallel approaches and pick the best; a manager agent with separate context is worth its tokens because a coding agent grading its own PR is biased toward success.<br>*[Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* | No. Stacking loops on loops and orchestrating quality problems away with more tokens does not survive contact with a company-scale budget; redundant LLM calls on work that doesn't need a model is how teams become token poor; and rented-endpoint agent loops are exactly where waste is structural — the observed failure mode is a year's token budget exhausted in month four.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Notion's Token Town](../talks/notions-token-town.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)* |

*Why it matters: If redundancy is cheap insurance, the right move is more parallel rollouts and more verification agents; if it isn't, the same reliability must come from deterministic verifiers, static checks, and capped loops — a completely different harness design and a different per-engineer token budget.*

## Practical Guidance

**Do:**

- Cache the system prompt (and where possible the tool prompt and messages) — it is provider-agnostic, not framework-specific, and reduces the payload on every call after the first
- Set a maximum iteration count on every tool loop; uncapped loops observed running 10–20 times or going infinite
- Store large tool results outside the context and pass a summary, rather than re-sending the full result to the model on each loop iteration
- Use a cheap model as the router that decides which model handles each request (e.g. Haiku for cheap work, Sonnet for harder)
- Design retrieval so context grows with hierarchy/tree depth rather than instance count — Phaidra held ~9,000 tokens per query at both 64 and 460,000 GPUs
- Replace LLM-based reranking with a weighted heuristic (50% semantic, 30% keyword, 20% recency) plus an adaptive threshold: 0.4ms instead of adding 2–3 seconds and an extra call
- Combine semantic and keyword search — each alone misses ~25% of relevant results, together ~10%
- Keep agent context under ~100k tokens even with million-token windows (~200k upper bound, under 60k for the hardest problems), and deterministically re-allocate a fresh context each iteration instead of compacting, since compaction is lossy
- Use batch mode for non-urgent work: 50% fewer token cost with results delivered within 24 hours
- Evaluate vendors on whole trajectories rather than single-call cost or latency — Notion chose Parallel for web search despite it not being cheapest
- Run observability on tool calls before production to see how long each tool runs and how many times it loops
- Treat the cost ceiling as a non-negotiable production constraint gathered before design, alongside latency budget and regulatory requirements
- Instrument real queries against a counterfactual baseline to measure savings rather than estimating them, and state the baseline you measured against
- Post-train an open model on your own harness for a specialized task when the economics justify it — a finance specialization beating Opus at a fraction of Haiku's cost took one to two weeks
- Keep model optionality: the ability to switch providers is the leverage, and open-weight models lower the cost floor and improve negotiating position

**Avoid:**

- Instructing the model in the prompt to use less context — the context is already transmitted and billed before the model reads the prompt
- Optimizing output length, max_tokens, or temperature to cut spend, when ~90% of the bill is input tokens
- Sending all traffic to the newest frontier model — charging a customer Opus rates to triage an email inbox
- Putting an LLM in the loop for CSV-to-PDF conversion, deterministic SQL, or tool calls that already sit behind a CLI
- Filling a million-token context window because it exists — it costs more and degrades answer accuracy
- Sharding entity enumeration across parallel LLM calls: it produces hallucinated entities and silent omissions on top of the token spend
- Committing to a single provider for a volume discount — no discount is worth the lost optionality, and you have no exit
- Assuming prepaid inference credits behave like a metered utility bill; without the periodic-bill anchor teams systematically overspend
- Leaving API keys as files or dashboards without per-seat usage limits — one talk cited a stolen key draining an endpoint in real time, another an accidental $500M single-month Claude bill from unset limits
- Assuming multiple probabilistic models checking each other's work is a cost-effective correctness strategy

## Notable Outliers

- Cutting input tokens by 94% yields only ~61% total savings, and the 94% figure is against a worst-case full-file-read baseline — modern agentic tools like Claude Code are already smarter than that, so real-world savings are lower. ([We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [6:31](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=391s))
- At 1GW scale the naive approach burned 116 million tokens per validation pass while still producing errors, versus 390,000 for the restructured one — roughly a 300x reduction with correctness rising from ~30% to 100%. ([Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s))
- For 20–30 step browser tasks, a small computer-use model costs about 80 cents per task versus $230 for a frontier model — and accuracy differences between them are within statistical noise, so the real advantage is latency and cost, not quality. ([Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [18:07](https://www.youtube.com/watch?v=Ki980nV0__0&t=1087s))
- Data curation alone cuts response length enough to yield roughly 35x fewer flops per correct answer versus Qwen 3.5 — inference cost optimization achieved in pre-training, not serving. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [8:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=530s))
- Running a coding agent in a loop works out to $10.42 an hour, which reframes token spend as cheap relative to engineer time. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [20:42](https://www.youtube.com/watch?v=c35YoMdnI78&t=1242s))
- On edge devices DRAM cost, not compute, is the binding constraint — some phone makers are shipping less RAM this year than last, and Raspberry Pi 6GB prices rose ~2.5x since launch. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [3:04](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=184s))
- A 10x local inference speedup on DGX Spark was achieved in about three weeks using only existing techniques — vLLM backend, quantization, config tuning — with no new computer science. ([State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [21:43](https://www.youtube.com/watch?v=KB41dTlX1Uc&t=1303s))
- There is no single highest-leverage inference optimization; the correct strategy is to pursue a thousand and one edges exhaustively rather than prioritize a few — and current GPU flop utilization should already be considered embarrassing. ([Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [12:03](https://www.youtube.com/watch?v=AVMr9PMINyo&t=723s))

## All Talks

- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)
- [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)
- [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md)
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
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Cormac Brick](../speakers/cormac-brick.md)
- [Dan Fu](../speakers/dan-fu.md)
- [Dat Ngo](../speakers/dat-ngo.md)
- [Dhruv Batra](../speakers/dhruv-batra.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Jeffrey Lee-Chan](../speakers/jeffrey-lee-chan.md)
- [Joanne Song](../speakers/joanne-song.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Lucas Atkins](../speakers/lucas-atkins.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Olive Song](../speakers/olive-song.md)
- [Raahul Singh](../speakers/raahul-singh.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Ramesh Raskar](../speakers/ramesh-raskar.md)
- [Richard Socher](../speakers/richard-socher.md)
- [Rishi Desai](../speakers/rishi-desai.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Saoud Rizwan](../speakers/saoud-rizwan.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Shafik Quoraishee](../speakers/shafik-quoraishee.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)
- [Vanč Levstik](../speakers/vanc-levstik.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)
- [Will Brown](../speakers/will-brown.md)

