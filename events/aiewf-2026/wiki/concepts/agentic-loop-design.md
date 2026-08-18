---
title: "agentic loop design"
type: "concept"
slug: "agentic-loop-design"
tier: "core"
maturity: "consolidating"
talk_count: 30
speaker_count: 32
---

# agentic loop design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **30** talk(s) by **32** speaker(s)

**Definition:** The structure of the perceive–decide–act–observe cycle itself: iteration control, stopping conditions, and how control flows between model and runtime.

*Also referred to as: agentic loops, agentic loop, agent loop architecture, agent loop design, react agent loop, agent tool-calling loop, agent loop termination*

## State of Practice

The field has stopped treating the loop as a thin while-loop around a chat completion and started treating it as an engineered control system with its own state, sensors, budgets, and gates. The consensus mechanics are: the runtime — not the model — owns workflow state and control flow; every loop needs an explicit termination gate (max iterations, a numeric threshold, a stop_reason branch, or an eval/grader that must pass) because the model's own claim of 'done' is a bundle of unverified claims; context is a budgeted resource inside each iteration (Codex caps the skill-description block at 2% of the window, panelists recommend staying under ~100k tokens even with million-token windows, tool schemas get filtered by semantic search to the top three); and the thing that closes the loop must be structurally separate from the thing that produced the work — a different model, a different sensory channel, or deterministic code. Speakers now routinely report that harness design, not model capability, is the binding constraint: one controlled experiment held model and eval fixed across 106 tasks and moved the score from 52.4% to 76.2% by changing only the harness, and a Microsoft team replaced Opus 4.7 with Haiku 4.5 at expected quality by moving control flow out of the model. Infrastructure concerns that used to sit outside the loop are now loop-design decisions: decoupling the agent loop from the tool-execution container bought Anthropic 60% faster time-to-first-token at P50 and >90% at P95, and at 1,000 tokens/sec the bottleneck moved from inference to network round-trips, pushing OpenAI to a persistent WebSocket. The live arguments are about how much scaffolding survives the next model release, whether compaction or fresh context is the right response to a full window, and whether a loop is ever allowed to close without a human in it.

## Consensus

### Multi-step control flow and workflow state belong in deterministic harness code; the model proposes actions, the runtime decides what happens next and where the process is.

Support: **6** talk(s)

> "the model never really um has to think. It proposes, but ultimately it is the harness that decides."
>
> — [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [4:04](https://www.youtube.com/watch?v=m24UKZomm7k&t=244s)

Supporting talks: [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)

### Every loop needs an explicit, engineered termination condition — an iteration cap, a numeric threshold, a stop_reason branch, or an eval gate — because the model's own report of completion is not a stopping condition.

Support: **7** talk(s)

> "you design loops for your agent so then they can autonomously work as many of these things in the background. Uh and then your job becomes designing these loops with a clear eval or termination gate."
>
> — [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [14:38](https://www.youtube.com/watch?v=pSto5YaNGUo&t=878s)

Supporting talks: [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)

### Whatever closes the loop must be structurally separate from whatever produced the work — a different model, a different methodology, or a different observation channel; an agent that acts and validates in the same loop provides no check.

Support: **5** talk(s)

> "But if the builder grades itself, you didn't remove the review, you hid it."
>
> — [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [19:17](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1157s)

Supporting talks: [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)

### Context must be actively budgeted per iteration rather than maximized; filling a large window degrades answer quality, not just cost, so tools, skills, and history are filtered, deferred, or summarized before each turn.

Support: **10** talk(s)

> "the more context you have in your in your context, the higher it is that you have contradicting information and it causes confusion for the model."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)

### The harness, not model capability, is now the limiting factor on agent performance — the same model swings tens of points depending on the loop around it.

Support: **8** talk(s)

> "So, scores range from 52.4% to 76.2%. So, more than a 20-point difference, and only the harness changed."
>
> — [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s)

Supporting talks: [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)

### Mutating and irreversible tool calls should be gated by the runtime — a deterministic interrupt, a policy check before credential issuance, or locked tool arguments — rather than by the model's judgment about whether an action is safe.

Support: **5** talk(s)

> "we deterministically interrupt the agent loop if there is a tool call approval required"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [10:28](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=628s)

Supporting talks: [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

## Disagreements

### When a long-running loop exhausts its context window, should it compact and continue the same session, or discard and re-allocate a fresh context each iteration?

| Position A | Position B |
|---|---|
| Compact and continue: use server-side auto-compaction in the form the model was trained on, or rolling summarization plus recall over the summary, so one session can run for hours without losing the thread. OpenAI names server-side compaction as one of three changes that made a persistent manager-agent workflow viable at all.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)* | Don't compact: compaction is a lossy operation that degrades fidelity, so deterministically re-allocate a fresh context for each iteration or unit of work — e.g. give each of 150 RPC migrations its own context window in a separate implementation phase, which is both cheaper and more reliable than batching.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)* |

*Why it matters: This determines whether a long task is one continuous session or many short bounded ones, which in turn dictates where durable state lives (conversation history vs. an external execution layer) and whether quality silently decays as a run gets longer.*

### Should the harness take control flow away from the model, or stay thin and defer to model judgment?

| Position A | Position B |
|---|---|
| Stay thin and design for tomorrow's model: harnesses encode assumptions about what the model cannot do, and those fixes become pure overhead — added latency and cache-invalidation bugs — the moment the limitation disappears. A carefully built harness can be irrelevant within a month, so keep it composed of small swappable primitives and let the model cook.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* | Take control away from the model: prompts are probabilistic suggestions, not constraints, so state transitions, rules, and stopping conditions belong in code. Doing this well is what let a team drop from Opus 4.7 to Haiku 4.5 at the same expected performance, and what makes a local open-source model reach proprietary-model performance.<br>*[Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)* |

*Why it matters: It decides where engineering effort goes: scaffolding that may be obsoleted by the next release, versus scaffolding that makes cheap or local models viable and caps your inference bill. It also sets your model-migration cost — a thick harness tuned to one model can take weeks to move.*

### Should in-loop verification be deterministic and static, or performed by other agents?

| Position A | Position B |
|---|---|
| Push verification toward deterministic checks: adding non-deterministic verification on top of non-deterministic output makes correctness worse. Use AST-grep sensors (language-agnostic and out-of-band from configs agents can disable with inline comments), types, ontology reasoners, and code-executed rules; never send an agent to do deterministic code's job.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)* | Use agent verifiers inside the loop: a separate verifier model, a rubric-based grader that keeps the agent retrying until success criteria are met, or an executor/validator/critic chain that catches fabricated tool-success confirmations a single agent reports as done. Calibrated LLM judges become the loop's termination gate.<br>*[What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)* |

*Why it matters: The verifier is what the stopping condition is made of, so its reliability bounds the whole loop's. It also decides cost shape: deterministic sensors are near-free per iteration, while grader agents multiply token spend on every retry — the panel's $10.42/hour loop economics assume one, not both.*

### Can an agentic loop close and ship without a human inside it?

| Position A | Position B |
|---|---|
| Yes, once the gate is good enough: if an optimized variant meets its target eval scores it can ship to production automatically, and a grader agent should keep the loop running until defined success criteria are hit. The human moves to the outer loop — setting direction, managing a small company of agents — rather than watching code get generated.<br>*[The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* | No: the loop must throttle on human attention. Cap it at one open PR at a time and never open a new one while the previous is unreviewed; surface one high-ROI finding rather than a rain of 80 PRs; require 80-90% trust before any autonomous automation; and accept that the only way to stop loops compounding slop is to read the output. Merging with no review at all — human or agentic — is not acceptable practice.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)* |

*Why it matters: This sets the throughput ceiling of the whole system — human review bandwidth becomes the hard limit if position B holds — and determines where liability lands, since a loop that closes autonomously still grounds out in a human or corporation that has to answer for what it shipped.*

## Practical Guidance

**Do:**

- Branch on stop_reason rather than consuming the model's first response, so a token-exhausted, truncated answer isn't silently accepted as complete
- Set an explicit max-iteration cap on every tool loop, and a domain-specific numeric threshold for breaking out (e.g. a fraud-score metric) where iteration count alone isn't meaningful
- Cap the available-skills/tool-description block at a fixed fraction of the context window (Codex uses 2%) and progressively truncate beyond it; mark rarely-used tools as deferred so they're reachable via tool search instead of preloaded
- Filter tools by semantic search to the top ~3 per query — this drops per-query tool context from thousands of tokens to under 300 and improves selection accuracy — and actively clear/re-add the registry each invocation in multi-turn conversations, since filtering alone doesn't bound growth
- Keep working context under ~100k tokens even with million-token windows; under 60k for the hardest problems
- Give each unit of work its own context window: run three-to-five migrations as separate implementation phases rather than batching 150 into one run
- Deterministically interrupt the loop for approval on mutating operations, and evaluate policy before minting the credential rather than issuing a broad one and restricting its use
- Request per-tool-call tokens that are audience-bound to a single MCP server, expire in minutes, and are never stored, instead of handing the loop a long-lived API key
- Constrain tool capability structurally — lock arguments via partial function application so the model can't change (or even see) the directory it operates in — to get safety without a human approval round-trip
- Separate the verifier from the author, usually meaning a different model (code with Claude, verify with Codex), and give the verifier real tools — browser harnesses, screenshots, hooks — to produce evidence
- Verify an action through a different channel than the one that performed it: if you clicked something, check the network or the screen, don't ask the click
- Feed the agent explicit state diffs after each action — what appeared, what was removed, whether the click landed — instead of leaving it to infer success
- Model 'done' as a structured object (artifact, scope, rubric, evidence, verifier, approver, residual risk, next action) rather than a boolean green checkmark
- Write concrete, verifiable goal prompts rather than essays, since the loop only terminates when the model can detect the goal was achieved
- Decouple the agent loop from the tool-execution container so first-token reasoning isn't blocked on container setup (60% faster TTFT at P50, >90% at P95)
- Keep durable run state outside the work — a three-hour run cannot hold state in memory or on disk — and treat the sandbox as ephemeral hands, not storage
- Only build a control loop for a task where you can measure the property, apply changes incrementally, and get feedback on the quality of each change; use AST-grep-style out-of-band sensors rather than lint/tsconfig that agents can disable with inline comments
- Cap the loop at one open PR at a time — never open a new one while the previous output is unreviewed
- Run loops on existing CI (GitHub Actions, GitLab, CircleCI) rather than standing up a dedicated cluster
- Use batch mode for non-urgent loop work: 50% fewer token costs with results inside 24 hours
- Route by difficulty across models, including a cheap model as the router, rather than paying frontier prices for every step in the loop

**Avoid:**

- Letting the model hold multi-step workflow state — it is terrible at remembering whether it's on step three of six, and asking it to is where step-skipping and looping failures come from
- Blind prompt-in-a-bash-loop setups on team or critical-systems work, even with verifier and code-review agents stacked on top — you still get 40,000-line PRs nobody reads
- Letting an agent act and validate in the same loop: it rationalizes tool errors into confident success responses that nobody surfaces
- Putting rules in the prompt and expecting them to constrain behavior — prompts are processed as probabilistic text; moving the same rule into a pre-tool-call hook flips the outcome from wrong to correct
- Using hooks for soft rules — they block unconditionally and force the user to retry; use runtime steering for soft rules and hooks only for hard constraints
- Filling a large context window because you have one; and letting subtask output dump into the primary thread, which crowds out the main context
- Passing a subagent the reasoning that produced a claim rather than just the claim and evidence — shared reasoning collapses multiple agents into groupthink
- Leaving interactive permission prompts enabled when running a coding agent in a CI pipeline
- Running in full-access mode on the theory that better models are safer — pushing a model toward high agency produces creative workarounds that diverge from intent (uploading a file to a share when it can't attach it to email)
- Keeping harness workarounds written for a model limitation after the limitation is gone — they become pure overhead, adding latency and causing incorrect cache discards
- Using the sandbox for durability, snapshots, or state; sandboxes are ephemeral and stateless by design
- Storing secrets as files in the agent's environment — the single most effective concrete step is simply not having them there
- Auto-opening large volumes of PRs from a loop; nobody wants to wake up to a rain of 80 pull requests, however small
- Merging PRs with no review at all, human or agentic (up 31% year over year, alongside a 242% rise in incidents per PR)
- Re-sending large tool results and full conversation history on every iteration — store results out of context and summarize, and summarize what a sliding window drops rather than losing the start of the conversation
- Giving one agent a large tool inventory instead of one or two tools and a single job

## Notable Outliers

- Running a coding agent in a loop works out to roughly $10.42 per hour — but stacking loops on loops and buying quality with more tokens is economically unsustainable at company scale, where you have to ask whether an engineer's token budget is $10k, $100k, or $1M a month. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [20:42](https://www.youtube.com/watch?v=c35YoMdnI78&t=1242s))
- Loops are not a new idea: Böhm and Jacopini proved in 1966 that sequence, conditionals, and loops are all you need for Turing completeness — the agentic loop is that result applied to a probabilistic next-word predictor that can't execute anything itself. ([Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [6:43](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=403s))
- An on-device game agent's entire perceive-plan-act cycle must fit inside a 16 ms frame at 60 Hz or the player sees jank, and the loop must be tuned for minimum energy or it drains the battery — a hard real-time constraint absent from every server-side agent design. ([Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md), [8:44](https://www.youtube.com/watch?v=418t26CVz-w&t=524s))
- At 1,000 tokens/sec inference, the bottleneck stops being inference and becomes the network: a stateful WebSocket that transmits only changed items materially outperforms server-sent events over HTTP for agent loops. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s))
- reCAPTCHA v2 cannot be beaten by any architecture that round-trips a model on every interaction, because challenge rounds expire on a clock — the only reliable approach is deterministic code driving at machine speed with exactly one AI vision call per round. ([The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [18:36](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1116s))
- The harness should be the output of the engineering process rather than its input: agent identity, roles, and governance should emerge from position relative to other agents and environmental pressure, with the rate of coupling between agents as the engineer's primary control lever. ([Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md), [21:12](https://www.youtube.com/watch?v=qdZzND79mcg&t=1272s))

## All Talks

- [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Beyond the Harness: A Journey Towards Adaptative Engineering](../talks/beyond-the-harness-a-journey-towards-adaptative-engineering.md)
- [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md)
- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Don't Let the LLM Drive](../talks/dont-let-the-llm-drive.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)
- [Guide, Verify, Solve](../talks/guide-verify-solve.md)
- [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)
- [Learned Execution Graphs for Anomaly Detection & Drift in APIs](../talks/learned-execution-graphs-for-anomaly-detection-drift-in-apis.md)
- [Let's integrate AI Agents in Event-Sourced Systems](../talks/lets-integrate-ai-agents-in-event-sourced-systems.md)
- [Local Agentic Theory For Mobile Games](../talks/local-agentic-theory-for-mobile-games.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [Perception Agents](../talks/perception-agents.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- [Skills are new features: Building Skill-Centric Harness](../talks/skills-are-new-features-building-skill-centric-harness.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- [The Agentic AI Engineer](../talks/the-agentic-ai-engineer.md)
- [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)
- ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)
- [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)
- [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)
- [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [Why Agentic Systems Need Ontologies](../talks/why-agentic-systems-need-ontologies.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)
- [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

## Speakers

- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Alex Volkov](../speakers/alex-volkov.md)
- [Alexander Embiricos](../speakers/alexander-embiricos.md)
- [Anirban Chatterjee](../speakers/anirban-chatterjee.md)
- [Antje Barth](../speakers/antje-barth.md)
- [Bennet Fenner](../speakers/bennet-fenner.md)
- [Corey Gallon](../speakers/corey-gallon.md)
- [Dan Farrelly](../speakers/dan-farrelly.md)
- [Dat Ngo](../speakers/dat-ngo.md)
- [Divakar Kumar](../speakers/divakar-kumar.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Dotta](../speakers/dotta.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Joanne Song](../speakers/joanne-song.md)
- [Joel Allou](../speakers/joel-allou.md)
- [Kim Maida](../speakers/kim-maida.md)
- [Kushan Raj](../speakers/kushan-raj.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [May Walter](../speakers/may-walter.md)
- [Ornella Bahidika](../speakers/ornella-bahidika.md)
- [Rajiv Chandegra](../speakers/rajiv-chandegra.md)
- [Ritvik Pandya](../speakers/ritvik-pandya.md)
- [Roberto Stagi](../speakers/roberto-stagi.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Shafik Quoraishee](../speakers/shafik-quoraishee.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)
- [Yogendra Miraje](../speakers/yogendra-miraje.md)

