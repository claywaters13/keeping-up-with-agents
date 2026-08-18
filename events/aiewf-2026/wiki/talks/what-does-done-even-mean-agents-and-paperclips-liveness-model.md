---
title: "What Does Done Even Mean? Agents and Paperclip's Liveness Model"
type: "talk"
slug: "what-does-done-even-mean-agents-and-paperclips-liveness-model"
org: "Paperclip"
video_id: "7P0elyLIxXo"
duration_sec: 433
word_count: 1325
speakers: ["Dotta"]
---

# What Does Done Even Mean? Agents and Paperclip's Liveness Model

**Speakers:** [Dotta](../speakers/dotta.md)

**Org:** Paperclip

**Duration:** 7m 13s

[Watch on YouTube](https://www.youtube.com/watch?v=7P0elyLIxXo)

## Summary

Dotta, creator of Paperclip, argues that 'done' is the wrong abstraction for agentic systems: agents now produce more code and documentation than humans can verify, so collapsing completion into a single green checkmark creates a new failure mode. He unpacks 'done' as a bundle of distinct claims — artifact, scope, rubric, evidence, verifier, approver, residual risk, and next action — and describes a ladder of completion levels from producer claim through real-world survival. The core design tension he names is liveness (work keeps moving) versus verification (work is correct): all liveness gives you AI slop, all human review gives you an unclearable queue and verification theater. Paperclip's answer is a control plane with explicit state transitions, first-class enforced blockers, explicit reviewers/approvers, audit-trailed human approval, and harness-agnostic 'watchdog' agents that push toward a goal. The talk closes with a concrete checklist, most notably separating the verifier from the author by using a different model.

## Key Points

- The new failure mode in agentic engineering is not bad code but volume: agents can create more work than humans have time to verify, so exhaustive human verification degrades into verification theater.
- Saying a task is 'done' bundles several separable claims — an artifact was produced, evidence exists, a rubric to check against exists, the owner of the next step is known, and the next step itself is known.
- Completion is a ladder, not a boolean: producer claims complete, a reviewer finds no obvious issues, evidence meets a standard, an authorized person approves, someone stands behind the decision, and ideally the outcome survives real-world conditions.
- Liveness (work continuing with no blockers) and verification (human-confirmed correctness) are in direct tension — full liveness yields AI slop, full peer review stalls tasks dead in their tracks.
- A naive for-loop over a task manager falls apart once you add dependency trees, blockers, multiple agents, and idempotent checkouts with locks; you need a control plane instead.
- Three invariants for an agentic control plane: productive work continues, only real blockers stop work, and infinite loops are bounded.
- Paperclip's mechanisms include explicit state transitions, control-plane-enforced first-class blockers, audit-trailed interactive human approval, explicit reviewers and approvers per task, and watchdog agents that drive work until a goal is met — with the watchdog deliberately harness-agnostic across Claude Code, Codex, and others.
- Practical checklist: define done per task, separate verifier from author (often a different model — code with Claude, verify with Codex), give agents real tooling (browsers, screenshots, hooks) to produce evidence rather than just asserting completion, and establish a clear chain of custody for handoffs.

## Notable Quotes

> "An agent opens a pull request. It passes the tests. It updates the documentation. It closes the issue and comments, "Looks done to me." But is it actually done?"
>
> — [0:00](https://www.youtube.com/watch?v=7P0elyLIxXo&t=0s) &middot; *The framing scenario the whole talk hangs on.*

> "Is it done enough to merge? Is it done enough to deploy? Is it done enough to announce to your customers? These are fundamentally different operational claims, and most agent systems just flatten it to a single green check mark."
>
> — [0:00](https://www.youtube.com/watch?v=7P0elyLIxXo&t=0s) &middot; *States the central critique of existing agent systems.*

> "Programming is solved, and agents can now produce more code and documentation faster than any human can ever verify."
>
> — [0:00](https://www.youtube.com/watch?v=7P0elyLIxXo&t=0s) &middot; *Deliberately provocative premise that others would contest.*

> "And this actually gives us a new failure mode, is that agents can actually create more work than humans have time to verify."
>
> — [0:37](https://www.youtube.com/watch?v=7P0elyLIxXo&t=37s) &middot; *Names the specific failure mode the talk addresses.*

> "Saying that something is done is actually a bundle of claims."
>
> — [0:37](https://www.youtube.com/watch?v=7P0elyLIxXo&t=37s) &middot; *The talk's thesis in one line.*

> "Because exhaustive human verification fails at high volume. You might be able to verify a few tasks per day, but essentially, if you have humans verifying all the tasks and they have to sign off on it, you eventually what you just get is a form of verification theater."
>
> — [1:11](https://www.youtube.com/watch?v=7P0elyLIxXo&t=71s) &middot; *Coins 'verification theater' and gives the scale argument against human sign-off.*

> "You need a control plane that actually has the execution of the tasks being tied to specific contracts and constraints about what the system will do and what agents it will hand off your next task to."
>
> — [2:03](https://www.youtube.com/watch?v=7P0elyLIxXo&t=123s) &middot; *The architectural prescription.*

> "When a task has been reviewed by a human, you get the assurance that it's correct. But having a human verify it means that the task is dead in its tracks."
>
> — [2:03](https://www.youtube.com/watch?v=7P0elyLIxXo&t=123s) &middot; *Crisp statement of the core tradeoff.*

> "If you have tasks that are completely alive with no approvals, then what you get is this classic AI slop because you're producing a lot of things with kind of no quality control and it's worse than creating nothing after a long period of time."
>
> — [2:45](https://www.youtube.com/watch?v=7P0elyLIxXo&t=165s) &middot; *Quantifies the downside of pure liveness as worse than doing nothing.*

> "These agents will be creating far more than you can ever actually review, and so we have to find a way to tease apart the bundle of claims that are involved in saying a task is done."
>
> — [2:45](https://www.youtube.com/watch?v=7P0elyLIxXo&t=165s) &middot; *Links the volume problem to the decomposition solution.*

> "You might think that you can easily just write a for loop over your task manager and have your agents work, but quickly you'll find that falls apart."
>
> — [3:24](https://www.youtube.com/watch?v=7P0elyLIxXo&t=204s) &middot; *Preempts the obvious naive implementation.*

> "You want to ensure that productive work continues. You want to make sure that only real blockers stop work."
>
> — [3:24](https://www.youtube.com/watch?v=7P0elyLIxXo&t=204s) &middot; *Two of the three stated control-plane invariants.*

> "We have first-class blockers between tasks, and the control plane enforces those blockers."
>
> — [4:07](https://www.youtube.com/watch?v=7P0elyLIxXo&t=247s) &middot; *Concrete mechanism rather than principle.*

> "When you have a watchdog, it's another agent, um, who is given a goal, and it enforces that all of your agents continue to work until that goal has been achieved."
>
> — [4:49](https://www.youtube.com/watch?v=7P0elyLIxXo&t=289s) &middot; *Defines the watchdog primitive.*

> "The important thing here is that the watchdog within Paperclip is harness agnostic."
>
> — [4:49](https://www.youtube.com/watch?v=7P0elyLIxXo&t=289s) &middot; *A deliberate product positioning choice about tool lock-in.*

> "So, one of the best pieces of advice we have is that you stop treating done as a Boolean and treat it more like an object."
>
> — [4:49](https://www.youtube.com/watch?v=7P0elyLIxXo&t=289s) &middot; *The single most portable takeaway from the talk.*

> "Humans automatically paper over these details, but when we're building agentic systems, it's important that your agents can distinguish between the different pieces of what they're claiming when they say something is done."
>
> — [5:25](https://www.youtube.com/watch?v=7P0elyLIxXo&t=325s) &middot; *Explains why implicit human norms fail when encoded into agents.*

> "You definitely want to separate the verifier from the author. Often, this means you're using a different model. So, if you're coding using Claude, have Codex verify."
>
> — [5:59](https://www.youtube.com/watch?v=7P0elyLIxXo&t=359s) &middot; *The most actionable and specific recommendation in the talk.*

> "You want to ask your agents to provide evidence. Don't just ask them to say, "Is this done?" But, give them the tools they need to verify that the work is done."
>
> — [5:59](https://www.youtube.com/watch?v=7P0elyLIxXo&t=359s) &middot; *Shifts the burden from self-report to instrumented proof.*

> "Make sure you have a clear chain of custody, that every agent knows that as soon as they're done, who they're supposed to give the work to next."
>
> — [6:36](https://www.youtube.com/watch?v=7P0elyLIxXo&t=396s) &middot; *Names handoff ownership as a first-class requirement.*

## Positions

- Programming is solved, and agents can produce code and documentation faster than any human can verify it. ([0:00](https://www.youtube.com/watch?v=7P0elyLIxXo&t=0s), confidence: stated)
- Most agent systems wrongly flatten distinct operational claims (mergeable, deployable, announceable) into a single green checkmark. ([0:00](https://www.youtube.com/watch?v=7P0elyLIxXo&t=0s), confidence: stated)
- Exhaustive human verification does not scale and degenerates into verification theater at high task volume. ([1:11](https://www.youtube.com/watch?v=7P0elyLIxXo&t=71s), confidence: stated)
- Fully live agent output with no approvals produces AI slop that is worse than producing nothing at all. ([2:45](https://www.youtube.com/watch?v=7P0elyLIxXo&t=165s), confidence: stated)
- Human review guarantees correctness but stops the task dead, so liveness and verification must be traded off deliberately. ([2:03](https://www.youtube.com/watch?v=7P0elyLIxXo&t=123s), confidence: stated)
- A simple for-loop over a task manager is insufficient once dependency trees, blockers, multiple agents, and idempotent checkouts are involved. ([3:24](https://www.youtube.com/watch?v=7P0elyLIxXo&t=204s), confidence: stated)
- Any agentic control plane must guarantee three invariants: productive work continues, only real blockers stop work, and infinite loops are bounded. ([3:24](https://www.youtube.com/watch?v=7P0elyLIxXo&t=204s), confidence: stated)
- 'Done' should be modeled as a structured object with fields (artifact, scope, rubric, evidence, verifier, approver, residual risk, next action) rather than a boolean. ([4:49](https://www.youtube.com/watch?v=7P0elyLIxXo&t=289s), confidence: stated)
- The verifying agent should be a different model from the authoring agent — e.g. code with Claude, verify with Codex. ([5:59](https://www.youtube.com/watch?v=7P0elyLIxXo&t=359s), confidence: stated)
- Verification tooling should be built for agents (browser harnesses, screenshots, custom hooks) rather than relying on agents self-reporting completion. ([5:59](https://www.youtube.com/watch?v=7P0elyLIxXo&t=359s), confidence: stated)
- Agent orchestration primitives like watchdogs should be harness-agnostic rather than tied to one coding agent. ([4:49](https://www.youtube.com/watch?v=7P0elyLIxXo&t=289s), confidence: implied)
- Following this done-definition checklist can yield roughly 100x more work completed. ([5:25](https://www.youtube.com/watch?v=7P0elyLIxXo&t=325s), confidence: stated)

## Concepts

- [adversarial agent supervision](../concepts/adversarial-agent-supervision.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [audit trails](../concepts/audit-trails.md)
- [citation and grounding](../concepts/citation-and-grounding.md)
- [cross-model verification](../concepts/cross-model-verification.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [reward hacking](../concepts/reward-hacking.md)
- [runtime policy enforcement](../concepts/runtime-policy-enforcement.md)
- [task decomposition](../concepts/task-decomposition.md)

