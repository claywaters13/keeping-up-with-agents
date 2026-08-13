---
title: "Agents, codebases, and teams"
type: "talk"
slug: "agents-codebases-and-teams"
track: "Amazon"
org: "Amazon AGI Lab"
day: "Day 2 — Session Day 1"
room: "Expo Stage 4 SE"
video_id: "aeTb5BdmTTc"
duration_sec: 1016
word_count: 3445
speakers: ["Aditya Khandelwal"]
---

# Agents, codebases, and teams

*Program title: Agents, codebases, and teams: what it actually takes to ship together*

**Speakers:** [Aditya Khandelwal](../speakers/aditya-khandelwal.md)

**Org:** Amazon AGI Lab

**Track:** Amazon &nbsp;|&nbsp; **Day/Room:** Day 2 — Session Day 1 &middot; Expo Stage 4 SE &nbsp;|&nbsp; **Duration:** 16m 56s

[Watch on YouTube](https://www.youtube.com/watch?v=aeTb5BdmTTc)

## Summary

Aditya Khandelwal of Amazon AGI Lab argues that most advice about making codebases agent-friendly fails once you move from a solo repo to a real team, and that fixing this is a leadership problem rather than an individual contributor's side project. He frames adoption along two axes — how fearful an engineer is of being replaced and how heavily they actually use agents — and says the goal is moving everyone toward low fear and high utilization. The practical playbook he describes from leading a team of ~10: enforce progressive disclosure everywhere (thin CLAUDE.md index, 100-line cap on skill.md files, runbooks referenced from code comments), invest in one high-value skill that proves trust (theirs, 'ship it', takes code-done to PR-ready and often runs over an hour), and close the loop with CI/CD, agentic reviews, and a nightly 'code gardener'. He is candid about what broke: 400-500 issues generated in weeks, merge hell, and skeptics reverting to babysitting. The talk is worth watching for org-level adoption tactics and diagnostic signals, not for novel harness tricks.

## Key Points

- Advice tuned for individual repos breaks down the moment a whole team tries to use it on a production codebase, which is the gap this talk targets.
- Adoption should be modeled on two axes — fear of being replaced and confidence/utilization — and the org's job is to move people to low fear plus high usage.
- Making engineers work well with agents is a leadership and company responsibility, because the highest-leverage changes (code organization, shared setups) require team buy-in that no IC can unilaterally make.
- A 'figure it out yourself' paradigm creates a damaging split where high-output engineers ship 10 PRs a day and low-output engineers absorb the review burden, see bad code, and sour on agents entirely.
- Concrete failure signals include babysitting agents, blaming the model for being 'dumb' when only the harness changed, silently burning through 500k-1M context on simple tasks, and sessions needing constant intervention.
- Harness engineering principles: treat the codebase as a smart prompt-injection surface (documentation lives in comments pointing to detail files), close the loop with self-healing detection of slop, and iterate continuously rather than treating setup as a one-month project.
- Investing in one high-value skill — theirs was 'ship it', handling everything from code-done to PR-ready including CI failures — is what converts skeptics, because it demonstrates trustworthy unsupervised execution.
- Long-running agents should be reframed as a feature, not a bug: in the reasoning paradigm, longer thinking yields better output, and it frees the engineer to do other work.
- Experimental/prototype code should explicitly opt out of the codebase's rigorous standards rather than being held to them or polluting the main setup.
- Progressive disclosure is measurable: watch how much context the first prompt burns — ~20-25K is baseline, and hitting 40-50K means the index is overloaded.

## Notable Quotes

> "there's so much content about, you know, how do you set up your own code base to like work well with agents, you know, like what skills do you add? You know, this skill's better, that setup's better. But it all seems to break the moment you like actually try to use it with your team in your actual production setup."
>
> — [0:01](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=1s) &middot; *States the exact gap the talk exists to fill.*

> "companies took that and said, "Well, if one person can do so well, let's just get everyone and let's mandate it." And like token max, right? And that was clearly a a galaxy brain moment"
>
> — [1:09](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=69s) &middot; *Sardonic capsule history of enterprise mandate-driven adoption.*

> "people figured out that tokens have to be paid for. Like you just can't token max your way through life. And budgets got bolted on. And you know, essentially money is being lit on fire, and the money has to come from somewhere."
>
> — [1:47](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=107s) &middot; *Names the cost reckoning that ended the mandate phase.*

> "the first thing is if you're babysitting your agents, it's not the right setup, right? And you got to realize that. If you're seeing people in your team babysitting their agents, something's wrong."
>
> — [3:51](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=231s) &middot; *The talk's primary diagnostic signal, stated flatly.*

> "insert whatever latest model there is being really dumb today. The model didn't change, right? The hardness may have changed underneath. But if it's really like that's that's acceptable to like small changes in the hardness, clearly your own code base isn't set up well."
>
> — [4:30](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=270s) &middot; *Reassigns blame from model to harness — a checkable, contrarian diagnostic.*

> "It's silently burning context and money. Like you don't realize it, you know, you go you blow through like 500k context, you might go to like 750k million and hit auto compact even though you're not doing like a really complicated task."
>
> — [4:30](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=270s) &middot; *Puts numbers on the context-waste failure mode.*

> "It isn't really an IC's job. It's a job for leadership. It's a job for the company, right?"
>
> — [5:12](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=312s) &middot; *The central thesis in one line.*

> "Making engineers work well with their agents is truly the most impactful thing you could do as an organization."
>
> — [5:49](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=349s) &middot; *The strongest normative claim in the talk.*

> "the people who are generating like 10 PRs a day are going to like look like, you know, gods compared to people who are shipping like one to two. And the one to two PR people are actually going to get left with the review burden."
>
> — [5:49](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=349s) &middot; *Identifies a specific team-level failure mode of uneven adoption.*

> "The most impactful things that you can do to set up your code base to like make it work well require team buy-in. You can't just like if you want to change the way your code base is organized, you can't do that as an IC, right?"
>
> — [6:23](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=383s) &middot; *The structural argument for why this can't be bottom-up.*

> "If it's looking at some code and that code has, let's say some documentation, it the documentation needs to live in the comments. So, if it ever grabbed into that code, it reads the comment, goes to that file, finds all the information about it."
>
> — [7:23](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=443s) &middot; *The one concrete progressive-disclosure mechanic he gives.*

> "close the loop, right? You got to make a self-healing system cuz slop is inevitable. There is going to be some slop that's going to seep in. But, you need to have a pipeline and a way to close the loop to remove the slop, to detect it, and to be able to like self-heal the system."
>
> — [7:58](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=478s) &middot; *Accepts slop as a given and shifts the goal to detection rather than prevention.*

> "the third most important thing is treat it like a human problem, guys. Like, this isn't It's not, you know, oh, it's this tool. Like, people will figure it out. Let's just mandate our way through life. Like, that's just not going to work."
>
> — [8:30](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=510s) &middot; *Direct rejection of mandate-based adoption.*

> "Find your best ICs and find what how they are making the code base work for them. Take those practices and pass them or guide. People can't live in their own practices. And this is really hard for engineers to do it. It's basically accepting that my setup is imperfect."
>
> — [9:02](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=542s) &middot; *Names the cultural cost of standardizing on a shared harness.*

> "the moment you're done with your code, it takes care of everything from code done to PR ready for review."
>
> — [9:02](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=542s) &middot; *Defines the scope of the one skill they bet on.*

> "often the skill was running for over an hour. And that scared people, but once you actually figure out once they saw the value, they get invested"
>
> — [10:09](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=609s) &middot; *Reports a concrete runtime and the trust dynamic around it.*

> "You have to win over the skeptics. It's really easy to say like the skeptic is just someone who's scared. It's really hard to get them to buy in, but if you can get them to buy in, you know you're doing something right."
>
> — [10:46](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=646s) &middot; *Treats skeptic buy-in as the success metric for the rollout.*

> "X% of your IC time is probably going to be spent on it trading on this thing, which is not going to lead to like meaningful PRs like up front, but it's useful and it's worth it."
>
> — [11:25](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=685s) &middot; *Explicitly budgets non-shipping engineering time for harness work.*

> "when we started like we blew up to like 4 or 500 issues uh without like, you know, just I think within like a couple of weeks, which is a crazy number for like a repo."
>
> — [11:52](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=712s) &middot; *Honest failure number from the rollout.*

> "It's good if agents take too long. That means you can actually go off and do other things and you have confidence that they're doing the right thing. At the end of the day like the moment we hit this reasoning paradigm, the longer the agent like thought, the better its output."
>
> — [12:20](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=740s) &middot; *Contrarian reframe of latency as a signal of quality.*

> "instead of saying like the model is so dumb, like we have to ask how can I make it smarter"
>
> — [13:26](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=806s) &middot; *The mindset shift the talk asks for, compressed.*

> "we've kind of set a hard limit for like 100 lines in your skill.md cuz your skill is really a folder."
>
> — [14:29](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=869s) &middot; *The most directly actionable rule in the talk.*

> "You want to make sure that like it's a thin index that can point through the right files and that's what the agent gets in its like first prompt cuz that's what gets loaded when it starts to work."
>
> — [15:25](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=925s) &middot; *Defines the target shape of a CLAUDE.md/AGENTS.md.*

> "I think like 20, 25K tokens get taken anyway, but like how much more is getting added? If you're coming to like 40K, 50K, like something's wrong. That's not really progressive disclosure."
>
> — [15:57](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=957s) &middot; *Gives a numeric threshold for auditing your own context budget.*

## Positions

- Setting up codebases and teams to work well with agents is a leadership/company responsibility, not something individual contributors should be left to solve on their own. ([5:12](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=312s), confidence: stated)
- Making engineers work well with their agents is the single most impactful thing an organization can do. ([5:49](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=349s), confidence: stated)
- If a developer is babysitting their agent, the codebase/harness setup is wrong — babysitting is a defect signal, not normal practice. ([3:51](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=231s), confidence: stated)
- When a model seems 'dumber' today, the model has not changed; the harness changed, and a well-set-up codebase should be robust to small harness changes. ([4:30](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=270s), confidence: stated)
- Mandating agent usage across a company does not work, because fear and human emotion are the real blockers. ([8:30](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=510s), confidence: stated)
- Uneven agent adoption within a team is actively harmful: low-adoption engineers inherit the review burden for high-adoption engineers' PRs and become more hostile to agents as a result. ([5:49](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=349s), confidence: stated)
- Slop is inevitable, so the correct investment is detection and self-healing pipelines rather than prevention. ([7:58](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=478s), confidence: stated)
- Long agent run times are good, not bad — under the reasoning paradigm, longer thinking produces better output. ([12:20](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=740s), confidence: stated)
- skill.md files should be capped at roughly 100 lines because a skill is really a folder, with detail deferred to other files. ([14:29](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=869s), confidence: stated)
- A first prompt should consume roughly 20-25K tokens of baseline context; reaching 40-50K indicates the setup has failed at progressive disclosure. ([15:57](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=957s), confidence: stated)
- Winning over skeptics — specifically getting them to edit and modify the shared setup — is the reliable indicator that an agent rollout is succeeding. ([10:46](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=646s), confidence: stated)
- Experimental/prototype code should be explicitly exempted from the codebase's rigorous standards rather than held to them. ([12:53](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=773s), confidence: stated)
- Engineers should give up personal bespoke agent setups in favor of a standardized shared setup derived from the team's best ICs. ([9:02](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=542s), confidence: stated)
- Harness/setup work is never finished and must be treated as continuous organizational investment, consuming a standing percentage of IC time that produces no immediate PRs. ([11:25](https://www.youtube.com/watch?v=aeTb5BdmTTc&t=685s), confidence: stated)

## Concepts

- [agent configuration files](../concepts/agent-configuration-files.md)
- [agent harness design](../concepts/agent-harness-design.md)
- [agent skills](../concepts/agent-skills.md)
- [agentic coding workflows](../concepts/agentic-coding-workflows.md)
- [ai adoption and change management](../concepts/ai-adoption-and-change-management.md)
- [ai-generated code quality](../concepts/ai-generated-code-quality.md)
- [code review bottlenecks](../concepts/code-review-bottlenecks.md)
- [context window management](../concepts/context-window-management.md)
- [progressive disclosure](../concepts/progressive-disclosure.md)
- [self-improving agent loops](../concepts/self-improving-agent-loops.md)

