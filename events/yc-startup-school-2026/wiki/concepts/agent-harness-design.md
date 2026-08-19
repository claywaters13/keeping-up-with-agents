---
title: "agent harness design"
type: "concept"
slug: "agent-harness-design"
tier: "core"
maturity: "contested"
talk_count: 5
speaker_count: 5
---

# agent harness design

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **5** talk(s) by **5** speaker(s)

**Definition:** The engineering of the scaffold around a model — loop, prompts, tools, memory, and control flow — treated as the primary unit of design and iteration, distinct from the model itself.

*Also referred to as: agent harness, agent harness engineering, harness design, agent skills and harnesses, agentic loop design, agent orchestration*

## State of Practice

By this conference the harness — loop, prompts, skills, tools, verification — is treated as the primary engineering surface, and the model as a rented commodity underneath it. The dominant technique is no longer prompt engineering but objective design: hand the agent a task slightly beyond its reach, give it a mechanical way to check its own output (test runs, a screenshot-and-pixel diff against a reference, an evaluator model scoring candidate solutions), and let it run — Anthropic reports an 11-day single-prompt Zig-to-Rust rewrite of the Bun runtime now shipping in production Claude Code, and Google reports agent flows running for days or weeks. The machinery itself is getting thinner, not thicker: Anthropic deleted 80% of Claude Code's system prompt for Opus 5 and found the model marginally smarter with none at all, and speakers on both the open-source and hyperscaler side describe high-leverage systems as 'skills, markdown files, and cron jobs' rather than orchestration graphs. Where the field splits is what fills the space a thin harness leaves: a large curated library of written cognition (Tan's ~220k-page wiki, Dean's 30-page performance-hints document, skills-plus-hints to keep agents on the well-lit path) versus deliberately shedding written instruction on every model release because most of it encodes deficiencies that the next generation no longer has. The practical constraints being named out loud are token cost, cache-invalidating always-on designs, cross-machine compute scheduling, and dependency on a single lab's pricing — not model capability.

## Consensus

### The binding constraint on agent value is the scaffold and its deployment, not further model progress — today's models already contain unrealized capability that harness design fails to elicit.

Support: **4** talk(s)

> "the bottleneck is not the progress of the AI models, the bottleneck is diffusing that through the rest of the world"
>
> — [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [9:27](https://www.youtube.com/watch?v=sJ4VJWycX9M&t=567s)

Supporting talks: [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [Own Your Intelligence](../talks/own-your-intelligence.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)

### The harness's core job is supplying an objective and a verification mechanism — a metric, eval, evaluator model, or self-check the agent can run — not orchestrating steps.

Support: **3** talk(s)

> "the skill nowadays is less about prompt engineering and more about figuring out how do you give Claude a hard task that seems a little bit too hard. And then how do you make it possible for Claude to verify its work along the way?"
>
> — [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [20:04](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1204s)

Supporting talks: [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)

### Leverage lives in the context and instructions you supply from outside the model, not in weights or API access — steering happens through guidelines, skills, and markdown rather than parameters.

Support: **4** talk(s)

> "you can actually make the model work better and succeed at that kind of problem by not just adjusting the model parameters which is hard to do from the outside but from you know creating better guidelines for the model"
>
> — [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [18:34](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1114s)

Supporting talks: [Own Your Intelligence](../talks/own-your-intelligence.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [Fun Is Velocity](../talks/fun-is-velocity.md)

### The executable machinery should stay minimal — elaborate orchestration (graphs, workflow DSLs, custom slash-command scaffolding, config surface) is optional overhead, not the source of capability.

Support: **4** talk(s)

> "It's mostly skill files. Plus a browser that the agents can drive, pages of English and a way to act on the world. Markdown, not magic. Fat skills, thin harness."
>
> — [Own Your Intelligence](../talks/own-your-intelligence.md), [16:46](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1006s)

Supporting talks: [Own Your Intelligence](../talks/own-your-intelligence.md), [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [Fun Is Velocity](../talks/fun-is-velocity.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)

### Multi-day to multi-week autonomous runs are already achievable with current models; the remaining limits are token cost, verification, and infrastructure rather than model capability.

Support: **3** talk(s)

> "for some problem domains and with highly capable models underlying them you can get them to run for days or weeks and do really really complicated tasks"
>
> — [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [4:21](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=261s)

Supporting talks: [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [Fun Is Velocity](../talks/fun-is-velocity.md)

## Disagreements

### Should a harness accumulate written instruction (specs, skills, hints, guidelines) or shed it?

| Position A | Position B |
|---|---|
| Write more down and write it more precisely: agents cannot ask clarifying questions the way a colleague can, so specification quality matters more than before; extracted cognition in skill files and multi-page hint documents is what keeps long-running agents on the well-lit path.<br>*[The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)* | Over-specification is the dominant failure mode, especially among long-tenured engineers: give a high-level task plus guardrails plus exit criteria, add an instruction back only after observing the model repeatedly fail the same way, and periodically delete your CLAUDE.md, skills, and hooks entirely to see what the model does unaided.<br>*[We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)* |

*Why it matters: It determines whether teams invest in growing a durable instruction corpus or in a discipline of continuous deletion — and every line kept is read on every single model call, so the two approaches diverge in cost and in how much the harness constrains a smarter model.*

### Are harness and context artifacts durable, compounding assets or disposable scaffolding tied to a model generation?

| Position A | Position B |
|---|---|
| They compound and appreciate: a curated personal context library gets more valuable as models improve, because a smarter reader extracts more from the same corpus, and skills should be owned in a repo from day one.<br>*[Own Your Intelligence](../talks/own-your-intelligence.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)* | They expire: evals typically survive one to three model generations before saturating and being thrown away, most system-prompt content exists only to patch deficiencies that vanish with the next model, and practitioners should be willing to abandon priors and retry what previously failed.<br>*[We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)* |

*Why it matters: If artifacts compound, the right move is to invest in curation and treat the corpus as the moat; if they expire, that investment is depreciating maintenance and the moat has to come from elsewhere.*

### Should a harness be co-designed tightly with one frontier model, or kept portable across models?

| Position A | Position B |
|---|---|
| Portability is a survival requirement — a harness over-optimized for one lab's model left a major open-source project exposed when subscription access was cut with roughly 24 hours' notice; run anywhere, work with any model, keep data local.<br>*[Fun Is Velocity](../talks/fun-is-velocity.md), [Own Your Intelligence](../talks/own-your-intelligence.md), [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)* | The harness should be retuned to the specific model on every release — ablate prompts and tools line by line per generation and exploit model-specific behavior, since each generation has a different personality and the gains from fitting it are large.<br>*[We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)* |

*Why it matters: Per-model tuning buys measurable capability now but couples your product's economics and availability to one vendor's pricing and access decisions; portability costs elicitation quality but makes the harness an asset you actually control.*

## Practical Guidance

**Do:**

- On every new model release, run a full ablation: delete the entire system prompt, tools, CLAUDE.md, skills, and hooks, then restore line by line to measure each line's contribution (Cherny suggests every 6 months for ordinary Claude Code users)
- Give the agent a concrete self-verification mechanism before adding any orchestration — e.g. run the Electron app in a Mac VM, screenshot it, compare pixel by pixel against the Swift port, and don't stop until they match
- Frame long tasks as high-level goal + guardrails + exit criteria rather than a step-by-step procedure
- Use inference-time compute to search over candidate solutions with an evaluator model scoring them, to raise reliability in long-running flows
- Re-run tasks that failed on a previous model against each new model before concluding they are out of reach
- Add a line back to the system prompt only after observing the model fail the same way repeatedly, since it is read on every call
- Keep skills and context in a repo you control and can move between models and vendors
- Budget for evals to expire after one to three model generations and plan replacements
- Prune and curate the context corpus — stale entries get retrieved and stated with total confidence
- When picking a domain to build a specialized harness for, choose tasks where general models succeed 0–1% of the time, not ~20%, and check whether the gap is durable for years rather than months
- Separate what belongs in latent space (taste, judgment, reading intent) from what belongs in deterministic code, and steer the former with a markdown file

**Avoid:**

- Adding instructions to the system prompt preemptively or defensively — most of them encode deficiencies of a model generation you are about to leave behind
- Prescriptive step-by-step instructions to modern models; over-specification is the most common failure mode among engineers with years or decades of experience
- Building elaborate scaffolding (custom /goal, /loop machinery, workflow graphs) as a substitute for a verification signal
- Treating loops, graphs, and workflows as a new paradigm rather than as ordinary trigger-input-decision automation
- Absorbing every requested feature as a config option — one project reached ~9,500 configuration options, making comprehensive testing impossible
- Coupling a harness to a single lab's model and subscription pricing; your dependency's business model becomes your business model
- Accumulating an uncurated memory store — a brain nobody curates is a garbage dump with great search, and a bad skill file encodes a bad process forever
- Designing always-on proactive agents around heartbeats that invalidate the prompt cache — the blocker there is token cost, not capability
- Merging harness contributions whose code nobody involved fully understands

## Notable Outliers

- The model is measurably more intelligent with no system prompt at all — prompts serve the product experience, not raw capability. ([We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [5:02](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=302s))
- Agents fail around step 10 and beyond mainly because they drift off the distribution of tasks they were trained on; skills and hints work by keeping them on the well-lit path. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [22:32](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1352s))
- Every agent failure observed traces to confusing what belongs in latent space with what belongs in deterministic code. ([Own Your Intelligence](../talks/own-your-intelligence.md), [18:05](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1085s))
- Always-on proactive agents are blocked by token cost and cache-invalidating heartbeat design, not by model capability. ([Fun Is Velocity](../talks/fun-is-velocity.md), [37:22](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2242s))
- Dynamic workflows are a fourth axis of test-time compute scaling, alongside neural net size, training data, and training flops. ([We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [27:15](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1635s))
- A correctly designed agentic loop with the right eval can accomplish more than a team of 100 engineers, and the mechanics are mundane: pick the metric, then use skills, markdown files, and cron jobs. ([This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md), [27:47](https://www.youtube.com/watch?v=sJ4VJWycX9M&t=1667s))

## All Talks

- [Fun Is Velocity](../talks/fun-is-velocity.md)
- [Own Your Intelligence](../talks/own-your-intelligence.md)
- [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)
- [This is a Once-in-a-Civilization Opportunity](../talks/this-is-a-once-in-a-civilization-opportunity.md)
- [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)

## Speakers

- [Alexandr Wang](../speakers/alexandr-wang.md)
- [Boris Cherny](../speakers/boris-cherny.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Jeff Dean](../speakers/jeff-dean.md)
- [Peter Steinberger](../speakers/peter-steinberger.md)

