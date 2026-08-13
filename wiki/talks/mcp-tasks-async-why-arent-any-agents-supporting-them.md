---
title: "MCP Tasks (async): Why Aren't Any Agents Supporting Them?"
type: "talk"
slug: "mcp-tasks-async-why-arent-any-agents-supporting-them"
track: "Context Engineering"
org: "Temporal"
day: "Day 3 — Session Day 2"
room: "Track 8"
video_id: "s4r6nk5WsZw"
duration_sec: 1434
word_count: 3982
speakers: ["Cornelia Davis"]
---

# MCP Tasks (async): Why Aren't Any Agents Supporting Them?

*Program title: MCP Tasks (async)/ Why the heck aren't any agents supporting MCP tasks/async?*

**Speakers:** [Cornelia Davis](../speakers/cornelia-davis.md)

**Org:** Temporal

**Track:** Context Engineering &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 23m 54s

[Watch on YouTube](https://www.youtube.com/watch?v=s4r6nk5WsZw)

## Summary

Cornelia Davis of Temporal explains why, despite MCP tasks (async, long-running tool calls) being specified in November, essentially no MCP clients support them — the V1 spec was marked experimental, is genuinely complex, and had two design flaws that made it painful to implement. She grounds the talk in a concrete purchase-order example where invoice processing runs as a long-running MCP tool with human-in-the-loop approval steps, and demos her own hand-built MCP client (a 'task tracker workflow') surviving servers being down mid-flight. She walks through the V1 protocol's stateful `tasks/list` endpoint (unfilterable, doesn't scale past a million tasks) and its awkward long-lived-connection tunneling of `input_required` via `tasks/result`, then covers the July V2 changes: a stateless core, MCP restructured into core plus extensions with tasks as an extension, `tasks/list` removed, and a client-initiated update endpoint replacing elicitation-over-session. Useful if you're building async or durable MCP tooling and want a concrete read on what the spec demands, what changed, and what's still missing. She flags that even V2 doesn't scale to millions without the notifications protocol, and says she's working to land an implementation in FastMCP.

## Key Points

- MCP tasks let a client invoke a tool and receive a handle instead of a response, so the tool can run long in the background and be interacted with over time.
- The spec requires launched tasks to be durable: they must survive client crashes, server crashes, network drops, and humans disappearing on vacation, and remain interactable when infrastructure returns.
- V1's `tasks/list` endpoint made the protocol stateful and shipped with no filter, so recovering a task ID from a server holding a million tasks means paging through all of them.
- V1 tunneled `input_required` through `tasks/result` over a long-lived connection where the server elicits from the client, which is hard to implement and hard to resume after the connection dies.
- The July V2 spec goes stateless, restructures MCP into a core plus extensions with tasks as an extension, drops `tasks/list`, and adds a client-side update endpoint that behaves like a signal into a long-running process.
- Because `tasks/list` is gone, clients must persist task IDs themselves — the spec only says 'should', which Davis argues should be a MUST since an unpersisted ID is unrecoverable.
- Task lifecycle management (working → input_required → working → completed/canceled/failed) is unchanged between V1 and V2, and Davis considers that part of the design sound.
- Implementing a server means mapping the task lifecycle states onto your own domain state machine, which is where most of the real work sits.
- Even V2 doesn't scale to millions of tasks because every client polls its own tasks; the spec's unimplemented notifications protocol, offering a single 'has anything changed' endpoint, is the promising fix.

## Notable Quotes

> "the first answer to that question is, well, cuz they're smart. The people who are building those clients are smart. What I mean by that is that the MCP tasks specification that came out in November was marked as experimental."
>
> — [0:01](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1s) &middot; *The talk's thesis in one breath: non-adoption is a rational response, not laziness.*

> "MCP tasks are allowing you to have an MCP tool that you can invoke and then it is long-running in the background, and then eventually you can get back some response."
>
> — [3:30](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=210s) &middot; *Cleanest one-sentence definition of the feature.*

> "You're going to invoke a tool, and instead of getting back a response, you're going to get a handle."
>
> — [4:15](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=255s) &middot; *Names the core protocol shift precisely.*

> "the longer something runs, the more likely there's going to be some kind of infrastructure blip that's going to cause a problem in that long-running task"
>
> — [4:15](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=255s) &middot; *States the durability motivation as a general distributed-systems principle.*

> "This is verbage from the spec itself that says once you've locked launched a task it has to be durable."
>
> — [5:51](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=351s) &middot; *Anchors the durability requirement in the spec rather than opinion.*

> "Remember I said nobody's implemented this on the client side? Well, I created my own implementation here."
>
> — [9:27](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=567s) &middot; *Establishes that the demo is a from-scratch client, the talk's main artifact.*

> "Task list. This is a stateful protocol."
>
> — [12:22](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=742s) &middot; *Identifies the first of the two V1 flaws.*

> "Spoiler alert, there is no filter on that endpoint. So, you would have to go through a million tasks to find the one that you're looking for that you want to interact with."
>
> — [13:50](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=830s) &middot; *Concrete, checkable criticism of the V1 API surface.*

> "Just because you can doesn't mean you should."
>
> — [13:50](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=830s) &middot; *Compact verdict on the tasks/list design.*

> "this middle section has this weird protocol where you open a long-running connection and then the server elicits a response from the client. That gets super tricky."
>
> — [13:07](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=787s) &middot; *Names the second V1 flaw and why it blocks client implementers.*

> "back to the question of why the heck aren't there any clients that are supporting this protocol? Yeah. That's why. Super involved. It's still involved with V2, but it gets better."
>
> — [15:14](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=914s) &middot; *Answers the title question directly and refuses to oversell V2.*

> "one of the things that made me jump up and celebrate a little bit is that the protocol is going stateless. So, as somebody who's been working in the microservices world for a long time, stateful protocols are the absolute worst thing in large-scale distributed systems."
>
> — [15:56](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=956s) &middot; *Her strongest stated position, with the distributed-systems reasoning behind it.*

> "Task list has gone away. Good. Wasn't particularly useful anyway, especially at large scale."
>
> — [16:44](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1004s) &middot; *Concrete V1→V2 delta plus her judgment on it.*

> "if you remember a while ago, I showed you that screenshot that said Temporal has this notion of a signal. That's effectively what this is. It's a way of signaling into this long-running task."
>
> — [17:23](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1043s) &middot; *Frames the new V2 update endpoint against durable-execution primitives.*

> "I put the picture on the right-hand side here to emphasize the fact that the life cycle management of these tasks is unchanged. That's actually sound."
>
> — [17:23](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1043s) &middot; *Marks what she thinks the spec got right, balancing the critique.*

> "The spec right now says that clients should persist task IDs, but it also points out that if you don't persist task IDs, there is no way to get it back. So, I'm not quite sure why this doesn't have a an all caps must."
>
> — [19:05](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1145s) &middot; *A specific, actionable objection to V2's normative wording.*

> "with the V1 protocol, the reference implementation, if you had input required on multiple even though you can see that there's many of them in flight, on the client side they were FIFO. So, you could only respond to the first one."
>
> — [20:26](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1226s) &middot; *Reports a concrete limitation found in the reference implementation, not just the spec.*

> "even though this is better, it still doesn't scale to the millions. Why? Because if I've got a million tasks running, I've got a million clients that are doing gets against each and every one of those tasks. That does not scale."
>
> — [21:51](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1311s) &middot; *The main open problem she leaves the audience with.*

## Positions

- No MCP clients currently support MCP tasks, and that is a reasonable decision given the spec was marked experimental and is about to change substantially. ([0:01](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1s), confidence: stated)
- The MCP tasks specification requires that once a task is launched it must be durable and survive client, server, and network failures. ([5:51](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=351s), confidence: stated)
- V1's tasks/list endpoint made the protocol stateful and, lacking any filter, is unusable at scales of a million tasks. ([13:50](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=830s), confidence: stated)
- Stateful protocols are the worst thing you can have in large-scale distributed systems, so V2 going stateless is a major improvement. ([15:56](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=956s), confidence: stated)
- V1's mechanism of tunneling input_required through a long-lived tasks/result connection with server-to-client elicitation is a major barrier to client implementation. ([13:07](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=787s), confidence: stated)
- The task lifecycle model (working, input_required, completed, canceled, failed) is well designed and correctly left unchanged in V2. ([18:13](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1093s), confidence: stated)
- The V2 spec's 'should persist task IDs' ought to be a normative MUST, because an unpersisted task ID is permanently unrecoverable. ([19:05](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1145s), confidence: stated)
- The V1 reference client implementation handles input_required FIFO, so with multiple tasks in flight only the first can be responded to. ([20:26](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1226s), confidence: stated)
- Even the V2 protocol will not scale to millions of concurrent tasks under a per-client polling model; the notifications protocol is needed instead. ([21:51](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1311s), confidence: stated)
- Implementing MCP tasks correctly requires a durable workflow engine on both server and client sides, not just request/response handlers. ([21:05](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1265s), confidence: implied)

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [durable execution](../concepts/durable-execution.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [mcp server design](../concepts/mcp-server-design.md)
- [model context protocol](../concepts/model-context-protocol.md)

