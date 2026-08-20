---
title: "ai-assisted code review"
type: "concept"
slug: "ai-assisted-code-review"
tier: "core"
maturity: "contested"
talk_count: 13
speaker_count: 15
---

# ai-assisted code review

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **13** talk(s) by **15** speaker(s)

**Definition:** Using models or agents to review diffs and pull requests — reviewer agents, review personas, and where automated review fits in the pipeline.

*Also referred to as: ai code review, automated code review, asynchronous code review, persona-based review agents, reviewer agent with fresh context, multi-pass agent review, shift-left code review*

## State of Practice

Review, not generation, is now the binding constraint: eBay measured commits up 25% year over year with PR comments down 27%, median review time up 441.5%, and 31% more PRs merged with no review at all, while Anthropic reports Claude Tag landing 65% of its product PRs. The field's answer is to stop treating review as a single human gate and decompose it into layered, mostly automated passes — static/computational analysis, a security-only pass, an LLM reviewer with fresh context, and an auto-fix agent — with the human retained for a narrowing set of high-criticality changes (auth, money movement, permissions, irreversible data) and for understanding rather than line-by-line defect hunting. The load-bearing methodological rule everyone converges on is separation: the agent that wrote the code (or its diagnosis) must not be the one that grades it, because self-scoring hides review rather than removing it. Practitioners also now attribute review burden to diff *shape* rather than authorship — agents fix at the call site instead of the root cause, sprawl across files and teams, ship a lower test-to-code ratio, and write tests that assert current behavior including bugs — so the fixes are structural (500-line PR caps, stacked diffs, forcing the human to write the PR body). The unresolved fault line is how far the human can be removed: Anthropic claims its auto mode's residual risk is already below the average human reviewer's and is explicitly engineering humans out of the loop for non-core changes, while Netflix, eBay, and Maven Clinic insist a human must still approve anything touching working production code. Meanwhile the honest data is uncomfortable — humans accept confidently wrong AI output nearly 80% of the time, and one survey reports 242% more incidents per PR.

## Consensus

### Review throughput, not code generation, is now the binding constraint on shipping — agents produce PRs faster than any human review process can responsibly absorb.

Support: **6** talk(s)

> "AI is producing the pull request very fast, but humans cannot responsibly review them at that pace."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [1:40](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=100s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

### Verification must be performed by a different agent, model, or methodology than the one that produced the code; an agent grading its own output is not review.

Support: **6** talk(s)

> "Use a different methodology to review the code that was used to write the code."
>
> — [Guide, Verify, Solve](../talks/guide-verify-solve.md), [9:49](https://www.youtube.com/watch?v=03l29gJXpCE&t=589s)

Supporting talks: [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)

### Rubber-stamping and no-review merges are the dominant real-world failure mode; AI-authored PRs must be held to the same review standard as human-authored ones, with no exemption.

Support: **4** talk(s)

> "Same essay, 31% increase in PRs merged with no review at all, human or agentic. Don't do this. I beg of you."
>
> — [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [10:19](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=619s)

Supporting talks: [Guide, Verify, Solve](../talks/guide-verify-solve.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

### Review cost is driven by the structural shape of agent-authored diffs (cross-file sprawl, size, weak tests), not by the fact of AI authorship, so large changes must be decomposed into small atomic PRs before review.

Support: **4** talk(s)

> "The review cost of a sprawling difference is not proportional to the size. It is actually much steeper."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [7:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=429s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Research to Reality: Bringing Frontier ML Research to Production](../talks/research-to-reality-bringing-frontier-ml-research-to-production.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

### Model intelligence does not close the quality gap, because security, performance, and convention correctness are contextual — the model lacks your threat model, internal platforms, and codebase patterns — so each needs its own dedicated review pass.

Support: **4** talk(s)

> "while the models are very smart and capable, often times security is very contextual. And the model just might not have the context in order to know that it's introducing a vulnerability"
>
> — [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [10:41](https://www.youtube.com/watch?v=7JgIS42mz7U&t=641s)

Supporting talks: [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)

### Automated review should act as non-blocking guardrails that route findings back to an agent for remediation, rather than as a merge gate that stops delivery.

Support: **4** talk(s)

> "Post the score as a PR comment on every PR. Don't block it."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [21:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1269s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)

### Today's AI code reviewers are a useful supplement but are not yet trustworthy enough to be the sole approver for changes to working production code.

Support: **4** talk(s)

> "We also tried the multiple like AI coding review review tools. It helps a little bit, but we don't feel comfortable 100% rely on them yet."
>
> — [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [10:50](https://www.youtube.com/watch?v=WJRdLNhrsLQ&t=650s)

Supporting talks: [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

## Disagreements

### Can humans be removed from the code review loop today, or must a human remain the final approver?

| Position A | Position B |
|---|---|
| Yes — for non-core changes automated review already catches 100% of issues, and the explicit goal is a world where humans are not in the loop; within 6–12 months the majority of shipped code will be reviewed by AI, and an agent pair (fixer + reviewer) can already out-ship a small human team by 10x.<br>*[Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)* | No — a human must approve before anything modifies working production code, PRs merged with no review at all are unacceptable practice, and authentication, money movement, permissions, and irreversible data changes must still be read line by line.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)* |

*Why it matters: This determines whether you invest in scaling human review capacity (PR size caps, scoring, reviewer routing) or in the eval and sandboxing infrastructure needed to retire it — and who is accountable when an AI-approved change causes an incident.*

### Which is the more reliable check on AI-generated code: the human reviewer or the automated one?

| Position A | Position B |
|---|---|
| The human is the weak link — participants followed AI advice nearly 80% of the time even when it was wrong, rubber-stamping is already widespread, and for prompt injection and data exfiltration an automated classifier's residual risk is below that of the average human reviewer.<br>*[Guide, Verify, Solve](../talks/guide-verify-solve.md), [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)* | The automated reviewer is the weak link — AI code reviewers were bad enough that mandating them was counterproductive, teams are not comfortable relying on them 100%, and human engineer feedback plus human understanding of the system remains the thing that actually catches problems.<br>*[Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)* |

*Why it matters: If humans are the weak link, adding reviewers is wasted spend and the fix is automation plus different-methodology verification; if the automation is the weak link, mandating AI reviewers degrades trust and slows the team.*

### Should review verdicts be anchored in deterministic computation or in agent judgment?

| Position A | Position B |
|---|---|
| Deterministic — a score must be traceable to a fixed computation because LLM-judged scores shift when the model changes and are not defensible to leadership; computational/static review is a required layer, not an optional one.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* | Agentic — rule-based checks, regex, and scripted simulations cover only one slice of failure, and analyzing what actually happened requires enough reasoning that it must itself be done by an agent; for questions with no empirically correct answer, use a jury of independent agents with a consensus judge.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)* |

*Why it matters: It decides whether review output is a stable, auditable metric you can govern and trend over time, or a richer but non-reproducible judgment that changes underneath you at every model upgrade.*

### What is human reading of agent-written code actually for — catching defects, or preserving understanding?

| Position A | Position B |
|---|---|
| Understanding. Correctness checking by humans is declining and that's fine; the reason to read is to stay a creative participant, and the gate should be whether you can pass a quiz on what your agent wrote (or, at minimum, whether you wrote the PR body yourself).<br>*[Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)* | Defect catching on critical paths. The question is what proof this specific change needs; auth, money movement, permissions, and irreversible data get read line by line, and profiler estimates plus tests are insufficient proof without a canary giving ground truth.<br>*[Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* |

*Why it matters: The two goals imply opposite process designs: understanding-first means shared agent transcripts, explainer artifacts, and comprehension gates; defect-first means criticality routing, canaries, and layered scanners.*

### Should an organization standardize on one verification/review toolchain or run many in parallel?

| Position A | Position B |
|---|---|
| Standardize — teams, projects, and AI coding tools should all report into a single independent multi-layered verification platform, because fragmented tooling leaves blind spots.<br>*[Guide, Verify, Solve](../talks/guide-verify-solve.md)* | Diversify — get the open-source scanners, the commercial ones, all of them, and have them check each other's work; support multiple competing coding tools because engineer preference shifts yearly; and let each repo's champion pick its own agent configuration rather than mandating one shape.<br>*[Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)* |

*Why it matters: Standardization buys comparable metrics and one integration surface; diversity buys coverage of each tool's blind spots and adoption that survives the next tooling shift.*

## Practical Guidance

**Do:**

- Split review into separate single-concern passes — security first and last, correctness, performance, standards — because combining security and correctness in one prompt produces a half-done job on both; expect up to four or five passes before an LLM's work is shippable.
- Run the fix-generating agent and the review agent as separate agents with fresh context, since the fixer is biased toward its own diagnosis and eager to open PRs.
- Cap PRs at 500 lines and use stacked diffs (e.g. Graphite) so review is asynchronous and each slice can be routed to the right subject-matter expert.
- Make the human author, not the agent, write the PR body — that is the moment they commit to understanding what they are shipping — and have them confirm the tests assert what the code *should* do rather than what it currently does.
- Gate sending code to teammates on being able to pass a quiz about what the agent wrote; reading an explanation is not evidence of understanding.
- Run verification inside the inner agentic loop, not only in CI/CD, so defects are caught before they propagate into subsequent loops.
- Require an automated canary comparing CPU, latency, and error rate before an agent-generated change reaches a human reviewer — the profiler gives an estimate, the canary gives ground truth.
- Post a deterministic review-burden score as a comment on every PR, backfilled and calibrated against your own last ~200 merged PRs, and track its slope rather than its absolute level.
- Route by criticality: read every line of authentication, money movement, permissions, and irreversible data changes; let low-criticality changes ride on automated verification.
- Gate high-stakes decisions on agreement between two different models and escalate to a human when they disagree.
- Add an auto-fix loop so that issues the AI reviewer identifies are fixed by another agent and committed to the PR rather than queued for a human.
- Give agents isolated cloud workspaces rather than local machines once you run them in parallel, since local dev boxes cannot support real multi-agent parallelism.

**Avoid:**

- Letting the same agent that wrote the code write and grade its own tests — if the builder grades itself you didn't remove the review, you hid it.
- Merging PRs with no review at all, human or agentic, and the rubber-stamp approval that gives false confidence.
- Treating PR count, PR size, and cycle time as evidence of AI success — they measure the speed of production, not the speed of trust, and cycle time falls precisely when reviewers stop pushing back.
- Penalizing PRs for AI authorship: complexity drives review burden, not authorship, and authorship detection is defeatable (co-authored footers can read 0% on agent-authored repos).
- Letting agents push fixes directly to production; modifying code that is already running fine is exactly the risky case.
- Introducing review agents before the ordinary foundations — test coverage, observability, canaries, verification logic — are solid, or they will create more friction and more production bugs than they remove.
- Mandating an AI code reviewer before it is actually good; shipping a bad reviewer burns engineer trust and makes later adoption harder.
- Trusting a single scanner's claims — run several and have them check each other's work; one vendor found 241 vulnerabilities in a codebase that had already passed a model-run security hardening pass.
- Dumping the whole codebase into the reviewing agent's context; it thrashes, explores, and burns tokens.
- Assuming a newer model will fix quality — it has no knowledge of your internal platforms, frameworks, or codebase patterns, and even the best models introduce vulnerabilities in 20–40% of coding tasks.

## Notable Outliers

- For prompt injection and data exfiltration specifically, an automated auto-mode classifier's residual risk is already far lower than that of the average human reviewer — and essentially every attack found by commissioned red teams has been mitigated. ([Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md), [31:54](https://www.youtube.com/watch?v=uU5Gv2h8-9g&t=1914s))
- Participants followed AI advice 92.7% of the time when it was correct — but also nearly 80% of the time when it was wrong, which makes human review an unreliable backstop by construction. ([Guide, Verify, Solve](../talks/guide-verify-solve.md), [6:35](https://www.youtube.com/watch?v=03l29gJXpCE&t=395s))
- Agents are biased toward fixing at the call site while human engineers route the fix to the root cause, which is why agent diffs sprawl across files and teams. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [7:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=429s))
- Across 524 PRs in three public repos, AI authorship stayed flat at 5–20% while review burden varied widely — complexity drives burden, not authorship. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [17:56](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1076s))
- The rule for delegating: don't send code to teammates for review unless you can pass a quiz about what your agents wrote — the quiz is the speed regulator that keeps you moving at the speed of understanding, not just correctness. ([Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [10:55](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=655s))
- Sequencing matters more than automation: close the loop and make yourself the bottleneck first, then remove the human — don't remove the human up front. ([The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [11:38](https://www.youtube.com/watch?v=kZsf_Sfm7RU&t=698s))
- AI output gains carry a measurable stability cost — 242% more incidents per PR and 6x more bugs per developer than 2025. ([Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [10:19](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=619s))
- Security is the one defect class with no half-life of urgency, so it must be both the first review pass and the last one over generated code. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [13:23](https://www.youtube.com/watch?v=yWS0udrIOc8&t=803s))

## All Talks

- [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Claude Fable, Claude Tag, and Anthropic's Culture](../talks/claude-fable-claude-tag-and-anthropics-culture.md)
- [Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers](../talks/design-patterns-for-ai-trust-juries-libraries-and-agent-tiers.md)
- [Guide, Verify, Solve](../talks/guide-verify-solve.md)
- [How to build an AI-Native Health Company](../talks/how-to-build-an-ai-native-health-company.md)
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
- [Dan Feng](../speakers/dan-feng.md)
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

