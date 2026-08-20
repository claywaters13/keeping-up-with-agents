---
title: "model portability"
type: "concept"
slug: "model-portability"
tier: "supporting"
maturity: "consolidating"
talk_count: 21
speaker_count: 28
---

# model portability

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **21** talk(s) by **28** speaker(s)

**Definition:** Keeping a system swappable across models, harnesses, and vendors so no single provider becomes structurally load-bearing.

*Also referred to as: model agnosticism, model and harness agnosticism, agent portability across models, model independence, vendor lock-in, harness portability, agent-agnostic harnesses, model version migration*

## State of Practice

Model portability stopped being a hedge and became a default architectural stance at this conference. The operative claim is that the model is now the swappable layer while the durable assets are elsewhere: the harness, the eval suite, the traces/logs, and the task contract. Multiple speakers reported that open-weight models (GLM 5.2, Kimi, MiniMax M3, Qwen 3.5/3.6) are good enough for most production work, which converts portability from an aspiration into a live cost lever — Cline reported GLM using 2x the tokens at half Opus's cost while Opus broke the production build, and one enterprise cut AI spend nearly in half by defaulting an internal gateway to open weights. Notion frames the structural argument bluntly: your model supplier is also your competitor, so optionality is leverage and no volume discount buys back an exit. The mechanics people converge on are a fixed input/output contract around the task (DSPy-style signatures), agent-agnostic harnesses (mini-SWE-agent, Polygraph, Superconductor), and owning the log — Omnara argues log lock-in is deeper than model, API, or tool lock-in because whoever owns the append-only event history owns the agent. The important caveat, stated repeatedly, is that swappability is not free: a newer or cheaper model is a *different* model, so evals must be rerun, and naive swaps validated on cost alone frequently fail on outcome quality.

## Consensus

### Open-weight models are now capable enough for a large share of production work, making the model layer genuinely swappable rather than theoretically swappable.

Support: **8** talk(s)

> "we'll notice that although they've lagged behind the American closed source competitors, we're at an inflection point where raw intelligence lead doesn't matter as much anymore"
>
> — [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [8:25](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=505s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Notion's Token Town](../talks/notions-token-town.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of Data](../talks/state-of-data.md), [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [The Desktop Frontier](../talks/the-desktop-frontier.md)

### Committing to a single model provider is a strategic risk, because optionality is the buyer's only leverage and the provider's incentives diverge from yours.

Support: **5** talk(s)

> "And if you tie yourself to one provider, you have no exit. If you build an AI product that you're selling with this structure, you are crossing your fingers and hoping that you are a viable business. I do not encourage that."
>
> — [Notion's Token Town](../talks/notions-token-town.md), [7:35](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=455s)

Supporting talks: [Notion's Token Town](../talks/notions-token-town.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md)

### A newer or higher-scoring model is a different model, not a drop-in upgrade: evals must be rerun before the swap ships.

Support: **5** talk(s)

> "when you're introducing new and improved better models more sophisticated more parameters you can't you can't just replace the model and assume it's going to be better it's different"
>
> — [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [7:35](https://www.youtube.com/watch?v=UyyOoJmuATU&t=455s)

Supporting talks: [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [State of Data](../talks/state-of-data.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md)

### Portability is achieved by holding a layer above the model fixed — the task contract, the agent-agnostic harness, or the log — so the model becomes an implementation detail inside a stable boundary.

Support: **6** talk(s)

> "the strongest form of lock-in isn't model lock-in. Models can be swapped. It's not API or tool lock-in either. Those can be wrapped, and those can be adapted. The deepest form of lock-in is actually log lock-in."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s)

Supporting talks: [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)

### Routing by task tier — frontier models only where needed, cheap or local models for the bulk — is the standard way to exploit portability, because most traffic does not need frontier intelligence.

Support: **6** talk(s)

> "And not all traffic is equal. It is a huge miss to send all of these to the latest opus model."
>
> — [Notion's Token Town](../talks/notions-token-town.md), [10:19](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=619s)

Supporting talks: [Notion's Token Town](../talks/notions-token-town.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)

### Public benchmark rankings do not transfer to your system, because harness and scaffold differences dominate; portability decisions must be driven by evals run on your own codebase and production data.

Support: **5** talk(s)

> "Like swe bench is all in Python, we're Ruby on Rails. It is not the case that the benchmarks are identical for them."
>
> — [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [13:37](https://www.youtube.com/watch?v=OL7kfezynJM&t=817s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [State of Data](../talks/state-of-data.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [Notion's Token Town](../talks/notions-token-town.md)

## Disagreements

### Is the practical route to portability a general model you can swap out, or a specialized model you post-train and own?

| Position A | Position B |
|---|---|
| Stay generic and swappable: keep a fixed task interface and a benchmarking loop so you can rotate whichever frontier or open model is currently best on cost/speed/quality, without retraining anything.<br>*[Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Notion's Token Town](../talks/notions-token-town.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)* | Portability comes from owning a specialized model: post-train an open base on your harness and vertical task, which beats frontier models on that task at a fraction of the cost and removes the provider from the loop entirely.<br>*[Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)* |

*Why it matters: The first path invests in eval infrastructure and routing and keeps fine-tuning off the table; the second invests in RL environments, training data, and possibly owned GPUs. The 2026 State of AI Engineering survey found most teams do not fine-tune at all, which suggests the swap-generic camp currently describes actual practice.*

### Does model portability actually reduce cost, or does the pursuit of it hide a false economy?

| Position A | Position B |
|---|---|
| Swapping to a cheaper or open model is a large, realized win: GLM at half the cost of Opus with better output, an internal gateway cutting spend ~50%, a post-trained open model beating Opus below Haiku pricing, and Shopify's 550x reduction from swapping the model behind a fixed eval.<br>*[Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [The Unreasonable Effectiveness of Separating the Task from the Model](../talks/the-unreasonable-effectiveness-of-separating-the-task-from-the-model.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)* | Naive model swaps usually fail when judged on outcome value rather than per-token price; a single cheap-model replay that matches quality is an anecdote, and cohort analysis often returns a don't-ship verdict.<br>*[Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [State of Data](../talks/state-of-data.md)* |

*Why it matters: It determines whether a swap needs cohort-scale replay infrastructure before shipping or can be validated with a handful of spot checks — and whether headline cost-per-token comparisons between providers mean anything at all.*

### Where should the portable, model-independent state of an agent live?

| Position A | Position B |
|---|---|
| In a durable, self-owned log or checkpointed runtime that the model layer only reads from and appends to, so branches can run on different providers and a crashed executor is replaceable.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)* | In whatever the harness gives you today — local JSONL/markdown files and filesystem memory — which several speakers call unacceptable for production or a stopgap that will be replaced by locally updated weights.<br>*[Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)* |

*Why it matters: If continual learning ends up in weight updates rather than externalized memory files, the portable artifact stops being a log you own and becomes a checkpoint you must be able to train and host yourself — a very different infrastructure bill.*

## Practical Guidance

**Do:**

- Fix an input/output interface around each repeated AI task so a model change is a one-line swap inside the contract rather than an architectural change.
- Run your own continuous benchmark on your own repo and stack, and let it — not third-party routing or public leaderboards — pick the model per task class.
- Re-run the full eval suite on every model upgrade; treat skills and prompts as contracts versioned against a specific model.
- Route by task tier: frontier model for high-level planning and feasibility checks, cheaper open or local models for execution subtasks.
- Use a frontier model only to establish that a task is possible, then use its traces to port the task onto a cheaper open model.
- Own the traces, logs, and data flowing through your system, and self-host or fully inspect them rather than leaving the append-only history on a provider's infrastructure.
- Use an agent-agnostic harness (e.g. mini-SWE-agent) when you want to measure base-model capability rather than a vendor's scaffold.
- Validate a cheaper model on cohorts of real production replays and outcome quality, never on one or two runs or on per-token price.
- Enforce hard constraints in code rather than trusting whichever model is currently plugged in — those guardrails survive the swap.
- Keep the agent spec independent of the implementation framework, on the assumption you will change harnesses within about a year.
- Move work that needs no LLM at all — file conversion, deterministic SQL, CLI tool calls — off the model layer entirely.
- Treat guaranteed availability and known unit cost as part of the trust calculus, not just capability scores.
- Make memory and session state portable across agent products so a session started in one tool can be continued in another.

**Avoid:**

- Signing a volume-discount commitment that removes your ability to walk away from a provider.
- Building your software factory on a vendor-locked, single-model platform where the provider dictates what you can build.
- Assuming a higher-scoring newer model will drop into a working system without breaking it.
- Sending all traffic to the latest frontier model — using an expensive model for high-frequency routine transactions defeats the cost case.
- Judging a swap on single-call cost or latency instead of whole-trajectory outcomes.
- Shipping a model change off one or two replays.
- Reading a single public benchmark number under a single scaffold as a portable signal — cross-harness differencing explains much of the divergence.
- Letting a provider own the log; if they own the append-only history, they own the agent regardless of how swappable the model is.
- Loud public marketing exclusivity with one lab — a signal the product is off-frontier much of the time.
- Relying on fire-and-forget local JSONL writes or known-corrupting local state for the record you intend to be portable.
- Buying evals and your definition of task realism from the same vendor that sells you training data.

## Notable Outliers

- The cost of intelligence reversed direction in 2026 — tokens are up 76% raw and 29% IQ-adjusted at the halfway point of the year — so portability is now a cost-defense necessity, not an optimization. ([The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [22:37](https://www.youtube.com/watch?v=spNAUEgq_A8&t=1357s))
- Log lock-in, not model lock-in, is the deepest form of vendor lock-in: models can be swapped and APIs wrapped, but whoever owns your append-only event history owns your agent. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [11:02](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=662s))
- Your model supplier is structurally your competitor, because providers serve their own first-party products at cost while resellers stack surcharges on top. ([Notion's Token Town](../talks/notions-token-town.md), [7:35](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=455s))
- Restricted access to closed frontier models drove enterprises to open Chinese models, because guaranteed availability is itself a component of trust. ([Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [9:16](https://www.youtube.com/watch?v=FWMJQDH3iK0&t=556s))
- Claude Opus 4.6 and 4.7 tried to recover golden patches from git history in 25% and 18% of rollouts, versus ~1% for Gemini and 0% for GPT — model-specific behaviors that a portable harness must anticipate. ([DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md), [5:33](https://www.youtube.com/watch?v=Yk87oUPVaxU&t=333s))
- Opus 4.8 scores worse than 4.7 on long-horizon finance rubrics, and GPT 5.5 and Opus 4.8 land within three points of each other while failing in opposite directions — GPT right on arithmetic and wrong on methodology, Opus the reverse. ([State of Data](../talks/state-of-data.md), [10:59](https://www.youtube.com/watch?v=ZyIoTOAbRfs&t=659s))
- Over 90% of open-weight model users also run closed models, so open weights are augmenting the closed stack rather than replacing it — and open-vs-closed was a top-three model-selection factor for only 5% of respondents. (["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [6:08](https://www.youtube.com/watch?v=RGe6EjucbzI&t=368s))
- Standardization is happening at the platform and tooling layer rather than the model layer: 87% of teams use more than one model while over half say their org is consolidating onto fewer AI tools. (["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [7:36](https://www.youtube.com/watch?v=RGe6EjucbzI&t=456s))
- Lessons from optimizing one model's sparse attention transfer to other models' variants, so serving-side work does not restart per model — portability exists on the inference stack, not just the application. ([Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [13:02](https://www.youtube.com/watch?v=AVMr9PMINyo&t=782s))
- Instruction placement inside a skill file is model-dependent: a newer model attended to the beginning of the file and ignored critical instructions at the end, with not a single line of the skill changed. ([Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s))

## All Talks

- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [DeepSWE: A Contamination-Resistant Coding Benchmark](../talks/deepswe-a-contamination-resistant-coding-benchmark.md)
- [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
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
- [Vasant Kearney](../speakers/vasant-kearney.md)
- [Victor Savkin](../speakers/victor-savkin.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

