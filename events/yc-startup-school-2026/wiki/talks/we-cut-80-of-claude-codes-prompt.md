---
title: "We Cut 80% of Claude Code’s Prompt"
type: "talk"
slug: "we-cut-80-of-claude-codes-prompt"
org: "Anthropic"
video_id: "qyPCVqFUyDo"
duration_sec: 2151
word_count: 6868
speakers: ["Boris Cherny"]
---

# We Cut 80% of Claude Code’s Prompt

**Speakers:** [Boris Cherny](../speakers/boris-cherny.md)

**Org:** Anthropic

**Duration:** 35m 51s

[Watch on YouTube](https://www.youtube.com/watch?v=qyPCVqFUyDo)

## Summary

Boris Cherny, creator of Claude Code, is interviewed at YC Startup School 2026 the day after Opus 5 shipped, and argues that building on frontier models is an empirical science rather than a systems-design discipline. His central claim: every new model generation invalidates most of your harness, so the right move is to delete — Anthropic cut over 80% of Claude Code's system prompt for Opus 5, runs full ablations (delete everything, add lines back one at a time) on each release, and finds evals typically survive only one to three model generations before saturating. He frames the startup opportunity as 'product overhang' and 'hobbling': today's models can already do far more than shipped products elicit, and Claude Code itself was born from un-hobbling Sonnet 3.5 by giving it a terminal instead of an IDE autocomplete box. He backs this with concrete long-horizon examples — an 11-day dynamic-workflow rewrite of the Bun runtime from Zig to Rust now running in production, and a Swift port of the Claude desktop app that had been running for over two weeks at the time of the talk. Worth watching if you build agentic products or want a concrete picture of what 'give it a hard task plus a way to verify' looks like at thousands-of-agents scale.

## Key Points

- Anthropic deleted more than 80% of Claude Code's system prompt when Opus 5 shipped, because most of it existed to correct behaviors the new model now gets right on its own.
- The standard practice on each model release is an ablation: delete the entire system prompt, then add lines back one at a time to measure the impact of each, and do the same for tools and harness code.
- An undocumented CLAUDE_CODE_SIMPLE=1 environment variable strips all system prompts including tool prompts, and Cherny reports the model is slightly more intelligent without them — the prompts exist to make the product behave, not to make the model smarter.
- Evals are not durable assets either; they last roughly one to three model generations before being saturated and thrown away, so the only real constant is empirically using the product and watching where it fails.
- 'Product overhang' is the gap between what today's model can already do and what any shipped product lets it do; 'hobbling' is the product actively getting in the way — Claude Code was created by un-hobbling Sonnet 3.5 with a minimal terminal harness when competitors were shipping autocomplete.
- The dominant failure mode among experienced engineers is over-specifying step-by-step instructions; modern models want a high-level task, guardrails, and exit criteria instead.
- Verification is the single thing Cherny says people most often get wrong — give the model a way to check its own output (test suites, screenshots, pixel comparison) and it can run for days or weeks without getting stuck.
- Dynamic workflows orchestrate agents in sequence and parallel inside a Bun sandbox as a new form of test-time compute, enabling runs like the 11-day Zig-to-Rust rewrite of Bun that now ships in production Claude Code.
- Anthropic runs 20-30 daily routines that maintain its own codebases — dead-code cleanup, shipping fully-rolled-out experiments, adding and deleting tests, and an 'abstraction police' that unifies near-duplicate abstractions — amounting to hundreds or thousands of agents a day.
- Cherny qualifies 'coding is solved' to mean solved for the kind of coding he does; deep systems code, distributed systems, and pixel-level UI verification still defeat the model.

## Notable Quotes

> "it runs for a very long period of time and especially when you combine Opus 5 with auto mode, it's just like incredible. Like it can go for days, weeks, months at a time."
>
> — [1:03](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=63s) &middot; *Sets the talk's central capability claim — long-horizon autonomous runs — which every later example illustrates.*

> "And then you combine that with the auto mode classifier and with these three layers we just cannot demonstrate prompt injection anymore."
>
> — [3:06](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=186s) &middot; *A strong, checkable security claim that directly contradicts the prevailing 'lethal trifecta' consensus.*

> "So, yeah, we deleted 80% of the system prompt. You can actually try deleting the rest of it, too."
>
> — [4:25](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=265s) &middot; *The headline number and the talk's core prescription in one line.*

> "And what's interesting is that the model is actually a little bit more intelligent without these prompts. That's something that we've been finding."
>
> — [5:02](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=302s) &middot; *Counterintuitive empirical finding: system prompts are a product-behavior tool, not an intelligence multiplier.*

> "So every time there's a new model, we try we call it in a research you call this a ablation. And so what this means is you delete the entire system prompt and then you bring it back line by line to figure out what is the impact of each individual line."
>
> — [5:42](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=342s) &middot; *The concrete, reproducible method behind the 80% number.*

> "for people that aren't building agentic products, but you're using Claude code, every 6 months delete your Claude MD. Delete your skills. Delete your hooks. See what the model does and it might surprise you."
>
> — [6:49](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=409s) &middot; *Directly actionable advice for the much larger audience of Claude Code users rather than harness builders.*

> "It's um the way to think about it is almost like a like a living creature, like it's something more organic. It's a thing where every model generation, it behaves differently. It has a slightly different personality."
>
> — [8:33](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=513s) &middot; *The mental-model shift the whole talk rests on: models as organisms to study, not systems to architect.*

> "Like an eval might live for maybe one, two, three model generations, but nowadays the you know, we're on the exponential. The model is improving so quickly, very often we just saturate the eval, and then we have to throw it away, and we have to come up with a new eval."
>
> — [9:40](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=580s) &middot; *Pushes back on the common assumption that evals are the durable asset in an AI product.*

> "the model is able to do all sorts of things with today's models, not a future model, but today's model, that we have not yet realized."
>
> — [10:56](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=656s) &middot; *Defines product overhang and locates the opportunity in the present model, not the next one.*

> "often what happens is the product gets in the way. And this getting in the way, we call this hobbling. And then not not eliciting the correct behavior from the model, we call this product overhang."
>
> — [11:40](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=700s) &middot; *Gives the talk's two key terms their working definitions.*

> "I I think that nowadays, with modern models, there's so much product overhang that I have I'm not seeing startups capture."
>
> — [13:24](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=804s) &middot; *The direct challenge to the founder audience, from someone with unusual visibility into model capability.*

> "You want to go a little bit higher level. You want to describe the task, you want to describe the guardrails, you want to describe like the exit criteria, and then just go with the model cook."
>
> — [15:07](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=907s) &middot; *Compresses his entire prompting philosophy into a three-part recipe.*

> "And it ran for 11 days, and it rewrote the entire code base."
>
> — [17:14](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1034s) &middot; *The single most concrete data point in the talk — an autonomous run measured in days, now in production.*

> "you should just keep throwing the latest model at it to see if it'll just do it. Cuz even if a previous model didn't, the new one might."
>
> — [18:20](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1100s) &middot; *A cheap, repeatable strategy for discovering capability jumps without prompt archaeology.*

> "And we didn't train the model to draw. Like it it's just like the solicitation gap. Like if you ask it to do it the right way, it can just do it."
>
> — [18:53](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1133s) &middot; *Names the elicitation gap with an example nobody trained for — evidence that overhang is real and accidental to find.*

> "the skill nowadays is less about prompt engineering and more about figuring out how do you give Claude a hard task that seems a little bit too hard. And then how do you make it possible for Claude to verify its work along the way?"
>
> — [20:04](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1204s) &middot; *States what replaces prompt engineering as the core skill.*

> "I want you to rewrite the Electron app in Swift. I want you to run the Electron app in the Mac virtual machine, screenshot it, and then look pixel by pixel, compare it to the Swift version, don't stop until you're done."
>
> — [21:12](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1272s) &middot; *The verbatim prompt behind a two-week-plus autonomous run — verification loop and stop condition in three sentences.*

> "You don't need the fancy stuff. You don't need slash goal, you don't need slash loop. These help, but really all you need is give the model the task, give it a way to verify the output of its work so it doesn't get stuck, and it will just go."
>
> — [22:31](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1351s) &middot; *Explicitly deflates the scaffolding-and-tricks culture around agent products.*

> "So when I look at engineers that have been, you know, coding for a long for a long time, you know, like for for years or for decades, this is a really really common failure mode is trying to over specify and it's trying to be overly specific"
>
> — [23:44](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1424s) &middot; *Identifies experience itself as the liability — a claim experienced engineers may resist.*

> "And so now we have every day maybe 20 or 30 of these routines. It's running across all of our code bases and it's not totally there yet, but we're on the path to fully automating the maintenance of our apps by doing this."
>
> — [29:32](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1772s) &middot; *Quantifies how far Anthropic has actually pushed self-maintaining codebases internally.*

> "So coding is solved for the kind of coding that I do. It's not solved for everyone. You know, there's still code bases that are like super deep systems code bases where quad still struggles."
>
> — [30:04](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1804s) &middot; *Walks back his own widely-quoted 'coding is solved' line with a specific boundary.*

> "So forget all of the things that you learned about past models. Forget everything that you've learned about computer science theory in class. Look at the model, try to do a task, see where it struggles, and then based on that adjust."
>
> — [31:30](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1890s) &middot; *His answer to what separates the best model users — discarding priors as an active skill.*

## Positions

- Opus 5 combined with an alignment-trained model, a mechanistic-interpretability-based prompt injection classifier, and an auto mode classifier makes prompt injection undemonstrable in Anthropic's testing. ([3:06](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=186s), confidence: stated)
- Most of a system prompt exists to correct model deficiencies that disappear with the next generation, so 80%+ of Claude Code's prompt could simply be deleted for Opus 5. ([4:25](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=265s), confidence: stated)
- The model is slightly more intelligent with no system prompt at all; the prompts serve the product experience, not raw capability. ([5:02](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=302s), confidence: stated)
- Every team building on models should run a full delete-and-restore ablation of prompts and tools on each new model release. ([6:49](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=409s), confidence: stated)
- You should only add an instruction back to the system prompt after observing the model repeatedly fail at the same thing — never preemptively, because the model reads it on every single call. ([8:04](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=484s), confidence: stated)
- Evals are not long-lived assets; they typically survive only one to three model generations before saturating and being discarded. ([9:40](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=580s), confidence: stated)
- There is large, commercially valuable product overhang in today's models that startups are currently failing to capture. ([13:24](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=804s), confidence: stated)
- For modern models, highly prescriptive step-by-step instructions produce worse results than a high-level task plus guardrails plus exit criteria. ([15:07](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=907s), confidence: stated)
- A dynamic workflow rewrote the Bun JavaScript runtime from Zig to Rust in 11 days from one prompt with steering, work that would have taken engineers well over a year, and that rewrite now runs in production Claude Code. ([17:14](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1034s), confidence: stated)
- Previous model generations could not complete the Bun rewrite even with steering; the capability appeared starting with Fable. ([17:48](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1068s), confidence: stated)
- Giving the model a way to verify its own work is the single most important thing practitioners get wrong. ([20:04](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1204s), confidence: stated)
- Elaborate scaffolding (slash goal, slash loop) is optional; a hard task plus a verification mechanism is sufficient for multi-week autonomous runs. ([22:31](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1351s), confidence: stated)
- There is no 'one weird trick' for using models well, and advice from LinkedIn influencers and Twitter is not worth following. ([23:09](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1389s), confidence: stated)
- Long-tenured engineers are the group most prone to the over-specification failure mode, and unlearning it is a distinct journey. ([24:25](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1465s), confidence: stated)
- Dynamic workflows constitute a new axis of test-time compute scaling, alongside neural net size, training data, and training flops. ([27:15](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1635s), confidence: stated)
- Automated daily maintenance routines are already doing the work of dozens or hundreds of engineers across Anthropic's codebases, freeing engineers to ship product and talk to users. ([30:04](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1804s), confidence: stated)
- Coding is solved only for the kind of coding Cherny does; deep systems code, distributed systems, and pixel-level UI verification remain unsolved. ([30:49](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1849s), confidence: stated)
- Software engineering with models has shifted from a theoretical science to an empirical one, and the winning skill is willingness to abandon priors and retry ideas that failed before. ([32:14](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=1934s), confidence: stated)
- CS students should still learn to apply computer science by hand through practical problems — design sense, business sense, data science, and talking to users — rather than theory alone. ([34:06](https://www.youtube.com/watch?v=qyPCVqFUyDo&t=2046s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [capability elicitation](../concepts/capability-elicitation.md)
- [evaluation as competitive moat](../concepts/evaluation-as-competitive-moat.md)
- [iteration speed](../concepts/iteration-speed.md)
- [long-horizon agent tasks](../concepts/long-horizon-agent-tasks.md)
- [prompt injection defense](../concepts/prompt-injection-defense.md)
- [startup timing and problem selection](../concepts/startup-timing-and-problem-selection.md)
- [test-time compute scaling](../concepts/test-time-compute-scaling.md)

