---
title: "From Signal to PR: Anatomy of a Self-Improving Agent"
type: "talk"
slug: "from-signal-to-pr-anatomy-of-a-self-improving-agent"
track: "Evals"
org: "Arize"
day: "Day 3 — Session Day 2"
room: "Track 5"
video_id: "9HbzAWnKbo4"
duration_sec: 1235
word_count: 3797
speakers: ["Jason Lopatecki"]
---

# From Signal to PR: Anatomy of a Self-Improving Agent

**Speakers:** [Jason Lopatecki](../speakers/jason-lopatecki.md)

**Org:** Arize

**Track:** Evals &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 20m 35s

[Watch on YouTube](https://www.youtube.com/watch?v=9HbzAWnKbo4)

## Summary

Jason Lopatecki, founder of Arize, argues that observability is being rebuilt for agents rather than humans, and demos Signal, a product that runs coding agents (Claude Code, etc.) against production telemetry on a schedule or on error events and returns pre-investigated issues or PRs. His core claim is that the bottleneck in AI systems has shifted from writing the fix to having enough confidence that a fix is the right one, so the fix loop should be inverted: the agent investigates first and the human wakes up to evidence already assembled. He predicts teams will trace and log orders of magnitude more than today, because agents — unlike humans — can actually dig through that volume to recover the code path a request took. Practically, the talk is about skill design: getting the right traces and eval data into the repo as files that a coding harness can work with, versus naively pointing Claude at a database. Worth watching if you're building an agentic SRE/debugging loop, or weighing hosted-sandbox versus VPC deployment for agents that touch production data.

## Key Points

- Observability 1.0 was UIs and graphs built for human eyes; 2.0 is coding agents plus skills that let a human debug faster; the endpoint Arize is driving toward is a continuous loop where systems fix themselves.
- Telemetry's real value to an agent is that it reveals which code path actually executed — without it, the agent is guessing among a million possible paths.
- The bottleneck in the improvement loop is no longer producing a fix but establishing confidence that the fix is the right one to push.
- Arize inverts the classic loop: instead of a human triaging and an agent fixing, an agent investigates continuously and files issues with evidence attached, so the human's role moves from responder to reviewer (or driver, for larger fixes).
- Because agents can process volumes humans cannot, teams should trace and log 10x or more than they do today — the noise argument against heavy logging was a human-attention constraint.
- Skill design is the hard part: skills must find the right subset of traces and land it in the repo as files (sometimes 10MB), since coding harnesses work exceptionally well over files.
- Signal is deliberately open-box — you pick the harness (e.g. Claude Code), the sandbox (Arize, Daytona, or Anthropic-managed), the prompt, and the skills, and can resume a session locally.
- Many large enterprise customers will not connect production systems to a third-party managed agent but will install a sandbox into their own VPC, which drives Arize's deployment model.
- Evals (LLM-as-a-judge) don't disappear — they run online against production traces and become pre-processed signal the debugging agent consumes, and new evaluators get created from newly discovered failures to catch recurrences.

## Notable Quotes

> "Our first version of our our own agent frankly sucked."
>
> — [0:58](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=58s) &middot; *Sets up the talk's credibility as lessons from shipping, not theory.*

> "Well, observability used to be for humans. Used to be a UI you click, a graph you click, something you look at."
>
> — [1:31](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=91s) &middot; *The framing thesis of the whole talk.*

> "telemetry is like this smoke uh thrown off of your system that can allow these agents to go make fixes. It tells you what path in the code it took. Without that, you're guessing and there's a million paths it could have taken."
>
> — [2:08](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=128s) &middot; *Clearest statement of why traces are the substrate for agentic debugging.*

> "You can build at agent speed, but today you can't improve your systems really at this agent speed."
>
> — [2:51](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=171s) &middot; *Names the asymmetry the product exists to close.*

> "So those of us feel this this kind of governor happening within our our our our products. um and and the bottleneck is actually not the fix anymore."
>
> — [3:35](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=215s) &middot; *A contestable claim about where the real constraint sits.*

> "the future observability actually looks a lot more like this than it does clicking around graphana UI"
>
> — [5:08](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=308s) &middot; *A direct swipe at incumbent dashboard-centric observability.*

> "and for us, your job kind of moves from responder to reviewer."
>
> — [9:12](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=552s) &middot; *Compact statement of the role shift he's predicting.*

> "Now, you're going to trace 10 times more. You're going to log 10 times more because that helps you know what path your software took."
>
> — [9:12](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=552s) &middot; *A concrete, checkable magnitude prediction about telemetry volume.*

> "Before, you wouldn't do that because because humans can't dig through all the logs. It's just noise."
>
> — [9:46](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=586s) &middot; *Explains why the old logging economics no longer apply.*

> "all we're really trying to do ourselves is take your local debugging experience with cloud code cursor and run it periodically so pick your sandbox pick your harness, pick your skills, we'll pre-bank a bunch of things with you."
>
> — [9:46](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=586s) &middot; *The product thesis in one line, positioned against black-box SRE agents.*

> "given what you saw in the previous uh presentation, I would not recommend doing a financial trading agent. Um they they they're unlikely to make you money."
>
> — [10:50](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=650s) &middot; *Rare on-stage skepticism about a popular agent use case.*

> "the ideas observability platforms are really starting to get are becoming tied to the continuous loop to the the fix not just the the signal."
>
> — [14:45](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=885s) &middot; *States where he thinks the observability category is heading.*

> "a lot of our customers um don't want to connect their production systems to Tanthropic."
>
> — [13:16](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=796s) &middot; *The commercial and trust argument for VPC-deployed sandboxes.*

> "These harnesses are magical with files. So you get the file what happened. In some cases we have 10meg files like sitting in the repo."
>
> — [16:51](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=1011s) &middot; *Concrete implementation detail — files, not APIs, are the interface to the agent.*

> "but you've got to kind of design the skill surface area in a way that Claude can really really work well and and and it's not just like point Claude at the data."
>
> — [17:30](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=1050s) &middot; *His direct answer to 'why not just connect Claude Code to your data?'*

> "it but it tends to be like you build an eval for a failure you've seen before a lot of times."
>
> — [18:54](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=1134s) &middot; *Honest scoping of what LLM-as-a-judge evals actually cover.*

## Positions

- The bottleneck in improving AI systems is no longer generating the fix but gaining confidence that the fix is correct to push. ([3:35](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=215s), confidence: stated)
- Teams should trace and log roughly 10x (or orders of magnitude) more than today, because agents can consume volumes of telemetry that humans could not. ([9:12](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=552s), confidence: stated)
- The loop should be inverted so an agent investigates and files an evidence-backed issue before a human ever looks at it. ([4:30](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=270s), confidence: stated)
- The future of observability looks like agent-driven triggers and skills rather than clicking around a Grafana-style UI. ([5:08](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=308s), confidence: stated)
- Simply pointing a coding agent at your production data is insufficient; the skill must select the right data and write it into the repo as files. ([16:51](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=1011s), confidence: stated)
- Coding harnesses work best when data is delivered as files in the repo, even very large ones (~10MB). ([16:51](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=1011s), confidence: stated)
- Black-box 'SRE agent' products are the wrong approach; the harness, sandbox, and skills should all be user-selectable and open. ([9:46](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=586s), confidence: stated)
- Large enterprises will not route production system connections to third-party managed agents but will accept a vendor sandbox installed in their own VPC. ([13:16](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=796s), confidence: stated)
- Evals remain a core part of the loop rather than being displaced by agentic debugging, serving as pre-processed signal layered onto production traces. ([18:15](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=1095s), confidence: stated)
- LLM-as-a-judge evals are inherently backward-looking — you build them for failures you have already seen. ([18:54](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=1134s), confidence: stated)
- Larger fixes still require a human to spearhead them; full autonomy is not yet achievable, so the value today is eliminating the cold start. ([9:12](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=552s), confidence: stated)
- Financial trading agents are unlikely to be profitable at present. ([10:50](https://www.youtube.com/watch?v=9HbzAWnKbo4&t=650s), confidence: stated)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agent skills](../concepts/agent-skills.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [online evaluation](../concepts/online-evaluation.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [sovereign and air-gapped deployment](../concepts/sovereign-and-air-gapped-deployment.md)

