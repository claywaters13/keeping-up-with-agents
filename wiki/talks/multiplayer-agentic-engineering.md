---
title: "Multiplayer agentic engineering"
type: "talk"
slug: "multiplayer-agentic-engineering"
track: "Agentic Engineering"
org: "Superconductor"
day: "Day 4 — Session Day 3"
room: "Track 8"
video_id: "OL7kfezynJM"
duration_sec: 1124
word_count: 3905
speakers: ["Arjun Singh"]
---

# Multiplayer agentic engineering

*Program title: Multiplayer agentic engineering: enabling your whole team and your best agents to work together*

**Speakers:** [Arjun Singh](../speakers/arjun-singh.md)

**Org:** Superconductor

**Track:** Agentic Engineering &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 18m 44s

[Watch on YouTube](https://www.youtube.com/watch?v=OL7kfezynJM)

## Summary

Arjun Singh argues that the interesting problem in agentic engineering is no longer the agent but the team around it: how multiple people — including non-engineers — share, steer, and review agent work. Drawing on his team's year of aggressively integrating coding agents at Superconductor, he lays out six lessons: stay model- and harness-agnostic, make every human interface (Slack, GitHub, desktop, mobile) a shared handle on the same agent session, make agent work visible and collaborative, turn external signals like meetings and bug reports into code automatically, run everything in isolated cloud sandboxes rather than on laptops, and benchmark agents on your own codebase rather than trusting public benchmarks. He backs the last point with internal numbers — 1.5 billion tokens in a month, 3,300 Claude Code runs at ~$10k/day of token value, Codex at 4x the sessions for less money — and with quality-vs-cost and quality-vs-time charts on their Ruby on Rails codebase. Worth watching if you're designing team-level agent workflows or wondering whether SWE-bench-style results transfer to your stack; less useful if you want model internals or prompting technique.

## Key Points

- Most agentic-engineering discourse centers the agent; the harder and less-discussed problem is how a whole team of humans collaborates around agents.
- Being model- and harness-agnostic is a strategic hedge: the best option changes weekly, options can disappear, open-weight models like GLM 5.2 are now good and much cheaper, and token vendors' incentives are not aligned with yours.
- Exposing agents via a Slack bot is an improvement over laptop-bound agents but insufficient — the goal is the exact same agent session reachable from Slack, the app, GitHub, and mobile, carrying identical context.
- Making sessions visible (who triggered, who was notified, who reviewed) matters most when non-technical teammates initiate work, and reviewers can interrogate the agent directly instead of waiting on the original author.
- A meeting bot that joins Google Meet/Zoom/Teams can turn conversations into linked or newly created tickets and working PRs with no manual handoff — Singh reports dozens of prototypes and a few shippable PRs per customer or team call.
- Running agents in isolated cloud sandboxes solves 'lid anxiety' but the stronger justification is least-privilege: laptops hold credentials agents shouldn't touch, and a configurable network sandbox prevents exfiltration of code and secrets.
- Sandboxed cloud environments are also what lets support and growth people trigger real, merged code changes without any local dev environment.
- Public benchmarks (SWE-bench, Terminal-Bench) may not transfer — SWE-bench is Python while their codebase is Ruby on Rails — so benchmark candidate agents against PRs from your own repo to get quality-vs-cost-vs-time data, and eventually route tasks automatically on that basis.

## Notable Quotes

> "the incentives of the people selling you tokens aren't really aligned with yours"
>
> — [2:14](https://www.youtube.com/watch?v=OL7kfezynJM&t=134s) &middot; *The sharpest statement of why he treats model-agnosticism as a business posture, not a technical preference.*

> "The best model and harness can change weekly. It could change cuz a new one comes out."
>
> — [2:14](https://www.youtube.com/watch?v=OL7kfezynJM&t=134s) &middot; *States the volatility premise the entire agnosticism argument rests on.*

> "The other thing is that open weight models are actually pretty good now. We've been really happy with GLM 5.2. They're much cheaper."
>
> — [2:14](https://www.youtube.com/watch?v=OL7kfezynJM&t=134s) &middot; *A concrete, checkable endorsement of an open-weight model in production use.*

> "So, the next one is to turn every human interface into an agent and human interface."
>
> — [2:55](https://www.youtube.com/watch?v=OL7kfezynJM&t=175s) &middot; *The talk's central design principle, stated in one line.*

> "So, what we really wanted was to be able to work with the same session from every relevant interface."
>
> — [3:28](https://www.youtube.com/watch?v=OL7kfezynJM&t=208s) &middot; *Names the specific technical requirement — session identity, not just multiple bots.*

> "And the second lesson builds on top of that, which is to make the agent work visible and collaborative across the team."
>
> — [4:00](https://www.youtube.com/watch?v=OL7kfezynJM&t=240s) &middot; *Lesson statement, useful as an anchor for cross-talk comparison on agent observability.*

> "to turn every external signal into code that your team can quickly evaluate"
>
> — [5:28](https://www.youtube.com/watch?v=OL7kfezynJM&t=328s) &middot; *Compact framing of signal-to-PR automation, the most differentiated claim in the talk.*

> "we almost always have dozens of new ideas that are prototyped, but more importantly, at least a few shippable PRs with a very minimal intervention. So we talk, stuff comes out, we look at it, we ship it."
>
> — [8:12](https://www.youtube.com/watch?v=OL7kfezynJM&t=492s) &middot; *Quantified outcome claim for the meeting-bot workflow.*

> "So the first one is to eliminate what some people are calling lid anxiety. You want to be able to close your laptop."
>
> — [9:02](https://www.youtube.com/watch?v=OL7kfezynJM&t=542s) &middot; *Coins the memorable term for the ergonomic motivation behind cloud sandboxes.*

> "I think you should only give your access give your agents access to only what they need."
>
> — [10:03](https://www.youtube.com/watch?v=OL7kfezynJM&t=603s) &middot; *The least-privilege position he calls the most important reason for sandboxing.*

> "You're either approving a bunch of stuff or you're hoping that your auto approval flow or your YOLO mode or whatever is configured properly and your sandbox is configured properly and doesn't read a bunch of stuff on your laptop that it shouldn't have."
>
> — [10:36](https://www.youtube.com/watch?v=OL7kfezynJM&t=636s) &middot; *Frames local agent security as a forced choice between toil and hope — a clear tradeoff statement.*

> "it finds a token on your laptop that it can use and it thinks it's working with staging, but actually it's production and now it just deleted everything."
>
> — [11:05](https://www.youtube.com/watch?v=OL7kfezynJM&t=665s) &middot; *The concrete failure mode motivating environment isolation.*

> "It's also make sure they can't exfiltrate your code or your projects or your secrets or your content to somewhere they shouldn't be able to."
>
> — [11:05](https://www.youtube.com/watch?v=OL7kfezynJM&t=665s) &middot; *Extends the security argument from credentials to egress control.*

> "the last thing I'll mention about that is that this is the key for allowing your non-technical team members to trigger real work."
>
> — [11:49](https://www.youtube.com/watch?v=OL7kfezynJM&t=709s) &middot; *Links the infrastructure choice to the organizational payoff, the talk's thesis in miniature.*

> "And the last lesson is to benchmark agents on your code base."
>
> — [13:03](https://www.youtube.com/watch?v=OL7kfezynJM&t=783s) &middot; *The lesson most directly at odds with relying on public leaderboards.*

> "Like swe bench is all in Python, we're Ruby on Rails. It is not the case that the benchmarks are identical for them."
>
> — [13:37](https://www.youtube.com/watch?v=OL7kfezynJM&t=817s) &middot; *Names the specific reason public benchmarks may not transfer to a given team.*

> "you can see that the Anthropic agents have just been consistently getting better, but not really any faster. The Codex agents and cursor are actually pretty fast and quite good."
>
> — [14:06](https://www.youtube.com/watch?v=OL7kfezynJM&t=846s) &middot; *A rare public head-to-head read on agent harnesses from real internal data.*

> "By cost, the Anthropic stuff is clearly just so much more expensive for us."
>
> — [14:06](https://www.youtube.com/watch?v=OL7kfezynJM&t=846s) &middot; *The cost finding that changed their default harness.*

> "essentially 100% like 99.9% of our pull requests are like heavily agent generated. We know that quality and reliability and security are really important, so we still have humans look at everything."
>
> — [15:47](https://www.youtube.com/watch?v=OL7kfezynJM&t=947s) &middot; *Pairs an extreme adoption number with an explicit human-review guardrail.*

> "we had 3,300 Claude code runs that cost $10,000 in tokens daily. We have plans, so we didn't spend $10,000 on it. And Codex had four times as many sessions, and it was cheaper overall."
>
> — [16:20](https://www.youtube.com/watch?v=OL7kfezynJM&t=980s) &middot; *The hardest numbers in the talk, including the honest caveat about subscription pricing.*

> "And lastly, find a way to benchmark and become model agnostic so you're not tied to anybody and you can just constantly stay at that right part on the frontier of cost, speed, quality."
>
> — [17:41](https://www.youtube.com/watch?v=OL7kfezynJM&t=1061s) &middot; *Closing recommendation that ties benchmarking to the agnosticism thesis.*

## Positions

- Teams should stay model- and harness-agnostic because the best option changes weekly and vendors' token-selling incentives diverge from customers' interests. ([1:42](https://www.youtube.com/watch?v=OL7kfezynJM&t=102s), confidence: stated)
- Open-weight models such as GLM 5.2 are now good enough and substantially cheaper for production coding work. ([2:14](https://www.youtube.com/watch?v=OL7kfezynJM&t=134s), confidence: stated)
- A Slack bot alone is insufficient — it moves the agent from trapped on a laptop to trapped in Slack. ([2:55](https://www.youtube.com/watch?v=OL7kfezynJM&t=175s), confidence: stated)
- The same agent session, with identical context, should be reachable from Slack, the desktop/mobile app, and GitHub. ([3:28](https://www.youtube.com/watch?v=OL7kfezynJM&t=208s), confidence: stated)
- Reviewers can get answers faster by asking the agent in-thread than by waiting for the human who started the session to respond on GitHub. ([4:30](https://www.youtube.com/watch?v=OL7kfezynJM&t=270s), confidence: stated)
- MCP connections alone don't solve the coordination problem, because a human still has to tell the agent which email or ticket to act on. ([6:03](https://www.youtube.com/watch?v=OL7kfezynJM&t=363s), confidence: stated)
- Meetings and customer calls can be automatically converted into tickets and working PRs with no manual intervention. ([7:41](https://www.youtube.com/watch?v=OL7kfezynJM&t=461s), confidence: stated)
- Least-privilege access is a more important reason to move agents to isolated cloud environments than eliminating 'lid anxiety'. ([10:03](https://www.youtube.com/watch?v=OL7kfezynJM&t=603s), confidence: stated)
- Developer laptops contain credentials and data that agents should not have access to, and sandbox/auto-approval configurations are not reliably safe. ([10:03](https://www.youtube.com/watch?v=OL7kfezynJM&t=603s), confidence: stated)
- Sandboxed cloud environments are the prerequisite for non-technical teammates triggering real, merged code changes. ([11:49](https://www.youtube.com/watch?v=OL7kfezynJM&t=709s), confidence: stated)
- Getting a project working in a sandbox environment used to be very painful but is now tractable because agents like Claude Code or Codex can do the setup for you. ([12:23](https://www.youtube.com/watch?v=OL7kfezynJM&t=743s), confidence: stated)
- Public benchmarks like SWE-bench and Terminal-Bench may not predict performance on your codebase; results can differ substantially across languages and stacks. ([13:37](https://www.youtube.com/watch?v=OL7kfezynJM&t=817s), confidence: stated)
- On their Ruby on Rails codebase, Anthropic agents improved in quality but not speed, while Codex and Cursor were faster and cheaper. ([14:06](https://www.youtube.com/watch?v=OL7kfezynJM&t=846s), confidence: stated)
- Their team used ~1.5 billion tokens in the past month, with 3,300 Claude Code runs valued at $10,000/day in tokens, while Codex had 4x the sessions at lower total cost. ([16:20](https://www.youtube.com/watch?v=OL7kfezynJM&t=980s), confidence: stated)
- Roughly 99.9% of their pull requests are heavily agent-generated, and every one is still human reviewed. ([15:47](https://www.youtube.com/watch?v=OL7kfezynJM&t=947s), confidence: stated)
- Third-party task routing cannot know what works best for your codebase; routing decisions should be driven by benchmarks run on your own repo. ([16:20](https://www.youtube.com/watch?v=OL7kfezynJM&t=980s), confidence: stated)
- Continuous internal benchmarking removes the FOMO and wasted evaluation time of manually trying each new model release. ([15:17](https://www.youtube.com/watch?v=OL7kfezynJM&t=917s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [background agents](../concepts/background-agents.md)
- [coding agent benchmarking](../concepts/coding-agent-benchmarking.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [model portability](../concepts/model-portability.md)
- [model routing](../concepts/model-routing.md)
- [session management](../concepts/session-management.md)

