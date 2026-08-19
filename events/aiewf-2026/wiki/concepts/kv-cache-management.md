---
title: "kv cache management"
type: "concept"
slug: "kv-cache-management"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 20
---

# kv cache management

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **20** speaker(s)

**Definition:** Exploiting and managing the KV cache — prefix reuse, compression, cache-aware serving — to cut latency and cost.

*Also referred to as: kv cache compression, kv cache reuse, prefix caching, prompt caching, kv cache aware serving, kv cache economics, prompt cacheability*

## State of Practice

Prefix caching has become the load-bearing economic primitive of agent serving: teams design the request so the first 80–90% of the context is byte-identical across calls and only the tail varies, which speakers report as up to 90% cheaper and faster inference and roughly 10x cheaper input tokens on a hit. The second-order consequence dominates 2026 design debates — any operation that rewrites earlier context (summarization, compaction, memory injection, tool-output eviction) invalidates the prefix and converts a cache hit into a full re-prefill, so compaction is now argued for on intelligence grounds rather than cost, and one team measured that keeping full history beat every compaction preset on recall, cost, and latency simultaneously because 97% of their tokens were cached. At 500K–1M context under concurrency the cache stops being a serving detail and becomes a storage system: MiniMax/Together describe it explicitly as rebuilding a distributed file system or large database, cache lifetime becomes a tunable cost knob, and object-storage-backed caching is anticipated on pure unit economics ($2/GB DRAM vs 2 cents/GB S3) even though almost nobody ships it yet. Provider-side parameters that feel physical — most notably the 5-minute cache TTL — are operational pricing choices, which is why several teams buy raw compute or self-host to control their own cache economics. Architectural consequences are already visible: one long-lived sidekick with a running context instead of fresh sub-agents, inference fired every 1–2 seconds during speech instead of waiting for silence, and cache-hit rate logged per turn next to tokens, cost, and TTFT. On the model side, weight quantization is considered near Pareto-optimal, so the next compression gains are expected to come from the KV cache itself.

## Consensus

### A stable, byte-identical context prefix is the primary cost and latency lever in production agents — cache the system prompt and tool definitions, and confine variation to the tail of the request.

Support: **4** talk(s)

> "if the beginning of the context you send to the model is the same each time, then you can get up to 90% cheaper, faster inference um depending on the conditions."
>
> — [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [11:22](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=682s)

Supporting talks: [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)

### Rewriting earlier context — compaction, summarization, or clever memory injection — invalidates the KV cache, so cache-awareness is a hard constraint on context-management design rather than an optimization applied afterward.

Support: **3** talk(s)

> "you're actually then now like paying 10 times as much for the for those input tokens if you didn't compact. Um the main reason we compact is actually intelligence."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s)

Supporting talks: [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)

### At agentic context sizes the KV cache is a storage-systems problem — placement, tiering, and lifetime — not a serving parameter, and its cost is managed by controlling how long each cache lives and where it lives.

Support: **4** talk(s)

> "Like in in some sense, it's like recreating a distributed file system. So, we we're in some sense building something like that or a very big database."
>
> — [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s)

Supporting talks: [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)

## Disagreements

### Should an agent trim or compact its context as a default discipline, or keep the full history intact and let the prefix cache absorb the cost?

| Position A | Position B |
|---|---|
| Do not compact by default. Keeping the entire conversation untouched beat every compaction preset on recall, cost, and latency at once, because ~97% of tokens were cache hits; aggressively clearing old tool outputs actually raises cost by forcing the agent to re-retrieve what it already had. Compaction is only justified once you can name the constraint forcing it (e.g. the conversation no longer fits the window, at which point caching stops helping anyway).<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)* | Trim and offload as standard hygiene: cache the system prompt but store large tool results outside the context and send summaries, run a sliding window over the last N messages with the dropped history summarized back in, and auto-compact server-side. Oversized context also degrades quality independently of cost, because more content means more chance of contradicting information confusing the model.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* |

*Why it matters: The two camps invert the cost model — one treats tokens-in-context as nearly free once cached and engineering effort goes into protecting hit rate, the other treats every resent token as recurring spend and builds compaction machinery. Picking wrong means either paying for repeated full prefills or shipping an agent that re-retrieves information it already had.*

### How much context can you safely accumulate behind a cache before quality, rather than cost, becomes the binding limit?

| Position A | Position B |
|---|---|
| Long context does not necessarily rot — distinctive facts were recalled reliably up to 800k tokens with no compaction at all, and the setup sending the most tokens was the cheapest to run.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* | Current models should not be used past ~200K tokens and ideally under 100K regardless of advertised windows; filling a context window too full degrades answer quality independent of hitting the hard token limit, which is why documents get split across multiple parallel caches with a supervisor querying them.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* |

*Why it matters: If the 100–200K ceiling is real, cache-augmented designs must shard context across multiple caches and add a routing layer; if long context holds, the far simpler single-growing-prefix architecture wins and the sharding work is wasted.*

### Should teams accept provider-managed caching semantics or take ownership of the cache layer themselves?

| Position A | Position B |
|---|---|
| Own it. The 5-minute cache window is an operational and pricing decision, not physics; buying direct compute instead of per-token pricing was materially cheaper for cached tokens, self-hosting lets you optimize for your specific workload shape, and at scale you end up building the distributed cache store yourself. Object storage for KV caching is still rare but the economics ($2/GB DRAM vs 2 cents/GB S3) make it inevitable.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)* | Use the provider's. Compaction should happen server-side in the exact form the model was trained on so performance is unchanged after compaction, and prompt caching is a one-flag, provider-portable feature — the caching, tool-search, and WebSocket advantages are all exposed through the API without owning any infrastructure.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)* |

*Why it matters: Owning the cache layer means inheriting a distributed-storage problem (eviction, P999 object latency, tiering) in exchange for control over TTL and unit cost; deferring to the provider means your architecture is silently bounded by a 5-minute TTL and opaque server-side compaction you cannot tune.*

## Practical Guidance

**Do:**

- Hold the first ~90% of every request byte-identical and confine variation to the final ~10%, so the prefix cache hits on every call
- Turn on prompt caching for the system prompt and, where supported, tool definitions and messages — it is provider-portable, not framework-specific
- Log cache hits per turn alongside tokens, cost, TTFT, and tool calls; it is cheap to implement and most teams skip it
- Name the specific constraint forcing compaction (e.g. conversation no longer fits the window, so caching no longer applies) before enabling it
- Run one long-lived sidekick agent with a running context instead of spawning fresh sub-agents, since cached tokens are ~10x cheaper than re-provisioning context
- Fire inference every 1–2 seconds while a user is still speaking rather than waiting for a second of silence — the stable prefix makes the repeated calls cheap
- Treat cache lifetime as an explicit cost knob: tune how long each cache lives rather than accepting defaults
- Make any memory-injection or retrieval-augmentation engine KV-cache-aware by construction
- If you compact, do it server-side in the exact representation the model was trained on so quality does not shift
- Cap tool-loop iterations — uncapped loops that run 10–20 times or spin infinitely destroy both cache locality and token budget
- Design object-storage-backed cache tiers against P99/P999 latency (a 256–512KB S3 read P99 is ~200ms), not P50, because one logical operation issues many requests

**Avoid:**

- Summarizing to save money — it invalidates the provider's prompt cache, so you need >50x compression before it pays off
- Assuming compaction reduces cost or throughput; it forces a cache miss and can make input tokens ~10x more expensive
- Aggressively clearing old tool outputs, which pushes the agent to re-retrieve information it already had and adds tool calls
- Doing anything "cute" model-side with memory or context ordering that silently breaks cache reuse
- Treating the 5-minute cache TTL as a physical law rather than a provider pricing decision
- Bucketing documents across parallel caches by domain — with densely related documents the supervisor skips domains that look irrelevant at first glance
- Evaluating context and cache strategies on single-turn benchmarks, which never accumulate enough tokens to trigger compaction at all
- Making infrastructure decisions from benchmarks instead of first-principles napkin math, since benchmarks routinely measure the wrong thing
- Running models past ~200K tokens of context on the assumption that a large advertised window plus caching makes it free

## Notable Outliers

- KV cache handling at 500K–1M context under concurrency is not conceptually hard — it is a distributed file system / database problem that ML practitioners simply never learned, and the industry is rediscovering undergraduate systems material live. ([Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s))
- Weight quantization is approaching Pareto optimality, so the next real compression gains have to come from KV cache compression and sparsity instead. ([Compression at the Edge](../talks/compression-at-the-edge.md), [39:54](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2394s))
- Using S3 for KV caching is still very uncommon, but the economics — $2 per GB of memory versus 2 cents per GB of S3 — make it inevitable. ([Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [31:23](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1883s))
- On DeepSeek, the configuration that sent the most tokens was the cheapest to run, because 97% of them were cache hits. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [52:08](https://www.youtube.com/watch?v=WP3hjUXd918&t=3128s))
- KV compaction as a learning mechanism is fundamentally limited: it only applies to what fits in context and forfeits the generalization you get from taking gradients. ([Scaling Compute on Context](../talks/scaling-compute-on-context.md), [13:01](https://www.youtube.com/watch?v=WiqDvX6isc4&t=781s))
- At ~1,000 tokens/sec inference the network, not inference or cache misses, becomes the dominant bottleneck, which is why a stateful WebSocket sending only changed items beats server-sent events. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [15:33](https://www.youtube.com/watch?v=shRR1e2HXMk&t=933s))

## All Talks

- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Compression at the Edge](../talks/compression-at-the-edge.md)
- [Context Engineering in 2026](../talks/context-engineering-in-2026.md)
- [Scaling Compute on Context](../talks/scaling-compute-on-context.md)
- [The State of Model Routing](../talks/the-state-of-model-routing.md)
- [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)
- [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

## Speakers

- [Alex Atallah](../speakers/alex-atallah.md)
- [Allen Pike](../speakers/allen-pike.md)
- [Asma Beevi](../speakers/asma-beevi.md)
- [Chris Alexiuk](../speakers/chris-alexiuk.md)
- [Dan Fu](../speakers/dan-fu.md)
- [Daniel Han](../speakers/daniel-han.md)
- [Dat Ngo](../speakers/dat-ngo.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Jack Morris](../speakers/jack-morris.md)
- [Louis-François Bouchard](../speakers/louis-francois-bouchard.md)
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Merve Noyan](../speakers/merve-noyan.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Olive Song](../speakers/olive-song.md)
- [Omar Solano](../speakers/omar-solano.md)
- [Parth Sareen](../speakers/parth-sareen.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Samridhi Vaid](../speakers/samridhi-vaid.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Walden Yan](../speakers/walden-yan.md)

