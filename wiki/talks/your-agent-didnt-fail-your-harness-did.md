---
title: "Your Agent Didn't Fail. Your Harness Did."
type: "talk"
slug: "your-agent-didnt-fail-your-harness-did"
track: "Claws & Personal Agents"
org: "OpenAI"
day: "Day 2 — Session Day 1"
room: "Track 1"
video_id: "BInpv7lGp1o"
duration_sec: 1105
word_count: 2514
speakers: ["Vinoth Govindarajan"]
---

# Your Agent Didn't Fail. Your Harness Did.

*Program title: Your Agent Didn’t Fail. Your Harness Did.*

**Speakers:** [Vinoth Govindarajan](../speakers/vinoth-govindarajan.md)

**Org:** OpenAI

**Track:** Claws & Personal Agents &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 1 &nbsp;|&nbsp; **Duration:** 18m 25s

[Watch on YouTube](https://www.youtube.com/watch?v=BInpv7lGp1o)

## Summary

Vinoth Govindarajan argues that most production agent failures are not model failures but harness failures — breakdowns in the surrounding system that owns state, orders writes, bounds work, checks authority, and records evidence. Using publicly visible OpenClaw issues as case studies, he walks through five recurring failure shapes: a state hole where a message is delivered but never durably recorded, overlapping writers in a load-modify-save race, dangling tool calls that leave a run waiting forever, approval drift where an expired authorization outlives the action it authorized, and missing edge proof where a tool reports success but nothing renders for the user. His organizing contract is 'a model proposes, the harness commits, and the receipt proves it,' with the receipt — not the transcript — as the artifact that survives the turn. He closes with a concrete five-question audit to run against one real production trace. Worth watching if you build agent infrastructure and want distributed-systems vocabulary (ownership, ordered commit, idempotency, deadlines) mapped onto agent architecture; less useful if you're looking for model or prompting techniques.

## Key Points

- The dangerous failure mode is silent success: the user-visible edge looks healthy while the durable record has a hole, so the next turn is coherent over a broken history — unlike a crash, which at least gives you a boundary and a last known good point.
- Agent runtimes are stateless; the harness rebuilds the working set (transcript, session state, memory, policy, tool definitions) every turn, so the model only ever sees what the harness supplies and coherence never proves the working set was complete.
- Every fact the agent may use later needs a named owner — the system of record that can replay it — and storage location is not ownership: a calendar event belongs to the calendar system, a conversation turn to the session transcript.
- The concurrency invariant is not 'no concurrency' — fan-out sub-agents, parallel reads, and many simultaneous sessions are fine — but one ordered commit path per mutable state boundary, enforced conservatively at commit time rather than across the whole system.
- Ordering is a product feature, because users perceive ordering bugs as personality: a lost correction feels forgetful, a stuck lane feels dead, and completion before delivery feels confused.
- Silence is not a terminal state: every external boundary needs an ending (success, failure, timeout, cancel, or max attempts), plus deadlines, watchdogs, tool timeouts, and recovery commands that don't queue behind the stuck work they're meant to fix.
- Approval must be a scoped execution state bound to a specific actor, session, run, tool, arguments, and lifetime — not a vague memory that a human clicked yes — and expiration must terminate rather than loop.
- A receipt differs from a transcript and from a tool result: it preserves the whole chain (model proposed, policy allowed, execution attempted, user-visible edge confirmed), because internal success is not external proof.
- The recommended action is a five-question audit on one real production trace: what woke it up, what state did it inherit, which authority did it use, what executed, and what evidence survived.

## Notable Quotes

> "most of the agent failures are not model failures. Those are harness failures."
>
> — [0:01](https://www.youtube.com/watch?v=BInpv7lGp1o&t=1s) &middot; *the thesis of the talk in one line*

> "The crash is annoying, but at at least it gives you a boundary. You know some you know something stopped. You usually see an error. You can often start from last known good point. Silent success gives you a lie."
>
> — [0:56](https://www.youtube.com/watch?v=BInpv7lGp1o&t=56s) &middot; *names the specific reason silent failure is worse than a crash*

> "A model proposes the harness commits and the receipts proves it."
>
> — [2:40](https://www.youtube.com/watch?v=BInpv7lGp1o&t=160s) &middot; *the production contract the whole talk hangs on*

> "Own the state, order the mutation and prove the action. A fact needs only one owner and one replay path."
>
> — [3:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=203s) &middot; *the three-item takeaway he repeats at open and close*

> "A transcript tells you what the agent said. A receipt tells you what the system allowed, attempted, executed and what the user visible edge confirmed."
>
> — [3:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=203s) &middot; *the transcript/receipt distinction that drives the audit*

> "The model gives you capability, but the harness gives you control. A powerful engine with no brakes is not autonomy. It is a liability with good acceleration."
>
> — [3:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=203s) &middot; *the car analogy at its sharpest*

> "The model only sees what the harness supplies. If one input is missing or stale, the answer may still sound coherent. Coherence does not proves the working set was complete."
>
> — [5:03](https://www.youtube.com/watch?v=BInpv7lGp1o&t=303s) &middot; *explains why fluent output is not evidence of correct context assembly*

> "So these failures are familiar agents makes them easier to trigger and harder to explain."
>
> — [6:00](https://www.youtube.com/watch?v=BInpv7lGp1o&t=360s) &middot; *positions agent reliability as old distributed-systems problems under new pressure*

> "A successful send proves transcript. It does not prove the future context."
>
> — [6:53](https://www.youtube.com/watch?v=BInpv7lGp1o&t=413s) &middot; *compresses the opening incident into a checkable claim*

> "Storage tells you where the bytes live. Ownership tells you who can reconstruct the reality."
>
> — [6:53](https://www.youtube.com/watch?v=BInpv7lGp1o&t=413s) &middot; *defines ownership as replayability rather than persistence*

> "Two correct rights can still produce one wrong outcome. and last writer wins is not a consistency model."
>
> — [7:39](https://www.youtube.com/watch?v=BInpv7lGp1o&t=459s) &middot; *takes a clear side against the default concurrency behavior of agent state stores*

> "The invariant is not no concurrency. That would be too slow and it would miss the point."
>
> — [8:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=503s) &middot; *names the tradeoff so the ordering rule isn't read as serialize-everything*

> "The rule is narrower and simple. One ordered commit path for one mutable state boundary."
>
> — [8:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=503s) &middot; *the precise form of the concurrency prescription*

> "Ordering is a product feature because users experience ordering books as personalities."
>
> — [9:15](https://www.youtube.com/watch?v=BInpv7lGp1o&t=555s) &middot; *reframes an infrastructure concern as a UX concern*

> "Every external boundary needs an ending. Success, failure, timeout, cancel, or max attempts."
>
> — [10:58](https://www.youtube.com/watch?v=BInpv7lGp1o&t=658s) &middot; *the lifecycle rule stated as a checklist*

> "Capability is not execution. The model can request an action. Requestability is not authority."
>
> — [10:58](https://www.youtube.com/watch?v=BInpv7lGp1o&t=658s) &middot; *the authority boundary in three clauses*

> "The model can reason about the boundary but it should not be the boundary. The model can request but the still the system decides."
>
> — [12:34](https://www.youtube.com/watch?v=BInpv7lGp1o&t=754s) &middot; *an explicit stance against model-enforced policy that others may dispute*

> "The tool proved that the internal path accepted the request. It does not prove the user saw the result."
>
> — [13:20](https://www.youtube.com/watch?v=BInpv7lGp1o&t=800s) &middot; *isolates the missing-edge-proof failure precisely*

> "Internal success is not external proof. Proof is a chain, not a claim."
>
> — [13:20](https://www.youtube.com/watch?v=BInpv7lGp1o&t=800s) &middot; *the receipt argument in its most quotable form*

> "Delivery survived while the state did not. That gap is the harness failure."
>
> — [16:33](https://www.youtube.com/watch?v=BInpv7lGp1o&t=993s) &middot; *closes the loop on the opening incident using the audit*

> "A better model helps inside the turn. Ownership, ordering, life cycle, authority and proof keep the system sane across turns."
>
> — [16:33](https://www.youtube.com/watch?v=BInpv7lGp1o&t=993s) &middot; *draws the line between what model quality can and cannot fix*

> "Do not only ask whether the model can reason. Ask whether the system can own the state, order the mutation, bound the work, constraint authority, and preserve evidence."
>
> — [17:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=1043s) &middot; *the closing reframe of the evaluation question*

## Positions

- Most production agent failures are harness failures, not model failures. ([0:01](https://www.youtube.com/watch?v=BInpv7lGp1o&t=1s), confidence: stated)
- Silent success is a worse failure mode than a crash, because a crash gives you an error boundary and a last known good point. ([0:56](https://www.youtube.com/watch?v=BInpv7lGp1o&t=56s), confidence: stated)
- The model should not be the production boundary; the harness owns state transitions, authority checks, ordered commits, and receipts. ([2:40](https://www.youtube.com/watch?v=BInpv7lGp1o&t=160s), confidence: stated)
- A transcript is not proof of what happened; only a receipt that records allowance, attempt, execution, and edge confirmation is. ([3:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=203s), confidence: stated)
- Every agent architecture — personal agents, coding agents like Codex, Cursor, OpenCode, Claude Code — shares the same underlying blueprint of event, session key, throttle, tools, audit. ([4:14](https://www.youtube.com/watch?v=BInpv7lGp1o&t=254s), confidence: stated)
- A fact is not reliably remembered unless a named owner can replay it. ([7:39](https://www.youtube.com/watch?v=BInpv7lGp1o&t=459s), confidence: stated)
- Last-writer-wins is not an acceptable consistency model for agent state. ([7:39](https://www.youtube.com/watch?v=BInpv7lGp1o&t=459s), confidence: stated)
- Concurrency should be restricted only at commit time for a single mutable state boundary, not globally — parallel reads, sub-agent fan-out, and concurrent sessions are fine. ([8:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=503s), confidence: stated)
- Ordering bugs are perceived by users as agent personality defects (forgetful, dead, confused), making ordering a product concern rather than a purely internal one. ([9:15](https://www.youtube.com/watch?v=BInpv7lGp1o&t=555s), confidence: stated)
- Silence is not a terminal state; every external boundary must resolve to success, failure, timeout, cancel, or max attempts. ([10:06](https://www.youtube.com/watch?v=BInpv7lGp1o&t=606s), confidence: stated)
- Recovery commands must be able to run without queueing behind the stuck work they are trying to fix. ([10:06](https://www.youtube.com/watch?v=BInpv7lGp1o&t=606s), confidence: stated)
- Approval must be a scoped execution state bound to actor, session, run, tool, arguments, and lifetime, and expiration must terminate rather than loop. ([11:47](https://www.youtube.com/watch?v=BInpv7lGp1o&t=707s), confidence: stated)
- A tool reporting success does not prove the user saw the result; internal success and external proof are different things. ([13:20](https://www.youtube.com/watch?v=BInpv7lGp1o&t=800s), confidence: stated)
- Teams should audit one real production trace against five questions rather than attempting to instrument every agent system at once. ([14:04](https://www.youtube.com/watch?v=BInpv7lGp1o&t=844s), confidence: stated)
- The OpenAI Agents SDK already implements these harness properties, so teams can build on it rather than reimplementing them. ([17:23](https://www.youtube.com/watch?v=BInpv7lGp1o&t=1043s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [audit trails](../concepts/audit-trails.md)
- [context engineering](../concepts/context-engineering.md)
- [durable execution](../concepts/durable-execution.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [parallel agent execution](../concepts/parallel-agent-execution.md)
- [semantic layer](../concepts/semantic-layer.md)

