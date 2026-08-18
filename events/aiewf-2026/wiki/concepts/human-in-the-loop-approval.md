---
title: "human-in-the-loop approval"
type: "concept"
slug: "human-in-the-loop-approval"
tier: "core"
maturity: "contested"
talk_count: 29
speaker_count: 28
---

# human-in-the-loop approval

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **29** talk(s) by **28** speaker(s)

**Definition:** Requiring explicit human authorization before an agent takes a consequential or irreversible action, including how approval is scoped and where gates are placed.

*Also referred to as: human-in-the-loop approval gates, human in the loop approval, human-in-the-loop tool approval, plan approval for irreversible actions, tool approval policy, approval scoping and authority binding, blocking gates*

## State of Practice

The field has converged on gating mutating and irreversible actions behind explicit human authorization, but has stopped believing that the approval click is itself a control. Three failure modes dominate the discussion: approvals that exist only as a prompt instruction (which the agent can satisfy for itself), approvals that a fatigued human rubber-stamps at coin-flip accuracy, and approvals that simply do not exist because the agent is running in the background at 2am. The response is to move enforcement down into the harness — deterministic loop interrupts on mutating tool calls, per-tool-call scoped credentials evaluated against policy before the credential is minted, locked tool arguments, and gates that block rather than log — and to move the human's decision up, from reviewing raw output to reviewing machine-generated evidence (canary results, traces, provenance click-throughs, structured non-code artifacts). Accountability is treated as non-delegable in every talk that raises it: a named human signs, and the agent cannot inherit the consequence. What remains unresolved is whether approval is the permanent control surface or a temporary scaffold to be removed once the loop is calibrated, and whether gates belong at the plan or at each individual call.

## Consensus

### Irreversible, mutating, or outbound actions must be walled behind explicit human approval while reversible work runs autonomously; the gate is placed at the blast-radius boundary, not uniformly.

Support: **7** talk(s)

> "those actions need to be walled behind like my approval, right? And when you draw that wall, what you've done is reduced the blast radius"
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [16:30](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=990s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)

### The approval gate must be enforced deterministically by the harness or policy layer; an instruction in a prompt telling the model to ask for confirmation is not a human in the loop.

Support: **7** talk(s)

> "people sometimes will add the instruction like you need to ask for confirmation but the AI may ask confirmation for itself. So from your perspective there is a human in the loop but for the AI perspective there is has been a confirmation"
>
> — [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [12:33](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=753s)

Supporting talks: [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Agentic Development Security](../talks/agentic-development-security.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md)

### A human approval click is weak evidence of oversight: reviewers rubber-stamp under volume and fatigue, so the presence of an approval step does not mean the decision was actually made.

Support: **6** talk(s)

> "despite the fact that our human reviewers are consistently scoring above 90% on their accuracy calibration metrics, they actually accepted 50% of these fake signals"
>
> — [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s)

Supporting talks: [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)

### Accountability for an agent's action stays with a named human and cannot be transferred to the model or its vendor, which is the underlying reason a signature step exists at all.

Support: **5** talk(s)

> "You can't outsource accountability to your own software. At the bottom of every real decision, a human signs."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [19:21](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1161s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Agentic Development Security](../talks/agentic-development-security.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)

### The approval step should be fed machine-generated evidence — canary results, runtime verification, provenance links, structured non-code artifacts — rather than raw agent output, so the human is investigating rather than validating.

Support: **6** talk(s)

> "you should use that deterministic final outcome to produce outputs that are easy to validate even for non-coders. The code is kind of just the means to an end."
>
> — [Respect The Process](../talks/respect-the-process.md), [15:57](https://www.youtube.com/watch?v=CLttOU7n6sI&t=957s)

Supporting talks: [Respect The Process](../talks/respect-the-process.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)

## Disagreements

### Is human approval a real access control for consequential agent actions, or a supplement to deterministic policy that cannot itself be relied on?

| Position A | Position B |
|---|---|
| Approval is the primary control for the consequential class of actions: the loop interrupts, a human authorizes the mutating call, and that gate is what keeps the system safe.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)* | Approval is not an access control. Humans are consent-fatigued, many agents run unattended, and the real enforcement must be policy evaluated before a credential is minted, arguments locked out of the model's reach, or capability withheld outright — with the human's approval itself subject to override.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Agentic Development Security](../talks/agentic-development-security.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)* |

*Why it matters: It decides whether you invest in approval UX and reviewer training or in an authorization layer with scoped, short-lived, audience-bound credentials. Side B's position also implies background and cloud agents are ungovernable by approval at all, so the control must exist below the interaction layer.*

### Should the human stay permanently in the approval path for consequential actions, or is the human a scaffold to be removed once the loop is calibrated?

| Position A | Position B |
|---|---|
| Keep the human permanently. Never auto-push to production, never let an agent send outbound communication, never let an agent drop a database — the gate is by intent, not a temporary limitation of current models.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)* | The human is the throughput ceiling and should be engineered out. Close the loop until you are the bottleneck, then remove yourself; a human is needed only at the first and last step; exhaustive human verification degenerates into theater at volume.<br>*[The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)* |

*Why it matters: This sets whether you build for a fixed approval rate or for an increasing autonomy ratio with trust thresholds (~80-90%) and verifier agents. It also determines whether approval throughput is a permanent capacity constraint on the whole system.*

### Where should the gate sit — on the individual tool call, or on the plan before execution begins?

| Position A | Position B |
|---|---|
| Per-action: interrupt at each mutating tool call, mint permissions for that single call, and raise an interrupt from sensitive functions themselves, so the human authorizes exactly the action being taken.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md)* | Plan-level: present the intended plan for approval before execution, pause when the agent is about to make an assumption, and let the human review the spec up front — with settings to switch the gate off for repeated flows.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)* |

*Why it matters: Per-call gates give precise authority scoping but generate the consent fatigue that makes approvals meaningless; plan-level gates preserve attention and latency but authorize a batch of actions whose details the human never sees.*

## Practical Guidance

**Do:**

- Interrupt the agent loop deterministically in code when a tool call requires approval, especially for mutating operations — do not leave the decision to the model's judgment.
- Request a token per tool call rather than per session, audience-bound to a single target MCP server, expiring within minutes and never stored.
- Evaluate policy before minting the credential, so a denied action leaves nothing to leak, replay, or steal.
- Check the approving human's role against policy and allow the system to override an approval the approver was not entitled to give.
- Lock sensitive tool arguments via partial function application so the LLM cannot see or change them — this buys safety without paying per-action approval latency.
- Model approval as scoped execution state bound to actor, session, run, tool, arguments, and lifetime, and make expiration terminate rather than loop.
- Run an automated canary comparing CPU, latency, and error rate before a change reaches a human reviewer; passing tests alone are not sufficient evidence for the approver.
- Frame the AI signal in reviewer guidelines as a preliminary alert requiring independent evidence, with the human as the final decision-maker — copy changes alone moved rejection rates 21%.
- Split the approval CTA so 'was the model's perception correct' is a separate question from 'should we take the consequential action', so labels stay honest.
- Add friction deliberately where stakes are high and remove it where oversight is low; treat the human as investigator rather than validator.
- Surface one high-ROI, human-readable finding at a time instead of a batch of auto-opened PRs.
- Present a plan for irreversible or dangerous actions, and pause whenever the agent is about to make an assumption.
- Route all outbound communication through a human — draft autonomously, send manually.
- Give non-engineer approvers structured review artifacts produced by deterministic post-run execution, not agent-written code to read.
- Show a time and cost estimate before the user approves an action, and keep a prominent, always-available stop control.
- Allocate each workflow step explicitly to autonomous, human-in-the-loop, or human-only, rather than declaring the whole process supervised.

**Avoid:**

- Writing 'ask the user for confirmation' into a prompt or skill and counting it as a human in the loop — the agent can satisfy that confirmation itself.
- Gates that only log a warning; a gate that cannot block the artifact from moving forward is a suggestion.
- Relying on approval prompts to govern background or cloud agents, where nobody is at the desk to answer them.
- Presenting one giant diff or a per-file accept/reject prompt — both reduce the reviewer to a rubber stamp and yield low-information labels.
- Logging the yes/no decision as ground truth while discarding the human's subsequent manual edit; that pollutes the training set and makes the model spuriously more confident.
- Assuming reviewer skill protects against automation bias — >90%-calibrated experts still upheld half of fabricated flags.
- Handing an agent a long-lived kitchen-sink API key and treating your supervision as the compensating control.
- Making human review the throughput ceiling of the system rather than a verification step on evidence.
- Treating a transcript, or the agent's own claim of completion, as proof that the approved action actually happened at the user-visible edge.

## Notable Outliers

- A human's approval can itself be rejected: policy checks the approver's role, so an exhausted person cannot simply accept everything — the approval was blocked even though the speaker had clicked allow. ([It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [14:54](https://www.youtube.com/watch?v=I3znWC3MEXM&t=894s))
- Changing only the reviewer guideline copy — framing the AI signal as preliminary and requiring independent evidence — increased rejection rates 21% with no model or UI change. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s))
- Partial function application on tool arguments removes the need for human approval entirely on that dimension: the model cannot change the locked argument and does not even know it exists. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [16:54](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1014s))
- Process redesign should assign autonomy per step explicitly — four of eight steps fully autonomous, three with human-in-the-loop intervention, one human-only, period. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [6:30](https://www.youtube.com/watch?v=l0FLhNqBOic&t=390s))
- Human override rate on AI verdicts should be tracked as a production metric; a rising rate above threshold is the signal that the system is not doing its job. ([AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md), [24:28](https://www.youtube.com/watch?v=T0HhO4YtTfE&t=1468s))

## All Talks

- [Agentic Development Security](../talks/agentic-development-security.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md)
- [AI System Design: From Idea to Production](../talks/ai-system-design-from-idea-to-production.md)
- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md)
- [Build Systems, Not Code](../talks/build-systems-not-code.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Every Harness Will Become A Claw](../talks/every-harness-will-become-a-claw.md)
- [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)
- [Field Guide to Fable](../talks/field-guide-to-fable.md)
- [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)
- [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)
- [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)
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
- [Rushabh Doshi](../speakers/rushabh-doshi.md)
- [Sam Bhagwat](../speakers/sam-bhagwat.md)
- [Shawn Chan](../speakers/shawn-chan.md)
- [Sumaiya Shrabony](../speakers/sumaiya-shrabony.md)
- [Thariq Shihipar](../speakers/thariq-shihipar.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)
- [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)

