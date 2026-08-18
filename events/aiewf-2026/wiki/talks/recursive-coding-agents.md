---
title: "Recursive Coding Agents"
type: "talk"
slug: "recursive-coding-agents"
track: "Software Factories"
org: "OpenProse"
day: "Day 2 — Session Day 1"
room: "Main Stage"
video_id: "3hXJI2q0Jz8"
duration_sec: 1428
word_count: 3697
speakers: ["Lee Robinson"]
---

# Recursive Coding Agents

*Program title: Recursive Model Improvement*

**Speakers:** [Lee Robinson](../speakers/lee-robinson.md)

**Org:** OpenProse

**Track:** Software Factories &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 23m 48s

[Watch on YouTube](https://www.youtube.com/watch?v=3hXJI2q0Jz8)

## Summary

Raymond Weitekamp argues that the bottleneck to trustworthy agents is not model intelligence but orchestration — today's agents are 'mismanaged geniuses' whose missing layer is how work gets specified, managed, reused, and verified. He presents recursive language models (RLMs), where the prompt is externalized as a variable manipulated symbolically in a REPL and the model decides how to decompose the problem into recursive sub-agent calls, as the next paradigm of test-time compute unifying reasoning and tool calling. He cites strong empirical results: RLMs processing tens of millions of tokens, a default RLM harness performing like a top-10 memory system, Qwen 3.5 9B as an RLM beating frontier LLMs on the Long CoT benchmark, and Symbolica's Agentica jumping ARC-AGI-3 from ~2-3% to 30-something percent within hours. He then applies these principles to coding agents through concrete artifacts: a py extension making the pi coding agent fully self-recursive, Claude Code dynamic workflows, and OpenProse, a markdown 'programming language' compiled by your coding agent that declares sub-agent decomposition, verification, and skill/tool dependencies. Worth watching if you want a rubric for what actually counts as recursion versus a hardcoded map-reduce, plus a practical path to turning any coding agent into an RLM.

## Key Points

- The claimed bottleneck to reliable agentic outcomes is not raw intelligence but the orchestration layer — how work is specified, managed, reused, and verified — which the speaker frames via Alex Zeng, Z Li, and Omar Khattab's 'mismanaged genius' phrase.
- In an RLM the context itself is the object of computation: the full prompt is externalized as a variable (a file or many files) that the agent explores symbolically in a REPL rather than reading wholesale into its context window.
- The speaker's rubric for a true RLM requires an executable environment, an externalized prompt, code that calls the model, model-chosen decomposition into sub-calls, and state that stays symbolic — which excludes plain LLMs, RAG, and hardcoded map-reduces like lambda RLM.
- Reported results include RLMs handling tens of millions of tokens, an unmodified RLM harness scoring like a top-10 memory system, and Qwen 3.5 9B as an RLM beating Opus and GPT-5.4 as LLMs on the Long CoT benchmark.
- Symbolica's Agentica harness scored 30-something percent on ARC-AGI-3 within hours of release against frontier baselines of two or three percent, and the ARC Prize team declined the full private evaluation because they don't like RLM harnesses — which the speaker calls insane and answers with a call for separate open-harness leaderboards.
- The speaker built y-pi and a pure pi-recursive extension so the pi coding agent literally calls itself to arbitrary depth, something that previously required forking pi but now works as a plain extension.
- Claude Code's dynamic workflows, released a few weeks before the talk, arguably make it an RLM — Omar Khattab publicly congratulated Anthropic — but the speaker notes dynamic workflows are Claude-Code-only and not the only route.
- OpenProse is a markdown-based 'programming language' compiled by your coding agent rather than your computer; it explicitly declares sub-agent decomposition, parent-session verification, and skills/CLI tools as hard dependencies, turning any agent with a file system and sub-agents into an RLM.
- A newly added OpenProse capability deconstructs a 'golden session' from Claude Code, Codex, or pi into a reusable recursive Prose workflow, attacking day-to-day reliability variance directly.

## Notable Quotes

> "And my argument and my experience is that the bottleneck to this is not intelligence."
>
> — [0:00](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=0s) &middot; *States the talk's central thesis in one line.*

> "The models are intelligent enough. They know all kinds of things. They know the entire internet. But they can't reliably deliver outcomes. And so I can't trust them."
>
> — [0:52](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=52s) &middot; *Frames reliability, not capability, as the gap.*

> "one day I get almost a fully working SaaS app from a single prompt, granted a long prompt. The next day, and I swear this actually happened, cloud code empties the entire contents of my Solana wallet."
>
> — [0:52](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=52s) &middot; *The concrete variance anecdote that motivates the whole talk.*

> "today's agents are mismanaged geniuses. The intelligence is there, and the missing layer is how do we specify and manage and reuse and verify the work."
>
> — [1:38](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=98s) &middot; *The thesis statement and the framing borrowed from the RLM authors.*

> "in an RLM, the context itself is the object of computation"
>
> — [2:23](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=143s) &middot; *The most compact definition of RLMs given.*

> "The full prompt is a variable. The full prompt could be a file or many files."
>
> — [3:05](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=185s) &middot; *Names the specific mechanism that distinguishes RLMs from prompting.*

> "RLMs are the new reasoning models and I see this as the next paradigm of test time compute"
>
> — [4:13](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=253s) &middot; *The strongest forward-looking claim in the talk.*

> "the RLMs can process information that is many orders of magnitude larger than their context window, tens of millions of tokens"
>
> — [5:01](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=301s) &middot; *Headline quantitative claim from the original paper.*

> "RLM with no modifications is essentially like a top 10 memory system and like you know, up there with all the people custom making memory systems and there's probably billions of dollars going into that."
>
> — [5:01](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=301s) &middot; *A pointed competitive claim against the memory-systems category.*

> "Qwen 3.59B as an RLM can beat Opus and um and GPT-5.4, all the top frontier models as LLMs on these long reasoning tasks"
>
> — [6:35](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=395s) &middot; *The small-model-beats-frontier result that anchors the argument.*

> "They blew it out of the water within hours using RLMs as a framework."
>
> — [7:44](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=464s) &middot; *Summarizes the ARC-AGI-3 result driving the benchmarking controversy.*

> "we refuse to actually do the full private part of the ArcadeGI evaluation. Uh, which to me is just insane."
>
> — [7:44](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=464s) &middot; *Takes an explicit side in a live benchmarking dispute.*

> "So, my take on this is I don't care. I don't care whether it's latent space or reasoning tokens or code execution. I want results. And I want AI programs that get those results."
>
> — [8:42](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=522s) &middot; *Outcome-over-purity stance that others in the field would contest.*

> "the model is able to pick the decomposition of the problem into the sub calls or sub agents, and the state itself is staying symbolic"
>
> — [9:21](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=561s) &middot; *The rubric criteria that separate real RLMs from near-misses.*

> "the LLM is not deciding or the RLM is not deciding how to decompose the problem. And that I see as like a key element of this that makes it very agent native"
>
> — [9:59](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=599s) &middot; *Draws the definitional line against hardcoded map-reduce.*

> "now pie has evolved um and the pie extensions have evolved such that you can uh make it fully recursive with a pure extension"
>
> — [13:02](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=782s) &middot; *Reports a concrete engineering result updated for the talk.*

> "open prose is technically a programming language, but it is not compiled by your computer. It's compiled by your coding agent."
>
> — [17:01](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=1021s) &middot; *The defining description of OpenProse.*

> "there's a way in Pros to actually wire those in as dependencies to ensure that um not only that the way the work is done um is what you want, but actually that the sub agents are specifically configured with the tools and skills that they need"
>
> — [19:02](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=1142s) &middot; *Names the specific reliability mechanism OpenProse adds over plain sub-agents.*

> "trust is reliability"
>
> — [21:27](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=1287s) &middot; *The first of three closing takeaways, stated bluntly.*

> "the next step is not, um, more raw intelligence. It's actually, uh, behavioral. It's actually orchestration."
>
> — [22:12](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=1332s) &middot; *The closing restatement of the thesis, and the claim most open to disagreement.*

> "Yes, coding agents can be LLMs. They aren't automatically LLMs."
>
> — [23:05](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=1385s) &middot; *Settles the talk's recurring definitional question (transcript renders RLM as LLM here).*

## Positions

- The bottleneck to reliable agent outcomes is orchestration and behavior, not model intelligence. ([22:12](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=1332s), confidence: stated)
- RLMs are the next paradigm of test-time compute, unifying reasoning and tool calling. ([4:13](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=253s), confidence: stated)
- An unmodified default RLM harness performs comparably to a top-10 purpose-built memory system. ([5:01](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=301s), confidence: stated)
- Qwen 3.5 9B run as an RLM beats Opus and GPT-5.4 run as plain LLMs on the Long CoT benchmark. ([6:35](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=395s), confidence: stated)
- The ARC Prize team's refusal to run the full private evaluation for Symbolica's RLM harness result was unjustified. ([7:44](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=464s), confidence: stated)
- Benchmarks should maintain a separate open-harness leaderboard rather than excluding RLM results outright. ([8:42](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=522s), confidence: stated)
- It does not matter whether performance comes from latent space, reasoning tokens, or code execution — only results matter. ([8:42](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=522s), confidence: stated)
- A system only qualifies as an RLM if the model itself chooses the decomposition; hardcoded map-reduce pipelines like lambda RLM do not qualify. ([9:59](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=599s), confidence: stated)
- Claude Code was not an RLM before dynamic workflows, but with dynamic workflows it now arguably is. ([15:26](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=926s), confidence: stated)
- Coding agents are not automatically RLMs, though they can be made into them. ([23:05](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=1385s), confidence: stated)
- Any coding agent with a file system and sub-agents can be converted into an RLM using OpenProse, without depending on Claude Code's dynamic workflows. ([17:36](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=1056s), confidence: stated)
- Capturing a successful 'golden session' as a reusable declarative workflow is a viable route to making agent performance repeatable. ([20:48](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=1248s), confidence: implied)
- Trust in an agent is reducible to its reliability. ([21:27](https://www.youtube.com/watch?v=3hXJI2q0Jz8&t=1287s), confidence: stated)

## Concepts

- [agent memory](../concepts/agent-memory.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [long-context processing](../concepts/long-context-processing.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)
- [task decomposition](../concepts/task-decomposition.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)

