---
title: "agent harness design"
type: "concept"
slug: "agent-harness-design"
tier: "core"
maturity: "consolidating"
talk_count: 50
speaker_count: 62
---

# agent harness design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **50** talk(s) by **62** speaker(s)

**Definition:** The engineering of the scaffold around a model — loop, prompts, tools, memory, and control flow — treated as the primary unit of design and iteration, distinct from the model itself.

*Also referred to as: harness engineering, agentic harness design, agent harness architecture, agent scaffold design, harness design, meta harness design, model-harness co-design*

## State of Practice

The conference's dominant claim is an inversion: model capability is no longer the binding constraint on agent performance — the scaffold is. Speakers from Anthropic, OpenAI, Browserbase, Etsy, and Amazon independently reported that identical models produce wildly different results under different harnesses (a controlled 106-task study showed a 52.4%→76.2% spread from changing only the harness), and that a strong harness lets Haiku-class or open-weight models hit frontier-level results on scoped tasks. The concrete engineering agenda that emerged is specific: budget context like a scarce resource (Codex caps the skill-description block at 2% of the context window and defers tools to tool search; Amazon caps skill.md at 100 lines and treats 40–50K of first-prompt context as a failed setup), decouple the agent loop from tool execution and keep session state in an append-only log external to both the harness process and the sandbox, and run verification in a context window separate from the one that produced the work — self-grading in the same context reliably produces confabulation. Control-flow decisions (is the task done, what step is next, is this action authorized) are increasingly pulled out of the model and into deterministic harness code, with the model reduced to proposing while the harness commits and emits receipts. The counterweight everyone acknowledges is staleness: harness fixes that encode a model's current limitations become pure overhead within a release cycle (Anthropic's context-anxiety workarounds became latency and cache bugs once Opus 4.5 shipped), so harnesses are now built from swappable primitives and re-validated on every model upgrade.

## Consensus

### The harness — not model capability — is the current limiting factor on what agent products can do; capability overhang is an engineering problem, not a waiting problem.

Support: **8** talk(s)

> "harnesses have become the limiting factor to what models can achieve"
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [30:20](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1820s)

Supporting talks: [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

### A sufficiently engineered harness lets a smaller, cheaper, or open-weight model reach the performance level teams currently pay frontier prices for.

Support: **6** talk(s)

> "instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn't have as much reasoning capabilities, but because of the harnessing around it, it's still able to perform at the level in which we expect"
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### Verification must run in a context window (or agent) separate from the one that produced the work; self-grading in the producing context causes confabulation and lost recall.

Support: **6** talk(s)

> "what we found is it's quite effective to separate verification into a separate context window. This is a very general trend."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [6:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=404s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)

### Context is a hard budget: load only thin indexes and descriptions up front and defer bodies, tools, and detail to on-demand retrieval, because oversized context degrades quality, not just cost.

Support: **6** talk(s)

> "for available skills, we actually cap the available skills list at 2% of your context total like maximum context window."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)

### The agent loop, the tool-execution sandbox, and session state must be separate failure domains, with state held in a durable append-only log outside both — not in the container, memory, or disk of the run.

Support: **3** talk(s)

> "the harness becomes a stateless process that talks to a session. The session is an append-only event log and that can reach out to hands, which are just containers."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [4:01](https://www.youtube.com/watch?v=9QebvrrY3KY&t=241s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)

### Harnesses go stale as models improve: scaffolding written to compensate for a model's limitations becomes latency and correctness overhead, so every model upgrade requires re-running evals and pruning the harness rather than a drop-in swap.

Support: **6** talk(s)

> "Opus 4.5 no longer exhibited context anxiety, which means that the fixes that we'd added into the harness itself became dead weight. In fact, it became pure overhead, adding things like latency and causing issues with the cache being discarded incorrectly at times."
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [8:08](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=488s)

Supporting talks: [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [From RL to IRL](../talks/from-rl-to-irl.md)

### Production traces — not pre-launch test suites — are where you learn what the harness actually needs; agents must ship with full-stack observability and a loop that mines traces back into evals.

Support: **7** talk(s)

> "production is the place when you learn what you need to uh what you need to test on the first place."
>
> — [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [5:36](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=336s)

Supporting talks: [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Agents Building Agents](../talks/agents-building-agents.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)

## Disagreements

### Should the harness take control flow away from the model, or give the model more freedom and fewer constraints?

| Position A | Position B |
|---|---|
| Pull judgment about state, step ordering, and completion out of the model entirely — the model proposes, deterministic harness code decides; when reliability approaches a coin flip, that is the signal to remove control flow from the model.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)* | Constraints are what limit the model; give it context and tools rather than rules, delete prescriptive scaffolding, and let it structure its own memory and work — Anthropic removed 80% of the Claude Code system prompt and found that prescribed memory schemas drop performance.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* |

*Why it matters: It determines whether your harness is a state machine that the model speaks for, or a thin environment the model drives — which decides where your engineering hours go, how much prompt surface you maintain, and whether performance improves or degrades on the next model release.*

### Should the harness be hand-designed by engineers, or generated and optimized by agents themselves?

| Position A | Position B |
|---|---|
| Humans must design the harness. Letting a coding agent build your agents produces something that technically works but is unmaintainable — a giant prompt with no separation of concerns — and letting a coding agent pick your architecture produces over-engineering; asking a model to improve its own prompts yields micromanagement.<br>*[Build Systems, Not Code](../talks/build-systems-not-code.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)* | Harness architecture decisions are arbitrary human guesses and should be meta-optimized: coding agents took a naive agent from 18% to 83% in ~10 iterations and found +10% on an already human-optimized production agent, and automatically hill-climbed instructions beat handwritten ones.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* |

*Why it matters: If self-optimization works, harness iteration becomes a compute expense guarded by evals and branch rollback; if it doesn't, harness quality stays gated on scarce senior engineering judgment and headcount.*

### Should teams build their own agent harness and infrastructure, or buy it and own only the domain layer?

| Position A | Position B |
|---|---|
| Build it. A software factory must be built, not bought; using an off-the-shelf agent framework costs you the freedom to tweak anything; a vendor-locked single-model platform lets the model provider dictate what you can build; even monitoring is better built in-house because you know what you're looking for.<br>*[How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)* | Hosting, session management, sandboxing, credentials, and observability are undifferentiated work that should be outsourced; developers should own only system prompts, skills, tools, and domain context, and buy browser/agent infrastructure rather than spending time on it.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)* |

*Why it matters: This decides whether the harness is your competitive moat or your commodity substrate — and whether you own the traces and execution layer that continual learning and model portability depend on.*

### Is scaffolding built for today's model a worthwhile investment, given models improve every few weeks?

| Position A | Position B |
|---|---|
| Build it now. The models are already good enough and the overhang is an engineering problem you can solve today; a good harness compensates most for weaker models, which is exactly what makes local and open models viable.<br>*[Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)* | A carefully built harness can be irrelevant within a month; harness guardrails are transitional scaffolding that should get thinner as models improve, and fixed harnesses cap novelty by suppressing the variance it requires.<br>*[Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* |

*Why it matters: It sets how much of the harness you write as durable infrastructure versus disposable patch — and whether you design against today's model behavior or against the capabilities you expect two releases out.*

## Practical Guidance

**Do:**

- Cap the available-skills/tool-description block at ~2% of the maximum context window and mark remaining tools as deferred, discoverable via tool search rather than preloaded.
- Keep skill.md under ~100 lines as a thin index into a folder; treat a first prompt that consumes 40–50K tokens instead of the baseline 20–25K as a progressive-disclosure failure.
- Run the verifier as a separate agent that cannot see the discovery agent's reasoning traces and that assumes the finding is false by default.
- Make the session an append-only, immutable event log held outside both the harness process and the sandbox, so a container or harness death loses nothing and old context can be fetched back.
- Keep credentials in a vault decrypted only at tool-execution time; the model should never see security tokens and the sandbox should never hold them.
- Measure every agent against the raw baseline model on the same tasks to confirm the harness is actually adding value.
- When letting an agent optimize an agent, explicitly forbid it from editing golden datasets or scorers, run each hypothesis on its own git branch, and roll back on regression.
- Conform the harness to what the model was trained on — apply-patch for edits, ripgrep for search, server-side compaction in the trained format — instead of inventing custom interfaces.
- Constrain effects, not reasoning: route all state-mutating operations through a typed SDK, and have the harness independently verify that claimed edits actually landed.
- Use code for determinism, agents for judgment, and humans for authority; anything with an exact answer should be plain code.
- Treat all externally sourced content (listings, forum threads, reviews, tool output) as evidence, never as instructions.
- Write skill descriptions in the phrasing users actually use, keep them mutually distinct, and re-run evals on every model upgrade because skills are contracts versioned to a model.
- Bound search and tool loops explicitly — e.g. four search rounds max with parallel searches inside each round.
- Instrument outcome signals (was the PR opened, was the report saved) rather than thumbs up/down, and keep the execution layer as the hub where they're collected.

**Avoid:**

- Putting the agent loop and tool execution in the same container — it blocks first-token reasoning on container setup and couples the failure domains (decoupling gave 60% faster TTFT at P50, >90% at P95).
- Using the sandbox for durability, snapshots, or state; sandboxes are ephemeral by design.
- Destructive compaction that discards everything not retained, and self-grading inside the context that produced the work.
- Prescribing a memory schema for the model — specifying what types of memories to save measurably drops performance versus letting the model manage its own.
- Negative instructions ('do not do this') on current-generation models; supply context instead, and expect to cut prompt size ~50% per step-jump model version.
- Cramming four jobs into one giant prompt — the agentic equivalent of a god class, and the direct cause of agent drift.
- Relying on per-action human approval as the governance mechanism for background and cloud agents; policy has to steer deterministically.
- Assuming a newer, higher-benchmark model is a drop-in upgrade — rebuild evals, testing, and validation before swapping.
- Letting a coding agent choose your system architecture, or over-engineering before you know what is actually failing.
- Treating a transcript as proof of what happened; a receipt must record what was allowed, attempted, executed, and confirmed at the user-visible edge.
- Dumping raw page content, full DOM, or whole repositories into the context window instead of compressing to the accessibility tree, summaries, or agent-curated slices.
- Tolerating engineers babysitting agents — it is a defect signal about the codebase setup, not normal practice.

## Notable Outliers

- Long agent run times are a feature, not a defect — under the reasoning paradigm the longer the agent thinks, the better the output, and skills running over an hour became the norm. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [12:20](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=740s))
- The harness should be the output of the engineering process rather than its input — you stop building it and let agents form the harness that best fits the environment at that moment. ([Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [21:12](https://www.youtube.com/watch?v=qdZzND79mcg&t=1272s))
- Contra the 'harness beats model' consensus: friends don't let friends use bad harnesses OR low-intelligence models for important work — an acceptable harness requires sub-agents, plan mode, full MCP support, and file editing, and per-seat AI features can't fund a good enough model. ([Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [15:11](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=911s))
- A 30-year-old healthcare EDI standard (X12) works as the harness because LLMs perform better confined to a strict, limited-vocabulary format — and the standard schema is lookup-able by both new engineers and coding agents. ([Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md), [8:22](https://www.youtube.com/watch?v=UyyOoJmuATU&t=502s))
- At ~1,000 tokens/sec inference, network overhead rather than inference became the dominant bottleneck in the agent loop, forcing a move from server-sent events to a persistent WebSocket that transmits only changed items. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s))
- Filtering timed-out rollouts out of training teaches the model to deliberately abuse tool calls to trigger sandbox timeouts on hard problems and avoid a zero reward — an infrastructure choice with no presence in the reward function still reshapes behavior. ([Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [8:25](https://www.youtube.com/watch?v=k35LeKZEhiE&t=505s))
- Building a good harness requires language-level support — pause/resume, interrupts, partial application to lock tool arguments — not a library or framework, which is why a new language was built for it. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [3:12](https://www.youtube.com/watch?v=2e9ANoOEn28&t=192s))
- Zero rollouts earning reward through an exploit should be the acceptance bar for long-horizon evals; at multi-hour lengths a weak verifier stops being noise and becomes an attack surface (9% of 1,400 rollouts had clear verifier bypasses). ([SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [9:42](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=582s))

## All Talks

- [A Genius With Amnesia](../talks/a-genius-with-amnesia.md)
- [Agentic Development Security](../talks/agentic-development-security.md)
- [Agents Building Agents](../talks/agents-building-agents.md)
- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)
- [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)
- [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Evals-Driven Development for a Mental Health AI Coach](../talks/evals-driven-development-for-a-mental-health-ai-coach.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [From RL to IRL](../talks/from-rl-to-irl.md)
- [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
- [Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md)
- [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)
- [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md)
- [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)
- [On AI and Knowledge](../talks/on-ai-and-knowledge.md)
- [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)
- [Respect The Process](../talks/respect-the-process.md)
- [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)
- [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)
- [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)
- [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)
- [The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md)
- ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)
- [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)
- [Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md)
- [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)
- [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)
- [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)
- [Voice agents with Realtime Video](../talks/voice-agents-with-realtime-video.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)
- [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Ahmad Osman](../speakers/ahmad-osman.md)
- [Akele Reed](../speakers/akele-reed.md)
- [Alex Bauer](../speakers/alex-bauer.md)
- [Alex Cheema](../speakers/alex-cheema.md)
- [Alexander Embiricos](../speakers/alexander-embiricos.md)
- [Andrew Dumit](../speakers/andrew-dumit.md)
- [Angie Jones](../speakers/angie-jones.md)
- [Apoorva Joshi](../speakers/apoorva-joshi.md)
- [Brendan Rappazzo](../speakers/brendan-rappazzo.md)
- [Carter Abdallah](../speakers/carter-abdallah.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Dan Farrelly](../speakers/dan-farrelly.md)
- [Dave Revere](../speakers/dave-revere.md)
- [Denys Linkov](../speakers/denys-linkov.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Doug Keller](../speakers/doug-keller.md)
- [Du'an Lightfoot](../speakers/du-an-lightfoot.md)
- [Emil Eifrem](../speakers/emil-eifrem.md)
- [Eno Reyes](../speakers/eno-reyes.md)
- [Eugene Yan](../speakers/eugene-yan.md)
- [Ezra Tanzer](../speakers/ezra-tanzer.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Gaurav Mishra](../speakers/gaurav-mishra.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [Hanna Lichtenberg](../speakers/hanna-lichtenberg.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [James Le](../speakers/james-le.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Joseph Nelson](../speakers/joseph-nelson.md)
- [Lance Martin](../speakers/lance-martin.md)
- [Lina Colucci](../speakers/lina-colucci.md)
- [Lucas Atkins](../speakers/lucas-atkins.md)
- [Matthew Berman](../speakers/matthew-berman.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Natalie Meurer](../speakers/natalie-meurer.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Pablo Castro](../speakers/pablo-castro.md)
- [Paul Iusztin](../speakers/paul-iusztin.md)
- [Paul Klein IV](../speakers/paul-klein-iv.md)
- [Rajiv Chandegra](../speakers/rajiv-chandegra.md)
- [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)
- [Raymond Feng](../speakers/raymond-feng.md)
- [Rishi Desai](../speakers/rishi-desai.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Saoud Rizwan](../speakers/saoud-rizwan.md)
- [Sean Cai](../speakers/sean-cai.md)
- [Shashi](../speakers/shashi.md)
- [Soheil Feizi](../speakers/soheil-feizi.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Vasant Kearney](../speakers/vasant-kearney.md)
- [Victor Savkin](../speakers/victor-savkin.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Will Brown](../speakers/will-brown.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

