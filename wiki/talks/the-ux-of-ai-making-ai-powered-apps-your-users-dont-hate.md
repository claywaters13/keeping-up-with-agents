---
title: "The UX of AI: Making AI-Powered Apps Your Users Don't Hate"
type: "talk"
slug: "the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate"
org: "Progress Software"
video_id: "L3RuP_q8Bwc"
duration_sec: 2158
word_count: 6296
speakers: ["Kathryn Grayson Nanz"]
---

# The UX of AI: Making AI-Powered Apps Your Users Don't Hate

**Speakers:** [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)

**Org:** Progress Software

**Duration:** 35m 58s

[Watch on YouTube](https://www.youtube.com/watch?v=L3RuP_q8Bwc)

## Summary

Kathryn Grayson Nanz, a design/developer advocate at Progress Software, argues that AI's biggest adoption problem right now isn't model quality — it's user experience. She frames the current moment as an unusually wide literacy gap between the engineers who build AI features and the users who encounter them, comparable to (but wider than) the early Macintosh GUI era, and argues that developers can't outsource the design work to AI because the interaction patterns for AI don't yet exist to be remixed. The talk organizes user complaints into five pillars — trust, clarity, control, transparency, and meaningful benefit — and walks through concrete UI patterns for each: source citations and agent action plans, streaming output and visible chain of thought, hard stop buttons and version history, granular permission structures and cost estimates, and prompt templates plus next-step action buttons. Her closing claim is the practical payoff: since models are converging on being good, the differentiator for AI software is the experience layer built around them. Worth watching if you ship user-facing AI features and want a checklist of patterns rather than a philosophical take.

## Key Points

- The knowledge gap between AI developers and AI users is one of the widest of any technology, and users get only a handful of bad experiences before they disengage from AI features permanently.
- You can't delegate AI interface design to AI, because AI remixes existing patterns and standardized AI interaction patterns don't yet exist — AI-generated UI reliably looks average, which is a fine starting point but a poor ending point.
- Rather than claiming your AI is uniquely trustworthy, build 'trust but verify' affordances: citations, inline links, tooltips with source snippets, and side panels that position the assistant as a librarian rather than a subject matter expert.
- Citations serve a second purpose beyond verification — they let users repurpose AI output in their own work while preserving a trail of accuracy that protects their professional reputation.
- Streaming text and visible chain of thought do double duty: they mask latency, let users abort bad generations early, and keep the user an active participant instead of walking away for a five-minute side quest.
- Users must have a prominent 'emergency brake' to halt any AI action — buried in a menu or behind a remembered command doesn't count — plus version history calibrated to task complexity, from nothing for simple chat to checkpoints and save states for advanced work.
- Permissions for AI agents are not binary or one-and-done; design for gray zones like read-vs-delete, one-time-vs-permanent, and specific-folder-vs-all-folders, with a revocable history users can inspect.
- Meaningful benefit requires not assuming AI literacy: supply examples, templates, suggested prompts, and guided workflows, and add next-step action buttons and integrations so output can actually flow into the user's real workflow.
- Mark AI-generated content as AI-generated so users never feel something was snuck past them, and show a visual indicator whenever an agent is independently driving the interface.

## Notable Quotes

> "it doesn't actually matter what our software can do if our users hate using it so much that they will avoid it at all costs"
>
> — [1:59](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=119s) &middot; *The thesis of the talk in one line.*

> "The more times they try an AI feature and get sub-par results, the less likely they are to engage with it again in the future."
>
> — [2:47](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=167s) &middot; *States the core risk model — user patience for AI is a depleting budget.*

> "this knowledge gap between developer and user when it comes to AI is one of the widest that I've seen with any technology"
>
> — [3:25](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=205s) &middot; *A comparative claim about AI versus prior technology waves.*

> "Right now, we are probably somewhere around system 3 in this metaphor of introducing AI to users. We may not need the turtle and rabbit icons anymore, but we also can't yet assume that they will sit down with our AI software as experts."
>
> — [4:53](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=293s) &middot; *The Macintosh analogy that anchors her argument about where AI literacy currently sits.*

> "The problem with that is that AI can only really remix things that already exist. It's fantastic for looking at those existing common patterns and replicating them, but the patterns for AI interfaces don't fully exist yet."
>
> — [7:40](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=460s) &middot; *Her direct answer to 'why not let AI design this' — a position others would contest.*

> "An AI-generated UI tends to look pretty darn average. And while that can be a really great starting point, it's not usually a great ending point."
>
> — [8:24](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=504s) &middot; *Names the tradeoff of AI-generated design in a memorable way.*

> "Right now, to the average user, AI is a black box. Many simply do not understand from a technical perspective how it works. And when you don't understand how something works, it makes it very, very hard to trust the output."
>
> — [10:30](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=630s) &middot; *Diagnoses the trust problem's root cause.*

> "In situations where we cannot promise the truth, we have to go above and beyond to earn it. Our honesty about current capabilities and limitations of our AI tools will go a lot further with our users than the denial of any potential problems."
>
> — [11:54](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=714s) &middot; *Takes a clear side against marketing-style trust claims.*

> "The more a user is able to click through and see where an answer came from, the more they'll be able to trust the content, even if they don't choose to check every source every time."
>
> — [12:34](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=754s) &middot; *Explains why citations work even when unused — availability, not usage, builds trust.*

> "how often would you share content from an unverifiable source if you knew that any errors would ultimately be attached back to your own name?"
>
> — [13:12](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=792s) &middot; *Reframes citations as reputation infrastructure for the user, not just accuracy checking.*

> "if you're creating some kind of an agentic tool and no plan is ever shown to the user and an action happens without them understanding why or how, it can be very, very hard for them to trust both the result of that action and the agentic tool itself"
>
> — [15:03](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=903s) &middot; *Concrete design mandate for agentic products.*

> "our own personal opinions on AI-generated content don't really matter too much in this context. What's more important is the awareness that our users will react to AI-generated content in a wide variety of ways and not all of those ways are going to be positive."
>
> — [16:40](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1000s) &middot; *Sidesteps the culture war to make a pragmatic design argument.*

> "I've noticed that there can be a kind of impulse to frame AI to our users as magic, right? We don't even have to look further than the prevalence of the sparkle icon to designate AI as an example of that."
>
> — [18:50](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1130s) &middot; *Names a widespread design convention and criticizes it.*

> "AI is just another technology, and our users deserve clarity over dramatics."
>
> — [18:50](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1130s) &middot; *Compact statement of her anti-mystification position.*

> "if we start showing a partial response as it's being generated, we give users the chance to start assessing it immediately"
>
> — [19:30](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1170s) &middot; *The functional (not cosmetic) argument for streaming.*

> "a 1-minute wait has become a 5-to-10-minute side quest, making it much harder to pick up where you left off"
>
> — [20:07](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1207s) &middot; *Quantifies the hidden productivity cost of latency and disengagement.*

> "If the user is unable to abort the process, then they're not actually the one in control, and frankly, that's not really acceptable."
>
> — [23:29](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1409s) &middot; *The strongest normative stance in the talk.*

> "now that we're dealing with non-deterministic output, having some kind of a version history is going to be pretty much a non-negotiable"
>
> — [24:12](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1452s) &middot; *Ties a specific UX requirement directly to a property of the technology.*

> "If you want to create a system that can remember things, then you also need to make sure that it can forget and that the user can not only see, but has the final say in what exactly gets remembered."
>
> — [28:37](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1717s) &middot; *A clean design rule for AI memory features.*

> "when we place a blank text box in front of a user and just tell them to ask AI, we're actually kind of asking them to do a lot of work in figuring out how to really use it"
>
> — [31:32](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1892s) &middot; *Criticizes the default chat-box UI as offloading labor onto users.*

> "the differentiator for the AI-powered software we build isn't performance anymore. It's the quality of the experiences that we can build around them."
>
> — [34:16](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=2056s) &middot; *The talk's closing strategic claim and the reason the rest matters.*

## Positions

- The developer-to-user knowledge gap for AI is the widest the speaker has observed for any technology. ([3:25](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=205s), confidence: stated)
- AI cannot be used to design AI interfaces well, because it can only remix existing patterns and standardized AI interface patterns do not yet exist. ([7:40](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=460s), confidence: stated)
- AI-generated UI is acceptable as a starting point but not as a finished design, and is fine for something simple like a quick landing page. ([8:24](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=504s), confidence: stated)
- No AI tool can currently be claimed to be 100% hallucination-free. ([11:15](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=675s), confidence: stated)
- Marketing your AI as more trustworthy than competitors is both questionably true and ineffective, since most teams are not training their own models. ([11:54](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=714s), confidence: stated)
- Uncitable AI output will not be used, because users need an accuracy trail to protect their own credibility when repurposing it. ([13:12](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=792s), confidence: stated)
- Agentic tools should show an action plan and get user approval before executing, with settings to toggle that off for repeated flows. ([15:03](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=903s), confidence: stated)
- All AI-generated content should be explicitly marked as AI-generated, regardless of the builder's own stance on AI content. ([17:23](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1043s), confidence: stated)
- Framing AI as magic (e.g. the sparkle icon) is inaccurate and users are better served by clarity. ([18:50](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1130s), confidence: stated)
- Streaming output is preferable to waiting for a complete response because it lets users assess and abort early, and keeps them engaged. ([19:30](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1170s), confidence: stated)
- An always-available, prominent stop control is a hard requirement; if a user cannot abort, they are not in control. ([23:29](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1409s), confidence: stated)
- Version history is non-negotiable for non-deterministic output, but Git-style version control is more than a user-facing application needs. ([24:56](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1496s), confidence: stated)
- Rising token costs make granular, targeted revision more valuable than regenerating from scratch. ([26:17](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1577s), confidence: stated)
- Permissions for AI agents must be non-binary and revocable, with a visible history of what was granted and when. ([29:20](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1760s), confidence: stated)
- Users should be shown a time and cost estimate before approving an AI action, even if only a rough one. ([30:02](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1802s), confidence: stated)
- A blank 'ask AI' text box is a design failure because it assumes AI literacy users don't have; examples, templates, and guided workflows should be provided instead. ([31:32](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1892s), confidence: stated)
- Model performance is no longer the competitive differentiator for AI software; experience quality is. ([34:16](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=2056s), confidence: stated)
- UX and interaction design are now part of the developer's job whether or not their title says designer. ([35:05](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=2105s), confidence: stated)

## Concepts

- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [citation and grounding](../concepts/citation-and-grounding.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [mechanistic interpretability](../concepts/mechanistic-interpretability.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [session management](../concepts/session-management.md)

