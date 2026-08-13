---
title: "MCP Apps: Extending the Frontier"
type: "talk"
slug: "mcp-apps-extending-the-frontier"
track: "Context Engineering"
org: "Aura (research lab for the agentic web); both speakers work on MCP-UI and are co-creators/maintainers of the MCP Apps spec in the MCP steering committee"
day: "Day 3 — Session Day 2"
room: "Track 8"
video_id: "-jY2T2PiJBE"
duration_sec: 1118
word_count: 3260
speakers: ["Ido Salomon", "Liad Yosef"]
---

# MCP Apps: Extending the Frontier

*Program title: MCP Apps - Extending the frontier*

**Speakers:** [Ido Salomon](../speakers/ido-salomon.md), [Liad Yosef](../speakers/liad-yosef.md)

**Org:** Aura (research lab for the agentic web); both speakers work on MCP-UI and are co-creators/maintainers of the MCP Apps spec in the MCP steering committee

**Track:** Context Engineering &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 8 &nbsp;|&nbsp; **Duration:** 18m 38s

[Watch on YouTube](https://www.youtube.com/watch?v=-jY2T2PiJBE)

## Summary

Ido Salomon and Liad Yosef, creators of MCP-UI and co-maintainers of the official MCP Apps spec, argue that text is the wrong interface for agent-to-service interaction and that the fix is letting servers ship their own interactive UI into the chat host. They trace the path from MCP-UI (launched May of the prior year, with early adopters like 11 Labs, Shopify, Postman, and Goose) to MCP Apps, the official MCP extension built with Anthropic and OpenAI and now supported by Claude, VS Code, ChatGPT, Cursor, and Copilot. The talk walks through the mechanics — a tool call linked to an HTML resource, rendered sandboxed by the host, with a callback channel so user clicks become host-mediated tool calls or prompts — and demos it with a PostHog funnel widget in Claude. The bigger claim is architectural: the web fragments from tabs and dashboards into composable UI 'atoms' assembled by a personal assistant, which inverts control so the host, not the application, owns the user journey. Worth watching if you build MCP servers or care about how agentic distribution and generative UI standards (A2UI, web MCP, declarative UI) will interoperate.

## Key Points

- The main blocker preventing companies from shipping MCP servers is not technical but brand-related: they refuse to be reduced to a textual database that strips their identity and hard-won UX.
- MCP Apps is the official MCP extension, built with Anthropic and OpenAI on top of MCP-UI and other prior art, and OpenAI recommends it as the protocol for building ChatGPT apps.
- The transport mechanism is deliberately mundane: a tool call is linked to an existing MCP resource containing HTML, which the host (often preloaded rather than fetched live) renders in a sandbox via a React or web component plus a callback.
- Interactivity is standardized rather than left to the app — a button click sends an event to the host, not to the vendor's backend, and the host decides whether to call a tool, run a prompt, or ignore it.
- The spec defines three levels of app control over the user journey, from notifying the chat that something happened to handing the chat full responsibility to run a prompt.
- Because everything routes through the chat, no application controls the user journey anymore — the speakers frame this as a win for auditability but it means vendors like Amazon lose visibility into user flows.
- The forward roadmap includes reusable/persistent views (so heavy apps like Autodesk 3D renders aren't re-rendered every turn) and 'app tools' / 'view tools' that let the host drive the app, e.g. filling out a form on the user's behalf.
- MCP Apps is positioned as agnostic across a generative-UI spectrum spanning predefined UI (iframe), declarative UI (JSON render, A2UI), and fully generative UI, with an interoperability guide published for shipping the same server content as A2UI to Gemini and as an MCP app to ChatGPT.
- The distribution argument: ChatGPT reportedly hit 800 million weekly users — roughly 10% of the world population, a scale the web took ~13 years to reach — making MCP Apps a write-once, run-everywhere channel with a far larger addressable market than the early App Store.

## Notable Quotes

> "text is really the worst way to convey a lot of information, right? Because we don't want walls of text."
>
> — [0:55](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=55s) &middot; *The premise the entire talk is built on, stated bluntly.*

> "And actually, this is the main blocker from companies to build an MCP server. They don't want to be reduced to a textual database. They don't want to lose their brand identity in the process."
>
> — [0:55](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=55s) &middot; *Names a business obstacle to MCP adoption most technical talks skip.*

> "So, instead of this, what if the apps could just send their UI to the chat, right? What if every service and every brand could just send their user interface to the chat?"
>
> — [1:36](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=96s) &middot; *The core proposal in one sentence.*

> "just a few months ago, we partnered with Anthropic and OpenAI to create the official extension to MCP, which we call MCP apps based on MCPUI, MCP SDK, and other solutions in the field."
>
> — [2:15](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=135s) &middot; *Establishes the provenance and official standing of the spec.*

> "ChatGPT apps that you know are actually based on MCP apps and open eye actually recommend using MCP apps as the protocol to build ChatGPT apps."
>
> — [3:54](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=234s) &middot; *Concrete adoption claim about a major vendor's recommended path.*

> "The host decides what to do. The host keeps this control of the flow."
>
> — [6:09](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=369s) &middot; *The central architectural commitment — host-mediated, not app-mediated, interaction.*

> "So, it reached out to the PostHog server, got back the textual response. It's factually correct, but it's useless."
>
> — [6:49](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=409s) &middot; *Sharp framing of why correct tool output can still fail the user.*

> "instead of us thinking of the web as tabs or services that we need to consume using a browser, we're now consuming it using our own personal assistants"
>
> — [10:02](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=602s) &middot; *States the broader thesis about the agentic web.*

> "I don't need 99% of the UI that is shown there because this UI doesn't know me. It doesn't have the context on me."
>
> — [10:42](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=642s) &middot; *The argument for UI fragmentation, with a specific (if rhetorical) number.*

> "What if we could just take these UIs and just break them into atoms? And those atoms can be composed by my own personal assistant"
>
> — [10:42](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=642s) &middot; *Introduces the 'UI atoms' framing that structures the second half of the talk.*

> "For Google it's good because it maintains their brand and identity and for the host it's good because they don't need to develop these capability themselves."
>
> — [11:15](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=675s) &middot; *Spells out the three-way incentive alignment the model depends on.*

> "So, this is going to be the shift that we're going to see very soon where websites are going to shift into small chunks of UIs inside inside personal assistants."
>
> — [11:56](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=716s) &middot; *The talk's most falsifiable prediction about the future of the web.*

> "no application will control the user journey anymore. So, Amazon won't be able to know to see my flow. It everything will go through the chat for auditability."
>
> — [12:34](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=754s) &middot; *Names the power shift away from vendors — the part incumbents would contest.*

> "in 2026, we had we had an amazing year of standardizing MCP UI and 2026 is going to be the year where it's going to be a global standard for UI"
>
> — [13:11](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=791s) &middot; *An explicit timeline claim for standardization.*

> "But what if the host or the chat wants to speak to the app? If the user writes something, uh, fill out this form for me and the chat will fill out the form for the user."
>
> — [14:54](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=894s) &middot; *Describes the bidirectional 'app tools' direction that is new in the spec.*

> "MCP apps is agnostic to the way the UI is generated."
>
> — [16:04](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=964s) &middot; *The positioning claim against competing generative-UI standards.*

> "someone said that ChatGPT in particular has 800 million weekly users which is 10% of the entire world population. That's insane."
>
> — [16:42](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1002s) &middot; *The distribution number underpinning the 'new way to distribute applications' argument.*

> "we have like 170 times the total addressable market of the Apple App Store when it launched"
>
> — [17:26](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1046s) &middot; *A specific comparative figure for the opportunity size.*

> "With MCP apps you can write once and run it everywhere."
>
> — [18:04](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1084s) &middot; *The portability promise, stated as the closing pitch.*

## Positions

- Text is the worst medium for conveying dense information in chat interfaces, and factually correct textual tool output is often useless to users. ([0:55](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=55s), confidence: stated)
- Loss of brand identity — being reduced to a textual database — is the primary reason companies have not built MCP servers. ([0:55](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=55s), confidence: stated)
- The host, not the application, should retain control over what happens when a user interacts with embedded UI. ([6:09](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=369s), confidence: stated)
- OpenAI recommends MCP Apps as the protocol for building ChatGPT apps, and ChatGPT apps are themselves built on MCP Apps. ([3:54](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=234s), confidence: stated)
- Websites will fragment into small composable UI chunks rendered inside personal assistants, replacing the multi-tab browsing model. ([11:56](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=716s), confidence: stated)
- Applications will lose the ability to observe or control the user journey, since all interaction routes through the chat host. ([12:34](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=754s), confidence: stated)
- 2026 will be the year MCP Apps becomes the global standard for UI in agent interfaces. ([13:11](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=791s), confidence: stated)
- MCP Apps is agnostic to how UI is generated and can wrap predefined, declarative (A2UI, JSON render), or fully generative UI. ([16:04](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=964s), confidence: stated)
- Claude's 'imagine' generative-UI feature is built on MCP Apps. ([16:04](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=964s), confidence: stated)
- ChatGPT has 800 million weekly users, about 10% of the world population, a scale that took the web roughly 13 years to reach. ([16:42](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1002s), confidence: stated)
- MCP Apps represents an addressable market about 170 times that of the Apple App Store at launch. ([17:26](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1046s), confidence: stated)
- Using the official mcp-apps SDK is preferable to alternatives because spec changes are reflected in it immediately by the maintainers. ([13:44](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=824s), confidence: stated)
- Re-rendering heavy app views on every turn is inefficient, so the spec needs a server-supplied identifier to persist and update a single view. ([14:17](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=857s), confidence: stated)
- MCP Apps is a new application distribution channel, not merely a UI feature. ([16:42](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1002s), confidence: stated)

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [agent sandboxing](../concepts/agent-sandboxing.md)
- [generative ui](../concepts/generative-ui.md)
- [human-ai interaction design](../concepts/human-ai-interaction-design.md)
- [mcp server design](../concepts/mcp-server-design.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [skill marketplaces](../concepts/skill-marketplaces.md)
- [web data infrastructure](../concepts/web-data-infrastructure.md)

