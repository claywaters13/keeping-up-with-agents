---
title: "cognitive debt"
type: "concept"
slug: "cognitive-debt"
tier: "supporting"
maturity: "consolidating"
talk_count: 8
speaker_count: 9
---

# cognitive debt

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **8** talk(s) by **9** speaker(s)

**Definition:** Erosion of human understanding, skill, and ownership as work shifts to agents — the human-side cost of delegation.

*Also referred to as: cognitive surrender, human taste and judgment in agentic workflows, labor displacement from automation, code ownership spread, accountability and ownership, velocity sickness, sunk cost in codebases*

## State of Practice

The field has stopped arguing about whether agents can write code and started measuring what that costs the humans nominally in charge of it. The shared diagnosis is a widening gap between code that exists and code any human genuinely understands: eBay reports commits up 25% year over year while PR comments dropped 27%, median review time up 441.5%, and 31% more PRs merged with no review at all; Duolingo shows that reviewers scoring above 90% on calibration still accepted 50% of deliberately fabricated AI flags, which means reviewer skill is no defense against automation bias. The failure is specifically not a model-quality failure — it is an interaction-design and process failure, and the remedies proposed are correspondingly procedural: deterministic (not LLM-judged) PR scoring surfaced without blocking, human-authored PR bodies, a self-administered quiz before requesting review, friction deliberately inserted where stakes are high, and decisions extracted into durable shared docs rather than left in ephemeral chat. Several speakers converge on responsibility as the boundary that cannot move: agents can execute, route, and escalate, but cannot inherit consequences, so 'explain it or don't ship it' is the operational rule. What remains genuinely open is the prescription — whether engineers should invest in keeping up with their own codebases, or accept that models improve faster than people do and redirect that effort into scaling ambition and delegation infrastructure. Also unresolved and openly discussed: whether running more agents in parallel adds capacity at all, given that cognitive bandwidth does not parallelize and review is already the binding constraint.

## Consensus

### Verification, not generation, is now the binding constraint — cheaper code production does not make review cheaper, so review capacity is where agent-era throughput actually stalls.

Support: **5** talk(s)

> "AI is producing the pull request very fast, but humans cannot responsibly review them at that pace."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [1:40](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=100s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)

### Responsibility cannot be delegated to an agent: a human must remain able to explain and answer for shipped code, regardless of who typed it.

Support: **5** talk(s)

> "The agent can follow your runbook, but it can't inherit the consequences."
>
> — ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [13:25](https://www.youtube.com/watch?v=n97BCfyFIvw&t=805s)

Supporting talks: ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)

### Humans under agent output degrade into rubber stamps — deferring to AI recommendations without independent evidence — and skill or calibration does not prevent it.

Support: **4** talk(s)

> "despite the fact that our human reviewers are consistently scoring above 90% on their accuracy calibration metrics, they actually accepted 50% of these fake signals"
>
> — [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s)

Supporting talks: [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)

### Individual output gains from AI do not convert into team or customer impact — measured throughput rises while delivery does not, so the standard productivity metrics are vanity metrics.

Support: **3** talk(s)

> "I had the numbers, both the metrics and the token bills. So, I knew that engineering was, in fact, using AI, but he was right. Features certainly weren't making it to our customers any faster."
>
> — [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [0:42](https://www.youtube.com/watch?v=whue9_YquGA&t=42s)

Supporting talks: [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

### Degraded understanding accumulates and compounds like debt — unreviewed or ununderstood code becomes the grounding for the next agent-authored change, so the interest rate rises over time.

Support: **3** talk(s)

> "similarly to tech debt, you might get away with it for a little bit, but at some point you get burned if your understanding degrades"
>
> — [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [5:09](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=309s)

Supporting talks: [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)

## Disagreements

### Should engineers invest effort in maintaining their own understanding and skill, or redirect that effort into scaling ambition and delegating more?

| Position A | Position B |
|---|---|
| Understanding is the thing worth protecting: gate review requests on being able to pass a quiz about what the agent wrote, fix some bugs by hand to keep peripheral feel for the system, write the PR body yourself, and refuse to ship what no human can explain.<br>*[Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)* | You cannot outpace the models, so trying to level yourself up is the wrong investment — increase project ambition instead, treat implementation as no longer human work, and replace each stage of your own pipeline with agents.<br>*[Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)* |

*Why it matters: It determines whether team practice adds deliberate speed regulators (quizzes, hand-debugging, human-written rationale) or removes them in favor of throughput and scope. Get it wrong in one direction and you cap velocity; wrong in the other and you end up with a codebase nobody on the team can defend during an incident.*

### Is the fix for automation bias to slow humans down with deliberate friction, or to make verification so cheap and automated that humans are needed less?

| Position A | Position B |
|---|---|
| Insert friction exactly where stakes are high, reframe the human as investigator rather than validator, hold AI PRs to the same standard as human PRs, and treat the quiz as a speed regulator — the interaction must force deliberation.<br>*[Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)* | Safety comes from making verification cheaper, clearer, and harder to skip — automate the loop (AI reviewers plus auto-fix agents committing back to the PR), and accept that the human role in correctness checking is declining, which is fine.<br>*["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)* |

*Why it matters: Friction-first designs cost throughput now to keep labels and judgment honest; automation-first designs recover throughput but risk the exact compounding effect Duolingo measured, where rubber-stamped approvals get logged as truth and make the next model more confident and the human less engaged.*

### Does running more agents in parallel actually increase a team's effective capacity?

| Position A | Position B |
|---|---|
| No — cognitive bandwidth does not parallelize, and each additional loop adds routing, merging, and verification decisions; parallelism just relocates the jam to review, where PRs pile up unreviewed.<br>*["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)* | Yes, given the right substrate — isolated cloud workspaces per agent, AI assets embedded in repos, and a machine-readable model of the codebase make parallelism nearly free; with self-orchestrating models it needs no custom software factory at all.<br>*[Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* |

*Why it matters: It decides whether the next infrastructure dollar goes into agent fan-out (workspaces, orchestration, world models) or into review and understanding capacity. Ramp's own numbers show the tension: 21x automated PRs alongside PRs stuck waiting for review.*

## Practical Guidance

**Do:**

- Gate sending code for team review on passing a self-administered quiz about what the agent wrote — reading the agent's explanation is not evidence you understood it
- Make the human author write the PR body; the 'why' is the moment the author commits to understanding what they are shipping
- Score every PR with a fully deterministic computation (not an LLM judge) and post it as a comment without blocking the merge
- Calibrate scoring weights against your own reviewers' experience by backfilling over the last 200 merged PRs instead of adopting defaults
- Track the slope of review debt over time rather than its absolute level
- Frame AI signals in reviewer-facing copy as preliminary alerts requiring independent evidence — that copy change alone moved rejection rates 21% at Duolingo
- Add friction deliberately where stakes are high and remove it where oversight is low
- Split conflated yes/no CTAs into separate questions (was the model's perception correct vs. should we act on it), and log the human's subsequent manual edit, not just the accept/reject
- Confirm that agent-written tests assert what the code should do, not what it currently does
- Move decisions into durable, shared, commentable docs before implementation, so agents start stateless from the same state and 'agent bankruptcy' stops being a thing
- Keep agent conversations and plans in shared spaces rather than individual local terminals — understanding is a team-level property
- Fix some bugs yourself to retain the peripheral feel for the system you lose by delegating the whole fix
- Use agents to build throwaway micro-worlds whose only purpose is helping you understand existing software
- Define success metrics and the data you need before building the system, rather than asking afterward how to evaluate the model
- Embed AI assets into repos per repo shape (web, mobile, monorepo) rather than mandating one config top-down or training individuals one at a time

**Avoid:**

- Treating PR count, median PR size, and cycle time as productivity wins — cycle time drops precisely when reviewers stop pushing back
- Assuming calibrated, high-accuracy reviewers are protected from automation bias
- Adding more human oversight as the fix when the defect is in the interaction design
- Coding-agent UX that offers either one giant diff or per-file accept/reject — both reduce the developer to a rubber stamp and yield low-information labels
- Thumbs up/down as your feedback mechanism
- LLM-judged PR scores — the same PR scores differently when the model changes, and the number is not defensible to leadership
- Penalizing AI authorship as a proxy for review burden; structural complexity and volume drive burden, and detection can be defeated (one repo showed 0% despite agent-authored code)
- Exempting AI-authored PRs from the normal review standard
- Letting an agent make a critical decision — at that point you have ceded ownership of the code to the agent
- Expecting local developer machines to support real multi-agent parallelism
- Delivering LLM writing feedback as a long block that rewrites the user's passage instead of inline, span-anchored suggestions
- Automating a request pipeline without scoping discipline — you get a token-maxing slop cannon
- Having an LLM summarize sessions after the fact instead of extracting decisions into docs up front

## Notable Outliers

- Building an autonomous engineering org may directly contribute to the layoffs of the very people who built it, and the industry has not reckoned with where this leads. ([Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md), [16:49](https://www.youtube.com/watch?v=whue9_YquGA&t=1009s))
- Taste is not a durable moat — it is alpha that decays as models learn from examples and preferences, just more slowly than speed or recall, and it often functions as a magic word for work we don't want to explain yet. (["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [7:20](https://www.youtube.com/watch?v=n97BCfyFIvw&t=440s))
- The human role in correctness checking is declining and will keep declining — and that is a good thing; understanding matters for creative participation, not for verification. ([Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [3:16](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=196s))
- Across 524 PRs in three public repos, AI authorship stayed flat at 5-20% while review burden varied widely — complexity drives burden, not authorship. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [17:56](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1076s))
- Because you cannot outpace the models, the correct response is to increase project ambition rather than to try to improve your own skills — if your idea doesn't feel stupid, it isn't big enough. ([Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [15:27](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=927s))
- Rubber-stamped approvals get logged as ground truth, making the model spuriously more confident over time while the human is progressively discouraged from thinking — the bias is self-reinforcing through the training loop. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [10:39](https://www.youtube.com/watch?v=CDqzWpwkSls&t=639s))
- Plans that get written and then deliberately not implemented are a positive signal, because it means ideas are being explored and prioritized rather than built by default. ([Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md), [14:08](https://www.youtube.com/watch?v=Kz4QJmNrVXU&t=848s))

## All Talks

- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Building an Autonomous Engineering Org](../talks/building-an-autonomous-engineering-org.md)
- [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)
- ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)
- [Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster](../talks/velocity-sickness-what-happens-when-your-whole-team-gets-10x-faster.md)

## Speakers

- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Benjamin Guo](../speakers/benjamin-guo.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [Leo Mehr](../speakers/leo-mehr.md)
- [Matt Dailey](../speakers/matt-dailey.md)
- [Rob Cheung](../speakers/rob-cheung.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)

