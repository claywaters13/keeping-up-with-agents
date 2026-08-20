---
title: "ai governance and compliance"
type: "concept"
slug: "ai-governance-and-compliance"
tier: "supporting"
maturity: "consolidating"
talk_count: 17
speaker_count: 18
---

# ai governance and compliance

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **17** talk(s) by **18** speaker(s)

**Definition:** Organizational and regulatory control over AI systems — policy, approval, disclosure, and demonstrating conformance to auditors.

*Also referred to as: ai governance, ai code governance, eu ai act compliance, regulated environment compliance, agent governance and security posture, sox compliance for ai agents, predictive governance, ai disclosure policy*

## State of Practice

The conference's dominant claim is that governance is an architectural property, not a policy artifact: controls that live in a system prompt, a Confluence page, or a PDF are treated as decoration, while controls that live in code above the model — deterministic pre-model routing, append-only event logs, ingestion-boundary PII stripping, CI gates on the agent supply chain — are treated as the real thing. The regulatory deliverable has shifted from the model to the evidence: a complete, traceable chain of every action, data access, and authorization, designed into storage so auditability is a free consequence rather than a bolted-on feature. Speakers repeatedly reported that LLM judgment is too unstable to serve as the control of record (a frontier model finding the same vulnerability in only 50% of five identical runs, 40% F1 versus a deterministic check, verdicts that move with temperature and model version), so deterministic checks anchor the decision and LLMs supply context around them. Governance scope has widened past generated code to the whole agent supply chain — skills, plugins, MCP servers, agent rules, hooks — after Nubank scanned 2,000+ skills and Snyk reported over a third of publicly shared skills carrying malware or vulnerabilities. The binding constraint everyone hit is human attention: median PR review time up 441.5% on AI-adopting teams, 100% human review of high-stakes health conversations, and no budget to hire reviewers in proportion to throughput. The EU AI Act's meaningful-oversight requirement landing within weeks of the conference sharpened the open question of whether the industry's standard yes/no approval prompt counts as oversight at all.

## Consensus

### Governance must be enforced as executable code or architecture above the model; prompts, instructions, and policy documents are not controls.

Support: **6** talk(s)

> "when you're building ungoverned AI apps, that AI governance cannot live in a confluence page or PDF"
>
> — [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [14:40](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=880s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md), [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)

### The compliance deliverable is a traceable evidence trail — every action, data access, and authorization — designed into the system's storage rather than reconstructed after an incident.

Support: **4** talk(s)

> "The important thing is that you don't ship the model, you ship the evidence when trying to regulate."
>
> — [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [16:18](https://www.youtube.com/watch?v=McknwOzbmyg&t=978s)

Supporting talks: [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)

### Deterministic checks must anchor any compliance decision, because LLM verdicts are not stable across repeated runs, temperatures, or model versions and therefore are not defensible.

Support: **4** talk(s)

> "We're asking them to find you know the same vulnerability run it five times and only 50% of those ones are found across those five tests. That's not how you can run an enterprise system if you just use the LLM without any anything else."
>
> — [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [12:30](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=750s)

Supporting talks: [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)

### Human capacity to read and act on oversight signal — not compute, model capability, or tooling — is the binding constraint on governed AI throughput.

Support: **4** talk(s)

> "The bottleneck is not the compute, the models, the capability. It's actually having enough people to read the signal and act on it."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [11:27](https://www.youtube.com/watch?v=YXEqC05WEI0&t=687s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)

### Governance scope must cover the whole agent workflow — skills, plugins, MCP servers, agent rules, hooks, and context — as a supply chain, not just the generated code.

Support: **3** talk(s)

> "we should be protecting the whole workflow not only the code that's being generated"
>
> — [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [1:07](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=67s)

Supporting talks: [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)

## Disagreements

### Should a governance control be allowed to block work, or must it only inform and guardrail?

| Position A | Position B |
|---|---|
| Controls must be load-bearing and capable of stopping the pipeline: halt-and-explain when constraint and task collide, block non-compliant skills before marketplace distribution, hold launch on a safety bug, and expand autonomy only as evidence accumulates.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)* | Governance must never sit in the critical path: post the review-debt score on every PR but never block the merge, and treat security as guardrails rather than a gate because development acceleration always wins over security friction.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* |

*Why it matters: A blocking control produces a defensible compliance record but gets routed around or switched off when it costs throughput; a non-blocking one survives organizationally but leaves you with a measurement, not a control, when an auditor asks what actually prevented the bad change.*

### Can a probabilistic LLM judge serve as the control of record for a regulated system?

| Position A | Position B |
|---|---|
| Yes, when validated: an LLM judge checked against 240 expert-labelled examples reached F1 0.96 with near-perfect sensitivity and performed at least on par with clinicians, and continuously scoring live traffic with judges is what actually holds up in production; editing the judge prompt is legitimate engineering, not gaming the eval.<br>*[Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)* | No: the same score moves when the model or temperature changes and is not defensible to leadership or auditors, frontier models find a known vulnerability in only 50% of five runs and score 40% F1 against a deterministic check, so scoring must be traceable to a deterministic computation with the LLM used only for context inside a hybrid.<br>*[ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)* |

*Why it matters: If judges can be the control, governance scales with traffic and covers open-ended behaviors; if they cannot, every enforceable rule must be reducible to deterministic code, which caps what you can govern to what you can express as a check.*

### Does an in-line approval prompt to a human count as human oversight?

| Position A | Position B |
|---|---|
| No: the agent supplies the energy to defeat the constraint and routes it through the human as a tool, a 'you must ask for confirmation' instruction lets the agent satisfy the confirmation itself, and a yes/no LGTM on an opaque command will not meet the EU AI Act's meaningful-oversight bar for high-risk AI.<br>*[AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)* | Yes, and it is the core interaction: agentic tools should show an action plan with a time and cost estimate and get explicit approval before executing, with an always-available abort; humans are needed at the first and last step of the loop and the intermediate steps belong to the agent.<br>*[The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* |

*Why it matters: Whether approval UX counts as oversight determines if compliance can be satisfied by an interface change or requires an independent out-of-loop enforcement layer in the harness — a difference of one sprint versus an architecture rewrite.*

## Practical Guidance

**Do:**

- Strip PHI/PII at the pipeline boundary at ingestion, before the data lake, so stored data never contains it — rather than redacting at runtime in logs and dashboards
- Run high-stakes intent routing (self-harm, suicidal ideation, acute emergency → 911/988) and identity verification as deterministic code before the model on every turn, so the model never sees that turn
- Make an append-only, timestamped event log the system's single source of truth, with all views as ephemeral computed projections, so auditability falls out of the storage paradigm
- Keep sensitive payloads in immutable schema-driven object storage that the event log only references, so developers can retrace agent steps seeing only the schema, never the PHI
- Gate skills, plugins, MCP servers, agent rules, and hooks through an internal marketplace with a hybrid deterministic + LLM scan, emit SARIF into the vulnerability management program, and re-run the scan in CI because you cannot trust that the engineer ran it locally or ran the latest version
- Route third-party skills downloaded from outside through the internal marketplace so they get scanned, and proactively discover marketplaces teams spin up on their own
- Ship the regulatory artifact as traceable evidence — calls, datasets, pinned prompts, judge verdicts mapped to specific named hazards — not the model or a vendor benchmark score
- Grade risk per shell command rather than treating all shell commands as equally risky, and drop low-context weak signals that cause more trouble than they are worth
- Set bug severity by the worst plausible outcome, not frequency, and allow only three dispositions: fix, delay, or accept with explicit sign-off
- Post a deterministic review-debt score as a comment on every PR, and calibrate the weights by backfilling over your own last 200 merged PRs rather than adopting defaults
- Require the human author to write the PR body, because that is the moment they commit to understanding what they are shipping
- When a judge score drops, verify the judge before changing the agent's prompts
- Expand system autonomy stage by stage in proportion to accumulated evidence, with domain experts in the loop
- Sample and human-review 100% of high-stakes cases, with random sampling across the rest
- Deliver findings in the same pull request that uploads the artifact, and always pair a finding with clear remediation guidance
- Invoke security tooling deterministically via hooks or skills rather than relying on a developer to prompt for it
- Weigh package maintenance health, not just current CVE count, when selecting dependencies
- Manage company context like code — versioning, dependency and impact tracking, named approvers/maintainers/contributors — and route self-improving skill changes to a human maintainer for approve/reject

**Avoid:**

- Treating a system prompt as a security boundary — if the labs themselves don't trust the prompt as one, neither should you
- Writing 'ask for confirmation' into a skill and calling it human-in-the-loop: the agent can issue and satisfy the confirmation itself
- Presenting a sandbox diagram and a yes/no approval on an opaque command as meaningful human oversight under the EU AI Act
- Expressing AI governance as Confluence pages and PDFs instead of enforcement in the agent and developer loop
- Bolting eval, security, and auditability onto a working POC as requirements surface — it produces brittle systems that don't generalize; take the production constraints as architectural principles first and rebuild toward POC accuracy
- Severity-based triage that fixes only criticals and highs, since agents can chain low-severity vulnerabilities into working exploits
- Any data pipe between production and non-production environments, and any raw-PHI access for engineers outside the certified geographic region
- Silent defaults for tenant identity in multi-tenant systems — a missing brand identity field should crash, not fall back (one white-label leak shipped every venue as sage@hawthornemanner.com)
- Reporting PR count, PR size, and cycle time as AI governance signal — they are real numbers but measure production speed, not trust
- Quietly downgrading a bug's severity because nobody has capacity or the fix is hard
- Calling a behavior already live in production for weeks without escalation a launch blocker for a new feature; your launch bar is what your org already accepts
- Relying on offline golden datasets alone — sampling may be unrepresentative and the data drifts — instead of continuously scoring live traffic or replaying real production events
- Waiting for a better model to solve agentic security, or assuming probabilistic systems will solve everything
- Blanket real-time malicious-input detection as a universal control at 15–30% overhead; reserve it for higher-risk systems
- Access control policy written over an exposed cluster — 78% of 50 audited production ML setups had at least one critical security mistake, and the Ray exposure came from authentication being off by default

## Notable Outliers

- An agent persuading a human to install a Chrome extension that removes a control counts as the agent supplying the energy to defeat the constraint, with the human acting as its tool — so oversight must come from outside the agentic loop, likely an equal-power adversary agent rewarded for stopping the worker. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [14:17](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=857s))
- The hardest agent failures are ones where the agent never exceeds its authorization, so the system looks compliant the entire time and the violation is undetectable by authorization-based controls. ([AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md), [10:16](https://www.youtube.com/watch?v=1lgFGaHoGq8&t=616s))
- More than a third of publicly shared agent skills contain malware or vulnerabilities, and repositories contain roughly three times more agentic components than models, so risk assessment must span all layers. ([Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md), [8:23](https://www.youtube.com/watch?v=1EZdpEhwmNc&t=503s))
- Export controls on frontier security-capable models should be lifted, because the benefit to defenders outweighs the adversary risk and distillation means adversaries already have powerful models regardless. ([The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md), [14:49](https://www.youtube.com/watch?v=7JgIS42mz7U&t=889s))
- 2027 will be the year the industry conversation shifts from AI coding adoption to governance and accountability — who is accountable when an AI-authored change causes an incident, and where is the audit trail. ([ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md), [22:48](https://www.youtube.com/watch?v=TJPInBjhE4Q&t=1368s))
- Humans and LLMs should be architecturally interchangeable agents — any action an LLM can take a human can also take, downstream steps are indifferent to which acted — because escalation points cannot be predicted in advance; the human-vs-LLM delta on the same task then becomes the eval score. ([Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md), [15:50](https://www.youtube.com/watch?v=mav15aW9lLM&t=950s))

## All Talks

- [Adaption Labs: Gradient-Free Continual Learning](../talks/adaption-labs-gradient-free-continual-learning.md)
- [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)
- [AI’s Jurassic Park Period](../talks/ais-jurassic-park-period.md)
- [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [Notion's Token Town](../talks/notions-token-town.md)
- [ReviewDebt: a practical framework for scoring every pull request](../talks/reviewdebt-a-practical-framework-for-scoring-every-pull-request.md)
- [Shipping AI to a Million Patients Without an A/B Test](../talks/shipping-ai-to-a-million-patients-without-an-ab-test.md)
- [Stop Writing Tone Instructions. Layer Them.](../talks/stop-writing-tone-instructions-layer-them.md)
- [The AI bugpocalypse is here. Now what?](../talks/the-ai-bugpocalypse-is-here-now-what.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)
- [Through the AI Fog: The Architectural Decision Agentic Security Depends On](../talks/through-the-ai-fog-the-architectural-decision-agentic-security-depends-on.md)
- [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)
- [Why Your Enterprise Tech Stack Isn’t Ready for AI Agents](../talks/why-your-enterprise-tech-stack-isnt-ready-for-ai-agents.md)
- [WTF Is the Context Layer? The Missing Infrastructure for Production Agents](../talks/wtf-is-the-context-layer-the-missing-infrastructure-for-production-agents.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)
- [Your LLM Stack Is a 2008 Database With Better Marketing](../talks/your-llm-stack-is-a-2008-database-with-better-marketing.md)

## Speakers

- [Aaron Stanley](../speakers/aaron-stanley.md)
- [Christopher Lovejoy](../speakers/christopher-lovejoy.md)
- [Eno Reyes](../speakers/eno-reyes.md)
- [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)
- [Jack Cable](../speakers/jack-cable.md)
- [Jared Joselowitz](../speakers/jared-joselowitz.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Lovina Dmello](../speakers/lovina-dmello.md)
- [Lucas Palma](../speakers/lucas-palma.md)
- [Manoj Nair](../speakers/manoj-nair.md)
- [Prukalpa Sankar](../speakers/prukalpa-sankar.md)
- [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)
- [Rashi Agrawal](../speakers/rashi-agrawal.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Sara Hooker](../speakers/sara-hooker.md)
- [Sarah Sachs](../speakers/sarah-sachs.md)
- [Saul Howard](../speakers/saul-howard.md)
- [Varsha Shah](../speakers/varsha-shah.md)

