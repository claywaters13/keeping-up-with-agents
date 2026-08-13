---
title: "web data infrastructure"
type: "concept"
slug: "web-data-infrastructure"
tier: "supporting"
maturity: "contested"
talk_count: 9
speaker_count: 9
---

# web data infrastructure

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **9** talk(s) by **9** speaker(s)

**Definition:** Acquiring and representing web-scale content for models — crawling, scraping, anti-bot handling, and page-to-token representation.

*Also referred to as: web scraping at scale, web scraping pipelines, long tail of the web, browser automation infrastructure, anti-bot evasion, web page representation for llms, dom compression*

## State of Practice

The field has largely stopped treating page acquisition as a model problem: speakers from Browserbase, ARK, Oxylabs and Rexmore all located the bottleneck in the harness — page representation, rendering consistency, latency, and action verification — rather than in model capability. The concrete state of the art is a compressed page representation (accessibility tree with ARIA tags, or a ~1,800-token markdown projection of a page whose raw DOM is ~20,000 tokens) supplied alongside a screenshot, plus explicit state-diff feedback telling the agent what appeared, what was removed, and whether its click landed. Pure click-by-click interaction is out of favor; the reliable production pattern is hybrid — intercept and replay network requests or write code for the deterministic parts, and spend model calls only where eyes and judgment are required. On the acquisition side, the economics have shifted from record volume to query frequency and freshness: web context decays in under a day for social and ~30 days for news, finance and retail, and per-query pricing pushes teams to refresh less often, which is why owning a scraping pipeline breaks even against rented context surprisingly early. Anti-bot handling is now an explicit engineering discipline — CDP-driven input carries Chrome's trusted stamp and is indistinguishable from a human to Cloudflare and Google — while the good-agent identity problem (who vouches for a legitimate agent) has no answer anyone presented.

## Consensus

### The limiting factor for web agents is the surrounding infrastructure — harness, page representation, rendering consistency, latency — not the capability of the underlying model.

Support: **4** talk(s)

> "The hypothesis here is models are pretty smart, but it's the infra around them that sucks."
>
> — [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [0:54](https://www.youtube.com/watch?v=JnubYCYunk8&t=54s)

Supporting talks: [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)

### Raw DOM/HTML is the wrong thing to put in front of a model; the page must be compressed into a purpose-built representation (accessibility tree, markdown projection, or a narrowed slice of the page) before it enters context.

Support: **4** talk(s)

> "The full DOM for this would be around 20,000 tokens. But so, let's say we have this screenshot. All right, this screenshot's about 1,100 tokens. My markdown's about 1,800 tokens"
>
> — [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [3:15](https://www.youtube.com/watch?v=JnubYCYunk8&t=195s)

Supporting talks: [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)

### Web automation should be hybrid rather than click-only: generate and run code, or intercept and replay network requests, for the deterministic portions, and spend model calls only where perception and judgment are needed.

Support: **3** talk(s)

> "Code does the deterministic driving and the agent does the only bits that require eyes and a brain."
>
> — [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [17:54](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=1074s)

Supporting talks: [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)

### An action must be verified through a different channel than the one that performed it — the agent needs independent evidence (network response, rendered screen, explicit page state diff) that the click actually landed.

Support: **3** talk(s)

> "if you've clicked something, don't ask the click if it was successful. Check the network or check the screen."
>
> — [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [6:10](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=370s)

Supporting talks: [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)

## Disagreements

### Should the primary observation channel for a web agent be pixels/screenshots, or a compressed structured-text representation of the page?

| Position A | Position B |
|---|---|
| Pixels are the source of truth. The web was built for human eyes, content is computed and rendered rather than present as text, and a general screenshot-in model beats any text extraction that has to be scaffolded per site.<br>*[Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)* | Screenshots are an inadequate primary channel because they expose only one viewport at a time; a compressed text representation (markdown projection or accessibility tree/ARIA) should be the main input, with the screenshot as a supplement. A cheaper model with the better representation beats a stronger screenshot-driven one on speed and success.<br>*[Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md), [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)* |

*Why it matters: It determines whether you buy vision-heavy computer-use models and eat per-step latency, or invest in an extraction/compression layer and run a cheaper model. It also determines the failure mode you must engineer against: OCR/rendering errors versus extraction drift when layouts change.*

### Will the web grow agent-native interfaces (APIs, MCP servers, MCP-delivered UI), or will agents be permanently stuck driving human-facing pages?

| Position A | Position B |
|---|---|
| Delusional to expect it. The head of the distribution may ship APIs but the long tail — 200 million active sites, FOIA-era government portals, PDFs embedded as JPEGs — will not, and 30 years of human-oriented infrastructure will not be reinvented in 2-10 years. Driving the web UI is the permissionless universal API, and often the only path when official API access needs admin approval you cannot get.<br>*[Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)* | It is already happening: sites can publish MCP servers inside the page for agents to use without pre-installation, teams should be designing agent-first signup and login flows now, and websites will fragment into composable UI chunks rendered inside personal assistants rather than browsed as tabs.<br>*[Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)* |

*Why it matters: If the long tail never becomes machine-readable, the durable investment is general vision-plus-code computer use and anti-bot handling; if agent-native surfaces arrive, that investment is a bridge technology and the work moves to publishing and consuming declarative UI/tool contracts.*

### Should teams buy web data and browser infrastructure from a vendor, or own the pipeline themselves?

| Position A | Position B |
|---|---|
| Buy it. Building compliant, consistent browser infrastructure at scale is not where product teams should spend time, and collection is an adapt-forever business — targets, layouts, and detection change continuously, so what you are really buying is the vendor's ability to keep adapting.<br>*[Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)* | Own it for anything recurring. Rented context is priced per query, so frequency — not record volume — is the cost killer, and the build-vs-rent break-even lands at just over 15,000 entities/queries against roughly a week and $5,000 of setup; go straight to the sources the vendors themselves scrape.<br>*[The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)* |

*Why it matters: It sets whether repeated retrieval is a marginal cost you must ration (capping result counts, refreshing weekly instead of daily) or a fixed cost you can query without fear, which directly changes how fresh the agent's context is.*

### Should agents reach browsers through MCP servers or through shell CLIs?

| Position A | Position B |
|---|---|
| Shell CLIs. Success rates are equivalent (~83% both ways per an Arize study) but a CLI sequence is written once and replayed a thousand times with no model in the loop — seven turns and under a minute versus 71 round trips and 8 minutes, and up to 75x cheaper in tokens.<br>*[The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)* | MCP, extended with UI. MCP Apps is the recommended protocol for ChatGPT apps, is being standardized as the UI layer for agent interfaces, and lets sites expose interactive surfaces the agent and host can both drive — including MCP servers published inside the page itself.<br>*[MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md), [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)* |

*Why it matters: The two answers optimize different things — token cost and repeatability versus distribution and rich interaction — and they lead to opposite tool-layer investments for a team automating the web at volume.*

## Practical Guidance

**Do:**

- Supply a compressed page representation (~1,800-token markdown projection, or the accessibility tree with ARIA tags) alongside the screenshot, instead of the raw DOM
- Emit an explicit state diff after every action — what appeared, what was removed, whether the click landed — so the agent can recover instead of guessing
- Verify actions through a different sensory channel than the one that acted: check the network response or the rendered screen, never the click's own return
- Escalate click technique in rungs: synthetic JavaScript click by default, trusted CDP input events only when the page silently rejects untrusted ones (Amazon's add-to-cart ignores untrusted clicks with no error)
- Intercept network requests and have a coding agent write a replay script for the deterministic parts of a flow rather than clicking every step
- Benchmark every agent against the bare baseline model on the same task to prove the harness is actually adding value
- Pin rendering consistency — same viewport and layout every run — since mobile-vs-desktop rendering drift alone produces inconsistent results
- Keep the browser infrastructure model-agnostic so the agent can be moved as models change
- Have agents author artifacts in HTML/CSS/JS, the languages their training data is made of, rather than a bespoke DSL or JSON schema
- Budget web context by query frequency rather than record volume, and compute the build-vs-rent break-even explicitly (~15,000 entities/queries against roughly a week and $5,000 of setup)
- Refresh on the data's actual decay clock: under a day for social media, roughly 30 days for news, finance, and retail
- Strip ads, widgets, rich results, and heavy layout from search collection and keep only organic results, top stories, and news when building for AI consumption
- Write agent skills that teach taste and domain craft, not framework syntax the model already knows

**Avoid:**

- Dumping full page content into the model — it raises cost and produces subpar results
- Screenshot-only observation loops: one viewport-sized snippet per look means scroll-screenshot-scroll cycles that burn 10-20 seconds and two minutes to complete a single button click
- Hand-writing per-site scaffolds, which do not generalize to the long tail of the web
- Round-tripping a model on every interaction when a clock is running — reCAPTCHA v2 challenge rounds expire before a per-click agent finishes
- Assuming the answer is in the HTML you fetched; content is fetched asynchronously and computed by rendering logic, so a raw-HTML read returns nothing useful
- Waiting for models to improve instead of doing the engineering — the capabilities overhang is solvable today
- Running production browser fleets on self-hosted Mac Minis, which do not give you a SOC 2 compliant path at scale
- Teaching the model a new DSL or custom JSON structure — output quality degrades even with many examples
- Trying to absorb a 6x traffic increase by adding hardware; even 2,000 extra servers do not close a 10k-to-60k requests-per-second gap without an architecture change
- Rationing refresh frequency or capping result counts to control per-query cost, which quietly degrades the knowledge work the agent is doing
- Treating CAPTCHAs as a reliable human/agent boundary — they no longer distinguish agents from humans, and no trust issuer exists yet to replace them

## Notable Outliers

- Cloudflare Turnstile's checkbox sits behind a closed shadow root inside a cross-origin iframe that contains another shadow root, so it is unreachable by normal automation — the workaround is to ask the browser where the iframe sits, compute the checkbox position, and fire a trusted click at that spot on the glass. ([The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [13:38](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=818s))
- Jigsaw captchas sample the entire mouse trail during the drag, so passing requires reproducing jitter, easing, curvature, and a deliberate overshoot that eases back in — correct final positioning alone fails. ([The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [15:48](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=948s))
- Mind2Web is saturated — 97% human eval with 8 bad trajectories out of 300 — and should be retired for a harder benchmark; the real differentiator is now latency per step and cost per task (80 cents versus $230 on a 20-30 step task), not accuracy. ([Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md), [16:31](https://www.youtube.com/watch?v=Ki980nV0__0&t=991s))
- Sub-second search collection came from many small decisions across layouts, parsers, sessions, and proxies rather than a breakthrough — 4s average down to 550ms while scaling from 400 million to nearly 6 billion daily requests — and browsers, though necessary for reliable collection, are fundamentally incompatible with low latency. ([How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md), [10:18](https://www.youtube.com/watch?v=1UmZHb_E_SM&t=618s))
- Context-as-a-service vendors are structurally capped in coverage — if they never collected a field, no agent can ever obtain it from them — whereas a search-based agent can keep exploring; owned context compounds while rented context decays. ([The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md), [11:34](https://www.youtube.com/watch?v=Ot4OPrPH4xY&t=694s))
- CDP-driven input traverses the same internal Chrome path as human input and receives the trusted stamp, making an agent's clicks and keystrokes indistinguishable from a human's to Google and Cloudflare. ([The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md), [1:45](https://www.youtube.com/watch?v=26RtyAm9y_Q&t=105s))
- The web needs a certificate-authority-like trust issuer to distinguish good agents from bad bots, and no one has built it. ([Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md), [12:41](https://www.youtube.com/watch?v=GqoNrUz8hEU&t=761s))

## All Talks

- [Bringing agents onto the world wide web](../talks/bringing-agents-onto-the-world-wide-web.md)
- [Browser Agents Don't Need Better Models. They Need Better Eyes.](../talks/browser-agents-dont-need-better-models-they-need-better-eyes.md)
- [Computer-use models will agentify the web, not APIs](../talks/computer-use-models-will-agentify-the-web-not-apis.md)
- [How Web Data Infrastructure Powers the Next Generation of AI](../talks/how-web-data-infrastructure-powers-the-next-generation-of-ai.md)
- [HTML Is All Agents Need](../talks/html-is-all-agents-need.md)
- [HTML is All You Need (for Agents to Make Graphics)](../talks/html-is-all-you-need-for-agents-to-make-graphics.md)
- [MCP Apps: Extending the Frontier](../talks/mcp-apps-extending-the-frontier.md)
- [The Dark Arts of Web Automation: Teaching Agents to Use Websites Like Humans](../talks/the-dark-arts-of-web-automation-teaching-agents-to-use-websites-like-humans.md)
- [The Rise of CaaS: Context-as-a-Service for Agentic AI](../talks/the-rise-of-caas-context-as-a-service-for-agentic-ai.md)

## Speakers

- [Corey Gallon](../speakers/corey-gallon.md)
- [Dhruv Batra](../speakers/dhruv-batra.md)
- [Ido Salomon](../speakers/ido-salomon.md)
- [James Russo](../speakers/james-russo.md)
- [Kushan Raj](../speakers/kushan-raj.md)
- [Liad Yosef](../speakers/liad-yosef.md)
- [Omer Primor](../speakers/omer-primor.md)
- [Patricija Žemaitytė](../speakers/patricija-zemaityte.md)
- [Paul Klein IV](../speakers/paul-klein-iv.md)

