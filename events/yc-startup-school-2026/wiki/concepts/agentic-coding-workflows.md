---
title: "agentic coding workflows"
type: "concept"
slug: "agentic-coding-workflows"
tier: "core"
maturity: "consolidating"
talk_count: 3
speaker_count: 3
---

# agentic coding workflows

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **3** talk(s) by **3** speaker(s)

**Definition:** How engineers actually work with coding agents day to day — delegation patterns, review rhythm, parallelism, and the shape of the resulting dev loop.

*Also referred to as: self-maintaining codebases, code review as risk management, spec-driven development, dogfooding*

## State of Practice

The working pattern that all three talks converge on is: hand the agent a task that looks slightly too hard, give it a mechanical way to check its own output, and let it run unattended for days rather than minutes. Cherny reports an 11-day single-prompt rewrite of the Bun runtime from Zig to Rust that now ships in production Claude Code, and 20-30 daily maintenance routines doing the work of dozens of engineers; Dean says agents already run for days or weeks on some domains and that most people have not internalized it. The scarce inputs have moved: not prompt craft (Cherny says there is no 'one weird trick' and the model is marginally smarter with no system prompt at all), but a verifier, taste in choosing what to point the agent at, and tokens/compute. Review rhythm is being renegotiated rather than settled — Steinberger reads code by risk rather than line by line and treats elapsed wall-clock time as his anomaly signal, while conceding company settings warrant full review. The sharpest live argument is whether to invest in persistent scaffolding (skills, hints, CLAUDE.md, prescriptive specs) or to keep deleting it, since much of it exists only to patch deficiencies the next model generation removes.

## Consensus

### Autonomous agent runs measured in days to weeks are a real, in-production workflow today, not a projection — hard tasks are handed off once and steered, not decomposed into human-sized steps.

Support: **3** talk(s)

> "And it ran for 11 days, and it rewrote the entire code base."
>
> — [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [17:14](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1034s)

Supporting talks: [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [Fun Is Velocity](../talks/fun-is-velocity.md)

### What makes a long run work is a verification mechanism the agent can execute itself — a self-check loop, an evaluator model over candidate solutions, or sub-agents running stress tests and review — not better instructions.

Support: **3** talk(s)

> "the skill nowadays is less about prompt engineering and more about figuring out how do you give Claude a hard task that seems a little bit too hard. And then how do you make it possible for Claude to verify its work along the way?"
>
> — [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [20:04](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1204s)

Supporting talks: [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [Fun Is Velocity](../talks/fun-is-velocity.md)

### Model capability is no longer the binding constraint on the dev loop; the limits are human- and infrastructure-side — token/compute budget, product scaffolding that hobbles the model, and knowing what to point the agent at.

Support: **3** talk(s)

> "the model is able to do all sorts of things with today's models, not a future model, but today's model, that we have not yet realized."
>
> — [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [10:56](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=656s)

Supporting talks: [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [Fun Is Velocity](../talks/fun-is-velocity.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)

### Manual QA and human code review are being partly displaced by agent-run verification, with humans reserved for the things agents cannot judge — feel, pixel-level UI, and risk triage.

Support: **3** talk(s)

> "I think that was really early in in deciding that I don't read all the code. I see code review more as a as risk management."
>
> — [Fun Is Velocity](../talks/fun-is-velocity.md), [31:05](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1865s)

Supporting talks: [Fun Is Velocity](../talks/fun-is-velocity.md), [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)

## Disagreements

### Should you accumulate persistent scaffolding — skills, hints, guidelines, CLAUDE.md — to keep agents on track, or periodically delete it?

| Position A | Position B |
|---|---|
| Build and maintain written guidance: agents fail around step 10 because they drift off their training distribution, and skills plus hints (Dean cites a 30-page performance-hints document he co-wrote) keep them on the well-lit path. Improving the surrounding guidelines is the lever available from outside the model.<br>*[The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)* | Delete it and see what happens. 80%+ of Claude Code's system prompt was deleted for Opus 5 because most of it patched deficiencies the new generation no longer has; run a full delete-and-restore ablation on every model release, delete your CLAUDE.md, skills, and hooks every six months, and add a line back only after observing the same failure repeatedly.<br>*[We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)* |

*Why it matters: It decides whether a team's agent config is a compounding asset worth version-controlling and growing, or a liability that silently costs tokens and intelligence on every call and must be re-earned each model generation.*

### Has the value of writing a detailed specification for an agent gone up or down?

| Position A | Position B |
|---|---|
| Up. Agents have far less ability than a human colleague to ask clarifying questions, so a clear, complete specification matters more than before — cross-language code translation works so well precisely because the source is an exhaustive spec.<br>*[The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)* | Down, at least for step-by-step detail. Prescriptive instructions produce worse results with modern models than a high-level task plus guardrails plus exit criteria; over-specification is the single most common failure mode among engineers with years or decades of experience.<br>*[We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)* |

*Why it matters: It determines where an engineer's hours go before a run starts — writing a precise spec versus writing a verifier and exit criteria — and whether long-tenured engineers' instincts help or hurt on agentic work.*

## Practical Guidance

**Do:**

- Give the agent an executable verifier before starting a long run — e.g. run the Electron app in a Mac VM, screenshot it, compare pixel by pixel against the Swift port, don't stop until done
- On every new model release, delete the entire system prompt and add it back line by line to measure each line's impact; for non-builders, delete CLAUDE.md, skills, and hooks every six months and see what the model does
- Retry tasks that previous models failed — the Bun Zig-to-Rust rewrite was impossible for prior generations and worked starting with Fable
- Allocate review effort by risk instead of reading every line, and use elapsed wall-clock time of an agent run as an anomaly signal
- Spend inference-time compute on multi-agent search over candidate solutions with an evaluator model to raise reliability in long-running flows
- Bring a maintainer a fully built, screenshotted, tested PR produced with an agent rather than an issue or feature idea
- Keep some manual clickthrough in the loop — sub-agent stress testing covers most QA but not whether the product feels right
- Treat evals as disposable: expect one to three model generations before saturation, and budget for writing new ones
- Restore full line-by-line review in a company setting, where the risk calculus differs from solo open-source work

**Avoid:**

- Writing prescriptive step-by-step instructions; describe the task, the guardrails, and the exit criteria, then let the model cook
- Adding an instruction to the system prompt preemptively — only add it after observing the model fail the same way repeatedly, because it is read on every single call
- Adding a config option per feature to avoid breaking users — Steinberger reached ~9,500 options, making comprehensive testing impossible
- Merging a large community PR that neither the author nor the maintainer fully understands
- Building elaborate scaffolding (slash goal, slash loop) as a prerequisite — it helps but a hard task plus a verifier is sufficient
- Following 'one weird trick' prompting advice from LinkedIn and Twitter influencers
- Over-optimizing your harness for a single lab's model or subscription — access was cut with ~24 hours' notice
- Assuming always-on proactive agents are a capability problem; today they are a token-cost and cache-invalidating-heartbeat problem

## Notable Outliers

- The model is measurably slightly more intelligent with no system prompt at all — prompts serve the product experience, not raw capability. ([We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [5:02](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=302s))
- Agents fail around step 10 and beyond mainly because they drift off the distribution of tasks they were trained on, not because the task is hard. ([The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md), [22:32](https://www.youtube.com/watch?v=CxXgV54KzpQ&t=1352s))
- Loops, graphs, and workflows are not a new paradigm — they are the same trigger-input-decision automation engineers have always built. ([Fun Is Velocity](../talks/fun-is-velocity.md), [28:47](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1727s))
- Dynamic workflows are a fourth axis of test-time compute scaling, alongside neural net size, training data, and training flops. ([We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [27:15](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1635s))
- Coding is solved only for the kind of coding Cherny does — deep systems code, distributed systems, and pixel-level UI verification remain unsolved. ([We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md), [30:49](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1849s))
- Enjoyment is a velocity input: the weeks Steinberger enjoyed building, the product visibly improved; the weeks he didn't, he shipped config options. ([Fun Is Velocity](../talks/fun-is-velocity.md), [22:53](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1373s))

## All Talks

- [Fun Is Velocity](../talks/fun-is-velocity.md)
- [The 1% Rule for Building in AI](../talks/the-1-rule-for-building-in-ai.md)
- [We Cut 80% of Claude Code’s Prompt](../talks/we-cut-80-of-claude-codes-prompt.md)

## Speakers

- [Boris Cherny](../speakers/boris-cherny.md)
- [Jeff Dean](../speakers/jeff-dean.md)
- [Peter Steinberger](../speakers/peter-steinberger.md)

