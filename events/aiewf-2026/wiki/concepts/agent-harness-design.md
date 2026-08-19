---
title: "agent harness design"
type: "concept"
slug: "agent-harness-design"
tier: "core"
maturity: "consolidating"
talk_count: 49
speaker_count: 61
---

# agent harness design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **49** talk(s) by **61** speaker(s)

**Definition:** The engineering of the scaffold around a model — loop, prompts, tools, memory, and control flow — treated as the primary unit of design and iteration, distinct from the model itself.

*Also referred to as: harness engineering, agentic harness design, agent harness architecture, agent scaffold design, harness design, meta harness design, model-harness co-design*

## State of Practice

The conference's organizing claim was that the harness — loop, prompts, tools, memory, control flow, execution substrate — has displaced the model as the binding constraint on what agents can do. This was asserted from both ends of the stack: Anthropic and OpenAI harness teams said harnesses now limit what models can achieve, and independent measurements backed it (holding model and eval fixed across 106 tasks, swapping only the harness moved scores 52.4%→76.2%; Anthropic's own data agents hit 21% accuracy without a domain data harness; Browserbase and Mixedbread each showed domain harnesses pushing above baseline model performance). The concrete architecture that converged is: decouple the agent loop from tool-execution containers, keep session state in an append-only durable log outside both, keep credentials in a vault decrypted only at tool-execution time, budget eagerly-loaded context as an explicit fraction of the window (Codex caps skill descriptions at 2%; Amazon caps skill.md at 100 lines and flags a first prompt above 40-50K tokens as broken progressive disclosure), and run verification in a separate context or agent from the one that produced the work. A second consensus is about authority: the model proposes, the harness commits — state transitions, ordering, approvals, and proof of effect belong in deterministic code, and a transcript or a tool's 'success' is not evidence the action landed. The live arguments are not about whether the harness matters but about who writes it (build-your-own vs. outsource undifferentiated infrastructure), whether harness investment is durable or decays with each model release, and whether agents should be optimizing their own harnesses.

## Consensus

### The harness — not model capability — is now the binding constraint on agent performance, and closing that gap is ordinary engineering work rather than lab work.

Support: **10** talk(s)

> "harnesses have become the limiting factor to what models can achieve"
>
> — [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [30:20](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=1820s)

Supporting talks: [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [A Genius With Amnesia](../talks/a-genius-with-amnesia.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)

### A sufficiently good harness lets a smaller, cheaper, or open model reach the performance level teams expect from a frontier model.

Support: **6** talk(s)

> "instead of having a very heavy model like a 4.7, we were actually able to rely on something like a Haiku 4.5, which is a much smaller model, doesn't have as much reasoning capabilities, but because of the harnessing around it, it's still able to perform at the level in which we expect"
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [2:27](https://www.youtube.com/watch?v=m24UKZomm7k&t=147s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Local Models: Trust, Control, Optimization](../talks/local-models-trust-control-optimization.md)

### Verification must run in a context separate from the one that produced the work; self-grading in the producing context degrades recall and produces confabulation.

Support: **6** talk(s)

> "what we found is it's quite effective to separate verification into a separate context window. This is a very general trend."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [6:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=404s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md)

### What the harness loads up front must be budgeted as an explicit fraction of the context window, with everything else deferred behind lazy discovery (tool search, file reads, thin indexes).

Support: **6** talk(s)

> "for available skills, we actually cap the available skills list at 2% of your context total like maximum context window."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)

### The harness, not the model, must own state transitions, control flow, and authority: the model proposes and the harness decides, commits, and proves the effect landed.

Support: **7** talk(s)

> "A model proposes the harness commits and the receipts proves it."
>
> — [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [2:40](https://www.youtube.com/watch?v=BInpv7lGp1o&t=160s)

Supporting talks: [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Respect The Process](../talks/respect-the-process.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md), [Agentic Development Security](../talks/agentic-development-security.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### How far an agent can be trusted to run autonomously is gated by the density of deterministic validation loops around it, not by model capability.

Support: **6** talk(s)

> "the quality of the output of these very long-running harnesses of advanced agents is directly proportional to the degree to which you can validate their work"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [12:57](https://www.youtube.com/watch?v=wpOA-UXynoM&t=777s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [Agents Building Agents](../talks/agents-building-agents.md), [SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)

### For long-running agents, the agent loop, the tool-execution sandbox, and session state must be three separate failure domains, with state in a durable append-only log and credentials never inside the sandbox.

Support: **3** talk(s)

> "If the session, uh sorry, if the harness dies or sandbox dies, it's completely fine because the session is always backed up in this append-only log and credentials are never actually added to the sandbox."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [4:38](https://www.youtube.com/watch?v=9QebvrrY3KY&t=278s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)

## Disagreements

### Should a coding agent be allowed to design and optimize the agent harness itself?

| Position A | Position B |
|---|---|
| Yes — point a coding agent at the harness with evals as the objective; it finds improvements humans missed (18%→83% pass rate in ~10 iterations, +10% on an already human-optimized production agent), and even the harness's own architectural choices (agent counts, roles) should be meta-optimized by an LLM rather than hand-picked.<br>*[Agents Building Agents](../talks/agents-building-agents.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [On AI and Knowledge](../talks/on-ai-and-knowledge.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* | No — a coding agent produces something that technically works but is unmaintainable (a giant prompt with no separation of concerns), risks over-engineering the architecture before you know what is failing, produces micromanagement when asked to improve its own prompts, and its trace-to-harness edits are untestable and introduce hidden regressions.<br>*[Build Systems, Not Code](../talks/build-systems-not-code.md), [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [Continual Learning for AI Agents: From Failures to Durable Improvements](../talks/continual-learning-for-ai-agents-from-failures-to-durable-improvements.md)* |

*Why it matters: If self-optimization works, harness quality becomes a compute-bound problem and the human's job is writing golden datasets and scorers; if it doesn't, harness design stays a human architecture discipline and the agent's role is capped at proposing changes that a regression-aware, human-reviewed loop must verify.*

### Should teams build their own agent harness or outsource it as undifferentiated infrastructure?

| Position A | Position B |
|---|---|
| Build it. An off-the-shelf framework costs you the freedom to tweak anything that matters; the software factory must be built rather than bought, and if you don't own the traces and data flowing through it you can't evolve it. Some went as far as building their own language because existing frameworks couldn't express the safety and pause/resume semantics a harness needs.<br>*[Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)* | Buy it. Hosting, session management, sandboxing, credential vaults, and observability are undifferentiated work; developers should own only system prompts, skills, tools, and domain context. Browser-agent infrastructure in particular should be bought so teams spend their time on customer problems.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)* |

*Why it matters: This decides where a team's engineering headcount goes and how much model/vendor lock-in it accepts — and both camps agree the harness is where competitive advantage lives, which makes outsourcing it either an obvious efficiency or a strategic mistake depending on which side is right.*

### Is harness engineering a durable investment, or scaffolding that decays with every model release?

| Position A | Position B |
|---|---|
| It decays. Harnesses encode assumptions about what the model cannot do; when the model improves, those fixes become pure overhead adding latency and cache-invalidation bugs. A carefully built harness can be irrelevant within a month, prompts should shrink ~50% per step-jump model version, 80% of a system prompt can be deleted outright, and guardrails should get progressively thinner as the model gets better.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [Field Guide to Fable](../talks/field-guide-to-fable.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [From RL to IRL](../talks/from-rl-to-irl.md)* | It is durable if layered correctly. Prompts last weeks and models months, but a properly decoupled execution layer — flow, state, durability, retries — lasts years; the harness that watches itself is the competitive advantage precisely because everyone has the same models.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)* |

*Why it matters: It sets whether harness work should be budgeted as a standing organizational investment or as disposable scaffolding to be audited and deleted at each model upgrade — and whether a stale harness or an under-built one is the bigger risk.*

### Should the harness be specified in advance by engineers, or allowed to emerge from agent interaction at runtime?

| Position A | Position B |
|---|---|
| Specified. The workflow defines the path, every run terminates in stop/retry/escalate, a lesson is an explicit state machine, and the model never decides where it is — reliability was never a prompting problem, it is a control problem.<br>*[Build Systems, Not Code](../talks/build-systems-not-code.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)* | Emergent. Fixed harnesses buy reliability by suppressing the variance novelty requires; for moving, complex problems the engineer should design constraints such that the harness emerges, stabilizes, and reorganizes at runtime, with roles and governance arising from local coordination rather than assignment.<br>*[Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)* |

*Why it matters: The determinism camp's methods are what make small models and auditability viable; if the emergent camp is right, that same determinism is a hard ceiling on what agent systems can discover, and legibility must be traded away deliberately.*

### How much structure should the harness impose on agent memory and context?

| Position A | Position B |
|---|---|
| Impose it. Push data discovery, mapping, and trust into a shared ontology-based substrate so agents stay thin; use an explicit index → summary → derivative → source hierarchy over plain markdown; store extracted primitives in a typed schema rather than letting the agent re-derive them; append-only memory with search over it will not scale to multi-year use.<br>*[Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer](../talks/thinner-agents-on-a-smarter-substrate-the-ontology-based-semantic-layer.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md), [When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [Video Has No Memory. Here's How We Built One.](../talks/video-has-no-memory-heres-how-we-built-one.md)* | Don't. Prescribing the structure of memory measurably drops performance; give the model a highly programmable substrate with simple primitives and let it structure and maintain its own memory, correcting drift with an out-of-band consolidation pass rather than an imposed schema.<br>*[Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Field Guide to Fable](../talks/field-guide-to-fable.md)* |

*Why it matters: It determines whether memory investment goes into ontology/schema engineering that transfers across agents, or into offline consolidation loops over unstructured stores the model owns — and the two produce very different migration costs when the model changes.*

## Practical Guidance

**Do:**

- Cap eagerly-loaded harness content as an explicit fraction of the context window (Codex: skill descriptions ≤2% of max context; Amazon: skill.md ≤100 lines, first-prompt baseline ~20-25K tokens, treat 40-50K as a progressive-disclosure failure) and defer the rest behind tool search or file reads.
- Run verification as a separate agent that cannot see the producing agent's reasoning traces and defaults to assuming the finding is false; independent discovery/verification raised true-positive rates to ~90-100% in security scanning.
- Decouple the agent loop from the tool-execution container — Anthropic measured 60% faster time-to-first-token at P50 and >90% at P95 — and keep session state in an append-only event log so a dead harness or sandbox loses nothing.
- Store credentials in a vault decrypted only at tool-execution time; the model should never see security tokens and secrets should never be added to the sandbox.
- Conform the harness to what the model was trained on (apply_patch for edits, ripgrep for search, server-side compaction in the trained format) instead of inventing your own interfaces.
- Measure every agent against the bare baseline model on the same tasks to prove the harness is actually adding value.
- Allocate responsibility explicitly: code for determinism, agents for judgment, humans for authority; if a task has an exact answer, use plain code.
- Have the harness independently confirm that claimed effects landed — receipts recording allowance, attempt, execution, and edge confirmation — because agents will report edits they never made.
- Constrain effects rather than expression: force all state-changing work through one typed SDK, lock tool arguments via partial application so the model can't see or change them, and orchestrate a deterministic final validation script on agent completion.
- Give every external boundary a terminal state (success, failure, timeout, cancel, max attempts) and one ordered commit path per mutable state boundary; keep recovery commands from queueing behind the stuck work.
- Re-run evals on skills and prompts at every model upgrade — skills are contracts versioned to a model, and instruction placement inside a skill file changes behavior across versions.
- Audit the harness at each model release and delete workarounds the new model no longer needs; cut prompt size roughly 50% per step-jump model version.
- Turn on tracing in production and point an agent at the traces — production is where you learn what to test, and a fix-generating agent should be separate from the reviewing agent.
- Forbid the optimizing agent from editing golden datasets or scorers, and run each optimization hypothesis on its own git branch with rollback on regression.

**Avoid:**

- Letting the model hold the state of a multi-step workflow — when reliability approaches a coin flip, take control flow out of the model entirely.
- Grading work in the same context window that produced it; it yields confabulation and, in security scanning, self-censoring that costs recall.
- Putting the harness and the sandbox in the same container — a container death takes the whole session, and container setup blocks first-token reasoning.
- Giant multi-job prompts: four responsibilities crammed into one prompt is the agentic god class, and it is why agents drift off the script.
- Treating a transcript, or a tool call returning success, as proof that anything happened or that the user saw the result.
- Dumping full page content, raw DOM/HTML, or whole traces into context — it costs more and produces worse results than a compressed, purpose-built representation.
- Relying on human approval as the governance mechanism for background and cloud agents, or on model-level safety judgment instead of deterministic local guardrails.
- Prescribing an explicit memory schema for the model to fill in; measured performance drops relative to letting the model manage its own memory.
- Building on a vendor-locked single-model platform where you don't own the traces and data flowing through your factory.
- Babysitting agents — it is a signal the codebase/harness setup is wrong, and silently burns context and money (blowing through 500K-1M context on simple tasks).
- Shipping an agent without an observability loop, and treating launch as the end of the work rather than the point where the real loop begins.
- Full-access/YOLO modes: pushing a model toward high agency produces actions that diverge from intent, and approval decisions need task context (deleting a file is fine or not depending on what was asked).
- Adding third-party skills and MCP servers without auditing them — 1 in 8 of ~4,000 audited ClawHub skills had a critical-severity issue, 76 carried malicious payloads, and malicious skills can persist by writing to agent memory.

## Notable Outliers

- Holding the model and the evaluation constant across 106 tasks and changing only the harness produced a 52.4% to 76.2% spread — and the harness matters more for weaker models than for stronger ones. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s))
- The harness should be the ongoing output of the engineering process rather than its input — you design constraints and let agents form the harness that fits the environment, because determinism and emergence pull in opposite directions. ([Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [21:12](https://www.youtube.com/watch?v=qdZzND79mcg&t=1272s))
- Anthropic published that agent accuracy on data projects is only ~21% until you add a purpose-built data harness and supply context — and that finding was on structured business data, so it understates the problem for unstructured data. ([When Agents Meet Physical Data: The Other Physics of Agent Harnesses](../talks/when-agents-meet-physical-data-the-other-physics-of-agent-harnesses.md), [0:02](https://www.youtube.com/watch?v=bUJgirn4_yc&t=2s))
- At 1,000 tokens/sec inference, the bottleneck in the agent loop stopped being inference and became the network, which is why Codex moved to a persistent WebSocket that transmits only changed items. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s))
- On billion-token project-scale tasks, the best configuration (Opus 4.8 + Claude Code) resolves only 26%, and 9% of 1,400 rollouts contained a clear verifier bypass — at multi-hour horizons a weak verifier is an attack surface, not noise. ([SWE-Marathon: Evaluating Coding Agents at Billion-Token Scale](../talks/swe-marathon-evaluating-coding-agents-at-billion-token-scale.md), [9:42](https://www.youtube.com/watch?v=Rx8f05JI_WA&t=582s))
- If a developer is babysitting their agent, the setup is wrong — and long agent run times are good, not bad, because under the reasoning paradigm longer thinking produces better output. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [3:51](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=231s))
- Harness fixes that encoded a model's limitations became pure overhead once Opus 4.5 stopped exhibiting context anxiety — adding latency and causing the cache to be discarded incorrectly. ([Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [8:08](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=488s))
- Harness guardrails are transitional scaffolding by design: strong early, then progressively thinner as the model absorbs recovery, handoff, and risk calibration as native actions. ([From RL to IRL](../talks/from-rl-to-irl.md), [17:12](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=1032s))
- Keep the harness ignorant that it is doing RL, so the identical harness runs in training and in production. ([Modern Post-Training: A Deep Dive](../talks/modern-post-training-a-deep-dive.md), [22:26](https://www.youtube.com/watch?v=V-EDrhIhHzQ&t=1346s))
- The general ability to do auto-research will commoditize, so an enterprise's durable value is in building environments, not harnesses — whatever lives in the middle, in the limit, doesn't matter. ([Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md), [18:25](https://www.youtube.com/watch?v=kiqubc5b5Yo&t=1105s))

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
- [Victor Savkin](../speakers/victor-savkin.md)
- [Vincent Weisser](../speakers/vincent-weisser.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Will Brown](../speakers/will-brown.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

