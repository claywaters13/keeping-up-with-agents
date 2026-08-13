---
title: "kv cache management"
type: "concept"
slug: "kv-cache-management"
tier: "supporting"
maturity: "consolidating"
talk_count: 10
speaker_count: 17
---

# kv cache management

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **10** talk(s) by **17** speaker(s)

**Definition:** Exploiting and managing the KV cache — prefix reuse, compression, cache-aware serving — to cut latency and cost.

*Also referred to as: kv cache compression, kv cache reuse, prefix caching, prompt caching, kv cache aware serving, kv cache economics, prompt cacheability*

## State of Practice

Prefix caching has stopped being an optimization and become an architectural constraint: practitioners now design the agent loop backwards from the requirement that the leading portion of the context be byte-identical across requests, because a stable prefix buys roughly 90% cheaper and faster inference and cached tokens run about 10x cheaper than fresh input. The consequence is that every mechanism that rewrites context — compaction, sliding-window trimming, memory injection, spawning a fresh subagent — is now priced as a cache miss rather than treated as free hygiene; Cognition explicitly compacts for intelligence, not cost, and runs a single long-lived sidekick instead of fan-out subagents to preserve the running context. At the serving layer the problem has been reframed as storage systems engineering: at 500K–1M context under concurrency, Together AI describes KV cache handling as building a distributed file system or a very large database, turbopuffer expects KV caching to move onto object storage on pure economics (a GB of DRAM is $2, a GB of S3 is 2 cents), and the ubiquitous 5-minute cache TTL is understood as a provider pricing decision rather than a physical limit — which is part of why teams with high reuse are buying raw compute instead of paying per token. Cache-as-retrieval is being tried directly: cache-augmented generation loads whole document collections into parallel KV caches and dispatches a supervisor across buckets, trading GraphRAG's graph-rebuild cost for cache lifetime cost. The counterweight to all of this is that context is not free even when it is cached — multiple speakers independently report that filling the window degrades answer quality through contradicting information, with a working recommendation of staying under 200K and ideally under 100K tokens.

## Consensus

### A stable, byte-identical context prefix is the primary lever for agent cost and latency, and applications should be architected so the front of the window does not change between requests.

Support: **5** talk(s)

> "if the beginning of the context you send to the model is the same each time, then you can get up to 90% cheaper, faster inference um depending on the conditions."
>
> — [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [11:22](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=682s)

Supporting talks: [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)

### Rewriting the context — compaction, sliding-window trimming, or clever memory injection — is not a free cost optimization; it invalidates the cached prefix or degrades behavior, so it must be spent deliberately to buy something else.

Support: **4** talk(s)

> "you're actually then now like paying 10 times as much for the for those input tokens if you didn't compact. Um the main reason we compact is actually intelligence."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s)

Supporting talks: [The State of Model Routing](../talks/the-state-of-model-routing.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

### More resident context degrades answer quality independently of cost or hitting the token limit, so what enters the window must be actively capped rather than allowed to grow to the advertised limit.

Support: **4** talk(s)

> "the more context you have in your in your context, the higher it is that you have contradicting information and it causes confusion for the model."
>
> — [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [4:05](https://www.youtube.com/watch?v=shRR1e2HXMk&t=245s)

Supporting talks: [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)

### At production scale the KV cache is a storage-systems problem — tiering, placement, and cache lifetime are the tunables, not model-level tricks.

Support: **4** talk(s)

> "Like in in some sense, it's like recreating a distributed file system. So, we we're in some sense building something like that or a very big database."
>
> — [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s)

Supporting talks: [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)

## Disagreements

### When context grows past what fits or performs well, should you compact it, or should you design so it never grows in the first place?

| Position A | Position B |
|---|---|
| Compact. Run automatic compaction (ideally server-side, in the exact format the model was trained on) or sliding-window trimming plus a summary of the dropped history, accepting the cache miss as the price of continued coherence.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)* | Don't let it overflow. Curate what enters context up front — extract atomic facts from conversations and score them for relevance rather than storing everything and compacting on overflow — and hold the prefix immutable, since compaction is a lossy patch over bad context discipline and forfeits what gradient-based learning would give you.<br>*[Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Scaling Compute on Context](../talks/scaling-compute-on-context.md)* |

*Why it matters: Compaction-first designs accept a periodic 10x input-token spike and a behavioral discontinuity at every compaction boundary; curation-first designs require building a memory extraction and relevance-scoring layer that must itself be KV-cache-aware. The two lead to entirely different memory subsystems and different steady-state token bills.*

### Is KV cache economics something you solve inside your application, or something you solve by owning the serving stack?

| Position A | Position B |
|---|---|
| Inside the application. Turn on prompt caching across whichever provider you use, keep the system prompt and tool definitions stable, defer tool schemas to lazy search, and take the provider's cache semantics as given — the wins are already exposed through the API.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* | Own the stack. The 5-minute cache window and per-token pricing are operational choices that amortize across everyone else's workload shape; buy raw compute directly, self-host, or build your own KV storage tier on object storage and optimize cache lifetime for your specific access pattern.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)* |

*Why it matters: If cache reuse is high and workload-shaped, per-token API pricing systematically overcharges you and the fix is an infrastructure project, not a prompt change. Teams that mis-diagnose this either build a distributed KV store they didn't need or keep paying for cache misses they could have designed away.*

### Should whole corpora be resident in KV cache, or should context be aggressively minimized and everything else retrieved?

| Position A | Position B |
|---|---|
| Load it all. When every document in a collection is relevant, push the corpus into multiple large-context caches in parallel, distributed in no particular order, and let a supervisor model interrogate the buckets — faster to build than GraphRAG and more accurate than similarity RAG, with cost controlled by tuning how long each cache lives.<br>*[When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* | Keep the window small. Cap what is resident — 2% of the window for skill descriptions, tools deferred behind search, large tool results stored out of band and summarized, and never run past 200K tokens (ideally under 100K) regardless of the advertised window.<br>*[Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md)* |

*Why it matters: One approach spends money on standing KV cache to avoid retrieval error; the other spends engineering on retrieval and out-of-band storage to avoid quality degradation. The break-even depends on whether your corpus genuinely has dense cross-document relationships or is separable — and getting it wrong means either a large idle cache bill or systematically missed context.*

## Practical Guidance

**Do:**

- Design the request so the first ~90% of the context window is identical from call to call, and put all variation in the trailing portion
- Enable prompt caching on the system prompt, and where the provider supports it, on tool definitions and messages too
- Cap the available-skills/tool-description block at a fixed fraction of the context window (Codex uses 2%) and truncate beyond it, marking additional tools as deferred behind a tool-search call
- Run compaction server-side in the exact format the model was trained on, so post-compaction performance matches pre-compaction
- Use one long-lived sidekick agent with a running context instead of spawning fresh subagents, so the accumulated prefix stays cached at ~10x lower token cost
- Keep working context under 200K tokens and ideally under 100K, independent of the advertised window
- Store large tool results in local or cloud storage and pass a summary into the loop rather than re-sending the full result every iteration
- Set an explicit max-iteration cap on tool loops and profile per-tool call counts and durations with observability tooling before shipping
- Treat cache lifetime/TTL as a tunable cost knob, and if reuse is high, negotiate direct compute capacity instead of per-token pricing
- In voice/real-time loops, fire inference every 1–2 seconds while the user is still speaking against the stable prefix rather than waiting for a second of silence
- If backing KV or vector storage with object storage, design against P99/P999 latency rather than P50, since one logical operation issues many requests and ~200ms object reads compound

**Avoid:**

- Injecting or reordering memory in the middle of the prefix — any model-side cleverness invalidates the cache it was meant to exploit
- Re-sending the full conversation history on every call in multi-turn agents
- Treating compaction as a cost reduction; it forces a cache miss and raises input token cost, so justify it by the intelligence you recover
- Filling the context window just because the tokens fit — quality degrades from contradicting information well before the hard limit
- Bucketing documents by domain when distributing them across parallel caches; with dense cross-document relationships the supervisor skips domains that look irrelevant at first glance
- Assuming the 5-minute cache window is a physical constraint rather than a provider pricing and operations decision
- Choosing an inference platform on model size alone — GPT-5 mini showed 5,000ms typical and 7,000ms P95 latency despite being small and cheap, because the platform did not prioritize latency
- Assuming a single inference stack serves both chat and agentic workloads; uploading a whole codebase changes the caching, routing, and kernel optimization targets
- Quantizing linear attention layers — short benchmarks look fine while long-context production output turns to gibberish

## Notable Outliers

- Weight quantization is approaching Pareto optimality, so the next round of inference gains has to come from KV cache compression and sparsity rather than from smaller weights. ([Compression at the Edge](../talks/compression-at-the-edge.md), [39:54](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2394s))
- Running KV caching on S3 is still very uncommon, but it will happen because a gigabyte of memory costs $2 and a gigabyte of S3 costs 2 cents. ([Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [31:23](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1883s))
- KV cache handling at 500K–1M context under concurrency is not conceptually hard — it is undergraduate distributed-systems material that most ML practitioners skipped and are now rediscovering live in industry. ([Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s))
- The 5-minute KV cache lifetime offered by providers is an operational and pricing determination, not a science-based or physical one. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [34:46](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2086s))
- Since GraphRAG already pushes every document through an LLM for entity extraction, loading those documents straight into a cached context is not a meaningfully larger cost — and parallel cache loading beats GraphRAG on knowledge-build time. ([When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [4:37](https://www.youtube.com/watch?v=XovaGv4f39A&t=277s))
- Per-user LoRA adapters over a shared memory layer enforce read permissions better than code-level access control, but the memory injection engine underneath must be KV-cache-aware or the cache breaks. ([Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [15:23](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=923s))

## All Talks

- [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md)
- [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Compression at the Edge](../talks/compression-at-the-edge.md)
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
- [Luis Romero-Sevilla](../speakers/luis-romero-sevilla.md)
- [Merve Noyan](../speakers/merve-noyan.md)
- [Nader Khalil](../speakers/nader-khalil.md)
- [Olive Song](../speakers/olive-song.md)
- [Parth Sareen](../speakers/parth-sareen.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Tanay Varshney](../speakers/tanay-varshney.md)
- [Walden Yan](../speakers/walden-yan.md)

