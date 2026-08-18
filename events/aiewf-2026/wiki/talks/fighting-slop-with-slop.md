---
title: "fighting slop with slop"
type: "talk"
slug: "fighting-slop-with-slop"
track: "Software Factories"
org: "Boundary"
day: "Day 2 — Session Day 1"
room: "Main Stage"
video_id: "AMiyLItEtLA"
duration_sec: 1292
word_count: 4029
speakers: ["Vaibhav Gupta"]
---

# fighting slop with slop

**Speakers:** [Vaibhav Gupta](../speakers/vaibhav-gupta.md)

**Org:** Boundary

**Track:** Software Factories &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 21m 32s

[Watch on YouTube](https://www.youtube.com/watch?v=AMiyLItEtLA)

## Summary

Vaibhav Gupta argues that the way to survive AI-generated 'slop' is to generate more of it — pointing it at the tooling and processes that keep a codebase trustworthy rather than at the code itself. His team at Boundary ships a programming language (BAML) with eight people, no code reviews, no AI tooling standardization, and everyone working in parallel; what makes that safe is a small invariant architecture.md, a design-doc tool with a Slack firehose and a mandatory-reader rule, a dependency-graph visualizer with CI-enforced boundaries, and agent swarms that write BAML programs so other agents can mine the transcripts for bugs, wasted tool calls, and A/B-testable language features. The second half is a harder claim: even perfect process loses the war because the foundations are built for human productivity, so he demos BAML's agent-first design — inferred and compiler-checked error types, every function as a standalone cross-platform CLI, a 'describe this symbol' tool replacing multi-call ripgrep, near-zero-cost execution tracing, and calling BAML from Python/TS/Rust with lambdas and generics crossing the boundary. Watch it if you want a concrete picture of what engineering process and language design look like when you assume nobody reads the code; skip it if you want a product pitch or hands-on BAML tutorial.

## Key Points

- Slop is defined operationally as any code you don't read, which means every codebase already contains it and will only contain more — the task is building systems that stay correct anyway.
- Instead of standardizing on a coding agent or a CLAUDE.md, the team maintains a deliberately tiny architecture.md containing only invariants that won't change for months or years, so any model can consume it.
- Writing is held to a higher bar than code: design docs are the one artifact that can't be slop, enforced socially by a Slack notification channel and a rule that shipping a doc requires securing actual readers.
- A dependency-graph tool with semantic boundaries plus CLI-enforced invariants in CI catches leaky dependencies the moment an agent introduces them, which has kept the architecture unchanged for three or four months.
- The team runs agents that continuously write BAML programs, then has other agents audit the full Claude transcripts — not only for incorrect output but for tasks that took three tool calls when one would do — turning language design into an A/B-testable, data-driven process.
- Gupta claims TypeScript's stated goal of balancing correctness and productivity implicitly means human productivity, and that layering CoffeeScript/TypeScript over a broken JavaScript foundation is patching the wrong layer.
- In a world where code goes unread, comprehension shifts to execution traces and interactive visualizations of semantic boundaries that let you opt into reading only the parts you care about.
- Agent-first language design should collapse multi-call workflows: a single 'describe' call returning docstrings, source, and call sites; every function auto-exposed as a type-safe standalone CLI binary that cross-compiles including to WASM.
- Errors should be inferred and propagated by the compiler so it can prove exhaustively whether a function throws — replacing the nested try/catch-then-console.log pattern agents fall into.
- Rather than asking the world to rewrite everything, BAML is callable from Python, TypeScript, Rust, Go, Ruby, and Java, with lambdas, generics, and closures passing across the language boundary, and sync/async variants generated automatically.

## Notable Quotes

> "We do no code reviews. We require every engineer to work on things in parallel. And we have no standardization on how people do AI."
>
> — [0:01](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1s) &middot; *the provocation the entire talk is built to justify*

> "To to defeat the slop, we must become the slop."
>
> — [0:50](https://www.youtube.com/watch?v=AMiyLItEtLA&t=50s) &middot; *the title thesis in one line*

> "Slop is just any code you don't read. And whether any of you admit it or not, this is the least amount of slop that your code base will ever have. Cherish it."
>
> — [1:27](https://www.youtube.com/watch?v=AMiyLItEtLA&t=87s) &middot; *gives the talk's central term a checkable definition and a direction of travel*

> "instead of trying to hold standards in our codebase, we did something that is an invariant. We built an architecture.md file. Instead of using Claude.md, just pick something that every model can just understand."
>
> — [2:03](https://www.youtube.com/watch?v=AMiyLItEtLA&t=123s) &middot; *concrete, transferable alternative to per-tool config files*

> "This file has to be incredibly small, and it can only have things that will not change for months or for years."
>
> — [2:03](https://www.youtube.com/watch?v=AMiyLItEtLA&t=123s) &middot; *names the constraint that makes the architecture.md approach work*

> "And we have a very simple rule in our team. Code can be slop, writing cannot."
>
> — [2:38](https://www.youtube.com/watch?v=AMiyLItEtLA&t=158s) &middot; *the tradeoff at the heart of their process*

> "I built this, and I hit a little bit of AI psychosis, and I started shipping 10 design docs a day, and soon the team was fighting my slop."
>
> — [3:10](https://www.youtube.com/watch?v=AMiyLItEtLA&t=190s) &middot; *candid failure mode that motivates the mandatory-reader rule*

> "not just what was bad in terms of what was incorrect in the language, but what took three tool calls when it should have only taken one."
>
> — [4:55](https://www.youtube.com/watch?v=AMiyLItEtLA&t=295s) &middot; *defines the non-obvious quality signal they mine from agent transcripts*

> "The point is you can start building data-driven systems without ever writing a single line of code."
>
> — [6:15](https://www.youtube.com/watch?v=AMiyLItEtLA&t=375s) &middot; *states the payoff of the agent-audit loop*

> "in order to build a programming language, it wouldn't have taken eight people. It wouldn't have taken less than two years. It would have taken hundreds and thousands and tens of thousands of man-hours and then you would still have a broken system."
>
> — [6:15](https://www.youtube.com/watch?v=AMiyLItEtLA&t=375s) &middot; *the concrete team-size and timeline claim behind the argument*

> "did you know that TypeScript's main design goal is to strike a balance between correctness and productivity? And there's an asterisk here because what they really mean is human productivity."
>
> — [7:22](https://www.youtube.com/watch?v=AMiyLItEtLA&t=442s) &middot; *the pivot from process to a contestable claim about language design*

> "Why do we turn things to strings when we sort them? This is just slop baked into the language, whether you like it or not."
>
> — [8:01](https://www.youtube.com/watch?v=AMiyLItEtLA&t=481s) &middot; *grounds the abstract complaint in a specific JavaScript wart*

> "In a world where we don't read all the code, the only way to understand the code is actually by the execution trace."
>
> — [10:39](https://www.youtube.com/watch?v=AMiyLItEtLA&t=639s) &middot; *reframes observability as the primary comprehension mechanism*

> "Don't read anything but the code itself. The docs may lie, the um the actual description or architecture file or readme file will definitely lie, but the code cannot lie."
>
> — [13:06](https://www.youtube.com/watch?v=AMiyLItEtLA&t=786s) &middot; *in tension with his own architecture.md and design-doc practice, which makes it interesting*

> "Have you seen error handling be beautiful ever, other than Rust?"
>
> — [15:02](https://www.youtube.com/watch?v=AMiyLItEtLA&t=902s) &middot; *takes a side on error-handling design in one line*

> "error types now get inferred without you ever having to do any guesswork. That means if you catch or handle errors, we can do exhaustive guarantees, and the compiler can prove that you have handled the error or not handled the error."
>
> — [15:42](https://www.youtube.com/watch?v=AMiyLItEtLA&t=942s) &middot; *the most specific technical claim about what BAML's compiler provides*

> "Code is a matter of trust. The reason that we don't use ML code blindly is because we don't trust it yet, cuz the systems underneath them don't have enough rigidity."
>
> — [17:04](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1024s) &middot; *connects the process half and the language half of the talk*

> "when the agent does something, the type system never lies. The type system becomes the absolute center of truth that prevents invariants from entering your codebase."
>
> — [18:58](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1138s) &middot; *states what replaces code review when nobody reads the diff*

> "just yesterday one of our engineers built a partial C compiler purely in BAML."
>
> — [19:38](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1178s) &middot; *a datable capability claim, useful for checking against the language's maturity*

> "They said adding CI/CD would slow us down. They They do slow down for 3 months while they add it, but after that, they move a lot faster. Our processes have to evolve if we're going to ship at agent speed."
>
> — [20:11](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1211s) &middot; *the analogy he uses to preempt the 'this is overhead' objection*

> "I think we do need a new Git. I think we do need a new database, and yes, I think we need a new programming language."
>
> — [20:44](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1244s) &middot; *the maximal version of his thesis, stated as a closing call to action*

## Positions

- Code review is not a necessary control for shipping correct software; invariant-enforcing tooling and a strong type system can replace it. ([19:38](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1178s), confidence: stated)
- Teams should not standardize which AI coding tool engineers use; standardize the codebase invariants instead. ([2:03](https://www.youtube.com/watch?v=AMiyLItEtLA&t=123s), confidence: stated)
- A model-agnostic architecture.md is better than a tool-specific CLAUDE.md, and it must be tiny and contain only things that won't change for months or years. ([2:03](https://www.youtube.com/watch?v=AMiyLItEtLA&t=123s), confidence: stated)
- Design documents must be human-quality writing even when code is allowed to be unread slop. ([2:38](https://www.youtube.com/watch?v=AMiyLItEtLA&t=158s), confidence: stated)
- Requiring an author to secure actual readers before shipping a design doc raises doc quality substantially. ([3:46](https://www.youtube.com/watch?v=AMiyLItEtLA&t=226s), confidence: stated)
- A programming language that would have taken tens of thousands of man-hours was built by eight people in under two years using agents and millions of tokens. ([6:15](https://www.youtube.com/watch?v=AMiyLItEtLA&t=375s), confidence: stated)
- TypeScript's correctness/productivity balance is optimized for human productivity, and would be designed differently if humans never wrote code. ([7:22](https://www.youtube.com/watch?v=AMiyLItEtLA&t=442s), confidence: stated)
- Layering CoffeeScript and TypeScript over JavaScript is patching a broken foundation rather than fixing it; a new language is the right response. ([8:56](https://www.youtube.com/watch?v=AMiyLItEtLA&t=536s), confidence: stated)
- Grep should not be used anywhere; ripgrep supersedes it, and a semantic 'describe' tool supersedes both for agents. ([11:52](https://www.youtube.com/watch?v=AMiyLItEtLA&t=712s), confidence: stated)
- Full-program execution tracing is untenable in Python or TypeScript but can be made effectively zero performance cost if designed in from first principles. ([10:39](https://www.youtube.com/watch?v=AMiyLItEtLA&t=639s), confidence: stated)
- Source code is more trustworthy than any doc, readme, or architecture file, because docs will lie and code cannot. ([13:06](https://www.youtube.com/watch?v=AMiyLItEtLA&t=786s), confidence: stated)
- Rust is the only language with beautiful error handling; agents in other languages degrade to nested try/catch and console.log. ([15:02](https://www.youtube.com/watch?v=AMiyLItEtLA&t=902s), confidence: stated)
- Error types can be inferred through the call graph so the compiler exhaustively proves whether a function throws, eliminating guesswork about error handling. ([15:42](https://www.youtube.com/watch?v=AMiyLItEtLA&t=942s), confidence: stated)
- We do not trust LLM-written code because the underlying systems lack rigidity, not because the models are inadequate. ([17:04](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1024s), confidence: stated)
- Asking everyone to rewrite their code in a new language would lose the war on slop, so a new language must be embeddable in existing ones. ([17:41](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1061s), confidence: stated)
- Process investments like CI/CD cost roughly three months of slowdown and then pay back in speed, and agent-era process changes follow the same curve. ([20:11](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1211s), confidence: stated)
- Git, databases, and programming languages all need to be rebuilt for an agent-first world. ([20:44](https://www.youtube.com/watch?v=AMiyLItEtLA&t=1244s), confidence: stated)
- Engineers will not read every line of AI-generated code regardless of policy, so process should be designed around that fact rather than against it. ([6:46](https://www.youtube.com/watch?v=AMiyLItEtLA&t=406s), confidence: implied)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [agent-readable codebases](../concepts/agent-readable-codebases.md)
- [ai-generated code quality](../concepts/ai-generated-code-quality.md)
- [code comprehension and indexing](../concepts/code-comprehension-and-indexing.md)
- [online evaluation](../concepts/online-evaluation.md)
- [production trace mining](../concepts/production-trace-mining.md)
- [spec-driven development](../concepts/spec-driven-development.md)

