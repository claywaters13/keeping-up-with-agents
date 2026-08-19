---
title: "Fun Is Velocity"
type: "talk"
slug: "fun-is-velocity"
org: "OpenClaw (nonprofit foundation); also works at OpenAI"
video_id: "whcfSGN6CAU"
duration_sec: 2513
word_count: 6077
speakers: ["Peter Steinberger"]
---

# Fun Is Velocity

**Speakers:** [Peter Steinberger](../speakers/peter-steinberger.md)

**Org:** OpenClaw (nonprofit foundation); also works at OpenAI

**Duration:** 41m 53s

[Watch on YouTube](https://www.youtube.com/watch?v=whcfSGN6CAU)

## Summary

Peter Steinberger tells the eight-month story of OpenClaw — from a WhatsApp relay he vibe-coded because he was annoyed and hungry, to a viral open-source agent project with 111,000 issues and PRs, a nonprofit, and a press cycle that declared it dead and then watched it hit record downloads. Structured as five questions he gets asked (why so fast, did you sell out, did the competition win, is it still fun, what's next), the talk is unusually candid about what went wrong: 9,500 config options, months lost to aggressive security researchers, over-optimizing the harness for one lab's model, and a stretch where he stopped using his own product. His thesis is that enjoyment is not a perk but a throughput metric — 'the weeks I enjoyed building, the product got visibly better' — and that in an era where anyone can prompt a product into existence, distribution and personal brand, not code, are the binding constraint. Worth watching for founders weighing open source, for anyone maintaining a project that got popular faster than it got good, and for a practitioner's view of where agent tooling still breaks.

## Key Points

- Product-market fit showed up as emotional reaction, not metrics: every friend he demoed the WhatsApp relay to was amazed, scared, or angry at being told it wasn't ready for them, which he read as the clearest possible signal.
- Feature velocity is cheap and maintenance is not — every feature shipped with a config option to avoid breaking existing setups, compounding to roughly 9,500 configuration options whose permutations are impossible to test.
- Building your harness around a single provider's model is a business risk: he optimized OpenClaw for Opus and got ~24 hours' notice that subscription access would be disabled, with no time to change course.
- The security-report flood was mostly noise — press claimed 20% of skills were malicious, his own scan of all 67,000 put it at 0.3% — and he says he should have published a clear security boundary instead of trying to fix everything.
- Hype is uncontrollable and non-monotonic: downloads bottomed at ~835,000 weekly in May, then peaked at 4.7 million after the project was declared dead in June.
- Fun is a leading indicator of output, not a reward for it; when the project became responsibility rather than something he used daily, quality dropped and he shipped config options instead of improvements.
- His working practice has shifted from managing sessions carefully to demanding proactive agent output: he wants fully reviewed and tested PRs with screenshots, not feature ideas or issue lists, so most bad ideas die before reaching him.
- He treats code review as risk management rather than line-by-line reading — closer attention for scary systems, a glance for UI — and uses elapsed time as a signal that something went wrong.
- The hardest problem for a new startup is no longer tech or people but attention, which is why he advises building your personal brand before you need it and picking problems in the 'hard and boring' category.

## Notable Quotes

> "it might be eight months in in human time, but in AI times it's it's more like four years."
>
> — [1:03](https://www.youtube.com/watch?v=whcfSGN6CAU&t=63s) &middot; *Frames the whole talk's compressed timeline in one line.*

> "everything you can build can be forked or cloned, but your name cannot. So your personal brand is way more important than any single product"
>
> — [12:48](https://www.youtube.com/watch?v=whcfSGN6CAU&t=768s) &middot; *His central strategic claim about what actually compounds in an era of cheap software.*

> "the press say 20% of our skills are malicious. Now we actually put a paper up with this. We did the the numbers and the numbers are more like 0.3%. We scanned all 67,000."
>
> — [13:38](https://www.youtube.com/watch?v=whcfSGN6CAU&t=818s) &middot; *A hard number correcting a widely repeated claim about agent skill security.*

> "but you know a correction never travels as far as a scare."
>
> — [13:38](https://www.youtube.com/watch?v=whcfSGN6CAU&t=818s) &middot; *Compact statement about the asymmetry of security press coverage.*

> "At our highest, I had to count that we ended up with around nine and a half thousand configuration options."
>
> — [16:14](https://www.youtube.com/watch?v=whcfSGN6CAU&t=974s) &middot; *The concrete cost of shipping every feature behind a flag.*

> "It is infinitely harder to evolve software that has users."
>
> — [17:01](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1021s) &middot; *The tradeoff that separates prototype velocity from maintained-product velocity.*

> "So when they ping me with around 24 hours notice that they're going to disable the subscription for everyone there was not really enough time to change course."
>
> — [17:56](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1076s) &middot; *Names the single external event that most damaged the project.*

> "So maybe write this one down. Your dependencies business model is your business model."
>
> — [17:56](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1076s) &middot; *The generalizable lesson from the model-provider dependency.*

> "We bottomed out at around 835,000 weekly downloads in May. And then after being declared death in in June, we peaked at 4.7 million, the highest ever."
>
> — [18:49](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1129s) &middot; *Reported numbers that contradict the 'killed by competitors' narrative.*

> "A hype is like the weather. You might see it coming, but you can't control it."
>
> — [18:49](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1129s) &middot; *His position that virality is not a strategy input.*

> "Somewhere in that time I stopped making a product I love and I worked on making something for everyone."
>
> — [19:40](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1180s) &middot; *Diagnoses the failure mode behind the fun-is-velocity thesis.*

> "It's hard to compete with someone who's just there having fun."
>
> — [22:03](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1323s) &middot; *The competitive framing of enjoyment against VC-funded rivals.*

> "Fun is velocity. The weeks I enjoyed building, the product got visibly better."
>
> — [22:53](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1373s) &middot; *The thesis stated outright with its evidence attached.*

> "Every lab will sell you an agent. Open claw is the alternative. Open source runs everywhere, works with any model. And if you run local models, your data never has to leave your device."
>
> — [24:52](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1492s) &middot; *The clearest statement of the project's positioning against lab-owned agents.*

> "when I shift my attention to something I don't want to read issues I want to see fully reviewed and tested PRs"
>
> — [27:24](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1644s) &middot; *Describes how agent capability changes what a maintainer should accept as input.*

> "I think that was really early in in deciding that I don't read all the code. I see code review more as a as risk management."
>
> — [31:05](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1865s) &middot; *A specific, contested engineering stance on reviewing agent-written code.*

> "User number one should be you. And my users two to 20 were friends."
>
> — [31:58](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1918s) &middot; *His concrete answer to the prototype-to-first-users question.*

> "I would be less stressed out about security researchers. They are really good at making you feel really bad."
>
> — [33:24](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2004s) &middot; *His single biggest regret, stated bluntly.*

> "And most of them really sent reports that their agent produced without actually even testing it."
>
> — [34:08](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2048s) &middot; *Reports a specific pattern of agent-generated security noise in open source.*

> "when you merge this feature it really means here's this pile of code that I don't that the person probably doesn't really understand that I don't fully understand"
>
> — [36:25](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2185s) &middot; *Why saying no to popular PRs is a maintainership skill.*

> "I mean, honestly, that's not so much a tech problem. It's more a token problem where we could do that today, but you wouldn't get very far with your subscription"
>
> — [37:22](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2242s) &middot; *Locates the always-on agent bottleneck in economics rather than capability.*

> "in this day and age there's so much noise out there that your hardest problem is not the tech, it's not the software, not even the people. The hardest problem now is like getting eyeballs."
>
> — [40:01](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2401s) &middot; *His answer for how to approach a startup now, and the reason for the brand advice.*

> "Maybe I would pick something again that's that's in the category hard and boring because that's usually a category that is a little bit easier to actually find people that will appreciate when you solved something."
>
> — [40:01](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2401s) &middot; *Contrarian idea-selection advice for a world where fun things get cloned instantly.*

## Positions

- Enjoyment of the work is a direct driver of shipping speed and product quality — the weeks he enjoyed building, the product visibly improved; the weeks he didn't, he shipped config options. ([22:53](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1373s), confidence: stated)
- A personal brand is more durable than any product, because products can be forked or cloned and a name cannot; founders should build it before they need it. ([12:48](https://www.youtube.com/watch?v=whcfSGN6CAU&t=768s), confidence: stated)
- Strong emotional reactions from early testers — including anger at being excluded — are a valid signal of product-market fit. ([4:55](https://www.youtube.com/watch?v=whcfSGN6CAU&t=295s), confidence: stated)
- The claim that 20% of OpenClaw skills are malicious is wrong; a scan of all 67,000 put the figure at about 0.3%. ([13:38](https://www.youtube.com/watch?v=whcfSGN6CAU&t=818s), confidence: stated)
- Your dependency's business model is your business model — over-optimizing a harness for one lab's model left the project exposed when access was cut with ~24 hours' notice. ([17:56](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1076s), confidence: stated)
- Adding a config option for every feature to avoid breaking users is a trap; the permutations (~9,500 options) make comprehensive testing impossible. ([17:01](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1021s), confidence: stated)
- Maintainers should publish an explicit security boundary declaring what is guaranteed and what will not be fixed, rather than trying to satisfy every reporter. ([34:08](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2048s), confidence: stated)
- Reading every line of agent-written code is not required; review effort should be allocated by risk, with elapsed time serving as an anomaly signal. ([31:05](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1865s), confidence: stated)
- Reviewing all code is still appropriate in a company setting even if it isn't for his solo open-source work — the risk calculus differs. ([39:19](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2359s), confidence: stated)
- Loops, graphs, and workflows are not a new paradigm — they are the same trigger-input-decision automation engineers have always built. ([28:47](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1727s), confidence: stated)
- Models are now good enough that multi-sub-agent stress testing and code review can substitute for most manual QA, though some manual clickthrough remains necessary to judge feel. ([29:31](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1771s), confidence: stated)
- Always-on proactive agents are blocked by token cost and cache-invalidating heartbeat design, not by model capability. ([37:22](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2242s), confidence: stated)
- Managing compute across machines is the biggest bottleneck in agent infrastructure today, and tooling for non-Linux environments (especially macOS) is essentially absent. ([34:52](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2092s), confidence: stated)
- Getting attention, not building software, is the hardest problem for a new startup now, which argues for picking 'hard and boring' problems over fun ones. ([40:55](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2455s), confidence: stated)
- Engineers should stop bringing feature ideas to a maintainer and instead bring a built, screenshotted, testable implementation produced with an agent. ([28:08](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1688s), confidence: stated)
- Open source agents are the necessary alternative to lab-owned agents because they run anywhere, work with any model, and can keep data local. ([24:52](https://www.youtube.com/watch?v=whcfSGN6CAU&t=1492s), confidence: stated)
- Merging a popular community PR imports code nobody fully understands, which is why saying no more often is correct; he says he didn't say no enough. ([36:25](https://www.youtube.com/watch?v=whcfSGN6CAU&t=2185s), confidence: stated)

## Concepts

- [agent configuration files](../concepts/agent-configuration-files.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [founder audience building](../concepts/founder-audience-building.md)
- [founder psychology](../concepts/founder-psychology.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [open source ai strategy](../concepts/open-source-ai-strategy.md)
- [personal ai agents](../concepts/personal-ai-agents.md)
- [platform dependency risk](../concepts/platform-dependency-risk.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)

