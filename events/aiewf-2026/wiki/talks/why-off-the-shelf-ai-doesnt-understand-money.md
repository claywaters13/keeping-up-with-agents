---
title: "Why Off-the-Shelf AI Doesn't Understand Money"
type: "talk"
slug: "why-off-the-shelf-ai-doesnt-understand-money"
track: "AI in Finance"
org: "Intuit"
day: "Day 4 — Session Day 3"
room: "Track 3"
video_id: "Owb8g3yDyzo"
duration_sec: 1190
word_count: 2841
speakers: ["Udi Menkes"]
---

# Why Off-the-Shelf AI Doesn't Understand Money

**Speakers:** [Udi Menkes](../speakers/udi-menkes.md)

**Org:** Intuit

**Track:** AI in Finance &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 19m 50s

[Watch on YouTube](https://www.youtube.com/watch?v=Owb8g3yDyzo)

## Summary

Udi Menkes, a principal product manager at Intuit, argues that frontier LLMs give confident but often harmful financial advice because they have read about money rather than observed what actually worked. He opens with real cases from an Intuit study of ~100,000 business situations: a cash-flow-negative landlord told to buy a second property, and an egg supplier with 70% customer concentration told to raise prices 15-20%. His counter is 'grounding in real outcomes' — mining millions of state/action/outcome trajectories from QuickBooks, TurboTax, Credit Karma and Mailchimp data, using causal inference (CATE) to isolate the true effect of actions, and training an RL model plus an LLM on that signal. He reports that a mid-size, cheaper grounded model beat frontier models head-to-head, and cites Princeton research where most frontier models drove a simulated business bankrupt while a simple rules-based system outperformed them. The broader claim: the moat in outcome-driven AI is your system of record and verified outcomes, not model access — which generalizes beyond finance to health care, logistics, and fraud.

## Key Points

- Frontier LLMs produce what Menkes calls 'the fluent bluff' — generic, confident financial advice learned from internet writing about money rather than from observed outcomes, and it persists even when the model is given all of a company's financial data.
- In Intuit's study across roughly 100,000 business situations, 40% of frontier-model advice reduced to 'acquire a new customer' and another 14% to 'increase revenue from your product' — over half the advice collapsing into two generic moves.
- Two concrete failures illustrate the risk: advising a cash-flow-negative first-time landlord to buy a second property, and advising an egg supplier whose single customer is 70% of revenue to raise prices 15-20%.
- A Princeton simulation gave models a harness, tools, data and $1M over 500 simulated days; most drove the company bankrupt, and a simple rules-based system beat almost all of them.
- Measuring experience requires causal inference, not raw correlation: businesses that raise prices are naturally more successful, so the naive $1,400/day gap must be adjusted (to ~$1,150 in his illustration) using conditional average treatment effect on matched-propensity groups.
- Intuit's pipeline builds millions of business trajectories — state, action, outcome vectors derived from the general ledger, P&L, cash flow and invoices — trains an RL model to score which actions lead to good outcomes, then trains an LLM to generate the advice.
- Frontier models still have a role in the stack: they generate hypothesis candidates, and the RL-trained grounded model decides which candidates are actually right.
- A mid-size, cheaper grounded model outperformed leading frontier models head-to-head, supporting the claim that the moat is proprietary outcome data rather than model size or model access.
- Menkes generalizes to 'outcome-driven AI': coding agents already have verified outcomes and are advanced, finance and other domains are unexplored, and winners will be those with the best systems of record.
- A trustworthy advisory product needs both grounded science and personalization — understanding user preferences and making the user feel part of the decision.

## Notable Quotes

> "who uses LLMs, has used LLMs for getting financial advice, a recommendation on something in the financial world. Great. Almost everyone. Wait, keep your hand up if you trusted the answer and you actually followed the advice. Okay. a lot of hands are going down and that's the core problem."
>
> — [0:46](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=46s) &middot; *The live audience poll that frames the entire trust gap the talk is about.*

> "I changed just a little bit, one of the assumptions, and it completely flipped. You should do B, never do A. And then I tweaked one more small thing, and it went all the way back to A."
>
> — [1:39](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=99s) &middot; *Concrete demonstration of advice instability under small perturbations.*

> "at that moment, I understood that the advice sounds good. It sounds sound, but I can't really trust it."
>
> — [1:39](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=99s) &middot; *States the sounding-right vs being-right distinction that structures the talk.*

> "And a frontier model gives the following response. Go and acquire a second rental property because that'll bring more income and compensate for the deficit."
>
> — [2:26](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=146s) &middot; *The first concrete example of dangerous frontier-model financial advice.*

> "a model that is grounded in real outcomes and what I mean by that is a model that has seen similar situations of such businesses what they did and what was the outcome actually recommended to raise prices on the existing tenant by 5 to 10%."
>
> — [3:13](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=193s) &middot; *Defines 'grounded in real outcomes' and shows the contrasting recommendation.*

> "This is an egg supplier where one customer is 70% of the revenue and one vendor is almost all of its cost. Same question, how do I improve my profit? A frontier model says raise your prices 15 to 20%."
>
> — [4:07](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=247s) &middot; *Second failure case with the concentration numbers that make the advice risky.*

> "The fluent bluff is a generic fluent and confident answer that frontier LLMs can give you around money because of what they learned on the internet, blogs, books, advice columns, what people wrote about money, but not based on what actually happened."
>
> — [4:53](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=293s) &middot; *The talk's coined term, defined precisely.*

> "across these 100,000 businesses in time frames 40% of the time the essence of the advice that the frontier models were giving was acquire a new customer"
>
> — [4:53](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=293s) &middot; *The headline number from the unreleased Intuit study.*

> "Each model got a million dollars to start with and guess what happened? Most of the models drove the company bankrupt and it didn't even take 500 days."
>
> — [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s) &middot; *Reports the Princeton long-horizon business simulation result.*

> "they also ran a simple rules-based system and that rules-based system outbeat almost all of the models."
>
> — [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s) &middot; *The most provocative external evidence against frontier models on business decisions.*

> "A frontier model has read about money, but a grounded model in real outcome has actually watched what happens."
>
> — [7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s) &middot; *The talk's central one-line thesis.*

> "you give it to a frontier LLM it's still just one group of data points on a company and that's a difference between sounding right and actually being right"
>
> — [8:06](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=486s) &middot; *Preempts the 'just add more context' objection.*

> "the question that I fixate on on a daily basis is not which model is the best now that I I can use. It's what do we fundamentally have that no model access can replicate"
>
> — [9:02](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=542s) &middot; *Frames the strategic question for anyone building on top of frontier models.*

> "That same vendor was actually enabling the generation of 97% of that company's revenue. So cut that biggest cost and you lose almost all the revenue. And that can be great margins on zero dollars."
>
> — [9:57](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=597s) &middot; *Memorable illustration that textbook answers ignore structural constraints.*

> "the group that raised prices actually gained $4,200 a day profit. And the group that didn't raise prices actually gained $2,800 a day."
>
> — [11:34](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=694s) &middot; *The numbers behind the causal-inference walkthrough.*

> "you need to account for the fact that the companies that raise prices are actually naturally more successful businesses, which is also why they could raise the prices. So, the real difference is more like $1,150 for this illustration."
>
> — [11:34](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=694s) &middot; *Explains selection bias and the corrected treatment effect concretely.*

> "find where you can see a lot of different situations across entities that you have in your data. In our case, it's businesses what they did and verify the outcomes and how things turned out. If you can see that in the data because that's the one thing that Frontier off-the-shelf models do not have."
>
> — [12:19](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=739s) &middot; *The actionable heuristic he asks practitioners to apply in their own domain.*

> "we use them to generate hypothesis candidates for actions we would suggest a business to do. But then we would use a model that we trained using reinforcement learning in order to figure out which one of those is actually a right move to do versus a mistake that could drive the business down."
>
> — [13:05](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=785s) &middot; *Describes the hybrid architecture, showing this isn't an anti-frontier-model talk.*

> "we were able with a midsize cheaper model to outperform the frontier models because of the grounding that I just showed you."
>
> — [15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s) &middot; *The core empirical claim of the whole approach.*

> "the moat here is that it's not about the model access, it's about the data itself that you have."
>
> — [15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s) &middot; *States the strategic takeaway in one sentence.*

> "The winners in my opinion are going to be those with the best system of records, creating unique data sets out of them and then training the models to achieve the outcomes."
>
> — [17:00](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=1020s) &middot; *Generalizes the thesis beyond finance into a market prediction.*

> "in coding agents and coding models, we're seeing it very advanced. A lot of verified outcomes and creating models that actually lead to better outcomes in coding, but it's very much unexplored in the financial domain and in other domains as well."
>
> — [17:51](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=1071s) &middot; *Explains why coding is ahead and positions finance as the next frontier.*

> "you don't close the gap with bigger models. You close the gap with experience, embedding experience into the model by looking at verified outcomes in your data."
>
> — [17:51](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=1071s) &middot; *Directly rejects scale as the solution — the talk's most contestable position.*

## Positions

- Frontier LLMs give financial advice that sounds sound but is often harmful, even when given all of a business's financial data. ([4:53](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=293s), confidence: stated)
- Giving a model more context is not a substitute for grounding in observed outcomes — a company's full financial data is still just one group of data points. ([8:06](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=486s), confidence: stated)
- In an Intuit study across ~100,000 business situations, over half of frontier-model advice reduced to 'acquire new customers' or 'increase revenue from your product' (40% + 14%). ([4:53](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=293s), confidence: stated)
- In the Princeton 500-day business simulation, most frontier models drove the company bankrupt and a simple rules-based system outperformed almost all of them. ([7:04](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=424s), confidence: stated)
- A mid-size, cheaper model grounded in outcome data outperformed leading frontier models head-to-head on business advice. ([15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s), confidence: stated)
- Model size and model access are not the competitive moat; proprietary outcome data is. ([15:21](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=921s), confidence: stated)
- Measuring the impact of a business action requires adjusting for selection bias, because firms that take an action are systematically different from those that don't. ([11:34](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=694s), confidence: stated)
- Frontier models are still valuable as hypothesis generators, with a separately trained RL model acting as the selector. ([13:05](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=785s), confidence: stated)
- Coding is the domain where outcome-verified model training is most advanced, while finance and other domains remain largely unexplored. ([17:51](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=1071s), confidence: stated)
- The outcome-grounding approach generalizes beyond finance to anti-fraud, health care, logistics, and developer tools. ([16:10](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=970s), confidence: stated)
- A trustworthy AI advisory product requires personalization and user participation in the decision, not just accurate science. ([17:00](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=1020s), confidence: stated)
- Scaling to bigger models will not close the gap between reading about a domain and having experience in it. ([17:51](https://www.youtube.com/watch?v=Owb8g3yDyzo&t=1071s), confidence: stated)

## Concepts

- [agentic science](../concepts/agentic-science.md)
- [data flywheels](../concepts/data-flywheels.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [semantic layer](../concepts/semantic-layer.md)
- [small language models](../concepts/small-language-models.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

