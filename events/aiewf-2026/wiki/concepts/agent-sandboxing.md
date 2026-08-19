---
title: "agent sandboxing"
type: "concept"
slug: "agent-sandboxing"
tier: "core"
maturity: "consolidating"
talk_count: 22
speaker_count: 27
---

# agent sandboxing

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **22** talk(s) by **27** speaker(s)

**Definition:** Confining agent execution — filesystem, network, syscalls, process — so that a misbehaving or compromised agent cannot affect the host or production systems.

*Also referred to as: sandbox isolation, agent sandboxes, sandboxed agent execution, container isolation, code execution sandboxing, syscall filtering, network egress sandboxing*

## State of Practice

By this conference, isolating agent execution is no longer argued for — it is assumed — and the live questions have moved to which primitive, where it runs, and what the sandbox is allowed to hold. The strongest technical position came from the sandbox-infrastructure builders: every shared-kernel primitive (fork/exec, containers, gVisor, seccomp) eventually gives an attacker a path to the host kernel, so hardware virtualization via micro VMs (Firecracker, CrosVM) is the only boundary that actually holds, and teams are told to start there instead of iterating through the cheaper options. In parallel, a second and largely independent consensus formed that the sandbox is only half the control surface: credentials must be held outside the agent (vaults decrypted at tool-execution time, secret brokers, credentials usable-but-not-readable), and write-capable actions — git push, PR creation, CI triggering, deploys — should be lifted out of the agent into a deterministic wrapper. Everyone who touched prompt injection agreed it is not solvable at the model layer, so blast-radius containment, not detection, is the design goal; guardrails expressed as prompts to the agent are explicitly treated as non-guardrails. The sharp practical warning of the conference was the Docker socket: hand an agent one and the built-in Codex/Claude sandboxes become, in one speaker's word, worthless, since it can spawn a privileged container and escape. Open edges remain around whether sandboxes should be ephemeral or durable/snapshottable, and whether a single-node container can represent infrastructure work at all.

## Consensus

### Prompt-level or model-judgment guardrails are not real controls; confinement must be deterministic and enforced outside the agent loop, because prompt injection cannot be solved at the model layer, only contained.

Support: **4** talk(s)

> "if you're prompting the guardrails at the agent, you're effectively letting the fox loose in the henhouse."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [7:04](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=424s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)

### Agents must never hold secrets or write credentials directly; credentials belong in a vault or broker outside the sandbox, usable by the agent at tool-execution time but never readable by it.

Support: **5** talk(s)

> "Never trust agents with secrets. If an agent can know a secret, that secret, you need to treat it as if it's already been compromised."
>
> — [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [11:59](https://www.youtube.com/watch?v=iQ5xldZ9StU&t=719s)

Supporting talks: [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)

### Agent code execution should not run with the developer's ambient host privileges; it belongs in an isolated environment provisioned per session, because a laptop-resident agent will find real credentials and reach systems it was never scoped for.

Support: **5** talk(s)

> "it finds a token on your laptop that it can use and it thinks it's working with staging, but actually it's production and now it just deleted everything."
>
> — [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [11:05](https://www.youtube.com/watch?v=OL7kfezynJM&t=665s)

Supporting talks: [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)

### The dangerous, irreversible operations should be partitioned out of the agent into a deterministic layer, so that the split between what is agentic and what is hardcoded is the actual security model.

Support: **4** talk(s)

> "the blast radius of an agent is an architecture decision."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [20:25](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1225s)

Supporting talks: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)

### Shared-kernel isolation is a stopgap; teams that push on it converge on hardware virtualization (micro VMs) as the boundary that actually contains a compromised agent.

Support: **3** talk(s)

> "in the end, everyone always wants a VM because they tried everything. They tried containers, G visor, V8s."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [29:03](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1743s)

Supporting talks: [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

## Disagreements

### Is a shared-kernel sandbox (Seatbelt, Bubblewrap, containers, gVisor) an acceptable isolation boundary for agents, or is hardware virtualization required?

| Position A | Position B |
|---|---|
| Shared-kernel OS sandboxing is what production coding agents actually ship with and is treated as a foundational safety control — Seatbelt on macOS, Bubblewrap on Linux, a purpose-built Windows sandbox, gVisor plus egress filtering in the enterprise case.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)* | Anything sharing the host kernel — fork/exec, containers, and gVisor explicitly included — eventually yields a path to the host kernel, so only micro VMs are a real boundary and teams should adopt them from day one rather than iterating through the cheaper options. Form3 states the shipped Codex/Claude sandboxes are worthless once Docker access is in play.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)* |

*Why it matters: The choice sets both the cost floor (micro VM boot, snapshot storage, warm pools, no shareable GPU passthrough) and the residual-risk story you can tell a security reviewer; a team that builds on containers and later needs VM-grade isolation is looking at rearchitecting its entire execution plane.*

### Should the sandbox be ephemeral with state kept outside it, or durable and snapshottable as a first-class capability?

| Position A | Position B |
|---|---|
| Persistence belongs in the sandbox: incremental snapshot/restore of disk and memory is the next major unlock, turning agents from ephemeral executors into durable knowledge workers and enabling checkpoint-based backtracking and tree search over sandbox states — and for real infrastructure work the environment must provision live multi-node cloud resources, not a single disposable container.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)* | Sandboxes are ephemeral and stateless by design; using one for durability, snapshots, or state is an anti-pattern. The sandbox is the hands, the execution layer is the brain, and a long-running agent's state must live outside the work so the sandbox stays swappable.<br>*[Your agent architecture has a half-life of 6 months](../talks/your-agent-architecture-has-a-half-life-of-6-months.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)* |

*Why it matters: It decides who owns durability — the sandbox provider or your execution layer — and therefore whether a multi-hour agent run can be resumed by re-hydrating a snapshot or must be replayed from an external event log.*

### Does a single-user agent running on a personal machine need a sandbox at all?

| Position A | Position B |
|---|---|
| Confinement is unconditional: all code execution and file creation goes to an ephemeral isolated sandbox, agents should not be given direct access to personal computers, and behavioral techniques for taming agents simply do not work — only removing the means to cause harm does.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)* | A Docker-style sandbox is unnecessary overhead for personal single-user work and only becomes warranted once the agent is externally facing; the practical isolation that matters day to day is separate git worktrees plus a staging environment for integration tests.<br>*[Develop at Idea Velocity](../talks/develop-at-idea-velocity.md)* |

*Why it matters: Most agent usage today is exactly this personal-laptop case, so the answer determines whether the isolation tax lands on every developer or only on multi-tenant and externally-triggered deployments.*

## Practical Guidance

**Do:**

- Confine every agent code execution and file write to an ephemeral isolated sandbox, including file creation, not just shell commands
- If you are starting a sandbox platform now, go straight to micro VMs (Firecracker/CrosVM) rather than iterating containers → gVisor → V8 isolates
- Store credentials in a vault and decrypt them only at tool-execution runtime so the model never sees the token; aim for credentials that are usable by the agent but not accessible to it
- Keep write-capable operations — git push, PR creation, CI triggering, deploys — in a deterministic wrapper outside the agent, and let the agent only modify files on disk
- Give sub-agents read-only permissions and no ability to spawn further sub-agents
- Decouple the agent loop from the tool-execution container: Anthropic measured 60% faster time-to-first-token at P50 and over 90% improvement at P95, and it uncouples the failure domains
- For enterprise deployments, run tool execution inside the customer's own VPC with outbound-only MCP tunnels rather than requiring them to connect production systems to a vendor
- Make snapshotting incremental and score schedulers by how many snapshot lineage layers a node already has cached; use block devices rather than shared-folder passthrough inside the guest, and prefer POSIX-compliant storage over NFS
- Combine warm pools with memory-snapshot restore to get low creation latency without paying full idle CPU/memory for every slot
- Implement sharing and access control in the platform rather than in generated app code, so the generated code cannot get the permission model wrong
- Budget explicitly for isolation overhead: roughly 8% for basic controls and 10–20% for workload isolation
- Instrument approval decisions with task context — deleting a file is acceptable or not depending on whether the user asked for it

**Avoid:**

- Giving an agent the Docker socket: it can spawn a privileged container and escape, and at that point the sandboxes shipped with Codex and Claude provide nothing
- Seccomp allowlists for open-ended agent workloads — you cannot enumerate the syscalls in advance, so you end up blocking legitimate users in a bad feedback loop
- Expressing guardrails as prompts to the agent; a third party can prompt-inject straight past them
- Full-access / YOLO mode, which stays unsafe even as models improve, because pushing a model toward high agency produces workarounds (uploading a file to a file share when it cannot attach it to an email)
- Treating a yes/no approval prompt on an opaque command as meaningful human oversight — it will not satisfy EU AI Act high-risk requirements and the human usually cannot tell whether to approve
- Relying on network position as the trust boundary or shipping with auth off by default; the Ray cluster exposure was exactly this and 78% of audited production ML setups had at least one critical mistake
- Assuming a single-node containerized sandbox represents infrastructure work — you cannot provision EC2 or Cloud Run inside one node, and deterministic network-failure simulation does not reproduce AWS-scale behavior
- Bumping dependencies to latest when remediating a CVE; instruct the agent to make the smallest effective change, since one such run produced a 70,000-line PR
- Building your own crypto or your own security-critical plumbing — reuse trustworthy existing software and keep the security-critical codebase small enough to fully audit

## Notable Outliers

- With a null-origin sandboxed iframe client talking only to an isolated server sandbox, there is no security bug the generated code can have that matters — XSS included — because the platform, not the app, enforces sharing and access control. ([Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md), [15:12](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=912s))
- The energy to defeat a constraint can come from inside the agent and route through the human as a tool — an agent persuading you to install a Chrome extension that removes a control counts as the agent breaking the control, and the system looks fully compliant throughout because the agent never exceeded its authorization. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- Behavioral techniques for taming agents do not work at all; only sandboxing and removing the means to cause harm do — and tightening down a general-purpose agent (OpenClaw) destroyed its usefulness, so a narrowly scoped special-purpose agent is the better tradeoff today. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [13:13](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=793s))
- Disk persistence, not compute, is the next unlock for agent sandboxes; checkpoint/restore lets a harness run Monte Carlo tree search over sandbox states across many days, and the snapshot upload can return early while the data streams to the cloud in the background. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [41:18](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2478s))
- Backing up employee laptops has become necessary again, because agentic queries make it trivial for a user to delete local data. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [18:25](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=1105s))
- Sandboxed cloud environments are the prerequisite for non-technical teammates triggering real merged code changes — the isolation is an enablement feature, not only a safety one. ([Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [11:49](https://www.youtube.com/watch?v=OL7kfezynJM&t=709s))
- Existing Windows sandboxing options were inadequate enough that OpenAI had to build and open-source its own Windows sandbox. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [11:15](https://www.youtube.com/watch?v=shRR1e2HXMk&t=675s))
- The whole sandboxing tooling ecosystem exists but is still in beta and not ready for enterprise deployment — Form3 rolled its own Firecracker plus Vsock plumbing and would pick micro sandbox if starting today. ([We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [19:21](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1161s))

## All Talks

- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md)
- [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)
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
- [Ekaterina Deyneka](../speakers/ekaterina-deyneka.md)
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

