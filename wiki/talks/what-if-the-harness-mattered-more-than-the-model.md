---
title: "What if the harness mattered more than the model?"
type: "talk"
slug: "what-if-the-harness-mattered-more-than-the-model"
org: "Etsy"
video_id: "2e9ANoOEn28"
duration_sec: 1923
word_count: 4378
speakers: ["Aditya Bhargava"]
---

# What if the harness mattered more than the model?

**Speakers:** [Aditya Bhargava](../speakers/aditya-bhargava.md)

**Org:** Etsy

**Duration:** 32m 03s

[Watch on YouTube](https://www.youtube.com/watch?v=2e9ANoOEn28)

## Summary

Aditya Bhargava (staff engineer at Etsy) argues against the prevailing view that frontier models are good enough to make harnesses trivial, claiming that direction leaves us dependent on a handful of proprietary, non-local models. He cites HarnessBench-style results where holding the model and tasks fixed but swapping harnesses moves scores from 52.4% to 76.2%, with the harness mattering more for weaker models — the basis for his bet that a great harness can let a local open-source model reach cutting-edge performance. The bulk of the talk is a live demo ladder in Agency, a new agent-oriented language he has been building for six months: a coding agent that fixes a buggy median function evolves through model-only, tools, interrupts and handlers, partial function application, a ReAct feedback loop, sub-agents, and finally GEPA-style prompt self-optimization. His second controversial claim is that good harnesses need language-level support — resumable interrupts inside loops, tools, and sub-agents; every function usable as a tool; sub-agents as plain functions. Worth watching if you care about agent safety-versus-autonomy tradeoffs or want a concrete, incremental taxonomy of what 'a better harness' actually means.

## Key Points

- The industry consensus that you should 'keep the harness simple and give the model a few tools' pushes toward dependence on proprietary models that cannot be run locally, which the speaker considers the wrong direction.
- A harness benchmark with 106 tasks, holding model and evaluation constant, produced scores from 52.4% to 76.2% — over a 20-point spread attributable to the harness alone.
- Harness quality matters more for weaker models, which is what makes local open-source models a plausible substitute for frontier APIs given enough harness engineering.
- The speaker claims building a genuinely good harness requires language-level support, and spent six months building a TypeScript-and-Python-flavored language called Agency to provide it.
- The harness improvement ladder is: bare model → tools → handlers/interrupts for safety → partial function application for safe autonomy → ReAct feedback loop for reasoning → sub-agents for capability → self-optimization for measured improvement.
- Partial function application locks arguments (like a directory) so the model never sees or controls them, constraining capability without requiring a human approval on every action.
- Every function in Agency is automatically a tool (schema generated from the signature, docstring as description), and sub-agents are just functions rather than a separate framework concept.
- Sub-agents add capability without bloating context; agents fail partly from too many unrelated tools and concepts competing in one context window.
- Agency's interrupts can pause and resume execution at an exact point inside a for loop, a tool call, or a sub-agent, and the execution state can be serialized and resumed a week later.
- Built-in optimizers (including a GEPA-style one) let you mark variables with an `optimize` modifier and improve prompts against a measured baseline objective instead of guess-and-check.

## Notable Quotes

> "the models are so good that you can just keep the harness simple."
>
> — [0:01](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1s) &middot; *States the industry consensus the entire talk is arguing against.*

> "that's moving in the wrong direction because that is making us reliant on fancy proprietary models that can't be run locally"
>
> — [0:52](https://www.youtube.com/watch?v=2e9ANoOEn28&t=52s) &middot; *The core objection — a strategic, not just technical, argument.*

> "What if we focused on open-source models that can be run locally? What if we focused on building a harness that is so good that we can get the performance of a cutting-edge model through a local open-source model?"
>
> — [0:52](https://www.youtube.com/watch?v=2e9ANoOEn28&t=52s) &middot; *The talk's central hypothesis in one sentence.*

> "So, scores range from 52.4% to 76.2%. So, more than a 20-point difference, and only the harness changed."
>
> — [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s) &middot; *The single hardest number backing the whole thesis.*

> "the really interesting thing is that for weaker models, the harness matters more"
>
> — [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s) &middot; *The finding that makes local models viable, and the crux of the argument.*

> "if a good harness can compensate, and can make a weaker model perform better, then you can build our own harnesses, and that's something that any of us can do, and we don't have to depend on paid models."
>
> — [2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s) &middot; *Frames harness work as a decentralization play.*

> "I think building a good harness actually requires language-level support."
>
> — [3:12](https://www.youtube.com/watch?v=2e9ANoOEn28&t=192s) &middot; *The talk's second, more contestable claim — most practitioners reach for frameworks, not new languages.*

> "how do you give agent capabilities so they can take actions, but not so much capability that they do something unsafe"
>
> — [6:26](https://www.youtube.com/watch?v=2e9ANoOEn28&t=386s) &middot; *Crisp statement of the capability-versus-safety tradeoff that structures the demo.*

> "giving the agent the ability to read and write arbitrary files on our file system is really unsafe. So, by default Agency won't allow you to do this."
>
> — [11:39](https://www.youtube.com/watch?v=2e9ANoOEn28&t=699s) &middot; *A concrete safe-by-default design decision, not just a principle.*

> "here's the safe version of our agent where the tools will raise an interrupt by default, and now this code is going to ask the user, do you approve?"
>
> — [14:26](https://www.youtube.com/watch?v=2e9ANoOEn28&t=866s) &middot; *Names the human-in-the-loop rung of the ladder before its cost is critiqued.*

> "And this is better, and it is safe, but it's also very slow. So, the next thing we want to do is make the agent autonomous, while still keeping it safe, and that's the tricky part"
>
> — [14:26](https://www.youtube.com/watch?v=2e9ANoOEn28&t=866s) &middot; *Explicitly names the cost of approval-gated safety.*

> "we're locking the directory argument to demo. Um the LLM isn't going to be able to change that argument. It's not even going to know that that argument exists."
>
> — [16:13](https://www.youtube.com/watch?v=2e9ANoOEn28&t=973s) &middot; *The mechanism of PFA-based sandboxing, stated precisely.*

> "partial function application is a really great way to constrain the capabilities of your agent. Now, no human input is needed, but it's still safe."
>
> — [16:54](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1014s) &middot; *The talk's proposed resolution to the autonomy/safety tension.*

> "in agency, a sub-agent is just another function. And you just call it, use it like a tool just like you would anywhere else."
>
> — [22:13](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1333s) &middot; *A design position against frameworks that make sub-agents a special concept.*

> "sub agents are cool because they let you add new capabilities without bloating context"
>
> — [23:46](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1426s) &middot; *The stated justification for sub-agents, in context-budget terms.*

> "Often when agents get confused and fail, it's because they have too much context blow, but also because they have too many unrelated concepts in their context."
>
> — [24:45](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1485s) &middot; *A specific failure-mode diagnosis others may dispute.*

> "So the baseline objective is 0.2 and it's going to try to improve upon that."
>
> — [26:20](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1580s) &middot; *Concrete number from the live optimizer run.*

> "the reason this self-optimization is so great is because we're not guessing and checking. We're systematically measuring and improving, which is a big leap forward."
>
> — [27:30](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1650s) &middot; *Positions prompt optimization as the endpoint of harness maturity.*

> "one of the really killer features of Agency is that when you raise that interrupt, it's actually going to pause execution and return control back to the user."
>
> — [29:57](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1797s) &middot; *The specific capability offered as evidence that language-level support is needed.*

> "You can serialize the execution, you can come back to it a week later, and you don't need to change anything about all the code we have been looking at."
>
> — [30:39](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1839s) &middot; *The strongest concrete differentiator claimed over existing frameworks.*

> "an agent is a model plus a harness for this talk, at least. Uh, better harness equals better performance, especially for weaker models."
>
> — [31:20](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1880s) &middot; *The takeaway slide compressed to one line.*

## Positions

- Keeping the harness simple because models are strong is the wrong direction, since it makes users dependent on proprietary models that cannot run locally. ([0:52](https://www.youtube.com/watch?v=2e9ANoOEn28&t=52s), confidence: stated)
- Changing only the harness, with model and evaluation held constant across 106 tasks, produces a spread of 52.4% to 76.2% — more than 20 points. ([2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s), confidence: stated)
- The harness matters more for weaker models than for stronger ones. ([2:23](https://www.youtube.com/watch?v=2e9ANoOEn28&t=143s), confidence: stated)
- A sufficiently good harness can make a local open-source model reach the performance of a cutting-edge proprietary model. ([29:16](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1756s), confidence: stated)
- Building a good harness requires language-level support, not just a library or framework. ([3:12](https://www.youtube.com/watch?v=2e9ANoOEn28&t=192s), confidence: stated)
- Existing tools and frameworks were incapable of doing what a good harness requires, which is why a new language was necessary. ([3:12](https://www.youtube.com/watch?v=2e9ANoOEn28&t=192s), confidence: stated)
- Agents should be unable to read or write arbitrary files by default; destructive or sensitive standard-library functions should raise an interrupt first. ([13:20](https://www.youtube.com/watch?v=2e9ANoOEn28&t=800s), confidence: stated)
- Locking tool arguments via partial function application gives safety without the latency cost of per-action human approval. ([16:54](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1014s), confidence: stated)
- Modeling sub-agents as ordinary functions is better than frameworks that make sub-agents a distinct, harder-to-grasp concept. ([22:13](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1333s), confidence: stated)
- Agent failures often stem from too many unrelated tools and concepts in context, making tool selection unreliable. ([24:45](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1485s), confidence: stated)
- Most frameworks' human-in-the-loop features carry significant restrictions and workarounds; very few languages support true pause and resume. ([29:57](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1797s), confidence: stated)
- Automated optimizers with a measured objective are a strict improvement over manual guess-and-check prompt iteration. ([27:30](https://www.youtube.com/watch?v=2e9ANoOEn28&t=1650s), confidence: stated)
- Harness quality is an under-benchmarked dimension — benchmarks for harnesses are something the field has not seen much of yet. ([1:34](https://www.youtube.com/watch?v=2e9ANoOEn28&t=94s), confidence: stated)

## Concepts

- [agent autonomy levels](../concepts/agent-autonomy-levels.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [context rot](../concepts/context-rot.md)
- [durable execution](../concepts/durable-execution.md)
- [human-in-the-loop approval](../concepts/human-in-the-loop-approval.md)
- [local inference](../concepts/local-inference.md)
- [prompt optimization](../concepts/prompt-optimization.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

