---
title: "Stop Writing Tone Instructions. Layer Them."
type: "talk"
slug: "stop-writing-tone-instructions-layer-them"
org: "Isadora & Co"
video_id: "ij-AU9dpJjc"
duration_sec: 1256
word_count: 3716
speakers: ["Isadora Martin-Dye"]
---

# Stop Writing Tone Instructions. Layer Them.

**Speakers:** [Isadora Martin-Dye](../speakers/isadora-martin-dye.md)

**Org:** Isadora & Co

**Duration:** 20m 56s

[Watch on YouTube](https://www.youtube.com/watch?v=ij-AU9dpJjc)

## Summary

Isadora Martin-Dye, who runs a 225-year-old Virginia wedding venue and built AI agents for it and other high-touch businesses, argues that a single detailed system prompt cannot carry brand voice because it's being asked to do four different jobs at once. She proposes a four-layer prompt architecture: immutable identity (hard rules nothing below can override), situational mode (real-time signals about who the user is and what they're going through), example-anchored voice (the tone guide most teams start and stop at), and a post-generation veto (a cheap deterministic check on what actually came out). Her core distinction is that the first three layers are instructions — probabilistic requests the model usually follows — while the fourth is permission, deterministic and enforceable. She grounds this in concrete failures: an AI offering wedding dates that were already booked, and a white-label leak where every tenant shipped as the same venue's persona. Worth watching if you're building brand-voice-critical agents where a single wrong sentence costs more than a refund.

## Key Points

- One system prompt fails because it's being asked to simultaneously be inviolable, situational, expressive, and self-checking — four fundamentally different jobs that should each get their own layer.
- Layer one holds immutable identity rules that no venue config, voice profile, or user request can override, such as always disclosing AI status or never claiming a physical body.
- Layer two encodes real-time situational signals — who the user is (couple vs. staff coordinator) and what they're going through — and most teams never build it at all.
- Order of assembly is load-bearing: soft human context is rendered before numeric constraints, because a model that commits to numeric framing first produces prose that feels mechanically slotted.
- Layer three, the example-anchored tone guide, is where most engineering teams stop because voice feels like a marketing problem rather than a technical one, but examples only cover the happy path.
- Layer four is a post-generation veto with two modes — soft flags from an honesty inspector and hard rejects from a numbers guard — and is the only non-prompt, deterministic part of the architecture.
- The veto exists because of a real recurring failure: a warm, confident model offering wedding dates that were already booked, having never been given the calendar.
- The same architecture transfers across wildly different stakes — for Thread Light, a tool for families of missing people, layer one forbids words like 'confirmed', 'matched', and 'solved'.
- In multi-tenant systems, brand identity must never have a silent default; a missing identity should crash rather than fall back, since the quiet failure is a venue speaking in a stranger's voice.

## Notable Quotes

> "I'm not programming a robot, I'm managing a brilliant intern with an incredibly high IQ and a terrible EQ."
>
> — [0:00](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=0s) &middot; *The framing device that drives every architectural decision in the talk.*

> "They will say something technically perfect and socially catastrophic in the same confident sentence."
>
> — [0:00](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=0s) &middot; *Sharp statement of the failure mode brand-voice systems actually face.*

> "If you're programming a robot, you write rules and walk away. If you're managing an intern, you build structure and you check their work before it goes out the door."
>
> — [0:42](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=42s) &middot; *Converts the analogy directly into the build-vs-check thesis.*

> "Places where a single wrong sentence can cost more than a refund."
>
> — [1:23](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=83s) &middot; *Scopes exactly when this architecture is worth the cost.*

> "Write in our brand's voice is a comment that says, "Just make it work." It does nothing that the model wasn't already going to try and do."
>
> — [1:23](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=83s) &middot; *Direct attack on the standard prompt-engineering advice.*

> "And the reason it keeps failing isn't that the examples are bad, it's that you're asking one prompt to do four completely different jobs."
>
> — [2:02](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=122s) &middot; *The central diagnosis of the talk.*

> "Before this architecture, my system had 24 different system prompts scattered across the code base."
>
> — [2:46](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=166s) &middot; *Concrete number describing the pre-refactor mess.*

> "Every AI in Bloom discloses that it is AI in its very first response. Not if asked, but before they ask. It's a product decision, not a legal one."
>
> — [5:34](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=334s) &middot; *A specific, checkable policy position others might disagree with.*

> "The voice layer wants to be warm and with AI, that does mean first person. They want to say, "I can't wait to show you around." But AI has no body, so that warmth and constraint produces a lie."
>
> — [6:12](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=372s) &middot; *Names the structural conflict between the warmth layer and the identity layer.*

> "The moment her user realizes they have been performing a relationship with someone who was never there, the trust doesn't just dip, it inverts."
>
> — [6:12](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=372s) &middot; *The strongest articulation of the trust stakes.*

> "For a missing person tool, layer one stops the AI from ever telling a person that their person has been found."
>
> — [7:26](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=446s) &middot; *Shows the architecture generalizing to genuinely high-stakes domains.*

> "It's reaching for the word match because statistically it is the natural word."
>
> — [7:26](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=446s) &middot; *Explains why hard rules must sit outside the voice layer rather than inside it.*

> "Use these notes for tone, empathy, and what not to say. Never quote them verbatim."
>
> — [9:58](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=598s) &middot; *A reusable, concrete policy for injecting sensitive personal context.*

> "Reversing the order makes the prose feel mechanically slotted because the model is already committed to the numeric framing before it reads the qualitative tone fuel."
>
> — [9:58](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=598s) &middot; *A non-obvious, testable claim about prompt section ordering.*

> "Examples are not the right tool for guarantees, they were never designed to be."
>
> — [12:41](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=761s) &middot; *Crisp statement of few-shot prompting's ceiling.*

> "A false positive means someone double-checked a phone response. A false negative remains a hallucinated number or a privacy violation that ships to a client."
>
> — [13:56](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=836s) &middot; *States the asymmetry that justifies an aggressive output guard.*

> "A warm, confident voice offering something that isn't real is worse than a cold one because the couple now believes they have a date."
>
> — [15:10](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=910s) &middot; *Counterintuitive claim that better voice can amplify harm.*

> "Usually is completely fine when the cost of being wrong is a slightly off-brand sentence."
>
> — [15:10](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=910s) &middot; *Defines precisely where probabilistic instruction stops being adequate.*

> "The first three layers are instruction, the fourth is permission. And that's the whole distinction. Instructions are probabilistic. Permission is deterministic."
>
> — [17:51](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1071s) &middot; *The thesis in its most compressed form.*

> "Everything before layer four is prompt engineering. You're asking nicely and hoping. Layer four is systems engineering. You're checking, and you are sure."
>
> — [17:51](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1071s) &middot; *The talk's most quotable reframing of prompt work as engineering discipline.*

> "In a multi-tenant system, identity must never have a default. A missing brand identity is a crash, not a fallback."
>
> — [17:09](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1029s) &middot; *A hard, transferable engineering rule derived from a real production leak.*

> "A prompt will eventually lose."
>
> — [19:14](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1154s) &middot; *The assumption the entire architecture is built on.*

> "And right now I'm choosing determinism over coverage. I'd make that choice again as it stands, but it is a real trade-off and not an obvious win."
>
> — [20:38](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1238s) &middot; *Honest naming of the regex-vs-classifier tradeoff rather than claiming a clean win.*

## Positions

- A single system prompt cannot simultaneously be situational, expressive, and self-checking, so brand voice must be split into four distinct layers. ([2:46](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=166s), confidence: stated)
- Hard identity rules must live in a layer that the voice layer physically cannot override, not merely as instructions among other instructions. ([8:00](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=480s), confidence: stated)
- AI agents should disclose they are AI in the first response, unprompted, because upfront disclosure builds more trust than discovery on turn seven. ([5:34](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=334s), confidence: stated)
- Most teams build only the example-anchored voice layer and never build a situational mode layer at all. ([8:00](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=480s), confidence: stated)
- Rendering soft human context before numeric constraints in the prompt produces less mechanical prose than the reverse order. ([9:58](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=598s), confidence: stated)
- Few-shot examples can teach quality on anticipated inputs but cannot provide guarantees on unanticipated ones. ([12:41](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=761s), confidence: stated)
- The post-generation veto is the cheapest of the four layers to build. ([15:49](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=949s), confidence: stated)
- For output guards, false positives are far cheaper than false negatives, so the guard should be tuned aggressively. ([13:56](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=836s), confidence: stated)
- A more fluent, warmer voice makes a factual error worse rather than better, because it increases the user's belief in the false claim. ([15:10](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=910s), confidence: stated)
- In multi-tenant systems, a missing brand identity field should throw rather than silently default, since silent defaults caused a white-label leak where every venue shipped as sage@hawthornemanner.com. ([17:09](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1029s), confidence: stated)
- Deterministic regex-based checks are preferable to a probabilistic classifier for output vetoes, trading coverage for reliability. ([20:38](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1238s), confidence: stated)
- The veto should be a shared service that every surface passes through by default rather than wired individually per surface, to prevent accidental opt-out. ([19:14](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=1154s), confidence: stated)
- This architecture is only worth its cost where voice is the product and a single wrong sentence carries reputational cost, not for commodity interactions like retail product search. ([1:23](https://www.youtube.com/watch?v=ij-AU9dpJjc&t=83s), confidence: implied)

## Concepts

- [agent configuration files](../concepts/agent-configuration-files.md)
- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [context engineering](../concepts/context-engineering.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [hallucination mitigation](../concepts/hallucination-mitigation.md)
- [output guardrails](../concepts/output-guardrails.md)
- [prompt engineering](../concepts/prompt-engineering.md)

