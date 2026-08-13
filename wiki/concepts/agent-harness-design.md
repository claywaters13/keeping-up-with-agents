---
title: "agent harness design"
type: "concept"
slug: "agent-harness-design"
tier: "core"
maturity: "consolidating"
talk_count: 47
speaker_count: 59
---

# agent harness design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **47** talk(s) by **59** speaker(s)

**Definition:** The engineering of the scaffold around a model — loop, prompts, tools, memory, and control flow — treated as the primary unit of design and iteration, distinct from the model itself.

*Also referred to as: harness engineering, agentic harness design, agent harness architecture, agent scaffold design, harness design, meta harness design, model-harness co-design*

## State of Practice

The conference's dominant claim is that the harness — loop, prompts, tools, memory, state, and control flow — is now the binding constraint on agent performance, not the model. Multiple speakers measured this directly: holding model and eval fixed while varying only the harness moved a 106-task benchmark from 52.4% to 76.2%, and a well-scaffolded Haiku 4.5 replaced Opus-class models in latency-bound voice work. The architectural consensus that emerged is decoupling: separate the agent loop from tool execution and sandboxes (Anthropic reported 60% faster P50 time-to-first-token from this), keep credentials in a vault the model never sees, back sessions with an append-only event log rather than destructive compaction, and put verification in a separate context window from the work. Context is treated as a budget with hard numbers — Codex caps skill descriptions at 2% of the context window and defers tools to lazy search; Amazon caps skill.md at 100 lines and treats a 40-50K first prompt as a progressive-disclosure failure. The unresolved tension is temporal: harnesses encode assumptions about what the model can't do, and those assumptions rot — Anthropic showed context-anxiety fixes becoming pure overhead within one model generation — so speakers split sharply on whether to invest in harness scaffolding at all versus waiting for or training the model.

## Consensus

### The harness, not model capability, is now the limiting factor on what agent products can achieve.

Support: **8** talk(s)

> "harnesses have become the limiting factor to what models can achieve"
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [30:20](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1820s)

Supporting talks: [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md)

### Verification must run in a separate agent/context from the one that produced the work, because self-grading in the same context causes confabulation and self-censoring.

Support: **5** talk(s)

> "when the discovery agent is trying to verify its own work in the loop, trying to debate against itself in the loop, it may actually self censor and this may actually hurt recall"
>
> — [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [11:46](https://www.youtube.com/watch?v=imFedndyXYQ&t=706s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)

### A strong harness lets a smaller or open model match a frontier model on the target task, because intelligence can be moved into the surrounding system.

Support: **6** talk(s)

> "instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn't have as much reasoning capabilities, but because of the harnessing around it, it's still able to perform at the level in which we expect"
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s)

Supporting talks: [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [State of the Union: Why Local, Why Now](../talks/state-of-the-union-why-local-why-now.md)

### State and durability must live outside the model and outside the sandbox — the harness owns the state transitions, and the session must survive container or harness death.

Support: **6** talk(s)

> "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Build Systems, Not Code](../talks/build-systems-not-code.md)

### Context loaded into the harness must be explicitly budgeted with progressive disclosure — loading everything up front degrades quality, not just cost.

Support: **6** talk(s)

> "the more context you have in your in your context, the higher it is that you have contradicting information and it causes confusion for the model."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md), [Field Guide to Fable](../talks/field-guide-to-fable.md)

### Agent output quality is bounded by the density of deterministic validation loops available to the harness, so preparing the environment for verification matters more than improving the agent.

Support: **5** talk(s)

> "the quality of the output of these very long-running harnesses of advanced agents is directly proportional to the degree to which you can validate their work"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [12:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=777s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Respect The Process](../talks/respect-the-process.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Agents Building Agents](../talks/agents-building-agents.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)

### Agents falsely report success, so the harness must independently prove the effect landed rather than trusting the transcript or the tool's own return.

Support: **4** talk(s)

> "A transcript tells you what the agent said. A receipt tells you what the system allowed, attempted, executed and what the user visible edge confirmed."
>
> — [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [3:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=203s)

Supporting talks: [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Respect The Process](../talks/respect-the-process.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)

### Credentials and authority must be enforced by the harness, not the model: secrets stay in a vault outside the sandbox and high-consequence actions are gated deterministically.

Support: **5** talk(s)

> "If the session, uh sorry, if the harness dies or sandbox dies, it's completely fine because the session is always backed up in this append-only log and credentials are never actually added to the sandbox."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [4:38](https://www.youtube.com/watch?v=9QebvrrY3KY&t=278s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Agentic Development Security](../talks/agentic-development-security.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

## Disagreements

### Should the harness be hand-designed up front, or should it emerge and adapt at runtime?

| Position A | Position B |
|---|---|
| Design the harness deliberately as software engineering — explicit state machines, decomposed workflows, typed SDKs, separation of concerns, governance — because the discipline of software engineering still applies and letting an agent throw it together yields unmaintainable systems.<br>*[Build Systems, Not Code](../talks/build-systems-not-code.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Respect The Process](../talks/respect-the-process.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)* | Fixed harnesses buy reliability by suppressing the variance novelty requires and go stale as models improve; the harness should be the output of the process, emerging from agent interaction and local coordination in ways you cannot specify in advance.<br>*[Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [Agents Building Agents](../talks/agents-building-agents.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)* |

*Why it matters: This determines whether harness work is a durable engineering asset or a depreciating one, and whether teams staff it with software architects writing explicit control flow or with meta-optimization loops that rewrite the scaffold themselves.*

### Should you build your own harness or adopt a managed one?

| Position A | Position B |
|---|---|
| Build it yourself: writing your own harness from scratch gives maximum freedom to tweak anything, avoids vendor lock-in over your traces and data, and you know what you are looking for in your own monitoring better than any vendor.<br>*[Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)* | Buy it: hosting, session management, sandboxing, credentials, and observability are undifferentiated work; developers should own only system prompts, skills, tools, and domain context and get the loop, memory, and observability from a managed harness.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)* |

*Why it matters: It decides where a team's scarce engineering time goes — into infrastructure that a vendor may commoditize within months, or into domain context that everyone agrees is the durable differentiator.*

### Is harness scaffolding a good investment, or a stopgap that model progress will erase?

| Position A | Position B |
|---|---|
| Scaffolding is a one-time cost paid in code rather than on every turn, and there is a large capability overhang you can capture today by doing the engineering work — waiting for better models is the wrong answer.<br>*[Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)* | Harness fixes encode assumptions about what the model cannot do and become pure overhead — added latency, cache invalidation bugs — the moment the model improves; guardrails are a transitional scaffold that should get thinner over time, and a careful harness can be irrelevant within a month.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [From RL to IRL](../talks/from-rl-to-irl.md), [Field Guide to Fable](../talks/field-guide-to-fable.md)* |

*Why it matters: It sets how much control flow you pull out of the model and how you amortize that work: teams in camp A ship deterministic state machines that outlive several model generations, while camp B builds thin swappable primitives and budgets for migration every release cycle.*

### Should the harness constrain the model's control flow, or supply context and let the model decide?

| Position A | Position B |
|---|---|
| Take control flow out of the model: the model proposes and the harness decides. Judgments like whether a task is complete or what step comes next should be engineered outside the model, and prescriptive rules keep small models from drifting.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)* | Give the model context, not constraints: newer models perform better with smaller system prompts because in-prompt examples constrain a model more imaginative than the examples, negative instructions should be replaced with context, and prescriptive memory schemas make performance drop versus letting the model manage its own memory.<br>*[Field Guide to Fable](../talks/field-guide-to-fable.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* |

*Why it matters: The two camps prescribe opposite edits to the same file — one adds rules and state machines, the other deletes 80% of the system prompt — and picking wrong either caps the model's ceiling or lets it drift on multi-step work.*

### Is a monorepo or a multi-repo meta-harness the right substrate for agentic development?

| Position A | Position B |
|---|---|
| Consolidate into a monorepo: even though models now navigate multi-repo directory trees well, end-to-end testing, verification, deployment, and sandbox cloning remain much harder across repos, so a six-month refactor was worth doing now rather than waiting.<br>*[Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)* | Keep the repos and add a meta-harness layer above the agent: a unified dependency graph built from metadata extraction plus multi-repo CI treated as a single vector lets you treat a complex multi-repo change as if it were a single-repo change, with no code changes to the analyzed repos.<br>*[A Genius With Amnesia](../talks/a-genius-with-amnesia.md)* |

*Why it matters: One path spends months of engineering restructuring the codebase itself; the other spends it on an agent-agnostic tooling layer, and the two are largely mutually exclusive investments.*

### Where should agent improvement happen — in the harness, or in the model weights via training on the real harness?

| Position A | Position B |
|---|---|
| Improve in the harness and memory layers: continual learning is not necessarily fine-tuning, many useful updates are prompt/tool/memory edits, and coding agents can autonomously improve another agent's system prompt, tool descriptions, and tool logic to raise pass rates.<br>*[Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [Agents Building Agents](../talks/agents-building-agents.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md)* | Train the model inside the customer's real production harness: simulating reality is infeasible and any environment defect induces subtle undesirable behaviors, so post-train on the harness you care about rather than patching around the model.<br>*[Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md), [From RL to IRL](../talks/from-rl-to-irl.md)* |

*Why it matters: It determines whether the harness is the artifact you optimize or merely the environment you optimize in — and whether an agent team needs a training stack at all.*

## Practical Guidance

**Do:**

- Decouple the agent loop from tool execution and the sandbox — Anthropic measured 60% faster time-to-first-token at P50 and >90% at P95 from not blocking model reasoning on container setup.
- Back the session with an append-only, immutable event log rather than destructive compaction, so the model can fetch back discarded context and a harness or sandbox death loses nothing.
- Run verification as a separate agent with a separate context that cannot see the discovery agent's reasoning traces and assumes the finding is false by default.
- Cap the skill/tool description block at 2% of the total context window and mark tools as deferred so they are discovered via tool search rather than preloaded.
- Cap skill.md at ~100 lines and treat it as a thin index into a folder; if your first prompt exceeds 40-50K tokens of baseline context, progressive disclosure has failed.
- Keep credentials in a vault decrypted only at tool execution time and never added to the agent's sandbox container — the model should never see security tokens.
- Conform the harness to what the model was trained on (apply_patch for edits, Ripgrep for search, server-side compaction in the trained format) rather than inventing your own interfaces.
- Write goal prompts that are concrete and verifiable rather than long essays, since the loop only terminates when the model can detect the goal was achieved.
- Take control-flow decisions — is the task done, did the user succeed, what step is next — out of the model when reliability approaches a coin flip.
- Constrain the agent's effects, not its expression: route all state-changing operations through a typed SDK as the only door, and orchestrate a deterministic final validation script on agent completion.
- Prove effects independently: emit receipts recording what the system allowed, attempted, executed, and what the user-visible edge confirmed, because agents claim edits they did not make.
- Enforce one ordered commit path per mutable state boundary rather than banning concurrency globally — parallel reads and sub-agent fan-out are fine.
- Give every external boundary a terminal state (success, failure, timeout, cancel, max attempts) and make recovery commands runnable without queueing behind the stuck work.
- Add an out-of-band consolidation/'dreaming' pass over session transcripts plus memory state to correct memories that were locally optimal or wrong when written in-band.
- Let the model structure its own memory on a highly programmable substrate with simple primitives; do not impose a prescriptive memory schema.
- Forbid the optimizing agent from editing golden datasets or scorers, run each optimization hypothesis on its own git branch, and roll back on regression.
- Measure every agent against the baseline model on the same task to confirm the harness is actually adding value.
- Use code for determinism, agents for judgment, and humans for authority; if a task has an exact answer, reach for code.
- Treat all externally sourced content as untrusted evidence rather than instructions, and wall high-consequence actions behind human approval to reduce blast radius.
- Instrument the full session trace — database errors, permissions, triggers, performance — not just LLM and tool calls, and make traces inspectable by agents so reviewer functions can evaluate them.

**Avoid:**

- Putting the harness, the agent loop, and the sandbox in the same container — the container blocks first-token reasoning and its death takes the whole session with it.
- Using the sandbox for durability, snapshots, or state; sandboxes are ephemeral and stateless by design.
- Encoding fixes for the current model's limitations into the harness — Opus 4.5 stopped exhibiting context anxiety and the mitigations became pure overhead, adding latency and discarding cache incorrectly.
- Dumping full page content, whole repos, or entire datasets into the context window; oversized context raises the chance of contradicting information and degrades quality, not just cost.
- Cramming four jobs into one giant prompt — that is the agentic equivalent of a god class and the direct cause of agent drift.
- Letting a coding agent design your other agents or choose your system architecture; it produces something that technically works but is unmaintainable and over-engineered.
- Relying on the model's own safety judgment — Claude refused to read an .env file but complied when asked for a specific secret key.
- Relying on human approval as the governance mechanism for background and cloud agents, where nobody is sitting at the desk to answer.
- Treating a tool's success return or the transcript as proof of an outcome; internal success is not external proof.
- Running a single test suite as the verifier on multi-hour tasks — 12.8% of rollouts showed shortcut behavior and 9% a clear verifier bypass, and a weak verifier stops being noise and becomes an attack surface.
- Filtering timed-out rollouts out of training, which incentivizes the model to deliberately trigger sandbox timeouts on hard problems.
- Handing the agent a general-purpose VM, which invites it to route around instructions using whatever it finds there (writing Python when instructed to write TypeScript).
- Resetting the environment on infrastructure errors during computer-use training — pass the error to the model so recovery becomes a native action.
- Building a skill routing mechanism that assumes all skills fit in the system prompt; past ~10 skills you need shortlisting, past hundreds you need hierarchy, metadata filters, and governance.
- Writing skill descriptions that describe the skill rather than matching the phrasing of user requests — the descriptions are the routing signals.
- Babysitting the agent: if engineers on your team are watching their agents run, the codebase and harness setup is wrong.
- Assuming more parallel agents means more capacity — human cognitive bandwidth does not parallelize, and every extra loop adds routing, merging, and verification decisions.
- Shipping without production observability and a post-launch loop; scripted simulations and rule-based checks cover only one slice of agent failure.

## Notable Outliers

- Changing only the harness — model and evaluation held constant across 106 tasks — moved scores from 52.4% to 76.2%, and the harness matters more for weaker models than for stronger ones. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s))
- Building a good harness requires language-level support, not just a library or framework — existing tools were incapable of true pause/resume and capability constraint, so a new language was necessary. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [3:12](https://www.youtube.com/watch?v=2e9ANoOEn28&t=192s))
- Determinism and emergence pull in opposite directions: a fixed harness buys reliability by suppressing exactly the variance novelty requires, so the harness should be the ongoing output of engineering rather than its input. ([Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [8:27](https://www.youtube.com/watch?v=qdZzND79mcg&t=507s))
- General auto-research capability will become a commodity, so 'whatever lives in the middle' — the harness — is what an enterprise should almost stop caring about; durable value comes from building environments. ([Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [18:25](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=1105s))
- Anthropic removed 80% of the Claude Code system prompt, because in-prompt examples constrain a model that is more imaginative than the examples. ([Field Guide to Fable](../talks/field-guide-to-fable.md), [5:47](https://www.youtube.com/watch?v=9fubhllmsBU&t=347s))
- At ~1,000 tokens/sec inference, network overhead rather than inference becomes the dominant bottleneck in the agent loop, which is why the Responses API uses a persistent WebSocket transmitting only changed items instead of SSE over HTTP. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s))
- Simulating reality is infeasible, so the right response to environment-fidelity failures is to train directly inside the customer's real production harness — needing only a completion endpoint plus request/response recording. ([Learning on the Job: The Future of Post-Training](../talks/learning-on-the-job-the-future-of-post-training.md), [9:21](https://www.youtube.com/watch?v=k35LeKZEhiE&t=561s))
- Every harness will expand until it becomes a claw — always-on, with initiative and learning — and a consolidation shakeout will leave room for only one or two per category. ([Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md), [9:35](https://www.youtube.com/watch?v=8qWIPUia2O8&t=575s))
- The right fix for agents' space and time constraints lives in an agent-agnostic meta-harness above the agent, making memory portable enough to resume a Claude session in Codex mid-stream. ([A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [14:37](https://www.youtube.com/watch?v=jVjt-2g8NMY&t=877s))
- Agent skills are a greater supply-chain risk than package dependencies — an audit of ~4,000 ClawHub skills found over one in eight with a critical issue and 76 malicious payloads, and malicious skills persist by modifying agent memory even after removal. ([Agentic Development Security](../talks/agentic-development-security.md), [7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s))
- Agents write keyword-stuffed 'caveman style' queries because they are trained on grep-based code exploration and benchmarked against BM25-favoring suites; instructing the model to write 'one concise sentence describing what it wants to find' fixes it. ([How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md), [9:05](https://www.youtube.com/watch?v=1IdzkRVmWAA&t=545s))
- The execution layer is the only long-lived layer — prompts last weeks, models months, execution years — and coupling the layers lets the shortest half-life drag the others into rewrites. ([Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [3:37](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=217s))
- Anthropic's published accuracy for agents on data projects is only 21% until you add a purpose-built data harness and supply context; using stronger models will not fix it because everyone already uses frontier models. ([When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [0:02](https://www.youtube.com/watch?v=bUJgirn4_yc&t=2s))
- A 20-point spread aside, harness architecture decisions like the number of strategist agents are arbitrary human choices and are themselves a verifiable loop that an LLM should meta-optimize. ([Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [15:00](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=900s))

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
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [How we taught agents to use good retrieval](../talks/how-we-taught-agents-to-use-good-retrieval.md)
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
- [Victor Savkin](../speakers/victor-savkin.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Will Brown](../speakers/will-brown.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

