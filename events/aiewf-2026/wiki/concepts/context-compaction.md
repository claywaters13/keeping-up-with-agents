---
title: "context compaction"
type: "concept"
slug: "context-compaction"
tier: "core"
maturity: "contested"
talk_count: 20
speaker_count: 26
---

# context compaction

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **20** talk(s) by **26** speaker(s)

**Definition:** Techniques for shrinking accumulated context — summarizing, trimming, or rewriting history — so an agent can keep running past what would otherwise be a full window.

*Also referred to as: context compression, context summarization, rolling summarization, conversation history trimming, knowledge-based compaction, context summarization per turn*

## State of Practice

Compaction has moved from a client-side hack to a first-class architectural decision, and the field split over it at this conference. One camp reports that summarization-based compaction now works well enough to be invisible — OpenAI ships auto-compaction server-side in the form the model was trained on so post-compaction performance is unchanged, and practitioners report threads weeks old with hundreds of subagents that still know what they are doing. The opposing camp treats destructive compaction as an anti-pattern: because a compaction step discards everything it did not summarize, they back the agent with an append-only session log or plain files on disk, and treat any compacted view as a lossy fork off that durable record rather than as the state itself. Both camps agree on the underlying physics: a full context window degrades answer quality because contradictory content confuses the model, so several speakers recommend staying under ~200K tokens (ideally under 100K) regardless of advertised window size, capping skill/tool description blocks at ~2% of the window, and deferring the rest to tool search. Where the two camps land determines whether you build recall over summaries or recall over raw logs. A widely-missed detail: compaction is not primarily a cost optimization — rewriting the prefix forces a KV-cache miss, so the next call's input tokens cost roughly 10x, and the real justification is intelligence.

## Consensus

### Durable state outside the context window — an append-only session log or files on disk — is what makes compaction survivable; the context window should be a rebuildable projection, not the system of record.

Support: **5** talk(s)

> "The state lives in files. It is not trapped inside one model. And this is the single most practical thing I learned all year."
>
> — [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### A large context window is not free capacity — filling it degrades answer accuracy, so limiting what enters context is a quality decision, not only a cost decision.

Support: **4** talk(s)

> "the more context you have in your in your context, the higher it is that you have contradicting information and it causes confusion for the model."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

### Compaction is lossy: whatever the summarizer does not retain is permanently gone unless a separate mechanism can fetch it back.

Support: **4** talk(s)

> "Compaction is lossy. A compacted summary is not going to perfectly reproduce the state of the agent in a smaller form. It's actually going to throw information away."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [4:47](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=287s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

### If you must shrink history in-band, summarize what falls out of the window rather than plainly truncating to the most recent N messages.

Support: **3** talk(s)

> "we found that having some sort of um rolling summarization was more effective than you know always stuffing in the latest and most recent uh messages"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [12:12](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=732s)

Supporting talks: [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)

## Disagreements

### Should long-horizon agents compact their history, or should they never compact and instead reset onto a durable external record?

| Position A | Position B |
|---|---|
| Compaction is the right primitive and has crossed the quality bar: run rolling summarization (or server-side auto-compaction) and keep the same thread running for weeks; the old advice to start a fresh thread after a long conversation is obsolete.<br>*[Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)* | Destructive compaction is the wrong default because you cannot choose what survives and what it drops is gone; instead keep an append-only immutable session log (or self-written handoff files), clear the context entirely, and let the model re-read what it needs — any compacted view is a best-effort fork, not the state.<br>*[Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)* |

*Why it matters: It decides whether your agent's identity lives in a mutable rolling summary or in an immutable event log, which in turn determines whether you can fork, migrate providers, resume after a crash, or audit how an answer was reached.*

### Where should compaction execute — inside the harness, or server-side in the model provider's stack?

| Position A | Position B |
|---|---|
| Compaction belongs server-side, performed in the exact form the model was trained on, so measured performance is unchanged across the compaction boundary; this is exposed as an API primitive precisely so builders stop rolling their own.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* | Compaction is harness-level application logic the team owns: rolling summarization with a truncated recent window and recall over the summary, sliding-window conversation managers with summarized overflow, or an explicit /compact triggered at a token threshold such as 150K.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)* |

*Why it matters: Harness-side compaction gives you control over what survives but drifts out of the model's training distribution and can silently degrade after a model upgrade; server-side compaction preserves performance but hands the provider your history and removes your ability to choose what is retained.*

### Is compaction a cost optimization?

| Position A | Position B |
|---|---|
| No — compacting rewrites the prefix and forces a KV-cache miss, so the following call pays roughly 10x on input tokens; the actual reason to compact is intelligence, and cost is better attacked by staying under 100-200K tokens and reusing cache via a long-lived sidekick context.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md)* | Shrinking what you send is the main cost lever available, since roughly 90% of agent spend is input tokens: cache the system prompt, trim and summarize conversation history, keep large tool results out of context, and retrieve narrow slices instead of whole files.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)* |

*Why it matters: If compaction is cache-hostile, aggressive context trimming can raise your bill while appearing to lower it, and the right optimization shifts from summarizing history to preserving a stable cacheable prefix.*

## Practical Guidance

**Do:**

- Back the agent with an append-only, immutable event log (or files on disk) so compaction, a harness crash, or a dead sandbox never destroys recoverable state
- Treat a compacted context as a best-effort lossy fork resumed as a new log, and retain the raw log alongside it
- Pair rolling summarization with recall: let the model query back into the summary and the discarded history rather than only reading the newest messages
- Cap the available-skills/tool-description block at 2% of the total context window and mark remaining tools as deferred, discoverable via tool search
- Keep working context under ~200K tokens, ideally under 100K, regardless of the advertised context window
- Trigger compaction at a threshold (around 150K tokens) rather than riding the window to exhaustion and branching on stop_reason so truncated output is not silently accepted
- Run compaction server-side in the form the model was trained on when the provider exposes it, so post-compaction performance is measurably unchanged
- Extract atomic facts from conversations with a continually adapting relevance scorer (knowledge-based compaction) instead of storing everything and compacting only on overflow
- Move verification and grading into a separate context window from the one that did the work
- Store large tool results outside the context and pass back a summary or handle instead of re-sending them every loop iteration
- Give subagents only the claim and evidence, and keep their full output out of the primary thread
- Run an out-of-band consolidation ('dreaming') pass over transcripts plus memory state to correct memories that were locally optimal when written in-band
- Budget for the KV-cache miss that compaction causes — prefer one long-lived sidekick context with a running cache over spawning fresh subagents

**Avoid:**

- Filling a million-token window just because it exists — more context means more contradicting information and a less accurate answer
- Naive destructive compaction that silently discards everything it did not summarize with no path to fetch it back
- Letting every subtask dump its full output into the primary thread, crowding out the parent context
- Assuming compaction is a cost win — rewriting the prefix invalidates the cache and can raise input cost roughly 10x on the next call
- Sliding-window truncation with no summarization of what falls off the front, which quietly loses the beginning of the conversation
- Prescribing an explicit memory schema for the model; specifying memory structure up front measurably drops performance versus letting the model manage its own
- Self-grading in the same context window that produced the work, which yields confabulation and odd artifacts
- Clever model-side memory injection that breaks KV-cache reuse
- Prompt instructions asking the model to use less context — the context is already transmitted and billed before the prompt is read
- Carrying harness-side context workarounds forward after a model upgrade; fixes for context anxiety became pure overhead and cache bugs once Opus 4.5 no longer had the problem

## Notable Outliers

- Compaction now works well enough that threads five weeks old containing 400 subagents still know what to do — the standing advice to start a new thread after ~20 messages or per feature is no longer true. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [3:29](https://www.youtube.com/watch?v=il1c1a2FufU&t=209s))
- Stopped compacting entirely: it is slow, offers no control over what survives, and discards permanently — reset the context to zero instead and re-read self-written handoff and history files. ([I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s))
- RL should be applied to the compaction step itself, not just the task — generate to the end of the window, summarize, continue, and train the summarizer. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [10:42](https://www.youtube.com/watch?v=2bvtay8wGYI&t=642s))
- The main reason to compact is intelligence, not cost — compaction forces a cache miss so you pay roughly 10x more for those input tokens than if you hadn't compacted. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s))
- KV compaction is a dead end as a learning mechanism: it only applies to what fits in context and forfeits the generalization you get from taking gradients. ([Scaling Compute on Context](../talks/scaling-compute-on-context.md), [13:01](https://www.youtube.com/watch?v=WiqDvX6isc4&t=781s))
- In a traditional harness the context window and the session are treated as one and the same, and separating them is what makes the session log serve as observability, recovery, and memory substrate simultaneously. ([Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md), [14:33](https://www.youtube.com/watch?v=K0X9QDRkIdg&t=873s))

## All Talks

- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Data Quality Is the Compute Multiplier](../talks/data-quality-is-the-compute-multiplier.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)
- [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md)
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)
- [Scaling Compute on Context](../talks/scaling-compute-on-context.md)
- [Scaling to Long Horizons](../talks/scaling-to-long-horizons.md)
- [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)
- [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)
- [The Log Is The Agent](../talks/the-log-is-the-agent.md)
- [The State of Model Routing](../talks/the-state-of-model-routing.md)
- [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)
- [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)
- [Your Voice Agent Doesn't Need a Frontier Model](../talks/your-voice-agent-doesnt-need-a-frontier-model.md)

## Speakers

- [Alex Atallah](../speakers/alex-atallah.md)
- [Alexander Embiricos](../speakers/alexander-embiricos.md)
- [Ari Morcos](../speakers/ari-morcos.md)
- [Chengxi Taylor](../speakers/chengxi-taylor.md)
- [Dat Ngo](../speakers/dat-ngo.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Gagan Bhat](../speakers/gagan-bhat.md)
- [Isabella Kai He](../speakers/isabella-kai-he.md)
- [Ishaan Sehgal](../speakers/ishaan-sehgal.md)
- [Jack Morris](../speakers/jack-morris.md)
- [Jason Liu](../speakers/jason-liu.md)
- [Kyle Jaejun Lee](../speakers/kyle-jaejun-lee.md)
- [Lance Martin](../speakers/lance-martin.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Paul Iusztin](../speakers/paul-iusztin.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Ross Taylor](../speakers/ross-taylor.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)
- [Walden Yan](../speakers/walden-yan.md)

