---
title: "Trading Desks to Clinical Trials: Parallels in Applied Vertical AI"
type: "talk"
slug: "trading-desks-to-clinical-trials-parallels-in-applied-vertical-ai"
track: "AI in Healthcare"
org: "Allos AI"
day: "Day 4 — Session Day 3"
room: "Track 7"
video_id: "Yphdry8ttAQ"
duration_sec: 1201
word_count: 3748
speakers: ["Ayush Bhardwaj"]
---

# Trading Desks to Clinical Trials: Parallels in Applied Vertical AI

**Speakers:** [Ayush Bhardwaj](../speakers/ayush-bhardwaj.md)

**Org:** Allos AI

**Track:** AI in Healthcare &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 20m 01s

[Watch on YouTube](https://www.youtube.com/watch?v=Yphdry8ttAQ)

## Summary

Ayush Bhardwaj, who moved from applied AI at a hedge fund to a pharma-tech startup, argues that building vertical AI is essentially the same job across radically different industries, and lays out a seven-step recipe: narrow the problem, source proprietary data, write the prompt as a model of the expert's reasoning, add observability, then — critically — stop and hire the domain expert before you iterate. His central claim is that the engineering half is commodity (the agent code 'fits one screen'), so the only durable moat is proprietary data and encoded domain judgment, neither of which OpenAI or Anthropic can have because regulation and incentives keep it off the internet: hedge funds hide trade theses, and roughly a third of pharma sponsors never disclose failed trials. He is blunt that engineers cannot self-evaluate outputs in fields they don't understand, and that trying to LLM-as-judge your way out is a mistake because the model can only jargon convincingly. Worth watching if you're building for a regulated or expert-gated vertical and want a candid account of why demos die before they sell.

## Key Points

- The right question about agents in production is not whether they ship but whether they justify their ROI — in finance and pharma an agent that doesn't make or save money is killed immediately, not given two years to improve.
- Formulate an extremely narrow task per agent rather than one general one: pick the market, then the industry, then the specific ranking criterion, and build as many agents as you need since there's no cost to having more.
- Proprietary data is the only real differentiator, and the highest-value examples are the negative results — trade theses explaining what worked and why, and pharma's failed-experiment data — precisely because those are the hardest to buy.
- The first four steps (problem, data, prompt, observability) are the easy part and fit on one screen of code, which is why they cannot be the moat.
- Engineers cannot judge vertical AI output because they lack the trained mental model — you can instantly tell a bad coding model, but not a bad trade thesis — and this is where vertical AI projects quietly die.
- LLM-as-judge fails in these domains because RLVR-style verification works where there are answer keys (math, code) and there are none for alpha or drug candidates; errors then compound.
- The unavoidable step is hiring the user you intend to sell to; at the pharma startup, hiring a senior scientist changed the trajectory of the tools and made big-pharma buyers respond because the output spoke their language.
- Rank improvement techniques by ROI: error analysis on observability logs first (no weights touched), then rubrics-as-rewards (watch for echo chambers), then SFT and RLHF, keeping in mind that fine-tuning must be redone with every new base model.
- Human-in-the-loop understates it for these fields — it's AI-in-the-loop, where the expert still makes the call and the agent only compresses the time to generate candidates.

## Notable Quotes

> "The question to ask is whether they actually work, whether they actually make or save money, whether they justify their ROI"
>
> — [3:02](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=182s) &middot; *Reframes the standard 'are agents in production' conference question into an economic one.*

> "you need to pick a very narrow task. You just cannot ask it to do everything."
>
> — [3:41](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=221s) &middot; *The core scoping prescription, stated as a flat rule.*

> "Last I checked, there was no tax on building more AI agents. So, why do you want your single agent to do everything?"
>
> — [4:21](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=261s) &middot; *Memorable argument for decomposition over monolithic agents.*

> "But what actually makes your application better than let's say ChatGPT or Claude? It is your proprietary data."
>
> — [4:58](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=298s) &middot; *States the differentiation thesis directly against frontier general models.*

> "So, to give you a great example of the proprietary data that finance industry has, it's the trade thesis, which is like what trade work and why it worked. And in pharma, it is the data for failed experiments."
>
> — [5:34](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=334s) &middot; *Names the specific asset class of data that matters in each vertical.*

> "The mythical 10x engineers can do this stuff in minutes. Like literally, this is the code you precisely need to build an AI agent. So, that's why it's not the moat."
>
> — [6:48](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=408s) &middot; *The talk's pivot: engineering effort is commodity, so it can't be the defensible part.*

> "I could build it, but I just could not tell if it worked cuz I'm not a trader. I'm not someone who has a PhD in biology or chemistry."
>
> — [7:25](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=445s) &middot; *Personal admission that sets up the entire evaluation problem.*

> "And this is also the place where like a lot of vertical AI projects quietly die because on the surface it looks like you have made it, you have built it, let's put this into production and start selling it."
>
> — [8:04](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=484s) &middot; *Diagnoses the specific failure mode of vertical AI startups.*

> "And this was a really, really stupid mistake to be honest cuz what LLM is essentially doing, it's it's predicting the next probable word."
>
> — [8:43](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=523s) &middot; *Direct repudiation of LLM-as-judge in expert domains, from someone who tried it.*

> "first thing is that model cannot verify itself, specifically in these fields, because reinforcement learning via verifiable rewards is really good at math and code because you have like answer keys"
>
> — [9:20](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=560s) &middot; *Gives the technical reason self-evaluation transfers to code but not to finance or pharma.*

> "any institutional manager holding over $100 million in qualifying US equities are forced to publicly file their holdings, long position holdings, every quarter"
>
> — [9:59](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=599s) &middot; *Concrete regulatory detail explaining why the valuable finance data stays hidden.*

> "by law, you are like required to disclose every clinical trial pass or failure you have done. But, 30% of the funds, which is like nearly 1/3 of firms, never do."
>
> — [10:47](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=647s) &middot; *Reports the number behind the claim that failed-trial data is missing from public corpora.*

> "You just cannot hire a trader for $100 an hour and have them annotate that stuff because there's like lots of NDAs and they definitely earn more."
>
> — [11:25](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=685s) &middot; *Explains why the labor-market fix for expert data doesn't work in these verticals.*

> "you hire the person who you want to sell it to cuz there is, to be honest, no other way around. I have tried a lot of stuff."
>
> — [11:25](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=685s) &middot; *The talk's central operational prescription, stated without hedging.*

> "And then we hired someone, right? And that someone actually changed the trajectory of our tools. Our tools started making sense."
>
> — [12:02](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=722s) &middot; *Evidence from his own company that the expert hire was the inflection point.*

> "And the cheapest of all, and I think the highest ROI is the error analysis. Whereas the observability part that you set up earlier, you just analyze the logs plain and simple."
>
> — [14:33](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=873s) &middot; *Ranks the improvement techniques and puts the cheapest one first.*

> "89% of enterprise AI agents never reach production. Again, I disagree. Every AI reaches production, but it just fails to work or like justify its own cost."
>
> — [16:20](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=980s) &middot; *Challenges a widely cited statistic and restates the failure as economic, not technical.*

> "And finance and pharma are two such industries where if it does not make money, it's shown the door. Simple."
>
> — [16:20](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=980s) &middot; *Sets the evaluation bar these verticals actually apply.*

> "Finance and pharma are still those two industries where it's AITL, AI in the loop cuz everything is like done by the expert, but the AI assistant really helps save time."
>
> — [17:41](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=1061s) &middot; *Inverts the standard human-in-the-loop framing for high-stakes verticals.*

> "for the models to actually make good decisions, they don't need to do correlation, they need to do causation"
>
> — [18:25](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=1105s) &middot; *States the capability gap he believes blocks full automation.*

> "Model infra ecosystem, everyone selling you tons of stuff at this conference is just commodity. Everyone has it. If you have it, everyone has it."
>
> — [19:07](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=1147s) &middot; *The single takeaway he asks the audience to keep, aimed squarely at the vendor floor.*

## Positions

- The core work of applied AI is essentially identical across verticals — moving from a hedge fund to pharma changed the domain but not the engineering method. ([2:26](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=146s), confidence: stated)
- 'Are people putting agents into production?' is the wrong question; everyone ships agents, and the real question is whether they justify their cost. ([3:02](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=182s), confidence: stated)
- Startups fail by asking a single agent to do too much; you should build many narrowly scoped agents instead. ([3:41](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=221s), confidence: stated)
- Most organizations already hold the proprietary data they need in unstructured form, and an LLM workflow can structure it overnight. ([5:34](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=334s), confidence: stated)
- The prompt should encode the step-by-step mental model of the human whose job the agent simulates. ([6:12](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=372s), confidence: stated)
- The agent scaffolding — prompts, data plumbing, observability — is not a moat because it fits on one screen and any strong engineer can reproduce it. ([6:48](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=408s), confidence: stated)
- You should not begin iterating until you have hired a domain expert, because engineers cannot tell whether vertical output is good. ([7:25](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=445s), confidence: stated)
- LLM-as-judge does not work in finance and pharma because the model produces plausible jargon without understanding concepts like alpha. ([9:20](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=560s), confidence: stated)
- Models cannot verify themselves in these fields because there are no answer keys, unlike math and code where RLVR works well. ([9:20](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=560s), confidence: stated)
- 13F-style quarterly disclosure measurably reduces hedge fund returns because competitors reverse-engineer the positions. ([9:59](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=599s), confidence: stated)
- About 30% of pharma sponsors never disclose clinical trial results despite legal requirements, and in 2026 the FDA publicly reminded roughly 2,000 sponsors. ([10:47](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=647s), confidence: stated)
- Neither OpenAI nor Anthropic has this gatekept vertical data, and it cannot be cheaply acquired through annotation labor because of NDAs and expert pay. ([11:25](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=685s), confidence: stated)
- The domain expert should participate across the whole stack — query scoping, source curation, problem decomposition, and final judgment — turning their judgment into the agent. ([12:38](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=758s), confidence: stated)
- Rubrics-as-rewards risks creating an echo chamber where the AI grades itself into agreement. ([14:33](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=873s), confidence: stated)
- Error analysis over observability logs is the cheapest and highest-ROI improvement method and should precede any weight-touching technique. ([14:33](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=873s), confidence: stated)
- RLHF is the current gold standard for gaining an edge, but fine-tuning carries recurring cost because each new base model release forces you to redo it. ([15:11](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=911s), confidence: stated)
- The expert-in-the-loop exercise itself generates a valuable proprietary dataset of what works and what doesn't. ([15:46](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=946s), confidence: stated)
- The Stanford AI Index figure that 89% of enterprise AI agents never reach production is wrong in framing — they reach production and fail to justify their cost. ([16:20](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=980s), confidence: stated)
- Human-in-the-loop is premature for finance and pharma; the correct model today is AI-in-the-loop, where the expert decides and AI compresses their time. ([17:41](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=1061s), confidence: stated)
- Current models are text statistics rather than world models, so they cannot do the causal reasoning these decisions require until some future AGI threshold. ([18:25](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=1105s), confidence: stated)
- Models, infrastructure, and the tooling ecosystem are commodities; domain expertise and non-public data are the only moat. ([19:07](https://www.youtube.com/watch?v=Yphdry8ttAQ&t=1147s), confidence: stated)

## Concepts

- [agent observability and tracing](../concepts/agent-observability-and-tracing.md)
- [data flywheels](../concepts/data-flywheels.md)
- [error analysis and failure taxonomy](../concepts/error-analysis-and-failure-taxonomy.md)
- [human annotation and labeling](../concepts/human-annotation-and-labeling.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [post-training](../concepts/post-training.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [rlhf and preference training](../concepts/rlhf-and-preference-training.md)
- [roi measurement](../concepts/roi-measurement.md)
- [rubric design](../concepts/rubric-design.md)
- [task decomposition](../concepts/task-decomposition.md)
- [vertical domain agents](../concepts/vertical-domain-agents.md)

