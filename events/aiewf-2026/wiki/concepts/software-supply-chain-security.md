---
title: "software supply chain security"
type: "concept"
slug: "software-supply-chain-security"
tier: "supporting"
maturity: "consolidating"
talk_count: 11
speaker_count: 10
---

# software supply chain security

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **11** talk(s) by **10** speaker(s)

**Definition:** Risk entering through dependencies, packages, models, and third-party skills or servers, including AI-specific vectors like hallucinated package names.

*Also referred to as: supply chain security, agent supply chain security, ai supply chain security, slop squatting, package health signals, model supply chain provenance, open-source supply chain hardening*

## State of Practice

The conference relocated supply chain security from the package manifest to the agent's whole operating surface: skills, plugins, MCP servers, agent rules, hooks, memory files, and the agent's own credentials are now the dependency graph, and speakers reported hard numbers on their rot — Snyk found critical-severity issues in over one in eight of ~4,000 audited ClawHub skills plus 76 malicious payloads, a high/critical finding in an MCP server for one in 12 developers, and Nubank found 1,500+ risks across 2,000+ scanned skills. The distinguishing property of this new tier is that a skill author steers code generation on someone else's machine using natural language that no signature scanner reads, and can persist through agent memory after removal. Meanwhile the classic vector got worse rather than better: LLMs hallucinate package names and attackers register them, base-image and build-time-downloaded CVEs sit outside what Dependabot and Renovate can see, and vulnerability backlogs grew 108% quarter over quarter across Snyk's 4,800+ customers. The dominant control pattern is deterministic containment rather than model judgment — hooks that fire on tool calls, secrets kept out of the filesystem, write credentials (push, PR, CI trigger) held by a deterministic wrapper and never by the agent, and micro-VM isolation where a Docker socket would otherwise mean host compromise. What is unresolved is who does the checking: models detect only ~75% of what a deterministic check finds and reproduce the same vulnerability in only 50% of five runs, yet several teams already ship AI PR review as their best line of defense.

## Consensus

### Agent extensions — skills, plugins, MCP servers, agent rules, hooks — are supply-chain dependencies and must be scanned and governed like packages, not treated as configuration.

Support: **4** talk(s)

> "It still have the traditional part, but it will it also includes skills, plugins, MCP servers, agent rules and much more things to be acting as supply chain"
>
> — [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [2:08](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=128s)

Supporting talks: [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Agentic Development Security](../talks/agentic-development-security.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)

### Security enforcement must be deterministic and live outside the model — the model's own judgment, refusals, and self-review are unreliable enough that they cannot be the control.

Support: **7** talk(s)

> "Only 75% of the issues were found versus a good old boring deterministic check. And you know 40% was the F1 score."
>
> — [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [12:30](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=750s)

Supporting talks: [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [Agentic Development Security](../talks/agentic-development-security.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)

### AI-generated code is measurably less secure per unit of code, not merely the same defect rate at higher volume.

Support: **3** talk(s)

> "even the best models introduce vulnerabilities about 20 to 40% of the time when writing code"
>
> — [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [10:41](https://www.youtube.com/watch?v=7JgIS42mz7U&t=641s)

Supporting talks: [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)

### Prompt injection has no solution at the model layer; the only available control is limiting blast radius through architecture and permissions.

Support: **3** talk(s)

> "I guess like prompt injection itself isn't solved and we cannot really solve it. All we can do is just to limit the blast radius in case that happens."
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [12:30](https://www.youtube.com/watch?v=LqLoYksJ6do&t=750s)

Supporting talks: [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)

### Security must operate as low-friction guardrails inside the agent/developer loop rather than as a gate, a document, or an end-of-run scan.

Support: **4** talk(s)

> "security cannot be the blocker when it comes to companies accelerating their development"
>
> — [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [13:51](https://www.youtube.com/watch?v=7JgIS42mz7U&t=831s)

Supporting talks: [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [Agentic Development Security](../talks/agentic-development-security.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)

### Vulnerability backlogs are compounding faster than remediation capacity, so prevention at generation time is now the only tractable strategy.

Support: **4** talk(s)

> "at our scale, we have thousands of repositories and it really is a backlog that never empties and you close 10 issues today and you know next week 20 more will arrive"
>
> — [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [0:01](https://www.youtube.com/watch?v=LqLoYksJ6do&t=1s)

Supporting talks: [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [Agentic Development Security](../talks/agentic-development-security.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)

## Disagreements

### Is AI-driven security review trustworthy enough to be the primary check on generated code?

| Position A | Position B |
|---|---|
| Yes — AI scanning on PRs already beats human reviewers at finding real issues at roughly $5 per PR, and within 6–12 months the majority of shipped code will be reviewed by AI rather than humans; human review is the bottleneck and won't hold.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)* | No — frontier models find the same vulnerability in only 50% of five repeated runs, catch 75% of what a deterministic check catches, and score 40% F1; LLM verdicts drift with temperature, and Snyk found 241 vulnerabilities in a codebase a frontier model had already 'hardened'. LLM review is only acceptable as one half of a hybrid with deterministic scanning.<br>*[Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)* |

*Why it matters: It determines whether you can staff down human security review as generation volume rises, or must fund a deterministic scanning tier that scales with token spend. Getting it wrong means either an unreviewable backlog or a false sense of coverage from a reviewer that misses half of what it saw last run.*

### How should teams handle open-source dependency risk in an agent-written codebase — reduce reliance on third-party code, or invest in hardening the shared commons?

| Position A | Position B |
|---|---|
| Minimize the dependency surface: generating your own dependencies to requirement instead of pulling open source shrinks supply-chain blast radius, third-party contributions and packages are more dangerous than ever (a package with 3.5M daily downloads was compromised for three hours and only caught by luck), and pre-existing NPM risk alone is reason not to run coding agents on a laptop.<br>*[The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)* | Invest in the commons: fund one-time rewrites of critical libraries into memory-safe languages instead of playing one-off whack-a-mole (60–70% of vulnerabilities in memory-unsafe products would be prevented outright), and select packages by maintenance health so future patches land faster.<br>*[The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)* |

*Why it matters: One path spends engineering budget on isolation and bespoke code with no shared patch stream; the other spends it on upstream hardening that only pays off if the ecosystem coordinates. The choice sets whether your CVE exposure is yours alone to fix or shared.*

### Should security budget go to model-layer threats (backdoors, model provenance, per-model safety profiles) or to ordinary infrastructure and insider risk?

| Position A | Position B |
|---|---|
| Infrastructure — almost everything actually breaking in production ML is boring misconfiguration (thousands of Ray clusters open on the internet because auth was off by default; 78% of 50 audited production ML setups had at least one critical mistake), and budget should be allocated to infrastructure compromise and insider threat rather than model-level attack research.<br>*[Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)* | The model layer — backdoors survive safety training and are invisible to behavioral testing, model safety properties are non-monotonic (one popular model leaked PII in 100% of attacks while doing well on decision override), so model selection must be per-use-case and every build should be diffed against its base checkpoint for implanted triggers.<br>*[Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)* |

*Why it matters: The two programs compete for the same limited security headcount and the same latency budget; treating model provenance as the frontier while a job API sits open on the internet inverts the actual breach distribution, and vice versa leaves fine-tuned checkpoints unverified.*

## Practical Guidance

**Do:**

- Gate skill and plugin publication on a scan that runs in the upload PR, then re-run the identical scan in CI because you cannot assume the engineer ran it locally or ran the current version
- Require third-party skills downloaded from outside to be uploaded to the internal marketplace so they get scanned before use, and proactively discover marketplaces teams spin up on their own
- Combine deterministic scanning with LLM context review — deterministic alone misses intent, LLM alone varies with temperature — and emit SARIF so findings enter the existing vulnerability management program
- Fire security scanning from asynchronous hooks on tool calls rather than an MCP server plus rule files, which agents ignore, add end-of-run latency, and burn context tokens
- Keep dangerous write credentials — GitHub push, PR creation, CI trigger — out of the agent entirely; let the agent only modify files on the filesystem and let a deliberately boring deterministic wrapper do the rest
- Stop storing secrets as files; it was named the single most concrete step to secure an agent environment
- Run security as its own pass, separate from correctness, and make it both the first pass and the last pass — combined prompts produce a half-effort job on both
- Instruct CVE-remediation agents to make the smallest change that fixes the specific CVE rather than bumping to latest, and to not revert their own prior edits
- Isolate agents that need Docker in Firecracker micro VMs with vsock-mediated networking; landlock, bubblewrap, seccomp, Kaniko and buildkit do not compose well enough to contain a Docker daemon
- Grade shell-command risk per command instead of treating all shell usage as equally dangerous, and attach concrete remediation guidance to every finding
- Weight package maintenance health alongside current CVE count, since unmaintained packages get patched later when the next vulnerability lands
- Train a sparse autoencoder on the base-to-fine-tuned activation difference and run it as a per-build backdoor unit test — a 4x expansion matches a 32x one, and the best delta feature fires with zero false positives on benign input
- Ask the agent for a short retrospective at the end of every invocation (what went well, what went wrong, what tools were missing, what context would help) as a stand-in for the agent observability tooling that does not exist yet
- Budget 5–10% security overhead as the production floor; basic controls run under ~8%, workload isolation 10–20%

**Avoid:**

- Treating a prompt instruction to 'ask for confirmation' as a human in the loop — the agent can satisfy its own confirmation
- Letting the system that generates the code also be the system that validates it
- Relying on model refusals as a safety boundary: Claude refused to read an .env file but complied when asked for one specific secret key
- Severity-based triage that fixes only criticals and highs — agents chain low-severity vulnerabilities into working exploits
- AI governance that lives in a Confluence page or PDF instead of being enforced in real time in the agent and developer loop
- Assuming Dependabot or Renovate covers you — the CVE often lives in an OS package in your base image or a binary downloaded at build time, invisible to manifest-based tooling
- Handing an agent a Docker socket, and trusting the sandboxes shipped with Codex and Claude, which are worthless once that socket is present
- Trying to catch a backdoored model with behavioral testing or production behavior monitors — you would need the trigger in advance, and if you had it you wouldn't need the monitor
- Blanket real-time malicious-input detection as a default control; at 15–30% overhead it cannot be applied to every request and should be reserved for higher-risk systems
- Low-context, weak-signal scanner rules — they cause more trouble than they are worth
- Installing packages by name that an agent proposed: attackers upload the hallucinated name with the expected functionality plus a payload
- Depending on human approval prompts as the governance mechanism for background and cloud agents, where nobody is sitting at the desk to approve

## Notable Outliers

- In an audit of nearly 4,000 ClawHub skills, over one in eight had a critical severity issue and 76 malicious payloads were found; malicious skills can modify agent memory so they persist after removal. ([Agentic Development Security](../talks/agentic-development-security.md), [7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s))
- A useful coding agent with production credentials is itself a supply chain actor and must be governed like an engineer in your department — the blast radius of an agent is an architecture decision. ([We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [2:48](https://www.youtube.com/watch?v=LqLoYksJ6do&t=168s))
- Snyk found 241 vulnerabilities in a codebase after a frontier model had already completed a dedicated security hardening pass on it. ([Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md), [7:46](https://www.youtube.com/watch?v=yWS0udrIOc8&t=466s))
- Generating your own dependencies to requirement instead of using open source minimizes supply-chain attack blast radius — and nobody should run coding agents on a local laptop, not because of AI but because of pre-existing NPM supply chain risk. ([The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md), [58:44](https://www.youtube.com/watch?v=c35YoMdnI78&t=3524s))
- Training an SAE on the base-vs-fine-tuned activation delta yields ~0.4 backdoor isolation versus ~0.01 for joint-feature crosscoders — a 40x gap with non-overlapping confidence intervals. ([Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md), [8:12](https://www.youtube.com/watch?v=IQkVMvXQKLY&t=492s))
- 78% of 50 audited real production ML setups had at least one critical security mistake, and the Ray cluster exposure — auth off by default — represented over a billion dollars of exposure. ([Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md), [8:32](https://www.youtube.com/watch?v=XjI-AR4pt7Y&t=512s))
- A published skill pulled its monitoring instructions and classification rules from a YAML file hosted on the internet, handing a third-party website live control of the skill's logic. ([Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [19:32](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=1172s))
- The community-contribution side of open source is no longer worth cultivating, because software is cheap to build and third-party contributions now carry supply-chain risk — GitHub added a feature to disable third-party pull requests altogether. ([Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md), [4:01](https://www.youtube.com/watch?v=CoEIs6Xm8m8&t=241s))
- Export controls on frontier security-capable models should be lifted, because the benefit to defenders far outweighs the risk and adversaries already have powerful models via distillation. ([The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [14:49](https://www.youtube.com/watch?v=7JgIS42mz7U&t=889s))
- A third-party vendor dependency on rented inference was redlined in an audit and blocked the project, because a model-generated recommendation cannot be reproduced without access into the model itself. ([Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [4:15](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=255s))

## All Talks

- [Agentic Development Security](../talks/agentic-development-security.md)
- [Agentic Security: Permissions, Provenance, and the Agent Supply Chain](../talks/agentic-security-permissions-provenance-and-the-agent-supply-chain.md)
- [Open Source Is Dead. Long Live Open Source.](../talks/open-source-is-dead-long-live-open-source.md)
- [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)
- [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)
- [The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents](../talks/the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in.md)
- [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
- [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)
- [Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data](../talks/your-llm-deception-monitor-is-broken-the-fix-is-in-the-training-data.md)
- [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)

## Speakers

- [Ezra Tanzer](../speakers/ezra-tanzer.md)
- [Jack Cable](../speakers/jack-cable.md)
- [Lovina Dmello](../speakers/lovina-dmello.md)
- [Lucas Palma](../speakers/lucas-palma.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Moritz Johner](../speakers/moritz-johner.md)
- [Sachin Kumar](../speakers/sachin-kumar.md)
- [Saoud Rizwan](../speakers/saoud-rizwan.md)
- [Steve Yegge](../speakers/steve-yegge.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)

