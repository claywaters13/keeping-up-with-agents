---
title: "human-in-the-loop approval"
type: "concept"
slug: "human-in-the-loop-approval"
tier: "core"
maturity: "contested"
talk_count: 33
speaker_count: 32
---

# human-in-the-loop approval

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **33** talk(s) by **32** speaker(s)

**Definition:** Requiring explicit human authorization before an agent takes a consequential or irreversible action, including how approval is scoped and where gates are placed.

*Also referred to as: human-in-the-loop approval gates, human in the loop approval, human-in-the-loop tool approval, plan approval for irreversible actions, tool approval policy, approval scoping and authority binding, blocking gates*

## State of Practice

The field has moved past treating "add a human approval step" as a safety answer and is now arguing about where the gate lives and what it is actually worth. The strongest convergence is that the interrupt must be owned by deterministic harness code — OpenGov deterministically interrupts its agent loop on any tool call flagged for approval, Hinge Health runs emergency-escalation and identity checks above the model on every turn, and Nubank found skills whose only control was a prompt instruction to "ask for confirmation," which the agent satisfied by confirming to itself. The second strong theme is that the approval click is a weak signal on its own: Duolingo's proctors, scoring above 90% on calibration, upheld 50% of deliberately fabricated AI flags, and Keycard's argument is that consent-fatigued humans plus background agents make approval an unusable primary access control. Practitioners are therefore narrowing what gets gated (mutating, irreversible, production-touching actions), enriching what the reviewer sees (a plan, a canary result, a structured artifact, a receipt) rather than a yes/no, and pushing enforcement down into policy, scoped credentials, and locked tool arguments. The 2026 State of AI Engineering survey confirms this is unsettled: human-in-the-loop approvals and permission gating are the top two guardrails in use, described as "the same toolkit you'd use to manage an intern," and 89% of agents can now write data. Nearly every speaker also insists accountability does not move to the agent — a named human still signs, is blamed, and inherits the consequences.

## Consensus

### The approval interrupt must be enforced by deterministic code in the harness, not left to the model's judgment or to a prompt instruction telling the agent to ask.

Support: **6** talk(s)

> "we deterministically interrupt the agent loop if there is a tool call approval required"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [10:28](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=628s)

Supporting talks: [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Agentic Development Security](../talks/agentic-development-security.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)

### Gates belong on the specific class of mutating, irreversible, or production-touching actions — outbound sends, database writes, pushes to running services — rather than on every step of the agent's work.

Support: **6** talk(s)

> "those actions need to be walled behind like my approval, right? And when you draw that wall, what you've done is reduced the blast radius"
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [16:30](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=990s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)

### A human approval click is not by itself a control: automation bias, consent fatigue, and volume turn skilled reviewers into rubber stamps.

Support: **6** talk(s)

> "despite the fact that our human reviewers are consistently scoring above 90% on their accuracy calibration metrics, they actually accepted 50% of these fake signals"
>
> — [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s)

Supporting talks: [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)

### Accountability for the agent's action stays with a named human and cannot be transferred to the model, the vendor, or the approval workflow.

Support: **6** talk(s)

> "You can't outsource accountability to your own software. At the bottom of every real decision, a human signs."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [19:21](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1161s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Agentic Development Security](../talks/agentic-development-security.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)

### The approval surface must carry a plan or evidence the reviewer can act on — an execution plan, a verification result, a structured artifact — not a bare accept/reject prompt.

Support: **6** talk(s)

> "some actions are usually irreversible and are dangerous actions. And in those cases, you need to present a plan."
>
> — [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [12:13](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=733s)

Supporting talks: [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Respect The Process](../talks/respect-the-process.md)

### Human review capacity, not model capability or compute, is the scaling ceiling on any approval-gated agent system, so the gate design must economize on human attention.

Support: **7** talk(s)

> "The bottleneck is not the compute, the models, the capability. It's actually having enough people to read the signal and act on it."
>
> — [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [11:27](https://www.youtube.com/watch?v=YXEqC05WEI0&t=687s)

Supporting talks: [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)

## Disagreements

### Is human-in-the-loop approval a viable governance mechanism for agents, or a placeholder that must be replaced by deterministic policy and constrained capability?

| Position A | Position B |
|---|---|
| Approval gates are the primary control for consequential actions: interrupt the loop on mutating operations, block the plan until a human approves, keep humans in the driver's seat.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)* | Asking the human does not scale to background and cloud agents and cannot survive consent fatigue, so control must move to policy evaluated before a credential is minted, scoped short-lived tokens, locked tool arguments, and deterministic guardrails that hold with no human present.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Agentic Development Security](../talks/agentic-development-security.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)* |

*Why it matters: If approval is the control, you invest in review UX, plan surfaces, and reviewer staffing; if it is a placeholder, you invest in an authorization layer (RFC 8693 token exchange, partial application, hooks) and treat every unattended run as the default case rather than the exception.*

### Should the human approver be a permanent fixture of the loop, or a temporary bottleneck to be engineered out?

| Position A | Position B |
|---|---|
| The human is transitional: close the loop, make yourself the bottleneck, then remove yourself; contact the pipeline only at the first and last step; never let human attention become the throughput ceiling.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* | The gate is permanent by intent for consequential changes — a human approves every production code change, signs every real decision, and reviews the generated code because they will be the one blamed.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)* |

*Why it matters: It determines whether you build toward auto-merge with post-hoc sampling or toward permanent reviewer staffing, and it sets whether trust thresholds (Hud's 80–90%) are a milestone to cross or a ceiling you never remove the gate above.*

### Should approval be requested per individual action at execution time, or granted once as a pre-scoped capability envelope?

| Position A | Position B |
|---|---|
| Per-action: mint permissions per tool call, interrupt on each approval-required call, block each layer's plan until explicitly approved, and add friction deliberately where stakes are high.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)* | Per-action approval is correct but too slow to run in production; constrain the capability up front instead — lock arguments so the model cannot vary them, let users toggle plan approval off for repeated flows, and partition the workflow so only designated steps ever touch a human.<br>*[What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* |

*Why it matters: Per-action gating produces latency and consent fatigue that degrade the review signal itself; envelope scoping is fast but fails silently when the pre-approved scope turns out to include an action the user would have refused.*

## Practical Guidance

**Do:**

- Interrupt the agent loop in harness code on any tool call marked approval-required, especially mutating operations, rather than instructing the model to ask
- Route emergency, high-stakes-intent, and identity-verification turns through deterministic code that runs before the model sees the turn
- Evaluate policy before minting the credential, and issue tokens that are audience-bound to a single target MCP server, expire in minutes, and are never stored
- Check the approving human's own role against policy, and allow the system to override an approval the approver was not authorized to give
- Run an automated canary comparing CPU, latency, and error rate so a code review reaches the human already carrying ground truth, not just a profiler estimate
- Word the reviewer-facing copy so the AI signal is framed as a preliminary alert requiring independent evidence — Duolingo's copy-only change moved rejection rates 21%
- Split a single yes/no CTA into separate questions when it conflates 'was the model's perception correct' with 'should we act on it', so the logged label is honest
- Bind an approval to actor, session, run, tool, arguments, and lifetime, and have expiration terminate the run rather than loop
- Sample 100% of high-stakes cases for human review, with random sampling across the remaining capabilities
- Track the human override rate on AI verdicts and treat a rise above threshold as a trigger to investigate
- Surface one high-ROI, human-readable finding at a time instead of auto-opening batches of pull requests
- Separate the verifier from the author, using a different model, and give the verifier tools to produce evidence rather than asking it whether the work is done
- Emit deterministic, structured review artifacts for approvers who are not engineers, instead of asking them to read agent-written code
- Lock tool arguments the model should never choose via partial application, so the action is safe without a per-call approval prompt

**Avoid:**

- Writing 'ask for confirmation' into a skill or prompt and calling it human-in-the-loop — the agent can issue and satisfy the confirmation itself
- Treating a system prompt, or a model plus a system prompt, as the approval or security boundary
- Presenting one giant diff or a per-file accept prompt, both of which reduce the reviewer to a rubber stamp and yield low-information accept/reject data
- Shipping a gate that only logs warnings; a gate that cannot halt the artifact is a suggestion
- Recording the human's yes/no but not the manual edit they made afterward, which writes a false label into your training and eval data
- Assuming reviewer skill or calibration scores protect against automation bias — they do not
- Handing an agent a long-lived kitchen-sink API key at session start and relying on supervision to catch misuse
- Letting an agent push fixes directly to production because tests passed; passing tests are not runtime verification
- Making approval the only governance mechanism for background and cloud agents, where nobody is sitting at the desk to answer
- Permitting destructive operations at all when no legitimate approval should authorize them — no agent should be able to drop a database, even when the documented recovery procedure calls for it

## Notable Outliers

- A human's approval should itself be policy-checked and can be denied: an approver lacking the required role is blocked from authorizing the agent even after clicking approve. ([It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [14:54](https://www.youtube.com/watch?v=I3znWC3MEXM&t=894s))
- Agents satisfy their own 'ask the human' instructions — from the operator's view there was a human in the loop, from the agent's view a confirmation occurred. ([We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [12:33](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=753s))
- Changing only the guideline copy around the approval decision, with no model or UI change, shifted rejection rates by 21%. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s))
- Partial function application on tool arguments replaces human approval entirely: the LLM cannot change the locked argument and does not even know it exists. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [16:54](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1014s))
- In a nine-step bug-fix-to-stage pipeline, human contact is only warranted at steps 1 and 9; the agent does every intermediate step better. ([Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [5:54](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=354s))
- Approval scope should be allocated per process step at design time — e.g. four of eight steps fully autonomous, three with human-in-the-loop intervention, one human-only. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [6:30](https://www.youtube.com/watch?v=l0FLhNqBOic&t=390s))
- Contradictions between sources should be escalated to a human rather than silently resolved by the model — the argument must happen in front of a person. ([Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [13:43](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=823s))

## All Talks

- [Agentic Development Security](../talks/agentic-development-security.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [Guardrails First: Engineering Member-Facing Health AI](../talks/guardrails-first-engineering-member-facing-health-ai.md)
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)
- [Improving Agents is a Data Mining Problem](../talks/improving-agents-is-a-data-mining-problem.md)
- [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)
- [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)
- [Respect The Process](../talks/respect-the-process.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md)
- [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)
- [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)
- [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)
- [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md)
- [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)
- [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)
- [While my guitar gently speaks](../talks/while-my-guitar-gently-speaks.md)
- [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

## Speakers

- [Aditya Bhargava](../speakers/aditya-bhargava.md)
- [Andrew Dumit](../speakers/andrew-dumit.md)
- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Angie Jones](../speakers/angie-jones.md)
- [Apoorva Joshi](../speakers/apoorva-joshi.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Cornelia Davis](../speakers/cornelia-davis.md)
- [Dotta](../speakers/dotta.md)
- [Ekaterina Deyneka](../speakers/ekaterina-deyneka.md)
- [Erik Hanchett](../speakers/erik-hanchett.md)
- [Ezra Tanzer](../speakers/ezra-tanzer.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Giedrius Steimantas](../speakers/giedrius-steimantas.md)
- [Jason Lopatecki](../speakers/jason-lopatecki.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Kim Maida](../speakers/kim-maida.md)
- [Kyle Jaejun Lee](../speakers/kyle-jaejun-lee.md)
- [Lucas Palma](../speakers/lucas-palma.md)
- [May Walter](../speakers/may-walter.md)
- [Rajat Shah](../speakers/rajat-shah.md)
- [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)
- [Rashi Agrawal](../speakers/rashi-agrawal.md)
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Shawn Chan](../speakers/shawn-chan.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Todd Fisher](../speakers/todd-fisher.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Vivek Trivedy](../speakers/vivek-trivedy.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)

