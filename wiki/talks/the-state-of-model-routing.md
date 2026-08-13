---
title: "The State of Model Routing"
type: "talk"
slug: "the-state-of-model-routing"
track: "Local AI"
org: "Cognition, OpenRouter"
day: "Day 4 — Session Day 3"
room: "Track 4"
video_id: "QHBjufYK8TA"
duration_sec: 2897
word_count: 9449
speakers: ["Alex Atallah", "Nader Khalil", "Tanay Varshney", "Walden Yan"]
---

# The State of Model Routing

*Program title: Model Routing*

**Speakers:** [Alex Atallah](../speakers/alex-atallah.md), [Nader Khalil](../speakers/nader-khalil.md), [Tanay Varshney](../speakers/tanay-varshney.md), [Walden Yan](../speakers/walden-yan.md)

**Org:** Cognition, OpenRouter

**Track:** Local AI &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 4 &nbsp;|&nbsp; **Duration:** 48m 17s

[Watch on YouTube](https://www.youtube.com/watch?v=QHBjufYK8TA)

## Summary

A four-way panel (NVIDIA, Cognition, OpenRouter) on the emerging practice of routing work across multiple models rather than picking one. The core argument is that naive routing — classify the task, send it to the cheapest model that scores well on that task type — is fragile for agentic work, because task complexity shifts mid-session and a small model that's out of its depth burns more money than the frontier model would have. Cognition's Walden describes Devin Fusion, which keeps a frontier model as planner/watcher while delegating execution to a persistent 'sidekick' with its own warm cache, claiming a 40% cost reduction at frontier-level intelligence; OpenRouter's Alex describes Fusion and the Pareto code router, and reports that in-distribution vs. out-of-distribution is the real routing signal (Opus beats Haiku 3x at 1/10 the cost on terminal bench despite costing more per token). NVIDIA's Tuhin argues models have jagged, complementary capabilities from differing post-training corpora, and that understanding those gaps is worth up to 10% accuracy. Worth watching if you're building multi-model orchestration and want the current state of the art plus honest admissions of how early it is — plus a good amount of practical detail on KV cache economics, compaction, and self-hosting cost dynamics.

## Key Points

- Routing to a dumber model based on task type is fragile in agentic settings because the task's complexity and domain drift within a single session, so the panel favors always keeping a frontier model in the loop as planner or observer even when it isn't doing the work.
- Cognition's Devin Fusion claims a 40% cost reduction at frontier-level intelligence by letting the frontier model plan and delegate implementation, and the delegated model can explore more deeply because its tokens are cheaper.
- The right routing signal is in-distribution vs. out-of-distribution, not benchmark rank: small models are cheap on in-domain work like text classification but thrash and inflate cost when out of domain — Opus scores ~3x better than Haiku on terminal bench at 1/10 the cost.
- KV cache economics dominate multi-model design: Cognition uses one long-lived 'sidekick' with a running context rather than spawning fresh sub-agents, so cached tokens stay ~10x cheaper, and a scheduled cache refresh doubles as an almost-free frontier-model check-in on the small model.
- Compaction is not primarily a cost tool — compacting forces a cache miss and raises input cost — its real purpose is preserving intelligence, since model quality falls off well before advertised million-token windows (the panel recommends staying under 200K, ideally 100K).
- OpenRouter's auto-router sat unused for nearly two years until open claw's 10-minute heartbeat created one app with two radically different intelligence needs, which kicked off broad market segmentation across models.
- The next frontier is co-designing models with the orchestration system — RL-training models both as orchestrators and as executors of other models' instructions — rather than orchestrating off-the-shelf models.
- Self-hosting changes the cost curve: API providers amortize a general workload shape into one price, while self-hosters can tune cache lifetimes and optimize for their own context/output profile and likely pay much less.
- Routing signals may come from model internals rather than heuristics — hallucination probes, linear probes, and perplexity analysis over prefill vectors can estimate how 'lost' a model is and trigger escalation.

## Notable Quotes

> "we're reducing the cost of Fable level intelligence by 40%. The way we do that is we allow Fable to still do like the planning and the the hard decision making but delegate a lot of the work to an implementation model."
>
> — [4:32](https://www.youtube.com/watch?v=QHBjufYK8TA&t=272s) &middot; *the headline number and the mechanism behind it in one breath*

> "I think actually there's this really unintuitive dynamic where smarter models actually get better and better at delegating work."
>
> — [3:53](https://www.youtube.com/watch?v=QHBjufYK8TA&t=233s) &middot; *states the counterintuitive premise the whole Fusion design rests on*

> "this kind of like naive like initial routing to based on the task type is extremely fragile, especially the more agentic the task you you work on is."
>
> — [9:02](https://www.youtube.com/watch?v=QHBjufYK8TA&t=542s) &middot; *direct rejection of the most common routing approach*

> "routing is a task of intimately intimately understanding of behavior of and strengths and weaknesses of different models, and then applying them thusly, right?"
>
> — [6:26](https://www.youtube.com/watch?v=QHBjufYK8TA&t=386s) &middot; *NVIDIA's jagged-capabilities framing of what routing actually is*

> "if you use these techniques, you can get like up to 10% higher accuracy even, right? It depends on the model pool. Depends on the task at hand."
>
> — [8:27](https://www.youtube.com/watch?v=QHBjufYK8TA&t=507s) &middot; *quantifies the upside of exploiting complementary model strengths*

> "overall, just the guarantee of always having frontier intelligence present, I think reduces the the fragility of of these systems quite a lot."
>
> — [10:14](https://www.youtube.com/watch?v=QHBjufYK8TA&t=614s) &middot; *the design principle distinguishing Fusion from prior routers*

> "you can use small models pretty easily and get a cost savings but if it's out of distribution small models may actually increase your cost because of how often they'll like call tools and how crazy their loops will be."
>
> — [14:05](https://www.youtube.com/watch?v=QHBjufYK8TA&t=845s) &middot; *names the failure mode that inverts naive cost reasoning*

> "Like if you run terminal bench on Opus and Haiku, like Opus will do about three times better at 1/10 the cost of Haiku, even though Haiku's significantly cheaper per token."
>
> — [15:25](https://www.youtube.com/watch?v=QHBjufYK8TA&t=925s) &middot; *the panel's hardest number against per-token cost intuition*

> "we don't use sub agents. We use what we call a sidekick, which is um, one sub agent that continually has a running context. So the main agent doesn't need to re-provide uh, context from earlier."
>
> — [18:04](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1084s) &middot; *the concrete architectural choice behind Devin Fusion's cache economics*

> "don't just like take models as they are and orchestrate them, but like can you actually co-design your models with the orchestration system?"
>
> — [19:13](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1153s) &middot; *frames the next research step for multi-model systems*

> "It's not obvious that actually more expensive models are actually creating an overall cheaper system."
>
> — [23:41](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1421s) &middot; *compact statement of the paradox the talk keeps returning to*

> "we've had a an auto router for like 2 years almost. Um but when we launched it, there was like no adoption of it. It was people really wanted to use specific models."
>
> — [26:31](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1591s) &middot; *honest report that routing had no market until agents created one*

> "at around like January this year with open claw, it exploded. And the reason it exploded is because there's this fundamental um idiosyncrasy in open claw where it sends heartbeats every like 10 minutes to your model of choice"
>
> — [27:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1623s) &middot; *identifies the specific workload accident that made routing mainstream*

> "you're actually then now like paying 10 times as much for the for those input tokens if you didn't compact. Um the main reason we compact is actually intelligence."
>
> — [32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s) &middot; *reframes compaction as a quality tool, not a cost tool*

> "I would like never recommend using like these models past like 200K tokens, under 100K if you can."
>
> — [32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s) &middot; *specific, checkable practitioner advice against advertised context windows*

> "the 5-minute uh window is what a lot of providers right now put, but that's uh that's that's more an operational operational operational determination rather than a like a science-based or like a core physics law determination."
>
> — [34:46](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2086s) &middot; *argues cache TTL is a business choice, not a hard constraint*

> "If you self-host, you can optimize specifically for your use, and you'll likely pay much less."
>
> — [35:37](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2137s) &middot; *the clearest statement of the self-host vs. API cost argument*

> "we actually bought direct compute capacity from these providers, and instead of paying on a per-token basis, we just paid for the underlying compute, knowing that the economics of the compute was that we were actually paying far less for for the cash tokens that we'd send over."
>
> — [36:27](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2187s) &middot; *historical detail on how Cognition made early agents economically viable*

> "I'm actually personally less bullish on these kind of like low level mechanical prompt tuning harnesses versus just telling like a smart model like here is the decision that was made and the context figure out why it went wrong."
>
> — [42:07](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2527s) &middot; *takes a side against gradient-style prompt optimization frameworks*

> "There's not going to be a thing as like a really great harness that is in absence of a really great model and vice versa."
>
> — [44:25](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2665s) &middot; *the panel's answer to whether routing is product or plumbing*

## Positions

- Devin Fusion reduces the cost of Fable-level intelligence by 40% while matching or exceeding frontier performance. ([4:32](https://www.youtube.com/watch?v=QHBjufYK8TA&t=272s), confidence: stated)
- Routing based on task type alone is extremely fragile for agentic workloads because task complexity changes mid-session. ([9:02](https://www.youtube.com/watch?v=QHBjufYK8TA&t=542s), confidence: stated)
- A frontier model should always remain present in the system — watching, if not executing — to reduce fragility. ([10:14](https://www.youtube.com/watch?v=QHBjufYK8TA&t=614s), confidence: stated)
- Benchmark rank on a domain does not imply a model is better at every task in that domain; models have complementary, jagged strengths from their training corpora. ([6:26](https://www.youtube.com/watch?v=QHBjufYK8TA&t=386s), confidence: stated)
- Exploiting complementary model strengths can yield up to 10% higher accuracy on router benchmarks like LM router bench. ([8:27](https://www.youtube.com/watch?v=QHBjufYK8TA&t=507s), confidence: stated)
- Opus scores about 3x better than Haiku on terminal bench at 1/10 the total cost, despite Haiku being much cheaper per token. ([15:25](https://www.youtube.com/watch?v=QHBjufYK8TA&t=925s), confidence: stated)
- A single long-lived sidekick agent with a running context is more cost-efficient than spawning multiple fresh sub-agents, because cached tokens are ~10x cheaper. ([18:39](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1119s), confidence: stated)
- For deep research tasks, making the smart model the outer orchestrator produces the best results; for coding it remains unclear. ([17:18](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1038s), confidence: stated)
- Compaction does not solve cost or throughput on its own, since compacting forces a cache miss that raises input token cost. ([32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s), confidence: stated)
- Current models should not be used past ~200K tokens of context, and ideally under 100K, regardless of advertised context windows. ([32:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1923s), confidence: stated)
- The 5-minute KV cache lifetime is an operational and pricing decision by providers, not a physical constraint. ([34:46](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2086s), confidence: stated)
- Self-hosting lets you optimize for your specific workload shape and will likely cost less than API pricing, which amortizes across all customers' usage patterns. ([35:37](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2137s), confidence: stated)
- Open claw's 10-minute heartbeat to the user's default model was the specific trigger that made auto-routing take off in January 2026. ([27:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=1623s), confidence: stated)
- Gradient-descent-style prompt tuning frameworks are less promising than having a smart model inspect a bad decision and rewrite the prompt itself. ([42:07](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2527s), confidence: stated)
- Newer frontier models (Fable, GPT-5.5/5.6) are already naturally collaborative and better at delegation, so routing capability is partly moving into the models themselves. ([43:48](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2628s), confidence: stated)
- Even if one model became most efficient at everything, an orchestration/arbitration layer would persist because of caching, limited memory, and imperfect visibility into other models' behavior. ([45:51](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2751s), confidence: stated)
- The current routing techniques, including Devin Fusion, will look like legacy ideas within a year. ([12:29](https://www.youtube.com/watch?v=QHBjufYK8TA&t=749s), confidence: stated)
- Model internals — hallucination probes, linear probes, perplexity over prefill vectors — can serve as a proxy for how lost a model is, and thus as a routing trigger. ([38:03](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2283s), confidence: stated)
- On local hardware like DGX Spark, spawning multiple collaborating agents is the way to raise compute utilization when memory is the binding constraint. ([43:11](https://www.youtube.com/watch?v=QHBjufYK8TA&t=2591s), confidence: stated)

## Concepts

- [context compaction](../concepts/context-compaction.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [local inference](../concepts/local-inference.md)
- [model routing](../concepts/model-routing.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

