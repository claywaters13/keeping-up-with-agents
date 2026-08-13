---
title: "I Run a Fleet of AI Agents Across Three Machines. Here's What Broke."
type: "talk"
slug: "i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke"
org: "KRAFTON"
video_id: "4kYl2_mqmnQ"
duration_sec: 551
word_count: 1651
speakers: ["Kyle Jaejun Lee"]
---

# I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.

**Speakers:** [Kyle Jaejun Lee](../speakers/kyle-jaejun-lee.md)

**Org:** KRAFTON

**Duration:** 9m 11s

[Watch on YouTube](https://www.youtube.com/watch?v=4kYl2_mqmnQ)

## Summary

Kyle Jaejun Lee describes running a personal fleet of AI coding agents across a MacBook and two always-on Linux boxes, and catalogs the failures he hit scaling from one terminal to a multi-machine setup. His core argument is that a flat pile of agents doesn't scale because the human becomes the scheduler, memory, and reviewer; the fix is an explicit org-chart hierarchy (CEO/VP/manager/worker) where each agent has scoped context and an approval boundary, so the operator reviews only one context instead of six. He argues agent state should live in files on disk rather than in the model's context window, which lets him reset context outright instead of compacting, and lets a crashed machine reboot the whole fleet from a single boot command. He then walks through five concrete multi-machine failures — orchestrators doing work instead of delegating, tmux pane sprawl, OOM from stacked sessions, git credential collisions, and a laptop dying mid-job — plus the fixes (CLI-only dispatch, per-machine directories with PR-gated shared state, a single consolidated review gateway on an always-on box, Discord bots as a phone-based router). He closes by mapping his four unsolved problems onto Kubernetes primitives and declaring he'll build orchestration on top rather than reinvent compute, secrets, and scheduling. Worth watching if you're operating multiple agents in parallel and want a concrete, battle-tested inventory of what breaks.

## Key Points

- Running six live agent contexts at once makes the human the bottleneck, because you simultaneously become the scheduler, the memory, and the reviewer.
- Modeling agents as an explicit hierarchy (CEO, VP, manager, worker) with real entity types — not a metaphor — gives each agent a scoped context slice and its own approval boundary, collapsing the operator's load to a single context.
- Agent state should live in files on disk (shared context, machine-bound state, mission, status, handoff folders) rather than inside the model's context window.
- The speaker abandoned context compaction entirely in favor of a hard reset: clearing context and letting the agent re-read its own handoff and history files, because compaction is slow and you can't control what survives.
- Plans drift as they flow down the hierarchy, so a review gateway makes every layer block on submitting its plan until approval, after which a hook auto-resumes the work — giving one inbox and one control point.
- Five things broke when scaling past one machine: orchestrators doing work instead of delegating, tmux panes multiplying until unreadable and unscrapable, out-of-memory from stacked Claude Code and MCP processes, git credentials colliding across workspaces, and a sleeping/crashing laptop killing in-flight jobs.
- Cross-machine context sync runs over git plus tmux send-keys over SSH, but shared directories silently diverge — the fix was per-machine directories for machine-specific state and pull-request-gated changes to shared state.
- The single point of control must live on an always-on machine, and Discord bots (one per machine) turn a phone into the fleet's remote control.
- The four remaining unsolved problems — cross-machine consistency, abstracting local-only tools, secure credential handoff, and resource placement — are exactly what Kubernetes already solves, so the plan is to stack K8s underneath and build only the orchestration layer on top.

## Notable Quotes

> "At that point, I'm not running agents anymore. I've become the scheduler, deciding who does what."
>
> — [0:35](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=35s) &middot; *names the core failure mode of parallel agent operation in one line*

> "I just couldn't hold what six agents were doing at once. My own attention was the bottleneck."
>
> — [1:13](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=73s) &middot; *states the scaling limit as human attention, not compute*

> "How does a handful of executives run a company of thousands of people? They don't hold all of it in their heads. They separate context. Each person only ever sees their own slice."
>
> — [1:13](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=73s) &middot; *the analogy that motivates the whole architecture*

> "These are real entity types in the system. It is not a cute metaphor. Each one is its own agent with its own scoped context and its own approval boundary."
>
> — [1:51](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=111s) &middot; *insists the org hierarchy is implemented structure, not framing*

> "So, instead of holding six contexts in my head, I hold exactly one."
>
> — [1:51](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=111s) &middot; *quantifies the payoff of hierarchical context scoping*

> "The state lives in files. It is not trapped inside one model. And this is the single most practical thing I learned all year."
>
> — [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s) &middot; *the speaker's own designation of his highest-value lesson*

> "I stopped doing it. It's slow. I can't choose what survives. And whatever it throws away is just gone."
>
> — [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s) &middot; *a three-part indictment of compaction that others would dispute*

> "So, instead, I don't compact, I reset. And by reset, I mean right inside Claude, I clear the context completely."
>
> — [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s) &middot; *the contrarian alternative to the built-in compaction workflow*

> "The context can get wiped, the machine can even crash, and the work still survives because it was never only in the model."
>
> — [3:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=190s) &middot; *states the durability property that file-based state buys*

> "Any layer that wants to act submits its plan and then it blocks. It waits. Nothing runs until I approve."
>
> — [3:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=190s) &middot; *concrete description of the human-in-the-loop gate design*

> "So I forced its hand. A CLI harness with skills that call those CLIs. So dispatching becomes the only path it can take."
>
> — [3:48](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=228s) &middot; *prescribes constraining the action space over prompting for delegation*

> "And honestly, I didn't build this gateway by hand. An infra team inside the fleet built it. Agents building the tools that run the agents."
>
> — [3:48](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=228s) &middot; *reports agents bootstrapping their own orchestration tooling*

> "The expectation is clean. Credential A to workspace A, credential B to workspace B, one to one. The reality, they collided, crossed over, bound to the wrong workspaces."
>
> — [5:07](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=307s) &middot; *specific, reproducible multi-workspace credential failure*

> "So, the very first thing I did was build a boot command, one overlord boot, and the whole fleet comes straight back up because all the state was sitting in files."
>
> — [5:07](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=307s) &middot; *ties crash recovery directly back to the file-state decision*

> "Per-machine directories for machine-specific state, and the shared stuff only changes through a pull request. It's boring, but boring is what stops the two machines from silently disagreeing."
>
> — [6:34](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=394s) &middot; *names the tradeoff: boring coordination beats silent divergence*

> "Your one point of control can't be a thing that falls asleep."
>
> — [7:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=430s) &middot; *crisp operational rule for where the control plane lives*

> "at one point I went looking for a feature I'd built, and I genuinely could not remember which machine I'd built it on"
>
> — [7:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=430s) &middot; *the failure that motivated a single unified router*

> "An agent should just declare what it needs, not where it runs."
>
> — [7:45](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=465s) &middot; *the declarative-placement thesis for agent infrastructure*

> "These are the exact questions Kubernetes already answers. So, that's where I'm headed. I'm not going to reinvent compute, secrets, and tools. Kubernetes already nailed those."
>
> — [8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s) &middot; *takes a clear side on build-vs-reuse for agent infrastructure*

> "One machine, I solved. Across machines, still rough, still building."
>
> — [8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s) &middot; *honest scoping of what is and isn't actually working*

## Positions

- A flat pile of parallel agents does not scale because the human is forced into three roles at once — scheduler, memory, and reviewer. ([1:13](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=73s), confidence: stated)
- Agent hierarchies should be implemented as real entity types with scoped context and approval boundaries, not used as a descriptive metaphor. ([1:51](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=111s), confidence: stated)
- Context compaction is the wrong default: it is slow, gives you no control over what survives, and permanently discards what it drops. ([2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s), confidence: stated)
- Clearing context entirely and re-reading self-written handoff and history files is a better recovery mechanism than summarizing history. ([2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s), confidence: stated)
- Agent state kept in files on disk survives context wipes and machine crashes, whereas state in the model's context window does not. ([3:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=190s), confidence: stated)
- Orchestrator agents will do the work themselves instead of delegating unless the tooling makes dispatching the only available path. ([4:29](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=269s), confidence: stated)
- Stacked Claude Code and MCP processes on a single machine will exhaust memory and fill swap. ([5:07](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=307s), confidence: stated)
- Two machines pointing at the same shared context directory will produce conflicts and silent divergence unless machine-specific state is separated and shared state is changed only via pull request. ([6:34](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=394s), confidence: stated)
- The fleet's single control point must run on an always-on machine, because a laptop that sleeps cannot serve as a control plane. ([7:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=430s), confidence: stated)
- Agents should declare their resource requirements rather than having a human decide which machine they run on. ([7:45](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=465s), confidence: stated)
- Kubernetes already solves compute, secrets, tools, and scheduling for agent fleets, so the only new layer worth building is orchestration, review flow, and context management. ([8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s), confidence: stated)
- Multi-machine agent orchestration is an unsolved problem that nobody has figured out yet. ([8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s), confidence: stated)
- Agents can successfully build the infrastructure that manages other agents, as evidenced by an in-fleet infra team building the review gateway. ([3:48](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=228s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent memory](../concepts/agent-memory.md)
- [context compaction](../concepts/context-compaction.md)
- [context engineering](../concepts/context-engineering.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

