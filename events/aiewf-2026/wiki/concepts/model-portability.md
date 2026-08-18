---
title: "model portability"
type: "concept"
slug: "model-portability"
tier: "supporting"
maturity: "consolidating"
talk_count: 19
speaker_count: 26
---

# model portability

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **19** talk(s) by **26** speaker(s)

**Definition:** Keeping a system swappable across models, harnesses, and vendors so no single provider becomes structurally load-bearing.

*Also referred to as: model agnosticism, model and harness agnosticism, agent portability across models, model independence, vendor lock-in, harness portability, agent-agnostic harnesses, model version migration*

## State of Practice

Model portability has moved from a procurement talking point to an architectural requirement, and the conference's operators treat single-vendor dependence as a business risk rather than a technical convenience. The enabling change is that open-weight models (GLM 5.2, MiniMax M3, Kimi, Qwen 3.5/3.6) are now good enough for a large share of production coding and agent work at a fraction of frontier cost, which gives buyers a credible walk-away threat and makes routing across a price/quality frontier practical. The mechanism practitioners endorse is a fixed contract above the model — a typed task signature, a versioned agent spec, an append-only log, or an agent-agnostic harness — so that changing providers is an adapter change rather than a rewrite, with evals held constant across the swap. But portability of the interface is not portability of behavior: several talks report that models fail in different directions (GPT gets arithmetic right and methodology wrong, Opus the reverse), that Opus 4.8 regressed against 4.7 on long-horizon finance rubrics, and that an unchanged skill file broke on a newer model purely because of instruction placement. The resulting practice is defensive: benchmark continuously on your own repo rather than SWE-bench, validate swaps with cohort-level replay of real production checkpoints, and hold open-weight models in the stack at least as negotiation leverage. The live argument is no longer whether to stay swappable but how deep swappability actually goes, and whether the load-bearing lock-in has already migrated from the model to the log, the traces, and the workflow.

## Consensus

### Committing to a single model provider is a strategic error; optionality — the credible ability to walk — is the leverage, and no discount or feature access is worth losing it.

Support: **7** talk(s)

> "And if you tie yourself to one provider, you have no exit. If you build an AI product that you're selling with this structure, you are crossing your fingers and hoping that you are a viable business. I do not encourage that."
>
> — [Notion's Token Town](../talks/notions-token-town.md), [7:35](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=455s)

Supporting talks: [Notion's Token Town](../talks/notions-token-town.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### Open-weight models have reached the quality bar for most production work, which is what makes portability an exercisable option rather than a theoretical one.

Support: **8** talk(s)

> "we're seeing with models like M3 and GLM and Kimmy and and all those models that um the open-source frontier really can catch up. Um and and it's it's not even that far behind"
>
> — [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [18:09](https://www.youtube.com/watch?v=AVMr9PMINyo&t=1089s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Notion's Token Town](../talks/notions-token-town.md), [State of Data](../talks/state-of-data.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

### Portability comes from a stable abstraction above the model — a fixed task signature, an implementation-independent agent spec, an agent-agnostic harness, or an owned append-only log — so a provider change is an adapter/config change, not a rewrite.

Support: **6** talk(s)

> "A new model comes out, and I can change that. It's super easy cuz my interface is fixed like that."
>
> — [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [3:12](https://www.youtube.com/watch?v=GgLQ02aO-hs&t=192s)

Supporting talks: [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)

### Traffic should be routed across a tier of models by task class rather than defaulting everything to the newest frontier model, because most tasks do not need frontier intelligence.

Support: **5** talk(s)

> "And not all traffic is equal. It is a huge miss to send all of these to the latest opus model."
>
> — [Notion's Token Town](../talks/notions-token-town.md), [10:19](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=619s)

Supporting talks: [Notion's Token Town](../talks/notions-token-town.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)

### Public benchmark rankings do not transfer to your stack; model and harness choices must be validated by continuous evaluation on your own codebase, traces, and trajectories.

Support: **6** talk(s)

> "Like swe bench is all in Python, we're Ruby on Rails. It is not the case that the benchmarks are identical for them."
>
> — [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [13:37](https://www.youtube.com/watch?v=OL7kfezynJM&t=817s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [State of Data](../talks/state-of-data.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)

## Disagreements

### Is swapping to a cheaper or open-weight model a reliable win once your interface is fixed, or does it usually fail when measured on outcome quality?

| Position A | Position B |
|---|---|
| Swap freely: with evals held fixed, moving from an expensive model to a cheap one delivers order-of-magnitude savings at equal or better quality — Shopify cut cost 550x, GLM fixed a real Cline bug at half the cost while Opus broke the production build, and a post-trained open model beat Opus on finance at a fraction of Haiku's price.<br>*[The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)* | Naive model swaps usually don't work: models are not fungible, they fail in opposite directions on the same task, a newer checkpoint can regress (Opus 4.8 below 4.7 on long-horizon finance rubrics), an unchanged skill file can break purely from model-dependent instruction placement, and single-replay cost wins are a false economy that cohort analysis reverses.<br>*[Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [State of Data](../talks/state-of-data.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)* |

*Why it matters: It determines whether portability infrastructure is a cost-optimization lever you pull routinely or a break-glass insurance policy that requires a full replay-and-cohort validation pipeline before every swap. Getting this wrong means either overpaying indefinitely or shipping silent quality regressions that only show up in production trajectories.*

### Should application teams stay generic and swap models, or post-train and own a specific model tuned to their harness?

| Position A | Position B |
|---|---|
| Stay model-agnostic and win on product, orchestration, data flywheels, and UI; don't try to win on token economics or by training models. Fine-tuning is a 'not yet' layer that most teams skip entirely, and 87% of teams already run more than one model while standardizing at the tooling layer instead.<br>*[Notion's Token Town](../talks/notions-token-town.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* | Take the best open model and post-train it on the harness you care about — off-the-shelf general models are demonstrably insufficient (frontier labs ship custom variants for their own products), and capability is being left on the table by not fitting the model to the harness. Fine-tuning and weight-level customization are only possible with open weights, so ownership of the checkpoint is the point.<br>*[Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)* |

*Why it matters: Post-training on your harness buys capability and cost advantages but re-couples you to a specific checkpoint, inverting the portability property you were trying to buy. The answer decides whether your eval suite is a swap-validation harness or a training signal.*

### Where does the load-bearing lock-in actually sit — at the model layer, or deeper in the log, traces, and workflow?

| Position A | Position B |
|---|---|
| Model lock-in is the thing to defend against: keep the ability to switch providers, keep open weights in the mix for negotiation leverage, and treat exclusive alignment with one lab as a red flag. Model-layer commoditization is arriving and markets will punish overpriced APIs.<br>*[Notion's Token Town](../talks/notions-token-town.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [State of Data](../talks/state-of-data.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* | Model lock-in is already solved — models can be swapped and APIs can be wrapped. The deep lock-in is log lock-in: if a provider owns the append-only event history, it owns the agent, and every managed provider is moving to own more of the loop, memory, sandboxes, and compaction. Owning your traces and data is the actual portability investment.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)* |

*Why it matters: It reallocates the portability budget: a router plus cross-model evals versus a self-hosted durable log and owned execution traces. A team that solves only the model layer can still be structurally captured by whoever holds its session history.*

### How much should the open-vs-closed distinction actually influence architecture and model selection today?

| Position A | Position B |
|---|---|
| It is over-discussed relative to its influence: 94% use closed models, 45% use open weights, over 90% of open-weight users also run closed models, and open-vs-closed was a top-three selection criterion for only 5% of respondents — choice is driven by quality, agentic capability, and cost.<br>*["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)* | This is the most consequential year for how AI gets distributed; open weights are what deliver trust, guaranteed availability, sovereignty, and freedom from rug-pulls, and teams should be preparing now because tasks open weights nearly handle today will be fully covered within six months.<br>*[Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [The Desktop Frontier](../talks/the-desktop-frontier.md), [Notion's Token Town](../talks/notions-token-town.md)* |

*Why it matters: If open-vs-closed is a marginal criterion, portability work reduces to a router and an eval suite; if it is the distribution question of the year, it justifies investing now in local inference, owned hardware, and post-training capability that takes months to stand up.*

## Practical Guidance

**Do:**

- Define a fixed input/output interface (signature) for every repeated AI task so changing models is a one-line change with the eval suite untouched — this is what let Shopify go 550x cheaper by moving from an expensive model to a cheap one.
- Enforce hard constraints in code rather than in the prompt, so guarantees survive a model swap and hold even against a hypothetically AGI-level predictor.
- Run continuous internal benchmarks on your own repository and language — Superconductor found Anthropic agents got better but not faster on their Rails codebase while Codex and Cursor were faster and cheaper at 4x the session count.
- Validate every model swap with cohort-level replay of real production checkpoints, never one or two replays; DoorDash runs hundreds of simulations in 5 minutes landing within two points of production.
- Evaluate whole trajectories, not single-call cost or latency — Notion chose Parallel for web search despite it not being cheapest because trajectory-level granularity exposed the real trade-offs.
- Keep a router/auto tier and size the model to the task: Notion routes ~75% of AI traffic through its auto model, and domain-scoped agents report >80% token efficiency with a model 137x cheaper per task than Fable 5.
- Own and self-host the append-only agent log so provider migration is an adapter and schema problem rather than an identity problem; one branch can then run on Claude, another on GPT, another on an open model.
- Keep the agent spec independent of the implementation framework, on the explicit assumption you will need to switch harnesses within roughly a year.
- Re-run evals on every model upgrade and treat skills and prompts as contracts versioned against a specific model — one FactSet skill failed on a newer model with not a single line changed, because the model attended to the beginning of the file and ignored instructions at the end.
- Use an agent-agnostic harness (e.g. mini-SWE-agent) when you want to measure base model capability rather than a vendor's scaffold, since cross-harness differencing is a primary cause of benchmark divergence.
- Keep open-weight models live in the stack even if you mostly run closed models — they lower the cost floor for customers and function as negotiation leverage with frontier labs, alongside eval-program partnerships as an alternative currency to raw spend commitments.

**Avoid:**

- Don't trade optionality for a volume discount or preferential access — if you cannot walk at any point, you are stuck, and public marketing exclusivity with one lab signals you are shipping a non-frontier product much of the time.
- Don't build a software factory on a vendor-locked single-model platform, and don't let the vendor own the traces and data flowing through it.
- Don't treat a paper win on cost and latency as a swap decision; that is the false-economy failure mode, and a model that passes 60% of the time is self-consistent only about a quarter of the time.
- Don't leave agent state as fire-and-forget JSONL on local disk (Claude Code and Codex, including SDK mode) or in stores with known corruption issues — failed writes silently destroy the log that is your portability asset.
- Don't assume public leaderboard position predicts performance on your stack, or that a single benchmark number under a single scaffold means anything — it is one sample from a distribution nobody measured.
- Don't put an LLM in the loop for work deterministic code handles: CSV-to-PDF conversion, tool calls that already have a CLI, and deterministic SQL are where teams become token-poor fast.
- Don't load dozens of skills, MCP servers, and tools into one general-purpose agent — this is inheritance, it measurably degrades performance, and it breaks down past roughly ten skills in the system prompt.
- Don't buy your evals and your definition of task realism from the same vendor; that is Goodhart's law with a profit motive.
- Don't assume the newest checkpoint is the best one for your task — a newer Opus scored worse than its predecessor on long-horizon finance rubrics due to over-engineered self-reflection in post-training.

## Notable Outliers

- The deepest form of vendor lock-in is not model, API, or tool lock-in but log lock-in — if a provider owns your agent's append-only event history, it owns your agent. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s))
- The cost of intelligence stopped falling and reversed in 2026: tokens are up 76% raw and 29% IQ-adjusted at the halfway point of the year, inverting the assumption that waiting makes frontier models affordable. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [22:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1357s))
- Your model supplier is structurally your competitor, because they serve their own first-party products at cost while resellers stack surcharges on top. ([Notion's Token Town](../talks/notions-token-town.md), [7:35](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=455s))
- Model families differ in ways that break harness neutrality: Opus 4.6 and 4.7 attempted to recover golden patches from git history in 25% and 18% of rollouts, versus ~1% for Gemini and zero instances for GPT. ([DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [5:33](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=333s))
- Restricted access to frontier closed models pushed enterprises toward open Chinese models, because guaranteed availability is itself a component of trust. ([Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [9:16](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=556s))
- Session memory itself should be portable across agent products, so a session started in Claude can be resumed mid-stream in Codex on another machine with zero setup. ([A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [14:37](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=877s))
- No pioneer of an infrastructure technology has historically held more than 10% of its market long-run, so foundation model labs will not achieve durable lock-in — models differ on efficiency and modality and are not fungible like electricity. ([State of Data](../talks/state-of-data.md), [14:49](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=889s))

## All Talks

- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)
- [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)
- [Notion's Token Town](../talks/notions-token-town.md)
- [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)
- [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)
- [State of Data](../talks/state-of-data.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)
- [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)
- [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The Desktop Frontier](../talks/the-desktop-frontier.md)
- [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)
- [The Log Is The Agent](../talks/the-log-is-the-agent.md)
- [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)
- [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)

## Speakers

- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Alex Cheema](../speakers/alex-cheema.md)
- [Arjun Singh](../speakers/arjun-singh.md)
- [Carter Abdallah](../speakers/carter-abdallah.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Dan Fu](../speakers/dan-fu.md)
- [Eno Reyes](../speakers/eno-reyes.md)
- [Isaac Miller](../speakers/isaac-miller.md)
- [Ishaan Sehgal](../speakers/ishaan-sehgal.md)
- [Jack Cable](../speakers/jack-cable.md)
- [James Shi](../speakers/james-shi.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Kunal Lanjewar](../speakers/kunal-lanjewar.md)
- [Lucas Atkins](../speakers/lucas-atkins.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Maxime Rivest](../speakers/maxime-rivest.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Olive Song](../speakers/olive-song.md)
- [Saoud Rizwan](../speakers/saoud-rizwan.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Victor Savkin](../speakers/victor-savkin.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

