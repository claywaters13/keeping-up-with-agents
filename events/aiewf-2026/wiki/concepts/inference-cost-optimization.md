---
title: "inference cost optimization"
type: "concept"
slug: "inference-cost-optimization"
tier: "supporting"
maturity: "consolidating"
talk_count: 29
speaker_count: 40
---

# inference cost optimization

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **29** talk(s) by **40** speaker(s)

**Definition:** Managing the unit economics of serving models — cost per token, per query, and per agent run — as a first-order product constraint.

*Also referred to as: inference cost management, inference cost economics, token economics, cost efficiency per token, token cost optimization, batch inference pricing, cost and latency optimization*

## State of Practice

Cost has stopped being a finance concern and become a design constraint that shapes architecture, monitored in production alongside quality — 40% of surveyed engineers say it regularly limits how ambitiously they use AI. The field has converged on where the money actually goes: input tokens, not output (roughly 90% of coding-agent spend), which makes prompt-cache hit rate, retrieval scope, and what re-enters the context on every loop iteration the dominant levers, well ahead of model choice. Falling per-token prices are explicitly not expected to fix this, because per-session token consumption is growing faster than prices fall — the recurring datapoints are a retailer at ~$200M with Anthropic, a company that accidentally spent $500M in a month, and Uber exhausting a year's token budget in month four. The concrete playbook is now fairly standard: cache the system prompt, route by difficulty behind a cheap classifier (Notion's auto-model absorbs ~75% of traffic), cap tool-loop iterations, keep large tool results out of context by reference, push counting/set logic/SQL/format conversion into deterministic code, and treat open-weight models as both a cost tier and negotiating leverage (GLM at half the cost of Opus despite 2x tokens; DeepSeek at $1.9K/month against Gemini's $40K for the same workload). What remains genuinely open is whether to compact context or keep it whole and cached, whether to rent inference or own the substrate, and whether spending more tokens is a legitimate way to buy reliability.

## Consensus

### Cost is now a first-class engineering constraint measured in production, not a post-hoc finance concern — it is second only to quality in model selection and regularly bounds what teams are willing to build.

Support: **4** talk(s)

> "it turns out that infinite intelligence still comes with a usagebased bill."
>
> — ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [8:16](https://www.youtube.com/watch?v=RGe6EjucbzI&t=496s)

Supporting talks: ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)

### Falling per-token prices do not reduce total spend, because tokens consumed per session or per task grow faster than prices fall — so unit economics must be engineered rather than waited out.

Support: **6** talk(s)

> "You can look at it, you know, the difference between GPT-4 when it first launched and GPT-5.5 is is is much, much cheaper per token, but at the same time the amount of tokens in an individual session has gone up exponentially as well."
>
> — [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [14:13](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=853s)

Supporting talks: [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Notion's Token Town](../talks/notions-token-town.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)

### The cost sits on the input side, so optimization means controlling what enters the context window — retrieval scope, tool-result handling, and cache hits — not tuning output length or model parameters.

Support: **6** talk(s)

> "This is the most important slide. 90% of your AI cost is input."
>
> — [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [1:57](https://www.youtube.com/watch?v=dRmWYHuIJxM&t=117s)

Supporting talks: [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)

### Traffic should be routed across a tier of models by task difficulty rather than sent to the strongest model by default, with a cheap model acceptable as the router itself.

Support: **5** talk(s)

> "When you triage an email inbox, if we're charging you to do that on Opus, we're ripping you off and ourselves."
>
> — [Notion's Token Town](../talks/notions-token-town.md), [10:19](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=619s)

Supporting talks: [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Notion's Token Town](../talks/notions-token-town.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### Work that can be expressed as deterministic code — arithmetic, counting, set logic, dedup, SQL, format conversion — should be moved out of the model entirely, which is simultaneously cheaper and more correct.

Support: **4** talk(s)

> "Why would I run 1 + 1 through a multi-billion parameter model instead of one CPU cycle?"
>
> — [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [12:12](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=732s)

Supporting talks: [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Notion's Token Town](../talks/notions-token-town.md), [Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### Open-weight models are now good enough that they function as a real cost tier — comparable output at a fraction of the price — and as negotiating leverage against closed providers.

Support: **6** talk(s)

> "GLM used twice as many tokens but only cost half as much."
>
> — [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [9:44](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=584s)

Supporting talks: [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Notion's Token Town](../talks/notions-token-town.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

## Disagreements

### Should long-running agents compact or trim context to control cost, or keep the full history and rely on prompt caching?

| Position A | Position B |
|---|---|
| Do not compact by default. Summarization invalidates the provider's prompt cache, and clearing old tool outputs forces the agent to re-retrieve what it already had — keeping everything won simultaneously on cost, latency, and recall, and the setup sending the most tokens was the cheapest to run because 97% of them were cached.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* | Actively bound the context: slide a window over conversation history and summarize what falls out, compact past ~150K tokens, keep working context under ~100K, and index the codebase so a query costs 4.9K tokens instead of 83K.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* |

*Why it matters: The two strategies invert each other: one treats cache hit rate as the objective and tokens-in-context as nearly free, the other treats token count as the objective and accepts cache misses. Getting it backwards can multiply spend several-fold on identical workloads, and the answer flips depending on whether the conversation still fits the cacheable window.*

### Should teams rent inference from hosted APIs, or own the serving substrate (self-hosted boxes, local models, on-device)?

| Position A | Position B |
|---|---|
| Own it once you are past product-market fit. Prepaid credits lack a periodic-bill anchor and systematically cause overspend, rented endpoints are blind to workload shape, rate limits are dictated by the vendor, third-party dependency gets redlined in audits, and recommendations cannot be reproduced without access into the model. Enterprises want control, sovereignty, and no rug-pulls.<br>*[Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md)* | Stay hosted and spend the effort elsewhere. Applied AI companies should not try to win on token economics at all — they win on product, data flywheels, and orchestration. Cloud hosting beats local for most agents because local hosting makes you responsible for uptime, and frontier price/performance is still moving fast enough (half-cost tiers, $1/$6 per million) to keep the rented path competitive.<br>*[Notion's Token Town](../talks/notions-token-town.md), [The Agentic Web and the Bazaar Era of AI](../talks/the-agentic-web-and-the-bazaar-era-of-ai.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* |

*Why it matters: This determines whether inference is a capex or opex line and who carries the operational burden — building your own substrate is a multi-quarter infrastructure commitment that is wasted if hosted prices keep collapsing, while staying rented leaves you exposed to unbounded bills, rate limits, and audit failures.*

### Is spending more tokens a legitimate way to buy reliability?

| Position A | Position B |
|---|---|
| Yes — tokens are cheap relative to engineer time. Running a coding agent in a loop works out to $10.42 an hour, running both local dev and a staging agent doubles token usage but buys reliability worth the tradeoff, AI security scanning at ~$5 per PR beats human reviewers, and serious long-horizon evaluation simply costs 31M tokens per trial.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)* | No — buying quality with more tokens does not scale and often does not work. Stacking loops on loops is unsustainable at company token budgets, probabilistic models checking each other is not verification, and a bounded two-or-three-step plan-then-resolve pipeline replaced a multi-step agentic loop while cutting 116M tokens per validation pass to 390K and raising correctness from 30% to 100%.<br>*[Semantic Blindness: 500,000 Sensors Confused an LLM](../talks/semantic-blindness-500000-sensors-confused-an-llm.md), [How Kepler Built Verifiable AI for Financial Services](../talks/how-kepler-built-verifiable-ai-for-financial-services.md), [Notion's Token Town](../talks/notions-token-town.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)* |

*Why it matters: It sets whether your reliability budget is spent on tokens or on engineering deterministic verification, and whether per-task cost stays flat as the system scales or grows with problem size — the difference between a constant 9,000 tokens per query and 116 million.*

### Is task-specific fine-tuning or post-training a practical cost lever today, or still premature for most teams?

| Position A | Position B |
|---|---|
| It is practical now and the payoff is large: a post-trained open model can beat Opus on a specialized finance task at a fraction of Haiku's cost in one to two weeks, a 50M–500M parameter model fine-tuned on 10K–10M synthetic samples matches a 2–4B model on a fixed task, and a $50K thousand-step GLM-5 RL run is comparable to a month of token spend.<br>*[Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* | It is a 'not yet' layer — most teams do not fine-tune at all and those who picked build or buy are not switching; fine-tuning-as-a-service never took off because customization is itself hard; and it should be reserved for behavioral failures, not reached for as a cost lever, since off-the-shelf open weights already handle moderate tasks without RL on top.<br>*["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Notion's Token Town](../talks/notions-token-town.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* |

*Why it matters: Whether the cheapest path to a cost reduction is a two-week training project or a routing config change decides how teams staff for cost work — and a wrong bet either burns weeks of ML effort or leaves a 10x price gap unclaimed.*

## Practical Guidance

**Do:**

- Cache the system prompt (and tool definitions and messages where the provider supports it) so only a reduced payload is sent after the first call; track cache hit rate per turn as a first-class metric — one team ran its cheapest configuration while sending the most tokens because 97% of them were cached.
- Route by task difficulty across a model tier, and use a cheap model as the router itself; Notion's auto model absorbs ~75% of AI traffic.
- Put non-urgent work through batch mode: 50% fewer token cost with results within 24 hours.
- Always set a max-iterations cap on tool loops, and run observability over tool calls before production to see how long each runs and how often it loops.
- Store large tool results outside the context and pass a summary or reference instead of re-sending them on every loop iteration.
- Move counting, set logic, dedup across near-identical names, deterministic SQL, arithmetic, and file-format conversion into code — do not spend model tokens on anything you can write down as rules.
- Design context to grow with hierarchy depth rather than instance count: the same 9,000-token query served a 64-GPU and a 460,000-GPU system.
- Index and retrieve rather than reading full files — hybrid scoring (50% semantic, 30% keyword, 20% recency) at 0.4ms cut context from 83K to 4.9K tokens per question with 90% recall, and beat LLM reranking that added 2–3 seconds.
- Evaluate models and vendors on whole-trajectory cost, not single-call price or latency; Notion chose Parallel for web search despite it not being cheapest per call.
- Log tokens, cache hits, cost, TTFT, tool calls, and user frustration per turn — it is cheap to implement and most teams skip it, then have nothing to investigate.
- Keep model optionality: no volume discount is worth committing to a single provider, and open-weight fallbacks are the leverage that makes negotiation possible.
- Set usage limits on provider dashboards before handing agent access to thousands of employees.
- Push toward smaller models where the task is fixed: shrinking a model speeds it up mainly by reading fewer bytes from memory per token, and DRAM — not compute — is the binding constraint on edge deployment.

**Avoid:**

- Summarizing or compacting by default — it invalidates the prompt cache, so you need >50x compression before it pays off, and it dropped one team's recall from ~92% to 32%.
- Aggressively clearing old tool outputs, which makes the agent re-retrieve information it already had and raises total cost.
- Sending all traffic to the strongest model — triaging an email inbox on Opus is charging the customer and yourself for nothing.
- Trying to cut spend by shortening answers or tuning max-tokens and temperature when ~90% of the cost is input tokens.
- Adding prompt instructions telling the model to use less context — the context was transmitted and billed before the model read the prompt.
- Running an LLM in the loop for CSV-to-PDF conversion, CLI tool calls, or deterministic SQL — this is where teams become token poor fastest.
- Using a multi-step agentic loop where a bounded two- or three-step plan-then-resolve pipeline keeps cost flat and constant.
- Leaving tool loops uncapped — they can run 10 or 20 times or become infinite.
- Buying quality by stacking loops on loops and orchestrating problems away with more tokens; ask what a sustainable monthly token budget per engineer actually is.
- Treating prepaid inference credits as a budget — without a periodic-bill anchor they behave like casino chips and overspend is systematic.
- Storing API keys where they can be stolen; one speaker watched a stolen key drive spend from $7,000 upward in real time.
- Judging a model on a within-noise accuracy edge when latency per step and cost per task are the real differentiators — 80 cents versus $230 for the same 20–30 step task.

## Notable Outliers

- There is no single highest-leverage inference optimization — the correct strategy is to exhaustively pursue every available edge rather than prioritize a few, and current GPU flop utilization should already be considered embarrassing. ([Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [12:03](https://www.youtube.com/watch?v=AVMr9PMINyo&t=723s))
- The configuration that sent the most tokens was the cheapest to run, because 97% of those tokens were cached — token count and cost can move in opposite directions. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [52:08](https://www.youtube.com/watch?v=WP3hjUXd918&t=3128s))
- Running a coding agent in a loop works out to $10.42 an hour, which is the whole economic argument for loops. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [20:42](https://www.youtube.com/watch?v=c35YoMdnI78&t=1242s))
- DRAM cost, not compute, is the binding constraint on edge AI, and it is getting worse — some phone makers are shipping less DRAM this year, and Raspberry Pi 6GB cost has risen ~2.5x since launch. ([Why Large? Tiny LMs & Agents on Edge/Robotics](../talks/why-large-tiny-lms-agents-on-edgerobotics.md), [3:04](https://www.youtube.com/watch?v=hacEQHHhu2Q&t=184s))
- Data curation alone reduces response length enough to yield roughly 35x fewer flops per correct answer — inference cost is partly a pre-training data decision, not a serving decision. ([Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md), [8:50](https://www.youtube.com/watch?v=_PdK6x7PQNM&t=530s))
- A $50K thousand-step GLM-5 RL run on real agentic coding tasks is comparable to a month of token spend, putting frontier-scale post-training inside an ordinary inference budget. ([Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [32:27](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1947s))
- Memory design is fundamentally a compute allocation problem — ChatGPT's ~4,000-token profile updated every few days versus Claude's ~1,000-token profile updated every 24 hours are opposite points on a serving-cost/update-cost curve. ([Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md), [12:35](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=755s))
- Mixture-of-expert models are still running on billion-dollar clusters at only around 30% utilization. ([First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md), [16:42](https://www.youtube.com/watch?v=pWXUkLP9uWM&t=1002s))
- Real-time generative video now costs about the same per stream as a voice model, and one real-time sample had better motion than the slow batch version at about 1/100th the cost. ([Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md), [1:46](https://www.youtube.com/watch?v=Xln-On3syJk&t=106s))
- Once computer-use agents are sub-penny, sub-100ms, and return structured output, the distinction between an agent and an API stops mattering — cost collapse is the thing that dissolves the architectural debate. ([Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [20:20](https://www.youtube.com/watch?v=Ki980nV0__0&t=1220s))

## All Talks

- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)
- [First Steps Toward Automated AI Research](../talks/first-steps-toward-automated-ai-research.md)
- [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)
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
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)
- [Will Brown](../speakers/will-brown.md)

