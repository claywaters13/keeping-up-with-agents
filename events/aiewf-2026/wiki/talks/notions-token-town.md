---
title: "Notion's Token Town"
type: "talk"
slug: "notions-token-town"
track: "Software Factories"
org: "Notion"
day: "Day 2 — Session Day 1"
room: "Main Stage"
video_id: "-I5W5QVAT8E"
duration_sec: 1435
word_count: 4016
speakers: ["Sarah Sachs"]
---

# Notion's Token Town

**Speakers:** [Sarah Sachs](../speakers/sarah-sachs.md)

**Org:** Notion

**Track:** Software Factories &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Main Stage &nbsp;|&nbsp; **Duration:** 23m 55s

[Watch on YouTube](https://www.youtube.com/watch?v=-I5W5QVAT8E)

## Summary

Sarah Sachs, who leads Notion's AI engineering teams and negotiates its model contracts, argues that token economics — not model capability — is the structural barrier keeping most companies stuck at 'AI as an assistant.' Her core thesis is that your model supplier is also your competitor: you resell their tokens at a markup on top of their markup, so any margin you win on tokens is undefensible, and single-provider lock-in removes the leverage you need to survive monthly price and pricing-unit changes. Her prescribed playbook is model agnosticism (Notion's 'auto' model routes ~75% of traffic), serious use of open-weight models for moderate tasks, and pushing deterministic work onto CPUs rather than GPUs. She closes with what she thinks the next six months are actually about — security (the lethal trifecta) and multi-agent orchestration — demoing Notion routing a task across Claude, Codex, and Decagon agents inside a live document. Worth watching if you buy AI capability wholesale and need a concrete vendor-negotiation and routing posture; skip if you're looking for model-training or capability content.

## Key Points

- Cost, not capability, is the main reason AI systems fail to reach production scale — 88% of companies, by her figure, can't get past AI-as-assistant.
- Your model provider is simultaneously your competitor: they serve a first-party product at their true cost of goods while you buy the same tokens at a surcharge and resell at another, which is not a defensible position.
- Price changes arrive in disguised forms — same per-token price but 3x more output tokens from a reasoning upgrade, or a new model tier at 40% more with the predecessor deprecated in four months — and your revenue is not growing to match.
- Optionality is the real leverage: without the ability to walk away from a provider, no negotiated discount is worth it, and locking to one lab means shipping a non-frontier product roughly half the time as leadership rotates between labs.
- Frontier model pricing behaves like the gas-station clustering effect — the second-best model only needs to be a dollar per million tokens cheaper — so price does not correlate with capability growth.
- Not all traffic deserves the frontier model: large-scale data analysis may warrant Opus, but billing a customer at Opus rates to triage an email inbox rips off both the customer and yourself.
- Open-weight models are now strong enough for moderate tasks without RL, act as credible downward pressure on an oligopoly of two or three top providers, and will likely cover today's tasks within six months.
- A great deal of agent work needs no LLM at all — CSV-to-PDF conversion, CLI tool calls, deterministic SQL — and routing those to GPUs is how teams go token-poor fast.
- Evaluate on whole trajectories and cost-per-capability-per-second rather than single-call latency or price; Notion chose Parallel for web search on trajectory-level evals even though it isn't cheapest per call.
- Eval-program partnerships and use-case expertise are tradeable currency with frontier labs — an alternative to signing extraordinarily large compute commits.

## Notable Quotes

> "Um, your supplier is your competitor. I know very few people who have convinced me that that's not true."
>
> — [7:35](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=455s) &middot; *The talk's thesis in one line, stated as a position she's defended repeatedly.*

> "And if you tie yourself to one provider, you have no exit. If you build an AI product that you're selling with this structure, you are crossing your fingers and hoping that you are a viable business. I do not encourage that."
>
> — [7:35](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=455s) &middot; *Frames vendor lock-in as an existential business risk, not an engineering preference.*

> "We have found that no one has figured out how to do this well. 88% of people can't even get past AI as an assistant."
>
> — [3:40](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=220s) &middot; *The one hard adoption number motivating the whole talk.*

> "Cost is a structural barrier to entry. It makes it hard for you to serve products. It makes it hard for you to build factories."
>
> — [4:55](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=295s) &middot; *States the central claim that economics, not capability, is the bottleneck.*

> "A reasoning model gets upgraded. Amazing. The per token pricing is the same. What's not to love, you try it out, it uses three times as many output tokens, right?"
>
> — [5:34](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=334s) &middot; *Concrete mechanism for hidden price increases that per-token comparisons miss.*

> "A model gets upgraded, but it has an entire new digit, right? Whatever demarcation system that model family likes, it's brand new. It's 40% more than its predecessor, which is being deprecated in the next four months."
>
> — [5:34](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=334s) &middot; *Names the forced-migration pricing pattern with specific numbers.*

> "Are you growing 40% in that time period? Are you making 30 3x more revenue? No."
>
> — [6:13](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=373s) &middot; *The rhetorical pivot showing why auto-upgrading models breaks unit economics.*

> "Help your customers, help your team. Bet on the frontier, not on the lab. and we'll talk about what it looks like to do that."
>
> — [9:34](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=574s) &middot; *The talk's memorable formulation of model agnosticism.*

> "And not all traffic is equal. It is a huge miss to send all of these to the latest opus model."
>
> — [10:19](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=619s) &middot; *Core routing argument stated bluntly.*

> "When you triage an email inbox, if we're charging you to do that on Opus, we're ripping you off and ourselves."
>
> — [10:19](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=619s) &middot; *Rare example of a vendor framing over-provisioned model choice as harming the customer.*

> "You know that economic theory about gas stations where the best gas stations are the ones that are right next to each other because they cover east and west the most. Yeah. It's the same with model pricing, which means that price does not correlate with capability growth."
>
> — [11:34](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=694s) &middot; *A crisp economic model of why frontier pricing clusters, ending in a checkable claim.*

> "oftentimes you'll see applied AI companies really be super outspoken on marketing with a specific lab. That's always kind of a red flag for me when they're not model agnostic"
>
> — [11:34](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=694s) &middot; *Takes a contrarian side against the common exclusive-lab-partnership marketing play.*

> "remember that that optionality is your leverage if you don't have the capability to walk at any point you are stuck"
>
> — [12:17](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=737s) &middot; *States the negotiating principle underlying her whole procurement stance.*

> "We have the ability to switch between models in our product and we also offer it to our customers so that they have access to these models without vendor lockin. That's part of our AI Switzerland approach."
>
> — [13:03](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=783s) &middot; *Names Notion's positioning and shows agnosticism as a product feature, not just procurement.*

> "The granularity of this eval is what lets us make the best decisions for our customers because we understand all of the trade-offs on entire trajectories, not just single calls."
>
> — [14:23](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=863s) &middot; *Names the tradeoff between per-call and trajectory-level evaluation.*

> "I view openw weight models as basically lowering the barrier to entry on cost for our customers and they also give you negotiation leverage."
>
> — [15:04](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=904s) &middot; *Frames open weights primarily as pricing leverage rather than as a technical choice.*

> "the gap gets covered eventually. So, if the tasks that you're having today are good enough, then in six months, they're probably covered by open weight. So, be prepared now."
>
> — [16:37](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=997s) &middot; *A falsifiable six-month prediction about open-weight catch-up.*

> "Like you don't need an LLM to turn a CSV into a PDF. You don't need an LLM to talk to notion tool calls if we have a CLI. You definitely don't need an LLM to do deterministic SQL queries. This is where people become token poor very quick."
>
> — [17:14](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=1034s) &middot; *The most actionable cost lever in the talk, stated with concrete examples.*

> "So I think the challenge of the next six months doesn't have to do with capabilities. I think it has to do with security."
>
> — [17:57](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=1077s) &middot; *A clear forward-looking bet that many capability-focused talks would contest.*

> "It's like actually your entire engineering time just spends time babysitting the factory, right? I mean, I get it. Ours started off like this. Agent orchestration is one of the most difficult tasks of making factories work."
>
> — [19:22](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=1162s) &middot; *Honest admission about where software-factory workflows actually are today.*

## Positions

- Model providers are structurally competitors to the applied AI companies that buy from them, because they serve first-party products at cost while resellers stack surcharges. ([7:35](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=455s), confidence: stated)
- No volume discount is worth the loss of optionality that comes with committing to a single model provider. ([14:23](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=863s), confidence: stated)
- Frontier model price does not correlate with capability growth, because the second-best model only needs to undercut the leader slightly to capture the rest of the market. ([11:34](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=694s), confidence: stated)
- 88% of companies cannot get past using AI as an assistant, and the cause is siloed data and the lack of a durable system of record. ([3:40](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=220s), confidence: stated)
- Notion's auto model handles about 75% of its AI traffic. ([13:03](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=783s), confidence: stated)
- Applied AI companies should not try to win on token economics or on training their own frontier models; they should win on product, data flywheels, UI, and orchestration. ([8:57](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=537s), confidence: stated)
- Open-weight models are now capable enough for moderate tasks without requiring RL on top, and are no longer limited to SFT on small tasks. ([15:46](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=946s), confidence: stated)
- Tasks that open-weight models nearly handle today will likely be fully covered by open weights within six months. ([16:37](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=997s), confidence: stated)
- A large share of agent workloads — file conversion, tool calls behind a CLI, deterministic SQL — should run on CPUs without any LLM in the loop. ([17:14](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=1034s), confidence: stated)
- The binding constraint over the next six months is security rather than model capability, and autonomy amplifies lethal-trifecta exposure because the risk goes unsupervised. ([17:57](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=1077s), confidence: stated)
- Public marketing exclusivity with a single lab is a warning sign that a company is shipping a non-frontier product a large fraction of the time. ([11:34](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=694s), confidence: stated)
- Selecting vendors on single-call cost or latency leads to worse decisions than evaluating whole trajectories, as with Notion's choice of Parallel for web search despite it not being cheapest. ([13:46](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=826s), confidence: stated)
- Eval-program partnerships and use-case expertise can substitute for very large spend commitments as currency in frontier lab negotiations. ([14:23](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=863s), confidence: stated)
- Notion's internal software factory saves over three minutes on a given task, with similar ROI reported by customers. ([22:10](https://www.youtube.com/watch?v=-I5W5QVAT8E&t=1330s), confidence: stated)

## Concepts

- [ai governance and compliance](../concepts/ai-governance-and-compliance.md)
- [deterministic versus probabilistic system design](../concepts/deterministic-versus-probabilistic-system-design.md)
- [inference cost optimization](../concepts/inference-cost-optimization.md)
- [model portability](../concepts/model-portability.md)
- [model routing](../concepts/model-routing.md)
- [multi-agent orchestration](../concepts/multi-agent-orchestration.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [trajectory evaluation](../concepts/trajectory-evaluation.md)

