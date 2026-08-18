---
title: "\"The engineer of the future is the person who is able to choose what is worth doing.\" — Addy Osmani"
type: "talk"
slug: "the-engineer-of-the-future-is-the-person-who-is-able-to-choose-what-is-worth-doi"
track: "AI Architects: Tokenmaxxing"
day: "Day 3 — Session Day 2"
room: "Leadership 2"
video_id: "n97BCfyFIvw"
duration_sec: 1106
word_count: 3070
speakers: ["Vlad Luzin"]
---

# "The engineer of the future is the person who is able to choose what is worth doing." — Addy Osmani

*Program title: Is Orchestration the Future?*

**Speakers:** [Vlad Luzin](../speakers/vlad-luzin.md)

**Track:** AI Architects: Tokenmaxxing &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Leadership 2 &nbsp;|&nbsp; **Duration:** 18m 26s

[Watch on YouTube](https://www.youtube.com/watch?v=n97BCfyFIvw)

## Summary

Addy Osmani argues that as coding agents absorb more of the execution loop, the scarce engineering skill shifts from producing code to owning the verdict on it — deciding what is worth doing, inspecting the evidence, accepting the risk, and being answerable after it ships. He traces the progression from harness engineering to loop engineering to 'software factories,' then makes the case that generation getting cheaper does not make review cheaper, citing Sonar survey data that ~96% of engineers distrust AI code while only about half always verify it. He introduces 'alpha' (the gap between what you can do and what models can do) and 'decay' (the clock on that gap), and applies the decay test to speed, recall, verification, and even taste — all of which erode as the frontier moves — while credibility and accountability persist. The talk names three failure modes to avoid: cognitive debt, cognitive surrender, and orchestration tax. Worth watching if you manage teams shipping AI-assisted code and need vocabulary for where humans still add leverage; less useful if you want concrete tooling or implementation detail.

## Key Points

- The engineer's differentiating role is moving from producing work to rendering verdicts: deciding whether something ships, is blocked, redirected, or has its risk accepted, and being accountable for that decision afterward.
- The coding agent is the model plus the harness (context, tools, file system, Git), and loop engineering added systems that keep prompting, checking, remembering, and deciding — which is when agents began to feel like infrastructure.
- Cheaper generation does not make review cheaper, so verification must be made cheaper, clearer, and harder to skip, or distrust of AI code coexists with no bandwidth to act on it.
- Sonar research found clean and messy repos had roughly the same agent pass rates, but clean code used fewer tokens and caused fewer revisits — maintainability is now an efficiency argument, not just a human-readability one.
- Every individual capability is 'alpha' with a decay clock: speed decayed, recall decayed into harness memory, verification is moving into evals and static checks, and even taste resets as models learn from examples and preferences.
- Three failure modes to avoid are cognitive debt (the gap between code that exists and code anyone understands), cognitive surrender (adopting the AI's answer before forming your own), and orchestration tax (adding agents when cognitive bandwidth does not parallelize).
- Agents can own the inner loop — investigate, implement, test, report — while the outer loop of deciding, verifying, approving, and owning remains engineering; the boundary is evidence and responsibility, not 'human looks at AI output.'
- Historically every reduction in the cost of writing software increased demand for it, so agents will move the bottleneck from 'can we build this' to 'should this exist and can we answer for it' rather than removing engineering work.

## Notable Quotes

> "I think that the engineer of the future is going to be really defined by the person who is able to choose what is worth doing."
>
> — [0:01](https://www.youtube.com/watch?v=n97BCfyFIvw&t=1s) &middot; *the thesis of the talk in one line*

> "Quality is something that we all talk about a lot, but quality produces evidence. A verdict assigns responsibility."
>
> — [0:57](https://www.youtube.com/watch?v=n97BCfyFIvw&t=57s) &middot; *draws the talk's central distinction between evidence and accountability*

> "the important question here becomes a lot less about what is your title and more what part of the system can you own?"
>
> — [1:44](https://www.youtube.com/watch?v=n97BCfyFIvw&t=104s) &middot; *reframes role definition around ownership rather than job function*

> "With harness engineering, the coding agent is the model plus the harness around it, right? Your context, your tools, your file system, Git. And the harness is what turns intelligence into something that you can delegate to."
>
> — [2:31](https://www.youtube.com/watch?v=n97BCfyFIvw&t=151s) &middot; *compact definition of harness engineering and why it enables delegation*

> "found that clean and messy repos had roughly the same pass rates, but clean code actually used fewer tokens and caused fewer revisits"
>
> — [3:50](https://www.youtube.com/watch?v=n97BCfyFIvw&t=230s) &middot; *reports a specific research finding tying code quality to agent efficiency*

> "Now, making generation cheaper does not automatically make review cheaper, right?"
>
> — [3:50](https://www.youtube.com/watch?v=n97BCfyFIvw&t=230s) &middot; *names the core asymmetry the rest of the talk is built on*

> "If 96% of people don't fully trust that code, but only about half always verify before committing, we have this danger that we've got distrust without bandwidth."
>
> — [4:31](https://www.youtube.com/watch?v=n97BCfyFIvw&t=271s) &middot; *the talk's sharpest number, quantifying the verification gap*

> "And so safety comes from making verification cheaper, clearer, and harder for people to skip."
>
> — [4:31](https://www.youtube.com/watch?v=n97BCfyFIvw&t=271s) &middot; *states the prescriptive fix for the verification bottleneck*

> "Alpha is the gap between what you can do today and what current models can do."
>
> — [5:53](https://www.youtube.com/watch?v=n97BCfyFIvw&t=353s) &middot; *defines a term the rest of the career argument depends on*

> "But I also think that we have to be very careful because taste can become a magic word for whatever part of the work we don't want to explain just yet."
>
> — [6:40](https://www.youtube.com/watch?v=n97BCfyFIvw&t=400s) &middot; *pushes back on the fashionable 'taste' discourse*

> "Taste is the ability to make high-quality qualitative judgments where no objective metric exists yet."
>
> — [6:40](https://www.youtube.com/watch?v=n97BCfyFIvw&t=400s) &middot; *the operational definition of taste the speaker endorses*

> "But taste is not some eternal moat. It's alpha as well."
>
> — [7:20](https://www.youtube.com/watch?v=n97BCfyFIvw&t=440s) &middot; *takes a contrarian side against taste-as-permanent-moat claims*

> "The better question for us is really what can only a human be answerable for."
>
> — [8:40](https://www.youtube.com/watch?v=n97BCfyFIvw&t=520s) &middot; *replaces the common 'what can agents do' framing*

> "For code, it's the gap between how much code exists in your repo and how much any human on your team genuinely understands."
>
> — [9:57](https://www.youtube.com/watch?v=n97BCfyFIvw&t=597s) &middot; *concrete definition of cognitive debt*

> "So, agents can now stay inside the system long enough for the human to lose the thread."
>
> — [10:35](https://www.youtube.com/watch?v=n97BCfyFIvw&t=635s) &middot; *explains why long-horizon agent runs break glance-at-the-end review*

> "So, the failure mode is not using AI, but it's borrowed confidence."
>
> — [11:12](https://www.youtube.com/watch?v=n97BCfyFIvw&t=672s) &middot; *names cognitive surrender precisely*

> "More AI agents running does not mean that there is more of you available. Your cognitive bandwidth does not parallelize."
>
> — [12:00](https://www.youtube.com/watch?v=n97BCfyFIvw&t=720s) &middot; *direct counter to the 'ship with thousands of agents' pitch*

> "Now, here is the career math. The half-life of an edge might be one model release."
>
> — [12:40](https://www.youtube.com/watch?v=n97BCfyFIvw&t=760s) &middot; *memorable framing of capability decay*

> "The agent can follow your runbook, but it can't inherit the consequences."
>
> — [13:25](https://www.youtube.com/watch?v=n97BCfyFIvw&t=805s) &middot; *separates execution from responsibility in one sentence*

> "So, the boundary is not human looks at AI output. The boundary is evidence and responsibility."
>
> — [15:29](https://www.youtube.com/watch?v=n97BCfyFIvw&t=929s) &middot; *redefines human-in-the-loop away from surface review*

> "So, here's an operational rule. Explain it or don't ship it."
>
> — [16:10](https://www.youtube.com/watch?v=n97BCfyFIvw&t=970s) &middot; *the single actionable rule the talk offers*

> "It's not going to remove engineering work. It's going to move the bottleneck from can we build this to should this exist and can we answer for it?"
>
> — [17:32](https://www.youtube.com/watch?v=n97BCfyFIvw&t=1052s) &middot; *the closing claim about where demand and constraint shift*

## Positions

- Cheaper code generation does not automatically make code review cheaper, so verification is now the bottleneck rather than production. ([3:50](https://www.youtube.com/watch?v=n97BCfyFIvw&t=230s), confidence: stated)
- Clean, maintainable repos do not improve agent pass rates but do reduce token usage and revisits, so maintainability pays off as efficiency. ([3:50](https://www.youtube.com/watch?v=n97BCfyFIvw&t=230s), confidence: stated)
- Roughly 96% of engineers do not fully trust AI-generated code, but only about half always verify it before committing. ([4:31](https://www.youtube.com/watch?v=n97BCfyFIvw&t=271s), confidence: stated)
- Taste is not a durable moat — it is alpha that decays as models learn from examples and preferences, just more slowly than speed or recall. ([7:20](https://www.youtube.com/watch?v=n97BCfyFIvw&t=440s), confidence: stated)
- 'What can the agent do?' is no longer a useful strategic question because the list of things agents can't do keeps shrinking; the better question is what only a human can be answerable for. ([8:40](https://www.youtube.com/watch?v=n97BCfyFIvw&t=520s), confidence: stated)
- Running more agents in parallel does not increase your effective capacity, because human cognitive bandwidth does not parallelize and each loop adds routing, merging, and verification decisions. ([12:00](https://www.youtube.com/watch?v=n97BCfyFIvw&t=720s), confidence: stated)
- The half-life of any individual capability edge is about one model release, while the half-life of credibility and accountability is much longer. ([12:40](https://www.youtube.com/watch?v=n97BCfyFIvw&t=760s), confidence: stated)
- Agents can legitimately choose, route, merge, and escalate inside policy, but execution and responsibility are categorically different and responsibility cannot be delegated to an agent. ([13:25](https://www.youtube.com/watch?v=n97BCfyFIvw&t=805s), confidence: stated)
- Code should not ship unless some human can explain it well enough to defend it, even if no human typed or read every line. ([16:10](https://www.youtube.com/watch?v=n97BCfyFIvw&t=970s), confidence: stated)
- Lowering the cost of building software has historically increased rather than decreased demand for it, and agents will follow the same pattern. ([17:32](https://www.youtube.com/watch?v=n97BCfyFIvw&t=1052s), confidence: stated)
- Organizational governance of AI-assisted code is lagging behind adoption, making review and validation an institutional bottleneck rather than just an individual one. ([4:31](https://www.youtube.com/watch?v=n97BCfyFIvw&t=271s), confidence: implied)
- High agency in an agent-heavy world means deciding which problems deserve your ownership, not personally executing everything. ([14:45](https://www.youtube.com/watch?v=n97BCfyFIvw&t=885s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [ai-generated code quality](../concepts/ai-generated-code-quality.md)
- [automation bias](../concepts/automation-bias.md)
- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [cognitive debt](../concepts/cognitive-debt.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [parallel agent execution](../concepts/parallel-agent-execution.md)

