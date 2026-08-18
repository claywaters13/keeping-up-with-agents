---
title: "Abhishek Bhardwaj"
type: "speaker"
slug: "abhishek-bhardwaj"
role: "Member of Technical Staff, RL & Agent Infrastructure"
company: "OpenAI"
talk_count: 1
---

# Abhishek Bhardwaj

**Member of Technical Staff, RL & Agent Infrastructure &middot; OpenAI**

Abhishek Bhardwaj works on Agent and Reinforcement Learning Infrastructure at OpenAI. He builds systems that enable large-scale model training in RL environments, as well as secure and scalable cloud sandboxes for OpenAI’s agents. Before joining OpenAI, he created Arrakis, an open-source sandbox for AI agents. Previously, he worked at Google on ChromeOS and foundational microVM technologies, and at Replit on core infrastructure and early versions of Replit Agent.

[LinkedIn](https://www.linkedin.com/in/abshkbh)

## Talks

- [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md) (Sandbox & Platform Engineering)

## Scheduled Sessions

- **From fork() to Fleet: Designing an Agent Sandbox Cloud Pt 1** &middot; Day 3 — Session Day 2 &middot; 1:30pm-1:50pm &middot; Track 1
- **From fork() to Fleet: Designing an Agent Sandbox Cloud Pt2** &middot; Day 3 — Session Day 2 &middot; 1:55pm-2:15pm &middot; Track 1

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [durable execution](../concepts/durable-execution.md)

## Quotes

> "it's kind of a slap on the face for 20 years of cloud computing that everyone's running this locally on on their laptops"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [5:37](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=337s)

> "the future is like us running your agents in the cloud. Like they're persistent, long-running."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [6:12](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=372s)

> "reliability is important on both both sides. Like, if you fail constantly, you've wasted like GPU tokens on both sides. And GPU is like gold right now."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [7:30](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=450s)

> "compute was the first unlock. People realized you give sandboxes a a Linux computer and they do crazy things because they're pre-trained on so much Linux data"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [8:10](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=490s)

> "if you get kernel exploit, it's like it's a it's a New York Times article waiting to happen"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [10:20](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=620s)

> "fork exec is the simplest thing you can do. It has one thing going for it. It's the most performance solution"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [11:38](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=698s)

> "many times you don't know beforehand what system calls some container might call, right? So, now you're blocking requests for users"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [15:21](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=921s)

> "containers interact with the same host kernel, so they do they do have some protections, but at the end it's the same host kernel they're trying to attack"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [16:00](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=960s)

> "you first exploit a problem in the sentry or the gofer, and then you exploit from the gofer to the kernel, right? You can still get to the host kernel eventually."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [17:21](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1041s)

> "ring zero gives the guest kernel full control inside the guest, but no control on the host. So, you can exploit the guest all you want, but the host is still protected."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [19:25](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1165s)

> "There's a performance penalty you pay every time the CPU is switching back and forth between these two modes."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [19:25](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1165s)

> "historically, many, many escape attacks were attacking the devices written in C"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [23:26](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1406s)

> "it has nothing to do with what's running inside the guest. It's It's everything to do with the VMM itself."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [24:06](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1446s)

> "system tricks can cover performance issues, but they cannot hide security breaches. And as a company, you can lose trust once and it's like very hard to regain."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [28:24](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1704s)

> "in the end, everyone always wants a VM because they tried everything. They tried containers, G visor, V8s."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [29:03](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1743s)

> "if you're a startup or a founder like in this space, like let me save you the story and two years of grief. Just please use micro VMs from the start."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [29:03](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1743s)

> "counterintuitively, persistence actually helps reliability and scale. They might seem like orthogonal concepts, but but they're very much related."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [31:29](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=1889s)

> "if I have to save gigabytes of data at every turn, like like I'm going to bankrupt the company and like it's just a slow experience regardless"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [33:33](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2013s)

> "I can actually lie to you while I'm uploading to the cloud. So, the snapshot can happen return very fast as I'm uploading in the background."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [39:20](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2360s)

> "NFS, for instance, isn't as performant and is not POSIX-compliant. And I think our models are just very good at anything POSIX compliant and standard."
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [39:57](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2397s)

> "storage is the next unlock here. As you're working on sandboxes, think of what what all you can snapshot and restore fast"
>
> — [From fork() to Fleet: Designing an Agent Sandbox Cloud](../talks/from-fork-to-fleet-designing-an-agent-sandbox-cloud.md), [41:18](https://www.youtube.com/watch?v=OqM67QG_Ikk&t=2478s)

