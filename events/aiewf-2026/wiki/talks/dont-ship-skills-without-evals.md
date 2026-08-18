---
title: "Don't Ship Skills Without Evals"
type: "talk"
slug: "dont-ship-skills-without-evals"
track: "Evals"
org: "Google DeepMind"
day: "Day 3 — Session Day 2"
room: "Track 5"
video_id: "0vphxNt4wyk"
duration_sec: 1305
word_count: 3967
speakers: ["Philipp Schmid"]
---

# Don't Ship Skills Without Evals

**Speakers:** [Philipp Schmid](../speakers/philipp-schmid.md)

**Org:** Google DeepMind

**Track:** Evals &nbsp;|&nbsp; **Day/Room:** Day 3 — Session Day 2 &middot; Track 5 &nbsp;|&nbsp; **Duration:** 21m 45s

[Watch on YouTube](https://www.youtube.com/watch?v=0vphxNt4wyk)

## Summary

Philipp Schmid of Google DeepMind argues that agent skills have become ubiquitous while evals for them are essentially nonexistent — a survey of ~50,000 indexed skills found almost none had tests, and most were AI-written and untested. He distinguishes the agents we use (where the engineer notices immediately when a skill fails to trigger) from the agents we build for customers (who don't know skills exist and will never invoke them by name), which is why model-triggered skill descriptions carry so much weight. The talk delivers concrete authoring guidance — layered progressive disclosure, directives over essays, goals over step-by-step workflows, negative cases, removing no-ops — and then shows the eval harness DeepMind used for a Gemini Interactions API skill: 117 test cases, cheap regex asserts, no LLM judge needed, taking valid code generation to nearly 90%. It closes with the practice that makes it stick: evals run on every skill diff, changes don't merge unless they improve the tests, and ablation runs with and without the skill tell you when a skill can be retired. Worth watching if you write skills for anyone other than yourself.

## Key Points

- Skills are near-universally adopted but almost never tested — Skill Bench indexed over 50,000 skills and almost none had evals, leaving authors unable to tell whether a failure came from a bad skill or a task that was too hard for the model.
- There is a critical distinction between skills in the agents you use, where you can notice a missed trigger and reprompt or use a slash command, and skills in agents you build for customers, who will never say 'use the refund skill'.
- Capability skills teach models things they can't do consistently and are inherently temporary; preference skills encode team-specific style and workflow and are durable — evals are what tell you which category a skill has fallen into.
- Skill Bench 1.1 measured roughly 15% average performance improvement from skills across ~100 coding and productivity tasks, but human-written skills outperformed AI-generated ones, which can hurt performance outright.
- The description is the token cost you pay on every single model call, so it should be short and directive — stating why, how, and when to use the skill, plus when not to — while depth belongs in layered reference files.
- If a workflow is always the same fixed sequence of steps, it should be a script the model invokes, not a skill; skills should define goals and constraints and leave the model freedom in how to reach them.
- AI-generated skills accumulate no-ops — instructions like 'write clear high-quality code' that change nothing about agent behavior — which cost tokens without buying anything.
- DeepMind's harness needs only a JSON file of test cases (prompt, language, should_trigger, expected checks) and a Python script running a coding agent; most assertions can be regex, making runs cheap enough to repeat on every model release.
- Evals should test outcomes rather than paths — whether the task got done, not whether the skill loaded on turn one — and should use isolated runs, because coding agents will cheat by pulling context from previous chats.
- Keep evals after retiring a skill: they become regression tests that tell you when model performance degrades and the skill should be reintroduced.

## Notable Quotes

> "Everyone uses skills, no one has evals."
>
> — [0:01](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1s) &middot; *the one-line diagnosis the entire talk is built to fix, delivered off a live show of hands*

> "it's very hard to know if your skill is good or bad because like agents are really non-deterministic. So you might not know if your uh task fails because your skill is bad or if your task fails because it's way too challenging for the model."
>
> — [0:45](https://www.youtube.com/watch?v=0vphxNt4wyk&t=45s) &middot; *states the core attribution problem that motivates skill-level evals*

> "When you build an agent inside your application for consumer or customers, they have no idea about what a skill is. They don't start their prompt with use customer support skill to like help me refund or use refund skill to help me solve my problem."
>
> — [1:59](https://www.youtube.com/watch?v=0vphxNt4wyk&t=119s) &middot; *the sharpest framing of why skill descriptions matter more in production than in personal use*

> "Capability skills teach models something they cannot do consistently at the moment."
>
> — [3:12](https://www.youtube.com/watch?v=0vphxNt4wyk&t=192s) &middot; *defines half of the talk's central taxonomy*

> "the better our model gets, the more likely it is that we can remove those skills. And Evals will tell us when we can retire skill and when not."
>
> — [3:12](https://www.youtube.com/watch?v=0vphxNt4wyk&t=192s) &middot; *ties skill lifecycle directly to eval infrastructure*

> "skills on average improve the performance by roughly 15%"
>
> — [4:05](https://www.youtube.com/watch?v=0vphxNt4wyk&t=245s) &middot; *the headline number establishing skills work at all*

> "human-written skills are the best we can provide. Uh AI-generated skills can uh impact performance negatively. And that skills or skills.md files should be below 500 lines of words."
>
> — [4:46](https://www.youtube.com/watch?v=0vphxNt4wyk&t=286s) &middot; *a contrarian claim plus a concrete length threshold readers can act on today*

> "the description is the cost you always pay on every model invocation. So, on every model call, the description is part of the model context. So, you always pay that 100 200 tokens cost"
>
> — [7:41](https://www.youtube.com/watch?v=0vphxNt4wyk&t=461s) &middot; *names the specific token economics behind progressive disclosure*

> "If you have those type of use cases, you should not use skills. You maybe you should write a script because if the the process or the workflow is always the same, you don't need to waste models and tokens for that exercise."
>
> — [8:49](https://www.youtube.com/watch?v=0vphxNt4wyk&t=529s) &middot; *a clear boundary on what skills are not for, where many practitioners get it wrong*

> "I like to create five for like the happy path. So, when do I want to use that skill? Five when I don't want to use that skill just to make sure the model is not over triggering the skill and confusing itself."
>
> — [10:03](https://www.youtube.com/watch?v=0vphxNt4wyk&t=603s) &middot; *the concrete recipe for a minimum viable skill eval set*

> "no-ops basically is an instruction which does nothing to change the agent's behavior. It's like before making an implementation easy to read."
>
> — [11:10](https://www.youtube.com/watch?v=0vphxNt4wyk&t=670s) &middot; *defines a specific, common failure mode in AI-authored skills*

> "we created 117 test cases"
>
> — [12:28](https://www.youtube.com/watch?v=0vphxNt4wyk&t=748s) &middot; *grounds the methodology in a real, sized production case*

> "the end result was that we improved the the performance up to like almost 90% for generating valid interactions API code with the latest Gemini models"
>
> — [12:28](https://www.youtube.com/watch?v=0vphxNt4wyk&t=748s) &middot; *the payoff number for the case study*

> "most of the tests or evals for skills can be regex. It's like very amazing how good of regex you can write using coding agents."
>
> — [14:17](https://www.youtube.com/watch?v=0vphxNt4wyk&t=857s) &middot; *argues against reaching for LLM judges by default, the cheapest practical advice in the talk*

> "if a change happens to or like a diff to the skill file, the eval will be run, and there will also be a result, and the change will not be merged if it is not improving the test cases."
>
> — [16:28](https://www.youtube.com/watch?v=0vphxNt4wyk&t=988s) &middot; *describes the enforcement mechanism that turns eval advice into an actual practice*

> "we have seen 50% of the failures uh because the skill was not triggered correctly because the prompt of the user was not uh detailed enough"
>
> — [17:04](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1024s) &middot; *quantifies triggering as the dominant failure mode*

> "we don't want to test if the model loads the skill on like the first turn. We really want to test if it can achieve the task based on the prompt."
>
> — [18:22](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1102s) &middot; *the outcomes-not-paths principle stated plainly*

> "coding agents are very good at finding or cheating. So, if you run inside uh your existing environment, it might look up previous chats or it might look up some other executions"
>
> — [18:22](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1102s) &middot; *a non-obvious eval-validity trap specific to agentic evaluation*

> "agent harnesses behave differently and of course model behaves differently. So, maybe your skill is very good with a Gemini but very bad with Codex"
>
> — [18:57](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1137s) &middot; *flags cross-harness portability as an underrated risk*

> "If your um model is good enough that it doesn't need the skill anymore, keep that eval. You don't need to throw that eval away because you throw the skill away."
>
> — [19:41](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1181s) &middot; *reframes evals as durable assets outlasting the skills they were written for*

> "run always evals with your skill loaded and without your skill loaded. Only that way you will know when you can retire skill or if a skill is really helpful for your performance."
>
> — [20:50](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1250s) &middot; *the single actionable method for deciding whether a skill earns its keep*

## Positions

- Human-written skills outperform AI-generated skills, and AI-generated skills can degrade performance. ([4:46](https://www.youtube.com/watch?v=0vphxNt4wyk&t=286s), confidence: stated)
- A skills.md file should be under 500 lines. ([4:46](https://www.youtube.com/watch?v=0vphxNt4wyk&t=286s), confidence: stated)
- Skills improve agent performance by roughly 15% on average, per Skill Bench 1.1 across ~100 tasks. ([4:05](https://www.youtube.com/watch?v=0vphxNt4wyk&t=245s), confidence: stated)
- If a workflow is a fixed sequence of steps, it should be a script rather than a skill. ([8:49](https://www.youtube.com/watch?v=0vphxNt4wyk&t=529s), confidence: stated)
- Most skill evals can be cheap regex assertions rather than LLM-as-judge. ([14:17](https://www.youtube.com/watch?v=0vphxNt4wyk&t=857s), confidence: stated)
- About 50% of skill failures come from the skill not being triggered, not from bad skill content. ([17:04](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1024s), confidence: stated)
- Evals should measure task outcomes, not whether the skill was loaded on a particular turn. ([18:22](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1102s), confidence: stated)
- Skill evals must run in isolated workspaces because coding agents will otherwise cheat by reading prior chats or executions. ([18:22](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1102s), confidence: stated)
- You should run three to six trials per eval case because agents are non-deterministic. ([18:57](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1137s), confidence: stated)
- Skills should be tested across multiple agent harnesses, since a skill that works on one harness may fail on another. ([18:57](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1137s), confidence: stated)
- A skill change should not be merged unless it improves the eval test cases. ([16:28](https://www.youtube.com/watch?v=0vphxNt4wyk&t=988s), confidence: stated)
- Evals should be retained after a skill is retired, serving as regression tests that signal when to reintroduce it. ([19:41](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1181s), confidence: stated)
- User-invoked skills are underrated and are the right fit for routine dev workflows like creating pull requests or staging documentation. ([5:32](https://www.youtube.com/watch?v=0vphxNt4wyk&t=332s), confidence: stated)
- Skill descriptions should include negative cases specifying when not to use the skill, to prevent over-triggering. ([10:03](https://www.youtube.com/watch?v=0vphxNt4wyk&t=603s), confidence: stated)
- Removing no-ops from skills saves tokens even when it does not change eval performance. ([20:50](https://www.youtube.com/watch?v=0vphxNt4wyk&t=1250s), confidence: stated)
- Capability skills are temporary and will be obsoleted by better models, while preference skills are durable. ([3:12](https://www.youtube.com/watch?v=0vphxNt4wyk&t=192s), confidence: stated)

## Concepts

- [agent skills](../concepts/agent-skills.md)
- [context window management](../concepts/context-window-management.md)
- [eval harness design](../concepts/eval-harness-design.md)
- [llm-as-a-judge](../concepts/llm-as-a-judge.md)
- [pre-training data curation](../concepts/pre-training-data-curation.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [verifier design](../concepts/verifier-design.md)

