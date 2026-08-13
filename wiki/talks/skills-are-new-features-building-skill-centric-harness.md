---
title: "Skills are new features: Building Skill-Centric Harness"
type: "talk"
slug: "skills-are-new-features-building-skill-centric-harness"
track: "AI in Finance"
org: "FactSet"
day: "Day 4 — Session Day 3"
room: "Track 3"
video_id: "7jjudsEhBtM"
duration_sec: 1043
word_count: 2177
speakers: ["Yogendra Miraje"]
---

# Skills are new features: Building Skill-Centric Harness

*Program title: Skills are new features: Building Skill-Centric Harness for Agentic Products*

**Speakers:** [Yogendra Miraje](../speakers/yogendra-miraje.md)

**Org:** FactSet

**Track:** AI in Finance &nbsp;|&nbsp; **Day/Room:** Day 4 — Session Day 3 &middot; Track 3 &nbsp;|&nbsp; **Duration:** 17m 23s

[Watch on YouTube](https://www.youtube.com/watch?v=7jjudsEhBtM)

## Summary

Yogendra Miraje (FactSet) argues that in agent-fronted products, skills — not screens, buttons, or forms — are where features now live, and that the engineer's job shifts correspondingly from shipping features to shipping the harness those skills run on. He walks through the minimum viable skill support in a custom harness (skill registry, system prompt injection of name/description/path for progressive disclosure, a file read tool, plus bash or a sandbox for scripts) with a worked company-research/report example. He then shares operational learnings: descriptions act as routing signals and must be phrased around user intent, skill libraries should be cut by user workflow rather than data model, and skills are contracts versioned against a specific model — a model upgrade broke his agent with zero skill changes because the new model weighted the beginning of the skill file. The last third covers scaling: system-prompt stuffing breaks past ~10 skills (use embeddings or a small shortlisting model), and hundreds of skills demand hierarchy, metadata filters, and a five-part governance model borrowed from software engineering practice. Watch it if you are adding skill support to your own harness or running a skill library beyond a handful of files; skip it if you only write skills for Claude Code.

## Key Points

- In agentic products the framing is who/what/how: prompts define who the agent is, tools define what it can connect to, and skills define how a task gets done — making skills the natural home for business logic and therefore the new unit of product feature.
- Because anyone with good product understanding can author a skill, feature shipping partly leaves engineering, and the engineer's role shifts to building the harness that runs skills well.
- A bare-minimum skill implementation in a custom harness needs only three things — a skill registry, a system prompt, and a file read tool — plus bash or a code sandbox if skills execute scripts.
- Progressive disclosure means only skill name, description, and path go into the system prompt; the agent reads the skill body on demand.
- Skill descriptions are routing signals, so they must be written in terms of the user's request (e.g. the trigger word 'PDF'), kept mutually distinct, and kept fresh — stale or overlapping descriptions are why skills fail to trigger.
- Skill libraries should be cut by user intent rather than by the underlying data model: 'earnings preparation' and 'pre-market briefing' beat 'estimate analysis' and 'analyst rating', and refactoring toward that as real use cases arrive is expected.
- Skills are contracts versioned to a model, not documentation: a model upgrade broke the speaker's agent with no skill changes because the new model attended to the start of the skill file while critical instructions sat at the end — so evals must be rerun on every model upgrade.
- Routing does not merely get tuned as the library grows, it changes mechanism: system-prompt stuffing works for a few skills, embeddings or a small shortlisting model are needed past roughly ten, and hundreds require hierarchy, metadata filters, and governance.
- Skill library governance has five aspects — admission, ownership, boundaries, lifecycle, coherence — implemented by borrowing decades-old code practices: PR-style automated gates with human in the loop, named skill owners like CODEOWNERS, semantic versioning with deprecation warnings and changelogs, periodic audits, and allow-listed access-controlled tools.

## Notable Quotes

> "Prompts define who the agent is. Tools define what it can connect to. And skills really tell you how a task gets done."
>
> — [3:05](https://www.youtube.com/watch?v=7jjudsEhBtM&t=185s) &middot; *the talk's organizing framework in one line*

> "this is the great place to keep your business logic that shapes your agents behavior. So skills are the new features."
>
> — [3:05](https://www.youtube.com/watch?v=7jjudsEhBtM&t=185s) &middot; *states the title thesis directly*

> "Then the role of engineer is shifting from shipping features to shipping harnesses."
>
> — [4:01](https://www.youtube.com/watch?v=7jjudsEhBtM&t=241s) &middot; *the practical consequence for engineering org design*

> "You only need these three things like skill registry, a system prompt, and a basic file read tool."
>
> — [5:38](https://www.youtube.com/watch?v=7jjudsEhBtM&t=338s) &middot; *concrete minimum implementation spec*

> "we are only using the name and description path in in this system prompt and not the skill body and that's what what they call about is progressive disclosure"
>
> — [7:27](https://www.youtube.com/watch?v=7jjudsEhBtM&t=447s) &middot; *defines progressive disclosure at the harness level*

> "the descriptions are really the routing signals"
>
> — [8:26](https://www.youtube.com/watch?v=7jjudsEhBtM&t=506s) &middot; *names the mechanism behind skill selection*

> "It's very important to keep your descriptions aligned to the user request and not about the skill itself."
>
> — [9:23](https://www.youtube.com/watch?v=7jjudsEhBtM&t=563s) &middot; *actionable and frequently violated authoring rule*

> "most of the skills are only model driven because for nontechnical users we're not adding that cognitive load to remember them"
>
> — [10:18](https://www.youtube.com/watch?v=7jjudsEhBtM&t=618s) &middot; *distinguishes product skills from coding-agent skills users invoke by name*

> "Another learning that had was cut by user intent and not by data model."
>
> — [10:18](https://www.youtube.com/watch?v=7jjudsEhBtM&t=618s) &middot; *the library decomposition principle*

> "instead of having an estimate analysis skill you should have earning preparation skill instead of having a skill for news and analysis analyst rating skill you should have a pre-market briefing skill"
>
> — [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s) &middot; *makes the intent-vs-data-model rule concrete with domain examples*

> "Nothing was changed. Not a single line in the skill was changed but still it failed."
>
> — [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s) &middot; *the model-upgrade failure story that motivates evals*

> "it's very important to run evals and skills without evals are really just wishful thinking"
>
> — [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s) &middot; *sharpest normative claim in the talk*

> "Skills are not the documentation and a lot of people treat them like that and skills are really the contracts versioned to a model."
>
> — [11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s) &middot; *reframes skills as versioned contracts, a contestable position*

> "When you have like more than 10 skill, maybe that's like a good point to think start thinking about, you know, how can you shortlist the skills that you're going to add to the system prompt."
>
> — [12:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=733s) &middot; *gives a specific scaling threshold*

> "The real trouble really starts when you have hundreds of skills."
>
> — [13:06](https://www.youtube.com/watch?v=7jjudsEhBtM&t=786s) &middot; *marks the second scaling regime*

> "there are like five aspect of skill library governance and these are admission, ownership, boundaries, life cycle and coherence"
>
> — [13:06](https://www.youtube.com/watch?v=7jjudsEhBtM&t=786s) &middot; *enumerates the governance framework*

> "when you hear governance, it really doesn't need to be a red tape bottleneck"
>
> — [14:01](https://www.youtube.com/watch?v=7jjudsEhBtM&t=841s) &middot; *preempts the obvious objection to enterprise governance*

> "the good news is that we can borrow a lot of good practices from code and apply them to the skills. And these coding practices like has worked for decades."
>
> — [14:01](https://www.youtube.com/watch?v=7jjudsEhBtM&t=841s) &middot; *the core analogy driving all five governance mechanisms*

> "Just like how features are maintained by application teams, we need skills to be maintained by application teams."
>
> — [14:55](https://www.youtube.com/watch?v=7jjudsEhBtM&t=895s) &middot; *ownership model — skills stay with product teams, not a central AI team*

> "routing mechanism doesn't get tuned as you scale. It changes the mechanism itself and at enterprise scale the skill library governance is really non-negotiable"
>
> — [16:00](https://www.youtube.com/watch?v=7jjudsEhBtM&t=960s) &middot; *closing takeaway with the talk's strongest scaling claim*

## Positions

- In agent-fronted products, skills replace UI surfaces (screens, buttons, dropdowns) as the unit in which features are shipped. ([3:05](https://www.youtube.com/watch?v=7jjudsEhBtM&t=185s), confidence: stated)
- The engineer's role in agentic products shifts from shipping features to shipping harnesses, because non-engineers with product knowledge can author skills. ([4:01](https://www.youtube.com/watch?v=7jjudsEhBtM&t=241s), confidence: stated)
- Adding skill support to a custom harness requires only a skill registry, a system prompt, and a file read tool (plus bash or a sandbox for script-running skills). ([5:38](https://www.youtube.com/watch?v=7jjudsEhBtM&t=338s), confidence: stated)
- Maintaining a proprietary skill-like standard is not worth it now that Anthropic has open-sourced skills; FactSet abandoned its own 'blueprints' format to adopt skills fully. ([1:27](https://www.youtube.com/watch?v=7jjudsEhBtM&t=87s), confidence: stated)
- Skill descriptions should be written to match the phrasing of user requests rather than describe the skill itself, and must be distinct from one another, or the right skill will not be triggered. ([9:23](https://www.youtube.com/watch?v=7jjudsEhBtM&t=563s), confidence: stated)
- Skill libraries should be decomposed by user intent rather than by the underlying data model, and refactoring the decomposition repeatedly as real use cases arrive is acceptable. ([10:18](https://www.youtube.com/watch?v=7jjudsEhBtM&t=618s), confidence: stated)
- In agentic products aimed at non-technical users, skill invocation should be model-driven rather than user-invoked, to avoid imposing cognitive load. ([10:18](https://www.youtube.com/watch?v=7jjudsEhBtM&t=618s), confidence: stated)
- Skills are contracts versioned against a specific model, so evals must be rerun whenever the model is upgraded. ([12:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=733s), confidence: stated)
- Instruction placement inside a skill file matters and is model-dependent: a newer model focused on the beginning of the skill and ignored critical instructions placed at the end. ([11:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=673s), confidence: stated)
- Putting all skills in the system prompt stops working past roughly ten skills, at which point embedding similarity search or a smaller shortlisting model is needed. ([12:13](https://www.youtube.com/watch?v=7jjudsEhBtM&t=733s), confidence: stated)
- At hundreds of skills, flat retrieval is insufficient and hierarchy of skills plus metadata filters and governance become necessary. ([13:06](https://www.youtube.com/watch?v=7jjudsEhBtM&t=786s), confidence: stated)
- Skill library governance is non-negotiable at enterprise scale and should reuse established software practices: PR-style admission gates with human in the loop, named skill owners, semantic versioning with deprecation warnings and changelogs, and periodic audits. ([14:01](https://www.youtube.com/watch?v=7jjudsEhBtM&t=841s), confidence: stated)
- Skills should declare allow-listed tools and those tools should be access-controlled, to enforce boundaries around what each skill can do. ([16:00](https://www.youtube.com/watch?v=7jjudsEhBtM&t=960s), confidence: stated)
- Most public discourse on skills over-indexes on coding agents, leaving skills-in-products and custom-harness integration underserved. ([2:16](https://www.youtube.com/watch?v=7jjudsEhBtM&t=136s), confidence: implied)

## Concepts

- [agent harness design](../concepts/agent-harness-design.md)
- [agent skills](../concepts/agent-skills.md)
- [agentic loop design](../concepts/agentic-loop-design.md)
- [eval-driven development](../concepts/eval-driven-development.md)
- [least-privilege agent permissions](../concepts/least-privilege-agent-permissions.md)
- [model portability](../concepts/model-portability.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [skill marketplaces](../concepts/skill-marketplaces.md)

