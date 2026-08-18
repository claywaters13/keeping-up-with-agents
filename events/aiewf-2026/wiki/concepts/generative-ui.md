---
title: "generative ui"
type: "concept"
slug: "generative-ui"
tier: "supporting"
maturity: "consolidating"
talk_count: 9
speaker_count: 10
---

# generative ui

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **9** talk(s) by **10** speaker(s)

**Definition:** Interfaces the model generates or drives at runtime — rendered components, ephemeral views, server-driven layouts — rather than fixed screens.

*Also referred to as: server-driven ui, ephemeral ui, declarative ui specs, tool result ui rendering, streaming ui, sandboxed iframe widgets, rendering contract*

## State of Practice

The field has stopped treating generative UI as "the model writes HTML" and converged on a data-and-catalog model: the agent emits typed UI intent — component blocks, registered primitives, or a widget reference — and a client renders it with native or vendor-supplied widgets. The protocol layer consolidated fast during this cycle: MCP Apps became the official Model Context Protocol extension for returning UI (superseding MCP UI), ChatGPT apps are built on it, Claude's 'imagine' generative-UI feature rides on it, and teams not on MCP are using A2UI or A2A as the front-end/back-end contract. The engineering problems that actually bite are downstream of the model: unknown component types crashing unpatchable mobile clients, gating component availability by app version, splitting tool output between what the widget shows and what the model sees, and streaming partial tool arguments so a view can update incrementally. Latency thinking has shifted from total completion time to time-to-first-chunk, with visual output explicitly chosen because its ~1s tolerance envelope is far more forgiving than the 200ms voice-conversation budget. The unsettled part is authority and location: how much the model is allowed to invent versus select, and whether generated UI lives inside your product or inside someone else's chat host.

## Consensus

### Text is the wrong output medium for dense tool results; agents should return structured UI that a client renders, not prose or raw JSON.

Support: **4** talk(s)

> "So, it reached out to the PostHog server, got back the textual response. It's factually correct, but it's useless."
>
> — [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [6:49](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=409s)

Supporting talks: [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)

### The model should select from a bounded, pre-registered set of components or capabilities rather than freely author UI, with the client or host retaining final control over what renders and what a tap does.

Support: **4** talk(s)

> "And notice what the model never does. It never invents a component. It chooses from a fixed menu that you provide to it."
>
> — [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [7:56](https://www.youtube.com/watch?v=maTp79FD9gI&t=476s)

Supporting talks: [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)

### A rigorous external spec (MCP Apps, A2UI, A2A) should be the contract between agent and renderer, rather than each team inventing a bespoke rendering protocol.

Support: **4** talk(s)

> "having this kind of rigorous protocol, this rigorous spec really helped drive our development and drive alignment because, you know, all we had to do was um align with this spec and follow this spec and we knew that this was kind of the contract that our front end and back end would both consume and and produce"
>
> — [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [8:14](https://www.youtube.com/watch?v=4uFVSLgD2Q4&t=494s)

Supporting talks: [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)

### Perceived latency is governed by how fast something appears and updates incrementally, not by total completion time; render partial state as tokens stream rather than waiting for a complete response.

Support: **3** talk(s)

> "you stop chasing the total latency, which we have done for over a decade. You start chasing time to first chunk."
>
> — [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [9:40](https://www.youtube.com/watch?v=maTp79FD9gI&t=580s)

Supporting talks: [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)

### The fixed one-size-fits-all screen is obsolete because it carries no context about the individual user; interfaces should be assembled or adapted per user at runtime.

Support: **3** talk(s)

> "I don't need 99% of the UI that is shown there because this UI doesn't know me. It doesn't have the context on me."
>
> — [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [10:42](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=642s)

Supporting talks: [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md)

## Disagreements

### How much latitude should the model have to generate UI at runtime — selection from a fixed catalog, or open-ended generation?

| Position A | Position B |
|---|---|
| Constrain the model to a declarative catalog of pre-shipped components; production apps (especially mobile) should stay in the controlled or declarative tiers because an unknown content type crashes an unpatchable client, and component availability must be gated by app version.<br>*[Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)* | Let the model generate the interface itself at runtime — fully generative widgets, per-user code divergences, software-on-demand — and manage the risk with isolation and bounded off-limits regions rather than a fixed component menu.<br>*[The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)* |

*Why it matters: It determines whether you invest in a versioned component catalog and a BFF that sanitizes model output, or in sandboxing, provenance, and per-context rollback infrastructure. The two architectures share almost no components.*

### Where does generative UI actually live — inside a third-party chat host, or inside your own product surface?

| Position A | Position B |
|---|---|
| Inside the host. Websites fragment into composable UI atoms rendered by a personal assistant, chat clients displace dashboards, MCP stores become the distribution channel, and applications lose the ability to observe or control the user journey.<br>*[MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)* | Inside your own app. Agentic UI should reuse the app's existing production components and action payloads rather than introducing a distinct agentic look, with a BFF absorbing model output so the client stays dumb and safe; adaptation happens per user against your own canonical stem.<br>*[Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)* |

*Why it matters: If UI migrates into hosts, the investment is in MCP server distribution and store placement, and you accept losing funnel analytics and journey control; if it stays in-product, the investment is in a rendering layer, component versioning, and your own agent loop.*

### Now that models can generate interfaces cheaply, what is the actual bottleneck?

| Position A | Position B |
|---|---|
| Idea generation. Models will one-shot essentially any build very soon, so the scarce resource is imagination — any recurring friction is worth generating a custom tool for on the spot.<br>*[Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md)* | Everything around generation. Code and UI generation is the easy 80%; the durable work is the rendering/delivery layer, observability, validation, provenance, and human understanding of what was produced.<br>*[The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)* |

*Why it matters: It decides where a team spends headcount — on faster prototyping loops and prompt surface, or on the measurement, isolation, and comprehension infrastructure that makes runtime-generated interfaces safe to ship.*

### Is just-in-time, per-user generated software a net improvement over shipped software?

| Position A | Position B |
|---|---|
| Yes — the one-version-for-everyone model was an artifact of cost, not merit; cheap correct changes mean every user can run their own adapted divergence, and horizontal SaaS can serve far more personas without more R&D spend.<br>*[The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md)* | Not on its current trajectory — we are automating the writing of software without increasing its expressiveness, and cheaply generated artifacts degrade human understanding like technical debt until you can no longer participate in your own project.<br>*[What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)* |

*Why it matters: If generation quantity is the win, you optimize for throughput of adaptations; if expressiveness and comprehension are the constraint, you gate generated UI behind understanding checks and measure it against goal metrics like retention and support volume rather than shipping speed.*

## Practical Guidance

**Do:**

- Have the agent emit UI as data — a list of typed component blocks the client renders with its own native widgets — instead of text or HTML.
- Supply the component catalog in the model's context and gate each component by client app version (e.g. offer a 2.0 flight card only to 2.0+ clients).
- Attach an action payload to every rendered element so tap behavior and deep links are defined by the client, not inferred by the model.
- Put a BFF between the model and the client to absorb and validate model output so the client stays dumb and safe.
- Replace total latency with time-to-first-chunk as the primary UX metric for AI features, and show a 'thinking' state sparingly instead of a spinner.
- Stream partial tool-call arguments into the widget and update it incrementally as tokens arrive rather than rendering only on completion.
- Choose voice-in/visuals-out to exploit the ~1s visual response envelope instead of chasing the 200ms budget a fully conversational voice loop requires.
- Split tool output into a widget channel and a model channel so sensitive displayed data never has to reach the LLM provider.
- Deterministically interrupt the agent loop for tool-call approval on mutating operations rather than letting the model decide when to ask.
- Return an alternate textual output alongside a widget so clients that don't support MCP Apps don't starve the model of information.
- Declare regions like auth and payments permanently off limits to runtime adaptation while leaving surface concerns like form layout adaptable.
- Reuse existing production components so agentic surfaces look like the rest of the app rather than a distinct 'AI' style.
- Keep a hand-maintained markdown glossary of a project's content for agents to read instead of making them parse the rendered page.

**Avoid:**

- Letting the model invent components or content types — an unrecognized type doesn't degrade gracefully on mobile, it crashes and keeps crashing for days or weeks.
- Shipping fully open-ended generative UI in a production mobile app when a controlled or declarative tier would do.
- Returning factually correct walls of text from a tool and calling the job done — correct text output is frequently useless to the user.
- Assuming a small model is a fast model: GPT-5 mini showed 5,000ms typical and 7,000ms P95 latencies, unusable for real-time interaction.
- Waiting for a second of silence before firing inference in a voice-driven interface; that alone blows the latency budget.
- Re-rendering a heavy app view on every conversational turn instead of persisting and updating one identified view.
- Traditional loading spinners for AI features — users have left the forgiving phase and expect to see what is happening.
- Treating generated UI as brittle because it is AI-generated; the real failure mode is unmanaged divergence inside a single tangled artifact with no boundaries.
- Judging adaptations by correctness tests alone rather than tying them to goal metrics like retention, churn, or support ticket volume.
- Shipping agent-written code you cannot explain — degraded understanding compounds like tech debt until you can't contribute to your own project.

## Notable Outliers

- MCP Apps represents roughly 170 times the total addressable market of the Apple App Store at its launch, and is a distribution channel rather than a UI feature. ([MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [17:26](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1046s))
- The two major hosts already diverge on agency: Claude puts a widget-originated follow-up message in the chat input for the user to approve, while OpenAI's client sends it straight to the model. ([MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [10:28](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=628s))
- With no single artifact, identifying what a user is running becomes a graph query over immutable divergences instead of a version-number lookup. ([The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [13:42](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=822s))
- The future of design is mostly sliders and user-adjustable parameters rather than fixed designed states. ([Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md), [6:14](https://www.youtube.com/watch?v=Z2Erdirpudo&t=374s))
- Claude is currently the only client doing dynamic MCP registry discovery — searching the registry for the right connector when assigned a task with no matching tool. ([MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [24:52](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1492s))
- The just-in-time software boom is automating the writing of software without increasing its expressiveness — SaaS has not meaningfully changed since 2019 apart from chatbots latched on. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [11:55](https://www.youtube.com/watch?v=cJ0EOzey--o&t=715s))
- Interactive figures are frequently slop and a crutch; add interactivity only where static explanation genuinely falls short. ([Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md), [9:12](https://www.youtube.com/watch?v=WkBPX-oDMnA&t=552s))

## All Talks

- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [Agents in Production: How OpenGov Built and Scaled OG Assist](../talks/agents-in-production-how-opengov-built-and-scaled-og-assist.md)
- [Imagination Engineering: "Live in the future and then build what's missing."](../talks/imagination-engineering-live-in-the-future-and-then-build-whats-missing.md)
- [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)
- [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)
- [Understanding is the new bottleneck](../talks/understanding-is-the-new-bottleneck.md)
- [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

## Speakers

- [Allen Pike](../speakers/allen-pike.md)
- [Bala Ramdoss](../speakers/bala-ramdoss.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Eve Bouffard](../speakers/eve-bouffard.md)
- [Gabe De Mesa](../speakers/gabe-de-mesa.md)
- [Geoffrey Litt](../speakers/geoffrey-litt.md)
- [Ido Salomon](../speakers/ido-salomon.md)
- [Liad Yosef](../speakers/liad-yosef.md)
- [Pietro Zullo](../speakers/pietro-zullo.md)
- [Varun Singh](../speakers/varun-singh.md)

