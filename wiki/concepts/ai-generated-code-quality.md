---
title: "ai-generated code quality"
type: "concept"
slug: "ai-generated-code-quality"
tier: "supporting"
maturity: "contested"
talk_count: 9
speaker_count: 9
---

# ai-generated code quality

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **9** talk(s) by **9** speaker(s)

**Definition:** Whether agent-written code is maintainable and correct beyond passing tests — slop, accumulated debt, and unverified output.

*Also referred to as: ai-generated code maintainability, ai-generated code slop, ai slop detection, code maintainability, functional correctness vs code quality, technical debt accumulation, verification debt, technical debt from prototypes*

## State of Practice

The field has stopped arguing about whether agents can produce working code and moved to arguing about what "working" leaves out. Speakers converged on a specific diagnosis: models now pass functional-correctness gates near-universally while still emitting high-complexity, insecure, sprawling diffs, so green tests are no longer evidence of shippable quality. The measured consequence is a velocity spike that decays — Carnegie Mellon data cited from two Sonar talks puts the 3-5x boost at roughly three months, with a persistent residue of static-analysis warnings and complexity — while eBay's PR telemetry shows commits up 25% against comments down 27%, median review time up 441.5%, and 31% more PRs merged unreviewed. The agreed structural fact is that generation got cheap and verification did not, so review attention, not typing, is the binding constraint, and unreviewed code compounds because it becomes grounding context for the next agent run. Where the field splits is the remedy: bake verification into the inner agentic loop and score every PR, versus abandon human reading entirely and push correctness down into type systems and language-level invariants. Nobody credible argued the problem solves itself with better models, though two talks expect the refactor-capability gap to close within six months.

## Consensus

### Functional correctness is an insufficient quality gate — state-of-the-art models pass tests while producing code that is complex, insecure, or wrong at the system level.

Support: **5** talk(s)

> "We give the models a series of over 4,000 problems and we basically ask it to generate the response to the problems and then we analyze both the functional correctness which is critical and they all do extremely well on this notion of functional correctness"
>
> — [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [4:42](https://www.youtube.com/watch?v=VrpEyglYgeU&t=282s)

Supporting talks: [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)

### Human review capacity is now the binding constraint on AI-generated code, and it is failing at agent output volume — rubber-stamping and unreviewed merges are already the norm, not an edge case.

Support: **6** talk(s)

> "AI is producing the pull request very fast, but humans cannot responsibly review them at that pace."
>
> — [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [1:40](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=100s)

Supporting talks: [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)

### Absent deliberate quality controls, AI coding accrues debt at least as fast as it generates code, so headline velocity gains erode rather than compound.

Support: **4** talk(s)

> "essentially, you're building the technical debt as quickly as you are generating the code or maybe even more quickly. And that creates a different set of work."
>
> — [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [7:14](https://www.youtube.com/watch?v=VrpEyglYgeU&t=434s)

Supporting talks: [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)

### Codebase cleanliness and context discipline are agent-efficiency levers measured in tokens and revisits, not just human ergonomics — clean repos do not raise pass rates but they cut token burn and thrashing.

Support: **4** talk(s)

> "found that clean and messy repos had roughly the same pass rates, but clean code actually used fewer tokens and caused fewer revisits"
>
> — ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [3:50](https://www.youtube.com/watch?v=n97BCfyFIvw&t=230s)

Supporting talks: ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)

### A permanent gap now exists between the code in the repo and the code any human understands; process should be designed around that fact rather than around a pretense that every line is read.

Support: **5** talk(s)

> "Slop is just any code you don't read. And whether any of you admit it or not, this is the least amount of slop that your code base will ever have. Cherish it."
>
> — [fighting slop with slop](../talks/fighting-slop-with-slop.md), [1:27](https://www.youtube.com/watch?v=AMiyLItEtLA&t=87s)

Supporting talks: [fighting slop with slop](../talks/fighting-slop-with-slop.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)

## Disagreements

### Should human code review remain a required control on AI-authored changes?

| Position A | Position B |
|---|---|
| Keep it and enforce it without exception: AI PRs meet the same review bar as human PRs, the human author writes the PR body and confirms tests assert intended behavior, and human review during large refactors also serves to spread codebase context across the team. Ship nothing no human can explain.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)* | Human reading is an unreliable formality that should not be the binding control — Boundary runs zero code reviews and enforces correctness through a type system and codebase invariants, while Sonar's data (developers accept confidently-wrong AI output nearly 80% of the time) argues the real gate must be automated multi-layer verification with the human review backstopped.<br>*[fighting slop with slop](../talks/fighting-slop-with-slop.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md)* |

*Why it matters: It determines whether you invest in reviewer headcount, PR-shaping and scoring instrumentation, or in compilers, invariants, and verification platforms — and whether accountability for an AI-caused incident attaches to a named human reviewer or to a tooling gate.*

### Should slop be prevented at generation time or accepted and remediated afterward?

| Position A | Position B |
|---|---|
| Slop is inevitable, so spend on detection and self-healing pipelines that remove it after the fact; hold the line on writing and design docs instead of on code, and explicitly exempt experimental code from rigorous standards.<br>*[Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md)* | Verification belongs inside the inner agentic loop so defects are fixed before they propagate into subsequent loops, and every PR should be scored for review debt as it lands — treating verification as an afterthought produces a self-reinforcing downward spiral.<br>*[Guide, Verify, Solve](../talks/guide-verify-solve.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)* |

*Why it matters: Post-hoc cleanup assumes debt is recoverable on demand; inner-loop verification assumes it compounds generatively because unreviewed code grounds the next agent run. Only one of these justifies slowing the generation loop down.*

### Does output quality come from picking a better model, or from the system built around it?

| Position A | Position B |
|---|---|
| Model selection measurably moves quality — Sonar's 4,000-task benchmark ranks models on maintainability, security, and complexity and recommends switching to Opus when those matter, and the same refactor that took 3 hours and 10 corrections with O3 now takes about a fifth of the time with Sonnet 4.6 / Opus 4.8.<br>*[Guide, Verify, Solve](../talks/guide-verify-solve.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)* | Raw intelligence lead no longer decides outcomes; put the intelligence in guardrails and system rigidity. GLM beat Opus on a real Cline repo bug at half the cost while Opus broke the production build; distrust of LLM code stems from insufficiently rigid underlying systems, not inadequate models; and a model that seems 'dumber' today usually means the harness or codebase setup changed.<br>*[Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [fighting slop with slop](../talks/fighting-slop-with-slop.md), [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)* |

*Why it matters: It decides where the budget goes: frontier-model spend and per-task model routing, versus harness engineering, type systems, and internal gateways on cheaper open-weights models.*

### What should an organization standardize — the AI tooling, or the codebase?

| Position A | Position B |
|---|---|
| Standardize the setup: derive one shared agent configuration from the team's best ICs and have engineers give up bespoke setups, and adopt a single independent verification platform across all teams, projects, and coding tools to eliminate blind spots.<br>*[Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* | Do not standardize how people use AI at all; standardize the codebase invariants instead, via a tiny model-agnostic architecture.md containing only things that will not change for months or years.<br>*[fighting slop with slop](../talks/fighting-slop-with-slop.md)* |

*Why it matters: Tooling standardization is a policy lever leadership can pull immediately but that Amazon's own experience says fails when mandated; invariant standardization requires rebuilding what the code enforces and pays off only if the enforcement is machine-checkable.*

## Practical Guidance

**Do:**

- Run verification inside the inner agentic loop as well as in CI/CD, and give agents the tooling and agency to remediate their own findings before the code propagates into the next loop.
- Verify with a different model and a different methodology than the one that generated the code — combine computational/static review with LLM-driven review rather than relying on either.
- Read agent time-horizon benchmarks at 80% success (ideally 90-99%), not the commonly published 50% — at 80% the achievable task length drops from ~18 hours to ~3.5 hours.
- Score every PR deterministically for review debt, post the score as a comment, and never block merges on it; calibrate the weights by backfilling over your last 200 merged PRs instead of adopting defaults.
- Make the human author write the PR body and confirm the tests assert what the code should do — agent-written tests default to asserting current behavior, bugs included.
- Cap skill.md at ~100 lines and treat a skill as a folder with detail deferred to other files; keep first-prompt baseline context to 20-25K tokens and treat 40-50K as a progressive-disclosure failure.
- Supply selective codebase context and explicit constraints rather than dumping the repo — measured at over 30% fewer tokens per problem plus less thrashing.
- Keep a tiny, model-agnostic architecture.md limited to invariants that will hold for months or years, instead of a tool-specific CLAUDE.md.
- Budget a standing percentage of IC time for harness and codebase setup that produces no immediate PRs, and treat that work as never finished.
- Adopt the rule 'explain it or don't ship it' — a human must be able to defend the change even if no human typed or read every line.
- Prefer a monorepo for agentic work: end-to-end testing, verification, deployment, and sandbox cloning remain much harder across multiple repos even though models navigate multi-repo trees fine.
- Track commit rate and breadth of contributing developers rather than lines of code, and explicitly exempt experimental/prototype code from the codebase's rigorous standards.

**Avoid:**

- Treating human code review as the quality gate — participants followed AI advice nearly 80% of the time when it was wrong, and rubber-stamping is already widespread.
- Using the same AI that wrote the code to validate it.
- Reporting PR count, median PR size, and cycle time as AI wins — they are real numbers but vanity metrics that measure production speed, not trust (one PR splitting into seven inflates count; cycle time falls when reviewers stop pushing back).
- LLM-judged PR scoring: the same PR scores differently after a model upgrade, which makes the number indefensible to leadership.
- Mandating agent usage top-down, and letting adoption go uneven — the 1-2 PR/day engineers inherit the review burden from the 10 PR/day engineers and turn hostile to agents.
- Babysitting agents: if engineers are watching runs, the codebase and harness setup is wrong, not the model.
- 'AI psychosis' — accepting a plausible 20-page deep research report or a stream of design docs as verified work; Boundary's own team ended up fighting its founder's 10-docs-a-day slop.
- Assuming clean code only matters to humans — agents have to understand the codebase to operate on it, and cleanup measurably cuts tokens and reasoning on identical tasks.
- Running more agents in parallel as a capacity strategy: cognitive bandwidth does not parallelize, and each loop adds routing, merging, and verification decisions.
- Shipping hacks labeled 'just temporary' — they run in production for 18 months and you support them indefinitely.
- Doing AI-native development without guardrails: it reproduces exactly the legacy-codebase pathology of large volumes of low-quality code nobody on the team understands.

## Notable Outliers

- Code review can be eliminated entirely — Boundary does zero code reviews, requires all engineers to work in parallel, and makes the type system the center of truth that keeps invariant violations out of the codebase. ([fighting slop with slop](../talks/fighting-slop-with-slop.md), [18:58](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1138s))
- Trust only the source: docs, readmes, and architecture files will lie, and in a world where nobody reads all the code the execution trace is the only real way to understand it. ([fighting slop with slop](../talks/fighting-slop-with-slop.md), [13:06](https://www.youtube.com/watch?v=AMiyLItEtLA&t=786s))
- A cheaper open-weights model produced better code than the frontier model on a real bug in Cline's own repo — GLM used twice the tokens at half the cost, cleaned up dead code and verified the build, while Opus left type errors and broke the production build. ([Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [9:44](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=584s))
- Agents are biased toward fixing at the call site rather than the root cause, and the resulting cross-file sprawl makes review cost grow super-linearly rather than in proportion to diff size. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [7:09](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=429s))
- Across 524 PRs in three public repos, AI authorship stayed flat at 5-20% while review burden varied widely — complexity drives burden, not authorship — so AI authorship should add reviewer attention as an amplifier, not a penalty (5 of 60 points on the high-debt example). ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [17:56](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1076s))
- Long agent run times are a good sign, not a bad one: under the reasoning paradigm the longer the agent thinks the better the output, and a skill running over an hour scared the team only until they saw the value. ([Agents, codebases, and teams](../talks/agents-codebases-and-teams.md), [12:20](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=740s))
- Model choice is a maintainability lever, not just a capability one — Sonnet 4.6 scores well on correctness and task-solving, but Opus is the better pick when maintainability, security, or low complexity are the priority. ([Guide, Verify, Solve](../talks/guide-verify-solve.md), [5:32](https://www.youtube.com/watch?v=03l29gJXpCE&t=332s))
- Taste is not a durable moat against agents — it is alpha that decays as models learn from examples and preferences, just more slowly than speed or recall. (["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [7:20](https://www.youtube.com/watch?v=n97BCfyFIvw&t=440s))

## All Talks

- [Agents, codebases, and teams](../talks/agents-codebases-and-teams.md)
- [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)
- [fighting slop with slop](../talks/fighting-slop-with-slop.md)
- [Guide, Verify, Solve](../talks/guide-verify-solve.md)
- [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)
- [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md)
- [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)
- ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)

## Speakers

- [Aditya Khandelwal](../speakers/aditya-khandelwal.md)
- [Anirban Chatterjee](../speakers/anirban-chatterjee.md)
- [Denys Linkov](../speakers/denys-linkov.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Saoud Rizwan](../speakers/saoud-rizwan.md)
- [Tariq Shaukat](../speakers/tariq-shaukat.md)
- [Vaibhav Gupta](../speakers/vaibhav-gupta.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)

