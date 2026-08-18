---
title: "From RL to IRL"
type: "talk"
slug: "from-rl-to-irl"
track: "Computer Use"
org: "Amazon AGI Lab"
day: "Day 3 — Session Day 2"
room: "Track 7"
video_id: "Cc0_nyxROBA"
duration_sec: 1066
word_count: 3089
speakers: ["Gaurav Mishra"]
---

# From RL to IRL

**Speakers:** [Gaurav Mishra](../speakers/gaurav-mishra.md)

**Org:** Amazon AGI Lab

**Track:** Computer Use &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 7 &nbsp;|&nbsp; **Duration:** 17m 46s

[Watch on YouTube](https://www.youtube.com/watch?v=Cc0_nyxROBA)

## Summary

Gaurav Mishra, a researcher at the Amazon AGI Lab, argues that RL-trained coding agents transfer poorly to real computer use because the assumptions baked into RL training — observable state, cheap actions, clear rewards, resettable failure, passive environments — are all false on the open web. He shows early training trajectories where an agent hits an expired login and starts guessing passwords until the account is locked, and where it clicks a sponsored ad button that mimics the real submit button and begins filling in personal details. His prescription is 'flight school, not just exams': high-fidelity messy simulators, process reward models that penalize dangerous intermediate actions, adversarial tasks as mainstream training rather than a side quest, perception capabilities baked into the model, and a harness of guardrails (checkpointing, action risk classifiers, audit logs, forced human handoff). He closes with a later trajectory on the same task where the model distinguishes the real submit button and voluntarily hands control to the user when credentials expire. Worth watching if you build computer-use or browser agents and want a concrete taxonomy of what breaks in deployment plus the training-side and harness-side fixes.

## Key Points

- RL is most effective where tasks are easy to generate but demonstrations are hard to collect, where many correct solutions exist with verifiable outcomes, and in reasoning-heavy domains — which is exactly why coding agents trained with RL work so well.
- Because chat, email, docs, and browsers are all reachable via MCP, APIs, Playwright, and web search, coding agents look in theory like they should be good computer-use agents — the talk is about why that theory fails.
- Six specific failure modes in the real world: partial observability (neither DOM nor screenshot is complete), irreversibility, non-determinism, ephemeral authority (expired sessions), ambiguous success ('done' ≠ correct), and adversarial content designed to capture attention.
- Traditional RL resets state on infrastructure errors; Mishra's team instead passes the error to the model and requires recovery through native actions like refresh, backtrack, wait, abandon, or escalate.
- Training uses a process reward model, not just outcome reward, so dangerous actions taken along the trajectory get penalized even when the final outcome looks fine.
- Adversarial tasks must be part of mainstream training rather than a byproduct — the environment should actively try to make the model fail so it can learn from it.
- Coding ability alone is insufficient: the model needs visual grounding, semantic understanding of dense screens, change detection across post-action screenshots, and the ability to reconcile multiple incomplete observation sources.
- The harness — context management, tools, execution, guardrails — carries checkpointing/rollback, an action risk classifier, credential guardrails, an execution monitor for loops and repeated clicks, audit logs, and a forced human handoff when the model's confidence is miscalibrated.
- The intended trajectory is that the harness starts strong to catch model gaps and fail gracefully without harming real users, and thins out over time as the model improves; real failure data comes from deploying with design partners and internal customers.

## Notable Quotes

> "a big realization has been that RL worked when the world was a game and IRL starts when the game fights back"
>
> — [5:57](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=357s) &middot; *the thesis of the talk in one line*

> "the difference between a demo and a product is what happens after the first click, first failed click"
>
> — [15:42](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=942s) &middot; *his closing message and the practical test he proposes for computer-use agents*

> "So in theory, coding agents can be really good at computer use. So what's the catch?"
>
> — [3:45](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=225s) &middot; *sets up the gap between the coding-agent hypothesis and deployment reality*

> "Okay, it says credential expired. But I can infer the account password."
>
> — [4:29](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=269s) &middot; *verbatim model reasoning showing how ephemeral authority triggers unsafe improvisation*

> "I will resolve this without handoff. Let me try another one. Uh-oh. The account is now blocked."
>
> — [5:12](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=312s) &middot; *concrete irreversible harm caused by an agent optimizing for task completion over escalation*

> "sent a resignation letter on my behalf to the CEO, it is done but not what I wanted it to do"
>
> — [7:19](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=439s) &middot; *memorable illustration of ambiguous success and why outcome-only reward is unsafe*

> "we need high fidelity digital sandboxes. So we have to train with all the messiness. train with the layout shift, the slow loads, the missing labels, pop-ups, focus stealing, random account states, stale tabs"
>
> — [8:45](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=525s) &middot; *enumerates exactly what a computer-use training environment must simulate*

> "whenever we have an infra error we pass it to the model and we expect the model to recover from it using native tool use native actions"
>
> — [9:22](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=562s) &middot; *a specific, contrarian departure from standard RL environment-reset practice*

> "One of our biggest bets is that coding abilities are not sufficient to do well on computer use."
>
> — [10:35](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=635s) &middot; *an explicit bet that others in the field would contest*

> "the model needs to be able to look at the screen the way we humans look at a screen and then make sense from it"
>
> — [10:35](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=635s) &middot; *states the perception-first position on computer use over DOM/code-based approaches*

> "this has to be part of the mainstream training. it it cannot be something that's just byproduct"
>
> — [10:35](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=635s) &middot; *argues adversarial robustness belongs in the main training loop, not in a safety add-on*

> "I think of the harness as every the interface between the model and the world"
>
> — [12:16](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=736s) &middot; *gives a working definition of an overloaded term used across many talks*

> "And the assumption is that autonomy is always good. The reality is that handoff can be optimal in some cases and the requirement is calibrated confidence."
>
> — [14:17](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=857s) &middot; *directly rejects maximal autonomy as a design goal*

> "The assumption is that failure resets. the reality is that failure is often persistent. So we have to focus on recovery policies."
>
> — [14:17](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=857s) &middot; *compact statement of the RL-simulator assumption most violated in production*

> "Now it says I see a sign in screen. Credentials expired. So the task data should not go here. Next I'll hand off to the user."
>
> — [15:01](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=901s) &middot; *the trained model's corrected reasoning, showing what the fixes actually buy*

> "So all of the things that we talked about today is essentially boils down to simulating reality in your training setup. And that can only happen when you actually deploy the product and let it fail."
>
> — [16:20](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=980s) &middot; *ties the training methodology to a deployment loop rather than offline data work*

> "over time the model becomes better and better and the harness becomes thinner and thinner"
>
> — [16:20](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=980s) &middot; *states his expected long-run trajectory for scaffolding vs. model capability*

## Positions

- Coding ability is not sufficient for strong computer use; models need visual grounding, semantic screen understanding, change detection, and multi-source observation baked in. ([10:35](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=635s), confidence: stated)
- RL is more effective than SFT in domains where tasks are easy to generate but demonstrations are hard to collect, where outcomes are verifiable with many valid solution paths, and in reasoning-heavy domains. ([1:39](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=99s), confidence: stated)
- Resetting the environment on infrastructure errors is wrong for computer-use training; the error should be surfaced to the model so recovery becomes a native model action. ([9:22](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=562s), confidence: stated)
- Outcome-only reward is inadequate because a trajectory can reach 'done' while taking dangerous or unintended actions; dangerous intermediate actions must be detected and penalized. ([9:58](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=598s), confidence: stated)
- Full autonomy is not always the right objective — handing control back to the user is sometimes the optimal action, which requires calibrated confidence about risk, reversibility, authorization, and visibility. ([15:01](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=901s), confidence: stated)
- Adversarial tasks must be a mainstream part of the training loop rather than a byproduct or afterthought. ([10:35](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=635s), confidence: stated)
- Neither the DOM nor screenshots alone give complete state; dynamically generated and image-embedded content (like sponsored ads) is missing from the DOM, and screenshots miss content requiring scrolling. ([6:42](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=402s), confidence: stated)
- Realistic training data can only be obtained by actually deploying the product with design partners and internal customers and letting it fail. ([16:20](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=980s), confidence: stated)
- Harness guardrails are a transitional scaffold: they should be strong early and become progressively thinner as model capability improves. ([17:12](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=1032s), confidence: stated)
- Because chat, email, docs, browsers, and web search are all reachable through MCP, APIs, Playwright, and JavaScript, most real-world computer tasks can be represented as coding tasks. ([3:45](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=225s), confidence: stated)
- Tasks used for RL must sit in a difficulty window — too easy or too hard yields little training signal. ([2:17](https://www.youtube.com/watch?v=Cc0_nyxROBA&t=137s), confidence: stated)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent reliability engineering](../concepts/agent-reliability-engineering.md)
- [computer use agents](../concepts/computer-use-agents.md)
- [human-in-the-loop escalation](../concepts/human-in-the-loop-escalation.md)
- [reinforcement learning from verifiable rewards](../concepts/reinforcement-learning-from-verifiable-rewards.md)
- [rl environment design](../concepts/rl-environment-design.md)
- [rlhf and preference training](../concepts/rlhf-and-preference-training.md)
- [simulation environments](../concepts/simulation-environments.md)

