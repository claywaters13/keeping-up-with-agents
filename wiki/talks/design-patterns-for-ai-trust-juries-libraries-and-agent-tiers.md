---
title: "Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers"
type: "talk"
slug: "design-patterns-for-ai-trust-juries-libraries-and-agent-tiers"
track: "GTM & Revenue"
org: "Upside.tech"
video_id: "YZQsWVeN3rE"
duration_sec: 1028
word_count: 2901
speakers: ["Alex Bauer"]
---

# Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers

**Speakers:** [Alex Bauer](../speakers/alex-bauer.md)

**Org:** Upside.tech

**Track:** GTM & Revenue &nbsp;|&nbsp; **Duration:** 17m 08s

[Watch on YouTube](https://www.youtube.com/watch?v=YZQsWVeN3rE)

## Summary

Alex Bauer of Upside.tech argues that the AI hallucination problem has matured into a trust problem: agents answer business questions confidently and wrongly, which is worse than saying 'I don't know.' His thesis is that the practical fix is not prompt incantations or bleeding-edge technical optimization but managing agents the way you'd manage humans — give them commander's intent, scaffold their context, and require second opinions. He walks through three concrete patterns his team uses: an 'anchor assets' library of structured company documentation (product capability references, personas) that agents consult before generating anything; a 'librarian' service that injects just-in-time company semantics (fiscal calendar, what 'pipeline' means, prior failed queries) before an agent touches data; and a jury-and-judge workflow for multi-touch attribution where independent analyst agents produce evidence-cited opinions and a consensus judge weighs reasoning quality rather than treating outputs as fact. A bonus 'agent tiers' argument warns that AI features crowbarred into cheap per-seat subscriptions can't afford real reasoning models and shouldn't be trusted with important work. Worth watching if you work in go-to-market or are building agent systems over messy business data; it's pattern-level and light on implementation detail.

## Key Points

- The hallucination discourse has been replaced by a trust problem: when asked to report revenue, an agent doesn't say 'I'm not sure,' it gives a wrong answer that looks exactly like a right one.
- The core thesis is that agent management should borrow from human management — when in doubt, manage your agents like other humans, because establishing trust is not a new problem.
- The single practical tip is to use 'commander's intent' from armed forces doctrine: tell agents why you want something done, not just what, and they perform better — but pull them back when they micromanage themselves.
- Fully autonomous 'YOLO mode' website generation failed even with Claude's plan mode; the working approach was to define structure first via scaffolding, then turn the model loose.
- Upside maintains 'anchor assets' — a product capabilities reference and persona definitions — compiled with AI but carrying citations back to source systems so the human can verify nothing important was hallucinated.
- The 'librarian' pattern intercepts a user question before the agent queries data and supplies just-in-time memory: documentation, company knowledge items, and a schema of prior failed queries, so the agent knows the fiscal year is February–April and that 'pipeline' means stage two or later.
- For problems with no empirically correct answer, like multi-touch attribution, a jury of independent analyst agents plus a consensus judge that weighs reasoning quality and escalates when consensus is thin outperforms a single agent perseverating alone.
- Agent tiers matter: AI bolted into per-seat subscription products lacks the margin to run an intelligent reasoning model, so require at least a tier-two harness with sub-agents, plan mode, full MCP support, and file editing.
- AI has made go-to-market teams — historically low-density in builders, working from spreadsheets and slides — into builders, giving non-engineers 'an infinite supply of valedictorian interns with computer science degrees.'

## Notable Quotes

> "And if you ask Claude to do something like report on revenue, it doesn't say, "I'm not sure." It says, "Here you go." And it gives you a wrong answer that looks exactly like being right."
>
> — [7:18](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=438s) &middot; *The talk's central framing of the trust problem, stated in one line.*

> "Somehow that big word seems to not come up as often anymore, but I think we have its older sibling now. It's a trust problem."
>
> — [7:18](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=438s) &middot; *Names the reframing from hallucination to trust that organizes the whole talk.*

> "So, the main thesis of the talk today is actually, when in doubt, manage your agents like other humans."
>
> — [8:32](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=512s) &middot; *Explicit thesis statement.*

> "And if you take nothing else from this talk, this is my one practical tip. Use commander's intent when you prompt."
>
> — [8:32](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=512s) &middot; *The speaker's single flagged actionable takeaway.*

> "This is something that comes out of the armed forces doctrine, but basically tell your agents why you want them to do something, and they will do it a lot better."
>
> — [8:32](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=512s) &middot; *Defines commander's intent and states the causal claim behind it.*

> "But, beware because the agents have been trained on material from other humans, and so they like to micromanage themselves, and that's not usually what you want."
>
> — [9:07](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=547s) &middot; *A non-obvious failure mode with a stated mechanism.*

> "Don't tell Claude to improve itself, you'll get micromanagement."
>
> — [9:07](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=547s) &middot; *Concrete anti-pattern, compactly stated.*

> "a lot of the talks this week I think have been around the bleeding edge of technical optimizations, and a lot of the influencer fluff you see on LinkedIn and Twitter tells you about the magic improvements if you, you know, do your prompt with exactly the right incantation. I think both of those things might well be true, but I don't generally have time to do either of them."
>
> — [7:57](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=477s) &middot; *Positions the talk against both the technical frontier and prompt-hacking advice.*

> "What AI has done for those second two groups is basically provided you with an infinite supply of valedictorian interns with computer science degrees who can help you implement all of the solutions that you probably know better than any engineer that you'd work with on a different team."
>
> — [6:32](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=392s) &middot; *The talk's argument for why non-technical domain experts now out-build engineers on their own problems.*

> "Cloud does for building basically what the bicycle did for mobility. It makes it accessible."
>
> — [5:46](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=346s) &middot; *Memorable framing of AI's democratizing effect (auto-caption renders 'Claude' as 'Cloud').*

> "And it was obviously a fail, even with using a nice plan mode in Claude first. I'm sure this will work eventually, but it doesn't today. So, you have to do some scaffolding."
>
> — [9:45](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=585s) &middot; *Reports a concrete negative result about end-to-end autonomous generation.*

> "So, the step here was define the structure first, and then turn Claude loose. Don't try and YOLO it from the beginning."
>
> — [10:59](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=659s) &middot; *States the scaffolding pattern as a rule.*

> "So, these are citations from across every system that it's connected to. I can follow them back if I need more details, but that helps me know that it didn't hallucinate the important parts."
>
> — [10:59](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=659s) &middot; *Names citation traceability as the verification mechanism for AI-compiled documentation.*

> "And the librarian has access to documentation and the library of knowledge items about your company and the schema of prior failed queries. And so it basically gives your agent a just-in-time memory of all the important things."
>
> — [12:40](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=760s) &middot; *The clearest definition of the librarian pattern, including the prior-failed-queries input.*

> "They are going to spin up a team of independent analysts who all look at the data independently and come up with an evidence-cited opinion for what they think the attribution credit of that deal should be."
>
> — [14:00](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=840s) &middot; *Defines the jury half of the jury-and-judge workflow.*

> "I'm treating them as input, and I'm going to weigh the reasoning quality of each of these analysts, and then I'm going to help you come up with the final version here. And if there's not enough consensus, then I'll escalate and expand the jury."
>
> — [14:37](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=877s) &middot; *Specifies how the judge aggregates — reasoning quality, not majority vote — plus the escalation rule.*

> "Turns out multiple researchers with somebody who helps at the end is better than a single person kind of perseverating on that forever."
>
> — [14:37](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=877s) &middot; *The human-analogy justification for multi-agent research over a single long-running agent.*

> "In my experience, you can't fix stupid. So, this basically means friends don't let friends use really bad harnesses or low intelligent models for important work."
>
> — [15:11](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=911s) &middot; *The agent-tiers thesis, bluntly stated.*

> "any AI product where it's been crowbarred into a pre- subscription model is probably not something that you should be using for anything important because the margin on those plans just doesn't leave enough space for an intelligent reasoning model to work"
>
> — [15:11](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=911s) &middot; *An economic mechanism for why cheap embedded AI features underperform.*

> "You need it to have attributes like sub agents, plan mode, full MCP support. It should be able to use file editing"
>
> — [16:12](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=972s) &middot; *The concrete checklist for what counts as an acceptable agent harness.*

> "So, do not let your team just use the chat GPT web interface and expect that it will be a great result."
>
> — [16:12](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=972s) &middot; *Names a specific tool the speaker considers inadequate for important work.*

> "there is no empirically correct answer. And we have a model for how we deal with that in the real world."
>
> — [13:18](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=798s) &middot; *The premise that motivates jury-based evaluation over ground-truth evals.*

## Positions

- The dominant problem with business-facing AI is no longer hallucination per se but trust: agents return confidently wrong answers indistinguishable from correct ones. ([7:18](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=438s), confidence: stated)
- Agents should be managed using human management techniques rather than through prompt-engineering tricks or bleeding-edge technical optimization. ([8:32](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=512s), confidence: stated)
- Telling an agent why it should do something (commander's intent) produces materially better results than instructing it what to do. ([8:32](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=512s), confidence: stated)
- Asking Claude to improve its own prompts or behavior yields micromanagement, because it was trained on human-produced material. ([9:07](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=547s), confidence: stated)
- End-to-end autonomous generation of a company website from raw sources fails today, even with plan mode; structured scaffolding is required first. ([9:45](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=585s), confidence: stated)
- Agents querying business data will silently apply wrong definitions (calendar quarters, created-date pipeline) unless a librarian layer supplies company-specific semantics first. ([12:04](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=724s), confidence: stated)
- For questions with no empirically correct answer, a jury of independent agents plus a consensus judge that weighs reasoning quality beats a single agent working alone. ([14:37](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=877s), confidence: stated)
- AI features embedded in per-seat subscription products (e.g. Slackbot's MCP client) are not usable for important work because the plan margins can't fund an intelligent reasoning model. ([15:11](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=911s), confidence: stated)
- An acceptable agent harness must have a powerful model plus sub-agents, plan mode, full MCP support, and file editing; the ChatGPT web interface does not qualify for team use. ([16:12](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=972s), confidence: stated)
- Multi-touch attribution required roughly two years of work and only became tractable once Opus-class models were available. ([13:18](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=798s), confidence: stated)
- Go-to-market practitioners, not engineers, are now best positioned to build their own tooling because they know the problems better and AI supplies the implementation capability. ([6:32](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=392s), confidence: implied)
- AI-compiled documentation is trustworthy only when it carries citations back to source systems that a human can follow. ([10:59](https://www.youtube.com/watch?v=YZQsWVeN3rE&t=659s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [ai-assisted code review](../concepts/ai-assisted-code-review.md)
- [citation and grounding](../concepts/citation-and-grounding.md)
- [context engineering](../concepts/context-engineering.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [semantic layer](../concepts/semantic-layer.md)
- [spec-driven development](../concepts/spec-driven-development.md)

