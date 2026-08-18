---
title: "forward deployed engineering"
type: "concept"
slug: "forward-deployed-engineering"
tier: "core"
maturity: "contested"
talk_count: 10
speaker_count: 10
---

# forward deployed engineering

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Core concept* &middot; discussed across **10** talk(s) by **10** speaker(s)

**Definition:** Engineers embedded with customers to build, tune, and ship AI systems in the customer's environment, and the operating model that makes that repeatable.

*Also referred to as: design partnership, customer embedding, enterprise customer onboarding, customer enablement, co-development, staff augmentation, enterprise software implementation*

## State of Practice

FDE has become the default enterprise motion for agentic products, and the track's operators converged on a structural definition: a customer-facing software engineer who builds on top of a shared platform and whose real output is generalized product, not customer deliverables. The consensus mechanic is the feedback loop — Factory calls deployed engineers 'the tip of the spear of the product,' Decagon architects every customer-specific fix 'for B, C, D, and E,' and Kepler frames FDE outright as a product strategy rather than a role. The near-universal failure mode named is the dev shop: per-customer bespoke builds with no shared primitives, whose maintenance cost eventually eats the P&L. Speakers agree the binding constraint has moved off model capability — coding is 'mostly solved' given context engineering (Cognition), agent autonomy is gated by the density of deterministic validation loops in a codebase rather than model quality (Factory), and the hard remaining work is understanding and redesigning the customer's process (Varick). What the field has not settled is whether FDE is a product function or a commercial one, and how much implementation work you may legitimately do on the customer's behalf before you have quietly become a consultancy; ROI measurement for agent deployments is openly called unsolved.

## Consensus

### The FDE's primary output is product signal and generalized capability fed back into the platform, not the customer deliverable itself.

Support: **6** talk(s)

> "we need deployed engineers to be the tip of the spear of the product"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [3:41](https://www.youtube.com/watch?v=wpOA-UXynoM&t=221s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md)

### Customer-specific work must sit on top of shared platform primitives and be upstreamed when it recurs; building from scratch per customer turns the function into an unscalable dev shop.

Support: **4** talk(s)

> "If you were to implement an FTE function where each FTE is building entirely from scratch, my friends, you do not have an FTE function. You have a dev shop."
>
> — [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [8:12](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=492s)

Supporting talks: [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)

### Hire real senior software engineers who can face a customer — technical depth is the non-negotiable filter, and the customer/business side can be developed on the job.

Support: **4** talk(s)

> "a FTE is nothing more than a customerfacing software engineer."
>
> — [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [16:50](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=1010s)

Supporting talks: [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)

### Saying yes to every customer request is the core FDE failure mode; scope must be narrowed, problem-anchored, and validated against the rest of the pipeline before anything is built.

Support: **4** talk(s)

> "So, I would say there's this thing where like people many many people think that as an FDE, your job is to just say yes to the customer. But that's wrong."
>
> — [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [2:14](https://www.youtube.com/watch?v=ITMXwI6QL6A&t=134s)

Supporting talks: [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)

### Model capability and code generation are no longer the bottleneck; the constraint has moved to context, validation, process design, and deployment.

Support: **5** talk(s)

> "Coding itself, at least from our perspective, is a mostly solved problem, right? These models are so good now that like with any type of context, with enough context engineering, you can get the code blocks that you really care about."
>
> — [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [4:08](https://www.youtube.com/watch?v=RVxym6mmIns&t=248s)

Supporting talks: [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)

### An explicit, business-denominated outcome must be agreed before the engagement starts, because ROI for agent deployments is otherwise ambiguous and unprovable.

Support: **4** talk(s)

> "there needs to be an ROI or an outcome story that is extremely clear from the beginning"
>
> — [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [8:59](https://www.youtube.com/watch?v=wpOA-UXynoM&t=539s)

Supporting talks: [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)

## Disagreements

### Is forward deployed engineering a product function or a go-to-market / commercial motion?

| Position A | Position B |
|---|---|
| FDE is an extension of the product organization and should report and be measured that way; treating FDEs as GTM extensions is a mistake, especially for early-stage companies, and produces PM-plus-customer-success theater instead of product direction.<br>*[How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)* | FDE is fundamentally a commercial motion — you sell product and services as one combined outcome, and the services/embedding component is what actually captures enterprise value; a pure product company cannot.<br>*[Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)* |

*Why it matters: It determines where the function reports, what its KPIs are (product influence and generalization vs. ACV, delivery, and expansion), and whether an engagement that never produces a product change counts as a success or a failure.*

### Should deployed engineers do implementation work on the customer's behalf?

| Position A | Position B |
|---|---|
| No. Professional services work does not improve the product and does not scale; a customer asking for FDEs because they are understaffed is staff augmentation and a red flag, and 'make the customer successful' is the solutions-architect job, not the FDE's.<br>*[How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)* | Yes, and at length — multi-month embeds that deliver measurable engineering capacity (a three-month embed delivering ~150%+ additional headcount, a ten-month deployment in Brazil, department-wide process transformation) are the value proposition.<br>*[How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)* |

*Why it matters: This decides whether your headline metric is customer engineering output delivered or product capability generalized, and whether long embeds are the business model or the symptom of a missing product.*

### When an FDE hits a customer-specific problem, should they ship the fix immediately or hold back until it can be generalized?

| Position A | Position B |
|---|---|
| Exercise restraint. The scarce skill now that AI coding is cheap is *not* building the fast one-off; architect the solution for the next four customers, because a pile of customer-specific prompts and patches is too brittle for both sides, and anything generalizable should be generalized.<br>*[How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)* | If it is under a day of work, just build it and ship it and close the loop — do not route it through product process. Solving small problems fast is precisely how FDEs earn the right to define product strategy later.<br>*[How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)* |

*Why it matters: Kepler's own warning that any hack solving a real problem runs for 18 months means the cheap fix carries permanent maintenance liability; the choice sets whether your platform accretes generalized primitives or a long tail of supported one-offs.*

### Are frontier models sufficient for the judgment-heavy parts of deployed work, or do you need post-trained custom models?

| Position A | Position B |
|---|---|
| Frontier models are good enough — they can one-shot medium-sized features from a well-shaped spec, and coding is mostly solved given enough context engineering; the remaining work is scoping, verification, and environment prep, not model quality.<br>*[How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)* | For long-form business analysis and process normalization, frontier models are verbose and incorrect and cannot judge which details a client cares about; post-trained open-source models plus RL-trained custom retrieval tools outperform them.<br>*[AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)* |

*Why it matters: If frontier models suffice, FDE tooling investment goes into context plumbing and validation harnesses; if not, teams must fund a post-training and RL pipeline to automate the client-facing half of the role.*

## Practical Guidance

**Do:**

- Ask 'do I need an FDE function, not want one' — it only fits when you sell a highly technical product to a non-technical buyer, and only if you have a platform or will invest in building one
- Ask the customer to name the specific people on their side who will work with you; if there is no named counterpart working team, the engagement is structurally broken
- Keep scope directional and phased ('phase one and two, these agents, six weeks'), never 'take two FDEs for six months and do whatever you want with them'
- Get success metrics and communication channels agreed in writing during the earliest deal conversations
- Measure agent readiness as the density of deterministic validation loops in the customer's codebase, and prepare the verification environment before trying to solve the problem
- Reduce every claimed outcome to increasing revenue, decreasing costs, or mitigating risk
- Treat any task an engineer has to do manually as a missing product capability and upstream it — Decagon self-served custom integrations after the 25th one
- Verify the sales rep's stated urgency against the customer's actual driver, and validate base assumptions (e.g. which mobile platform they mandate) before committing engineering weeks
- Staff multiple FDEs per customer project and hire 5+ years of engineering experience rather than early-career; organize by industry rather than geography once you scale, because wrong vocabulary costs credibility instantly
- Ship every hack as if it will run for 18 months, because it will and you will support it
- Preserve enough of the customer's original step structure when redesigning workflows that operators still recognize the process, and mark explicitly which steps are autonomous, human-in-the-loop, and human-only
- Tell the customer when your product is the wrong tool — it builds credibility and generates later opportunities

**Avoid:**

- Building each engagement from scratch with no shared primitives — that is a dev shop, and maintenance costs will eat the P&L before your engineers quit
- Doing professional-services work on the customer's behalf: it produces decent revenue but does not scale and does not improve the product
- Running product 101/201 sessions, writing bug reports, updating documentation, or doing company-wide rollout training — delegate change management to SI and consulting partners
- Accepting an engagement whose justification is 'we're understaffed' — that is staff augmentation wearing an FDE label, and the engineers you sold will get bored and leave
- Taking the customer's requirements document at face value: customers describe solutions, not problems, and whoever defines the problem owns the solution
- Deploying agents with no specific direction — that is token maxing, and scoping failure at scale produces a 'token maxing slop cannon'
- Requiring the customer to migrate off their system of record (NetSuite, SAP, Dynamics, Salesforce) — they spent years and millions getting there
- Building a demonstration deployment far ahead of the org's current practice; it gets dismissed as a theme park rather than copied
- Being a forward deployed engineer in name from a conference room instead of on site — the badge and the contractor email are the actual data-mining permits
- Forcing one canonical schema onto teams that use different words for the same entity; terminology divergence across sales, ops, finance, and engineering is how humans work
- Building a software factory on a vendor-locked single-model platform where you do not own the traces and data
- Applying AI on top of broken, undocumented processes and expecting ROI

## Notable Outliers

- Post-trained open-source models beat frontier models at writing normalized process flows, because frontier models have no concept of which detail the client actually cares about — and custom RL-trained graph traversal tools are needed just to resolve that there are many Mikes at every company. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [16:40](https://www.youtube.com/watch?v=l0FLhNqBOic&t=1000s))
- Controlling an enterprise's vocabulary through your ontology is the real lock-in: users don't just adopt your product, they adopt your language, and if you become the linguistic foundation everything else builds on you. ([How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md), [15:20](https://www.youtube.com/watch?v=1OMHGsUZiqA&t=920s))
- The term 'forward deployed engineer' does not exist as a coherent role — it describes so many jobs it means nothing — yet it is the hottest job in AI, and hiring managers should ask candidates what 'vintage' of FDE they are. ([The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md), [2:21](https://www.youtube.com/watch?v=Byv311hdoHE&t=141s))
- Factory reports ~15-20% autonomy internally with an autonomy ratio in the upper 80s — the ratio of actions done by AI systems to humans before interruption — and expects constrained internal tools to hit 100% autonomy before general product codebases. ([How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md), [18:13](https://www.youtube.com/watch?v=wpOA-UXynoM&t=1093s))
- Palantir's ~$4M ACV is the highest of any public SaaS company in the Fortune 500, ahead of ServiceNow at $1.2M and Workday at ~$600K, with no other public SaaS company cracking half a million. ([Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md), [6:54](https://www.youtube.com/watch?v=KwhgfwOSToQ&t=414s))
- The one-version-for-everyone software pipeline was an artifact of change being expensive; the endpoint is deploying one canonical stem where every user runs their own bounded divergence, with blast radius of one context and rollback without a deploy. ([The Pipeline Is Dead](../talks/the-pipeline-is-dead.md), [7:56](https://www.youtube.com/watch?v=bRnoEpoK5m4&t=476s))
- Outcome-based pricing is where software pricing is heading, and forward deployed engineering is the only mechanism that makes guaranteeing that outcome possible. ([The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md), [14:40](https://www.youtube.com/watch?v=Byv311hdoHE&t=880s))

## All Talks

- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Forward Deployed Engineering 101](../talks/forward-deployed-engineering-101.md)
- [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)
- [How Forward Deployed Engineering is done at Factory](../talks/how-forward-deployed-engineering-is-done-at-factory.md)
- [How Forward Deployed Engineering is done at Kepler](../talks/how-forward-deployed-engineering-is-done-at-kepler.md)
- [How Forward Deployed Engineering is done at Ramp](../talks/how-forward-deployed-engineering-is-done-at-ramp.md)
- [The Dirty Secret of Forward Deployed Engineering](../talks/the-dirty-secret-of-forward-deployed-engineering.md)
- [The Pipeline Is Dead](../talks/the-pipeline-is-dead.md)

## Speakers

- [Eno Reyes](../speakers/eno-reyes.md)
- [Jia Wu](../speakers/jia-wu.md)
- [Kevin Bai](../speakers/kevin-bai.md)
- [Leo Mehr](../speakers/leo-mehr.md)
- [Natalie Meurer](../speakers/natalie-meurer.md)
- [Pauline Brunet](../speakers/pauline-brunet.md)
- [Sunny Rekhi](../speakers/sunny-rekhi.md)
- [Varun Singh](../speakers/varun-singh.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)
- [Vinoo Ganesh](../speakers/vinoo-ganesh.md)

