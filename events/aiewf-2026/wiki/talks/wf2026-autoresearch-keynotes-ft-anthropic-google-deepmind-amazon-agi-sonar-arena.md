---
title: "WF2026: Autoresearch & Keynotes ft. Anthropic, Google DeepMind, Amazon AGI, Sonar, Arena, Recursive"
type: "talk"
slug: "wf2026-autoresearch-keynotes-ft-anthropic-google-deepmind-amazon-agi-sonar-arena"
video_id: "4sX_He5c4sI"
duration_sec: 31915
word_count: 82678
speakers: []
---

# WF2026: Autoresearch & Keynotes ft. Anthropic, Google DeepMind, Amazon AGI, Sonar, Arena, Recursive

**Speakers:** unknown / not credited

**Duration:** 8h 51m

[Watch on YouTube](https://www.youtube.com/watch?v=4sX_He5c4sI)

## Summary

This is the day-two keynote block of AI Engineer World's Fair 2026, stitching together short talks from Anthropic, Sonar, Amazon AGI, Google DeepMind, Arize, Meta, Jina/Elastic, Prime Intellect, GEPA/Databricks-adjacent researchers, Artificial Analysis, Arena, and a dozen startups. The through-line is that model capability has outrun our ability to verify and manage it: Anthropic's Tariq Shihipar argues the new 'mythos-class' models (Fable) need smaller system prompts and better-specified unknowns rather than more constraints, while Sonar, Amazon AGI, and Google DeepMind all converge on verification as the real bottleneck — coding got reliable first only because code is checkable, and most knowledge work has no unit test. The second half is dominated by auto research: multiple teams report agents beating human leaderboards on nanoGPT speedruns, CUDA kernels, and parameter-golf competitions, but consistently through recombination of existing ideas rather than novel invention. Closing talks from Addy Osmani, Artificial Analysis, and Arena reframe the economics and the human role — token prices fall 5–10x/year at fixed intelligence while cost-per-task climbs past $20, input tokens and cache hit rates dominate agentic spend, and the scarce resource becomes judgment backed by evidence. Watch it if you want a dense cross-section of where verification, evals, and auto research stood in mid-2026; skip to individual segments, since it's 9 hours of ~15-minute talks.

## Key Points

- Anthropic reports that the newest model generation inverts prior prompting best practice: they removed 80% of Claude Code's system prompt because examples now constrain a model that is more imaginative than the examples given to it.
- Sonar's reading of METR data is that coding agents reach 16–18 hour task horizons only at a 50% success rate; dial accuracy to 80% and the horizon collapses to about 3.5 hours, which is still below enterprise-grade reliability.
- A Carnegie Mellon study cited on stage shows the 3–5x velocity boost from AI coding agents dissipates within three months as security, maintainability, reliability, and complexity debt accumulate — customers running multi-layered verification report 44% fewer AI-derived production outages.
- Amazon AGI's argument is that coding became trustworthy first because it is verifiable, and that the open frontier is reliability for unverifiable knowledge work — their proposed answer is 'perception agents' that read the rendered screen to confirm their own output, released as open-source annotation and verification tools.
- Google DeepMind's Benoit Schillings claims roughly 80% of new GitHub code is machine-generated, so human code as training data is exhausted and self-play is the next scaling axis; he predicts within a year generated code will ship largely unread and suggests designing new, strongly-typed, non-human-readable languages for models.
- Multiple auto research talks (Prime Intellect, Weco, kernel optimization) report agents setting leaderboard records — seven parameter-golf records, sub-record nanoGPT optimizer runs, better-than-leaderboard CUDA kernels — but consistently find the agents combine existing papers and ideas rather than inventing novel mechanisms.
- Evaluation talks converge on the same shift: Arize argues classical LLM-as-a-judge cannot score non-deterministic agent trajectories and proposes agent-as-a-judge; Meta argues production telemetry, not offline benchmarks, is the highest-value eval signal because benchmarks measure model capability while production measures system behavior.
- Artificial Analysis quantifies the cost paradox: token prices fall 5–10x per year at each fixed intelligence level and open-weights models trail the frontier by a consistent 3–9 months, yet cost-per-task now exceeds $20 on agentic knowledge work, with input tokens and cache-hit pricing — not output tokens — dominating the bill.

## Notable Quotes

> "I think something we say really often is that the models are grown not designed"
>
> — [18:51](https://www.youtube.com/watch?v=4sX_He5c4sI&t=1131s) &middot; *Frames Anthropic's whole 'field guide' posture — empirical discovery over specification.*

> "we recently removed 80% of the system prompt for cloud code"
>
> — [22:09](https://www.youtube.com/watch?v=4sX_He5c4sI&t=1329s) &middot; *A concrete, reversible engineering number that contradicts common prompt-engineering practice.*

> "most recently we found this new class of models want fewer want a smaller system prompt the examples tend to constrain it because it's actually more imaginative than the examples we give it"
>
> — [22:09](https://www.youtube.com/watch?v=4sX_He5c4sI&t=1329s) &middot; *States the tradeoff explicitly: examples now cost capability rather than adding it.*

> "one of my favorite parts of anthropic is that we believe that trade-offs are not real"
>
> — [32:45](https://www.youtube.com/watch?v=4sX_He5c4sI&t=1965s) &middot; *The talk's cultural thesis, and the most contestable claim in it.*

> "I think the only way to prove that agents work is to do the best work of our lives faster than ever before"
>
> — [33:22](https://www.youtube.com/watch?v=4sX_He5c4sI&t=2002s) &middot; *Sets a burden of proof on the audience rather than on the models.*

> "building is easier, but generating value is still hard"
>
> — [34:41](https://www.youtube.com/watch?v=4sX_He5c4sI&t=2081s) &middot; *The bridge between the Anthropic talk and every enterprise talk that follows.*

> "But the critical caveat when you read the data is this is at a 50% success rate."
>
> — [39:28](https://www.youtube.com/watch?v=4sX_He5c4sI&t=2368s) &middot; *The single most-cited caveat about METR-style task-horizon curves.*

> "So essentially you're building the technical debt as quickly as you are generating the code or maybe even more quickly and that creates a different set of work."
>
> — [42:36](https://www.youtube.com/watch?v=4sX_He5c4sI&t=2556s) &middot; *Explains the mechanism behind the three-month productivity decay.*

> "they are reporting AI derived production outages being 44% less frequent than the ones who do not"
>
> — [47:27](https://www.youtube.com/watch?v=4sX_He5c4sI&t=2847s) &middot; *A rare quantified outcome for verification practice rather than a capability benchmark.*

> "if your agent one in four times deletes a database, you will never touch that agent again"
>
> — [57:39](https://www.youtube.com/watch?v=4sX_He5c4sI&t=3459s) &middot; *Makes the reliability-vs-capability gap visceral in one sentence.*

> "Why was coding first solved? It's because code is verifiable. You can run it, you can test it, you can check it and you can be for sure that it worked."
>
> — [59:53](https://www.youtube.com/watch?v=4sX_He5c4sI&t=3593s) &middot; *The load-bearing claim shared across the Amazon AGI, Sonar, and DeepMind talks.*

> "software engineering is not about writing code software engineering is the first time you join a company and you realize that there are 35 million lines of PHP in the codebase"
>
> — [1:22:26](https://www.youtube.com/watch?v=4sX_He5c4sI&t=4946s) &middot; *DeepMind's definition of where the frontier actually still is.*

> "I think that 80% of the new code added to GitHub today is machine generated."
>
> — [1:24:55](https://www.youtube.com/watch?v=4sX_He5c4sI&t=5095s) &middot; *A specific, checkable number underpinning the argument that code training data is exhausted.*

> "I would predict that in one year we'll let Gemini or other model generate the code and nobody will actually look at it."
>
> — [1:27:03](https://www.youtube.com/watch?v=4sX_He5c4sI&t=5223s) &middot; *A dated, falsifiable prediction that directly contradicts the verification-first talks earlier in the day.*

> "so this led to our really big revelation what if the best way to evaluate an agent was actually with an agent"
>
> — [1:40:39](https://www.youtube.com/watch?v=4sX_He5c4sI&t=6039s) &middot; *Names the agent-as-judge position that the rest of the eval track argues over.*

> "Because benchmarks measure model capability. Production measures system behavior."
>
> — [2:17:14](https://www.youtube.com/watch?v=4sX_He5c4sI&t=8234s) &middot; *The cleanest formulation of the offline-vs-production eval split.*

> "So more compute did not transfer the cheap structure did."
>
> — [2:33:48](https://www.youtube.com/watch?v=4sX_He5c4sI&t=9228s) &middot; *A negative result: test-time compute scaling for retrieval did not generalize out of domain.*

> "Search is test time compute. So don't reach for bigger model. Do more search at inference instead."
>
> — [2:40:26](https://www.youtube.com/watch?v=4sX_He5c4sI&t=9626s) &middot; *Compresses the retrieval talk's whole thesis into a prescription.*

> "Japa in just one round of reflection using just three data points is already able to get twice the performance gains that gpo got after 25,000 rollouts"
>
> — [5:40:01](https://www.youtube.com/watch?v=4sX_He5c4sI&t=20401s) &middot; *The strongest sample-efficiency claim of the day, pitting text-space optimization against RL.*

> "Token prices have continued to fall by 5 to 10x every year for each fixed level of intelligence."
>
> — [8:11:14](https://www.youtube.com/watch?v=4sX_He5c4sI&t=29474s) &middot; *Resolves the apparent contradiction between falling prices and rising bills.*

> "The vast majority of tokens to complete longrunning agentic tasks are input tokens."
>
> — [8:21:32](https://www.youtube.com/watch?v=4sX_He5c4sI&t=30092s) &middot; *Practical cost-modeling correction — most teams optimize output tokens instead.*

> "More AI agents running does not mean that there is more of you available. Your cognitive bandwidth does not parallelize."
>
> — [7:58:39](https://www.youtube.com/watch?v=4sX_He5c4sI&t=28719s) &middot; *Names 'orchestration tax' as the limit on parallel-agent workflows.*

> "So here's an operational rule. Explain it or don't ship it."
>
> — [8:02:54](https://www.youtube.com/watch?v=4sX_He5c4sI&t=28974s) &middot; *The day's most actionable governance heuristic for AI-generated code.*

## Positions

- The newest class of models performs better with a smaller system prompt and fewer examples, because examples constrain a model more imaginative than they are. ([22:09](https://www.youtube.com/watch?v=4sX_He5c4sI&t=1329s), confidence: stated)
- The good/fast/cheap tradeoff no longer forces a choice — with these models you can pick all three, and teams should stop being 'reasonable' about prioritization. ([33:22](https://www.youtube.com/watch?v=4sX_He5c4sI&t=2002s), confidence: stated)
- Coding agents reach 16–18 hour task horizons only at 50% success; at 80% accuracy the horizon drops to roughly 3.5 hours, which is not enterprise-grade. ([39:28](https://www.youtube.com/watch?v=4sX_He5c4sI&t=2368s), confidence: stated)
- Verification must be baked into the development loop (guide, verify, solve) rather than treated as after-the-fact code review, or benefits dissipate within three months. ([43:18](https://www.youtube.com/watch?v=4sX_He5c4sI&t=2598s), confidence: stated)
- Customers using zero-trust multi-layered verification report 44% fewer AI-derived production outages, and cleaner codebases cut token consumption by over 30%. ([48:19](https://www.youtube.com/watch?v=4sX_He5c4sI&t=2899s), confidence: stated)
- Coding was solved first specifically because it is verifiable; reliability for unverifiable knowledge work is still a wide-open field. ([59:53](https://www.youtube.com/watch?v=4sX_He5c4sI&t=3593s), confidence: stated)
- About 80% of new code added to GitHub is machine-generated, so human code as a training-data source is ending and self-play must take over. ([1:24:55](https://www.youtube.com/watch?v=4sX_He5c4sI&t=5095s), confidence: stated)
- Within about a year, models will generate code that nobody actually reads, analogous to compiler assembly output. ([1:27:03](https://www.youtube.com/watch?v=4sX_He5c4sI&t=5223s), confidence: stated)
- It is time to design new programming languages for models rather than humans — strongly typed, Lean-inspired, and not necessarily human-readable. ([1:32:38](https://www.youtube.com/watch?v=4sX_He5c4sI&t=5558s), confidence: stated)
- Classical LLM-as-a-judge evals with fixed rubrics cannot catch agent failure modes on varying trajectories; agent-as-a-judge is required as a third eval type alongside deterministic and LLM judges. ([1:40:39](https://www.youtube.com/watch?v=4sX_He5c4sI&t=6039s), confidence: stated)
- For a frozen small embedding model, spending more test-time compute yields in-domain gains that do not transfer to held-out tasks or unseen encoders, while cheap structural recombinations do transfer. ([2:33:48](https://www.youtube.com/watch?v=4sX_He5c4sI&t=9228s), confidence: stated)
- Auto research agents on optimizer speedruns produced no genuinely novel optimizers or mechanisms — they combined existing papers and made incremental improvements. ([3:29:19](https://www.youtube.com/watch?v=4sX_He5c4sI&t=12559s), confidence: stated)
- Reflective optimization in text space beats gradient-based RL on sample efficiency, matching or doubling GRPO's gains with three data points versus 25,000 rollouts. ([5:40:01](https://www.youtube.com/watch?v=4sX_He5c4sI&t=20401s), confidence: stated)
- Prompt optimization becomes more important as models improve, not less, because better instruction-following amplifies precise task specification. ([5:53:36](https://www.youtube.com/watch?v=4sX_He5c4sI&t=21216s), confidence: stated)
- The engineer's durable edge is answerability and evidence-backed judgment, not any single capability — speed, recall, verification, and even taste all decay as the frontier moves. ([8:02:54](https://www.youtube.com/watch?v=4sX_He5c4sI&t=28974s), confidence: stated)
- Open-weights models have trailed the overall intelligence frontier by a consistent 3–9 months across the last three years, implying a Mythos-class open model within nine months. ([8:10:36](https://www.youtube.com/watch?v=4sX_He5c4sI&t=29436s), confidence: stated)
- Token prices fall 5–10x per year at each fixed intelligence level, yet cost per task is rising because agentic tasks consume vastly more tokens. ([8:11:14](https://www.youtube.com/watch?v=4sX_He5c4sI&t=29474s), confidence: stated)
- Input tokens and cache-hit pricing, not output tokens, dominate the cost of long-running agentic tasks, so cache discount rates (80–99%) should be the first thing teams model. ([8:22:22](https://www.youtube.com/watch?v=4sX_He5c4sI&t=30142s), confidence: stated)

