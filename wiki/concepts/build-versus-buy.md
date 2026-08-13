---
title: "build versus buy"
type: "concept"
slug: "build-versus-buy"
tier: "supporting"
maturity: "contested"
talk_count: 9
speaker_count: 9
---

# build versus buy

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **9** talk(s) by **9** speaker(s)

**Definition:** Deciding whether to build an AI capability in-house or adopt a vendor's, and when a thin wrapper stops being enough.

*Also referred to as: build vs buy decisions, build versus rent decisioning, build-vs-buy tipping point, thin wrappers vs custom dsls, productization of services, custom-to-product funnel, product breadth vs depth, switching costs and moats*

## State of Practice

The build/buy line moved down the stack this year, and it moved because coding agents made the build side cheap. Speakers repeatedly reported that things that were formerly vendor purchases — a database platform, a scraping pipeline, a PR-triage service, a custom integration — are now one to two days, one week and $5,000, or a single markdown file. Survey data puts the current equilibrium concretely: inference and model serving are the clear buy market, while layers close to product logic stay in-house (61% build their own prompt management), and fine-tuning is a 'not yet' layer most teams skip entirely. The forcing function is metered pricing, not capability — 40% say cost regularly shapes how ambitiously they use AI, and both the inference and web-context talks argued the rent-to-own break-even arrives far sooner than teams assume (just over 15,000 entities/queries for context; post-PMF for inference). On the vendor side of the same question, the recurring rule is that per-customer bespoke work must be architected as generalizable platform primitives or the maintenance P&L eats the business — an FDE function without a platform underneath is just a dev shop. The genuinely unsettled part is where the thin wrapper stops being enough: one camp argues the winning layer is the thinnest possible skin over the model's native abilities, the other that durable value requires an owned platform underneath.

## Consensus

### Coding agents have moved the build/buy threshold down a tier: capabilities that used to be obvious vendor purchases are now days-to-a-week of in-house work, at lower-than-vendor reliability but acceptable quality.

Support: **5** talk(s)

> "I'm not saying you can build something as reliable as RDS. I'm saying that you can build a database platform into your product in a day or two of work with enough prompting and enough effort."
>
> — [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [14:15](https://www.youtube.com/watch?v=xUnRQ9vLXxo&t=855s)

Supporting talks: [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)

### Bespoke per-customer builds must be converted into generalizable platform primitives; shipping one-off solutions without that abstraction layer is a business-model failure, not just technical debt.

Support: **3** talk(s)

> "If you were to implement an FTE function where each FTE is building entirely from scratch, my friends, you do not have an FTE function. You have a dev shop."
>
> — [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [8:12](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=492s)

Supporting talks: [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)

### When wrapping a model, the thinnest layer over what the model already knows outperforms heavier custom scaffolding — custom DSLs, framework abstractions, and bespoke orchestration systems degrade output rather than improve it.

Support: **3** talk(s)

> "but to our surprise, the thinnest wrapper ultimately won, which is essentially just HTML at the end of the day with a few data attributes as metadata"
>
> — [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [5:15](https://www.youtube.com/watch?v=Cz4v1WHVyZc&t=315s)

Supporting talks: [HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)

### Metered, per-call vendor pricing is now the dominant forcing function in build-vs-buy decisions — cost is treated as a production engineering constraint that shapes architecture, not a budget line item.

Support: **3** talk(s)

> "40% of respondents say that cost regularly shapes how ambitiously they use AI and another 36% say that it sometimes does."
>
> — ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [8:16](https://www.youtube.com/watch?v=RGe6EjucbzI&t=496s)

Supporting talks: [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)

## Disagreements

### Should teams own their inference and context infrastructure, or is renting it from vendors the correct steady state?

| Position A | Position B |
|---|---|
| Renting is a trap past the validation stage: prepaid credit pools cause overspend, endpoints can't see workload shape so waste is structural, and rented models fail audit, reproducibility, and rate-limit control requirements. Post-PMF startups and enterprises should buy hardware and own the pipeline; for web context, self-built scraping breaks even at just over 15,000 entities against ~1 week and ~$5,000 of setup, and owned context compounds while rented decays.<br>*[Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)* | Practitioners overwhelmingly buy at this layer and it is working: inference and model serving is the clear buy market in the survey, with in-house effort concentrated on prompts, RAG, and eval — the layers closest to product logic. Vendor context services also stay correct for ad hoc, changing, or one-time questions where a pipeline would never amortize.<br>*["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)* |

*Why it matters: The answer determines whether AI infrastructure is a capex decision (DGX boxes, scraper fleets, an ops team) or a vendor-management decision, and whether audit/reproducibility requirements are designed for up front or discovered when a third-party dependency gets redlined.*

### Where does durable value live in an agentic product — in the thinnest possible layer over the model, or in an owned platform of primitives underneath it?

| Position A | Position B |
|---|---|
| Thin. Let the model speak its native tongue (HTML/CSS/JS over a custom DSL), teach taste rather than framework syntax, replace MCP servers with a progressively-disclosed skills folder, and skip custom orchestration entirely because the model will spawn and verify its own subagents if asked. Entire services collapse into markdown files.<br>*[HTML Is All Agents Need](../talks/html-is-all-agents-need.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)* | Thick. Without an underlying platform of shared primitives you have a dev shop whose maintenance costs destroy the P&L, and an agent assembled from customer-specific prompts and patches is a brittle black box that's bad for both vendor and customer. The prerequisite question before starting is 'do I have a platform, or am I willing to invest in building one.'<br>*[Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)* |

*Why it matters: It decides whether engineering headcount goes into product primitives and configuration surfaces or into prompt/skill craft on top of a commodity harness — and whether the thing you sell survives the next model release or gets absorbed by it.*

### How should a vendor make an enterprise customer successful with a customizable agentic platform — by embedding engineers, or by making the product teachable enough that customers and their agents do it themselves?

| Position A | Position B |
|---|---|
| Embed engineers. Nearly every platform is now agentic and therefore customizable, which puts most vendors in the technical-product/non-technical-buyer quadrant; leaving success to the customer's own implementation ability makes it hard to sell upmarket or expand. Staff multiple FDEs per account, hire at the product-engineering bar, and sell an outcome rather than software or hours.<br>*[Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)* | Ship the right shape and let users build. Architect for extensibility and missing vertical features stop being your problem — Slack won as an agent platform on shape, not product quality. The enterprise moat is shifting from friction to fluency and teachability: how fast a new agent harness can absorb your platform's operational knowledge, delivered as skills rather than deployed humans.<br>*[Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md), [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)* |

*Why it matters: One path builds a services-heavy cost structure with a high ACV ceiling; the other bets that customers' own coding agents will close the last mile, and misjudging which regime you're in either burns margin on headcount or loses deals to competitors who show up with engineers.*

## Practical Guidance

**Do:**

- Rent inference while pre-PMF and still validating demand; move to owned infrastructure once you're post-PMF or once audit, reproducibility, or rate-limit control becomes a requirement
- Compute the rent-vs-build break-even explicitly before signing a context/data API — one worked example put it at just over 15,000 entities or queries against ~1 week and ~$5,000 of setup
- Model agentic data cost by query frequency rather than record volume, since every repeated query costs the same as the first even when nothing changed
- Architect each customer-specific solution for the next four customers before they ask, and upstream anything an engineer had to do manually as a missing product capability
- Stop hand-building custom integrations and invest in a self-serve path — Decagon drew that line at roughly the 25th one
- Before standing up an FDE function, check both gates: are you selling a technical product to a non-technical buyer, and do you have (or will you fund) a platform of shared primitives
- Keep baseline system prompt plus tool definitions under 40% of the context window before the first user turn; prefer skills' progressive disclosure to connecting 15 MCP servers (~100K tokens of tool definitions alone)
- Keep MCP specifically for authentication, process isolation, restricted-environment data access, and compute the agent's local machine can't provide
- Emit output in the model's native formats (HTML/CSS/JS) and use skills to teach taste and domain craft, not framework syntax
- Write skills by hand and treat them as software artifacts — versioned, evaluated, tested
- Staff more than one FDE per customer engagement to avoid a single point of failure
- Get success metrics and channels agreed in writing during the earliest deal conversations, and deliberately narrow initial scope to prove value fast

**Avoid:**

- Prepaid inference credit pools with no periodic-bill anchor — they systematically cause overspend because there's no utility-bill feedback loop
- Standing up an FDE function because it's in vogue rather than because the quadrant and platform tests both pass
- Letting an agent become a pile of customer-specific prompts and patches — too brittle, and a black box the customer can't own
- Teaching the model a bespoke DSL, custom JSON schema, or framework convention when a native language would do — output quality drops even with many examples
- Shipping LLM-generated skills: they burn more tokens and reasoning time than human-written ones and measurably hurt performance
- Pulling from skill marketplaces that lack verification controls — the current state is comparable to NPM ten years ago, and skills execute unisolated on the agent's own machine
- Cutting research refresh frequency or capping result counts to control per-query bills — that degrades your own knowledge work rather than fixing the cost model
- Splitting an application into two services with a hand-maintained contract, plus a second set of frontend types, purely to keep the agent layer in Python
- Building a separate agent per domain instead of one general-purpose engine specialized through skills
- Taking vendor guidance on inference architecture at face value — each major player advocates the architecture that favors its own business
- Assuming breadth is unreachable for a small team; the old 'compete on depth only' startup rule no longer holds

## Notable Outliers

- One of the largest US retailers spent close to $200M on inference with a single vendor before deciding it was out of hand and building its own infrastructure; Uber's CTO reported burning a full year's token budget by month four. ([Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md), [0:00](https://www.youtube.com/watch?v=Bck7ABCZRZI&t=0s))
- Context-as-a-service vendors are structurally capped in coverage — if they never collected a field, an agent can never obtain it from them, which is why search-based agents beat a purpose-built vertical index on company enrichment. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [11:34](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=694s))
- Prompt management is the one layer where a clear majority (61%) build rather than buy — 'apparently everyone's prompts are special' — while fine-tuning is a 'not yet' layer most teams skip entirely. (["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md), [12:50](https://www.youtube.com/watch?v=RGe6EjucbzI&t=770s))
- Enterprise moats are flipping from friction (high switching cost) to fluency, because coding agents made porting a codebase cheap; 'teachability' is becoming an evaluation criterion alongside security, compliance, and SLAs. ([Skills are the New SDKs](../talks/skills-are-the-new-sdks.md), [7:26](https://www.youtube.com/watch?v=LC3-P7v3yoI&t=446s))
- Palantir's ~$4M ACV is the highest of any public SaaS company in the Fortune 500 — ServiceNow is next at $1.2M and no other public SaaS company cracks $500K — which is the economic case for the services-heavy FDE model. ([Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [6:54](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=414s))
- Choosing the application-layer language is itself a build-vs-buy decision: TypeScript buys you NPM plus a single Zod schema end-to-end, and overlooking it now means falling behind — directly against the view that language identity was always near-meaningless. ([A Song of Types and Agents](../talks/a-song-of-types-and-agents.md), [13:45](https://www.youtube.com/watch?v=UlFB6efYN5Q&t=825s))

## All Talks

- [A Song of Types and Agents](../talks/a-song-of-types-and-agents.md)
- [Everything we knew about software has changed](../talks/everything-we-knew-about-software-has-changed.md)
- [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md)
- [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)
- [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)
- [Skills are the New SDKs](../talks/skills-are-the-new-sdks.md)
- [Stop Renting Your Cognitive Infrastructure](../talks/stop-renting-your-cognitive-infrastructure.md)
- ["The biggest challenge in your stack? Evals, Evals, Evals"](../talks/the-biggest-challenge-in-your-stack-evals-evals-evals.md)
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)

## Speakers

- [Benjamin Guo](../speakers/benjamin-guo.md)
- [Elvin Aghammadzada](../speakers/elvin-aghammadzada.md)
- [James Russo](../speakers/james-russo.md)
- [Kevin Bai](../speakers/kevin-bai.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Rob Cheung](../speakers/rob-cheung.md)
- [Roberto Stagi](../speakers/roberto-stagi.md)
- [Sunny Rekhi](../speakers/sunny-rekhi.md)
- [Thiyagarajan Maruthavanan](../speakers/thiyagarajan-maruthavanan.md)

