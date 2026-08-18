---
title: "Build for the Memo, Not the Demo"
type: "talk"
slug: "build-for-the-memo-not-the-demo"
track: "AI in Finance"
org: "China Resources Holdings"
day: "Day 4 — Session Day 3"
room: "Track 3"
video_id: "tJFjeMBKbIY"
duration_sec: 1462
word_count: 2561
speakers: ["Shawn Chan"]
---

# Build for the Memo, Not the Demo

*Program title: Build for the Memo, Not the Demo — Notes from 200 Investment Committees*

**Speakers:** [Shawn Chan](../speakers/shawn-chan.md)

**Org:** China Resources Holdings

**Track:** AI in Finance &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 24m 22s

[Watch on YouTube](https://www.youtube.com/watch?v=tJFjeMBKbIY)

## Summary

Shawn Chan, a cross-border dealmaker who has sat in roughly 200 investment committee meetings, argues that almost every AI product in finance is engineered to impress a room for five minutes rather than to survive a room whose job is to not be impressed. He draws a hard line between a 'demo' (one clean document in, one fluent answer out) and a 'memo' (hundreds of conflicting sources that must withstand argument before real money moves), then walks through six recurring ways AI systems break trust: flat source hierarchies, internally inconsistent numbers, smoothed-over contradictions, guesses dressed as facts, unverifiable claims, and no accountable human signature. Each failure mode is anchored to a real incident — the 2023 chatbot demo error tied to an ~8% stock drop, the algorithmic homebuying write-off, the New York lawyer's fabricated citations, the airline chatbot tribunal case. His prescribed fixes are deliberately unglamorous: per-claim receipts with source trust levels, visual fact/guess separation, automated numeric reconciliation, contradiction surfacing, and a logged human approval gate. He closes by noting the same discipline applies to founders raising money, because a pitch deck also becomes someone's internal memo. Worth watching if you build AI for regulated, high-stakes document work and want the buyer's-side view of why demos don't convert.

## Key Points

- The distinction that organizes the talk is demo vs. memo: a demo produces one fluent answer from one clean document, while a memo must reconcile hundreds of disagreeing sources and survive hostile questioning before capital moves.
- Retrieval systems typically treat all sources as equally credible, but an audited filing, an analyst note, and a group-chat guess carry radically different trust levels, and Chan describes a tool that preferred a texted estimate over the real audit number three rows away.
- Internal numeric inconsistency kills a memo not because the discrepancy matters but because of what it implies: if the author missed easy arithmetic, reviewers assume the hard analysis is worse.
- Contradictions between sources are the most valuable signal in diligence, but fluency-optimized models silently pick the nicer-reading version; the builder's job is to force the disagreement in front of a human rather than resolve it invisibly.
- Facts and estimates must stay visually separated, because a guess in fact-shaped language ('will likely receive approval next quarter') hardens into an assumed fact across successive drafts.
- Provenance must be a one-click, 30-second verification to the exact source paragraph; Chan calls the click-through the actual product and everything else packaging.
- Accountability cannot be delegated to software — the airline that argued its chatbot was a separate legal entity lost, and an architecture without a named human signer is 'an excuse generator.'
- Chan's five vendor requirements are all plumbing and honesty problems rather than model-capability problems: per-claim receipts, fact/guess separation, automatic numeric agreement, contradiction surfacing, and a logged human approval gate.
- The same scrutiny applies to fundraising: after a pitch, someone writes an internal memo checking every spoken number against the data room, so the discipline that fixes the product is the discipline that wins the check.

## Notable Quotes

> "The problem is being sure of yourself and being right are two different skills."
>
> — [1:11](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=71s) &middot; *Compresses the talk's central critique of fluent AI into one line.*

> "First, almost every AI finance product is built to impress people for five minutes, and almost none are built to survive a room whose entire job is to not be impressed."
>
> — [2:05](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=125s) &middot; *The thesis statement, framed from the buyer's side of the table.*

> "Money doesn't follow intelligence. Money follows trust, and the trust is fragile, especially when the thing that wrote the page has never once in its entire life said the words, "I'm not sure.""
>
> — [4:08](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=248s) &middot; *States the position that capability is not the bottleneck — calibration is.*

> "That's roughly $100 billion of value gone because of unchecked sentence. $100 billion for one sentence."
>
> — [8:02](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=482s) &middot; *Puts a concrete number on the cost of a single unverified claim.*

> "The moment real money is watching and the real money is always watching. Every sentence become a memo sentence. There is no safe demo anymore."
>
> — [8:02](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=482s) &middot; *Collapses his own demo/memo distinction into a stronger claim: there is no low-stakes output.*

> "If your system can can't tell an accountant under oath from a rumor in a group chat, it it is not ready for real money."
>
> — [10:16](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=616s) &middot; *Names source-tiering as a hard gate for production deployment.*

> "nobody in the room cares about the missing 0.6. They care about what it what it means if this person didn't check the easy mathematics what did they not check on the hard stuff"
>
> — [11:12](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=672s) &middot; *Explains why small inconsistencies are read as evidence about unseen work.*

> "The company ended up writing off around half a billion dollars shut the whole unit down and let a quarter of the staff go. The model wasn't stupid the model was unsupervised"
>
> — [12:27](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=747s) &middot; *Reports a large loss and attributes it to missing supervision rather than model quality.*

> "A contradiction is not a bug a contradiction is a gift."
>
> — [12:27](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=747s) &middot; *Inverts the usual product instinct to smooth over conflicting retrieval results.*

> "We caught it because one person happened to have both documents open at once. Pure luck. Luck is not a control."
>
> — [13:43](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=823s) &middot; *Concrete anecdote arguing that contradiction detection must be systematized.*

> "Your job as a builder isn't resolve the argument. It's to make sure that the argument happens in front of a human instead of quietly along inside box."
>
> — [13:43](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=823s) &middot; *A direct design directive that many RAG systems violate by default.*

> "Model four. Facts and the guesses have to live in separate box. And the fluent AI loves melting them into one smooth sentence."
>
> — [14:52](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=892s) &middot; *Identifies fluency itself as the mechanism that destroys epistemic labeling.*

> "Label your guesses, a tag, a color, anything that survives being copy pasted into someone else's slides three weeks later."
>
> — [15:57](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=957s) &middot; *Cheap, specific fix with the durability requirement that makes it non-trivial.*

> "Before filing, the lawyer got suspicious, so he asked the chatbot, "Are these cases real?" And the chatbot said, "Yes." That is like asking the guy who sold you the watch whether the watch is real."
>
> — [17:06](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1026s) &middot; *Memorable argument against self-verification as a hallucination control.*

> "When someone points at a sentence and says, "Show me where this come from." You either click once or land on exact source paragraph, or you open seven browser tabs and start swiping."
>
> — [18:10](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1090s) &middot; *Defines a falsifiable UX standard for citation quality.*

> "The click-through is a product. Everything else is well-written packaging."
>
> — [18:10](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1090s) &middot; *The single line he asks the audience to remember.*

> "You can't outsource accountability to your own software. At the bottom of every real decision, a human signs."
>
> — [19:21](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1161s) &middot; *States the legal and organizational limit on autonomy in high-stakes workflows.*

> "If your architecture doesn't have a fundable human at the end of it, you you have not built a product. You have have built an excuse generator."
>
> — [20:28](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1228s) &middot; *Turns accountability from a policy concern into an architectural requirement.*

> "The system refuse to ship a memo where the figures don't match. No human checking at 2:00 in the morning."
>
> — [21:40](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1300s) &middot; *Specifies numeric reconciliation as a blocking system behavior, not a review step.*

> "The winners in the in this category won't win on benchmark points. They will win because a tired, skeptical finance person finance person can trust that their output at 11:00 at night without opening seven tabs."
>
> — [22:44](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1364s) &middot; *Explicitly bets against benchmarks as the competitive axis in this vertical.*

## Positions

- Almost every AI finance product is optimized to impress for five minutes rather than to withstand adversarial review, and this is why they fail with real buyers. ([2:05](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=125s), confidence: stated)
- Deals are approved on trust rather than on the quality of the numbers, so trust-building mechanics matter more than analytical intelligence. ([4:08](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=248s), confidence: stated)
- A single wrong fact in a 2023 promotional AI demo coincided with roughly an 8% stock drop, about $100 billion of value. ([7:02](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=422s), confidence: stated)
- There is no such thing as a low-stakes demo anymore; every generated sentence should be held to memo-grade standards. ([8:02](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=482s), confidence: stated)
- Most retrieval systems cannot distinguish an audited filing from an informal note and will select text by proximity to the query rather than by source authority. ([10:16](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=616s), confidence: stated)
- Small internal numeric inconsistencies cause rejection because reviewers infer from them that harder analysis was also unchecked. ([11:12](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=672s), confidence: stated)
- The algorithmic homebuying failure was a supervision failure, not a modeling failure; roughly half a billion dollars was written off and a quarter of staff let go. ([12:27](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=747s), confidence: stated)
- Contradictions between sources are the highest-value signal in diligence, and systems should escalate them rather than resolve them silently. ([12:27](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=747s), confidence: stated)
- Fluent generation systematically converts estimates into apparent facts across successive document revisions. ([15:57](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=957s), confidence: stated)
- A claim's correctness is irrelevant if its provenance cannot be verified in about 30 seconds with a single click to the source paragraph. ([18:10](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1090s), confidence: stated)
- Asking a model to verify its own output is not a valid hallucination control. ([17:06](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1026s), confidence: implied)
- Legal and organizational accountability cannot be transferred to an AI system; a named human must sign every real decision. ([19:21](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1161s), confidence: stated)
- All five of his required fixes are plumbing and honesty problems rather than model-capability problems, so a smarter model does not solve them. ([21:40](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1300s), confidence: stated)
- Category winners in AI for finance will be determined by trustworthiness in practical use rather than by benchmark performance. ([22:44](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1364s), confidence: stated)
- Investors write an internal memo after a pitch and check every spoken number against the data room, so founders face the same verification standards as their products. ([22:44](https://www.youtube.com/watch?v=tJFjeMBKbIY&t=1364s), confidence: stated)

## Concepts

- [audit trails](../concepts/audit-trails.md)
- [citation and grounding](../concepts/citation-and-grounding.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [verifier design](../concepts/verifier-design.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

