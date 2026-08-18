---
title: "How Kepler Built Verifiable AI for Financial Services"
type: "talk"
slug: "how-kepler-built-verifiable-ai-for-financial-services"
track: "AI in Finance"
org: "Kepler"
day: "Day 4 — Session Day 3"
room: "Track 3"
video_id: "Tt2kX2sgQio"
duration_sec: 1349
word_count: 3848
speakers: ["Vinoo Ganesh"]
---

# How Kepler Built Verifiable AI for Financial Services

**Speakers:** [Vinoo Ganesh](../speakers/vinoo-ganesh.md)

**Org:** Kepler

**Track:** AI in Finance &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 22m 29s

[Watch on YouTube](https://www.youtube.com/watch?v=Tt2kX2sgQio)

## Summary

Vinoo Ganesh, CEO and co-founder of Kepler, argues that the financial services industry's AI conversation is stuck on producing more output ('token maxing') when the real bottleneck is verification. His core contention is that evals cannot make a probabilistic LLM deterministic, so verifiable work product requires augmenting models with a deterministic substrate: the model decides what to compute and where information lives, but never touches the number itself. He walks through Kepler's three mechanisms — atomic provenance (the model writes a reference, not the value), scope determinism (models plan, code computes), and derivation chains (replayable records of how a ratio was built) — and notes that even a fine-tuned extraction model at 94% accuracy is unusable when a wrong number is still wrong. He also reframes verification as firm-specific rather than universal: two desks can hold opposite views on the same data, so verification means respecting your organization's rules, not finding ground truth. Worth watching if you build AI for regulated, numbers-heavy domains; the architecture generalizes past finance to legal citations and drug discovery.

## Key Points

- Citations are an after-the-fact audit that only gets you halfway; verification means a deterministic, repeatable mechanism that proves a specific number was correctly extracted from its source.
- You cannot eval your way from a non-deterministic LLM to a deterministic system, so verifiable financial work product requires pairing the model with a deterministic substrate rather than better prompting or fine-tuning.
- Kepler's atomic provenance has the model write a reference to a number rather than the number itself; databases and code do the reading and writing, and any value that fails an independent deterministic check is stripped before reaching a user.
- Multi-model cross-checking is explicitly rejected — probabilistic systems evaluating each other's work is not verification; there is instead one canonical extract-persist-confirm process.
- Scope determinism splits planning from computation: the model decides what to compute and never performs the math, which is both more accurate and cheaper than running arithmetic through a multi-billion-parameter model.
- Verification is firm-relative, not universal ground truth — two desks at the same fund can be long and short the same stock on identical data, so the system must encode each organization's own definitions of EBITDA adjustments, enterprise value, and recurring items.
- A fine-tuned extraction model that beat foundation models at 94% accuracy still isn't tradeable, because being in the wrong 6% means a wrong number.
- The architecture generalizes: deterministic pre-processing of entities could prevent hallucinated legal citations or missed compounds in drug discovery literature.
- Ganesh predicts token maxing gives way to a cost-optimization phase mirroring the Snowflake/Databricks ROI reckoning, with the last mile being firm-specific ontologies that proxy an investment process.

## Notable Quotes

> "Evals are not verifiable. You cannot take a non-deterministic LLM and eval your way to something deterministic. These are probability machines."
>
> — [1:26](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=86s) &middot; *The sharpest statement of the talk's central methodological claim, and a direct challenge to eval-centric practice.*

> "AI has made a writing problem a reading problem. We can produce insane amounts of content, whether that's code, whether it's marketing, whether it's like a DCF in record time. But we can't easily verify this."
>
> — [2:07](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=127s) &middot; *Frames the whole talk's diagnosis in one line.*

> "The problem is when a model reads everything, you have the most real version of alpha decay that you possibly can."
>
> — [2:07](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=127s) &middot; *Names the specific economic consequence for finance of commoditized reading.*

> "the reason that people buy products like Bloomberg and FactSet is to displace culpability"
>
> — [3:37](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=217s) &middot; *The talk's most contrarian claim about why incumbent data tools sell.*

> "at least if it's wrong, everyone on Wall Street has the same incorrect information"
>
> — [3:37](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=217s) &middot; *Crisply explains the culpability-displacement mechanic.*

> "The citation is effectively an after-the-fact audit. Now, a verification is a deterministic, repeatable, numerically verifiable mechanism that we can use to produce validity that a number is right."
>
> — [6:01](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=361s) &middot; *The load-bearing definitional distinction between citation and verification.*

> "Finance is one of the rare industries where two people can be have the same information, and one can be long a stock, and one can be short that stock with the exact same data. And so, the idea of verification is not actually ground truth."
>
> — [6:44](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=404s) &middot; *Reframes verification as firm-relative, which is where others would most likely disagree.*

> "It is verifying that you got an output that respects the nouns and verbs or the rules of your organization."
>
> — [7:26](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=446s) &middot; *The positive definition that replaces ground truth.*

> "AI is great at doing non-deterministic tasks. It can solve problems in a way that's novel. It can figure out exactly how to do EBITDA adjustments, but it can't be the one responsible for doing the mathematical adjustments."
>
> — [8:02](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=482s) &middot; *States the exact division of labor the architecture rests on.*

> "you cannot use AI to produce verifiable work product in finance without augmenting it with a deterministic substrate"
>
> — [8:02](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=482s) &middot; *The talk's explicitly labeled second contention.*

> "It outperformed foundation models, it's 94% great. It's in the article. Who here would trade off of something that's 94% accurate?"
>
> — [10:11](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=611s) &middot; *A reported number used to argue that accuracy improvements don't reach the bar finance requires.*

> "a wrong number is still wrong if you're in that unfortunate 6%"
>
> — [10:11](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=611s) &middot; *Compresses the case against probabilistic extraction in regulated work.*

> "with atomic provenance, what we do is the model writes effectively a reference to the number. It cannot write the number or manipulate the number in any way. It doesn't even understand what that number is."
>
> — [10:11](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=611s) &middot; *The concrete architectural mechanism, stated precisely.*

> "this is not me saying, "Have 10 models and each individual have OpenAI check chat check Anthropic and have Anthropic check XAI." These are not probabilistic systems evaluating each other's work."
>
> — [11:26](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=686s) &middot; *Explicitly rejects a popular alternative approach to AI verification.*

> "the model decides what to compute. It never does the computation itself."
>
> — [12:12](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=732s) &middot; *One-sentence definition of scope determinism.*

> "Why would I run 1 + 1 through a multi-billion parameter model instead of one CPU cycle?"
>
> — [12:12](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=732s) &middot; *The cost-and-fit argument for offloading determinism, memorably put.*

> "in what time in history has an employee been rewarded for your company to pay another vendor for how much money you're spending?"
>
> — [17:10](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=1030s) &middot; *Pointed critique of token-consumption-as-status in the current AI culture.*

> "the interesting thing here is the work product itself is the proof"
>
> — [18:43](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=1123s) &middot; *Distills the talk's forward-looking thesis about verifiable artifacts.*

> "we're almost like pre-SSL in the e-commerce ecosystem. Where like what's the TAM of e-commerce? Trillions, but how many people were comfortable putting their credit card number on the internet before there was security? Zero."
>
> — [15:44](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=944s) &middot; *The analogy that carries his claim that verification unlocks the market.*

> "everyone wants AI like the dream is the AI portfolio manager. The portfolio managers don't want the AI portfolio manager. Like they want the AI analyst."
>
> — [20:51](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=1251s) &middot; *Direct customer-demand report that contradicts the common agentic-PM framing.*

## Positions

- Evals cannot turn a non-deterministic LLM into a deterministic system, so evals do not constitute verification. ([1:26](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=86s), confidence: stated)
- Institutions buy Bloomberg and FactSet primarily to displace culpability for data errors, not because the underlying information is unavailable. ([3:37](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=217s), confidence: stated)
- Citations only get you about halfway to trustworthy AI output; they are an after-the-fact audit rather than a proof. ([18:43](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=1123s), confidence: stated)
- You cannot produce verifiable financial work product with AI unless you augment it with a deterministic substrate. ([8:02](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=482s), confidence: stated)
- Verification in finance is not about ground truth but about conforming to an individual firm's rules and definitions, since two desks can reach opposite conclusions from identical data. ([6:44](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=404s), confidence: stated)
- Fine-tuning a model to 94% extraction accuracy, even beating foundation models, is insufficient for trading decisions. ([10:11](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=611s), confidence: stated)
- Having multiple probabilistic models check each other's work is not a valid verification strategy. ([11:26](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=686s), confidence: stated)
- Models should never perform arithmetic; routing computation to code is both more correct and cheaper than running it through a large model. ([12:12](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=732s), confidence: stated)
- Intelligence is commoditized — openly downloadable models now match frontier proprietary models in reasoning and planning capability. ([12:12](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=732s), confidence: stated)
- The industry will shift from maximizing token consumption to cost optimization, repeating the ROI reckoning that followed Snowflake and Databricks adoption. ([18:03](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=1083s), confidence: stated)
- Deterministic-substrate verification generalizes beyond finance to legal citation extraction and drug discovery literature. ([15:44](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=944s), confidence: stated)
- RAG-based platforms, including science-focused ones from foundation labs, are insufficient for verifiable work product because they are not deterministic systems. ([16:27](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=987s), confidence: implied)
- Portfolio managers do not want an AI portfolio manager; the demand is for an AI analyst that reclaims analyst time. ([20:51](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=1251s), confidence: stated)
- Humans should never be manually transcribing numbers from filings into spreadsheet models. ([9:34](https://www.youtube.com/watch?v=Tt2kX2sgQio&t=574s), confidence: stated)

## Concepts

- [citation and grounding](../concepts/citation-and-grounding.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [document parsing](../concepts/document-parsing.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [ontology design](../concepts/ontology-design.md)
- [token efficiency](../concepts/token-efficiency.md)
- [verifier design](../concepts/verifier-design.md)

