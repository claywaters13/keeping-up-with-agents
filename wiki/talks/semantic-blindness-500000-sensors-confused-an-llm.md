---
title: "Semantic Blindness: 500,000 Sensors Confused an LLM"
type: "talk"
slug: "semantic-blindness-500000-sensors-confused-an-llm"
org: "Phaidra"
video_id: "EUsPvBeIx70"
duration_sec: 984
word_count: 2782
speakers: ["Raahul Singh", "Vanč Levstik"]
---

# Semantic Blindness: 500,000 Sensors Confused an LLM

**Speakers:** [Raahul Singh](../speakers/raahul-singh.md), [Vanč Levstik](../speakers/vanc-levstik.md)

**Org:** Phaidra

**Duration:** 16m 24s

[Watch on YouTube](https://www.youtube.com/watch?v=EUsPvBeIx70)

## Summary

Raahul Singh and Vanč Levstik of Phaidra describe how their AI agents for data centers ('AI factories') broke when asked to reason over hundreds of thousands of near-identical equipment names — a failure they call semantic blindness. They argue that neither stuffing names into context, nor vector RAG, nor sharded parallel LLM calls survives 1-gigawatt scale: embeddings can't separate 'Chiller 6' from 'Chiller 7', and sharded calls hallucinate phantom equipment while silently dropping real ones. Their fix exploits the fact that an AI factory is a tree whose depth grows slowly while width explodes: the LLM sees only a summarized path-level graph and emits a structured search plan (collect / scope / filter), which a deterministic resolver executes with pre-indexed subtrees and set operations. Measured head-to-head, the old approach fell from 80% to ~30% correctness as GPU count grew from 64 to 460,000, while the new one held 100% at a flat ~9,000 tokens per query. The closing frame inverts Karpathy's software 1.0/3.0 trend: AI-native systems should start at 3.0 and migrate the structured parts back into deterministic code.

## Key Points

- At 1-gigawatt scale an AI factory has 400,000+ GPUs plus supporting chillers, power meters, and switches, so any approach that puts equipment names in the LLM context window saturates immediately.
- Vector search fails on this data because equipment names are 20-character strings differing by a single character, giving poor recall.
- LLM frequency penalties actively sabotage long enumerations: asked to list 100 GPUs, the model's guardrails read the repeating tokens as spiraling and shut the output down.
- Sharding names across parallel LLM calls produces hallucinated phantom equipment and silent omissions — unacceptable in mission-critical infrastructure where trust erodes fast.
- The architectural insight is to scale with tree depth rather than instance count: a summarized root-to-leaf path list means a 64-GPU system and a 460,000-GPU system produce roughly the same context.
- LLMs are used for planning, not searching — the model emits structured output naming what to collect, the subtree scope, and the filter, and a deterministic resolver does the rest via pre-indexed subtrees and set intersections.
- For genuinely vague queries the LLM generates naming-convention patterns rather than reading name lists, keeping token cost roughly constant.
- Evals across synthetic scales and 66 cases on six real production systems showed 100% correctness and zero failures, with a 1GW validation pass dropping from 116 million tokens to about 390,000.
- The generalizable heuristic: if you can write down the structure or rules, it belongs in deterministic code; keep the LLM for ambiguity parsing, judgment, and final human-readable synthesis.

## Notable Quotes

> "Like we say, a product is something that works for all scenarios and does not fail silently. A demo just has to work for one."
>
> — [1:28](https://www.youtube.com/watch?v=EUsPvBeIx70&t=88s) &middot; *Crisp statement of the bar that kills the naive context-stuffing approach.*

> "The industry has not really figured out a common naming pattern yet and every single customer can have their own things"
>
> — [0:44](https://www.youtube.com/watch?v=EUsPvBeIx70&t=44s) &middot; *Names the domain constraint that makes the whole problem hard.*

> "the problem is often times the names are so similar that semantic search just fails"
>
> — [2:15](https://www.youtube.com/watch?v=EUsPvBeIx70&t=135s) &middot; *Direct rejection of the default RAG answer.*

> "The problem is you get horrible recall and hallucinations. You will see LLMs invent phantom equipment that do not exist, and also silently drop things that do exist."
>
> — [3:36](https://www.youtube.com/watch?v=EUsPvBeIx70&t=216s) &middot; *Concrete failure mode of the obvious divide-and-conquer fix.*

> "We have to find something that grows sub-linearly with increasing equipment count. And this is what we figured out. So, we should not grow with instances, we should grow with tree depth."
>
> — [4:22](https://www.youtube.com/watch?v=EUsPvBeIx70&t=262s) &middot; *The central design principle of the talk.*

> "The depth of the tree grows very slowly, the width grows extremely fast. In other words, you will have a hierarchy that only adds new equipments very rarely, but it adds a lot of them when it does."
>
> — [4:57](https://www.youtube.com/watch?v=EUsPvBeIx70&t=297s) &middot; *Explains why the tree-depth trick works structurally.*

> "because you want to go from the root to the leaf, all you have to do is describe all the paths and that's a very small finite list"
>
> — [5:39](https://www.youtube.com/watch?v=EUsPvBeIx70&t=339s) &middot; *The compression mechanism behind constant-size context.*

> "The second insight that we had was LLMs are good for planning but not good for searching."
>
> — [6:29](https://www.youtube.com/watch?v=EUsPvBeIx70&t=389s) &middot; *The talk's most portable claim about where to place the model.*

> "Set operations ensure that we have perfect recall and accuracy"
>
> — [8:32](https://www.youtube.com/watch?v=EUsPvBeIx70&t=512s) &middot; *States the reliability guarantee that deterministic resolution buys.*

> "All of this is a two or three-step process instead of a multi-step agentic loop, which can keep on running over and over again. And this keeps our total cost also relatively flat and constant."
>
> — [10:08](https://www.youtube.com/watch?v=EUsPvBeIx70&t=608s) &middot; *Explicit tradeoff against open-ended agentic architectures.*

> "So, we got 80% correctness at 64 GPUs, and that dropped to about 30% when the GPU grew to 400 460,000."
>
> — [10:57](https://www.youtube.com/watch?v=EUsPvBeIx70&t=657s) &middot; *The headline degradation number for the baseline.*

> "the old approach burned 116 million tokens for just a single validation pass while still having a lot of errors"
>
> — [11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s) &middot; *Quantifies the cost side of the baseline failure.*

> "the cost of the query was 9,000 tokens a query where the system was 64 GPUs or 460,000"
>
> — [11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s) &middot; *The flat-cost result that validates the architecture.*

> "It's great at parsing ambiguous requests, judging where to look for data and what to look for, handling phrasing we've never seen from a new user that has a different query"
>
> — [13:16](https://www.youtube.com/watch?v=EUsPvBeIx70&t=796s) &middot; *Positive definition of what should stay in the model.*

> "If your data has structure, call it a hierarchy, graph, or a schema, a language model scanning it token by token is definitely the wrong tool."
>
> — [14:04](https://www.youtube.com/watch?v=EUsPvBeIx70&t=844s) &middot; *The sharpest version of the talk's design rule.*

> "The simple heuristic that usually works, if you can write down the structure or the rules, it's a 1.0 job. And pure LM is weakest exactly when the system is large and well structured, which is precisely where we operate and our customers."
>
> — [14:04](https://www.youtube.com/watch?v=EUsPvBeIx70&t=844s) &middot; *Gives a reusable decision heuristic plus the scope where it bites hardest.*

> "We started almost pure 3.0. We threw everything in the context window because that is the fastest way to find out what's even worth building."
>
> — [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s) &middot; *Defends prototyping with brute-force context as a deliberate stage, not a mistake.*

> "Legacy software drifts from 1.0 towards 3.0 and new AI native software starts at 3.0 and matures towards 1.0 for the use cases that earn it, of course."
>
> — [14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s) &middot; *The talk's thesis-level inversion of Karpathy's framing.*

> "So every 1.0 function you add is more reliable ground for the LLM to stand on."
>
> — [15:33](https://www.youtube.com/watch?v=EUsPvBeIx70&t=933s) &middot; *Reframes determinism as support for the model rather than replacement of it.*

## Positions

- Vector embedding retrieval fails on data center equipment names because near-identical strings produce indistinguishable embeddings and poor recall. ([2:15](https://www.youtube.com/watch?v=EUsPvBeIx70&t=135s), confidence: stated)
- LLM frequency penalties cause the model to truncate or shut off output when asked to enumerate many similar names. ([2:54](https://www.youtube.com/watch?v=EUsPvBeIx70&t=174s), confidence: stated)
- Sharding entity names across parallel LLM calls yields hallucinated entities and silent omissions, making it unsuitable for mission-critical systems. ([3:36](https://www.youtube.com/watch?v=EUsPvBeIx70&t=216s), confidence: stated)
- Context should scale with hierarchy depth rather than instance count, so a 64-GPU and a 460,000-GPU system produce roughly the same summary size. ([5:39](https://www.youtube.com/watch?v=EUsPvBeIx70&t=339s), confidence: stated)
- LLMs are good at planning searches but bad at performing them. ([6:29](https://www.youtube.com/watch?v=EUsPvBeIx70&t=389s), confidence: stated)
- The baseline LLM approach dropped from 80% correctness at 64 GPUs to about 30% at 460,000 GPUs, while the new architecture held 100% across all tested scales. ([10:57](https://www.youtube.com/watch?v=EUsPvBeIx70&t=657s), confidence: stated)
- On 66 cases across six real production systems the new system produced zero failures. ([11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s), confidence: stated)
- At 1GW scale the old approach used 116 million tokens per validation pass versus 390,000 for the new one, roughly a 300x reduction. ([11:40](https://www.youtube.com/watch?v=EUsPvBeIx70&t=700s), confidence: stated)
- A two-or-three-step plan-then-resolve pipeline is preferable to a multi-step agentic loop because it keeps cost flat and bounded. ([10:08](https://www.youtube.com/watch?v=EUsPvBeIx70&t=608s), confidence: stated)
- Anything that must be 100% reproducible — exact set logic, counting, dedup across near-identical names — should be deterministic code, not an LLM. ([14:04](https://www.youtube.com/watch?v=EUsPvBeIx70&t=844s), confidence: stated)
- Karpathy's observed drift of software 1.0 into 3.0 runs backwards for AI-native systems, which should start at 3.0 and migrate toward 1.0 as they mature. ([14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s), confidence: stated)
- Prototyping by throwing everything into the context window is the right first move because it is the fastest way to discover what is worth building. ([14:52](https://www.youtube.com/watch?v=EUsPvBeIx70&t=892s), confidence: stated)
- Adding deterministic tooling improves rather than constrains model performance, since each 1.0 function gives the LLM more reliable ground. ([15:33](https://www.youtube.com/watch?v=EUsPvBeIx70&t=933s), confidence: implied)

## Concepts

- [agentic retrieval](../concepts/agentic-retrieval.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [entity resolution](../concepts/entity-resolution.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [long-context processing](../concepts/long-context-processing.md)
- [retrieval pipeline design](../concepts/retrieval-pipeline-design.md)
- [structured output contracts](../concepts/structured-output-contracts.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

