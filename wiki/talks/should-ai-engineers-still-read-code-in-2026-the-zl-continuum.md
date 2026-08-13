---
title: "Should AI Engineers Still Read Code in 2026? The Z/L Continuum"
type: "talk"
slug: "should-ai-engineers-still-read-code-in-2026-the-zl-continuum"
track: "AI Architects: Tokenmaxxing"
org: "ThursdAI"
day: "Day 3 — Session Day 2"
room: "Leadership 2"
video_id: "ZpK5PWX2YRM"
duration_sec: 1294
word_count: 3950
speakers: ["Alex Volkov"]
---

# Should AI Engineers Still Read Code in 2026? The Z/L Continuum

*Program title: The Z/L Continuum: Should AI Engineers Still Read Code?*

**Speakers:** [Alex Volkov](../speakers/alex-volkov.md)

**Org:** ThursdAI

**Track:** AI Architects: Tokenmaxxing &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Leadership 2 &nbsp;|&nbsp; **Duration:** 21m 34s

[Watch on YouTube](https://www.youtube.com/watch?v=ZpK5PWX2YRM)

## Summary

Alex Volkov stages a debate between two AI Engineer Europe talks — Ryan LeFebvre's "code is free" optimism and Mario Zechner's "read every effing line" caution — and argues both are right about different things. He walks through 2026 data (Faros AI's 22,000-engineer survey, Anthropic's own numbers) showing that AI-assisted output has genuinely exploded while stability has not: code deletion per PR up 861%, but incidents per PR up 242% and bugs per developer up 6x. His mea culpa is that the continuum he coined is not a spectrum of engineers but of tasks: authentication, money movement, permissions, and irreversible data get line-by-line review, while non-critical code can be routed to systemic proof (linters, docs, evals, traces, shadow mode) instead of human eyes. He closes on "capability drift" — as models improve, the review layer moves up from outputs to task direction to loops, but the requirement for proof never disappears, and self-grading agent loops hide review rather than remove it. Worth watching if you manage engineers arguing about this in Slack; the routing table slide is the practical artifact.

## Key Points

- The framing question "should I still read code in 2026?" is the wrong one; the better question is "what proof does this specific change need?", since the same engineer should YOLO some tasks and read every line of others.
- The optimists are empirically right about output: the Faros AI April 2026 survey of 22,000 engineers shows an 861% increase in code deletion per PR, and Anthropic reports shipping eight times more code per quarter than in 2025.
- The pessimists are empirically right about stability: the same survey shows a 242% increase in incidents per PR, a 31% increase in PRs merged with no review at all (human or agentic), and bugs per developer up six times over 2025.
- Volkov's routing table says to read every line for authentication, money movement, permissions, and irreversible data, and to route everything else to systemic proof.
- LeFebvre and Zechner agree more than their framings suggest: LeFebvre's mechanism is moving attention up a layer (encode the caught mistake into docs, linters, and reviewers so the system remembers), while Zechner's is routing by criticality.
- Separating the agent that writes code from the agent that reviews and tests it is essential — otherwise it's like writing your own exam, taking it, and grading yourself.
- Anthropic's own RSI essay predicts 10x-to-1000x output growth and names human code review as the new bottleneck via Amdahl's law, yet neither Anthropic nor OpenAI is removing humans from the loop.
- Loops — scheduled agents that discover a task, write the plan, execute, and verify themselves — are the emerging primitive, but a builder that grades itself hasn't removed the review, only hidden it.
- Capability drift moves where proof belongs (outputs → task direction → loops) but never removes the requirement for proof, which is why flexibility, not a fixed practice, is what keeps you an engineer.

## Notable Quotes

> "Because code got cheap, attention didn't."
>
> — [0:01](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1s) &middot; *The talk's thesis compressed into one line.*

> "In fact, 80% of Anthropic's code is now AI written and this is this stat is at least a few months old."
>
> — [2:19](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=139s) &middot; *Concrete number anchoring the claim that hand-written code is now the exception at frontier labs.*

> "They're seeing 14x the number of commits, which is insane and most of this is AI assisted."
>
> — [2:19](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=139s) &middot; *Quantifies the industry-wide output explosion via GitHub.*

> "It's free for you to produce, free to refactor, and it is not a thing to get hung up on anymore. Humans no longer need to concern themselves with implementation."
>
> — [4:07](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=247s) &middot; *The maximalist pole of the continuum, in LeFebvre's own words.*

> "The important thing is not the code, but the prompt and the guardrails that got you there."
>
> — [4:07](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=247s) &middot; *States where the optimist camp thinks attention should move.*

> "Agents are actually compounding booboos, which is my word for errors, with zero learning and no bottlenecks and delayed pain."
>
> — [4:54](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=294s) &middot; *Zechner's mechanism for why unreviewed agent output degrades over time.*

> "Non-critical code, sure, write slop ahead. Critical code, read every line."
>
> — [5:38](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=338s) &middot; *The cautious pole, and already a task-routing rule rather than a blanket one.*

> "861% increase in code deletion per PR. So us together with AI agents, we love deleting code."
>
> — [9:03](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=543s) &middot; *Headline stat from the Faros AI survey supporting the optimists.*

> "Anthropic also said that they're shipping eight times more code per quarter than in 2025."
>
> — [9:03](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=543s) &middot; *Reported throughput figure from the company with the most AI-generated code.*

> "Same essay, 31% increase in PRs merged with no review at all, human or agentic. Don't do this. I beg of you."
>
> — [10:19](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=619s) &middot; *The one practice Volkov flatly condemns, with a number attached.*

> "Same study, 242% increase in incident per PR. This kind of scary. The second study is also scary. Bugs per developer is up six times than 2025."
>
> — [10:19](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=619s) &middot; *The counterweight data showing output gains are not free.*

> "The continuum is real. It's not about the people. It's about the task."
>
> — [11:50](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=710s) &middot; *The talk's central correction and reusable reframe.*

> "He's not saying don't inspect your code. He's saying inspect the system, not every line."
>
> — [12:33](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=753s) &middot; *Reconciles the two poles by distinguishing object-level from system-level review.*

> "I think the better question right now for all of us is what proof does this specific change need?"
>
> — [13:50](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=830s) &middot; *Replaces the binary question with the operational one.*

> "You read every line of authentication, money movement, permissions, and irreversible data."
>
> — [14:28](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=868s) &middot; *The concrete, checkable boundary of the routing table.*

> "This is what Ryan Le Popo talks about. Build the system that builds the system because read spends your attention once, engineer makes the system remember."
>
> — [15:00](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=900s) &middot; *Names the tradeoff between one-time attention and durable systemic proof.*

> "We used to check if Claude is doing the work right. With Fable, we check if Claude is doing the right work."
>
> — [16:10](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=970s) &middot; *Captures the capability-driven shift in what review is even for.*

> "It's never felt so tempting to stop looking at code at all. But don't do this in production."
>
> — [16:49](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1009s) &middot; *Karpathy stating the anxiety from both ends in one sentence.*

> "Capability drift changes where proof belongs. It doesn't remove the requirement of proof."
>
> — [17:28](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1048s) &middot; *The talk's answer to "does this survive the next model?"*

> "But if the builder grades itself, you didn't remove the review, you hid it."
>
> — [19:17](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1157s) &middot; *The sharpest critique of self-verifying agent loops.*

> "So again, loops don't remove judgment, but they do raise the stakes on where you put it."
>
> — [19:51](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1191s) &middot; *Positions loops as an amplifier of review placement, not a replacement.*

> "Not every line in 2026 needs your eyes. Every system still needs your judgment."
>
> — [21:06](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1266s) &middot; *The closing formulation of the whole argument.*

## Positions

- The read-every-line vs. code-is-free continuum is a property of tasks, not of engineers; the same engineer should sit at both ends depending on the change. ([11:50](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=710s), confidence: stated)
- Authentication, money movement, permissions, and irreversible data changes must be read line by line by a human. ([14:28](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=868s), confidence: stated)
- Merging PRs with no review at all — human or agentic — is unacceptable practice, and it rose 31% per the Faros AI survey. ([10:19](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=619s), confidence: stated)
- AI-driven output gains are real but come with a stability cost: 242% more incidents per PR and 6x more bugs per developer than 2025. ([10:19](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=619s), confidence: stated)
- The same agent should not both write the code and write/grade its tests, because self-scoring is not productive verification. ([15:00](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=900s), confidence: stated)
- Self-verifying loops do not eliminate review; they conceal it, and relying entirely on them degrades product quality. ([19:17](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1157s), confidence: stated)
- Rising model capability relocates where proof is required but never removes the requirement for proof. ([17:28](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1048s), confidence: stated)
- LeFebvre and Zechner are not actually in opposition — one advocates inspecting the system rather than every line, the other advocates routing by criticality. ([12:33](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=753s), confidence: stated)
- Encoding a caught mistake into documentation, linters, and reviewers is more durable than catching it again in review, because humans are unreliable at catching repeated mistakes of the same type. ([13:12](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=792s), confidence: stated)
- Advice from lab engineers about loops should be treated as a lighthouse rather than immediate practice, because their tokens are free and yours are not. ([18:46](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=1126s), confidence: stated)
- Anthropic's status page instability is suggestive evidence that high AI-generated code output does not imply stability. ([9:48](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=588s), confidence: implied)
- Agents are better than humans at decomposing large changes into atomic reviewable PRs, and should be asked to do so. ([15:00](https://www.youtube.com/watch?v=ZpK5PWX2YRM&t=900s), confidence: stated)

## Concepts

- [adversarial agent supervision](../concepts/adversarial-agent-supervision.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [automation bias](../concepts/automation-bias.md)
- [catastrophic forgetting](../concepts/catastrophic-forgetting.md)
- [cross-model verification](../concepts/cross-model-verification.md)
- [developer productivity metrics](../concepts/developer-productivity-metrics.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [output guardrails](../concepts/output-guardrails.md)
- [task decomposition](../concepts/task-decomposition.md)

