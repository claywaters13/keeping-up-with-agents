---
title: "The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents"
type: "talk"
slug: "the-great-loops-debate-dex-horthy-geoff-huntley-ian-livingstone-greg-pstrucha-in"
track: "Agent & Harness Engineering"
org: "Panel — Keycard (Ali Howard, host; Ian Livingstone, CEO/co-founder), Human Layer (Dex Raad, CEO), Sentry (Greg Pstrucha), Geoff Huntley (creator of the Ralph loop; formerly tech lead at Canva)"
video_id: "c35YoMdnI78"
duration_sec: 3616
word_count: 11597
speakers: []
---

# The Great Loops Debate — Dex Horthy, Geoff Huntley, Ian Livingstone, Greg Pstrucha, @insecure-agents

**Speakers:** unknown / not credited

**Org:** Panel — Keycard (Ali Howard, host; Ian Livingstone, CEO/co-founder), Human Layer (Dex Raad, CEO), Sentry (Greg Pstrucha), Geoff Huntley (creator of the Ralph loop; formerly tech lead at Canva)

**Track:** Agent & Harness Engineering &nbsp;|&nbsp; **Duration:** 1h 0m

[Watch on YouTube](https://www.youtube.com/watch?v=c35YoMdnI78)

## Summary

A five-person Oxford-style panel at AI Engineer World's Fair 2026 debates whether there is a gap between the hype around agentic "loops" (Geoff Huntley's Ralph loop, software factories) and what actually works. Huntley and Ian Livingstone argue loops are inevitable and already economically compelling — Huntley claims he hasn't hand-written code in 2.5 years and pegs looped agent work at $10.42/hour — with the real engineering being back-pressure: pre-commit hooks, static types, linters, simulators that keep the loop from closing until domain constraints are satisfied. Dex Raad and Greg Pstrucha counter that the hype is outrunning the discipline: you still have to read the code, per-iteration error compounds across loops, token spend is not sustainable at enterprise scale, and architectural judgment about what *not* to build stays human. Notably both sides converge on the same practical advice — start small, aim for 2-3x rather than 100x, verify deterministically wherever possible, and distrust Twitter. Worth watching for the concrete verification tactics and for the honest post-mortem of Huntley's Loom experiment, which he shelved for six months because verification wasn't there.

## Key Points

- Huntley frames loops as a new programmable substrate — treating the LLM like a CPU architecture — reducible to a `while true` bash loop with `cat prompt`, using the file system as state and recycling the context window each iteration.
- The pro-loop side argues the models have been good enough for over a year and that what changed was human understanding and time to experiment, not model capability.
- The skeptical side's core argument is compounding error: a 5% per-iteration error rate looped 10-20 times degrades correctness badly, and each iteration costs money, making unbounded loop-on-loop orchestration economically unsustainable.
- Both sides agree verification is the bottleneck, and specifically that deterministic/static verification (types, linters, pre-commit hooks, simulators, test suites) is what makes looping work — adding non-deterministic verifiers on top makes things worse.
- Livingstone argues models cannot keep themselves aligned; better models are more goal-seeking and better at finding exploits, so safety must come from surrounding infrastructure, and liability must always ground out in a human.
- Huntley's own Loom experiment — using PostHog-style A/B data to give agents a feedback loop on UI quality — has been paused for six months, which Raad cites as the clearest example of hype outrunning discipline.
- Raad advises against the 3-month 'build the software factory' project, recommending small incremental loops that get you 2-3x faster while still reading the code and owning the architecture.
- Pstrucha argues agents love complexity and add to the stack unbounded, so decisions about simplicity, architecture, and what not to build remain human-in-the-loop.
- Huntley makes a language-choice claim: dynamic languages (Python, Ruby) produce maintainability messes under loops, while static type systems (Haskell, Rust) act as a form of verification — and code may need to be explainable rather than readable.
- Attribution is unsolved: Git allows only one commit signer, and there is no substrate for attributing agent-generated code back to the human who authorized the loop.

## Notable Quotes

> "Um I don't see myself going back to writing code by hand. It's been 2 and 1/2 years since I manually wrote code by hand."
>
> — [4:24](https://www.youtube.com/watch?v=c35YoMdnI78&t=264s) &middot; *the single strongest personal-practice claim on the pro-loop side*

> "we are all looking for magic, you're all looking for a silver bullet, we're all looking for something that will take away that horrible part of our jobs that we all hate, which is like reviewing code."
>
> — [8:21](https://www.youtube.com/watch?v=c35YoMdnI78&t=501s) &middot; *names the psychological driver the skeptics say the hype exploits*

> "I actually think we need to step down an abstraction level if anything."
>
> — [9:59](https://www.youtube.com/watch?v=c35YoMdnI78&t=599s) &middot; *direct inversion of the 'stop prompting, start writing loops' thesis*

> "loops are at the core of everything we build already. They were at the core of how we built software 30 years ago. What is CICD, PR pull requests, design review, feedback from customers other than just driving a loop."
>
> — [11:06](https://www.youtube.com/watch?v=c35YoMdnI78&t=666s) &middot; *Livingstone's framing that loops are not new, only faster*

> "but one of the things that the current sort of hype-based discourse uh leads you to believe is that you can just have loops on top of loops on top of loops and orchestrate that or orchestrate your problems of quality away by more tokens"
>
> — [14:07](https://www.youtube.com/watch?v=c35YoMdnI78&t=847s) &middot; *states the specific hype claim the skeptics are rejecting*

> "you have to ask yourself what is a good budget for an engineer? Is it 10K a month? 100K? 1 million dollar a month for for a token spend? At some point that that just starts cracking and it's not sustainable in the way that we are doing it today."
>
> — [14:46](https://www.youtube.com/watch?v=c35YoMdnI78&t=886s) &middot; *the economic-viability argument, with concrete numbers*

> "as we scale with these models and as we use reinforcement learning, they're inherently incredibly goal-seeking"
>
> — [16:40](https://www.youtube.com/watch?v=c35YoMdnI78&t=1000s) &middot; *security framing: capability gains and alignment risk move together*

> "the the most concrete thing you can do to secure your environment is just not have secrets as files"
>
> — [18:43](https://www.youtube.com/watch?v=c35YoMdnI78&t=1123s) &middot; *single most actionable security recommendation in the talk*

> "Um it doesn't matter how good models get, folks. The models have been good enough for at least the last year."
>
> — [19:14](https://www.youtube.com/watch?v=c35YoMdnI78&t=1154s) &middot; *Huntley's claim that adoption, not capability, is the limiting factor*

> "These LLMs generate code better than any software developer in the mass market that most founders can actually hire for."
>
> — [19:59](https://www.youtube.com/watch?v=c35YoMdnI78&t=1199s) &middot; *the most contestable capability claim made on stage*

> "Um now why loops? It's really simple. Cuz if you run it in a loop, it works out to $10.42 an hour."
>
> — [20:42](https://www.youtube.com/watch?v=c35YoMdnI78&t=1242s) &middot; *the pro-loop cost number, directly opposing Pstrucha's spend argument*

> "to be frank, the model the model's a drunk. Right? You can't trust them. But, like, we accept that, but we engineer away those failure domains."
>
> — [22:53](https://www.youtube.com/watch?v=c35YoMdnI78&t=1373s) &middot; *crisp statement of the engineering-around-unreliability posture*

> "the engineering here is to prevent the loop from actually closing until it satisfies your engineering certification and your your requirements in the domain"
>
> — [22:53](https://www.youtube.com/watch?v=c35YoMdnI78&t=1373s) &middot; *defines what 'loop engineering' concretely means*

> "And so now you've even removed like the human visual taste from the equation."
>
> — [34:24](https://www.youtube.com/watch?v=c35YoMdnI78&t=2064s) &middot; *describes the Loom idea of turning subjective UI quality into loop-verifiable data*

> "the way to not loop slop together and make more slop is to like read the thing that's coming out the other end and make sure it's not slop"
>
> — [35:32](https://www.youtube.com/watch?v=c35YoMdnI78&t=2132s) &middot; *the skeptics' bottom line in one sentence*

> "The labs haven't cracked it. So what makes you think you're going to crack it?"
>
> — [35:32](https://www.youtube.com/watch?v=c35YoMdnI78&t=2132s) &middot; *Huntley conceding the verification problem is genuinely open*

> "we do security scanning after on our PRs in local, and after our PRs even land, because they will always find some things that are real, um, that we have overlooked, and they sort of beat humans on the on the code review"
>
> — [36:57](https://www.youtube.com/watch?v=c35YoMdnI78&t=2217s) &middot; *a skeptic reporting a loop that demonstrably pays for itself*

> "in my experience, agents love complexity. They will keep adding to the stack um unbounded."
>
> — [42:35](https://www.youtube.com/watch?v=c35YoMdnI78&t=2555s) &middot; *the argument for keeping architecture human-owned*

> "instead of trying to automate everything end-to-end, build these small incremental loops throughout your system and you will wake up one day and you will be moving two to three times faster while still being able to read the code, while still owning the architecture"
>
> — [48:28](https://www.youtube.com/watch?v=c35YoMdnI78&t=2908s) &middot; *the talk's most transferable piece of adoption advice*

> "the only people who have liability are people that can have consequences, right? And that always has to be grounded in it being a human."
>
> — [50:15](https://www.youtube.com/watch?v=c35YoMdnI78&t=3015s) &middot; *the accountability limit on any fully autonomous factory*

> "our profession is a bit of a clown show. We actually don't have liability at a personal level. Like we call ourselves engineers, we're not really engineers."
>
> — [52:27](https://www.youtube.com/watch?v=c35YoMdnI78&t=3147s) &middot; *sharp rebuttal to the liability framing from a nominal ally*

> "if you try to run in loops or try to build a factory to using Python, it's going to be a clown show."
>
> — [57:24](https://www.youtube.com/watch?v=c35YoMdnI78&t=3444s) &middot; *a falsifiable, opinionated language claim few others would make on stage*

> "my advice is uh pay attention to Jeff. Uh let me know when Loom is actually working and until then uh use loops, but not like that."
>
> — [56:36](https://www.youtube.com/watch?v=c35YoMdnI78&t=3396s) &middot; *the skeptics' closing position, stated as a concrete falsifiable test*

## Positions

- Model capability has not been the bottleneck for at least a year; adoption lagged because people needed time to build intuition, not because models improved. ([19:14](https://www.youtube.com/watch?v=c35YoMdnI78&t=1154s), confidence: stated)
- Running a coding agent in a loop costs roughly $10.42 per hour. ([20:42](https://www.youtube.com/watch?v=c35YoMdnI78&t=1242s), confidence: stated)
- Current LLMs generate better code than the median software developer most founders can hire in the mass market. ([19:59](https://www.youtube.com/watch?v=c35YoMdnI78&t=1199s), confidence: stated)
- The current pattern of stacking loops on loops and buying quality with more tokens is economically unsustainable at company scale. ([14:46](https://www.youtube.com/watch?v=c35YoMdnI78&t=886s), confidence: stated)
- Adding non-deterministic verification on top of agent output makes correctness worse; verification should be pushed toward static and deterministic checks. ([25:38](https://www.youtube.com/watch?v=c35YoMdnI78&t=1538s), confidence: stated)
- A model can never be made 100% safe through alignment or reinforcement learning; safety must come from surrounding infrastructure. ([17:56](https://www.youtube.com/watch?v=c35YoMdnI78&t=1076s), confidence: stated)
- As models get better they become more goal-seeking and better at finding exploits and privilege escalations. ([18:43](https://www.youtube.com/watch?v=c35YoMdnI78&t=1123s), confidence: stated)
- Not storing secrets as files is the single most effective concrete step to secure an agent environment. ([18:43](https://www.youtube.com/watch?v=c35YoMdnI78&t=1123s), confidence: stated)
- As humans interact less directly with software, the surface becomes more API-constrained, less subjective, and therefore more verifiable — making loops more viable over time. ([12:20](https://www.youtube.com/watch?v=c35YoMdnI78&t=740s), confidence: stated)
- You should keep agent context under roughly 100,000 tokens even with million-token context windows; ~200k is the upper revision and under 60k is right for the hardest problems. ([28:31](https://www.youtube.com/watch?v=c35YoMdnI78&t=1711s), confidence: stated)
- Compaction is a lossy operation that degrades fidelity, so deterministically re-allocating a fresh context each iteration beats compacting. ([31:12](https://www.youtube.com/watch?v=c35YoMdnI78&t=1872s), confidence: stated)
- You cannot prevent loops from compounding slop except by reading the output yourself. ([35:32](https://www.youtube.com/watch?v=c35YoMdnI78&t=2132s), confidence: stated)
- Loom does not work yet and will not until programming languages or models get substantially better. ([35:01](https://www.youtube.com/watch?v=c35YoMdnI78&t=2101s), confidence: stated)
- AI security scanning on PRs beats human reviewers at finding real issues and is worth roughly $5 per PR. ([36:57](https://www.youtube.com/watch?v=c35YoMdnI78&t=2217s), confidence: stated)
- Architectural and design decisions — especially what not to build and where to keep complexity — should stay with humans for the foreseeable future. ([42:35](https://www.youtube.com/watch?v=c35YoMdnI78&t=2555s), confidence: stated)
- Targeting 100x speedup traps you in meta-optimization; 2-3x is the realistic and achievable target and would still transform every company. ([49:02](https://www.youtube.com/watch?v=c35YoMdnI78&t=2942s), confidence: stated)
- Liability for agent-produced software must always ground out in a human or corporation; agents cannot be liable entities. ([50:43](https://www.youtube.com/watch?v=c35YoMdnI78&t=3043s), confidence: stated)
- Git's single-signer commit model is inadequate for agent-authored code and must be fixed. ([50:15](https://www.youtube.com/watch?v=c35YoMdnI78&t=3015s), confidence: stated)
- Software engineering as a profession has no personal liability, so appeals to engineering accountability are hollow. ([52:27](https://www.youtube.com/watch?v=c35YoMdnI78&t=3147s), confidence: stated)
- Dynamically typed languages like Python and Ruby produce unmaintainable results under loops; statically typed languages like Haskell and Rust work far better because types are verification. ([57:24](https://www.youtube.com/watch?v=c35YoMdnI78&t=3444s), confidence: stated)
- Code may no longer need to be readable, only explainable, since the model can explain it on demand. ([58:01](https://www.youtube.com/watch?v=c35YoMdnI78&t=3481s), confidence: stated)
- Generating your own dependencies to requirement instead of using open source minimizes supply chain attack blast radius. ([58:44](https://www.youtube.com/watch?v=c35YoMdnI78&t=3524s), confidence: stated)
- Nobody should be running coding agents on their local laptop — not because of AI, but because of pre-existing NPM supply chain risk. ([45:52](https://www.youtube.com/watch?v=c35YoMdnI78&t=2752s), confidence: stated)
- Software factories are not yet a solved product; companies are only now being founded to build them, so organizations should not expect to implement one internally today. ([56:36](https://www.youtube.com/watch?v=c35YoMdnI78&t=3396s), confidence: stated)
- Agent shared-memory access control is an unsolved problem, though markdown files plus attribution may be a workable substrate. ([39:53](https://www.youtube.com/watch?v=c35YoMdnI78&t=2393s), confidence: stated)

## Concepts

- [agent identity and authorization](../concepts/agent-identity-and-authorization.md)
- [agent memory](../concepts/agent-memory.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [context rot](../concepts/context-rot.md)
- [context window management](../concepts/context-window-management.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [parallel agent execution](../concepts/parallel-agent-execution.md)
- [software supply chain security](../concepts/software-supply-chain-security.md)
- [verifier design](../concepts/verifier-design.md)

