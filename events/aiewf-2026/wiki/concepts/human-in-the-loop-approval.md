---
title: "human-in-the-loop approval"
type: "concept"
slug: "human-in-the-loop-approval"
tier: "core"
maturity: "contested"
talk_count: 32
speaker_count: 31
---

# human-in-the-loop approval

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **32** talk(s) by **31** speaker(s)

**Definition:** Requiring explicit human authorization before an agent takes a consequential or irreversible action, including how approval is scoped and where gates are placed.

*Also referred to as: human-in-the-loop approval gates, human in the loop approval, human-in-the-loop tool approval, plan approval for irreversible actions, tool approval policy, approval scoping and authority binding, blocking gates*

## State of Practice

The conference treated approval gates as necessary but demonstrably insufficient, and spent most of its energy on where the gate goes and what it is backed by rather than whether to have one. The dominant engineering pattern is a deterministic interrupt owned by the harness — the agent loop halts on a tool call flagged as mutating or irreversible, and the model has no say in whether the halt happens; a prompt instruction telling the agent to "ask for confirmation" was explicitly named a non-control, because the agent can satisfy its own confirmation. Against that, the security and access-control track argued approval is the weakest layer available: humans are consent-fatigued, agents increasingly run unattended in the background, and policy evaluated before a credential is minted (per-tool-call, audience-bound, minutes-long tokens) is strictly safer than a tired human clicking allow. Duolingo supplied the empirical bottom: reviewers scoring above 90% on calibration upheld 50% of fabricated AI flags, and a pure copy change framing the AI signal as preliminary moved rejection rates 21% — the interface, not the model or the reviewer's skill, determined the outcome. The remaining consensus is legal rather than technical: accountability does not transfer to the agent, so a named human must be answerable, which is why almost nobody endorsed auto-pushing to production even when the pipeline verifies itself. Where the field is actively split is whether the human sits before execution (plan approval) or after it (verified PR review), and whether friction at the gate should be deliberately added or engineered away.

## Consensus

### Irreversible, mutating, or externally-visible actions (sending mail, pushing to production, submitting offers, dropping state) should be walled behind explicit human approval, with the gate placed at those specific actions rather than uniformly across the loop.

Support: **7** talk(s)

> "those actions need to be walled behind like my approval, right? And when you draw that wall, what you've done is reduced the blast radius"
>
> — [Build Systems, Not Code](../talks/build-systems-not-code.md), [16:30](https://www.youtube.com/watch?v=ZD9-4fW2HhM&t=990s)

Supporting talks: [Build Systems, Not Code](../talks/build-systems-not-code.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md)

### The approval gate must be enforced deterministically by the harness or platform; a prompt instruction asking the model to check with the user, or a warning-only check, is not a gate.

Support: **6** talk(s)

> "people sometimes will add the instruction like you need to ask for confirmation but the AI may ask confirmation for itself. So from your perspective there is a human in the loop but for the AI perspective there is has been a confirmation"
>
> — [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [12:33](https://www.youtube.com/watch?v=iKQ78wyJEXU&t=753s)

Supporting talks: [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [We Vetted 2000 AI Skills Before They Reached Developers](../talks/we-vetted-2000-ai-skills-before-they-reached-developers.md), [Agentic Development Security](../talks/agentic-development-security.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md), [Respect The Process](../talks/respect-the-process.md), [Your Agent Didn't Fail. Your Harness Did.](../talks/your-agent-didnt-fail-your-harness-did.md)

### Human approval on its own is not a safety control: reviewers rubber-stamp under automation bias and consent fatigue, and human attention does not scale to agent output volume, so approval must be backed by policy, deterministic guardrails, or independent evidence.

Support: **7** talk(s)

> "And we can't just solve this with human in the loop. We spent decades solving access management for humans. So just blindly trusting a human who might be a little bit consent fatigued uh or who might be tired enough at night, this isn't really going to be enough."
>
> — [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [5:15](https://www.youtube.com/watch?v=I3znWC3MEXM&t=315s)

Supporting talks: [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [Agentic Development Security](../talks/agentic-development-security.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)

### The approval surface should present a plan, evidence, or a structured review artifact — a bare yes/no on an opaque output is a design failure that both destroys trust and produces worthless labels.

Support: **7** talk(s)

> "if you're creating some kind of an agentic tool and no plan is ever shown to the user and an action happens without them understanding why or how, it can be very, very hard for them to trust both the result of that action and the agentic tool itself"
>
> — [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [15:03](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=903s)

Supporting talks: [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Respect The Process](../talks/respect-the-process.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md)

### Accountability for an agent's actions stays with a named human and cannot be delegated to the model or its vendor, which is why an identifiable approver must exist at the end of every consequential action.

Support: **6** talk(s)

> "You can't outsource accountability to your own software. At the bottom of every real decision, a human signs."
>
> — [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [19:21](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1161s)

Supporting talks: [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), ["The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani](../talks/the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Agentic Development Security](../talks/agentic-development-security.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [Build Systems, Not Code](../talks/build-systems-not-code.md)

### Automated verification should run before the human gate so the reviewer sees an already-checked artifact — canaries, runtime confirmation, or a separate verifier agent — rather than a plausible-looking proposal.

Support: **6** talk(s)

> "You want to ask your agents to provide evidence. Don't just ask them to say, "Is this done?" But, give them the tools they need to verify that the work is done."
>
> — [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [5:59](https://www.youtube.com/watch?v=7P0elyLIxXo&t=359s)

Supporting talks: [AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Respect The Process](../talks/respect-the-process.md), [Every Solo Agent Builder Eventually Reinvents a Worse Version of CI/CD](../talks/every-solo-agent-builder-eventually-reinvents-a-worse-version-of-cicd.md)

## Disagreements

### Is per-action human approval a real control for consequential agent actions, or should it be replaced by deterministic policy and capability constraints that make approval unnecessary?

| Position A | Position B |
|---|---|
| Approval is the control: deterministically interrupt the loop on mutating or high-consequence tool calls and require a human to authorize before the agent proceeds.<br>*[Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Build Systems, Not Code](../talks/build-systems-not-code.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The Factory That Dreams: 39 AI Agents, No Framework](../talks/the-factory-that-dreams-39-ai-agents-no-framework.md)* | Approval does not scale and should be engineered out: constrain what the agent can do at all — policy evaluated before a credential is minted, per-tool-call short-lived audience-bound tokens, arguments locked by partial application — so that no human click is needed and there is nothing overprivileged to misuse.<br>*[It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [Agentic Development Security](../talks/agentic-development-security.md), [What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* |

*Why it matters: It decides whether you invest in approval UX or in an access-control/permission layer, and whether background and cloud agents that nobody is watching are viable at all — a gate that requires a present human simply does not fire for unattended runs.*

### Should the human gate sit before execution (approve the plan) or after it (review a completed, verified artifact)?

| Position A | Position B |
|---|---|
| Gate before the action: present a plan or pause the moment the agent is about to make an assumption or touch something irreversible, so nothing consequential happens unreviewed.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [I Run a Fleet of AI Agents Across Three Machines. Here's What Broke.](../talks/i-run-a-fleet-of-ai-agents-across-three-machines-heres-what-broke.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)* | Let the agent run to completion inside a sandbox and gate at the artifact: it opens a PR with a canary or runtime verification attached, and the human reviews evidence rather than intentions.<br>*[AI Agents for Performance: Ship Faster, Pay Less](../talks/ai-agents-for-performance-ship-faster-pay-less.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* |

*Why it matters: Pre-execution gates bound blast radius but stop the task dead and put the human on the critical path of every run; post-hoc gates preserve throughput but only work where the work is sandboxed, reversible, and independently verifiable before it reaches production.*

### Should friction at the human checkpoint be deliberately increased, or systematically removed?

| Position A | Position B |
|---|---|
| Add friction where stakes are high and reframe the human as investigator rather than validator — the checkpoint exists to force deliberation, and removing effort is what produced rubber-stamping in the first place.<br>*[Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Build for the Memo, Not the Demo](../talks/build-for-the-memo-not-the-demo.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)* | Minimize human contact points and automate the human out of the middle of the loop — human touch belongs at the start and end only, and exhaustive verification at volume degenerates into theater anyway.<br>*[Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [The Missing Layer After Launch](../talks/the-missing-layer-after-launch.md), [From Signal to PR: Anatomy of a Self-Improving Agent](../talks/from-signal-to-pr-anatomy-of-a-self-improving-agent.md)* |

*Why it matters: The two camps optimize opposite metrics — oversight quality versus throughput — and produce incompatible interfaces: one deliberately slows the reviewer down at the decision, the other measures success by how few decisions reach a human.*

## Practical Guidance

**Do:**

- Interrupt the agent loop deterministically in harness code when a tool call is marked approval-required, rather than instructing the model in a prompt to ask the user.
- Bind an approval to actor, session, run, tool, arguments, and lifetime, and make expiry terminate the run rather than loop back for another attempt.
- Check the approving human against policy and role before honoring the approval — an approver without the required role should be blocked even after they click allow.
- Request per-tool-call tokens that are audience-bound to a single target MCP server, expire in minutes, and are never stored, instead of handing the agent a session-scoped API key.
- Lock sensitive tool arguments by partial application so the model cannot vary them and never sees them, when the goal is safety without per-action approval latency.
- Frame the AI signal in reviewer guidelines as a preliminary alert requiring independent evidence — this alone moved rejection rates 21% at Duolingo with no model or UI change.
- Log the human's subsequent manual edit, not just the accept/reject click, so the approval produces an honest training label.
- Run the canary, test, or verifier agent before the artifact reaches a human, and put the verifier on a different model than the author.
- Track human-override rate on AI verdicts as a monitored metric and set a threshold that triggers investigation.
- Surface one high-ROI finding at a time rather than opening a large batch of PRs a human must triage.
- Give the user an always-available stop control and settings to disable plan approval on repeated low-risk flows.
- Show a rough time and cost estimate alongside the action being approved.

**Avoid:**

- Treating a natural-language instruction like "ask for confirmation" as a human-in-the-loop control — the agent can issue and satisfy that confirmation itself.
- Shipping a gate that only logs a warning; if it cannot halt the artifact, it is a suggestion.
- Presenting one giant diff or a stream of per-file yes/no prompts — both reduce the reviewer to a rubber stamp and yield low-information accept/reject data.
- Conflating two questions in one CTA (e.g. "was the model's perception correct" and "should we penalize this user"), which produces false labels that make the model spuriously more confident.
- Assuming reviewer skill protects against automation bias — reviewers calibrated above 90% still upheld half of fabricated flags.
- Relying on approval as the governance mechanism for background or cloud agents, where no human is sitting there to ask.
- Letting the agent push fixes directly to production even when tests pass; modifying working production code warrants a human-approved review.
- Making the human the throughput ceiling of the system, or attempting exhaustive human verification at agent volume.
- Requiring non-engineer users to read agent-written code to approve its work instead of emitting structured review artifacts.
- Giving an agent a long-lived kitchen-sink credential and hoping supervision catches misuse — it will use every permission it has to finish the task.

## Notable Outliers

- A human's approval can itself be rejected: policy checked the approver's role and blocked the action even though the human had already clicked allow. ([It's 10pm. Do You Know Where Your Agents Are?](../talks/its-10pm-do-you-know-where-your-agents-are.md), [14:54](https://www.youtube.com/watch?v=I3znWC3MEXM&t=894s))
- Expert reviewers scoring above 90% on accuracy calibration accepted 50% of deliberately fabricated AI flags — a coin-flip rate indicating automation bias, not skill deficiency. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s))
- In a nine-step bug-fix-to-stage pipeline, human contact is only needed at step 1 and step 9; the agent does the intermediate steps better than a human would. ([Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md), [5:54](https://www.youtube.com/watch?v=z0sh8HyTrDo&t=354s))
- 'Done' should be a structured object with artifact, scope, rubric, evidence, verifier, approver, residual risk, and next action — not a boolean, because mergeable, deployable, and announceable are different claims. ([What Does Done Even Mean? Agents and Paperclip's Liveness Model](../talks/what-does-done-even-mean-agents-and-paperclips-liveness-model.md), [4:49](https://www.youtube.com/watch?v=7P0elyLIxXo&t=289s))
- Per-action approval interrupts are safe but very slow; locking the argument via partial function application achieves the same safety with no human input, and the model never learns the argument exists. ([What if the harness mattered more than the model?](../talks/what-if-the-harness-mattered-more-than-the-model.md), [16:54](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1014s))
- Autonomous agent automation requires crossing an 80-90% trust threshold, whereas an 80% success rate is perfectly acceptable for interactive IDE use because the human is already in context. ([From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [20:49](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=1249s))

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

