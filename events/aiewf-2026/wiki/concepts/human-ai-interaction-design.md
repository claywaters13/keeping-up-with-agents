---
title: "human-ai interaction design"
type: "concept"
slug: "human-ai-interaction-design"
tier: "supporting"
maturity: "consolidating"
talk_count: 22
speaker_count: 22
---

# human-ai interaction design

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Supporting concept* &middot; discussed across **22** talk(s) by **22** speaker(s)

**Definition:** Designing how people perceive, steer, and collaborate with AI systems — progress disclosure, steering affordances, and trust-shaping UX.

*Also referred to as: ai user experience design, human-centered ai design, interaction design for ai systems, human-agent coordination, human-ai collaboration, agent progress disclosure, agentic workflow transparency, streaming output*

## State of Practice

The dominant claim across this conference is that the binding constraint on agentic products is no longer model capability but the layer between model output and the human — rendering, progress disclosure, approval, and reversibility. Practitioners now treat raw text as a failure mode: agents should emit typed UI intent into a host that renders native components (A2UI, MCP Apps), or author in HTML/CSS/JS, rather than dumping walls of markdown. Trust primitives have converged into a checkable set: show a plan before irreversible actions, stream partial output and chase time-to-first-chunk instead of total latency, keep an always-available stop, keep version history, and preserve a full manual editing surface so users can take the wheel back. The sharpest empirical result came from Duolingo: reviewers scoring above 90% on calibration accepted 50% of fabricated AI flags, and a pure copy change framing the signal as preliminary moved rejection rates 21% — evidence that interaction design, not model quality or reviewer skill, determines oversight quality and the honesty of the labels you log. What remains open is the container: whether chat is the substrate to enrich (MCP Apps, component rendering), to escape entirely for asynchronous background agents or continuously-participating perception interfaces, and how much freedom the model should have over the interface itself — from a fixed, version-gated component catalog to fully generated HTML per user.

## Consensus

### The failure of AI products is in the interaction/delivery layer, not the model; treat interface design as the primary engineering surface.

Support: **6** talk(s)

> "these are delivery problems and they live in between the model output and what's on the screen. That is the layer that decides whether your product succeeds or not."
>
> — [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [2:20](https://www.youtube.com/watch?v=maTp79FD9gI&t=140s)

Supporting talks: [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)

### Before irreversible or high-stakes execution, show the user a plan and get explicit approval rather than acting and reporting after.

Support: **3** talk(s)

> "some actions are usually irreversible and are dangerous actions. And in those cases, you need to present a plan."
>
> — [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [12:13](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=733s)

Supporting talks: [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)

### Delegation only works if the user can take manual control back: keep the conventional editing surface, an abort control, and rollback alongside the agentic path.

Support: **4** talk(s)

> "if they don't have the confidence that, you know, if something goes wrong they can take them back control then then the users will completely lose trust."
>
> — [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [10:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=651s)

Supporting talks: [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)

### Opaque waits are no longer tolerated: stream partial output and disclose what the system is doing, because perceived progress buys latency budget and builds trust in the final answer.

Support: **3** talk(s)

> "Even though it takes 10 seconds, I'm okay if I know what's happening and be able to trust the agent's final output."
>
> — [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [11:15](https://www.youtube.com/watch?v=maTp79FD9gI&t=675s)

Supporting talks: [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)

### A blank prompt box is a design failure; scaffold the entry point with templates, examples, guided workflows, or usage-captured conventions instead of expecting users to prompt well.

Support: **4** talk(s)

> "when we place a blank text box in front of a user and just tell them to ask AI, we're actually kind of asking them to do a lot of work in figuring out how to really use it"
>
> — [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [31:32](https://www.youtube.com/watch?v=L3RuP_q8Bwc&t=1892s)

Supporting talks: [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)

## Disagreements

### Should the interaction be designed to minimize user effort, or to deliberately impose effort at decision points?

| Position A | Position B |
|---|---|
| Add friction on purpose where stakes are high: frame AI output as a preliminary alert, require independent evidence, split the perception judgment from the consequential decision, and reframe the human as investigator rather than validator — because effortless approval produces rubber stamps and false labels.<br>*[Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)* | Strip effort out of the loop: design for delegation not participation, hide the workflow from the user entirely, and treat mechanisms that push verification work back onto the customer (citations, synchronous chat, prompt engineering) as the defect to eliminate.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)* |

*Why it matters: It decides whether your approval surfaces are one-click confirmations or multi-part investigations, and therefore whether the accept/reject events you log are trustworthy training and eval data or noise that makes the next model spuriously confident.*

### Is the chat window the container that agentic UI should be built inside, or the thing to be replaced?

| Position A | Position B |
|---|---|
| Keep the chat host and enrich it: agents send typed UI intent or embedded app views into the conversation, the host retains control of the flow, and websites fragment into composable UI chunks rendered inside personal assistants.<br>*[MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)* | Chat is structurally the wrong protocol — a one-slot batch submission that only engages after the human packages a complete turn. Replace it with asynchronous background agents the user supervises, or with interfaces that perceive the user's screen and participate while they are still working, letting the system choose modality and timing.<br>*[The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Perception Agents](../talks/perception-agents.md)* |

*Why it matters: One path invests in rendering protocols and distribution inside a handful of assistant hosts; the other invests in ambient perception, background execution, and supervision surfaces — incompatible roadmaps and incompatible success metrics (session engagement vs. weekly active users declining).*

### How much freedom should the model have over the interface it produces?

| Position A | Position B |
|---|---|
| Constrain it hard. The model selects from a fixed catalog of components gated by client version and never invents one; a backend absorbs model output so the client stays dumb and safe; adaptation regions like auth and payments are declared permanently off limits; the engine omits scripting entirely.<br>*[Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)* | Let the model author freely in its native languages — HTML, CSS, JavaScript — because any custom DSL, JSON schema, or framework you interpose degrades output quality; the thinnest wrapper wins, and the rendering protocol should stay agnostic all the way up to fully generative UI.<br>*[HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)* |

*Why it matters: It determines whether an unknown content type is a caught schema violation or a mobile client crash that persists for weeks, and whether product differentiation lives in a curated component system or in taste-level skills layered over free generation.*

## Practical Guidance

**Do:**

- Have the agent emit typed UI intent selected from a fixed component catalog, with availability gated by client app version in the model's context (a 2.0 flight card offered only to 2.0+ clients)
- Replace total latency with time to first chunk as the primary UX metric for AI features
- Show a plan and require approval before irreversible actions, with a setting to toggle approval off for repeated flows
- Pause the agent whenever it is about to make an assumption, and hand the decision to the user
- Keep the level-two self-service surface — timeline editor, manual editing, per-file control — alongside the agentic path so users can take the wheel
- Provide an always-available, prominent stop control and version history for non-deterministic output
- Split a single yes/no CTA into separate controls for 'was the model's perception correct' and 'what should we do about it', so logged labels stay honest
- Frame the AI signal in guideline copy as a preliminary alert requiring independent evidence, with the human as final decision-maker
- Log the human's subsequent manual edit, not just the accept/reject event
- Anchor LLM writing feedback inline to specific spans instead of returning a block that rewrites the user's passage
- Deliberately add friction where stakes are high and remove it where oversight is low
- For voice interaction, target visuals as the output to get the ~1 second forgiving envelope, fire inference every 1-2 seconds while the user is still speaking, and use a Haiku-class model on a latency-prioritizing platform
- Keep the first ~90% of the context window identical across requests to get prefix caching (up to 90% cheaper and faster)
- Reuse the app's existing production components rather than introducing a distinct 'agentic' look, and give every rendered element an action payload
- Capture user-specific conventions automatically from observed product usage rather than shipping a separate skill-authoring interface
- Let users point at or annotate on-screen elements as input — a more precise, less lossy signal than a natural-language description
- Explicitly mark AI-generated content, and show a rough time and cost estimate before the user approves an action
- Make agent permissions non-binary and revocable, with a visible history of what was granted and when
- Define the success metric and the data you need before building the system, rather than asking afterward how to evaluate the model

**Avoid:**

- Assuming reviewer skill protects against automation bias — reviewers above 90% calibration accepted 50% of fabricated flags
- Coding-agent patterns that produce one giant diff or a stream of per-file approve prompts; both reduce the developer to a rubber stamp and yield low-information accept/reject data
- Traditional loading spinners for AI features, and opaque waits generally; also use 'thinking' UX sparingly rather than everywhere
- Letting an unknown content type reach an unpatchable mobile client — it crashes rather than degrading, and keeps crashing for days or weeks
- Treating thumbs up/down as sufficient explicit feedback
- Adding more human oversight as the fix for AI quality problems
- Teaching the model a custom DSL or JSON structure for authoring output when it already knows HTML/CSS/JS
- Marketing your AI as more trustworthy than competitors or claiming any tool is 100% hallucination-free
- Using AI to design your AI interfaces — it can only remix existing patterns, and AI interface patterns do not yet exist
- Framing AI as magic (the sparkle icon) instead of giving users clarity about what it is doing
- Making users manage memory visibly without also removing the management burden, as in ChatGPT's v1 fact list
- Expecting consumers to prompt effectively in domains like video; use directional templates as the default entry point
- Shipping citations as your trust mechanism in healthcare, legal, or tax — they push the verification burden back onto the customer

## Notable Outliers

- Changing only the guideline copy — framing the AI signal as preliminary and requiring independent evidence — shifted rejection rates by 21% with no model change and no UI change. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s))
- Weekly active users is the wrong success metric for agentic products; the goal is weekly active sessions rising while WAU declines (though not to zero). ([Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [13:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=816s))
- Prompt engineering is not a power-user skill but a set of packaging rules for a batch protocol; human proficiency at it is evidence of a design failure. ([The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [7:56](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=476s))
- Fully conversational voice-in/voice-out needs 200ms end-to-end, but visual responses tolerate about one second — so voice-in/visuals-out is shippable today without novel architectures. ([Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md), [7:24](https://www.youtube.com/watch?v=65X0pQ6Lmbg&t=444s))
- The model must never invent a component; it picks intent (1-3 flights a swipable carousel, 4+ a vertical list) from a fixed menu you supply. ([Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [7:56](https://www.youtube.com/watch?v=maTp79FD9gI&t=476s))
- One-shotting complete games is not a worthwhile goal; the assistant's job is getting people unstuck so they finish and share, and teaching them the language of game design rather than code. ([The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md), [16:18](https://www.youtube.com/watch?v=VBCDhRrvlYo&t=978s))
- Every user should run their own bounded divergence of a canonical stem, with regions like auth and payments declared permanently off limits to adaptation and rollback possible without a deploy. ([The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [10:25](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=625s))

## All Talks

- [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)
- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Building an Agentic Video Editor for Mass Consumer](../talks/building-an-agentic-video-editor-for-mass-consumer.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Generative Video at the Speed of Light](../talks/generative-video-at-the-speed-of-light.md)
- [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)
- [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- [Lessons from Studying Every Memory System](../talks/lessons-from-studying-every-memory-system.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)
- [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)
- [Perception Agents](../talks/perception-agents.md)
- [Recursive Model Improvement](../talks/recursive-model-improvement.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- [The Next Game Engine Won't Have a Manual](../talks/the-next-game-engine-wont-have-a-manual.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)
- [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)
- [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

## Speakers

- [Allen Pike](../speakers/allen-pike.md)
- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Antje Barth](../speakers/antje-barth.md)
- [Arturo Nunez](../speakers/arturo-nunez.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Bala Ramdoss](../speakers/bala-ramdoss.md)
- [Brendan Rappazzo](../speakers/brendan-rappazzo.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Ekaterina Deyneka](../speakers/ekaterina-deyneka.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Ido Salomon](../speakers/ido-salomon.md)
- [James Russo](../speakers/james-russo.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Keegan McCallum](../speakers/keegan-mccallum.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Liad Yosef](../speakers/liad-yosef.md)
- [Sanja Grbic](../speakers/sanja-grbic.md)
- [Shlok Khemani](../speakers/shlok-khemani.md)
- [Ted Johnson](../speakers/ted-johnson.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Zubin Aysola](../speakers/zubin-aysola.md)

