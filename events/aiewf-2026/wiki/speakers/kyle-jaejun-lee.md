---
title: "Kyle Jaejun Lee"
type: "speaker"
slug: "kyle-jaejun-lee"
talk_count: 1
---

# Kyle Jaejun Lee

## Talks

- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent memory](../concepts/agent-memory.md)
- [context compaction](../concepts/context-compaction.md)
- [context engineering](../concepts/context-engineering.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

## Quotes

> "At that point, I'm not running agents anymore. I've become the scheduler, deciding who does what."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [0:35](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=35s)

> "I just couldn't hold what six agents were doing at once. My own attention was the bottleneck."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [1:13](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=73s)

> "How does a handful of executives run a company of thousands of people? They don't hold all of it in their heads. They separate context. Each person only ever sees their own slice."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [1:13](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=73s)

> "These are real entity types in the system. It is not a cute metaphor. Each one is its own agent with its own scoped context and its own approval boundary."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [1:51](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=111s)

> "So, instead of holding six contexts in my head, I hold exactly one."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [1:51](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=111s)

> "The state lives in files. It is not trapped inside one model. And this is the single most practical thing I learned all year."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

> "I stopped doing it. It's slow. I can't choose what survives. And whatever it throws away is just gone."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

> "So, instead, I don't compact, I reset. And by reset, I mean right inside Claude, I clear the context completely."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

> "The context can get wiped, the machine can even crash, and the work still survives because it was never only in the model."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [3:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=190s)

> "Any layer that wants to act submits its plan and then it blocks. It waits. Nothing runs until I approve."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [3:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=190s)

> "So I forced its hand. A CLI harness with skills that call those CLIs. So dispatching becomes the only path it can take."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [3:48](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=228s)

> "And honestly, I didn't build this gateway by hand. An infra team inside the fleet built it. Agents building the tools that run the agents."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [3:48](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=228s)

> "The expectation is clean. Credential A to workspace A, credential B to workspace B, one to one. The reality, they collided, crossed over, bound to the wrong workspaces."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [5:07](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=307s)

> "So, the very first thing I did was build a boot command, one overlord boot, and the whole fleet comes straight back up because all the state was sitting in files."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [5:07](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=307s)

> "Per-machine directories for machine-specific state, and the shared stuff only changes through a pull request. It's boring, but boring is what stops the two machines from silently disagreeing."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [6:34](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=394s)

> "Your one point of control can't be a thing that falls asleep."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [7:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=430s)

> "at one point I went looking for a feature I'd built, and I genuinely could not remember which machine I'd built it on"
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [7:10](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=430s)

> "An agent should just declare what it needs, not where it runs."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [7:45](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=465s)

> "These are the exact questions Kubernetes already answers. So, that's where I'm headed. I'm not going to reinvent compute, secrets, and tools. Kubernetes already nailed those."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s)

> "One machine, I solved. Across machines, still rough, still building."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [8:23](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=503s)

