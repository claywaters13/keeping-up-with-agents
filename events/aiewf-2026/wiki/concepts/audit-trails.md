---
title: "audit trails"
type: "concept"
slug: "audit-trails"
tier: "supporting"
maturity: "consolidating"
talk_count: 14
speaker_count: 14
---

# audit trails

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **14** talk(s) by **14** speaker(s)

**Definition:** Durable, attributable records of what an agent did and why, produced for compliance and after-the-fact accountability rather than debugging.

*Also referred to as: audit trail, agent audit logging, audit logging and attribution, run receipts and auditability, agent auditability, verification trails, decision ledger*

## State of Practice

The field has moved from "log everything" to "produce evidence," and the distinction is now load-bearing: a transcript, a tool's success return, or an agent's own "looks done to me" are treated as claims, not proof, while a receipt records what the system allowed, what was attempted, what executed, and what the user-visible edge confirmed. The record is expected to be emitted by deterministic infrastructure outside the model — harness commit paths, blocking gates, flag middleware, async hooks on tool calls, immutable event logs — because anything the agent narrates about itself is unverifiable. Attribution has hardened into a specific schema several speakers converge on independently: which agent identity acted, on behalf of which user, under which authorization, granted when, scoped how, expiring when — which is why the identity talks reject giving agents user credentials outright, since acting-as-the-user erases the attribution the audit trail exists to capture. Replayability, not retention, is the acceptance test: a named owner must be able to reconstruct the run, which drives event-sourcing at one end and, at the other, complaints that rented inference endpoints make a generated recommendation impossible to recreate under audit. What remains unsettled is how heavy the record must be (signed tamper-evident chains versus an append-only internal log), whether auditability requires rearchitecting around the log or just a handful of boundary gates, and how much of the accountability chain a human is still supposed to sign.

## Consensus

### Agent self-report is not evidence; the record of what happened must be emitted by the system at the action boundary, and a transcript or a tool's success return does not prove the external effect occurred.

Support: **5** talk(s)

> "A transcript tells you what the agent said. A receipt tells you what the system allowed, attempted, executed and what the user visible edge confirmed."
>
> — [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [3:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=203s)

Supporting talks: [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)

### Every recorded action must be attributable to a distinct agent identity plus the principal and authorization behind it — who acted, on behalf of whom, under what grant, when, and for how long.

Support: **5** talk(s)

> "you have to have absolute visibility into what your agent can do, every action that's taken in your system, who took it, on behalf of whom, and who authorized it, when was the authorization given, what authorization was given, how long is it given for"
>
> — [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [11:43](https://www.youtube.com/watch?v=lMCxVorb9wM&t=703s)

Supporting talks: [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [Agentic Development Security](../talks/agentic-development-security.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)

### The purpose of the record is after-the-fact reconstruction — replay, rollback, or reproduction of a specific decision — not storage; a log nobody can replay does not count.

Support: **4** talk(s)

> "in the end you get this beautiful typed event log, which gives you replays. It gives you rollbacks and it gives you forks."
>
> — [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [3:43](https://www.youtube.com/watch?v=khVX_BUnEwU&t=223s)

Supporting talks: [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)

### Accountability terminates in an identified human or organization and cannot be transferred to the model or its vendor; the audit trail exists to make that signature defensible.

Support: **4** talk(s)

> "You can't outsource accountability to your own software. At the bottom of every real decision, a human signs."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [19:21](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1161s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Agentic Development Security](../talks/agentic-development-security.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)

### An observability layer that only records without the ability to stop an action is insufficient; the same path that produces the record must be able to block, kill, or refuse.

Support: **4** talk(s)

> "A gate which logs only warnings is not a gate. It's a suggestion. The gate needs to block the artifact from moving forward."
>
> — [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [10:01](https://www.youtube.com/watch?v=WLXxTaPagA8&t=601s)

Supporting talks: [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [Agentic Development Security](../talks/agentic-development-security.md), [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)

## Disagreements

### Should human approval be the mechanism that makes agent actions accountable, or does it collapse at production volume and need to be replaced by machine-produced evidence?

| Position A | Position B |
|---|---|
| A named human must sign at the end of the chain and autonomy should default to 'suggest', with auto-approve earned per surface and auto-execute opt-in per tool; a system whose figures don't match should refuse to ship rather than defer to a reviewer.<br>*[Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)* | Exhaustive human sign-off becomes verification theater at high task volume, and approval prompts are unworkable for background and cloud agents, so authority must be encoded as deterministic policy and 'done' proven by a separate verifying agent plus receipts.<br>*[What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Agentic Development Security](../talks/agentic-development-security.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)* |

*Why it matters: It determines whether your audit trail is a queue of approvals a person must clear (which caps throughput at human review capacity) or a stream of machine-generated evidence a person samples after the fact. The second scales but shifts the compliance burden onto the completeness of the evidence schema.*

### How strong must the record be — a cryptographically signed, tamper-evident chain, or an append-only internal log plus source links?

| Position A | Position B |
|---|---|
| Sign the chain: per-agent private keys, signed receipts whose chain is only valid if no data point is tampered with, attestation with a public transparency log, and a security-critical codebase kept small enough (~20k lines) to fully audit.<br>*[Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)* | An immutable typed event log, a flag audit trail in an off-the-shelf service, a record of which gate failed, and one-click provenance back to the source paragraph are sufficient; the work is plumbing and honesty, not cryptography.<br>*[Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)* |

*Why it matters: Signature chains are the only option when the counterparty reading the record is outside your trust boundary — another lab, a payer, a regulator — while inside one org they are cost with no additional assurance. Picking wrong either blocks cross-organizational agent collaboration or burns budget on crypto nobody verifies.*

### Does auditability require rearchitecting the agent around its log, or can it be retrofitted as a few boundary checks on the system you already have?

| Position A | Position B |
|---|---|
| Build around the log: flatten agent changes and agent actions into one immutable event log as ground truth, derive graph state as a projection of it, and accept that the resulting code is unintuitive enough that only an AI should write it.<br>*[Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)* | No new platform, framework, or flag backend is needed — add a small number of blocking gates at the most expensive handoff and put a thin middleware layer in front of the existing agent loop.<br>*[Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)* |

*Why it matters: One path costs a rewrite and buys replay, rollback, and forking as free properties; the other costs a week and buys evidence only at the boundaries you instrumented. Teams that pick the cheap path and later need full replay cannot reconstruct history that was never written.*

### Can a decision made on a rented inference endpoint be made auditable, or does reproducibility require owning the model?

| Position A | Position B |
|---|---|
| It cannot: recreating a model-generated recommendation requires access into the model itself, third-party inference dependencies get redlined in real audits, and controlling data, traces, and compute locally is what makes step-by-step verification possible.<br>*[Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md), [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)* | Auditability is a property of the harness, not the weights: receipts at the commit boundary, evidence produced by a separate verifier model, and a shared receipt interface that explicitly does not require every node to run the same software stack.<br>*[Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)* |

*Why it matters: If reproducibility genuinely requires model access, regulated deployments must own or self-host inference, which changes the cost structure by orders of magnitude. If receipts at the boundary suffice, hosted frontier models stay viable in compliance-bound settings.*

## Practical Guidance

**Do:**

- Emit a receipt per action recording four things separately: what policy allowed, what was attempted, what executed, and what the user-visible edge confirmed — internal success is not external proof.
- Model 'done' as an object with artifact, scope, rubric, evidence, verifier, approver, residual risk, and next action, instead of a single green checkmark that conflates mergeable, deployable, and announceable.
- Make the verifier a different model from the author (code with Claude, verify with Codex) and give it real verification tooling — browser harnesses, screenshots, custom hooks — rather than asking the author whether it is done.
- Keep agent self-modification and agent actions in one immutable event log rather than tracking them in two places, so state is a projection of the log and replay/rollback/fork come for free.
- Bind every agent to its own identity — its own private key or client ID, always reporting to a named user — instead of handing it the user's credentials, and log the grant, its scope, and its expiry.
- Resolve flags and authority per turn, not at session start, and force sub-agents through the same middleware, so a kill switch reaches in-flight work and spawned children.
- Hold flag audit-trail completeness at 100% (who flipped what, when), and target under 5 minutes to a kill switch and under 30 minutes to a prompt rollback.
- Make provenance one click: a reviewer should land on the exact source paragraph in about 30 seconds, and estimates should carry a label that survives being copy-pasted into someone else's slides three weeks later.
- Escalate contradictions between sources to a human instead of resolving them silently — the contradiction is the highest-value signal in diligence.
- Log which gate failed, not just the final artifact, so a 2 a.m. scheduled-run failure is diagnosable from the record alone.
- Instrument the most expensive handoff first — the one where bad data costs the most — rather than the most technically interesting one.
- Give every external boundary a terminal state (success, failure, timeout, cancel, max attempts) and make recovery commands runnable without queueing behind the stuck work.

**Avoid:**

- Asking the model to check its own output — 'are these cases real?' answered by the same chatbot is not a hallucination control.
- Treating a tool's success return or a clean transcript as proof the effect reached the user; delivery can survive while state does not.
- Gates that only log warnings, which are suggestions rather than controls.
- Sub-agents that bypass the flag/audit middleware — the parent looks governed while a flipped kill switch never reaches the child.
- Letting the agent act as the user or pretend to be the user, which destroys per-agent attribution at exactly the moment you need it.
- Coarse OAuth scopes as the audit substrate: 'can send email on your behalf' records nothing about hour, sender, or recipient.
- Relying on a person happening to have both documents open at once to catch a contradiction — luck is not a control.
- Keeping temporary rollout flags past their removal date; every flag needs an owner and a deletion date or it becomes a load-bearing hidden coupling.
- Assuming a rented inference endpoint will let you reconstruct a recommendation when an auditor asks; third-party dependencies have been redlined for exactly this.
- Shipping because the artifact looks complete — the dangerous failure is a polished output that passed no check, not a visibly bad one.
- Prompting a human for approval on every read action in a background-agent setting; it is both unusable and no longer a real control.

## Notable Outliers

- An agent's identity should be understood as derived from its own event log — we are not our reasoning capability but the beliefs and behaviors derived from lived experience — making the audit log constitutive of the agent rather than a record about it. ([Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md), [16:36](https://www.youtube.com/watch?v=khVX_BUnEwU&t=996s))
- In an audit of nearly 4,000 ClawHub skills, over one in eight had a critical severity issue and 76 malicious payloads were found; malicious skills can modify agent memory, so they persist even after the skill is removed. ([Agentic Development Security](../talks/agentic-development-security.md), [7:14](https://www.youtube.com/watch?v=cgimkNGNjvU&t=434s))
- More than two kill-switch fires per week indicates a problem worth investigating; the target is zero. ([Agents Need Feature Flags](../talks/agents-need-feature-flags.md), [14:41](https://www.youtube.com/watch?v=zU4EagB311U&t=881s))
- Deliberately capping the security-critical codebase at roughly 20k lines of a memory-safe language, mostly attestation verification, is what makes full external audit feasible at all. ([Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md), [11:40](https://www.youtube.com/watch?v=IvE8n-ylFYY&t=700s))
- Cross-document correlation cut false positives by 76% and manual audit effort by roughly 40% across ~3 million records over 4 regulatory jurisdictions, turning compliance from periodic review into a continuous function. ([AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md), [11:28](https://www.youtube.com/watch?v=Iwe_RY-fYgI&t=688s))
- A third-party inference vendor dependency was redlined during an audit and the deployment could not go forward — the blocker was procurement-side auditability, not model quality. ([Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [4:15](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=255s))

## All Talks

- [Active Graph Agent Runtime (BabyAGI 4)](../talks/active-graph-agent-runtime-babyagi-4.md)
- [Agentic Development Security](../talks/agentic-development-security.md)
- [Agents Need Feature Flags](../talks/agents-need-feature-flags.md)
- [Agents Need Receipts, Not More Tool Calls](../talks/agents-need-receipts-not-more-tool-calls.md)
- [AI-Driven Multi-Document Correlation for Financial Compliance](../talks/ai-driven-multi-document-correlation-for-financial-compliance.md)
- [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)
- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)
- [Full Workshop: Better Auth](../talks/full-workshop-better-auth.md)
- [Memory Harnesses for Long-Running Research Agents](../talks/memory-harnesses-for-long-running-research-agents.md)
- [Privacy-Preserving Intelligence](../talks/privacy-preserving-intelligence.md)
- [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)
- [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)
- [You Didn't Ship a Bug. You Just Wrote It for a Human.](../talks/you-didnt-ship-a-bug-you-just-wrote-it-for-a-human.md)
- [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)

## Speakers

- [Armanas Povilionis](../speakers/armanas-povilionis.md)
- [Dotta](../speakers/dotta.md)
- [Ezra Tanzer](../speakers/ezra-tanzer.md)
- [Paola Estefania](../speakers/paola-estefania.md)
- [Ravi Madabhushi](../speakers/ravi-madabhushi.md)
- [Sachin Gupta](../speakers/sachin-gupta.md)
- [Shawn Chan](../speakers/shawn-chan.md)
- [Stefania Druga](../speakers/stefania-druga.md)
- [Steve Korshakov](../speakers/steve-korshakov.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)
- [Varsha Shah](../speakers/varsha-shah.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Yohei Nakajima](../speakers/yohei-nakajima.md)

