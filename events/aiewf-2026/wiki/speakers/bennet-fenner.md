---
title: "Bennet Fenner"
type: "speaker"
slug: "bennet-fenner"
talk_count: 1
---

# Bennet Fenner

## Talks

- [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md) (Agent & Harness Engineering)

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [session management](../concepts/session-management.md)

## Quotes

> "at Zed, we asked ourselves like how can we let users bring their agent of choice to our tool and enjoy like a nice interface that is unified across all of them"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [0:14](https://www.youtube.com/watch?v=HsxQICTLF84&t=14s)

> "And so that's why we decided we need some kind of type of protocol uh called agent client protocol, uh which is similar to like MCP or uh LSP."
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [0:14](https://www.youtube.com/watch?v=HsxQICTLF84&t=14s)

> "It's a JSON RPC based protocol. And the idea is basically that uh agents and clients can talk to each other through through a unified interface."
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [0:54](https://www.youtube.com/watch?v=HsxQICTLF84&t=54s)

> "And we also have a bunch of uh clients at this point up to 40 that uh implement this including open claw for example."
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [0:54](https://www.youtube.com/watch?v=HsxQICTLF84&t=54s)

> "here's a very minimal coding agent that just doesn't support ACP, but it's kind of the bare minimum you need to like build a coding agent"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [1:42](https://www.youtube.com/watch?v=HsxQICTLF84&t=102s)

> "So, all it has is really like two tools. One to read a file and one to edit an existing file."
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [2:27](https://www.youtube.com/watch?v=HsxQICTLF84&t=147s)

> "that is kind of like the way all agents basically work is the model APIs are stateless"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [2:27](https://www.youtube.com/watch?v=HsxQICTLF84&t=147s)

> "So, now the question is how do we make this thing ACP compatible? And hopefully we can do it in 10 minutes."
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [3:41](https://www.youtube.com/watch?v=HsxQICTLF84&t=221s)

> "And then you have to at minimum implement these three uh four functions."
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [4:19](https://www.youtube.com/watch?v=HsxQICTLF84&t=259s)

> "So, basically every time you start a thread in Zed or in a different editor or client, uh you you call a new session."
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [5:02](https://www.youtube.com/watch?v=HsxQICTLF84&t=302s)

> "And then you can send updates kind of like notifications to the client that are not like a usual request response, right?"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [8:33](https://www.youtube.com/watch?v=HsxQICTLF84&t=513s)

> "you have to emit like a tool call, like session update of type tool call, and then once once the client knows about it, uh you can emit updates for that"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [11:31](https://www.youtube.com/watch?v=HsxQICTLF84&t=691s)

> "But MC uh ACP actually proxies the file system too. Like the client can provide a uh a file system capability"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [12:11](https://www.youtube.com/watch?v=HsxQICTLF84&t=731s)

> "if I have unsafe changes in my buffer, they're not actually on the file system, but the agent should still see them"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [12:11](https://www.youtube.com/watch?v=HsxQICTLF84&t=731s)

> "Okay, something is going wrong because everything is duplicated."
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [12:49](https://www.youtube.com/watch?v=HsxQICTLF84&t=769s)

> "the client can um advertise that it supports creating terminal and managing terminals for the agent"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [15:02](https://www.youtube.com/watch?v=HsxQICTLF84&t=902s)

> "so that's how you kind of build an ACP compatible coding agent in 15 minutes or so"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [16:38](https://www.youtube.com/watch?v=HsxQICTLF84&t=998s)

> "in case anyone wants the demo code, but please don't use it in production. It's all agent generated."
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [16:38](https://www.youtube.com/watch?v=HsxQICTLF84&t=998s)

> "in ACP there are multiple content types, and one content type is diff, and so the agent sends old text, new text, and then Z does the diffing for you"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [16:38](https://www.youtube.com/watch?v=HsxQICTLF84&t=998s)

> "the connection works over standard IO. Uh there are some folks well, I think from the JetBrains people are working on like remote uh transport"
>
> — [Building an ACP-Compatible Agent Live](../talks/building-an-acp-compatible-agent-live.md), [17:36](https://www.youtube.com/watch?v=HsxQICTLF84&t=1056s)

