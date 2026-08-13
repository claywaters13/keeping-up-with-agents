---
title: "agent execution infrastructure"
type: "concept"
slug: "agent-execution-infrastructure"
tier: "supporting"
maturity: "consolidating"
talk_count: 21
speaker_count: 25
---

# agent execution infrastructure

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **21** talk(s) by **25** speaker(s)

**Definition:** The compute substrate agents run on — VM and container pools, warm starts, cloud dev environments — as an operations and cost problem distinct from security isolation.

*Also referred to as: cloud sandboxes for agents, sandboxed cloud dev environments, micro vms, micro vm isolation, sandbox warm pools, managed agent infrastructure, distributed agent infrastructure, cloud dev environments*

## State of Practice

The conference treated agent compute as a fleet-operations problem with GPU-denominated economics: an idle sandbox is not a latency annoyance but wasted accelerator time, so the accepted move is to push spin-up cost onto cheap infrastructure via demand-scaled warm pools plus incremental memory snapshots, and to decouple the agent loop from tool execution so container setup never blocks first-token reasoning (Anthropic reported 60% faster TTFT at P50, >90% at P95). Hardware virtualization has become the default substrate — OpenAI's sandbox team and Form3 both landed on micro VMs after exhausting fork/exec, containers, and gVisor, and GitHub's automations run entirely as micro VMs in the cloud. The second structural shift is that durable state moved out of the execution process: session logs, handoff files, and snapshot lineages are the agent, and the worker is disposable, which is what makes autoscaling, migration, and crash recovery tractable at all. Storage, not compute, was repeatedly named as the current frontier — incremental snapshot/restore, block devices over filesystem passthrough, and scheduler placement scored by which snapshot layers a node already has cached. Where the field is still unsettled: whether a single containerized node is even a valid unit for real infrastructure work, whether to build this layer or rent it, and whether the scarce resource to optimize around is GPU time or general-purpose CPU.

## Consensus

### The durable home for agent execution is cloud-hosted, persistent environments rather than the developer's laptop; local-only running is a transitional state.

Support: **6** talk(s)

> "it's kind of a slap on the face for 20 years of cloud computing that everyone's running this locally on on their laptops"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [5:37](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=337s)

Supporting talks: [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)

### Sandbox startup and reset latency should be absorbed by over-provisioned, demand-scaled infrastructure so that expensive model/GPU workers never sit idle waiting on an environment.

Support: **3** talk(s)

> "you're paying the cost of that startup time on the infrastructure side not on the GPU side so your GPU workers have full utilization"
>
> — [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [13:48](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=828s)

Supporting talks: [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### Agent state must be externalized to durable substrate (append-only logs, files on disk, snapshots) so the executing process, container, or machine can be treated as disposable and replaceable.

Support: **4** talk(s)

> "When the log is the agent, the executor is allowed to be fallible."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### Hardware-virtualized micro VMs, not containers or userspace kernels, are the substrate teams converge on for agent execution — and should be adopted up front rather than arrived at after two years of iteration.

Support: **3** talk(s)

> "in the end, everyone always wants a VM because they tried everything. They tried containers, G visor, V8s."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [29:03](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1743s)

Supporting talks: [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Realtime multiplayer, automation, and you!](../talks/realtime-multiplayer-automation-and-you.md)

### Existing distributed-systems infrastructure — Kubernetes, CI runners, established reliability patterns — should be reused for agent compute, secrets, and scheduling rather than reinvented as agent-specific systems.

Support: **3** talk(s)

> "These are the exact questions Kubernetes already answers. So, that's where I'm headed. I'm not going to reinvent compute, secrets, and tools. Kubernetes already nailed those."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s)

Supporting talks: [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)

## Disagreements

### Is a single-node containerized or micro-VM sandbox an adequate execution unit for agent work, or does real infrastructure work require multi-node environments with live cloud resources?

| Position A | Position B |
|---|---|
| A single sandbox per rollout is the right unit; scale and fidelity come from warm pools, incremental snapshotting, and checkpoint/restore of that one node — you can even fork a run at any point in its trajectory.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md)* | Single-node sandboxing hits a hard ceiling: you cannot provision EC2 or Cloud Run inside one node, and deterministic simulation of network failures does not represent AWS-scale behavior, so environments must provision real infrastructure across multiple nodes.<br>*[Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md)* |

*Why it matters: It determines whether agent execution infra is a pooling-and-snapshotting problem solvable with one VM image, or a cloud-provisioning-per-rollout problem where a single environment takes hours to stand up and blows the economics of a post-training rollout.*

### Should teams build their own agent execution substrate, or treat hosting, sandboxing, session management, and credentials as undifferentiated work to outsource to a provider?

| Position A | Position B |
|---|---|
| It is undifferentiated heavy lifting — developers should own only system prompts, skills, tools, and domain context, and consume the agent loop, sandboxing, vaults, and session logs from a managed harness that ships the same primitives its vendor uses internally.<br>*[Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* | The execution/control plane is precisely where competitive advantage now lives, and handing your logs and sandboxes to a provider is the deepest form of lock-in — prompts and models are commoditizing, so teams should own and inspect the substrate themselves.<br>*[Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md)* |

*Why it matters: It decides whether an engineering org staffs a platform team for agent runtime, snapshotting, and log durability, or buys it — and whether agent history stays portable across providers.*

### Do agent loops need purpose-built sandbox fleets, or should they run on the CI infrastructure teams already have?

| Position A | Position B |
|---|---|
| Use GitHub Actions, GitLab, or CircleCI as the loop runtime — it already has your code and your secrets, and a dedicated cluster is unnecessary.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)* | Agent execution needs its own fleet: micro VMs with warm pools, snapshot-lineage-aware scheduling, per-turn incremental checkpointing, and isolation that CI runners do not provide — and isolated cloud sandboxes are the prerequisite for least-privilege access and non-technical teammates triggering real work.<br>*[From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [Multiplayer agentic engineering](../talks/multiplayer-agentic-engineering.md)* |

*Why it matters: One path is a weekend of YAML on infrastructure you already pay for; the other is a standing platform investment in VMM plumbing, snapshot storage, and autoscalers.*

### Which resource should agent execution infrastructure be optimized around — accelerator time, or general-purpose CPU?

| Position A | Position B |
|---|---|
| GPU time is the scarce, expensive resource; deliberately over-provision cheap sandbox compute (2–4x cheaper) and eat idle CPU and memory in warm pools to keep accelerators busy.<br>*[Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md)* | CPU is now scarce too — RL training environments and agent workloads are consuming general-purpose compute, cloud capacity is bounded by regional power allocation, and the shortage will get worse before it gets better.<br>*[Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)* |

*Why it matters: If CPU is also constrained, the standard advice to over-provision warm sandbox pools stops being free money and becomes a bid against your own training fleet for the same capacity.*

## Practical Guidance

**Do:**

- Run the agent loop and tool execution in separate failure domains so container setup does not block model reasoning — Anthropic measured 60% faster time-to-first-token at P50 and over 90% at P95 after decoupling
- Size the sandbox warm pool with a demand-based autoscaler that tracks how many workers currently need a sandbox, since the optimal pool size shifts over a multi-day training run and cannot be set upfront
- Deliberately over-provision the warm pool: sandbox compute runs 2–4x cheaper than GPU time, so redundancy still nets savings
- Combine warm pools with memory-snapshot restore rather than choosing one — the hybrid gets low creation latency without permanently idle capacity
- Snapshot incrementally per turn and return the snapshot immediately while uploading in the background, instead of saving multi-gigabyte images synchronously
- Score scheduler nodes by how many snapshot lineage layers they already have cached, to cut restore download time
- Expose storage to the guest as a block device rather than shared-folder filesystem passthrough, so you use the guest cache and avoid a VM exit on every filesystem operation; prefer POSIX-compliant storage over NFS
- Adopt micro VMs from day one rather than iterating through fork/exec, containers, gVisor, and V8 isolates
- Keep agent state in files on disk or an append-only log so a context wipe or machine crash does not destroy work, and build a single boot command that brings the whole fleet back up from that state
- Give each machine its own directory for machine-specific state and route all changes to shared state through pull requests, to stop silent divergence between hosts
- Run the fleet's single control point on an always-on machine — a laptop that sleeps cannot be a control plane
- Let agents declare their resource requirements and have the scheduler place them, instead of a human picking which machine each agent runs on
- Cap retries explicitly at the infrastructure layer, treating uncontrolled retry as a compute-incident risk rather than a resilience feature
- Reuse Kubernetes and existing CI for compute, secrets, and scheduling; build only the orchestration, review flow, and context management on top

**Avoid:**

- Giving an agent access to the Docker socket inside a container sandbox — it can spawn a privileged container and escape, making the container boundary meaningless
- Relying on the sandboxes shipped inside Codex and Claude Code as your isolation boundary for anything that needs Docker
- Seccomp syscall allowlists for open-ended agent workloads, since you cannot know in advance which syscalls the workload needs and you end up blocking real users
- Saving full multi-gigabyte snapshots on every turn — it is infeasible on both cost and latency
- Stacking many Claude Code and MCP processes on a single machine until memory is exhausted and swap fills
- Pointing two machines at the same shared context directory without separating machine-specific state
- Leaving harness workarounds in place after the model no longer needs them — Opus 4.5 dropped context anxiety and the old fixes became pure overhead, adding latency and causing incorrect cache discards
- Fire-and-forget writes of session logs to local disk (Claude Code and Codex JSONL, OpenCode SQLite), where a failed write silently loses the run's history
- Letting the model directly control production systems instead of emitting proposals that infrastructure validates and a gateway enforces
- Treating context compaction as the default recovery mechanism — it is slow, you cannot choose what survives, and what it drops is gone

## Notable Outliers

- Disk persistence, not compute, is the next major unlock for agent sandboxes — the thing that turns agents from ephemeral executors into durable knowledge workers. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [41:18](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2478s))
- Checkpoint/restore lets a harness run Monte Carlo tree search over sandbox states across many days, backtracking and re-exploring branches of the environment itself. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [32:52](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1972s))
- Scoping the agent's view to a single window instead of the full desktop raised pass rate from 62% to 80% while cutting token usage 34% — an infrastructure-side change that beat model swaps. ([Computer-Use 2.0: Agents Just Got Multi-Cursor](../talks/computer-use-20-agents-just-got-multi-cursor.md), [8:38](https://www.youtube.com/watch?v=ZSQb5fzRFPw&t=518s))
- Spinning up the entire stack for something like AWS Lambda takes hours, which simply does not fit inside a post-training rollout. ([Emulated: The Data for Fully Autonomous Software Engineers and Companies](../talks/emulated-the-data-for-fully-autonomous-software-engineers-and-companies.md), [12:13](https://www.youtube.com/watch?v=zkX03APVj0M&t=733s))
- With the log as the unit of state, one process can advance thousands of agents, eliminating sticky sessions and state migration entirely. ([The Log Is The Agent](../talks/the-log-is-the-agent.md), [7:24](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=444s))
- CPUs — not just GPUs — are now scarce because RL environments and agent workloads consume general-purpose compute, and cloud capacity is ultimately allocated by where power is available. ([Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [39:06](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=2346s))
- KV cache handling at 500K–1M context under concurrency is fundamentally a distributed file system / database problem, not conceptually hard — just unfamiliar to ML practitioners. ([Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s))
- GPU-accelerated sandboxes are poorly served by micro VMs today because VFIO passthrough cannot be shared across multiple tenants. ([From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [28:24](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1704s))

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

