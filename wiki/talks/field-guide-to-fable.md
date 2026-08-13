---
title: "Field Guide to Fable"
type: "talk"
slug: "field-guide-to-fable"
track: "Autoresearch"
org: "Anthropic"
day: "Day 3 — Session Day 2"
room: "Main Stage"
video_id: "9fubhllmsBU"
duration_sec: 1168
word_count: 3542
speakers: ["Thariq Shihipar"]
---

# Field Guide to Fable

**Speakers:** [Thariq Shihipar](../speakers/thariq-shihipar.md)

**Org:** Anthropic

**Track:** Autoresearch &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 19m 28s

[Watch on YouTube](https://www.youtube.com/watch?v=9fubhllmsBU)

## Summary

Thariq Shihipar, who works on Claude Code at Anthropic, gives a practical field guide to working with Fable, Anthropic's new frontier model, framed as an 'open world' that has just unlocked after the tutorial. His central argument is that models are grown rather than designed, so what limits them is our harness and prompting — the work of 'unhobbling' Claude is discovering capability overhang, like giving the model a bash tool instead of a bigger context window. The second half is about unhobbling yourself: with a model that explores this much territory, the bottleneck becomes the gap between your mental map and the actual codebase, so he offers concrete techniques (blind-spot passes, brainstorm prototypes, having Claude interview you, reference implementations, implementation notes, quizzing yourself) for surfacing your unknowns before Claude hits them. He closes on the emotional cost of losing hand-written coding, and an exhortation to be 'unreasonable' — refuse implicit tradeoffs, do more ambitious work, and remember that building got easy while generating value did not. Worth watching for prompting practice with the newest models and for Anthropic-internal signals like the 80% system-prompt reduction in Claude Code.

## Key Points

- Models are grown rather than designed, so their practical ceiling is set by the harness and prompts we build around them — 'unhobbling' means improving our understanding of the model, not the model itself.
- Capability gains are spiky, not uniform: a chat model can't name the Pokémon ending in 'aw', but Claude Code can because it fetches the list and writes a filter script — the unlock was the code execution tool, not more knowledge.
- The insight behind Claude Code was that giving a model 'arms' (bash, environment access) to build and search its own context beats trying to paste an entire codebase into an enormous context window.
- System prompt best practices have inverted across model generations: small prompts with few tools, then large prompts with many examples and tools, and now smaller prompts again because examples constrain a model that is more imaginative than the examples.
- Anthropic recently removed 80% of the Claude Code system prompt, and now favors giving the model context rather than negative constraints like 'do not do this'.
- The gap between your mental map (prompt, spec, plan) and the territory (real codebase and constraints) produces 'unknowns' — unspecified decision points — and Fable traverses enough territory that it hits many of them.
- You can use the model itself to surface unknowns: blind-spot passes over unfamiliar modules, multi-variant HTML prototypes to elicit taste you can't articulate, having Claude interview you with questions that would change the architecture, and passing reference code as a map.
- Ask Fable to log implementation notes when it deviates, and to quiz you afterward, so you stay in the loop and can defend the work at PR time.
- Tradeoffs that used to be forced by the cost of code (fast vs. new features, good vs. fast vs. cheap) should now be treated as suspect — force reality to show you the tradeoff instead of assuming it.
- Building is easier but generating value is still hard; AI engineers over-focus on process and setup when the goal is value creation, which still takes many swings.

## Notable Quotes

> "something we say really often is that the models are grown, not designed, right?"
>
> — [2:29](https://www.youtube.com/watch?v=9fubhllmsBU&t=149s) &middot; *the framing the whole talk rests on*

> "what contains them is us, right? The harness we put them in and the way we prompt them is basically like a function of our understanding of Claude"
>
> — [2:29](https://www.youtube.com/watch?v=9fubhllmsBU&t=149s) &middot; *states the core thesis that the harness, not the model, is the bottleneck*

> "We call this capability overhang, right? Claude gets smarter in spiky ways."
>
> — [3:59](https://www.youtube.com/watch?v=9fubhllmsBU&t=239s) &middot; *names the central concept in one line*

> "if you give it arms, like you give it the bash tool and ways to work with the environment, it can build and search its own context. And that's sort of like the insight that led to Claude Code"
>
> — [5:14](https://www.youtube.com/watch?v=9fubhllmsBU&t=314s) &middot; *insider account of the design decision behind Claude Code, and a position against giant context windows*

> "we recently removed 80% of the system prompt for Claude code"
>
> — [5:47](https://www.youtube.com/watch?v=9fubhllmsBU&t=347s) &middot; *concrete number about production prompting practice*

> "The examples tend to constrain it cuz it's actually more imaginative than the examples we give it."
>
> — [6:26](https://www.youtube.com/watch?v=9fubhllmsBU&t=386s) &middot; *reverses a widely held few-shot prompting convention*

> "we tried to give it context and not just constraints. We're really trying to avoid being like, "Do not do this.""
>
> — [6:26](https://www.youtube.com/watch?v=9fubhllmsBU&t=386s) &middot; *actionable prompting guidance that contradicts older negative-instruction habits*

> "I really like to emphasize that this is closer to a biology than a physics, right? It's still very empirical, very organic."
>
> — [8:19](https://www.youtube.com/watch?v=9fubhllmsBU&t=499s) &middot; *crisp epistemic stance on how to reason about model behavior*

> "the plan and prompt and spec that I have in my mind is the map, right? But the territory is the actual code base, the real world, the constraints that Claude needs to navigate"
>
> — [8:58](https://www.youtube.com/watch?v=9fubhllmsBU&t=538s) &middot; *sets up the talk's second half*

> "whenever Claude runs into something in the territory that's not in the map, I call that an unknown"
>
> — [8:58](https://www.youtube.com/watch?v=9fubhllmsBU&t=538s) &middot; *defines the unit of analysis for his prompting workflow*

> "Fable is one of the first models where I felt that like I really have to figure out my unknowns because if not, it's going to traverse such a large area that like it's going to run into a lot of them."
>
> — [9:37](https://www.youtube.com/watch?v=9fubhllmsBU&t=577s) &middot; *explains why more capable models raise, not lower, the specification burden*

> "I like to do what I call a blind spot pass."
>
> — [10:46](https://www.youtube.com/watch?v=9fubhllmsBU&t=646s) &middot; *names the most reusable technique in the talk*

> "in many ways, the model knows more about you know, almost everything than I do. I just need to get it out of it."
>
> — [11:25](https://www.youtube.com/watch?v=9fubhllmsBU&t=685s) &middot; *reframes the user's job as elicitation rather than instruction*

> "One of the best ways to give Claude a map is to give it another map"
>
> — [12:37](https://www.youtube.com/watch?v=9fubhllmsBU&t=757s) &middot; *compact argument for reference implementations over written specs*

> "It was like the things that would have taken me weeks, I could do in hours"
>
> — [15:03](https://www.youtube.com/watch?v=9fubhllmsBU&t=903s) &middot; *his personal magnitude estimate on a real legacy codebase*

> "One of my favorite parts of Anthropic is that we believe that tradeoffs are not real."
>
> — [16:20](https://www.youtube.com/watch?v=9fubhllmsBU&t=980s) &middot; *a contestable cultural claim other speakers would push back on*

> "But what if you just did all of it, you know? What if you forced reality to show you the tradeoff, right?"
>
> — [17:00](https://www.youtube.com/watch?v=9fubhllmsBU&t=1020s) &middot; *the operational version of 'be unreasonable'*

> "there are so many tradeoffs that you make implicitly in your head, right? Like good, fast, cheap. Now it's pick three, right?"
>
> — [17:00](https://www.youtube.com/watch?v=9fubhllmsBU&t=1020s) &middot; *memorable inversion of the classic triangle*

> "I think the only way to prove that agents work is to do the best work of our lives faster than ever before"
>
> — [17:39](https://www.youtube.com/watch?v=9fubhllmsBU&t=1059s) &middot; *the talk's call to action, aimed squarely at the audience*

> "for example, I made this deck last night in about 4 hours with Fable"
>
> — [17:39](https://www.youtube.com/watch?v=9fubhllmsBU&t=1059s) &middot; *self-referential evidence with a specific number*

> "it's also worth calling out that building is easier, but generating value is still hard"
>
> — [18:13](https://www.youtube.com/watch?v=9fubhllmsBU&t=1093s) &middot; *the counterweight that keeps the talk from being pure hype*

## Positions

- Model capability is limited primarily by the harness and prompting around it, not by the model's underlying knowledge. ([2:29](https://www.youtube.com/watch?v=9fubhllmsBU&t=149s), confidence: stated)
- Giving a model tools to search and build its own context is a better path than scaling context windows to fit an entire codebase. ([5:14](https://www.youtube.com/watch?v=9fubhllmsBU&t=314s), confidence: stated)
- The newest class of models performs better with a smaller system prompt, because in-prompt examples constrain a model that is more imaginative than the examples. ([6:26](https://www.youtube.com/watch?v=9fubhllmsBU&t=386s), confidence: stated)
- Anthropic removed 80% of the Claude Code system prompt. ([5:47](https://www.youtube.com/watch?v=9fubhllmsBU&t=347s), confidence: stated)
- Negative instructions ('do not do this'), which were necessary for previous models, should be replaced with context for current models. ([6:26](https://www.youtube.com/watch?v=9fubhllmsBU&t=386s), confidence: stated)
- Understanding model behavior is an empirical, biology-like discipline rather than a physics-like one with known rules. ([8:19](https://www.youtube.com/watch?v=9fubhllmsBU&t=499s), confidence: stated)
- More capable models increase rather than decrease the need for upfront specification, because they cover more territory and hit more unspecified decision points. ([9:37](https://www.youtube.com/watch?v=9fubhllmsBU&t=577s), confidence: stated)
- The human's bottleneck when working with Fable is their own ability to match map to territory and identify unknowns. ([9:37](https://www.youtube.com/watch?v=9fubhllmsBU&t=577s), confidence: stated)
- Passing existing code or an HTML mockup as a reference is more effective than writing out a spec in prose. ([12:37](https://www.youtube.com/watch?v=9fubhllmsBU&t=757s), confidence: stated)
- Claude Tag's unlock was the model's ability to work proactively and in multiplayer, which is what enables the next wave of agents. ([5:14](https://www.youtube.com/watch?v=9fubhllmsBU&t=314s), confidence: stated)
- Many product tradeoffs previously imposed by the cost of writing code are no longer real and should be tested rather than assumed. ([16:20](https://www.youtube.com/watch?v=9fubhllmsBU&t=980s), confidence: stated)
- The burden of proof that AI agents work rests on AI engineers producing their best work faster, not on benchmarks or claims. ([17:39](https://www.youtube.com/watch?v=9fubhllmsBU&t=1059s), confidence: stated)
- AI engineers over-invest in build process and tooling setups relative to the harder problem of generating value. ([18:13](https://www.youtube.com/watch?v=9fubhllmsBU&t=1093s), confidence: implied)
- Despite genuine loss of the craft of hand-written code, returning to pre-LLM programming is not a viable option. ([15:37](https://www.youtube.com/watch?v=9fubhllmsBU&t=937s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [context window management](../concepts/context-window-management.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [prompt engineering](../concepts/prompt-engineering.md)
- [requirements elicitation](../concepts/requirements-elicitation.md)

