---
title: "The Prompt is the Platform"
type: "talk"
slug: "the-prompt-is-the-platform"
org: "Resonate HQ"
video_id: "DqtmZE6Hl0g"
duration_sec: 1053
word_count: 2075
speakers: ["Dominik Tornow"]
---

# The Prompt is the Platform

**Speakers:** [Dominik Tornow](../speakers/dominik-tornow.md)

**Org:** Resonate HQ

**Duration:** 17m 33s

[Watch on YouTube](https://www.youtube.com/watch?v=DqtmZE6Hl0g)

## Summary

Dominik Tornow, founder/CEO of Resonate, argues that as coding agents make implementations cheap to generate, reuse moves upstream: the durable product becomes the abstract specification (the protocol), and target-specific implementations get synthesized on demand onto whatever infrastructure a customer already runs. He reports a concrete failure — asking an agent to jump straight from an abstract spec to a production Rust/Postgres server produced a happy-path prototype that broke under concurrency, process failure, and network failure — and two successive fixes. The first fix inserted a human-driven concrete specification (schema, indices, queries, transaction boundaries), which worked but left the agent doing implementation rather than design. The second fix, used for Resonate on NATS.io, gave the agent a deterministic simulation environment where it first builds an executable design, discovers the correct algorithm under partial failure via fuzz testing, then writes the concrete spec and only then the production code. Worth watching if you care about how to structure agentic engineering for distributed-systems correctness, and specifically for the 'forbidden fruit' trick of exposing simulation-only facts (was this read stale? what was the value you missed?) to the agent as debugging signal.

## Key Points

- Resonate's working theory is that general-purpose implementations will be replaced by bespoke implementations generated on demand as minimal extensions of infrastructure a customer already has in place.
- If implementations become generatable, a vendor's value migrates from implementation to specification — Resonate now treats the protocol, not the server, as the product, with the reference server as just one derived implementation.
- To support many target-specific implementations, the abstract specification must assume nothing about the target: no schema, no indices, not even whether there is a relational database, a key-value store, weak consistency, or strong consistency.
- The naive one-shot prompt ('build a Resonate server in Rust on top of Postgres') failed: the generated system passed basic tests but broke on concurrency, process failure, and network failure.
- Inserting a human-driven concrete specification (data schema, indices, SQL queries, transaction boundaries) let the agent produce a production system, but the agent was only building, not designing.
- The NATS approach moves the agent upstream: it first builds a simulated implementation as 'executable design' to discover the correct algorithm under partial order and partial failure, then writes the concrete spec, then the production implementation.
- Correctness must hold whenever the target behaves legally, not merely conveniently — the NATS KV store's versioned reads may legitimately return stale values, discovered only when the optimistic-concurrency write fails.
- Deterministic simulation is what makes agents effective here: it is repeatable and inspectable, so a failing execution can be reproduced exactly and repaired against the trace.
- The 'forbidden fruit' is simulation-only trace data (fresh vs. stale read, and the latest value the algorithm was not allowed to see) that the algorithm may not depend on but the agent can use to explain why its design was wrong.
- Minimalism and simplicity are prerequisites, not defaults: three years of removing abstractions, properties, and relationships reduced the protocol to two objects, a durable promise and a durable task.

## Notable Quotes

> "In 2026, coding agents will quietly retire their first software platform. Not because it's bad, simply because the platform is unnecessary."
>
> — [0:02](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=2s) &middot; *the thesis, stated as a dated prediction*

> "General-purpose implementations will increasingly be replaced by bespoke implementations generated on demand."
>
> — [0:02](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=2s) &middot; *the core industry claim the rest of the talk is downstream of*

> "Instead of reusing a general-purpose implementation, we will reuse a specification, and we will derive a bespoke implementation from it."
>
> — [1:00](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=60s) &middot; *defines what 'reuse moves upstream' concretely means*

> "If implementations become generatable, where does our value live? And our answer? Our value moves from implementation to specification."
>
> — [1:00](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=60s) &middot; *frames the business consequence for infrastructure vendors*

> "The product is no longer the implementation. The product is the specification, the protocol."
>
> — [2:02](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=122s) &middot; *the sharpest statement of the strategic bet*

> "The question is, can we repeatedly synthesize trusted servers from the same specification?"
>
> — [2:02](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=122s) &middot; *reframes the engineering problem from capability to repeatability and trust*

> "The specification must be abstract. Only the implementation must be concrete."
>
> — [4:52](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=292s) &middot; *the design constraint that makes multi-target synthesis possible*

> "And the agent failed. The gap between the abstract specification and the concrete implementation was too large."
>
> — [4:52](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=292s) &middot; *reports a negative result rather than a demo success*

> "It passed the basic tests, but it was not correct. It broke on the concurrency. It broke on the process failure. It broke on the network failure."
>
> — [4:52](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=292s) &middot; *specifies exactly how agent-generated distributed code fails*

> "The agent helped us build the system, but the agent did not help us design the system."
>
> — [5:46](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=346s) &middot; *names the limitation that motivates the whole simulation approach*

> "Do not build the production system. Build a simulated implementation. The simulated implementation is not the product. It is executable design."
>
> — [6:50](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=410s) &middot; *the central methodological move, in one line*

> "Unfortunately, minimalism and simplicity are not the starting point. They are the finish line. We spent 3 years making the protocol smaller and simpler."
>
> — [7:58](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=478s) &middot; *a cost number attached to the precondition others will want to skip*

> "Every time we ran into a problem, we asked, what can we take away? What abstraction can we erase? What property can we remove? What relationship can we break?"
>
> — [7:58](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=478s) &middot; *an actionable heuristic for shrinking a protocol*

> "our implementation cannot be correct only when the target behaves conveniently. The implementation has to be correct when the target behaves legally."
>
> — [10:04](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=604s) &middot; *the correctness standard, stated as a tradeoff against happy-path testing*

> "Building always correct applications on top of a concurrency model that allows occasional stale reads is not simple. Not for humans."
>
> — [11:02](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=662s) &middot; *concedes the difficulty is intrinsic, not an agent deficiency*

> "Agents thrive on feedback. Immediate unambiguous feedback. Not just feedback that shows this went wrong. Feedback that shows why and how this went wrong."
>
> — [11:57](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=717s) &middot; *the design principle behind the simulation tooling*

> "unlike the real target, the simulation is deterministic, it's repeatable, and it's inspectable. So, when the agent writes the wrong algorithm, we can reproduce the exact execution that broke it."
>
> — [12:55](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=775s) &middot; *states why determinism specifically matters for agent-driven debugging*

> "That information is forbidden to the algorithm, but it is incredibly useful to the agent."
>
> — [13:56](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=836s) &middot; *the 'forbidden fruit' idea compressed to one sentence*

> "Not just the invariant failed, but the invariant failed because the algorithm made a decision from a stale view of the world."
>
> — [14:55](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=895s) &middot; *shows the granularity of feedback an agent needs on distributed bugs*

> "The agent does not just learn that the system is wrong, it learns why the system is wrong."
>
> — [15:51](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=951s) &middot; *the payoff claim for the whole tracing approach*

> "Deterministic simulation lets agents participate in the design, not just in the implementation."
>
> — [16:49](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=1009s) &middot; *the talk's conclusion about where agents can move*

> "The prompt is the platform and the specification is the product."
>
> — [16:49](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=1009s) &middot; *the title thesis in final form*

## Positions

- General-purpose software platforms will increasingly be displaced by bespoke implementations generated on demand as minimal extensions of existing infrastructure. ([0:02](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=2s), confidence: stated)
- For infrastructure vendors, value shifts from the implementation to the specification/protocol, which becomes the actual product. ([1:00](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=60s), confidence: stated)
- A specification intended to yield multiple target-specific implementations must not assume any storage model at all — not a relational database, not a key-value store, not weak or strong consistency. ([4:00](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=240s), confidence: stated)
- Asking an agent to go directly from an abstract specification to a production distributed system does not work; the result passes basic tests but breaks under concurrency, process failure, and network failure. ([4:52](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=292s), confidence: stated)
- Inserting a human-driven concrete specification is sufficient to get a production implementation out of an agent, but insufficient if the specification itself is meant to be the reusable product. ([5:46](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=346s), confidence: stated)
- Agents should be moved upstream into design, with humans still involved but the agent as driver. ([7:58](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=478s), confidence: stated)
- The correct pipeline is abstract specification → simulation implementation → concrete specification → concrete implementation. ([7:58](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=478s), confidence: stated)
- Protocol minimalism and simplicity are prerequisites for agent-driven synthesis, and they take years of deliberate removal to reach rather than being available up front. ([7:58](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=478s), confidence: stated)
- Even simple protocols built on a few simple primitives have complex state and behavior spaces, making them hard to implement correctly. ([9:01](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=541s), confidence: stated)
- Implementations must be correct under every legal behavior of the target platform, not just its convenient behaviors. ([10:04](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=604s), confidence: stated)
- Agents need feedback that explains why and how something failed, not merely that it failed; generic test failures are insufficient for distributed algorithm design. ([11:57](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=717s), confidence: stated)
- Simulations should deliberately expose information the real platform hides (whether a read was stale, and the latest value missed) to the agent, even though production algorithms must not depend on it. ([13:56](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=836s), confidence: stated)
- A simulation only needs to reproduce the parts of the target platform that matter for correctness, not the full system. ([12:55](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=775s), confidence: implied)
- With deterministic simulation plus fuzz testing, an agent can design and build a correct distributed platform implementation from a single abstract specification. ([15:51](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=951s), confidence: stated)
- Discussion of agentic engineering overweights verification and underweights how agents can participate in specification. ([2:02](https://www.youtube.com/watch?v=DqtmZE6Hl0g&t=122s), confidence: stated)

## Concepts

- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [ai-assisted vulnerability discovery](../concepts/ai-assisted-vulnerability-discovery.md)
- [durable execution](../concepts/durable-execution.md)
- [mcp server design](../concepts/mcp-server-design.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)
- [simulation environments](../concepts/simulation-environments.md)
- [spec-driven development](../concepts/spec-driven-development.md)

