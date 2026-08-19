---
title: "background agents"
type: "concept"
slug: "background-agents"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 13
---

# background agents

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **13** speaker(s)

**Definition:** Agents that run detached from a live session — scheduled, event-triggered, or long-lived — and notify rather than being watched.

*Also referred to as: asynchronous agents, long-running background agents, cron-scheduled agents, scheduled agent automations, event-triggered agents, proactive agents, background agent automation*

## State of Practice

Background agents crossed from demo to production architecture at this conference, and the architectural pattern is now fairly specific: the work runs in cloud micro-VMs or sandboxes rather than on a developer's laptop, the harness is a stateless process against an append-only session log so a dead container doesn't kill the run, credentials live in a vault or broker outside the sandbox, and verification happens in a context window separate from the one that did the work. Speakers repeatedly located the remaining bottleneck not in model capability but in environment-specific context — Resolve AI, monday.com, and Filed all argued that a frontier model with no precomputed understanding of your services, your user, or your conventions gets 80–90% of the way and stalls. Failure is assumed rather than hoped against: Inngest put the number at roughly one failure per ~200 tool calls, which is why durable external state, retries, and full-stack traces (not just LLM/tool spans) are treated as table stakes. Async only became a sensible UX once METR task horizons passed about an hour, and Anthropic argued the frontier gap in long-horizon products now comes from combined architecture, infrastructure, security, and memory investment rather than the model alone. What remains genuinely unsettled is the human surface: whether Slack is the right home for these agents, whether guardrails can live in prompts or must be deterministic configuration outside the agent, and whether every artifact needs a human reviewer or only the exceptions do.

## Consensus

### Background agents should run in cloud sandboxes detached from the developer's machine, so closing the laptop doesn't stop the work.

Support: **5** talk(s)

> "none of this is running on my machine. It's all micro VMs in the cloud. So, every session is just a branch of my repo checked out to a spot in the cloud."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [14:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=899s)

Supporting talks: [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)

### Credentials and secrets must be held outside the agent's sandbox and reached through a vault or broker, not mounted into the environment the agent runs in.

Support: **4** talk(s)

> "Never trust agents with secrets. If an agent can know a secret, that secret, you need to treat it as if it's already been compromised."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [11:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=719s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)

### Verification must be a separate pass in a separate context from the one that produced the work; self-grading in the working context produces confabulation and half-done reviews.

Support: **5** talk(s)

> "what we found is it's quite effective to separate verification into a separate context window. This is a very general trend."
>
> — [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [6:44](https://www.youtube.com/watch?v=9QebvrrY3KY&t=404s)

Supporting talks: [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)

### Model capability is no longer the binding constraint on background agents; capturing environment- and user-specific context ahead of time is.

Support: **4** talk(s)

> "the most capable agent in the world whether it's like a cloud and Gemini, it doesn't understand you. He need to process it beforehand."
>
> — [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [14:55](https://www.youtube.com/watch?v=Btk8wDUVs74&t=895s)

Supporting talks: [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)

### State for a long-running run must live outside the process and outside the sandbox, because failure over hundreds of tool calls is a certainty rather than an edge case.

Support: **3** talk(s)

> "So, for this this to work, a 3-hour run cannot hold state in memory or in disk. The state must live outside of the work."
>
> — [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [6:41](https://www.youtube.com/watch?v=X1kp-ABIIxQ&t=401s)

Supporting talks: [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)

### Synchronous chat is the wrong default surface for agent work, because it pins the human in place while the agent runs instead of letting them leave and be notified.

Support: **5** talk(s)

> "This synchronous medium does not allow the customers to leave the platform and go and do their work."
>
> — [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [1:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=111s)

Supporting talks: [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)

## Disagreements

### Is Slack (and chat surfaces generally) the right home for background agents, or a trap they need to be moved out of?

| Position A | Position B |
|---|---|
| Meet people where they already work: embed the agent in Slack/Teams/GitHub rather than a separate product UI, and treat Slack's extensible bot shape as the reason it wins as an agent platform.<br>*[Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)* | Slack is the wrong surface — it was designed for the average office worker, not software teams, and a Slack bot merely moves the agent from being trapped on a laptop to being trapped in Slack; the same session must be reachable from every interface, or creation and collaboration must converge on a purpose-built surface.<br>*[Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* |

*Why it matters: It determines whether you invest in chat integrations or in a session abstraction portable across interfaces, and whether org context reaches the agent through conversation history or through a dedicated context layer.*

### Do background agents require a purpose-built execution and orchestration layer, or will model capability absorb that work?

| Position A | Position B |
|---|---|
| You must design the execution layer yourself — durable state, retries, scheduling, full-stack traces, per-customer knowledge systems — because frameworks from three months ago were not built for loops and background agents, and the frontier gap comes from architecture, infrastructure, security, and memory together.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* | Current models self-orchestrate: tell the model to spawn sub-models, split work, and verify, and it will, with no custom tooling or 'software factory' — a service that used to triage and review PRs is now a markdown file, and scheduled heartbeats into an existing thread replace bespoke automation plumbing.<br>*[Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* |

*Why it matters: One path spends months of engineering on a layer meant to outlive models; the other spends nothing and rewrites the markdown when the model changes. Betting wrong means either building infrastructure the model made obsolete or discovering at 200 tool calls that nothing survives a failure.*

### Should every background-agent output be human-reviewed, or should humans be invoked only on exceptions?

| Position A | Position B |
|---|---|
| Gate the artifacts: 99.9% agent-generated PRs still get human review, irreversible actions require presenting a plan for approval, agents pause whenever they are about to make an assumption, and adversarial supervisor agents watch queues because any single agent eventually fails.<br>*[Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)* | Interruption is the scarce resource: automations must be allowed to produce no output at all and be output-bounded so they don't deny-service their owner, agents should invoke humans only when they need clarification or a pair of hands, and AGENTS.md rules plus auto-review are sufficient controls for individual use since models are already more reluctant than eager about destructive actions.<br>*[Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* |

*Why it matters: Mandatory review caps the throughput of background agents at human review bandwidth, which is the whole point of running them detached; exception-based review scales but pushes the failure mode from noise to unreviewed merged changes.*

### Can guardrails for detached agents be expressed to the agent, or must they be deterministic configuration outside it?

| Position A | Position B |
|---|---|
| Guardrails written as prompts are not guardrails — a third party can prompt-inject past them, so constraints must be deterministic config outside the agent, backed by least-privilege sandboxes, in-house permission and monitoring systems, and deterministic scanners run as separate passes.<br>*[Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)* | AGENTS.md rules plus automatic review are adequate safety controls for individual use, with org-level admin settings reserved for externally-facing actions.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)* |

*Why it matters: If instruction-level rules are insufficient, every team running background agents needs a permission broker and sandbox policy before deployment rather than after — and Jason Liu's own observation that a determined agent will route around a blocked connector using computer use is evidence for the harder position.*

## Practical Guidance

**Do:**

- Split the harness from the sandbox: run a stateless harness against an append-only session event log, with containers as disposable 'hands' so a sandbox or harness death doesn't lose the run
- Keep credentials in a separate vault and access them through a broker; never add them to the agent's sandbox container
- Run verification in a separate, separately tuned context window from the one that produced the work
- Run security as its own pass — first and last — rather than bundling it with correctness in one prompt
- Bound automation output (e.g. at most one PR) and explicitly permit automations to produce no output at all
- Pick background-agent tasks that currently take a user more than a couple of hours and that repeat
- Present a plan for approval before irreversible or dangerous actions; pause whenever the agent is about to make an assumption
- Precompute per-user and per-environment context offline — monday.com's split of a slow engine that learns the user and a fast engine that reads live urgency signals
- Schedule heartbeat messages back into the same long-lived thread rather than spawning a new thread per automation run
- Write an enrichment timestamp into each processed artifact so repeat agent passes only touch what lacks the marker
- Give the agent a fixed reference list of tags and instruct it to be reluctant to add new ones
- Benchmark candidate agents on your own repo continuously — SWE-bench is all Python and won't predict Ruby on Rails results
- Score on outcome signals (was the PR opened, was the report saved) rather than thumbs up/down
- Expose the full session trace — triggers, database errors, permission failures, performance — and make it inspectable by reviewer agents, not just humans
- Default to low/medium reasoning effort for operational background tasks
- Capture user-specific conventions automatically from observed product usage, since the generic agent only reaches 80–90%

**Avoid:**

- Putting the harness and the sandbox in the same container
- Using the sandbox for durability, snapshots, or state — it is ephemeral by design
- Holding a multi-hour run's state in memory or on disk, or rehydrating it from logs with manual checkpointing
- Prompting guardrails at the agent and treating that as a control
- Letting the same context both do the work and grade it
- Scheduling automations on local tooling that requires your laptop to be open when the timer fires
- Prescribing a memory schema for the model instead of letting it structure and maintain its own
- Shipping an async experience when the model's task horizon is well under an hour — it errors out and returns too fast for async to be good UX
- Assuming CI/CD covers the change surface: feature flags and infra changes frequently bypass it and get no monitoring at all
- Building a separate skill-creation interface for users to author skills in
- Measuring agentic product success by weekly active users
- Trusting a single agent to manage a work queue without adversarial supervision
- Assuming a security scanner's 'proprietary vulnerability' claims hold on your codebase — Snyk's findings were all already public CVEs

## Notable Outliers

- Running agents fully unsupervised overnight is the actual next frontier, and very few practitioners can do it reliably today. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [18:06](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1086s))
- Queue-processing agent systems need adversarial groups of supervisor agents, because any single agent will eventually screw it up. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [19:21](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1161s))
- For agentic products, the target is weekly active users going down while weekly active sessions go up — WAU is the wrong metric. ([Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [13:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=816s))
- A background service that triaged, AI-reviewed, and prioritized all his PRs is now just a markdown file piped to Codex or Claude. ([Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [11:24](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=684s))
- A background agent instructed to poll a support queue every five minutes, then every minute under five-minute wait, recovered $400 while he took a shower. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [1:13:02](https://www.youtube.com/watch?v=il1c1a2FufU&t=4382s))
- In-band memory writing is not enough — an offline 'dreaming' consolidation pass is required, and 5/5 replicates with a raw memory store fell into a trap that dreaming corrected. ([Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [14:14](https://www.youtube.com/watch?v=9QebvrrY3KY&t=854s))
- Precomputed-context background agents structurally cannot serve new users, because there is no reliable historical data to reason from — an admitted cold-start failure. ([From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md), [12:57](https://www.youtube.com/watch?v=Btk8wDUVs74&t=777s))
- Skills connected to live systems like Slack cannot be evaluated with standard eval methods, because live state can't be snapshotted. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [24:30](https://www.youtube.com/watch?v=il1c1a2FufU&t=1470s))

## All Talks

- [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)
- [Always-on agents run production without the on-call tax](../talks/always-on-agents-run-production-without-the-on-call-tax.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)
- [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)
- [From Systems of Record to Systems of Context](../talks/from-systems-of-record-to-systems-of-context.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [LLM Knowledge Bases: a practical guide](../talks/llm-knowledge-bases-a-practical-guide.md)
- [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)

## Speakers

- [Arjun Singh](../speakers/arjun-singh.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Ben Holmes](../speakers/ben-holmes.md)
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

