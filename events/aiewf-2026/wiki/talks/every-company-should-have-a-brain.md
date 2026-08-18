---
title: "Every company should have a Brain"
type: "talk"
slug: "every-company-should-have-a-brain"
track: "Startups"
org: "Y Combinator"
video_id: "eBUyTS7SzV4"
duration_sec: 1268
word_count: 3541
speakers: ["Garry Tan"]
---

# Every company should have a Brain

**Speakers:** [Garry Tan](../speakers/garry-tan.md)

**Org:** Y Combinator

**Track:** Startups &nbsp;|&nbsp; **Duration:** 21m 08s

[Watch on YouTube](https://www.youtube.com/watch?v=eBUyTS7SzV4)

## Summary

Y Combinator president Garry Tan argues that the leverage in AI engineering is not in model weights but in how you wire the work — and that the right unit of design is an organization, not a program. He maps agent primitives onto org structure: skill files are employees, resolver tables are org charts, filing rules are process, trigger evals are performance reviews, all made of markdown. The second half argues that every company needs a 'company brain': a curated retrieval layer plus a 'librarian' that decides which few documents load into an agent's limited context for a given task, with provenance, contradiction checks, and pruning as first-class concerns. He backs this with YC data points (a quarter of the W25 batch had 95% AI-generated code; Emergence hit nine figures of ARR in eight months; Retool-like 'Retail' at $60M with ~40 people) and a personal 400X output claim he pre-emptively deflates to 8-80X. Watch it for the org-as-agents framing, the latent-vs-deterministic compute split, and the 'never do one-off work — skillify it' discipline.

## Key Points

- The performance gap between AI users is not explained by model choice — the 2X and 100X people use the same model, so the leverage lives in workflow architecture, not weights.
- Agent primitives map one-to-one onto organizational structures: skill files are employees, resolver tables are the org chart, filing rules are internal process, and trigger evals are performance reviews.
- In YC's Winter 2025 batch, roughly a quarter of companies had codebases that were 95% AI-generated, and that batch became the fastest-growing and most profitable in YC history.
- AI-native companies encode sales, support, ops, and finance as written procedures agents execute, and hire engineers to maintain those skills rather than hiring headcount for each function.
- Engineering effort should be consciously partitioned between latent space (taste, judgment, interpreting vague human intent) and deterministic space (state, arrays, code) — most AI engineering bugs come from putting computation on the wrong side.
- Human working memory is about seven items while an agent holds roughly a million tokens (~1,000 pages), but a company's knowledge is a library, so the decisive question is who selects which few documents get loaded — that is context engineering.
- A company brain is more than RAG: retrieval is the easy primitive, while what gets written down, enriched, promoted to hot memory, and arbitrated between conflicting facts is the actual product.
- Company brains fail without hygiene — provenance on every fact, contradiction checks, and a human-plus-agent librarian whose job is pruning — otherwise you get a confidently wrong agent nobody can audit.
- The compounding discipline is to never do one-off work: after any successful agent task, convert it into a reusable skill file, because if you have to ask for something twice you failed.
- Model quality is rented while an accumulated brain is owned, so an organization that captures what it learns gets smarter daily regardless of which model it runs.

## Notable Quotes

> "The 2X people and the 100X people are using the exact same Claude. Same weights, same context window, same API. So, the leverage is not in the weights. It's in how you wire the work."
>
> — [2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s) &middot; *The talk's central thesis, stated in its sharpest form.*

> "In the winter 25 batch, a quarter of the companies had code base code bases that were 95% AI-generated, and that was a year ago."
>
> — [2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s) &middot; *Concrete portfolio-level data behind the claim.*

> "I can't prove that the AI-generated code caused the growth, but what I can tell you is the fastest growing founders we fund are not treating AI as auto-complete. They're treating it as a workforce."
>
> — [3:31](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=211s) &middot; *Rare explicit acknowledgment of a causal limit, paired with the reframe he's actually selling.*

> "A skill file is an employee. It has one capability, one job, written down clearly enough that someone can execute it."
>
> — [4:11](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=251s) &middot; *The core analogy the rest of the org mapping hangs on.*

> "We've been building organizations this whole time, but we didn't have a management layer, but now that's what we have."
>
> — [5:43](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=343s) &middot; *Names what he thinks is genuinely new.*

> "When you sit down with Claude Coder Codex, you're not writing software, you're hiring, training, and managing a workforce made of markdown."
>
> — [5:43](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=343s) &middot; *The memorable compression of the org-as-agents argument.*

> "Retail out of Winter 24, it's at $60 million with about 40 people. The kind of that kind of revenue per head did not exist before. Not in software, not in oil, not in railroads, never."
>
> — [6:25](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=385s) &middot; *A specific revenue-per-head number plus a strong historical claim.*

> "The AI-native companies that I see inside YC encode all of that as skills, written procedures that their agents execute, and they hire they hire engineers whose job it is to maintain those skills, to do the work the skills can't do yet."
>
> — [6:25](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=385s) &middot; *Defines the AI-native operating model and where humans still sit in it.*

> "you actually have to be really, really careful about where the compute computation is actually happening. It's happening almost always in two different places and all of the bugs, all of the AI engineering that we run into that's a problem, it's usually because something is happening in one side of the equation that should be in the other."
>
> — [7:41](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=461s) &middot; *The talk's most actionable engineering diagnosis.*

> "it actually must not live in the context window. The LLM has to do the human part and seat people."
>
> — [9:01](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=541s) &middot; *Concrete rule for splitting state from judgment, drawn from a real scheduling problem.*

> "an AI agent holds a million tokens. That's about a thousand pages."
>
> — [11:04](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=664s) &middot; *The quantitative hinge for the working-memory argument.*

> "Almost every company on the earth is still running an org that's designed for the seven-digit brain."
>
> — [11:48](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=708s) &middot; *One-line statement of the market opportunity he's pointing founders at.*

> "The question that determines whether your agents are geniuses or goldfish is who decides which three books are open on that desk. That's context engineering."
>
> — [12:37](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=757s) &middot; *Defines context engineering in the talk's own vocabulary.*

> "you're right that retrieval is the primitive, the same way Postgres is just B-trees. The hard part is everything around it."
>
> — [12:37](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=757s) &middot; *Directly answers the 'this is just RAG' objection.*

> "Retrieval is easy. Being worth retrieving from is the product."
>
> — [12:37](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=757s) &middot; *The most quotable formulation of the company-brain thesis.*

> "a brain nobody curates becomes a garbage dump with great search. Retrieval will surface a stale fact with total confidence."
>
> — [13:58](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=838s) &middot; *The steelmanned failure mode, offered by the advocate himself.*

> "the primitive is not memory. It's memory plus hygiene, provenance on every fact, contradiction contradiction checks when new information collides with the old, and a librarian, human plus agent, whose actual job is pruning."
>
> — [14:39](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=879s) &middot; *The prescriptive remedy — concrete requirements for a knowledge layer.*

> "Because if you have to ask for something twice, you failed."
>
> — [15:30](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=930s) &middot; *The single takeaway he tells the audience to keep.*

> "The organization that captures what it learns like this gets smarter every single day. The one that doesn't wakes up every morning with amnesia, no matter how good the model is. Model quality is rented, but if you build your brain, you you own that brain."
>
> — [16:06](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=966s) &middot; *Frames memory as the durable moat versus model choice.*

> "Open Claw is the Ferrari, I will always recommend it, but Codex is a really good Honda. It will do 90% of this. Uh it will not blow your face off, but it will get you there. Use whatever. The concepts are the point, not my repos."
>
> — [17:56](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=1076s) &middot; *Explicitly decouples the argument from his own tooling.*

> "A lot of people in the world right now are terrified about what happens to all the jobs, and I understand the fear. But I want to say it plainly, that is a failure of imagination."
>
> — [17:56](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=1076s) &middot; *Takes a contested side on AI and employment.*

> "He built a repo of 80,000 markdown files, a company brain for one small boy, and he pushed himself to the absolute edge of human, what humanity knows about his son's exact condition. No lab, no grant, no permission."
>
> — [18:35](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=1115s) &middot; *The talk's emotional anchor and its clearest non-commercial application.*

## Positions

- Differences in AI-assisted output are caused by workflow architecture, not by model choice — high and low performers use identical models. ([2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s), confidence: stated)
- The speaker's own coding output has increased roughly 400X since 2013, and at least 8X even under the most punitive discounting for AI verbosity and scaffolding. ([2:15](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=135s), confidence: stated)
- About a quarter of YC's Winter 2025 batch had codebases that were 95% AI-generated, and that batch became the fastest-growing and most profitable in YC history. ([2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s), confidence: stated)
- 94 YC companies have crossed $100 million in revenue starting from a seed check. ([3:31](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=211s), confidence: stated)
- AI-generated code cannot be proven to have caused the batch's growth. ([3:31](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=211s), confidence: stated)
- Emergence went from public launch to nine figures of ARR in eight months and was only 15 people at $15M ARR; Retail is at $60M with about 40 people. ([5:43](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=343s), confidence: stated)
- This level of revenue per employee has never previously existed in any industry. ([6:25](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=385s), confidence: stated)
- Non-technical staff — finance, media, events — can and should build skill files and cron jobs; one YC finance employee replaced ~100 Excel workbooks with a self-built app. ([7:41](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=461s), confidence: stated)
- Most AI engineering bugs come from placing computation in latent space when it belongs in deterministic space, or vice versa. ([7:41](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=461s), confidence: stated)
- Large combinatorial state, such as a seating arrangement for 800 people, must not be held in the context window. ([9:01](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=541s), confidence: stated)
- A task like optimally seating 800 people that would take a month by hand can now be done in about ten minutes for a couple hundred dollars of tokens, and was not possible six months ago. ([10:30](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=630s), confidence: stated)
- A company brain is not merely RAG — retrieval is the easy part, and the value lies in curation, enrichment, hot/cold memory promotion, and conflict arbitration. ([12:37](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=757s), confidence: stated)
- Without provenance, contradiction checking, and active pruning, a memory layer degrades into confidently wrong, untraceable output. ([14:39](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=879s), confidence: stated)
- Every agent task that succeeds should be converted into a reusable skill file rather than left as one-off work. ([15:30](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=930s), confidence: stated)
- An accumulated company brain is a more durable competitive advantage than model quality, which is rented rather than owned. ([16:06](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=966s), confidence: stated)
- The memory/company-brain layer should be open source infrastructure rather than a proprietary profit center, analogous to Linux. ([17:22](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=1042s), confidence: stated)
- Codex will accomplish about 90% of what the speaker's preferred harness does, so tool choice is secondary to the concepts. ([17:56](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=1076s), confidence: stated)
- Fear of AI-driven job loss is a failure of imagination, and the correct response is for individuals to multiply their own output. ([17:56](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=1076s), confidence: stated)
- Companies not operating this way will be outcompeted by rivals who are. ([7:05](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=425s), confidence: stated)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [context engineering](../concepts/context-engineering.md)
- [context window management](../concepts/context-window-management.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [institutional knowledge capture](../concepts/institutional-knowledge-capture.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [roi measurement](../concepts/roi-measurement.md)

