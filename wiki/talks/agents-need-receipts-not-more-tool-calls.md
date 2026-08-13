---
title: "Agents Need Receipts, Not More Tool Calls"
type: "talk"
slug: "agents-need-receipts-not-more-tool-calls"
org: "Alithea Bio"
video_id: "Fu45geO3zX8"
duration_sec: 1176
word_count: 2245
speakers: ["Armanas Povilionis"]
---

# Agents Need Receipts, Not More Tool Calls

**Speakers:** [Armanas Povilionis](../speakers/armanas-povilionis.md)

**Org:** Alithea Bio

**Duration:** 19m 36s

[Watch on YouTube](https://www.youtube.com/watch?v=Fu45geO3zX8)

## Summary

Armanas Povilionis of Alithea Bio argues that giving agents more or better tools only improves local work, and that the real bottleneck for scientific automation is cross-organizational collaboration — data, algorithms, and compute siloed across institutions. His analogy: a cook with better knives versus an executive chef who sources suppliers, negotiates terms, and keeps records. The proposed answer is Froglet, an open-source protocol where agents discover services, transact with external providers, and receive cryptographically signed, verifiable receipts of what happened. He also forecasts that mature agent automation means giving agents budgets, not just tools, so they can pay for data and compute across organizational boundaries. The talk is roughly half live demo (remote trial node, local Docker install, Claude driving it over MCP), so watch it if you care about agent-to-agent commerce, provenance, or federated scientific data — skip it if you want depth on the cryptography or economics, which are only sketched.

## Key Points

- Adding more tools to an agent only optimizes local work, whereas scientific research is inherently collaborative and requires aligning a whole supply chain of providers, data, and compute across organizations.
- The missing primitive is a verifiable chain of receipts that proves every step, so results can be trusted and workflows repeated and shared at scale.
- Povilionis predicts that as agent workflows mature, organizations will give agents budgets rather than just tools, letting them discover services, request data, negotiate terms, and pay across organizational boundaries.
- Froglet is positioned as an integration layer rather than a replacement: it plugs into different payment rails, agent harnesses, execution environments, and transport protocols, and does not require every node to run the same stack — only the same interface.
- Every Froglet node is the same software and only differs by role — provider, requester, or marketplace — and a single node can hold multiple roles simultaneously, verified in the demo by two endpoints sharing one node ID.
- Each node generates a key pair at creation and signs artifacts throughout execution, forming a chain that is valid only if no data point has been tampered with.
- Discovery goes through a marketplace, but once a requester picks a service, quote, deal, execution, and receipt all happen directly between the two parties with no third party in the middle.
- He frames the cost comparison as bespoke closed-source data-sharing projects taking years and millions of dollars, versus a Froglet setup costing a few thousand tokens and minutes.
- Packaging payment, execution, negotiation, and receipts behind the protocol is presented as a context-management win: the agent sees only the services it needs instead of having every underlying protocol stuffed into its LLM context.

## Notable Quotes

> "from my experience, adding more tools to agents will not suffice"
>
> — [0:00](https://www.youtube.com/watch?v=Fu45geO3zX8&t=0s) &middot; *the talk's thesis in one line, stated as a claim against the prevailing tool-count approach*

> "science and especially lives in in specially in life sciences is inherently collaborative process. And in order to enable agents to collaborate, we need a way to have a verifiable chain of receipts."
>
> — [1:01](https://www.youtube.com/watch?v=Fu45geO3zX8&t=61s) &middot; *states the premise and the proposed primitive together*

> "We need a solution which can provide these receipts proving every step, ensuring that every result can be trusted, and enabling repeatability as well as collaboration at scale."
>
> — [1:01](https://www.youtube.com/watch?v=Fu45geO3zX8&t=61s) &middot; *the three requirements the protocol is designed against*

> "scientific work is not cooking alone in your own kitchen. It is closer to running a Michelin-star restaurant."
>
> — [2:06](https://www.youtube.com/watch?v=Fu45geO3zX8&t=126s) &middot; *the central analogy that carries the argument*

> "You cannot bring everything into one kitchen. The challenge isn't local. It's not local tools. The challenge is aligning the entire supply chain that it's repeatable and consistent."
>
> — [2:06](https://www.youtube.com/watch?v=Fu45geO3zX8&t=126s) &middot; *names the tradeoff between local tool quality and cross-org coordination*

> "our vision is that whenever AI agent workflow automation matures, organizations will give to the agents not only tools, they will give them budgets"
>
> — [3:23](https://www.youtube.com/watch?v=Fu45geO3zX8&t=203s) &middot; *the talk's most forward-looking and contestable prediction*

> "At that point, an agent is no longer just a cook with a better knife. It starts to act like a chef."
>
> — [3:23](https://www.youtube.com/watch?v=Fu45geO3zX8&t=203s) &middot; *crisp framing of the capability shift budgets would unlock*

> "An open-source protocol for agents to discover, transact with, and receive verifiable receipt from external data uh data and service providers."
>
> — [4:34](https://www.youtube.com/watch?v=Fu45geO3zX8&t=274s) &middot; *the product definition in the speaker's own words*

> "And it doesn't require that every node in the network uses the same software stack. That's the beauty. We are not forcing everyone to use the same to to work the same way."
>
> — [4:34](https://www.youtube.com/watch?v=Fu45geO3zX8&t=274s) &middot; *states the interoperability design constraint*

> "closed source and the collaboration often turns into a bespoke project, enterprise project that can take years and cost millions before any reusable workflow exists"
>
> — [5:37](https://www.youtube.com/watch?v=Fu45geO3zX8&t=337s) &middot; *the cost baseline the whole pitch is measured against*

> "an agent can discover it, understand the terms, request the work, and receive a verifiable receipt."
>
> — [5:37](https://www.youtube.com/watch?v=Fu45geO3zX8&t=337s) &middot; *the four-step loop the protocol implements*

> "That setup costs few thousand tokens and takes minutes."
>
> — [6:41](https://www.youtube.com/watch?v=Fu45geO3zX8&t=401s) &middot; *the concrete number claimed against years-and-millions*

> "It It helps to find, to trust, to pay, and to prove that the work has happened. That is it. We're not trying to replace any of functionalities of other tools or protocols."
>
> — [7:41](https://www.youtube.com/watch?v=Fu45geO3zX8&t=461s) &middot; *scopes the protocol explicitly against replacing MCP or similar*

> "everything is being signed in a chain, and the chain is only valid if all data points are not tampered with"
>
> — [7:41](https://www.youtube.com/watch?v=Fu45geO3zX8&t=461s) &middot; *the actual verification mechanism behind 'receipts'*

> "once the requester identifies the service that they want to work with, the communication is direct. There is no uh third party. And everything from quote to deal to execution and receipt happens in one interaction."
>
> — [8:40](https://www.youtube.com/watch?v=Fu45geO3zX8&t=520s) &middot; *names the disintermediation property of the marketplace design*

> "The primary interface for humans should be an LLM. An LLM should drive usage of Froglet, whether you are a provider or a requester."
>
> — [9:45](https://www.youtube.com/watch?v=Fu45geO3zX8&t=585s) &middot; *an opinionated UX position others would contest*

> "I actually look at the node ID, I see that this is one and the same ID. And that means that each each Froglet can assume different roles, and at the same time can assume multiple roles."
>
> — [13:44](https://www.youtube.com/watch?v=Fu45geO3zX8&t=824s) &middot; *the demo moment proving the single-node, multi-role architecture claim*

> "it packages a lot of um underlying protocols and underlying tools where now you're not shoving everything into a uh LLM context. It just has a services that it needs to interact."
>
> — [17:48](https://www.youtube.com/watch?v=Fu45geO3zX8&t=1068s) &middot; *frames the protocol as a context-engineering benefit, not just a commerce one*

> "it allows to have a verifiable receipt of receipts of what has happened. And I think that actually enables a collaborative science."
>
> — [18:46](https://www.youtube.com/watch?v=Fu45geO3zX8&t=1126s) &middot; *closing statement of the causal claim from receipts to collaborative science*

## Positions

- Adding more or better tools to agents is insufficient for automating scientific research, because the binding constraint is cross-organizational coordination rather than local capability. ([0:00](https://www.youtube.com/watch?v=Fu45geO3zX8&t=0s), confidence: stated)
- Agent collaboration requires a verifiable chain of receipts proving every step, without which results cannot be trusted or repeated. ([1:01](https://www.youtube.com/watch?v=Fu45geO3zX8&t=61s), confidence: stated)
- As agent automation matures, organizations will give agents budgets to discover services, negotiate terms, and pay for work across organizational boundaries — not just token allocations. ([3:23](https://www.youtube.com/watch?v=Fu45geO3zX8&t=203s), confidence: stated)
- A shared interface, not a shared software stack, is sufficient for a cross-organizational agent network. ([4:34](https://www.youtube.com/watch?v=Fu45geO3zX8&t=274s), confidence: stated)
- Closed-source data collaboration typically takes years and costs millions before producing a reusable workflow, whereas exposing a resource on Froglet costs a few thousand tokens and takes minutes. ([5:37](https://www.youtube.com/watch?v=Fu45geO3zX8&t=337s), confidence: stated)
- Froglet is complementary rather than competitive with existing agent tools and protocols; it only adds find, trust, pay, and prove. ([7:41](https://www.youtube.com/watch?v=Fu45geO3zX8&t=461s), confidence: stated)
- After discovery via a marketplace, transactions should be peer-to-peer with no third party mediating quote, deal, execution, or receipt. ([8:40](https://www.youtube.com/watch?v=Fu45geO3zX8&t=520s), confidence: stated)
- The primary human interface to this kind of protocol should be an LLM rather than a GUI or direct API use. ([9:45](https://www.youtube.com/watch?v=Fu45geO3zX8&t=585s), confidence: stated)
- Abstracting payment, negotiation, and execution behind a protocol reduces LLM context consumption compared to exposing the underlying protocols directly to the agent. ([17:48](https://www.youtube.com/watch?v=Fu45geO3zX8&t=1068s), confidence: stated)
- Verifiable receipts are the enabling precondition for collaborative, perpetually automated science. ([18:46](https://www.youtube.com/watch?v=Fu45geO3zX8&t=1126s), confidence: implied)

## Concepts

- [agent interoperability protocols](../concepts/agent-interoperability-protocols.md)
- [agentic science](../concepts/agentic-science.md)
- [audit trails](../concepts/audit-trails.md)
- [context window management](../concepts/context-window-management.md)
- [data governance and privacy](../concepts/data-governance-and-privacy.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [mcp server design](../concepts/mcp-server-design.md)
- [skill marketplaces](../concepts/skill-marketplaces.md)

