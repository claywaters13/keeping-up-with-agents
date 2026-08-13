---
title: "The AI bugpocalypse is here. Now what?"
type: "talk"
slug: "the-ai-bugpocalypse-is-here-now-what"
org: "Corridor"
video_id: "7JgIS42mz7U"
duration_sec: 1183
word_count: 3223
speakers: ["Jack Cable"]
---

# The AI bugpocalypse is here. Now what?

**Speakers:** [Jack Cable](../speakers/jack-cable.md)

**Org:** Corridor

**Duration:** 19m 43s

[Watch on YouTube](https://www.youtube.com/watch?v=7JgIS42mz7U)

## Summary

Jack Cable, co-founder/CEO of Corridor and a former CISA senior technical advisor, argues that frontier models are simultaneously making vulnerability discovery/exploitation cheap and making vulnerable code far more plentiful, producing what he calls an 'AI bugpocalypse.' His central claim is optimistic, though: almost nothing the models find is a novel vulnerability class, so the winning defensive move is systemic hardening (memory-safe rewrites, secure-by-design guarantees) rather than millions spent on one-off patching. He backs this with CISA/MITRE data, the 60–70% memory-safety figure, and Google's Android numbers showing memory-safety bugs falling from ~75% (2019) to ~30% (2022) just by writing new code in safe languages. He also stakes out policy positions: export controls on frontier security-capable models should be lifted because the defender benefit outweighs the risk, and the US needs frontier open-weight models. Worth watching if you care about AI-assisted code security, secure-by-design policy, or how security tooling should sit in an agentic development pipeline.

## Key Points

- Both sides of the equation are shifting at once: frontier models are getting better at finding and exploiting vulnerabilities while AI-written code massively expands the attack surface.
- Essentially all vulnerabilities frontier models are finding belong to well-known classes documented for decades, which means known systemic mitigations still apply.
- Memory-safe languages can eliminate roughly 60–70% of vulnerabilities in products currently written in memory-unsafe languages, and Android's data shows the effect is real even without rewriting old code.
- Cable argues defenders should prefer one-time rewrites of critical open-source libraries into languages like Rust over perpetual whack-a-mole patching, because programmatic guarantees hold even as models get smarter.
- Models still introduce vulnerabilities 20–40% of the time per BaxBench (ETH Zurich / UC Berkeley), largely because security is contextual and models lack a company's business logic and threat model.
- The vulnerabilities Corridor sees in customer code are shifting from one-liner bugs toward contextual issues like authorization flaws that require business-logic understanding.
- Corridor's bet is that within 6–12 months most shipped code will be reviewed by AI rather than humans, since human code review has become the bottleneck.
- Security tooling must enable rather than block acceleration: the question for security teams is not whether to allow coding agents but what guardrails make autonomous merging acceptable.
- On policy, Cable urged the White House to lift export controls on frontier models and testified to Congress recommending prevention in new code, hardening the open-source foundation, and fostering American open-weight models.

## Notable Quotes

> "AI coding tools are scaling faster than any software category in history"
>
> — [1:26](https://www.youtube.com/watch?v=7JgIS42mz7U&t=86s) &middot; *Frames the scale premise the whole talk rests on.*

> "about 84% of developers were using AI coding tools, 30 to 40% of companies encouraging use of AI coding assistants"
>
> — [2:10](https://www.youtube.com/watch?v=7JgIS42mz7U&t=130s) &middot; *Concrete adoption baseline from Stack Overflow data.*

> "a lot of the vulnerabilities, pretty much all of the vulnerabilities that even frontier AI models are finding aren't anything new"
>
> — [4:57](https://www.youtube.com/watch?v=7JgIS42mz7U&t=297s) &middot; *The core optimistic claim that makes systemic defense viable.*

> "While it's true that it's hard to build a perfectly secure system, we do know how to build systems that are fundamentally more resilient to common classes of vulnerabilities."
>
> — [6:28](https://www.youtube.com/watch?v=7JgIS42mz7U&t=388s) &middot; *Crisp statement of the secure-by-design thesis.*

> "approximately 60 to 70% of vulnerabilities in products written in memory unsafe languages can be completely prevented using memory safe languages"
>
> — [8:02](https://www.youtube.com/watch?v=7JgIS42mz7U&t=482s) &middot; *Headline quantitative claim behind the rewrite argument.*

> "the percent of memory safety vulnerabilities has dropped quite dramatically from you know about 75% in 2019 to maybe 30% in 2022"
>
> — [8:51](https://www.youtube.com/watch?v=7JgIS42mz7U&t=531s) &middot; *Empirical evidence from Android that the mitigation works in practice.*

> "we could pour millions of dollars into essentially playing whack-a-mole with vulnerabilities and patching them one-off in some of the open-source libraries that we all rely on, or we could do a one-time rewrite, for instance, to move some of these critical libraries into a language like Rust"
>
> — [9:41](https://www.youtube.com/watch?v=7JgIS42mz7U&t=581s) &middot; *States the central resource-allocation tradeoff he wants the field to make.*

> "even the best models introduce vulnerabilities about 20 to 40% of the time when writing code"
>
> — [10:41](https://www.youtube.com/watch?v=7JgIS42mz7U&t=641s) &middot; *Benchmark number quantifying AI-introduced risk.*

> "while the models are very smart and capable, often times security is very contextual. And the model just might not have the context in order to know that it's introducing a vulnerability"
>
> — [10:41](https://www.youtube.com/watch?v=7JgIS42mz7U&t=641s) &middot; *Explains why raw model intelligence doesn't solve secure coding.*

> "the vulnerabilities being introduced are often and less so the basic one-liner vulnerabilities, and more so contextual issues"
>
> — [11:37](https://www.youtube.com/watch?v=7JgIS42mz7U&t=697s) &middot; *Field observation on how the bug mix is shifting under AI authorship.*

> "within the next 6 to 12 months, the majority of code that is being shipped will be reviewed uh not by human but by AI"
>
> — [13:14](https://www.youtube.com/watch?v=7JgIS42mz7U&t=794s) &middot; *A dated, falsifiable prediction others would dispute.*

> "given that code review is not is now the bottleneck and I don't think we're going to accept that for very long"
>
> — [13:14](https://www.youtube.com/watch?v=7JgIS42mz7U&t=794s) &middot; *Names the specific constraint driving AI review adoption.*

> "security cannot be the blocker when it comes to companies accelerating their development"
>
> — [13:51](https://www.youtube.com/watch?v=7JgIS42mz7U&t=831s) &middot; *His governing principle for how security tooling should be positioned.*

> "the conversation is less around should you allow your, you know, development teams access to coding agents? The answer is obviously yes, right? It's more around how can you do that with guardrails in place"
>
> — [13:51](https://www.youtube.com/watch?v=7JgIS42mz7U&t=831s) &middot; *Reframes the security team's decision from permission to guardrails.*

> "we urged the White House to lift the export controls on these models. And the perspective there is that the benefit to defenders far outweighs the risk"
>
> — [14:49](https://www.youtube.com/watch?v=7JgIS42mz7U&t=889s) &middot; *Explicit, contestable policy position.*

> "whether we like it or not, right, adversaries already have access to incredibly powerful models um and they're already using them today to exploit systems"
>
> — [15:45](https://www.youtube.com/watch?v=7JgIS42mz7U&t=945s) &middot; *The premise underpinning his anti-export-control argument.*

> "open-source software is going to be the kind of proving ground for a lot of adversaries"
>
> — [16:37](https://www.youtube.com/watch?v=7JgIS42mz7U&t=997s) &middot; *Identifies where he expects AI-driven exploitation to concentrate.*

> "for many companies, while there's a place for for closed-weight models, you also might want to do things like fine-tuning models. Um and that is only possible with an open-weight model."
>
> — [18:09](https://www.youtube.com/watch?v=7JgIS42mz7U&t=1089s) &middot; *Practical justification for his open-weight competitiveness recommendation.*

## Positions

- Essentially all vulnerabilities frontier AI models are currently discovering belong to already-known vulnerability classes, not novel ones. ([4:57](https://www.youtube.com/watch?v=7JgIS42mz7U&t=297s), confidence: stated)
- Roughly 60–70% of vulnerabilities in memory-unsafe products would be completely prevented by memory-safe languages. ([8:02](https://www.youtube.com/watch?v=7JgIS42mz7U&t=482s), confidence: stated)
- One-time rewrites of critical libraries into memory-safe languages are a better use of defensive resources than one-off vulnerability patching. ([9:41](https://www.youtube.com/watch?v=7JgIS42mz7U&t=581s), confidence: stated)
- Even the best models introduce vulnerabilities in 20–40% of code-writing tasks, per the BaxBench benchmark. ([10:41](https://www.youtube.com/watch?v=7JgIS42mz7U&t=641s), confidence: stated)
- High model intelligence does not fix secure coding because security is contextual and models lack proprietary business logic and threat models. ([11:37](https://www.youtube.com/watch?v=7JgIS42mz7U&t=697s), confidence: stated)
- Within 6–12 months, the majority of shipped code will be reviewed by AI rather than by humans. ([13:14](https://www.youtube.com/watch?v=7JgIS42mz7U&t=794s), confidence: stated)
- Development acceleration will always win over security friction, so security must operate as guardrails rather than as a gate. ([13:51](https://www.youtube.com/watch?v=7JgIS42mz7U&t=831s), confidence: stated)
- Export controls on frontier security-capable models should be lifted because the defender benefit outweighs the adversary risk. ([14:49](https://www.youtube.com/watch?v=7JgIS42mz7U&t=889s), confidence: stated)
- Distillation from closed-weight models is shrinking the lag before open-weight models reach frontier capability, so adversaries already have powerful models regardless of controls. ([15:45](https://www.youtube.com/watch?v=7JgIS42mz7U&t=945s), confidence: stated)
- The United States needs domestically produced frontier open-weight models to remain competitive in AI. ([18:09](https://www.youtube.com/watch?v=7JgIS42mz7U&t=1089s), confidence: stated)
- Companies should allow developers to use coding agents; the only real question is what guardrails accompany that access. ([13:51](https://www.youtube.com/watch?v=7JgIS42mz7U&t=831s), confidence: implied)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [ai-assisted vulnerability discovery](../concepts/ai-assisted-vulnerability-discovery.md)
- [model portability](../concepts/model-portability.md)
- [secure code generation](../concepts/secure-code-generation.md)
- [software supply chain security](../concepts/software-supply-chain-security.md)
- [sovereign and air-gapped deployment](../concepts/sovereign-and-air-gapped-deployment.md)

