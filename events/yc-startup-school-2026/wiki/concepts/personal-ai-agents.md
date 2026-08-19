---
title: "personal ai agents"
type: "concept"
slug: "personal-ai-agents"
tier: "supporting"
maturity: "frontier"
talk_count: 3
speaker_count: 3
---

# personal ai agents

**Maturity: FRONTIER** — Frontier — too new or sparse for consensus yet

*Supporting concept* &middot; discussed across **3** talk(s) by **3** speaker(s)

**Definition:** Agents built for one individual's life and work — accumulating that person's context, acting proactively on their behalf — rather than a shared product for many users.

*Also referred to as: personal AGI, personal superintelligence, proactive agents, scheduled agent jobs, context ownership*

## State of Practice

As of this conference the field treats the personal agent — one agent accumulating one person's context and acting on their behalf — as the actual delivery vehicle for frontier capability, not a niche use case. The consensus architecture is embarrassingly plain: a large curated corpus of markdown (Tan runs ~220,000 pages of a Karpathy-style knowledge wiki), skill files that encode how you personally do a task, a thin harness, browser control, and cron jobs — explicitly not new graph/workflow paradigms. Speakers locate the differentiator in context and curation rather than weights: the same API and context window produce 2x and 100x operators, and improving frontier models are argued to *increase* the value of a private context library rather than commoditize it. The unresolved economics are proactive operation — always-on agents are described as a token-cost and cache-design problem, not a capability problem — and the unresolved politics are custody: whether it is sufficient to own the context while renting the model, or whether the runtime itself must be open and local. Everyone agrees the failure mode is uncurated accumulation ('a brain nobody curates is a garbage dump with great search') and dependency on a single lab's business model.

## Consensus

### The end state of AI is a per-person agent grounded in that individual's accumulated context, not a shared vendor chatbot — and it compounds with use rather than with vendor release cycles.

Support: **3** talk(s)

> "The corporate AGI you don't own gets better only when the company ships something. Your personal AGI gets better every single day you use it because every day it knows more of your life."
>
> — [Own Your Intelligence](../talks/own-your-intelligence.md), [7:11](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=431s)

Supporting talks: [Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Fun Is Velocity](../talks/fun-is-velocity.md)

### The implementation substrate is markdown skill files, a thin harness, and cron — not a novel agent framework; loops/graphs/workflows are restated conventional automation.

Support: **3** talk(s)

> "It's mostly skill files. Plus a browser that the agents can drive, pages of English and a way to act on the world. Markdown, not magic. Fat skills, thin harness."
>
> — [Own Your Intelligence](../talks/own-your-intelligence.md), [16:46](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1006s)

Supporting talks: [Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Fun Is Velocity](../talks/fun-is-velocity.md)

### Model quality is no longer the binding constraint on what a personal agent can do — the constraints are context selection, diffusion into real workflows, and infrastructure/token cost.

Support: **3** talk(s)

> "the bottleneck is not the progress of the AI models, the bottleneck is diffusing that through the rest of the world"
>
> — [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [9:27](https://www.youtube.com/watch?v=sJ4VJWycX9M&t=567s)

Supporting talks: [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Own Your Intelligence](../talks/own-your-intelligence.md), [Fun Is Velocity](../talks/fun-is-velocity.md)

### Building a personal agent on a single lab's proprietary stack is a structural risk; the stack should be portable across models and the intelligence layer should be commodity-cheap and decentralized.

Support: **3** talk(s)

> "So maybe write this one down. Your dependencies business model is your business model."
>
> — [Fun Is Velocity](../talks/fun-is-velocity.md), [17:56](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1076s)

Supporting talks: [Fun Is Velocity](../talks/fun-is-velocity.md), [Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)

## Disagreements

### Is an always-on, proactive personal agent buildable today, or is it gated by economics?

| Position A | Position B |
|---|---|
| Not yet — the capability exists but continuous operation is unaffordable and heartbeat designs invalidate the prompt cache, so proactive agents burn a subscription without getting far; managing compute across machines (especially on macOS) is the real bottleneck.<br>*[Fun Is Velocity](../talks/fun-is-velocity.md)* | Yes, now — correctly designed agentic loops with a metric plus cron already outperform large engineering teams, inference is getting an order of magnitude cheaper, and the personal-agent flywheel pays off within roughly twelve weeks of daily use.<br>*[This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Own Your Intelligence](../talks/own-your-intelligence.md)* |

*Why it matters: If it is a token-cost problem, the near-term product is a fast on-demand agent and the roadmap waits on price curves; if it is already viable, the differentiated product is the persistent background agent and whoever ships it first owns the user's context.*

### Where does ownership of a personal agent actually have to live — the context, or the runtime?

| Position A | Position B |
|---|---|
| Own the context and rent the intelligence: models are a rented commodity, custody of your skill files and knowledge repo is the security model, and consolidating your life into one system you control is more private than scattering it across ten clouds.<br>*[Own Your Intelligence](../talks/own-your-intelligence.md)* | Ownership has to extend to the execution layer: an open-source harness that runs anywhere with any model — or open-weight models you can run yourself — because a lab can cut off access with 24 hours' notice regardless of who owns the markdown.<br>*[Fun Is Velocity](../talks/fun-is-velocity.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)* |

*Why it matters: It decides whether you invest engineering in a portable harness and local-model support or spend that time enriching a context library on top of whichever frontier API is currently best.*

## Practical Guidance

**Do:**

- Keep your brain and skill files in a repo you control from day one, before an employer, platform, or acquirer has an opinion about it.
- Write skill files as executable cognition — the test is whether a smart intern could follow the instruction; if so, an agent can run it.
- Put taste, judgment, and interpreting vague requests in latent space steered by a markdown file, and put anything that must be exact in deterministic code — Tan attributes every agent failure he has seen to confusing the two.
- Build the agent for an audience of one (yourself first, then 2–20 friends) and treat requests to borrow it as the market signal.
- Curate the corpus continuously — prune stale facts and bad process, because retrieval surfaces a stale fact with total confidence and a bad skill file encodes a bad process forever.
- Pick the metric or eval first, then wire the agentic loop with skills, markdown, and cron jobs.
- Bring a built, screenshotted, agent-tested implementation instead of a feature request; use multi-sub-agent stress testing and review in place of most manual QA, keeping a short manual clickthrough to judge feel.
- Allocate code review by risk rather than reading every agent-written line — use elapsed time as an anomaly signal — while keeping full review in company settings where the risk calculus differs.
- Expect the flywheel to feel worthless until roughly week four and to pay off around week twelve; most people quit in week two.

**Avoid:**

- Assuming a personal agent's advantage erodes as frontier models improve — a smarter reader extracts more from the same library, so the differentiator moves toward context.
- Building on one lab's subscription or harness-specific optimizations; access can be revoked faster than you can port.
- Adding a configuration option for every feature to avoid breaking users — ~9,500 options made comprehensive testing impossible.
- Merging popular community PRs that import code neither the contributor nor the maintainer fully understands; say no more often.
- Letting the corpus grow without curation — accumulation alone produces confident retrieval of stale facts.
- Treating loops, graphs, and workflow engines as a new paradigm requiring new abstractions.
- Pricing or architecting so that agent intelligence is rationed to the wealthiest developers.
- Going all-in on verbal skill at the expense of quantitative and systems thinking, which survives every shift in abstraction layer.
- Drifting from a product you love toward a product for everyone — the moment Steinberger identifies as where velocity died.

## Notable Outliers

- The blocker on always-on proactive personal agents is purely economic — 'we could do that today, but you wouldn't get very far with your subscription' — combined with heartbeat designs that invalidate the prompt cache. ([Fun Is Velocity](../talks/fun-is-velocity.md), [37:22](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2242s))
- Skill files end the protection knowledge workers had from their tools living in their heads: cognition becomes extractable and ownable — Tan cites 40 files still executing with their author's name absent from the commit history, 'she didn't have a career, she had an extraction.' ([Own Your Intelligence](../talks/own-your-intelligence.md), [30:43](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1843s))
- A personal context library at extreme scale is already operational, not aspirational: ~220,000 markdown pages covering 25 years diarized, and a separate example of an 80,000-file repo built as 'a brain for one small boy.' ([Own Your Intelligence](../talks/own-your-intelligence.md), [14:36](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=876s))
- AGI arrives with no announcement or singular event — it diffuses as personal agents running on individual context. ([This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [5:31](https://www.youtube.com/watch?v=sJ4VJWycX9M&t=331s))
- With agents commoditizing building, the hardest startup problem is no longer tech or people but getting eyeballs — which argues for picking 'hard and boring' problems over fun ones. ([Fun Is Velocity](../talks/fun-is-velocity.md), [40:01](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2401s))
- The widely reported figure that 20% of OpenClaw skills are malicious is wrong; a scan of all 67,000 put it near 0.3%. ([Fun Is Velocity](../talks/fun-is-velocity.md), [13:38](https://www.youtube.com/watch?v=whcfSGN6CAU&t=818s))

## All Talks

- [Fun Is Velocity](../talks/fun-is-velocity.md)
- [Own Your Intelligence](../talks/own-your-intelligence.md)
- [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)

## Speakers

- [Alexandr Wang](../speakers/alexandr-wang.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Peter Steinberger](../speakers/peter-steinberger.md)

