---
title: "agent execution infrastructure"
type: "concept"
slug: "agent-execution-infrastructure"
tier: "supporting"
maturity: "consolidating"
talk_count: 23
speaker_count: 27
---

# agent execution infrastructure

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **23** talk(s) by **27** speaker(s)

**Definition:** The compute substrate agents run on — VM and container pools, warm starts, cloud dev environments — as an operations and cost problem distinct from security isolation.

*Also referred to as: cloud sandboxes for agents, sandboxed cloud dev environments, micro vms, micro vm isolation, sandbox warm pools, managed agent infrastructure, distributed agent infrastructure, cloud dev environments*

## State of Practice

The center of gravity for agent execution moved off the laptop and into cloud fleets during 2026, and the practitioner consensus is that hardware virtualization — micro VMs (Firecracker, CrosVM lineage) rather than containers, gVisor, or V8 isolates — is the right substrate to standardize on from day one. Once you are running fleets, the dominant cost term is not the sandbox itself but the accelerator waiting on it: sandbox and CPU compute run roughly 2–4x cheaper than GPU time, which makes an over-provisioned, demand-autoscaled warm pool plus memory-snapshot restore the accepted default rather than an extravagance. Creation latency and snapshot economics are now first-order design problems: incremental snapshots (not full multi-gigabyte images per turn), lineage-aware scheduling that scores nodes by cached snapshot layers, block-device access instead of shared-folder passthrough, and returning a snapshot to the caller while the upload finishes in the background. The second structural shift is that execution nodes are treated as disposable and durability is pushed into storage — an append-only session log, files on disk, or a VM snapshot — so a crashed worker or wiped context is an operational event rather than a lost agent. Most teams are explicitly refusing to reinvent the scheduler: Kubernetes, virtual kubelet, HPA, descheduler, and existing CI runners are being adapted to agent workloads, with the new layer confined to orchestration, review flow, and context management. The genuinely unresolved edges are multi-machine coordination, whether single-node sandboxes are sufficient at all for infrastructure-shaped work, and whether the durable substrate should be a machine snapshot or a log.

## Consensus

### Agents should execute in cloud-hosted, isolated environments rather than on developer laptops; local execution is a transitional state.

Support: **5** talk(s)

> "it's kind of a slap on the face for 20 years of cloud computing that everyone's running this locally on on their laptops"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [5:37](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=337s)

Supporting talks: [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)

### Agent state must be durable outside the running process — in files, an append-only log, or a database — so that the executor and its machine can be treated as disposable.

Support: **5** talk(s)

> "The context can get wiped, the machine can even crash, and the work still survives because it was never only in the model."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [3:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=190s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)

### Over-provisioning cheap sandbox/CPU capacity is economically correct because idle accelerator time, not sandbox time, is the dominant cost of an agent fleet.

Support: **4** talk(s)

> "these also could be like, you know, easily uh two to four times cheaper than your GPUs. So having a little bit of redundancy here, uh you still wind up saving money because you're maximizing the use of your GPU time."
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [13:48](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=828s)

Supporting talks: [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)

### Existing cluster and CI infrastructure (Kubernetes, HPA, virtual kubelet, GitHub Actions) should be adapted for agent fleets rather than replaced with purpose-built agent compute.

Support: **4** talk(s)

> "These are the exact questions Kubernetes already answers. So, that's where I'm headed. I'm not going to reinvent compute, secrets, and tools. Kubernetes already nailed those."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)

### Micro VMs, not containers or userspace kernels, are the execution unit teams converge on for agent sandboxes — and teams should start there rather than iterating through weaker primitives.

Support: **3** talk(s)

> "if you're a startup or a founder like in this space, like let me save you the story and two years of grief. Just please use micro VMs from the start."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [29:03](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1743s)

Supporting talks: [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

## Disagreements

### Where should the durable state of a running agent live — in the execution substrate (VM memory/disk snapshots) or in an append-only log outside the executor?

| Position A | Position B |
|---|---|
| Persistence belongs in the sandbox: incrementally snapshot and restore VM memory and disk, schedule restores onto nodes that already cache the snapshot lineage, and let harnesses fork and backtrack across sandbox states. Disk persistence, not compute, is framed as the next unlock.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)* | The executor should hold nothing worth saving. The agent's identity is its append-only log (or its files on disk); one process can advance thousands of agents, sticky sessions and state migration disappear, and machine-level snapshots are unnecessary machinery.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* |

*Why it matters: The snapshot path requires lineage-aware schedulers, incremental image storage, and per-turn upload budgets; the log path requires none of that but forfeits the ability to restore arbitrary machine state (installed packages, running processes, uncommitted filesystem mutations) after a crash or fork.*

### Is agent execution infrastructure a source of competitive differentiation, or undifferentiated work to outsource?

| Position A | Position B |
|---|---|
| It is the next differentiator. Prompts and models are commoditizing, an agentic control plane is emerging as a distinct layer analogous to Kubernetes for containers, and the organizations that build it win — including owning your own logs rather than leaving them on a provider whose incumbent incentive is to own more of the stack.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md)* | Hosting, session management, sandboxing, credentials, and observability are undifferentiated; developers should own only system prompts, skills, tools, and domain context. Run loops on the CI you already have rather than standing up a cluster, and use an existing sandbox product rather than rolling your own micro-VM plumbing.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)* |

*Why it matters: It determines whether a team staffs a platform group against sandbox lifecycle, snapshotting, and scheduling — or treats all of it as a vendor line item and accepts the resulting log/session lock-in.*

### Is a single-node containerized sandbox an adequate execution environment for agent work?

| Position A | Position B |
|---|---|
| Yes — a single micro VM per agent, made fast with warm pools and snapshot restore and made durable with incremental checkpoint/restore, is the unit that scales to ChatGPT/Codex volumes and to RL rollouts for computer use.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* | No — past a threshold the single-node sandbox breaks down, because you cannot provision EC2- or Cloud Run-style resources inside one node and deterministic simulation of network failures does not reproduce AWS-scale behavior. The future is multi-node environments with real provisioned cloud infrastructure.<br>*[Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)* |

*Why it matters: Multi-node real-infra environments break the homogeneous one-container-per-rollout assumption in post-training pipelines and introduce hours-long stack spin-up, which is irreconcilable with a per-rollout latency budget unless the whole rollout infrastructure is redesigned.*

## Practical Guidance

**Do:**

- Run a demand-based autoscaler over the warm sandbox pool, sizing it to the number of GPU workers currently requesting a sandbox, since the optimal pool size shifts during a multi-day training run and cannot be set upfront
- Combine a warm pool with memory-snapshot restore rather than choosing one — the pool absorbs creation latency, the snapshot absorbs idle CPU/memory cost
- Snapshot incrementally and return the snapshot to the caller while the upload to cloud storage continues in the background
- Score scheduler nodes by how many snapshot lineage layers they already have cached, to cut restore download time
- Give the guest a block device rather than shared-folder filesystem passthrough — it uses the guest cache and avoids a VM exit on every filesystem operation
- Decouple the agent loop from the tool-execution container so model reasoning is not blocked on container setup (measured at 60% faster time to first token at P50 and >90% at P95)
- Keep fleet state in files on disk so a single boot command brings the whole fleet back after a crash, and run the fleet's control point on an always-on machine rather than a laptop that sleeps
- Have agents declare resource requirements and let a scheduler place them, instead of a human choosing which machine each agent runs on
- Mark broken pods failed and let Kubernetes and the HPA recreate them rather than writing custom cross-cluster recovery logic
- Use a descheduler with ordinary taints to drain nodes gradually; NoExecute evicts every pod simultaneously and takes production down
- Instrument tensor core utilization and InfiniBand metrics for multi-node training, and pull any GPU running above ~78°C out of the pool immediately
- Run agent control loops on the CI you already have (GitHub Actions, GitLab, CircleCI) — it already holds your code and secrets
- Benchmark models and harnesses on your own repository for cost, speed, and quality; public benchmarks in another language or stack will not predict your results
- In enterprise settings, put agent memory in a database rather than on the local filesystem the way Claude Code and Codex do

**Avoid:**

- Handing an agent a Docker socket — it can spawn a privileged container and escape, and the sandboxes bundled with Codex and Claude are worthless once that access exists
- Saving full multi-gigabyte images on every turn; at fleet scale it is financially and latency-wise infeasible
- Seccomp allowlists for open-ended agent workloads — you cannot know the required syscalls in advance, so you end up blocking real users
- Fire-and-forget local JSONL log writes (Claude Code, Codex SDK mode): a failed write silently loses the data
- Pointing two machines at the same shared context directory without per-machine directories and PR-gated changes to shared state — you get collisions and silent divergence
- Stacking Claude Code and MCP processes on one machine until memory is exhausted and swap fills
- Trusting GPU utilization percentage as a training efficiency metric
- Running Ceph as the training filesystem if you can afford a commercial parallel filesystem — losing trust in your data is worse than the license cost
- Kueue's manually specified queue quotas on a fluid cluster where nodes come and go; they drift out of sync and break gang scheduling
- NFS or other non-POSIX-compliant storage for agent sandboxes — models are much better at standard POSIX behavior
- Leaving harness workarounds in place after a model upgrade; fixes for a limitation the new model no longer has become pure latency and cache-invalidation overhead
- Uncontrolled retries, which turn a minor API error into exponential resource growth and a compute incident

## Notable Outliers

- Disk persistence, not compute, is the next major unlock for agent sandboxes — turning agents from ephemeral executors into durable knowledge workers. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [41:18](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2478s))
- Checkpoint/restore lets a harness run Monte Carlo tree search over sandbox states across many days, backtracking and re-exploring branches of machine state. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [32:52](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1972s))
- CPUs — not just GPUs — are now scarce, because RL training environments and agent workloads consume large amounts of general-purpose compute, and the shortage will get worse before it gets better. ([Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [39:06](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2346s))
- Training should have strictly higher scheduling priority than production inference, evicting inference off the cluster — the value extracted from GPUs doing training exceeds that from serving the site. ([Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [10:33](https://www.youtube.com/watch?v=byn9PURoBNY&t=633s))
- When the log is the state, one process can advance thousands of agents, eliminating sticky sessions and state migration entirely. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s))
- Diffusion transformer inference is robust to degraded hardware and needs no multi-node setup, so GPUs too unhealthy for training remain usable for serving. ([Infra behind Krea 2: How to train and serve at scale](../talks/infra-behind-krea-2-how-to-train-and-serve-at-scale.md), [15:57](https://www.youtube.com/watch?v=byn9PURoBNY&t=957s))

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
- [Healthcare’s Agent Bytecode: X12 as the Harness for AI Agents](../talks/healthcares-agent-bytecode-x12-as-the-harness-for-ai-agents.md)
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
- [Vasant Kearney](../speakers/vasant-kearney.md)

