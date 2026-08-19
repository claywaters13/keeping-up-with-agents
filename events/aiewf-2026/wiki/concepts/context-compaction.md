---
title: "context compaction"
type: "concept"
slug: "context-compaction"
tier: "core"
maturity: "contested"
talk_count: 21
speaker_count: 29
---

# context compaction

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **21** talk(s) by **29** speaker(s)

**Definition:** Techniques for shrinking accumulated context — summarizing, trimming, or rewriting history — so an agent can keep running past what would otherwise be a full window.

*Also referred to as: context compression, context summarization, rolling summarization, conversation history trimming, knowledge-based compaction, context summarization per turn*

## State of Practice

Compaction moved from a background implementation detail to one of the most actively argued design decisions in the agent stack, and the conference did not settle it. The clearest technical agreement is mechanical: compaction is lossy and it invalidates the prompt cache, so the compacted turn costs roughly an order of magnitude more per input token than the cached turn it replaced — meaning compaction has to be justified by intelligence or by a hard window limit, not by an assumption that fewer tokens are cheaper. The strongest architectural response, voiced by Anthropic, Omnara, and independent fleet operators, is to stop treating the context window as the agent's state at all: back the session with an append-only event log or on-disk files, and treat compaction as a best-effort lossy fork that can always fetch back what it dropped. OpenAI's counter-position is that compaction is now a solved provider primitive — Codex auto-compacts server-side in the form the model was trained on so performance holds across the boundary, which is what made five-week-old threads and persistent manager-agent workflows viable. Against both camps, the Towards AI team measured compaction presets against an untouched full history and found no-compaction won on recall, cost, and latency simultaneously, with distinctive facts still recalled at 800k tokens. What everyone rejects is naive uniform trimming: rolling summaries you can recall over, atomic-fact extraction, relevance-scored knowledge compaction, and out-of-context tool-result storage all beat dropping the oldest N messages.

## Consensus

### Compaction is irreversibly lossy, so the durable substrate must be something outside the context window — an append-only session log or files on disk — with the compacted view treated as a derived projection.

Support: **4** talk(s)

> "Compaction is lossy. A compacted summary is not going to perfectly reproduce the state of the agent in a smaller form. It's actually going to throw information away."
>
> — [The Log Is The Agent](../talks/the-log-is-the-agent.md), [4:47](https://www.youtube.com/watch?v=UPwGaM2MKHY&t=287s)

Supporting talks: [The Log Is The Agent](../talks/the-log-is-the-agent.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Evolution of agentic surfaces](../talks/evolution-of-agentic-surfaces.md)

### Compaction breaks the KV/prompt cache, and that cache miss is a first-order cost that has to be weighed against the token savings — compaction is not automatically cheaper.

Support: **3** talk(s)

> "you're actually then now like paying 10 times as much for the for those input tokens if you didn't compact. Um the main reason we compact is actually intelligence."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s)

Supporting talks: [The State of Model Routing](../talks/the-state-of-model-routing.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)

### Oversized context degrades answer quality, not just cost, because contradicting or irrelevant material confuses the model — so bound what enters the window rather than filling the advertised capacity.

Support: **4** talk(s)

> "the more context you have in your in your context, the higher it is that you have contradicting information and it causes confusion for the model."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [We Cut 94% of AI Coding Tokens With a Local Code Index](../talks/we-cut-94-of-ai-coding-tokens-with-a-local-code-index.md)

### Recency-based trimming is the wrong shrinking policy; selective retention — rolling summaries you can recall over, extracted atomic facts, or tool results moved to external storage — outperforms dropping the oldest messages.

Support: **4** talk(s)

> "we found that having some sort of um rolling summarization was more effective than you know always stuffing in the latest and most recent uh messages"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [12:12](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=732s)

Supporting talks: [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Turn 10,994 Notes Into Memory](../talks/turn-10994-notes-into-memory.md)

## Disagreements

### Should long-running agents compact by default, or only when a named constraint forces it?

| Position A | Position B |
|---|---|
| Compaction is now good enough to be the invisible default — it is what makes multi-week threads, persistent manager agents, and long-horizon tasks work at all, and the old advice to start a fresh thread is obsolete.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* | Do not compact by default. Keeping the full untouched history beat every compaction preset on recall, cost, and latency at once; compaction is slow, destroys what you didn't choose to keep, and should be replaced by a full reset plus re-read of durable files, or by an append-only log the model can fetch back from.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md), [The Log Is The Agent](../talks/the-log-is-the-agent.md)* |

*Why it matters: If compaction is the default, you build around a provider primitive and stop thinking about window management; if it isn't, you must build durable external state, retrieval, and an explicit trigger condition before your agent ever runs long. The two paths produce incompatible architectures and very different cost curves once caching is factored in.*

### Does long context actually degrade recall, or is 'context rot' overstated?

| Position A | Position B |
|---|---|
| Long context rots: quality falls as the window fills, so cap usable context well below the advertised window — never past ~200K tokens and ideally under 100K — and limit what goes in even with a million-token window available.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* | Long context does not necessarily rot: distinctive facts were recalled reliably up to 800k tokens with no compaction at all, and compacting first dropped answer rate to 32%. The real retrieval failure was dense semantic search, where BM25 held 100% recall as embeddings went to 0%.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: The entire justification for compaction rests on this. If long context holds up, compaction is a pure cost and cache regression you should skip; if it degrades, compaction buys accuracy and the cache miss is the price of correctness.*

### Should compaction be owned by the provider (server-side) or by the harness/operator?

| Position A | Position B |
|---|---|
| Compact server-side, in the exact form the model was trained on, so performance stays the same across the boundary — and expose it as an API primitive so every builder gets the same behavior the first-party harness gets.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [The Golden Age of AI Engineering](../talks/the-golden-age-of-ai-engineering.md)* | Own the compaction step yourself, because a provider-managed compactor gives you no control over what survives, and whoever owns the log owns the agent — log lock-in is deeper than model or API lock-in.<br>*[The Log Is The Agent](../talks/the-log-is-the-agent.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: Server-side compaction is the only version that can be trained-for and therefore performance-neutral, but it makes your agent's memory a vendor artifact you cannot inspect, fork, or migrate. Teams choosing wrong here discover it during a provider migration or an audit, not during development.*

## Practical Guidance

**Do:**

- Name the specific constraint forcing compaction (window overflow, caching no longer applying) before enabling it, and benchmark cost, latency, and recall against an untouched-history baseline first
- Back the session with an append-only event log or on-disk files so the harness and sandbox are disposable and a compaction or full context reset is recoverable rather than destructive
- Treat compaction as a best-effort lossy fork resumed as a new log, retaining the raw log alongside it
- Keep the rolling summary itself retrievable so the agent can do recall over the summarization instead of only reading the summary
- Use provider server-side auto-compaction where available, since it is compacted in the form the model was trained on and is designed to hold performance across the boundary
- Prevent context growth upstream instead of compacting later: cap the available-skills block (Codex uses 2% of the max context window), mark tools as deferred so they load via tool search, and give each subagent only its claim and evidence rather than its full output
- Store large tool results outside the context and pass a summary or handle, so they are not re-sent on every loop iteration
- Extract atomic facts continuously as conversation happens rather than storing everything and compacting on overflow, and score relevance adaptively so compaction is knowledge-based
- Keep BM25/keyword retrieval in the mix at large context sizes — dense semantic search dropped to 0% recall at 400k tokens where BM25 held 100%
- Instrument per-turn tokens, cache-hit rate, cost, and TTFT, since these are cheap to log and are the only way to tell whether a compaction policy is helping
- Cap tool-loop max iterations so a runaway loop cannot force compaction in the first place
- Run verification and grading in a separate context window from the one that did the work

**Avoid:**

- Compacting on a schedule or by default with no measured constraint — it is slow, you cannot choose what survives, and what it throws away is gone
- Summarizing for compression ratios under ~50x, because the prompt-cache invalidation costs more than the tokens saved
- Aggressively clearing old tool outputs — the agent re-retrieves what it already had, producing more tool calls and higher total cost
- Letting every subtask dump its full output into the primary thread, crowding out the main context
- Comparing context-management strategies on single-turn benchmarks, which never accumulate enough tokens to trigger compaction at all
- Treating the context window and the session as the same thing, which is what most traditional harness implementations do
- Relying on Claude Code's or Codex's local JSONL writes as your durable log — in SDK mode those writes are fire-and-forget, so a failed write loses the data
- Prescribing an explicit memory schema for the model; performance drops relative to letting the model structure its own memory
- Carrying forward harness-side context workarounds after a model no longer needs them — they become pure overhead and can cause the cache to be discarded incorrectly
- Assuming a smaller local model is a drop-in substitute: a 32K window cut chat recall from 92-95% to 33%, and more parameters do not widen the window

## Notable Outliers

- Keeping the entire conversation history untouched beat every compaction preset on memory recall, cost, and latency simultaneously — on DeepSeek the setup sending the most tokens was the cheapest to run, because 97% of tokens were cached. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [45:31](https://www.youtube.com/watch?v=WP3hjUXd918&t=2731s))
- Compaction now works well enough that a single thread can stay alive for five weeks with ~400 subagents in it and still know what it needs to do. ([Full Workshop: Setting Yourself Up for Success —Jason Liu, OpenAI Codex](../talks/full-workshop-setting-yourself-up-for-success-jason-liu-openai-codex.md), [3:29](https://www.youtube.com/watch?v=il1c1a2FufU&t=209s))
- Apply RL to the compaction step itself, not just to the task — generate to the end of the window, summarize, then keep generating, and train that summarization decision. ([Scaling to Long Horizons](../talks/scaling-to-long-horizons.md), [10:42](https://www.youtube.com/watch?v=2bvtay8wGYI&t=642s))
- Don't compact — reset. Clear the context completely and have the agent re-read its own handoff and history files from disk, because state in files survives context wipes and machine crashes. ([I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [2:25](https://www.youtube.com/watch?v=4kYl2_mqmnQ&t=145s))
- KV compaction is a dead end as a learning mechanism: it only applies to what fits in context and forfeits the benefits of taking gradients. ([Scaling Compute on Context](../talks/scaling-compute-on-context.md), [13:01](https://www.youtube.com/watch?v=WiqDvX6isc4&t=781s))
- Memory injection and compaction engines must be KV-cache-aware, because clever model-side manipulation breaks cache reuse and erases the savings. ([Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [15:23](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=923s))

## All Talks

- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Claude for Long-Horizon Tasks](../talks/claude-for-long-horizon-tasks.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
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
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Neil Zeghidour](../speakers/neil-zeghidour.md)
- [Omar Solano](../speakers/omar-solano.md)
- [Paul Iusztin](../speakers/paul-iusztin.md)
- [Rajkumar Sakthivel](../speakers/rajkumar-sakthivel.md)
- [Romain Huet](../speakers/romain-huet.md)
- [Ross Taylor](../speakers/ross-taylor.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)
- [Walden Yan](../speakers/walden-yan.md)

