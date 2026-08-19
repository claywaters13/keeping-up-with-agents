---
title: "Own Your Intelligence"
type: "talk"
slug: "own-your-intelligence"
org: "Y Combinator"
video_id: "eRrc1pUY5oU"
duration_sec: 2528
word_count: 6546
speakers: ["Garry Tan"]
---

# Own Your Intelligence

**Speakers:** [Garry Tan](../speakers/garry-tan.md)

**Org:** Y Combinator

**Duration:** 42m 08s

[Watch on YouTube](https://www.youtube.com/watch?v=eRrc1pUY5oU)

## Summary

Garry Tan argues that AGI is not arriving as a single event in a data center but is already here, diffused as "personal AGI": an agent running on your own infrastructure, reading a memory you own, and executing skill files you wrote. His core equation is that frontier models are a rented, commoditizing input, so the durable advantage moves to the context and procedures you accumulate — which compound daily rather than only when a vendor ships. Most of the talk is a concrete how-to (pick a harness, start a markdown library, write your first skill file, schedule it as a recurring job, and never do one-off work), backed by receipts from his own setup and YC portfolio numbers. The final third turns political: because a skill file is your cognition extracted and executable, whoever owns the repo owns the compounding judgment, and Tan urges knowledge workers to keep their skills in a repo they control. Worth watching if you want a founder-facing operating manual for agent leverage plus an explicit ideological frame for why ownership of context matters.

## Key Points

- Tan reframes AGI as "personal AGI" — general intelligence for one person, running on infrastructure you own — rather than a singular threshold event announced by a lab.
- He draws a sharp line between a rented corporate assistant, which improves only when the vendor ships, and an owned agent stack, which improves every day because it accumulates more of your life.
- The stated equation for the decade is commodity frontier model + your unique context + a harness that wires them together; the leverage lives in the context, not the weights.
- He claims roughly 400x personal code output versus 2013, and argues that even under the harshest verbosity discount the floor is still about 8x — and that the multiplier applies to design, PM, growth, and all knowledge work, not just code.
- YC evidence offered: a quarter of Winter 25 batch companies had 95% AI-generated codebases; Emergent hit nine figures of revenue in eight months and was 15 people at $15M ARR; Retail hit $60M annualized with about 40 people.
- Architecture advice: split work between latent space (taste, judgment, vague requests) and deterministic space (arithmetic, SQL, scheduling), with markdown files calling databases and scripts — the conference's own 6,000-person scheduling was built this way.
- The five-step playbook is: run an agent locally, start a markdown library of people and projects, write one skill file for the weekly task you hate most, wire it to a recurring job, and "skillify" every task so nothing is one-off.
- The political thesis: skill files are externalized cognition, so the same 40 files are either a portable career asset or an extraction, depending solely on whose repo they live in.
- He addresses three objections head-on — better models will obsolete harnesses (no: they raise the value of your library), this is just RAG (retrieval is the primitive, being worth retrieving from is the product), and privacy (custody in your own infra beats scattering your life across ten clouds).
- He warns that an uncurated brain is "a garbage dump with great search," requiring provenance, contradiction checks, and active pruning to compound rather than mislead.

## Notable Quotes

> "The corporate AGI you don't own gets better only when the company ships something. Your personal AGI gets better every single day you use it because every day it knows more of your life."
>
> — [7:11](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=431s) &middot; *The cleanest statement of the owned-vs-rented distinction the whole talk rests on.*

> "In 2013, I was a YC partner building Bookface, our internal social network at night. I shipped maybe 14 useful lines of code a day"
>
> — [8:00](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=480s) &middot; *Establishes the personal baseline for his headline productivity claim.*

> "It's still 8x at the absolute floor, and 10 times that in the middle of the range. The number is large no matter how you torture it."
>
> — [8:39](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=519s) &middot; *Pre-emptively discounts his own 400x number and states the defensible floor.*

> "A year and a half ago, in the winter 25 batch, a quarter of the companies had codebases that were 95% AI generated."
>
> — [9:17](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=557s) &middot; *A concrete portfolio-scale data point, with an explicit correlation caveat right after it.*

> "There are 2X people and there are 100X people who are using the same cloud, same weights, same context window size, same API, but the leverage is not in the weights."
>
> — [9:59](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=599s) &middot; *States the central claim that variance comes from context, not model access.*

> "In Ethics, he defines joy as the feeling of your power of acting increasing, which is why the first time an agent does a week of your work in an afternoon, it doesn't feel like a convenience, it feels like joy."
>
> — [9:59](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=599s) &middot; *The Spinoza frame the talk keeps returning to, applied directly to agent use.*

> "Model quality is rented, but your brain is owned, ideally by you."
>
> — [11:28](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=688s) &middot; *The thesis compressed into one line.*

> "An AI agent, though, holds a million tokens. That's about 1,000 pages. Three Harry Potter books sitting open on its head all at once."
>
> — [12:53](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=773s) &middot; *The working-memory comparison that motivates the library-plus-librarian architecture.*

> "My personal open claw has a Karpathy-style knowledge wiki with about 220,000 markdown pages. 25 years of my life diarized."
>
> — [14:36](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=876s) &middot; *Names the actual scale of his own system, which anchors every later claim.*

> "It's mostly skill files. Plus a browser that the agents can drive, pages of English and a way to act on the world. Markdown, not magic. Fat skills, thin harness."
>
> — [16:46](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1006s) &middot; *A design principle other builders can adopt or argue with.*

> "Markdown is actually code. If you can write clear instructions in English, you're a programmer. The compiler is a language model."
>
> — [17:24](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1044s) &middot; *His most contested claim, which he acknowledges drew flak.*

> "Some computation belongs in latent space. Taste, judgment, reading what a human actually wants from a vague request. That lives in the model, and you steer it with a markdown file."
>
> — [18:05](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1085s) &middot; *Names the latent/deterministic split he blames for every agent failure he's seen.*

> "She is not a programmer. She is a manager of agents now. Everyone is about to be."
>
> — [18:05](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1085s) &middot; *Extends the argument beyond engineers with a specific in-house example.*

> "Emergent out of our summer 24 batch went from public launch to nine figures of revenue in eight months. When they crossed $15 million in annualized revenue, they were 15 people."
>
> — [21:37](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1297s) &middot; *Hard revenue-per-employee numbers supporting the new-physics claim.*

> "Retail winter 24 hit 60 million annualized with about 40. That revenue per person did not exist before, not in software, not in oil, not in railroads."
>
> — [22:20](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1340s) &middot; *A second data point plus the strong historical comparison he stakes on it.*

> "a brain nobody curates is a garbage dump with great search. Retrieval will surface a stale fact with total confidence. A bad skill file encodes a bad process forever."
>
> — [23:43](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1423s) &middot; *The talk's main self-imposed caveat and its case for memory hygiene.*

> "I'll say it the way I say it at YC. If you have to ask for something twice, you failed."
>
> — [27:52](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1672s) &middot; *The operating rule behind 'never do one-off work.'*

> "A skill file is not a document. It's a piece of your cognition, how you do the thing, extracted from your head, written down, and executable."
>
> — [29:14](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1754s) &middot; *The pivot from tooling advice to the labor-politics argument.*

> "40 files executing forever and her name isn't even in the commit history. She didn't have a career, she had an extraction."
>
> — [30:43](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1843s) &middot; *The Maya thought experiment's punchline on what losing skill-file ownership costs.*

> "I believe skill files are yours. Own your skills because if you don't, your job becomes a skill file."
>
> — [30:43](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1843s) &middot; *The doctrine he explicitly asks the audience to repeat.*

> "The better the models get, the more the differentiator moves to context. When everyone's engine is a thousand horsepower, the race is won on the driver and the map."
>
> — [33:18](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1998s) &middot; *His direct rebuttal to the bitter-lesson objection.*

> "Objection two, is this just rag? Sure, and Postgres is just B-trees. Retrieval is the primitive, not the product."
>
> — [33:58](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2038s) &middot; *Concedes the technical reduction while relocating where the work actually is.*

> "Retrieval is easy. Being worth retrieving from is the product."
>
> — [34:43](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2083s) &middot; *A quotable inversion of the usual RAG framing.*

> "I took custody of it. Custody is the security model, and if you don't trust yourself to hold the keys, I promise you the answer isn't trusting someone else's terms of service more."
>
> — [35:22](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2122s) &middot; *His answer to the consolidation-risk objection, stated as a security position.*

> "I say agents write most of my code now, and the dunks arrive by lunch. Then I look at what the loudest dunkers are actually shipping, and it's agents all the way down."
>
> — [37:40](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2260s) &middot; *A claim about the gap between public criticism and actual practice.*

> "He built a repo of 80,000 markdown files. A brain for one small boy."
>
> — [38:23](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2303s) &middot; *The talk's emotional proof that the architecture isn't only about startups.*

> "The difficulty just collapsed. The rarity is now up to you. Go and build."
>
> — [41:49](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2509s) &middot; *The closing call to action, framed against Spinoza's final line.*

## Positions

- AGI will not arrive as a singular event or announcement; it arrives diffused as personal agents running on individual context. ([5:31](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=331s), confidence: stated)
- Subscription chatbots are 'corporate AGI you don't own' — they reset, know only what everyone else knows, and can be degraded on the vendor's schedule. ([6:24](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=384s), confidence: stated)
- Tan's own code output is roughly 400x his 2013 baseline, with an absolute floor of 8x under the most pathological verbosity discount. ([8:39](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=519s), confidence: stated)
- The productivity multiplier from coding agents applies equally to design, product management, growth, and all knowledge work. ([9:17](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=557s), confidence: stated)
- The Winter 25 batch, a quarter of which had 95% AI-generated codebases, is on track to be one of the fastest-growing and most profitable batches in YC history — though Tan explicitly declines to claim causation. ([9:17](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=557s), confidence: stated)
- Leverage differences between 2x and 100x operators come from context selection and timing, not from model weights, cloud, or API access. ([9:59](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=599s), confidence: stated)
- If a smart intern could follow a written instruction, an agent can run it — which makes writing clear English a form of programming. ([17:24](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1044s), confidence: stated)
- Every agent failure Tan has seen comes from confusing what belongs in latent space with what belongs in deterministic code. ([18:05](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1085s), confidence: stated)
- The revenue-per-person achieved by companies like Emergent and Retail has no historical precedent in software, oil, or railroads. ([22:20](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1340s), confidence: stated)
- The old advice to 'scratch your own itch and hope it's a market' should be replaced by building tools for an audience of one, because some will turn into companies when others start asking to borrow them. ([23:05](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1385s), confidence: stated)
- Most people who attempt this will quit in week two; the flywheel only catches around week four and pays off around week twelve. ([28:32](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1712s), confidence: stated)
- Knowledge workers were previously protected because their tools lived in their heads; skill files end that protection by making cognition extractable, storable, and ownable by an employer. ([31:26](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1886s), confidence: stated)
- Founders should keep their brain and skills in a repo they control from day one, before any platform or acquirer has an opinion about it. ([32:23](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=1943s), confidence: stated)
- Improving frontier models increase rather than decrease the value of a personal context library, because a smarter reader extracts more from the same books. ([33:58](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2038s), confidence: stated)
- Consolidating your life into a system you control is more private than the default of scattering it across ten clouds owned by companies whose incentives differ from yours. ([34:43](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2083s), confidence: stated)
- Tools of the powerful should be given away, because privately held leverage technology produces a priesthood while widely distributed leverage produces a renaissance. ([35:56](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2156s), confidence: stated)
- Public criticism of agent-written code is an early stage of adoption — the loudest critics are already shipping the same way. ([37:40](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2260s), confidence: implied)
- The traditional startup prerequisites — team, funding, permission, credentials — were workarounds for human working-memory and time limits that agents have now removed. ([39:19](https://www.youtube.com/watch?v=eRrc1pUY5oU&t=2359s), confidence: stated)

## Concepts

- [agent configuration files](../concepts/agent-configuration-files.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [context engineering](../concepts/context-engineering.md)
- [open source ai strategy](../concepts/open-source-ai-strategy.md)
- [personal ai agents](../concepts/personal-ai-agents.md)
- [research taste](../concepts/research-taste.md)
- [small team leverage](../concepts/small-team-leverage.md)

