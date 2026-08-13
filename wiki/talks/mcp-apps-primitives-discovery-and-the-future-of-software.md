---
title: "MCP Apps: Primitives, discovery, and the Future of Software"
type: "talk"
slug: "mcp-apps-primitives-discovery-and-the-future-of-software"
org: "Manufact, Inc"
day: "Day 4 — Session Day 3"
room: "Expo Stage 4 SE"
video_id: "sAOBXCDiDOs"
duration_sec: 1734
word_count: 4772
speakers: ["Pietro Zullo"]
---

# MCP Apps: Primitives, discovery, and the Future of Software

*Program title: The Software Factory*

**Speakers:** [Pietro Zullo](../speakers/pietro-zullo.md)

**Org:** Manufact, Inc

**Day/Room:** Day 4 — Session Day 3 &middot; Expo Stage 4 SE &nbsp;|&nbsp; **Duration:** 28m 54s

[Watch on YouTube](https://www.youtube.com/watch?v=sAOBXCDiDOs)

## Summary

Pietro Zullo, co-founder of Manufact (maker of the MCP-use SDKs), gives a practical tour of MCP apps — the January 2026 official extension of the Model Context Protocol (formerly MCP-UI) that lets MCP servers return interactive UI widgets in sandboxed iframes rather than just JSON. Roughly half the talk is a walkthrough of the app primitives most developers don't know exist: setState for syncing UI state back into model context, follow-up messages sent from the widget, incremental UI updates driven by streaming tool-argument tokens, tool calls triggered from the widget, split outputs that let you show private data to the user while hiding it from the model, and display modes (inline, fullscreen, picture-in-picture). The second half argues the bigger news is distribution: ChatGPT, Claude, and Cursor have all moved from design-partner gating to self-serve submission, giving MCP servers a one-click install channel and, on Claude today, dynamic discovery where the model searches the registry for a connector matching an unmet user intent. The pitch is that being in those stores is now a high-intent acquisition channel, and that if AI apps are the new browsers, MCP apps are the new websites. Watch it if you're shipping an MCP server and want to know what UI you can build and how to actually get distributed.

## Key Points

- MCP UI, which began around May 2025 as a way for MCP servers to return UI components, became MCP apps — the official Model Context Protocol extension — in January 2026.
- An MCP app tool call returns a sandboxed iframe widget instead of a JSON string, with a bidirectional message channel between the widget and the host application.
- The setState primitive lets a widget push its current UI state back into the model's context, so the model knows what the user has selected or is looking at.
- A widget can send follow-up messages to the chat and can trigger additional tool calls; clients differ in behavior, with Claude placing the message in the chat input for user confirmation while ChatGPT sends it directly and starts streaming.
- Because tool arguments stream in token by token, widgets can render incrementally — demonstrated with Excalidraw drawing a mermaid diagram live and a Remotion app rendering React video as tokens arrive.
- Tool results can be split into an output rendered in the widget and a separate output sent to the model, which lets you display private data to the user while telling the model only 'the user is seeing his private information in the widget above.'
- ChatGPT, Claude, and Cursor all now offer self-serve MCP submission after a period of design-partner-only gating; submission involves tool annotation scans, auth verification, and partly manual testing with supplied test prompts.
- Claude already does dynamic discovery — searching the MCP registry for a connector when a task has no matching installed tool — and ChatGPT is expected to follow, making store presence an organic high-intent acquisition channel.
- Servers can detect client capabilities from exchanged metadata and return a widget only to hosts that render them, falling back to a different text output otherwise.

## Notable Quotes

> "MCP apps is now the official extension of the Model Context Protocol that allows to return UI elements within MCP servers."
>
> — [4:10](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=250s) &middot; *Defines the talk's subject and pins its official status.*

> "First, MCP apps. MCP servers are not only returning JSON. And that allows much richer experiences. And the second thing, maybe even bigger, is that the stores opened."
>
> — [4:10](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=250s) &middot; *The speaker's explicit ranking of the two shifts, with distribution rated above the UI capability.*

> "the MCP server in this case doesn't return a JSON string again, but it returns a widget in a sandboxed iframe"
>
> — [5:54](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=354s) &middot; *The core technical mechanism in one line.*

> "So, without UI you would see like a wall of text. The UI allows you to organize the information in a more human readable way."
>
> — [7:28](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=448s) &middot; *States the basic value proposition of widgets over text output.*

> "the model doesn't really know it doesn't really cannot really uh introspect in real time what is going on in the UI"
>
> — [8:08](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=488s) &middot; *Names the problem that the setState primitive exists to solve.*

> "Cloud will display the message in the chat input and tell the user like the user has the choice to send it or not. While OpenAI is a bit more integrated in this sense, it directly sends the model the message to the model"
>
> — [10:28](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=628s) &middot; *Concrete cross-client behavioral difference developers must design around.*

> "If the model streams the input tokens into the tool arguments, you can uh in live take those partial input and update the UI incrementally."
>
> — [11:09](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=669s) &middot; *The streaming-render pattern behind the talk's best demos.*

> "we use Remotion to create a video with React, and uh we render the Remotion video inside the widget in real time as the tokens are streaming in"
>
> — [11:58](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=718s) &middot; *Shows how far the streaming-widget pattern can be pushed.*

> "So, there's two types of output, the ones that are shown in the UI, to put it simply, and the ones that are sent to the model."
>
> — [14:15](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=855s) &middot; *The clearest statement of the dual-output model.*

> "In this case, you can show the UI to the user, but the model won't see the data that you display in the UI, unless you choose so."
>
> — [14:52](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=892s) &middot; *Spells out the privacy guarantee developers can rely on.*

> "the model itself can read those analytics and go do its job on the code you're you're writing"
>
> — [16:59](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1019s) &middot; *Captures the dual-audience design goal: human-readable UI plus machine-readable output.*

> "you're um bringing the three most popular clients, ChatGPT, Claude, and Cursor, which the three of them, they all support a self-serve submission process."
>
> — [22:03](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1323s) &middot; *The distribution claim that motivates the second half of the talk.*

> "MCP apps or servers can be both uh submitted in all these three stores, so you it doesn't need to return a UI your your server to be eligible for submission."
>
> — [22:03](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1323s) &middot; *Corrects a likely misconception about store eligibility.*

> "So, you don't have to share that ugly JSON file anymore with your MCP configuration."
>
> — [24:12](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1452s) &middot; *Memorable framing of what one-click install replaces.*

> "Today Cloud is the only client that actually does this, but for all apps in the stores, when Cloud needs is like assigned a task that doesn't have a specific tool to do, it will actually search in the MCP registry for the right connector to do the task."
>
> — [24:52](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1492s) &middot; *Defines dynamic discovery and states exactly which client ships it today.*

> "if you're there, and you do your work to be the connector that is selected, this is going to be like a a huge wave of uh high intent individuals"
>
> — [25:39](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1539s) &middot; *The acquisition-channel argument in the speaker's own terms.*

> "today I'm checking if a product has an MCP server and that's for me is like the most basic buying decision"
>
> — [26:31](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1591s) &middot; *A personal but pointed claim about MCP support becoming table stakes.*

> "if AI apps are the new browsers, the ChatGPTs are the new websites"
>
> — [27:50](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1670s) &middot; *The talk's central analogy, extending Paul Graham's line.*

> "I don't want to look at your dashboard anymore. I want to use it in Cloud."
>
> — [28:31](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1711s) &middot; *The closing thesis about where software surfaces move.*

## Positions

- The opening of MCP app stores is a bigger development than MCP servers gaining the ability to return UI. ([4:10](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=250s), confidence: stated)
- MCP apps became the official Model Context Protocol extension for returning UI elements in January 2026, superseding MCP UI. ([4:10](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=250s), confidence: stated)
- Claude surfaces widget-originated follow-up messages in the chat input for user approval, while OpenAI's client sends them straight to the model. ([10:28](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=628s), confidence: stated)
- Splitting tool output between widget and model lets developers build MCP apps in privacy-sensitive domains where sending data to an LLM provider is not acceptable. ([14:52](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=892s), confidence: stated)
- Clients that do not support MCP apps simply fail to show the widget, so returning one is not harmful — but developers should return alternate output so the model isn't starved of information. ([19:57](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1197s), confidence: stated)
- A server does not need to return UI to be eligible for submission to the ChatGPT, Claude, or Cursor stores. ([22:03](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1323s), confidence: stated)
- Claude's app submission process is currently slower than ChatGPT's, which has sped up acceptance considerably. ([22:47](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1367s), confidence: stated)
- Claude is currently the only client performing dynamic MCP registry discovery, and ChatGPT is expected to add it soon. ([25:39](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1539s), confidence: stated)
- Being listed in an MCP store drives meaningful traffic to a product. ([26:31](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1591s), confidence: stated)
- Whether a product ships an MCP server is becoming a primary purchasing criterion for buyers. ([26:31](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1591s), confidence: stated)
- Chat clients will displace conventional web dashboards as the primary interface for using software. ([28:31](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1711s), confidence: stated)
- Agent SDK abstractions over the official MCP SDKs let developers ship without learning the underlying spec. ([1:35](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=95s), confidence: implied)

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [agent tool design](../concepts/agent-tool-design.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [generative ui](../concepts/generative-ui.md)
- [model context protocol](../concepts/model-context-protocol.md)
- [session management](../concepts/session-management.md)
- [skill marketplaces](../concepts/skill-marketplaces.md)
- [tool selection](../concepts/tool-selection.md)

