---
title: "Wearing the Agent: From Group Chats to Glasses"
type: "talk"
slug: "wearing-the-agent-from-group-chats-to-glasses"
track: "AI in Finance"
day: "Day 4 — Session Day 3"
room: "Track 3"
video_id: "s67bE2Ur3bY"
duration_sec: 1148
word_count: 3089
speakers: ["Sai Krishna Rallabandi"]
---

# Wearing the Agent: From Group Chats to Glasses

*Program title: Wearing the Agent: Engineering a Family-and-Friends Personal Agent, from Group Chats to Glasses*

**Speakers:** [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)

**Track:** AI in Finance &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 19m 08s

[Watch on YouTube](https://www.youtube.com/watch?v=s67bE2Ur3bY)

## Summary

Sai Krishna Rallabandi argues that the agent stack we've collectively built assumes a 'customer of size one,' and that the next wave — agents living in group chats and always-on wearables like glasses — breaks those assumptions in three specific places: security, memory, and routing. Drawing on Judith, an agent he deployed among friends and family for eight months, he shows examples of an agent DMing a user instead of answering in the group, syncing calendars across a household, and speaking through glasses rather than a car's speakers to preserve privacy. His central technical claims: guard at the action surface rather than the input (because you cannot gate everything an all-day agent reads), treat memory as atomic fact extraction with continual relevance scoring rather than store-everything-then-compact, and bake per-user permissions into per-user LoRA adapters over a shared memory layer instead of into code. He also cites work showing that two individually benign skills can combine into a malicious runtime behavior, so static scanning is insufficient. Worth watching if you're designing multi-user or ambient agents and want a concrete checklist of what changes versus the single-user case.

## Key Points

- Nearly every agent built today has a 'customer of size one,' and the next generation will serve groups and run all day on wearables, which changes the engineering problem rather than merely scaling it.
- Agentic systems cannot be secured the way an LLM is secured, because the agent acts on the world and its surface area — web pages, group messages, GitHub issues, promotional emails — is far larger and is amplified in group settings.
- Static scanning is insufficient: cited papers found that code surviving a static scan can break at runtime, and that two individually benign skills can become malignant when run together, with around 90% of observed attacks fitting this pattern.
- The recommended defense is to let the agent read everything but place a fast deterministic guard at the action surface (bash variables, exports, secret configs), classifying actions into allow, require-approval, and block.
- Regex and traditional NLP guards fail on evasion like text interspersed with dots ('L.I.K.E'), which motivates training a LoRA-fine-tuned small language model to separate the data channel from the instruction channel; on the inspect agent benchmark the naive baseline is a coin flip at 50%.
- In a group setting the model is just the engine while memory is what the agent becomes, so storage, curation, and forgetting matter more than in single-user deployments.
- Rather than storing full conversations and compacting later, extract atomic high-value facts and build autoraters that check extraction quality, relevance, hierarchical relationships, temporal decay, and retrieval accuracy.
- A continually-adapting relevance scorer enables knowledge-based compaction and real token savings, and any memory injection engine should be KV-cache-aware since cache reuse breaks when you get clever with the model.
- Privacy in a shared assistant is contextual — the same fact is benign or sensitive depending on the room — and permissions can be baked in via per-user LoRA adapters over a shared memory layer plus a classifier that decides when the agent should speak at all.

## Notable Quotes

> "almost every agent we build today has the customer of size one"
>
> — [1:25](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=85s) &middot; *The one-line framing the entire talk hangs on.*

> "you work hard as an engineer to solve a problem and then the moment you solve it, you realize that the question itself has slightly changed"
>
> — [2:12](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=132s) &middot; *Names the structural reason single-user agent engineering may already be obsolete.*

> "group settings pose uniquely different challenges compared to settings where we have single users"
>
> — [2:12](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=132s) &middot; *The talk's core thesis stated plainly.*

> "an agent called Judith which is deployed in a group setting among friends and family for a period of 8 months"
>
> — [2:12](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=132s) &middot; *Establishes the production deployment the examples come from.*

> "the agent didn't chose to not answer in the group but DM' me because of the privacy issue"
>
> — [2:57](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=177s) &middot; *Concrete instance of routing-as-privacy, the talk's third pillar.*

> "we can't secure an agentic system like we secure a large language model"
>
> — [5:32](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=332s) &middot; *The security section's thesis in one sentence.*

> "the surface area that the agentic system touches is much more richer and more vast compared to a large language model and it is amplified in a group setting"
>
> — [6:18](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=378s) &middot; *States why agent security is categorically harder, with the group multiplier.*

> "we can't guard everything and remove everything from entering there has to be a balance between how we design the security layer"
>
> — [6:18](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=378s) &middot; *The tradeoff that justifies action-surface guarding over input filtering.*

> "a static scan surviving code can break at runtime"
>
> — [7:36](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=456s) &middot; *The empirical result undercutting static-analysis-based skill vetting.*

> "two skills which are benign at the surface when they run together they can be malignant"
>
> — [7:36](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=456s) &middot; *Names the compositional attack class most skill marketplaces don't model.*

> "The the papers have observed that around 90% of the attacks have this."
>
> — [8:31](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=511s) &middot; *The only hard frequency number offered for the compositional attack pattern.*

> "Instead of guarding whatever the agent reads, we let the agent read everything and then design a guard which is deterministic."
>
> — [9:22](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=562s) &middot; *The talk's central architectural recommendation for agent security.*

> "the naive approach here is basically at 50% which is a coin flip and it improves on top of that"
>
> — [10:55](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=655s) &middot; *Reports the benchmark baseline the learned guard is measured against.*

> "if you write it interspersed with dots like I do. LIi. K. The regax based approaches and most of the static approaches fail at that."
>
> — [10:55](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=655s) &middot; *Concrete evasion that motivates replacing regex guards with a learned model.*

> "we want to be able to build a system not at the input because that is going to gate everything but at the action surface where the agent actually is performing some task"
>
> — [10:55](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=655s) &middot; *The clearest statement of the input-vs-action-surface tradeoff.*

> "the model is just the engine especially when it comes to a group chat"
>
> — [12:29](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=749s) &middot; *Sets up the claim that memory, not the model, defines a group agent.*

> "The memory is what the agent becomes and it's becoming in real time it's evolving in real time."
>
> — [12:29](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=749s) &middot; *The memoir line of the memory section; frames memory as identity rather than storage.*

> "A probably smarter way would be to ex extract some form of atomic information, atomic bits from this conversation."
>
> — [13:50](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=830s) &middot; *States the alternative to store-everything-and-compact.*

> "once we have a relevant scorer which is continuously adapting we can save much more on the tokens because now we are doing knowledge based compaction"
>
> — [15:23](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=923s) &middot; *Ties continual relevance scoring to a measurable cost benefit.*

> "we all of us use KV caches and KV caches break when we try to do something cute with respect to the model"
>
> — [15:23](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=923s) &middot; *A practical serving constraint most memory-architecture talks omit.*

> "a shared assistant is not just a large model which is shared between different people but it's almost a new social contract"
>
> — [16:06](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=966s) &middot; *Reframes multi-user agents as a social rather than purely technical problem.*

> "the data has not changed the room in which it is deployed has changed"
>
> — [16:06](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=966s) &middot; *Crisp formulation of contextual privacy — sensitivity is a property of context, not content.*

> "Therefore the permissions are baked in. Now this is baking the permissions not by using code but by using machine learning itself."
>
> — [17:12](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=1032s) &middot; *The most contestable design claim in the talk: permissions enforced by adapters rather than access control code.*

> "A typical observation from where agents are deployed in group setting is they tend to o be over proact be over uh articulative when they are not asked questions."
>
> — [17:12](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=1032s) &middot; *Names the dominant failure mode of group-deployed agents from real usage.*

## Positions

- Almost every agent built today serves a single user, and the next generation will serve groups and run all day on wearables. ([1:25](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=85s), confidence: stated)
- Agentic systems require a fundamentally different security approach than LLMs because they act on the world, giving them a far larger attack surface. ([5:32](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=332s), confidence: stated)
- Static scanning of agent skills is insufficient; code that passes a static scan can break at runtime, and two benign skills can be malignant in combination. ([7:36](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=456s), confidence: stated)
- Around 90% of observed attacks involve the pattern where individually benign skills combine to exfiltrate data. ([8:31](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=511s), confidence: stated)
- Security should be enforced at the action surface with a fast deterministic guard, not by filtering everything the agent reads. ([9:22](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=562s), confidence: stated)
- Regex and static approaches fail against character-interspersed obfuscation, so a learned model is needed as a guard. ([10:55](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=655s), confidence: stated)
- On the inspect agent benchmark, the naive guard baseline performs at 50% — a coin flip — and the trained model improves on it. ([10:55](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=655s), confidence: stated)
- In group deployments memory, not the model, is what determines the agent's behavior and identity. ([12:29](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=749s), confidence: stated)
- Extracting atomic facts from conversations is superior to storing everything and compacting when context overflows. ([13:50](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=830s), confidence: stated)
- A continually adapting relevance scorer enables knowledge-based compaction that saves substantially more tokens than naive compaction. ([15:23](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=923s), confidence: stated)
- Memory injection engines must be KV-cache-aware, because clever model-side manipulation breaks cache reuse. ([15:23](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=923s), confidence: stated)
- Whether information is public or private depends on the room it is shared in, not on the data itself. ([16:06](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=966s), confidence: stated)
- Per-user LoRA adapters over a shared memory layer are a better way to enforce permissions than implementing access control in code. ([17:12](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=1032s), confidence: stated)
- Agents deployed in group settings tend to be over-proactive and speak when not asked, which a small classifier trained to predict turn-taking could fix. ([18:02](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=1082s), confidence: stated)
- Group agent harnesses need three components beyond the standard single-user stack: a security gate, a curated memory layer, and information routing. ([18:46](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=1126s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [context compaction](../concepts/context-compaction.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [kv cache management](../concepts/kv-cache-management.md)
- [post-training](../concepts/post-training.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)
- [session management](../concepts/session-management.md)

