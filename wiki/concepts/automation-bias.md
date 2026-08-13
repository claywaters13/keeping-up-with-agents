---
title: "automation bias"
type: "concept"
slug: "automation-bias"
tier: "supporting"
maturity: "consolidating"
talk_count: 8
speaker_count: 8
---

# automation bias

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **8** talk(s) by **8** speaker(s)

**Definition:** Human oversight degrading because reviewers rubber-stamp agent output — approval fatigue, alert fatigue, and the erosion of meaningful review.

*Also referred to as: approval fatigue, consent fatigue, human-in-the-loop approval friction, self-verification bias, alert fatigue, stated attitudes vs revealed behavior*

## State of Practice

Automation bias has moved from a psychology-literature curiosity to a measured, reproducible failure mode in production AI systems, and the conference treated it as a design defect rather than a training problem. Duolingo's controlled injection of fabricated AI flags found that proctors scoring above 90% on calibration accuracy still upheld 50% of the fake signals — a coin-flip rate that reviewer skill did not protect against — while Sonar cited work showing developers follow AI advice nearly 80% of the time when the AI is wrong. The consequence is not just bad individual decisions but corrupted feedback loops: rubber-stamped approvals get logged as ground truth, making models spuriously more confident and polluting the next training set. The field's emerging answer is to stop treating 'add a human in the loop' as a control and instead engineer the interaction — route friction by stakes (auth, money movement, permissions, irreversible data get line-by-line reading; low-criticality changes do not), keep the generator out of the verification path, and back approval with policy that can override a fatigued human. Alert volume is understood as the other half of the problem: a system that flags everything as high-priority trains reviewers to stop acting entirely. Nobody at this conference argued that better models will dissolve the problem; the debate is over whether the fix is interaction design, independent automated verification, or policy enforcement below the approval layer.

## Consensus

### Human reviewers accept confidently-wrong AI output at rates near 50-80%, so review skill and calibration do not protect against automation bias.

Support: **4** talk(s)

> "while participants did follow the AI advice 92.7% of the time when the AI was correct, they unfortunately also listened to the AI nearly 80% of the time when the AI was wrong"
>
> — [Guide, Verify, Solve](../talks/guide-verify-solve.md), [6:35](https://www.youtube.com/watch?v=03l29gJXpCE&t=395s)

Supporting talks: [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)

### Human-in-the-loop approval by itself is not a sufficient control and must be backed by something structural — interaction redesign, independent verification, or policy enforcement.

Support: **4** talk(s)

> "And we can't just solve this with human in the loop. We spent decades solving access management for humans. So just blindly trusting a human who might be a little bit consent fatigued uh or who might be tired enough at night, this isn't really going to be enough."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s)

Supporting talks: [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

### Oversight should be routed by stakes rather than applied uniformly: high-criticality actions (auth, money movement, permissions, irreversible data, destructive infra operations) get deliberate friction and line-by-line human attention; low-criticality changes do not.

Support: **4** talk(s)

> "You read every line of authentication, money movement, permissions, and irreversible data."
>
> — [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [14:28](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=868s)

Supporting talks: [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)

### Alert and approval volume is itself a cause of oversight collapse — flagging too much makes reviewers stop acting and stop trusting the system.

Support: **3** talk(s)

> "If everything is flagged as hot to a sales rep, they would stop acting because it's it just gets overwhelming for them. And at that moment, they stop trusting the system and the system's dead."
>
> — [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [21:34](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1294s)

Supporting talks: [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)

### Cheaper generation has not made verification cheaper, so review is now the bottleneck — and the measured cost of skipping it is showing up as incidents, bugs, and static-analysis debt.

Support: **3** talk(s)

> "Now, making generation cheaper does not automatically make review cheaper, right?"
>
> — ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [3:50](https://www.youtube.com/watch?v=n97BCfyFIvw&t=230s)

Supporting talks: ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Guide, Verify, Solve](../talks/guide-verify-solve.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)

## Disagreements

### Is the fix for rubber-stamping to redesign the human's interaction so they actually deliberate, or to assume humans will rubber-stamp and put an automated/policy backstop underneath them?

| Position A | Position B |
|---|---|
| Fix the interaction. Duolingo shifted rejection rates 21% by changing only guideline copy — no model, no UI change — and argues the engineer's only real lever is the interaction, with the goal of making verification cheap, clear, and hard to skip.<br>*[Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)* | Assume the human fails. Sonar argues rubber-stamping is already pervasive and must be backstopped by independent automated verification; Keycard evaluates policy before a credential is even minted and will override a human's explicit approval when the approver lacks the required role.<br>*[Guide, Verify, Solve](../talks/guide-verify-solve.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)* |

*Why it matters: It determines where engineering budget goes — into review UX and label quality, or into a separate verification/policy layer that can veto approvals — and whether a human 'yes' is treated as authoritative or as one input among several.*

### Should oversight systems deliberately add friction, or minimize it to preserve adoption?

| Position A | Position B |
|---|---|
| Add friction on purpose. Build it in exactly where stakes are high, reframe the reviewer as an investigator rather than a validator, and read every line of critical code even though attention is expensive.<br>*[Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)* | Friction kills the system. If editing an AI-drafted email takes more than 30 seconds, reps abandon the tool and write their own — the initiative is dead, so review cost must be driven near zero.<br>*[Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)* |

*Why it matters: Sets the design target for every approval surface: whether you optimize for reviewer deliberation (accepting slower throughput and possible abandonment) or for reviewer throughput (accepting that some approvals will be reflexive).*

## Practical Guidance

**Do:**

- Inject fabricated or known-false signals into your review queue and measure the uphold rate — a rate near 50% among calibrated reviewers is evidence of automation bias, not of reviewer skill.
- Frame the AI output in reviewer-facing copy as a preliminary alert requiring independent evidence, and name the human as the final decision-maker (this alone moved rejection rates 21% at Duolingo).
- Split conflated CTAs: ask separately whether the model's perception was correct and whether the action should be taken, so labels stay honest.
- Log the human's subsequent manual edit, not just the yes/no decision — recording only the verdict captures a false signal that pollutes the dataset.
- Verify with a different methodology than the one that generated the code; combine computational/static review with LLM-driven review rather than relying on either.
- Run verification inside the inner agentic loop, not just in CI/CD, so defects are caught before they propagate into subsequent loops.
- Request tokens per tool call, audience-bound to a single target server, expiring in minutes and never stored, so an approval grants only the action being proposed.
- Check the human's approval itself against policy and the approver's role — an exhausted person should not be able to accept everything.
- Ask agents to decompose large changes into atomic, reviewable PRs; they are better at this than humans.
- Encode a caught mistake into docs, linters, and reviewers rather than relying on catching it again in review.
- Define success metrics and the data you need before building the system, instead of asking afterward how to evaluate the model.
- Keep fit score and intent score separate rather than collapsing them into one priority signal.

**Avoid:**

- Treating 'add more human oversight' as a quality fix — sometimes the defect is the interaction, not the model or the reviewer.
- Coding-agent interfaces that present one giant diff or a per-file approval prompt; both reduce the developer to a rubber stamp and yield low-information accept/reject data.
- Letting the same agent write the code and write or grade its own tests — if the builder grades itself, you hid the review rather than removed it.
- Merging PRs with no review at all, human or agentic (up 31% per the Faros AI survey).
- Flagging everything as high-priority; overwhelmed reviewers stop acting and stop trusting the system.
- Giving agents long-lived kitchen-sink API keys — an agent will use every permission it has to complete the task.
- Permitting an agent to drop a database, even when the documented recovery runbook calls for it.
- Running more agents in parallel as a capacity strategy — cognitive bandwidth does not parallelize, and each loop adds routing, merging, and verification decisions.
- Thumbs up/down as your feedback mechanism; it lacks the nuance to drive improvement.
- Shipping code no human on the team can explain well enough to defend, even if no human typed or read every line.

## Notable Outliers

- Reviewers scoring consistently above 90% on accuracy calibration still accepted 50% of injected fake AI signals — a coin-flip rate that is diagnostic of automation bias. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s))
- A pure copy change to the reviewer guidelines — no model change, no UI change — produced a 21% increase in rejection rates. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s))
- A human's explicit approval of an agent action can and should be overridden by policy when the approver lacks the required role. ([It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [14:54](https://www.youtube.com/watch?v=I3znWC3MEXM&t=894s))
- There is a hard ceiling on how well any system can match human judgment, because humans were measured as only 80% consistent with themselves. ([Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md), [17:03](https://www.youtube.com/watch?v=YnNF55QV0zs&t=1023s))
- Full-access agent modes remain unsafe regardless of model quality, because pushing a model toward high agency produces creative workarounds that diverge from user intent. ([Codex, Behind the Harness](../talks/codex-behind-the-harness.md), [12:30](https://www.youtube.com/watch?v=shRR1e2HXMk&t=750s))

## All Talks

- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Build the AI GTM Agent That Knows the Buyer](../talks/build-the-ai-gtm-agent-that-knows-the-buyer.md)
- [Codex, Behind the Harness](../talks/codex-behind-the-harness.md)
- [Guide, Verify, Solve](../talks/guide-verify-solve.md)
- [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)
- [Persona Engineering: A Field Guide to AI Synthetic Personas](../talks/persona-engineering-a-field-guide-to-ai-synthetic-personas.md)
- [Should AI Engineers Still Read Code in 2026? The Z/L Continuum](../talks/should-ai-engineers-still-read-code-in-2026-the-zl-continuum.md)
- ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)

## Speakers

- [Alex Volkov](../speakers/alex-volkov.md)
- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Anirban Chatterjee](../speakers/anirban-chatterjee.md)
- [Dominik Kundel](../speakers/dominik-kundel.md)
- [Ishan Anand](../speakers/ishan-anand.md)
- [Kim Maida](../speakers/kim-maida.md)
- [Sajjan Kanukolanu](../speakers/sajjan-kanukolanu.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)

