---
title: "ai-assisted code review"
type: "concept"
slug: "ai-assisted-code-review"
tier: "core"
maturity: "contested"
talk_count: 12
speaker_count: 14
---

# ai-assisted code review

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **12** talk(s) by **14** speaker(s)

**Definition:** Using models or agents to review diffs and pull requests — reviewer agents, review personas, and where automated review fits in the pipeline.

*Also referred to as: ai code review, automated code review, asynchronous code review, persona-based review agents, reviewer agent with fresh context, multi-pass agent review, shift-left code review*

## State of Practice

The field agrees the constraint has moved: generation is cheap and review capacity is now what gates delivery, with eBay reporting median PR review time up 441.5% and 31% more PRs merged with no review at all, and Netflix, Anthropic, and Notion all describing review queues rather than authoring as the pinch point. The working architecture that emerged is layered and adversarial: never let the agent that wrote the code be its only grader, run deterministic static analysis alongside LLM review, split review into specialized passes (security separate from correctness, performance separate from both), and run verification inside the inner agentic loop so findings are auto-fixed before a PR ever opens. Everyone converged on the same failure diagnosis — models lack org-specific context (internal frameworks, business definitions, threat models), which is why 20–40% of model-written code carries a vulnerability and why teams now ship repo-resident review assets: markdown anti-pattern catalogs in a central Git repo, librarian layers for business semantics, machine-readable service graphs. Where the field splits hard is the human: Anthropic is deliberately removing humans from review of non-core changes and claims auto mode's prompt-injection/exfiltration risk is below an average human reviewer, while Netflix, eBay, and Sonar insist on mandatory human approval, citing that people rubber-stamp confidently wrong AI output nearly 80% of the time. The pragmatic middle that most speakers landed on is routing by criticality — read every line of auth, money movement, permissions, and irreversible data changes; let the loop handle the rest — plus attention-preserving rituals like requiring the human author to write the PR body or pass a quiz about the diff before requesting review.

## Consensus

### Review capacity, not code generation, is now the binding constraint on shipping — and it is not solved.

Support: **5** talk(s)

> "AI is producing the pull request very fast, but humans cannot responsibly review them at that pace."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [1:40](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=100s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

### The agent that wrote the code must not be its own verifier; review requires a separate agent with fresh context or, better, a different methodology entirely.

Support: **4** talk(s)

> "Use a different methodology to review the code that was used to write the code."
>
> — [Guide, Verify, Solve](../talks/guide-verify-solve.md), [9:49](https://www.youtube.com/watch?v=03l29gJXpCE&t=589s)

Supporting talks: [Guide, Verify, Solve](../talks/guide-verify-solve.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)

### Review quality is limited by missing organizational context — internal frameworks, business semantics, threat models — not by model intelligence, so that context must be supplied explicitly as durable repo artifacts.

Support: **5** talk(s)

> "while the models are very smart and capable, often times security is very contextual. And the model just might not have the context in order to know that it's introducing a vulnerability"
>
> — [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [10:41](https://www.youtube.com/watch?v=7JgIS42mz7U&t=641s)

Supporting talks: [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)

### Review must be decomposed into multiple specialized passes rather than issued as one general 'review this diff' prompt; bundling concerns degrades all of them.

Support: **4** talk(s)

> "you can't give them security at the same time as you give them correctness. They'll do a half-ass job of both."
>
> — [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [8:28](https://www.youtube.com/watch?v=yWS0udrIOc8&t=508s)

Supporting talks: [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)

### Automated review belongs inside the agent's inner loop with findings routed back to an agent to remediate, not only in CI after the PR is open.

Support: **4** talk(s)

> "The verification needs to run in both the inner agentic loop and also in the outer loop for CICD."
>
> — [Guide, Verify, Solve](../talks/guide-verify-solve.md), [18:11](https://www.youtube.com/watch?v=03l29gJXpCE&t=1091s)

Supporting talks: [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)

### Agents should open reviews, never merge or push to production themselves; merging with zero review of any kind is unacceptable practice.

Support: **3** talk(s)

> "Same essay, 31% increase in PRs merged with no review at all, human or agentic. Don't do this. I beg of you."
>
> — [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [10:19](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=619s)

Supporting talks: [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

## Disagreements

### Should humans be removed from the code review approval loop, or is human approval a permanent requirement?

| Position A | Position B |
|---|---|
| Remove humans from review for non-core changes now: AI review already catches 100% of issues in those categories, auto mode's residual prompt-injection and exfiltration risk is below that of an average human reviewer, and within 6–12 months the majority of shipped code will be reviewed by AI rather than humans. Human correctness-checking is declining and that is fine.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)* | Keep a mandatory human approval gate. Agents send a code review and never push, because modifying working production code is risky; AI PRs are held to the same review standard as human PRs with no exceptions; and for high-criticality code the quality gap must be closed by a human, since humans who do review still follow AI advice nearly 80% of the time when it is wrong.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)* |

*Why it matters: This decides whether you invest in months of eval and sandboxing infrastructure to retire the human gate, or in reviewer-attention accounting and criticality routing to keep it affordable. Get it wrong in the permissive direction and unreviewed code becomes the grounding for tomorrow's agent suggestions.*

### Is AI authorship itself a signal that a diff needs extra review scrutiny?

| Position A | Position B |
|---|---|
| Yes — AI-written code has a materially worse defect profile, not merely the same rate at higher volume; even after a dedicated hardening pass a scanner found 241 vulnerabilities, the best models introduce vulnerabilities in 20–40% of coding tasks, and AI tools leave a persistent increase in static analysis warnings and complexity. Every generated line needs far more scrutiny than code has ever had.<br>*[Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* | No — complexity drives burden, not authorship. Across 524 PRs in three public repos AI authorship stayed flat at 5–20% while review burden varied widely; authorship should be an amplifier worth ~5 of 60 debt points, and scrutiny should be routed by task criticality (auth, money movement, permissions, irreversible data) rather than by who typed the diff.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)* |

*Why it matters: It determines whether your review policy keys off a co-authored-footer detector — which one repo defeated entirely, showing 0% despite agent-authored code — or off diff shape and blast radius. The first approach is trivially gamed; the second costs more to instrument.*

### Should the review signal be a deterministic computation or a model judgment?

| Position A | Position B |
|---|---|
| Deterministic. The same PR scores differently once the model changes, which makes LLM-judged scores indefensible to leadership; you want a number traceable to a deterministic computation. Correspondingly, offload as much review cognition as possible to static scanners.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)* | Model judgment, structured for reliability. Use a jury of independent agents plus a consensus judge that weighs reasoning quality and escalates by expanding the jury when consensus is thin, or a classifier model judging the action plus conversation context — because many review questions have no empirically correct answer.<br>*[Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* |

*Why it matters: Deterministic scores are reproducible and auditable but only capture structural proxies; model juries capture judgment but drift silently across model upgrades, which is exactly the property that breaks year-over-year governance reporting.*

### Should verification be standardized on one platform, or built in-house and diversified?

| Position A | Position B |
|---|---|
| Standardize on a single independent multi-layered verification platform across all teams, projects, and AI coding tools, so there are no blind spots between them and constraints are centrally enforced.<br>*[Guide, Verify, Solve](../talks/guide-verify-solve.md)* | Build the loop yourself, or run many tools against each other. Vendors sell the same monitoring system but you know what you are looking for; nothing mature exists to buy for agent permissions; and for security you should get the open-source ones, the commercial ones, all of them, and have them check each other's work.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)* |

*Why it matters: Standardizing gives you one comparable score across the fleet but inherits one vendor's blind spots; diversifying catches more but leaves no single defensible number and multiplies integration cost per repo.*

## Practical Guidance

**Do:**

- Run security as its own pass, first and last over generated code, separate from the correctness pass
- Expect to put an LLM through four or five review passes over its own work before it is shippable
- Give the review agent a fresh context separate from the fix agent, since the fixer is biased toward its own diagnosis and eager to ship PRs
- Route scrutiny by criticality: read every line of authentication, money movement, permissions, and irreversible data changes; let the loop handle the rest
- Require the human author — not the agent — to write the PR body, and to confirm that tests assert what the code should do rather than what it does
- Gate sending code to teammates on being able to pass a quiz about what the agent wrote
- Post a deterministic review-debt score as a comment on every PR and never block the merge on it
- Calibrate scoring weights against your own reviewers by backfilling over the last 200 merged PRs instead of adopting defaults
- Make an automated canary comparing CPU, latency, and error rate a prerequisite before an agent-generated fix reaches a human reviewer
- Ask agents to decompose large changes into atomic reviewable PRs — they are better at it than humans — and use stacked diffs so specific subject-matter experts can review slices asynchronously
- Store review knowledge as hierarchically indexed markdown anti-pattern catalogs in a central Git repo rather than a vector database
- Pair every LLM review with computational/static review; neither technique alone is sufficient
- Run an auto-fix loop where a second agent commits fixes for issues the reviewer agent found
- Track the slope of review debt over time rather than its absolute level

**Avoid:**

- Asking one prompt for security and correctness together — you get a half-hearted job on both
- Letting the builder grade itself or write and score its own tests; that hides the review rather than removing it
- Treating passing tests as verification — agent-written tests assert current behavior including the bugs
- Trusting a completed 'security hardening pass' as sufficient; a scanner still found 241 vulnerabilities afterward
- Merging PRs with no review at all, human or agentic
- Reporting PR count, PR size, and cycle time as AI wins — they measure production speed, not trust, and cycle time drops precisely when reviewers stop pushing back
- Mandating AI reviewers before repo-level context assets exist; early reviewers were bad enough that forcing them only alienated engineers
- Letting agents push fixes directly to production, even well-verified performance fixes
- Dumping the entire codebase into the reviewing agent's context — it thrashes, explores, and burns tokens
- Relying on human review as the backstop, given that reviewers accept confidently wrong AI output nearly 80% of the time
- Using low-capability models or per-seat-subscription AI features as the harness for important review work
- Loading the full anti-pattern catalog at authoring time — it slows generation and consumes more tokens unless indexed

## Notable Outliers

- For prompt injection and data exfiltration specifically, an automated review mode's residual risk is far lower than that of an average human reviewer. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [31:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1914s))
- Across 524 PRs in three public repos, AI authorship stayed flat at 5–20% while review burden varied widely — complexity drives burden, not authorship. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [17:56](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1076s))
- Participants followed AI advice 92.7% of the time when it was correct and nearly 80% of the time when it was wrong, making human review an unreliable backstop. ([Guide, Verify, Solve](../talks/guide-verify-solve.md), [6:35](https://www.youtube.com/watch?v=03l29gJXpCE&t=395s))
- Within the next 6 to 12 months the majority of shipped code will be reviewed by AI rather than by a human. ([The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [13:14](https://www.youtube.com/watch?v=7JgIS42mz7U&t=794s))
- A PR score must be deterministic because the same PR will score differently when the judging model changes, which makes it indefensible to leadership. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [6:20](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=380s))
- Agents preferentially fix at the call site rather than the root cause, and review cost grows super-linearly with cross-file spread rather than with diff size. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [7:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=429s))
- Delegating a bug fix entirely to an agent forfeits the peripheral understanding of the system you would have gained by debugging it yourself. ([Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [13:19](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=799s))
- Agent queue-processing systems need adversarial supervisor agents, because any single agent will eventually fail. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [19:21](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1161s))

## All Talks

- [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [Guide, Verify, Solve](../talks/guide-verify-solve.md)
- [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)

## Speakers

- [Alex Bauer](../speakers/alex-bauer.md)
- [Alex Volkov](../speakers/alex-volkov.md)
- [Anirban Chatterjee](../speakers/anirban-chatterjee.md)
- [Cat Wu](../speakers/cat-wu.md)
- [Deepak Pathak](../speakers/deepak-pathak.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [Jack Cable](../speakers/jack-cable.md)
- [Rajat Shah](../speakers/rajat-shah.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Simon Willison](../speakers/simon-willison.md)
- [Steve Yegge](../speakers/steve-yegge.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)

