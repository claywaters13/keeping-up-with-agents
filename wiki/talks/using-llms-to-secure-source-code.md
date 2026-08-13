---
title: "Using LLMs to Secure Source Code"
type: "talk"
slug: "using-llms-to-secure-source-code"
track: "Security"
org: "Anthropic"
day: "Day 2 — Session Day 1"
room: "Track 5"
video_id: "imFedndyXYQ"
duration_sec: 1290
word_count: 3967
speakers: ["Eugene Yan"]
---

# Using LLMs to Secure Source Code

**Speakers:** [Eugene Yan](../speakers/eugene-yan.md)

**Org:** Anthropic

**Track:** Security &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 21m 30s

[Watch on YouTube](https://www.youtube.com/watch?v=imFedndyXYQ)

## Summary

Eugene Yan of Anthropic reports on several months of work with security teams using Claude to find and fix vulnerabilities in real codebases, and argues that frontier models have crossed a capability threshold where finding vulnerabilities is no longer the hard part. He backs this with time-horizon benchmarks from the UK AI Security Institute, Mozilla Firefox's jump from ~20 security bug fixes per month in 2025 to 400 in April, and Anthropic's own scan of 1,000+ open source repos that produced 6,200 high/critical findings. The core of the talk is a six-step agentic harness most teams converge on — threat model, sandbox, discovery, verification, triage, patching — with discovery optimizing recall and an independent, adversarial verification agent optimizing precision. He insists the real bottlenecks are now verification, triage, patching, and organizational issues like severity calibration and patch review bandwidth, none of which scale with compute. Watch it if you want a concrete, opinionated blueprint for standing up an LLM security pipeline and a realistic account of where it will jam.

## Key Points

- Model capability on cyber tasks shows a step jump above the previous time-horizon regression line, and the practical consequence is that vulnerability discovery has become largely straightforward.
- Mozilla Firefox's monthly security bug fixes went from roughly 20 in 2025 to 60-70 in February and March and 400 in April, about 20x the prior year's average, with about two-thirds attributed to a frontier model preview.
- Anthropic's scan of over a thousand open source repos surfaced 23,000 candidates, 6,200 rated high or critical, 1,600 reported to maintainers, and about 100 patched upstream.
- Teams converge on a six-step harness: threat model and sandbox as one-time setup per codebase, then a loop of discovery, verification, triage, and patching.
- A well-documented threat model raises true positive rates to around 90% because it supplies the system-level context — compensating controls, internal-only deployment, undocumented on-call fixes — that is nowhere in the code.
- Discovery and verification should be separate agents: a discovery agent that self-critiques may self-censor and hurt recall, while an independent adversarial verifier that never sees the discovery reasoning traces sets a high bar and cuts false positives.
- Giving models dynamic tools (query the API, read logs, read source, detonate proof-of-concept exploits in a sandbox) rather than only static code reading pushed one pentesting team's true positive rate to nearly 100%.
- As models improve, prompts should get shorter and less prescriptive — Yan reports cutting prompt size roughly 50% with each step-jump model version.
- Triage matters because engineer attention is the scarce resource; flooding product engineers with true-but-low-impact findings destroys trust.
- The remaining bottlenecks are organizational — vulnerability routing, severity calibration disagreements between red and blue teams, and patch review bandwidth — and unlike compute they cannot be solved with money.

## Notable Quotes

> "We shared our observation that finding vulnerabilities now is quite straightforward. The bottleneck has now shifted to verification, triage, and patching."
>
> — [3:11](https://www.youtube.com/watch?v=imFedndyXYQ&t=191s) &middot; *The thesis of the entire talk in two sentences.*

> "So what this means is that what's happened in April is 20x of last year's average."
>
> — [1:49](https://www.youtube.com/watch?v=imFedndyXYQ&t=109s) &middot; *The headline number motivating the claim that capability crossed a threshold.*

> "they attributed about twothirds of this to mess preview about 271 which shows that frontier models can help defenders like yourself find and fix vulnerabilities at scale"
>
> — [1:49](https://www.youtube.com/watch?v=imFedndyXYQ&t=109s) &middot; *Attributes the Mozilla spike specifically to a frontier model, not to process change.*

> "from 23,000 candidates uh 6,200 of them were rated as high or critical and at the time of the update 1,600 of them were reported to maintainers and about 100 patch upstream"
>
> — [3:11](https://www.youtube.com/watch?v=imFedndyXYQ&t=191s) &middot; *Concrete funnel numbers from Anthropic's own open source scan, showing the drop-off after discovery.*

> "Early experiments showed that some promise, but the high rates of false positives made it impractical to scale. But the introduction of agentic harnesses that can reliably detect security issues has changed this."
>
> — [3:58](https://www.youtube.com/watch?v=imFedndyXYQ&t=238s) &middot; *Third-party (Mozilla) framing of why harnesses, not just models, changed the economics.*

> "having a well doumented thread model really increases your true positive rate to 90%"
>
> — [5:48](https://www.youtube.com/watch?v=imFedndyXYQ&t=348s) &middot; *Puts a specific number on the payoff of threat-model context.*

> "the model has great context of the code but poor context of the system"
>
> — [5:48](https://www.youtube.com/watch?v=imFedndyXYQ&t=348s) &middot; *A CISO's one-line diagnosis of the core context gap in LLM security work.*

> "the biggest lever we had is having the model test beds essentially sandboxes with live systems and where they can run and detonate the pox to confirm that they are true positives"
>
> — [8:38](https://www.youtube.com/watch?v=imFedndyXYQ&t=518s) &middot; *Names sandboxed exploit detonation as the single highest-leverage investment.*

> "That's what I found with every new model version of StepJum, I actually have to cut my prompt size by maybe about 50%."
>
> — [9:51](https://www.youtube.com/watch?v=imFedndyXYQ&t=591s) &middot; *A counterintuitive, quantified prompt-engineering claim tied to model generations.*

> "for newer models you can just probably say something like look for where untrusted data hits the trust boundary and the model is very good at inferring this"
>
> — [9:51](https://www.youtube.com/watch?v=imFedndyXYQ&t=591s) &middot; *Shows concretely how prescriptive vulnerability-class prompting gives way to abstract instruction.*

> "A lot of times you expect the model to just read the code. That doesn't quite work."
>
> — [10:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=631s) &middot; *Takes a side against static-analysis-style usage of LLMs.*

> "And when they did this, their true positive rate was almost 100%, because the model could actually verify in the loop."
>
> — [10:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=631s) &middot; *Ties tool access directly to a precision outcome.*

> "when the discovery agent is trying to verify its own work in the loop, trying to debate against itself in the loop, it may actually self censor and this may actually hurt recall"
>
> — [11:46](https://www.youtube.com/watch?v=imFedndyXYQ&t=706s) &middot; *The mechanistic argument for separating discovery from verification.*

> "Independent means that the verification agent doesn't see the reasoning traces, doesn't see all the work that the discovery agent has done."
>
> — [11:46](https://www.youtube.com/watch?v=imFedndyXYQ&t=706s) &middot; *Precise, implementable definition of agent independence.*

> "you can lose trust with product engineers by sending them all the vulnerabilities that are true, even those that are medium or low severity because those engineers can't cope. And as we've seen so many times, the scars resource now is engineer attention."
>
> — [13:19](https://www.youtube.com/watch?v=imFedndyXYQ&t=799s) &middot; *Argues triage is a trust problem, not just a ranking problem.*

> "first the original PC has to stop working that's basic second the existing test suite should stay green no regression"
>
> — [15:43](https://www.youtube.com/watch?v=imFedndyXYQ&t=943s) &middot; *Spells out the patch validation ladder in checkable terms.*

> "when you're building the building harnesses, right? You're building loops. They're operational expense, but when you close the loop, they now become capital expense. You get better with each iteration you run."
>
> — [16:50](https://www.youtube.com/watch?v=imFedndyXYQ&t=1010s) &middot; *The opex-to-capex framing is the talk's most portable idea.*

> "non-technical problems are an order of magnitude harder than technical problems"
>
> — [17:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=1051s) &middot; *Sets up the pivot from pipeline design to organizational bottlenecks.*

> "You spend more compute. You pay more money. Things that can be solved with money are not really problems."
>
> — [17:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=1051s) &middot; *Sharp delineation of which scaling problems are actually hard.*

> "But human attention doesn't scale. Your deaf, your product engineers and your security engineers, what if they don't agree on what high severity or uh critical severity is?"
>
> — [18:14](https://www.youtube.com/watch?v=imFedndyXYQ&t=1094s) &middot; *Identifies severity calibration disagreement as a load-bearing organizational failure.*

> "Don't try to aim for automation immediately. Right? Start interactively. Do it hands on the wheel with uh claw code or your favorite ID."
>
> — [20:09](https://www.youtube.com/watch?v=imFedndyXYQ&t=1209s) &middot; *The adoption-path recommendation, stated as a directive.*

## Positions

- Finding vulnerabilities is no longer the bottleneck; verification, triage, and patching are. ([3:11](https://www.youtube.com/watch?v=imFedndyXYQ&t=191s), confidence: stated)
- Models alone are insufficient — it is the combination of model plus agentic harness that produces actionable findings rather than unusable false positive volume. ([3:58](https://www.youtube.com/watch?v=imFedndyXYQ&t=238s), confidence: stated)
- A well-documented threat model raises true positive rates to about 90%, and anything above 75% is a good target. ([5:48](https://www.youtube.com/watch?v=imFedndyXYQ&t=348s), confidence: stated)
- Discovery and verification must be run as separate agents, because a discovery agent verifying its own work self-censors and loses recall. ([11:46](https://www.youtube.com/watch?v=imFedndyXYQ&t=706s), confidence: stated)
- The verification agent should be denied access to the discovery agent's reasoning traces and should assume the vulnerability is false by default. ([12:27](https://www.youtube.com/watch?v=imFedndyXYQ&t=747s), confidence: stated)
- Prompts should shrink and become less prescriptive as models improve — roughly 50% reduction per step-jump model version. ([9:51](https://www.youtube.com/watch?v=imFedndyXYQ&t=591s), confidence: stated)
- Giving the model dynamic tools (API queries, logs, source) rather than code alone raises true positive rate to nearly 100%. ([10:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=631s), confidence: stated)
- Sending product engineers all true findings, including medium and low severity, destroys trust and should be avoided in favor of a curated top 10-20. ([13:19](https://www.youtube.com/watch?v=imFedndyXYQ&t=799s), confidence: stated)
- Severity ratings produced by a model are unreliable without business context, and human review should be expected to move findings in both directions. ([14:34](https://www.youtube.com/watch?v=imFedndyXYQ&t=874s), confidence: stated)
- Fully automated patch review for security issues is not yet practiced at most companies; a human should confirm patches before merge. ([18:53](https://www.youtube.com/watch?v=imFedndyXYQ&t=1133s), confidence: stated)
- Scaling the scanning harness is a solved problem because it only costs compute and money; the unsolved constraints are human and organizational. ([17:31](https://www.youtube.com/watch?v=imFedndyXYQ&t=1051s), confidence: stated)
- Teams should start interactively and hands-on rather than aiming for full automation immediately. ([20:09](https://www.youtube.com/watch?v=imFedndyXYQ&t=1209s), confidence: stated)
- Vulnerability routing at scale can be solved with simple code-owner heuristics and does not require an LLM in the loop. ([18:53](https://www.youtube.com/watch?v=imFedndyXYQ&t=1133s), confidence: stated)
- The discovery-verification-triage-patching loop is structurally an ML pipeline: recall, precision, ranking, and closing the loop. ([16:50](https://www.youtube.com/watch?v=imFedndyXYQ&t=1010s), confidence: stated)

## Concepts

- [adversarial agent supervision](../concepts/adversarial-agent-supervision.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [ai-assisted vulnerability discovery](../concepts/ai-assisted-vulnerability-discovery.md)
- [context engineering](../concepts/context-engineering.md)
- [legacy code migration](../concepts/legacy-code-migration.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [retrieval evaluation](../concepts/retrieval-evaluation.md)

