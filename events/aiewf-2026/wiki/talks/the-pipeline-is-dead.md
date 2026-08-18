---
title: "The Pipeline Is Dead"
type: "talk"
slug: "the-pipeline-is-dead"
track: "Data Quality"
org: "Sky Valley Ambient Computing"
day: "Day 2 — Session Day 1"
room: "Track 9"
video_id: "bRnoEpoK5m4"
duration_sec: 1189
word_count: 2788
speakers: ["Varun Singh"]
---

# The Pipeline Is Dead

*Program title: The Base Model is Dead*

**Speakers:** [Varun Singh](../speakers/varun-singh.md)

**Org:** Sky Valley Ambient Computing

**Track:** Data Quality &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Track 9 &nbsp;|&nbsp; **Duration:** 19m 49s

[Watch on YouTube](https://www.youtube.com/watch?v=bRnoEpoK5m4)

## Summary

Iris ten Teije argues that the entire software distribution stack — CI, registries, container images, app store review — exists to solve one problem (move a frozen artifact from build machine to run machine) and that the constraint behind it has evaporated. Producing a correct, scoped change used to be expensive and rare, which forced one frozen version for everyone; with coding agents, change production is collapsing toward zero cost and can happen at runtime in the user's own session. Her company Differ bets on replacing the single artifact with a canonical 'stem' plus per-user divergences that are bounded, immutable, inspectable, and individually reversible, with developer-set boundaries around things like auth and payments. She takes the standard CTO objection head-on — 'you want me to run millions of AI-generated code bases?' — and answers that brittleness comes from tangled artifacts without boundaries, not from generation itself. Worth watching for the framing and for her honest list of unsolved hard parts: lineage as a graph query, testing every possible divergence, measuring desirability rather than correctness, autonomy-versus-control, and propagating updates by merging intent rather than code.

## Key Points

- The one-way build-and-ship pipeline was never a considered design decision; it was the direct consequence of software production being expensive, skilled, and rare, so the artifact was frozen once and shipped to everyone.
- Every production guarantee engineers rely on — reproducibility, previewability, rollback — flows from the single fact that there is one artifact that does not change after shipping, which is exactly the assumption adaptive software removes.
- Demand for personalized software is not new: professional services and forward-deployed engineers, developer dotfiles and editor configs, and Excel as a substrate for millions of user-built programs are all decades-old evidence that people customize when they can afford to.
- Prior attempts at divergence — feature flags, segmentation, A/B testing — forced software into predeclared buckets and segments rather than allowing genuine per-user adaptation.
- Differ's proposed architecture is one canonical stem plus per-user divergences that are bounded, isolated, immutable, and individually reversible, so a change's blast radius is a single user context and rollback requires no deploy.
- Developers retain explicit control surfaces: they mark what can and cannot be adapted, so form fields can be reordered for conversion while auth and payments stay off limits.
- The hard problems are not generation but lineage/provenance (answering 'what is this user running and why' as a graph query), correctness testing across the stem and all divergences, and desirability — knowing whether a correct change was actually an uplift on retention, churn, or support tickets.
- For coordination across a million versions, the answer is to merge intent and outcome rather than code, so users converge on the same goal via different paths; the speaker frames generation as the easy 80% and observability/validation/coordination as the actual business.

## Notable Quotes

> "So, the one-way pipeline is not arbitrary. It's the direct consequence of production of software being expensive and risky."
>
> — [1:25](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=85s) &middot; *states the core causal claim the whole talk rests on*

> "And every guarantee that we lean on in production flows from one fact. There is one artifact and it doesn't change after we ship it."
>
> — [2:13](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=133s) &middot; *names precisely what is being given up*

> "We call it reliability. But the price was that the software couldn't really be for anyone in particular."
>
> — [2:13](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=133s) &middot; *sharp statement of the tradeoff being reversed*

> "But it was never really a fact about software. It was a fact about cost and budget and the economics and that cost just changed."
>
> — [3:04](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=184s) &middot; *the pivot from historical description to argument*

> "The cost of producing a correct and scope change is collapsing towards zero and just as importantly the production of the software no longer has to happen in one place up front before anyone runs it."
>
> — [3:47](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=227s) &middot; *the two-part premise, including the underrated location claim*

> "But now as making a change becomes as cheap as running one and it can happen in the same place as um as where you run it, the reason to separate them is dissolving."
>
> — [4:33](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=273s) &middot; *collapses development and distribution into one thing*

> "and it's not that smaller customers can't benefit from this type of customization. It just didn't make sense financially until today."
>
> — [5:19](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=319s) &middot; *reframes forward-deployed engineering as a cost artifact, not a segment*

> "And lastly, Excel, the most successful business software ever created. And Excel isn't really a static program. It's millions of people that all build their own programs on top of it."
>
> — [6:12](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=372s) &middot; *the strongest existing-proof example for per-user software*

> "Give people the power to make software to make their software theirs, and they take it."
>
> — [6:12](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=372s) &middot; *compact statement of the demand-side thesis*

> "But we go forced into a specific shape, that of creating buckets and segments that you declare in advance. And now, for the first time, we can make software truly adaptive."
>
> — [7:08](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=428s) &middot; *distinguishes adaptive software from feature flags and A/B testing*

> "when the agent is the runtime, when the thing that runs your software can also modify it, development and distribution stop being two phases."
>
> — [7:08](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=428s) &middot; *the title claim, stated directly*

> "instead of one code base gated by flags and shipped to everyone, you deploy one canonical stem and every user runs her own divergence of it. Same origin, but individually adapted live."
>
> — [7:56](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=476s) &middot; *the concrete architecture being proposed*

> "I can already barely reason about one AI-generated code base. And you want me to run millions of these? You're not describing a capability. You're describing my worst problem multiplied."
>
> — [8:51](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=531s) &middot; *the strongest objection, quoted from a skeptical CTO*

> "The brittleness that you're picturing is a specific type of failure mode. It's unmanaged divergence inside a single artifact."
>
> — [8:51](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=531s) &middot; *her rebuttal locates brittleness in structure, not in AI generation*

> "Which means that the blast radius of a changes in the system is one context. And any single divergence can roll back life with no deploy."
>
> — [9:40](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=580s) &middot; *the safety property the architecture is meant to buy*

> "Because anyone can make a code change now, but the hard part is knowing whether you actually found an improvement, an uplift."
>
> — [14:37](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=877s) &middot; *names desirability as distinct from correctness*

> "So, for us, the challenge isn't building more control. It's winning enough trust that you don't have to."
>
> — [16:20](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=980s) &middot; *takes an explicit side on autonomy versus human-in-the-loop*

> "the answer that we keep coming back to is don't merge code, merge intent, merge outcome."
>
> — [17:11](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=1031s) &middot; *the most quotable proposed solution to coordination*

> "Generation has become easy, and I would say that's actually the easy 80%. Calling a model to write some code is something that everyone can do."
>
> — [17:11](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=1031s) &middot; *puts a number on where the difficulty actually sits*

> "We spent 20 years getting good at shipping one version for everyone. The next 20 years are about shipping the right version to anyone with the isolation and provenance that makes it safe instead of terrifying."
>
> — [19:07](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=1147s) &middot; *the closing thesis in one line*

## Positions

- The one-version-for-everyone model was never chosen on merit; it was the only economically viable shape given the cost of producing a correct change. ([3:04](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=184s), confidence: stated)
- The cost of producing a correct, scoped code change is collapsing toward zero, and production no longer has to happen in one place before anyone runs the software. ([3:47](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=227s), confidence: stated)
- Brittleness in AI-generated systems comes from unmanaged divergence inside a single tangled artifact with no boundaries, not from the code being AI-generated. ([8:51](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=531s), confidence: stated)
- A stem-plus-bounded-divergences architecture limits the blast radius of any change to a single user context and makes rollback possible without a deploy. ([9:40](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=580s), confidence: stated)
- Developers should be able to declare regions like auth and payments permanently off limits to adaptation, while other regions such as form layout stay adaptable. ([10:25](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=625s), confidence: stated)
- Adaptive software lets a horizontal SaaS product serve a much wider set of customer personas without increasing R&D spend. ([12:55](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=775s), confidence: stated)
- With no single artifact, identifying what a user is running becomes a graph query over immutable divergences rather than a version number lookup. ([13:42](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=822s), confidence: stated)
- The recommendations-only, never-autonomous approach is defensible but is the wrong long-term target; the goal should be earning enough trust that humans choose to step back. ([16:20](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=980s), confidence: stated)
- Updates should propagate by merging intent and outcome rather than code, so users converge on shared goals without running the same commit. ([17:11](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=1031s), confidence: stated)
- Code generation is roughly the easy 80% of the problem; observability, validation, provenance, and coordination are where the durable business value lies. ([17:54](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=1074s), confidence: stated)
- Existing personalization infrastructure — feature flags, segmentation, A/B testing — is fundamentally limited because segments must be declared in advance. ([7:08](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=428s), confidence: stated)
- Measuring whether an adaptation is desirable requires tying it to company-specific goal metrics like retention, churn, or support ticket volume, and correctness testing alone is insufficient. ([15:32](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=932s), confidence: implied)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [continual learning](../concepts/continual-learning.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [forward deployed engineering](../concepts/forward-deployed-engineering.md)
- [generative ui](../concepts/generative-ui.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)

