---
title: "Cornelia Davis"
type: "speaker"
slug: "cornelia-davis"
role: "Principal Technologist"
company: "Temporal"
talk_count: 1
---

# Cornelia Davis

**Principal Technologist &middot; Temporal**

Cornelia's career has spanned several major shifts in software, from image processing algorithm development to web-centric computing in the late 90s, and then more than a decade working in cloud-native software, infrastructure and platforms (Cloud Foundry, Kubernetes and friends). Those experiences in distributed systems, combined with a longstanding interest in programming models, led her to Temporal where she is helping to bring a new programming paradigm to an industry that was increasingly in need of one - a need that has accelerated dramatically with the advent of modern AI systems. Much of her work today focuses on the architectural needs and evolving practices of these AI systems. Her current research explores asynchronous processing and the development of AI-native distributed systems abstractions, with an emphasis on the emerging patterns and programming models shaping this new era of software. She is the author of Cloud Native Patterns: Designing Change-Tolerant Software.

[LinkedIn](https://www.linkedin.com/in/corneliadavis/)

## Talks

- [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md) (Context Engineering)

## Scheduled Sessions

- **MCP Tasks (async)/ Why the heck aren't any agents supporting MCP tasks/async?** &middot; Day 3 — Session Day 2 &middot; 3:20pm-3:40pm &middot; Track 8

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [durable execution](../concepts/durable-execution.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [mcp server design](../concepts/mcp-server-design.md)
- [model context protocol](../concepts/model-context-protocol.md)

## Quotes

> "the first answer to that question is, well, cuz they're smart. The people who are building those clients are smart. What I mean by that is that the MCP tasks specification that came out in November was marked as experimental."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [0:01](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1s)

> "MCP tasks are allowing you to have an MCP tool that you can invoke and then it is long-running in the background, and then eventually you can get back some response."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [3:30](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=210s)

> "You're going to invoke a tool, and instead of getting back a response, you're going to get a handle."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [4:15](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=255s)

> "the longer something runs, the more likely there's going to be some kind of infrastructure blip that's going to cause a problem in that long-running task"
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [4:15](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=255s)

> "This is verbage from the spec itself that says once you've locked launched a task it has to be durable."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [5:51](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=351s)

> "Remember I said nobody's implemented this on the client side? Well, I created my own implementation here."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [9:27](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=567s)

> "Task list. This is a stateful protocol."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [12:22](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=742s)

> "Spoiler alert, there is no filter on that endpoint. So, you would have to go through a million tasks to find the one that you're looking for that you want to interact with."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [13:50](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=830s)

> "Just because you can doesn't mean you should."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [13:50](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=830s)

> "this middle section has this weird protocol where you open a long-running connection and then the server elicits a response from the client. That gets super tricky."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [13:07](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=787s)

> "back to the question of why the heck aren't there any clients that are supporting this protocol? Yeah. That's why. Super involved. It's still involved with V2, but it gets better."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [15:14](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=914s)

> "one of the things that made me jump up and celebrate a little bit is that the protocol is going stateless. So, as somebody who's been working in the microservices world for a long time, stateful protocols are the absolute worst thing in large-scale distributed systems."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [15:56](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=956s)

> "Task list has gone away. Good. Wasn't particularly useful anyway, especially at large scale."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [16:44](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1004s)

> "if you remember a while ago, I showed you that screenshot that said Temporal has this notion of a signal. That's effectively what this is. It's a way of signaling into this long-running task."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [17:23](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1043s)

> "I put the picture on the right-hand side here to emphasize the fact that the life cycle management of these tasks is unchanged. That's actually sound."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [17:23](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1043s)

> "The spec right now says that clients should persist task IDs, but it also points out that if you don't persist task IDs, there is no way to get it back. So, I'm not quite sure why this doesn't have a an all caps must."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [19:05](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1145s)

> "with the V1 protocol, the reference implementation, if you had input required on multiple even though you can see that there's many of them in flight, on the client side they were FIFO. So, you could only respond to the first one."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [20:26](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1226s)

> "even though this is better, it still doesn't scale to the millions. Why? Because if I've got a million tasks running, I've got a million clients that are doing gets against each and every one of those tasks. That does not scale."
>
> — [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [21:51](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1311s)

