---
title: "Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing"
type: "talk"
slug: "agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing"
org: "Amazon Lens"
video_id: "maTp79FD9gI"
duration_sec: 852
word_count: 2032
speakers: ["Bala Ramdoss"]
---

# Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing

**Speakers:** [Bala Ramdoss](../speakers/bala-ramdoss.md)

**Org:** Amazon Lens

**Duration:** 14m 12s

[Watch on YouTube](https://www.youtube.com/watch?v=maTp79FD9gI)

## Summary

Bala Ramdoss argues that the hardest part of shipping agentic products isn't the model — it's the rendering layer between model output and the screen. Using a restaurant-booking example (a wall of correct-but-useless text versus a two-tap booking card), he frames chat text as a delivery failure rather than a model failure, then walks through three patterns for fixing it: a versioned rendering contract that tells the model which components the client can actually draw, streaming typed UI chunks instead of text so you optimize time-to-first-chunk rather than total latency, and a backend-for-frontend that hydrates components, attaches action payloads, and carries conversational context so the client can stay dumb and safe. The mobile constraint drives the whole design: you cannot meaningfully patch hundreds of millions of installs, so an unknown component type doesn't degrade, it crashes for weeks. Worth watching if you're putting agent output in front of real users, especially in a native app, and want concrete architecture rather than chat-UI aesthetics.

## Key Points

- The failure mode in most agentic products is delivery, not intelligence: the model produces correct information but the product forces the user to do the remaining work manually.
- Generative UI now has a shared vocabulary and an open spec (A2UI from Google), where the agent describes UI as data — a list of components the client renders with its own native widgets — instead of returning text or HTML.
- Generative UI is a spectrum with three tiers (per CopilotKit): controlled, where the model picks a prebuilt component; declarative, where it composes from a catalog; and fully open-ended, where it invents novel UI — and the higher you go, the more the client must trust the model.
- Most production mobile apps should stay in the bottom two tiers, because mobile can't hot-fix: an unrecognized content type crashes rather than degrading, and keeps crashing for weeks on un-updated installs.
- The rendering contract should be version-aware — a new flight card introduced in app version 2.0 is only surfaced to the model from 2.0 onward — so the client never has to infer intent from raw tokens.
- The contract can encode layout rules themselves (one to three flights renders as a swipeable carousel, four or more as a vertical list) while the model only picks from a fixed, handful-sized menu of components.
- Streaming changes the metric that matters: stop optimizing total latency and start optimizing time to first chunk, rendering a skeleton, then a partial fill, then completion.
- Loading spinners no longer work for AI features; users have left the forgiving phase and expect visible progress — either a 'thinking' UX used sparingly or an engaging interaction like Lens Live's tap-to-focus while results load.
- The BFF does more than ship layout: it handles hydration, attaches action payloads (taps, deep links, impression metrics) to every element, and carries conversational context across turns.
- This approach reuses UI components the app already ships in production, so the agentic surface keeps the same brand, density, and native feel rather than becoming a bolted-on AI look.

## Notable Quotes

> "The model did the real work, but look at the outcome. I have to do my research and work towards actually booking the table."
>
> — [0:01](https://www.youtube.com/watch?v=maTp79FD9gI&t=1s) &middot; *The opening example that defines the whole problem: correct output, failed product.*

> "The only thing that you need to focus on is the layer between the model and something that a human can interact with."
>
> — [0:45](https://www.youtube.com/watch?v=maTp79FD9gI&t=45s) &middot; *States the talk's thesis in one line.*

> "none of these problems are due to the model itself. The model does its job well."
>
> — [2:20](https://www.youtube.com/watch?v=maTp79FD9gI&t=140s) &middot; *Explicitly relocates blame from model capability to delivery.*

> "these are delivery problems and they live in between the model output and what's on the screen. That is the layer that decides whether your product succeeds or not."
>
> — [2:20](https://www.youtube.com/watch?v=maTp79FD9gI&t=140s) &middot; *The strongest version of his central claim about where product success is determined.*

> "Instead of the agent handing you a raw text or HTML, it describes the UI as data. A list of components and the client renders them with its own native widgets."
>
> — [3:03](https://www.youtube.com/watch?v=maTp79FD9gI&t=183s) &middot; *Cleanest definition of generative UI / A2UI in the talk.*

> "The higher you go, the more your client has to trust whatever the model hands it."
>
> — [4:43](https://www.youtube.com/watch?v=maTp79FD9gI&t=283s) &middot; *Names the core tradeoff along the generative-UI spectrum.*

> "when a client meets a content type it's never seen, it doesn't gracefully degrade, it crashes. And it keeps crashing for days or weeks"
>
> — [5:25](https://www.youtube.com/watch?v=maTp79FD9gI&t=325s) &middot; *Concrete failure mode justifying conservative mobile design.*

> "So, one rule holds everything that follows for mobile clients. You cannot meaningfully patch the client."
>
> — [5:25](https://www.youtube.com/watch?v=maTp79FD9gI&t=325s) &middot; *The constraint the speaker says drives every subsequent pattern.*

> "In this example, one to three flights a swipable carousel. Four or more, a vertical list. The model picks the intent."
>
> — [7:56](https://www.youtube.com/watch?v=maTp79FD9gI&t=476s) &middot; *Specific example of layout rules living in the contract, not the model.*

> "And notice what the model never does. It never invents a component. It chooses from a fixed menu that you provide to it."
>
> — [7:56](https://www.youtube.com/watch?v=maTp79FD9gI&t=476s) &middot; *The hard boundary he draws on model authority over UI.*

> "It may take 3 to 4 seconds to get there, but the wait is bearable."
>
> — [9:40](https://www.youtube.com/watch?v=maTp79FD9gI&t=580s) &middot; *Puts a number on acceptable perceived latency under progressive rendering.*

> "you stop chasing the total latency, which we have done for over a decade. You start chasing time to first chunk."
>
> — [9:40](https://www.youtube.com/watch?v=maTp79FD9gI&t=580s) &middot; *A concrete metric change teams can adopt directly.*

> "For this reason, the traditional loading spinner won't work for AI features."
>
> — [9:40](https://www.youtube.com/watch?v=maTp79FD9gI&t=580s) &middot; *A blunt design prescription others might contest.*

> "The overall AI users have moved out of the forgiving phase, and now they expect to know what is happening."
>
> — [10:33](https://www.youtube.com/watch?v=maTp79FD9gI&t=633s) &middot; *Claim about shifting user expectations that motivates progress UX.*

> "Even though it takes 10 seconds, I'm okay if I know what's happening and be able to trust the agent's final output."
>
> — [11:15](https://www.youtube.com/watch?v=maTp79FD9gI&t=675s) &middot; *Ties visible agent progress to trust in the output, not just patience.*

> "Every rendered element carries an action payload to handle what what a tap does, what the deep link hit opens."
>
> — [12:01](https://www.youtube.com/watch?v=maTp79FD9gI&t=721s) &middot; *Specifies what the BFF adds beyond layout.*

> "let the BFF absorb the model output so the client can stay dumb and safe."
>
> — [12:56](https://www.youtube.com/watch?v=maTp79FD9gI&t=776s) &middot; *The architectural takeaway in one clause.*

> "No, none of these are about the model. The model was fine. This layer is what ships the product."
>
> — [12:56](https://www.youtube.com/watch?v=maTp79FD9gI&t=776s) &middot; *Closing summary of the argument.*

> "your agent output is not the CX. You build on it."
>
> — [13:52](https://www.youtube.com/watch?v=maTp79FD9gI&t=832s) &middot; *The title claim, stated plainly at the close.*

## Positions

- The bottleneck in agentic products is the rendering layer between model output and screen, not model capability. ([2:20](https://www.youtube.com/watch?v=maTp79FD9gI&t=140s), confidence: stated)
- Agents should emit typed UI intent (component blocks) rather than text or HTML. ([7:02](https://www.youtube.com/watch?v=maTp79FD9gI&t=422s), confidence: stated)
- The model must never invent a component; it should only select from a fixed catalog supplied in its context. ([7:56](https://www.youtube.com/watch?v=maTp79FD9gI&t=476s), confidence: stated)
- Most production mobile apps should stay in the controlled or declarative tiers of generative UI, not fully open-ended generation. ([4:43](https://www.youtube.com/watch?v=maTp79FD9gI&t=283s), confidence: stated)
- Mobile clients cannot be meaningfully patched, so unknown content types cause crashes that persist for days or weeks. ([5:25](https://www.youtube.com/watch?v=maTp79FD9gI&t=325s), confidence: stated)
- Component availability must be gated by app version in the model's context (e.g. a 2.0 flight card only offered to 2.0+ clients). ([7:02](https://www.youtube.com/watch?v=maTp79FD9gI&t=422s), confidence: stated)
- Teams should replace total latency with time to first chunk as the primary UX metric for AI features. ([9:40](https://www.youtube.com/watch?v=maTp79FD9gI&t=580s), confidence: stated)
- Traditional loading spinners are inadequate for AI features because users no longer tolerate opaque waits. ([9:40](https://www.youtube.com/watch?v=maTp79FD9gI&t=580s), confidence: stated)
- Showing a 'thinking' UX builds trust in the agent's final output, but should be used sparingly. ([10:33](https://www.youtube.com/watch?v=maTp79FD9gI&t=633s), confidence: stated)
- Agentic UI should reuse an app's existing production components rather than introducing a distinct 'agentic' look. ([12:01](https://www.youtube.com/watch?v=maTp79FD9gI&t=721s), confidence: stated)
- A standardized spec (A2UI) means teams no longer have to solve the rendering layer bespoke each time. ([3:03](https://www.youtube.com/watch?v=maTp79FD9gI&t=183s), confidence: implied)

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [context engineering](../concepts/context-engineering.md)
- [generative ui](../concepts/generative-ui.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [latency budgets](../concepts/latency-budgets.md)

