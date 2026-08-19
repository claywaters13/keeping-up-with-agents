---
title: "agent execution infrastructure"
type: "concept"
slug: "agent-execution-infrastructure"
tier: "supporting"
maturity: "consolidating"
talk_count: 22
speaker_count: 26
---

# agent execution infrastructure

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **22** talk(s) by **26** speaker(s)

**Definition:** The compute substrate agents run on — VM and container pools, warm starts, cloud dev environments — as an operations and cost problem distinct from security isolation.

*Also referred to as: cloud sandboxes for agents, sandboxed cloud dev environments, micro vms, micro vm isolation, sandbox warm pools, managed agent infrastructure, distributed agent infrastructure, cloud dev environments*

## State of Practice

The conference treated agent compute as a scheduling-and-cost problem that has outgrown the laptop: sessions are micro VMs in the cloud, and the local-versus-cloud distinction is being designed away rather than exposed to users. The dominant cost lever named repeatedly is idle time on the expensive resource — GPU workers stalling on sandbox spin-up during RL rollouts, or agent reasoning blocked on container boot — so the pattern that emerged is to move provisioning off the critical path via demand-scaled warm pools, incremental memory/disk snapshots, and decoupling the agent loop from tool execution (Anthropic reported 60% faster time-to-first-token at P50, >90% at P95, from that split alone). On the primitive itself, OpenAI and Form3 both landed on hardware virtualization after exhausting containers, gVisor, and seccomp, and both advise starting there. The second consistent move is refusing to reinvent the substrate: Kubernetes for placement and secrets, existing CI runners for agent loops, virtual-kubelet and deschedulers for cross-cluster capacity, distributed-systems reliability patterns for retries and consistency. What is unresolved is where durability lives — in snapshotted machine state or in an append-only log that makes the executor disposable — and whether a single-node sandbox can represent real infrastructure work at all. Multi-machine fleet orchestration was described outright as still unsolved.

## Consensus

### Agent execution should move off developer laptops onto cloud compute the operator controls, with the local/cloud split hidden from the user.

Support: **5** talk(s)

> "it's kind of a slap on the face for 20 years of cloud computing that everyone's running this locally on on their laptops"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [5:37](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=337s)

Supporting talks: [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)

### Sandbox provisioning must be pulled off the critical path of the expensive resource — over-provisioned warm pools and pre-booted environments are worth their idle cost because the GPU or the model call is the thing you cannot afford to leave waiting.

Support: **3** talk(s)

> "these also could be like, you know, easily uh two to four times cheaper than your GPUs. So having a little bit of redundancy here, uh you still wind up saving money because you're maximizing the use of your GPU time."
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [13:48](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=828s)

Supporting talks: [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### Hardware-virtualized micro VMs, not containers or userspace kernels, are the execution primitive teams converge on for agent workloads — and teams that iterated through the cheaper options say to skip straight to them.

Support: **3** talk(s)

> "if you're a startup or a founder like in this space, like let me save you the story and two years of grief. Just please use micro VMs from the start."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [29:03](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1743s)

Supporting talks: [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

### Agent infrastructure should be built by adapting existing cloud-native machinery — Kubernetes scheduling, CI runners, distributed-systems reliability patterns — rather than inventing a new substrate; only the orchestration/review/context layer above it is genuinely new.

Support: **4** talk(s)

> "These are the exact questions Kubernetes already answers. So, that's where I'm headed. I'm not going to reinvent compute, secrets, and tools. Kubernetes already nailed those."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md)

### Durable agent state must live outside the running process — in files, an append-only session log, or a restorable snapshot — so that a crashed worker, a dead sandbox, or a wiped context does not destroy the work.

Support: **4** talk(s)

> "The context can get wiped, the machine can even crash, and the work still survives because it was never only in the model."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [3:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=190s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)

## Disagreements

### Should durability come from persisting the execution environment itself, or from persisting only the event log and treating compute as fungible?

| Position A | Position B |
|---|---|
| Persist the machine: incremental VM memory and disk snapshots, checkpoint/restore, and snapshot-lineage-aware scheduling turn the sandbox into a durable workspace, and disk persistence is the next major unlock for agents.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)* | Persist the log: the executor should be explicitly fallible and disposable, state lives in an append-only log or in files on disk, and one process can then advance thousands of agents without sticky sessions or state migration.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* |

*Why it matters: The choice determines whether you invest engineering in a snapshot/restore storage layer and node affinity, or in a durable event store and stateless workers — and it sets whether sandboxes are pets that must be recoverable or cattle that may be killed at any moment.*

### Is a single-node containerized sandbox an adequate execution environment for agent work and agent training?

| Position A | Position B |
|---|---|
| Yes, with engineering: one micro VM or container per rollout, optimized via warm pools, snapshot restore, and window-scoped observation, is the right unit and the remaining work is startup latency and utilization.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* | No: past a threshold a single node cannot represent infrastructure work at all — you cannot simulate EC2 or Cloud Run inside a sandbox, and deterministic network-failure simulation does not reproduce AWS-scale behavior, so environments must provision real multi-node cloud resources.<br>*[Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)* |

*Why it matters: If single-node holds, sandbox clouds are a latency and packing problem solvable with snapshots; if it does not, RL rollouts need real cloud provisioning per episode, which breaks rollout time budgets (spinning up an AWS-Lambda-like stack takes hours) and changes the cost model entirely.*

### Is agent execution infrastructure undifferentiated plumbing to outsource, or the primary source of competitive advantage?

| Position A | Position B |
|---|---|
| Undifferentiated: hosting, session management, sandboxing, credential handling, and observability should come from a harness vendor; developers should own only system prompts, skills, tools, and domain context.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* | Differentiating: prompts and models are both commoditizing and the agentic control plane is the next frontier, and whoever owns the log owns the agent — so teams should build and self-host this layer rather than hand it to a provider.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md)* |

*Why it matters: This decides whether a team's scarce infra engineers go into an internal control plane and log store or into domain tooling on top of a managed loop — and it determines exposure to log-level vendor lock-in, which was argued to be deeper than model or API lock-in.*

## Practical Guidance

**Do:**

- Run the agent loop and the tool-execution container as separate failure domains so model reasoning starts before the sandbox is ready (measured at 60% faster TTFT at P50, >90% at P95)
- Size the sandbox warm pool with a demand-based autoscaler tied to the number of GPU workers currently needing a sandbox, and re-scale it during multi-day runs rather than fixing it up front
- Combine a warm pool with memory-snapshot restore to get both low creation latency and fast state recovery
- Snapshot incrementally rather than writing full multi-gigabyte images per turn, and return the snapshot call immediately while uploading to object storage in the background
- Score scheduler nodes by how many snapshot lineage layers they already have cached, to cut restore download time
- Expose sandbox storage as a block device using the guest cache rather than shared-folder filesystem passthrough, and prefer POSIX-compliant filesystems over NFS
- Run agent control loops on existing CI (GitHub Actions, GitLab, CircleCI) which already has code and secrets access, instead of standing up a dedicated cluster
- Put the fleet's single control point on an always-on machine; a laptop that sleeps cannot be a control plane
- Let agents declare their resource requirements and have the scheduler place them, rather than assigning machines by hand
- Separate per-machine state into per-machine directories and change shared state only through pull requests when multiple machines share a context directory
- Store credentials in a vault decrypted only at tool-execution time, and offer MCP tunnels so enterprise tool execution runs inside the customer's own VPC with outbound-only calls to the agent loop
- For GPU fleets: track tensor core utilization and InfiniBand metrics, pull any GPU running above ~78°C out of the pool immediately, and checkpoint every 20-30 minutes on a filesystem fast enough to make that free
- Handle cross-cluster failures by marking the pod failed and letting Kubernetes and the HPA recreate it, instead of writing custom recovery logic
- Bound retries explicitly — an uncontrolled retry storm turns a minor API error into a compute incident

**Avoid:**

- Putting the agent loop and tool execution in the same container — it blocks first-token reasoning on container setup and couples the failure domains
- Relying on seccomp allowlists for open-ended agent workloads; you cannot know the syscall set in advance and you end up blocking real users
- Handing an agent a Docker socket — it can spawn a privileged container and escape, which makes the built-in Codex and Claude sandboxes worthless
- Optimizing sandbox startup time alone for computer-use environments that can be 40 GB
- Using NoExecute taints to reclaim nodes — they evict every pod simultaneously and take production down; use a descheduler with ordinary taints for gradual migration
- Trusting the GPU utilization metric as a training-efficiency proxy, or running Ceph as the parallel filesystem if you can afford a commercial one
- Swapping nodes reflexively after crashes — the same machines and code often run 12-24 hours after a series of hourly failures
- Fire-and-forget local JSONL log writes (Claude Code, Codex SDK mode) and SQLite state with known corruption issues (OpenCode) as the durability story for production agents
- Leaving authentication defaults off when promoting ML infrastructure to production — the Ray cluster exposure was an unset default, not a novel attack
- Letting the model directly control production systems; it should emit proposals that infrastructure validates, policy approves, and a gateway enforces
- Stacking many agent and MCP processes on one machine until memory is exhausted and swap fills

## Notable Outliers

- Disk persistence, not compute, is the next major unlock for agent sandboxes — it is what turns agents from ephemeral executors into durable knowledge workers. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [41:18](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2478s))
- Checkpoint/restore of sandbox state lets a harness run Monte Carlo tree search over machine states across many days, backtracking and re-exploring branches. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [32:52](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1972s))
- CPUs, not just GPUs, are now scarce, because RL training environments and agent workloads consume large amounts of general-purpose compute — and it will get worse before it gets better. ([Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [39:06](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2346s))
- Training workloads should preempt production inference on shared GPU clusters, because the value extracted from GPUs doing training exceeds that from serving production — and evicted inference can be transparently relocated to rented capacity without an outage. ([Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [10:33](https://www.youtube.com/watch?v=byn9PURoBNY&t=633s))
- Scoping a computer-use agent to a single window rather than the whole desktop raised pass rate from 62% to 80% while using 34% fewer tokens. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s))
- When the log is the state, one process can advance thousands of agents — removing sticky sessions, state migration, and coordination overhead from the execution layer. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s))
- Multi-machine agent orchestration remains unsolved: one machine is manageable, across machines is still rough. ([I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s))

## All Talks

- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)
- [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md)
- [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)
- [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)
- [OpenClaw in Your Hand: Building a Physical AI Terminal](../talks/openclaw-in-your-hand-building-a-physical-ai-terminal.md)
- [Production Evals For Agentic AI Systems](../talks/production-evals-for-agentic-ai-systems.md)
- [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)
- [RLM: Recursive Language Models for Large Codebases](../talks/rlm-recursive-language-models-for-large-codebases.md)
- [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)
- [The Log Is The Agent](../talks/the-log-is-the-agent.md)
- [The Messy Reality of Scale: Synthetic Data and Pre-Training](../talks/the-messy-reality-of-scale-synthetic-data-and-pre-training.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
- [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)

## Speakers

- [Abhishek Bhardwaj](../speakers/abhishek-bhardwaj.md)
- [Alexander Embiricos](../speakers/alexander-embiricos.md)
- [Arjun Singh](../speakers/arjun-singh.md)
- [Dan Fu](../speakers/dan-fu.md)
- [Dillon DuPont](../speakers/dillon-dupont.md)
- [Francesco Bonacci](../speakers/francesco-bonacci.md)
- [Gabriel Jorge Menezes](../speakers/gabriel-jorge-menezes.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [George Cameron](../speakers/george-cameron.md)
- [Idan Gazit](../speakers/idan-gazit.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Ishaan Sehgal](../speakers/ishaan-sehgal.md)
- [Joseph Wang](../speakers/joseph-wang.md)
- [Kevin Bai](../speakers/kevin-bai.md)
- [Kyle Jaejun Lee](../speakers/kyle-jaejun-lee.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [Lovina Dmello](../speakers/lovina-dmello.md)
- [Marah Abdin](../speakers/marah-abdin.md)
- [Micah Hill-Smith](../speakers/micah-hill-smith.md)
- [Moritz Johner](../speakers/moritz-johner.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Olive Song](../speakers/olive-song.md)
- [Robert McHardy](../speakers/robert-mchardy.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Shashi](../speakers/shashi.md)

