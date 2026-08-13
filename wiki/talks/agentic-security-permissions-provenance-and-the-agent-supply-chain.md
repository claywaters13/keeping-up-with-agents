---
title: "Agentic Security: Permissions, Provenance, and the Agent Supply Chain"
type: "talk"
slug: "agentic-security-permissions-provenance-and-the-agent-supply-chain"
track: "Security"
org: "Gas Town"
day: "Day 2 — Session Day 1"
room: "Track 5"
video_id: "yWS0udrIOc8"
duration_sec: 1352
word_count: 3782
speakers: ["Steve Yegge"]
---

# Agentic Security: Permissions, Provenance, and the Agent Supply Chain

**Speakers:** [Steve Yegge](../speakers/steve-yegge.md)

**Org:** Gas Town

**Track:** Security &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 22m 32s

[Watch on YouTube](https://www.youtube.com/watch?v=yWS0udrIOc8)

## Summary

Steve Yegge (speaking on behalf of Snyk, though unpaid) delivers a deliberately alarmist talk whose 'real title' is 'Be Scared': if AI lets teams ship code 10x faster while the vulnerability rate stays flat or worsens, the attack surface scales proportionally. He argues that security is unlike every other class of bug because it has no half-life — the problem compounds rather than fading — so vulnerabilities must be surfaced at the point of generation, which now means surfacing them to the LLM rather than to a human's fingertips. His practical prescription is the 'rule of five' multi-pass approach: security is its own pass, never bundled with correctness, performance, or style, and it should be both the first and last pass. He recommends handing agents security tooling (Snyk, Chainguard) as token-saving tools they'll willingly use, noting Fable's own hardening pass on his codebase missed 241 vulnerabilities Snyk found. The Q&A extends into agent permissions, adversarial supervisor agents, prompt injection, and a personal warning to establish family code words against AI voice/video scams.

## Key Points

- A bank's chief security architect posed the framing question of the talk: if code ships 10x faster and the defect rate stays constant, the defect surface grows 10x — and Yegge argues the rate will actually get worse with AI writing code.
- New attack classes are already here, notably 'slop squatting,' where attackers upload real packages under names LLMs reliably hallucinate, so the code builds, runs, and passes tests while containing a backdoor.
- Google's TAP team found bugs have a 'half-life of urgency' that motivates surfacing them as you type — but security bugs are the one class with no half-life, because the problem compounds over time instead of decaying.
- Since the developer writing the code is now an LLM without fingers, vulnerability findings have to be surfaced into the agent's loop rather than into an IDE gutter.
- The 'rule of five': LLMs need up to four or five review passes over their own work, and each concern — security, correctness, performance, elegance, house style — must be a separate pass or the model does a half-assed job of both.
- Yegge ran Snyk over a codebase Fable had just security-hardened and it found 241 vulnerabilities the model never thought to look for, though none were beyond already-public CVEs.
- Because LLMs are 'lazy in a good way' about spending tokens, they will readily adopt security tools that offload cognition — so the play is to give agents Snyk, Chainguard, and open-source scanners and have them check each other's work.
- Five Eyes has warned that open-source models catching up to frontier capability is months away, not years, which puts strong hacking capability in anyone's hands on roughly a six-to-seven-month horizon.
- For agents taking actions rather than writing code, Yegge advocates thinking adversarially — supervisor agents watching queue-processing agents, and aggressive least-privilege auditing of service account credentials — because one agent will always eventually screw it up.
- He predicts a new in-house role, 'agentic security,' will emerge as an extension of existing security functions, and urges companies to design solutions now despite almost nothing mature existing on the market.

## Notable Quotes

> "If everyone's shipping code at the same at sorry, at 10 times faster and the defect rate stays the same, the security defect, right? The the vulnerability rate. Then that doesn't that mean that the defects surface goes up by 10x?"
>
> — [1:28](https://www.youtube.com/watch?v=yWS0udrIOc8&t=88s) &middot; *The question from a bank's chief security architect that frames the entire talk.*

> "the subtle implied question is not if the defect rate stays the same, the defect rate's going to get worse. A lot worse with AIs writing the code."
>
> — [2:12](https://www.youtube.com/watch?v=yWS0udrIOc8&t=132s) &middot; *Sharpens the 10x framing into a stronger, more contestable claim.*

> "The real answer is you have to be scared of what's coming."
>
> — [2:12](https://www.youtube.com/watch?v=yWS0udrIOc8&t=132s) &middot; *The talk's actual thesis, stated plainly.*

> "it builds and it runs, and the tests pass, and it looks right, but what it downloaded was a backdoor."
>
> — [3:38](https://www.youtube.com/watch?v=yWS0udrIOc8&t=218s) &middot; *Compact statement of why slop squatting evades normal verification.*

> "somebody noticed that the LLMs are hallucinating its name, and they uploaded one that does exactly the same thing as the one it thought it was getting, plus a vulnerability."
>
> — [3:38](https://www.youtube.com/watch?v=yWS0udrIOc8&t=218s) &middot; *The clearest mechanical explanation of the slop-squatting attack.*

> "we're entering a world where everything you write every bit of code that you generate is going to have to get far more security scrutiny than it's ever had before."
>
> — [4:14](https://www.youtube.com/watch?v=yWS0udrIOc8&t=254s) &middot; *States the operational consequence for every team shipping AI-written code.*

> "the problem, folks, is that that works for all classes of bugs except for security. There's no half-life on it biting you."
>
> — [5:39](https://www.youtube.com/watch?v=yWS0udrIOc8&t=339s) &middot; *The talk's most original conceptual argument, drawn from Google's TAP data.*

> "What if the developer doesn't have any fingers? I don't know how how many fingers the LLMs have."
>
> — [6:28](https://www.youtube.com/watch?v=yWS0udrIOc8&t=388s) &middot; *Memorably reframes shift-left tooling for the agentic era.*

> "You all know security is an arms race. One that never ends. One that's going up exponentially with Moore's law. One that's going to get real uncomfortable when quantum comes along."
>
> — [6:28](https://www.youtube.com/watch?v=yWS0udrIOc8&t=388s) &middot; *Explains why 'can't the model just write secure code' is the wrong question.*

> "When you do things with LLMs, often you have to get them to do up to four to five reviews of the work that they did before it's like actually ready to ship."
>
> — [7:46](https://www.youtube.com/watch?v=yWS0udrIOc8&t=466s) &middot; *The 'rule of five' — his most portable practical heuristic.*

> "you can't give them security at the same time as you give them correctness. They'll do a half-ass job of both."
>
> — [8:28](https://www.youtube.com/watch?v=yWS0udrIOc8&t=508s) &middot; *The core tradeoff claim behind separating passes.*

> "LLMs can synthesize any software that they want, but they're very lazy in a good way, right? Lazy in like they don't want to spend tokens if they don't have to"
>
> — [9:14](https://www.youtube.com/watch?v=yWS0udrIOc8&t=554s) &middot; *The economic argument for why agents will actually adopt security tools.*

> "get the open source ones, get the sneak one, get the chain guard one, get the all of them and have them check each other's work, too."
>
> — [11:15](https://www.youtube.com/watch?v=yWS0udrIOc8&t=675s) &middot; *The concrete implementation recipe.*

> "They just announced that it is now months, not years, until it starts happening."
>
> — [11:51](https://www.youtube.com/watch?v=yWS0udrIOc8&t=711s) &middot; *The Five Eyes timeline claim that anchors his urgency.*

> "you can't trust it to automatically write good code any more than you can trust it to write elegant code by default. That's a separate concern. It's a separate pass."
>
> — [12:31](https://www.youtube.com/watch?v=yWS0udrIOc8&t=751s) &middot; *Generalizes the multi-pass principle across quality dimensions.*

> "security should be your first one and your last one."
>
> — [13:23](https://www.youtube.com/watch?v=yWS0udrIOc8&t=803s) &middot; *The single most actionable prescription in the talk.*

> "Go to your families offline, like in person, and get your your code words refreshed."
>
> — [13:23](https://www.youtube.com/watch?v=yWS0udrIOc8&t=803s) &middot; *Unusual personal-security advice from a developer conference stage.*

> "You're all not scared enough of what's coming."
>
> — [14:05](https://www.youtube.com/watch?v=yWS0udrIOc8&t=845s) &middot; *The quote he says radicalized him two years ago, now repeated as his own message.*

> "I think of adversarial groups of agents tasked with doing that queue management cuz one agent will always eventually screw it up."
>
> — [19:21](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1161s) &middot; *His architectural answer to agents-taking-actions risk.*

> "your engineers are going to spin up or your non-engineers are going to spin up a bunch of agents with way too many permissions"
>
> — [20:05](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1205s) &middot; *Names the specific permissions failure mode the talk title promises.*

> "I feel like there are like new security roles about ready to emerge inside of companies, agentic security that it's kind of an extension of what they're already doing."
>
> — [21:15](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1275s) &middot; *Organizational prediction, useful for cross-talk synthesis on team structure.*

## Positions

- AI-written code will have a worse vulnerability rate than human-written code, not merely the same rate at higher volume. ([2:12](https://www.youtube.com/watch?v=yWS0udrIOc8&t=132s), confidence: stated)
- Security bugs are the one class of defect with no half-life of urgency — the problem compounds over time rather than fading. ([5:39](https://www.youtube.com/watch?v=yWS0udrIOc8&t=339s), confidence: stated)
- Security findings must be surfaced to the LLM in its loop, the way Google surfaced bugs at a developer's fingertips. ([6:28](https://www.youtube.com/watch?v=yWS0udrIOc8&t=388s), confidence: stated)
- Frontier models cannot be trusted to write secure code by default; security is a separate pass, just like performance, elegance, and coding standards. ([12:31](https://www.youtube.com/watch?v=yWS0udrIOc8&t=751s), confidence: stated)
- LLMs need up to four or five review passes over their own work before it is ready to ship. ([7:46](https://www.youtube.com/watch?v=yWS0udrIOc8&t=466s), confidence: stated)
- Combining security and correctness in a single prompt produces poor results on both. ([8:28](https://www.youtube.com/watch?v=yWS0udrIOc8&t=508s), confidence: stated)
- Security should be both the first pass and the last pass over generated code. ([13:23](https://www.youtube.com/watch?v=yWS0udrIOc8&t=803s), confidence: stated)
- Snyk found 241 vulnerabilities in his codebase after Fable had already completed a security hardening pass on it. ([7:46](https://www.youtube.com/watch?v=yWS0udrIOc8&t=466s), confidence: stated)
- Snyk's claim to find proprietary vulnerabilities ahead of the CVE registry was not borne out on his codebase — everything it found was already a public CVE. ([10:31](https://www.youtube.com/watch?v=yWS0udrIOc8&t=631s), confidence: stated)
- Open-source models will reach frontier hacking capability in roughly six to seven months. ([12:31](https://www.youtube.com/watch?v=yWS0udrIOc8&t=751s), confidence: stated)
- Because LLMs minimize token spend, they will voluntarily adopt security tools that offload cognition to deterministic scanners. ([9:14](https://www.youtube.com/watch?v=yWS0udrIOc8&t=554s), confidence: stated)
- Agent queue-processing systems require adversarial supervisor agents because any single agent will eventually fail. ([19:21](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1161s), confidence: stated)
- Companies must design in-house agent permission and monitoring solutions now, because nothing mature exists to buy. ([20:05](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1205s), confidence: stated)
- Convincing AI-generated family-distress scams with video are months away and will drain real bank accounts. ([14:05](https://www.youtube.com/watch?v=yWS0udrIOc8&t=845s), confidence: stated)
- There is no good technical defense for prompt injection today; it is currently an education problem. ([21:15](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1275s), confidence: stated)
- Running agents fully unsupervised overnight is the next frontier and very few practitioners can do it reliably today. ([18:06](https://www.youtube.com/watch?v=yWS0udrIOc8&t=1086s), confidence: stated)
- Skepticism about AI progress stems from tunnel vision — people extrapolate from roughly three months back and three months forward and see a flat curve. ([15:59](https://www.youtube.com/watch?v=yWS0udrIOc8&t=959s), confidence: stated)

## Concepts

- [adversarial agent supervision](../concepts/adversarial-agent-supervision.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [ai-assisted vulnerability discovery](../concepts/ai-assisted-vulnerability-discovery.md)
- [background agents](../concepts/background-agents.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [secure code generation](../concepts/secure-code-generation.md)
- [software supply chain security](../concepts/software-supply-chain-security.md)

