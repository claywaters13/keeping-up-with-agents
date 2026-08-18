---
title: "secure code generation"
type: "concept"
slug: "secure-code-generation"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 9
---

# secure code generation

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **9** speaker(s)

**Definition:** Preventing agents from writing insecure code, and the static analysis and CI gates that catch it when they do.

*Also referred to as: ai-generated code vulnerabilities, secure by default, secure by design, ci security gating, secure software development lifecycle, static analysis, ast-based static analysis*

## State of Practice

The field has stopped arguing about whether AI writes insecure code and started arguing about where the checking goes. The measured baseline is bad: BaxBench-style evaluation puts even frontier models at a 20–40% vulnerability-introduction rate on coding tasks, and Sonar's 4,000-problem harness shows models passing functional correctness while emitting high-complexity, insecure code — so tests-pass is not a security gate. The dominant architecture is a separate security pass run by different tooling than the generator, mixing deterministic static analysis with LLM review, executed inside the agent's inner loop (hooks on tool calls, AST-grep sensors, guide-verify-solve controllers) and re-enforced in CI because you cannot prove the developer ran the local check. Scope has widened past generated code to the agent's own supply chain: Snyk's audit of ~4,000 ClawHub skills found over one in eight with a critical issue and 76 malicious payloads, and Nubank now gates skills through a scanned internal marketplace. The unresolved fault line is durability — DeepMind argues detect-and-patch is a treadmill and models should be taught to write correct code from the start, while the security and quality vendors treat in-loop verification as the permanent layer because security is contextual and models lack the business logic and threat model.

## Consensus

### Frontier models cannot be trusted to produce secure code by default; passing functional correctness says nothing about security, so a dedicated security check is mandatory regardless of model quality.

Support: **5** talk(s)

> "even the best models introduce vulnerabilities about 20 to 40% of the time when writing code"
>
> — [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [10:41](https://www.youtube.com/watch?v=7JgIS42mz7U&t=641s)

Supporting talks: [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Security Track Intro](../talks/security-track-intro.md)

### Security must be verified by a different model, tool, or methodology than the one that generated the code — never by the generating agent reviewing itself, and never bundled into the same prompt as correctness.

Support: **4** talk(s)

> "Use a different methodology to review the code that was used to write the code."
>
> — [Guide, Verify, Solve](../talks/guide-verify-solve.md), [9:49](https://www.youtube.com/watch?v=03l29gJXpCE&t=589s)

Supporting talks: [Guide, Verify, Solve](../talks/guide-verify-solve.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)

### Neither deterministic scanning nor LLM review is sufficient alone; the working pattern is a hybrid where deterministic tooling handles anything mechanically decidable and the LLM supplies context.

Support: **4** talk(s)

> "You need to use computational review, you also need to use LLM driven review, and everything else in between"
>
> — [Guide, Verify, Solve](../talks/guide-verify-solve.md), [10:21](https://www.youtube.com/watch?v=03l29gJXpCE&t=621s)

Supporting talks: [Guide, Verify, Solve](../talks/guide-verify-solve.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Agentic Development Security](../talks/agentic-development-security.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)

### Verification belongs inside the agent's generation loop, surfaced back to the model, not applied only afterward at the CI or code-review stage.

Support: **4** talk(s)

> "The verification needs to run in both the inner agentic loop and also in the outer loop for CICD."
>
> — [Guide, Verify, Solve](../talks/guide-verify-solve.md), [18:11](https://www.youtube.com/watch?v=03l29gJXpCE&t=1091s)

Supporting talks: [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Agentic Development Security](../talks/agentic-development-security.md)

### Human code review is not a reliable backstop for AI-generated code and is already being rubber-stamped or displaced, so the safety property has to be carried by automated verification.

Support: **3** talk(s)

> "while participants did follow the AI advice 92.7% of the time when the AI was correct, they unfortunately also listened to the AI nearly 80% of the time when the AI was wrong"
>
> — [Guide, Verify, Solve](../talks/guide-verify-solve.md), [6:35](https://www.youtube.com/watch?v=03l29gJXpCE&t=395s)

Supporting talks: [Guide, Verify, Solve](../talks/guide-verify-solve.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)

### Securing generated code is only part of the problem: skills, MCP servers, plugins, hooks and agent permissions are a supply chain that must be scanned and governed with the same rigor.

Support: **4** talk(s)

> "we should be protecting the whole workflow not only the code that's being generated"
>
> — [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [1:07](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=67s)

Supporting talks: [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Agentic Development Security](../talks/agentic-development-security.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [Security Track Intro](../talks/security-track-intro.md)

## Disagreements

### Is insecure AI-generated code a tooling problem to be solved by external verification, or a model/language problem to be solved by making models write correct code from the start?

| Position A | Position B |
|---|---|
| Detection-and-patch is a permanent, necessary layer: models will never be perfect because security is contextual and depends on proprietary business logic and threat models the model does not have, so multi-layered verification is the durable investment.<br>*[In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Agentic Development Security](../talks/agentic-development-security.md)* | Detecting vulnerabilities and suggesting fixes is a never-ending treadmill; the correct target is teaching models to write correct code from the start, plus designing a new strongly-typed, model-oriented language (Lean-inspired, not necessarily human-readable) in which whole vulnerability classes are unrepresentable.<br>*["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)* |

*Why it matters: If verification is the durable layer, the right spend is scanner integration, in-loop controllers and multi-model review; if the fix is upstream, that spend is depreciating and the leverage is in memory-safe rewrites, language design and training.*

### Will humans keep reading AI-generated code, and should systems be designed on that assumption?

| Position A | Position B |
|---|---|
| Human reading is on its way out — within roughly a year generated code ships without anyone looking at it the way nobody inspects compiler output, and within 6–12 months the majority of shipped code will be reviewed by AI rather than humans because human review is now the bottleneck.<br>*["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)* | The 'code is read-only now' thesis is unproven and prohibitively expensive without a frontier lab's token budget; bad code is more expensive than ever, so loops should be designed to make code easier to read, and for high-criticality projects humans still close the quality gap.<br>*[Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* |

*Why it matters: It determines whether you cap agent output at reviewable sizes (one open PR at a time, per-migration context windows) or invest instead in fully automated review pipelines and accept 40,000-line PRs no human will ever read.*

### Is AI-generated code a qualitatively new security risk, or the same known vulnerability classes arriving faster?

| Position A | Position B |
|---|---|
| Nothing fundamentally new: humans generate security issues and so do models, essentially all vulnerabilities frontier models find belong to already-known classes, and the genuinely harder problem is deploying autonomous agents into production safely.<br>*[Security Track Intro](../talks/security-track-intro.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)* | The defect rate itself gets worse, not just the volume — AI-written code will have a worse vulnerability rate than human code, security bugs have no half-life so the problem compounds, and organizations that ship AI code without verification enter a self-reinforcing downward spiral.<br>*[Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* |

*Why it matters: The first framing says extend your existing AppSec lifecycle to cover agents; the second says throughput of AI code must be actively throttled by verification or the security backlog grows faster than it can ever be worked down.*

### Should security controls on agent output be allowed to hard-block, or must they stay non-blocking guardrails?

| Position A | Position B |
|---|---|
| Security cannot be the blocker on development acceleration — velocity always wins, so controls must be guardrails around agent access rather than gates, and false-positive noise in a developer's workflow is itself a failure mode.<br>*[The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Agentic Development Security](../talks/agentic-development-security.md)* | Hard chokepoints work and are being run in production: artifacts get blocked before marketplace distribution, local checks are re-enforced in CI so they cannot be skipped, and organizations should enforce a centralized verification scheme across all teams and tools as bounded autonomy.<br>*[We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md)* |

*Why it matters: It decides whether the security team owns a merge-blocking gate with a false-positive budget, or an advisory feedback channel that developers and agents can route around.*

## Practical Guidance

**Do:**

- Run security as its own pass with its own prompt, separate from correctness — and make it both the first pass and the last pass over generated code.
- Expect to run four to five review passes over LLM output before it is shippable.
- Verify with different models and different techniques than the one that generated the code, since every model carries its own biases.
- Combine deterministic scanners with LLM review, and emit findings as SARIF so they feed the existing vulnerability management program rather than living in a side channel.
- Re-run local checks in CI — you cannot ensure the engineer ran them, or ran the latest version.
- Integrate scanning as async hooks on tool calls rather than MCP server plus rule files: agents ignore rule files, end-of-run scans add latency, and in-context scans burn tokens.
- Keep deterministic guardrails on the developer machine, because approval prompts stop being viable once agents run in the background or in the cloud.
- Treat skills, plugins, MCP servers, agent rules and hooks as supply chain dependencies; route externally downloaded skills through an internal scanned marketplace and proactively discover marketplaces teams spin up on their own.
- Grade shell-command risk per command instead of flagging all shell usage equally, and ship every finding with concrete remediation guidance.
- Use AST-grep as the loop sensor rather than lint or TypeScript config, because it is language-agnostic and out-of-band from configs agents disable with inline comments.
- Cap an agent loop at one open PR at a time — never open a new PR while the previous one from that loop is unreviewed.
- Give each fix or migration its own context window in a separate implementation phase; it is both cheaper and more reliable than batching.
- Supply agents explicit codebase context and constraints instead of the whole repo — measured at over 30% fewer tokens per problem.
- For high-criticality codebases, favor a one-time memory-safe rewrite of critical libraries over one-off patching: 60–70% of vulnerabilities in memory-unsafe products are eliminated outright.
- Deliver findings in the same pull request that introduces the change or skill, so feedback is co-located with the work.

**Avoid:**

- Using the same AI that wrote the code to validate it.
- Asking for security and correctness in one prompt — you get a half-done job on both.
- Treating functional correctness or a green test suite as a security gate; state-of-the-art models pass those while emitting insecure, high-complexity code.
- Relying on human review as the backstop — reviewers accept confidently-wrong AI output nearly 80% of the time, and rubber-stamping is already widespread.
- Accepting a prompt instruction like 'ask for confirmation' as a human in the loop; the agent can satisfy the confirmation itself.
- Depending on rule files or model-level judgment for enforcement — Claude refused to read an .env file but complied when asked for a specific secret key.
- Dumping the entire codebase into an agent's context, which produces thrashing and token burn.
- Running blind prompt-in-a-bash-loop agents on team-owned or critical systems, even with verifier and code-review agents bolted on.
- Emitting low-context, weak-signal findings, or findings with no remediation path — they cost more than they are worth.
- Sending an agent to do a job deterministic code can do.
- Letting a security backlog accumulate on the assumption it will age out; security bugs have no half-life.
- Treating a single canonical marketplace or registry as a sufficient chokepoint.
- Expecting zero false positives from any vendor in this space.

## Notable Outliers

- Snyk found 241 vulnerabilities in a codebase that Fable had already completed a dedicated security hardening pass over — and everything it found was already a public CVE, not the pre-registry proprietary finding the vendor claims. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [10:31](https://www.youtube.com/watch?v=yWS0udrIOc8&t=631s))
- Existing languages like Python were designed for humans and are bad for safe code; the answer is a new strongly-typed, Lean-inspired language for models that does not need to be human-readable. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [17:17](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=1037s))
- Within about a year, generated code will ship without any human reading it, the way nobody inspects compiler assembly output. (["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md), [11:42](https://www.youtube.com/watch?v=1P1hJ36rxM0&t=702s))
- An audit of nearly 4,000 ClawHub skills found over one in eight with a critical severity issue and 76 malicious payloads — and malicious skills can modify agent memory, so removing the skill does not remove the compromise. ([Agentic Development Security](../talks/agentic-development-security.md), [7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s))
- One in 12 developers observed had an MCP server with a high or critical severity finding in the server itself. ([Agentic Development Security](../talks/agentic-development-security.md), [8:29](https://www.youtube.com/watch?v=cgimkNGNjvU&t=509s))
- Export controls on frontier security-capable models should be lifted, because adversaries already have powerful models via distillation and the defender benefit outweighs the risk. ([The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [14:49](https://www.youtube.com/watch?v=7JgIS42mz7U&t=889s))
- LLMs are lazy about token spend in a useful way, so they will voluntarily adopt deterministic security scanners that offload cognition — and you should run the open-source, Snyk and Chainguard scanners together so they check each other's work. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [9:14](https://www.youtube.com/watch?v=yWS0udrIOc8&t=554s))
- Sonar's 4,000-task benchmark found Claude Sonnet 4.6 strong on correctness and task-solving, but Opus the better pick when maintainability, security, or low complexity are the priority. ([Guide, Verify, Solve](../talks/guide-verify-solve.md), [5:32](https://www.youtube.com/watch?v=03l29gJXpCE&t=332s))
- Clean code measurably matters to agents, not just humans: a cleaned codebase reduces the tokens and reasoning needed for identical agentic tasks. ([In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md), [13:09](https://www.youtube.com/watch?v=VrpEyglYgeU&t=789s))
- There is no good technical defense for prompt injection today — it is currently an education problem — and agent queue systems need adversarial supervisor agents because any single agent will eventually fail. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [21:15](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1275s))

## All Talks

- [Agentic Development Security](../talks/agentic-development-security.md)
- [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)
- [Guide, Verify, Solve](../talks/guide-verify-solve.md)
- [In the Land of AI Agents, the Verifiers Are King](../talks/in-the-land-of-ai-agents-the-verifiers-are-king.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [Security Track Intro](../talks/security-track-intro.md)
- ["Software engineering is not about writing code"](../talks/software-engineering-is-not-about-writing-code.md)
- [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)
- [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)

## Speakers

- [Anirban Chatterjee](../speakers/anirban-chatterjee.md)
- [Benoit Schillings](../speakers/benoit-schillings.md)
- [Ezra Tanzer](../speakers/ezra-tanzer.md)
- [Jack Cable](../speakers/jack-cable.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [Lucas Palma](../speakers/lucas-palma.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Steve Yegge](../speakers/steve-yegge.md)
- [Tariq Shaukat](../speakers/tariq-shaukat.md)

