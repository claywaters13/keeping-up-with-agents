---
title: "From fork() to Fleet: Designing an Agent Sandbox Cloud"
type: "talk"
slug: "from-fork-to-fleet-designing-an-agent-sandbox-cloud"
track: "Sandbox & Platform Engineering"
org: "OpenAI"
day: "Day 3 — Session Day 2"
room: "Track 1"
video_id: "OqM67QG_Ikk"
duration_sec: 2673
word_count: 7745
speakers: ["Abhishek Bhardwaj"]
---

# From fork() to Fleet: Designing an Agent Sandbox Cloud

*Program title: From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2*

**Speakers:** [Abhishek Bhardwaj](../speakers/abhishek-bhardwaj.md)

**Org:** OpenAI

**Track:** Sandbox & Platform Engineering &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 44m 33s

[Watch on YouTube](https://www.youtube.com/watch?v=OqM67QG_Ikk)

## Summary

Abhishek Bhardwaj of OpenAI's RL and agent infrastructure team gives a first-principles walkthrough of why AI agents need sandboxes and how to build a cloud that runs them securely at scale. He traces the escalation of isolation primitives — raw fork/exec, containers with namespaces/cgroups/seccomp, gVisor's user-space kernel, and finally hardware-virtualized micro VMs — arguing that every option short of a VM eventually leaves the host kernel reachable, so teams should start with micro VMs rather than grieving their way there. The second half argues that disk persistence is the next major unlock: cheap incremental block-level snapshot/restore lets agents survive node failures, run multi-day tasks, and do Monte Carlo tree search over sandbox states. He closes with orchestration, showing how snapshot lineage can be fed into the scheduler to route sandboxes to nodes that already hold the needed layers. Worth watching if you build or operate agent execution infrastructure and want the OS-level tradeoffs laid out plainly.

## Key Points

- Sandboxes matter for both RL training and product serving, but the objectives differ: research optimizes for throughput across many parallel rollouts, while product optimizes for latency, with reliability and security mattering to both.
- There are two fundamental attack vectors on Linux — getting root in ring three, and a kernel-mode exploit in ring zero — and every sandboxing primitive should be judged by how hard it makes reaching the host kernel.
- Containers (namespaces plus cgroups) solve resource isolation and noisy-neighbor problems, and seccomp shrinks the syscall attack surface, but containers still share the host kernel, and seccomp filters have a painful feedback loop because you cannot predict which syscalls an agent will need.
- gVisor moves syscall handling into a user-space kernel (the Sentry, with the Gofer for filesystem access), which raises the bar to a two-step chained exploit but still ultimately sits on the host kernel.
- Hardware virtualization is the only primitive where the guest running in ring zero under VMX non-root mode leaves the host genuinely protected, at the cost of a performance penalty on every guest-host context switch.
- 'Micro' in micro VM refers to the VMM, not the guest: Rust-based VMMs like CrosVM, Firecracker, and Cloud Hypervisor have smaller memory footprints and faster boot because they support fewer devices than QEMU, and their emulated devices can be individually jailed.
- Micro VM tradeoffs include heavy guest-host exit costs, awkward memory reclaim via the balloon driver, and GPU access that is either high-level (virtio-GPU) or exclusive to a single sandbox (VFIO).
- Persistence should be incremental and block-level rather than full-image or file-level, with a fast-returning save API that uploads in the background, and a choice between always-on write-through storage and explicit copy-on-write snapshots using FIEMAP to find changed extents.
- Checkpointing improves reliability and scale, not just durability: it lets a long-running sandbox be restored on another node after a failure or during a cluster upgrade, and enables harnesses to branch and backtrack across multi-day exploration.
- Scheduling can exploit snapshot lineage by scoring nodes on how many of the required layers they already hold, and low-latency creation can come from warm pools, just-in-time memory-snapshot restore, or a hybrid of the two.

## Notable Quotes

> "it's kind of a slap on the face for 20 years of cloud computing that everyone's running this locally on on their laptops"
>
> — [5:37](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=337s) &middot; *Frames the whole talk's thesis that agent workloads belong in a purpose-built cloud.*

> "the future is like us running your agents in the cloud. Like they're persistent, long-running."
>
> — [6:12](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=372s) &middot; *States the speaker's core prediction plainly.*

> "reliability is important on both both sides. Like, if you fail constantly, you've wasted like GPU tokens on both sides. And GPU is like gold right now."
>
> — [7:30](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=450s) &middot; *Ties infra reliability directly to compute economics.*

> "compute was the first unlock. People realized you give sandboxes a a Linux computer and they do crazy things because they're pre-trained on so much Linux data"
>
> — [8:10](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=490s) &middot; *Explains why a full Linux box is the right abstraction for agents.*

> "if you get kernel exploit, it's like it's a it's a New York Times article waiting to happen"
>
> — [10:20](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=620s) &middot; *Memorable framing of the stakes of the kernel boundary.*

> "fork exec is the simplest thing you can do. It has one thing going for it. It's the most performance solution"
>
> — [11:38](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=698s) &middot; *Names the performance-versus-isolation tradeoff at the baseline.*

> "many times you don't know beforehand what system calls some container might call, right? So, now you're blocking requests for users"
>
> — [15:21](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=921s) &middot; *Concrete operational objection to seccomp allowlisting for agent workloads.*

> "containers interact with the same host kernel, so they do they do have some protections, but at the end it's the same host kernel they're trying to attack"
>
> — [16:00](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=960s) &middot; *The central security argument against containers as an agent sandbox.*

> "you first exploit a problem in the sentry or the gofer, and then you exploit from the gofer to the kernel, right? You can still get to the host kernel eventually."
>
> — [17:21](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1041s) &middot; *Specific technical critique of gVisor's security boundary.*

> "ring zero gives the guest kernel full control inside the guest, but no control on the host. So, you can exploit the guest all you want, but the host is still protected."
>
> — [19:25](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1165s) &middot; *The precise reason virtualization is qualitatively different from the alternatives.*

> "There's a performance penalty you pay every time the CPU is switching back and forth between these two modes."
>
> — [19:25](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1165s) &middot; *States the cost side of the virtualization tradeoff explicitly.*

> "historically, many, many escape attacks were attacking the devices written in C"
>
> — [23:26](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1406s) &middot; *Motivates the industry shift to Rust-based VMMs with evidence.*

> "it has nothing to do with what's running inside the guest. It's It's everything to do with the VMM itself."
>
> — [24:06](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1446s) &middot; *Corrects a widespread misconception about the term 'micro VM'.*

> "system tricks can cover performance issues, but they cannot hide security breaches. And as a company, you can lose trust once and it's like very hard to regain."
>
> — [28:24](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1704s) &middot; *The speaker's explicit design principle for resolving the security-performance tension.*

> "in the end, everyone always wants a VM because they tried everything. They tried containers, G visor, V8s."
>
> — [29:03](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1743s) &middot; *The 'seven stages of sandboxing' claim that anchors his recommendation.*

> "if you're a startup or a founder like in this space, like let me save you the story and two years of grief. Just please use micro VMs from the start."
>
> — [29:03](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1743s) &middot; *The talk's single most actionable prescription.*

> "counterintuitively, persistence actually helps reliability and scale. They might seem like orthogonal concepts, but but they're very much related."
>
> — [31:29](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1889s) &middot; *The non-obvious claim underpinning the persistence half of the talk.*

> "if I have to save gigabytes of data at every turn, like like I'm going to bankrupt the company and like it's just a slow experience regardless"
>
> — [33:33](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2013s) &middot; *Cost argument for incremental snapshotting at ChatGPT scale.*

> "I can actually lie to you while I'm uploading to the cloud. So, the snapshot can happen return very fast as I'm uploading in the background."
>
> — [39:20](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2360s) &middot; *A concrete latency trick that makes cheap snapshotting practical.*

> "NFS, for instance, isn't as performant and is not POSIX-compliant. And I think our models are just very good at anything POSIX compliant and standard."
>
> — [39:57](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2397s) &middot; *Argues model behavior itself should drive storage-interface choices.*

> "storage is the next unlock here. As you're working on sandboxes, think of what what all you can snapshot and restore fast"
>
> — [41:18](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2478s) &middot; *The talk's forward-looking takeaway.*

## Positions

- Any sandbox primitive that shares the host kernel — fork/exec, containers, or gVisor — eventually allows an attacker to reach the host kernel; only hardware virtualization prevents this. ([17:59](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1079s), confidence: stated)
- Startups building agent sandboxes should adopt micro VMs from the start rather than iterating through containers, gVisor, and V8 isolates. ([29:03](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1743s), confidence: stated)
- Security should be prioritized over performance because system tricks can compensate for performance issues but not for a breach. ([28:24](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1704s), confidence: stated)
- Seccomp filtering is a poor fit for open-ended agent products because you cannot know in advance which syscalls the workload needs, creating a bad feedback loop of blocked users. ([15:21](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=921s), confidence: stated)
- The 'micro' in micro VM refers to the VMM's smaller footprint and faster boot, not to anything about the guest. ([24:06](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1446s), confidence: stated)
- CrosVM was the first Rust-based VMM, and Firecracker was forked from it. ([24:57](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1497s), confidence: stated)
- Disk persistence, not compute, is the next major unlock for agent sandboxes, turning agents from ephemeral executors into durable knowledge workers. ([41:18](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2478s), confidence: stated)
- Snapshotting must be incremental at ChatGPT/Codex scale because saving full multi-gigabyte images every turn is financially and latency-wise infeasible. ([33:33](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2013s), confidence: stated)
- Block-device access inside a micro VM is more efficient than shared-folder filesystem passthrough because it uses the guest cache and avoids exiting on every filesystem operation. ([36:35](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2195s), confidence: stated)
- Checkpoint/restore enables harnesses to run Monte Carlo tree search over sandbox states across many days, backtracking and re-exploring. ([32:52](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1972s), confidence: stated)
- Schedulers should score nodes by how many snapshot lineage layers they already have cached, reducing download time on restore. ([43:08](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2588s), confidence: stated)
- Warm pools trade idle CPU and memory consumption for low creation latency, and a hybrid of warm pool plus memory-snapshot restore gets the best of both. ([42:32](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2552s), confidence: stated)
- Giving models code execution was the key unlock for domains with verifiable rewards like math and code. ([2:11](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=131s), confidence: stated)
- Running agents locally on laptops is a temporary state and the durable future is persistent, long-running agents in the cloud. ([6:12](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=372s), confidence: implied)
- GPU-accelerated sandboxes are poorly served by micro VMs today, since VFIO passthrough cannot be shared across multiple tenants. ([28:24](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1704s), confidence: stated)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [durable execution](../concepts/durable-execution.md)

