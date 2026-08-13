---
title: "human-ai interaction design"
type: "concept"
slug: "human-ai-interaction-design"
tier: "supporting"
maturity: "contested"
talk_count: 18
speaker_count: 18
---

# human-ai interaction design

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **18** talk(s) by **18** speaker(s)

**Definition:** Designing how people perceive, steer, and collaborate with AI systems — progress disclosure, steering affordances, and trust-shaping UX.

*Also referred to as: ai user experience design, human-centered ai design, interaction design for ai systems, human-agent coordination, human-ai collaboration, agent progress disclosure, agentic workflow transparency, streaming output*

## State of Practice

The field has converged on a blunt diagnosis: for agentic products, the model is rarely the limiting factor — the layer between model output and human perception is. Speakers from Amazon Lens, Duolingo, Filed, Progress Software and JoinIn all independently traced product failures (crashes, rubber-stamped approvals, abandoned features, unusable answers) to interaction and rendering decisions rather than model quality, and several demonstrated large behavioral swings from interface-only changes — Duolingo shifted reviewer rejection rates 21% by rewriting guideline copy alone, with no model or UI change. Practically, this cashes out as: agents should emit typed, structured UI intent (component blocks, HTML, MCP Apps payloads) rather than raw text; time-to-first-chunk replaces total latency as the primary UX metric; provenance traces and plan-before-execute gates are the mechanisms that actually build trust, while citations alone are considered a cost transfer onto the user; and users must always retain an abort control, version history, and a self-service path back to manual operation. A second, sharper thread treats every interaction as a labeling event — the accept/reject CTA you ship becomes your next training set, so conflated yes/no buttons and thumbs-up/down widgets are now treated as data-quality bugs, not just UX blemishes. The unresolved fault line is directional: one camp wants deliberate friction and human investigation designed into high-stakes moments, while another argues the entire human-in-the-loop framing is the defect and the goal is to earn enough trust that humans step out.

## Consensus

### The binding constraint on agentic product quality is the interaction/rendering layer, not model capability — teams diagnosing product failures repeatedly found the model was performing correctly.

Support: **5** talk(s)

> "these are delivery problems and they live in between the model output and what's on the screen. That is the layer that decides whether your product succeeds or not."
>
> — [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [2:20](https://www.youtube.com/watch?v=maTp79FD9gI&t=140s)

Supporting talks: [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)

### Raw text is the wrong default output medium for agents; agents should emit structured, renderable artifacts (typed component blocks, HTML/CSS/JS, embedded app UI) instead of prose or walls of markdown.

Support: **5** talk(s)

> "So, it reached out to the PostHog server, got back the textual response. It's factually correct, but it's useless."
>
> — [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [6:49](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=409s)

Supporting talks: [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)

### Users tolerate long waits when the process is visible; progress disclosure, streaming partial output, and per-value traces are what convert latency into trust — opaque waits are no longer acceptable.

Support: **3** talk(s)

> "Even though it takes 10 seconds, I'm okay if I know what's happening and be able to trust the agent's final output."
>
> — [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [11:15](https://www.youtube.com/watch?v=maTp79FD9gI&t=675s)

Supporting talks: [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)

### Irreversible or high-stakes actions require an explicit plan-and-approval gate before execution, with friction deliberately concentrated at those points rather than spread evenly.

Support: **4** talk(s)

> "some actions are usually irreversible and are dangerous actions. And in those cases, you need to present a plan."
>
> — [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [12:13](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=733s)

Supporting talks: [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)

### Delegation depends on reversibility: users only hand work to an agent when they are confident they can abort, roll back, and resume manual control, so stop controls, version history, and self-service paths must stay in the product.

Support: **4** talk(s)

> "if they don't have the confidence that, you know, if something goes wrong they can take them back control then then the users will completely lose trust."
>
> — [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [10:51](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=651s)

Supporting talks: [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)

### The human role in these systems shifts up the stack — from operator and author to supervisor, enabler, and designer of the environment the agent works in — rather than being eliminated.

Support: **5** talk(s)

> "So the search is automated. the human would just move up the stack not out of it."
>
> — [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [15:04](https://www.youtube.com/watch?v=iCj_ATyThvc&t=904s)

Supporting talks: [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Recursive Model Improvement](../talks/recursive-model-improvement.md), [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)

## Disagreements

### Should interaction design add friction and keep the human deliberating, or remove the human's burden so they can step back entirely?

| Position A | Position B |
|---|---|
| Deliberately engineer friction where stakes are high, reframe the human as investigator rather than validator, and treat automation bias as the primary risk to design against — more delegation without more scrutiny degrades both decisions and the training data.<br>*[Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)* | Human-in-the-loop is itself the defect: the goal is to win enough trust that control mechanisms become unnecessary, to strip the interface tax off the user entirely, and to optimize models for calibrated decision-making instead of human preference/approval.<br>*[The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)* |

*Why it matters: It determines whether you invest in approval gates, span-level review UIs, and label-quality instrumentation, or in autonomy, provenance, and calibration so the human never sees the decision. The two roadmaps produce incompatible products from the same model.*

### Is the chat host the destination surface for AI interaction, or is turn-taking chat itself the thing to be replaced?

| Position A | Position B |
|---|---|
| Chat is where users are and where distribution now lives; the fix is to enrich it — send brand-owned, interactive UI into the chat host, standardize the rendering contract, and treat the assistant as the new application platform.<br>*[MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)* | The single-slot, submit-and-wait protocol is the structural problem regardless of what it renders — chat's synchronicity blocks delegation, it has no concept of who holds the floor, and the interface must start participating (background agents, perception agents, voice-in/visuals-out) rather than taking turns.<br>*[The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Perception Agents](../talks/perception-agents.md), [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)* |

*Why it matters: One path invests in MCP Apps/component catalogs and accepts losing control of the user journey to the host; the other invests in asynchronous conveyor-belt architectures, screen perception, and sub-second multimodal loops, and treats the chat box as a legacy surface.*

### How much freedom should the model have to generate the interface it returns?

| Position A | Position B |
|---|---|
| Constrain hard: the model selects from a fixed component catalog supplied in its context, gated by client app version, and never invents a component — mobile clients cannot be patched, so an unknown content type is a crash that persists for weeks.<br>*[Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)* | Let the model author freely in its native medium — HTML/CSS/JS — because any custom DSL, JSON schema, or framework you teach it degrades output quality; the thinnest wrapper beat heavier alternatives with larger prompts and added skills.<br>*[HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)* |

*Why it matters: This sets the ceiling on what an agent can express and who absorbs the failure mode — a constrained catalog caps creativity but makes the client safe, while open generation unlocks charts, motion, and layout for free at the cost of an unbounded trust surface on the rendering client.*

### Should per-user customization be inferred from observed behavior, or expressed explicitly by the user?

| Position A | Position B |
|---|---|
| Infer it: capture skills automatically from product usage (a dedicated skill-creation interface won't work), and let each user run their own live divergence of a canonical stem rather than declaring segments in advance.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)* | Make steering explicit and inspectable: pointing at on-screen elements is a more precise, less lossy signal than inferred intent, memory must be visible and forgettable with the user having final say, and permissions need to be non-binary, revocable, and audit-logged.<br>*[Perception Agents](../talks/perception-agents.md), [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)* |

*Why it matters: Inference gives a frictionless product that quietly diverges per user and needs provenance tooling to stay debuggable; explicit steering gives auditability and user consent but reintroduces exactly the interface burden the other camp is trying to delete.*

## Practical Guidance

**Do:**

- Replace total latency with time-to-first-chunk as the primary UX metric for AI features, and stream partial output so users can assess and abort early
- Supply the model a fixed component catalog in context, gated by client app version (a 2.0 flight card offered only to 2.0+ clients), and reuse the app's existing production components rather than a distinct 'agentic' look
- Frame the AI signal in reviewer-facing copy as a preliminary alert requiring independent evidence and name the human as the final decision-maker — this alone moved Duolingo's rejection rate 21% with no model or UI change
- Split conflated CTAs: ask separately whether the model's perception was correct and whether action should be taken, so both labels stay honest
- Log the human's subsequent manual edit, not just the accept/reject decision — a yes/no with no edit capture is a false signal in your dataset
- Anchor LLM writing feedback inline to specific spans instead of returning a block that rewrites the user's passage
- Pause the agent whenever it is about to make an assumption, and present a plan for approval before irreversible or dangerous actions (with a setting to disable for repeated flows)
- Trace every value the agent produced back to its source in a format users can read — this is where customer complaints get resolved
- Keep a prominent, always-available stop control and user-facing version history; keep self-service features in the product so users can take the wheel back
- Give agents HTML/CSS/JS rather than a custom DSL or JSON schema, and write skills that teach taste and domain craft rather than framework syntax
- Define success metrics and the data you need before building the system, instead of asking afterward how to evaluate the model
- For real-time voice: target ~1s for visual response, fire inference every 1-2 seconds while the user is still speaking, use a Haiku-class model on a latency-prioritizing platform, and keep the first ~90% of context stable for prefix caching
- Track weekly active sessions rising while weekly active users declines as the success signal for delegation products
- Mark AI-generated content explicitly as AI-generated, and give users examples, templates, and guided workflows instead of an empty prompt
- Show a rough time and cost estimate before the user approves an AI action, and make agent permissions non-binary, revocable, and visible in history

**Avoid:**

- Traditional loading spinners for AI features — users have left the forgiving phase and expect to see what is happening
- Sending unknown content types to mobile clients you cannot patch; absorb model output in a BFF and keep the client dumb and safe
- Coding-agent patterns that produce one giant diff or a per-file approval prompt — both reduce the developer to a rubber stamp and yield low-information accept/reject data
- Treating citations as the trust mechanism; they shift verification burden onto the user, which is worst in healthcare, legal, and tax
- Teaching the model a custom DSL or JSON structure — it degrades output quality even with many examples
- Canvas-based agent tooling (Figma MCPs, PowerPoint CLIs, screenshot-and-replace loops) that forces agents to imitate human hand-and-eye interaction
- A blank 'ask AI' text box, which assumes AI literacy users do not have
- Thumbs up/down as your feedback mechanism — insufficient nuance to drive improvement
- Adding more human oversight as the fix for AI quality problems; sometimes the fix is engineering the interaction itself
- Framing AI as magic (the sparkle icon) or marketing your model as more trustworthy or hallucination-free than competitors
- Waiting for a second of silence before triggering inference in voice interfaces — the latency budget is already blown
- Opening a new PR from an agent loop while a previous PR from that loop is still unreviewed
- A dedicated user-facing skill-creation interface for capturing per-user conventions
- Building UI for AI with AI — it can only remix patterns that already exist, and AI interface patterns don't exist yet

## Notable Outliers

- Expert reviewers consistently scoring above 90% on accuracy calibration still accepted 50% of entirely fabricated AI flags — a coin-flip rate indicating reviewer skill offers no protection against automation bias. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [6:15](https://www.youtube.com/watch?v=CDqzWpwkSls&t=375s))
- A guideline copy change alone — no model change, no UI change — produced a 21% increase in rejection rates. ([Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md), [7:41](https://www.youtube.com/watch?v=CDqzWpwkSls&t=461s))
- For agentic products the target is weekly active users going down while weekly active sessions go up (though not to zero) — inverting the standard engagement metric. ([Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [13:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=816s))
- Prompt engineering is not a power-user skill but a packaging protocol — the same mastery a punch card operator had in assembling a deck so the job wouldn't fail — and human proficiency at it is evidence of a design failure. ([The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md), [7:56](https://www.youtube.com/watch?v=hVJOnuhFmTA&t=476s))
- Of several candidate agent-authoring formats, the thinnest wrapper won: essentially just HTML with a few data attributes as metadata, beating alternatives with larger system prompts, more context, and added skills. ([HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s))
- Pointing at on-screen elements is a more precise and less lossy input signal than natural-language description, eliminating the clarification back-and-forth entirely. ([Perception Agents](../talks/perception-agents.md), [12:55](https://www.youtube.com/watch?v=2JX6JYyQG4Y&t=775s))
- The world spends roughly 34,000 human years per day making slide decks, most of it formatting rather than thinking; a 10-hour deck should take about 25 minutes. ([HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [0:53](https://www.youtube.com/watch?v=JRTAtZ5iBkU&t=53s))
- Overconfidence and overpromising in assistants are by construction, not a correctable defect — the RLHF reward model rewards apparent confidence, so no matter how wrong the model is, it will look right. ([What's Next After RLHF?](../talks/whats-next-after-rlhf.md), [6:44](https://www.youtube.com/watch?v=cJ0EOzey--o&t=404s))

## All Talks

- [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)
- [Agent Output Is Not UX: Rendering Layer Your LLM Pipeline Is Missing](../talks/agent-output-is-not-ux-rendering-layer-your-llm-pipeline-is-missing.md)
- [Build AI Systems for Discernment, Not Approval](../talks/build-ai-systems-for-discernment-not-approval.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [How Autoresearch is changing ML research](../talks/how-autoresearch-is-changing-ml-research.md)
- [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- [Loop Engineering from First Principles](../talks/loop-engineering-from-first-principles.md)
- [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)
- [Morgan Stanley's ALPHALAB: Multi-Agent Research Across Optimization Domains](../talks/morgan-stanleys-alphalab-multi-agent-research-across-optimization-domains.md)
- [Perception Agents](../talks/perception-agents.md)
- [Recursive Model Improvement](../talks/recursive-model-improvement.md)
- [Stop AI Agent Hallucinations: 5 Techniques + Production Patterns](../talks/stop-ai-agent-hallucinations-5-techniques-production-patterns.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)
- [The Prompt Is Still a Punch Card](../talks/the-prompt-is-still-a-punch-card.md)
- [The UX of AI: Making AI-Powered Apps Your Users Don't Hate](../talks/the-ux-of-ai-making-ai-powered-apps-your-users-dont-hate.md)
- [Voice In, Visuals Out: The Agony and the Ecstasy](../talks/voice-in-visuals-out-the-agony-and-the-ecstasy.md)
- [What's Next After RLHF?](../talks/whats-next-after-rlhf.md)

## Speakers

- [Allen Pike](../speakers/allen-pike.md)
- [Angel Ortmann Lee](../speakers/angel-ortmann-lee.md)
- [Antje Barth](../speakers/antje-barth.md)
- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Bala Ramdoss](../speakers/bala-ramdoss.md)
- [Brendan Rappazzo](../speakers/brendan-rappazzo.md)
- [Diogo Almeida](../speakers/diogo-almeida.md)
- [Elizabeth Fuentes Leone](../speakers/elizabeth-fuentes-leone.md)
- [Ido Salomon](../speakers/ido-salomon.md)
- [James Russo](../speakers/james-russo.md)
- [Kathryn Grayson Nanz](../speakers/kathryn-grayson-nanz.md)
- [Kyle Mistele](../speakers/kyle-mistele.md)
- [Lee Robinson](../speakers/lee-robinson.md)
- [Liad Yosef](../speakers/liad-yosef.md)
- [Sanja Grbic](../speakers/sanja-grbic.md)
- [Ted Johnson](../speakers/ted-johnson.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Zubin Aysola](../speakers/zubin-aysola.md)

