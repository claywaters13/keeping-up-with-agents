---
title: "background agents"
type: "concept"
slug: "background-agents"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 12
---

# background agents

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **12** speaker(s)

**Definition:** Agents that run detached from a live session — scheduled, event-triggered, or long-lived — and notify rather than being watched.

*Also referred to as: asynchronous agents, long-running background agents, cron-scheduled agents, scheduled agent automations, event-triggered agents, proactive agents, background agent automation*

## State of Practice

The conference treated background agents as an infrastructure problem, not a model problem. The converged architecture is: a stateless harness talking to an append-only session log, with ephemeral cloud sandboxes as disposable 'hands,' credentials held in a vault or broker that never enters the sandbox, and verification run in a context window separate from the one that did the work. Speakers repeatedly located the binding constraint not in model capability — METR horizons of 12+ hours, Opus 4.5-class models already trivially closing typical Jira tickets — but in per-environment context: production topology, user-specific conventions, org knowledge that a generic agent cannot infer and that must be precomputed offline rather than assembled at query time. Operationally the field has learned that a ~200-tool-call run will fail at least once, that a sandbox used for durability is an anti-pattern, and that an unbounded automation is a denial-of-service on its owner, so output must be capped and producing nothing must be a legal outcome. What remains genuinely open is how much scaffolding the agent still needs (self-orchestrating models vs. a hand-built execution layer), which surface background work should be reachable from, and whether anyone can actually run these things unattended overnight — Yegge's answer was that very few can.

## Consensus

### Verification must run in a context separate from the one that produced the work; self-grading in-context confabulates, and concerns like security and correctness must be split into distinct passes.

Support: **5** talk(s)

> "what we found is it's quite effective to separate verification into a separate context window. This is a very general trend."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [6:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=404s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)

### Background agents belong in isolated cloud sandboxes with least-privilege access, and secrets must live outside the sandbox behind a vault or broker rather than on the developer's laptop or inside the agent's environment.

Support: **5** talk(s)

> "Never trust agents with secrets. If an agent can know a secret, that secret, you need to treat it as if it's already been compromised."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [11:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=719s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)

### Session state must be durable and external to the compute doing the work, so that a dead sandbox, dead harness, or closed laptop does not destroy a multi-hour run.

Support: **3** talk(s)

> "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)

### Model capability is no longer the limiting factor for background agents; the constraint is captured, environment-specific context — production topology, per-user history, codebase idiosyncrasy — that a generic agent cannot infer.

Support: **5** talk(s)

> "You need the execution engine, that's great, but you really need that production context that tells you is this important or not important."
>
> — [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [10:48](https://www.youtube.com/watch?v=vSx5IULvBns&t=648s)

Supporting talks: [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)

### Detached agents need explicit interruption and notification discipline: bounded output, permission to return nothing, and a defined trigger for escalating to a human (an assumption about to be made, or an irreversible action).

Support: **3** talk(s)

> "in a world where I have lots of automations, the last thing I want is noise. I don't want the agents denial of servicing me."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [8:21](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=501s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)

### Background agents should be multiplayer and org-scoped — the same session reachable from wherever the team already works — rather than a single developer's private, laptop-bound process.

Support: **4** talk(s)

> "So, what we really wanted was to be able to work with the same session from every relevant interface."
>
> — [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [3:28](https://www.youtube.com/watch?v=OL7kfezynJM&t=208s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

### Synchronous chat is structurally wrong for delegated work, because it pins the user to the interface while the agent runs; the value of background agents is precisely that the human leaves.

Support: **4** talk(s)

> "This synchronous medium does not allow the customers to leave the platform and go and do their work."
>
> — [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [1:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=111s)

Supporting talks: [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)

## Disagreements

### Do background agents still require a hand-built orchestration and execution layer, or do current models self-orchestrate well enough that the scaffolding is dead weight?

| Position A | Position B |
|---|---|
| Frontier models now spawn sub-agents, split work, and verify it if you simply ask them to — no custom tooling, no 'software factory,' no orchestration framework needed.<br>*[Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* | You must design the execution layer yourself: durable state, retries, queues, backoff, scheduling, full-stack tracing, plus adversarial supervisor agents and a per-environment knowledge system, because no single agent run is trustworthy and off-the-shelf frameworks were not built for this shape.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)* |

*Why it matters: It decides whether a team's engineering investment goes into prompts and ambition or into months of execution-layer infrastructure — and whether that infrastructure is durable capital or scaffolding the next model release deletes.*

### Are background agents ready to run unattended, or does every artifact still need a human in the loop?

| Position A | Position B |
|---|---|
| Unattended overnight automation is the main event and already shipping — agents that triage issues, walk stack traces, and close tickets while you sleep will be a bigger category than interactive AI.<br>*[Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* | Fully unsupervised operation is still a frontier very few can do reliably; in practice every agent-generated PR gets human review, the agent pauses whenever it would make an assumption, and irreversible actions require plan approval first.<br>*[Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)* |

*Why it matters: The answer sets whether human review capacity is the real throughput ceiling on agent-generated work, and whether 'agent count' or 'reviewer count' is the number to plan headcount around.*

### Should guardrails for background agents be expressed to the agent, or enforced deterministically outside it?

| Position A | Position B |
|---|---|
| Rules in AGENTS.md plus auto-review are sufficient safety controls for individual use, with admin settings reserved for externally-facing actions; models today err toward being too reluctant to act destructively, so over-restriction is the bigger practical cost.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* | Guardrails stated as prompts are not guardrails — a third party can prompt-inject past them — so enforcement must be deterministic configuration outside the agent, backed by real credential isolation, since sandbox and auto-approval configs are not reliably safe and there is no technical defense for prompt injection today.<br>*[Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)* |

*Why it matters: Prompt-level rules are cheap and immediate; deterministic enforcement requires a broker, a permission model, and org infrastructure. Choosing wrong means either shipping agents with no real containment or blocking every useful action behind approvals.*

### How should a long-lived agent carry context — compaction inside one persistent thread, or an external append-only substrate?

| Position A | Position B |
|---|---|
| Compaction now works well enough that the old advice to start fresh threads is obsolete; keep one long-lived pinned thread (five weeks old, hundreds of sub-agents), schedule heartbeats back into it, and prefer visible pinned threads over sub-agents so you notice state changes.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* | Compaction is destructive — it discards everything not compacted — so the session should be an immutable append-only event log the model can always read back from, with state held outside the running work rather than rehydrated from logs or manual checkpoints.<br>*[Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)* |

*Why it matters: It determines whether long-horizon reliability comes free from the harness vendor or requires building session storage, and whether a run that goes wrong at hour six can be inspected and resumed or is simply lost.*

### Is Slack the right surface for background agents to live in?

| Position A | Position B |
|---|---|
| Meet people where they already work — agents should be embedded in Slack and MS Teams rather than a separate product UI, and Slack's extensible bot-shaped API is exactly why it won as an agent platform even though the product itself is weak.<br>*[Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* | Slack was designed for the average office worker, not for building software; a Slack bot alone just moves the agent from trapped on a laptop to trapped in Slack, so the agent session must be reachable identically from the IDE, the repo host, and mobile, and collaboration surfaces should carry only the facts that are not in the code.<br>*[Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* |

*Why it matters: Surface choice determines who can trigger agent work — a chat-first design lets non-engineers file real changes, while a repo-first design keeps the artifact and its review in one place at the cost of reach.*

## Practical Guidance

**Do:**

- Split the harness from the sandbox: keep the harness a stateless process against an append-only session log, with containers as disposable hands, so a sandbox death does not lose the run.
- Keep credentials in a separate vault or broker and never inject them into the agent's sandbox; treat any secret the agent can see as already compromised.
- Run verification as its own pass in its own context window, and split concerns across passes — security first and last, never bundled with correctness in one prompt.
- Budget four to five review passes over an LLM's own work before shipping it, and stack multiple independent scanners so they check each other.
- Bound every automation's output (e.g. at most one PR) and explicitly allow it to produce nothing at all.
- Pause and ask whenever the agent is about to make an assumption, and require an approved plan before irreversible or dangerous actions.
- Benchmark candidate agents and models continuously on your own repository — SWE-bench is all Python, and Rails results diverged sharply on both speed and cost.
- Instrument the execution layer as the observability hub and score on outcome signals (was the PR opened, was the report saved) rather than thumbs up/down.
- Design for at least one failure per run: a background agent making ~200 tool calls will almost certainly hit one.
- Add an out-of-band memory consolidation pass to correct memories that were written incorrectly or only locally-optimally in-band.
- Pick background-agent targets that take the user more than a couple of hours and are repeatable, then capture the last 20% of user-specific convention automatically from observed usage.
- Track weekly active sessions rising while weekly active users falls — WAU is the wrong success metric for a delegation product.
- Use low or medium reasoning effort for routine operational tasks; highest effort does not pay off proportionally.

**Avoid:**

- Putting the harness and the sandbox in the same container — one container death takes the whole session with it.
- Using the sandbox for durability, snapshots, or state; sandboxes are ephemeral and stateless by design.
- Prompting your guardrails at the agent — a third party can prompt-inject straight past them.
- Grading work in the same context window that produced it; it produces confabulation and odd artifacts.
- Prescribing a memory schema for the model; explicitly specifying what kinds of memories to save measurably drops performance.
- Building a separate user-facing interface for authoring skills — users will not use it.
- Treating citations as a trust mechanism; they push verification burden back onto the user. Show the trace of how each value was produced instead.
- Assuming CI/CD covers your risk surface — feature flags and infra changes routinely bypass it and get no monitoring at all.
- Shipping an async experience when your task horizon is under an hour; the agent errors out and returns too fast for async to be good UX.
- Letting a single agent own queue management or long-horizon supervision unchecked — any one agent eventually fails.
- Coupling the execution layer to models, prompts, and context; the shortest-lived layer will force rewrites of everything it touches.

## Notable Outliers

- Queue-processing agent systems need adversarial groups of supervisor agents, not a single supervisor, because one agent will always eventually screw it up. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [19:21](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1161s))
- Snyk found 241 vulnerabilities in a codebase that a frontier model had already completed a dedicated security hardening pass over. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [7:46](https://www.youtube.com/watch?v=yWS0udrIOc8&t=466s))
- An entire PR-triage-and-review service collapsed into a single markdown file piped to a coding agent. ([Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [11:24](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=684s))
- A background agent told to poll a support queue every five minutes, escalating to every minute under five-minute wait times, recovered a $400 refund unattended while its owner showered. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [1:13:02](https://www.youtube.com/watch?v=il1c1a2FufU&t=4382s))
- Per-user context should be computed by two offline engines on different time windows — a slow one that learns durable patterns and a fast one that computes live urgency — mirroring complementary learning systems in neuroscience and lambda architecture in data infrastructure. ([From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [10:29](https://www.youtube.com/watch?v=Btk8wDUVs74&t=629s))
- Longitudinal study of ~100 developers over thousands of hours: hands-on-keyboard typing is only about 5% of the job, which is the share AI has addressed so far. ([Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [19:56](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=1196s))
- A determined agent blocked at a connector will open a browser and perform the action through computer use instead, routing around the block entirely. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [54:37](https://www.youtube.com/watch?v=il1c1a2FufU&t=3277s))

## All Talks

- [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)
- [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)

## Speakers

- [Arjun Singh](../speakers/arjun-singh.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Benjamin Guo](../speakers/benjamin-guo.md)
- [Dan Farrelly](../speakers/dan-farrelly.md)
- [Idan Gazit](../speakers/idan-gazit.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Justin Smith](../speakers/justin-smith.md)
- [Lance Martin](../speakers/lance-martin.md)
- [Omri Bruchim](../speakers/omri-bruchim.md)
- [Rob Cheung](../speakers/rob-cheung.md)
- [Steve Yegge](../speakers/steve-yegge.md)
- [Ted Johnson](../speakers/ted-johnson.md)

