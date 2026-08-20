---
title: "kv cache management"
type: "concept"
slug: "kv-cache-management"
tier: "supporting"
maturity: "consolidating"
talk_count: 12
speaker_count: 21
---

# kv cache management

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **12** talk(s) by **21** speaker(s)

**Definition:** Exploiting and managing the KV cache — prefix reuse, compression, cache-aware serving — to cut latency and cost.

*Also referred to as: kv cache compression, kv cache reuse, prefix caching, prompt caching, kv cache aware serving, kv cache economics, prompt cacheability*

## State of Practice

Prefix caching has stopped being an optimization and become the load-bearing assumption of agent architecture: with cached input tokens roughly 10x cheaper than uncached ones and prefill speedups reported up to 18x, the shape of an agent's context is now designed backwards from what keeps the KV prefix byte-identical across turns. The practical consequence is that every context-management technique that rewrites history — summarization, compaction, tool-output eviction, sliding windows — must be charged for the cache miss it causes, and several teams found the miss dominates the savings (Towards AI measured that summarization must compress >50x to break even, and their highest-token configuration was also their cheapest at 97% cache hits). Architecture follows the cache: one long-lived sidekick with a running context beats spawning fresh sub-agents, and voice and clinical stacks explicitly hold conversations warm (96%+ hit rate at Hippocratic AI). At the serving layer, KV cache at 500K–1M context under concurrency is being rediscovered as a distributed-storage problem — residency, eviction, tiering, and lifetime — with S3-backed KV caching openly predicted on economics (2¢/GB vs $2/GB DRAM), and the ubiquitous 5-minute cache TTL identified as a provider pricing decision rather than a physical limit. Looking forward, weight quantization is near Pareto-optimal, so the remaining compression headroom is expected to move to the KV cache itself and to sparsity.

## Consensus

### A stable context prefix is the single largest available lever on both cost and latency, so system prompts, tool definitions, and skill blocks should be laid out to stay byte-identical across calls.

Support: **5** talk(s)

> "if the beginning of the context you send to the model is the same each time, then you can get up to 90% cheaper, faster inference um depending on the conditions."
>
> — [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [11:22](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=682s)

Supporting talks: [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)

### Any transformation that rewrites earlier context invalidates the cached prefix, and the resulting cache-miss cost must be counted against the token savings before calling the transformation a win.

Support: **3** talk(s)

> "you're actually then now like paying 10 times as much for the for those input tokens if you didn't compact. Um the main reason we compact is actually intelligence."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s)

Supporting talks: [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)

### At production context lengths and concurrency, KV cache management is a storage-systems problem — residency, tiering, and cache lifetime — not a modeling problem.

Support: **5** talk(s)

> "Like in in some sense, it's like recreating a distributed file system. So, we we're in some sense building something like that or a very big database."
>
> — [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s)

Supporting talks: [Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md), [The State of Model Routing](../talks/the-state-of-model-routing.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)

### Prefer one long-lived context that stays warm in cache over spawning fresh contexts that must re-send state, because re-provided context is billed at uncached rates.

Support: **3** talk(s)

> "we don't use sub agents. We use what we call a sidekick, which is um, one sub agent that continually has a running context. So the main agent doesn't need to re-provide uh, context from earlier."
>
> — [The State of Model Routing](../talks/the-state-of-model-routing.md), [18:04](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1084s)

Supporting talks: [The State of Model Routing](../talks/the-state-of-model-routing.md), [Context Engineering in 2026](../talks/context-engineering-in-2026.md), [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)

## Disagreements

### Should agents compact, summarize, or trim conversation history by default?

| Position A | Position B |
|---|---|
| No — keep the full history untouched. Compaction breaks the prefix cache and the re-prefill plus re-retrieval cost exceeds the token savings; only compact once a named constraint (e.g. the conversation no longer fits the window, so caching stops applying) forces it. Towards AI measured full history as simultaneously cheaper, faster, and higher-recall than every compaction preset; Cognition/OpenRouter note compaction is worth it for intelligence, not for cost.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md), [The State of Model Routing](../talks/the-state-of-model-routing.md)* | Yes — treat history reduction as standard hygiene. Cache the system prompt, then trim with a sliding window and summarize what falls out, store large tool results outside the context and send summaries, or extract atomic facts continuously; OpenAI runs auto-compaction server-side in the format the model was trained on so quality is preserved.<br>*[Your Agent Is Wasting Tokens and You Don't Know It](../talks/your-agent-is-wasting-tokens-and-you-dont-know-it.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)* |

*Why it matters: The two camps produce opposite bills: under high cache hit rates the token-count-minimizing agent is the expensive one, while under low hit rates or small windows it is the cheap one. Teams must instrument cache hit rate per turn before choosing, and a compaction default baked into a framework may be a net cost regression.*

### Is it safe to let a cached context grow to hundreds of thousands of tokens, or does quality degrade well before the window limit?

| Position A | Position B |
|---|---|
| Degradation is real and arrives early: never run past ~200K tokens and ideally stay under 100K regardless of advertised windows; oversized context raises the odds of contradicting information confusing the model; filling a context window too full degrades answer quality independent of the hard token limit.<br>*[The State of Model Routing](../talks/the-state-of-model-routing.md), [Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [When All Context Matters: Extended Cache Augmented Generation](../talks/when-all-context-matters-extended-cache-augmented-generation.md)* | Long context does not necessarily rot — distinctive facts were recalled reliably up to 800K tokens with no compaction at all, and the untouched-history configuration won on recall as well as cost.<br>*[Context Engineering in 2026](../talks/context-engineering-in-2026.md)* |

*Why it matters: If quality holds, the cache-maximizing strategy (never touch the prefix) is strictly dominant and cache TTL/residency becomes the only engineering problem. If it does not, teams must pay recurring cache misses to keep contexts short, and retrieval — including keyword search, which held 100% recall where dense retrieval hit 0% at 400K — stays mandatory.*

## Practical Guidance

**Do:**

- Cache the system prompt and, where the provider allows, the tool definitions and message prefix; the first call sends the full prompt and every subsequent call sends a much reduced one.
- Instrument per-turn cache hit rate alongside tokens, cost, TTFT, and tool calls — it is cheap to log and most teams skip it, and it is the number that decides whether compaction helps or hurts.
- Design for a ~90/10 split: hold the first ~90% of the context window identical request to request and vary only the tail.
- In real-time voice loops, fire inference every 1–2 seconds against the stable prefix instead of waiting for a second of silence before starting.
- Keep active conversations resident in cache rather than re-prefilling; Hippocratic AI reports 96%+ hit rate and 18x faster prefill from KV cache compression plus warm-cache residency.
- Make memory-injection and context-assembly engines KV-cache-aware — any clever mid-prefix insertion breaks reuse.
- Distribute documents across parallel caches in no particular order and balance bucket sizes, rather than bucketing by domain, and tune how long each cache lives to control cost.
- Route to reduce prefill volume (cheap model as router, expensive model only where needed) and cap tool loops with a max-iteration limit so runaway loops don't blow the cache and the budget.
- Treat KV cache at 500K–1M context as a distributed file system / database design exercise, and evaluate object storage for it on economics (~2¢/GB S3 vs ~$2/GB DRAM).

**Avoid:**

- Summarizing to save money without doing the arithmetic — you must compress by more than ~50x for it to pay off against the invalidated cache.
- Aggressively clearing old tool outputs: the agent re-retrieves what it already had, adding tool calls and cost on top of the cache miss.
- Assuming the 5-minute cache window is a physical constraint — it is a provider pricing/operations decision, and self-hosting or buying raw compute lets you set it to your workload.
- Spawning fresh sub-agents that must be re-fed context when one sidekick with a running context would keep the tokens cached.
- Porting a chat-workload inference configuration to agentic/coding workloads — uploading a whole codebase changes the caching, routing, and kernel targets entirely.
- Quantizing linear attention layers to save cache: short benchmarks look fine while long-context production output becomes gibberish.
- Client-side compaction in an ad-hoc format when server-side compaction in the form the model was trained on preserves post-compaction performance.
- Setting compaction thresholds by vibes — 'it looks good, we'll set it like this' — and validating them on single-turn benchmarks that never accumulate enough tokens to trigger compaction at all.

## Notable Outliers

- Weight quantization is close to Pareto-optimal, so the next round of compression gains has to come from the KV cache and sparsity rather than from smaller weights. ([Compression at the Edge](../talks/compression-at-the-edge.md), [39:54](https://www.youtube.com/watch?v=J4_jCrTxMkk&t=2394s))
- Using S3 as the substrate for KV caching is still very uncommon, but it will happen because the economics — 2 cents per GB versus $2 for DRAM — make it inevitable. ([Building Turbopuffer: Gergely Orosz (@pragmaticengineer ) × Simon Eskildsen (CEO)](../talks/building-turbopuffer-gergely-orosz-pragmaticengineer-simon-eskildsen-ceo.md), [31:23](https://www.youtube.com/watch?v=jQDXzEVHMSE&t=1883s))
- The 5-minute KV cache lifetime offered by providers is an operational and pricing determination, not a physics constraint — and buying compute directly rather than per-token pricing exposes how much cheaper cached tokens really are. ([The State of Model Routing](../talks/the-state-of-model-routing.md), [34:46](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2086s))
- The highest-token configuration was the cheapest to run, because 97% of the tokens sent were cached — token count and cost have decoupled. ([Context Engineering in 2026](../talks/context-engineering-in-2026.md), [52:08](https://www.youtube.com/watch?v=WP3hjUXd918&t=3128s))
- KV cache handling at 500K–1M context under concurrency is not conceptually hard, just unfamiliar — it is undergraduate distributed-systems material that most ML practitioners skipped and are now rediscovering live in industry. ([Agents at Scale: Inside MiniMax's Model and the Infrastructure Behind It](../talks/agents-at-scale-inside-minimaxs-model-and-the-infrastructure-behind-it.md), [16:32](https://www.youtube.com/watch?v=AVMr9PMINyo&t=992s))
- KV compaction is fundamentally limited: it only applies to what fits in context, and it forfeits the generalization you get from taking gradients. ([Scaling Compute on Context](../talks/scaling-compute-on-context.md), [13:01](https://www.youtube.com/watch?v=WiqDvX6isc4&t=781s))

## All Talks

- [200 Million Patient Interactions Later](../talks/200-million-patient-interactions-later.md)
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
- [Vivek Muppalla](../speakers/vivek-muppalla.md)
- [Walden Yan](../speakers/walden-yan.md)

