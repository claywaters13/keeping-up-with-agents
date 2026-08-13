---
title: "Dominik Kundel"
type: "speaker"
slug: "dominik-kundel"
role: "Developer Experience Lead"
company: "OpenAI"
talk_count: 1
---

# Dominik Kundel

**Developer Experience Lead &middot; OpenAI**

Dominik Kundel works on Developer Experience at OpenAI, where he helps builders get the most out of Codex and the OpenAI APIs. His work has spanned the Agents SDK, GPT-OSS, and most recently Codex. Before OpenAI, he led Product & Design for Twilio’s Emerging Tech & Innovation team, working on developer tools and customer-aware AI agents. Dominik has spent more than a decade in developer tools, usually across APIs, CLIs, JavaScript, and strange demos. Outside work, he’s probably tinkering with cocktails, food, photography, or something that should not need JavaScript but somehow does.

[LinkedIn](https://linkedin.com/in/dkundel)

## Talks

- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md) (Agentic Engineering)

## Scheduled Sessions

- **Building on the Codex Harness** &middot; Day 3 — Session Day 2 &middot; 3:45pm-4:05pm &middot; Expo Stage 2 NW
- **Codex, Behind the Harness** &middot; Day 4 — Session Day 3 &middot; 1:30pm-1:50pm &middot; Track 8

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

## Quotes

> "the Codex harness and everything I'm showing you is actually open source. Uh it's MIT it's Apache 2 license and the harness is written in Rust."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [0:46](https://www.youtube.com/watch?v=shRR1e2HXMk&t=46s)

> "the more context you have in your in your context, the higher it is that you have contradicting information and it causes confusion for the model."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s)

> "for available skills, we actually cap the available skills list at 2% of your context total like maximum context window."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s)

> "we're marking some of these tools as deferred, and that means that they're not added directly to the context window, but instead are available through tool search later on."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s)

> "Since GPT-5.4, you can mark any tool as deferred loading."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [6:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=365s)

> "an agent really only becomes an agent if it performs actions"
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [6:44](https://www.youtube.com/watch?v=shRR1e2HXMk&t=404s)

> "what happens when uh Codex uses browser use is it actually interacts with a persistent node repl that gets persisted throughout different uh throughout the turns."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [8:57](https://www.youtube.com/watch?v=shRR1e2HXMk&t=537s)

> "all of the recent models starting with GPT-5 have been trained on the concept of an apply patch tool to do file editing"
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [9:37](https://www.youtube.com/watch?v=shRR1e2HXMk&t=577s)

> "we're actually in the Codex harness shipping Ripgrep with uh with the harness if you don't have it installed on your own."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [10:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=633s)

> "on macOS, we use Seatbelt for that, similar to most agents. And on Linux, we use Bubblewrap."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [11:15](https://www.youtube.com/watch?v=shRR1e2HXMk&t=675s)

> "you asking a model to send out a file to through an email, pushing it to have high agency, and it realizes it can't attach the file, so it uploads it to a file share"
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [12:30](https://www.youtube.com/watch?v=shRR1e2HXMk&t=750s)

> "this subagent runs entirely separate and can't spin up other subagents and has read permissions only."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [13:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=785s)

> "in some cases you want the agent to actually delete a file. In other cases you don't."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [14:25](https://www.youtube.com/watch?v=shRR1e2HXMk&t=865s)

> "we uh launched GPT 5.3 Codex Spark, uh and it's running on Cerebras at 1,000 tokens per second."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s)

> "with all of these tool calls and the interactions, inference wasn't no longer was no longer the bottleneck. It was actually the network."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s)

> "the responses API doesn't run through service-side events and HTTP, but instead uses uses a persistent WebSocket connection"
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s)

> "we continue to do this until the model itself calls an update plan update goal tool, which specifies that the plan was actually or the goal was actually achieved."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [17:56](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1076s)

> "that is the reason why you actually don't want to, you know, write full essays like I know a lot of you have been trying to um into your goal, but instead have very concrete and very fiable um prompts"
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [17:56](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1076s)

> "we introduced uh end end of last year auto compaction, and this has been uh used by Codex since then to automatically trigger compaction on the server side in a way that the model got trained with so that the performance stays the same."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [18:49](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1129s)

> "most of the features that are stand out for Codex are actually features that are exposed in the responses API."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [19:34](https://www.youtube.com/watch?v=shRR1e2HXMk&t=1174s)

