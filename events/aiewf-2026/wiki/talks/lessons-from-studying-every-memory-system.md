---
title: "Lessons from Studying Every Memory System"
type: "talk"
slug: "lessons-from-studying-every-memory-system"
track: "Memory & Continual Learning"
org: "Independent"
day: "Day 3 — Session Day 2"
room: "Track 3"
video_id: "5ZGyKWjQDr0"
duration_sec: 1170
word_count: 2994
speakers: ["Shlok Khemani"]
---

# Lessons from Studying Every Memory System

**Speakers:** [Shlok Khemani](../speakers/shlok-khemani.md)

**Org:** Independent

**Track:** Memory & Continual Learning &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 19m 30s

[Watch on YouTube](https://www.youtube.com/watch?v=5ZGyKWjQDr0)

## Summary

Shlok Khemani spent a year reverse-engineering how ChatGPT, Claude, Gemini, and Poke actually implement memory for consumer personalization, and this talk is a guided tour of that evolution plus the lessons he draws from it. Part one traces three years of divergence and eventual convergence: ChatGPT went from a user-managed fact list (2024) to a dense ~4,000-token 'running profile' updated every few days, while Claude launched with the opposite design — no profile at all, just tools to search past conversations — before adding a smaller, user-visible, 24-hour-refresh profile. Part two argues that there is no single correct memory architecture, that memory is a compute-budget tradeoff between update cost and serving cost, and that running profiles already constitute a form of continual learning happening outside the weights. His closing rant is that the real ceiling is not architecture or compute but context acquisition: products don't notice their own contradictions, don't reason over email or calendar, and don't share memory with each other. Worth watching if you are designing a memory layer and want concrete, observed implementation details from shipped consumer products rather than a vendor's framework pitch.

## Key Points

- ChatGPT's memory v1 (February 2024) extracted user-stated facts into a visible, deletable list injected into every conversation, but it pushed the burden of memory management onto the user and had no mechanism for handling facts that went stale.
- ChatGPT's v2 (April 2025) introduced a 'running profile' — an asynchronous background process (sometimes called 'dreaming') that periodically re-reads recent conversations and rewrites a ~4,000-token, 16-section profile of extremely dense, keyword-like memories that frontier models can expand from limited clues.
- Claude's first memory version (August 2025) was architecturally the opposite: no profile and no fact list, just two tools letting the model search prior conversations by keyword/topic or by time period, so every conversation starts cold and retrieval happens on demand.
- The two systems have converged — both now have a running profile that is (somewhat) visible and editable plus tools to search past conversations — but the implementation details still differ sharply, and Gemini and coding agents like Claude Code use different approaches again (markdown files, heartbeats, knowledge bases, skills).
- Because there is no single right architecture and memory must evolve with the product, Khemani argues memory cannot be outsourced; he notes that every top consumer AI product today has memory and none of them buy it from a vendor.
- Memory is a function of compute: a running profile carries a maintenance cost (update frequency × compute per update) and a serving cost (profile length, paid on every conversation), and ChatGPT and Claude sit at opposite corners of that tradeoff — 4,000 tokens updated every few days versus ~1,000 tokens updated every 24 hours.
- The running-profile loop — profile shapes conversations, conversations feed synthesis, synthesis updates profile — is already continual learning, just outside the weights; whether it moves into weights per-individual is open, since the economics amortize at enterprise scale but not for one person.
- The binding constraint is context, not architecture: ChatGPT recorded that he visited both Thailand and Turkey on overlapping dates because it never reconciled the conversation against his email bookings, and the deeper failure is that it isn't curious enough to notice the conflict at all — a product problem, not a model limitation.
- Personal AI is fragmented: each chatbot, assistant, vertical app, agent, and hardware device rebuilds its own model of the user, none share memory, and none reason over rich existing sources like email, calendar, and photos.

## Notable Quotes

> "The biggest one was that as a user, because you could see every time a memory was created, it felt like you were responsible for both creating memories while you were just trying to have a conversation."
>
> — [2:48](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=168s) &middot; *Names the core UX failure of first-generation fact-list memory.*

> "So, staleness was another huge problem with this version of chat GPT's memory."
>
> — [3:34](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=214s) &middot; *Identifies the second structural flaw — facts true at write time that decay silently.*

> "First, these are extremely dense memories. So ChatG tries to pack in as much context as it can within every single memory."
>
> — [5:02](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=302s) &middot; *Concrete observed design choice: compression via keyword clues the model expands at read time.*

> "So in V1 of Claude, you had no user profile. You had no list of facts. Instead, the model was given two tools."
>
> — [7:09](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=429s) &middot; *The cleanest statement of the retrieval-first architecture that opposed ChatGPT's profile-first one.*

> "on September 11 of last year, I released a blog post saying Claude's memory architecture is the opposite of chat GPTs. This hit the hacker news front page."
>
> — [7:46](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=466s) &middot; *Establishes the speaker's basis for the comparison and dates the divergence.*

> "Claude's profile updates every 24 hours. For chat GPT, it's every few days."
>
> — [8:31](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=511s) &middot; *A hard reported number that anchors the update-frequency tradeoff.*

> "I think the biggest lesson for me is that there is no single way to do memory."
>
> — [9:54](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=594s) &middot; *The talk's thesis, stated plainly.*

> "The implications of this is that memory cannot be outsourced. If you're a serious team, you do not outsource memory. It is something that you build alongside your product."
>
> — [11:10](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=670s) &middot; *The most contestable claim in the talk, aimed squarely at the memory-vendor category.*

> "So if you look at all of the top consumer products today across different categories, each of these has some form of memory. Yet none of them outsource it. All of them build memory inhouse."
>
> — [11:48](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=708s) &middot; *The empirical support offered for the no-outsourcing position.*

> "Lesson two, memory is a function of compute. What does that mean? Let's look at the costs associated with a running profile."
>
> — [11:48](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=708s) &middot; *Frames memory design as a budget problem rather than an algorithm problem.*

> "So they have a higher serving cost for a lower update cost and for claude it's a thousand tokens updates every 24 hours. So they make the exact opposite tradeoff"
>
> — [13:18](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=798s) &middot; *Names the specific axis on which two shipped systems made opposite calls.*

> "Third we had a bunch of talks about continual learning today. I'm not an expert here but what I would say is that continual learning is already here."
>
> — [13:18](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=798s) &middot; *A deliberately provocative reframing of the running-profile loop as continual learning.*

> "And this loop keeps repeating itself again and again and again. And what you have is a continual learning process."
>
> — [13:56](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=836s) &middot; *Completes the argument that in-context profile synthesis is a learning loop.*

> "continuous learning does make sense at an enterprise level because the costs of these models are amotized across different employees different customers but that's not the case and at an individual level"
>
> — [13:56](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=836s) &middot; *Draws the economic line between enterprise and consumer continual learning.*

> "Yet your memory system is capped by how much context it can gather about you."
>
> — [15:08](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=908s) &middot; *The ceiling claim — architecture and compute are not the binding constraint.*

> "But what really bothers me is that chat GPD today doesn't realize that there is a conflict. It's not curious about trying to fill in gaps in the information it knows about me."
>
> — [16:46](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1006s) &middot; *Pinpoints a specific missing capability: conflict detection and active gap-filling.*

> "And this is particularly interesting and also infuriating because the tech it's not a technology problem. It's a product problem. There is no fundamental reason from an LLM level that these things can't be solved."
>
> — [16:46](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1006s) &middot; *Assigns blame to product design rather than model capability — a checkable, arguable position.*

> "Each of these products is trying to build its own memory of me. None of these memories are shared with each other. So I have to rebuild context within every single product from scratch."
>
> — [17:43](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1063s) &middot; *States the fragmentation problem that motivates portable or shared personal context.*

> "So for me, none of this feels like 2026. And what I keep asking myself every day is when will personal AI feel like personal AI?"
>
> — [17:43](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1063s) &middot; *The rant's punchline and the talk's emotional center.*

> "Memory for AI is just a three-year-old field. Memory is also foundational to how humans interact with AI."
>
> — [18:36](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1116s) &middot; *Closing framing that sets expectations for how immature the field still is.*

## Positions

- There is no single correct way to implement memory; ChatGPT, Claude, Gemini, and coding agents all evolved materially different architectures. ([9:54](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=594s), confidence: stated)
- RAG over chunked conversations with embeddings and semantic search is not how leading consumer memory systems actually work, despite being the assumed default. ([9:54](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=594s), confidence: stated)
- Serious teams should not outsource memory to a third-party provider; it must be built in-house and evolve with the product. ([11:10](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=670s), confidence: stated)
- Every top consumer AI product today has some form of memory and all of them build it in-house. ([11:48](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=708s), confidence: stated)
- Memory design is fundamentally a compute allocation problem, trading maintenance cost (update frequency and compute per update) against serving cost (profile length in every context window). ([12:35](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=755s), confidence: stated)
- ChatGPT runs a ~4,000-token profile updated every few days while Claude runs a ~1,000-token profile updated every 24 hours, representing opposite ends of the same tradeoff. ([13:18](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=798s), confidence: stated)
- Continual learning is already deployed today, in the form of the running-profile loop operating outside the model weights. ([13:18](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=798s), confidence: stated)
- Weight-level continual learning is economically viable at enterprise scale because costs amortize across employees and customers, but not yet at the individual consumer level. ([13:56](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=836s), confidence: stated)
- The ceiling on any memory system is how much context it can gather about the user, not the quality of its architecture or the compute poured into it. ([15:08](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=908s), confidence: stated)
- Systems failing to detect and resolve contradictory memories is a product problem, not a technology problem — nothing at the LLM level prevents solving it. ([16:46](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1006s), confidence: stated)
- Memory systems should proactively notice conflicts and be curious about filling gaps, rather than passively accumulating whatever the user happens to say in chat. ([16:46](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1006s), confidence: implied)
- Connecting an assistant to a data source like email is insufficient; unless it reasons over that source and updates the profile from it, existing rich context goes unused. ([16:01](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=961s), confidence: stated)
- The current landscape of siloed per-product memory forces users to rebuild and manually update context in every application, which is a state of affairs that should not be acceptable in 2026. ([17:43](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=1063s), confidence: stated)
- Claude's V1 memory architecture — on-demand tool-based retrieval with no stored profile — was the direct opposite of ChatGPT's profile-injection approach. ([7:46](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=466s), confidence: stated)
- Making memory visible to the user without also removing the management burden, as in ChatGPT's v1 fact list, produces a worse experience than background extraction. ([2:48](https://www.youtube.com/watch?v=5ZGyKWjQDr0&t=168s), confidence: implied)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [context window management](../concepts/context-window-management.md)
- [continual learning](../concepts/continual-learning.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [session management](../concepts/session-management.md)

