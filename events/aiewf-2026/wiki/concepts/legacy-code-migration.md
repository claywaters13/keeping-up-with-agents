---
title: "legacy code migration"
type: "concept"
slug: "legacy-code-migration"
tier: "supporting"
maturity: "consolidating"
talk_count: 7
speaker_count: 7
---

# legacy code migration

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **7** talk(s) by **7** speaker(s)

**Definition:** Using agents to modernize, refactor, or port existing systems at a scale that was previously not worth the human cost.

*Also referred to as: legacy codebase refactoring, incremental code migration, technical debt remediation, monorepo consolidation, agent framework migration, dependency patching automation, automated patching and patch validation*

## State of Practice

The economics flipped in 2025-2026: migrations that were never worth the human cost — COBOL/JCL modernization, ETL ports, 150-procedure RPC rewrites, CVE backlogs across thousands of repos — are now routinely staffed with agents, with reported results like a 50-engineer ETL migration delivered in a third of the timeline and a refactor that took 3 hours and 10 corrections on O3 taking roughly a fifth of that on Sonnet 4.6/Opus 4.8. The architecture that has converged is a boring deterministic wrapper around an agentic core: the agent only edits files on disk, while push, PR creation, CI triggering, and approval interrupts live in deterministic code, because that split is effectively the security model. Verification is the hard part, not generation — the field agrees you must not verify with the same model or methodology that generated the change, and Anthropic's security work goes further by running discovery and verification as separate agents with the verifier denied the discovery agent's reasoning traces. Work is decomposed rather than batched: each migration unit gets its own context window, agents are told to make the smallest change that fixes the specific defect, and loops are throttled to one unreviewed PR at a time because human review capacity, not compute, is the binding constraint. The unresolved tension is autonomy: some teams run unattended remediation loops in CI today, while others insist models still cannot self-validate a substantial multi-repo refactor and that you should start hands-on-the-wheel.

## Consensus

### Agents have made large-scale legacy migration and refactoring economically viable — work previously deferred indefinitely because nobody wanted to touch the code is now being shipped.

Support: **5** talk(s)

> "taking on technical debt and refactoring later is getting exponentially easier as the days go by."
>
> — [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [12:45](https://www.youtube.com/watch?v=7vn4WpqNpck&t=765s)

Supporting talks: [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)

### Verification of migrated code must be independent of generation — a different methodology, tool, or agent than the one that wrote the change, run inside the loop rather than only at CI.

Support: **4** talk(s)

> "Use a different methodology to review the code that was used to write the code."
>
> — [Guide, Verify, Solve](../talks/guide-verify-solve.md), [9:49](https://www.youtube.com/watch?v=03l29gJXpCE&t=589s)

Supporting talks: [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)

### The migration harness should be a deterministic shell around an agentic core: the agent edits files, while credentials, PR creation, CI triggering, and approval gates stay in deterministic code.

Support: **4** talk(s)

> "The dangerous ones, the get up right access, um and trigger UCI is something that we did not give the agent. Instead, we pushed um that functionality out to the deterministic part"
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [11:53](https://www.youtube.com/watch?v=LqLoYksJ6do&t=713s)

Supporting talks: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)

### Migrations should be decomposed into small units each getting its own fresh context window, rather than batched into one large agent run or one large context dump.

Support: **4** talk(s)

> "we could have our controller pick three or five and then do each of those in a separate implementation phase, which will be both cheaper and more reliable since each migration gets its own context window"
>
> — [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [16:29](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=989s)

Supporting talks: [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)

### Human review capacity — not model capability or compute budget — is the real throughput ceiling on agent-driven migration, so pipelines must be throttled and findings curated to what humans can actually absorb.

Support: **3** talk(s)

> "No human reviewed the last output, so there's no reason to stack up even more work for humans to review."
>
> — [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [15:57](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=957s)

Supporting talks: [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)

### Unguarded agent-generated code recreates the exact pathologies of legacy codebases — high volume, rising complexity and static-analysis warnings, and nobody on the team understanding it.

Support: **3** talk(s)

> "when you build a lot of code and you do this kind of development in an AI AI-native world, it starts looking like some of the legacy code we've we've seen in the past."
>
> — [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [12:45](https://www.youtube.com/watch?v=7vn4WpqNpck&t=765s)

Supporting talks: [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)

## Disagreements

### Should migration agents be run as unattended automated loops today, or kept hands-on-the-wheel with a human gating every change?

| Position A | Position B |
|---|---|
| Run them autonomously now: a deterministic controller spawns agents against a tracked violation queue, agents are given agency and tooling to remediate their own verification findings, and the whole thing lives in CI — human review is an unreliable backstop anyway, since people accept confidently-wrong AI output nearly 80% of the time and rubber-stamping is already endemic.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* | Start interactive and keep humans in the driver's seat: fully automated patch review is not yet practiced at most companies, a human should confirm patches before merge, mutating tool calls should deterministically interrupt the loop, and kicking off a long unattended run at today's per-task success rates mostly wastes the hour.<br>*[Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)* |

*Why it matters: It determines whether you invest in automated verification tooling and blast-radius containment (micro VMs, deterministic credential layers) or in review workflow and approval UX. Getting it wrong either caps your migration at human review bandwidth or ships unreviewed changes into production from a supply-chain actor.*

### Is code generation itself a solved problem for legacy migration, with the remaining difficulty in the surrounding lifecycle?

| Position A | Position B |
|---|---|
| Yes — with enough context engineering the models reliably produce the code blocks you want, including in COBOL and JCL; roughly 80% of the problem is testing, reviewing, deploying, and maintaining the result across the enterprise, so the leverage is in the harness and the org, not the generation step.<br>*[How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)* | No — frontier models still cannot self-validate or one-shot a substantial multi-repo refactor (GPT 5.5 extra high produced scaffolding and silently omitted the model implementations in 10 minutes and 2,000 lines), and AI-generated code carries a persistent increase in static analysis warnings and complexity that must be closed for high-criticality systems.<br>*[Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)* |

*Why it matters: If generation is solved, you staff migrations by scaling agent deployment and delivery process; if it isn't, you must spend engineering effort on golden patterns, deterministic sensors, and quality gates before the loop is safe to run at all.*

### Is a large legacy migration best handled as one consolidated restructuring project, or ground down incrementally by a throttled control loop?

| Position A | Position B |
|---|---|
| Pause and do the big one: a six-month monorepo consolidation was worth doing in 2025 rather than waiting a year for better models, with all-human PR review throughout — the monorepo is what makes end-to-end testing, verification, deployment, and sandbox cloning tractable for agents afterward.<br>*[Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)* | Never batch: measure the violations, sort them deterministically into version control, and let a control loop pick three to five per phase with one open PR at a time — batching produces 40,000-line PRs that nobody wants to read, and bad code is more expensive in the age of agents than ever before.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* |

*Why it matters: One path front-loads a multi-month freeze on feature work and bets on human review to spread codebase context; the other spreads the cost across quarters but requires building measurement sensors and a controller before any migration value lands.*

## Practical Guidance

**Do:**

- Run one full deterministic scan on main, sort every violation deterministically, and commit the resulting worklist to version control so the loop has a stable, resumable queue
- Use AST-grep as the loop's sensor rather than lint or TypeScript config rules, because it is language-agnostic and out-of-band from configs that coding agents disable with inline comments
- Cap the loop at one open PR at a time — block a new PR until the previous one has been reviewed by a human
- Have the controller pick three to five migration units per phase, each executed in its own separate context window
- Hand-write golden pattern examples in the repo before setting the loop loose; coding agents are pattern replicators and will follow in-repo idiom over internet-derived knowledge
- Keep push, PR-creation, and CI-trigger credentials out of the agent entirely; let the agent only modify files on the filesystem and put the write path in the deterministic wrapper
- Instruct the agent to make the smallest effective change that fixes the specific CVE or violation, rather than bumping to latest
- Run discovery and verification as separate agents, and deny the verification agent access to the discovery agent's reasoning traces so it starts from the assumption that the finding is false
- Run verification in the inner agentic loop as well as the outer CI/CD loop, so defects are caught before they propagate into subsequent iterations
- Require two hard gates on any remediation: the original reproduction must stop working, and the existing test suite must stay green
- Give the agent dynamic tools — API queries, logs, live sandboxed systems it can detonate a PoC against — rather than source code alone; this pushed true positive rates to nearly 100%
- Ask the agent for a short retrospective at the end of every invocation: what went well, what went wrong, what tools were missing, what context would help next time
- Evaluate model time-horizon claims at the 80%+ success rate, not the commonly published 50%, since that is where delegation actually pays off
- Keep the migration target in a monorepo — end-to-end testing, verification, deployment, and sandbox cloning are still much harder across multiple repos
- Track commit rate and the breadth of developers contributing as the payoff signal, not lines of code
- Run the loop on your existing CI (GitHub Actions, GitLab, CircleCI) — it already has your code and secrets; a dedicated cluster is unnecessary
- If the agent genuinely needs Docker, isolate it in a micro VM (Firecracker) with Vsock-mediated networking

**Avoid:**

- Blind prompt-in-a-bash-loop setups on team-owned or critical systems — even with verifier and code-review agents attached, they produce 40,000-line PRs nobody reads
- Giving an agent Docker socket access, and trusting the sandboxes shipped with Codex or Claude once you have; the agent can spawn a privileged container and escape to the host
- Dumping the entire codebase into the agent's context up front — it thrashes, explores, and burns tokens
- Bumping dependencies to latest rather than minimally patching; one such PR changed 70,000 lines
- Using the same model or methodology to verify code that generated it
- Assuming manifest-based tools like Dependabot and Renovate cover your exposure — CVEs in base-image OS packages and build-time downloaded binaries are structurally invisible to them
- Sending product engineers every true finding including medium and low severity; curate to a top 10-20 or you lose their trust permanently
- Trusting a 20-page deep research report at face value — the features it describes may not exist in the product, and acting on it sets you back
- Letting the agent revert its own prior changes — this is a known failure mode you must explicitly prompt against
- Deploying agents at a legacy codebase with no specific direction, which is just token maxing with no tangible outcome
- Using an agent for a job deterministic code can do, including vulnerability routing that simple code-owner heuristics already solve

## Notable Outliers

- The blast radius of an agent is an architecture decision — the line you draw between deterministic and agentic components *is* your security model. ([We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [21:04](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1264s))
- Prompts should shrink roughly 50% with every step-jump model version; on newer models 'look for where untrusted data hits the trust boundary' outperforms a prescriptive prompt. ([Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [9:51](https://www.youtube.com/watch?v=imFedndyXYQ&t=591s))
- Human PR review during a refactor is valuable not primarily as a quality gate but as the mechanism that spreads codebase context among developers. ([Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [16:05](https://www.youtube.com/watch?v=7vn4WpqNpck&t=965s))
- Agents can now operate across COBOL, JCL, and other languages people no longer learn because they are not fun or interesting — making the most complicated legacy codebases in the world addressable. ([How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [14:49](https://www.youtube.com/watch?v=RVxym6mmIns&t=889s))
- Model choice should be split by objective within a migration: Sonnet 4.6 for correctness and task-solving, Opus when maintainability, security, or low complexity are the priority. ([Guide, Verify, Solve](../talks/guide-verify-solve.md), [5:32](https://www.youtube.com/watch?v=03l29gJXpCE&t=332s))
- Scaling the migration harness is a solved problem because it only costs compute and money; the unsolved constraints are entirely human and organizational, and an order of magnitude harder. ([Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md), [17:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=1051s))
- The 'code is read-only now' thesis is unproven and prohibitively expensive for anyone without a frontier lab's token budget; well-designed loops make code easier to read rather than making reading unnecessary. ([Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [4:10](https://www.youtube.com/watch?v=xIt_mTQp6mY&t=250s))

## All Talks

- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)
- [Guide, Verify, Solve](../talks/guide-verify-solve.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [Using LLMs to Secure Source Code](../talks/using-llms-to-secure-source-code.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)

## Speakers

- [Anirban Chatterjee](../speakers/anirban-chatterjee.md)
- [Denys Linkov](../speakers/denys-linkov.md)
- [Eugene Yan](../speakers/eugene-yan.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Jia Wu](../speakers/jia-wu.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [Moritz Johner](../speakers/moritz-johner.md)

