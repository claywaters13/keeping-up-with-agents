---
title: "On AI and Knowledge"
type: "talk"
slug: "on-ai-and-knowledge"
track: "Software Factories"
org: "Distinguished Engineer & CVP for AI Knowledge, Microsoft"
day: "Day 2 — Session Day 1"
room: "Main Stage"
video_id: "RGSFUqzqErE"
duration_sec: 1055
word_count: 3086
speakers: ["Pablo Castro"]
---

# On AI and Knowledge

**Speakers:** [Pablo Castro](../speakers/pablo-castro.md)

**Org:** Distinguished Engineer & CVP for AI Knowledge, Microsoft

**Track:** Software Factories &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 17m 35s

[Watch on YouTube](https://www.youtube.com/watch?v=RGSFUqzqErE)

## Summary

Pablo Castro, Microsoft's CVP for AI Knowledge, frames agent knowledge as three categories — intrinsic (what's baked into model weights), extrinsic (retrieved/grounded context), and learned (knowledge accumulated by observing and tuning agent work) — and argues each demands different infrastructure. He traces the coding-assistance exponential from IntelliSense in 1996 through GitHub Copilot to agents that ship whole products without hand-written code, crediting intrinsic knowledge for launching it. The bulk of the talk covers extrinsic knowledge: why pure vector search proved insufficient, why hybrid and agentic retrieval win on real customer evaluations, and how Microsoft IQ and Foundry IQ expose a layered stack that defaults to automatic but lets experts drop down to index and quantization control. He closes with a live demo of an 'agent optimizer' that generates an eval, hill-climbs agent instructions against it, and applies the winning configuration — his concrete instantiation of the human-agent learning loop. Worth watching if you want a vendor-grounded but technically specific view of retrieval architecture and automated agent optimization; it is explicitly a Microsoft platform talk.

## Key Points

- Castro splits agent knowledge into intrinsic (parametric, from training), extrinsic (grounded/retrieved), and learned (accumulated from doing the work), and argues intrinsic knowledge is what launched the current exponential.
- The coding-assist timeline compresses dramatically: 22 years from IntelliSense (1996) to ML-ranked completions, then only 3 years to GitHub Copilot, then Cursor and Copilot X within a couple more.
- Pure vector search was a useful unblock but insufficient; Microsoft's own evaluations show combined retrieval methods consistently beat individual methods, especially on real-world customer scenarios.
- Agents need not just their own curated data but the 'ambient' organizational data — documents, email, chat, calendar, warehouses, BI reports, and the public web — which Microsoft IQ (Work/Fabric/Foundry/Web IQ) exposes through a single entry point.
- Foundry IQ is deliberately layered so the default path hides chunking, vectorization, ranking, and agentic retrieval, while experts can descend to control vector indexes, quantization, and lexical retrieval in the same stack.
- Agentic retrieval — a loop that reflects on the data and judges whether the information need is satisfied before returning — pays off on difficult cases (better evidence recall and answer completeness) but single-shot retrieval remains fine for easy ones.
- Retrieval effort is tuned as an explicit latency-versus-quality dial, and the system is evaluated for token efficiency: most information-dense answer in the fewest tokens.
- Every Foundry knowledge base is exposed as an MCP server, so existing agent harnesses can consume it without glue code.
- The agent optimizer materializes the learning loop: generate a task-adherence eval from traces and instructions, establish a baseline, hill-climb candidate configurations (a ~45-minute run in the demo), then apply the winning instructions — which are machine-generated, not handwritten.

## Notable Quotes

> "And while it's kind of the obvious thing, I would argue this is the knowledge that actually threw us into the exponential we are in today."
>
> — [1:01](https://www.youtube.com/watch?v=RGSFUqzqErE&t=61s) &middot; *States his central claim about intrinsic knowledge's role.*

> "It takes 22 years from there to go for the next step where machine learning helps us actually rank the options we give you in IntelliSense, so it's quicker to pick the right choice. Just 3 years after that, GitHub Copilot launches."
>
> — [2:28](https://www.youtube.com/watch?v=RGSFUqzqErE&t=148s) &middot; *Concrete numbers anchoring the compression of the timeline.*

> "where incredibly successful software like like Open Claw comes out to existence with not a single line of code written by hand"
>
> — [3:16](https://www.youtube.com/watch?v=RGSFUqzqErE&t=196s) &middot; *His endpoint example for how far intrinsic-knowledge-driven coding has gone.*

> "In fact, just yesterday we announced that Claude in Microsoft Foundry is generally available so you can use all the capabilities of Claude in the context of the unified experience in Foundry."
>
> — [3:53](https://www.youtube.com/watch?v=RGSFUqzqErE&t=233s) &middot; *Dated platform announcement, useful as a factual marker.*

> "One is kind of the evolution from simple and isolated data sets to whole company-wide grounding. And the other one is how we started with simple vector search and whatnot and we really saw this evolve into fairly complicated retrieval systems."
>
> — [5:16](https://www.youtube.com/watch?v=RGSFUqzqErE&t=316s) &middot; *Names the two axes the middle of the talk is organized around.*

> "I think, you know, for a hot second as an industry, we thought that if we could get really, really good at computing cosine similarity between vectors, we were all set for retrieval. It turns out, you know, things never are are never that easy."
>
> — [7:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=444s) &middot; *The talk's sharpest rebuke of vector-only retrieval.*

> "And you can see how individual methods don't do as well as combined methods, particularly when you apply them to real-world customer scenarios."
>
> — [7:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=444s) &middot; *The evaluation result behind the hybrid-retrieval position.*

> "Now, the trick is how you build a platform that allows you to combine all these building blocks without putting the complexity right in front of you."
>
> — [7:58](https://www.youtube.com/watch?v=RGSFUqzqErE&t=478s) &middot; *Frames the platform design problem as complexity management.*

> "for easy cases, like, you know, quick single-shot retrieval is great, but for more sophisticated cases, you do want a system that can reflect on on what's in the data set and decide whether or not we've satisfied the information need as stated in the input before we come back with results"
>
> — [8:36](https://www.youtube.com/watch?v=RGSFUqzqErE&t=516s) &middot; *Defines agentic retrieval and scopes when it's warranted.*

> "You can go to the bottom of the stack, you want to build vector indexes and tell us how to quantize the vectors or control lexical retrieval and whatnot. You can do all of that and you can do it in the same stack, which means you can go up and down as you as your needs change."
>
> — [8:36](https://www.youtube.com/watch?v=RGSFUqzqErE&t=516s) &middot; *The layered-abstraction design principle stated directly.*

> "And I can say how much effort you want the model to uh to make or the system to make. And this is effectively a trade-off between latency and quality."
>
> — [10:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=624s) &middot; *Names the explicit tradeoff exposed as a product knob.*

> "every knowledge base is an MCP server, so you can just connect to it uh without having to write any glue code in the middle"
>
> — [10:55](https://www.youtube.com/watch?v=RGSFUqzqErE&t=655s) &middot; *Interoperability claim relevant to anyone with an existing harness.*

> "we carefully evaluate this system to make sure that we give you the most information dense answer that has the fewest tokens uh so that you you know, the the your consumption of tokens has a high value when it comes to all retrieval tasks"
>
> — [12:36](https://www.youtube.com/watch?v=RGSFUqzqErE&t=756s) &middot; *Token efficiency stated as an explicit retrieval optimization target.*

> "learned knowledge is the result of us doing the work we do as individuals and as organizations every day"
>
> — [13:17](https://www.youtube.com/watch?v=RGSFUqzqErE&t=797s) &middot; *Definition of his third knowledge category.*

> "So we built a component called the agent optimizer that effectively goes through this process and allows you to evaluate a baseline, generate candidates, and then you know, evaluate the new candidates and we have a strong result, then deploy that to production."
>
> — [13:59](https://www.youtube.com/watch?v=RGSFUqzqErE&t=839s) &middot; *Describes the optimization loop end to end.*

> "it doesn't matter how you write your agent as long as you externalize configuration like you know, your instructions, tool definitions, skills, and whatnot"
>
> — [13:59](https://www.youtube.com/watch?v=RGSFUqzqErE&t=839s) &middot; *States the one architectural prerequisite for automated optimization.*

> "In this case, this run for maybe 45 minutes or so and you get an optimized version by effectively hill climbing the metric that's established from by evaluation."
>
> — [15:22](https://www.youtube.com/watch?v=RGSFUqzqErE&t=922s) &middot; *Reports a concrete runtime for the optimization loop.*

> "you can see like a bunch of instructions that are not handwritten but that that they emerged out of the hill climbing process"
>
> — [16:06](https://www.youtube.com/watch?v=RGSFUqzqErE&t=966s) &middot; *The payoff of the demo: machine-authored agent instructions.*

## Positions

- Intrinsic model knowledge, not retrieval or tooling, is what triggered the current exponential in AI-assisted work. ([1:01](https://www.youtube.com/watch?v=RGSFUqzqErE&t=61s), confidence: stated)
- Vector similarity search alone is insufficient for retrieval; combining retrieval methods produces measurably better results, especially on real customer scenarios. ([7:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=444s), confidence: stated)
- Agentic retrieval outperforms single-shot retrieval on difficult cases across metrics like evidence recall and answer completeness, but single-shot is adequate for easy cases. ([9:21](https://www.youtube.com/watch?v=RGSFUqzqErE&t=561s), confidence: stated)
- Retrieval effort is a direct latency-versus-quality tradeoff that should be a user-configurable knob rather than a fixed platform choice. ([10:24](https://www.youtube.com/watch?v=RGSFUqzqErE&t=624s), confidence: stated)
- A retrieval platform should be layered so complexity is opt-in — automatic by default, with full control over indexing, quantization, and lexical retrieval available in the same stack. ([7:58](https://www.youtube.com/watch?v=RGSFUqzqErE&t=478s), confidence: stated)
- Agents built for an organization need grounding in ambient company data (documents, email, chat, analytics, web), not just the curated dataset the builder supplies. ([5:16](https://www.youtube.com/watch?v=RGSFUqzqErE&t=316s), confidence: stated)
- Retrieval systems should be optimized for information density per token, not just relevance. ([12:36](https://www.youtube.com/watch?v=RGSFUqzqErE&t=756s), confidence: stated)
- Externalizing agent configuration (instructions, tools, skills) is a precondition for automated agent optimization. ([13:59](https://www.youtube.com/watch?v=RGSFUqzqErE&t=839s), confidence: stated)
- Automatically hill-climbed agent instructions, derived from evals and production traces, can outperform handwritten instructions. ([16:06](https://www.youtube.com/watch?v=RGSFUqzqErE&t=966s), confidence: stated)
- The durable competitive differentiation for a company lies in the learning loop between people and agents, which captures organization-specific knowledge. ([13:17](https://www.youtube.com/watch?v=RGSFUqzqErE&t=797s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent memory](../concepts/agent-memory.md)
- [agentic retrieval](../concepts/agentic-retrieval.md)
- [context engineering](../concepts/context-engineering.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [hybrid retrieval](../concepts/hybrid-retrieval.md)
- [quantization](../concepts/quantization.md)
- [retrieval-augmented generation](../concepts/retrieval-augmented-generation.md)
- [token efficiency](../concepts/token-efficiency.md)

