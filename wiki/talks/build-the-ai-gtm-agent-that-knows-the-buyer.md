---
title: "Build the AI GTM Agent That Knows the Buyer"
type: "talk"
slug: "build-the-ai-gtm-agent-that-knows-the-buyer"
org: "Position2 (Position Squared)"
video_id: "ltv-L5oMPIs"
duration_sec: 1586
word_count: 3961
speakers: ["Sajjan Kanukolanu"]
---

# Build the AI GTM Agent That Knows the Buyer

**Speakers:** [Sajjan Kanukolanu](../speakers/sajjan-kanukolanu.md)

**Org:** Position2 (Position Squared)

**Duration:** 26m 26s

[Watch on YouTube](https://www.youtube.com/watch?v=ltv-L5oMPIs)

## Summary

Sajjan Kanukolanu of Position2 argues that bolting AI onto an existing go-to-market stack cannot work, because modern B2B buyers arrive at your site late in their decision process and generic AI chat interfaces actively push them backwards. He proposes a three-layer architecture — signals (CRM, enrichment, social/LinkedIn), buyer intelligence (knowledge base, ICP scoring, context graph, routing logic), and action (personalized chat, rep alerts, CRM context updates, sequence triggers) — and insists all three must be solved simultaneously or the system won't scale. The middle of the talk is an implementation walkthrough of chained agents (identification → enrichment → ICP filter → CRM match → action) plus a live dashboard demo of de-anonymized visitors and LinkedIn engagement intelligence. The most useful section is the failure-mode catalog: ICP drift, alert fatigue, the identity ceiling (~70% company vs. 15–20% person identification accuracy), and the human approval bottleneck with a hard 30-second edit budget. Worth watching if you are building GTM agents and want a concrete architecture plus honest limits; skip if you want model-level or eval detail, as there is none.

## Key Points

- Buyers now complete most of their research before contacting a vendor, so GTM systems must assume every inbound visitor is late-stage rather than early-stage.
- AI bolted onto legacy GTM stacks fails on three fronts simultaneously — the AI can't identify the buyer standalone, old stacks can't capture and unify intent signals, and the underlying architecture isn't AI-native — and solving only two of the three still leaves you stuck.
- The proposed architecture has three layers: signals (CRM, visitor enrichment, LinkedIn/social), buyer intelligence (knowledge base, de-anonymized identity, ICP scoring, context builder, routing logic), and action (personalized chat, rep alerts, CRM context updates, sequence triggers).
- A context graph links per-person signals to accounts and deals, which is what surfaces the buying committee and lets teams prioritize high-intent accounts rather than treating all traffic equally.
- Position2's implementation chains discrete agents — identification across multiple vendor tools, enrichment, an ICP filter agent reading from the knowledge base, a CRM match agent, and an action agent that decides Slack alerts, email drafts, and LinkedIn outreach per person or per buying committee.
- Visitor identification tools have a structural ceiling — roughly 70%+ accurate at company level but only 15–20% at individual level — and the only remedy is continuous tool testing plus planning outreach around those known limits.
- ICP definitions drift as you close deals outside your stated profile, so agents must be retrained quarterly on closed-won and closed-lost opportunities or they will keep pointing at the wrong accounts.
- Both alert fatigue and approval-queue friction kill adoption by destroying rep trust; the practical threshold is that an AI-drafted email must be sendable with roughly one click and under 30 seconds of editing.

## Notable Quotes

> "The uncomfortable truth is that by the time the buyer reaches you, the decision is mostly made."
>
> — [0:00](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=0s) &middot; *States the premise the entire architecture is designed around.*

> "We've launched 75-plus AI agents specifically for our clients, 18-plus vertical knowledge bases that power these agents, and we've had 800-plus runs per month"
>
> — [0:52](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=52s) &middot; *Quantifies the deployment scale behind the claims.*

> "By just bolting AI onto your existing systems, AI doesn't really and cannot really find out who your buyer is. It doesn't understand their role. It doesn't understand their history."
>
> — [1:44](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=104s) &middot; *The central negative thesis, stated bluntly.*

> "94% of buyers use GenAI as a primary research. And these platforms are almost like a black box where we don't know what they consumed, what they read about, who they've investigated"
>
> — [3:22](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=202s) &middot; *Names both a number and the visibility problem it creates.*

> "80% of deals go to the buyers who are part of the pre-contact list."
>
> — [3:22](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=202s) &middot; *Sharpest single statistic supporting the late-stage-buyer argument.*

> "only 17% of the total buying time is spent talking with potential vendors. What all these numbers tell us is the buyers do their research thoroughly."
>
> — [3:22](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=202s) &middot; *Reports a number and draws the conclusion from it.*

> "But these are questions that actually move you backwards. They don't move you forward as an organization. The buyer has done their research and then some basic questions are asked to them. They're actually walking out of the system."
>
> — [5:05](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=305s) &middot; *Explains why generic AI chat greetings are actively harmful, not merely neutral.*

> "That's the power of social signals, and it's very important that these are captured, and not many companies leverage this in a automated, systematic way."
>
> — [7:23](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=443s) &middot; *Identifies job-change signals as an underexploited input.*

> "Everything that makes you successful sits in a knowledge base."
>
> — [8:08](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=488s) &middot; *Compact statement of the knowledge base's role as the system's source of truth.*

> "Without all these three layers running in tandem, the GTM model is still obsolete, is old school, and it's not set for the AI era that we are talking about."
>
> — [10:59](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=659s) &middot; *The all-or-nothing architectural claim others might dispute.*

> "The reason why a context graph is important is because without it, you don't know which account is a priority and which one is not."
>
> — [11:59](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=719s) &middot; *Ties the context graph abstraction to a concrete GTM outcome.*

> "I'm using more than one source here running together, and that's because no single tool catches every visitor."
>
> — [13:38](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=818s) &middot; *Concrete design decision: multi-vendor identification with dedupe.*

> "These tools change all the time for us, but not necessarily the architecture as such."
>
> — [13:38](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=818s) &middot; *Names the vendor-swappability tradeoff that justifies the layered design.*

> "You retrain your agents every quarter with your closed one or closed lost opportunities. And this is critical. Without this, your agents are looking at wrong information, pointing you to the wrong accounts and the wrong people."
>
> — [21:34](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1294s) &middot; *Gives a specific retraining cadence and its data source.*

> "If everything is flagged as hot to a sales rep, they would stop acting because it's it just gets overwhelming for them. And at that moment, they stop trusting the system and the system's dead."
>
> — [21:34](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1294s) &middot; *The alert-fatigue failure mode framed as a trust collapse.*

> "they're almost 70% or a little more than 70% accurate when it comes to company identification. They're only about 15 to 20% accurate when it comes to individual identification. And this is a structural limit"
>
> — [22:23](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1343s) &middot; *Rare hard accuracy numbers on de-anonymization tooling.*

> "If it's longer than 30 seconds, then this is a dead initiative because the sales would then rather focus on drafting their own email as opposed to trusting what the system gives them."
>
> — [23:55](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1435s) &middot; *A falsifiable adoption threshold for human-in-the-loop review.*

> "The second is the score fit and intent needs to be looked at separately. Conflating them is going to send the wrong message to the wrong person."
>
> — [24:38](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1478s) &middot; *A specific scoring-design position others commonly get wrong.*

> "you are able to control the system and fix it when needed. Because things do break quite frequently when it comes to AI and managing the output from AI."
>
> — [25:16](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1516s) &middot; *Argues GTM owners, not developers, should hold the debugging controls.*

> "every send, every reply, and every closed deal should make the model smarter, should make your system smarter"
>
> — [25:54](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1554s) &middot; *States the compounding-feedback closing thesis.*

## Positions

- Bolting AI onto an existing GTM stack is itself a hindrance to scale; the AI layer, the integration layer, and the underlying architecture must all be solved simultaneously. ([2:32](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=152s), confidence: stated)
- By the time a buyer contacts a vendor they are late-stage, not early-stage, because they have already researched and shortlisted. ([3:22](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=202s), confidence: stated)
- 94% of buyers use GenAI as primary research (Forrester 2026), 67% prefer a rep-free experience, 80% of deals go to vendors on the pre-contact list, and only 17% of buying time is spent with vendors. ([3:22](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=202s), confidence: stated)
- Generic chat openers like 'How can I help you?' move the buyer backwards and cause them to leave. ([5:05](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=305s), confidence: stated)
- LinkedIn job changes and engagement are high-value GTM signals that most companies fail to capture systematically; a departing exec sponsor should trigger adding their new company to the target account list. ([7:23](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=443s), confidence: stated)
- CRM updates must carry account-level context produced by the signals and intelligence layers, not just contact records from sales activity. ([10:59](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=659s), confidence: stated)
- Multiple identification vendors must be run in parallel and deduped because no single tool catches every visitor. ([13:38](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=818s), confidence: stated)
- Contacts failing ICP criteria (wrong industry, geo, size, persona) should be deleted rather than retained. ([14:25](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=865s), confidence: stated)
- Agents must be retrained quarterly on closed-won and closed-lost data or ICP drift will make them surface the wrong accounts. ([21:34](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1294s), confidence: stated)
- Current visitor identification platforms are ~70%+ accurate at company level and only 15–20% accurate at individual level, and this is a structural limit rather than a tuning problem. ([22:23](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1343s), confidence: stated)
- If editing an AI-drafted email takes longer than 30 seconds, reps will write their own and the initiative is dead. ([23:55](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1435s), confidence: stated)
- Fit score and intent score must be kept separate; conflating them sends the wrong message to the wrong person. ([24:38](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1478s), confidence: stated)
- The policy engine must be auditable and adjustable by GTM team members without developer involvement, because AI systems break frequently. ([25:16](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1516s), confidence: stated)
- Wins, losses, and deferred deals must feed back into the knowledge base so the system compounds over time. ([25:54](https://www.youtube.com/watch?v=ltv-L5oMPIs&t=1554s), confidence: stated)

## Concepts

- [automation bias](../concepts/automation-bias.md)
- [institutional knowledge capture](../concepts/institutional-knowledge-capture.md)
- [knowledge graph construction](../concepts/knowledge-graph-construction.md)
- [task decomposition](../concepts/task-decomposition.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

