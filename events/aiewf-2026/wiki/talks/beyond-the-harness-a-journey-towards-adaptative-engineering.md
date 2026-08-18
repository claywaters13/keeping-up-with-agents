---
title: "Beyond the Harness: A Journey Towards Adaptative Engineering"
type: "talk"
slug: "beyond-the-harness-a-journey-towards-adaptative-engineering"
org: "Annicha Labs"
video_id: "qdZzND79mcg"
duration_sec: 2221
word_count: 5005
speakers: ["Rajiv Chandegra"]
---

# Beyond the Harness: A Journey Towards Adaptative Engineering

**Speakers:** [Rajiv Chandegra](../speakers/rajiv-chandegra.md)

**Org:** Annicha Labs

**Duration:** 37m 01s

[Watch on YouTube](https://www.youtube.com/watch?v=qdZzND79mcg)

## Summary

Rajiv Chandegra, a London-based practicing physician and AI engineer, argues that today's dominant AI engineering paradigm — building or configuring a fixed harness (Claude Code, Codex, Cursor, Pi, LangChain) ahead of runtime — is a 'factory' model that buys reliability by suppressing the variance novelty requires. He predicts two shifts break this model: models becoming powerful enough that hand-built scaffolding goes stale within months, and AI engineering moving off the screen into a messy, multi-agent, multi-human, multi-institutional physical world. Drawing on complexity science (emergence, attractors, Ackoff's 'messes', complicated vs. complex problems, flocking rules), he proposes 'adaptive engineering': the engineer designs constraints and rates of coupling rather than roles and sequencing, and lets agents self-organize a harness that emerges, specializes, forms boundaries and conventions, and dissolves mid-runtime. He distinguishes this 'horizontal intelligence' (how groups of agents coordinate) from the 'vertical intelligence' of self-improving single agents like Hermes, and from design-time customizability like Pi's. The talk is conceptual and philosophical rather than implementation-focused — no code or benchmarks — but it is honest about failure modes: premature attractors, absent selection pressure, monoculture from shared training data, and collapsing legibility.

## Key Points

- The current paradigm is harness engineering: roles, tools, sequencing, memory and outputs are all predetermined before the engineering run begins, and customization happens ahead of runtime rather than mid-engineering.
- Fixed harnesses deliver three real payoffs — reliability, auditability, and linear causality where a break can be traced to its source — which makes them the right answer for closed, deterministic, well-specified problems.
- The core tradeoff is that harness reliability is purchased by suppressing variance, and determinism and emergence pull in opposite directions, imposing a hard ceiling on novelty.
- Two assumptions drive the argument: models improve exponentially enough to make carefully built harnesses obsolete within a month, and AI engineering leaves the sandbox to run in real-time contact with social and physical environments.
- Chandegra distinguishes complicated problems (a jumbo jet or clock — decomposable, analyzable, predictable) from complex problems (flocks, markets, organizations — where parts adapt to each other and the whole can't be derived from the parts), and argues that treating complex problems as complicated is one of the most expensive mistakes in modern design.
- Adaptive engineering is defined as designing constraints such that the harness emerges, stabilizes, and adapts on its own in ways that could not be specified in advance — making the harness the output of engineering rather than its input.
- In the simulated dynamic, undifferentiated agents interact until roughly one connection per agent tips the system into a whole; environmental pressure amplifies tiny differences into specialization, clusters form emergent boundaries, and conventions crystallize into governance without a governor.
- The engineer's role is relocated, not abolished: set constraints (enable vs. govern, reward coherence vs. cost deviation, and the rate of coupling), then sense and respond to the emergent harness rather than hard-editing it or restarting from scratch.
- Horizontal intelligence (coordination among agents) is presented as orthogonal to and higher-leverage than vertical intelligence (making individual agents smarter, as in Hermes' self-improving skills), and runtime adaptivity is distinguished from Pi's design-time extensibility.
- Named failure modes include settling into a stable-but-suboptimal attractor, drift without genuine selection pressure, monoculture because agents share training data, collapsing legibility, and the loss of any pre-runtime predictability.

## Notable Quotes

> "models are going to become so powerful that existing fixed harnesses are constantly going to become outdated"
>
> — [1:22](https://www.youtube.com/watch?v=qdZzND79mcg&t=82s) &middot; *States the first load-bearing assumption of the whole thesis in one line.*

> "adaptive engineering, where you actually allow the harness to emerge and adapt mid-engineering to find its most optimal position and structure"
>
> — [2:08](https://www.youtube.com/watch?v=qdZzND79mcg&t=128s) &middot; *The talk's central coinage, defined at its first appearance.*

> "the model is the engine and the harness is everything built around to make that engine useful"
>
> — [5:09](https://www.youtube.com/watch?v=qdZzND79mcg&t=309s) &middot; *Crisp, reusable definition of 'harness' that other talks can be indexed against.*

> "But the customization occurs ahead of the engineering runtime. Uh and not mid-engineering. And that's largely directed by us as humans."
>
> — [6:58](https://www.youtube.com/watch?v=qdZzND79mcg&t=418s) &middot; *Preempts the obvious objection that existing harnesses are already customizable.*

> "It's reliable. Um you know, the same input leads to a similar set of outputs. Obviously, there's going to be some variation. It's auditable. Um you can inspect exactly what changed and when."
>
> — [6:58](https://www.youtube.com/watch?v=qdZzND79mcg&t=418s) &middot; *Concedes the fixed harness's genuine payoffs before attacking it.*

> "this is like a factory line though. Like think Taylorism for AI. Just like a factory assembly line, every station is engineered in advance."
>
> — [7:40](https://www.youtube.com/watch?v=qdZzND79mcg&t=460s) &middot; *The governing metaphor for the paradigm he wants to displace.*

> "that reliability isn't free. Um, you buy it by suppressing, um, variance that I'd argue novelty requires. Um, and determinism and emergence pull kind of in opposite directions."
>
> — [8:27](https://www.youtube.com/watch?v=qdZzND79mcg&t=507s) &middot; *The sharpest statement of the tradeoff the talk turns on.*

> "You can build a careful harness today or you can use one off the shelf. But it could be irrelevant in the next month."
>
> — [9:26](https://www.youtube.com/watch?v=qdZzND79mcg&t=566s) &middot; *Puts a concrete time horizon on harness obsolescence.*

> "The more real world it needs, the more rules you bolt on and eventually the harness just becomes ever more complicated than the actual problem that you need to solve."
>
> — [9:26](https://www.youtube.com/watch?v=qdZzND79mcg&t=566s) &middot; *Names the patch-the-harness failure spiral that practitioners will recognize.*

> "the factory method is the right answer to a fixed problem and the wrong answer to a moving problem"
>
> — [10:18](https://www.youtube.com/watch?v=qdZzND79mcg&t=618s) &middot; *The speaker's own designated one-line takeaway.*

> "A flame looks like an object, but it isn't. It's a pattern held together moment by moment by a process. You stop the process and the thing doesn't exist."
>
> — [12:13](https://www.youtube.com/watch?v=qdZzND79mcg&t=733s) &middot; *The clearest articulation of the relational metaphysics underpinning the argument.*

> "The flock lives in the relationships, not the parts."
>
> — [13:53](https://www.youtube.com/watch?v=qdZzND79mcg&t=833s) &middot; *Compresses the emergence argument into the talk's most quotable line.*

> "managers aren't handed neat separate problems. They're handed dynamic situations, tangles of problems that keep changing and keep bumping to each other."
>
> — [14:44](https://www.youtube.com/watch?v=qdZzND79mcg&t=884s) &middot; *Imports Ackoff's 'mess' concept, the intellectual anchor for why decomposition fails.*

> "you don't analyze and plan a complex system. Instead, you probe and sense and respond"
>
> — [16:40](https://www.youtube.com/watch?v=qdZzND79mcg&t=1000s) &middot; *Prescriptive methodological claim that follows from the complicated/complex split.*

> "things fail not due to lack of execution, but essentially because there's a failure in categorizing the problem spaces"
>
> — [16:40](https://www.youtube.com/watch?v=qdZzND79mcg&t=1000s) &middot; *A strong diagnostic claim others might contest.*

> "adaptive engineering is the discipline of designing constraints to the extent that the harness emerges on its own, stabilizes, and adapts as needed in response to the changing environment in ways that you could not specify in advance"
>
> — [21:12](https://www.youtube.com/watch?v=qdZzND79mcg&t=1272s) &middot; *The formal definition, delivered as such.*

> "Essentially, the harness becomes the ongoing output rather than the input."
>
> — [21:12](https://www.youtube.com/watch?v=qdZzND79mcg&t=1272s) &middot; *The inversion that distinguishes adaptive from harness engineering in one sentence.*

> "So, you don't build the harness anymore. You let the agents form the harness that best fits the environment in that moment, in that context."
>
> — [22:22](https://www.youtube.com/watch?v=qdZzND79mcg&t=1342s) &middot; *The practical upshot for the engineer's day-to-day role.*

> "the agent's identity isn't something you gave it. It's actually the position, role, or capability it took relative to the others and its environment"
>
> — [23:57](https://www.youtube.com/watch?v=qdZzND79mcg&t=1437s) &middot; *Reframes agent role definition as emergent rather than assigned.*

> "the system produce some level of governance without a governor. Conventions emerge spontaneously from the local coordination with no central authority"
>
> — [24:43](https://www.youtube.com/watch?v=qdZzND79mcg&t=1483s) &middot; *The decentralization claim that most directly opposes orchestrator-based multi-agent designs.*

> "you don't abolish the engineer, you're just relocating the emphasis of engineering"
>
> — [25:34](https://www.youtube.com/watch?v=qdZzND79mcg&t=1534s) &middot; *Answers the obvious 'what's left for me to do' objection.*

> "that adaptation is in the form of vertical intelligence, which is about making individual agents smarter. What I'm talking about here is horizontal intelligence, which is all about how groups of agents coordinate."
>
> — [28:06](https://www.youtube.com/watch?v=qdZzND79mcg&t=1686s) &middot; *Introduces the vertical/horizontal distinction that positions the thesis against self-improving-agent work.*

> "There's adaptive at the design stage, like when you're preparing for that engineering process. Um Uh where the engineer can customize and the tool's quite malleable."
>
> — [28:56](https://www.youtube.com/watch?v=qdZzND79mcg&t=1736s) &middot; *Draws the design-time vs. runtime line using Pi as the named example.*

> "There is a risk of monoculture, where you don't get genuine diversity amongst agents because they're all trained on the same data."
>
> — [34:05](https://www.youtube.com/watch?v=qdZzND79mcg&t=2045s) &middot; *The most concrete and technically checkable of the admitted failure modes.*

> "the limiting factor which is the case now, but probably more so in the future, is not going to be the strength of the model."
>
> — [35:04](https://www.youtube.com/watch?v=qdZzND79mcg&t=2104s) &middot; *Sets up the talk's closing thesis about where the bottleneck actually sits.*

> "It's going to be the adaptability of the harness."
>
> — [36:01](https://www.youtube.com/watch?v=qdZzND79mcg&t=2161s) &middot; *The concluding claim the entire talk builds toward.*

## Positions

- Fixed harnesses buy reliability by suppressing variance, and that suppression imposes a hard ceiling on novelty because determinism and emergence pull in opposite directions. ([8:27](https://www.youtube.com/watch?v=qdZzND79mcg&t=507s), confidence: stated)
- A carefully built harness can become irrelevant within a month because the underlying model improves enough not to need the scaffolding. ([9:26](https://www.youtube.com/watch?v=qdZzND79mcg&t=566s), confidence: stated)
- The factory/fixed-harness method is the correct approach for fixed, complicated problems and the wrong approach for moving, complex ones. ([10:18](https://www.youtube.com/watch?v=qdZzND79mcg&t=618s), confidence: stated)
- Complex systems cannot be planned or analyzed; the correct method is to probe, sense, and respond. ([16:40](https://www.youtube.com/watch?v=qdZzND79mcg&t=1000s), confidence: stated)
- Most failures in modern design and engineering come from miscategorizing a complex problem as a complicated one, not from poor execution. ([16:40](https://www.youtube.com/watch?v=qdZzND79mcg&t=1000s), confidence: stated)
- The harness should be the output of the engineering process rather than its input, emerging from agent interaction in ways that cannot be specified in advance. ([21:12](https://www.youtube.com/watch?v=qdZzND79mcg&t=1272s), confidence: stated)
- Agent identity, roles, and specialization should arise from position relative to other agents and environmental pressure rather than being assigned by the engineer. ([23:57](https://www.youtube.com/watch?v=qdZzND79mcg&t=1437s), confidence: stated)
- Central authority in a multi-agent system leads to brittleness in a changing environment, so governance should emerge from local coordination. ([24:43](https://www.youtube.com/watch?v=qdZzND79mcg&t=1483s), confidence: stated)
- Horizontal intelligence (coordination among agents) is a higher-leverage direction than vertical intelligence (making individual agents smarter, as in self-improving skill-learning agents). ([28:56](https://www.youtube.com/watch?v=qdZzND79mcg&t=1736s), confidence: stated)
- Pi's extensibility counts as design-stage adaptivity, not adaptive engineering, because it is not a self-organizing multi-agent system that reorganizes during runtime. ([29:53](https://www.youtube.com/watch?v=qdZzND79mcg&t=1793s), confidence: stated)
- The rate of coupling between agents is the engineer's primary new control lever in adaptive systems. ([23:12](https://www.youtube.com/watch?v=qdZzND79mcg&t=1392s), confidence: stated)
- Adaptive engineering will produce monoculture unless agent diversity is engineered, because agents are trained on the same data. ([34:05](https://www.youtube.com/watch?v=qdZzND79mcg&t=2045s), confidence: stated)
- Without a genuine selection pressure analogous to environmental pressure in evolution, emergent agent systems will drift or settle into suboptimal attractors. ([33:21](https://www.youtube.com/watch?v=qdZzND79mcg&t=2001s), confidence: stated)
- The binding constraint on future AI engineering will be harness adaptability rather than model strength. ([35:04](https://www.youtube.com/watch?v=qdZzND79mcg&t=2104s), confidence: stated)
- Legibility and explainability necessarily degrade as system adaptability increases, and this is an inherent feature of complex systems rather than a fixable defect. ([34:05](https://www.youtube.com/watch?v=qdZzND79mcg&t=2045s), confidence: stated)
- Fixed and adaptive engineering lie on a continuum rather than being a binary choice, and neither is superior — they serve different use cases. ([27:22](https://www.youtube.com/watch?v=qdZzND79mcg&t=1642s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [scaling laws](../concepts/scaling-laws.md)
- [sub-agent delegation](../concepts/sub-agent-delegation.md)

