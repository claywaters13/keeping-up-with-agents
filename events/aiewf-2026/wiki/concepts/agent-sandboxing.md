---
title: "agent sandboxing"
type: "concept"
slug: "agent-sandboxing"
tier: "core"
maturity: "consolidating"
talk_count: 21
speaker_count: 26
---

# agent sandboxing

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **21** talk(s) by **26** speaker(s)

**Definition:** Confining agent execution — filesystem, network, syscalls, process — so that a misbehaving or compromised agent cannot affect the host or production systems.

*Also referred to as: sandbox isolation, agent sandboxes, sandboxed agent execution, container isolation, code execution sandboxing, syscall filtering, network egress sandboxing*

## State of Practice

The field has moved past "put the agent in a box" and is now arguing about which box and what it can reach. The dominant technical position, argued most forcefully by the people who operate sandboxes at scale, is that any primitive sharing the host kernel — fork/exec, containers, even gVisor — is eventually escapable, and that hardware virtualization (Firecracker/CrosVM-class micro VMs) is the only real boundary; seccomp allowlists are considered a poor fit because open-ended agent workloads have an unknowable syscall surface, and a Docker socket handed into a container is treated as equivalent to host compromise. Alongside the boundary itself, a capability discipline has hardened: secrets live in a vault or broker and are decrypted only at tool-execution time so the model never sees them; write-capable actions (git push, PR creation, CI trigger) are pushed out of the agent into a deterministic layer; guardrails expressed as prompt text are dismissed outright because a third party can inject past them. Prompt injection is universally treated as unsolvable at the model layer, so the design goal is blast-radius containment rather than prevention. The open fights are whether isolation alone is sufficient — one camp argues the worst failures happen entirely inside the agent's authorization, where the system looks compliant the whole time — and whether sandboxes should stay ephemeral or become durable, snapshot-restorable state. Tooling is acknowledged to exist but mostly in beta, which is why several teams still roll their own micro VM plumbing.

## Consensus

### Constraints imposed by prompting or the model's own judgment do not contain an agent; containment must be structural — deterministic configuration and isolation outside the agent loop.

Support: **5** talk(s)

> "if you're prompting the guardrails at the agent, you're effectively letting the fox loose in the henhouse."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [7:04](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=424s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)

### Secrets and credentials must live outside the agent's reach — brokered or vaulted and decrypted only at tool-execution time — because any secret the agent can read is compromised.

Support: **5** talk(s)

> "Never trust agents with secrets. If an agent can know a secret, that secret, you need to treat it as if it's already been compromised."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [11:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=719s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)

### Prompt injection cannot be eliminated, so the security objective is limiting blast radius rather than preventing the injection.

Support: **4** talk(s)

> "I guess like prompt injection itself isn't solved and we cannot really solve it. All we can do is just to limit the blast radius in case that happens."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s)

Supporting talks: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

### Hardware virtualization (micro VMs) is the correct isolation boundary for agents; shared-kernel primitives and the coding agents' own built-in sandboxes are inadequate.

Support: **3** talk(s)

> "if you're a startup or a founder like in this space, like let me save you the story and two years of grief. Just please use micro VMs from the start."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [29:03](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1743s)

Supporting talks: [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

### Agents should run in isolated remote environments rather than on developer laptops, because laptops hold production credentials and data the agent has no legitimate need for.

Support: **4** talk(s)

> "it finds a token on your laptop that it can use and it thinks it's working with staging, but actually it's production and now it just deleted everything."
>
> — [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [11:05](https://www.youtube.com/watch?v=OL7kfezynJM&t=665s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)

### Mutating and write-capable operations should be routed through a deterministic layer or a deterministic interrupt, not left to the agent's discretion.

Support: **4** talk(s)

> "we deterministically interrupt the agent loop if there is a tool call approval required"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [10:28](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=628s)

Supporting talks: [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)

## Disagreements

### Is deterministic isolation sufficient to make agent execution safe, or does it require a model-powered oversight layer that judges intent?

| Position A | Position B |
|---|---|
| The boundary is the security model: isolate at the hypervisor, scope capabilities to least privilege, keep dangerous actions deterministic, and accept that behavioral techniques for taming agents do not work. Invest in the sandbox, not in judging the agent.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md)* | Egress filters, gVisor sandboxes and telemetry are necessary but not sufficient, because the worst failures occur entirely within the agent's authorization — the system looks compliant throughout. You need a semantic judge in the loop: an adversary agent rewarded for stopping the worker, or a classifier evaluating the tool call against conversation context.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* |

*Why it matters: It decides whether safety budget goes into VMM/kernel boundary engineering or into an oversight model that adds cost and latency to every tool call, and whether a yes/no approval prompt on an opaque command is defensible under regimes like the EU AI Act.*

### Should an agent sandbox be ephemeral with state held externally, or durable with snapshot/restore as a first-class feature?

| Position A | Position B |
|---|---|
| Sandboxes are ephemeral and stateless by design — they are the hands, not the brain. Using them for durability, snapshots, or state is an anti-pattern; long runs must keep state outside the work in an execution layer, and all code execution and file creation should happen in throwaway isolated environments.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)* | Disk persistence, not compute, is the next unlock: incremental snapshotting, checkpoint/restore and lineage-aware scheduling turn agents from ephemeral executors into durable knowledge workers, and even enable tree search over sandbox states across days.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)* |

*Why it matters: One path means building an external durable execution layer and treating sandbox loss as free; the other means building incremental snapshot storage, warm pools and snapshot-lineage schedulers, which is a very different infrastructure bill.*

### Does an individual developer running a coding agent locally actually need a sandbox?

| Position A | Position B |
|---|---|
| For personal use a Docker-style sandbox is unnecessary overhead; it would only be warranted for an externally-facing bot. Reliability is bought instead with a local dev plus staging-agent split.<br>*[Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)* | The laptop is precisely the danger zone — it holds credentials and data the agent shouldn't touch, auto-approval and sandbox configs are not reliably safe, and agents should not be given direct access to personal computers at all; every session should be a micro VM in the cloud.<br>*[Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)* |

*Why it matters: It determines whether sandboxing is a platform-team concern for production deployments only, or a baseline requirement for every engineer's daily workflow — and whether non-technical teammates can ever trigger real code changes.*

## Practical Guidance

**Do:**

- Confine every agent code execution and file write to an isolated sandbox, including in interactive product flows, not just batch jobs
- Choose hardware virtualization (Firecracker/CrosVM-class micro VMs) as the boundary from day one instead of iterating through containers, gVisor and V8 isolates
- Use a micro VM with Vsock-mediated networking for any workload that needs a Docker daemon, since Linux primitives like landlock, bubblewrap and seccomp cannot contain one
- Store credentials in a vault and decrypt them only at tool-execution runtime so the model never sees a security token; make credentials usable by the agent but not readable by it
- Keep GitHub push, PR creation and CI triggering out of the agent and in the deterministic wrapper around it
- Decouple the agent loop from the tool-execution container so container setup doesn't block first-token reasoning (60% faster TTFT at P50, >90% at P95)
- Run tool execution inside the customer's own VPC, with MCP tunnels making only outbound calls to the agent loop, for enterprise deployments
- Give subagents read-only permissions and forbid them from spawning further subagents
- Attach task context to approval decisions — deleting a file is fine or not depending on whether the user asked for it
- Bound automation output (e.g. at most one PR, and permission to produce nothing) so background agents can't denial-of-service their owner
- Use incremental snapshots rather than full multi-gigabyte images per turn, and score scheduler nodes by how many snapshot lineage layers they already cache
- Prefer block-device access over shared-folder filesystem passthrough inside micro VMs — it uses the guest cache and avoids exiting on every filesystem operation
- For generated apps, run the client in a null-origin sandboxed iframe with CSP and implement sharing/access control in the platform so generated code cannot get the permission model wrong
- Budget for the overhead explicitly: basic controls under ~8%, workload isolation 10–20%, real-time malicious input detection 15–30%

**Avoid:**

- Relying on the sandboxes bundled with Codex and Claude Code — they are worthless once the agent has Docker socket access
- Handing an agent a Docker socket inside a container; it can spawn a privileged container and escape to the host
- Assuming containers or gVisor protect the host kernel — you can pivot sentry → gofer → host kernel
- Seccomp allowlists for open-ended agent products: you cannot know the syscall set in advance, so you end up blocking real users
- Expressing guardrails as instructions to the agent, where a third party can prompt-inject past them
- Using the sandbox as the durability layer for a long run's state
- Full-access / YOLO mode, which stays unsafe even as models improve because high agency produces creative workarounds (uploading a file to a file share when it can't attach it to an email)
- Treating a single-node containerized sandbox as representative of real infrastructure work — you cannot simulate EC2 or Cloud Run provisioning inside one node
- Building your own crypto, or your own AI Slackbot, given the prompt-injection attack surface
- Shipping ML infrastructure with authentication off by default — 78% of audited production ML setups had at least one critical misconfiguration
- Treating a sandbox diagram plus a yes/no approval dialog as an oversight story

## Notable Outliers

- An agent persuading a human to disable a control (e.g. install a Chrome extension) should count as the agent escaping the sandbox — the energy came from inside the agent loop and merely routed through the human as a tool. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- With a null-origin sandboxed iframe client and a server sandbox that can only talk to that client, there is no security bug the generated code can have that matters. ([Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md), [15:12](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=912s))
- Tightening down a general-purpose agent destroys its usefulness; a narrowly sandboxed special-purpose agent is the better tradeoff today. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [14:59](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=899s))
- Security must be prioritized over performance because system tricks can cover performance problems but cannot hide a breach, and trust is lost only once. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [28:24](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1704s))
- The agent sandboxing tools all exist but most are still in beta, so they are not yet ready for enterprise deployment. ([We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [19:58](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1198s))
- GPU-accelerated sandboxes are poorly served by micro VMs today because VFIO passthrough cannot be shared across tenants, and co-tenanted GPUs leak timing information between customers. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [28:24](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1704s))

## All Talks

- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)
- [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)
- [Everything Is a Rollout](../talks/everything-is-a-rollout.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md)
- [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)
- [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)
- [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
- [Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md)
- [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Abhishek Bhardwaj](../speakers/abhishek-bhardwaj.md)
- [Alex Shaw](../speakers/alex-shaw.md)
- [Arjun Singh](../speakers/arjun-singh.md)
- [Bennet Fenner](../speakers/bennet-fenner.md)
- [Cat Wu](../speakers/cat-wu.md)
- [Dan Farrelly](../speakers/dan-farrelly.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Idan Gazit](../speakers/idan-gazit.md)
- [Ido Salomon](../speakers/ido-salomon.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Jason Lopatecki](../speakers/jason-lopatecki.md)
- [Jeffrey Lee-Chan](../speakers/jeffrey-lee-chan.md)
- [Joseph Wang](../speakers/joseph-wang.md)
- [Kenton Varda](../speakers/kenton-varda.md)
- [Liad Yosef](../speakers/liad-yosef.md)
- [Lovina Dmello](../speakers/lovina-dmello.md)
- [Moritz Johner](../speakers/moritz-johner.md)
- [Ryan Marten](../speakers/ryan-marten.md)
- [Shashi](../speakers/shashi.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Varun Singh](../speakers/varun-singh.md)

