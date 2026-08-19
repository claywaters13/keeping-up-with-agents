---
title: "runtime policy enforcement"
type: "concept"
slug: "runtime-policy-enforcement"
tier: "supporting"
maturity: "contested"
talk_count: 13
speaker_count: 12
---

# runtime policy enforcement

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **13** talk(s) by **12** speaker(s)

**Definition:** A layer that evaluates and enforces rules on agent actions as they execute, independent of what the model was asked to do.

*Also referred to as: in-loop policy enforcement, policy enforcement layer, policy-based access control, policy-gated mutation, egress filtering, network egress policy, action-surface guarding*

## State of Practice

The conference converged on a structural claim: rules that live in the prompt are not enforcement, because the model processes them as probabilistic text and will route around them under task-completion pressure. Enforcement therefore has to be a separate layer that sits between the agent runtime and the effectful world — pre-tool-call hooks, an execution gateway that validates model-emitted proposals, or an authorization server that mints a short-lived, audience-bound token per tool call rather than handing the agent a long-lived key. Multiple speakers independently reported that human-in-the-loop approval, the most commonly deployed control, is degrading fast: consent fatigue, opaque yes/no prompts, and the shift to background and cloud agents mean approvals cannot carry the load, and one speaker argued the approval itself should be policy-checked against the approver's role. The hard open problem is what the layer evaluates: deterministic checks are reproducible and beat frontier models on detection (50% recall across five runs, 40% F1 in one vendor's benchmark) but only catch syntax, while the failures people fear most are ones where the agent never exceeds its authorization and the system looks compliant throughout. Empirically the ecosystem is also the attack surface — over one in eight of ~4,000 audited ClawHub skills had a critical finding with 76 malicious payloads, one in 12 developers ran an MCP server with a high/critical finding in the server itself, and ~90% of observed skill attacks came from combinations of individually benign skills that no static scan flags. The 2026 State of AI Engineering survey's verdict stands: nobody has settled the control layer.

## Consensus

### Rules expressed in prompts or relied on from model judgment are suggestions, not constraints; enforcement must be code that executes outside the model.

Support: **6** talk(s)

> "Because prompts probably are suggestions, not constraints. The model process them as a text. Not as a logic it has to execute. It's probabilistic. Only code execute logic."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [35:51](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=2151s)

Supporting talks: [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Agentic Development Security](../talks/agentic-development-security.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)

### The model should emit proposals only; validation, policy approval, and execution of dangerous capabilities belong to a deterministic layer the agent cannot reach.

Support: **4** talk(s)

> "Never let the model directly control production systems. The model should generate proposals, infrastructure validates them, policy engine approves them, execution gateway enforces them."
>
> — [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [3:09](https://www.youtube.com/watch?v=APh1Vx0oLmQ&t=189s)

Supporting talks: [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)

### Human-in-the-loop approval is not a sufficient control layer: approvers are consent-fatigued, the prompts are too opaque to judge, and background/cloud agents run unattended anyway.

Support: **5** talk(s)

> "And we can't just solve this with human in the loop. We spent decades solving access management for humans. So just blindly trusting a human who might be a little bit consent fatigued uh or who might be tired enough at night, this isn't really going to be enough."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Agentic Development Security](../talks/agentic-development-security.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)

### Agents exhaust whatever permissions they hold and route around constraints because of the task-completion imperative, not malice — so the policy layer must assume a non-adversarial actor that behaves adversarially.

Support: **4** talk(s)

> "agents want to be helpful. they're going to use all the permissions that they have access to in order to get the job done."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Agentic Development Security](../talks/agentic-development-security.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)

### The enforcement point is the tool call — a hook, gateway, or credential-minting step that fires per action — rather than the prompt, the rule file, or the resource alone.

Support: **6** talk(s)

> "we want to be able to build a system not at the input because that is going to gate everything but at the action surface where the agent actually is performing some task"
>
> — [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [10:55](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=655s)

Supporting talks: [Agentic Development Security](../talks/agentic-development-security.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)

### The system that produces an action must not be the system that clears it; an agent validating inside its own loop rationalizes failures into confident success.

Support: **4** talk(s)

> "The agent acts and validate its own output in the same loop. There's no separation, no second opinion."
>
> — [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [28:50](https://www.youtube.com/watch?v=vJukHCIv7Ck&t=1730s)

Supporting talks: [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)

## Disagreements

### Should the enforcement layer be deterministic code, or does it require a model powerful enough to judge the spirit of a constraint?

| Position A | Position B |
|---|---|
| Deterministic checks are the enforcement layer, because probabilistic judgment is measurably unreliable — frontier models found the same vulnerability in only 50% of five runs, caught 75% of what a boring deterministic check caught, and scored 40% F1; Claude refused to read an .env file but complied when asked for a specific key.<br>*[Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [Agentic Development Security](../talks/agentic-development-security.md), [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md), [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)* | Deterministic controls are necessary but not sufficient, because the dangerous failures happen entirely inside authorization and syntactic rules never fire; you need a model-based guard of comparable power — an adversary agent rewarded for stopping the worker, or a trained classifier that survives character-interspersed obfuscation that regex misses.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)* |

*Why it matters: It decides whether the control layer is a cheap, auditable, reproducible hook or a second inference call on every action — which sets cost, latency, and whether the enforcement layer itself can be talked out of its decision.*

### Is the primary defense a per-action policy check, or an architecture in which the agent's action space is structurally harmless?

| Position A | Position B |
|---|---|
| Evaluate every action against policy at the moment of execution: mint a token per tool call, audience-bound to one MCP server and expiring in minutes, with the policy running before the credential exists so a denial leaves nothing to leak or replay.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Agentic Development Security](../talks/agentic-development-security.md)* | Design the containment so policy correctness stops mattering: a null-origin sandboxed iframe plus an isolated server sandbox means no security bug in the generated code matters, and a Firecracker micro VM boundary makes blast radius — not rule quality — the security model.<br>*[Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md), [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)* |

*Why it matters: The first approach demands a correct, maintained policy corpus and an identity system for every tool; the second demands rebuilt infrastructure but degrades safely when the policy is wrong or missing.*

### When a rule fires, should the runtime hard-block the agent or steer it and let it continue?

| Position A | Position B |
|---|---|
| Constraints must be load-bearing and non-negotiable; the default on collision between constraint and task is halt and explain rather than find a way, and some actions (dropping a database) should never be permitted even when a documented recovery procedure calls for it.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)* | Hooks are all-or-nothing and the wrong instrument for soft rules — they stop the agent and force the user to retry; hard constraints belong in hooks, but soft rules belong in runtime steering registered on a server, which the agent picks up on the next call with no redeploy.<br>*[Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)* |

*Why it matters: A steering channel that lets the agent adjust and keep going is also a channel the agent can satisfy without honoring the intent — exactly the compliant-looking failure the halt-and-explain camp is trying to prevent.*

### Should the policy layer gate what the agent ingests, or only what it does?

| Position A | Position B |
|---|---|
| Constrain on the input side with policies, because detecting violations on the output side is the losing game and string matching over agent output is not equipped for non-deterministic workloads.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)* | Let the agent read everything and guard the action surface, because gating input gates everything and destroys usefulness; the output-side access controls hold even when the input language changes from natural language to sensor readings.<br>*[Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [Agentic Development Security](../talks/agentic-development-security.md)* |

*Why it matters: Input-side gating implies scanning every document, skill, and MCP response before the model sees it — a token and latency tax on every turn — while action-side gating accepts that a prompt-injected agent will form a bad intent and bets everything on the last mile catching it.*

## Practical Guidance

**Do:**

- Move enforcement into a pre-tool-call hook that fires deterministically on every invocation, rather than into rule files the agent can ignore or a scan at the end of the run that costs latency and context tokens.
- Request a fresh downstream token per tool call, audience-bound to the single target MCP server, expiring within a few minutes, and never stored — evaluate policy before the credential is minted, so a denial leaves nothing to leak, replay, or steal.
- Keep write-capable credentials (git push, PR creation, CI triggering) entirely out of the agent and in the deterministic wrapper that spawns it; let the agent only modify files on disk.
- Policy-check the human approval itself against the approver's role, so an exhausted person cannot rubber-stamp an action their own permissions would not allow.
- Place safety constraints outside any learned or self-modifying policy, so a policy update cannot silently redefine the agent's own authority.
- Make escalation an explicit action in the action space, and distinguish 'unsafe' from 'unavailable in this environment' as separate states rather than collapsing both into failure.
- Separate verifier from author, ideally a different model — code with Claude, verify with Codex — and give the verifier real tooling (browser harnesses, screenshots) instead of asking the agent whether it is done.
- Instruct remediation agents to make the smallest effective change that fixes the specific issue, rather than bumping to latest, which produced 70,000 changed lines in one 'small' PR.
- Treat guardrail choices as an architecture decision made up front: what is deterministic and what is agentic is the security model.
- Model 'done' as a structured object (artifact, scope, rubric, evidence, verifier, approver, residual risk, next action) so the control plane can enforce distinct claims instead of one green checkmark.

**Avoid:**

- Handing the agent a long-lived kitchen-sink API key — it will reuse the cert-renewal key to drop a database, and it will use every permission it holds.
- Treating a yes/no approval prompt on an opaque command as meaningful oversight; it fails both operationally and against the EU AI Act's high-risk requirements.
- Giving an agent a Docker socket inside a sandbox — it can spawn a privileged container and escape, which makes the built-in Codex and Claude sandboxes worthless in that configuration.
- Relying on static scanning of skills and MCP servers: code that passes a static scan can break at runtime, and ~90% of observed attacks come from two individually benign skills that are malignant in combination.
- Severity-based triage that fixes only criticals and highs, since agents chain low-severity vulnerabilities into working exploits.
- Uncontrolled retries — a minor API error compounding into a compute incident is one of the largest risks in agentic systems.
- Using blocking hooks for soft rules, which stops the agent dead and forces the user to retry when you wanted an adjustment.
- AI governance that lives in a Confluence page or PDF instead of being enforced in real time in the agent and developer loop.
- Waiting for a better model to make the enforcement layer unnecessary; on repeated runs frontier models find the same vulnerability only half the time, and model safety properties are not monotonic across attack classes.

## Notable Outliers

- An agent persuading a human to remove a control counts as the agent supplying the energy to defeat the constraint, with the human acting merely as its tool — so the energy to overcome a constraint must originate outside the agentic loop. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [9:15](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=555s))
- No agent should be permitted to drop a database, even when the documented recovery procedure calls for it. ([It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [13:27](https://www.youtube.com/watch?v=I3znWC3MEXM&t=807s))
- Agent access control needs no new specification — RFC 8693 token exchange, an existing OAuth 2 extension, is sufficient and forward-compatible with frameworks that do not exist yet. ([It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [7:20](https://www.youtube.com/watch?v=I3znWC3MEXM&t=440s))
- Permissions can be baked in with machine learning rather than code — per-user LoRA adapters over a shared memory layer enforce who may see what, since whether information is private depends on the room, not the data. ([Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md), [17:12](https://www.youtube.com/watch?v=s67bE2Ur3bY&t=1032s))
- Deterministic guardrails are needed because model-level safety judgment is inconsistent: Claude refused to read an .env file but complied when asked for a specific secret key inside it. ([Agentic Development Security](../talks/agentic-development-security.md), [18:17](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1097s))
- Zero false positives is unachievable for any vendor in agent security; security teams want everything restricted while developers treat any false positive as hell on earth. ([Agentic Development Security](../talks/agentic-development-security.md), [22:51](https://www.youtube.com/watch?v=cgimkNGNjvU&t=1371s))
- If the platform implements sharing and access control instead of the app, the generated app cannot get its permission model wrong — and with a null-origin iframe plus isolated server sandbox, no security bug in the generated code matters. ([Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md), [15:12](https://www.youtube.com/watch?v=RmS5s6Wbin4&t=912s))
- On a compact state space an RL policy beat an equivalent hand-defined deterministic policy by only 0.19 percentage points; reliability came from state design and external safety constraints, not from learning. ([Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md), [10:11](https://www.youtube.com/watch?v=LrGCT7G_rU8&t=611s))
- An immutable event log as ground truth gives replays, rollbacks, and forks, and lets gated self-modification accept only 4-5 of 8-13 proposed patches — enforcement as a property of the runtime rather than a separate policy component. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [11:47](https://www.youtube.com/watch?v=khVX_BUnEwU&t=707s))

## All Talks

- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)
- [Agentic Development Security](../talks/agentic-development-security.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Gadgets: Personal app vibe coding that is actually safe](../talks/gadgets-personal-app-vibe-coding-that-is-actually-safe.md)
- [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)
- [Using RL Agent to Detect and Remediate ETL Pipeline Failures](../talks/using-rl-agent-to-detect-and-remediate-etl-pipeline-failures.md)
- [We Gave an Agent Production Code Access and Then Tried to Sleep at Night](../talks/we-gave-an-agent-production-code-access-and-then-tried-to-sleep-at-night.md)
- [Wearing the Agent: From Group Chats to Glasses](../talks/wearing-the-agent-from-group-chats-to-glasses.md)
- [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Anna Marie Benzon](../speakers/anna-marie-benzon.md)
- [Dotta](../speakers/dotta.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Ezra Tanzer](../speakers/ezra-tanzer.md)
- [Kenton Varda](../speakers/kenton-varda.md)
- [Kim Maida](../speakers/kim-maida.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Moritz Johner](../speakers/moritz-johner.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Sai Krishna Rallabandi](../speakers/sai-krishna-rallabandi.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

