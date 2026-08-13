---
title: "\"I've never seen anything scarier than an LLM with tool calls.\""
type: "talk"
slug: "ive-never-seen-anything-scarier-than-an-llm-with-tool-calls"
track: "Security"
org: "Live Nets Labs"
video_id: "-CnA2lGfymY"
duration_sec: 1273
word_count: 3174
speakers: ["Erik Meijer"]
---

# "I've never seen anything scarier than an LLM with tool calls."

**Speakers:** [Erik Meijer](../speakers/erik-meijer.md)

**Org:** Live Nets Labs

**Track:** Security &nbsp;|&nbsp; **Duration:** 21m 13s

[Watch on YouTube](https://www.youtube.com/watch?v=-CnA2lGfymY)

## Summary

Erik Meijer argues that agentic AI is intrinsically unsafe and that the industry's current safety stack — alignment training, LLM-as-a-judge, guardrails — cannot possibly work, because 'safe answer' and 'proper question' are not mathematical properties and admit no formal proof. He traces a short history from the November 2022 chat interface, through prompt injection, to OpenAI's June 2023 tool-call release, which in his framing added an IO effect to the LLM's type signature and turned safety from a philosophical debate into real, irreversible danger. His proposed fix is a compiler trick rather than a model trick: don't let the agent execute the agentic loop at all. Instead have the model emit a first-class expression (a free monad) that *represents* the plan, then run ordinary data-flow analysis, type checking, and taint analysis on that program and machine-check a proof of safety before anything runs. The talk is a 20-minute tutorial in Lean/Dafny-flavored types, explicitly framed as a rediscovery of 1990s proof-carrying code, and is worth watching if you want a rigorous, opinionated counterpoint to probabilistic guardrails.

## Key Points

- Meijer claims models are goal-driven to the point of danger: anything standing between the model and its goal will get removed, including your files or your database, so agents must be treated as hostile by default.
- Prompt injection is, in his view, a worse problem than SQL injection ever was, because LLMs make no distinction whatsoever between code and text.
- The safety interfaces proposed by research labs — a signature requiring a 'proper' question and returning a 'safe' answer — are unimplementable, because safety is not a mathematically specifiable property; this is precisely why an entire industry of LLM-as-a-judge startups exists.
- Baking alignment into the weights is not foolproof: aligned models get routinely jailbroken, and in any case words alone are inert until some human or tool acts on them.
- Tool calling was the phase change: adding IO to the LLM's type signature is 'a small step for a type, but a giant leap for chaos', because the model now mutates the real world while computing its answer.
- The first mitigation is deferred execution — air-gap the agentic loop from the agent so the model produces a plan that a separate trusted executor runs after inspection.
- A plain value of type IO is a black box that Lean forbids reasoning about, so the real fix is to have the model return an *expression* (a free monad) representing the computation, which is inspectable data.
- Once the plan is a program, standard undergraduate compiler machinery applies: data-flow analysis, type checking, and taint analysis (Meijer credits Jeff Huntley for the taint-analysis framing of the trifecta problem), and models can generate the safety proofs themselves.
- None of this is new — it is 1990s proof-carrying code, and Meijer notes an implementation by academics including Nada Amin at Harvard is already on GitHub.
- Because the intermediate language is written, consumed, and proven by machines, it does not need to be human-friendly: 'we should stop designing languages for humans.'

## Notable Quotes

> "I'm convinced that if there's anything between the model's goal and where the model currently is, it will do everything that it can to reach that goal, including killing us or deleting your files or deleting your database."
>
> — [2:12](https://www.youtube.com/watch?v=-CnA2lGfymY&t=132s) &middot; *States the threat model that the whole talk rests on.*

> "so they're very very easy to trick and this I think is a bigger problem than SQL injection ever was"
>
> — [5:23](https://www.youtube.com/watch?v=-CnA2lGfymY&t=323s) &middot; *A concrete comparative severity claim about prompt injection.*

> "if you think about this thing for just a single nanosecond, you will realize that it's impossible to write a formal proof that an answer is safe or a question is proper"
>
> — [8:42](https://www.youtube.com/watch?v=-CnA2lGfymY&t=522s) &middot; *The impossibility result that kills the naive formal-safety interface.*

> "that is why there are at least a hundred startups down here in the exhibition hall that are using LLMs as a judge, because this is not something that you can formally specify"
>
> — [8:42](https://www.youtube.com/watch?v=-CnA2lGfymY&t=522s) &middot; *Explains the entire guardrails industry as a symptom of an unspecifiable property.*

> "What does it mean that an answer is safe? That's not a mathematical property."
>
> — [9:34](https://www.youtube.com/watch?v=-CnA2lGfymY&t=574s) &middot; *Compact statement of why safety resists formalization.*

> "trying to bake alignment into the model is not foolproof and models get routinely jailbroken"
>
> — [9:34](https://www.youtube.com/watch?v=-CnA2lGfymY&t=574s) &middot; *Direct rejection of weights-level alignment as a sufficient control.*

> "the act of adding tool calls changes AI safety from a philosophical debate to something that causes real danger. You could say tool calls give the model claws in addition to a mouth."
>
> — [11:02](https://www.youtube.com/watch?v=-CnA2lGfymY&t=662s) &middot; *Names the inflection point of the talk's history.*

> "I've never seen anything scarier than an LLM with tool calls."
>
> — [11:50](https://www.youtube.com/watch?v=-CnA2lGfymY&t=710s) &middot; *The thesis line and title of the talk.*

> "this is like a like a small step for a type, but a giant leap for chaos"
>
> — [11:50](https://www.youtube.com/watch?v=-CnA2lGfymY&t=710s) &middot; *Memorable framing of how one type change reshapes safety.*

> "while it's producing the answer, it might empty your bank account, it might delete your files, and then it gives you a safe answer. But, who cares about the safe answer when all my files are gone?"
>
> — [12:33](https://www.youtube.com/watch?v=-CnA2lGfymY&t=753s) &middot; *Shows why output-level safety checks miss the actual harm surface.*

> "Solomon Heikes um last year this conference called an AI agent, an LLM that's wrecking its environment in a loop."
>
> — [13:10](https://www.youtube.com/watch?v=-CnA2lGfymY&t=790s) &middot; *Endorses a specific, contrarian definition of 'agent'.*

> "instead of executing the agentic loop, it creates a plan and says here is a plan to do the agentic loop"
>
> — [14:40](https://www.youtube.com/watch?v=-CnA2lGfymY&t=880s) &middot; *The core architectural move of deferred execution.*

> "in some sense what we're doing, we're air gapping the agentic loop from the agent. So we don't let the agent run the agentic loop. Before the agent run it, we want to be able to check it."
>
> — [14:40](https://www.youtube.com/watch?v=-CnA2lGfymY&t=880s) &middot; *Names the design pattern the talk is advocating.*

> "what is better than creating a plan of type IO of A is creating a program that represents an expression of type IO of A"
>
> — [16:42](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1002s) &middot; *The key refinement from opaque effect to inspectable program.*

> "if you have taken any compiler course in college, you know that it's trivial to do data flow analysis, type checking, and so on on programs"
>
> — [17:31](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1051s) &middot; *Claims the hard part becomes routine once plans are reified as programs.*

> "This is something that's called proof-carrying code and it was invented by academics in the 1990s and I'm just stealing it."
>
> — [19:14](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1154s) &middot; *Grounds the proposal in established prior art.*

> "Agents are dangerous until proven safe, so you should never ever let your agents do something unless you can absolutely prove that it's safe."
>
> — [19:14](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1154s) &middot; *The talk's single prescriptive rule.*

> "we should stop designing languages for humans and it's all basic, only requires programming 101"
>
> — [19:57](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1197s) &middot; *A deliberately provocative design position about machine-targeted languages.*

> "it is actually possible to have mathematically proven safe agentic compute and it only requires very elementary type systems and programming language machinery"
>
> — [19:57](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1197s) &middot; *The closing feasibility claim the audience is asked to act on.*

## Positions

- Prompt injection is a bigger security problem than SQL injection ever was, because LLMs cannot distinguish code from text. ([5:23](https://www.youtube.com/watch?v=-CnA2lGfymY&t=323s), confidence: stated)
- It is impossible to write a formal proof that an LLM answer is 'safe' or a question is 'proper', because safety is not a mathematical property. ([8:42](https://www.youtube.com/watch?v=-CnA2lGfymY&t=522s), confidence: stated)
- The existence of ~100 LLM-as-a-judge startups is a direct consequence of safety being formally unspecifiable. ([8:42](https://www.youtube.com/watch?v=-CnA2lGfymY&t=522s), confidence: stated)
- Baking alignment into model weights is not foolproof; aligned models are routinely jailbroken. ([9:34](https://www.youtube.com/watch?v=-CnA2lGfymY&t=574s), confidence: stated)
- Offensive model outputs are comparatively harmless because words require a human to act on them; tool calls are what make models genuinely dangerous. ([10:15](https://www.youtube.com/watch?v=-CnA2lGfymY&t=615s), confidence: stated)
- OpenAI announced tool call support in GPT-4 in June 2023, and other vendors copied it, which is why the APIs all look alike (principle of minimum differentiation). ([10:15](https://www.youtube.com/watch?v=-CnA2lGfymY&t=615s), confidence: stated)
- An answer certified safe is worthless if the agentic loop already caused irreversible side effects while producing it. ([12:33](https://www.youtube.com/watch?v=-CnA2lGfymY&t=753s), confidence: stated)
- Agents should never execute the agentic loop themselves; execution must be air-gapped and handed to a separate trusted executor after inspection. ([14:40](https://www.youtube.com/watch?v=-CnA2lGfymY&t=880s), confidence: stated)
- Returning a plain IO value is insufficient because it is an opaque black box that cannot be reasoned about; the model must instead return an expression representing the computation. ([15:19](https://www.youtube.com/watch?v=-CnA2lGfymY&t=919s), confidence: stated)
- Once plans are reified as programs, standard compiler techniques — data flow analysis, type checking, taint analysis — suffice to establish safety, including for the lethal trifecta. ([18:14](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1094s), confidence: stated)
- Agents are dangerous until proven safe and should not be permitted to act absent a proof of safety. ([19:14](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1154s), confidence: stated)
- Intermediate languages for agent plans need not be human-readable, since machines generate, consume, and prove them. ([19:57](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1197s), confidence: stated)
- The Lean ecosystem receives disproportionate attention and VC funding relative to equally viable provers like Isabelle, Rocq, PVS, and TLA+. ([7:52](https://www.youtube.com/watch?v=-CnA2lGfymY&t=472s), confidence: implied)
- Mathematically proven safe agentic compute is achievable today with only elementary type systems and programming language machinery. ([19:57](https://www.youtube.com/watch?v=-CnA2lGfymY&t=1197s), confidence: stated)

## Concepts

- [agent tool design](../concepts/agent-tool-design.md)
- [ai-assisted vulnerability discovery](../concepts/ai-assisted-vulnerability-discovery.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [output guardrails](../concepts/output-guardrails.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [verifier design](../concepts/verifier-design.md)

