---
title: "roi measurement"
type: "concept"
slug: "roi-measurement"
tier: "supporting"
maturity: "contested"
talk_count: 9
speaker_count: 9
---

# roi measurement

**Maturity: CONTESTED** — Contested — active, unresolved disagreement across talks

*Supporting concept* &middot; discussed across **9** talk(s) by **9** speaker(s)

**Definition:** Quantifying the business return of AI deployments and using it to prioritize, justify, or kill agent investments.

*Also referred to as: enterprise ai roi measurement, agent deployment roi, roi scoring and prioritization, time to value, technical debt roi, revenue per employee, cost governance for agents*

## State of Practice

The field has converged on what ROI is *not*: token spend, lines of code, PR counts, weekly active users, and demo quality are all rejected as proxies, and speakers repeatedly cite the MIT figure that 95% of generative AI pilots never reach production with ~87% showing no measurable return. What replaced them is outcome-anchoring — delivery-timeline compression, headcount-equivalent delivered, whether the customer keeps the system running after the vendor leaves, commit rate and breadth of contributing developers — plus a hard prerequisite that any claimed win be verified at runtime rather than accepted because it reads plausibly. The consensus diagnosis of failed ROI is not model quality but wiring: broken or undocumented processes, missing context plumbing, and unreliable infrastructure, with the same frontier model producing 2X for one team and 100X for another. Scope is treated as the dominant ROI variable — single-function point solutions are quoted at 5–10% return versus 25–75% for department-wide redesign, and single-point tools (a CLI, an IDE) are argued to be structurally incapable of moving an org-level number. What remains genuinely unresolved is attribution: vendor-side speakers quote precise multiples (82% delivery reduction, 150%+ headcount equivalent, ~2x PR output) while the DORA 2026 data and YC's own read say individual effectiveness rises without team throughput moving, and one FDE lead flatly calls agent ROI measurement an unsolved problem.

## Consensus

### Model capability is no longer the binding constraint on returns; the constraint is process design, context plumbing, and reliability — how the work is wired around the model.

Support: **5** talk(s)

> "The 2X people and the 100X people are using the exact same Claude. Same weights, same context window, same API. So, the leverage is not in the weights. It's in how you wire the work."
>
> — [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [2:52](https://www.youtube.com/watch?v=eBUyTS7SzV4&t=172s)

Supporting talks: [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)

### Activity proxies (token usage, lines of code, PR volume, weekly active users) are the wrong success metrics for agent deployments; measure delivered outcomes and durable use instead.

Support: **5** talk(s)

> "your actual aim should be the weekly active users go down while weekly active sessions go up"
>
> — [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [13:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=816s)

Supporting talks: [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)

### Agents deployed without a narrowly defined, pre-agreed problem produce no measurable return — scope must be problem-anchored before the engagement starts.

Support: **4** talk(s)

> "So, if the software development life cycle is extremely complex, deploying the agents for with like no specific direction, you're straight up just token maxing."
>
> — [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [4:46](https://www.youtube.com/watch?v=RVxym6mmIns&t=286s)

Supporting talks: [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)

### Plausible-looking agent output must be verified against runtime reality before it counts as value; a convincing artifact is not evidence of a result.

Support: **4** talk(s)

> "it's very easy to undergo AI psychosis, where you look at a deep research report that's 20 pages long and you say, "Wow, this looks good." And then those features don't actually exist in the product, and you've set yourself back."
>
> — [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [4:24](https://www.youtube.com/watch?v=7vn4WpqNpck&t=264s)

Supporting talks: [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md), [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)

### Returns concentrate at the department/organization level, not the individual-tool or single-function level; making engineers faster does not move a business number.

Support: **3** talk(s)

> "You can make engineers like 10x faster. That's fine. That's still valuable. But can you make an organization 10x faster, including every single person that might be technical or non-technical uh across the company?"
>
> — [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [11:20](https://www.youtube.com/watch?v=RVxym6mmIns&t=680s)

Supporting talks: [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)

## Disagreements

### Can the ROI of agent deployments actually be measured and attributed today?

| Position A | Position B |
|---|---|
| Yes — enterprise value reduces to revenue up, cost down, or risk mitigated, and deployments produce quotable numbers: 82% delivery-timeline reduction, ~150% headcount-equivalent delivered over a three-month embed, ~2x PR output versus single-point tools, 5–10% ROI for point solutions versus 25–75% for department-wide transformation.<br>*[Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)* | No — attribution is unresolved. The 2026 DORA data shows individual effectiveness rising while team throughput stays flat and software breaks more often; YC concedes it cannot prove AI-generated code caused its fastest-growing batch's growth; and Cognition's own FDE calls measuring agent ROI an ambiguous, unsolved problem.<br>*[From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)* |

*Why it matters: If the quoted multiples are real, agent spend justifies itself on delivery metrics alone and buyers should scale up now; if individual gains don't aggregate to team throughput, every vendor case study is measuring the wrong level and budgets are being approved against a number that doesn't exist at the P&L.*

### Where does the durable return come from — bespoke per-customer work, or productizing that work away?

| Position A | Position B |
|---|---|
| From the bespoke last mile. A generic end-to-end agent only gets 80–90% of the way there and the remaining value is in customer-specific conventions; a pure product company cannot capture enterprise AI value at all, so a services/forward-deployed motion is required and multi-month embeds are the delivery unit.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)* | From generalization. Customer-specific prompts and patches are too brittle for both vendor and customer; the scarce skill now that AI coding is cheap is restraint — solve customer A for B, C, D and E, upstream anything done manually, and hand mature customers self-service documentation instead of an FDE.<br>*[How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)* |

*Why it matters: This decides whether headcount scales with customer count or with product surface, and therefore whether the ROI you book is gross-margin-bearing software revenue or services revenue that has to be re-earned on every account.*

### Should an AI deployment preserve the shape of the existing human workflow, or deliberately restructure it so humans stop operating and start supervising?

| Position A | Position B |
|---|---|
| Preserve it. Changing an 11-step workflow into a one-step one takes operators aback and adoption rates suffer; the right move is per-step allocation (some steps autonomous, some human-in-the-loop, some human, period), and rollouts must accompany people or nobody uses the tool.<br>*[AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)* | Restructure it. Design for delegation, not participation — agents are workers on a conveyor belt and users are supervisors, target tasks that take more than a couple of hours, and accept that almost every org is still built for a seven-digit brain and needs rewiring.<br>*[Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)* |

*Why it matters: The adoption-preserving path caps measurable savings at whatever the legacy step structure allows, while the restructuring path unlocks the larger number but risks a deployment nobody uses — and the two produce opposite success metrics (usage up versus usage down).*

## Practical Guidance

**Do:**

- Anchor every business case to one of three levers — increasing revenue, decreasing cost, or mitigating risk — and reject cases that don't reduce to one of them
- Get success metrics and communication channels agreed in writing during the earliest deal conversations, before any building starts
- Use durable-use as the ROI test: did the customer keep the deployed systems running after the team walked away?
- Scope department-wide rather than single-function; a single function (e.g. AP alone) is quoted at 5–10% return versus 25–75% for whole-department redesign
- Prioritize by ROI rather than raw impact — weigh impact against review risk, and surface one high-signal, human-readable finding at a time instead of a batch of PRs
- Rank automation candidates from the customer's own historical data (e.g. ingest historical support tickets to show which workflow automates for highest return first)
- Require runtime verification that a proposed fix improved the specific production flow before counting it as a win
- Evaluate model time-horizon curves at 80% success and above, not the commonly shared 50% — a one-hour task at 50% is a coin flip on a wasted hour
- Hold autonomous automations to roughly 80–90% trust; 80% is only acceptable for interactive IDE use where a human is in context
- Track commit rate and the breadth of developers contributing, not lines of code, as the signal that a refactor paid off
- Convert every agent task that succeeds into a reusable skill file so the same work is never paid for twice
- Build on top of the customer's existing system of record (NetSuite, SAP, Dynamics, Salesforce) rather than requiring migration off it
- Deliberately narrow the initial enterprise scope to prove value fast, then expand, instead of accepting the kitchen-sink scope

**Avoid:**

- Token-maxing — treating token usage or spend as the deployed-engineering KPI
- Selling or buying a fixed allocation of engineers for a fixed period with no defined problem attached
- Accepting a polished artifact as evidence of a result ("AI psychosis" from a 20-page research report describing features that don't exist)
- Shipping the plausible-unverified fix — e.g. catching the exception so the error stops appearing
- Optimizing things that run every three weeks or save 20 milliseconds
- Auto-opening large volumes of PRs; nobody wants to wake up to a rain of 80 pull requests
- Applying AI on top of broken, undocumented processes instead of redesigning the process first
- Shipping citations as your trust mechanism — they shift the verification burden back onto the customer, which is worst in healthcare, legal, and tax
- Treating weekly active users or lines of code as a success metric for agentic products
- Taking an FDE engagement where the stated need is "we're understaffed" — that's staff augmentation, not a deployment
- Letting the agent author its own queries against observability data when a structured skill would cut eval variance
- Adding complexity to the codebase faster than the ROI you generated can absorb it
- Assuming general AI tooling gives non-technical operators in finance, sales, and procurement the same return it gives software engineers

## Notable Outliers

- Whoever solves ROI measurement for agent deployments becomes a $5 trillion market cap company — it is currently an ambiguous, unsolved problem. ([How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md), [5:18](https://www.youtube.com/watch?v=RVxym6mmIns&t=318s))
- Point solutions inside a single function yield 5–10% ROI; department-wide transformation yields 25–75%. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [11:07](https://www.youtube.com/watch?v=l0FLhNqBOic&t=667s))
- Google's 2026 DORA report shows AI's biggest effect is individual effectiveness, while team throughput is unchanged and software breaks more often. ([From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md), [2:20](https://www.youtube.com/watch?v=JJGbw4ggaFs&t=140s))
- 95% of generative AI pilots fail to reach production and roughly 87% produce no measurable ROI. ([AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md), [5:05](https://www.youtube.com/watch?v=l0FLhNqBOic&t=305s))
- Kicking off a one-hour agent run with a 50% completion rate is likely a wasted hour, which is why the 80%+ point on the time-horizon curve is the only one that matters for delegation. ([Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md), [8:33](https://www.youtube.com/watch?v=7vn4WpqNpck&t=513s))
- The correct success signal for a delegated agentic product is weekly active users declining while weekly active sessions rise. ([Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md), [13:36](https://www.youtube.com/watch?v=RGiXcVxSD3s&t=816s))

## All Talks

- [AI tools for Forward Deployed Engineering](../talks/ai-tools-for-forward-deployed-engineering.md)
- [Benchmarking Coding Agents on New vs Legacy Codebases](../talks/benchmarking-coding-agents-on-new-vs-legacy-codebases.md)
- [Chat and citations won't save your vertical AI](../talks/chat-and-citations-wont-save-your-vertical-ai.md)
- [Deterministic Infra for Non-Deterministic AI Agents](../talks/deterministic-infra-for-non-deterministic-ai-agents.md)
- [Every company should have a Brain](../talks/every-company-should-have-a-brain.md)
- [Forward Deployed Engineering at Cursor](../talks/forward-deployed-engineering-at-cursor.md)
- [From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization](../talks/from-blind-spots-to-merged-prs-continuous-agentic-performance-optimization.md)
- [How Forward Deployed Engineering is done at Cognition](../talks/how-forward-deployed-engineering-is-done-at-cognition.md)
- [How Forward Deployed Engineering is done at Decagon](../talks/how-forward-deployed-engineering-is-done-at-decagon.md)

## Speakers

- [Atul Ramachandran](../speakers/atul-ramachandran.md)
- [Denys Linkov](../speakers/denys-linkov.md)
- [Garry Tan](../speakers/garry-tan.md)
- [Jia Wu](../speakers/jia-wu.md)
- [May Walter](../speakers/may-walter.md)
- [Nishant Gupta](../speakers/nishant-gupta.md)
- [Pauline Brunet](../speakers/pauline-brunet.md)
- [Sunny Rekhi](../speakers/sunny-rekhi.md)
- [Vasuman Moza](../speakers/vasuman-moza.md)

