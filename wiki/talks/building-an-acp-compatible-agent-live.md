---
title: "Building an ACP-Compatible Agent Live"
type: "talk"
slug: "building-an-acp-compatible-agent-live"
org: "Zed"
video_id: "HsxQICTLF84"
duration_sec: 1099
word_count: 2822
speakers: ["Bennet Fenner"]
---

# Building an ACP-Compatible Agent Live

**Speakers:** [Bennet Fenner](../speakers/bennet-fenner.md)

**Org:** Zed

**Duration:** 18m 19s

[Watch on YouTube](https://www.youtube.com/watch?v=HsxQICTLF84)

## Summary

Bennet Fenner of Zed introduces the Agent Client Protocol (ACP), a JSON-RPC protocol that lets any coding agent talk to any editor or client through a unified interface — analogous to LSP or MCP but for agent front-ends. Motivated by the 2025 wave of model-provider CLI agents (Claude Code, Codex, Gemini CLI), Zed built ACP so users could bring their agent of choice into a consistent UI. The bulk of the talk is a live coding session that takes a bare-bones TypeScript agent with only read-file and edit-file tools and makes it ACP-compatible in about 15 minutes, implementing initialize, authenticate, newSession, and prompt, then layering on streaming session updates, tool-call status updates, ACP-proxied file system access, and terminal support. Worth watching if you want a concrete, minimal picture of what the protocol actually requires rather than a spec walkthrough — including the honest bits where the demo half-broke on stage. Ends with the practical detail that ACP currently runs over stdio, with remote transport in progress.

## Key Points

- ACP is a JSON-RPC-based protocol, open source and modeled after LSP/MCP, that lets agents and clients communicate through a unified interface so users can bring their agent of choice to any editor.
- Adoption is already broad: agents support it either natively (open code, cursor CLI ACP mode) or via adapters that translate the agent's native protocol, and roughly 40 clients implement it including JetBrains, Obsidian, and open claw.
- A minimal ACP agent requires implementing only four functions: initialize (respond with supported protocol version and capabilities), authenticate, newSession, and prompt.
- Sessions are the core abstraction — each thread in a client maps to a session ID, which the agent generates and the client passes back on every prompt request.
- Streaming output is delivered via session updates, which are notifications rather than request/response pairs and can be sent at any time; the agent message chunk type carries streamed model text.
- Tool calls follow a two-phase pattern: emit a session update of type tool call with title, status in progress, and optional file locations, then emit tool call update messages to set final status and return content.
- ACP proxies file system access — the client can advertise a file system capability so the agent reads through ACP instead of fs.readFile, which matters in an editor because unsaved buffer changes are not on disk but the agent should still see them.
- Clients can also advertise a terminal capability, letting the client create and manage terminals on the agent's behalf; the speaker used his own agent to write its terminal tool live.
- Diffs are a first-class ACP content type: the agent sends old text and new text and the client (Zed) renders the diff itself.
- The transport today is standard IO, with remote transport being worked on by JetBrains contributors.

## Notable Quotes

> "at Zed, we asked ourselves like how can we let users bring their agent of choice to our tool and enjoy like a nice interface that is unified across all of them"
>
> — [0:14](https://www.youtube.com/watch?v=HsxQICTLF84&t=14s) &middot; *states the motivating problem ACP was designed to solve*

> "And so that's why we decided we need some kind of type of protocol uh called agent client protocol, uh which is similar to like MCP or uh LSP."
>
> — [0:14](https://www.youtube.com/watch?v=HsxQICTLF84&t=14s) &middot; *positions ACP relative to the protocols the audience already knows*

> "It's a JSON RPC based protocol. And the idea is basically that uh agents and clients can talk to each other through through a unified interface."
>
> — [0:54](https://www.youtube.com/watch?v=HsxQICTLF84&t=54s) &middot; *the one-sentence definition of the protocol*

> "And we also have a bunch of uh clients at this point up to 40 that uh implement this including open claw for example."
>
> — [0:54](https://www.youtube.com/watch?v=HsxQICTLF84&t=54s) &middot; *the only adoption number in the talk*

> "here's a very minimal coding agent that just doesn't support ACP, but it's kind of the bare minimum you need to like build a coding agent"
>
> — [1:42](https://www.youtube.com/watch?v=HsxQICTLF84&t=102s) &middot; *sets the baseline the whole live demo builds from*

> "So, all it has is really like two tools. One to read a file and one to edit an existing file."
>
> — [2:27](https://www.youtube.com/watch?v=HsxQICTLF84&t=147s) &middot; *concrete claim about how little surface area a coding agent needs*

> "that is kind of like the way all agents basically work is the model APIs are stateless"
>
> — [2:27](https://www.youtube.com/watch?v=HsxQICTLF84&t=147s) &middot; *the architectural premise underlying the agent loop*

> "So, now the question is how do we make this thing ACP compatible? And hopefully we can do it in 10 minutes."
>
> — [3:41](https://www.youtube.com/watch?v=HsxQICTLF84&t=221s) &middot; *frames the talk's implicit claim that ACP integration is cheap*

> "And then you have to at minimum implement these three uh four functions."
>
> — [4:19](https://www.youtube.com/watch?v=HsxQICTLF84&t=259s) &middot; *quantifies the minimum implementation burden*

> "So, basically every time you start a thread in Zed or in a different editor or client, uh you you call a new session."
>
> — [5:02](https://www.youtube.com/watch?v=HsxQICTLF84&t=302s) &middot; *defines the session abstraction in client-facing terms*

> "And then you can send updates kind of like notifications to the client that are not like a usual request response, right?"
>
> — [8:33](https://www.youtube.com/watch?v=HsxQICTLF84&t=513s) &middot; *names the key asymmetry in ACP's message model*

> "you have to emit like a tool call, like session update of type tool call, and then once once the client knows about it, uh you can emit updates for that"
>
> — [11:31](https://www.youtube.com/watch?v=HsxQICTLF84&t=691s) &middot; *spells out the two-phase tool-call protocol*

> "But MC uh ACP actually proxies the file system too. Like the client can provide a uh a file system capability"
>
> — [12:11](https://www.youtube.com/watch?v=HsxQICTLF84&t=731s) &middot; *introduces one of ACP's least obvious design decisions*

> "if I have unsafe changes in my buffer, they're not actually on the file system, but the agent should still see them"
>
> — [12:11](https://www.youtube.com/watch?v=HsxQICTLF84&t=731s) &middot; *the concrete justification for filesystem proxying (auto-caption garble of 'unsaved')*

> "Okay, something is going wrong because everything is duplicated."
>
> — [12:49](https://www.youtube.com/watch?v=HsxQICTLF84&t=769s) &middot; *honest live-demo failure worth knowing about before watching*

> "the client can um advertise that it supports creating terminal and managing terminals for the agent"
>
> — [15:02](https://www.youtube.com/watch?v=HsxQICTLF84&t=902s) &middot; *describes the terminal capability handoff between client and agent*

> "so that's how you kind of build an ACP compatible coding agent in 15 minutes or so"
>
> — [16:38](https://www.youtube.com/watch?v=HsxQICTLF84&t=998s) &middot; *the talk's summary claim about integration cost*

> "in case anyone wants the demo code, but please don't use it in production. It's all agent generated."
>
> — [16:38](https://www.youtube.com/watch?v=HsxQICTLF84&t=998s) &middot; *candid caveat on the demo artifact*

> "in ACP there are multiple content types, and one content type is diff, and so the agent sends old text, new text, and then Z does the diffing for you"
>
> — [16:38](https://www.youtube.com/watch?v=HsxQICTLF84&t=998s) &middot; *answers where diff rendering responsibility sits*

> "the connection works over standard IO. Uh there are some folks well, I think from the JetBrains people are working on like remote uh transport"
>
> — [17:36](https://www.youtube.com/watch?v=HsxQICTLF84&t=1056s) &middot; *states the current transport limitation and what's coming*

## Positions

- The proliferation of provider-specific CLI coding agents created a need for a unified agent-client protocol, analogous to LSP for language tooling. ([0:14](https://www.youtube.com/watch?v=HsxQICTLF84&t=14s), confidence: stated)
- ACP already has roughly 40 client implementations, including JetBrains, Obsidian, and open claw. ([0:54](https://www.youtube.com/watch?v=HsxQICTLF84&t=54s), confidence: stated)
- A functional coding agent needs only two tools — read file and edit file — as its bare minimum. ([2:27](https://www.youtube.com/watch?v=HsxQICTLF84&t=147s), confidence: stated)
- Because model APIs are stateless, every agent works the same way: resend the conversation, get a message or tool call, execute locally, loop. ([2:27](https://www.youtube.com/watch?v=HsxQICTLF84&t=147s), confidence: stated)
- Making an existing agent ACP-compatible requires implementing only four functions and can be done in roughly 15 minutes. ([16:38](https://www.youtube.com/watch?v=HsxQICTLF84&t=998s), confidence: stated)
- Agents should read files through ACP's proxied filesystem rather than native fs APIs, because the client may hold unsaved buffer state the agent needs to see. ([12:49](https://www.youtube.com/watch?v=HsxQICTLF84&t=769s), confidence: stated)
- Diff rendering belongs on the client side: the agent sends only old text and new text, and the client computes and displays the diff. ([16:38](https://www.youtube.com/watch?v=HsxQICTLF84&t=998s), confidence: stated)
- Letting the client own terminal creation and management, rather than the agent, is the better default because it adds interactivity to the editor UI. ([15:49](https://www.youtube.com/watch?v=HsxQICTLF84&t=949s), confidence: implied)
- ACP currently only supports standard IO transport; remote transport is not yet available. ([17:36](https://www.youtube.com/watch?v=HsxQICTLF84&t=1056s), confidence: stated)
- Agent-generated code such as this demo should not be used in production. ([16:38](https://www.youtube.com/watch?v=HsxQICTLF84&t=998s), confidence: stated)

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [session management](../concepts/session-management.md)

