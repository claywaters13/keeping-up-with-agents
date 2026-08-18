---
title: "Codex, Behind the Harness"
type: "talk"
slug: "codex-behind-the-harness"
track: "Agentic Engineering"
org: "OpenAI"
day: "Day 4 — Session Day 3"
room: "Track 8"
video_id: "shRR1e2HXMk"
duration_sec: 1254
word_count: 3727
speakers: ["Dominik Kundel"]
---

# Codex, Behind the Harness

**Speakers:** [Dominik Kundel](../speakers/dominik-kundel.md)

**Org:** OpenAI

**Track:** Agentic Engineering &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 20m 54s

[Watch on YouTube](https://www.youtube.com/watch?v=shRR1e2HXMk)

## Summary

Dominik Kundel of OpenAI walks through the internals of the Codex harness — the open-source Rust agent runtime behind Codex — covering how it constructs context, executes actions, sandboxes them, and manages long-running loops. The core argument is that most of what makes Codex distinctive is not proprietary harness magic but capabilities exposed directly in the Responses API (tool search with deferred tools, apply patch, WebSocket transport, server-side compaction), so builders can adopt them in their own agents. He details concrete design decisions: capping the skills list at 2% of the context window, deferring tools out of the prompt, using a read-only auto-review subagent to cut approval fatigue without granting blanket full access, and scripting browser interactions via a persistent Node REPL with Playwright instead of one-action-at-a-time computer use. He also reports that once inference hit 1,000 tokens/sec on Cerebras with GPT-5.3 Codex Spark, the network — not the model — became the bottleneck, motivating a stateful WebSocket mode. Worth watching if you build agents and want a concrete, current reference implementation of harness-level tradeoffs.

## Key Points

- The Codex harness and app server are open source (Apache 2 / MIT) and written in Rust, and are usable both as a blueprint and as a runtime other UIs can build on via the app server protocol.
- Context construction optimizes for three things — size, flexibility across variable skill/MCP counts, and cacheability — with the skills list hard-capped at 2% of the maximum context window.
- Deferred tools keep MCP and other tool definitions out of the prompt entirely; since GPT-5.4 any tool can be marked deferred and surfaced later through tool search, either OpenAI's built-in one or your own.
- Async actions (sub-agents and background terminals) are handled with a spawn-agent tool plus a send-input tool that can push data, wait, or shut the child down.
- Computer use has shifted from a limited one-action-at-a-time API to code execution: Codex's browser use writes Playwright JavaScript against a persistent Node REPL, letting it script repeated interactions like scraping instead of clicking step by step.
- Recent GPT-5-family models are trained on an apply-patch tool for edits, on Ripgrep for search (which Codex ships in case you lack it), and on PowerShell natively for Windows.
- Sandboxing uses Seatbelt on macOS and Bubblewrap on Linux; Windows required OpenAI to build and open-source its own sandbox.
- Auto-review addresses approval fatigue with a read-only, non-recursive subagent that judges escalated actions using the transcript, tool calls, user authorization level, and a risk taxonomy — auto-approving low-risk actions while still blocking data exfiltration.
- At 1,000 tokens/sec inference, the network became the bottleneck, so Responses moved to a stateful WebSocket mode that sends only changed items rather than the whole item list each turn.
- The /goal loop works by injecting a continuation prompt containing the objective until the model calls an update-goal tool, which is why goals should be short and verifiable rather than long essays.

## Notable Quotes

> "the Codex harness and everything I'm showing you is actually open source. Uh it's MIT it's Apache 2 license and the harness is written in Rust."
>
> — [0:46](https://www.youtube.com/watch?v=shRR1e2HXMk&t=46s) &middot; *Establishes the talk's premise that everything described is inspectable and forkable.*

> "the more context you have in your in your context, the higher it is that you have contradicting information and it causes confusion for the model."
>
> — [4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s) &middot; *States the quality (not just cost) rationale for aggressive context trimming.*

> "for available skills, we actually cap the available skills list at 2% of your context total like maximum context window."
>
> — [6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s) &middot; *A concrete, copyable budget number for skill descriptions.*

> "we're marking some of these tools as deferred, and that means that they're not added directly to the context window, but instead are available through tool search later on."
>
> — [6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s) &middot; *Defines deferred tools, the main answer to MCP-driven context bloat.*

> "Since GPT-5.4, you can mark any tool as deferred loading."
>
> — [6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s) &middot; *Pins the capability to a specific model version and makes it available outside Codex.*

> "an agent really only becomes an agent if it performs actions"
>
> — [6:44](https://www.youtube.com/watch?v=shRR1e2HXMk&t=404s) &middot; *The pivot from context design to action design, stated as a definition.*

> "what happens when uh Codex uses browser use is it actually interacts with a persistent node repl that gets persisted throughout different uh throughout the turns."
>
> — [8:57](https://www.youtube.com/watch?v=shRR1e2HXMk&t=537s) &middot; *Reveals the actual mechanism behind browser use — a persistent REPL, not a click API.*

> "all of the recent models starting with GPT-5 have been trained on the concept of an apply patch tool to do file editing"
>
> — [9:37](https://www.youtube.com/watch?v=shRR1e2HXMk&t=577s) &middot; *Model training shapes which edit tool a harness should expose.*

> "we're actually in the Codex harness shipping Ripgrep with uh with the harness if you don't have it installed on your own."
>
> — [10:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=633s) &middot; *Illustrates harnesses adapting to model habits formed in training.*

> "on macOS, we use Seatbelt for that, similar to most agents. And on Linux, we use Bubblewrap."
>
> — [11:15](https://www.youtube.com/watch?v=shRR1e2HXMk&t=675s) &middot; *Names the concrete sandbox primitives per platform.*

> "you asking a model to send out a file to through an email, pushing it to have high agency, and it realizes it can't attach the file, so it uploads it to a file share"
>
> — [12:30](https://www.youtube.com/watch?v=shRR1e2HXMk&t=750s) &middot; *A vivid failure mode showing why full-access mode remains risky despite better models.*

> "this subagent runs entirely separate and can't spin up other subagents and has read permissions only."
>
> — [13:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=785s) &middot; *Specifies the containment guarantees of the auto-review judge.*

> "in some cases you want the agent to actually delete a file. In other cases you don't."
>
> — [14:25](https://www.youtube.com/watch?v=shRR1e2HXMk&t=865s) &middot; *Justifies context-aware approval over static permission rules.*

> "we uh launched GPT 5.3 Codex Spark, uh and it's running on Cerebras at 1,000 tokens per second."
>
> — [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s) &middot; *Reports the throughput number that triggered the transport rework.*

> "with all of these tool calls and the interactions, inference wasn't no longer was no longer the bottleneck. It was actually the network."
>
> — [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s) &middot; *The talk's sharpest architectural claim about where agent latency now lives.*

> "the responses API doesn't run through service-side events and HTTP, but instead uses uses a persistent WebSocket connection"
>
> — [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s) &middot; *Names the specific protocol change and its stateful payoff.*

> "we continue to do this until the model itself calls an update plan update goal tool, which specifies that the plan was actually or the goal was actually achieved."
>
> — [17:56](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1076s) &middot; *Demystifies the /goal loop termination condition.*

> "that is the reason why you actually don't want to, you know, write full essays like I know a lot of you have been trying to um into your goal, but instead have very concrete and very fiable um prompts"
>
> — [17:56](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1076s) &middot; *Direct, actionable prompting advice derived from the loop mechanism.*

> "we introduced uh end end of last year auto compaction, and this has been uh used by Codex since then to automatically trigger compaction on the server side in a way that the model got trained with so that the performance stays the same."
>
> — [18:49](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1129s) &middot; *Argues compaction should be trained-in and server-side rather than harness-improvised.*

> "most of the features that are stand out for Codex are actually features that are exposed in the responses API."
>
> — [19:34](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1174s) &middot; *The talk's closing thesis for builders of other harnesses.*

## Positions

- Oversized context hurts agent quality, not just cost, because more content raises the chance of contradicting information confusing the model. ([4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s), confidence: stated)
- Skill descriptions should be budgeted as a fraction of the context window — Codex caps them at 2% and progressively truncates descriptions beyond that. ([6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s), confidence: stated)
- Tools should be lazily discoverable via tool search rather than all loaded into the context window up front. ([6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s), confidence: stated)
- Code execution against a persistent REPL is a better computer-use primitive than a one-action-at-a-time tool API, because the agent can script repeated interactions. ([8:06](https://www.youtube.com/watch?v=shRR1e2HXMk&t=486s), confidence: stated)
- Harnesses should conform to what the model was trained on — apply patch for edits, Ripgrep for search, PowerShell on Windows — rather than inventing their own interfaces. ([9:37](https://www.youtube.com/watch?v=shRR1e2HXMk&t=577s), confidence: implied)
- Existing Windows sandboxing options were inadequate, so OpenAI had to build its own open-source Windows sandbox. ([11:15](https://www.youtube.com/watch?v=shRR1e2HXMk&t=675s), confidence: stated)
- Full-access mode remains unsafe even with better models, because pushing a model toward high agency can produce actions that diverge from user intent. ([12:30](https://www.youtube.com/watch?v=shRR1e2HXMk&t=750s), confidence: stated)
- Approval decisions require the task context — the same action, such as deleting a file, is acceptable or not depending on whether the user asked for it. ([14:25](https://www.youtube.com/watch?v=shRR1e2HXMk&t=865s), confidence: stated)
- At ~1,000 tokens/sec inference, network overhead rather than inference is the dominant bottleneck in agent loops. ([15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s), confidence: stated)
- A stateful WebSocket connection that transmits only changed items significantly outperforms server-sent events over HTTP for agent traffic. ([16:21](https://www.youtube.com/watch?v=shRR1e2HXMk&t=981s), confidence: stated)
- Goal prompts should be concrete and verifiable rather than long essays, because the loop only ends when the model can detect the goal is achieved. ([17:56](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1076s), confidence: stated)
- Compaction should happen server-side in the form the model was trained on so that performance stays the same after compaction. ([18:49](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1129s), confidence: stated)
- Builders don't need the Codex harness to get its main advantages, since tool search, apply patch, WebSockets, and server-side compaction are all exposed in the Responses API. ([19:34](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1174s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [automation bias](../concepts/automation-bias.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [context compaction](../concepts/context-compaction.md)
- [context engineering](../concepts/context-engineering.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [latency budgets](../concepts/latency-budgets.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)
- [tool selection](../concepts/tool-selection.md)

