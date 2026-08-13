---
title: "model context protocol"
type: "concept"
slug: "model-context-protocol"
tier: "core"
maturity: "consolidating"
talk_count: 16
speaker_count: 17
---

# model context protocol

**Maturity: CONSOLIDATING** — Consolidating — converging practice, some open edges

*Core concept* &middot; discussed across **16** talk(s) by **17** speaker(s)

**Definition:** MCP as a protocol and ecosystem for connecting models to tools, resources, and applications — its primitives, adoption, and role as a standard.

*Also referred to as: mcp servers, mcp tool integration, mcp and agent protocols, mcp apps, mcp tasks, mcp client implementation, web mcp*

## State of Practice

MCP's tool layer is settled and universally deployed — it is the de facto way to get an organization's tools and data into an agent someone else built (Gates Foundation exposes a four-system property graph through one MCP semantic layer; Automattic exposes decades of internal documentation; Pinterest replaced raw log ingestion with two MCP tools; Docling ships one so agents don't need to know its CLI arguments). What is unsettled is everything above that layer. The dominant technical complaint is context cost: tool definitions are charged upfront on every session, ~100k tokens for 15 connected servers, which collides with the widely cited 25-40% context-degradation threshold and has pushed a chunk of the field toward skills-style progressive disclosure (~100 tokens at listing, ~5k on activation) with MCP reserved for what it uniquely provides — auth, process isolation, restricted-environment data access, and compute the agent's laptop lacks. Two extensions dominated the conference: MCP Apps, which became the official UI extension in January 2026, now underpins ChatGPT apps and Claude's generative 'imagine' feature, and is paired with self-serve stores at ChatGPT, Claude, and Cursor plus dynamic registry discovery (Claude only, so far); and MCP tasks for async work, which no client has implemented — V1's stateful, unfilterable tasks/list and its server-elicits-client-over-a-long-lived-connection pattern were judged too involved, and V2's stateless redesign still won't scale to millions of concurrent tasks under per-client polling. Practitioners report that off-the-shelf servers need forking for production enterprise use, and that the biggest non-technical blocker to shipping a server at all was brand erasure — being reduced to a textual database — which is precisely what MCP Apps targets.

## Consensus

### MCP has succeeded as a tool and data distribution mechanism — the way to reach agents you don't control — and organizations should ship a server rather than build another chat UI.

Support: **6** talk(s)

> "So, MCP has become a de facto tool distribution mechanism for agents. So, if I need to get my company's tools into that other agent, then MCP's a good way to do that. It has not proven to be great at providing other value yet."
>
> — [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [8:13](https://www.youtube.com/watch?v=spNAUEgq_A8&t=493s)

Supporting talks: [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md), [Structuring the Unstructured](../talks/structuring-the-unstructured.md), [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)

### Connecting one agent to a large inventory of MCP servers is a measurable cost, not a free capability upgrade: tool definitions consume context on every turn and degrade answer quality, so agents should carry a small, curated tool set.

Support: **4** talk(s)

> "If it's connected to 15 MCP server, I'm pretty sure it's consuming over 100,000 tokens per session just in tool definitions itself."
>
> — [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s)

Supporting talks: [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)

### Plain textual/JSON MCP tool output is a real product limitation — factually correct responses are often unusable for the end user — which is what MCP Apps' host-rendered UI exists to fix.

Support: **3** talk(s)

> "And actually, this is the main blocker from companies to build an MCP server. They don't want to be reduced to a textual database. They don't want to lose their brand identity in the process."
>
> — [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [0:55](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=55s)

Supporting talks: [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

### MCP is still immature above the tools layer — the async task spec, security model, and off-the-shelf server quality all require significant work before production use.

Support: **3** talk(s)

> "I really think MCP is still maturing. There's a lot uh a long road ahead for it, especially with some of the security stuff it's doing. I would keep an eye out for MCP"
>
> — [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [13:36](https://www.youtube.com/watch?v=IddXPepIAS4&t=816s)

Supporting talks: [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Disagreements

### Should agent capability be delivered primarily through MCP servers, or through skills with MCP reserved for a narrow set of cases?

| Position A | Position B |
|---|---|
| Default to skills/local instruction files with progressive disclosure — roughly 10x less context overhead — and call MCP only where it is structurally required: authentication, process isolation, restricted-environment data access, and compute the agent's own machine cannot provide. MCP loaded broadly into one agent's context behaves like inheritance and breaks down.<br>*[Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)* | MCP is the integration layer you build the system on: the semantic/graph interface enterprises expose to Claude and ChatGPT, the memory backend, the queryable runtime handle, the ticket/requirements ingress into a spec flow — still maturing, but the durable substrate rather than a fallback.<br>*[Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md), [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md), [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)* |

*Why it matters: It decides where a vendor invests: a versioned, tested skills library shipped with the product, or a hosted server with auth, schema, and store listings. It also sets the context budget an agent has left for actual work before the first user turn.*

### Will the long tail of the web become agent-accessible by publishing MCP servers, or must agents keep operating on rendered pixels?

| Position A | Position B |
|---|---|
| No. Roughly 200 million active websites — county records offices, FOIA portals, organizations still faxing each other — will never expose MCP servers or APIs; the content on screen is computed and rendered, not present in HTML, so pixels remain the source of truth and per-site scaffolds are the bitter-lesson mistake.<br>*[Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)* | Yes, and it is already starting: sites can publish MCP servers inline in the page for agents to use without pre-installation, and services will fragment into composable MCP App UI chunks rendered inside personal assistants, with stores and registry discovery as the distribution path.<br>*[Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)* |

*Why it matters: If MCP becomes the web's agent surface, the engineering investment is server-side and per-brand; if it does not, the investment is in browser infrastructure, accessibility-tree extraction, and cheap fast computer-use models. The two roadmaps share almost no code.*

### Does agent value come from breadth of connected MCP servers under one general host, or from many narrow agents each carrying a minimal tool set?

| Position A | Position B |
|---|---|
| One general host client is the destination — ChatGPT/Claude/Cursor stores, dynamic registry discovery, write once and run everywhere; the assistant composes many servers' capabilities and displaces conventional dashboards as the primary software interface.<br>*[MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)* | Breadth actively degrades the agent. Build small domain-specific agents with one or two tools each, communicating in natural language, each with its own sandboxed filesystem and execution — this yields 80%+ token efficiency and makes capability limits, not permission dialogs, the security boundary.<br>*[The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md), [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)* |

*Why it matters: It determines whether you optimize for store discoverability inside someone else's assistant or for an internally orchestrated fleet, and whether the MCP registry becomes the distribution chokepoint for software.*

## Practical Guidance

**Do:**

- Budget MCP tool definitions as context spend: keep baseline system prompt plus tool definitions under 40% of the window before any user turn, knowing ~15 servers costs 100k+ tokens per session
- Give each agent one or two tools and a single job rather than the full connected inventory; measure the agent against the baseline model to confirm the harness is adding value
- Design MCP tools to return pre-compressed, purpose-built output — top-K truncated exceptions plus a drill-down tool instead of raw logs, rendered images instead of raw time series (fixed input tokens regardless of job duration)
- Put a semantic layer or property graph behind the MCP interface so the agent can discover and traverse schema at query time, instead of exposing raw systems of record
- Split MCP Apps tool output between what the widget renders and what the model sees, so privacy-sensitive data can be displayed to the user without being sent to the LLM provider
- Return alternate non-UI output alongside any MCP Apps widget, so clients without MCP Apps support and the model itself are not starved of information
- Submit to the ChatGPT, Claude, and Cursor stores even if your server returns no UI — all three have self-serve submission, and Claude already performs dynamic MCP registry discovery when a task has no matching tool
- Use the official mcp-apps SDK rather than alternatives, since spec changes land there first
- Expect to fork off-the-shelf MCP servers for enterprise production — schema updates, state passing such as conversation and message IDs
- Persist MCP task IDs on the client; the spec only says 'should', but an unpersisted task ID is permanently unrecoverable

**Avoid:**

- Don't connect one general-purpose agent to dozens of MCP servers and skills at once; research and speaker experience both show substantial measured degradation
- Don't expose destructive memory operations (a 'forget' tool) as callable MCP tools — the agent is one call away from wiping its own memory
- Don't pipe raw tool output — full page HTML, complete logs, unsampled time series — through MCP into the primary context; it crowds out the main thread and costs tokens twice
- Don't build on MCP tasks V1: tasks/list makes the protocol stateful and has no filter (unusable at a million tasks), and the long-lived tasks/result connection with server-to-client elicitation is why zero clients implemented it
- Don't assume V2 solves scale — per-client polling against a million running tasks still doesn't scale; wait for the notifications protocol
- Don't reduce your product to a textual database when exposing it over MCP; loss of brand identity is the stated primary reason companies have not shipped servers at all
- Don't write per-site scaffolds for the long tail of the web expecting MCP-style structure to appear there
- Don't build another chat UI on top of your enterprise data — the interface is not defensible; the modeled tacit knowledge behind the MCP endpoint is

## Notable Outliers

- The premise that the long tail of the web will publish MCP servers is delusional — county records offices publishing JPEGs of PDFs and organizations still using fax will never ship one. ([Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [7:04](https://www.youtube.com/watch?v=Ki980nV0__0&t=424s))
- Zero MCP clients support MCP tasks, and that is the correct engineering decision — the November spec was marked experimental and V2 changes it substantially. ([MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md), [0:01](https://www.youtube.com/watch?v=s4r6nk5WsZw&t=1s))
- Whether a product ships an MCP server has become a primary purchasing criterion — checked before other evaluation. ([MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md), [26:31](https://www.youtube.com/watch?v=sAOBXCDiDOs&t=1591s))
- Websites can now publish MCP servers inline within the page, so an agent can use them without pre-installing anything. ([Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [11:00](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=660s))
- Skills impose roughly 10x less context overhead than the equivalent MCP setup, and a skills folder can replace MCP for most use cases given a good base reasoning model. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [13:42](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=822s))
- MCP Apps addresses roughly 170 times the total addressable market of the Apple App Store at its launch, making it a distribution channel rather than a UI feature. ([MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [17:26](https://www.youtube.com/watch?v=-jY2T2PiJBE&t=1046s))
- Exposing memory through MCP tools puts the agent one call away from invoking forget and wiping its own memory. ([CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md), [6:23](https://www.youtube.com/watch?v=Q0VkgCyNVUg&t=383s))

## All Talks

- [500 people vibe-coded for 30 days. I was one of them.](../talks/500-people-vibe-coded-for-30-days-i-was-one-of-them.md)
- [Anthropic's CCA Exam as a Field-Guide for Agentic Engineering](../talks/anthropics-cca-exam-as-a-field-guide-for-agentic-engineering.md)
- [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)
- [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)
- [CrabRAG: Why Automated Assistants Need Graph Memory, Not More Tokens](../talks/crabrag-why-automated-assistants-need-graph-memory-not-more-tokens.md)
- [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)
- [MCP Apps: Primitives, discovery, and the Future of Software](../talks/mcp-apps-primitives-discovery-and-the-future-of-software.md)
- [MCP Tasks (async): Why Aren't Any Agents Supporting Them?](../talks/mcp-tasks-async-why-arent-any-agents-supporting-them.md)
- [Medic for Apache Spark - First Aid for Failing Jobs](../talks/medic-for-apache-spark-first-aid-for-failing-jobs.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [Structuring the Unstructured](../talks/structuring-the-unstructured.md)
- [The Future Is Domain-Specific Agents](../talks/the-future-is-domain-specific-agents.md)
- [Using Spec-Driven Development for Production Workflows](../talks/using-spec-driven-development-for-production-workflows.md)
- [Your Agents Need a Save Button](../talks/your-agents-need-a-save-button.md)
- [Your Finance Agent's Bottleneck Is You](../talks/your-finance-agents-bottleneck-is-you.md)
- [Your Moat Is Your Data Model](../talks/your-moat-is-your-data-model.md)

## Speakers

- [Cedric Clyburn](../speakers/cedric-clyburn.md)
- [Cornelia Davis](../speakers/cornelia-davis.md)
- [Dhruv Batra](../speakers/dhruv-batra.md)
- [Drasko Profirovic](../speakers/drasko-profirovic.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [Erik Hanchett](../speakers/erik-hanchett.md)
- [Frank Coyle](../speakers/frank-coyle.md)
- [Ido Salomon](../speakers/ido-salomon.md)
- [Kunal Lanjewar](../speakers/kunal-lanjewar.md)
- [Liad Yosef](../speakers/liad-yosef.md)
- [Mike Phipps](../speakers/mike-phipps.md)
- [Paul Klein IV](../speakers/paul-klein-iv.md)
- [Pietro Zullo](../speakers/pietro-zullo.md)
- [Ramana Siddanth Emani](../speakers/ramana-siddanth-emani.md)
- [Sanja Grbic](../speakers/sanja-grbic.md)
- [Stephen Chin](../speakers/stephen-chin.md)
- [Vlad Luzin](../speakers/vlad-luzin.md)

