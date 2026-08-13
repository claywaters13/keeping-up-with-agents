---
title: "RLM: Recursive Language Models for Large Codebases"
type: "talk"
slug: "rlm-recursive-language-models-for-large-codebases"
org: "Superagentic AI"
video_id: "8oyalrfwgjw"
duration_sec: 1047
word_count: 2433
speakers: ["Shashi"]
---

# RLM: Recursive Language Models for Large Codebases

**Speakers:** [Shashi](../speakers/shashi.md)

**Org:** Superagentic AI

**Duration:** 17m 27s

[Watch on YouTube](https://www.youtube.com/watch?v=8oyalrfwgjw)

## Summary

Shashi, founder of Superagentic AI, explains MIT's Recursive Language Models (RLM) pattern and argues it is the right context-management strategy for large monorepos, where coding-agent performance degrades as context grows. The core thesis he relays is that context management should be externalized into a programmable execution environment: the repository is treated as data, the model writes REPL code to inspect and slice it, and when it needs more it recursively calls another model via an LLM query, returning bounded observations until a final synthesized answer. He frames this with an analogy to a lead engineer joining a huge codebase — inspecting, note-taking, and asking a specialist — and distinguishes codebases from books because they are structured data with imports, tests, configs, and dependencies. The talk includes a live demo of RLM Code, Superagentic's open-source reference harness (CLI plus an experimental coding-agent TUI) running against Gemini in a Docker sandbox, showing REPL code, sub-calls, budgets, token counts, and JSONL traces. He closes by claiming RLM-shaped patterns already appear in proprietary harnesses like Codex and managed cloud agents. Worth watching if you want a concrete, implementation-level picture of the RLM loop rather than the paper itself.

## Key Points

- Coding agents work well on small repos but degrade on monorepos, because performance falls as the context window fills up.
- The RLM core thesis is to externalize context management into a separate programmable execution environment rather than stuffing everything into the model's context window.
- In RLM the repository is treated as data the model operates on: it writes REPL code to inspect, slice, and compute the relevant chunks that get fed into the main context.
- Recursion enters via an LLM query — the model asks another model or system one or more questions, gets a bounded observation back, and continues the loop until a final result.
- Shashi frames RLM through a lead-engineer analogy: inspect the codebase, keep notes in a programmable REPL notebook, ask a specialist when stuck, and return a clean synthesized note.
- Codebases are a deliberately chosen test case because they are structured data — directories, imports, tests, configs, dependencies — not just long text.
- RLM is a pattern, not a library: the official authors shipped RLM and RLM-minimal implementations and a DSPy integration, and Superagentic built RLM Code as an independent open-source reference harness.
- RLM Code is provider-agnostic (local or cloud models), sandboxed in Docker, supports step/recursion-depth and spend budgets, and emits JSONL traces importable into any observability platform.
- Practical use cases named are root-cause analysis and onboarding onto large or unfamiliar repositories, where you design your own harness capturing planning, coding, observation, sub-call budget, and final output.
- Shashi claims RLM-style patterns are already inside proprietary systems — Codex writing Python in a REPL to curate context, and managed Claude/Gemini agents spawning sub-agents with separate sandboxes.

## Notable Quotes

> "If you're using the coding agents for smaller repos or monor repos, they works exceptionally well."
>
> — [0:45](https://www.youtube.com/watch?v=8oyalrfwgjw&t=45s) &middot; *Sets up the scoping premise: the problem is size, not capability.*

> "as the context grows the performance degrade and if you're working with the monor repose this problem get worse"
>
> — [0:45](https://www.youtube.com/watch?v=8oyalrfwgjw&t=45s) &middot; *States the failure mode the whole talk is organized around.*

> "Core thesis of the RLM is you need to externalize the context management into programmable execution environment."
>
> — [1:27](https://www.youtube.com/watch?v=8oyalrfwgjw&t=87s) &middot; *The single-sentence statement of the pattern.*

> "In this case for example your whole repository is treated as a data that model can operate on."
>
> — [2:14](https://www.youtube.com/watch?v=8oyalrfwgjw&t=134s) &middot; *The key reframe — repo as data, not as context.*

> "Then model can write the code to inspect slice and compute the relevant chunks value you can then feed into the main context window."
>
> — [2:14](https://www.youtube.com/watch?v=8oyalrfwgjw&t=134s) &middot; *Describes the mechanism concretely.*

> "So basically rather than putting everything into the model's context create a separate dedicated environment give them a coding agent or ripple and then model write the code to curate the context that can be used into the main."
>
> — [2:14](https://www.youtube.com/watch?v=8oyalrfwgjw&t=134s) &middot; *Contrasts RLM directly against the stuff-the-window default.*

> "So it's another context management technique proved to be very effective. Could be also be used as a memory layer for your coding agents."
>
> — [2:14](https://www.youtube.com/watch?v=8oyalrfwgjw&t=134s) &middot; *Positions RLM relative to memory solutions, a claim others might contest.*

> "So the recussion part here is engineer ask another specialist using LLM query that can be one question or that can be number of questions."
>
> — [4:37](https://www.youtube.com/watch?v=8oyalrfwgjw&t=277s) &middot; *Pins down exactly where recursion lives in the loop.*

> "So the codebase is not only just um the text, it is a structured data and the model need to understand and reason over the text."
>
> — [5:37](https://www.youtube.com/watch?v=8oyalrfwgjw&t=337s) &middot; *Justifies why codebases, not books, are the chosen stress test.*

> "RLM itself is a concept and a pattern and you can implement that concept and pattern in your own way."
>
> — [6:36](https://www.youtube.com/watch?v=8oyalrfwgjw&t=396s) &middot; *The talk's stance that RLM is not a framework dependency.*

> "So Omar is author of RLM and he is also author of another popular framework called DSP."
>
> — [6:36](https://www.youtube.com/watch?v=8oyalrfwgjw&t=396s) &middot; *Attributes the ecosystem lineage and the DSPy connection.*

> "RLM code is just a reference implementation to demonstrate how the RLM concepts works under the hood."
>
> — [7:46](https://www.youtube.com/watch?v=8oyalrfwgjw&t=466s) &middot; *Sets honest expectations about the demoed library.*

> "We are using RLM as it is. We are not adding anything on top of RLM's ideas and RLM's paper."
>
> — [7:46](https://www.youtube.com/watch?v=8oyalrfwgjw&t=466s) &middot; *Explicit fidelity claim distinguishing implementation from invention.*

> "However, you can run it with the local model. You can run with run it with cloud-based model. You can plug into any observability framework of your choice."
>
> — [7:46](https://www.youtube.com/watch?v=8oyalrfwgjw&t=466s) &middot; *Names the portability tradeoff the harness is designed for.*

> "Recently I saw that the codeex harness is writing the Python Python code in the ripple that you can see to curate the context that is one form of RLM I have seen myself"
>
> — [15:55](https://www.youtube.com/watch?v=8oyalrfwgjw&t=955s) &middot; *Concrete evidence claim that shipped products already use the pattern.*

> "A lot of software factories concepts are probably using the RLMs but we are not sure yet. However, some of the cloud code engineers from anthropic has accepted on X that they have used concepts of RLM."
>
> — [16:51](https://www.youtube.com/watch?v=8oyalrfwgjw&t=1011s) &middot; *Rare moment of explicit uncertainty paired with a sourced claim.*

## Positions

- Coding agents perform well on small repos but degrade measurably on monorepos as context grows. ([0:45](https://www.youtube.com/watch?v=8oyalrfwgjw&t=45s), confidence: stated)
- Context management should be externalized into a separate programmable execution environment rather than loading everything into the model's context window. ([1:27](https://www.youtube.com/watch?v=8oyalrfwgjw&t=87s), confidence: stated)
- RLM is an effective context-management technique and can also serve as a memory layer for coding agents. ([2:14](https://www.youtube.com/watch?v=8oyalrfwgjw&t=134s), confidence: stated)
- Codebases are a harder and more revealing test of long-context handling than plain text like books or dictionaries, because they are structured data with imports, tests, configs, and dependencies. ([5:37](https://www.youtube.com/watch?v=8oyalrfwgjw&t=337s), confidence: stated)
- RLM is a pattern rather than a framework, so DSPy's RLM implementation and other implementations should be treated as completely different things. ([6:36](https://www.youtube.com/watch?v=8oyalrfwgjw&t=396s), confidence: stated)
- RLM Code adds nothing on top of the RLM paper's ideas; it is a faithful reference implementation. ([7:46](https://www.youtube.com/watch?v=8oyalrfwgjw&t=466s), confidence: stated)
- An RLM harness should be model-agnostic and observability-agnostic, runnable against local or cloud models and pluggable into frameworks like Pydantic AI or Google ADK. ([7:46](https://www.youtube.com/watch?v=8oyalrfwgjw&t=466s), confidence: stated)
- AI engineers should design their own harness capturing planning, coding, observation, sub-call budget, and final output, targeting use cases like root cause analysis and repo onboarding. ([15:03](https://www.youtube.com/watch?v=8oyalrfwgjw&t=903s), confidence: stated)
- The Codex harness writes Python in a REPL to curate context, which is one form of RLM. ([15:55](https://www.youtube.com/watch?v=8oyalrfwgjw&t=955s), confidence: stated)
- Managed cloud agents and dynamic multi-agent workflows with separate sandboxes are applications of RLM concepts. ([15:55](https://www.youtube.com/watch?v=8oyalrfwgjw&t=955s), confidence: stated)
- Anthropic Claude Code engineers have publicly acknowledged on X that they use RLM concepts. ([16:51](https://www.youtube.com/watch?v=8oyalrfwgjw&t=1011s), confidence: stated)
- Existing approaches — grep-style search, semantic search, context compression, and memory products — are insufficient for large monorepos. ([1:27](https://www.youtube.com/watch?v=8oyalrfwgjw&t=87s), confidence: implied)

## Concepts

- [agent execution infrastructure](../concepts/agent-execution-infrastructure.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [code comprehension and indexing](../concepts/code-comprehension-and-indexing.md)
- [context rot](../concepts/context-rot.md)
- [context window management](../concepts/context-window-management.md)
- [long-context processing](../concepts/long-context-processing.md)

