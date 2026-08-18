---
title: "Anthropic's CCA Exam as a Field-Guide for Agentic Engineering"
type: "talk"
slug: "anthropics-cca-exam-as-a-field-guide-for-agentic-engineering"
track: "Agentic Engineering"
org: "UC Berkeley"
day: "Day 4 — Session Day 3"
room: "Track 8"
video_id: "Z-c11pV_uvU"
duration_sec: 1208
word_count: 2938
speakers: ["Frank Coyle"]
---

# Anthropic's CCA Exam as a Field-Guide for Agentic Engineering

**Speakers:** [Frank Coyle](../speakers/frank-coyle.md)

**Org:** UC Berkeley

**Track:** Agentic Engineering &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 20m 08s

[Watch on YouTube](https://www.youtube.com/watch?v=Z-c11pV_uvU)

## Summary

Frank Coyle, a computer science instructor at UC Berkeley, uses Anthropic's newly released Claude Certified Architect (CCA) exam as a lens for teaching agentic engineering practice. His argument is that the exam's five domains and six production scenarios encode what Anthropic has learned about how people actually build with Claude, so studying it is useful even if you never sit for it. The talk's organizing device is anti-patterns: for each scenario (customer support loops, code generation with CLAUDE.md, multi-agent research, developer productivity, CI), he names the wrong move first — ignoring stop_reason, overloading one agent with every tool, letting subtask output flood the primary context, running interactive mode in a pipeline — on the theory that knowing what not to do is the key to knowing what to do. He also grounds the current excitement about agent loops in Böhm and Jacopini's 1966 result on Turing completeness, arguing loops aren't new, just newly available to LLM systems. Watch it for a compact, practitioner-level map of agent design tradeoffs and exam logistics; skip it if you want deep implementation detail, since the code walkthroughs stay at the sketch level.

## Key Points

- The Claude Certified Architect exam was released in March, is timed and proctored, costs $99 for individuals who can retake it once every six months, and uses multiple-choice questions built around realistic production constraints rather than trivia.
- The exam covers five weighted domains — agentic architecture at 27%, Claude Code configuration and workflow at 20%, plus prompt engineering and structured output, tool design and MCP integration, and context management and reliability.
- Six production scenarios exist and the exam randomly selects four for any given sitting, with all questions centered on those four.
- Checking stop_reason on every loop iteration is the core agentic loop discipline: it tells you whether the model wants a tool run, finished normally, or hit a token limit and returned a partial response requiring action.
- The LLM never executes tools itself — it is a probabilistic next-word predictor that extracts and formats the parameters your code then uses to actually run the tool.
- Agents should be specialized rather than overloaded with tools, echoing functional programming's rule that a function does one thing; Coyle's analogy is hiring a carpenter who shows up with plumbing and electrical tools too.
- Subagents should receive only the slice of context they need — passing a critic agent just the claim and evidence, not the reasoning that produced them — because collaborating agents that see each other's thinking devolve into groupthink.
- Context isolation and compaction are the defense against unbounded growth: fork subtasks so their tokens don't pollute the main thread, return only summaries, and trigger compaction past a threshold like 150,000 tokens.
- For CI, disable interactive permission prompts so pipelines run straight through, and use batch mode for a 50% token cost reduction with results promised within 24 hours.

## Notable Quotes

> "I think anti-patterns are a key to understanding what you should not do because understanding what you should not do is the key to leading you to what you should do."
>
> — [1:53](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=113s) &middot; *States the organizing thesis of the entire talk.*

> "I feel that Anthropic knows how people are using their system and what the issues are going to be."
>
> — [1:03](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=63s) &middot; *The justification for treating a vendor certification as a field guide.*

> "It is timed. It is proctored. It is available to companies in the Claude ecosystem, the Anthropic ecosystem, but individuals can pay $99 and take the exam once every once every 6 months."
>
> — [2:41](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=161s) &middot; *Concrete logistics and pricing for anyone considering the exam.*

> "So, agentic architecture, 27%. Claude code, how to configure the Claude code system and workflow, 20%."
>
> — [2:41](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=161s) &middot; *Reports the actual domain weightings.*

> "they provide you with six production scenarios and your the exam will randomly choose four and all the questions will be centered around the four that they choose"
>
> — [3:35](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=215s) &middot; *Explains the exam's structure, which shapes how to study for it.*

> "Keep the little threads independent. Keep your agents independent."
>
> — [5:03](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=303s) &middot; *Compresses the multi-threading analogy into the talk's central design rule.*

> "Böhm and Jacopini, 1966 proved that if you want a language to be Turing complete, which means can compute anything that computers are possibly able to compute, then you need only three things."
>
> — [6:43](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=403s) &middot; *The historical grounding for his contrarian take on loop hype.*

> "So, loops are the new big thing, right? Well, no, they're not."
>
> — [5:56](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=356s) &middot; *A direct pushback on a widely repeated 2026 framing.*

> "The problem is the LLM can't do anything. It is just a probabilistic next word predictor. It can't execute tools."
>
> — [8:19](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=499s) &middot; *The mechanical fact behind the tool-use loop that beginners most often get wrong.*

> "One of the stop reasons may be you have run out of tokens, and this response is based on partial when the LLM had to stop."
>
> — [10:45](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=645s) &middot; *Names the specific failure mode that makes stop_reason checking non-optional.*

> "you hire a carpenter to come to the house, and the guy shows up with uh plumbing tools, carpenter tools, electrical tools. He says, "I can do anything." Well, maybe you don't want this guy, maybe you want a a professional carpenter."
>
> — [12:21](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=741s) &middot; *The talk's most memorable framing of the tool-overload anti-pattern.*

> "So, specialize, don't overload."
>
> — [13:02](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=782s) &middot; *The compressed prescription for multi-agent design.*

> "don't let your agents context spill over into the main context because context means tokens, tokens mean money, and the more context you have, the more confused the LLM is going to be in giving you an answer"
>
> — [13:02](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=782s) &middot; *Ties context isolation to both cost and accuracy in one line.*

> "even though oh, a million token context window, I can put everything in there. No, no, don't put everything in there. Limit what's going to go in there because then you're going to get a much more accurate system."
>
> — [13:02](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=782s) &middot; *Takes a side against the large-context-window-solves-everything view.*

> "When you get a bunch of agents together collaborating and talking to each other, there's a tendency to have group think. And all the agents seem to kind of devolve into one idea."
>
> — [13:52](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=832s) &middot; *Names a multi-agent failure mode that motivates restricting subagent context.*

> "Every agent gets its own slice"
>
> — [14:39](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=879s) &middot; *The talk's mnemonic for per-agent context scoping.*

> "Let every subtask dump its full output into the primary thread, crowding out the context."
>
> — [14:39](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=879s) &middot; *The verbatim statement of the developer-productivity anti-pattern.*

> "if you have more than 150,000 tokens, then what you want to do is you can run a compact"
>
> — [16:26](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=986s) &middot; *A concrete numeric threshold for triggering compaction.*

> "Always have interactive modes in a pipeline. Well, no no no cuz interactive modes mean uh Cloud will stop and ask you, "You want to do this? You want to do that? Can I have permission for that?""
>
> — [17:15](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=1035s) &middot; *The CI anti-pattern stated with its reason.*

> "you can put them in a batch and for 50% fewer token cost you will get the result they promise in at at least 24 hours"
>
> — [17:54](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=1074s) &middot; *A specific cost/latency tradeoff engineers can act on immediately.*

## Positions

- Studying the CCA exam is worthwhile even for people who never take it, because Anthropic's scenario choices reveal what actually breaks in production agentic systems. ([1:03](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=63s), confidence: stated)
- Anti-patterns are more pedagogically useful than patterns, because knowing what not to do leads you to what to do. ([1:53](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=113s), confidence: stated)
- The current excitement about agent loops is not a new idea — Böhm and Jacopini established in 1966 that sequence, conditionals, and loops are all you need for Turing completeness. ([6:43](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=403s), confidence: stated)
- An agentic loop must branch on stop_reason rather than simply consuming the model's first response, or it will silently accept truncated output when tokens run out. ([10:45](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=645s), confidence: stated)
- Agents should be given one or two tools and a single job rather than a large tool inventory. ([12:21](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=741s), confidence: stated)
- Subagents should receive only the claim and evidence, not the reasoning that produced them, to avoid convergent groupthink across agents. ([13:52](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=832s), confidence: stated)
- Filling a million-token context window degrades answer accuracy; limiting context produces a more accurate system. ([13:02](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=782s), confidence: stated)
- Interactive permission prompts should be disabled when running Claude Code in a CI pipeline. ([17:15](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=1035s), confidence: stated)
- Batch mode costs 50% fewer tokens with results delivered within 24 hours, making it the right choice for non-urgent work. ([17:54](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=1074s), confidence: stated)
- Computer science is no longer a reliable pathway to a job, which is why students need explicit preparation for agentic AI work. ([0:01](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=1s), confidence: stated)
- Multi-threaded programming's lessons about shared memory and synchronization transfer directly to multi-agent system design. ([5:03](https://www.youtube.com/watch?v=Z-c11pV_uvU&t=303s), confidence: implied)

## Concepts

- [agent tool design](../concepts/agent-tool-design.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [context compaction](../concepts/context-compaction.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

